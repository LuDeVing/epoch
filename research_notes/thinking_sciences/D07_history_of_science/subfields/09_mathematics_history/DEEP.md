# Mathematics history: deep document

*Subfield D07.09: Conjecture and proof development (Lakatos, Polya). Sources: evidence_a-d.jsonl, claims.jsonl (K01-K22), critique.md in this folder. Evidence ids (a01...d18) point to the jsonl lines. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

This subfield asks how mathematical claims are born and repaired. Two founders matter.

- **Polya** (How to Solve It, 1945; Mathematics and Plausible Reasoning, 1954) gave a four-phase method (understand, plan, carry out, look back) and about twelve named heuristics (specialise, generalise, analogy, auxiliary element or problem, decompose and recombine, work backwards, vary the problem, induction). He described how people guess. [a03, a21]
- **Lakatos** (Proofs and Refutations, papers 1963-64, book 1976) described how a guess lives after it is made. A naive conjecture gets a proof. A counterexample appears. The proof, the claim, or the definitions are then changed. The loop repeats. The worked case is Euler's V-E+F=2 for polyhedra. [a01, a02]

For our agent this is the logic of conjecture refinement (links to D01). The agent proposes a claim or a rule, tries to break it with code, then repairs it using the located failure. Schema parts touched: S3 generate, S4 test, S5 revise, S6 impasse, S9 look back, operators O1 (specialise), O2 (generalise), O3 (decompose), O4 (drop a constraint), O7 (analogue), and guardrails G2, G3, G5, G8.

What this folder adds beyond earlier documents: measured funnels for model-made conjectures, the human-AI conjecture loops of 2021-2026, proof-writing benchmarks, and the (thin) tests of Polya-style prompting. No controlled test of Lakatos moves on LLMs exists. That absence is itself the main finding. [K05, K21, d18, b26]

Evidence quality warning. Lakatos 1976 and Polya 1945/1954 were never opened as primary texts. Schoenfeld 1985 was seen only through Wikipedia. [critique] Several 2026 items were read at abstract level only. Each table row below carries its status.

Linked subfields researched in parallel (not covered here): Problem posing and conjecture; Anomalies and paradigm change; Conceptual change and revolutions; Interactive theorem proving; Neural and LLM proof search; Proof planning and repair; Scientific discovery systems; Methodologies of discovery; Integrated HPS and the method of case studies; Cognitive conflict and impasse.

## 2. History and theories in depth

**Polya's method (1945, 1954).** Four phases, none rigid. Understand: what is unknown, what is given, what is the condition. Plan: find a related solved problem, a special case, an auxiliary element. Carry out. Look back: check the result, derive it another way, see what else it solves. The 1954 volumes treat induction, analogy and patterns of plausible inference as the way mathematicians guess before proving. The book sold over 1 million copies and appeared in more than 15 languages. It reports no controlled tests with effect sizes. [a03, a21]

**Schoenfeld's correction (1985).** Teaching Polya heuristics alone did not carry undergraduates through non-routine problems. Students were confused about which of dozens of heuristics to pick. Domain knowledge and monitoring (control) were also needed. Only a secondary source was read, so no effect sizes are available. [a04, a23] The lesson for a machine: a bag of heuristics needs a selector and a monitor. This matches the schema's S6, which picks one unused operator under a code rule.

**Lakatos's logic of discovery.** The proof is a thought experiment split into lemmas. Counterexamples come in three types: [a01]
- global but not local (the claim fails, but no lemma of the proof fails): there is a hidden lemma, improve the proof;
- local but not global (a lemma fails, the claim holds): replace the lemma, keep the claim;
- both (a lemma fails and the claim fails): add the lemma as a condition of the claim.

The hollow cube (V-E+F=4) and the picture frame (16-32+16=0) are the stock cases. [a01, d05] Martin and Pease (2013) list six reactions: surrender, monster-barring, exception-barring, monster-adjusting, lemma-incorporation, and proofs-and-refutations. Most are triggered by a counterexample. Monster-barring and monster-adjusting act on vague definitions. Exception-barring adds a condition. Lakatos does not say how hidden assumptions arise. [d04, d05] The history in the book is admitted to be idealised, so it is a model of method, not a measured record. [a02] Definitions are also variables the loop may change (proof-generated definitions such as "normal polyhedron"). [a02]

**Human base rates.** In sampled MathOverflow responses (Martin and Pease 2013): explicit examples or counterexamples in 34%, errors found and corrected in 37%, citations in 56%. Descriptive coding only, no outcome measure. [d04] Polymath1 (2009, over 40 participants, "probably solved" after about seven weeks, 2012 Annals paper) shows open refinement works when small contributions are checkable. Polymath5 (Erdos discrepancy) was not solved by the project itself. Tao solved it in 2015. [a20]

