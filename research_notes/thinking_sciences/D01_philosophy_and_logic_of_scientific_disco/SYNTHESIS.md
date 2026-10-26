# Philosophy and logic of scientific discovery: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means status "established" in claims.jsonl. Only 2 of the field's 10 subfields are researched, so this is a partial view. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Most human-side findings in this field are single-lab; the established set is mostly LLM results on 2023-24 models (GPT-4 class), so sizes are design hints until rerun on our model.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Abduction and inference to the best explanation | [DEEP](subfields/01_abduction_and_ibe/DEEP.md) | 33 (17 single-source, 3 contested, 2 open) | 11 |
| 02 Proofs and refutations (conjecture refinement) | [DEEP](subfields/02_proofs_and_refutations/DEEP.md) | 34 (30 single-source) | 4 |
| **Total** | | **67** | **15** |

Each researched subfield has a UNKNOWNS.md: 14 test rows for 01 and 16 for 02 (30 in all).

Listed in SUBFIELDS.md but not yet researched: research programmes (Lakatos); falsificationism (Popper); anomalies and paradigm change (Kuhn); heuristic programming and machine discovery (BACON, KEKADA, robot scientists; rated High and named in "Dig into next"); methodologies of discovery (Nickles, Schaffner, Darden, Laudan); cognitive approaches (analogy, model-based reasoning); social epistemology of discovery (background only); pragmatic logics (background only).

## 2. Established findings, merged

Where two claims describe one source, they are merged and counted once. D01.02-K12 and D01.02-K13 repeat the Wang et al. and Qiu et al. results already in D01.01-K02; they are single-source in 02 and add no independence.

