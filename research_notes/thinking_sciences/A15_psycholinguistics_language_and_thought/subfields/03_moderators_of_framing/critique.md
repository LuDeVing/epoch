# Critique: A15.03 Moderators of framing (cross-check)

## Numbers re-opened this session (10)
| # | Source | Result |
|---|--------|--------|
| 1 | Druckman 2001 (PDF text) | Confirmed: Democrats neutral 70% (N=30) vs 24% (N=34), reversal 46%, z=3.73; Exp1 N=464, Exp2 N=313. Nuance added: the drop from 46% to 21% under a Democratic endorsement was only z=1.61, p=.054 (one-tailed), so "more than half" is a point estimate with weak support. |
| 2 | Roberts et al. 2022 (PMC) | d=1.52 vs .75, F(1,44)=57.06, gain d=1.32, loss d=.003 confirmed. CORRECTION: evidence a13 says N=40 analysed; df=44 means 45 analysed in the behaviour analysis (61 completed; 40 was the power target and the eye-tracking sample). b01 had it right. |
| 3 | Gong et al. 2026 (PMC) | Interaction F(1,25)=309.50, partial eta2 .93 confirmed; df 25 implies 26 analysed. Recruited count not re-found in text. |
| 4 | Costa et al. 2014 (PLoS ONE) | Confirmed 20% to 33% utilitarian, chi2(1,N=317)=6.9, p<.01. |
| 5 | Kuhberger 2023 (PMC) | Confirmed d=.31, .52, .60, h=.612 [.568,.656], 49 countries. Note: d=.52 is a "corrected for publication bias" estimate that came out higher, which is odd. |
| 6 | Zhang 2026 FrameBench (arXiv text) | Confirmed 32.41% [30.48, 34.36], 0.63%, 98.1% of 2,153, 63.33%, 36.81%, 6.68%, 22.83%, 7.12%. |
| 7 | Suri et al. 2023 (arXiv text) | Confirmed 5 vs 4 of 7 in 11 trials each; humans 5.2 vs 4.6, t(80)=3.86. |
| 8 | Echterhoff 2024 (arXiv text) | CORRECTION: paper says GPT-4 "admits 40.5% more students in the reject framing" (a relative figure), not "40.5 points" as a25 wrote. Debias residuals (0%, 1.4%, 2.7%) confirmed, but they are the share of prompts that still carry bias elements after rewriting, not an outcome bias measure. |
| 9 | Jones and Steinhardt 2022 (arXiv text) | Confirmed 32.9% to 2.4-10.6%; verbatim copying 62.2-92.7% Codex, 58.2% (print Hello world) to 79.3% CodeGen. |
| 10 | Hwang et al. 2026 (arXiv text) | 5.69%, 5.77%, 66.29% confirmed. Cell attribution not safe: the 80.08% for LLaMA 3.1 70B comes from a garbled table row; it may be the acquiescence or truthfulness column, not jailbreak as c01 states. Treat the example cells as unverified. |

## Contradictions between sources
- Time pressure: raises framing in two small lab studies (Roberts, Gong), yet Kuhberger's review says thinking-style scales give no consistent picture, and Hinson finds only non-affective load matters. The mechanism (attention to the gamble vs. non-engagement) is not settled.
- Foreign-language effect: robust for moral dilemmas (Costa), null for risky choice and CRT (Bialek review), reversed sign in Hadza. Not a framing moderator we can rely on.
- LLM framing direction: Suri (human direction, deterministic), Kraishan (all seven reversed), Payne (scenario dependent), FrameBench (changes mostly into "uncertain", direct reversals 0.63%). Results depend on how the vignette is written and whether the answer is categorical.
- Debiasing: DeFrame and canonicalisation report large gains; CogBias and Echterhoff report small or backfiring gains from generic warnings. Not contradictory if the lever is "change the input", not "tell the model".

## Weak spots
- Druckman's two experiments are the whole evidence for the credible-advice claim; no independent replication was found. Student samples, one-tailed tests, small cells (N=14 to 55).
- Several LLM items are preprints with 2026 dates and author-built tasks (CogBias, Kraishan with only 5 items per bias, FrameBench with its own templates).
- Human time-pressure studies have 26 to 45 analysed participants.
- Many LLM papers test only bias families nearby (omission, anchoring, sycophancy), not gain-loss framing.

## Only seen in snippets or abstracts
Keysar 2012 (a18, b05), Hayakawa 2019 (b06), Strough 2011 (b19), Peters 2009 (b20), Druckman abstract page (b17), Macmillan-Scott, Nguyen, Liu 2026 ethics (c21-c23), Lampinen 2024 (abstract), Hagendorff 2023. Tennis-player study (a16) and cross-linguistic LLM bias study (b22) read mostly at abstract level.

