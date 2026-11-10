# E13.04 Cognitive artifacts: cross-check critique

## Numbers re-checked against source text (10+)
Confirmed in the downloaded paper text:
1. SWE-agent GPT-4 Turbo 12.47% (286/2,294) full, 18.00% (54/300) Lite. Confirmed.
2. SWE-agent ablations (edit/lint 18.0/15.0/10.3; search 18.0/12.0/15.7; window 100/30/full 18.0/14.3/12.7; history 18.0/15.0). Confirmed. 51.7% (1,185/2,294) with a failed edit. Confirmed.
3. Tam et al.: 0.148% parse error vs 38.15% gap; GSM8K gpt-4o-mini 94.57 / 87.17 / 86.95 / 91.71. Confirmed.
4. Hsieh et al.: docs-only F1 0.37 (davinci-002), 0.45 (gpt-3.5); docs plus demos 0.35 text-davinci. Confirmed.
5. PAL: GSM8K 72.0; GSM-HARD 61.2; CoT 23.3 on GSM-HARD. Confirmed.
6. Cognitive tools: GPT-4.1 AIME2024 32.0 / 42.0 (prompting) / 53.0 (tools); +4.2 to +27.2. Confirmed.
7. RAG-MCP: 43.13% accuracy, 1084 prompt tokens (actual-match baseline 18.20%, 1646 tokens). Confirmed.
8. Kosmyna: session 1, 15/18 (83.3%) of LLM group failed to quote vs 2/18 in the other two groups. Confirmed.
9. Hesselmann: sequential BF01 = 5.07 for the null at N=89. Confirmed.

## Corrections
- c01 says the shell-only agent is "10.7 points lower". The paper text says 10.7 points, but its own Table 1 gives Shell-only 11.00 vs SWE-agent 18.00 (7.0 points), and "64% relative" matches 7.0/11.0. The claims use 7 points and flag the text-table mismatch. (Shell-only on full SWE-bench is 1.46 in the table; unclear if that is the same variant.)
- a16 and b02 give HumanEvalFix as 87.7 while the paper text says 88.3% pass@1 in one place; the table shows 87.7 for Python. Use 87.7 for Python only.
- b16 (session 4: 78% / 11%) is right but each group has only n=9 (7/9 vs 1/9), not 18. a15 says 18 in session 4; that is the two groups together. Always cite 7/9 and 1/9.
- a19 "ReAct vs Act 71 vs 45" is best-trial only; the claim is stated with that limit.
- c20 names Hesselmann and Gollo as authors; a09 names Hesselmann alone. Not resolved. Cite as Hesselmann (2020).
- c06 and c17 recorded no numbers; the claims use b06/a22 numbers instead.

## Contradictions between sources
- Interface gains vs Agentless (b04): a fixed pipeline with no tool loop reached 32.00% on Lite, above SWE-agent's 18.00%. The interface effect is real but relative to a weak baseline; it is not proof that an agent loop is needed.
- ReAct: wins on ALFWorld/WebShop, loses to CoT on HotpotQA (27.4 vs 29.4). So "interleave tools and thought" is task-dependent.
- Memory: Reflexion stores history and gains; SWE-agent finds full history worse than last 5 observations.
- Position: lost-in-the-middle is from 2023 models; no source in these files tests 2025-26 models.
- Human offloading: strong reminder benefit (a13) vs reliance cost (a14, b21, b16). Both can hold: benefit now, loss of self-maintenance later.

