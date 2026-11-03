# D05.02 Process models: cross-check critique

Scope: evidence_a/b/c (78 lines). Claims in claims.jsonl (K01-K21).

## Sources re-opened (full text, this session)
Huang 2024 (arXiv 2310.01798), Self-Discover (2402.03620), Plan-and-Solve (2305.04091), Friedman 2026 (2603.06878), Self-Refine (2303.17651), Cognitive Prompting (2410.02953), Peczuh 2025 (2510.12915). Abrami, Garrison, CQoT, CRITIC, Reflexion, Dewey, SEP were not re-opened (relied on the finders' opened:true).

## Corrections
1. MAJOR. Huang et al. oracle-label result was misread in a25, c04 (and any text copying them): "oracle lifts GPT-3.5 GSM8K from 75.9 to 95.5" is WRONG. The PDF table 2 text is scrambled; read by row: GPT-3.5 standard 75.9 / 75.8 / 26.0 (GSM8K / CSQA / HotpotQA), GPT-3.5 oracle 84.3 / 89.7 / 29.0; GPT-4 standard 95.5 / 82.0 / 49.0, GPT-4 oracle 97.5 / 85.5 / 59.0. The 95.5 is GPT-4's plain score, so the oracle gain on GSM8K for GPT-3.5 is +8.4, not +19.6. a25 ("Oracle stop lifts GPT-3.5 ... 75.9 to 95.5") and c04 should be treated as wrong. K05 uses the corrected numbers.
2. Friedman 2026 (a15): long-output, LLM-correct accuracy is 79.5% (CI .542-.927), not "about 81%"; LLM-wrong long is 30.7%. The 81.1% is medium. Overall range 71 to 81% is right. N=24, 15 items confirmed.
3. Huang Table 3 (GPT-3.5 and GPT-4 intrinsic): confirmed. Column labels in the PDF are scrambled, but the sequence 75.9/75.1/74.7, 75.8/38.1/41.8, 26.0/25.0/25.0 and GPT-4 95.5/91.5/89.0, 82.0/79.5/80.0, 49/49/43 matches. Note the "# calls" column (1,3,5) is calls, not rounds.
4. Confirmed with no change: Self-Discover table (PaLM 2-L 56/30/45, +CoT 60/40/42, +PS 61/42/49, +SD 67/69/50.5; GPT-4 58/51/70.5, 75/52/71, 73/53/70, 81/85/73); Plan-and-Solve averages 70.4/73.5/76.7; Self-Refine 20% absolute average claim and the math 64.1 to 64.1 row, dialogue 36.4 to 63.6, sentiment 8.8 to 30.4; Cognitive Prompting 95% on LLaMA 70B and the GC-DC-PR order; Peczuh accuracies (.604, .563, .543, .532), RMSE .933, alpha .606, kappa 0.87.
5. Self-Refine "average 20%" is a headline over mostly preference tasks; per-task gains range from 0 (math) to +32 (sentiment). Do not quote 20% as a general effect.
6. Self-Discover "+39%" headline on T4D is against direct prompting (30 to 69) for PaLM 2-L; against CoT it is +29.

## Contradictions between sources
- Huang (intrinsic self-correction fails) vs Self-Refine (large gains): reconciled by task type (preference-judged vs reasoning with a ground truth) and by prompt design (Huang argues Self-Refine style gains partly come from weak initial prompts). Status kept "contested" (K07).
- Hitchcock/SEP advise postponing hypotheses until evidence narrows them (b02); Dewey's model puts suggestion before testing. The two are in tension; no empirical test.
- Dewey 1910 lists the difficulty first; 1933 starts with suggestion (a05). Edition differences matter for "S1".

## Weak spots
- Zero order-ablation studies were found (a24, b27). The central question for S1-S9 (does order matter) has no direct evidence; all LLM support is indirect and from different framings (Polya, Toulmin, self-refinement).
- Only two non-math domains tested for CQoT; judged by an LLM on MT-Bench (judge bias).
- Most LLM evidence is on 2023-vintage models (GPT-3.5, text-davinci-003, PaLM 2). Newer reasoning models (o-series, R1) show different behaviour (b22 overthinking); results may not transfer.
- Human CT-education evidence (Abrami, Huber and Kuncel) concerns teaching students, not process order; only loosely relevant.
- Equal-token comparisons are rare: Self-Discover and Plan-and-Solve compare to CoT without sample-matched baselines; Huang's own critique concerns exactly this (self-consistency at equal calls beats self-correction).

## Seen only in snippets or not opened
a22 (Wallas), a23 (Ennis), b12 (Rourke and Kanuka, snippet), b13 (Klahr and Dunbar N=10 from a summary), b14 (Kuhn et al., no percentages). Do not cite their numbers.
Search notes: arXiv and OpenAlex were reported unavailable to finder B; nothing on Watson-Glaser-style LLM benchmarks beyond Friedman 2026 and Peczuh 2025 was found.

## GAPS
1. Does the order or presence of stages (define, hypothesise, reason, test) change accuracy at equal tokens for LLMs? Need direct ablation (permute/skip) studies, or run our own.
2. Which review step survives equal-token comparison with simply drawing more independent samples (self-consistency, best-of-N), for current reasoning models rather than GPT-3.5 and GPT-4?
3. What external signal is cheap enough to gate revision (tests, tool calls, retrieval, a separate verifier) and how much of the oracle gain (Huang: +8 to +10 points) does it recover?
4. Do modern reasoning models already perform Dewey-like back-steps internally (the mechanistic study c14 hints at stage structure), so that explicit scaffolds are redundant or harmful?
5. When should the agent stop? Evidence on learned or rule-based termination for the test stage (overthinking, b22) is thin; what stop rules work?
6. Is there evidence of the problem-definition stage helping on underspecified or adversarial items (missing premises), rather than on clean math benchmarks?
7. Do human critical-thinking tests (Watson-Glaser, CCTST, Cornell) have published LLM results by subskill, and does the subskill profile map to S1-S9?
8. How reliable are LLM judges of process quality (kappa vs human) for scoring stage adherence, given Peczuh's .54 to .60 accuracy?
9. What does the human literature say about premature closure and stage skipping (Klahr and Dunbar dual-space search, Kuhn) with verified numbers, to set agent guardrails?
10. Is the 41% base-accuracy threshold for useful critique (CriticBench) reproducible with newer models, and can it gate S-stage review?


## Gap search results
Sources opened in full text this session (PDF to text): Self-Correction Bench, Tyen 2024, Stechly 2024, Self-Debug, DEER, Answer Convergence, Overthinking, Gandhi 2025, QuestBench, ProcessBench, Zheng 2023 judge paper, Snell 2024, Zhang 2025, Wang 2023, Chen 2024, Kamoi 2024. WebSearch was refused (shared budget used up); OpenAlex and Semantic Scholar were rate limited; the arXiv API gave 429, so only direct PDF fetches worked. New evidence: evidence_d.jsonl (d01-d16). Claims K22-K29 added; K02, K04, K05, K06, K12, K13 got extra evidence ids.

1. Order/presence of stages: PARTLY CLOSED. No stage-order ablation exists, but step order (d01: GSM8K 48.5 to 23.1 when order is broken) and premise order (d02: over 30 points) are causal. Our own define/test permutation is still needed.
2. Review vs more samples at equal tokens: PARTLY CLOSED. Stechly (GPT-4): resampling plus verifier matches critique; Snell: depends on difficulty. No test on current reasoning models: open.
3. Cheap external gate: PARTLY CLOSED. Sound verifier or unit tests (Self-Debug, up to +12 points with tests; Stechly) and an error-location classifier at about 65% accuracy (Tyen). Share of the oracle gain recovered is not measured in one study: open.
4. Reasoning models back-step internally: CLOSED in direction (d05, d06): no blind spot in reasoning models; scaffold likely redundant there.
5. Stop rules: MOSTLY CLOSED (d07-d09). Learned stop for hard items; no test inside a Dewey-stage agent.
6. Define stage on underspecified items: PARTLY CLOSED (d10, plus b22). No study shows a define stage fixing it; CoT did not help.
7. Human CT tests (Watson-Glaser, CCTST, Cornell) by subskill for LLMs: STAYS OPEN. Search blocked; nothing found.
8. Judge reliability for process quality: PARTLY CLOSED (d12, d13); stage-adherence judging unvalidated.
9. Klahr and Dunbar / Kuhn verified numbers: STAYS OPEN. Publisher PDF not retrievable; b13 and b14 remain unusable.
10. CriticBench 41% threshold with newer models: STAYS OPEN. Tyen's about 65% classifier accuracy and Self-Correction Bench give related but different thresholds.
