# Critique and cross-check: E14.07 Novelty measurement

## Numbers re-opened this session (10 checks)
1. Uzzi 2013 hit rates 9.11 / 5.82 / 5.33 / 2.05 per 100, and 3.54% (1980s) / 2.67% (1990s) negative median z: CONFIRMED from the paper text.
2. Uzzi team-size tail novelty 36.1 / 39.8 / 49.7%: CONFIRMED. The paper itself prints 36.2 / 39.9 / 49.7% in a second passage (rounding inconsistency inside the source).
3. Bornmann et al. 2019: +7.47% 'new finding', +17.71%, +58.78%, -13.45%, -19.86%, pseudo R2 0.33% (n=23,206): CONFIRMED. The table also gives per-model pseudo R2 (0.58%, 1.06%, 2.84%), so "under 3%" in a04/a08 is right.
4. Lin, Evans, Wu: 2.3% highly atypical, 3.9% to 1.4%, 61% vs 36%, r=-0.05, r=0.08, r=0.74: CONFIRMED. Note the paper confirms Uzzi's hit finding (its Fig 1d) and adds that the disruption chance peaks at the highly novel end (Fig 1c).
5. Si et al. 2024: novelty 4.84 / 5.64 / 5.81 (n=119/109/109 reviews), reviewer agreement 56.1%, Claude-3.5 pairwise 53.3%, 200 of 4,000 non-duplicate: CONFIRMED. Table shows p=0.00** for AI and 0.00*** for rerank, so a21's "p<0.01" and b13's "p<0.001 for rerank" are both fine.
6. Si et al. 2025 ideation-execution gap: numbers CONFIRMED but a23 mislabelled two columns. Correct reading of the gap table (columns Novelty, Excitement, Effectiveness, Overall): human -0.010, +0.078, -0.052, -0.628; AI -1.049, -1.760, -1.879, -1.976; FDR p 0.025, 0.001, 0.003, 0.004. So a23's "excitement -0.052 vs -1.760" and "effectiveness 0.078 vs -1.879" are swapped. c12 had the right labels except it said "all four metrics p<0.05", which is true. The execution-stage means (human 4.903 novelty, AI 4.729) match a24; FDR p 0.586 / 0.175 / 0.266 / 0.175, so a24's "0.175 to 0.586" is right. Ideation novelty p=0.035.
7. Gu and Krenn: 2.350 / 2.446 / 2.414, mean 2.403, 24.9% rated 4-5, completion 84.3%, AUC 67.44 / 60.39 / 63.20: CONFIRMED. The "1.94" is a z-statistic, not a mean. Difference between conditions is only about 0.1 point, so "tension between citation and interest" is a weak claim.
8. RINoBench (arXiv 2603.10303): 1,381 ideas, best macro-F1 17.2, 0.0 F1 on the 'not novel' class for all models: CONFIRMED. The model table is garbled in extraction, so which model scored 16.2 or 14.6 is unreliable (c08 already says so).
9. Sinhahajari et al. 2026 (arXiv 2606.12071): 27.2% standalone and 49.1% comparative win rate for gpt-5.5, human-LLM agreement as low as 22%, expert-expert 60%, LLM-LLM 52%, ref win rates 78% / 56% vs LLM judges 82% / 52%: CONFIRMED. The 78%/56% are two separate expert annotators, not one.
10. SciMON and Doshi and Hauser: SciMON +54.4/+55.6/+47.8/+46.7%, +57.8%, 88.9%, 45%, 85%: CONFIRMED; the "six NLP experts" were SciMON's own human raters (a20's limits line wrongly credits this to Gu and Krenn). Doshi and Hauser +6.7% (b=0.259), +8.1% (b=0.311), +10.7% low-DAT, 5.2% more similar: CONFIRMED.

