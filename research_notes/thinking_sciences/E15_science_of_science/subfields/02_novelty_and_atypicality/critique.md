# Critique: Novelty and atypicality (E15.02), cross-check

## Numbers re-opened this session (full text, not snippets)
Confirmed from source text, no change needed:
1. Li, Lin, Wu 2025 (arXiv 2506.15959): top 5% atypical A>22.9, top 5% displacing D>0.04, 40,935,251 articles 1965-2020, negative A-D link by discipline, period and team size. Llama-3.1-70B classified 50,147 papers (evidence says "about 50k"; fine).
2. Si, Yang, Hashimoto 2024 (arXiv 2409.04109): novelty 4.84 / 5.64 / 5.81, 49 ideas per condition, 79 reviewers, 298 unique reviews, about 5% non-duplicates at cosine 0.8, r=0.725 novelty vs overall, feasibility r<0.1.
3. Si et al. 2025 ideation-execution gap (arXiv 2506.20803, HTML): human changes -0.010, +0.078, -0.052; AI drops 1.049, 1.760, 1.879; post-execution execution scores: excitement AI 3.896 vs human 4.482 (FDR p=0.004), effectiveness 4.125 vs 4.782.
4. Foster, Rzhetsky, Evans (arXiv 1302.6906): 85.8% vs 14.2%; 12.4% vs 1.8%; means 8.38, 11.00, 12.90; p(new)=0.76 p(repeat), p(jump)=0.65 p(repeat); 137 prizes; surprisal R2 = 0.2916 (the "29.2%").
5. Holst et al. (arXiv 2402.14583): 972,161 papers and 142,362 patents hidden; 97% and 78% zero-reference; PDF check 93% papers and 98% patents do list references.
6. Gupta and Pruthi (arXiv 2502.16487): 13 experts, 50 documents, 14.0% score 5 plus 10.0% score 4 = 24%.
7. Lin, Evans, Wu 2022 (arXiv 2103.03398): 61% vs 36%, 2.3% highly atypical, 3.9% (1970) to 1.4% (2000), r=-0.05, embedding correlation 0.74.
8. Huang and Xie (arXiv 2610.07329): 60 million OpenAlex publications; AUC values 0.94-0.98 and 0.79/0.73/0.60/0.55/0.40/0.26 appear in the figure text. The order of the six benchmark names in the figure text was scrambled by PDF extraction; the mapping benchmark to value rests on the evidence file and is not independently re-verified.

Corrections and clarifications:
- Evidence a22/b21/c03: the "rankings flip" is true for excitement (AI 3.90 vs human 4.48 after execution) and effectiveness, but NOT for novelty. The paper's table of execution outcomes shows novelty 4.93 vs 4.73 with p=0.21 (not significant; the table's column order was not checked against condition labels). Claim K16 states this.
- Si 2024 review counts: 119 / 109 / 109 novelty reviews in the table add to 337, above the 298 "unique reviews". The paper counts reviews per condition with some reviews covering ideas in two conditions. Use 298 only for unique reviews.
- Holst's description of Park et al.'s data (about 45M papers, 3.9M patents) differs from the 25M papers and 3.5M patents in a16. Park's own main analysis used 25M WoS papers and 3.5M patents; the 45M figure is the combined multi-database size as Holst states it. Not an error, but do not mix them.
- Gupta and Pruthi: the PDF table text is misaligned by extraction; the text statement 14.0% and 10.0% is used.
- Not re-opened: Uzzi 2013 (a01, a02, b01-b03) full text was not reachable this session; its numbers (9.11, 5.82, 5.33, 2.05, 5 background) are held as in evidence lines marked opened:true by the earlier agents and are single-sourced in this check. Also not re-opened: Park 2023, Wang et al. 2017, Bornmann 2019.

