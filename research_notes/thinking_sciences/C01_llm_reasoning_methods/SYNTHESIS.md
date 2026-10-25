# LLM reasoning methods: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl, set before the stricter independence re-check. Treat each row as a candidate until that check is done. "Contested" and "single-source" claims are named only where they matter for a contradiction or a gap. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Almost all evidence here is math or code, and much of it comes from 2023-24 models. Unlike A01, these are results on LLMs, so they apply to the agent more directly, but not to non-numeric tasks.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 04 Verification design | [DEEP](subfields/04_verification_design/DEEP.md) | 31 | 13 |
| 08 Adaptive stopping and metareasoning | [DEEP](subfields/08_adaptive_stopping_and_metareasoning/DEEP.md) | 27 | 8 |
| **Total** | | **58** | **21** |

Contested claims: 5 (C01.04-K06, C01.04-K08, C01.08-K17, C01.08-K18, C01.08-K20). Single-source: 32. Each subfield has an UNKNOWNS.md with 14 test rows (28 in all).

Not yet researched (from SUBFIELDS.md): chain-of-thought prompting; sampling and voting (self-consistency); test-time compute scaling; self-correction; learned refinement and self-verification; search over thoughts (overlaps C05); RL on verifiable rewards; overthinking. Three of these (voting, self-correction, overthinking) are already partly covered by claims in 04 and 08 (for example C01.04-K18, C01.04-K05, C01.08-K09), but not researched on their own.

## 2. Established findings, merged

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | A model-based verifier can be gamed, and more selection pressure makes it worse. Best-of-N against a learned verifier peaks at a finite N and then falls. Higher static accuracy does not predict resistance. Simple adversarial strings fool most LLM verifiers. RL-trained models find shortcuts that pass instance-level checkers. | C01.04-K02, C01.04-K24 | G5, G7, G12 | partly (G5 code selects, G7 pay for itself; no cap on N for model scorers) |
| F2 | A checker with a false-pass rate puts a ceiling on resampling. Weaker generators have higher false-positive rates. With a cost on false passes the best number of tries is small (about 3 to 5). Stop-on-pass beats stop-on-agreement only as far as the checker is sound; known leaks are flaky tests and wrong reference solutions. | C01.04-K03, C01.08-K23 | G3, G7, S4, S8 | partly (G3 held-out pass; no cap K, no false-pass audit) |
| F3 | A model reviewing its own answer without an outside signal does not improve it and often lowers accuracy. Gains in earlier papers came from oracle labels. In reasoning models most rechecks are confirmatory (over 90%) and wrong-to-right flips are rare. Mid-trace self-verification rarely finds errors. The hidden state carries a correctness signal that the model does not use (needs weights). | C01.04-K05, C01.04-K29, C01.08-K21 | G1, G2, S5 | yes (G1, G2, 4b "unstructured self-reflection") |
| F4 | A verifier that writes a check before judging beats a scalar score and a prompted judge, and improves with more sampled checks. | C01.04-K09 | S8 | no (S8 is a final unfitted-part check, no k-check design) |
| F5 | Step-level checks beat answer-level checks on hard maths when right answers hide wrong steps. Open PRMs trained on automatic labels generalise poorly and lose to prompted strong models. Measure any step or prompted verifier on first-error location, not only on final selection. | C01.04-K10, C01.04-K11 | S8, G3 | no |
| F6 | LLM judges carry position bias, verbosity bias and self-preference (tracks self-recognition). Fixes: hide authorship, judge in both orders, use another family where possible, give a code reference answer. | C01.04-K12, C01.04-K14 | G5, S8 | partly (G5 blind, length-normalised; no both-orders rule, no family rule) |
| F7 | Checks written after seeing the candidate catch fewer faults (14% vs 25% written from the task text). Model-written tests share the generator's errors, so they are weak independent evidence. Chain-of-thought and verification prompting do not repair it. | C01.04-K17 | G3, G4, S4 | partly (G3, G4; no spec-first, fresh-context rule) |
| F8 | Spend by difficulty. Allocation by difficulty bin matches best-of-N with up to 4x less compute (oracle bins; gain shrinks with predicted bins). Beam search wins at low budget and on hard items; best-of-N wins on easy items. Savings from adaptive rules are large on easy data and small on hard data. A cheap pilot of 2 to 4 samples, stopped on agreement, is a usable difficulty signal. | C01.04-K16, C01.04-K30, C01.08-K02 | S0, G12 | yes (G12 "spend by difficulty"); pilot-agreement route partly (no pilot rule) |
| F9 | Stopping sampling when the vote is stable cuts samples about 2x to 5x with accuracy near unchanged, but the factors are measured against 40 samples. Against 16 samples the saving is 4% to 71%, and when the prompt is re-sent each round the saving can vanish. Always report total tokens (input plus output) against fixed small baselines. | C01.08-K01, C01.08-K19 | S3, G7, G11 | no (G11 says short attempts; no stop rule, no cost accounting rule) |
| F10 | Within one question, correct chains are shorter than wrong ones. Overthinking on easy items is real (first round correct in over 92% of cases with under 60% of tokens; early exit cuts chains 19% to 80% with accuracy flat or up). Prefer cap and restart to extending. | C01.08-K08, C01.08-K09 | G11, S3 | partly (G11 cap per mode and short attempts; no restart, no exit rule) |
| F11 | The ideal stop rule (stop when no computation has expected value above cost) is intractable; myopic approximations stop too early where one step is worth zero but several pay. Keep the stop decision in code, with a cost term and a minimum-sample floor. | C01.08-K15 | G5, S3, S6 | no |