## Corrections to record
- a23: swap the excitement and effectiveness labels (see check 6).
- a20: the six-expert evaluation belongs to SciMON, not Gu and Krenn.
- b22 and c15/c16 are the same paper (Shahid et al. 2025), so they count as one source. Same for b13/c10/a21 (Si 2024), b18/c08/c09 (RINoBench), a14/a15/b04-b07 (Lin et al.), a08/b01-b03 (Bornmann).
- The scratch file own/2201.03406.txt is an unrelated SIR-model paper; the Lin et al. paper is arXiv 2103.03398 (a14 URL is right). The file named 2603.22510.txt is Safari and Babaei (IS journals), not RINoBench (that is 2603.10303). Check ids before reusing those files.
- own/1905.05142.txt is also unrelated (federated sensor model); the Krenn-Zeilinger paper is 1906.06843.

## Contradictions and tensions
- Uzzi (hit = top 5% citations rises with conventional-plus-tail) vs Lin (disruption rises at the extremely atypical end) vs Bornmann (the measure barely tracks expert novelty tags). These are three different outcomes (citation hit, disruption, expert label), so they do not strictly contradict, but no source shows one proxy that wins on all three.
- Si 2024 says AI ideas are more novel; Si 2025 says that edge disappears after execution; Gu and Krenn find citation-selected pairs no more interesting than random; Beel and Gupta find many "novel" outputs are not. The common thread is that rated novelty before execution and verification is unreliable.
- LLM-as-judge: Si 2024 reports Claude-3.5 at 53.3% (ranking ideas) but also 71.4% on another quality task; RINoBench reports F1 17.2; Shahid reports 89.66% only with retrieval. Task framing and retrieval explain most of the spread; they are not comparable numbers.

## Weak spots
- Almost no paper-level causal evidence: Uzzi's hits, Lin's r values and Bornmann's R2 are all correlational.
- Nearly all LLM studies are NLP or ML ideas, with LLM or small expert panels as gold labels. No study tests a thinking scaffold on novelty at equal tokens.
- Uzzi's null model uses only 10 random networks (SOM).
- Several LLM results come from 2026 preprints not yet peer-reviewed; model names (gpt-5.5, deepseek-v4-pro) mean results age fast.

## Seen only in snippets or second-hand (not opened)
a11, a12, a13 (Wang 2017, Lee 2015, Foster 2015), b08-b10, b23-b25 (Veugelers and Wang, Mairesse and Pezzoni, Fleming 2001), c04 and c27 (Liu 2025, Kwon and Yang 2025, Kobak 2025), c23-c26 (Uzzi via LLM papers, Lu 2024, Park-Leahey-Funk 2023), c18-c19 details (Chain of Ideas and Nova win rates). Note that a01-a07 and a03's core numbers were opened (by the first agents and re-checked here), but the Uzzi original appears in c23 as snippet only; ignore c23.

