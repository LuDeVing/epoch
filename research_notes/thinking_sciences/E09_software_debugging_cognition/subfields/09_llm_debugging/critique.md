# Cross-check critique: LLM debugging (E09.09)

## Method
Re-opened the PDF text (pdftotext, or arXiv HTML for SWE-agent) for: Chen self-debug, Olausson self-repair, Huang self-correction, SWE-agent, Agentless, LDB, Reflexion, Tyen mistake-finding, PatchDiff. About 14 headline numbers were checked. The three evidence files were produced from the same few papers, so agreement across files a/b/c is NOT independent confirmation. Independence in claims.jsonl is counted by paper or research group.

## Corrections made (applied in the evidence files)
1. Huang et al. oracle-label numbers (a06, b09) were wrong. Table 2 reads: GPT-3.5 GSM8K 75.9 to 84.3 (not 95.5), CSQA 75.8 to 89.7, HotpotQA 26.0 to 29.0; GPT-4 GSM8K 95.5 to 97.5 (84.3 was the GPT-3.5 oracle figure), HotpotQA 49.0 to 59.0 (not 29.0). c05 already had them right. The direction of the finding is unchanged.
2. Chen MBPP Codex (b01, c01): UT = 69.4, UT+Expl = 69.8, UT+Trace = 70.8. The files had "UT 69.8".
3. Huang debate (b10): the table cells are ambiguous about whether 83.2 and 83.0 use 6 or 9 responses. The fair comparison is self-consistency 85.3 at 6 and 88.2 at 9, so debate is below it either way. The old wording compared 83.2 to the 9-response figure.
4. Reflexion (a11): HumanEval Python false-positive rate is 1.4% in the text (0.01 in the table). The "false negative" columns in the paper's table do not sum to 1 with the true-positive column, so FN figures were not used in any claim.

## Confirmed on re-opening
Chen TransCoder GPT-4 77.3 to 90.4 (+13.1), Codex no-test 80.4 to 83.9, GPT-3.5 flat at 89.1; Olausson human vs own feedback 33.30 vs 52.60 (and the per-difficulty figures), 1.05 (np=10, 1 repair) and 0.97 (np=2, 10 repairs) heatmap cells; Huang CSQA 38.1/41.8 and 74.7% kept; SWE-agent 51.7% (1,185/2,294), 90.5% and 57.2%, 23.4% cascading failed edits, Lite 18.00 vs shell-only 11.00 vs RAG 2.67, Agentless 77/81/96 and 32.00% at $0.70, LDB 73.8/81.1/82.9 and the GPT-4 and Reflexion seeds, Reflexion 91.0/80.1 and 16.3%, Tyen 52.87 and backtracking table, PatchDiff 7.8%/29.6%/46.8%/27.3%/260 of 877.

## Contradictions between sources
- Chen says a single debug turn on a greedy sample equals 16 samples (Spider, Codex). Olausson finds repair about equal to resampling at matched tokens (1.05x and 0.97x for GPT-4 on APPS). Different units (samples vs tokens), models, tasks and feedback source. Left as contested.
- Chen says extra turns add under 0.1%; LDB keeps climbing to 10 iterations. Different task and feedback type.
- Chen's StarCoder gains (MBPP +6) vs Reflexion StarChat zero and LDB StarCoder about zero: the model-strength claim is contested.
- Agentless explicitly uses model-written reproduction tests as a selector (+19 patches), while Reflexion's own tests hurt on MBPP. Likely resolution: tests are good filters across many candidates but bad lone stop signals. Not tested directly.
- SWE-agent cost per Lite task: $1.67 in its own paper, $2.51 in AutoCodeRover and about $1.62 in Agentless (GPT-4o). Different model versions and cost accounting. Do not compare costs across papers.
- Huang Table 2 uses different baselines for GPT-4 than Table 3 on some benchmarks (GSM8K 95.5 in both rows after correction, but CSQA standard 82.0 vs earlier papers). Treat cross-paper baselines as non-comparable.

