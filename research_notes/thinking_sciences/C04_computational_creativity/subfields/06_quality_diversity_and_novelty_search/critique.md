# Critique: Quality-diversity and novelty search (cross-check)

Sources re-opened this session (text extracted from PDF, numbers compared line by line): Lehman and Stanley 2011, Mouret and Clune 2015, Fontaine et al. 2020 (CMA-ME), QDAIF, Rainbow Teaming, Mind Evolution, Si et al. 2024, OMNI (Zhang et al. 2023), ShinkaEvolve. Pugh et al. 2016 could not be downloaded (Frontiers link returned no PDF), so its numbers rest on the first-pass notes.

## Numbers confirmed (10)
1. Medium maze: novelty 18,274 evals (sd 20,447) vs fitness 56,334 (sd 48,705), 40 runs, p<0.001; random selection 21/40. Confirmed.
2. Hard maze: fitness 3/40, random 4/40, novelty 39/40, 35,109 evals (sd 30,236). Confirmed.
3. Unenclosed maze: novelty 5/100 vs fitness 2/100, not significant. Confirmed.
4. Biped: 4.04 m (novelty) vs 2.88 m (sd 1.04). Confirmed.
5. MAP-Elites retina: p<1e-7 on all four criteria vs three controls; soft robots reliability and coverage p<0.002, precision worse. Confirmed.
6. CMA-ME: CMA-ES 3.46%, MAP-Elites 56.22%, CMA-ME(rd) 90.32% cells at n=20; Hearthstone QD-score 16,024.8 / 25,936.0 / 28,132.7 / 63,295.6; win rates 44.8 / 45.2 / 50.5 / 65.9. Confirmed.
7. QDAIF Table 1: Fixed-Few-Shot 0.767, Shuffling 0.696, Random 0.606, LMX quality-only 0.650, QDAIF 0.772; quality 4.133 vs 3.900; agreement 0.833. Confirmed. Note the table is one median-QD run per method (c02 already says so); the tie is within noise.
8. Mind Evolution: TravelPlanner 172/180 = 95.6%, Best-of-N 100/180 = 55.6%, Sequential-Revision+ 149/180 = 82.8%; Trip Planning 308/320 = 96.2%; Meeting 425/500 = 85.0%; island ablation 87.5% vs 77.4%. Confirmed.
9. Si et al.: novelty 4.84 / 5.64 / 5.81 (N=49 per condition); 4,000 seed ideas, 200 non-duplicate (about 5%) at cosine 0.8. Confirmed. Note 4.84 vs 5.64 is across reviews with mixed-effects tests, not a simple N=49 t-test.
10. OMNI: Crafter tasks learned uniform 4, learning progress 55, OMNI 82 (CI 80-87), interesting tasks 14 (OMNI) vs 9 (LP). Confirmed.

## Corrections made
- c27 attributes the OMNI numbers to "Faldor et al. (2025)". The paper opened is Zhang, Lehman, Stanley, Clune (2023), arXiv 2306.01711; Faldor et al. is a different later paper (OMNI-EPIC) and was not opened. b27 and c27 are therefore the same source, not two. Claim K13 counts one source.
- b20/c12 "PAIR 1 across 1 vs Rainbow Teaming 66 across 41": the Rainbow Teaming paper's Table 1 text layout is garbled in extraction. Rainbow Teaming 66/41 (Llama Guard) and 0.51 self-BLEU are clear; the PAIR cell next to Llama Guard reads 1/1 for the variant using Rainbow Teaming's mutator, but a "14/11" cell appears on the neighbouring row and the PAIR (Mixtral) column is "-". Treat "1 across 1" as unconfirmed. Safe reading: Rainbow Teaming found several times more jailbreaks across more behaviours than either PAIR variant (at most 14/11 on the layout that is visible), with the PAIR budget fixed at 2,000 prompts.
- b25/c26 and the ShinkaEvolve figure caption: the caption says "embedding-based rejection sampling with LLM as a novelty judge strongly outperforms no rejection sampling". The text says the LLM judge adds marginal gain over embeddings alone. Both readings are consistent; the claim that embedding rejection helps is supported, but the figure does not isolate embedding-only against none in its caption. Run counts for the ablation are not stated.
- a02/b01 etc. were duplicates of the same Lehman and Stanley table; the sources are one paper, so independent_sources was counted by paper, not by line.
- a24 vs c01: same paper (QDAIF); counted once. LMX is cited as an LMX Quality-Only baseline in QDAIF, not as the 2023 LMX paper (c06/c07) unless stated.

