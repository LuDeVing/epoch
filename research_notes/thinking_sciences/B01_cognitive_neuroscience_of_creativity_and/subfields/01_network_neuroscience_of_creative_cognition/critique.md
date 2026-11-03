# Critique: B01.01 Network neuroscience of creative cognition

## Corrections made (sources re-opened this session)
Re-checked against full text: Beaty 2018 PNAS (PMC5798342), Beaty 2015 (PMC4472024), Kenett 2025 (PMC11733278), Cogdell-Brooke 2020 (PMC7643395), Si 2024 (arXiv 2409.04109), Yao 2023 (arXiv 2305.10601), Ismayilzada 2026 (arXiv 2604.03480).

Confirmed unchanged: 224/603 edges; r(161)=.30 (P=1.29e-4) and .22; external r(37)=.35, r(52)=.28, r(403)=.13; r=.44 p=.02 N=25 (Beaty 2015); N=2433 over 10 samples with inverted U (Kenett); Si novelty 4.84/5.64/5.81, feasibility 6.61/6.34, 4000 ideas to about 5% non-duplicate, reviewer agreement 56.1%; ToT 7.3/4.0/9.0/45/74% and creative-writing 6.19/6.93/7.56.

Corrections and notes:
1. a25: the two LLM-brain correlations (size r=.55, AUT score r=.52) come from DIFFERENT pooling strategies (last-token vs mean-token); each is weaker under the other. The AUT correlation depends on the smallest model (Gemma-3 270M): dropping it gives DMN r=+0.40 (FPN +0.46 to +0.29). Treat as fragile.
2. a16/b06/b07: the low-creative network did replicate in the large rest sample (r(403)=.11, P=.03). The paper's Steiger test found high vs low network not significantly different. "Low network failed" should read "weaker; replicated in 1 of 3 external samples".
3. b11: Cogdell-Brooke reports 162 foci in 19 experiments in one place and 127 foci in 19 experiments in another. Internal inconsistency; rely on 596 participants and 20 studies only.
4. c04: ToT's 74% needs GPT-4 (GPT-3.5 gives 19%). The bottleneck was generation (GPT-4 gen + GPT-3.5 eval 64%; reverse 31%), which weakens a "control phase is what matters" reading.

## Contradictions between sources
- Coupling (Beaty 2014/2015/2018; Kenett 2025 switching) vs differentiation (2025 gradient study: achievement tied to more separation of control and default). Samples and measures differ; unresolved.
- Default network as the engine (Beaty 2016 model) vs meta-analysis (Cogdell-Brooke: largest overlap is semantic control network) vs Dietrich and Kanso 2010 (nothing reliable beyond diffuse prefrontal).
- Executive network attenuated during generation (Liu 2015 poetry) vs executive active from window 2 in the AUT (Beaty 2015). Task type may decide.

## Weak spots
- Founding studies are small: N=25, 12 per group, 27, about 35, 24. Marek 2022 says brain-behaviour effects at n about 25 are inflated. Only Kenett 2025 (N=2433) and Beaty 2018 (N=163 plus 3 replications, r .13-.35) are well sized, and effects are small.
- Beaty 2018 data are reused in Ismayilzada 2026: not independent.
- Creativity scores often come from a separate session (Beaty 2015), not the scanned trials.
- No study tests the two-phase idea on an LLM with a neural-style control. All LLM "support" (ToT, multi-agent, NeoCoder) is indirect.
- Statistics: 2015 MVPA at p<.001 uncorrected; only the precuneus survived FWE in the 2017 constraint study.

## Seen only in snippets or abstracts
a12 (Ellamil), a15 (Madore), a20, a21, a22 (Wu ALE), a23, a24 (abstract-level); b04, b05 (review-table level); b16 (Lloyd-Cox, page 403); b22 (Summers-Stay, as cited); c18, c19, c20 (via the 2026 review); c25, c26 (not opened in stream C). Claims K09, K19 and K08 rest partly on these.

