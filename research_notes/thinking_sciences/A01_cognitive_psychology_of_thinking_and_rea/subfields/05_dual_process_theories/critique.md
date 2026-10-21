# Critique: dual-process theories (cross-check of evidence a, b, c)

Date 2026-10-21. Cross-checker pass. Claims are in `claims.jsonl` (K01 to K20).

## 1. Numbers re-opened this session (text of the PDF or HTML read)

| # | Source | Numbers checked | Result |
|---|---|---|---|
| 1 | Sprague 2025 (b05, b24, c13) | CoT gains 14.2 / 12.3 / 6.9; 56.9 vs 45.5; 56.8 vs 56.1; MATH 41.6, GSM8K 66.9 | Confirmed. Note: "gains as large as 41.6 and 66.9" is for the best model, not an average. |
| 2 | Bouwmeester 2017 RRR (b03, b22) | N=3,596; -0.37 vs 8.6; 10.37 vs 15.31; 65.9% / 7.5% non-compliance; Q(20)=16.84, I2=2.72% | Confirmed. b22's 34.1% / 92.5% compliance are the complements of b03's figures, so consistent. |
| 3 | Liu 2025 (b08, c12) | 94.0%, 36.3, 23.1, 57.7 | **Corrected.** See section 2. |
| 4 | Chen 2025 (b07, c14) | 1,953% more tokens; 13 solutions; 48.6% fewer tokens | Confirmed. |
| 5 | Hagendorff 2023 (c01, c02, a23, a24) | 96% / 59% / 5% / 38% correct; 80% / 15% / 0% / 55% lure; 500 recruited; 5% to 28% with the algebra suffix; atypical 15% to 43% | Confirmed. a23 and c01 are the same paper (see section 3). |
| 6 | Boissin 2022 (a20) | 39.6 / 27.0 baseline; +48.3 vs +6.2; F(1,99)=36.17; conjunction +58.3, F=72.25; 53.1% / 51.4% | Confirmed from the HAL full text. Effect sizes missing in a20: generalized eta squared .07 (base-rate) and .21 (conjunction). |
| 7 | Travers 2016 (b01) | N=131; 80% / 36% / 58%; 27.3 s vs 21.0 s, p=.0192; 49% vs 55.5% | Confirmed. The time test is at trial level (181 correct vs 297 heuristic conflict trials, df 470.8), not at participant level. Add that. |
| 8 | Pennycook 2016 (b10) | 372 of 497; 30.3 / 30.3 / 43.2% correct; 64.9 / 58.4 / 40.8% lure | Confirmed. |
| 9 | Weston 2023 (c06) | 62.8 to 80.3, oracle 82.0; 51.7 to 61.3 | Confirmed. |
| 10 | Ma 2025 (c17) | 99.1% to 1.5%; 95.9% of errors reused the old method; CRT2 Claude 3 62.0% to 22.0%; o1-preview 10.0%, 82.5% repeats | Confirmed. |
| 11 | Lin 2023 SwiftSage (c09) | 84.7; 757.07, 1,855.84, 1,971.03, 2,983.46 tokens per action | Confirmed. |

Not re-verified (could not open the source): Bago and De Neys 2017 (a18, a19). The HAL record `hal-03510054` has no file and the publisher was blocked. The 74.8% and 87.6% figures stay as written in evidence_a; treat them as opened-by-the-first-pass only. Also not re-opened: Frederick 2005 (a08), Toplak 2011 (b12), Shojaee 2025 (b09; equal-budget pairing not re-read), Gema 2025 (c16), Rand 2014 (b04, b21).

## 2. Corrections

1. **b08 is wrong on the 36.3 figure.** It says "GPT-4o 94.0% direct, 36.3 points worse with CoT". In the paper, 36.3 points is the gap between **o1-preview (57.7%)** and **GPT-4o zero-shot (94.0%)** on a subset. GPT-4o with CoT on the full set fell 87.5% to 64.4% (-23.1 points). c12 states it correctly. Fix b08 before any use. The "36.3" must not be quoted as a CoT drop for GPT-4o.
2. **b01 N detail.** The 27.3 s vs 21.0 s test uses trials, not people. Add this to limits.
3. **a20 baseline wording.** "Initial accuracy before training 39.6% control / 27.0% training" is the first block of the first-response task, i.e. pre-training. Correct as stated, but note the two groups started 12.6 points apart (training group lower), which makes the +48.3 gain partly regression to the mean.
4. **b20 (Smart System 1).** Marked unopened. The full text is available at `https://hal.science/hal-02106554/document` and was opened in this pass (not re-verified line by line). It adds two boundary numbers: only **20.1%** correct at the first response on conflict problems (vs 93.4% on no-conflict controls), and correct justifications rose from **20.7%** (initial-correct) to **60.6%** (final-correct). So fast-correct answers are real but often lack an explicit rationale, which weakens a18's "fast logic" reading. Update b20 to opened:true with these numbers.
5. **Duplicate counting.** See section 3.

