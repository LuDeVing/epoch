# Critique: E15.09 Scientific discovery as reasoning (cross-check of evidence_a, evidence_b, evidence_c)

Method: I re-opened the arXiv HTML or PDF text of the papers behind the ten most decision-relevant numbers and compared them with the evidence lines. PDFs were saved on D: under research_scratch/E15.09 and deleted after use.

## 1. Numbers re-checked (10)

| # | Number | Source re-opened | Result |
|---|---|---|---|
| 1 | Human Wason baseline: 6/29 right first time, 21/29 eventually, I:C 1.79 vs 0.24, second-chance 0.50 vs 0.19 (a09, b20, c04) | Jhaveri 2026, PDF text | Confirmed. The HTML version drops the numbers (math tags), so use the PDF. |
| 2 | Success 6% to 78% over 11 LLMs; 42% to 56% from counterexample prompts (a12, c01, c02) | Jhaveri 2026 abstract and intro | Confirmed. |
| 3 | FalsifyBench: DeepSeek-V3.1 41%, GPT-5.2-Chat 75%, GPT-OSS-120B 68%, others 33-35% (a11, c05) | Bertolazzi 2026 | Confirmed. |
| 4 | Spearman rho -0.779 (p=.003) and -0.937 (p<.001) (c06, c07) | Bertolazzi 2026 PDF | Confirmed. |
| 5 | Sycophancy study: 29.5 / 14.1 / 11.8 / 8.4 / 5.9%, 557 recruited, 504 final hypotheses (a14) | Batista and Griffiths 2026 | Confirmed. |
| 6 | WILT: Claude 3.5 Sonnet 14/50, o1-mini 13/50, o1-preview 12/50 (a13, c08) | Banatt 2024 Table 1 | Confirmed. |
| 7 | DiscoveryWorld averages and human 66% / 55% (a15, b10) | Jansen 2024 Table 5 and text | Confirmed (ReAct .38/.18/.18 completion, Hypothesizer knowledge .34/.19/.08). |
| 8 | Hypothesis Search: 49 correct hypotheses, 33 (67%) correct programs, 28 of 30 (a16, c18) | Wang 2023 PDF | Confirmed, including 17/23/30/33% and Icecuber 43%. |
| 9 | Si et al. novelty 4.84 / 5.64 / 5.81 (a18, b16) | Si 2024 table | Confirmed, with a unit note: the table counts REVIEWS (119 human, 109 AI), not ideas. The 49 ideas per condition is a different count. |
| 10 | NewtonBench GPT-5 75.9%, Gemini-2.5-pro 65.4%, noise 0.0001 gives 12-16% drop; SHELDON 84.00 / 66.67 / 59.17 (c15, c16, a21, c12) | Zheng 2026, Joshi 2026 | Confirmed. |

Not re-confirmed: the Klahr, Fay and Dunbar 1993 group rates (83 / 65 / 53 / 33%; 56% vs 13% implausible) in a04. The Springer page returned only an abstract-level text this session, and the 1988 Wiley PDF is blocked (HTTP 403). These stay as "secondary, unverified".

## 2. Corrections and flags

- BoxingGym is credited to "Gandhi et al." in a22 and c10, and to "Gu et al." in b12. The author list should be checked; use "Gandhi et al." only after a check against the arXiv page (2501.01540). The numbers agree across all three lines.
- a13 and b24 give the same WILT result as counts and as percentages (o1-mini 13/50 = 26%). No conflict.
- a09, b20, c04 and b19 all describe the same human sample (N=29) in the same paper. They are one source, not four. Claims count them as one.
- a11, b23, c05, c06, c07, c29 are all Bertolazzi et al. One source.
- a14 sample: 557 recruited, 504 gave a final hypothesis; effect percentages use the 504.
- a18 "49 ideas per condition" and the review count 119/109 are both right but must not be mixed.
- b16 and a18 are duplicates; a15, b10, c17 and a20 are duplicates (DiscoveryWorld); a16 and c18 duplicates (Hypothesis Search). Independent-source counts in claims.jsonl already allow for this.

## 3. Contradictions between sources

- Do reasoning models help? Jhaveri and Bertolazzi say yes (thinking models far above instruction-tuned). WILT shows o1-mini and o1-preview at 24-26% against Claude 3.5 Sonnet 28%, and BoxingGym shows instruct Qwen2.5 beating reasoning-tuned OpenThinker. Likely reasons: different tasks, different base model quality, and the 2024 reasoning models being weaker. Claim K04 is marked contested.
- Does an explicit hypothesis list help? DiscoveryWorld Hypothesizer wins on easy knowledge (.34 vs .25) and loses on challenge (.08 vs .10). SHELDON reports large gains from comparing hypotheses. SHELDON is a 2026 system paper by its own authors on new benchmarks; the two are not the same design.
- Does prompting to falsify help every model? Dual-Goal helps thinking models (+0.148) and hurts non-thinking ones (-0.060). The headline "42% to 56%" hides this split.
- Domain prior information: BoxingGym says it often hurts after 10 experiments. Hypothesis-generation work (HypoGeniC, Hypothesis Search) uses priors as the source of candidates. Not a true contradiction, but the sign depends on whether a test follows.

## 4. Weak spots