## Duplicates that inflate counts
Several evidence lines describe the same source: a11 = b04 = c01 (Li, Lin, Wu); a21 = b19 = c02 (Si 2024); a22 = b21 = c03; a19 = c20; a14 = b26; a13/a14/a15 = Lin 2025 family; b11 = c24; b24 = c25; b25 = a18 = c23; b27 = c19. Claims count independent_sources by paper, not by line.

## Contradictions between sources
- Lin, Evans, Wu 2022 says atypical papers are nearly twice as likely to disrupt (61% vs 36%), while the 2025 paper by overlapping authors says atypicality and disruption correlate negatively everywhere, and the 2022 paper itself has r=-0.05. The different bins and the different atypicality definition (journal pairs vs topic-level references) may explain it. Not reconciled (K05).
- Uzzi tail novelty (hits mix conventional core plus atypical tail) vs Li et al. (atypical and disruptive anti-correlate): the first is about citation counts at 8 years, the second about displacement. They answer different questions, which is the point of the subfield, but nobody ran both against a common outcome.
- Disruption decline: Park et al. vs Holst, Petersen, Bentley, Macher. The Park reply (a17) says decline survives Holst's data. Both camps rely on the same index, which K06 shows is unstable.
- Team size and D: Wu 2019 (small teams disrupt), Petersen (positive at 5-year window), Lin 2025 (negative returns with longer windows), Huang and Xie (large teams more disruptive after equalising references).
- Idea novelty: Si 2024 (AI more novel) vs Si 2025 (that edge disappears on execution) vs Gupta and Pruthi (many AI ideas copy existing work). Judge reliability evidence (K17) says the 2024 result is weak on its own.

## Weak spots
- Almost every LLM idea-generation gain (Nova, Deep Ideation, Gu et al., SciMON, Chen and Zhang) is scored by an LLM judge or embedding similarity. K17 shows such judges are near chance. No such pipeline was executed to a real result.
- Only one study (Liu et al. 2026, a23) tests source-target distance directly on both humans and LLMs. The agent decision "how far should a distant add-on be?" rests on that single paper.
- The mechanism of functional equivalence (K04) comes from the group that created the finding.
- Nearly all human-science evidence is bibliometric and correlational. None tests an intervention.
- The 2026 papers (Hao et al., Larregue and Gingras, Safari and Babaei, Yan and Ni, Wei et al.) are newest and least replicated.

## Seen only in snippets or summaries
- a20 (Hao, Xu, Li, Evans 2026): opened:false, search summary only.
- c22 (Doshi and Hauser 2024, 10.7% lower diversity): opened:false.
- a28 (Foster 2015, Funk and Owen-Smith 2017, Wu 2019): background, Wu numbers second-hand through Lin 2025.
- a27 (NovBench) and c15 (Chen et al. 2025): abstract only, no detailed scores.
- b29 (Wang 2024): abstract only in b29; c16 holds the numbers.

## GAPS
1. Does a distant add-on to a conventional core (the Uzzi mix) beat all-distant and all-conventional candidate sets when the agent is scored by an executable verifier at equal tokens? No LLM study tests the mix, only each side.
2. At what source distance does the cross-domain operator start to help, and does that threshold depend on model strength? Only one paper (Liu et al. 2026) measures it, and with an originality rater.
3. How much of the LLM idea novelty edge survives execution on tasks other than NLP research ideas (code, math, puzzles)? The ideation-execution gap was measured on one domain with 43 experts.
4. What is the right trigger for choosing displacement (replace the incumbent inside the topic) over recombination (extend into a new topic)? Is "name the incumbent answer first" enough?
5. Can a cheap non-LLM novelty gate (distance to nearest prior items in embedding space, plus a lookup of the nearest source) detect disguised copying, given that plagiarism checkers missed 24% of cases?
6. Do Lin 2022 (atypical papers disrupt more) and Li 2025 (negative link) reconcile once definitions are matched? This decides whether atypicality is a useful positive signal for selection.
7. What budget share of distant moves is worth it for an agent, given Foster's break-even numbers for human science (new moves must succeed 76% and jump moves 65% as often as repeats)? Is there an LLM equivalent measured anywhere?
8. Does diversity collapse across LLM samples (Wenger and Kenett; Doshi and Hauser; Si 5% unique) survive a forced-distance seed, and does it cost correctness?
9. Is the far-distance payoff delayed (Wang 2017: slow start, long-run hits), and does an agent benefit from an extra revision round for distant candidates before ranking?
10. Did any outside group replicate the functional-equivalence mechanism with a topic model other than the authors' own?

