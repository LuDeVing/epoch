# Critique of evidence a, b, c (syllogistic and conditional reasoning)

Cross-checker pass, 2026-10-21. Method: re-opened open-access PDFs for the ten most decision-relevant numbers (ACL Anthology EMNLP 2024 Bertolazzi et al.; arXiv 2311.00445 Eisape et al.; arXiv 2305.12295 Logic-LM; Frontiers 2014 Singmann et al.; J-STAGE 2004 Girotto and Johnson-Laird; UCL repository Skovgaard-Olsen et al. 2016; Springer De Neys et al. 2003). Text was extracted with pdftotext. Khemlani and Johnson-Laird 2012 is paywalled; two author-site URLs returned HTML 404 pages and Europe PMC marks it not open access. Its numbers could not be re-opened by me.

## Numbers checked

| # | Number | Source reopened | Result |
|---|---|---|---|
| 1 | LLaMA-3 70B instruct: 58.89% valid, 32.50% invalid (a26) | Bertolazzi Table 1 | CORRECTED. 58.89% valid (30.63 overall, 10.28 invalid) is the 70B BASE model. 70B instruct is 41.25 overall, 32.50 invalid, 54.44 valid. c04 had it right; a26 mixed the rows. Fixed in claims A01.08-K08. |
| 2 | Atmosphere predicts 92.31 / 82.97 / 62.79 (a26, b21, c06) | Bertolazzi Table 4 | Confirmed. Human atmosphere fit 62.50 valid, 0 invalid also confirmed. Model is LLaMA-3 8B ZS-CoT. |
| 3 | Contradiction rates 1.09, 0.31, 18.91, 73.91, 70.47; completeness 43.14 vs 96.93/72.93/76.24 (a27, b22, c05) | Bertolazzi Tables 4, 5 | Confirmed. Completeness claim is for LLaMA. |
| 4 | Human 44.63% valid, 40.97% invalid | Bertolazzi (citing KJL 2012) | Confirmed as quoted; originates in KJL, not re-derived. |
| 5 | Eisape: best LM about 75%, human about 50%, nothing-follows near 0%, 1296 grid / 923 finished, PC1 77% (b24-b26, c01, c03) | Eisape text | Confirmed. |
| 6 | Logic-LM GPT-4 table and 39.2 / 18.4 average gains (b28, c18) | Logic-LM Table 2 and text | Confirmed. The 39.2 and 18.4 are averages with GPT-3.5, not GPT-4. PrOntoQA is the exception (83.20 vs CoT 98.79). |
| 7 | Singmann 2014: r = .84 vs .61; b = .78, F(1, 88.14) = 86.81 (b13) | Frontiers text | Confirmed. |
| 8 | Girotto and Johnson-Laird: 68% vs 17%, z = 11.8; Oberauer and Wilhelm 52% / 23% (a18, a19) | J-STAGE text | Confirmed. |
| 9 | Skovgaard-Olsen: slopes .78 / .61 / .43, t = 3.26, 6.22, 577 vs 348 (b18) | UCL PDF | Confirmed. |
| 10 | De Neys 2003: F(1,87) = 20.84 "AC/DA fall with alternatives" (b11) | Springer PDF | CORRECTED. The linear trend F(1,87) = 20.84 is for AC only. For DA there was no clear effect of additional alternatives (Rao R(3,85) = 1.86, p < .15). The MP F(1,85) = 20.46 and MT F(1,85) = 16.02 are confirmed. Disabler presentation raising AC (Rao R(4,82) = 4.67, p < .002) is confirmed. A01.08-K12 states the corrected version. |

Not re-opened (still single trust in earlier agents): KJL 2012 hits / correct rejections (95/74, 44/93, 63/90), Kendall W .86 / .64, 12 theories, 6 data sets; Byrne 1989 table (96/96/38, 71/13, 33) which the evidence draws from secondary tables (Dietz and Holldobler slides; a cognitive-argumentation paper); Oaksford, Chater and Larkin 2000 F-values; Evans et al. 2007 table; Eisape accuracy figure values; Holliday et al.; Poddar et al.

## Contradictions and inconsistencies between sources