| # | Finding | Claim ids | Schema part | Already in SCHEMA.md? |
|---|---|---|---|---|
| E1 | SEP presents Peirce's cycle as abduction forming explanatory hypotheses, deduction drawing testable consequences and induction judging the hypothesis by how many consequences hold; Frankfurt reads abduction as picking hypotheses worth investigating (SEP questions that reading for Peirce), and Hanson's retroductive schema yields a type of hypothesis worth elaborating. Generate-then-test is the classic frame; the discovery-machine objection says no rule mechanically outputs good hypotheses. Secondhand via SEP only. Our rule that a hypothesis counts as accepted only after code has run it is a design choice (G3, G5), not part of the source claim. | D01.01-K01 | S3, S4, G3, G5 | yes (G3, G5, S4). The logged rate of S3 candidates rejected at S4 is not there. |
| E2 | A generate-then-test loop whose test is run by code beats direct prompting (ARC 17% to 30%; ACRE task accuracy 28 to 59, GPT-4). It is not universal: MiniARC raw accuracy fell from 33.1 to 18.7. | D01.01-K02 | S3, S4, S5 | partly (S3/S4 loop yes; per-class evidence of when it loses is not stated) |
| E3 | The loop helps when the true rule is short and symbolic, and fails on perceptual or wide-context rules. Read across three papers; no head-on test. Route in S0 by a cheap check: does some short program fit the examples? | D01.01-K28, D01.01-K02 | S0 | partly (S0 gate exists as [S]; this criterion is new) |
| E4 | Fit to the shown examples is a weak gate. CodeARC: 67.6% pass the examples, 38.9% pass the oracle. BARC: about 9% of fitting programs are false. Test suites also err (11.3% of SWE-bench Lite problems have flaky tests). Use held-out or differential checks and measure each gate's own precision. | D01.01-K25 | G3, S4, S7 | yes (G3, S7 discriminating test). Gate-precision logging is not there. |
| E5 | The correct hypothesis is often in the pool but not chosen. MATH Llama-3-8B: coverage 98.4% vs 41.4% for the vote or reward-model pick. A strict code check closes much of the gap (SWE-bench Lite 15.9% to 56%). Log pool coverage next to accuracy. | D01.01-K23 | S7, G5, G3 | partly (G5 code selects; no pool-coverage log) |
| E6 | Choosing among given explanations is near human level on short commonsense items, not on long or open tasks. Producing explanations is much weaker (ProofWriter abductive 21.5%; diagnosis hit@3 63 vs 98.7 when ranking given options). Generation is the weak half. | D01.01-K04 | S3, S7 | partly (S3 open mode spends on diversity; G8 bars a model selector) |
| E7 | Accuracy falls fast as the number of required or interacting causes grows (above 80% at height 1 to below 50% at height 2; attribution 0.90, 0.32, 0.15 for zero, one, two or more rule changes). | D01.01-K06 | S2, S3, S6 | no |
| E8 | Deduction skill does not predict abduction skill (pooled medians 79.96% vs 42.50%; same syllogism content 72.2% deduction vs 41.7% abduction for GPT-4). Medians pool mixed datasets: rough ordering only. | D01.01-K07 | bench, S0 class record | no |
| E9 | Models almost never say no explanation fits (GPT-4 "Neither" 0.00%; reasoning fine-tuning lowers abstention recall 24% on average on AbstentionBench). Instructions rescue some models and not others. No test uses a pool lacking the true explanation. | D01.01-K08 | G6, S7, S8 | partly (G6 never abstain; no code flag for a bad lot) |
| E10 | Standard IBE has two stages; Dellsen adds a consolidation stage and replaces "best" with "good enough". The bad lot is unresolved. Accept only a candidate that passes an unfitted check; otherwise return to S3. Philosophical, no measured result. | D01.01-K18 | S7, S8 | no |
| E11 | Few-shot demonstrations help abduction only when matched to the test and are unstable across models (GPT-4 41.7 to 28.7; Llama-3-70B to 75.5). | D01.01-K09 | S3 | no |
| E12 | Without an external check, model self-correction does not help reasoning and can hurt (GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0). Earlier gains came from oracle labels. | D01.02-K07 | G2 | yes (G2, 4b) |
| E13 | Executable or tool feedback gives repair gains that model-only feedback does not (CRITIC 42.0 to 50.0; Self-Debug MBPP 72.8 to 80.4 with unit tests vs +3.6 without; Reflexion HumanEval 91.0 vs 80.1, which is against a no-reflection baseline, not a model-only-feedback contrast). | D01.02-K09 | G2, S5 | yes (G2, S5 locates failure by code). The "specific, located feedback" detail is only partly stated. |
| E14 | Repair loops silently change the claim. An Isabelle audit found 16 of 100 original declarations changed; statute repair left 15-45% meaning drift; a protected-statement diff rejected a weakened theorem the prover accepted. No seeded-set rate exists. | D01.02-K26 | new guardrail (G13) or S8 | no |
| E15 | Dropping a hypothesis from a proved theorem is a cheap source of candidate false conjectures. Li et al. made about 575K candidate counterexample problems in Lean from 212,463 seed theorems (candidates, not all confirmed false); Zouak et al.'s SymCE has 4,707 false statements with verified witnesses and a 97.7% accurate verifier. A test-bed source, not an agent part. | D01.02-K17 | evaluation | no (evaluation only) |

## 3. Contradictions between subfields