## Gap search results

Evidence: evidence_d.jsonl (d01-d18). New claims: K26-K32. Updated: K04, K05, K09, K10, K12, K15, K16, K18, K19. Limits: the web search quota ran out at the start and the arXiv API, Semantic Scholar and OpenAlex returned 429, so sources came from direct arXiv PDF reads and files already downloaded. Absence below means "not found with thin search".

1. **Mix versus all-distant versus all-conventional: OPEN.** No LLM study tests the mix. Zhang et al. (d01) generate from one conventional anchor plus one distant cited paper but do not compare arms. Zhao et al. (d02) show the distance trade-off without a core: random combinations 0.41 diversity but 0.05 relevance, trending ones 0.21 and 0.11. The AutoPyVerifier abstract (d16) supports the verifier design only. Run as our own experiment (K29).
2. **Distance threshold and model strength: PARTLY CLOSED.** The second reading of Liu et al. (d10) gives the shape: strong LLMs gain only in the farther half of pairs (beta 0.12) and more in the top 10% (0.24); pooled LLMs need the closest 20% removed. Still one paper, lay originality raters, no correctness check. Human work hints at an inverted U but I could not open it (d15).
3. **Edge outside NLP ideas: PARTLY CLOSED, negative.** In code the push away from known methods costs correctness (d04: pass@1 16.1% to 2.1%). In math, novel share of correct answers is high and rises with difficulty, but is LLM-judged (d05). The edge does not clearly survive execution; the two studies are not tests of the same claim as Si 2025.
4. **Displacement trigger: PARTLY CLOSED.** An independent group ties displacement to stance toward a named incumbent (d03). Naming the incumbent is plausibly necessary but is not shown sufficient; showing prior solutions cut novelty in math (d05), so pair it with a differ-from-this instruction.
5. **Cheap non-LLM novelty gate: CLOSED negative for embeddings alone.** An embedding filter found the known overlap in the top 10 in 10.34% of 58 cases versus 89.66% for facet-level re-ranking (d14). A cheap gate needs purpose and mechanism facets. A pure non-LLM gate on disguised copying remains untested.
6. **Lin 2022 versus Li 2025: NARROWED, not reconciled.** They differ on dataset, cohort, atypicality scale and outcome (d11, d12); the later paper does not discuss the 61% vs 36% result. Best reading is tail versus bulk, untested. Keep atypicality out of the selection score (K30).
7. **Budget share of distant moves: OPEN.** No LLM measure found. Foster numbers confirmed on re-read (d09). Estimate the success ratio with a verifier on a calibration set (K32).
8. **Diversity collapse and forced distance: PARTLY CLOSED.** Collapse is large (d07: same-model similarity above 0.8 in 79% of cases; d06: under 3 distinct answers in 10). Showing earlier answers restores human-level diversity (d06) and verbalized sampling raises diversity with higher downstream accuracy (d08). A distance-forced seed and its correctness cost are still untested (K28).
9. **Delayed payoff and an extra revision round: OPEN for LLMs.** The delay is documented for citations only (d18, d03). No LLM test of a revision round.
10. **Outside replication of functional equivalence: OPEN, one partial hit.** Huang (d13) separates bridges from within-topic redirectors with an independent embedding-cluster method; Ustyuzhanin (d03) ties displacement to the incumbent. Neither tests the mechanism, so K04 stays single-source.

New caution (K30): originality ratings by experts have test-retest ICC about 0.6 (d01), and an LLM rater scored AUC 0.42 for highly cited papers (d13). Selection by originality score alone is weak.