## Contradictions and tensions
- QDAIF headline (beats all baselines on AI-judged QD) vs its own human check (ties a fixed few-shot prompt, and the fixed prompt has higher human quality). The AI-judged win may be partly judge-hacking.
- Mouret and Clune: MAP-Elites wins on retina but not on best solution in soft robots. Pugh: plain MAP-Elites had outlier runs. QD gains are mostly in coverage and reliability, not in the best single answer. This matters because our agent is paid on correct answers.
- Lehman and Stanley's maze is hand-built to deceive; Pugh shows a misaligned descriptor is worse than fitness. Novelty is not free; it moves the prior into the descriptor (Kistemaker and Whiteson).
- Rainbow Teaming's stepping-stone win is large (0.91 vs 0.79) but tested on one target-attacker pair family. CodeEvolve and ShinkaEvolve show the same direction, with seed counts of 3 or unstated.

## Weak spots
- Almost all LLM-QD ablations are authors' own systems on tasks with a cheap automatic scorer (code, circle packing, jailbreak classifier). No test on open reasoning questions. Only Mind Evolution tests search structure on natural-language planning, and it needs a programmatic checker.
- No source compares QD archives to plain best-of-N at equal tokens on reasoning accuracy. Most compare at equal evaluations, which hides token cost of the judge and descriptor calls.
- AlphaEvolve and FunSearch ablations are figure-only; exact numbers were not readable. The archive's own contribution (MAP-Elites part vs island part) is not separated.
- LEVI (2026) is a preprint by one author; its claim that archive and seeding matter more than model size had one counter-case (no-large-models beat full on Transaction Scheduling, 67.4 vs 64.7).
- NoveltyBench and Artificial Hivemind show LLM diversity is low, but they measure answer variety on open prompts, not diversity that helps a task with one right answer.

## Seen only in snippets or not re-opened
- a32 (Stanley and Lehman book) and a33 (Lehman and Stanley 2011 NSLC): not opened, only cited by others.
- c28 (Guo et al. 2026): title and keywords only.
- Pugh et al. 2016 (a14-a16, b08, b09): opened by the first agents; not re-verified here (download failed).
- Cully et al. 2015 (a19, a20), Samvelyan JBB-only transfer numbers (c14), CodeEvolve (b24), LEVI (b26), Lim et al. (b21, b22, c15), NoveltyBench (c18, c19), Artificial Hivemind (c20, c21), LLMatic (c11): not re-opened by the cross-checker.