| # | Where sources disagree | How to resolve |
|---|---|---|
| C1 | **Does hypothesis-then-test help?** Helps: D01.01-K02 (ARC, ACRE), D01.02-K12 and K13 (same sources). Hurts: D01.01-K02 itself (MiniARC 33.1 to 18.7), D01.01-K28 (InductionBench near 0). | Class-dependent, not a conflict. Route in S0 (D01.01-U12) and compare with always-direct. Do not generalise from ARC. |
| C2 | **Is repair worth its tokens?** Tool feedback gives gains over no repair (D01.02-K09). But single-source D01.02-K10 and K24 say repair is break-even with fresh sampling, and a Lean restart beat sequential repair. A01.09-K18 and A01.02-K21 say refinement plateaus after about 2 rounds. | The gains in K09 are against no-tool repair, not against resampling. No established claim compares repair with restart at equal tokens. Decide with D01.02-U3. Keep SCHEMA S5 at 2 rounds until then. |
| C3 | **Vote as selector.** SCHEMA S7 records a code selector beating the vote by one item (34 of 36 vs 33 of 36). D01.01-K23 says the vote loses most of the pool's coverage (98% vs 41%) and an oracle pick beats self-consistency by 6 to 20 points. | Same direction: the vote is a weak selector when a strict check exists. The size depends on the class. Run D01.01-U6 and log pool coverage. |
| C4 | **Flag the bad lot vs never abstain.** D01.01-K08 and K18 want a "no candidate fits" flag. SCHEMA G6 says never abstain on the first pass. | Not a conflict if the flag comes from code and only triggers a new S3 pass or a marked low-confidence submit. Never from model self-report (K08). Test: D01.01-U3. |
| C5 | **Extra reasoning.** D01.01-K08 says a larger reasoning budget lowers abstention; D01.01-K30 (single-source) says reasoning effort does not fix attribution. A01 F9 and A01.02-K10 say larger thinking models falsify more. SCHEMA G11 says think briefly. | Depth helps when hypotheses must be searched and hurts when the right output is "none fits". Cap by class (A01 C3). Test with the extended-thinking arm named in SCHEMA section 7. |
| C6 | **Models as judges of explanations.** D01.01-K04: near-human ranking of given short explanations (ART 87.2). SCHEMA G8 and G5: model judges rank ideas near chance and favour long text. | Different tasks. Short, closed, commonsense choice is fine for a judge; novelty and long open tasks are not. For the schema, keep code selection and treat K04 as a reason to spend on generation. |
| C7 | **Counterexample search.** D01.02-K09 (code feedback works) fits A01.07-K12 (LLMs falsify under 9% unprompted) and single-source D01.02-K14 (REFUTE best 8.3%). A01.01-K30 shows slow gains from a bare "wrong". | Consistent only if code builds and runs the search and the model reads the result. Merged with A01 C4. Test: D01.02-U5, D01.02-U6. |
| C8 | **Self-explanation.** SCHEMA S2 cites self-explanation as [E] (F03, F11). Single-source D01.01-K27 says explaining before predicting pushes LLMs to the broad rule and slows learning of exceptions. | Not established against it. Test D01.01-U5 (exceptions list) before changing S2. |
| C9 | **Abduction as a gap in A01.** A01 section 7 lists abduction as untested (one study, 42% vs 72%). D01.01-K07 now has two sources. | Update the A01 gap line when A01 is next patched. |

## 4. Recurring mechanisms

| Mechanism | Subfields and claims | What it means for the agent |
|---|---|---|
| **Code is the test, the model proposes** | 01 (K01, K02, K25), 02 (K07, K09) | The same rule from both sides. Hypotheses and repairs are accepted only on a code run against a part the candidate was not fitted to. |
| **Pool has the answer, selection loses it** | 01 (K23, K04, K25), A01.09-K18 | Spend on breadth and on a strict selector. Log coverage so the loss is visible. |
| **Fit gate is weak** | 01 (K25), 02 (K26 for the claim-side version), A01.09-K22 | Held-out or differential checks. Measure the gate's own precision. The same idea applies to the claim text itself (E14). |
| **Nothing-fits is invisible to the model** | 01 (K08, K18), A01 "nothing follows" (A01.01-K06, A01.03-K34) | Two fields show the same failure: models answer from what they have and do not offer "none". Fix once, with a code flag. |
| **Interacting causes break the model** | 01 (K06), A01.01-K05 (single-source, models held) | Difficulty tracks how many things must hold at once. A code-built table of what changed is the candidate fix (D01.01-U4). |
| **Silent change of the question** | 02 (K26), A01 surface brittleness (A01.01-K27) | The statement the loop works on must be fixed and diffed (E14). |
| **No matched resampling control** | 02 (K22, single-source), 01 (K02 vs MiniARC) | Every loop in this field must be tested against best-of-N and restart at equal tokens, counting input tokens (G7). |

## 5. Merged tests

Each row merges UNKNOWNS rows that share one design. Run the extended-thinking baseline of SCHEMA section 7 as an arm wherever a loop is tested.

| # | Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|---|
| T1 | **Loop router and loss accounting** | D01.01-U12, D01.01-U13, D01.02-U14 | 100+ rule-induction items: always-direct, always-hypothesis-then-code, S0 router on "does any short program fit"; log pool coverage and implementation loss; max 3 feedback rounds; compare with best-of-N at equal tokens. Run first. | High |
| T2 | **Selector and gate on hypothesis pools** | D01.01-U1, U2, U6, U7, U8, U9 | Pools of 8 to 16 candidates with known truth. Arms: vote; blind length-normalised judge; fit gate; fit plus held-out; plus code virtue score or parsimony count; optional small bonus and simplicity term (U7, U8 are low-priority extra arms). Metric: top-1 hit, false accepts, gap to oracle. | High |
| T3 | **Bad-lot flag** | D01.01-U3, D01.01-U14 | Same pools with the true rule deleted. Code gate "no candidate passes the unfitted test" vs the instruction line "flag if none fit". Metric: recall at 10% false alarm, accuracy on pools with a truth. | High |
| T4 | **Code-run counterexample search and false refutation** | D01.02-U5, D01.02-U6 | Seeded true and false claims (COUNTERMATH-style plus mutation sets). Prompt-only refute vs code enumeration, random and mutated inputs; leave the claim standing when nothing is found. Metric: find rate, false-refutation rate, invalid share. | High |
| T5 | **Locate step and refute framing** | D01.02-U2, D01.02-U10, D01.02-U11, D01.02-U12 | Numbered-step output vs free form; third-party framing in a fresh context; challenge-and-defence critic for no-executor classes; hidden-lemma probes vs "what did the proof assume?". Metric: fault-location accuracy, false refutations, fix rate. | Med |
| T6 | **Repair budget and stop rule** | D01.02-U3, D01.02-U7, D01.02-U9, D01.02-U16 | Pure restart vs long repair vs 2 to 3 rounds then restart, split by error type; worth-saving gate; patch counter at 2 exceptions; stop at a fixed point. Equal tokens. | High (U3); Med to Low (others) |
| T7 | **Typed counterexample repair (the Lakatos test)** | D01.02-U1, D01.02-U8 | Seeded false claims: code-typed repair (global-only, local-only, both) vs untyped reflect vs best-of-N; coverage meter against over-narrowing. Run after T6 fixes the budget. | High |
| T8 | **Statement-fidelity guard** | D01.02-U4, D01.02-U15 | Seeded claims, repair loops with and without a claim-diff check and a guarded redefinition path. Metric: drift rate, repair success. Cheap; run alongside T4 to T7. | High |
| T9 | **Interacting-cause table and impasse** | D01.01-U4, D01.01-U10, D01.01-U11 | Hidden-cause ladders with 1, 2, 3 causes, long mysteries: code-built diff or fact table, S6 operator tied to cause count, confidence-gap stop, vs plain, CoT and extended thinking. | High (U4); Med (U10, U11) |
| T10 | **Exceptions list** | D01.01-U5 | Vehicle-style rule-plus-exceptions task: direct, self-explain, self-explain with a separate exceptions list. | Med |
| T11 | **Counterexample store** | D01.02-U13 | Re-run stored counterexamples first on each revision; count refutation tokens saved. | Low |

Order to run: T1 first (it says where the loop belongs), then T2 with T3 on the same pools, then T4 and T6, with T8 logging alongside. T7 last, against the strongest untyped control.

## 6. Not to add

