# C02.05 ACT-R production selection - cross-check critique

## Corrections made (sources re-opened this session, PDFs under D:/research_scratch/C02.05, text extracted)
1. Krishnamurthy et al. 2024 (arXiv 2403.15371): confirmed >60% suffix failure for GPT-4 basic prompt, 32 prompt designs, 72 configurations, 50K queries, one configuration succeeds. b20/c13 consistent. (b20 says "32 prompt designs" and c13 "72 configurations": both true, not a conflict.)
2. EVOLvE (arXiv 2410.06238): confirmed Pro 45.5 raw / 60.0 summarized / 59.6 guided, Flash 27.7/34.8/32.2, Gemma 7.6/10.5, 10.5/5.3, 4.9/4.1 (2B/9B), UCB 90.6, contextual Flash 0.0 vs 46.4, Pro 7.1 vs 64.3, LinUCB 96.4, fine-tuned 65.6 vs 54.5. Note: arXiv 2412.06438 is a different paper (Sawyer et al., foundation agents); do not cite it as EVOLvE.
3. Binz and Schulz 2023: confirmed regret 2.72 (SD 5.98) vs humans 3.24 (SD 10.26), t(38878)=-5.03; short horizon t(5566)=-0.043; descriptions t=-16.85 (above chance) and -11.50 (below human). Note GPT-3 had LOWER regret than humans in the horizon task overall.
4. Schubert et al. 2024: confirmed alpha+ = 0.87 +/- 0.01, alpha- = 0.10 +/- 0.04, t(49)=20.1.
5. Gray et al. 2006: confirmed t = 0.491 and 88.5% at a 1 s difference; 98% and 87% variance; Table: keypress/0-lock/1000-lock = low/medium/high: accesses 6.8/6.4/4.1, first look 1179/1241/2334 ms, blocks 1.7/1.9/2.9. The column order concern in b12 is resolved.
6. Brasoveanu and Dotlacil 2020 (ICCM paper): confirmed 5,000 / 9,000 / 22,000 episodes and 15,000 / 25,000 episode runs, -0.15 step reward.
7. Zhu and Simmons 2024 (arXiv 2403.00810): confirmed gamma 0.95, no update on quit, find 14/15 action-only vs 15/15 bootstrapped, paired t-test p 0.446 (find) and 0.347 (slice). The table columns "success without LLM" and tokens stay garbled (clear countertops action-only shows 15/15 with a 12/15 entry); do not quote those columns.
8. Wu et al. 2024 (arXiv 2408.09176): confirmed 0.4826 / 0.3564 / 0.6576 and NLL 0.6931 / 1.1330 / 0.6534, 2,012 trials, 32 problem sets, coefficient 0.086, threshold 0.88. CORRECTION to b19: the paper prints U(n)=U(n-1)+0.2[R(n)+U(n-1)], but its own traces (U(n-1)=0, R=-2.25 gives -0.45; U(n-1)=3, R=-2.2 gives 1.96) use the standard minus sign. The printed plus is a typo; the -1.02 worked example is therefore also unreliable.

Not re-opened (taken from earlier files): Taatgen et al. chapter numbers (Lovett task), Stocco primer, Gall and Fruehwirth, Atalar 2025, life-sciences Thompson sampling (c19), Feng 2026 (c20, arXiv id 2608.20274 looks unusual and was not verified), SkillCraft.

## Contradictions and weak spots
- a01, b01, c01 (and a02, b02, c02, a04) are the SAME 2005/2006 chapter. Counted as one source. The central "humans learn strategy by utility" claim therefore rests on one secondary description of Lovett and Anderson 1996, which no one opened. Fu and Anderson 2006 (a27, b14, c05) also never opened.
- No human-data replication or failed replication of the utility equation was found. The only competing evidence: TD models fit better (Walsh and Anderson), poor fit for non-reward-seekers (Stocco primer), and the Sugar Factory fit, which does not separate instances from utility.
- Two ACT-R formulations (success/cost 5.0 vs reward-difference 6.0) disagree on tie-breaking (Gall and Fruehwirth); behavioural studies rarely say which was used.
- LLM evidence is indirect: zero studies ablate ACT-R-style utility vs random operator choice in an LLM agent. Zhu and Simmons has 15 trials, simulated kitchen. LLM-ACTR is training and its gain is small.
- Bandit studies (Krishnamurthy, EVOLvE, Schubert) are about the LLM's own exploration, which supports keeping counts in the scaffold, but they test no reasoning operators.
- c19 (30 queries per mode, no CI) and c18 (7% gains) are weak; c20 is correlational.
- Snippet-only: a19, b14, b15, c03, c05, a26, a27, c25 coverage gap (ICCM/MathPsych 2024-26 LLM and ACT-R papers likely missed).

