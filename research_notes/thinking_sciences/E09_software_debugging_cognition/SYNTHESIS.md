# Software debugging cognition: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" is the claim's status in claims.jsonl after the source audit of 2026-10-26 (see the last paragraph). Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Most agent evidence here comes from older or small models and from SWE-bench-style repo tasks. Our bench is puzzle-sized, so every row is a design hint until tested (section 5).

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 02 Hypotheses in debugging | [DEEP](subfields/02_hypotheses_in_debugging/DEEP.md) | 24 | 8 (15 single-source, 1 contested) |
| 09 LLM debugging | [DEEP](subfields/09_llm_debugging/DEEP.md) | 36 | 16 (14 single-source, 6 contested) |
| **Total** | | **60** | **24** |

Each researched subfield has an UNKNOWNS.md with 15 test rows (30 in all).

Not yet researched (from SUBFIELDS.md, no DEEP.md):
- Cognitive breakdowns (Ko and Myers 2005)
- Mental model of the system (Li and Coblenz 2026)
- Debugging as scientific method (Zeller; Whyline)
- Program comprehension (Brooks, Letovsky)
- Tools and questions (slicing, why/why-not)
- Fault localisation and repair (spectrum, mutation, repair)
- Novices and education (Murphy et al.)
- Verbalisation (rubber duck)

## 2. Established findings, merged

Only claims with status established. Many rest on older or small models.

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | A debug loop works only with real execution output (tests, errors, traces). Model-imagined output lowers plausible-patch rate (73% to 63%). Without execution the same loop gains little or loses. | E09.02-K09, E09.09-K01 | G2, S4 | yes (G2 revise only from real output) |
| F2 | Intrinsic self-correction with no outside signal does not help and often hurts. Earlier gains used oracle labels as the stop signal. | E09.02-K11, E09.09-K02, E09.09-K03 | G2, 4b | yes (4b unstructured self-reflection) |
| F3 | When the model alone decides whether to keep correcting, it breaks more correct answers than it fixes, under every gating rule tried. | E09.09-K31 | G2, S6, S8 | partly (G2, G5; no rule on who gates a revision) |
| F4 | Self-written tests are unreliable as the only judge. Reflexion MBPP had 16.3% false positives. SWE-bench passes: 7.8% fail the full tests, 29.6% behave differently from the real fix. | E09.09-K11 | G3, S8 | partly (G3 unfitted check; no ban on own-test-only stop) |
| F5 | Finding the cause (first wrong step, right fault) is harder than fixing it once shown. Best model finds the wrong step in 52.87% on BIG-Bench Mistake. Failed agent runs often reach the right file and fail at fine-grained reasoning. | E09.02-K15, E09.09-K06 | S5, S6, O (localise) | partly (S5 "model names what is wrong"; no localise operator) |
| F6 | In a small study (25 participants) offering fault locations (where, not why) gave no significant gain in correct hypotheses (p=0.41, 0.13) or fix rate (p=0.67), a null result and not proof of no effect; a ranked suspicious-statement list helped only on the easy task and only high performers (Parnin and Orso). Seeing the faulty line did not mean recognising it. | E09.02-K02, E09.02-K17 | S3 | no |
| F7 | Humans in real work rarely state formal testable hypotheses. They hold vague speculations and test by edit-and-run. | E09.02-K05 | S3 | no (design caution only) |
| F8 | Confirmation bias is common in LLMs. More disconfirming tests go with success. Prompts raise rule discovery from 42% to 56%. Boundary: disconfirming tests are required only when the hypothesis is narrower than the truth. Untested on code. | E09.02-K12 | S7, S4 | yes (S7 counterexample search, marked E) |
| F9 | A real debugger or execution trace helps strong models and can hurt weak ones. Handing it over after repeated failed rewrites beat both extremes (Claude 3.7: 52.1 vs 48.4 vs 37.2). | E09.02-K13 | S6, O (probe) | no |
| F10 | Debug loops repair small slips (wrong JOIN, missing clause). Unresolved agent runs are dominated by wrong or over-narrow designs (52%) and flawed reasoning. Loops fix near-misses, not wrong designs. (TRAJEVAL: 56.9% of SWE-agent failures over all 7 models, 64-69% for the five stronger ones, reach and edit the right function and still fail; overwriting a correct edit is 39.7% of those, 22.6% of all failures; wrong branch point 18.6%.) | E09.09-K10 | S6, O | partly (S6 operators exist; no slip vs design test) |
| F11 | Failed edits compound. Edit success is 90.5% after no failure and 57.2% after one. Failed runs are longer. Returns drop after about 25 rounds. | E09.09-K15 | S6 trigger, G1 | partly (S6 fires on same error twice; no failed-edit count) |
| F12 | Most serial-feedback gain arrives in the first 1 to 3 rounds. | E09.09-K28 | S5 | yes (S5 at most 2 rounds) |
| F13 | For strong models, most failures are not localisation. On SWE-bench Verified, 56.9% of SWE-agent failures (weighted over 7 models; 64.7-69.1% for the five capable ones, GPT-5 68.1%) reach and edit the right locations yet give a wrong patch; failed runs hit the gold file in 72-81% of cases on SWE-Bench Lite only (59-67% on Verified). The largest sub-type is coherence collapse (overwriting or thrashing a correct edit, 22.6% of failures). An edit-commit checkpoint recovered all 5 bit-identical-to-gold cases (existence proof only). | E09.09-K34 | S7, S8, G6 | partly (G6 keeps best attempt; no best-checkpoint rule across edits) |
| F14 | Specific feedback beats generic feedback, which beats none. | E09.09-K25 | S5, G2 | partly (S5 cites failing output) |
| F15 | A committee picking among diverse agents' candidate patches beats the best single agent (27.3% vs 34.3%; union about 53%). | E09.09-K22 | S3, S7 | yes (S3 isolated diverse attempts, S7 code selects) |
| F16 | Tool and interface design changes results at a fixed model (SWE-agent 18.0 vs shell-only 11.0; viewer size; linting-guarded edits). CodeAct (up to 20% higher success per its abstract) points the same way; AutoCodeRover does not isolate an interface effect. | E09.09-K13 | harness | no |
| F17 | Non-reasoning models fail to fix an error in their own output but fix it in the user turn (blind spot 64.5% over 14 models; appended "Wait" cut it 89.3%). | E09.09-K19 | S1, S5 | no (see contradiction C5) |
| F18 | Public SWE-bench scores are inflated by leakage, weak tests and flawed items. Held-out and private sets give half or less. | E09.09-K18, E09.09-K36 | G3, G7, harness | partly (G3, G7; no private-split rule) |

