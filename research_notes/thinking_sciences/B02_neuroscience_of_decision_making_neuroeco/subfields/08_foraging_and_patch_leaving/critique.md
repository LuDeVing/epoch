# B02.08 Foraging and patch leaving: cross-check critique

## Numbers re-opened this session (10)
1. Kolling 2012 t(17)=-2.54, p=0.021 (PMC3440844): CONFIRMED. The page text still gives no N. df 17 is a slope comparison and may not equal N-1, so "about 18 participants" stays an inference. Do not cite N=18.
2. Shenhav 2014 Exp1 indifference RVforage=1.65, SE 0.26, t(14)=6.5, p=1.4e-5 (PMC4156480): CONFIRMED.
3. Shenhav 2014 Exp2 indifference 5.0, SE 1.3, t(13)=3.9: CONFIRMED.
4. Shenhav difficulty t(13)=2.8, p=0.014 vs foraging value t(13)=0.47, p=0.64: CONFIRMED (df 13 means the N=14 sample). The rho=0.80 is an average Spearman, t(14)=14.1, for Exp1; a08 and b02 are consistent. a08 wording "Exp2 rho=0.07" was not re-checked.
5. Lacosse 2026 switch ratio 0.55 human vs 0.40 LLM, 699 sequences, 681 human and 2285 LLM kept, Spearman 0.701, probe AUROC 0.57 vs 0.751: CONFIRMED (arXiv 2603.01822 text). Note: LLM sequences were generated to match the human count (699), so the 2285 is after pooling four model sizes.
6. Leckie 2026 steering Gemma-2-9B 0.29 -> 0.70 / 0.07: CONFIRMED (text of 2609.35599). r>=0.31 not re-verified line by line.
7. Wispinski +15.8 steps SE 2.7 (p<0.05) and +0.9 SE 2.8 p=0.74 (t(11)=0.34), N=12 agents, 3 per discount rate: CONFIRMED.
8. Krishnamurthy 2024: more than 60 percent of GPT-4 basic-prompt replicates had suffix failure: CONFIRMED. The c17 line says "chose the best arm only a handful of times" which is the paper's description of the same bimodal group. Not a conflict.
9-10. Not re-opened (no free full text reachable or quota): Hayden 2011 (2.2 s overstay, beta 1.247), Constantino and Daw 2015 (9-10 percent), Harhen t(115)=3.88, Kane 2019/2022. They carry opened:true from the earlier agents, but this cross-check did not re-verify them. Treat as single-pass.

Corrections: none to the numbers above. One wording fix: a05 "likelihood ratio 1.31e52" is odd for a strong claim and was not re-checked; do not quote it.

## Contradictions and tensions
- Kolling 2012 (dACC = foraging value) vs Shenhav 2014 (dACC = difficulty) vs Kolling 2016 (reply, under 2.5 percent shared variance). Unresolved; the two designs differ. Not needed for our agent.
- Evidence a16 (Webb) gives 17,877 patches in one place and 14,060 in the discussion; counts disagree inside the paper or the summary. Low impact.
- Mice: leave rate tracks own average rate, difference not significant (b14), while heuristics match MVT at low stochasticity (a25). Both fit "MVT is hard to tell from a constant timer".
- Bayesian vs MVT winner flips with setting (baboons, mice). K04 is therefore contested.
- Overstay: monkeys, humans and rats overstay; the gerbil study found that only some humans did (a13), and rich environments show none (a12). So "all foragers overharvest" is a tendency, not a law.
- b04 duplicates a04, b01 duplicates a01, b17 duplicates c09, b18 duplicates c01, b21 duplicates c17, b23 duplicates c10, b24 duplicates c14, b07 duplicates a12. Independence counts in claims.jsonl count papers, not lines.

## Weak spots
- Zero direct LLM tests of patch leaving with a depleting reward. All LLM evidence is indirect: semantic fluency (two small-model workshop or preprint papers, Llama-3 and Gemma 2B-9B, animals only), bandits (older models), retrieval-agent design (foraging as metaphor).
- Several 2026 arXiv items (Leckie, Lacosse, SCOUT, LLM-Foraging, Kilpatrick 2026) are unreviewed preprints, mostly read only in the front pages.
- Founding sources (Charnov 1976, 1973; Stephens and Krebs) not opened. Charnov rule is taken from secondary papers.
- c10 InForage table columns were scrambled in extraction; do not quote the benchmark pair. SCOUT score columns not tied to a named task.
- c12 DeepNews: one author, one outlet, "knowledge cliff" is weak.
- Only seen in snippets: Marshall 2013 baboons (c23), bioRxiv 2025 stochastic choice (c22; a14 appears to be the same work read in full), Hutchinson 2008, Hills 2012 (a20, a22 numbers not read).
- c25 to c28 are synthesis by an earlier agent; they are claims here, not evidence.
- Search: web-search quota ran out for earlier agents; "no LLM test exists" rests on arXiv listing pages only.

