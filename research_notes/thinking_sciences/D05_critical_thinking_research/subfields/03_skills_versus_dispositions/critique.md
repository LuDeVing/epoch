# Critique: D05.03 Skills versus dispositions

Cross-check done by re-opening the full text of Huang 2024, Tyen 2024, Self-Correction Bench, Sharma 2024, SycEval, Hagendorff 2023, MillStone, Abrami 2015 (summary), Alpindo 2024, and the longitudinal paper b01 (PMC).

## Numbers confirmed
- Huang (a19, b15, b16, c01): CommonSenseQA 75.8 -> 38.1 -> 41.8; GSM8K 75.9 -> 75.1 -> 74.7; GPT-4 GSM8K 95.5 -> 91.5 -> 89.0; HotpotQA 49 -> 49 -> 43. Oracle table: GPT-3.5 GSM8K 84.3, CSQA 89.7, HotpotQA 29.0; GPT-4 GSM8K 97.5, CSQA 85.5, HotpotQA 59.0. The pairings were scrambled in the text and are now confirmed by row order. One caveat: Table 3 labels "# calls" 1, 3, 5, so the columns are calls, not rounds as such.
- Self-Correction Bench (a18): 64.5%, 89.3%, 156%, 76.0%, 5,306 traces, Haiku 52.5%, Sonnet 4 41.4%, natural errors 4.3 to 10.8%. All confirmed.
- Sharma (a23, b17, b18, c04): 98%, 27%, 32% to 86%, 42% to 98%, 45%, 75% vs 25% all confirmed. Note: the "27%" appears twice with two meanings: "Are you sure?" up to 27% (Claude 1.3), and a user-suggested wrong answer up to 27% (LLaMA 2). Do not merge them.
- SycEval (c06): 58.19%, 43.52%, 14.66%, 61.75% vs 56.52%, Z=5.87, 78.5% confirmed.
- Hagendorff (c13): CRT 38% humans, 59% ChatGPT-3.5, 96% ChatGPT-4, intuitive 55% humans, 80% davinci-003, 15% and 0% confirmed.
- MillStone (a16, a17, b13): 222 of 575 (38.6%), 39.2%, 12.2%, refusal 37.8/68.9/83.3% confirmed.
- Alpindo (b07): r=.649, CI lower .593 confirmed. b01 paths beta .28 (WM) and .15 (dispositions) confirmed; r=.29 and .35 not re-found in the text slice I read.

## Corrections
1. a20 (Tyen): the figures 87.73, 86.68, 77.79 (word sorting, GPT-4-Turbo) and 6.58 / 35.07 are NOT mistake-finding accuracy. They sit in the table of accuracy on traces that contain NO mistake (the text says that accuracy "goes down considerably" from direct trace-level to CoT step-level). The real mistake-location result is c02: GPT-4 overall 52.87 (direct step), 39.80 (trace-level), 43.40 (CoT step); GPT-3.5-Turbo 10.10 on one task and 14.78 overall. Use c02, not a20, for the claim that finding errors is weak. Table 6 gains (+18.04, +18.06) and losses (-8.89, -15.91) are confirmed as listed, but they belong to a specific task row (Dyck/ other) and the model alignment remains unverified.
2. a07 (Abrami 2015): the summary I opened says "341 studies", not "341 effect sizes". It also gives what a07 lacked: critical thinking disposition outcomes only g=0.23 (25 studies), content-specific CT g=0.57 (97 studies), and the three-approach combination g=0.57 (19 studies). The 0.57 appears twice for two different things. The skill-vs-disposition gap in training is real (0.57 vs 0.23).
3. a14 / b11 / a15: the CTDS and AOT numbers are "normalised to human = 1.0" in the appendix; the column-to-model mapping is still unconfirmed, so no model names should be attached to any score.
4. c08 (o1-preview 81.25%): single item, author scored. Treat as a weak anecdote, not a benchmark.
5. b23 and b24 (Abrami, recalled) duplicate a07; b24 "117 studies, 161 effects, 0.34" is recalled and stays unverified.

## Contradictions between sources
- a20 and c02 give different "mistake-finding" numbers (see correction 1).
- Self-Refine (a24, c25) reports about +20% from self-feedback; Huang (a19) and Kamoi (a21) find none on reasoning. Resolved by task type: preference and open tasks vs single-answer reasoning with hidden errors.
- Reflexion (c18, 91% HumanEval) is a self-correction success, but it uses test results as a trigger, so it agrees with the signal-needed view.
- MillStone says models are "open-minded on most issues" (a16) while also showing wrong-direction shifts (a17) and refusals dissolving (b14). The word "open-minded" there means movable, not calibrated.
- Reflective skepticism did not rise (b05) but is the very disposition the agent needs; the one source is n=16 with scale alpha .41 and .53.
- b07 (metacognition r=.649) vs b01 (disposition-skill r=.29): different constructs and methods, not a direct conflict, but self-report inflation probably explains some of the gap.

## Weak spots
- Almost all human disposition evidence is self-report and same-method.
- Nothing opened for the three founding authors beyond the Delphi report and SEP: Ennis 1987/1996, Halpern 1998, Stanovich and West 1997 are recalled or second-hand (a05, a09, a12, b25, b28). No exact AOT-ability correlation was read.
- No CCTDI/CCTST correlation figures were read (a10, b26 recalled).
- No LLM paper manipulates a disposition and measures a skill outcome directly. Existing LLM studies measure either stated scales (Zhou) or one behaviour (sycophancy, self-correction).
- Most LLM models are 2023-2024 era. Reasoning models show a small or negative blind spot (a18), so conclusions about non-reasoning models may not carry over.