## GAPS
1. Does scaffold-kept success/cost utility choice among reasoning operators beat random and fixed-order choice at equal tokens? (no ablation exists anywhere)
2. What is the original Lovett and Anderson 1996 data (N, fit statistics, how many participants stayed with overshoot)?
3. What softmax temperature and goal value G work for operator choice, and how sensitive is accuracy to them?
4. How much credit assignment is needed for multi-step operator sequences: end-of-episode sharing vs TD with traces?
5. How many observations per context are needed before learned success rates beat a uniform prior (cold start, prior strength V)?
6. Do LLMs bias operator success estimates (optimism, 0.87 vs 0.10) when asked to self-estimate, versus scaffold counts?
7. Are there 2024-26 ICCM, MathPsych or arXiv papers using ACT-R utility in LLM agents that we missed?
8. Does Fu and Anderson 2006 show that utility learning reproduces human recurrent choice, and with what fit?
9. Does shared utility across tasks transfer (Feng 2026 binned utilities, SkillCraft) when outcome-based rather than similarity-based?
10. How should non-stationary operator success (operator stops working) be handled: decay of counts or a change detector?

## Gap search results (evidence_d.jsonl, d01-d17; claims K18-K26 added, K02/K13 upgraded)
Search tools were rate limited (OpenAlex and Semantic Scholar returned 429, arXiv API 429 after a few calls); 8 WebSearch calls used, the rest by direct page and PDF fetch.

1. Ablation, utility vs random vs fixed order at equal tokens: STILL OPEN. Nearest evidence: MACLA (d05) Bayesian selection vs similarity-only, -7.8/-9.1 points; life-sciences bandit (d07) 76.7% vs random 49.0% but 30 queries, no CI; CogRouter (d09) adaptive depth vs fixed levels 92.5% vs 76.5/86.5, trained not counts-based. No study uses reasoning operators with counts and a random control.
2. Lovett and Anderson 1996 data: PARTLY CLOSED. The 1996 paper was not reachable. The 1995 CogSci precursor (d01) gives N=67, 90 problems, noise variance 0.052, R2 .99 aggregate / .66 individual, extreme preferrers 6 to 18% per condition. The count of overshoot-stayers is not reported there. Xie and Moss 2025 (d02, N=100) replicates the related Lovett and Schunn 1999, so the human effect now has a second lab (K02 upgraded to established).
3. Temperature and G: PARTLY. Humans: noise SD about 0.23 (d01), 0.491 (Gray, earlier). LLM bandit work supports decaying temperature (d17) and shows LLMs have excess random exploration (d16). No sensitivity sweep of accuracy on operator choice exists. Open.
4. Credit assignment: PARTLY. TD-extended ACT-R fits human single-step data (d03, a=0.1, R2 .94-.98); CogRouter (d10) shows step-level credit beats uniform and that failure penalties cause collapse. Fu and Anderson 2006 not opened (d04, abstract only). No operator-chain comparison. Open.
5. Cold start: PARTLY. MACLA learning curve (d06) and warm-start ablation +5.5 points (d07). No prior-strength sweep. Open.
6. LLM self-estimate bias: CLOSED. Barkan et al. (d11) and Kaddour et al. (2026, d12): predicted 77% vs true 22%, no recovery after failure. Keep counts in the scaffold (K23 established).
7. Missed 2024-26 papers: PARTLY. Found MACLA (d05), CogRouter (d09), ParetoBandit (d13), TextBandit (d15), LLM-enhanced MAB (d17). No new ICCM or MathPsych paper with ACT-R utility in an LLM agent was found; arXiv API limits stopped a systematic sweep. Open for ICCM proceedings.
8. Fu and Anderson 2006: STILL OPEN. Full text blocked. Only the 2004 TD paper (d03) was read; it is a different paper.
9. Cross-task sharing: PARTLY. Feng 2026 verified (id is real, v2 Oct 2026; d14) and extended: whole-task skills hurt, subtask skills help by 0.5 to 1.9 points. Outcome-based shared utility untested. Open.
10. Non-stationarity: PARTLY CLOSED. ParetoBandit (d13): forgetting 0.997 recovered reward to 0.8630 vs 0.8850, 20 seeds; LLMs show weak directed exploration in changing tasks (d16). Arms were models, not operators; the other paper's window/forgetting values (d08) are untested.

Cautions: the life-sciences results (d07) are 30 queries without CI; MACLA ablation control is similarity ranking; CogRouter 82.3% (abstract) and 92.5% (ALFWorld) were not reconciled.