## GAPS
1. Does a separate generate pass plus a separate control pass beat one-pass generation at EQUAL tokens on creative tasks (AUT, NoveltyBench)? ToT and LLM Discussion do not hold tokens equal.
2. What is the best number of generate/control alternations? Kenett's inverted U suggests a middle value; no LLM test exists.
3. Does "inhibit the obvious" (discard the first k answers, which are the repeated ones) raise novelty beyond the saturation effect (5% unique at 4000 samples)?
4. Can a model judge its own ideas? Si 2024 judges are near chance (53.3% vs 56.1% human). Does an external check (executed code, retrieval) repair the control phase?
5. Is human "control" better modelled as semantic control (retrieval of weak associates) than as evaluation, as Cogdell-Brooke suggests? Which LLM operator matches?
6. Which network result survives large preregistered replication (coupling vs separation; salience-first then executive time course of Beaty 2015)?
7. Does creativity post-training (CrPO) change internal representations as Ismayilzada reports, with controls for pooling and model size?
8. Does cross-model homogeneity (similarity above 0.8) persist under persona, decomposition or rare-fact retrieval scaffolds, and at what token cost?
9. Do the results hold for non-AUT tasks with a correct answer (insight problems, design)?


## Gap search results (gap searcher, 2026-11-03; evidence in evidence_d.jsonl, d01-d17)
Tool limits this run: arXiv, OpenAlex and Semantic Scholar APIs returned 429 or no budget; only 2 useful web searches. Sources were opened as arXiv PDFs (VS, Sen 2026, Gacha, Nova, CresOWLve, IMO pipeline) and Europe PMC abstracts (Lloyd-Cox, Beaty 2021, Sunavsky, Marek). Brain items are abstract-level only.

1. Equal-token generate pass plus control pass: STILL OPEN. VS (d01, d17) controls compute and its CoT variant gives the best diversity-quality point, but it is not a generate/critic split. IMO verifier (d10) is not token-matched. No direct test found.
2. Best number of alternations: STILL OPEN. Only weak signal: Nova (d07) gains flatten at step 3 without planning (44.1 vs 42.4). No LLM sweep.
3. Inhibit the obvious beyond saturation: PARTLY INFORMED, open. Nova shows retrieval planning gives 3.4x unique ideas; Gacha (d06) 4.7x-11x fewer samples. VS (d02) Sequence listing helps modestly. No discard-first-k experiment. Typicality bias (d03) gives a reason it should work.
4. Can a model judge its own ideas, does an external check help: SPLIT. For correctness, a same-model verifier loop works (d10, d11: 85.7% vs 21-38%). For novelty ranking no repair found; Si 2024 near chance stands. External checks for creative ideas untested.
5. Human control as semantic control, matching LLM operator: PARTLY CLOSED. CresOWLve (d09) shows LLM failures are missing links, not missing facts; retrieval planning (Nova) helps ideation. So the matching operator is forced cross-cluster linking plus outside retrieval, not extra evaluation. No direct human-LLM mapping test.
6. Surviving network result: PARTLY CLOSED. Coupling replicated at n=171 (d13); pre-registered IFG-IPL predictor (d14). Salience-first order is NOT supported: Lloyd-Cox (d12) finds executive already above default early; K03 downgraded to contested. Coupling vs separation (K07) unresolved; no large pre-registered study. Marek (d15) supports caution.
7. CrPO changes internal representations with controls: NOT RESEARCHED (no source reached). Stays open.
8. Cross-model homogeneity under scaffolds: PARTLY INFORMED, open. VS and Gacha raise diversity within one model with token numbers (d01, d06); cross-model similarity under these scaffolds not measured.
9. Tasks with a correct answer: PARTLY CLOSED. CresOWLve (d08) and IMO (d10) show extra thinking or verification helps on checkable tasks; gap is in the associative leap.

New claims K22-K28 added; K03 set to contested; K08 set to established (Marek read); other claims got extra evidence ids. All new evidence is arXiv preprints from the same period, mostly authors' own evaluations.