1. a26 vs c04 on LLaMA-3 70B (see check 1). Resolved with the paper.
2. a22 says the 55% valid-conclusion sample is "a selective US university"; b05 says "Columbia students". Probably the same, not verified.
3. Human syllogism accuracy: KJL gives 44.63% valid / 40.97% invalid (via Bertolazzi) and Eisape says "about 50%" overall. Both fit if invalid items count "nothing follows" correctly, but the two papers use different scoring (free production vs. choice among nine), so LLM-vs-human comparisons across the two papers are not like for like.
4. Eisape: model accuracy near 0% on nothing-follows items; Bertolazzi: up to 32.5% (70B instruct). Difference is plausibly prompt (generative vs. extra options) and model, not a conflict. Eisape also reports that a binary yes/no method scores much higher on those items, so the "aversion" is partly an elicitation effect (c03).
5. Suppression size differs by lab: Byrne MP 38% vs Dieussaert 60% for the additional-requirement group, and the "certain conclusion" share 33% vs 44% (b09, b10). Direction replicates, size does not.
6. Probability of conditionals: Girotto and Johnson-Laird (a18) found people often do not equate P(if A then C) with P(C|A); Singmann (b13) found r = .84 and a clean slope of .78. Oberauer and Wilhelm (a19) found only a minority (52% / 23%) giving equal values. The new-paradigm claim is a distribution of reader types (b15), not a universal. Treat as contested (A01.08-K14).
7. Verschueren and Schaeken's "Denial inferences: Oaksford, Chater and Larkin (2000) on shaky ground" (seen as an abstract record only, not read in full) argues that estimating probabilities of negated propositions for DA and MT is problematic. This is a direct challenge to a10 to a12 and a29, and was not carried into the evidence files. It supports A01.08-K17 as contested.

## Weak spots

- The LLM syllogism literature is dominated by small open models (LLaMA-3 8B, Pythia) and by the PaLM 2 family. There is almost nothing on current frontier reasoning models with long chains of thought, except Zang et al. 2026 and Poddar et al. 2025 (14 models, 160 items). Findings such as "LLMs never say nothing follows" may already be out of date for reasoning-tuned models.
- Atmosphere fits are for one model (LLaMA-3 8B ZS-CoT). Do not generalize.
- c22, c25, c26 and several 2026 papers (c10, c20, c21, c24) are single-paper results, with the risk that they are un-peer-reviewed arXiv preprints.
- Most human conditional work uses small, WEIRD, student samples (N=20 to 120).
- Several schema_part entries are proposals, not tested effects.

## Seen only in snippets or secondary tables

- KJL 2012: all numbers (agents opened it; I could not).
- Byrne 1989: secondary tables only; the 1989 paper itself was not opened.
- Verschueren and Schaeken 2001-ish: abstract only (via OpenAlex).
- c14, c22, c23, c24 and c25 numbers: not re-opened.
- c27: a search-gap claim, opened:false; the gap was not re-searched by me beyond a single OpenAlex query that also returned no LLM suppression study.

## GAPS

1. Do current reasoning-tuned frontier models (long chain of thought) still avoid "nothing follows", and what do they score on the 37 invalid-conclusion syllogisms and on the atmosphere-fit measure?
2. Does an explicit counter-model search step (list a model that satisfies the premises but falsifies the candidate) raise recall on the 37 nothing-follows items at equal tokens, without cutting accuracy on the 27 valid items?
3. How do LLMs behave on Byrne (1989) suppression (additional vs. alternative premises) and does a "list possible defeaters first" step change MP/AC/DA/MT acceptance? No study found.
4. Is the LLM P(if A then C) closer to P(C|A) or to the conjunction or material conditional, and is it relevance-sensitive in the way people are (slopes .78 / .61 / .43)?
5. Why is modus tollens so hard for LLMs (MT .31 vs MP .59): negation handling, contrapositive, or modal scope? Would a contrapositive-rewrite step fix it at equal tokens?
6. What do the original KJL 2012 tables say for hits / correct rejections and for the effect sizes of figure and 'some' quantifier cases (needs the paper or author copy)?
7. Does a formal solver step (FOL parse plus prover) help on syllogisms and conditional inference specifically, once translation errors are counted, and does it beat a 5-sample vote with solver tiebreak (A01.08-K10) at equal tokens?
8. Which existential-import reading do the target benchmarks assume, and does stating the reading in the problem restatement (S0) remove the drift reported by Zang et al. 2026?
9. Are content effects removable by a prompt-only abstraction step (replace terms by letters, then reason) in modern models, since prompting plain CoT does not remove them?
10. Do individual-difference results (conditional-probability vs. conjunctive responders; strategy variability) have an agent analogue, i.e. does response style vary across samples of the same prompt, and can a vote across styles help?

## Gap search results

Gap searcher pass, 2026-10-21. New evidence is in evidence_d.jsonl (d01 to d24, all opened). Claims A01.08-K01 to A01.08-K26 were updated and A01.08-K27 to A01.08-K36 added. WebSearch ran out of budget partway, so later gaps were searched through arXiv listings only. No frontier-model experiments were run here; everything below is read from papers.

**Correction to the critique itself.** Gap 3 said no LLM suppression study was found. That was wrong: Belief-R (Wilie et al. 2024, arXiv 2406.19764) is a Byrne-style requirement-versus-alternative test on 30 LMs (A01.08-K26 now refuted as worded; see A01.08-K27). The earlier searches missed it because it calls itself "belief revision".

