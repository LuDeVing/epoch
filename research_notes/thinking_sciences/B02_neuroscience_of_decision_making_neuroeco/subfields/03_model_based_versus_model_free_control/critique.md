# Critique: B02.03 Model-based versus model-free control (cross-check)

## Numbers re-opened this session (confirmed)
- Daw et al. 2011 (PMC full text): median weighting 61% model-free, 39% model-based; reward p<1e-8, reward x transition p<5e-5; reward effect positive 14/17, interaction positive 10/17. Confirmed. (a07 finding text is truncated at "0.3"; the table value 0.39 is right.)
- Chen et al. 2024 overthinking (PDF text): 1,953% more tokens for "2 plus 3"; 39 of 901 tokens = 4.3%. Confirmed.
- Paglieri et al. (arXiv 2509.03581, PDF text): 0.387 vs 0.379 reward, 85% fewer output tokens (1,714 vs 11,510); SFT+RL 0.387 vs SFT 0.343. Goldilocks in Crafter and POGS, 100 seeds. Confirmed.
- AdaptThink (arXiv 2505.13417, PDF text): -53.0% length, +2.4 accuracy (1.5B); -40.1%, +2.3 (7B); lambda 0.1 row gives -64.5% length and -0.5 accuracy; 86.9/76.8/40.4 NoThinking shares. Confirmed.
- Momennejad et al. 2023 (arXiv 2309.15129, PDF text): GPT-4 0 of 30 at temperature 0, at most 10% at 0.5 or 1. Confirmed, but a26 dropped the scope: this is the "1 cluster away" task on dense community graphs only, not planning in general.

## Corrections
1. a21 gives the authors as "Otto, Skatova, Madlon-Kay, Daw 2015"; b13 gives Gillan, Otto, Phelps, Daw 2015 for the same finding (N=90, then 95). Gillan et al. 2015 is the right attribution. Count a21 and b13 as ONE source.
2. Dates: Paglieri et al. appears on arXiv in September 2025; b23 says 2025, c06 says 2026. Use 2025 (arXiv) and note the later version.
3. Duplicates that must not count as independent: b23/c06/c07/c08 (Paglieri); b22/c13 (AdaptThink); b25/c11/c12 (He and Feng); b24/c09/c10 (Ghoshal); a27/b18/c02/c03 (CogBench); a28/c04/c05 (Demircan); b26/c15 (SwiftSage); a26/b20 (Momennejad); a20/b11 (Gillan 2016); a10/b03/c20 (Keramati 2011).
4. b08 (Patzelt 2019) is titled "Incentives boost model-based control across a range of severity on several psychiatric constructs" (Biol Psychiatry). It tests incentives, not a strict replication of Kool 2016 cost-benefit; type "replication" is loose.
5. a20 and b11 report different Gillan 2016 coefficients (factor betas vs OCD beta -0.040). Both can be right (different models), but the replication sample is N=1413 per b11; a20 says only "independent sample".

## Contradictions and weak spots
- The central human fact is contested. Daw 2011 w=0.39 (N=17) vs story-instructed samples w=0.78-0.79 (N=21, 24; Feher da Silva and Hare 2020) and Castro-Rodrigues 2022 (instruction raises model-based use). The "hybrid" may be partly task misunderstanding. Feher da Silva numbers were NOT re-opened by me (fetch failed); they rest on the evidence agents' reading.
- Cost-benefit arbitration (Kool 2016/2017, Patzelt) is supported, but the original task has no payoff gap, so many "failures to find arbitration" are uninformative.
- Keramati 2011, Daw 2005 and Sezener 2019 are simulation theory. No direct test of the VPI-versus-time-cost rule on humans was found; Keramati 2016 (n=15 per group) is the only close behavioural test.
- LLM gate studies are small gains: He and Feng +1.02 points, and cost-aware utility did not beat always-fast. Ghoshal is 60 examples per task. SwiftSage compared against different baselines and its gain mixes the fast module and the switch.
- CogBench two-step model-basedness may reflect recall of a public task; Da Pelo 2026 shows retrieval LLMs nearly match Centaur. No LLM study tests the Keramati rule itself.
- Mapping to LLMs is analogy: human "time cost" is RT, LLM cost is tokens and latency; the uncertainty signal for "direct answer" is not defined in any source.

## Only seen in snippets (opened:false or abstract-level)
a17/b07/c28 (Kool 2017), a18 (Otto 2013 load), a23, a24, a25, b27, b28, c25, c26, c27, c29. Claims K05, K09 and K12 lean partly on these and are marked accordingly.