## Weak spots
- Almost all code-repair numbers are from 2023-2024 models (Codex, GPT-3.5, GPT-4, GPT-4o). No reasoning-model (long chain-of-thought) data for the self-debug question. The model-strength claim may have shifted.
- Chen's baselines are few-shot with 1 to several samples; no variance or confidence intervals reported. Many gaps are 1 to 3 points on 100-500 items.
- SWE-agent ablations are single runs on 300 items (standard error about 2 points), so linter +3.0 and viewer differences are suggestive, not tested.
- LDB is a single group's benchmark and its margin over Self-Debug (about 1.8 points GPT-3.5) is small.
- Agentless vs SWE-agent is across different system versions, not a matched ablation.
- Tsui "blind spot" (2026) is a preprint on non-reasoning open models only; headline 156% accuracy gain from "Wait" not re-checked.
- Rubber-duck benefit rests on essentially one paper (Chen, Spider) with small margins; nobody has isolated explanation from re-reading.
- No evidence at all on equal-token comparisons of SWE-bench agent loop designs; cost is reported but not matched.

## Only seen in snippets or not re-opened by the cross-checker
SWE-ABS (c29) and the 28-syntax-error anecdote (c30) are snippet-only; not used in claims. Not re-opened by me this session: SWE-Bench+ (a32/b25), Kang AutoFL (a22/a23), AutoCodeRover, DEI (c19), Liu failures study (c21/c22/c28), Majgaonkar (c23), Cemri (b27), Tsui (b13), MINT (a34), CodeAct (c24), Self-Refine, Kamoi. Their numbers rest on the search agents' reading and should be treated as single-read.

## GAPS (most decision-relevant first)
1. At equal total tokens, does test-guided repair beat best-of-N plus test-based selection for a modern reasoning model? (Chen and Olausson disagree; no matched modern test.)
2. Does an explicit "name the first wrong step, with evidence" operator before rewriting raise repair rates, and how accurate is our agent at that localisation? (Tyen shows 52.87 and large gains given the true step; nobody has built the operator.)
3. What is the right stop rule: how many failed edits or rounds before forcing relocalisation or a change of approach, and does that beat continuing at equal tokens? (SWE-agent 90.5 vs 57.2 and the 25-round cliff are observational.)
4. When is an agent-written test a good filter and when a bad stop signal? Quantify test false-positive rate versus gain across tasks (Reflexion MBPP vs Agentless).
5. Does re-presenting the agent's own draft as external text (colleague framing, "Wait" interrupt) fix the self-output blind spot in reasoning models, at equal tokens?
6. Does the self-debug gain depend on base-model strength once models are strong, or are the Chen/Reflexion small-model results obsolete?
7. Do runtime probes (inserted prints, variable values) beat reading code plus a pass/fail result on our task types? Only LDB tests this, with small margins.
8. Which share of unresolved failures are "wrong design" versus "slip", and does a dedicated abandon-approach operator or a strategy-level supervisor (Liu: 22.2% rescue) help on the wrong-design share?
9. Does rubber-duck explanation add anything beyond re-reading when a test is available, and does a wrong explanation hurt (AutoFL: about 20% accurate)?
10. How should we measure our agent on held-out, post-cutoff, hidden-test tasks given SWE-bench leakage and weak-test inflation (32.67%, 29.6%)?

## Gap search results (2026-10-26)
New evidence is in `evidence_d.jsonl` (d01-d21, all opened this session as PDF text). Claims K27-K36 are new; K04, K08, K09, K10, K11, K15, K18, K19 and K21 were extended. Web search quota ran out partway, so Gaps 9 and 3 had fewer targeted searches than the others. Also re-opened and confirmed: SWE-Bench+ (32.67% leak, 31.08% weak-test, 12.47 to 3.97), AutoFL (20% / 56.7%, Spearman 0.57 / 0.52), Tsui (64.5%, 89.3%), Majgaonkar (12.6% to 82.5% longer). Correction: the 156% "Wait" figure is mean accuracy gain on non-reasoning models only.