**Computational ancestors.** Lenat's Automated Mathematician (1977), Fajtlowicz's Graffiti (1984-86), Colton's HR, Pease's HRL (a Lakatos model). Only Graffiti was read (Wikipedia). It stores graphs, computes invariants, and keeps any inequality true on all stored graphs. The Dalmatian rule (1990s) keeps a conjecture only if it is sharper than all existing ones on at least one graph. About 80 publications were written on its conjectures. Some were proved (Favaron-Maheo-Sacle 1991: residue <= independence number). [a09] TxGraffiti (Davila 2026) fits affine bounds by linear programs, keeps table-true conditionals, and ranks by "touch" and "sharp" counts. It removes redundant and transitive claims. No accuracy comparison was given. [b22] Benchmark numbers for Lenat AM and HRL were not found. [critique gap 9]

**The 2021-2026 human-AI loop.**
- Davies et al. 2021 (Nature 600): a mathematician hypothesises a relation, a model tests if it is learnable above chance, attribution shows which inputs matter, the human conjectures, repeat. Knot theory: signature predicted from geometric invariants at 78% on held-out data (baseline 25%). A linear model on "natural slope" alone also reaches 78%. The first conjecture (signature tied to slope) was refuted by braid-built counterexamples from an unsampled region. The repaired theorem adds the injectivity radius. This is a Lakatos lemma-incorporation move done by hand. [a05, a06, a25, b24]
- Ramanujan Machine (Raayoni et al., Nature 2021): numeric search (MITM-RF, Descent and Repel) conjectures continued fractions for pi, e, Catalan, zeta values. Chance of a random match for a 10^9 space with over 50 matching digits is below 10^-40. Checked to 2000 digits. Readers proved all formulas of the first manuscript within months. Some stay unproven. A digit match is not proof. [a07, a08, b21]
- Wagner 2021 (via a 2026 survey): reinforcement learning with the cross-entropy method built counterexamples to graph-theory conjectures. Reward is the degree of violation. The paper itself was not opened. [b25]
- AlphaEvolve at scale (Georgiev, Gomez-Serrano, Tao, Wagner 2025): 67 problems. It matched best known results in most, improved several, and failed on others. It needs a smooth computable score. The finite-field Kakeya chain used AlphaEvolve (construction), Deep Think (proof) and AlphaProof (Lean). [a13, a14, b17]
- 2026 multi-agent systems: QED, First Proof Sprint, a skeptic-agent system for homology. See section 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Most model conjectures die or repeat (group theory, solubilizer) | 757 outputs, 420 unique (55.48%); 109 with counterexample (25.95%); 40 survivors (9.52%); 271 of 420 code not runnable (64.52%) | Chuharski 2024 [b01, b03], re-checked in critique | [E] |
| Survival differs by model, and survival is not quality | Survivors: ChatGPT 25/94 (26.60%), Claude 4/89 (4.49%), Gemini 11/237 (4.64%). Non-executable: Gemini 81.86%, Claude 49.44%, ChatGPT 35.1% (text prints 37.76%; its table says 33/94) | [b02, b03, critique] | [S] |
| Lean conjecture funnel | 12,289 generated; 10,950 valid; 4,130 novel; 3,776 not aesop-provable (30.7% of generated, 34.5% of valid); 103.25 novel per seed file; 25 of 40 files hit the 15-round cap | LeanConjecturer 2025 [a10, b05] | [E] with Chuharski |
| "Non-trivial" here only means aesop failed | truth unknown; false statements included | [b05, a10] | [E] |
| Prompt wording changes yield | One Mathlib file: without "as many as possible" 1 conjecture, 0 valid; with it 412 total, 392 valid, 108 non-trivial. One file, one run | [a11] | [C] vs b04 |
| Wording did not fix duplicates (group theory) | alternate prompt gave no significantly more diverse conjectures | Chuharski [b04] | [C] |
| Context shown to the generator changes diversity | only proven theorems in context: repeats; all prior conjectures in context: more diverse. Qualitative | [b07] | [S] |
| Training on own conjectures: more proofs, little coverage | GRPO on 192 topology items, 24,576 attempts: proofs 2,285 to 3,657 (10 epochs) to 5,307; problems solved 47 to 49 to 50 of 192; 14 held-out items no clear gain | [a12, b06] | [S] |
| Learnability probe finds real structure | Knot signature: 78% test accuracy vs 25% chance; slope-only linear model also 78% | Davies 2021 [a05, a25] | [E] |
| Counterexample from unsampled region repaired a conjecture | slope bound refuted by braid-built knots; injectivity radius added | [a06, b24] | [E] (single case, human in loop) |
| Counterexample construction is harder than judging | CounterMATH 1,216 pairs; open 7B 28-38 F1; Qwen2.5-Math-72B 41.8; best commercial row 80.7 F1 (strict 54.2); a different commercial row F1 77.0 with 65.1 strict / 75.7 loose; 1,025-sample SFT helps a little | Li 2025 [b08-b10, critique] | [S] |
| Formal counterexamples are trainable | Validation pass@1 49.8% vs best baseline 25.4% (pass@4 52.7 vs 36.0; pass@9 54.1 vs 39.9); about 575K candidates from 212,463 sources; test built by same pipeline; rejected from ICLR 2026 | Learning to Disprove 2026 [d01, d02] | [S] |
| Counterexample-then-repair loop gives gains | 50 claims, 25 families, 7 models; Qwen2.5-7B 78% to 94%; all 25 canonical repairs pass. Baseline is round-1 judgment, not untyped retry | CRAFT 2026 (abstract page) [d03] | [S] |
| Proof writing is far below answer giving | USAMO 2025, 6 problems x 4 runs: Gemini-2.5-Pro 10.1/42 (24.05%; paper prints 24.4%); R1 2.0, Grok 3 2.0, Flash-Thinking 1.8, Claude 3.7 1.5, QwQ 1.2, o1-pro 1.2, o3-mini 0.9 | Petrov 2025 [b11, c05] | [E] |
| LLM graders inflate proof scores | up to 20x; LLM-judge rows about 15-20/42 for top models vs human 1-10 (a "9-24" range was not reproduced) | [b13, critique] | [E] |
| Seen vs novel gap | Grok 4 heavy 76.2% on USAMO 2025 vs 11.1% on novel problems; AnswerBench 80.0% (Deep Think), 73.1% (Grok 4), 65.6% (GPT-5); advanced ProofBench Deep Think 65.7%, next models 23.3% and 7.1% | IMO-Bench [b15] | [E] |
| A rubric+reference autograder tracks experts | Pearson 0.96 (basic), 0.93 (advanced); GradingBench best MAE 18.4% | [b16] | [S] |
| Models prove false statements | GPT-5 sycophantic 29.0% (best model) on BrokenMath | Zheng 2025 [c11, critique] | [E] |
| Skipping the conjecture step inflates formal results | ConJudge GPT-4.1 78.77 seen vs 26.70 unseen (pass@1); DeepSeek-V3.1 92.78 vs 55.80; mean seen-to-unseen drop 23.7% | ConjectureBench [d15] | [S] |
| Failure modes of proofs | first-error classes: flawed logic and unproven assumptions, then no change of strategy across attempts, then algebra; models claim to have solved problems; over-generalise small-case patterns | [b12, b14] | [E] |
| Search programs beat direct constructions | search mode more efficient than asking for the construction; cheap LLM 50 runs vs expensive 20 runs, cheap needed about 2x calls; mixed cheap and strong sometimes beat strong-only. No controlled numbers | [a14, a15, b19] | [E] as practice, anecdotal |
| Scorers get gamed | leaky verifier (positivity on a discrete grid); irregular function exploited numerical integration; fixed by restricting to bounded step functions. No rates | [a14, d07, d08] | [E] qualitative |
| Skeptic agent helps in a toy domain | Proven formulas using chi or b1: full 12.72% [9.83, 16.83]; no provability 7.02%; no skeptic 5.90%; conjecturer only 0% (723 unique formulas, none with chi or b1). 15 eval episodes | Aggarwal 2026 [c01, d10] | [S] |
| Verifier agent had no false accepts | QED: 214 candidates, 17 accepted, all 17 expert-confirmed (0/17; 95% upper bound about 18%); 5 of 18 projects gave original proofs; 3 comparable to specialist venues; cost about 100-600 USD per case | An 2026 [d12, d13] | [S] |
| Multi-agent sprint on research problems | 10 problems: 4 closed and validated, 2 closed with partial QC, 2 partial, 1 computational only, 1 conditional | Corneli 2026 [d17] | [S] |
| Plan-then-execute prompt (Polya analogue) | text-davinci-003, zero-shot: PS+ 76.7 vs CoT 70.4 average over six math sets; GSM8K 56.4 to 59.3; SVAMP 69.9 to 75.7; AQuA 38.9 to 46.0; wrong GSM8K answers: misunderstanding 27%, missing step 12%, calculation 7% | Wang 2023 [a16] | [E] (small, old model) |
| Least-to-most decomposition | SCAN, code-davinci-002: at least 99% with 14 exemplars vs 16% CoT; math gains smaller | Zhou 2023 [a18] | [E] (synthetic task) |
| Self-generated analogues | about +4% average; Codeforces: GPT-3.5 with method 15% vs GPT-4 3-shot CoT 16% | Yasunaga 2024 [a19] | [E] (covered elsewhere) |
| Polya heuristics as system prompts | Auxiliary elements in geometry: GPT -25%, Haiku +14%; Gemini 2.5 Flash Lite up to +6 points; segmentation most reliable, pattern recognition worst. Blog, no n | Anand 2026 [c13] | [C] |
| Look-back is rarely trained | Llama-3.1-8B tuned on about 32,000 Polya dialogues: look-back share 23.4% vs 16.5% for instruct; no accuracy measured | Llama-Polya [c14] | [S] |
| Human conjecture practice | errors corrected 37%, counterexamples or examples 34% of sampled MathOverflow responses | Martin and Pease 2013 [d04] | [S] human-only |
| Draft-sketch-prove | prover success 20.9% to 39.3% with sketches (abstract only) | Jiang 2022 [c12] | [S] |