## GAPS
1. Does any LLM study test an explicit expected-gain-versus-token-cost gate (value of information, not just confidence) against fixed and random routing at equal total tokens, with cost-adjusted utility reported?
2. Which cheap signal best predicts that a slow pass will change the answer (sample disagreement, logit margin, verbalised confidence)? Head-to-head numbers on the same items.
3. What is the measured break-even: for which task difficulty and token price does planning stop paying for current LLMs (the Kool-style payoff-gap analysis applied to LLM tasks)?
4. Do human samples with proper instructions still show cost-benefit arbitration (Kool 2016/2017 redone with story instructions), and what is the effect size (N, d)?
5. Does a cached answer (memory of an earlier solved case) get over-trusted like a habit: any LLM study of stale cache or Einstellung-like failure when the task changed (devaluation analogue)?
6. How large is the gate's own cost (extra tokens for the fast pass and the decision) relative to savings, in agent loops such as SwiftSage, Imagine-then-Plan?
7. Is the Goldilocks replan frequency stable across environments and models, or must it be tuned per task? Any rule that predicts it?
8. Does depth-limited planning with cache plug-in (plan-until-habit) work for LLMs: truncated reasoning plus a learned value estimate versus full chain of thought at equal tokens?
9. Replication status of Keramati 2016 (time pressure shallower planning) and Otto 2013 (load) with larger samples.
10. Do the Feher da Silva and Hare 2020 numbers hold on direct re-reading (medians 0.24, 0.39, 0.78, 0.79, simulated 0.94 and 0.36)?

## Gap search results (evidence_d.jsonl, d01 to d20; claims K22 to K29 added)
Search engines were out of quota and the arXiv, Semantic Scholar and OpenAlex APIs returned 429, so sources were found by known IDs, direct PDF/HTML downloads, the Gershman lab site and the Europe PMC citation lists. This limits recall: gaps 1, 2 and 5 may have studies this pass could not find.

1. **Expected-gain vs token-cost gate at equal tokens: STILL OPEN (partly).** No study found. Nearest: He and Feng 2026 (learned gain-minus-cost gate, equal slow-call count not equal tokens; every routed method has lower cost-adjusted utility than Always-Fast, 0.4731 best vs 0.4789), RaM (trained VOC reward, no routing control), Imagine-then-Plan (adaptive beats fixed and random on a budget curve). See K24.
2. **Best cheap signal: PARTLY CLOSED.** Same 5,000 items: learned gate +1.02, avg log-prob +0.32, logit gap -0.06, random -1.14. Sample vote beat verifier routing on GSM8k (Yue 2024). Verbalised confidence vs sample disagreement vs logit margin on identical items for "slow pass changes the answer": not found. See K23.
3. **Measured break-even: PARTLY CLOSED.** Snell 2024 gives difficulty and inference-load dependence; Paglieri gives a token-cost point (3.4x tokens for lower reward). No Kool-style payoff-gap curve over token price. See K25.
4. **Human cost-benefit arbitration with proper instructions: MOSTLY CLOSED.** Kool 2017 opened: Exp 1 N=98, d=0.47; replication N=93, d=0.29; Exp 2 no payoff gap N=100, d=-0.04; extensive instructions with comprehension checks (not the story format). A 2026 sample n=140 supports learned arbitration (abstract only). Nobody combined story instructions with the payoff-gap design. See K22.
5. **Stale cache / Einstellung in LLMs: PARTLY CLOSED.** Pattern-over-trust evidence (Wu 2024, GSM-NoOp up to 65% drop, Ullman 2023), but no study of an agent's own cached solution after the task changed. See K26.
6. **Gate cost vs savings: PARTLY CLOSED.** SwiftSage switch costs no tokens (Swift-only 49.22 vs 62.22); He and Feng fast pass 5.26 tokens vs about 519 routed; VGS value model 0.024% of FLOPs. Imagine-then-Plan does not separate predictor cost. See K27.
7. **Goldilocks stability: CLOSED as "not stable".** Shapes differ by model and environment; no predictive rule; longer-horizon tasks favour larger lookahead. See K28.
8. **Plan-until-habit in LLMs: STILL OPEN.** VGS is the closest (value-guided block search, 39.8 vs 31.6 majority voting at N=256), not a truncated-reasoning-plus-value test at equal tokens. See K29.
9. **Replication of Keramati 2016 and Otto 2013: STILL OPEN.** Both re-read (n=15 vs 15; 25 of 43 analysed). No larger direct replication in 137 and 252 citing records. A tDCS null (n=22) and other paradigms are not replications. See K08, K09.
10. **Feher da Silva and Hare numbers: CLOSED.** 0.24, 0.39, 0.78, 0.79 observed and 0.94, 0.36 simulated all confirmed on the bioRxiv v1 PDF (also 0.80 for a TDLR wrong-model agent; IQRs in d01). Peer-reviewed version seen at abstract level only.

Still weakly sourced: d04 and d07 are abstract-level (opened:false). Ullman 2023 and Wu 2024 numbers are partial (figures not extracted).
