# Critique: A02.05 Representational change theory (cross-check)

## Re-opened and confirmed (against extracted text in D:/research_scratch/A02.05)
1. Knoblich 1999: F(3,57)=7.11 (Exp 1A), type x block F(3,57)=3.24, similarity F(3,74)=0.34, type effect F(4,222)=46.45. Confirmed.
2. Knoblich 2001: A 23/24, B 9/24 (chi2=18.38), C 18/24 (A vs C chi2=4.18; B vs C 4.78). Confirmed.
3. Nasvytis 2026: N=189, 80.7% vs 19.2%, 83.7% vs 44.0%, 89.9 s vs 179.0 s, 0.32 to 0.75. Confirmed.
4. Fedor 2015: 29/39 vs 6/62 insight reports, repetition 0.5 vs 0.3 t(99)=5.13, impasse button 8/24 vs 34/43. Confirmed.
5. Kershaw and Ohlsson 2001: chi2(2,N=90)=8.836, 17/19 (89%). Confirmed.
6. Graf 2023: N=61, 34% solved, change point near 90% bin. Confirmed.
7. NazoNazo: 52.9, 7.6, 17.6, OR 2.29, verification 5.23 to 39.34%, Grok-4 Japanese 29.5% p=.0071. Confirmed.
8. d'Aliberti 2026: 6.31%, 2.57% vs 16.44%, 1.79%, +8.41 pp, +0.45 pp. Confirmed.
9. MathSticks: 82.01%, 4.18%, o3 60.00 / 38.50, humans 91.72. Confirmed.

## Corrections and flags
- a25 gives ChatGPT BRAINTEASER as "53% and 63% (sentence and word)". c04 gives 62.68 sentence and 53.46 word. The extracted table is garbled, so the sentence/word order cannot be settled. Use "roughly 53 to 63%" and do not cite which is which.
- Fedor 2015: b15 says N=129 but the t-test has df 99, and 101 people (39 solvers, 62 non-solvers) are used for the insight-report split. Samples shrink after exclusions; cite 129 only as the recruited count.
- a14 says nine-dot baseline "under 5%" but the study's own control solved 37%. Treat the 5% figure as second-hand from older work and the 37% as this sample.
- Hint effect in Graf (b07): 34% + 11 points = 45%, consistent.
- Qiu 2026 (c14): I could not match the 47%/53% mediation split in the text file I looked at; marked single-source and unverified by me.
- Ormerod and MacGregor 2020 (a12, a13): not re-opened by me; numbers are the first agent's. Internal arithmetic checks (23/30 = 77%, 13/30 = 43%).

## Contradictions between sources
- RCT vs progress monitoring: Knoblich 1999/2001 argue RCT alone fits; Ormerod and MacGregor 2020 show value disparity erases the chunk penalty; Jones 2003 gives mixed support. The contest is open.
- Ohlsson's account says restructuring causes insight; Fedor 2015 finds solvers cycle search and impasse with no clean stage order.
- Graf 2023 shows suddenness appears or vanishes by analysis method.
- LLM side: Nazonazo says restructuring plus verification is the bottleneck; d'Aliberti says spontaneous restructuring shifts are rare and harmful in small RL models. Both can hold (generation vs commitment vs trigger).
- c21: the LLM agent that proposes new constraint models equals best-of-5, which argues against crediting the agent's restructuring.

## Weak spots
- All human RCT evidence is matchstick, N of 20 to 121 per study, one lab family; a12/a13 are the only independent lab replication and they only partly replicate.
- Which constraints and chunks are active is stipulated by the authors, never measured.
- No LLM study tests Roman-numeral chunk theory. MathSticks is seven-segment; Nazonazo is wordplay; none ablates O4 vs O6.
- LLM results are mostly 2023 to 2025 models, small RL models for d'Aliberti, tiny samples for Haq (6 per cell) and the situation-puzzle reformulation (5 puzzles).
- Cue-vs-resample is not separated in the forced-reconsideration result.

## Seen only in snippets or abstracts
a15, a16/b19/c25 (Oellinger 2006), a17/b17/c26 (Jones 2003), a18/b18 (Oellinger 2013), a19 (Ohlsson 1992/2011 books never found), b20, b21 (abstract), c27 (Frontiers 2025), c20 (RM-PoT numbers missing), c24 (partial).