## 3. Independence problems (reduce the "established" counts)

- **a23 and c01 are one paper** (Hagendorff, Fabi, Kosinski; arXiv title "Thinking fast and slow in large language models", journal title "Human-like intuitive behavior and reasoning biases emerged in LLMs but disappeared in ChatGPT"). Also c02/c03/a24/a25 are the same paper. Count it as one source.
- **Sprague 2025** appears as b05, b06, b24 and c13. One source (a meta-analysis, but still one analysis).
- **Chen 2025** appears as b07, b25, c14, c26. One source.
- **Liu 2025** appears as b08 and c12. One source.
- **De Neys group.** a18, a19, a20, b13, b14, b20 come from one lab (Bago, Boissin, Raoelison, De Neys). Their agreement is not independent confirmation. The independent challengers are Travers (b01), Hoover and Healy (b15), Pennycook (a14), Trippas (a16, a17).
- I reduced `independent_sources` in claims.jsonl accordingly. K09 is "established" on Chen, Zhang (S1-Bench), Li (DynamicMind), and Shojaee, which are four different groups.

## 4. Contradictions between sources

1. **Is the fast answer ever correct?** Bago and De Neys 2017 (a18): 74.8% to 87.6% of final-correct conflict answers were correct at the first response. Raoelison and De Neys 2019 (b13): only 16% had an insight, 23% were correct from the start, 61% stayed biased across 50 items. Bago 2019 (b20): 20.1% first-response correct on conflict items. These are different tasks and samples, so the headline "most correct answers are intuitive" is task-dependent, not a general fact.
2. **Is conflict detected?** Pennycook 2015 (a14) finds a response-time cost for lure answers (d=.75 to .99). Travers 2016 (b01) finds no overall conflict-vs-no-conflict time difference (t(7.4)=.55) on the CRT, and heavy lure responders show no hidden pull to the right option (b02). Franssens and De Neys's critique (c19, snippet only) points to extreme base rates as an artifact. Detection looks real for base-rate tasks and weak or absent for the CRT.
3. **Serial vs parallel.** Travers (b01) supports default-interventionist on the CRT. Trippas (a16, a17) supports parallel processing for simple belief-bias syllogisms and default-interventionist for complex ones. No theory wins everywhere.
4. **Substitution vs conscious error.** Hoover and Healy (b15) show wrong reasoners remember the relational wording ("more than") better than controls, against silent substitution (a27, not opened). The confidence effect is tiny (eta squared .02).
5. **Rand 2014 (b04) vs the RRR (b03).** Self-pooled 15 studies find a positive effect; the preregistered 21-lab replication finds about zero under intent-to-treat. b04's experience moderator is post hoc.
6. **Pure CoT value.** Sprague (b05) says CoT helps little off math. Hagendorff (c02) shows a large CoT effect on CRT traps for an old model, and tells ChatGPT-3.5 to be brief with no accuracy loss. Both fit one rule: CoT helps where the base model's first pass falls to a lure; it does little once the model has already learned the trap.
7. **Model-specific direction in Liu (b08/c12).** Claude 3.5 Sonnet had -1.8 (i.e. CoT slightly better) on grammar learning, and the mapping from human to model failed in 3 of 6 tasks. Do not turn it into a rule that "deliberation hurts wherever it hurts humans".

## 5. Weak spots

- Almost all human data are WEIRD online or student samples, mostly bat-and-ball and base-rate items. Transfer to a coding or science agent is by analogy only.
- LLM evidence is mostly 2023 to 2025 models. Hagendorff shows the CRT failure disappeared in one model generation; any "System 1 error" result on a modern model must be re-measured, not assumed.
- Three LLM sources (c08 Dualformer, c21 ACPO, c07 distillation) need weight training, which our scaffold cannot do. They only show that difficulty-aware allocation is possible, not how to get it from prompts.
- c11 (Talker-Reasoner) has no results. c20 DynamicMind uses a self-built router dataset.
- Shojaee 2025 (b09): the three-regime result has been disputed (token limits, unsolvable instances). I did not open the replies, so K08 uses b09 only as a supporting line and K09/K20 not as the main support. The inverted-U claim in b09's relevance line has no separate claim here because it rests on a disputed single paper.
- Several "relevance" lines state G-rules as if the study had tested them. The studies only show the pattern; the schema rule is our inference.
- Equal-token comparisons are mostly missing: Sprague says compute should be matched, but few studies match it. Tokens saved (Chen, ACPO) are not the same as accuracy at equal tokens.

