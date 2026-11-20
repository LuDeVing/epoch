# Critique: Social epistemology of discovery (D01.09)

Cross-check done 2026-11-19. Sources re-opened this session: Hong and Page (PMC full text), Li et al. Self-MoA (arXiv 2502.00674), Wang et al. MoA (2406.04692), Hegazy (2410.12853), Zhang et al. MAD (2502.08788), Jiang et al. Artificial Hivemind (2510.22954), plus OpenAlex abstracts for Grim et al. and the Weisberg-Muldoon replication.

## Numbers re-checked (10)
1. Hong-Page Table 1: 92.56/94.53 (10 agents, l=12), 93.78/94.72 (20 agents), 93.52/96.08 (l=20), diversity 70.98/90.99 etc. CONFIRMED. Single run 87.3, 84.3, 93.2 CONFIRMED.
2. MoA 65.1 vs 57.5 (GPT-4o), +7.6, MoA-Lite 59.3: CONFIRMED. CORRECTION: the paper's introduction text says 65.8 in one place; abstract and results say 65.1. Use 65.1.
3. MoA ablation 61.3 vs 56.7 (n=6), 58.8 vs 54.5 (n=2), Llama-3-70B 45.0 aggregator vs 60.6 proposer: CONFIRMED.
4. Self-MoA 65.7 vs mixed MoA 59.1 (+6.6), average +3.8%: CONFIRMED. CORRECTION: the 59.1 baseline is Li et al.'s own 2-layer mixed MoA. Wang et al. report 65.1 for their 3-layer six-model MoA, so Self-MoA 65.7 is almost the same as the original MoA headline. The "Self-MoA beats MoA by 6.6" claim is against a weaker replication setup (a28/c10 should carry this caveat). Also a28 says "+6.6 over mixed MoA" and b07 says mixed beats single; these two contradict only in setup, not in data.
5. Hegazy: Gemini-Pro 78%, PaLM 2-M 64%, Mixtral 70%; diverse debate 91% after 4 rounds; 3 Gemini copies 82% (80% without CoT); ASDiv 94%; small models +17%: CONFIRMED. a29 "above GPT-4" compares with a quoted number.
6. Zhang et al.: Multi-Persona 0% wins, ChatEval/AgentVerse about 15%, single win +0.85% (Claude-3.5-haiku MMLU): CONFIRMED. Heter-SoM +6.4%, Heter-EoT +8.2%, +5.8% over CoT-average (the +5.8 is a maximum over benchmarks; a column shows -1.4% and -2.0% on some tasks, so "consistently" in c09 is too strong).
7. Jiang et al.: 26K queries, 70+ models, 31,250 labels, 79% of cases above 0.8, cross-model 71-82%: CONFIRMED.
8. Grim et al. (2019, published 2018 online): abstract confirms sensitivity to landscape randomness. a23/b14 only recalled this; now partly opened.
9. Weisberg-Muldoon replication (OpenAlex abstract, "Epistemic Landscapes Reloaded"): code reproduces, but small rule changes change results. a20/b16 (Alexander et al. 2015) remain recalled; their exact claim is unverified.
10. Not re-opened (time): Hofstra (b03), Yang (b04), Wang standpoint (c15), Si et al. (c19). Semantic Scholar API rate-limited (429). These stay as the earlier agent opened them.

## Contradictions
- Diversity helps (Hegazy, MoA ablation, Heter-MAD) vs diversity hurts when quality differs (Self-MoA). Reconciled only by the quality-diversity regression (c11, R2 about 0.7), which is one paper.
- Debate wins (Du et al.) vs debate fails against baselines (Smit, Zhang). Du et al. used copies of one model, so it also lacks heterogeneity.
- Hivemind (b08) says cross-model diversity is small; Hegazy and MoA say cross-model diversity is useful. Not incompatible (small but nonzero) but unmeasured: nobody has linked embedding similarity to ensemble gain except Self-MoA's Vendi regression.
- Zollman effect: a09/a11 positive; a24 (Rosenstock) says parameter-dependent. Status contested.

