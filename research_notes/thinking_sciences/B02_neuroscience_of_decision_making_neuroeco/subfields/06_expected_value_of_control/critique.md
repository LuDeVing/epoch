# B02.06 Expected value of control: cross-check and critique

## Numbers re-opened (local text copies in D:/research_scratch/B02.06 of the cited papers)
Confirmed unchanged: Kool 2010 (0.68 low-demand choice, 36/43); Kool 2013 (t(49)=4.60; r(48)=-.38; -.49); Fromer 2021 (reward and efficacy b values for Studies 1-2, CNV interaction -0.35 p=.046); Strobel 2020 (N=217); Maekela 2023 (N=663; r=.168, .176, .085; retest r=.537); Job replication (N=60 vs 187); RaM Table 1 (47.4/222.7, 50.1/170.8, 61.9/215.1, 63.5/146.2); RaM MMLU-CF (27.0 to 29.5; 40.2 to 36.4); Chen (1,953%); Zhou 2026 AIME curve (37.8, 46.5, 53.8, 55.8, 54.9); Arora and Zanette (16%/-3.3, 37%/-2.2, 65%/-1.7); Snell (about 4x).

## Corrections
1. c08 (Zhai 2026) is misleading as written. "At average budget 3.0, +5.8 points" compares learned (0.575 at realised cost 2.73) with Fixed-b (0.517 at cost 2.00, because fixed budget is capped at a grid value). A random allocator at cost 2.98 got 0.534. The equal-cost gain is about 4.1 points, still real. Use cost-matched comparisons only.
2. b18/c10 (Chen): ">92% of cases first round correct" is the paper's overall statement; the figure shows per-set values of roughly 89% to 97%. Quote as range.
3. c24 URL points to the MGV paper (2511.04341), not Lieder 2018; the entry was never opened. Treat as unverified.
4. a12/b03 text had an encoding glitch in the author name (Fromer); no numbers affected.
5. Duplicates: a24/a25, b16/b17, c01-c03 are one paper (De Sabbata); a12/a13 and b03/b04 are one paper (Fromer); a18/b01 repeat Shenhav 2013. Independent counts in claims.jsonl reflect this.

## Contradictions between sources
- Efficacy x reward interaction: Fromer Study 1 p=.116 (null), Study 2 p=.009 (present). Not stable.
- Trait link: Kool 2013 r=-.38 (N=50) vs Strobel 2020 and Maekela 2023 (weak or absent). Demand avoidance has poor retest (.54) but COG-ED good (.80), so the two tasks measure different things.
- Ego depletion (strong-resource cost) fails in replications, yet cost of control is still supported through choice data; the cost is probably opportunity or computed, not fuel (Kurzban).
- LLM side: length penalties save tokens but sometimes lose accuracy (c26) while DEER and AdaptThink report accuracy gains; these differ in method (training-free early exit vs trained penalty) and benchmarks, so no clean comparison.

## Weak spots
- Almost all human EVC data are small samples (N=21, 44, 35, 32, 22, 15), many from one lab (Shenhav).
- Hagger 2016 and Vohs 2021 (b12, b13) were recalled, not opened. Do not cite numbers.
- Kouneiher 2009, Kolling 2012/2014, Westbrook 2013 original paper details (a21, a22, b22, b23) not opened or second-hand.
- Bustamante 2021 and Callaway 2022 (a20, a28), Lieder 2017, Musslick 2015, Inzlicht 2018 and Kurzban 2013 (b14, b15) were not opened.
- de Varda 2025 (human RT vs reasoning tokens) only seen as a news piece (c23).
- No meta-analysis of incentive effects on control (b25). Search quota ran out during the A/B passes.
- LLM studies mostly use maths benchmarks, 1.5B to 32B open models; nothing on agentic or open-ended tasks. Nobody tests the EVC form (payoff and efficacy both varied) on an LLM.

## Seen only in snippets
a20, a21, a22, a26, a27, a28, b12-b15, b22-b25, c21 table figures, c23, c24.

## GAPS (most decision-relevant first)
1. Does a stated token price or reward in the prompt (no training) shift an LLM's thinking length by difficulty the way RaM training does, at equal total tokens?
2. Do LLMs show the efficacy effect: does telling the model its extra thinking will or will not change the outcome change its allocation (Fromer design, run on an LLM)?
3. What is the knee of the accuracy-versus-thinking curve per difficulty bin for our own agent, and does a stop rule at the knee beat fixed depth at equal tokens?
4. What are the cost-matched gains (not nominal budget gains) of learned or difficulty-routed allocation over random allocation, across Zhai, Damani and Snell?
5. How reliable is difficulty prediction before thinking (the input to any EVC rule), and what does a wrong prediction cost (the Luo 2025 prefix-dominance trap, about 20% loss, unopened)?
6. Hagger 2016 and Vohs 2021 ego-depletion numbers: open and verify, to settle whether the cost term can be modelled as fuel.
7. Is there a human or LLM study where the payoff term was misjudged (overconfident value, Bustamante 2021 over-exertion) and how does it compare to LLM overthinking?
8. Do effort-discounting choice tasks (COG-ED style) on LLMs exist anywhere (2024-2026)? Search again with a working search tool.
9. Does the per-step (within-chain) budgeting of HAB beat per-problem budgeting at equal tokens, with exact table figures?
10. Is the effort paradox (effort valued) relevant to LLM scaffolds, e.g. does forcing a verification step raise answer quality beyond its token cost?