## Only seen in snippets / abstract pages
b08, b09, b10, b20, b21, c22, c23, c24 (abstract or snippet only); a24 abstract only; c19 and c20 without exact figures.

## GAPS
1. Does a code-fired doubt signal beat a "be open-minded / re-check" disposition prompt at equal tokens on single-answer reasoning, including with a reasoning-class model? (Nobody has run this head to head; our 92% vs 75% needs n and CIs.)
2. What is the miss rate of the trigger (sensitivity failure): how often does a real error occur with no signal fired, on natural rather than injected errors? Self-Correction Bench natural-error catch rate is only 4.3-10.8%.
3. Can an LLM disposition be measured by behaviour (evidence-driven vs pressure-driven belief change) with a validated score, rather than self-report scales? SycEval's progressive/regressive split is the only start.
4. How large are the original Stanovich and West AOT and Argument Evaluation Test effects after ability control, and have they replicated (primary text not opened)?
5. What are the actual CCTDI-CCTST correlations and factor structure criticisms, and Halpern's transfer data?
6. Do reasoning models (o1 class, extended thinking) still show a self-correction blind spot and sycophancy on challenge, and does "Wait" still help?
7. Does open-mindedness toward arguments depend on argument quality? Test true vs false authoritative arguments, which MillStone could not because opinion issues lack ground truth.
8. Is training or a scaffold able to move the skepticism-type disposition in people with a proper control, and is there an analogue for agents (does a persistent policy beat an in-prompt reminder)?
9. Does hiding authorship and stance from the judge (G5) remove self-preference and sycophancy at equal tokens?
10. Do human-trained instruction gains (Abrami 0.30 overall, 0.23 for dispositions) have any analogue in prompt-level "teaching" of an LLM on held-out items?


## Gap search results (evidence_d.jsonl, d01 to d17; claims K27 to K33 added)

Search note: WebSearch budget ran out after two calls. OpenAlex and Semantic Scholar were rate limited. All papers below were opened as full PDF text (arXiv) unless marked.

### Closed or mostly closed
- **Gap 4 (reasoning models, blind spot, Wait):** Mostly closed. Reasoning models still flip under challenge: Li 2026, nine models, 8 of 9 beat GPT-4o on consistency (d=0.12 to 0.40) but a suggested wrong answer is the strongest attack on all (d01). Jittham 2026: o3 -7.0 pp, R1 -6.0 pp, mean -6.3 pp when asked to reconsider (d03). 'Wait' still helps a reasoning model: s1-32B AIME24 50% to 57% (d13). K27 and K28 added.
- **Gap 3 (behavioural disposition measure):** Partly closed. Resistance scores exist (SYCON-Bench Turn of Flip and Number of Flip, 17 LLMs, d09; FlipFlop 46% flips, 17% drop, d06). None measures evidence-driven change, none is validated against a human scale. K29 added. Open: build and validate a two-sided score.
- **Gap 7 (hide authorship, G5):** Partly closed, with a warning. Self-recognition is real (GPT-4 73.5%, d14) but the bias follows familiarity (low perplexity) as well (d15). Hiding authorship alone is unlikely to be enough. No blind-vs-unblind test at equal tokens exists. K32 added.
- **Gap 2 (trigger miss rate):** Partly addressed. ProcessBench on natural errors shows a large gap between reasoning and non-reasoning auditors (o1-mini F1 87.9 vs GPT-4o 61.9, d10), but only when the model is told to audit. The no-instruction miss rate is still unmeasured. Self-Correction Bench's 4.3 to 10.8% natural catch rate stands.

### Stayed open
- **Gap 1 (code signal vs disposition prompt at equal tokens):** Still open. Only indirect support: reconsideration loops lower accuracy (d03), confidence is a bad trigger (d02, d07), CRITIC no-tool critique helps math about as much as the tool (d12). Our 92% vs 75% still lacks n and CIs; no source found that can supply them.
- **Gap 5 (true vs false authoritative arguments):** Still open. Xu 2024 used only false content; logical tone beat credibility (d08). K30 added as single-source.
- **Gap 6 (original Stanovich and West AET / AOT):** Still open. The 1997 paper and the 2007 myside paper were behind paywalls (d17, opened:false). Only Haran 2013 was read: AOT correlates with CRT r=.300, need for cognition r=.355, and the effect runs through information search; with fixed information AOT predicted nothing (d16). Ennis, Halpern, CCTDI-CCTST correlations remain unopened.
- **Gap 8 (move skepticism disposition, persistent policy vs reminder):** Still open. Only SYCON's third-person prompt (up to 63.8% Turn of Flip gain, d09) shows a prompt-level lever; no persistent-policy comparison found.
- **Gap 9 (training analogue):** Weak partial. CQoT (d11) is the closest prompt-level analogue: about +5% on a tiny MT-Bench subset, with extra compute. Not an equal-token or held-out test.

### Caveats on the new evidence
- Jittham 2026 is a single-author preprint on 200 true/false statements.
- Wataoka (d15) numbers 0.749 and 0.520 come from different parts of the paper and are not reconciled.
- CRITIC (d12) table rows were aligned by inference from flattened PDF text.
- ProcessBench (d10) per-subset numbers were not cleanly extracted; only the headline F1 values are used.

### Status changes
K24 single-source to established (d02, d07). K20, K14, K10, K09 extended with new evidence ids; K09 stays unresolved on the n and CI requirement.
