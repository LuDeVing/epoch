# Critique: E18.02 Ecological rationality, adaptive toolbox

Cross-check date 2026-10-27. Sources re-opened this session: Sprague 2024 (arXiv 2409.12183), Liu 2024 (2410.21333), Bogdan 2026 (2606.15877), Chen FrugalGPT (2305.05176), Simsek & Buckmann 2015 (NIPS PDF), Parpart et al. 2018 (PMC5886040), Pachur et al. 2011 (Frontiers full text, first 100k of 159k characters).

## Numbers confirmed
- c19 Sprague: 110 papers, 1,218 comparisons, 264 datasets; +14.2 / +12.3 / +6.9; 56.9 vs 45.5 in top three; 56.8 vs 56.1 elsewhere; 95% of MMLU gain on "=" questions. All match.
- c20 Liu: GPT-4o 87.5 vs 64.4; Claude 3 Opus 70.7 vs 62.7; Llama 3.1 70B 65.9 vs 57.1; o1-preview 57.7 vs GPT-4o subset 94.0 (36.3 gap); face recognition 64.0 vs 51.2 and 44.0 vs 29.6. All match.
- a24/c04/c05 Bogdan: 7,875 responses, 17.3 points, CI [7.7, 25.5], 77.1% direct, beta1 = -0.183, P = 0.905, 26,696 comparisons. All match.
- c17 FrugalGPT: 98%, 0.872 vs 0.857, $6.5 vs $33.1, thresholds 0.96 and 0.37. Match.
- a18/c14 Simsek: 0.747 / 0.746 / 0.743 / 0.743 / 0.734 / 0.725 at 50% train; 63 data sets; 83% bound; fitting 0.758 / 0.756 / 0.742. Match.
- b01 Parpart: TTB beats regression at 20 training cases and reverses at 100 (house prices, 231 pairs). Match.
- b11 / b10 Pachur: r = 0.64, p = 0.03 over 11 environments; Richter & Spath 95% (median 97%, mean 82%, 17 of 28); Newell & Fernandez 64% vs 98%, 23% always; Hilbig 62-76%. Match.

## Corrections
1. b01/b02/b03: authors are Parpart, Jones and Love (2018, Cognitive Psychology 102:127-144), not "Parpart, Schulz, Gershman, Yeung-Jacobs". Fix the author field in all three lines.
2. b10: the "individual level r = -0.03" is NOT adherence versus validity. In Pachur et al. it is individual estimated validity versus actual recognition validity (Pachur 2008). The review reports no individual-level adherence-validity correlation. Reword the limit.
3. c20: Claude 3.5 Sonnet showed no CoT harm on implicit learning (65.9 vs 67.7, -1.8, p = .969). Add this to limits, since strong models are not uniformly hurt.
4. Bogdan: the paper is arXiv 2606.15877 (June 2026), single author, preprint. Confirmed as stated.
5. FrugalGPT text in the PDF is garbled at the GPT-4 accuracy; 0.857 read from the layout, consistent with a17.

## Not re-verified (still snippet or second-hand)
- a02 / a03 Gigerenzer & Goldstein 1996 Table 2 (.658 etc.): the MPG PDF returned a damaged file; numbers not re-checked.
- b16 Glockner & Broder 2011 (77.5% PCS): journal page gave 404 and the PDF did not download; only Pohl's secondary report agrees (b15).
- a21 / b24 DeMiguel 2009 (3000 / 6000 months): publisher page truncated; search budget was used up. Still abstract-level.
- a20 Dawes 1979, b25 Dana & Dawes 2004, b23 Brighton & Gigerenzer 2015, b26 Katsikopoulos 2010, b27 Newell & Shanks 2004: unopened.
- c24 Nikankin: abstract only.

## Contradictions between sources
- Founders versus Glockner/Broder, Newell: noncompensatory use of recognition ranges from 23% always-follow to 97% median; depends on whether cues are shown or retrieved, and on averaging versus individual classification (K07).
- TTB beats regression (a02, a27, a07) versus regression slightly ahead on 63 data sets (a18) versus reversal with more data (b01). Not a contradiction in kind, but the headline "beats optimal" is not stable. Differences are 0.3-0.4 points.
- Katsikopoulos 2010 (less-is-more frequent but small, about 0.01-0.02) versus Goldstein & Gigerenzer 2002 (original condition assumes perfect memory) versus Pohl (max 26.3% in theory, 0.3% to 3.5% observed).
- Chain-of-thought: Sprague and Liu say CoT helps symbolic tasks and hurts some others; Liu's feature-aggregation task (c21) shows CoT helping strong models on weighted-sum choice, which fits "use the compensatory rule when the environment is compensatory", yet Llama 3.1 70B collapsed (42 to 6%).

## Weak spots
- Almost all positive TTB evidence is from the founders' own simulations on the same 20 data sets, many of them small and chosen by them.
- The LLM link is by analogy. The only direct test (Bogdan) is a single-author preprint where the frontier-model effect is directional only, regimes are assigned by item category, and the scoring is abstention on unanswerable items.
- No LLM study tests a TTB or tallying prompt. K18 rests on one search log.
- CoT-harm studies (Liu, Gema, Bogdan) use synthetic or narrow tasks and 2024-2025 models.
- FrugalGPT, Chen overthinking, Ross & Lo use "frugal/heuristic" loosely; only the stop-at-sufficient shape matches.