## GAPS (most decision-relevant first)
1. At equal tokens, does a deterministic input rewrite (canonicalised numbers, neutral wording) beat a warning prompt and a reframe-and-compare step on our agent's tasks, and what does the setup cost?
2. Does the FrameBench result (36.81% to 6.68%) hold on non-medical, non-probability tasks such as ARC and BrainTeaser wording, and does it survive a larger model?
3. Is there any independent replication of Druckman 2001 (credible advice removing framing), and does an LLM treat a "credible source" label the way humans do, or just defer (sycophancy)?
4. Does a checkable signal (tool output, computed expected value) beat a source label as a frame-remover for LLMs? Does it help strong models or harm them (Kawada and Kellis)?
5. What is the actual mechanism of the human time-pressure effect (attention vs. non-engagement), and does its LLM analogue (token cap) show any frame gap change in a matched budget test?
6. Which LLM framing results use real two-option gain-loss pairs with stakes, and how large is the gap there against the noise floor of repeated runs (7.12% in FrameBench)?
7. Does prompt language (second language) change LLM framing, given the cross-linguistic bias study and the mixed human foreign-language effect?
8. How much of the "framing" in LLM results is order or position bias (first-option selection 77-79% in CogBias) rather than frame?
9. Do expert personas or domain context reduce LLM framing the way expertise reduces it in tennis players, or does G4 apply (persona is not independent evidence)?
10. How large is the reverse (against-human) framing effect across reasoning models released after 2025, and is it a product of alignment training?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d32; d23-d32 are new this pass, d01-d22 kept). Claims K02, K08-K13, K15, K16 updated; K19-K23 added.

| Gap | Outcome | What was found |
|-----|---------|----------------|
| 1 Rewrite vs warning vs reframe at equal tokens | OPEN | FrameBench (d28): canonicalisation 6.68% vs frame-robust instruction 22.83% vs conversational 34.20%, but no token cost and no reframe-and-compare arm. Echterhoff self-help rewriting (d11) closed the GPT-4 gap (-0.405 to -0.010) in admissions only. Needs our own test (K23). |
| 2 FrameBench beyond medical, larger model | PARTLY CLOSED | The held-out set is 8 scenarios in each of healthcare, finance, education/career, legal; models include GPT-5, Gemini 2.5 Pro, Claude Sonnet 4.6 (22.81% to 63.33% baseline change). Still probability wording only. ARC and BrainTeaser wording untested. Note the 36.81% to 6.68% is the 3-model, 32-scenario test, not all 240. |
| 3 Independent replication of Druckman; LLM and credible source | PARTLY CLOSED | No direct human replication found (d31); nearest is the 2023 trust-in-source study (d18), partial. LLMs: a human-expert label has large effect (beta=1.00; 14.45x switch odds) even when the prior is random (d23). It is deference, not evidence use. |
| 4 Checkable signal vs label; harm to strong models | CLOSED for the direction | Kawada and Kellis (d26) and Zhao et al. (d30), independent: evidence helps weak states and harms strong ones; 93-100% integration of candidates already judged invalid. K16 now established. A computed expected value was not tested directly. |
| 5 Mechanism of time pressure; token-cap analogue | OPEN | Hinson (d20) supports non-engagement for humans. LLM side: shortened reasoning raises inconsistency (d29, indirect), visible thinking cut a wording gap (d13), no matched-budget frame-gap test found. K12 moved to contested. |
| 6 Real two-option gain-loss pairs, noise floor | PARTLY CLOSED | Ge et al. (d25) use two-option lotteries (reasoning models insensitive); FrameBench (d28) gives noise floor 7.12% and risk shift by probability (.535 at 20% to .109 at 80%). No LLM study found with real stakes. |
| 7 Prompt language | OPEN | Only multilingual item at floor (d08), and BiasLab (d09) gives no per-language gap. Human foreign-language effect mixed (d01, d05-d07). |
| 8 Order vs frame | CLOSED | CogBias (d24): the 77-79% first-option rate is a separate opinion-question family; order bias is a separate measure. It cannot be read as frame. Randomise order in tests. |
| 9 Persona and expertise | PARTLY CLOSED | One-sentence persona flipped framing sign (d27: +.62 to -.32 canonical); Wharton snippet (d32, unopened) says expert personas do not lift accuracy. No direct expert-vs-novice test. G4 applies. |
| 10 Reverse effect in newer reasoning models | PARTLY CLOSED | Reasoning-class models are near frame-insensitive on lotteries (d25); reverse sign seen in a persona (d27) and career scenarios (Payne, d14). Whether alignment training causes it is not tested; authors point to maths-reasoning training. |

New caveat from d27: framing measured on a named paradigm can be inflated; the blind gap was about zero in one model.

Corrections to the cross-check: the "40.5% more" for GPT-4 (Echterhoff) is 40.5 percentage points (0.780 minus 0.375, Table 3), so a25 was right and the cross-check's "relative figure" reading is withdrawn (d10). The FrameBench appendix per-model table is garbled; use the main-text numbers (d28).