## 6. What was seen only in snippets or abstracts

b17 (Meyer disfluent fonts, abstract only), b18 (Melnikoff and Bargh, nothing but a one-line summary), b19 (Keren and Schul, title and count), c18 (Beucler CCN abstract), c19 (Franssens and De Neys, snippet, attribution unverified), a21, a22, a26, a27 (cited second-hand). The single-process side of the debate is therefore unread; K01 and K14 are "contested" on that basis, and should not move to "established" until the critic papers are read.

## GAPS

1. Does the model's own first-pass signal (disagreement across 3 short samples, token entropy, a stated "I am not sure") predict a wrong first answer better than a constant rule or the class's plain pass rate, on perturbed items in a modern model? This is the core S0/S6 gate question; the human feeling-of-rightness literature is not enough.
2. At equal tokens, how much of the best-mode gain does a cheap structural gate (numbers, equals sign, multi-step calculation, known class) recover compared with always-direct and always-step-by-step on a mixed task set that includes pattern, perception and distractor items?
3. Do modern frontier models, prompted for brief answers, still fall for perturbed CRT-style traps (modified principle, not just modified numbers)? Ma 2025 shows o1-preview at 10.0%; is this still true for the current Claude and other models, and does an S4 perturbation check fix it?
4. Do reasoning-length caps help or hurt at equal tokens: one long attempt vs 3 to 4 short independent attempts with code selection, split by problem class? (Gema 2025 and Chen 2025 imply caps help; no test fixes total tokens.)
5. How large was the real fast-correct share, and is it task-dependent? Bago 2017 (75% to 88%) was not re-verified, and later work gives 20% to 39%. This decides whether a "direct" route should be learned per family (memory) or never trusted.
6. Is the Weston System 2 Attention gain (62.8% to 80.3%) reproduced on current models, and by other labs, and does it hold when the cleaned text is produced by a different pass than the solver (S1 input hygiene)?
7. What do the single-process and multi-dimensional critiques (Melnikoff and Bargh 2018; Keren and Schul 2009; Osman 2004 follow-ups) actually say empirically, and do they predict a different design than a gate on task features? Both papers are unread.
8. Can the SwiftSage trigger set (5 steps with no reward, invalid action, critical decision, unexpected observation) be copied to a non-simulator task as an impasse detector, and does it beat always-deliberate at equal tokens?
9. Does a verified worked example in the first-pass prompt (Boissin-style logic training, Hagendorff few-shot 2% to 92%) raise first-pass accuracy on held-out variants in a modern model, or only on items that look like the example (pattern learning)?
10. Which of the six Liu 2025 deliberation-hurts tasks are close to our agent's real task classes, and is there a measurable human-model mapping rule that predicts the three cases where it failed?

## Gap search results

Evidence added: d01 to d20 in evidence_d.jsonl (all opened this session from PDF or full text). Claims changed: K01, K04, K05, K08, K10, K11, K12, K13 (text or evidence list). New claims: K21 to K27. No gap is fully closed. Search was done on 2026-10-21; the newest model tested in any source I could open is GPT-5.4, Gemini-3-Flash and DeepSeek-V4-Flash (d18, a no-thinking study, not a trap study), and the newest Claude in a source is the Claude haiku-4.5, sonnet-4.6 and opus-4.7 check in d04.

1. Own first-pass signal predicts a wrong first answer (OPEN, partly informed). Sample disagreement beats stated confidence on older models (d05: GPT-4 Brier .116 to .119 vs .154 to .181; 3 to 5 samples help). On a frontier model agreement is weak and over-confident (d04: gpt-4.1, 48% wrong at agreement of 0.8 or more; exploratory Claude check shows the same). Nobody compared it with the class pass rate or a constant rule on perturbed items. Treat the signal as one input to log, not a gate to trust. New claim K21.

