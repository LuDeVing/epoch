# Critique: Whorfian psychophysics (A15.06)

## Numbers re-checked against the source text (this session)
Confirmed unchanged: Boroditsky 2001 English 2128 vs 2300 ms, F(1,25)=13.76; Mandarin 2347 vs 2503 ms; three-way F(1,44)=5.24; age of acquisition r=.47 (a02, a03). Dolscheid 2020 Turkish height-pitch 15%, t(39)=-9.71, d=-1.54; 36 of 39 (92%) thickness; language x task chi2=67.73 (b07, b08). Crossley and Bylund 2025 reading 87.5% vs mirror, replication 78.1% vs 40.6% (b15; the mirror-baseline figure appears as 46.9% in the PDF text, see below). Goli and Singh 22%, 16%, 34.5%, CIs [1.715,1.948] vs [1.948,2.210], 20% and 13.8% topic gaps (c01-c03). Wang 2025 Babel: 91.0/91.2 forward, 88.5/76.5 reversed, SVCCA .73/.64, Llama-3.2-3B Zh 56.8 (b22, c16). Gurnee and Tegmark Table 2 (a23).

## Corrections
1. c15 labels the 0.896/0.825/0.237/0.804/0.806/0.645 row as Llama-2-70b. In the ICLR Table 2 the rows read 7b 0.881, 13b 0.896, 70b 0.911 (linear, 60% depth). So c15 is the 13b row and a23 (70b = 0.911, USA 0.864, NYC 0.359, headlines 0.746) is right. K10 uses the 70b numbers. c15 should be relabelled.
2. b15: the PDF text gives 46.9% past-left in the first mirror condition, while the evidence line records 53.1%. The two sum to 100%, so the line probably recorded the complement (future-left or similar). Treat the exact baseline mirror figure as unresolved; the replication 78.1 vs 40.6 is confirmed.
3. c16/c17: Llama-3.2-3B En 27.0 vs Zh 56.8 is a column average in a 400-sample set; it is the one case where Chinese beats English by a lot and contradicts any story that Chinese is harder. Not a correction, but do not cite the 1.8B Qwen result alone.

## Contradictions
- Boroditsky 2001 (vertical bias, Mandarin) vs Chen 2007, January and Kako 2007, Tse and Altarriba 2008 (no effect). Partly reconciled by Chen 2011/2017: bias appears in Taiwan, not China, and tracks vertical text reading. Yang 2022 (b13) found a vertical effect again (N=91), so the literature stays split.
- Russian blues: Winawer 2007 effect vs Martinovic 2020 null (p=.29). The shift under frequency context was only in Russian speakers, so some language effect survives.
- Goli and Singh: standard-conjoint CIs touch at 1.948, so "strong FTR languages discount more" is not clearly shown; chain-of-thought CIs are separated by only a small margin.
- Pitch: thickness-pitch is shared across languages (b07) while height-pitch differs, so "language builds the mapping" is contradicted by the infant data (b28, second-hand).

## Weak spots
- Many original sources were seen only as citations in later papers: a07, a12, a13, a16-a22, b06, b09, b16, b19, b25-b27, c09, c10, c24, c25. Original N and statistics for the replication failures (a18-a20, b26) were not read, so K01 rests on a list of failures without their effect sizes.
- Casasanto 2016 (the key handbook chapter, a22) was not opened.
- LLM evidence is thin and mostly not Whorfian: representation probes (K10), perception and iconicity (K13), spatial frames (K14). Only Goli and Singh and Wang et al. test language as a variable on reasoning, and each is one study. Zhang and Rayz 2026 (b23) has no extracted effect sizes.
- Several 2026 entries (a26, b24, b23, c07) are recent and single-lab; not replicated.
- Relevance to our agent is low by the subfield's own verdict ("background only"). Schema mapping is mostly "none".

