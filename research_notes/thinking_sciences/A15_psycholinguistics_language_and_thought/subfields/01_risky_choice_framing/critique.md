# Critique: A15.01 Risky-choice framing (cross-check)

## Verification pass (re-opened sources this session)
Confirmed against live pages:
- Tarabeih 2026 (arXiv 2610.33103): 102 estimates, 11 studies, 32 models, lambda 1.26 (1.06-1.46), human 1.96/1.31/1.07, curvature 1.01 and 0.52, weighting 0.81 and 0.84. All match b21/a27.
- Rachev 2021 (PMC8432807): N=88,181, 47 countries, B=1.24, d=.69. Matches b06. Correction: the paper itself gives the Many Labs reference as d=.60 in Results and .62 in the Introduction; b06 and a12-style notes should say "about .60-.62".
- FrameBench-HPS (2610.29294): abstract confirms 2,880 prompts, 240 scenarios, 7 LLMs, 32.4% category change, most changes via uncertainty. The abstract has no CI, no 98.1%, no canonicalization numbers. Those (6.68%, 22.83%, 7.12%, 0.363 to -0.010) were read in the full text by agents b and c, who agree with each other (a29, b15, b16, c01-c03), but this pass did not re-open the body.
- Not confirmable from abstracts (page gave no numbers): Wang and Zhang 4.3%/68.8% (abstract has none), Echterhoff GPT-4 admit rates, Payne scenario numbers, Ge et al. correlations, Pinon and Gambara (PDF unreadable as text). These rest on full-text reads by agents b and c, whose figures agree where they overlap (Payne b13 vs c04; Echterhoff b17 vs c14). Correction: Echterhoff prompt count is 13,465 in the abstract; b17 said 16,800.
- Qualitative corrections: a12's note that delta may be 0.65 stays unresolved; Tversky and Kahneman 1992 gives gamma 0.61, delta 0.69 (standard values), and the 0.65 is a different source.
- Memory check of 1981 and 1979 numbers (Asian disease 72/28 and 22/78 with N=152/155; Problems 3, 5-7) agrees with my knowledge of the papers.

## Contradictions between sources
1. Reasoning models: Ge et al. (reasoners nearly frame-invariant) vs Payne (o3, Claude-4-Thinking still large effects). Likely difference is task format: explicit two-option prospects vs story scenarios with three options.
2. Echterhoff: GPT-4 effect negative (-0.405), GPT-3.5 positive (+0.165). Direction is model-dependent.
3. Mandel 2014 ('at least') vs Data Colada replication: disputed, one side is a blog.
4. Numeracy: Peters and Levin positive, Mandel and Kapler null.
5. Time pressure: Svenson and Benson vs Guo/Diederich, unopened.
6. Per-model rates differ between FrameBench full set (GPT-4o-mini 63.33%) and robustness subset (56.5%): different data, not an error.
7. Jones and Steinhardt "11.3%/60.0%" are GPT-3 averages over probability ranges (b11), not Binz and Schulz (c10 correctly says not found there).

## Weak spots
- Almost all LLM framing studies are preprints, many 2026, single-author or small. Several test attribute framing, fairness, or admissions, not the gain/loss risky choice.
- The classic text is likely in training data; only Suri et al. avoided it.
- Human meta-analysis figures (Kuhberger 1998, Many Labs 1 per-lab counts, Zhou 2021 summary) include second-hand numbers.
- FrameBench canonicalization is tested on 3 models, 32 scenarios, single stated probabilities only.
- No study measured a full agent loop; no test at equal tokens for any mitigation.

## Seen only in snippets or secondary pages
a23, a24 (Many Labs 1 totals), a25, a26, b22, b23, b24, b25, b26, c09, c27; Keysar 2012 numbers; Talboy and Fuller; Horton results tables.

## GAPS
1. Does code-run canonicalization (both complements, final-state table) beat a self-written neutral rewrite and an instruction-only prompt on the classic Asian disease and multi-stage (pseudocertainty) items, at equal tokens, on a current reasoning model?
2. Does the flip rate of a reasoning-class model on story-format (not explicit-prospect) problems exceed its same-wording repeat noise, across at least four domains?
3. Does a second wording within one context (both frames shown) reduce LLM flips as it cuts the human effect by two thirds, and does the model then choose consistently or just agree with the first?
4. Are Wang and Zhang, Echterhoff and Payne figures reproduced by their full texts (those not checkable here), and do Talboy and Fuller (2023) primary numbers exist?
5. Does context length or mental-demand padding amplify the frame in an LLM as it does in humans (Pilli and Nallur)?
6. Does token budget (short vs long reasoning) change frame sensitivity, given the unresolved time-pressure literature?
7. Do parallel votes with different canonical wordings beat same-wording sampling at equal token cost?
8. How much of the Asian disease flip in humans survives the Zhou 2021 structural controls when the missing-complement manipulation is applied to LLM prompts (does removing the zero outcome remove the flip in models)?
9. Does CoT raise or lower framing flips in frontier (not 7-8B) models?
10. What are the primary-source numbers for Many Labs 1 and Kuhberger 1998 and Steiger and Kuhberger 2018 (corrected d)?


## Gap search results

