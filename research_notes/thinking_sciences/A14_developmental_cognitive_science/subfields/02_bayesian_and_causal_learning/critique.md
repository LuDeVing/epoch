# Critique: A14.02 Bayesian and causal learning (cross-check)

## Numbers re-opened (this session, full text)
Confirmed: Denison 2013 (28/40 = 70%, p=.017); Gopnik 2017 conjunctive D-as-blicket 4y 0.92 vs 6-7y 0.56, 9-11y 0.60 (PMC text); Kosoy 2022 given vs not-given 71% vs 32%, N=85, p=.002; Kosoy 2022b decision transformer 0.16 / 2.06 (5-step) / 2.37 (15-step), accuracy 0.67/0.71/0.77; CLadder CausalCoT 70.40, +8.37 over vanilla GPT-4 (so 62.03), earlier run 63.95 -> 66.64 (+2.36 in the text, +2.69 by subtraction; the paper says 2.36); Corr2Cause 207,972 samples, 18.57% positive, best F1 33.38, random 20.38; Kiciman 97% / 92% / 86%; Samiei 2026 means 9.6 vs 6.4 tests, object accuracy 0.69 / 0.45 / 0.12; Jhaveri 2026 success 6% to 78%, discovery 42% to 56%; Qiu 2026 Bayesian Assistant 81%, 624 users, 5 rounds; Weisberg 2020 Table 1 (38.46/41.03/55.29 blicket; 26.19/38.10/59.52 butterfly).

## Corrections
1. b08 (Weisberg 2020): Exp 2 had N=112 enrolled and 103 analysed (abstract vs results); Exp 2 has its own age table (blicket 23.5 / 42.9 / 70.6; butterfly 29.4 / 37.1 / 58.8), better than Exp 1. Only the 8-10 group is above chance. The "46% / 42%" are pooled Exp 2 accuracy.
2. b14 says off-the-shelf LLMs "36-58%". In the Qiu figure the 58 appears to be the human bar (48-user subset), and c13 says humans about 58%. Treat LLM final-round range as roughly 36-51%, with the exact per-model values unread (figure text only).
3. a19 vs b09 looked like a contradiction (2.37 vs 2.06). Not one: 2.06 is 5-step forced exploration, 2.37 is 15-step.
4. a21/b11/c16, a22/b12/c17, a23/b13/c18, a25/b14/c13, a26/b15/c01 and a28/b18/c05 are the same papers entered several times. Independent-source counts in claims.jsonl count papers, not lines.
5. Gopnik 2017 4-year-old and adult data are reused from Lucas 2014 (b05, b27), so K02 has fewer independent samples than the line count suggests.
6. a02, a03, a04, a05, a06, a17, b26 (founding blicket and backward-blocking papers) were never opened. Their pass rates are absent.

## Contradictions and tensions
- Probability matching (Denison) versus noisy maximising or pragmatic switching: the authors rule out pure noise (needs 58% random responses) but not all alternatives. Contested.
- "Children are Bayesian" versus the 2018 PLoS replication (b07): children split into strategy subgroups; group means hide this. And Weisberg 2020: 4-7 year olds at chance on diagnostic inference. The strong form is weaker than the review (a01) implies.
- Qiu 2026 says prompt-level fixes fail; GX-Chen 2025 says a prompt-level scaffold (hypothesis sampling) works. They differ in task (preference learning vs rule discovery) and in what is externalised (code vs text).
- CausalCoT gain shrinks from +8.37 to +2.36 across model versions: staged prompting is not a stable lift.
- Alderete 2026 (a27): context graphs alone were numerically worse than base (77.3% vs 87.3%), only the combination reached 89.1%. Scaffolds can hurt. p=0.015 is one-tailed on a post-hoc contrast; base vs both (87.3 vs 89.1) is not significant.

