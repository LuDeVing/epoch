# D07.07 critique (cross-check)

## Re-opened sources (full arXiv PDF text, this session)
Confirmed exactly: Si et al 2409.04109 (4.84 / 5.64 / 5.81; N=104 participants, 298 reviews; 56.1% agreement; Claude-3.5-Sonnet 71.4% ranker); AgentReview 2406.12708 (27.2%, 18.7%, 37.1%, 27.7%, Jaccard 0.364/0.154, no-rebuttal 0.622, no-rating 0.20, 53,800 documents); Ideation-Execution Gap 2506.20803 (N=43, over 100 hours, gaps -1.049/-1.760/-1.879); PaperBench 2504.01848 (21.0%, 41.4% vs 26.6%, 8,316 tasks); AI Scientist 2408.06292 (balanced acc 0.65 vs 0.66, F1 0.57 vs 0.49, AUC 0.65, two-human correlation 0.14); Liang 2310.01783 (30.85/28.58, 39.23/35.25, 308 researchers, 110 institutions, 57.4%, 82.4%); Cortes and Lawrence 2109.09774 (166 papers, 43 = 25.0% disagree, 22 of 43 = 51%, r=0.55, SE 0.065, 50% subjective); Beel and Baumgart 2502.14297 (42% failed, 8% more characters, median 5 citations, 5 of 34 from 2020+).

## Corrections
- c02/c03-c06 name the AgentReview authors "Li et al". The PDF author list starts with Yiqiao Jin; a17/a18 ("Jin et al") is correct. Cite as Jin et al.
- c02 says 523 papers; the paper text gives 500+ submissions (350+125+29+19 = 523). Both fine, but the 523 is a sum.
- a13/b10 novelty p-value: the table shows p=0.00 with Bonferroni stars; "p<0.01" (b10, a13) is right, c18's "p<0.05" is loose.
- b08 says "5 of 12 experiments (42%)": consistent (5/12=41.7%).
- Cortes and Lawrence: "43 disagreed" and "43 accepted by committee 1" are two different 43s (coincidence); do not merge.
- c19 Claude BasicAgent 21.0 is the top overall; the headline "21.0%" is the best agent, not an average across agents.

## Contradictions and weak spots
- Si et al 2024 (LLM ideas more novel) vs Si et al 2025 (gap reverses after execution) is the key tension. Same group; the later study is a smaller N (43) and only the later one measures execution. Treat novelty-before-execution as unreliable.
- LLM reviewer: a16/c14 say accuracy matches humans, but accuracy is 0.66 vs 0.73 on the imbalanced set; balanced accuracy matches only after calibration (b23).
- Disruption decline (b16-b19) is contested; a critique claims an artifact, the reply says it holds, and the index itself has known flaws. All figures come from a 2026 review summary, not the original papers. Wu et al 2019 numbers not re-opened.
- The history part (a01-a12) rests on Wikipedia only. The Shapin and Schaffer book, Shapin 1994, Collins 1985, Schaffer 1989 were never opened (a23-a26 are recall). No mercury heights, no primary Boyle text. Claims K01-K04 and K23-K24 are therefore single-source or contested at best.
- Only snippets/abstracts: a20 AgentRxiv, a21 Co-Scientist, a22 and c12 Algaba, c01 Generative Agents, c07, c08, c13, c22. No effect sizes.
- c11 Thakkar (27%, 20,000 reviews): arXiv lookup failed (Semantic Scholar rate-limited, an ID guess hit an unrelated paper). Unverified this session.
- Agent simulations (AgentReview, CABAL, Elo) show what GPT-4 agents do, not what humans do.
- The whole subfield is "background only" for the agent; transfer to schema is by analogy.

