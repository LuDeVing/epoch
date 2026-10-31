# A02.03 Impasse-driven subgoaling and chunking: cross-check

Checked 2026-10-31. Sources re-opened this session (full PDF text): SkillsBench (2602.12670), ADaPT (2311.05772), NL2GenSym (2510.09355), Kirk et al. (2208.09554), Wang et al. anti-persistence (2610.27406), Agent Workflow Memory (2409.07429), Tambe et al. 1990, Heathcote et al. 2000, CogRec (2512.24113), Soar manual ch. 4 (html, 1263 string found).

## Confirmed
- SkillsBench: 33.9% to 50.5%, +16.6 pp, 18 configs, 9,396 trajectories, 13 of 87 tasks worse; self-generated -8.1 / -11.3 / -11.5 pp (Opus 4.7, GPT-5.5, Gemini 3.1 Pro). Matches b16.
- ADaPT: ALFWorld 71.6 vs ReAct 43.3, Reflexion 57.5; Pick2 52.9 vs 5.9 (Reflexion) and 11.8 (ReAct); WebShop 44.0; TextCraft 52.0. Matches c13, c14, c26.
- Kirk et al.: Search+LLM 54%, 96% correct actions, 30% goal relevancy in depth-4 condition, 70 instructions minus 43 yes/no. Matches b12, c06.
- Wang et al. 2026: 59.9 / 53.5 / 49.0 / 49.3 / Reflexion 52.9. Matches b21.
- AWM: +24.6% and +51.1% relative, 35.5 vs 23.5, 8.9 to 14.0 points. Matches b23, c16.
- Heathcote et al.: 40 data sets, 7,910 series, 475 subjects, 24 experiments; Seibel averaged power R2 .9858 vs exponential .9584; 76.4%. Matches a09. (b10 and b11 list this as not opened; a09 did open it. Treat the numbers as verified; Evans et al. 2018 is still unopened.)
- Soar manual: 1263 string present in the manual page (a16, c02).
- Tambe Table 1: cognitive and computational effects match a12/b03.

## Corrections
1. Tambe total speedups. The extracted table is shifted by half a row. Recomputing cognitive x computational effect and matching to the text (Magic-square 0.25): Eight-puzzle about 0.99, 2-Queens 0.32, Grid 0.85, Magic-square 0.25; Syllogisms 10.27, Monkey and bananas 5.16, Water jug 5.22, Farmer 5.04. So Eight-puzzle is roughly break-even, not a clear slowdown, though the paper groups it with the four expensive tasks. The per-task chunk counts are 11, 3, 14, 5, 10, 4, 11, 14 (likely), not 142/86 as read in a13/b05; those larger numbers came from other tables (unique-attribute comparison) and were unreliable. Do not cite them.
2. a12 calls the computational effect "time per action before/after". It is a ratio (before over after); values below 1 mean each action got slower.
3. NL2GenSym (c10/c11): "one-shot" baselines are Gemini-2.5-Pro and Qwen-max; the framework used a cheaper Gemini 2.5 variant (labelled "FP" in the table) and Qwen-max. "Hard cases: one-shot 20% vs 76.67% (Gemini)" is right. Manual hard SR is 46.67%, manual overall SR 84%, manual decision cycles 3390x optimal. Ablation (no critic -23%, no knowledge base -17%, no case base -14%) matches text.
4. SkillsBench versions. a25/b26 cite an older version (+16.2 pp curated, -1.3 pp self-generated, Opus 4.6). The final paper reports -8.1 to -11.5 pp for self-generated on three configs. Use the later primary numbers; the sign agrees, the size does not.
5. CogRec results table is garbled; reordering rows by the "+5.7%" line gives CogRec ML-1M HR@10 0.3124 against Soar-alone 0.2956 and LLM-Direct 0.2815. Improvements over the best baseline are 4.1 to 9.1% across metrics. a23/c08 said "above all baselines" without size. No ablation numbers appear in text, only a figure.
6. b21: "best in 7 of 9" is correct; it beat joint memory in 8 of 9 (not all 9) and trajectory and abstraction in all 9.
7. Attribution: the c24 and b09 rows are not evidence (unopened, placeholders). b09 points to a wrong URL. Ignore both.

## Contradictions between sources
- Self-written skills hurt (SkillsBench) versus compiled workflows help (AWM, Voyager-type). Difference: AWM induces from verified successes; SkillsBench self-generated skills are written before the task. Neither is an impasse-triggered test.
- Insights vs trajectories: ExpeL says insights plus examples is best and the split is task dependent; anti-persistence says abstractions mislead. Both are authors' own methods on ALFWorld-like tasks.
- Cost: Soar authors say analysis overhead is minimal and gains outweigh costs (Laird 2022, via Assanie); Tambe 1990 found four of eight tasks slower. Different eras and matchers; no LLM-agent equivalent measured.
- Power law (Rosenbloom and Newell) versus exponential (Heathcote, Evans). Unresolved; matters only if we model library gains.