## Weak spots
- Most LLM causal evidence is from 2022-2024 models (GPT-3, GPT-4, LaMDA). The 2025-2026 blicket papers are preprints, mostly one research group (Gopnik/Precup/Richards circle), so independence is limited.
- No test of whether a scaffold step (hypothesis list, falsification, EIG) beats equal-token plain reasoning with a current frontier model on a non-blicket task.
- Human numbers for the 2026 active-learning study are online Prolific adults (N=306); small cells (102 each).
- Bayesian-brain critique (b25) is a thin secondary source.

## Only seen in snippets or secondary text
a02-a06, a17, b26 (founding studies via reviews), c23, c24, c25 (as reported by others), figure-derived values in b14, b19, c15, c21.

## GAPS
1. Does the hypothesis-sampling plus max-elimination scaffold (GX-Chen) beat plain reasoning at equal tokens on a current model and on tasks outside the blicket game (code debugging, diagnosis)?
2. How much of the conjunctive handicap comes from exploration versus reading evidence for frontier reasoning models (2026), and does enumerating rule forms first (a18-style) fix it?
3. Does forcing one falsifying (incompatible) test per cycle raise success at equal tokens outside Wason-style tasks, and what is its token cost?
4. What are the exact pass rates and sample sizes in the founding blicket studies (Gopnik 2001, Sobel 2004, Schulz 2007, Kushnir and Gopnik 2005), and how many replicated beyond the 2018 PLoS partial replication?
5. Can an externalised numeric belief table updated by code (not text) close the Qiu et al. gap without fine-tuning?
6. Does Bayesian sampling from the posterior (variability) beat argmax decisions in agent search, or is sampling only useful when diversity is rewarded (best-of-N, self-consistency)?
7. Do 2025-2026 LLMs still fail seeing-versus-doing separation (Waldmann-type tasks) that GPT-3 failed?
8. Is the overhypothesis transfer effect (learn a rule form on one task, apply to the next) usable as agent memory, and what does it cost when the new task's rule form differs?
9. Which stated priors help or hurt? BoxingGym shows prior information can anchor; when does a stated prior in the prompt reduce test diversity?
10. Replications outside the Gopnik group: who has independently reproduced the 2025-2026 LLM blicket findings?


## Gap search results

Search tools were limited: web search budget was used up, arXiv and OpenAlex returned HTTP 429, and Semantic Scholar worked only now and then. So the search was mostly by following citations from papers already in hand and opening full texts. Evidence is in evidence_d.jsonl (d01-d16). New claims K25-K31 are in claims.jsonl, and K03, K04, K05, K08, K09, K10, K13, K19, K20, K21 were updated.

