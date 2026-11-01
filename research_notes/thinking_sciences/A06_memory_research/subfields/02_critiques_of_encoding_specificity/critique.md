# Critique: A06.02 Critiques of encoding specificity (cross-check, second pass)

Inputs: evidence_a (26 lines, founding studies and AI memory), evidence_b (33), evidence_c (23), evidence_d (27, gap search). Claims: 36 in claims.jsonl (K01-K36).

## Re-opened this session (full text, pdftotext)
CONFIRMED against the text:
- Tulving and Wiseman 1975: c=.50, 40 data points, r=.95, SE .028; 12 experiments; Watkins and Tulving Exp 3 table (.26, .06, .37, .31; recall .63).
- Duan, Glass and Raanaas 1998: r=.90 with P(Rn), r=.06 (CI -.05 to .17) with P(Rc); subject-wise r=.59 (CI .32-.77) vs item-wise r=-.03.
- Isarida et al. 2012: d' 1.466 vs 0.738 (1.5 s), 1.901 vs 1.972 (4 s); hits .723/.613 and .796/.788; nonword F(1,38)=18.18.
- Shin et al. 2021: .32 vs .26; beta .349, Z 2.690; useful .521, harmful .177 (Z .918, p .359).
- Choi et al. 2025: d .49 (CI .42-.55), top 31%, rare .44 vs common .15, 47 analysed, 198 trials (4.63%) removed, no power analysis.
- Postman 1975: F(1,92)=94.68 and 11.78; cell gains 3.67, 2.29, 1.67.
- Stern and Nadel 2026: 73.7 vs 53.5, +20.2 [12.1, 29.3]; per-category table; 156,430 vs 159,211 and 244,385 vs 252,750 tokens; all arms Claude Sonnet 4.6; GPT-4o judge; authors state the encoding-versus-retrieval ablation was not run.
- RippleMem: LoCoMo 52.49 / 44.05 / 87.14; 1,471.93 tokens; RF-Mem judge 83.83.
Earlier pass (kept): Dinh 2026, Guo 2026, Cuconasu 2024, NoLiMa Table 6, Sciavolino 2021, HippoRAG, Weller, Anthropic blog all confirmed.

## Corrections
1. a18 (RippleMem ablation) is mislabelled. In the paper's ablation figure 83.83 (-3.80%) is "w/o Structural" and 83.12 (-4.61%) is "w/o Graph Expansion"; a third row 84.35 (-3.20%) is another component. Neither is "hybrid cues". Coincidence: 83.83 is also RF-Mem's score. Use the 3.2 to 4.6 percent range only.
2. a09/a20 say Postman found recall lower than recognition "in all eight" Tulving-Wiseman conditions. The paper text I read supports only "recall was not found to be superior to recognition"; the eight-condition sentence was not located. Treat the all-eight wording as unverified. Postman also notes hit rates fell once false alarms were subtracted, so the comparison depends on scoring.
3. a25: the P(RN|RC) vs P(RC) r=.27 (CI .06-.55) is confirmed as printed; the authors' wording "nonsignificant" is odd given a CI that excludes zero. Cite as r=.27 only with that caveat.
4. NoLiMa row mix-up (Llama 3.1 vs 3.3 70B) and the HippoRAG text-vs-table conflict stand from the first pass: cite tables.
5. Cuconasu -25% and -67% are peaks. Random-document +35% is +0.07 absolute on a base near 0.2.

## Contradictions between sources
- Match: Goh and Lu say match helps when overload is equal; Poirier and Badham say it is diagnostic value, not match. Badham notes Goh and Lu left the overloaded cue untrained. Verdict: "match alone is not enough" established, "match is a myth" contested.
- Postman vs Watkins and Tulving: recall over recognition fails to replicate (K28). Postman himself cannot explain the gap.
- Outshining: Smith and Vela moderator holds (d .13 vs .33, chi2 6.67) but the test-type prediction failed; Isarida supports it directly; Ensor 2023 says context is not a retrieval cue in recognition at all. Contested (K05).
- Higham: report bias explains the strong-cue failure (free .07 vs forced .26) yet Postman's Exp 1 shows strong output cues win with forced scoring too. They agree that cue strength is what counts, not the original match.
- Gardiner 1988 says no extra dependence; Duan 1998 says the dependence is item-specific. Both can hold: the law fits pooled data, failures live in few items.
- Random documents help RAG (+35%) while related distractors hurt (-25% to -67%). Unexplained.

## Weak spots
- AI evidence is indirect. Stern and Nadel is the strongest write-time-context test, yet one run per arm, 20 questions per category (CI about 30 points), no filler arm, no ablation. Its single-session null is weak evidence.
- Poirier effects are in reaction time near ceiling, N 21-25, one lab plus Goh and Lu.
- Choi 2025 has no power analysis and confounds dwell time with place importance. Shin 2021 cells are 16 subjects.
- Guo 2026: arXiv id 2606 but stamped 9 May 2026; human slope not replicated.
- Many machine studies use 2022-2024 models.