1. Equal-token repair vs best-of-N plus tests. PARTLY CLOSED, still open for modern reasoning models. At matched calls, plain repair often falls below sampling (BESTER, 21 calls: DeepSeek APPS 57.54 sampling vs 53.67 repair). Small frozen models: blind resampling beat bare-code retry by +18 net unlocks and tied code+facts (d01). CodeMonkeys: equal-cost serial and parallel mixes reach similar coverage after the first few iterations; selection is the limit (random 45.8, final 57.4, oracle 69.8). S* shows self-debug +1.0 to +3.4 and -2.8 for reasoning models vs 8-10 point gains from sampling plus selection, but at unequal cost. No one has run a matched-token test on a current reasoning model.
2. First-wrong-step operator. PARTLY CLOSED on the localisation side, OPEN on the operator. Trusting the model's own hint lowered correction for 2 of 3 models (Li, GSM8K; DeepSeek n=30 rose). Structured step-by-step traces made self-localisation more reliable and gave 20-40% lift under an oracle (Thought-ICS, not code). ProcessBench: o1-mini 87.9 F1 vs GPT-4o 61.9, so the 52.87 figure is stale for reasoning models. Nobody has built or measured the operator for code.
3. Stop rule. PARTLY CLOSED. Convergent evidence for a cap of about 1-3 rounds on one draft (Chen, debug-gym, S*, CodeMonkeys) and for content triggers over length (repeat cycle, 5 steps with no edit; failed runs are longer but length confuses hard with stuck). External stall checks raised resolution (SWE-PRM +10.6 at 9x cost; rule monitor +7 to +23.5 on selected cases) but neither is equal-token and the monitor needs to be stronger than the actor. The exact round count that beats continuing is still unmeasured.
4. Agent-written tests as filter vs stop signal. MOSTLY CLOSED as a rule of thumb, not quantified. Good filter over many candidates when no real test exists (CodeMonkeys, Agentless); no help or slightly worse when real public tests exist (S*: 53.1 vs 53.8); worst as the lone stop signal (Reflexion MBPP 16.3% false positives; Thought-ICS self-verification breaks more than it fixes). Best selector: model invents inputs, real execution gives outputs. No false-positive-versus-gain curve across tasks yet.
5. Colleague framing / Wait. CLOSED in direction, with a scope limit. Reasoning models show a small or negative blind spot (R1-Distill-70B -0.03 to -0.05); non-reasoning models gain most from Wait. So the fix is probably moot for a reasoning agent. Evidence is injected errors in math and logic, not code, and no equal-token control for Wait.
6. Base-model strength. STILL CONTESTED, better framed. Gains depend on loop and task more than size alone: S* self-debug +12.1 for Qwen-32B but about 0 for reasoning models; debug-gym debugger helps Claude 3.7 and can hurt weak models; Li finds weaker models correct more. The 2023 small-model results are not obsolete or confirmed.
7. Runtime probes. PARTLY CLOSED. debug-gym: pdb after 5 failed rewrites lifted Claude 3.7 from 37.2 to 52.1 on Lite; early pdb hurt weak models; no effect on Aider. Not token-matched. Together with LDB's small margins, probes look useful on hard repo bugs for strong models only.
8. Wrong design vs slip. PARTLY CLOSED. For strong models localisation is not the main failure: 56.9% of SWE-agent failures reach the right function. Overwriting a correct edit is 22.6% of all failures; wrong branch point about 10%. So a keep-best checkpoint is worth more than an abandon-approach operator. Liu's 22.2% rescue is still single-source; no abandon-approach test.
9. Rubber duck vs re-reading. OPEN. AutoFL has no no-explanation arm; 20% of explanations accurate. No study found isolates explanation from re-reading when a test exists.
10. Measurement. CLOSED as guidance. Fresh and private sets give half or less: SWE-bench-Live 19.25% vs 43.20% same pair; SWE-Bench Pro public 43.6 vs commercial 17.8. Use post-cutoff or private tasks, check answer not in issue text, use hidden tests stronger than the agent's own.

Weaknesses of the new evidence: many 2026 items are single preprints (d01, d08, d12, d16); several are math not code (d08-d12); the monitor results (d13, d14) are not equal-compute and d14 is selection-biased; S* and debug-gym tables had scrambled cells, so only checked cells are quoted. Still missing: any matched-token test with a current reasoning model on code debugging.