## GAPS
1. Does an explicit constraint-listing then relax-one-constraint step (O4) beat plain sampling and best-of-k at equal tokens on matchstick items with known constraint types? Nothing tests this.
2. Does the Knoblich difficulty order (value < operator < tautology; loose < tight) appear in LLM solve rates on Roman-numeral matchsticks, and does it shift with a scaffold?
3. How much of the Nazonazo/BRAINTEASER gap is generation vs verification, and does a harvest-and-commit step on the thought log recover the 5 to 39% verification failures?
4. Is the forced-reconsideration gain (+8.41 pp MATH-500) larger than a plain second sample at equal tokens, and does it work on non-math restructuring tasks (crosswords gain was +0.45 pp)?
5. Does progress monitoring (switch on stall) or representation change (O6) explain more variance in LLM trace outcomes? Ormerod 2020 suggests monitoring; needs a head-to-head.
6. What do Ohlsson 1992/2011 and the full Oellinger 2006/2013 and Jones 2003 papers report (numbers, model details)? Only abstracts were seen.
7. Is there any executable RCT model (constraint/chunk simulator) that could generate predicted orders for items beyond matchsticks?
8. Does typed memory of "which representation change worked" (transfer by change type, 0.32 to 0.75) transfer to LLM agents better than surface-similar retrieval?
9. Do the results replicate on uncontaminated insight items (ChatGPT 12/30 on famous problems may be memorised)?
10. What are the real BRAINTEASER ChatGPT sentence/word numbers and the reconstruction-consistency drop for 2025 reasoning models?

## Gap search results

Searched and re-read sources; evidence is in evidence_d.jsonl (d01 to d15) and claims K21 to K25 were added. The web search budget ran out partway, and arXiv search and OpenAlex returned 429 or empty, so "open" below means not found in a limited search.

- Gap 1 (constraint-list then relax vs sampling and best-of-k): OPEN. No study found. Ormerod & MacGregor 2020 warn that number disparity alone moves matchstick solving (12% to 62%), so any such test must hold disparity fixed (K24).
- Gap 2 (Knoblich order in LLM solve rates): OPEN. MathSticks (o3 60.00% with text, sign-changed 51.45 vs 65.19) is seven-segment, so no chunk test. Its generator is public and could be adapted to Roman numerals.
- Gap 3 (generation vs verification): PARTLY CLOSED. The 5.23 to 39.34% table is real but exists only in NazoNazo v3 (string match, 4 models). Upper-bound recovery: Grok 4 37% to 62%, Gemini 14% to 19%. Whether a commit rule can actually pick the right candidate was not tested.
- Gap 4 (forced reconsideration vs plain second sample): OPEN. Table 5 has no cue-free second sample and no equal-token arm. The high-entropy bucket gain (+15.38 pp math) is partly regression to the mean (my inference). Off-math gains stay tiny (+0.45 crosswords, +0.01 Rush Hour).
- Gap 5 (monitoring vs representation change in LLM traces): OPEN. Only human evidence (Ormerod & MacGregor 2020, full text now read). Jones 2003 still not opened.
- Gap 6 (Ohlsson, Oellinger, Jones full papers): OPEN. Oellinger 2006 and 2014, Ohlsson 1992/2011 and Jones 2003 are paywalled or blocked. Ormerod & MacGregor 2020 and Kershaw 2004 were read in full; the unaided nine-dot baseline is about 0% (cited from MacGregor 2001), and trained groups reach 30 to 97%.
- Gap 7 (executable RCT simulator): OPEN. None found; Ormerod & MacGregor say Ohlsson 2011 gives only a partial specification.
- Gap 8 (typed memory by change type): OPEN for LLM agents. Human same-type repetition result (0.32 to 0.75) not re-checked.
- Gap 9 (uncontaminated insight items): PARTLY CLOSED. NazoNazo splits items into 42 open and 159 blind, reasoning vs non-reasoning odds ratio 2.29 (CI 1.99 to 2.64), and GPT-5 sits inside the human 95% CI (46.6 to 59.2%; descriptive only). The ChatGPT 12/30 on classic problems was not rerun by anyone.
- Gap 10 (BRAINTEASER numbers): CLOSED for ChatGPT 2023: sentence 62.68 overall (group 39.71), word 53.46 (group 29.27), humans 91.98 and 91.67. The 53 vs 63 conflict was word vs sentence. OPEN for 2025 reasoning models.

Status changes: K10 to contested (GPT-5 inside the human range), K12 reworded (+8.41 pp is math only, Pass-2 vs Pass-1, no cue-free control), K11 annotated (v3 only), K06 numbers verified from full text. Not re-checked: Qiu 2026 split, Nasvytis 2026, Frontiers 2025.