## GAPS
1. At equal tokens, does an archive-and-descriptor loop beat plain best-of-N (and best-of-N with a duplicate filter) on accuracy for reasoning tasks with one right answer, e.g. ARC and BrainTeaser? Nobody has run it; this decides whether any QD machinery enters the schema.
2. How much of Mind Evolution's gain over Best-of-N comes from islands, from the critic and feedback, and from recombination, at matched tokens and without a programmatic checker (i.e. with a model verifier only)?
3. What is the cheapest descriptor for LLM reasoning attempts (method class, first-step choice, answer cluster) that is aligned with success (Pugh's condition), and how reliable is model labelling of it (agreement with a second labeller)?
4. When does the explore-then-exploit switch pay off? Is there a measured rule (budget fraction, plateau signal) from novelty search plus objective hybrids (NSLC, MAP-Elites with improvement emitters) that transfers to a token-limited agent?
5. How do judge-hacking and score saturation (QDAIF 0.995-1) change if the quality score is replaced by a verifier or a held-out check? Is there a measured size of the gap for code or maths tasks?
6. Does conditioning each new sample on previous answers ("give a different one", NoveltyBench) match a full archive loop for distinct-approach count and solve rate, at lower token cost?
7. What are the exact PAIR vs Rainbow Teaming numbers and budgets (JBB table), and does the QD gain survive when PAIR is given the same total prompt budget and restarts?
8. How much of AlphaEvolve and FunSearch's gain is attributable to the MAP-Elites or island database rather than to the strong model and the evaluator? Any open reimplementation with a no-archive control and more than 3 seeds?
9. Are there failed replications or negative results of novelty search on real (non-hand-built) deceptive domains, and how often does the objective turn out not to be deceptive?
10. What is the token and wall-clock overhead of descriptor labelling, judge calls and embedding dedup inside an LLM QD loop, as a share of the budget?

## Gap search results (evidence_d.jsonl, d01-d17)

Web search quota ran out during this pass; sources were opened as PDFs from arXiv by id, found through arXiv listing pages. Search APIs (arXiv, OpenAlex, Semantic Scholar) returned 429.

Closed or mostly closed
- Gap 7 (PAIR vs Rainbow Teaming): CLOSED. Raw text extraction gives the Table 1 cells. Llama Guard: Rainbow Teaming 66 jailbreaks over 41 behaviours, PAIR with the same mutator 14/11. JBB classifier: 8/7 vs 1/1 (the earlier "1 across 1" was this cell). Self-BLEU 0.51 vs 0.74. Budget: PAIR 2,000 prompts (20 streams), Rainbow Teaming 1,000. The QD side had half the budget. PAIR restarts were not run. (d01, new claim K18)
- Gap 5 (judge vs verifier): PARTLY CLOSED. Maths: coverage 98.44% vs majority-vote or reward-model selection 41.41% at 10,000 samples (d10); optimising against a proxy lowers true score past an optimum (d11); a PRM has 44 exploits under mean pooling vs 1 under min readout (d12). No source measures the QDAIF-style AI-vs-true quality gap with a verifier swapped in. (K17)
- Gap 9 (negative results): PARTLY CLOSED. Real tasks where novelty alone loses: humanoid walking (p<0.05) and most Atari games (d14); ES was truly stuck in 5 of 12 Atari games. Lexicase over sub-objectives beat MAP-Elites on deceptive domains, a competing explanation (d16). No failed replication of the Lehman and Stanley maze was found. (K02, K21)
- Gap 4 (switch rule): PARTLY CLOSED. NSRA-ES gives a measured plateau rule (50 generations without a new best, step 0.05; every 10 generations fixed one trap) and GEP-PG a robust fixed hand-off (d13, d15). Both are control tasks; no LLM or token-budget rule. (K20)
- Gap 2 (Mind Evolution): PARTLY CLOSED. The ablation puts most gain on the critic and evaluator feedback (46.1% to 95.6%); islands about 10 points; no recombination-only run; ablation table columns are garbled. A model-only verifier was not tested. (d03, d04; K11 updated)
- Gap 10 (overheads): PARTLY CLOSED. Rainbow Teaming: judge is 4 of 7 calls per iteration, 14,000 batched calls per run (d02); embedding dedup is cheap and an LLM novelty judge is marginal (d09). Descriptor-labelling share alone, and token or wall-clock shares, are not reported anywhere found. (K19)

Still open
- Gap 1 (archive vs best-of-N at equal tokens on ARC or BrainTeaser): OPEN. The nearest work, Land 2026, has no archive and no matched best-of-N, and lists the ablations as not done (d07). DEI shows heterogeneous model archives beat solo at equal calls in Core War only (d06).
- Gap 3 (cheapest aligned descriptor and labeller agreement): OPEN. Only evidence is that smooth, success-linked descriptors matter in robotics (d17) and classifier-label agreement of 78-83% in jailbreaks (d02). No reasoning-method labelling study found. (K23)
- Gap 6 (give-a-different-one vs archive loop): OPEN. NoveltyBench compares only prompt styles; in-context regeneration is best of those and roughly human-level (d05). No archive comparison, no token cost, no solve rate.
- Gap 8 (archive share of AlphaEvolve and FunSearch gain): OPEN. AlphaEvolve's "no evolution" ablation removes the whole database over 3 seeds, figure-only (d08). ShinkaEvolve ablates parent selection and dedup but seeds are unstated (d09). No open reimplementation with a no-archive, matched-context control and more than 3 seeds was found.

Cautions
- Several new sources are 2026 preprints (DEI, Land, PRM stress test) by small teams; their numbers are single-run and not replicated.
- Pugh et al. (2016) still not re-verified.
- Net effect on the schema: nothing here supports adding archive machinery. What is supported is cheap: stagnation counter then forced method change (K20), embedding dedup (K09), a hard check instead of a model judge (K17), and judging by reading all attempts rather than counting votes (K22).