Claims with no schema action: none among established ones. Check: all 21 established claims appear above (04: K02, K03, K05, K09, K10, K11, K12, K14, K16, K17, K24, K29, K30; 08: K01, K02, K08, K09, K15, K19, K21, K23).

## 3. Contradictions between subfields

| # | Where the claims disagree | How to resolve |
|---|---|---|
| C1 | **Verify-then-vote vs plain voting.** Contested C01.04-K08: voting is more compute-efficient than a generative verifier below about 8x compute (fine-tuned verifiers). Single-source C01.04-K22: prompted verification beat 1000-sample consistency on AIME (8/15 vs 3/15) at about 130M tokens per question, and lost on AIME in another setting (28.3 vs 32.2). F9 says compare at total tokens. | Depends on whether checking is easier than solving in the class. Equal-token test, split by pilot agreement: C01.04-U1, C01.04-U2. |
| C2 | **Is LLM self-verification reliable?** Contested C01.04-K06: GPT-4 rejected 95.8% of correct graph colourings (FNR) vs recall 92 to 94% on Trip Planning plan checks and 7 to 23% error on maths. F3 says self-review without a signal does not help. C01.04-K23 (single): o1-preview flags 27% of unsolvable instances. | Task- and model-specific. Do not assume either. Build a per-class FNR/FPR table: C01.04-U4. |
| C3 | **Does a second look help?** Forced reconsideration at high entropy lifted maths 32.2% to 40.6% (C01.04-K29, small RL models, needs logits). Forced Wait gave small gains (single C01.08-K11). But over 90% of reflections are confirmatory (C01.08-K21) and prompted correction lowers accuracy (C01.04-K05). | Not a real conflict if the trigger is a signal and not a schedule. Match G1. Test: C01.04-U3, C01.08-U4, C01.08-U14. |
| C4 | **Is agreement a safe stop and selection signal?** Pilot agreement works as a difficulty signal (C01.04-K30, established) and vote-stability stops save samples (C01.08-K01). But contested C01.08-K18: no paper counts unanimous-wrong stops (simulation range under 1% to over 50%). Contested C01.08-K17: agreement fails when samples share an error. C01.04-K28 (single) finds majority-vote errors negatively correlated in one olympiad setting, which sits oddly beside G4 (samples are not independent). | Agreement measures agreement with a large vote, not truth. Count wrong stops on our labelled sets before relying on it: C01.08-U1. Treat K28 as one setting. |
| C5 | **Can difficulty be estimated cheaply enough to route?** C01.04-K16 shows 4x with oracle bins and a smaller gain with predicted bins. Contested C01.08-K20: coarse bins are cheap (72 to 87%), fine bins need about 16 samples, and routing can lose to a fixed budget at high compute. | Use coarse classes only. Test: C01.08-U3, C01.04-U5. |
| C6 | **Stopping at a verified answer.** Early exit at the first complete solution is safe on maths (C01.08-K09, established). Stopping at the agent's own first self-verified answer lost 6 to 8 points (single C01.08-K22). Stop-on-pass is good only if false-pass is low (C01.08-K23). | Different verifiers: stable trial answer, self-verification, code check. Rank by false-pass rate: C01.04-U4, C01.08-U10, C01.08-U9. |
| C7 | **More budget for verification vs ceilings.** C01.04-K19 (single): verifier-based methods pull ahead as test-time spend grows. C01.04-K02, C01.04-K03 and C01.04-K18 say learned selectors plateau or reverse and that the selector is the bottleneck (coverage 98.44% vs 41.41%). | Both hold: code checkers scale (C01.04-K01), vote and learned scorers do not. Reserve share is untested: C01.04-U14. |
| C8 | **With other fields (A01 synthesis).** A01 F12 calls code verifiers cheap and accurate; C01.04-K04 and C01.08-K23 show they leak (flaky tests, wrong reference solutions), so the code check itself needs an audit. A01 C6 and this field agree: stated confidence is barred and agreement is a candidate signal only after tests. A01 C5 (solver as gated tie-break) fits C01.04-U2 (pairwise tie-break on close votes). A01 C3 (thinking helps search, hurts easy items) fits F10: cap by class, not globally. A01 F10 (breadth beats refinement) fits C01.08-K10 (single: revision rarely fixes, parallel gives better coverage). | No action beyond keeping the checker audit (T1) in front of every code-run claim from A01. |