| Gap | Result | Status |
|---|---|---|
| 1. Does the GX-Chen scaffold beat plain reasoning at equal tokens, and does it work outside blicket? | Not tested anywhere I could open. GX-Chen states generalisation beyond blicket is future work. The sampling agent is shown on gpt-4o only and its prompt also names the two rule forms (d06, d07). Piriyakulkij 2024 shows a related design (weighted hypotheses plus code-computed information gain) beating a ReAct agent on Zendo, 6.55 vs 4.60 of 8 (d13), but with 2024 models and not at equal tokens. | Open |
| 2. Exploration vs evidence reading for 2026 reasoning models; does listing rule forms fix it? | Partly. Samiei 2026: gpt-5 and deepseek-reasoner near perfect on disjunctive and gpt-5 near adult level on conjunctive, but about 30-45% more tests (d08). Alderete 2026: plain Sonnet 4.5 with both rule types named gets 87.3% (96/110) (d12). GX-Chen's own appendix finds higher reasoning effort in o3-mini and o4-mini explores worse in the conjunctive case (d06). No study tests listing vs not listing, and the split between exploration and reading is not done. | Partly closed (handicap smaller; mechanism open) |
| 3. Does a forced falsifying test help at equal tokens outside Wason tasks, and at what token cost? | Cost found: 12-58% more tokens per turn in thinking models; success up (Qwen3-32B blicket 0.57 to 0.86); small or mixed in non-thinking models (d09). Not matched on tokens and not tested outside rule games. | Partly closed (cost known; equal-token and other tasks open) |
| 4. Exact pass rates and sample sizes in the founding blicket studies; replications | Sobel 2004: n=16 per age cell, pass rates 100%, 94%, 50%, 88%, 63% (as quoted in the 2018 replication, d01). 2018 replication N=90 matched 5 of 6 comparable cells; the 4-year-old Exp2 backward-blocking cell differed (96% vs 63%, p=.03). Griffiths 2011 gives child N=16 and N=24 (d02). Independent checks: Kloos and Sloutsky 2005 (N=33 and 25 children) failed to find cause/effect asymmetry (d03); Beaton and Benton 2024 (26 + 33 children) found backward blocking tied to additivity training (d04). Gopnik 2001, Schulz 2007, and Kushnir and Gopnik 2005 original pass rates were not obtained: paywalled or not found in text read. Note: the 2018 paper is mostly a replication, not a partial one as the first critique said. | Partly closed (Sobel 2004 done; three papers still without numbers) |
| 5. Can a code-updated numeric belief table close the Qiu gap without fine-tuning? | No source tests this. Qiu appendix B shows an external symbolic decision step on LLM-verbalised beliefs beats direct choice, but stays below fine-tuned models; CoT, numeric encoding, and 30 rounds did not help (d10). Models were Gemini 1.5 Pro, GPT-4.1 Mini and open models; no 2025-26 reasoning model. | Open |
| 6. Posterior sampling vs top hypothesis in agent search | Indirect only. Piriyakulkij: tracking weighted particles let the agent choose splitting tests; their text says a single best-guess gives little guidance for the next experiment (d13). GX-Chen: sampling 16 to 96 equal-weight hypotheses removes the conjunctive gap (d06). Neither compares sampling with always taking the top one at equal compute outside a diversity-rewarded setting. | Open |
| 7. Do 2025-26 LLMs still fail seeing vs doing | No 2025-26 Waldmann-type test found. CLadder (2023 model) shows GPT-4 rung 1 and rung 2 about equal (63.01 vs 62.82; row read from a garbled table, check the PDF) (d15). | Open |
| 8. Overhypothesis transfer as agent memory; cost of mismatch | Human data only: Jiang and Lucas 2024 (N=212, N=250) show matched training helps disjunctive transfer (p=.017 to .051) and that a no-transfer model predicts as well as the transfer model (.059 vs .055) (d14). No LLM-agent test. | Partly closed (human cost known; agent open) |
| 9. Which stated priors help or hurt | BoxingGym: context often did not help, with an early strong assumption not revised named as the cause (d11). But it measures error and information regret, not test diversity, so the anchoring-of-tests claim is not shown. | Partly closed (premise corrected) |
| 10. Independent reproduction of the 2025-26 LLM blicket findings | None found. Samiei and Jhaveri share authors with GX-Chen. Alderete 2026 is a separate group with Sonnet 4.5 but tests scaffolds on a regime-change task with rule types given, not the conjunctive bias (d12). A Semantic Scholar check found one blicket-LLM hit in 15 results (d16). | Open (claim K30 unsupported) |

### Changes to earlier claims
- K21: the 2018 paper is mostly a replication (5 of 6 comparable cells), with one failed cell. Raised to two independent sources.
- K05: the GX-Chen scaffold gain is confounded with naming the rule forms in its prompt.
- K09: added token cost.
- K20: BoxingGym does not measure test diversity.
- New K25-K31. K30 is marked unsupported.

### Limits of this pass
- Several pages were read through a fetch tool that summarises text (d01, d02, d14); table values there should be rechecked in the PDF before quoting.
- Figures with garbled text (Samiei per-model accuracies, some Piriyakulkij and CLadder table rows) are not quoted or are marked unsure.
- Reasoning on 'who replicated' is limited by a search tool that was out of quota.