## GAPS
1. Does a cheap executed test (O-test) beat judge-based selection of candidate answers at equal tokens, as the Ideation-Execution Gap implies? Needs a direct experiment on our agent.
2. How many independent judge samples are needed before judge agreement passes about 70% on our tasks (humans sit at 56-72%)?
3. Does multi-agent discussion collapse diversity the way AgentReview reports (-27.2% rating spread), and does independent first-round answering prevent it at equal tokens?
4. What exactly do Shapin and Schaffer, and Collins, claim about replication failures? Open the book and primary Boyle/Huygens sources to replace Wikipedia.
5. Verify Thakkar et al 2025 (ICLR 2025 feedback agent): correct arXiv id and numbers, and whether the effect on review quality was measured by humans.
6. Do shared memories of prior failed attempts (AgentRxiv style) help agents more than isolated runs, with a clean equal-token comparison and replication beyond MATH-500?
7. Open Wu, Wang and Evans 2019 and Park et al 2023 for the team-size disruption numbers, and test whether larger ensembles produce less novel answers.
8. Do LLM judges' prestige and affiliation biases (Pataranutaporn 2025) appear in our own judge, and does blinding remove them?
9. Is there any replication of the AI Scientist-v2 workshop result beyond 1 of 3 papers?

## Gap search results (evidence_d.jsonl, d01-d17)
Search note: the WebSearch budget was spent and the arXiv, OpenAlex and Semantic Scholar APIs were rate-limited, so sources came from direct PDF and page fetches.

1. Executed test vs judge selection: PARTLY CLOSED by analogy. Large Language Monkeys (d06): with unit tests 15.9% to 56% at 250 samples; voting on MATH 40.50% to 41.41% from 100 to 10,000. Zhang 2025 (d07): the only debate method that won added an execution step. No matched-token run on our agent; still needs one. New claim K26.
2. Judge samples needed for 70% agreement: STAYS OPEN. PoLL (d10) shows a panel of three beats one GPT-4 judge (kappa 0.763 vs 0.627 on NQ); Zheng (d11) shows GPT-4 position consistency 65.0%. No agreement-vs-number-of-judges curve exists in what was read.
3. Debate collapse vs independent first round: PARTLY CLOSED. Debate rarely beats CoT or self-consistency, more agents or rounds do not help, and model mixing helps (d07, d08); same-family outputs are above 0.8 similar (d09). The -27.2% spread figure still comes only from AgentReview simulations. New claims K27, K28.
4. Shapin and Schaffer, Collins primary text: PARTLY CLOSED. The books could not be opened. Boyle's own 1660 text was read (d14): leaks admitted, failures recommended for recording, named witnesses. SEP pages (d15, d16) give Boyle's view and Franklin's reply to Collins (Weber case). Huygens suspension and the TEA laser case remain unverified from primary text; K02 and K03 stay single-source and contested. New claim K30.
5. Thakkar 2025: CLOSED (d01, d02). ID 2504.09737 confirmed. Correct numbers: 18,946 recipients, 26.6% updated vs 9.4% control, +80 words for updaters, 89% preference by two annotators on 100 pairs; no score effect. K19 reworded.
6. Shared failed-attempt memory: STAYS OPEN. AgentRxiv full text (d03, d04): isolated plateau 73.4-73.8% vs 78.2%, but best-test-set tracking, two isolated curves, three times the compute in the parallel arm, MATH-500 only. K16 reworded.
7. Wu, Wang, Evans 2019 and Park 2023: PARTLY CLOSED. Wu numbers re-opened and confirmed with extra detail (d12: two thirds of effect within scientists). Park 2023 abstract only (d13). Ensemble novelty: Artificial Hivemind (d09) says larger same-family ensembles add little.
8. Prestige bias in our own judge: STAYS OPEN. Pataranutaporn 2025 not located. Only generic judge biases (d11). Needs a blind-vs-unblind test on our judge.
9. Replication of AI Scientist-v2 workshop result: STAYS OPEN. Re-read (d05): 1 of 3, hand-selected from seeds, authors' own review says below main-track bar. No independent replication found, though the search was limited.