## 4. Recurring mechanisms

| Mechanism | Subfields and claims | What it means for the agent |
|---|---|---|
| **An outside signal is needed to change an answer** | 04 (K05, K29), 08 (K21, K10, K11) | Self-review, reflection and Wait cues mostly confirm. Revise or recheck only on a failed check or a disagreement (G1, G2). |
| **The selector is the bottleneck, not the sampler** | 04 (K01, K18), 08 (K06) | Coverage keeps rising with samples; vote and learned scorers stall far below it. Spend on better selection (a sound checker) before more samples. |
| **Checker false-pass rate caps everything downstream** | 04 (K03, K04, K17, K25), 08 (K23) | Audit the checker on known-wrong outputs, write it from the spec in a fresh context, cap the number of tries, re-run on a perturbed copy. |
| **Same-model errors are correlated** | 04 (K14, K17, K25, K28), 08 (K17, K18) | Generator, test writer and judge from one model share mistakes and favour their own text. Hide authorship; do not read agreement as proof (G4). |
| **Spend by difficulty and class** | 04 (K16, K30), 08 (K02, K07, K20, K24, K25) | Savings are large on easy items and small on hard. Set budget and stop point per class and per model, using a 2 to 4 sample pilot and the class record. |
| **Shorter is better within an item** | 08 (K08, K09), 04 (K29) | Correct chains are shorter. Cap and restart; do not ask for longer thinking when a chain runs long. |
| **Savings depend on the baseline and the accounting** | 04 (K08), 08 (K01, K19) | Quote cost as total tokens against fixed k = 4, 8 and 16, not 40. The same rule applies to verifiers (equal tokens). |
| **Evidence is narrow** | all | Nearly all numbers are maths or code, with many from 2023 models. Treat sizes as direction, and fill the table on our own model and tasks. |

## 5. Merged tests

Each row merges UNKNOWNS rows that share one design.

| # | Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|---|
| T1 | **Checker and verifier error table** | C01.04-U4, C01.08-U10 | 30 to 100 labelled right and wrong candidates per class; single check vs 4-check majority vs code check; FNR, FPR, false-pass rate. Enable reject loops or pass-stops only where FNR <= 20% and FPR or false-pass <= 5 to 10%. Run first; gates T3 to T7. | High |
| T2 | **Wrong consensus on early stops** | C01.08-U1 | Stop at 4 unanimous vs plus a second signal vs fixed k=8, on ARC, BRAINTEASER and maths, 150+ items; wrong share of stopped items and accuracy at equal tokens. | High |
| T3 | **Pilot-agreement router and per-model gate** | C01.04-U5, C01.08-U3, C01.08-U8, C01.08-U12, C01.08-U5 | Fixed best-of-4 vs 3-class route from 3 to 4 pilot samples (agree: stop; split: verify; flat: code check or deeper) vs oracle bins; include think-depth route, DSC-style rank-then-allocate, and a per-model calibrated threshold on two model sizes; 150 to 200 items. | High |
| T4 | **Verify-then-vote and tie-break** | C01.04-U1, C01.04-U2, C01.04-U7, C01.08-U6 | Run the pairwise 2-order tie-break on close votes (top-two gap under 10 points) first; then k=4 check chains at S/2 samples vs vote at S; then accuracy-weighted vs unweighted checks; P(True)-weighted vote with the extra call counted. Equal total tokens, split by easy and hard bins. | High |
| T5 | **Second-look trigger** | C01.04-U3, C01.08-U4, C01.08-U14 | No recheck vs one more sample vs recheck only on disagreement or weak first answer vs forced Wait; log right-to-wrong and wrong-to-right flips by first-answer correctness; drop revision per class if net flips are not positive. | High |
| T6 | **Stop-rule form** | C01.08-U2, C01.08-U13 | Window rule vs myopic value-of-computation rule with a 3-sample floor at equal mean tokens; mid-trace partial-answer agreement as a stand-in for token confidence when logprobs are missing. | Med |
| T7 | **Length cap, restart, early exit and budget counter** | C01.08-U11, C01.08-U9, C01.08-U7 | Check within-item accuracy by length quantile on existing traces first; then long chain vs cap and restart vs two short chains; exit when a trial answer is unchanged at two transitions; hidden cap vs visible remaining-budget counter. | High |
| T8 | **Checker hygiene** | C01.04-U6, C01.04-U8, C01.04-U9 | Resample cap K=3, 5, 10, 30 against a draft checker; tests written after the candidate vs spec-only same model vs spec-only other family; accept-on-pass vs pass plus perturbed re-run; held-out false-accept rate. | Med |
| T9 | **Judge hygiene** | C01.04-U10, C01.04-U13 | No reference vs sampled reference (independent call) vs code reference; same-family shown vs hidden vs other-family hidden; misgrade rate and own-output preference. | Low |
| T10 | **Step checks off maths** | C01.04-U11 | Rate of right answer with wrong reasoning per class, strong critic plus human audit; step check as selector lift. | Low |
| T11 | **Failed-attempt memory and verification reserve** | C01.04-U12, C01.04-U14 | Failed-attempt line after the first attempt vs none; 20% budget reserve for S8 vs all on generation. | Low |