| Gap | Status | What was found |
|---|---|---|
| 1. Reasoning-tuned models and "nothing follows" | Partly closed | Binary tasks: o3 and GPT-5 reject invalid and import-dependent conclusions at about 99.6 to 100% (Zang, d12); belief bias near zero for Gemini 2.5, GLM-4.6 (d20); countermodel construction 89% (Qwen3-32B) and 99% (o3) (d18). Non-reasoning: Claude 3.5 Sonnet 63.2% and GPT-4o-mini 25.3% on "neutral" (d21). Still open: free production of "nothing follows" on the 37 items and the atmosphere-fit score for a reasoning model. No such paper found. |
| 2. Counter-model search step at equal tokens | Open | LogicSkills (d18) shows the skill separates instruction-tuned (0 to 42%) from reasoning-tuned (89 to 99%) models, but the models were told the argument was invalid, and no scaffold step was tested. Fine-tuning on countermodels did not transfer to validity. |
| 3. Suppression in LLMs, defeater-listing step | Partly closed | Belief-R (d01 to d03): LLMs almost never retract (update accuracy about 10 to 22% for named API and Llama-3 models) and keep when they should (35 to 92%); CoT and plan-and-solve add about 1 BREU point; MT bases harder. RULEBREAKERS (d04): the opposite failure, rigid rule use against world knowledge. Open: reasoning-tuned models on these sets, MP/AC/DA/MT rates, and a defeater-listing step. |
| 4. LLM P(if A then C) vs P(C given A), conjunction, material | Partly closed | Orth et al. 2026 (d05, d06): slopes on P(B given A) 0.21 to 0.65 (vanilla, four small models), relevance effects weaker than people and reversed in shape for larger or prompted variants. Conjunction and material readings not tested; stimulus probabilities came from human norming. |
| 5. Why MT is hard; contrapositive rewrite | Open | Evidence is mixed (d03, d04, d23): negation in context, backward direction and yes-bias all appear (GPT-4 PL(MT) about 59%; FOL MT "yes" high but "no" low). No contrapositive-rewrite test found. |
| 6. Original KJL 2012 tables | Closed for the reported numbers | Author copy found at mentalmodels.princeton.edu (d08 to d11). Verified: hits and correct rejections (95/74, 44/93, 63/90; correct predictions 84 for verbal models), W = .86 and .64, N = 156 over six data sets. New: entropy W = .45, r = -0.52 with accuracy; correct "nothing follows" by figure 50/57/70/86%; I recomputed 44.63% valid and 41.05% invalid from the per-item table. Not available: separate effect sizes for "some" quantifier cases (only per-item percentages). |
| 7. Formal solver vs 5-sample vote, equal tokens | Partly closed, equal-token part open | Ten SemEval systems at 100% (d14); a 4B model with a structured LaTeX parse and Prover9 gets 95.8% while direct-syntax parsing drops to 86.0% and LLM-as-prover to 79.2% (d15); GPT-5 with rules in the prompt 89.9%, with a checker 96.6% (d16). FregeLogic cost is about 4,300 tokens and six calls per item (d24). All templated data; no matched-token comparison. This weakens A01.08-K10 (now contested): solver-only fails when the parse is poor, not by nature. |
| 8. Existential-import reading in benchmarks; S0 restatement | Mostly closed | SemEval Task 11 states the traditional reading (24 forms), confirmed by organizers (d14, d15). o3 and GPT-5 answer with the modern reading (15 forms). A prior-check prompt about empty terms raised modern-reading accuracy by about 3 to 11 points for most Qwen3 models (d13). Open: a prompt that pins the traditional reading was not tested; Zang et al. 2026 does not report one. |
| 9. Prompt-only abstraction | Open, narrowed | No paper replaces terms by letters and lets the same model reason in prose. Nearest: rules-in-prompt (d16) CE 19.14 to 4.95; explicit CoT or strict-logic frame recovers 87% and 76% of GPT-4o failures (d19); translate-to-logic +5.6 points for GPT-4, a loss for GPT-3.5 (d22); masked parsing before a verifier (d17). Plain CoT is mixed (d24: CE up for GPT-OSS-20B). A01.08-K22 now contested. |
| 10. Response-style variability and style vote | Open | Only numeric reproducibility is reported (ICC .77 to .98 over five samples, d07). No classification of samples as conditional-probability or conjunctive responders; no style vote. |

**Still unreliable after this pass.** Table 2 of Orth et al. and Table A1 of Belief-R are partly scrambled in the PDF text; I used only the readable rows and flagged the rest. Zang et al. Tables 4 and 5 were assigned by caption position (d13). The SemEval results are on templated, shared-task data with its own metric, and several are un-peer-reviewed system papers. Frontier reasoning-model results come from binary tasks only.

**Suggested first tests for the agent (cheap, discriminating).**
1. 64-mood production task with a reasoning model and a non-reasoning model, scoring the 37 invalid items, atmosphere fit and per-figure recall (closes gaps 1 and 2 together).
2. Belief-R and RULEBREAKERS item subsets with a requirement-versus-alternative classification step versus plain CoT at equal tokens (gap 3).
3. A paired P(C given A) versus P(if A then C) probe on irrelevant-antecedent items, five samples each, with style classification (gaps 4 and 10).
4. S0 existence line (traditional versus modern) on the nine import-dependent moods (gap 8).