## Only seen in snippets or abstracts
Tulving and Thomson 1973 and Thomson and Tulving 1970 (paywalled; no numbers used). Higham 2002 and Nairne 2002 (abstracts; the .26/.07 figures come from the b-file). Poirier 2012 (b-file; abstract in d27). Goh and Lu 2012, Smith and Vela 2001, Stein 1977, Badham 2016 (b-file, not re-opened now). MemoCue (a19): LLM-judged 17.74% gain, not re-checked. c20 and c21 were never opened.

## GAPS
1. Does a write-time distinguishing line beat a same-length neutral filler line, and does the gain exist only when the plain key is missing or weak (outshining)? Run on the agent's own notes at equal tokens; crossing tag type with strong-key present/absent. Closest evidence is Stern and Nadel (no filler arm) and RaMem (wrong tags 0.236 vs none 0.571 vs right 0.807 Recall@10).
2. Is Stern and Nadel's +20.2 pp due to the write-time scene, the read-time scene, or just extra text? Needs the encoding-versus-retrieval ablation they did not run, with more than 20 questions per category.
3. Which key-scoring rule works best on agent memory: similarity over summed rival similarity (Nairne ratio), IDF-weighted, or plain cosine? Only cosine 73.4 vs BM25 57.1 vs hybrid 77.2 is known (LoCoMo).
4. How often does a copy-style (restated item) probe miss facts that the original-context cue finds in an LLM store, and are those misses concentrated in items with outside-episode links, as Duan 1998 predicts? Score per item.
5. Does Higham's report-bias result transfer: how many correct candidates does an agent withhold under confidence gating, and does forced listing recover them? Known: LLMs under-abstain with retrieved text, the opposite risk.
6. Does the question-shaped vs item-shaped key direction (Fisher 1979) show up in agent retrieval: are notes retrieved better by a key written as the likely question or as a summary of the item?
7. Does the benefit of a tag grow with the number of intervening writes (Smith and Vela long-delay moderator), or with same-key writes (log-linear loss in PI-LLM)?
8. Why do random documents raise RAG accuracy (Cuconasu), and does it hold on 2025-2026 models?
9. Are there replications of Poirier 2012 with accuracy, preregistered, outside its network, including failures? None found in PubMed.
10. Do Tulving and Thomson 1973 and Watkins and Tulving 1975 report the figures usually quoted (recognition failure rate; recall of recognition-failed words)? Verify from a legal copy before the synthesis cites them.

## Gap search results (evidence_d d28-d36, claims K37-K42)

Budget note: web search was rate-limited and the arXiv, Semantic Scholar and OpenAlex APIs returned HTTP 429 for most of the session. Papers were opened as full PDFs (pdftotext). Evidence file keeps d01-d27 from the earlier pass and adds d28-d36.

Gap 1 (write-time distinguishing line vs neutral filler; outshining): PARTLY CLOSED, still open for the exact test. LongMemEval (d28, d29) shows raw text plus extracted fact beats raw text; condensed key alone loses; the gain is largest with the weakest retriever (BM25 +.082 vs Stella -.016 at round level). That fits outshining but there is no filler arm and no crossed design. Open.
Gap 2 (Stern and Nadel ablation): OPEN. No follow-up found.
Gap 3 (key scoring rule: Nairne ratio vs IDF vs cosine): OPEN. Only retriever comparisons (d29: BM25, Contriever, Stella); no ratio-to-rivals score tested on agent memory.
Gap 4 (copy-style probe misses, item-level): PARTLY addressed by Locomo-Plus (d31): when the trigger shares no wording with the cue, all methods fall to 12-26 percent. Item-level concentration on outside-episode links not scored. Open.
Gap 5 (Higham report bias in agents): CLOSED IN PART, direction reversed. Models withhold under irrelevant context (d34) and some over-abstain on answerable items (d35, Claude-Sonnet-4 .259), while also over-answering when evidence is insufficient (d22). K22 changed to contested. No forced-listing recovery test exists. Open.
Gap 6 (question-shaped vs item-shaped keys): CLOSED IN PART. QuOTE (d32) favours question-shaped additions when competitors are many; LongMemEval (d28) shows summaries alone lose. Doc2Query-- (d33) shows unsupported questions hurt. No test on non-extractive agent queries and no length control.
Gap 7 (tag benefit vs intervening writes): OPEN. Only history-length drop (30.3 to 48.1 percent, d30) and date-tag gains; tag benefit by delay not measured.
Gap 8 (random documents raise RAG accuracy): OPEN. Searches found no accuracy replication on 2025-2026 models; search summaries describe the random-document gain as not consensus. Treat +35 percent as unreplicated.
Gap 9 (Poirier replications with accuracy): OPEN. Searches return only Poirier 2012, Badham 2016 and Beaman 2013.
Gap 10 (Tulving and Thomson 1973, Watkins and Tulving 1975 figures): OPEN. Journal pages paywalled; Wikipedia and Hanley 1984 (d36) have no figures. Do not cite their percentages.

Opened this session but not used as evidence: Terranova et al. 2025 (arXiv 2510.23730, memory types in long-context QA) and Pink et al. 2026 (arXiv 2607.22575, a temporal-context reinstatement head in long-context models); both only skimmed.
Note: the earlier critique text above predates this section; K22 is now contested, and RippleMem figures remain as corrected.