## 3. Contradictions between subfields

| # | Contradiction | Claims | Reading |
|---|---|---|---|
| C1 | Is locating the cause the bottleneck? Humans and weak models: yes (F5, F6). Strong agents: no, they reach the right function and fail afterwards or thrash. | E09.02-K15, E09.09-K06 vs E09.09-K34 | Likely depends on model strength and task size. Do not build a heavy localise step before T7 and T4 results. |
| C2 | Repair vs fresh draw. SCHEMA S5 shows the failing output and repairs. Small-model tests say fresh sampling ties or beats re-showing the failed program. Chen (Spider) says repair beats 16 samples, but counts samples, not tokens. | E09.09-K04 (contested), E09.09-K27, E09.02-K14, E09.02-K21 | Unresolved for a reasoning model. Real execution facts tie blind resampling (26 vs 26). Test T2 first. |
| C3 | Does self-debugging need a strong base model? Helps strong models, hurts weak (F9); yet StarCoder gains with traces in one paper and S* shows +3.4 / -2.8 across models. | E09.02-K13, E09.09-K21 (contested), E09.09-K35 | Sign flips with model and benchmark. Per-model gating at S0 is the safe design. |
| C4 | Runtime probes: small margins (LDB +0.6 to +1.8, Aider no effect) vs a large gain from debug-gym pdb after 5 rewrites (+14.9 points). | E09.09-K07, E09.09-K35, E09.02-K13 | Probes may matter only after failure and only for strong models. Matches the "after k failures" trigger. |
| C5 | Self-output blind spot. Established for non-reasoning models; reasoning models show about zero; data are math and logic, not code. | E09.09-K19 vs E09.09-K33 | Fix for non-reasoning only. Do not add colleague framing for a reasoning agent without a test. |
| C6 | Own tests as filter. Good when no real test exists (CodeMonkeys 45.8 to 57.4), poor when public tests exist (S*), and dangerous as the sole judge (F4). | E09.09-K29 (contested), E09.09-K11, E09.09-K12 | Role-dependent: filter among many candidates yes, final judge no. |
| C7 | Textbook scientific debugging (hypothesis, prediction, experiment) vs observed behaviour (vague speculation) vs LLM loop that only matches plain prompting at about 5x time. | E09.02-K05, E09.02-K08 | A forced template has no evidence of benefit. Keep it out of default modes. |
| C8 | Round cap. First turn carries nearly all benefit on Spider; LDB kept improving to 10 iterations on HumanEval; returns cliff near 25 rounds in repo agents. | E09.09-K09 (contested), E09.09-K28, E09.09-K15 | Fits "at most 2 rounds" for puzzle-size items; repo-scale may differ. |
| C9 | Location hints. Humans get no gain from locations (F6) but one coverage-hint result raised LLM code search 57 to 66 resolved, and localiser agreement tracks correctness. | E09.02-K02 vs E09.09-K17, E09.09-K16 (both single-source) | Different consumers (human vs LLM search). Single-source, not decisive. |

