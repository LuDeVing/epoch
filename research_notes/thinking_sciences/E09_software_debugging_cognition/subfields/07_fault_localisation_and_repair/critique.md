# Critique: E09.07 Fault localisation and repair (cross-check)

## Numbers re-opened this session (arXiv full text, pdftotext)
Confirmed unchanged: AutoFL +19.7% / +166.7% / +233.3% and Spearman 0.57 (a11, b18, c01, a12, c03); LLMAO 88 (22.3%), 149 (37.7%), 183 (46.3%) and "84.8% improvement over Ochiai" (a16, b21, c19); Agentless 32.00% (96), $0.70, file hits 78.7 / 67.7 / 81.7 (a24, b23, c26); SWE-Bench+ 32.67%, 31.08%, 12.47% to 3.97% (b26); Olausson 1.05x and 0.97x, feedback 42.64 vs 62.21, 19.33 vs 45.67, 33.30 vs 52.60 (a28, a29); AgentFL 157/395, $0.074, 97 s (a17, c07); Wu et al. 23.13, +46.9%, -49.9% class level (a14, c10); Rondon 25.6/73/17.9/43 (b29); RepairAgent 164 bugs, 16 bugs for $29, 25% / 81% (a20, a21, c20, c22); Xia and Zhang 162/337, $0.42, 114 and 48 (a19, c23).
Corrections and notes:
- No numeric corrections were needed on these. Note the 78.7% also appears in the Agentless leaderboard table as a SWE-agent column; the localisation 78.7% is a different quantity (prompting-based file retrieval).
- a21: the "subset size not stated" gap is closed. The 16 bugs at $29 compares with 21 bugs at full-oracle localisation (c21, c22); the 25% drop is 21 to 16. The paper reports this on a small subset, not all 835 bugs; do not quote 25% as a general effect.
- a08 was "recalled, unverified" but is confirmed by b12 (same 2 of 105 figure), so the claim is now backed by an opened source.
- Not re-opened (no arXiv/open text found quickly): Parnin and Orso 2011 numbers (b01-b05), Xia 2016 user study (b06-b09), Qi 2015 (b12, b13), Pearson 2017 (b10, b11), LLM4FL (c13-c15), FlexFL (c16, c17). These stay as reported by earlier agents (marked opened:true by them); treat as unverified by me.
- Duplicate counting: a11, b18, c01 are one paper (AutoFL); a16, b21, c19 one paper (LLMAO); a14, c10 one paper (Wu); a17, c07 one paper. Independent source counts in claims.jsonl reflect papers, not lines.

## Contradictions
- Parnin and Orso (no overall speed gain, N=34 students, 2 programs) versus Xia et al. (2x faster, 36 professionals, 16 Defects4J bugs). Likely causes: tool accuracy, participant skill, bug difficulty, and that Parnin used a Tarantula ranking on whole programs. Xia's own mediocre-tool arm still beat no tool, which is hard to square with Parnin; the studies differ in design, so no clean replication exists. Status contested.
- GenProg success 59% (a05, own metric: passes tests) versus 2 of 105 correct (b12). Not a contradiction of numbers but of the meaning of "fix". Benchmarks also differ (10 programs vs 105 defects).
- FlexFL's rerun of AgentFL gives 144 on a v1.2 subset versus 157 in the AgentFL paper (c09). Different subset and model version; weak evidence of fragility only.
- Top-1 numbers across benchmarks are not comparable: Defects4J v1.0 (353), v1.2 (395), v2.0, function vs line level, with or without tests. LLMAO line-level 22.3% and AutoFL method-level numbers must not be set side by side.
- Time comparison of AutoFL 87 s vs SBFL 112 s (a12, b19) compares across papers and hardware.

## Weak spots
- Almost all LLM localisation results are Defects4J (Java, public, pre-cutoff). Memorisation is shown for SWE-bench (b28) but not tested directly for Defects4J; Wu et al. use class-level drop as only indirect evidence (c12).
- Cognitive-science link is thin: only Parnin and Orso, Xia 2016 and Kang user studies measure humans. No study measures whether a localisation list changes how an LLM agent reasons.
- Cost and token accounting is inconsistent (dollars, seconds, tool calls). Equal-token comparisons are rare; Agentless and Xia and Zhang come closest.
- Seen only in snippets: c06 (AutoFL 149/353), a09, a10 (Semantic Scholar counts only), a13 and a22 (figures only).
- Ablation numbers (c08, c14) come from the authors' own systems and are single runs.
- Gaugerty/others on human localisation strategy belong to other subfields and are not repeated here.

