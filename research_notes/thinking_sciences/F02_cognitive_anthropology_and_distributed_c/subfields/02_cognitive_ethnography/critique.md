# Critique F02.02 Cognitive ethnography (cross-check)

## Re-checked numbers (opened against source text this session)
- Hutchins 1995: 100+ observer flights over 6 years, 122,000 lb card (Vref 132/128), set 25-30 min before landing, 2,000 lb bands, call-out at 5 knots and 500 ft AFL, salmon bug about 10 knots wide. All confirmed. "Used 10-15 min later" not re-checked.
- Park et al. 2023 Generative Agents: TrueSkill 29.89/26.88/25.64/22.95/21.21, d=8.16, H(4)=150.29. Confirmed. The paper adds that crowdworker vs fully ablated baseline did not differ significantly.
- Gilardi et al. 2023: n=6,183, +25 points, under $0.003, 30x cheaper. Confirmed.
- Shen et al. 2026 (arXiv 2609.27327): HNS 97.0 and 121.5; 17.8 to 140.1; 47.0 to 113.8; 35.4 to 100.0; time -48.9% (45.0 s to 23.0 s per video); $16.03; $1.07/h; 31.3%-44.5%. Confirmed. Caveat: each human condition ran on half the benchmark and full-benchmark human time was extrapolated by doubling.
- Kirsten et al. 2024: GPT-4 kappa 0.97/0.94 (A), 0.75 (B), 0.56 (C). Confirmed.
- An 2025 Cognitive Workspace: 54.52%, 57.1%, 58.8%, 59.8%, effect sizes 23-196. Confirmed (own metric).
- CORRECTION, MetaGPT (c16): the 503 s run time belongs to the no-executable-feedback variant (executability 3.67). The full model with feedback is 3.75 executability, 541 s, 31,255 tokens, 124.3 tokens per line. The earlier line mixed the two. Pass@1 85.9/87.7 confirmed.
- CORRECTION, Park et al. 2024 1,000 people (c15): the text now served on arXiv is a later revision (1,052 participants, Claude Opus 5.5 simulations). GSS accuracy 72.8% for interview+survey vs 79.5% participant retest (about 92%) vs 60.4% demographics only; Big Five r 0.86 vs retest 0.95; no gain on incentivised economic games (MAE 0.29 vs 0.27 demographic; retest 0.21). The 83/82/86% figures in c15 come from an earlier version; label them v1 and cite the version.
- NOT re-checked: Shang et al. 2026 (c19; a grep of the paper text did not find the quoted bootstrap numbers, so they may be from another version), Jain et al. kappas, Poquet clusters, Venkatesh and Cui.

## Contradictions and tensions
- Distributed cognition vs situated action vs extended mind: conceptual only, no data contest.
- LLM coding: GPT-4 kappa runs 0.56-0.97 by task in one paper. "LLM beats crowd" (Gilardi) is for easy label sets benchmarked on trained annotators. They do not conflict, but "LLMs match humans" fails for hard codebooks.
- Verification helps on average (Shen) but hurt on 2 of 15 tasks; anchoring is a plausible cause.
- Park 2024 headline numbers differ across versions.

## Weak spots
- Founding evidence is one author's stylised account. No error rates, no with/without-artifact comparison, no replication found.
- Most LLM entries study LLMs as coders or simulated people, not cognitive ethnography of agents. The link to the schema is by analogy.
- Cognitive Workspace effect sizes (d up to 196) are not credible; the metric makes RAG score zero.
- Several 2026 entries are single preprints. Shen 2026 uses one VLM and reports no repeated runs.

## Seen only in snippets or not opened
a11, a13, a21-a23, a27, a28, b09, b10, b18, b19, b24, b25, c23-c26 (books and listings; not opened). Search was limited (Semantic Scholar and OpenAlex rate limited earlier), so the negative results "no replication" and "no LLM-agent ethnography" are weak.

## GAPS
1. Has any controlled study tested that task-transforming artifacts (bugs, cards) reduce errors against plain memory, in aviation or elsewhere (error rates, N)?
2. Does ethnographic coding of LLM agent traces (who holds which state at each step) lead to design changes that raise accuracy at equal tokens?
3. Does a verification pass anchor on the first pass's errors, and on which task types (Shen's two losing tasks)?
4. What is the kappa of current models on video and field-note coding with open codebooks, and how often do they invent categories?
5. Does the multi-agent gain over a single agent with role-switching survive at equal total tokens (MetaGPT, CoThink style)?
6. Do reflection and memory ablations show up in task success rather than rater rankings, and do other labs replicate them?
7. Is the Shang et al. 2026 result (+5 to +6 points) verified, and how large is it at equal tokens?
8. Do interview-grounded simulations still fail on incentivised behaviour in newer model versions, and why?
9. Do the ship-navigation numbers in Cognition in the Wild (team size, fix cycle, errors) hold up, and has anyone replicated them? The book was not opened here.

## Gap search results
Web search was exhausted, so sources came from PubMed, arXiv PDFs and one Hutchins page. Evidence in evidence_d.jsonl (d01-d19).

1. Artifacts reduce errors: PARTLY CLOSED. No controlled speed-bug test found. Checklists give the nearest data: Haynes 2009 death 1.5% to 0.8%, complications 11.0% to 7.0% (N=3733/3955); Pronovost 2006 infections 7.7 to 1.4 per 1000 catheter-days; Ontario 2014 found no effect (death OR 0.91, P=0.13, 101 hospitals). Claim K16, status contested.
2. Trace ethnography leading to better design: PARTLY CLOSED. MAST (kappa 0.88) led to ChatDev 25.0 to 40.6 and AG2 +5 points, but tokens were not matched. Who&When shows LLMs reach only 53.5% agent and 14.2% step attribution. Claim K17.
3. Verification anchoring: PARTLY CLOSED. Self-correction flips right answers to wrong (Huang 2024). Shen 2026 names anchoring but did not test it. No blind versus shown-first-pass experiment found. Claim K18.
4. Open-codebook kappa and invented categories for current models: STAYED OPEN. Only closed-codebook studies were reached (Chew 2023, Xiao 2023). Claim K22.
5. Multi-agent versus single at equal tokens: CLOSED enough. Kim 2026 (260 configurations, matched budgets) shows +80.8% to -70.0% by task; debate loses to self-consistency. Claim K19, established. Not checked: MetaGPT itself at equal tokens.
6. Reflection and memory ablations on task success: PARTLY CLOSED. Reflexion reports +8 points on HotPotQA over episodic memory; an independent paper shows error propagation in memory (numbers not extracted). No clean other-lab replication of Park's ablation. Claim K21.
7. Shang 2026: CLOSED. The v3 text confirms +5.1 to +6.0 points with Holm tests, but CoThinker uses 14,323 tokens versus 643 for CoT, so no equal-token result. Claim K20.
8. Incentivised behaviour in newer models: PARTLY OPEN. The earlier Park text shows games without a significant gain (ANOVA p=0.16, interview 0.66 vs demographic 0.48). Twin-2K-500 gives 87.67% of retest on average but no game-level breakdown extracted. No newer-model rerun found. Reason not established.
9. Cognition in the Wild ship numbers: STAYED OPEN. The book was not available and no replication search was possible.

Claims file now has 22 claims (K16-K22 new; K02, K06, K07, K10, K12, K13 extended; K13 changed from established to contested because equal-token gains are not shown).
