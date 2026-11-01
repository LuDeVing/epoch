# Cross-check critique, A03.02 Fast and frugal heuristics, ecological rationality

## 1. Corrections made (sources re-opened this session)
Re-opened and compared with the evidence lines (all confirmed unless noted):
1. Gigerenzer & Goldstein 1996 Table 2 (.658 TTB, .657 regression, .656 tallying, .623 weighted linear, .621 unit-weight, .647 Minimalist, .645 Take The Last; lookups 5.91/5.64/5.29): confirmed.
2. G&G 1996 city set: the paper text says 83 cities (recognition levels 0 to 83, so 84), not 81. a02 already notes this; 81 is the later-paper number. Cite 83 for the 1996 paper.
3. Gigerenzer & Brighton 2009 Fig. 1: 2.4 vs 7.7 cues confirmed. CORRECTION to a08/b12: the "95% CI plus or minus .4 points" is per study and per strategy, not a CI on the 20-study mean. The headline accuracies (Czerlinski et al. 1999) are only in a figure and are not in the text we read, so no exact percentages are claimed.
4. Phillips et al. 2017: mean cues 1.85 (fan) vs 4.85 (zig-zag), SVM .86, others .83: confirmed. Heart-disease tree 1.74 cues, weighted accuracy .88: confirmed (a26 said "about 1.7").
5. Hilbig & Richter 2011: r = .80 (SE .01) and 20 of 28 (71%) confirmed. The adherence M = .91 was NOT found in the text on re-check; treat .91 as unverified.
6. Bogdan 2026 (arXiv 2606.15877): 7,875 responses, 17.3 points [7.7, 25.5], Qwen2.5 32B -2.92 [-4.05,-1.81], Claude Sonnet 4.5 -0.80 [-2.08,+0.48] with 0.884, phi3.5 +0.98: confirmed. The paper itself says the 0.913 and 0.884 for the frontier models "suggests rather than establishes".
7. Sprague et al. 2025 (14.2, 12.3, 6.9; "as much as 95%" on MMLU equals-sign questions): confirmed. Wording is "as much as", not a flat 95%.
8. AdaptThink (50.9/63.5/44.7 length cut; +4.1/+1.4/+1.6 accuracy; 53% overall): confirmed.
9. Liu et al. 2025 (87.5 to 64.4, -23.1; 94.0 vs 57.7; +331% rounds, 2.9 vs 12.5): confirmed.
10. Hagendorff et al. 2023 (humans 38%, original 41% n=3,428, ChatGPT-3.5 59%, GPT-4 96%): confirmed.
11. Alaswad et al. 2026 (90.2, 88.5, 80.3, 70.5) and the VLM tree-walk paper (33.19 to 6.33; 12.6 points): confirmed.
No number was found wrong. Two wording fixes (items 3 and 5).

## 2. Duplicates that are NOT independent
The three evidence files repeat several sources. Counted once in claims: Bogdan 2026 (a31, b24, b25, c01, c02), Jagadish 2026 ERMI (a30, b23, c23), Phillips 2017 (a24, a25, a26, b17), Schulz 2016 (a28, b22, c22), Peltola 2019 (a29, b21, c21), Bobadilla-Suarez & Love (a27, b18), G&G 1996 (a03, b30). Pachur et al. 2011 and Gigerenzer & Goldstein 2011 are chapters from the same camp reporting overlapping studies, so the two reviews are not fully independent.

## 3. Contradictions between sources
- Recognition heuristic: group data (high adherence, 98% to 82% with a negative cue) look like pure use; Hilbig & Richter's model says 80% true use and most individuals differ from pure use. Gigerenzer & Goldstein 2011 say group means hide strict users. Both sides are partisan; no neutral adjudication in the evidence.
- Less-is-more for recognition: analytic and simulated (77% peak), informal confirmations (Goldstein 1997, BBC radio), mixed in tests (Pachur 2010 reviewed 10 sets). Treated as contested.
- Fast-and-frugal trees vs regression: Phillips (ML-level), Chen et al. 2018 (43 of 56 wins), Dhami and Green-Mehr (trees win) vs Hug 2023 (regression slightly better) and Alaswad (LLM rules worse). Wins are largest where data are few, and many were fits not predictions.
- Time pressure: Bobadilla-Suarez & Love experiments 1 and 2 reverse each other depending on stimulus format.
- "More thinking hurts": strong in mid-size Qwen, weak in frontier, reversed in the smallest (Bogdan); varies by model in Gema et al.; CoT also helps strongly on math (Sprague). Model- and task-specific.

## 4. Weak spots
- The LLM link to take-the-best rests on one single-author, non-peer-reviewed preprint (items author-built, LLM judge, amended pre-registration, 45 items). The other LLM papers measure heuristics-and-biases or CoT length, not the adaptive toolbox. Mapping "stop after one cue" to "stop thinking early" is an analogy.
- The founding simulation (G&G 1996) is one environment (German cities) with simulated knowledge, not human data.
- The Czerlinski 20-data-set result is cited secondhand by every source here; the 1999 chapter was not opened. Half the sets come from one textbook.
- FrugalGPT and RouteLLM are cost results, not tests of heuristic theory; checked via evidence lines only.
- Many applied results (bail, coronary triage, hiatus heuristic, Wimbledon) are secondhand in reviews (opened:false lines a09, a15, a16, a17, a22, a23).