## Weak spots
- The founding human work is mostly unread: Norman 1991 (a05), Hutchins 1995 (a06), Larkin and Simon 1987 (a08) not opened; Zhang and Norman 1994 (b01 opened, but a07 says not) and Kirsh and Maglio (a01 opened, b26 says not). Evidence files disagree on opened status for the same paper. Treat only the opened lines as verified.
- Most LLM results are single run, one model, one benchmark (SWE-agent GPT-4 Turbo, 300 tasks; 1-3 point gaps are near noise; the paper's own 6-run Lite spread is about 17.3-18.7).
- Brain-drain and Kosmyna sample sizes were taken from abstracts or secondary reports; Kosmyna is a preprint with n=9 per cell in session 4.
- b11 (scratchpad Fig. 3) read from plots only. c06, c17, c24, b15 lack exact numbers.
- Camerer 2018 only seen through secondary text (a10, b17).
- None of these LLM studies hold tokens equal across the artifact and the no-artifact arm; costs are 8-13x higher for SWE-agent.
- Human-to-LLM mapping is by analogy only. No source tests a cognitive-artifact prediction (e.g. rules in the display) on a language model directly.

## Seen only in snippets or abstracts
Ward et al. replication (a11, b18), Boettger meta-analysis (b19, pooled size missing), Fisher et al. (b22), Buchli and Storm (b24), Gorilla accuracies (b15), CodeAct per-model results, Parasuraman and Manzey (b27, recalled).

## GAPS
1. Does a designed code interface (validator, summary view, limited window) still beat a plain tool at equal tokens on a current model, or was the 2024 gain a weak-baseline effect (Agentless contradicts)?
2. Which parts of the Zhang and Norman (1994) result transfer: does putting rules into each prompt state (not only the system prompt) lower constraint violations for an LLM?
3. How much does output format (free text vs JSON vs code) tax reasoning on 2025-26 models, and does a two-step "reason then format" recover it at equal tokens?
4. Does lost-in-the-middle still hold on current long-context models for state laid out by the code, and where should checks and goals go?
5. Does an LLM over-trust or under-check when its code tools are always right (automation complacency), and does telling it the tool reliability change this?
6. Can a model calibrate when to call a tool vs answer from memory (Ngai and Gilbert offloading analogue), and does prediction-plus-feedback help it?
7. Do the exact numbers in Norman 1991, Hutchins 1995, Larkin and Simon 1987 and Kirsh and Maglio 1994 (timings, pilot sizes) hold when read in full?
8. Does cheap probe-before-commit (epistemic action) save tokens or just add steps for an LLM, per task type?
9. Does the dependency finding (Kosmyna, GPS) have any parallel for models: does a scaffold's help vanish when removed, or is the model unchanged?
10. Is tool/operator exposure best done by retrieving per state (RAG-MCP) or by a fixed small set, at equal prompt size?


## Gap search results (evidence_d.jsonl, d01-d19; claims K27-K33 added)
Search APIs (arXiv, Semantic Scholar, OpenAlex) were rate-limited, so papers were found with 5 WebSearch calls and opened as PDFs.

1. Designed interface vs plain tool on current models: PARTLY CLOSED. Live-SWE-agent (d01): plain bash agent already 59.8-74.2% on SWE-bench Verified; a tool layer adds 3.2-4.8 points on four models (75.4 vs 70.6 Claude 4.5 Sonnet) and hurts GPT-5-Nano (44 to 14 on 50 problems). So the 2024 gain was largely a weak-baseline effect (K01 now contested). Equal-token tests still missing.
2. Rules in each prompt state: STILL OPEN. Only indirect evidence: Snowball restating recovers 15-20% (d04); a coding-agent report claims just-in-time user-role reminders help, with no numbers (d05). Needs our own A/B test.
3. Output format tax on 2025-26 models: CLOSED. Near-zero for strong closed models, large near the capability limit (Haiku 4.5 -36.2 points, Opus 4.7 AIME -5.3), and reason-then-format recovers most (d11-d13). Not token-equal.
4. Lost-in-the-middle on current models: PARTLY CLOSED. Length alone hurts (d02), effective length 1-8K for most models (d03). Placement of checks and goals in code-laid-out state untested; no 2026 model in these tests.
5. Over-trust of correct tools: CLOSED for corrupted tools (d06-d08): adoption 35.5-68.0%, verification instruction helps, reliability labels help partly. Always-correct tools (the complacency setting) not tested.
6. Tool-vs-memory calibration: STILL OPEN. Overuse is shown (d09) but only fixed by training; prediction-plus-feedback in prompting not tested.
7. Founding papers: PARTLY CLOSED. Kirsh and Maglio read in full (d18: 3-player pilot). Larkin and Simon, Norman, Hutchins still unread (paywall) (d19).
8. Probe-before-commit: STILL OPEN. Only web-agent interaction scaling (d10); no code-task probe test.
9. Scaffold dependence: PARTLY CLOSED. For fine-tuned models the scaffold becomes a dependence (d15); for a frozen model removing it removes the help, no carry-over shown. Scaffold alone can carry a benchmark (d14).
10. Retrieve per state vs fixed set: STILL OPEN. Retrieval saves tokens (d17); description design changes selection (d16); no equal-prompt comparison.