## GAPS
1. Does anyone test ego-moving vs time-moving framing, or spatial-metaphor wording, on an LLM's behaviour? (0 found in 9 searches; K15)
2. Do the Goli and Singh language-FTR effects replicate with other models, other tasks, and controls for translation quality and training-language share?
3. Does the Chinese-vs-English causal-order gap in Wang 2025 hold above 7B and in other models, and is it a language effect or a data-mix effect?
4. What are the sample sizes and effect sizes of the three failed replications of Boroditsky 2001 (Chen 2007, January and Kako 2007, Tse and Altarriba 2008)?
5. What does Casasanto 2016 conclude about which Whorfian effects are robust, and how does it weigh the Deep vs Shallow View?
6. Does the pitch-height/thickness metaphor affect LLM performance on music or acoustic judgement tasks (Marjieh-style), and does prompt language change it?
7. Do the Winawer-type colour boundary effects appear in LLM or VLM colour naming across Russian and English prompts (Marjieh c05 hints at differences: sinij 18 vs 29 chips)?
8. What is the exact mirror-reading baseline in Crossley and Bylund 2025 (46.9% or 53.1%), and do their writing-direction nulls survive a larger N?
9. Do Zhang and Rayz 2026 deictic time-frame asymmetries (future vs past) hold when measured with effect sizes across languages?
10. Is there any LLM study of the space-time asymmetry (length judgments distort duration judgments more than the reverse)?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d21); claims K01, K05, K11, K12, K15 were updated and K17-K23 added.

1. Gap 1 (ego/time-moving or spatial-metaphor wording on LLMs): STAYED OPEN. About 20 more searches, 0 direct tests (d20). Nearest: Zhang and Rayz 2026 deictic vs sequential frame (d12), vocabulary-constraint agents (d18).
2. Gap 2 (Goli and Singh replication): STAYED OPEN, weakened. No independent replication found (d09). A direct human test of the mechanism found more future-tense use predicted LESS discounting (N=235 and N=606, d07, d08). K12 stays contested.
3. Gap 3 (Wang 2025 above 7B, language vs data mix): PARTLY CLOSED. Second table: Mistral-7B 93.8 vs 81.5, Qwen1.5-1.8B 88.5 vs 76.8, but Qwen 14B 97.5 vs 97.5, 32B 90.5 vs 94.0, 72B 97.0 vs 96.2 (d10, d11). Gap shrinks with scale; no data-mix control exists, so language vs data stays unresolved. Caption check needed: the PDF calls Table 2 "paraphrased data".
4. Gap 4 (Ns of the three failed replications): STAYED OPEN for Ns. New: January and Kako ran six experiments; Tse and Altarriba partly replicated the bilingual half and both groups showed a vertical-prime advantage (d03, d04). Papers are paywalled.
5. Gap 5 (Casasanto 2016): STAYED OPEN. Only the abstract was read: continuity of linguistic, cultural and bodily relativity, "language is not special" (d01). Routledge chapter and the Deep vs Shallow weighing unread.
6. Gap 6 (pitch metaphor on LLMs): CLOSED AS "NOT TESTED". Marjieh gives pitch r=.92 with English prompts only (d13); no height vs thickness test exists (K17).
7. Gap 7 (Winawer-type effects in LLMs): PARTLY CLOSED. GPT-4 naming ARI 0.59 English vs 0.54 Russian, with different partitions from the same hex codes (d14); a vocabulary effect, not a discrimination effect. New caution: much cross-language colour difference is a spelling artifact (d16).
8. Gap 8 (Crossley and Bylund mirror baseline): STAYED OPEN. Not re-opened this pass. K05 text now flags the 46.9 vs 53.1 ambiguity.
9. Gap 9 (Zhang and Rayz effect sizes): STAYED OPEN. The paper reports no effect sizes or tests, English only, Qwen3-4B and 30B, 2,916,927 deictic entries (d12).
10. Gap 10 (LLM space-time asymmetry): STAYED OPEN. No study found (d20).

New items: Miles et al. 2011 bilingual two timelines (d05); Yoruba prompting preprint (d17, n=10, weak); Umwelt Engineering (d18, the only agent-relevant study: vocabulary constraints change reasoning by task and model, preprint). Constraint: Semantic Scholar rate-limited and the arXiv API returned nothing, so absence findings are limited.