## GAPS
1. Does a take-the-best style prompt (ordered checks, stop at the first decisive one) beat a weighted-sum prompt and plain direct answer for an LLM at equal tokens on cue-based judgement items? No study exists; this is the key experiment.
2. Where does the crossover sit for an agent: how many past S0-class cases are needed before a learned stop-early rule beats the full routine (Parpart: about 20 versus 100 pairs for humans' data)?
3. Can a cheap class test (maths/symbolic yes-no, or Knightian versus definite) route items to direct or deliberate mode, and what routing accuracy is needed for a net gain at equal tokens (Sprague, Liu, Bogdan)?
4. Does Bogdan's CoT-length penalty replicate independently, on frontier models (Claude, GPT-5-class) and with unanswerable-versus-answerable items matched, in another lab?
5. Is familiarity/recognition in an LLM a valid cue? Measure LLM "recognition validity" (does the model know the entity) and whether answers follow it when other cues contradict (noncompensatory versus compensatory).
6. Does a fast-and-frugal tree built from an S0 class record match the full routine on held-out items (FFTrees reported 0.83 vs 0.83 on small sets, authors' data)?
7. What does the original Gigerenzer & Goldstein 1996 Table 2 and Glockner & Broder 2011 classification actually say (unverified here)? Needed before quoting them.
8. Do equal-weight/unit-weight combinations of multiple sampled answers or checks match fitted weights for LLM ensembles (Dawes analogue), and at what sample sizes?
9. Is there independent replication of the DeMiguel 1/N result and of cascade stop-at-sufficient gains (FrugalGPT) with 2025-2026 models and prices?

## Gap search results (evidence_d.jsonl, d01-d19)

Search note: the WebSearch quota ran out partway; OpenAlex and Semantic Scholar were rate-limited. Most papers were opened through direct arXiv or publisher PDFs. Scratch PDFs are on D:/research_scratch/E18.02/d.

**Corrections applied to the record**
- Gigerenzer & Goldstein 1996 Table 2 is now read (d01). TTB .658, weighted tallying .658, regression .657, tallying .656, weighted linear .623, unit-weight linear .621, Minimalist .647, Take The Last .645. The regression in that table was fit in-sample on all city populations, so "ties" is the right word, not "beats". Earlier a02/a03 figures stand but gain this caveat.
- Glockner & Broder 2011 is now read (d03, d04). N = 80 classified; PCS 62 (77.5%), TTB 12 (15%), RHe 4, RHe/TTB 2. Cues were shown on screen, 120 US-city comparisons. Process fit of TTB users was poor (time contrast significant for 25% of them, PCS 61-71%).
- Dawes 1979 is now read (d05). Table columns are garbled in extraction, so only the pattern and the Libby example (74% officers, 72% their models, about 78% proper models, 80% for one ratio) are quoted.
- Still to apply in b01-b03 and b10: the Parpart/Jones/Love author fix and the Pachur individual-level r meaning, and the Liu 2024 Claude 3.5 Sonnet exception. Those evidence files were not edited.

**Gap status**
1. TTB prompt versus weighted-sum prompt versus direct at equal tokens: OPEN. About 12 arXiv queries and one web search found no such study (d19). Nearest: a unit-weight LLM checklist (d06).
2. How many past cases before a learned rule beats the routine: PARTLY CLOSED. Random Rule Forest shows a crossover near 100 positives for unit-weight versus fitted weights (d07), in line with Parpart's 20-100. Not tested for a stop-early rule, and positives rather than total cases are the unit.
3. Routing by a cheap class test: STILL OPEN for the needed accuracy. Routers exist and cut tokens 41-76% (d12, d13, d16) but none reports the routing accuracy needed for a net gain. Simple break-even, derived here and not from a source: with misroute rate m, accuracy lost per item sent to direct wrongly L (12 points on MATH-500, d13) and accuracy gained per item correctly sent to direct G (about 0 there, since the tokens are the gain), routing pays at equal accuracy only if m x L stays below the accuracy value of the tokens saved. At L = 12 points, a 10% misroute rate costs about 1.2 points overall. This must be measured on our items.
4. Bogdan 17.3-point penalty replication: PARTLY CLOSED in direction. Two other labs show reasoning models run longer and abstain worse on unanswerable or missing-premise items (d14, d15). The size, the frontier models and the Knightian items are not replicated.
5. Familiarity as an LLM cue: PARTLY CLOSED for validity, OPEN for use. Popularity predicts accuracy (r about 0.4 for davinci-003) and gates retrieval well (d09); an internal known-entity signal is causal for refusal (d10); familiarity predicts belief stability (d11). No study pits familiarity against contradicting cues.
6. Fast-and-frugal tree from an S0 class record versus the full routine: OPEN. No new evidence found.
7. GG96 Table 2 and Glockner & Broder: CLOSED (d01, d03, d04).
8. Equal weights for LLM ensembles: PARTLY CLOSED. Unit-weight checklist (d06, d07) and equal-weight model pooling (d08) both support equal weights, but pooling did not beat the best single model, and same-model sampled answers were not tested. Dawes opened (d05); Dana & Dawes 2004 still unopened.
9. DeMiguel 1/N and FrugalGPT replication: FrugalGPT PARTLY CLOSED (d16-d18: 40% of GPT-4 cost, -31% cost, +8-12% over prior routers), but all are 2023-2026 small or mid models and not at 2026 frontier prices. DeMiguel stays OPEN: the publisher page returned only navigation text and the faculty PDF link redirected away.

**New weak spots**
- RRF is one team's framework with margins not separable at founder level; do not cite it as proof that counting beats weighting.
- The vLLM router's +10.2 points may reflect a weak baseline mode.
- The silicon-crowd result shows pooling can lose to the best member (GPT-4 .15 versus crowd .20 Brier).