Other fields. (a) A01 F9 says falsifying tests track success and thinking models do better, while G11 says think briefly; E09.02-K12 repeats the 42% to 56% result, so it is the same source, not new support (counts once). (b) A01 F10 (refinement plateaus after about 2 rounds, breadth beats refinement) agrees with F12 here. (c) A01 F12 (LLMs rarely falsify their own wrong solutions) agrees with F2 and F4. (d) Both subfields reuse the Olausson 33.3% vs 52.6% result (E09.02-K10, E09.02-K22, E09.09-K05). It is one study, so it is not independent support.

## 4. Recurring mechanisms

| Mechanism | Where it shows | What it says |
|---|---|---|
| Outside signal is the lever, not the loop | F1, F2, F3, F14, E09.02-K09 | Loops help exactly as far as the feedback is real and specific. |
| Own judgment is a weak judge | F3, F4, F5, E09.02-K10 | Self-diagnosis, self-tests and self-stop rules all err. Code and real runs should decide. |
| Diagnosis before repair | F5, E09.02-K04, E09.02-K22 | The right cause predicts success but does not guarantee a fix (6 of 20 humans held it and failed). |
| Early commitment and fixation | E09.02-K07, E09.02-K19, E09.02-K20 | A wrong early hypothesis or supplied cause sends the search wrong. A generic warning only partly helps; naming the exact wrong item removes it. Single-source. |
| Failure accumulates | F11, F13, E09.02-K14 | More attempts in the same context get worse. Keep best, restart clean. |
| Fix slips, redesign wrong designs | F10, E09.09-K23 | Local repair cannot fix a wrong approach. A different operator is needed at the impasse. |
| Diverse candidates, then select | F15, E09.09-K12, E09.09-K29 | Breadth plus code selection beats one long refinement. Same as A01. |
| Strength gates tools | F9, C3, C4 | Debugger, traces and self-debug help strong models and hurt weak ones. |

## 5. Merged tests

All tests: equal total tokens per arm, setup counted, at least 2 seeds, results split by difficulty band. Build a small seeded-bug suite with known causes and hidden tests first (needed by most rows).

| Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|
| T1 Supplied hypothesis and test-the-hint | E09.02-U1, E09.02-U2, E09.02-U7, E09.02-U15 | Arms: none / 1 wrong / 2 (1 right, 1 wrong) / right; plus wrong hint with warning vs a code-forced refuting probe before edit. | High |
| T2 Repair vs fresh draw, and round cap | E09.09-U1, E09.09-U2, E09.02-U6, E09.02-U3 | On items where the first draft fails: one repair from failing output vs fresh draw vs half and half; cap 1, 2, 3, 5; full history vs rejected list vs rejected plus facts; ledger loop vs best-of-N. | High |
| T3 Diagnosis ceiling | E09.02-U4, E09.02-U12 | M short diagnoses with one probe each vs one diagnosis plus extra repairs vs gold diagnosis; log confidence for AUC. | High |
| T4 Keep-best checkpoint | E09.09-U8 | Log how often the last draft is worse than an earlier one; submit best by independent check. Costs no tokens. | High |
| T5 Impasse trigger by failed edits | E09.09-U6, E09.02-U14, E09.09-U7, E09.09-U13, E09.09-U9, E09.02-U13 | Arms: continue / forced relocalise or new operator after k failed edits (k = 2, 5) / abandon design / stall review / probes after k. Measure on items with 2+ failed edits. | High |
| T6 Selector choice | E09.09-U4, E09.09-U5, E09.09-U14 | Own asserts vs differential inputs with real outputs vs vote vs held-out ceiling; fixed localise-repair-select vs free loop. | High |
| T7 First-wrong-step operator | E09.09-U3, E09.09-U10 | Planted bugs: rewrite with named step vs without vs true step; explain vs re-read. Drop if localisation under 50%. | Med |
| T8 Disconfirming-probe rules | E09.02-U9, E09.02-U10, E09.02-U11 | No rule / always disconfirm / scope-matched / required refuting probe; failed probe as rejected vs undecided. | Med |
| T9 Hypothesis count and template | E09.02-U5, E09.02-U8 | K = 1, 2, 4 live hypotheses; free-form vs forced hypothesis-plus-prediction by difficulty band. | Med |
| T10 Private split | E09.09-U15 | Post-cutoff fresh set vs public set with the same agent. | Med |
| T11 Blind spot and localiser agreement | E09.09-U11, E09.09-U12 | Colleague framing or "Wait" for code in reasoning mode; gate extra search on 3-run localiser disagreement. | Low |

## 6. Not to add

| Idea | Why not | Claims |
|---|---|---|
| Model-decided "keep correcting" loops with no outside signal | Break more correct answers than they fix under every gating rule tried. Already barred by 4b. | E09.09-K31, E09.09-K02, E09.02-K11 |
| Imagined debugger output in place of a real run | Plausible-patch rate fell 73% to 63%. | E09.02-K09 |
| Self-written tests as the only final judge | 16.3% false positives, pass@1 fell on MBPP. | E09.09-K11 |
| Location-only or ranked-suspect hints as a hypothesis aid | No significant gain in a small human study (25 participants). | E09.02-K02, E09.02-K17 |
| Many serial repair rounds on one draft | Gain arrives in rounds 1 to 3; failed edits compound. | E09.09-K28, E09.09-K15 |
| Public SWE-bench numbers as proof an element works | Leakage and weak tests inflate them. | E09.09-K18, E09.09-K36 |

Single-source, so not established, but do not add before the test: multi-agent debate as a debugging step (gains mostly extra sampling, E09.09-K20; same as G9); a "distrust the hint" warning as the only guard against a wrong supplied cause (E09.02-K20, test T1); a forced hypothesis-prediction template in default modes (E09.02-K05, E09.02-K08, test T9).

## 7. Gaps

- No LLM replay of the supplied-hypothesis result (humans, N = 20, odds ratio CI 1.1 to 35, Fisher p about 0.18). The "six-fold" claim is weak (E09.02-K01, E09.02-K18).
- Eight subfields are unresearched. The mental-model-first phase (about 57% of professional time) and the scientific-method loop are the largest untouched.
- Most agent data are from older or small models (up to 16B) or from math and logic, not code. Frontier and reasoning models are thinly covered.
- All repo-scale findings (25-round cliff, failed edits, branch points) need repo-style items. Our bench has none.
- Founding classics (Gould, Vessey, Katz and Anderson) were read at abstract level only. The "novices hold early hypotheses" claim rests on them.
- No second, stronger model for the monitor test (E09.09-K32 gain needs one at about 9x cost).
- Wrong-design vs slip labels are LLM-assigned (87% agreement with authors).
- Whether a model recognises the true cause when shown it among candidates is untested.
- Several claims share one source (Olausson, Chen, debug-gym); the 2026-10-26 audit found no further established claim in E09 to downgrade.

**Source audit, 2026-10-26:** 24 established claims in E09 were re-opened against their papers: 20 confirmed, 4 reworded (E09.02-K02, E09.09-K10, E09.09-K13, E09.09-K34, in F6, F10, F16, F13), 0 downgraded. Established claims stay at 24 (8 in 02, 16 in 09). Downgraded ids: none.