## Weak spots
- Almost all LLM evidence is authors' own methods on ALFWorld, WebArena and similar. No study triggers compilation by an impasse in a reasoning task and measures correctness of reused entries.
- Founding Soar evidence is toy puzzles with hand-designed representations and hand-picked trials; generality claims are partly design choices.
- Newell 1990, Laird-Newell-Rosenbloom 1987, Assanie 2022, Doorenbos, Rosenbloom and Newell 1987b, Evans 2018, Voyager numbers were not opened.
- Several 2026 arXiv items (anti-persistence, self-evolving, SkillOps, AgentDebugX, mechanism review) are single preprints with no replication.
- Only seen in snippets or secondhand: a18, a20, a26, a27, b09, b10 (now verified), b11, c24, c25.

## GAPS
1. Does an impasse-triggered, test-gated library beat the same library filled after every success, at equal tokens, on reasoning tasks (not web or household tasks)? No study separates the trigger from the gate.
2. What false-reuse rate do compiled subgoal entries have on near-duplicate tasks that need a different fix? Soar's correctness theory exists, but no LLM measurement does.
3. How many entries retrieved per state is best, and where does retrieval cost overtake the saved steps (the LLM version of Tambe's expensive chunks)? Measured: 1 to 3 skills best, but only on SkillsBench.
4. Which impasse types matter for an LLM agent (nothing to try, tie, stalled option, repeated no-change), and does typing the trigger beat a single generic stuck trigger? No ablation exists.
5. Does storing a raw checked case beat storing a distilled rule for subgoal reuse? ExpeL and anti-persistence disagree; the 2026 result is from one group.
6. What does Assanie's EBBS thesis report in numbers (14 agents, 8 domains, 12 correctness issues)? Open and read it for the checklist of wrong-reuse causes.
7. Do Voyager's verified-skill numbers hold when re-read from the primary paper, and how much of its gain comes from verification versus the library?
8. Does the call-frequency drop seen in CogRec appear in a frozen-LLM reasoning scaffold, and over how many tasks does it plateau?
9. How should an entry go stale or be demoted (match then fail), given Soar has no deletion mechanism? SkillOps gives one maintenance design; no head-to-head exists.
10. Is the power-law versus exponential question relevant to library gain curves, or only to human practice data? Check Evans et al. 2018 and any LLM learning-curve study.

## Gap search results (evidence_d.jsonl, d01-d18; claims K28-K34 added)

Search quota ran out and some hosts blocked downloads (Michigan repository, figshare, Semantic Scholar, OpenAlex), so two sources stayed unopened.

- Gap 1 (trigger vs gate): PARTLY CLOSED. The gate half is measured: ASI verified vs unverified induction gives about +4 points (32.6 to 36.4, d12); Xiong et al. show strict selection beats add-all and coarse selection (d05); Dynamic Cheatsheet shows append-everything can fall below baseline on AIME (d09). The trigger half (impasse vs after every success) is still untested. OPEN.
- Gap 2 (false-reuse rate): OPEN. Only qualitative reports (d10, d05 "experience-following"). No counted rate on near-duplicate tasks.
- Gap 3 (entries per state, retrieval cost): OPEN. Voyager used top-5 with 96.5% retrieval accuracy (d02); no sweep. SkillsBench 1-3 remains the only sweep.
- Gap 4 (typed vs generic trigger): OPEN. DPR uses a 5-step low-progress gate (d15) but the ablation was not found.
- Gap 5 (raw case vs distilled rule): STILL CONTESTED. ReasoningBank (d07, d08) favours distilled lessons; Wang 2026 (K15) favours raw cases. Differences in judge and benchmark, not resolved.
- Gap 6 (Assanie 2022): OPEN for the thesis (blocked, d17). The Soar manual's correctness list was read (d04) and works as the checklist. The 14 agents / 8 domains figures are not confirmed.
- Gap 7 (Voyager): CLOSED on numbers (d01-d03). Verification mattered more than the library (-73% items vs plateau only); the verified-library effect is concentrated at later tiers and transfer; verification also steers retry, so not a pure gate.
- Gap 8 (CogRec in a frozen scaffold): PARTLY CLOSED. The ablation text confirms a call-frequency plateau with chunking (d14) but gives no task count and no frozen-scaffold test.
- Gap 9 (demotion): PARTLY CLOSED. Xiong et al. give a measured rule (n retrievals plus mean utility) that helps only with a reliable judge (d06). No head-to-head with SkillOps.
- Gap 10 (power vs exponential for library curves): OPEN. Evans 2018 not opened (blocked, d16). No LLM study fits a curve; Voyager, LEGO-Prover and Dynamic Cheatsheet show flat-then-rising shapes (d01, d11, d09).

Cautions: AIME sets are 30 questions (one question is 3.3 points), so Dynamic Cheatsheet gains are noisy. Table cells in Xiong et al. and some CogRec figures were garbled in text extraction and are not cited. Search-result summaries gave 4.9 vs 3.3 for LEGO-Prover; the arXiv text says 3.3. d15, d16, d17, d18 are weaker (event page, or unopened).