| Idea | Why not | Claim ids |
|---|---|---|
| Generic self-critique and revision without an executor | Lowers accuracy in the verified cases; already in SCHEMA 4b | D01.02-K07 (established) |
| Accepting a hypothesis on a virtue score (simplicity, scope) alone | "Loveliness is not likeliness"; virtue scores may only break ties after a passed unfitted check | D01.01-K18 (established), D01.01-K17 (contested) |
| Letting the model apply its own proposed rule instead of a code interpreter | The gain mostly disappears (ACRE 82.5 down to 70.0) | D01.01-K03 (single-source), D01.02-K12 (single-source) |
| Asking the model to say "none fits" and trusting it | Models almost never do (0.00% "Neither") | D01.01-K08 (established) |
| Fixed few-shot exemplars in S3 | Unstable across models and classes | D01.01-K09 (established) |
| Inferring abduction skill from deduction scores | The two differ by about 37 points in pooled medians | D01.01-K07 (established) |
| Human simplicity preference as an LLM prior | One lab; outside labs find no general preference | D01.01-K13, K33 (single-source, contested) |
| Explanatory bonus on credence | Simulation-only; early false confidence; best size small | D01.01-K26 (single-source), D01.01-K17 (contested) |
| Multi-role frameworks (abductive, deductive, inductive agents) and multi-agent HRL | Conflicts with G4 and G9 | DEEP 9 of both subfields |
| Pease's numbers, thresholds and interestingness as outcome | Three toy domains, self-defined and circular measure | D01.02-K03, K28, K29 (single-source) |
| Lakatos' method as a source of first ideas | It repairs an existing attempt and does not generate one | DEEP 9 of subfield 02 |
| Training-based results (GEAR DPO, SymCE RLVR, SFT on counterexamples) | We scaffold only; counterexample drill alone broke truth recognition (0.27 to 0.00) | D01.02-K16 (single-source) |
| Counterexample drill or "always try to disprove" as a prompt | Teaches the output shape and breaks truth handling | D01.02-K14, K16 (single-source) |
| Unguarded monster-barring (silent redefinition) | The main way an agent changes the claim without notice | D01.02-K06 (single-source), D01.02-K26 (established) |

## 7. Gaps

- **Thin evidence base.** 15 established claims from 67. Subfield 02 is 30 of 34 single-source, and many rest on 2026 preprints from single groups.
- **Eight subfields not researched:** research programmes, falsificationism, anomalies and paradigm change, heuristic programming and machine discovery (rated High, "Dig into next" number 3), methodologies of discovery, cognitive approaches, social epistemology, pragmatic logics. The "stop patching" signal (degenerating programme) and the anomaly trigger for S6 have no evidence here yet.
- **Old models.** Most numbers come from GPT-4 and 2023-24 setups. Direction is robust (code test helps); size is not. Rerun a small subset on the deployed model before trusting sizes.
- **No bad-lot benchmark.** U3 pools are built by deleting the true rule. A natural source of pools with no true answer is missing (D01.01-K29, open).
- Single lab only: no Lakatos-labelled LLM loop (monster-barring, lemma-incorporation, concept refinement) with a matched resampling control was found; LLM work measures pieces only and Pease's own evaluation had no baseline (D01.02-K22, one opened source, not established). Our T7 is that design; its motivation rests on this single-source claim alone.
- **Formal tools absent from the bench.** Lean, model finders and a numbered-step proof corpus are missing, so the restart-beats-repair result (D01.02-K24, Lean, 11 sequential problems per model) cannot be checked here.
- **Philosophy is secondhand.** Peirce, Hanson, Harman and Lipton are read through SEP only. The 2017 dialogue-game paper was read as an abstract only (D01.02-K34).
- **Human results are single-lab.** The simplicity preference and the explanation-and-credence data rest on one lab; outside work finds no general preference (D01.01-K13, K33).
- **Real-world abduction.** Diagnosis and debugging evidence is one paper plus synthetic sets.
- **Cross-field links not yet merged.** Conjecture refinement shares S6 and S7 questions with lemma discovery, conflict-driven clause learning, analogical access and bandits for operator choice; their UNKNOWNS files should be merged with T2, T6 and T7. The A01 gap line on abduction (C9) needs updating.

**Source audit, 2026-10-26:** the papers behind all 15 established claims of this field were re-opened. 13 confirmed, 2 reworded (D01.01-K01, D01.02-K17), 1 downgraded to single-source (D01.02-K22). E16, which cited K22, was removed from section 2 and moved to Gaps as single lab only. The T7 motivation and the mechanism row "No matched resampling control" rested on K22 alone and are now flagged single-source.
