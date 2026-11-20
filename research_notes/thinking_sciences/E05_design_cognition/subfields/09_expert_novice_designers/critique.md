# Critique: Expert-novice designers (E05.09), cross-check

## Numbers re-checked against the saved source text (D:/research_scratch/E05.09)
Confirmed: Lawson block task (3x4 bays, over 6000 answers, hidden rules; How Designers Think text); Ball et al. 2004 (32.2 vs 22.9; F(1,14)=5.04, p=.041; 53.1/11.3 vs 16.5/29.4; F=31.24); Morozov et al. 2007 (1418 segments, 124 novices, 11.5 vs 57 statements, 77% first-pass agreement, mean 19 years); Wadinambiarachchi 2024 (GenAI .32, Bayes Factor 124, Image Search .27, rho .56, 277 sketches); Ege et al. (37.66 m, 14.8 m, 6.56 m, 116 prototypes); Chen, Chen, Yang 2022 (976 s vs 446 s, p=.03); Chen et al. 2025 (67.4% vs 78.2%, 208.57 vs 142.71, 16.2509 vs 16.0503); Zhang et al. 2025 (31.7 vs 16.3 formulation; PS 6.7 vs 10.5; SS 9.9 vs 29.4, t=-8.949); Perisic et al. 2019 (steps 290.7/379.6, 316.2/494.7).

## Corrections
1. a20 "expert design detail 30 to 51 percent versus context 49 to 70 percent" is a per-expert range. The group totals in Table 7 are 46/54 (experts) vs 48/52 (novices), so there is no group difference. b09 is right; read a20 with it.
2. a24 "about 2 frames in 23.25 minutes per participant" is the manual condition only (direct 21.82, structured 28.35, free-form 20.78 minutes). "Four conditions" counts manual plus three LLM ways. Also the abstract says inexperienced users felt lower agency with LLMs; a24 says agency did not drop overall. Treat as: no overall drop, lower for novices.
3. a25 source name "Gold-affiliated authors" is wrong. The paper is Guo, Yin, Sun, Chen (2024), DRS2024, doi 10.21606/drs.2024.983. Claims use the id only.
4. Wadinambiarachchi fixation CI upper bound is .54 in one place and .55 in another in the paper. Immaterial.
5. a01 and b01: the Lawson group sizes and significance remain unknown. The first-year replication claim rests on Cross and Lawson's book text, not the 1979 paper.
6. a17 (Atman 2007 sample: 19 experts, 26 freshmen, 24 seniors) was seen only in search-result abstract text; it matches my recollection of the paper but is not re-opened here.

## Contradictions between sources
- Cross and Lawson say experts are solution-focused; Kruger and Cross and Lemons say problem-driven designers do better. These are compatible only if "solution-first" describes common expert habit, not the best strategy. Still unresolved (K03, K19).
- Chen et al. 2022 finds almost no expert-novice process difference, while the older protocol literature reports many. N is 4 vs 5, so it cannot overturn them.
- Morozov: experts are said to scope more broadly, but the mix data show no group difference; only volume differs.
- Shin et al. 2025 (no LLM benefit for reframing) vs Zhang et al. 2025 (style prompts raise novelty and integrity). Different tasks, raters and baselines.

## Weak spots
- Almost every human expert-novice number is from tiny samples (N=2, 4 vs 5, 8 vs 8, N=10, one team vs one team) or from reviews that give no N.
- No true failed replication of the original Lawson result was found. The first-year null is a different population, not a replication.
- LLM studies use one model family (GPT-4, GPT-4o, Midjourney) in 2024-25; none tests current frontier reasoning models.
- Ege et al. is a single team in a single event; the "fixation" label is the authors' reading of prompts.
- Zhang et al. 2025 N is 10 runs per cell; the check that the model follows a style is by their own index.
- LLM raters (c19) are weak but are used in several designs.

## Only seen in snippets or unopened
a01 (original 1979 paper), a16, a17, b06 (Kruger and Cross 2006, numbers second-hand via Lemons), b21 (Mehalik and Schunn, via Lemons), c28 Dorst and Cross 2001, c29 Maher and Tang 2003, c30 Jiang, Gero and Yen 2014. Lloyd and Scott 1994/95, Christiaans and Dorst 1992, Atman 1999, Jansson and Smith, Smith and Tjandra are known only through Cross (2001/2004) summaries with no N.