Order to run: T1 first (it gates T3 to T8), then T2 and T7 (cheapest; reuse existing traces), then T4 (tie-break part) and T3. T5 shares item pools with T3.

## 6. Not to add

| Idea | Why not | Claim ids |
|---|---|---|
| Default self-review or reflection round after the first answer | Over 90% of reflections confirm; wrong-to-right under about 2%; prompted correction lowers accuracy; already in 4b | C01.04-K05, C01.08-K21, C01.04-K29 |
| Model's stated confidence as a stop or doubt signal | Within-question discrimination 52 to 62%; agreement is better but only a hint; already in 4b | C01.08-K17 (contested), C01.08-K04 (single) |
| Learned scorer or model judge picking among very many samples without a cap and a held-out check | Best-of-N peaks then falls; verifiers get gamed | C01.04-K02, C01.04-K24 |
| Model-written tests, or tests written after seeing the code, as independent evidence | Errors correlate; fault detection drops from 25% to 14% | C01.04-K17, C01.04-K25 (single) |
| Step-level scorers outside the domain they were trained on | Math PRMs add at most +0.71 over voting off maths | C01.04-K11, C01.04-K26 (single) |
| Savings quoted against 40 or 512 samples | They shrink against 16 samples and when input tokens are counted | C01.08-K19 |
| Stopping at the agent's own first self-verified answer | Lost 6 to 8 points | C01.08-K22 (single), C01.08-K23 |
| Debate and prompt-diversity voters | Debate did not beat self-consistency at equal responses; diversity lowered the score. Already G9 | C01.04-K15 (single), C01.04-K28 (single) |
| Forced "Wait" extension as a main lever | Small gains that flatten; 2 problems of 30 on AIME | C01.08-K11 (single) |
| Trained levers: RL length control, RaM reward, V-STaR verifiers, learned PRMs, hidden-state probes | Need training or weights; a text scaffold cannot reach them | C01.08-K12, C01.08-K13, C01.04-K20, C01.04-K21, C01.04-K29 |
| Token-level confidence stops (DeepConf) | Need logprobs; no outside replication | C01.08-K05, C01.08-K27 (single) |
| Human metareasoning data as support for a stop rule | Theory support only, no schema action | C01.08-K14 (single) |

## 7. Gaps

- **Eight of ten subfields unresearched:** chain-of-thought, voting, test-time scaling, self-correction, learned refinement, search over thoughts, RLVR, overthinking (see section 1). The voting and overthinking claims here are second-hand.
- **No numbers outside maths and code.** Free-text and open-mode tasks have no answer to vote over or check. Needs a small set with a grader that is not a model opinion (C01.08 open questions, C01.04 open questions).
- **No current-model data for self-verification.** All intrinsic self-correction tests are on GPT-3.5/4, Qwen2.5-Math-7B and small RL models. T1 and T5 on our model are the only fill.
- **No equal-token crossover curve** for verify-then-vote (C01.04-K08 contested). T4 produces it.
- **Wrong-consensus rate is unmeasured** for vote-stop rules on non-maths items (C01.08-K18). T2.
- **Error correlation between solver and verifier on hard items** is not measured anywhere (C01.04 open questions).
- **Verifier gaming at inference time** (selection only) lacks data; the hacking evidence is RL-based (C01.04-K24). Peak test: sweep N for a model-judge selector.
- **Thin replication.** DeepConf, DSC and ReASC were run only by their authors (C01.08-K27). Many 08 claims are single-source; only 8 of 27 are established.
- **Logprobs:** several signals (P(True), DeepConf, RaM) need token probabilities. Check whether our API exposes them.
- **Independence of "established" claims is unchecked.** Re-run section 2 through the stricter check before any row enters SCHEMA.md.