## 4. Mechanisms and models

**M1. The generate-filter funnel.** Implementation:
1. The generator writes N candidate claims in isolated calls.
2. Code removes duplicates (hash after a canonical rewrite).
3. Code removes known or trivial claims (exact match against a stored set, a cheap automatic prover, or brute force on small cases).
4. Code runs a falsifier on each survivor.
5. Keep survivors.
6. Run a second, held-out check before accept.

Expected rates from the data: about 45% duplicates, about 26% killed by counterexamples, under 10% survive on a narrow domain (Chuharski). About 31-35% survive the triviality filter in Lean. Plan the token budget so the filter, not the generator, takes most of it. [K01]

**M2. Survival plus sharpening (Dalmatian rule).** Keep a conjecture only if it is true on all stored cases and strictly stronger than the kept set on at least one case. Implementation: store the kept claims as predicates or bounds. For a new claim, find a stored case where it is tighter than every kept bound. Survival alone rewards easy claims (GPT-4's 26.6% was mostly solubilizer size statements). [a09, b02, K02]

**M3. Learnability probe, attribution, targeted counterexample (Davies).**
1. Fit a small model or a linear fit on cases to predict the target.
2. If it beats chance on held-out cases, the pattern exists.
3. Rank features by attribution and write a conjecture from the top features.
4. Sample cases from regions that were rare in training (extremes, special constructions) and test the conjecture there.
5. If refuted, add the missing variable and refit.

A failed probe is weak evidence (a model that cannot beat chance does not show there is no pattern). A trivial baseline (slope only) matched the net, so always run the simple baseline first. [a05, a06, a25, K04]

**M4. Typed counterexample reaction (Lakatos as a rule table).** Given a proof with steps L1..Lk, a claim C, and a counterexample x found by code, run each lemma on x.
- All lemmas hold on x and C fails: the proof has a gap (global not local). Find the hidden step, add a lemma, re-prove.
- A lemma fails on x and C holds on x: local not global. Replace or repair the lemma, keep C.
- A lemma fails and C fails: add the lemma's condition to C (lemma incorporation, exception-barring).
- Definition check (monster-barring): ask if x is in the intended class. Allow this only if the class definition is written down and logged. This is the main cheat route, so G3 requires the independent check to run on the original definition too.

The rule is implementable because the lemma tests are code. No study has measured it against untyped retry. [a01, d05, K05, K21]

**M5. Search program, not answer.** Ask the model for a program that searches for the object. Code scores it. Evolve with the best programs kept. Chain: small cases, pattern, general formula, proof, formal check. Guard: a hold-out check at larger n, and a scorer that cannot be exploited (restrict the search space, check at random points not only grid points). [a13, a15, d08, K12, K19]

**M6. Skeptic phase.** A second pass in a separate context tries to make the claim fail. In the toy system it re-weighted data points so statements were hard to prove. Single-agent version: after S3, a fresh call receives only the claim and writes the cases most likely to break it. Code runs them. [c01, K14]

**M7. Prover and verifier separation.** The verifier sees the proof text and the problem, not the prover's reasoning or confidence. Code collects only accept or reject plus located gaps. QED reports 0/17 false accepts but has no control. The schema's G5 and G10 already forbid trusting the generator's own account. [d12, d13, K20]

**M8. Look-back as a code-triggered step (Polya phase 4).** After a pass: re-derive by another route, test a generalisation (O2), test a special case that should flip the answer (O1), and write one lesson line (S9). Not measured for accuracy. [a03, c14, K18]

**M9. Selector over heuristics (Schoenfeld control).** Do not list all 12 heuristics. Code picks one unused operator at an impasse using the failure type. Example rule: wrong value, specialise; claim too strong, drop a constraint; too many parts, decompose; stuck on form, change representation. Evidence for this selection rule is absent. Evidence that the unselected list is weak is secondary. [a04, a23, a24, c13, K07]

## 5. What holds up

**Holds up (two or more independent sources, or confirmed by re-opening).**
- Funnels are steep. Chuharski and LeanConjecturer, different languages and models, both show that most output is duplicate, trivial, false or not runnable. [K01]
- Generator plus checker is the shared structure of every discovery system (Lean, numeric score, counterexample code, verifier agents). Where the checker can be exploited, it is exploited (AlphaEvolve cases). [K03]
- Over-trust. LLM graders inflate proof scores up to 20x. The best model proves a false statement 29.0% of the time. Models claim solutions they did not reach. [K08]
- The seen-novel gap is large on proofs (76.2% vs 11.1%) and on conjecturing (78.77 vs 26.70). [b15, d15]
- Decomposition helps, especially on weak models and synthetic compositional tasks. [K06]

**Failed, mixed, or limited.**
- Polya-style heuristics as prompts: mixed (GPT -25% on auxiliary elements in geometry, Haiku +14%). Plan-and-Solve gains are small (GSM8K +2.9 points), and the paper does not cite Polya. Gains shrink with model strength. [K07]
- Prompt wording as a yield lever: large in LeanConjecturer's single-file ablation (1 vs 412), nil in Chuharski. Different domains and metrics. Marked contested. [K13]
- Self-generated conjectures as training data: proofs counted rise (2,285 to 5,307) but problems solved move 47 to 50 of 192, and 14 held-out items show no gain. [K11]
- Learnability probe: a linear slope model matched the network at 78%. The ML contribution to the knot result was to direct attention, not to beat a simple model. [a05]
- Repeated attempts keep the same strategy. [b12, K17]

**Moderators found.**
- Smooth, computable score: AlphaEvolve works. Otherwise it struggles. [a13]
- Model strength: cheap models need about 2x calls. Mixed cheap-plus-strong runs sometimes beat strong-only. [a14]
- Domain: GAP code failed to run in 64.52% of cases. Python would likely do better. [b03]
- Denominator: 31% vs 34.5% depends on whether all generated or only valid statements are used. State it.

**Interventions that worked.** Counterexample feedback and repair (CRAFT, 78% to 94%, small, abstract only). A verifier in a separate agent (QED, small). A code-run falsifier (Chuharski, Davies). Training for formal counterexamples (49.8% vs 25.4% pass@1). Rubric-plus-reference grading (Pearson 0.93-0.96 against experts).

**Not tested.** Typed vs untyped counterexample reaction. Forced look-back and accuracy. Program-chosen heuristics. Skeptic-gain replication outside homology. Hold-out checks against gaming. [critique gaps 1, 3, 4, 7, 10]

## 6. Language models

**Generating conjectures.** Raw LLM conjecturing is a high-volume, low-yield process (section 3). Models differ greatly: ChatGPT/GPT-4 survived 26.60%, Claude 4.49%, Gemini 4.64% (2024 models). Unique outputs per model were about 94, 89 and 237 of about 250 each, so duplicates came mostly from ChatGPT and Claude. [b02, critique]

**Writing proofs.** Early 2025: the best model scored 10.1/42 on USAMO 2025, most under 2. By late 2025 IMO-Bench reports Deep Think at 65.7% on the advanced proof set, others at 23.3% and 7.1%. The benchmark authors are from the same family, and older items may be contaminated. The 2025 numbers are already superseded. [b11, b15] No 2026 frontier model was measured with and without a scaffold at equal tokens. [K22]

**Grading proofs.** LLM judges inflate scores up to 20x unless given a rubric, a reference solution and guidelines. With those, Pearson is 0.93-0.96 against experts. [b13, b16]

**Counterexamples.** Judging a statement false is easier than constructing the counterexample (CounterMATH). Fine-tuning on 1,025 samples helps a little. Formal-counterexample training (575K problems) gave 49.8% pass@1 vs 25.4%. Test sets came from the same pipeline, so the gain is likely inflated. [b08-b10, d01, d02]

**Sycophancy to false statements.** GPT-5 proves a false statement 29.0% of the time on BrokenMath. Test-time fixes and fine-tuning reduce but do not remove it. [c11]

**What changed behaviour, by how much.**

| Change | Size | Status |
|---|---|---|
| Plan-and-Solve prompt (old model) | +6.3 average points (70.4 to 76.7) | [E] |
| Least-to-most (SCAN) | 16% to at least 99% | [E], synthetic |
| Self-generated analogues | about +4% | [E] |
| Counterexample feedback (CRAFT) | 78% to 94% on 7B, 50 claims | [S] |
| Verifier in separate agents (QED) | 0/17 false accepts, no control | [S] |
| Skeptic agent (toy RL) | 5.90% to 12.72% | [S] |
| Seeing the answer vs not (autoformalisation) | 23.7% mean drop when hidden | [S] |
| Polya heuristic system prompts | -25% to +14% by model and type | [C] |

**Research-scale systems (2026, self-reported).** QED: 18 projects, 5 original proofs confirmed, 3 comparable to specialist-venue work, USD 100-600 per case. It names seven failure modes of single-query proving, each tied to a fix: shared context, citation hallucination, effort misallocation, unstable plans, unfocused verification, problem modification, single-model bottleneck. Ablations were on two cases only and qualitative. First Proof Sprint: 4 of 10 closed and validated, with verification gaps remaining. Neither has a no-scaffold arm, so the scaffold's own contribution is unknown. [d12-d14, d17]

**Cheating.** Search loops exploit scorer holes: a leaky verifier, irregular functions beating a numerical integral. Proof models over-generalise small-case patterns and leak RL artefacts such as \boxed{}. [a14, b14, d08]

## 7. What our agent should take

### Add now (established)

1. **Falsify before keeping, and funnel hard.** Generate several isolated candidates, remove duplicates and trivial ones in code, run a code falsifier, keep survivors. Schema: S3/S4, G3, G5, G8. [E] K01. Evidence: a10, b01, b05, c09, d02. SCHEMA already has S4 test and S7 counterexample search. What is new is the explicit dedupe-and-triviality stage with expected pass rates (survivors 10-35%).
2. **Judge by running, never by self-grade.** Final acceptance of any claim or proof comes from code, or from a rubric-plus-reference grader that sees no authorship. Never accept a model's own statement that it solved the item. Schema: G2, G3, G8, G10. [E] K08. Evidence: b12, b13, b16, c05, c11, c24.
3. **A checker plus a hold-out.** Every code checker inside a refine loop can be gamed. Restrict the search space and add a second check on unseen cases. Schema: G3. [E] K03 (the hold-out effect itself is [S] K19). Evidence: a14, d07, d08.
4. **Search-program mode for scorable constructions.** Write a program that searches, scored by code, rather than a one-shot object. Check at larger n after a small-case pattern. Schema: O1/O2 (specialise then generalise) with G3. [E] as practice, K12. Evidence: a13, a15, b14, b19, b20.
5. **Decomposition is the best-supported Polya operator.** Keep O3 as the first operator at an impasse on multi-step items. Do not expect big gains on strong models. Schema: O3. [E] K06. Evidence: a16, a17, a18.
6. **Do not turn the 12 Polya heuristics into a prompt list.** Keep one operator per impasse, chosen by code (already in S6). Schema: G1, S6. [C] K07, but the action matches SCHEMA 4b. Evidence: c13, a04, a23.
7. **Test on novel items and report the seen-novel gap.** Seen-problem scores overstate proof ability (76.2% vs 11.1%). Hide the target conjecture or answer when scoring conjecture ability (78.77 vs 26.70). Schema: G7 bench rule. [E] K09, [S] K15. Evidence: b15, d15.
8. **Locate the failing sub-step by code, not by a model's opinion.** This is G2 restated. The Lakatos typing is only a labelling of it. Schema: S5. [E] for G2. The typing itself is under Test first. Evidence: a01, d05.

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Typed Lakatos reaction (claim / step / both) vs untyped retry | S5/S6, O4 | [S], untested, K05, K21 | a01, d03, d05, d18 |
| Survival plus sharpening (Dalmatian) score for kept claims | G8, S7 | [S] K02 | a09, b02, b22 |
| Learnability probe plus counterexample from an unsampled region | S4/S5 | [E] in human loop, LLM untested, K04 | a05, a06, a25 |
| Separate verifier context without the prover's trace | G5, S8 | [S] K20 | d12, d13 |
| Explicit skeptic phase in one agent | G2/G3, S4 | [S] K14 | c01, d10, d11 |
| Code-triggered look-back (re-derive, generalise, lesson line) | S9 | [S] K18 | a03, c14 |
| Forced operator change after a failed attempt | S6, G1 | [S] K17 | b12, a23 |
| Program-chosen Polya heuristic vs list in prompt | S6 | [C] K07 | c13, a04, a23 |
| Own-conjecture lemma memory for later same-topic items | memory | [S] K11 (inverse of the training result) | a12, b06 |
| Context policy for generators (show all prior conjectures) | S3 | [C] K13 | a11, b04, b07 |
| Hold-out check against gaming | G3 | [S] K19 | d07, d08 |

## 8. Concrete tests on our bench

All tests: both arms use the same total tokens, setup included (G7). Report per model and per problem type. Use novel items only.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Seeded items: a rule or claim with a hidden-variable flaw, with a code counterexample finder (ARC-style rules, small group or graph claims) | A: counterexample found, free retry. B: model labels the reaction (claim, step, definition) then acts; code checks the label against which lemma tests fail | Share of final claims that survive an independent hold-out check | B at least +8 points. No gain if the model labels at random. If label accuracy is under 70%, typing does not help |
| T2 | Claim generation on one domain with checkable truth (small graphs, finite groups) | A: accept first N claims. B: dedupe, triviality filter, code falsifier | Share of kept claims that pass an independent check; unique-and-novel kept per 1k tokens | B well above A (A near 10-35% survive). Cost is filter overhead |
| T3 | Same claims | Survival only vs survival plus Dalmatian sharpening | Blind usefulness rating; count of non-redundant claims kept | Sharpening cuts redundancy and may lose some true claims. Measure both |
| T4 | Proofs with seeded known flaws | Self-grade vs rubric-plus-reference grader vs code check | Inflation (graded score / true score); false-accept rate | Self-grade inflates. Rubric grader near expert |
| T5 | Same proofs | Verifier sees prover's reasoning vs sees proof only | False accepts against expert labels | Proof-only gives fewer false accepts |
| T6 | Multi-step math (hard GSM8K, MATH subset) | Plain vs plan-only vs decompose-first (O3) | Accuracy per model | Small gain on weak models, none on strong |
| T7 | Items where the first attempt fails | Free retry vs forced different operator chosen by code vs fixed heuristic list | Success; count of distinct strategies tried | Forced change raises distinct strategies. Success gain uncertain |
| T8 | Scorable construction (bounds, packings) | Direct answer vs search-program arm, plus held-out larger n | Score at fixed tokens; count of gamed passes | Search program better. Hold-out catches gaming |
| T9 | Tasks with a gradable answer and a hidden target | Target given vs hidden | Accuracy gap | Large drop when hidden (compare 23.7% mean) |
| T10 | Two-session set of same-topic items | No memory vs stored own code-verified lemmas | Accuracy on session-2 items | Any gain is new. The training result found none |
| T11 | Look-back | With vs without a code-triggered re-derive and generalise step | Final accuracy; errors caught after first pass | Small gain, costs tokens. Keep only if it pays at equal tokens |

## 9. What does not transfer, and why

- **Euler's polyhedra history.** Lakatos's account is an idealised rational reconstruction, not data. It gives a pattern of moves, not rates. [a02]
- **Monster-barring as a strategy.** In human practice it clarifies definitions. For an agent it is an easy cheat: redefine the class to exclude the counterexample. G3 and G8 forbid accepting it unless the definition change is logged and the check runs on the original definition.
- **Polymath-style crowds.** Open collaboration worked where small contributions were checkable and many humans were available. It cannot be tested in one agent. It belongs to the multiplayer idea. [a20, K16]
- **Human intuition in the loop.** Davies's result needed a mathematician reading attributions. The model did not write the conjecture. [a05]
- **Heavy research systems.** QED costs USD 100-600 per case with frontier coding agents. That is too much for routine bench items. They also have no equal-token control. [d12]
- **Training results.** GRPO on own conjectures is training. Our agent does not train. [a12]
- **Lean-only counts.** Lean funnels use a formal prover as checker. Our items mostly use code checks or none. Use the yields for orientation, not as targets.
- **Old-model prompt effects.** Plan-and-Solve and Least-to-Most gains come from text-davinci-003 and code-davinci-002. Effects shrink with newer models.
- **USAMO 2025 numbers.** Already superseded. Use them only for the grader-inflation and failure-mode points.

## 10. Open questions

1. Does typed counterexample reaction beat untyped retry at equal tokens? No study. [K21]
2. What fraction of surviving model conjectures is both true and non-trivial under an independent check? The funnel counts "not killed", not "true". [critique gap 2]
3. Does a forced look-back raise final accuracy? Only dialogue-share data exist. [gap 3]
4. Do program-selected Polya heuristics help when listed prompts do not? [gap 4]
5. How do 2026 frontier models do on novel proofs with and without a scaffold, at equal tokens? [gap 5, K22]
6. What are Schoenfeld's primary effect sizes? [gap 6]
7. How often is a code-checked loop gamed, and does a hold-out check cut it? [gap 7]
8. Do stored own-conjecture lemmas help on later same-topic items? [gap 8]
9. What measured results exist for HRL, Lenat's AM, and Graffiti critiques? [gap 9]
10. Does the skeptic gain replicate beyond homology and beyond a small symbolic RL system? [gap 10]
11. Georgiev et al.: how many of the 67 problems were matched, improved, failed? Not extracted. [d09]
12. Is the Chuharski vs LeanConjecturer prompt-sensitivity contradiction a domain effect or a metric effect?

## 11. Sources

[V] = opened this session in text. [M] = snippet, abstract only, or memory.

- [V] Stanford Encyclopedia, Lakatos entry (read to 100,000 of 130,627 chars). https://plato.stanford.edu/entries/lakatos/ (a01)
- [M] Lakatos (1976) Proofs and Refutations, via SEP only. https://plato.stanford.edu/entries/lakatos/ (a02, c19)
- [M] Polya (1954) Mathematics and Plausible Reasoning, via SEP. (a21)
- [V] How to Solve It (Wikipedia). https://en.wikipedia.org/wiki/How_to_Solve_It (a03, a24)
- [V] Alan H. Schoenfeld (Wikipedia). https://en.wikipedia.org/wiki/Alan_H._Schoenfeld (a04, a23)
- [V] Davies et al. (2021) Nature 600. https://www.nature.com/articles/s41586-021-04086-x (a05, a06, a25)
- [V] Raayoni et al., The Ramanujan Machine. https://arxiv.org/abs/1907.00205 (a07, a08, b21, c18)
- [V] Graffiti (Wikipedia). https://en.wikipedia.org/wiki/Graffiti_(program) (a09)
- [V] Onda et al. (2025) LeanConjecturer. https://arxiv.org/abs/2506.22005 (a10-a12, b05-b07, c09)
- [V] Georgiev, Gomez-Serrano, Tao, Wagner (2025) Mathematical exploration and discovery at scale. https://arxiv.org/abs/2511.02864 (a13-a15, b17-b20, c07, d07-d09)
- [V] Wang et al. (2023) Plan-and-Solve. https://arxiv.org/abs/2305.04091 (a16, a17)
- [V] Zhou et al. (2023) Least-to-Most. https://arxiv.org/abs/2205.10625 (a18)
- [V] Yasunaga et al. (2024) Analogical reasoners. https://arxiv.org/abs/2310.01714 (a19)
- [V] Polymath Project (Wikipedia). https://en.wikipedia.org/wiki/Polymath_Project (a20)
- [V] Chuharski et al. (2024) Mining Math Conjectures from LLMs. https://arxiv.org/abs/2412.16177 (b01-b04)
- [V] Li et al. (2025) CounterMATH. https://arxiv.org/abs/2502.10454 (b08-b10)
- [V] Petrov et al. (2025) Proof or Bluff. https://arxiv.org/abs/2503.21934 and https://arxiv.org/html/2503.21934v5 (b11-b14, c05)
- [V] Luong et al. (2025) IMO-Bench. https://arxiv.org/abs/2511.01846 (b15, b16)
- [V] Davila (2026) TxGraffiti. https://arxiv.org/abs/2409.19379 (b22)
- [V] Extremal descendant integrals on moduli spaces of curves. https://arxiv.org/abs/2512.14575 (b23)
- [V] Chen and Jiang (2026) Lectures on AI for Mathematics (contents and passages only). https://arxiv.org/abs/2604.11504 (b24-b26, c04, d06)
- [V] Aggarwal, Kim, Ek, Mishra (2026) multi-agent concept discovery. https://arxiv.org/abs/2603.04528 and https://arxiv.org/html/2603.04528v2 (c01, d10, d11)
- [V] Corneli (2026) A First Proof Sprint. https://arxiv.org/abs/2602.13587 (c02, d17)
- [V] An, Ye, Pan, Zhang (2026) QED. https://arxiv.org/abs/2604.24021 (c03, d12-d14)
- [M] Feldman and Karbasi (2025) Godel Test, abstract. https://arxiv.org/abs/2509.18383 (c06)
- [V] Sivakumar et al. (2025) Conjecturing: an overlooked step. https://arxiv.org/abs/2510.11986 (c08, d15, d16)
- [M] Romera-Paredes et al. (2023) FunSearch, from memory. https://www.nature.com/articles/s41586-023-06924-6 (c10)
- [M] Zheng et al. (2025) BrokenMath, abstract and table. https://arxiv.org/abs/2510.04721 (c11)
- [M] Jiang et al. (2022) Draft, Sketch, and Prove, abstract. https://arxiv.org/abs/2210.12283 (c12)
- [M] Anand (2026) Testing Polya heuristics, blog. https://www.s-anand.net/blog/testing-polya-heuristics-on-ai-math/ (c13)
- [M] Llama-Polya (2026). https://arxiv.org/html/2602.10597v1 (c14)
- [M] Glazer et al. (2024) FrontierMath, abstract. https://arxiv.org/abs/2411.04872 (c15)
- [M] Zhang et al. (2025) DeepTheorem, abstract. https://arxiv.org/abs/2505.23754 (c16)
- [M] Lenat (1977) Automated Mathematician; Pease and Colton HRL, from memory (c21, c22)
- [V] Learning to Disprove (2026). https://arxiv.org/abs/2603.19514 (d01, d02)
- [M] CRAFT (ICML 2026, abstract page). https://icml.cc/virtual/2026/74819 (d03)
- [V] Martin and Pease (2013) Mathematical practice, crowdsourcing, and social machines. https://arxiv.org/abs/1305.0900 (d04, d05)
- [M] Gap-search note (d18); related link https://arxiv.org/abs/2502.19414 (not re-opened).