## 5. Only seen in snippets or abstracts
c10 (Jones & Steinhardt), c12 (Opedal), c24 (Jagadish category learning), c28 (LLM rule trees, abstract and intro), b27 (Macmillan-Scott & Musolesi, abstract), b11 attribution unconfirmed, c18 (Hug) and c19/c20 (Menzies) not rechecked in full. FrugalGPT and RouteLLM numbers not rechecked this pass.

## GAPS
1. Does a cue-limited prompt (LLM sees only the top k validity-ordered cues) match full-information prompting on the city-size paired comparison and on a new cue-based task, at equal tokens? No one has run it (K16).
2. Does Bogdan's "longer CoT hurts on indeterminate items" replicate on independent items, by another group, with a non-LLM judge, and on current frontier models where it was only directional?
3. What are the exact Czerlinski et al. 1999 cross-validated accuracies for take-the-best, tallying and regression, and does the edge persist on larger modern data sets with proper tuning?
4. How do we set the S0 gate cheaply: which observable features (task class, equals sign, answer type, model confidence) predict when direct mode equals the full schema, and what is the false-skip cost?
5. Does recognition-like familiarity (retrieval hit, answer frequency, self-consistency across samples) act as a valid single cue in an LLM, and does its validity change by domain as in the 54% vs 89% human split?
6. Can an LLM learn cue order from a handful of in-context examples (ABC-TTB style), or does it default to compensatory weighting? Has anyone run LLMs on the Rieskamp and Otto adaptive-strategy paradigm?
7. Do fast-and-frugal trees built from data beat LLM-chosen mode routing at equal tokens, given that LLM-written rules lost to trained learners (K14)?
8. What is the real token and latency cost of a few-cue mode vs a many-cue mode in an agent (K07: frugal is not fast for humans)?
9. Are there peer-reviewed 2024-2026 studies (Judgment and Decision Making, Cognition, Psychological Review) on LLMs and ecological rationality that arXiv search missed?
10. Does mode use look pure at the mean but mixed per item in our own measurements, as in the recognition-heuristic dispute?

## Gap search results (2026-11-01, evidence_d.jsonl d01-d16, claims K18-K24)
Limits: the shared WebSearch quota ran out early, so only arXiv, direct PDF fetches and one Wikipedia/Cambridge page fetch were possible. Peer-reviewed venues (Cognition, Psychological Review, CogSci) could not be searched.

1. Cue-limited prompt vs full information at equal tokens: OPEN. No study found (d15). Only indirect support: irrelevant context hurts (Shi 2023, d10; K21). Must run ourselves.
2. Bogdan replication: PARTLY CLOSED in direction. Fan 2025 (d08) and AbstentionBench (d09, 20 LLMs, 35k items, -24% abstention recall, bigger budgets worsen it) are independent groups with the same sign (K18). Not an exact replication; frontier Claude/GPT with a non-LLM judge still untested.
3. Czerlinski exact accuracies: OPEN. Chapter not obtainable. Only secondary figures for the city set (72.2 / 71.9 / 71.4 out of sample, Wikipedia, d14) and Hutchinson & Gigerenzer text (d13) with no percentages. Margin on the founding case is under one point (K23). Modern larger data sets not checked.
4. S0 gate features: PARTLY. Cost side measured (d06: +1,953% tokens on 2+3; first round right in over 92% of correct cases; d07: 50-90% less thinking at near-flat accuracy; with Sprague equals-sign result K11). False-skip cost and a feature-based predictor remain unmeasured (K20).
5. Familiarity as cue: PARTLY. Internal known-entity signal exists (d01), semantic entropy and P(IK) are valid detectors (d02, d03), and confidence informativeness is domain-specific (d04), the same shape as the human split (K19). Not tested as a one-reason cue, and not through a black-box API except via sample agreement.
6. In-context cue order: OPEN. LLMs learn numeric weights in context at 50 examples (d11) but nobody tested noncompensatory cue order or the Rieskamp-Otto paradigm (d16; K22).
7. FFT from data vs LLM routing: OPEN. Only a trained router (Thinkless, d07) found; no head-to-head with an FFT.
8. Token and latency cost of few-cue vs many-cue: PARTLY. Token multiples known (d06, d07); latency and agent-level cost of few-cue modes not measured. K07 updated.
9. Missed peer-reviewed work: UNRESOLVED. Quota ran out. Opened peer-reviewed items are JDM theory (d05) and an LLM heuristics-and-biases study (d12); none is on the adaptive toolbox (K24).
10. Mean-pure vs mixed per item in our own data: OPEN. Needs our own measurements; no literature to find.

Corrections to earlier claims: K10 now cites two independent same-direction sources; K16 re-checked (about 28 further arXiv queries, no hit); K07 gained the LLM token-cost number. Not verified: d12's later journal publication, Thinkless table alignment, AbstentionBench judge identity.