- The founding human studies (Klahr and Dunbar 1988; Klahr, Fay, Dunbar 1993) were never opened. All their numbers come from Klahr's 1994 summary (a01-a06) and from Trickett's description (b07, "no counts"). The human BigTrak result is the weakest-sourced claim in the folder.
- The Wason human baseline is a small sample (N=29) run by the LLM authors, not a replication of Wason 1960 or Klayman and Ha 1987 numbers. No failed human replication of the 2-4-6 results was gathered.
- The key LLM results (Jhaveri, Bertolazzi, Batista, SHELDON) are 2026 preprints; none has a replication. Correlations between bias and success (rho -0.78, -0.94) rest on 11-12 models and cannot show cause.
- Benchmarks mix old models (GPT-4, GPT-3.5, Claude 3.5) with 2026 models; scores are not comparable across rows.
- ScienceAgentBench, DiscoveryBench: only top-line numbers read. LLM-SR numbers: the table text was garbled in extraction (a17), so use c21/c22 for citations.
- Si et al. measure idea novelty by reviewers, not by executing the ideas. Our guardrail G8 says novelty is judged by running.
- Only seen in abstracts or snippets: b09 (Piriyakulkij), b17 (MOOSE-Chem2), a26 (Fa and Culjak), a27 (Yuh), c27 (Yang), c28 (Jagadish). Not usable for numbers. a28, a29, b26, b27 are metadata only (opened false).
- No evidence yet on Klahr and Nigam 2004 (direct instruction vs discovery) or Alfieri 2011 meta-analysis, though both bear on whether the agent should be told to "explore".
- No source tests Kuhn-style anomaly handling (what an agent does after a result that contradicts its hypothesis). This is the centre of the subfield focus ("anomalies") and remains thin.

## GAPS

1. Does forcing a hypothesis-splitting test (code checks that the next test has different predicted outcomes under two live hypotheses) raise rule-discovery success at equal tokens, causally and not only by correlation? (No source ran it; FalsifyBench rho is correlational.)
2. Are the Klahr and Dunbar 1988 and Klahr, Fay, Dunbar 1993 numbers (exact group sizes, 83 / 65 / 53 / 33%, 56 vs 13% implausible) correct? Open the original papers or a full-text copy.
3. How do LLMs treat anomalies, meaning results that contradict a held hypothesis? Is there any study measuring revise-vs-patch-vs-ignore behaviour (Dunbar's "ignore, then notice when repeated")?
4. Does the Think-in-Opposites or counterexample prompt gain survive on 2026 frontier models and at equal total tokens, given it only helped thinking-mode models?
5. When does an explicit hypothesis ledger beat plain ReAct on hard tasks? DiscoveryWorld says it does not at challenge level; SHELDON says it does. Run both at equal tokens.
6. Is the human plausibility effect (implausible true rules dropped) present in LLMs, and how large? No LLM study was found that used implausible rules.
7. Did anyone replicate the Wason 2-4-6 and Klayman-Ha positive-test-strategy effects with larger human samples or find boundary conditions (task framing, base rates)? Needed to calibrate what "normal" is for the human baseline.
8. How do modern LLM discovery systems (NewtonBench, LLM-SRBench) degrade with noise, and does a code-level constant-ratio or held-out check (BACON-style) restore robustness?
9. Does direct instruction beat discovery for an LLM agent (Klahr and Nigam; Alfieri meta-analysis analogue), i.e. is it better to give the agent the design strategy (VOTAT) in the prompt than to let it search the experiment space?
10. Are DiscoveryWorld-style failures mainly in chaining sub-skills? Unit tests pass at about 60%+ but full tasks reach 18%; find which transition fails.

## Gap search results

Limits: the web search quota was used up, Semantic Scholar and OpenAlex returned rate-limit errors, and the arXiv API found nothing new. Work rests on evidence_d.jsonl (d01-d22, mostly opened in an earlier pass; d22 is a snippet only). claims.jsonl now has K22-K29.

1. Forced hypothesis-splitting test at equal tokens: OPEN. d06 shows prompts raise tokens per turn; d11, d18 and d19 are indirect support (discriminating experiment choice matters; ablation losses), but no equal-token causal run exists.
2. Klahr and Dunbar 1988 / Klahr, Fay, Dunbar 1993: PARTLY CLOSED. The 1988 paper was opened (d01-d03: 19 of 20 solved; 56% retention of disconfirmed hypotheses). The 83/65/53/33% group rates and 56 vs 13% are from the 1993 paper and stay unverified (K18).
3. Anomaly treatment by LLMs: CLOSED in the descriptive sense. d09 (ignore dominates: 68% non-uptake, 71% never updated, 26% refutation-driven revision), d10 (dismiss as noise, saw contradiction but did not act), d12 and d20 (surprise handling). No intervention study of a contradiction log.
4. Counterexample prompt on 2026 frontier models at equal tokens: OPEN. Gemini-2.5-Pro gains only +0.05 (0.73 to 0.78); no equal-token control.
5. Hypothesis ledger vs ReAct at equal tokens: OPEN, with more context. d11 and d14 favour explicit structure, DiscoveryWorld challenge level does not; designs differ.
6. Plausibility effect in LLMs: OPEN. No LLM study with implausible rules found; d16 (PhysGym) shows context can trap, which is related, not the same.
7. Human replications of 2-4-6 and positive testing: PARTLY CLOSED. Klayman and Ha 1987 opened (d04): boundary condition is hypothesis size and target rarity. Large-sample replications not found.
8. Noise and BACON-style checks: OPEN. d08 repeats the noise fragility; no study of a code-level constant-ratio check.
9. Direct instruction vs discovery for LLM agents: OPEN. No source found; Klahr and Nigam not retrieved this pass.
10. Where chained skills fail: PARTLY CLOSED. d10, d15, d17, d21: failures split between generation, selection and conclusion by model; d21 reports history tracking as a separate bottleneck. No transition-level breakdown of DiscoveryWorld.