## GAPS (most decision-relevant first)
1. Does a scaffold step that adds one distant element to a known frame (the Uzzi pattern) raise blind-rated novelty and correctness of an LLM agent's answers at equal tokens, compared with all-near and all-far candidate sets?
2. Which cheap novelty proxy (token surprisal, embedding distance to retrieved prior work, journal-pair-style distance) best matches blind expert labels, and does any beat chance on a 'not novel' class where every LLM judge scored F1 0.0?
3. Does retrieval of prior work (K = 5 to 10) before accepting a candidate cut the rate of false 'novel' claims in a self-generating agent, and what is the token cost at equal budget?
4. Does the ideation-to-execution novelty drop (-1.049 for AI ideas) also show up for a scaffolded agent when a verification or execution step is added, and can a pre-commit check predict the drop?
5. Is the Uzzi hit-rate result replicated outside Web of Science (OpenAlex, patents, preprints) with a better null model than 10 random networks, and what is its effect size beyond the 2x2 hit cut?
6. What is the effect of team or ensemble diversity (Uzzi's 36.1% to 49.7%) when replaced by multi-sample or multi-persona agents, with diversity measured by distinct-k as in NoveltyBench?
7. How do LLM-judge novelty scores shift when the generator and judge are different model families, and does self-preference explain the gpt-5.5 favouring seen by Sinhahajari et al.?
8. Is there a threshold in distance where novelty stops paying (Lin's extreme-group 61% vs 36% against r=-0.05 overall), and can we locate it on our task bank?
9. Do the findings transfer from NLP/ML idea tasks to the non-research tasks our agent faces (math, planning, puzzles), where novelty is solution-path novelty rather than topic novelty?
10. Have the replication or corrigendum notes (Bornmann 2024 corrigendum, DOI 10.1016/j.joi.2024.101544; Veugelers and Wang 2019) changed any of the validity numbers above?

## Gap search results (evidence_d.jsonl, d01-d17; claims K27-K35 added)
Search note: WebSearch budget was exhausted for the session, and the arXiv, Semantic Scholar and OpenAlex APIs were rate-limited. Sources were found by direct arXiv abs/PDF fetches and read with pdftotext. Publisher pages (ScienceDirect) returned 403.

1. Uzzi-style frame plus one distant element (gap 1): PARTLY CLOSED for humans, OPEN for LLM agents. Hope et al. 2017 (d06): near-purpose far-mechanism inspirations gave 46% good ideas vs 37% random vs 30% near-domain (749 ideas; mixed model 0.71 vs 0.28 and 0.27). No equal-token LLM-agent test exists in what I read.
2. Best cheap proxy (gap 2): STAYS OPEN. Embedding distance has r=.170 with self-rated newness (d13); journal-pair z was weaker (earlier evidence). Nothing found that beats chance on the 'not novel' class.
3. Retrieval cuts false 'novel' claims (gap 3): STAYS OPEN for token cost. Earlier evidence (Shahid, Liu) shows retrieval helps judging. Wen et al. 2025 (d04) shows retrieval alone left o3 near random on outcome prediction, a caution.
4. Ideation-to-execution drop (gap 4): PARTLY CLOSED. Pre-execution scores barely predict execution scores (d03); a trained predictor gets 64.4% on effectiveness (d04). No scaffolded-agent test with a verification step.
5. Replication outside WoS, better null (gap 5): PARTLY CLOSED. SOM robustness read (d14): field fixed effects, top-1% cut, reference-count control, peak near 85th percentile conventionality; null is 10 rewired networks. No outside-WoS replication opened; Shibayama 2021 (d13) validates a different measure. Paywalled sources not read.
6. Ensemble or multi-persona diversity (gap 6): PARTLY CLOSED. Chen 2025 (d05): diverse teams with a leader +0.46 overall, flat past 3 agents, not equal tokens, no distinct-k. Hivemind (d08): 71-82% cross-model similarity. NoveltyBench (d09): in-context regeneration matches human diversity. Equal-token distinct-k test still missing.
7. Cross-family judge shift (gap 7): PARTLY CLOSED on mechanism. Self-recognition drives self-preference (d01: 73.5% for GPT-4); judges favour low-perplexity text (d02). Not measured on novelty ratings; Sinhahajari's gpt-5.5 favouring is plausibly the same effect but not shown to be.
8. Distance threshold (gap 8): STAYS OPEN. Hope 2021 (d07) only hints at a near/far balance. Needs our task bank.
9. Transfer to maths, planning, puzzles (gap 9): PARTLY CLOSED. Code (d10) and maths (d11) path-novelty measures exist; capability does not predict novelty (d11, d12); reasoning scaffolds mostly raise correctness and cut divergence (d10). No planning or puzzle study found.
10. Corrigendum and Veugelers-Wang (gap 10): STAYS OPEN. Both pages blocked (d16, d17). Shibayama 2021 also has a January 2026 correction (content unread).

Claim status changes: K14 moved from single-source to established (d01, d02 give a second independent source on judge self-preference). K19, K13, K11, K04, K01 gained evidence ids but kept status. New claims K27 to K35.
