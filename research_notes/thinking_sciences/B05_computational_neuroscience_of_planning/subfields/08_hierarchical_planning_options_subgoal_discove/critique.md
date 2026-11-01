# B05.08 Cross-check critique: hierarchical planning, options, subgoal discovery

Checked 2026-11-01. Re-opened sources (full text): Machado 2017 (arXiv 1703.00956), Machado 2023 JMLR (2110.05740), Czechowski kSubS (2108.11204), ADaPT (2311.05772), CogEval (2309.15129), Least-to-Most (2205.10625), Solway 2014 (PMC4133163), Tomov 2020 (PMC7162548). 21 claims in claims.jsonl.

## Numbers re-opened (10)
1. Machado 2017: fifth eigenoption first to end at a doorway; 64 options best; Q-learning alpha 0.1, gamma 0.9; 100 trials. CONFIRMED.
2. Machado 2023: four eigenoptions accelerate and never hurt in ten tasks; covering options no gain. CONFIRMED. Setup: 1,000-step episodes, 50 runs (c05 says "50 episodes", b04 says "50 runs"; the paper says evaluated for 50 episodes and averaged over 50 runs, so both are partly right).
3. Czechowski: Sokoban graph size 50: 0.66/0.15, 0.42/0.04, 0.46/0.02; 65% of subgoals improve, 17% worsen; expert 78/67/60. CONFIRMED.
4. ADaPT ALFWorld 71.6 vs 43.3, 43.3, 47.8, 57.5; WebShop 44.0, TextCraft 52.0. CONFIRMED. CORRECTION: the "up to 28.3 points" headline is over ReAct and Plan-and-Execute (both 43.3). Over the best baseline (Reflexion 57.5) the gain is 14.1 points. Evidence lines b20/c10/c21 quote the headline without that qualifier; read it as an upper bound.
5. ADaPT TextCraft depth: depth-2 recipes 26.9 to 78.2; depth-3 recipes 1.8 to 38.7 (vs ReAct). CONFIRMED. CORRECTION: c11 lists "depth-3 recipes 38.7%" without the 1.8% baseline.
6. CogEval: GPT-4 0 of 30 at temperature 0 for shortest path one cluster away; at most 10% at 0.5 and 1. CONFIRMED. Chi-squares 2357.87 (LLM) and 3431.53 (graph) CONFIRMED.
7. Least-to-most: SCAN length 99.7 vs 16.2 (16.7 for another CoT variant); last letter length 12 74.0 vs 31.8 (CoT with more exemplars 37.4/38.4); GSM8K 62.39 vs 60.97, 5+ steps 45.23 vs 39.07. CONFIRMED. Note the GSM8K table also shows CoT 60.87 in one cell; minor.
8. Solway: bottlenecks chosen first 4.4x as often (after chance adjustment); 98% correct on probes. CONFIRMED.
9. Tomov: 58/87, p=0.003; 53/78 bad-structure, bad vs control chi2(1,165)=6.52, p=0.01; N=241 (78 bad, 87 control, 76 good). CONFIRMED. Caveat: the "65% of choices" figure is the model's simulation that replicated the human result; b13 labels it simulation, a19/b12 treat it as human data. Treat as model-matches-human, not as a new human number.
10. Machado 2017 "robust across number of options": CONFIRMED in text ("fairly robust"), but only on one three-domain tabular set.

Not re-opened (taken from the agents, status unchanged): Schapiro 2013, Ribas-Fernandes 2011 (partly seen via cached PMC pages only for title), Momennejad 2017, Xia & Collins 2021, Li & Collins 2025, Jinnai 2019, Nachum 2019, Klissarov & Machado 2023, Voyager, DLLM, CALM, ELLM, PlanBench, LAST.

## Contradictions between sources
- Covering vs eigenoptions: Jinnai 2019 reports covering >= eigen in six domains; Machado 2023 finds covering gives nothing in ten four-room tasks. Authors of the latter attribute it to the single-state initiation set; untested. Different domains, different option counts (8 vs varied), so not a clean replication.
- The topic framing "SR eigenvectors help find subgoals" (Momennejad 2020, Stachenfeld) vs Machado 2017: eigenoptions deliberately do not seek bottlenecks. The bottleneck link comes through the eigenvector sign partition (normalised cut), not through the option set. Both are true; the claims file separates them.
- Nachum 2019 (benefit is exploration) vs Solway 2014 / Tomov 2020 (hierarchy lowers planning cost): different regimes (RL exploration vs search cost). Not in conflict, but only one of them is about a planning agent that already has a model.
- Xia & Collins first-stage negative transfer did not replicate on MTurk; Li & Collins replicates later-block transfer only.
- ELLM: LLM goals "usually match or beat" novelty rewards (c27) but goal conditioning gave no significant pretraining gain (c13). Task and seed dependent.

## Weak spots
- Human evidence for subgoal discovery rests on small samples (EEG N=9, fMRI N=14 and 30, Solway Exp 2 N=10) and a handful of graph tasks.
- All eigenoption results use small tabular grids, or Atari with qualitative plots. There is no test on a reasoning or text task.
- No LLM study in the evidence tests SR/eigen-style or bottleneck subgoal discovery directly. LLM work covers hand-built or prompted decomposition (ADaPT, least-to-most, kSubS, Voyager, DLLM), none of which discover subgoals by graph structure.
- ADaPT compares arms with different numbers of model calls; gains are not at equal tokens. Same for Voyager vs prior agents.
- kSubS subgoal generators are trained on domain data; no zero-shot prompt-only analogue measured.
- Single-source status for 11 of 21 claims.