## Gap search results (evidence_d.jsonl, d01 to d21; claims K03, K07, K13, K14, K16, K18 edited, K19 to K26 added)

Status: 2 closed, 5 partly closed, 3 still open. 18 of 21 new lines were opened (d19, d20 are search records; d21 is a search summary only).

1. Stated token price or reward in the prompt, no training (OPEN). Only a stated length budget has been tested: TALE-EP (d17) scales output with difficulty (about 40 tokens on arithmetic, about 260 on college maths, -68.6% tokens, -2.7 points). No random-length control at equal tokens, no price or reward framing (d20). Run it on our agent.
2. Efficacy effect in LLMs (OPEN). No study found (d20). Same cheap prompt test as gap 1.
3. Knee per difficulty bin (PARTLY CLOSED for other models, OPEN for ours). For a 7B distilled model the knee is at the smallest tested budget (256 tokens) on GSM8K and MATH-500; on AIME 43.5% of chains never finish and score 11.5% (d12). Caveat: n = 200 per set, low uncapped GSM8K accuracy (0.74) hints at extraction artefacts. Stop rule vs fixed depth at equal tokens for our agent is unmeasured.
4. Cost-matched gains (PARTLY CLOSED). Damani is matched to uniform at equal average budget but needs an oracle verifier, and the 25 to 40% chat figure is a high-variance subset (d08). Snell's 4x leaves out difficulty-estimation cost (2048 samples per problem for oracle bins) and holds at low budgets (d09). Brown 2026 gains vanish above about 96 to 128 tokens per query (d07). Zhai's 4.1 points against random remains the only random-allocator comparison. Treat all nominal-budget gains as upper bounds.
5. Difficulty prediction reliability and cost of a wrong call (PARTLY CLOSED). Reliability: question-only AUROC 0.83 to 0.88 (Bulut, d06); two-class accuracy 72 to 84% (Damani); 3-class 66.3% against a 58.7% majority baseline (Brown); early thinking signals add nothing beyond difficulty. Cost of a wrong call: the Luo 2025 "about 20%" is a forced-prefix result on 10 failed AIME questions per model, not the cost of choosing a wrong strategy (d04, d05); the MGV paper's wording is wrong. A real cost-of-wrong-allocation measurement still does not exist; Brown's crossover is the only indirect evidence.
6. Ego depletion numbers (CLOSED). Hagger 2016: 23 labs, N = 2,141, d = 0.04 [-0.07, 0.15] (abstract level only). Vohs 2021: 36 labs, 3,531 tested, d = 0.06 [-0.02, 0.14], BF about 4.4 for the null, only fatigue moderated (read through a fetch summary of two thirds of the text). K07 upgraded to established: do not model cost as fuel.
7. Misjudged payoff (PARTLY CLOSED). Bustamante 2021 opened: N = 30, over-exertion persists after 40 trials (d14). LLM side now has both directions: overthinking (Chen) and reduced effort on the hardest puzzles (o3-mini peak near size 100, d15); underthinking numbers (d21) are search-summary only. No study compares human and LLM misjudgment directly.
8. Effort-discounting tasks on LLMs (OPEN). Three more searches, none found (d19). Looks like a real hole; we would have to run a COG-ED style test on our agent.
9. Per-step vs per-problem budgeting (PARTLY CLOSED). HAB tables extracted (d10): no ablation isolating the per-step budget, MATH500 test set only 78 items (2 questions separate HAB from CoT), and a fixed setting matches HAB on GSM8K at 18% fewer tokens. TAB (d11) beats uniform per-turn budgets with 40% fewer tokens at equal accuracy but was not compared with per-problem allocation. Unproven either way.
10. Effort paradox and forced verification (CLOSED for LLM scaffolds, negative). Forced self-critique and reflection lose to repeated sampling at equal tokens, 18 of 18 comparisons negative (d16). K18 rewritten.

New caveats found while checking: HAB's reported gains rest on 78 test items; TALE's abstract and Table 3 disagree (80.22% vs 81.03%); Snell's difficulty bins use ground truth in the oracle condition; Mirzaei, Bulut, Oladri, Jali and Kassenaar are 2026 preprints by small teams and not yet peer reviewed. Sources not opened: Wang underthinking paper (summary only), Hagger full text, last third of Vohs.
Tool notes: Semantic Scholar and OpenAlex APIs were rate-limited; the Berkeley Hagger PDF and Minnesota Vohs PDF links returned error pages, so Hagger was read at abstract level via a repository record.