## Weak spots
- Many human-science rows (a18-a26, b13-b25, c25-c28) are recalled snippets, not opened: Kitcher, Weisberg-Muldoon numbers, Thompson, Singer, Zollman 2007, Lazer-Friedman, Woolley, Horwitz, Stasser-Titus, Levine, AlShebli, Page. Claims built on them are marked single-source or contested.
- a15/a16 lack authors. Hegazy is single-author in a small journal. c18 and c17 Elo is self-judged.
- Nothing tests Longino or standpoint claims empirically; c15 is the only LLM test and uses opinion questions in 2023 models.
- No study compares diversity vs sampling at EQUAL TOKENS except Self-MoA (partly) and Naik et al. (b05). Most "diverse teams" use more compute than the baseline.
- Single-agent relevance is low (stated in the task); mapped parts are G (keep alternatives), O (parallel branches), not new states.

## GAPS
1. At equal tokens, does heterogeneity (different prompts, methods, or models) beat k samples of the best single configuration for a single scaffold agent, and when quality gaps are what size?
2. Does transient diversity (delayed sharing among parallel branches) improve final accuracy vs immediate sharing in LLM agents, and on which problem difficulty?
3. How much of the diversity gain in LLM ensembles survives the hivemind effect: what embedding or Vendi diversity is needed before ensemble gain appears?
4. Do approach-diverse prompts (Naik et al.) replicate across models and tasks, with variance reported?
5. What exactly do Alexander, Himmelreich and Thompson (2015) and Thompson (2014) show, with numbers? (needs full text)
6. Zollman 2007 and Rosenstock et al. 2017: exact parameters where less communication helps or hurts; translate to branch-merge timing.
7. Do persona or standpoint prompts beat plain prompts at equal tokens on discovery tasks (c04, c15 conflict in spirit)?
8. Does mandatory uptake of critique (Longino norm) improve an agent over free self-critique, at equal tokens?
9. Does a verifier or judge agent remove the multi-agent failure rates in Cemri et al., and which of the 14 failure modes map to schema guardrails?
10. Are there replications of Hofstra et al. and Yang et al. in non-US or non-medical data, and do they bear on how an agent should discount its own novelty ratings?

## Gap search results
Done 2026-11-19. New evidence is in evidence_d.jsonl (d01 to d16; d15 and d16 are not opened). New claims K28 to K32; K20 changed to contested; K12, K13, K14, K17, K18, K21 gained evidence ids. WebSearch was exhausted, OpenAlex and Semantic Scholar rate-limited, PMC and PhilSci blocked, so only arXiv PDFs were opened.

1. Equal tokens, heterogeneity vs k samples: PARTLY CLOSED. Tran and Kiela (d01) show a single agent beats five multi-agent designs at equal thinking tokens above about 500 tokens (2000 tokens: 0.421 vs debate 0.403, ensemble 0.372), but all copies are the same model. Heterogeneity at equal tokens is still untested. Also, Self-MoA's +6.6 is against a weaker baseline (d15, from cross-check).
2. Transient diversity: OPEN. Chen et al. (d09) show blind-writing and subgroups keep diversity higher, but no accuracy result. Li et al. (d10): more rounds hurt after 15, group size 3 to 7 cuts the communication gain from +0.348 to +0.006.
3. Hivemind and diversity needed: PARTLY CLOSED. Answer-level diversity, not temperature, drives the gain (d03: Pass@5 0.79 to 0.91). Vendi/N falls from 1.03 to 0.47 for 3 to 7 agents (d08). No threshold Vendi value for gain was found.
4. Naik et al. replication: OPEN. Paper re-read (d13): big gains with GPT-4 (graph colouring 15 to 97), none with GPT-3.5 on planning, no variance reported, no independent replication found.
5. Alexander et al. 2015 and Thompson 2014: OPEN, sources not reachable.
6. Zollman 2007 and Rosenstock 2017: OPEN, sources not reachable. Only LLM-side analogues (premature convergence, d10) found.
7. Persona vs plain at equal tokens: MOSTLY CLOSED for objective questions. Zheng et al. (d14): 162 roles, 2,410 questions, no gain, role selection no better than random. Discovery tasks untested; c04 and c15 are not reconciled.
8. Mandatory uptake vs free self-critique: OPEN. Closest are d10 (accuracy 0.04-0.17 to 0.73-0.80 with a forced counter-reason step, against no protocol), d05 and d06 (free debate adds nothing or hurts via conformity).
9. Verifier vs MAST failures: PARTLY CLOSED. d11 and d12: verification 21.3% of failures; verification fixes give +9.4 to +15.6 points but not universal. Full mapping of the 14 modes to G1-G12 not done.
10. Hofstra and Yang replications: OPEN, sources not reachable.