## GAPS
1. Does an LLM agent that stops an operator when its recent yield falls below its running average beat fixed-step and sufficiency stops at equal tokens? (No test exists; this is the S6 core.)
2. What is the right yield measure for a reasoning step (new verified facts, new constraints, answer-probability change), and is it cheap enough to compute inside the token budget?
3. Is the best threshold slightly more patient than the average rate (as the discounting and uncertainty accounts imply), and how large is the margin when the yield signal is noisy?
4. How does the optimal stopping rule change with how noisy and variable the yield is (Kilpatrick's roughly 25 percent variability switch between counting and timing)? Which regime do hard reasoning items fall in?
5. Does giving the model an externally computed yield statistic fix overstaying, as the bandit results suggest, or does the model ignore the number? Test with and without.
6. What does the travel cost (cost of switching operator, losing context) look like in a scaffold, and does a higher cost lengthen stays as MVT predicts?
7. Can a memory of earlier yields per operator (a prior over environment richness) cut overstay the way experience cuts it in humans (Harhen 2023)?
8. Are the semantic fluency results (LLMs switch less than humans; internal supply predicts switching) reproducible with frontier chat models and tasks beyond animal names?
9. Is the human "bias against searching" present in LLM agents, and does it differ by model or prompt?
10. How much of the overthinking literature (reasoning models on easy items) is the same stopping problem, and do its fixes match an average-rate trigger?

## Gap search results (evidence_d.jsonl, d01-d18)

Search conditions: arXiv API, Semantic Scholar, OpenAlex and dblp were rate-limited (429); Crossref worked but returned little. Web search worked for one query. Most papers were opened by direct PDF download from arxiv.org and read with pdftotext. Absence claims are therefore weak.

1. LLM average-rate leave rule vs fixed-step and sufficiency stops: STAYS OPEN. Closest: Zhang 2025 (d04) probe-based exit beats a fixed-step exit at equal tokens (87.4% vs about 82.5%), but it is a level rule. DEER (d02) and answer convergence (d03) are sufficiency stops. Nobody tests yield-below-average.
2. Yield measure: PARTLY CLOSED. Cheap candidates exist: change in the probed answer (d03), trial-answer confidence (d02), probe score (d04, open weights only), marginal coverage per sample (d10). Which is best is untested.
3. Threshold patience: PARTLY CLOSED in theory (d13: longer stay when yield only falls, shorter when payoffs can rise). No LLM margin measured.
4. Noise regime: OPEN. d05, d07 show hard items are under-stayed and easy items over-stayed; no variability switch measured. Kilpatrick's 25 percent figure still has no LLM counterpart.
5. External yield number: PARTLY CLOSED. d11: handing statistics helps larger models (Pro 45.5 to 60.0) but stays far below UCB (90.6); small Gemma models did not gain. d12: tool use helps. Not tested on stopping.
6. Switching cost: PARTLY CLOSED. d14 (agents) and d06 (thought-switch penalty) show higher cost, longer stays, and gains on hard items. No scaffold test of context loss.
7. Yield memory as prior: OPEN. Nothing found in LLMs; only the human result (Harhen, not re-opened).
8. Fluency on frontier models: OPEN (d17: Llama-3 and animals only).
9. Bias against searching in LLMs: OPEN. Indirect only: d15 shows LLMs divest alone but escalate in groups; d16 shows sunk-cost answers mostly rational.
10. Overthinking literature as the same problem: CLOSED as a mapping, with a twist. d01-d04, d08 show the overstay; fixes are sufficiency or confidence exits, not average-rate triggers. d05-d07 show the opposite error (underthinking) on hard items, so any rule needs a dwell floor.

Claims changed: K17 raised to established (6 sources); K14 and K15 extended; K20-K26 added. Earlier caveats stand: do not cite Kolling N=18; Hayden 2011, Constantino and Daw, Harhen 2023 and Kane rat studies remain single-pass. Limits of this pass: DEER and Su tables only partly read; d12 read abstract and introduction only; Barkett model names not captured.