## Only seen in snippets or secondhand
- Jong, Hester, Stone 2008 (b11): secondhand, original not opened.
- Sutton, Precup, Singh 1999; McGovern & Barto; Simsek & Barto; Menache (a30, a31): described, not opened. Feudal Networks and Option-Critic (b24, b25): not read for numbers.
- Wu, Tucker, Nachum 2019 (b06): abstract and method only.
- Machado 2018 count-based exploration (b23): no scores recorded.

## GAPS
1. Does any study (2023-2026) test automatic subgoal discovery from a text-reasoning trace (bottlenecks, clustering of solved-problem steps) in an LLM agent, with a matched-token comparison against hand-written or prompted decomposition?
2. In LLM agents, does as-needed decomposition (ADaPT style) still beat always-decompose and best-of-N at equal total tokens, and on frontier models (not GPT-3.5)?
3. What is the right library size and granularity for LLM subgoals: is there a sweet spot like kSubS k=3-4 and the "four eigenoptions" result, measured on language tasks?
4. How reliably can an LLM judge "subgoal reached" or "subgoal still valid" (CALM F1 as low as 0.16 on NetHack), and does a verifier fix it (Voyager self-verification: minus 73%)?
5. How large is negative transfer from stale stored subgoals in LLM agents, and which invalidation rule (version tag, precondition check, test run) removes it? Humans show it (Xia & Collins; Li & Collins), LLM data is missing.
6. Do human bottleneck and community-structure effects (Solway 4.4x; Schapiro) replicate in LLMs given a graph in text, and does CogEval's near-zero cluster-crossing path success (GPT-4 0/30) change with newer reasoning models or with an explicit graph tool?
7. Do covering options or eigenoptions beat bottleneck options when the "graph" is a learned or approximate problem-state graph (noisy, partial)? The covering-vs-eigen dispute is unresolved and untested outside grids.
8. How much of subgoal-library benefit in LLM agents comes from exploration diversity versus from structure (Nachum 2019 finding in RL)? A flat agent given the same diverse samples is the missing control.
9. Which cost accounting makes hierarchical planning pay: Solway's search-cost model predicts hierarchy helps only above some problem size. Where is that threshold for LLM reasoning tasks?
10. Replication of the PPE (pseudo-reward prediction error) result with larger N and tasks beyond the delivery game; its relevance as a design cue for a separate subgoal-progress check is unproven.

## Gap search results

Evidence in `evidence_d.jsonl` (d01-d18); new claims K22-K27 and updated notes on K14, K17, K19, K20. Search budget (WebSearch quota and arXiv 429s) ran out partway, so gaps 7, 9 and 10 got no new primary source.

1. Automatic subgoal discovery from text traces (gap 1): PARTLY CLOSED. ARISE (arXiv 2606.02994, d01) does exactly this and beats other learned memories (67.4 vs ReAct 38.8 on DeepSeek-V3; 77.7 vs 68.2 on Gemini 2.5 Flash). Still open: no token-matched comparison with hand-written or prompted decomposition. A counter-result (d11) shows mined GUI skills lose to a frequency baseline.
2. As-needed vs always-decompose at equal tokens, frontier models (gap 2): OPEN. ADaPT matched LLM calls, not tokens, and has no always-decompose arm (d05). Select-Then-Decompose (d06) shows explicit decomposition costs 4-10x tokens with no gain on GSM8K, which supports gating but is not ADaPT.
3. Library size and granularity (gap 3): PARTLY CLOSED. ARISE K=3/5/10: K=10 never best (d03). Distractor-skill study shows recall falling from 73.6% to 27.4% at 1,000 added skills (d07). Supports a cap near 5 (K24). Granularity (how big each subgoal is) was not measured.
4. LLM judging of subgoal reached; effect of a verifier (gap 4): OPEN. Only whole-trajectory judges found (no judge above 70% precision, d15). CALM re-opened but 0.16 F1 not re-derived (d16). No verifier-vs-no-verifier arm at subgoal level.
5. Damage from stale stored subgoals and the invalidation rule (gap 5): PARTLY CLOSED. Closest data is on stored reasoning macros, not subgoals: counters serve 7.0-13.5x (35-73x on code) more stale answers than a certified rule; explicit edit notice plus likelihood-ratio detector gave 0 stale (d08). Test-run style certificates worked best. Version tag vs precondition check vs test run were not compared head to head. Authors' own preprint.
6. Bottleneck and community effects in LLMs (gap 6): OPEN. CogEval re-read (d14): GPT-4 0 of 30 at temperature 0, at most 10% at other temperatures. No reasoning-model or graph-tool retest found.
7. Covering vs eigen vs bottleneck on learned or noisy graphs (gap 7): OPEN. LDSC (d13) uses LLM subgoals but has no such arm.
8. Exploration diversity vs structure (gap 8): OPEN. SkillRL ablation shows hierarchy worth 11-13 points over a flat list (d10) but has no same-sample flat control.
9. Size threshold for hierarchy to pay (gap 9): OPEN, no source found. Indirect: decomposition did not help on easy GSM8K (d06) while ADaPT gains grew with recipe depth (d05: depth 2 26.9 to 78.2, depth 3 1.8 to 38.7).
10. Pseudo-reward prediction error replication (gap 10): OPEN, nothing found.

Still weak: d12, d13, d16 are method-level reads without per-cell numbers; d17 and d18 not opened. Several 2026 sources are single-group preprints (d08, d09, d11).