## GAPS
1. At equal tokens, does a spectrum (Ochiai) hint added to an LLM agent's prompt help, harm, or do nothing versus the agent localising alone? No study isolates this.
2. Does an inaccurate suspect list anchor the LLM agent (as mediocre lists did not harm humans in Xia 2016 but wasted time in Parnin 2011)? Dose-response by list accuracy is untested for agents.
3. How much of Defects4J and BugsInPy localisation performance is memorisation? Needs post-cutoff or mutated-identifier tests for Defects4J, as done for SWE-bench.
4. Is there a reliable stop rule after the fault is found (humans kept inspecting 61% extra time)? Do agents over-verify or under-verify?
5. How well do self-consistency and verbalised confidence predict localisation correctness beyond AutoFL (rho 0.5)? Can it gate extra search at fixed budget?
6. When does re-localising after failed patches beat sampling more patches (RepairAgent 6 vs 17 write calls, Olausson 1.05x)?
7. Which faults defeat all methods (missing code, custom test helpers in Closure, multi-file)? RepairAgent fixed 4 of 81 multi-location bugs; what scaffold step helps?
8. Does test-free (LLMAO-style) localisation add value to test-based agent localisation, or is it redundant once an error log is present?
9. What is the real-world transfer gap (Google human-reported 17.9% valid) and which part is bug-report quality versus localisation?
10. Are hypothesis-then-experiment prompts (AutoSD) better than plain reasoning at equal tokens once real execution is available (73% vs 63% plausible with real vs hallucinated)?

## Gap search results (evidence_d.jsonl, d01-d17; claims K21-K26 added)
Search note: WebSearch quota ran out and arXiv and Semantic Scholar APIs returned 429, so papers were opened directly by arXiv id. All 17 lines are opened:true.

1. Ochiai hint at equal tokens: PARTLY CLOSED. No equal-token study exists. Best evidence: FuseFL ablation (324 student faults, GPT-3.5) SusScore 169 vs CoT 163 Top-1 (+3.7%), test results 187; Codeflaws (3,902 bugs) +0.4 to +4.3 points from adding SBFL in three Llama models. Small gain, no harm seen (d01, d02). Still open for agents on real repos.
2. Anchoring by inaccurate list: OPEN. No LLM study varied list accuracy. Related: Liu et al. found agents fixate on issue keywords (d15).
3. Memorisation of Defects4J: LARGELY CLOSED for repair, OPEN for localisation. Defects4J 80% in TheStack; renaming cuts repair success 4.1 to 16.0 points; post-cutoff GitBug-Java mostly shows no significant drop for Claude-3.7 and GPT-4o (d03, d04). A localisation-only test is still missing.
4. Stop rule: PARTLY CLOSED. Agents do both: stop without a valid test and loop (54 rounds vs 25 to cover 80% of failures); overthinking correlates with lower resolution (d07, d08, d16). No study measures extra checking after the fault is actually located.
5. Confidence gating: OPEN, with a warning. General code confidence is poorly calibrated (ECE 0.09 to 0.73, d11); no new localisation-specific data beyond AutoFL.
6. Re-localise vs resample: OPEN. CodeMonkeys shows serial and parallel spending are similar at equal cost (d12); backtracking and supervisors help but are not compute-matched (d16, d17).
7. Faults defeating all methods: PARTLY CLOSED. Multi-file issues: 25.3% vs 55-58% single-file; 96 of 500 SWE-bench Verified issues unsolved by all six systems (d05, d14). No scaffold step has been shown to fix them.
8. Test-free localisation vs error log: PARTLY. Brute-force file scan gets 92.6% file recall at about 15% of cost (d13); test results beat other single inputs (d01). Added value over an error log is still untested.
9. Benchmark vs industrial gap: PARTLY CLOSED. Solution-in-report quality drives the gap (1.95x vs 1.01x for reproduction examples, d06). Still one industrial study (Google).
10. AutoSD at equal tokens: CLOSED for accuracy, negative. With 10 samples each AutoSD did not beat plain prompting (76 vs 87 and 113 vs 110 correct on Defects4J; d09). Real execution matters (73% vs 63% plausible, d10). Token-matched version not run.

Caveats: the FuseFL Top-1 row was read from garbled PDF text and checked against the prose; the 18.3% and 11.3% multi-file figures in d14 were not fully legible; SWE-Search (d17) was read at abstract level only.