## GAPS
1. Does forcing an LLM agent to write a candidate solution first, then derive constraints from its failures, beat a constraints-first order at equal tokens on hidden-rule tasks (a direct Lawson replication on a model)?
2. What are the actual group sizes, scores and significance in Lawson (1979) and Lawson's later block-task follow-ups with professionals?
3. What are the effect sizes in Kruger and Cross (2006): how much better is problem-driven than solution-driven design, and does it hold for ill-defined briefs?
4. Is there any study of frontier reasoning models (2025-26) on design fixation or problem-solution co-evolution, rather than GPT-4o and Midjourney?
5. Does a pivot rule (persist k tries, then restart) fix the "abandons after one setback" failure of Ege et al., and is it replicated beyond one hackathon?
6. Does a memory of abstract schemas (the expert pattern in Ball et al.) improve an LLM agent more than a memory of concrete cases?
7. Does forced alternation of problem and solution steps (the human co-evolution pattern missing in Zhang et al.) raise design integrity at equal tokens?
8. Are there larger-sample human expert-novice studies (N of 30 or more per group) that test the breadth-first claim?
9. How well do LLM judges track expert design ratings once calibrated, and can a calibrated judge serve as a stop rule?
10. Does problem well-definedness moderate whether solution-first or problem-first works better (Cross's claim)?

## Gap search results (evidence_d.jsonl, d01-d17)
Search budget: 8 WebSearch calls used; OpenAlex, Semantic Scholar and the arXiv query API all returned rate-limit errors, so arXiv PDFs and direct page fetches were used. Kruger and Cross 2006 and Lawson 1979 are behind Cloudflare or paywalls and were not opened.

1. Solution-first vs constraints-first at equal tokens on an LLM: STAYED OPEN. No direct replication found. Nearest work (d07, d08, d09) shows LLMs in hidden-rule loops mostly confirm their guess; counterexample prompts lifted discovery from 42% to 56% (11 LLMs); reasoning models 68-75% vs 33-41% on FalsifyBench. Added K20. The experiment in K01 is still the one to run.
2. Lawson group sizes and significance: STAYED OPEN (d06 second-hand only; no follow-up with professionals found).
3. Kruger and Cross effect sizes: PARTLY CLOSED. Sample is 9 designers (d01), no effect sizes found; abstract adds that solution-driven designers had higher creativity (d02). K03 updated.
4. Frontier reasoning models on fixation or co-evolution: STAYED OPEN for design (d13, d16 use old models). Closed only for hypothesis testing (d09, GPT-5.2). Added K24.
5. Pivot rule: PARTLY CLOSED. No replication of Ege et al., but TraceML (d12) shows pivot rates 25% human, 9% Codex, 58% MLEvolve without gain, and no returns to abandoned lines; Fail-Fast Restart-Smart (d11) shows restart works only with carry-over (71.8% vs 66.8% cold). Added K22.
6. Abstract schema vs concrete case memory: PARTLY CLOSED (d10). Abstract transfers across tasks (+6.5, +9.0 vs -9.5, -7.5); cases win within task. One backbone. Added K21.
7. Forced alternation of problem and solution steps: STAYED OPEN. Only d13 (LLM never reshaped the problem space) found.
8. Human samples of 30 or more per group: STAYED OPEN. Studer et al. (d03) has 252 problems but no expert-novice split; Atman counts unverified (d17). Added K25.
9. Calibrated LLM judge as stop rule: STAYED OPEN. Uncalibrated agreement is moderate (r = 0.50, d14) and blind to context; no calibrated design-judge study found (d15). Added K23.
10. Problem definedness as moderator: STAYED OPEN. Only the claim that experts treat well-defined problems as ill-defined (d05); Studer shows narrowing is common (d03, d04).
Other: a17 stays unverified (d17). Kruger and Cross N=9 is now confirmed second-hand, which strengthens the "small sample" warning on K03.