Evidence file: `evidence_d.jsonl` (d01-d15, all opened this session). Claims: K01, K02, K09-K14, K17, K18 updated; K20-K24 added.
Limits of this pass: the shared web-search quota was used up, and arXiv API, OpenAlex and Semantic Scholar all returned rate-limit errors. I used arXiv listing pages, direct PDFs, Crossref and the OSF file store. A broad forward-citation sweep was therefore not possible; "no study found" below means "none surfaced in the title searches I could run", not "none exists". No new LLM experiment was run, so gaps that need a measurement stay open.

| Gap | Status | What was found |
|---|---|---|
| 1. Code-run canonicalization vs self-rewrite vs instruction, equal tokens | OPEN (partial support) | Nobody ran the three-way test. FrameBench (d10) used a one-sentence canonical form: 34.20% to 6.68% vs 22.83% for an instruction. Echterhoff (d07) shows a model-written rewrite removes GPT-4's gap (-0.405 to -0.010). Payne (d15) shows symbolic form plus forced EV calculation gives 200/200 indifference for o3. Pseudocertainty items: nothing found. Token cost never matched. |
| 2. Story format, reasoning model flips vs repeat noise, 4+ domains | PARTLY CLOSED (yes) | Payne (d08): o3 significant in 4 of 7 scenarios, Claude-4-Thinking 6 of 7 (25 runs per cell). FrameBench (d09): GPT-5 33.40% category change vs 7.12% pooled repeat noise, 4 domains, but noise not measured per model and no per-domain table in the text I read. |
| 3. Both wordings in one context for LLMs | OPEN | No LLM study found. Human anchor stays about two thirds reduction. Not measured whether the model answers consistently or just copies the first wording. |
| 4. Unchecked figures | MOSTLY CLOSED | Wang and Zhang (d06): 4.3% and 68.8% confirmed, but denominators include non-compliant replies (valid-only 4.5% and 76.5%) and the task is not gain-loss. Echterhoff (d07): Table 3 confirmed, 13,465 prompts. Payne (d08, d15): table values confirmed. Pinon and Gambara (d04): PDF did extract this time; d=0.437 / 0.260 / 0.444 confirmed. Ge et al. (d13, d14): correlation 0.86-1 confirmed; explanation per-model values only partly extracted. Talboy and Fuller (d05): no primary numbers exist (qualitative demo). |
| 5. Context length or padding amplifies the frame | PARTLY CLOSED (role-play only) | Pilli and Nallur (d11): LLM persona effect rose after complex dialogue in 2 of 3 prompt styles (z 4.53, 7.04; third ns). This is role-play of a human, effects 3-9 times human size. Own-judgment padding test not done. |
| 6. Token budget vs frame sensitivity | OPEN | No study found. Time-pressure literature in humans still unverified (Diederich et al. not re-opened). |
| 7. Votes with different canonical wordings vs same-wording | OPEN | Only the same-wording failure is documented (Wang and Zhang, 82 models). No test of mixed-wording voting. |
| 8. Remove zero outcome of the risky option in LLMs | OPEN | No LLM study found. Zhou 2021 page could not be re-opened (connection refused), so the human numbers stay second-hand. |
| 9. CoT raises or lowers flips in frontier models | OPEN (split signal) | Knipper (d12): reasoning-trained open models 14-70B more frame-resistant (R1-Qwen-14B .826 vs Qwen2.5-14B .365). Ge (d13): reasoning models ignore framing on explicit gambles. Payne (d08): reasoners still flip on stories. No same-weights thinking on/off test on a frontier model. Format decides. |
| 10. Primary numbers for Many Labs 1, Kuhberger, Steiger | MOSTLY CLOSED | Many Labs 1 (d01, d02): 62.2% vs 33.5% sure option, chi2(1)=516.41, N=6,271, d=.60, 36 samples, 6,344 participants. Steiger and Kuhberger (d03, abstract only): corrected d=0.52 vs Kuhberger's 0.31, 2016 meta-analysis 0.56. Kuhberger 1998 itself: abstract not retrievable; d=0.31 comes from Steiger's abstract. |

### Corrections to earlier material
- Human pooled effect: the 'small to moderate' reading of K02 is wrong. Publication-bias-corrected d is 0.52, 2016 studies 0.56, Many Labs 0.60.
- Many Labs 1 swing is about 29 points (62.2/33.5), not the 50 points of the 1981 original (72/22).
- Wang and Zhang rates need a denominator note; the study is a survival-threshold story, not gain-loss.
- FrameBench model rates differ between the full set (Gemini 2.5 Pro 32.56%) and the robustness subset (14.1%); these are different data.

### Minimum experiment grid still needed (not run here)
1. Asian disease, a multi-stage pseudocertainty item, and two story items in four domains; five arms: plain, instruction only, self-written neutral rewrite, one-sentence canonical, code-run final-state table; same token cap; at least 20 repeats per cell; report flip rate against same-wording repeat noise.
2. Same items with both wordings shown in one context, asking for one answer, and a check whether the answer follows the first wording.
3. Thinking on/off and a low versus high reasoning budget, same model.
4. Votes of 5 with 5 different canonical wordings vs 5 samples of one wording.
5. Risky option with and without the stated zero outcome.
