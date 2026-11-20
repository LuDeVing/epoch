# E02.03 Structured analytic techniques: critique (cross-check)

## Corrections made (sources re-opened from arXiv PDF text, this session)
Checked: Du et al. (arithmetic 67.0/72.1/69.0/81.8, GSM8K 85.0, chess 122.9), Huang et al. (self-correct tables 2, 3, 7), Liang et al. (26.0/29.5/37.0, diversity 24.8/49.7), Smit et al. (Medprompt 0.650), Khan et al. (76/48, 88/60), Zhang et al. (15% of 36 configs; Heter-SoM +6.4%, +5.8%, +8.2%), Si et al., Sharma et al.
1. Huang table is in "# calls": round 1 = 3 calls, round 2 = 5 calls. GPT-3.5 CommonSenseQA 75.8 -> 38.1 after round 1, 41.8 after round 2 (c01, b21 right). a23 only quotes round 2 for some cells; consistent, but a23 omits the 38.1 low point.
2. Huang Table 7 column order is garbled in text extraction. Reading: SC 3 = 82.5, debate (6 responses) 83.2, SC 6 = 85.3, debate (9) 83.0, SC 9 = 88.2. a24 is right. Note a24 labels debate "round 1/round 2" by response count; the table labels are shifted.
3. Si et al. novelty: a29 gives 4.86/5.62/5.78 (idea-level means, N=49, AI p=0.03); b23 gives 4.84/5.64/5.81 (review-level, N=109). Both appear in the paper; they are two units of analysis, not a contradiction. Cite one unit only.
4. Otzipka (a15, b07): a15 says "no significant difference in credibility ratings", b07 gives F(1,153)=1.79, p=.183. Compatible. The only significant effect was retaining party (p=.047), not ACH.
5. Dhami 2024 (a11, b01): the two are the same table read two ways (60.8% balanced vs 39.2% chose confirming-consistent in HypRow). a12 vs b03 agree (66.1% balanced). a11 balanced numbers for HypCol (38.2%) and HypText (32.7%) match b01 complements within rounding. Not re-opened this session (source not re-fetched); marked as carried over.
6. a30 ChatEval column order was "read from extracted table" and not verified; treat the single vs multi labels as unconfirmed.

## Contradictions between sources
- Debate helps (Du, Liang) vs debate no better than self-consistency at equal calls (Huang sec 4, Smit, Zhang). Resolution: gains are real versus a single sample, and vanish versus an equal-compute ensemble. Claims K02 and K03 stay both established.
- Disagreement intensity: Liang says more disagreement helps on counter-intuitive tasks; Smit finds it helps there but hurts or is neutral on MedQA and PubMedQA.
- Zhang: heterogeneous models help; same-model debate does not. Single source.

## Weak spots
- No direct human or LLM test of key-assumptions check, premortem, or devil's advocacy as the SAT literature defines them. Human ACH evidence is three small null results; strength of "ACH does not help" is limited by training time, task artificiality, and student samples.
- Most LLM debate work uses GPT-3.5 or older models on arithmetic/QA, not analytic tasks, and is 2023-2024. Modern models may behave differently.
- Many claims are single-source (K05, K07, K10-K12, K15, K16, K18-K20).
- Nemeth 2001 (devil's advocate vs authentic dissent) is not opened (a09); Lehner 2008 not opened (a10); Folker and Mitre only via RAND.

## Seen only in snippets or abstracts
a09, a10, a16 (Wilcox and Mandel 2024 meta-review, abstract), a17, a18 (abstract), a19 (via Dhami summary), a31, c05 (numbers not recorded), c08 (abstract), c19, c20, c21, b26 (no numbers). b25 and c18 are design or small-case.

## GAPS
1. Does an explicit competing-hypotheses step (ACH-style rival set) improve accuracy of an LLM at equal tokens versus plain CoT and versus self-consistency on diagnostic or forecasting tasks? No direct study found.
2. Does a key-assumptions check or premortem step reduce errors in LLM agents, and how often does it induce wrong flips (sycophancy to its own critic)?
3. What did Wilcox and Mandel (2024) pool across the 6 ACH experiments: effect sizes, direction on accuracy, bias, and coherence?
4. Nemeth, Brown and Rogers 2001: what exactly were the means for devil's advocate vs authentic dissent, and do LLM "authentic dissent" prompts (rival with own conclusion) beat assigned devil's advocate?
5. Can LLM rival hypotheses be made diverse enough (embedding distance, dedup yield per token) given the 71-82% cross-model similarity; does a mixed-model set help?
6. Do the 2025-2026 stronger or reasoning models still lose accuracy under self-challenge (Huang, Sharma replications on o-series, Claude 4+)?
7. What do the Lehner et al. 2008 and Folker 2000 experiments actually show on confirmation bias reduction with structured methods?
8. Do human analyst SAT benefits show up in calibration (Brier) rather than accuracy, e.g. Mandel et al. 2018 and Tetlock-style forecasting with structured prompts?
9. Does standardised probability range wording (best predictor of norm adherence in the 138-report study) improve LLM calibration at no token cost?

## Gap search results
Tools: arXiv API, OpenAlex, Semantic Scholar and WebSearch were rate limited or exhausted; evidence came from direct PDF and page fetches (Wilcox and Mandel full PDF, Mandel et al. 2018 full PDF, Wynn 2025, Tsui 2025, Kumar 2024, Li 2025, Dhuliawala 2023). Evidence is in evidence_d.jsonl (d01-d16).

- Gap 1 (ACH-style rival set vs CoT vs self-consistency at equal tokens): STAYS OPEN. No direct study found; weaker negative because search was cut. Closest: CoVe (d11). Self-consistency numbers not extracted (d12 opened:false).
- Gap 2 (assumption check, premortem, wrong flips): PARTLY CLOSED. No premortem study found. Wrong-flip rates measured: SCoRe base 15.8% correct-to-incorrect vs 4.6% fixed on MATH (d08); debate flips exceed fixes (d06); factored checks help (d11); blind spot 64.5% and fixed by 'Wait' (d07).
- Gap 3 (Wilcox and Mandel pooled): CLOSED. No pooled effect size; it is a verbal tally of 6 experiments (d01, d03). K12 now established.
- Gap 4 (Nemeth 2001 means; LLM authentic dissent): STAYS OPEN. Only the abstract read (Wiley 403). Direction known, means not. No LLM test found (d15).
- Gap 5 (rival diversity, mixed-model sets): PARTLY CLOSED. Self-MoA says mixing lowers quality and the best single model resampled wins (d10); K05 now contested. Embedding-distance dedup yield for rival hypotheses not found.
- Gap 6 (stronger and reasoning models): PARTLY CLOSED. Reasoning models show little blind spot; Claude Sonnet 4 non-reasoning 41.4% (d07). No direct replication of Huang's tables on o-series or Claude 4+.
- Gap 7 (Lehner 2008, Folker 2000): PARTLY CLOSED. Lehner via the review table: confirmation bias reduced in non-analysts, not shown in analysts, about 12 analysts (d03). Folker 2000 still only via RAND.
- Gap 8 (calibration vs accuracy for human SATs): PARTLY CLOSED. Mandel 2018 measured MAE, not Brier: ACH no gain, coherentizing -35%, aggregation -61% total (d04). No Brier-based SAT study found.
- Gap 9 (standard probability wording and LLM calibration): STAYS OPEN. Only word-interpretation studies (d13, d14); no test of a range table improving calibration.
