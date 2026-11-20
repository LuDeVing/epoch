# Critique E17.09 Assumption testing (cross-check)

## Corrections made
Sources re-opened this session: Failing to Falsify (arXiv 2604.02485), FalsifyBench (2606.04751), Batista and Griffiths (2602.14270), Camuffo et al. 2020, Koning et al., Huang et al., Otis et al.
- Batista and Griffiths: 557 recruited; 504 gave a final hypothesis (chi-square(4)=28.02 uses n=504). Lines a21 and c14 each right but name different groups.
- Camuffo 2020: line c26 says "250 nascent entrepreneurs". Not in the paper text. Paper: 116 startups randomly chosen from 164 applicants (control n=57). Use 116/164.
- Failing to Falsify confirmed: 11 LLMs, success 6-78%, 45 turns, 42% to 56%, 29 humans, I:C 1.79 vs 0.24.
- FalsifyBench confirmed: 41%, 75%, 68%, n=1,200, coefficient -4.15, Spearman -0.937, rates 59.2/53.4/49.5.
- Koning confirmed: 7.6%, 16.75%, 280%, 11.8%, 8.5%, 9-18% launches. The headline page-view effect is 8.5-11.8%; 46% is only the fixed-effects step.
- Huang: table text garbled, but GPT-3.5 CommonSenseQA 75.8 to 38.1 to 41.8 and GPT-4 GSM8K 95.5 to 91.5 to 89.0 match the rows.
- Otis confirmed: 640 randomized, 634 completed, gap 0.267 s.d. (p=0.013), -0.09 s.d. low performers.
- Camuffo 759 vs 754 replication firms: unresolved.

## Contradictions
- Low-performer loss given as 8% and 10% in different lines.
- Information-gain querying (b19) vs disconfirmation (Failing to Falsify, FalsifyBench): disconfirming tests win in rule games, yet boundary queries can hurt on simple concepts.
- Camuffo panel results positive in some specifications, not significant in others.

## Weak spots
- Nearly all LLM evidence is rule-discovery games (2-4-6, WILT, FalsifyBench), far from business assumptions. Transfer is assumed.
- Business evidence is small (116 firms, fragile panel significance); the replication was seen only as a working paper. A/B testing study is observational.
- Most 2026 items are single preprints.
- Not opened: Wason 1960, Klayman and Ha 1987, McGrath and MacMillan 1995, Kerr et al. 2014, Mitchell et al. 1989 (the "30% more reasons" premortem figure is from memory; do not use).
- Snippet-only or without exact numbers: a28, c28 (search notes), c20, c24.
- a05 detail (21 mentors, 1,856 panel observations) not rechecked.
- FalsifyBench rho pairing (which two quantities) was not checked in detail.

## GAPS
1. Does an assumption-mapping step (list assumptions, rank by risk, design one test) beat plain reasoning at equal tokens on any decision benchmark?
2. Does Think-in-Opposites transfer from rule games to open business or forecasting questions, and to non-thinking models where gains were mixed?
3. Does the 2024 four-RCT replication (759 firms) report the same revenue and pivot effects, and the same panel fragility?
4. Which test policy (positive, disconfirming, information gain) wins as concept complexity grows (support-mismatch trap)?
5. Does a premortem or devil's advocate step reduce LLM overconfidence, with measured numbers (Mitchell 1989 figure unverified)?
6. Do agents resist user-seeded hypotheses when they choose tests, and does an unbiased test generator restore the 29.5% discovery rate?
7. How well do LLM-proposed cheap experiments match what founders actually ran (any field study)?
8. Is the Otis split (low performers harmed) reproduced for other advisers, and does forcing riskiest-assumption questions remove the harm?
9. What is the token cost of extra falsification turns compared with best-of-N?

## Gap search results
Evidence file: evidence_d.jsonl (d01-d18). Claims updated (K02, K05, K07, K12, K15, K16) and K17-K21 added. WebSearch used 8 times; Semantic Scholar, OpenAlex and arXiv APIs were rate-limited (429), so sources came from page fetches.

- Gap 1 (assumption map vs plain at equal tokens): OPEN. No benchmark found (d18). Popper (d06) tests a falsification loop; nothing tests risk-ranked assumption lists.
- Gap 2 (Think-in-Opposites transfer): PARTLY CLOSED. Human result is 78.3% vs 38.3% vs 36.7%, N=180, one task (d03). LLM gains significant for thinking models, mixed for non-thinking (d04). No open-ended business or forecasting test.
- Gap 3 (759-firm replication): OPEN. Abstract only (d16): 759 firms, four RCTs, more terminated ideas, nonlinear pivots. It is a published SMJ 2024 paper. Revenue and panel fragility not seen; full text blocked.
- Gap 4 (policy vs complexity): CLOSED for rule tasks (d02). Positive tests as good or better on easy rules, information gain better on compound rules, all fail when the generator cannot propose the target. Single small workshop paper.
- Gap 5 (premortem / devil's advocate): OPEN, negative result (d12, d13, d14, d17). Arguing a side raised confidence (72.9% to 83%). Distractor-normalised confidence helps on factual QA. Mitchell 1989 still unverified.
- Gap 6 (user-seeded hypotheses; 29.5%): CLOSED with a correction (d01). The 29.5% came from random hypothesis-independent sequences. A disconfirming generator reached 14.1%. The AI chose the tests; agents choosing their own tests under a seeded hypothesis were not studied.
- Gap 7 (LLM experiments vs founders): OPEN. Only proxies: ideation-execution gap (d08), plan ratings (d09, d10), synthetic founders (d11).
- Gap 8 (Otis split for other advisers): OPEN. No replication found (d15, search snippets). The low-performer loss is 8% in the working paper and nearly 10% in the published version, which explains the earlier contradiction.
- Gap 9 (token cost vs best-of-N): PARTLY OPEN. Think-in-Opposites cost about 41% more tokens per turn (1,030 to 1,450) for a 20-point gain on Qwen3-32B thinking (d05). No equal-token best-of-N arm exists in opened sources.