2. Cheap structural gate vs best mode at equal tokens (OPEN, partly informed). A prompt-only trained switch recovered about 90% of the long-versus-short gain at about 71% of the tokens on maths and beat a random mix and a BERT switch (d11; d14 for a three-way mode). No hand rule on numbers, equals sign or multi-step, and no mixed set with pattern, perception or distractor items. K22.

3. Frontier models on principle-perturbed CRT traps (PARTLY CLOSED for 2025 models, OPEN for 2026 models). Still failing in 2025: o1-preview 10.0% (d20, re-read), o3 59.73% and Claude Sonnet 4 54.36% on 149 perturbed puzzles (d16), puzzle-to-unpuzzle gap 9.1 points for o3 (d17). No 2026 model on CRT-style items, and no test of an S4 perturbation check. Gap-closing detail: the check must change the principle, not the numbers (d20). A brief-answer prompt does not remove reasoning (d18), so a test needs to log pre-answer text. K11 updated, K24 new.

4. Length caps at equal tokens (OPEN). Closest: shortest-of-k with early stop beats majority at matched thinking tokens on maths and GPQA for reasoning models (d12), parallel beats sequential at equal solution count (d13), inverse scaling on constructed tasks (d19). No one-long vs 3 to 4 short capped attempts at fixed total tokens split by class. K23, K27.

5. Real fast-correct share (PARTLY CLOSED). Bago and De Neys 2017 (75% to 88%) could not be opened (HAL page returned HTML, journal paywalled). Re-measured: about 53% on the CRT (d07, N=908), 56% and 78% on untrained bat-and-ball controls and about 84% after training (d06). So the share is task and sample dependent and much lower than 75% to 88% on the CRT. The "20% to 39%" figure in the gap text was not located in a source I opened. Decision for the design: learn the direct route per family from outside feedback, never trust it in general. K04 updated.

6. Weston S2A reproduction (OPEN). Original re-read (d09): same model for rewrite and solve, LLaMA-2-70B-chat only, 200 and 100 problems, GPT-4 judge. I found no replication on a current model or by another lab. Whether a different pass than the solver should do the cleaning was not tested beyond "a separate call of the same model". K12 note added.

7. Single-process and multi-dimensional critiques (CLOSED as to what they say; OPEN as to whether they predict a different design). Read: Melnikoff and Bargh (d01), Keren and Schul (d02), Evans and Stanovich 2013 reply (d03). Both critics are conceptual: they say feature alignment was never measured and the systems were never shown to be separable. They offer no new data. Their implied design is depth as a continuous dial set by task goals; Evans and Stanovich keep two types but call speed and the rest correlates. For our gate this means: key on separately logged cues, allow more than two depths. Not tested head to head. A reply to Melnikoff and Bargh by Pennycook and colleagues was seen only in a search summary. K01 updated; Osman 2004 follow-ups not searched further.

8. SwiftSage triggers as an impasse detector (OPEN). Re-read (d10): four triggers, 84.7 vs 33.8 to 45.3 for always-LLM baselines, 757 vs 1,856 to 2,983 tokens per action; no trigger ablation, no always-slow arm at equal tokens; the fast-only module beat the gated agent on short tasks (78.68 vs 72.81, ChatGPT). No later non-simulator copy found. The four stand-ins for a non-simulator task are listed in d10. K13 updated.

9. Verified worked example and held-out variants (OPEN for LLMs, answered for humans). Humans: the fix is family-bound (d06: carried to bat-and-two-balls, not to algebra or other lure items). LLM: the 2% to 92% jump used same-type examples (d08), so it shows pattern copying cannot be ruled out. No test with principle-changed held-out variants on a current model. K05, K25.

10. Liu 2025 tasks near our classes and the mapping rule (PARTLY CLOSED). Closest to our real task classes: rule learning with exceptions and noisy pattern or perceptual matching (CoT hurt: GPT-4o 87.5% to 64.4%, 2.9 vs 12.5 rounds to learn, face recognition down for all six models). The three cases where the rule failed have a post hoc pattern (model has trained logic, lacks motor priors, has more working memory), not tested on new tasks. K26.

Sources not opened or not found: Bago and De Neys 2017 full text; Pennycook and colleagues' reply to Melnikoff and Bargh; Osman 2004 full text; any replication of S2A; any 2026 frontier-model result on CRT-style traps; the "20% to 39%" fast-correct figure. Data quality notes: d04 is course-assignment data without preregistration; d17's text says the opposite of its own table in one sentence (table used); d16 uses 2025 models.
