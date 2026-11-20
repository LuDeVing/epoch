# Argumentation and defeasible rules: deep document

*Subfield E11.06. Evidence ids (a01 to d18) point to the evidence_a-d.jsonl files in this folder. Claim ids (E11.06-K01 to K23) point to claims.jsonl. Numbers were re-checked in critique.md; where an earlier line was wrong, the corrected value is used here (GPT-4 0613 zero-shot is 93.52, not 96).*

## 1. What it is

Defeasible reasoning is reasoning where a conclusion can be withdrawn when new information arrives. "Birds fly" is true as a default. It stops being true for penguins. Law is full of this: a rule, an exception to the rule, an exception to the exception, and a rule about which one wins.

Argumentation theory models this as a fight between arguments. An argument has premises, an inference step and a conclusion. Other arguments can attack it. A set of arguments is then accepted if it can defend itself against every attack.

Three parts matter for our agent.

1. **Attack types.** Rebut: contradict the conclusion. Undercut: say the rule does not apply here (an exception), without claiming the opposite. Undermine: attack a premise. (a03, a06)
2. **Defence and acceptance.** An argument that is attacked but defended by an argument that beats the attacker is "reinstated". Different formal semantics (grounded, preferred, stable, CF2) give different answers on cycles and floating conclusions. (a04)
3. **Burden of proof.** Who must show what, and how much is enough. This is separate from how strong the arguments are. The same evidence can give a different verdict under a different burden or standard. (a09 to a12)

Why it matters for a thinking scaffold: most real tasks mix defaults and exceptions. A model that treats "usually" as "always", or that sees a late exception and keeps its old answer, fails in a way that looks fluent. This subfield tells us what the failure looks like, how large it is, and which fixes are tested.

Links to other subfields in this run (not covered here): Analogy and precedent in legal theory (the case-based branch, HYPO and CATO, only noted in a13); Pragma-dialectics; Argument mapping training; Evidence and probability reasoning; Judicial bias and noise; Imprecise credences; Modal and epistemic logic; Debiasing; Verbal confidence; Autoformalisation; Automated discovery (DeFAb and ABD overlap).

## 2. History and theories in depth

**Toulmin (1958), The Uses of Argument.** Toulmin rejected the view that a good argument must be deductively valid. Outside mathematics, an argument is good if it survives criticism in a proper dispute. His layout has six parts: claim, data (grounds), warrant (licenses the step from data to claim), backing (supports the warrant), qualifier (certainly, probably, typically) and rebuttal (conditions where the warrant does not hold). The warrant is itself defeasible. This is a picture, not a logic. Influence on AI stayed modest until others formalised it. (a01, a02, a29; the book was not opened, only secondary sources.)

**Reiter, McCarthy, Gelfond and Lifschitz (1980 to 1988).** Classical non-monotonic logics: default logic, circumscription, stable models. Exceptions are a feature. Dung later showed these share structure with argumentation. (a25, read only through secondary sources.)

**Pollock (1987, 1995).** Introduced the defeasible (prima facie) reason and two defeaters. A rebutting defeater supports the opposite conclusion. An undercutting defeater attacks the inference itself. Example: an object looks red (reason to think red), but it is lit by red light (undercutter: it does not say the object is not red, only that the look is no evidence). Pollock's 1995 semantics turned out to be an instance of Dung's grounded semantics. (a03)

**Dung (1995).** The key abstraction. An argumentation framework is just a set of arguments and an attack relation. Semantics pick sets that defend themselves. Grounded extension: unique, the most sceptical, contained in all others. Preferred: maximal admissible sets. Stable: attacks everything outside. Every stable extension is preferred, not the reverse. Dung also showed default logic, Pollock's system and logic programming all map onto this. Today the paper is cited mostly for the abstract part; how arguments are built is left open. (a04, b27)

**Prakken and Sartor (1996 to 2009).** Legal argument systems with rule priorities and burdens. Their 2009 analysis separates three burdens: production (liability to lose if no evidence is given; once met, it does not shift), persuasion (fixed by law, can be split between parties; failing it means losing the issue) and tactical (not set by law; moves back and forth as the dispute goes). Dutch and Italian law put persuasion for some exceptions on the defendant. Courts keep discretion on fairness. (a10, a11, a12)

**Carneades (Gordon, Prakken, Walton 2007).** An argument graph evaluated with a proof standard per statement. Burden can be assigned per premise and can change during a dialogue. Three standards are defined formally: scintilla of evidence (SE), best argument (BA), dialectical validity (DV). Preponderance and beyond reasonable doubt are not modelled precisely; the authors list that as future work. Critical questions are attached to argument schemes. (a09)

**Calegari and Sartor (2020).** A two-stage labelling. First label each argument accepted, rejected or undecided. Then the allocated burden of persuasion settles the undecided ones. It also handles inversion of the burden for sub-arguments. Formal only; no LLM test found. (c19)

**ASPIC+ (Prakken 2010; Modgil and Prakken 2014).** Arguments are inference trees built from strict and defeasible rules. Attacks: on a premise (undermining), on a conclusion (rebutting), on an inference (undercutting). Preferences resolve undermining and rebutting. Undercutting always succeeds as defeat. Four rationality postulates (sub-argument closure, closure under strict rules, direct consistency, indirect consistency) hold only under conditions: strict rules closed under transposition, consistent axioms, a reasonable preference ordering. Naive preference-based frameworks break them. The ordering rule matters: last-link (compare only the last rules) fits legal rules, weakest-link fits empirical generalisations. These intuitions are argued in the tutorial, not tested with people. (a06, a07, a08)

**Case-based branch.** HYPO (Rissland and Ashley 1987) and CATO (Aleven 1997) model argument as plies: cite a case, distinguish it, counter-cite. This belongs to the Analogy and precedent subfield and is only noted here. (a13)

**Toulmin back in formal dress.** Bex and Prakken (2026) give Toulmin's scheme a formal logic (TAL) with a proved correspondence to ASPIC+, and propose it as an evaluation standard and prompting basis for LLM arguments. No experiments. (c18)

**Human-side competing view.** Mercier and Sperber (2011) argue human reasoning evolved for arguing, not solo truth-finding, and works better on others' arguments than on one's own. Seen only as a snippet. It is a rival explanation to accounts where reasoning serves private truth-seeking. (b29)

**Descriptive work on humans.** Rahwan et al. (2010) ran the founding behavioural study (N=20 per Bezou et al.; known only second-hand). People follow reinstatement but do not recover full confidence. Cramer and Guillaume (2018) and Bezou Vrakatseli, Prakken and Janssen (2021) followed. See section 5.

## 3. Core findings with exact numbers

Status: E = established (two or more independent teams, or multiple consistent opened sources), S = single-source, C = contested, G = gap (no test found). All LLM numbers are time-stamped; most models are 2023 to 2025 vintage.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A valid argument survives criticism; three attack types (rebut, undercut, undermine) | Toulmin scheme 6 elements; ASPIC+ 3 attack types; 4 rationality postulates | a01 a03 a06 a07 (K01) | E |
| Burden of proof is a separate parameter from argument strength | 3 burdens; 3 formal Carneades standards (SE, BA, DV) | a09 a10 a11 a12 c19 (K02) | E (theory and law; no LLM test) |
| Humans rate a reinstated argument below one that was never attacked | Base M=5.61 (SD 0.99), reinstated M=5.21 (SD 0.96), 7-point scale, N=103 analysed (130 started), t(102)=4.636, p<.001. Original N=20 | b04 (Bezou 2021, replicating Rahwan 2010) | E |
| Showing all arguments at once does not change ratings | Exp 2 M=5.12, Welch t(196.56)=-0.683, p=.496 vs Exp 1 | b05 | S |
| Giving the theory first raises ratings but not the recovery gap | Exp 3 ANOVA df(1,211): experiment F=12.906 p<.001; stage F=53.66 p<.001; interaction F=1.227 p=.269 | b05 | S |
| Humans on floating reinstatement follow preferred/CF2, not grounded | Preferred/CF2 predicted 100% (science) and 97.5% (maths) of responses; grounded 0% and 2.5%; news context 67.5% vs 27.5%. Floating N=60, chi2(2)=55.60 | b01 b02 | S (one lab) |
| Humans on 3-cycles: CF2 best, but a third fit no semantics | CF2 56%; grounded and preferred 12%; none 32%. N=25, chi2(2)=7.28 p=.026. Simple reinstatement N=45 chi2(2)=12.93 | b03 | S |
| Which abstract semantics describes humans is unsettled | Three studies (N=20, 45/60/25, 103) disagree on what is shown; best case is "void precedence" (unattacked beats attacked) | b06 (K04) | C |
| Frontier LLMs do well on generic default patterns zero-shot, with a wide spread | Claude 3 Opus 96.51, Claude 3.5 Sonnet 96.01, GPT-4 0613 93.52, GPT-4 Turbo 92.69, Claude 3 Sonnet 91.36, GPT-4o Aug 89.03, Gemini 1.5 Pro 83.55, GPT-3.5 48.00. 28 models, 20 patterns, chance 50%, temp 0 | a18 b07 c10 (K05) | S |
| Chain-of-thought lowers default-reasoning accuracy in many models | Mean drop -11.14 points (SD 15.74) for models above 75% zero-shot. Claude 3 Sonnet -16.28, GPT-4 0613 -12.62, Gemini 1.5 Flash -18.77, Yi 34B -33.22, Claude 3.5 Sonnet -0.33. GPT-4o gains (+17.44 May, +4.98 Aug) | a19 c10 (K06) | S |
| But thinking helps on multi-turn belief updating | Qwen3-32B default BiasGap 0.670 non-thinking to 0.008 with extended thinking | d01 d02 | S (different task) |
| Few-shot helps weak models and hurts some strong ones | +28.74 Llama 2 Chat 7B, +25.08 Claude 3 Haiku, +16.27 GPT-4o May; -6.81 Claude 3 Opus, -10.29 Llama 3.1 8B | a20 b08 c11 | S |
| Prompt wording of one pattern changes results | Wording correlations 0.99, 0.99, 0.88, 0.54, 0.47, 0.43, -0.05 | a20 c11 | S |
| Few-shot format can break a strong model on a legal task | GPT-5.4 cuad_covenant_not_to_sue 83/154 (53.9%) few-shot, yes-rate 98.7%; zero-shot 143/154 (92.9%), yes-rate 45.5%; engine 150/154 | c05 b20 (K13) | E for the direction (two sources), S for the number |
| LLMs over-universalise generics and cling to shallow cues | GPT-4 predicts "no impact" on 60% of items (GPT-3.5 7%); word "not" correlates with "weakens"; best macro-F1 0.64 on 95k questions, 12 LLMs | b16 b17 c09 (K07) | E |
| Conflicting rules without priorities break GPT-4o | 8 theories x 4 settings = 32 cells; 7 cells wrong: levels- 4/4, levels(5) 2/4, dag(3,2) 1/4. Priorities and false-premise facts raise correctness | a17 b15 c12 (K15) | E (tiny sample, one model; supported by BoardgameQA direction) |
| ChatGPT ignored specificity until told | A handful of hand cases, no counts | c13 | S |
| Accuracy falls as conflict, depth and chain length rise | BoardgameQA: 1000/500/1000 split, majority baseline 33%, conflict prob 0.0/0.2/0.5/0.8, depth 1 to 3; exact scores only in figures. Prompt-tuned model predicted "unknown" 268 times at depth 1 vs 2 at depth 2 | a14 a15 a16 c14 (K08) | E |
| Linear attack-graph puzzles (1 to 25 arguments, 100 variants each, 2,500 prompts) | GPT-4o-mini 54.38, GPT-4o 72.31, Gemini-1.5-flash 64.64, Gemini-1.5-pro 60.32, Claude-3.5-haiku 58.84, Claude-3.5-sonnet 77.32 (per-model labels probable; table scrambled). o1-preview 100 on only 75 prompts | c06 c08 (K08) | S |
| Branching graphs: accuracy hides weak recall | "yes" correct in 8.85% of 2,540 prompts. Claude-3.5-sonnet accuracy 86.81, recall 38.15, MCC 48.73; GPT-4o-mini 74.57 / 18.81 / 21.08; GPT-4o 51.77 / 14.95 / 24.21 | c07 (K10) | S |
| Computing grounded extensions of abstract frameworks is hard without training | Llama3-8B 0.18, Llama3-70B 0.37, Qwen2.5-7B 0.31, Qwen2.5-72B 0.48, GPT-3.5 0.15, GPT-4o 0.54. After SFT with explanations 0.97 (Qwen) and 0.95 (Llama) | a21 a22 c23 (K09) | S |
| Intermediate steps beat answer-only training on larger graphs (26 to 35 arguments, 100 tests each) | Qwen2.5 grounded/complete: answer-only 0.68/0.56, with P-then-Q steps 0.85/0.78. Llama3: 0.58/0.42 vs 0.80/0.71. Some answer-only runs fall to about 30% | d09 d10 | S (fine-tuning only) |
| Nested "A unless B unless C" rules break frontier models, unstably | Opus 4.6 spacecraft (68 scenarios, 3-level chain): 61/68 (89.7%, CI 80.2 to 94.9) in March; 98.5% in April. 7 failing scenarios x 10 reruns = 0/70 in March. GPT-5.4 construction insurance 96.6% to 100% (74/74). Flat rules: 43/43 | b18 c01 c02 d16 (K11) | S (vendor paper) |
| One revoking exception cut Opus 4.6 accuracy | 61/68 (89.7%) to 44/68 (64.7%, CI 52.8 to 75.0) | b19 | S |
| An "evaluate each exemption" prompt made things worse | Net accuracy 64.7% vs 89.7%; false negatives 7 to 4, but 20 new false positives; baseline failures identical in reruns (same 7) | c03 b19 (K12) | S |
| Rule engine beats frontier models on multi-prong rule tasks | 9 LegalBench tasks, 949 cases; up to +41 points vs Anthropic models; personal_jurisdiction 24/25 vs Sonnet 4.6 16/27 (+40.7); discordant 44/15 vs Sonnet 4.6, 34/13 vs Opus 4.7, 340/35 vs GPT-5.4 | b20 c04 | S (vendor; engine uses vendor-authored rules) |
| Default-exception abduction: validity high, parsimony poor | ABD: 11 LLMs, 600 instances, 7 default theories, 3 regimes. Opus-4.6 validity 100/98/99/99; Gemini-3.1 99/97/96/96. 1 to 1.5 extra exceptions per world; gaps roughly double on holdout worlds (5 per instance) | a23 a24 b13 b14 (K14) | E (two benchmarks agree in direction) |
| Over-broad exceptions delete valid predictions | DeFAb: generalized circular defeater resolved all 36 L3 tasks but removed protected predictions on 34 across 29 families; a symbolic verifier rejected all 34. Constructed probe, not model behaviour | b11 b12 (K14) | S |
| DeFAb released panel is mostly a format test | 336 tasks x 2 prompt styles; 4,032 responses; 1,054 failed: 652 contract violations, 366 token cap, 36 semantic. Claude Sonnet 5.5 133 vs 336 depending on prompt style. 225,507 records, 2,099 families | b10 c24 d14 | S |
| Step-by-step legal answers often hide wrong premises | Civ Pro MCQ: mean 27% drop from accuracy to correctness; Llama-3-8B 31.4%; GPT-4o 78.4% of premises error-free; 96% of chains from false premises carry a misinterpretation error; error-taxonomy feedback at most +4% | b21 b22 c21 (K18) | E (two entries, one group's LLM evaluator) |
| Argument scaffolds around LLMs give small, mixed gains | ArgLLM StrategyClaim Llama 3 8B: direct 0.77, CoT 0.76, depth-1 estimated base 0.81, depth-2 0.78. CQoT (GPT-4o judge, 1 to 10, 40 questions): reasoning Claude 3.5 Sonnet 8.6/8.55/8.95 (standard/CoT/CQoT); Nemotron-51b 6.75/7.7/7.3 (CoT beat CQoT). Text says +4.61% reasoning, +5.4% math; own table gives +4.74, +4.48, +5.71, +5.09 | b23 c15 c16 d07 (K16) | E that gains are small; no token accounting |
| Neuro-symbolic defeasible context (LOGicalThought) | Average +4.41% over strongest baseline, +11.82% over average baseline; ContractNLI Mistral-7B 44.4 to 53.4, Llama3.1-8B 44.3 to 50.4, Llama3.3-70B 62.7 to 66.9, o3-mini 61.6 to 69.2, R1 61.3 to 70.2; SARA R1 62.45 to 72.41. Ablation vs CoT: logic context alone +2.4, graph alone +0.5, full +7.4. False negatives 41% to 28%. About 21.5% more steps. Losses: -0.8 ContractNLI defeasible, -3.2 SARA negation | c22 d05 d06 (K21) | S (not equal tokens) |
| Toulmin fields are produced reliably by strong models | All three terms: GPT-4 99.0 (ARCT) / 100.0 (MCT), GPT-3 94.6 / 95.4, Llama-2-70B 75.2 / 90.2, Falcon-40B 35.0 / 42.5 (column order inferred). Measures presence, not accuracy gain | c17 (K17) | S |
| Late exceptions are the main failure in belief updating | DERELAB: GPT-5.1 default BiasGap 0.935 (C2 accuracy 3.5%, OR 891); GPT-5-mini labels the update "weakening" in 95.4% of turns but gets the entailment right in 20.3%; Llama-3.1-70B 85.1% vs 14.9%. 9 base models, 10 configurations, 9,029 to 11,682 turns each. Question order swap: Gemma-4-31B effect-label accuracy 0.970 to 0.264 | d01 d02 d03 (K20) | S |
| Anchoring and noise differ by model | Anchoring GPT-5.1 0.433, Qwen3-32B 0.483; Gemma-4-31B and GPT-5-mini under 5%. Llama-3.1-70B semantic override 83.9% on default C3 turns. Llama-3.1-8B changes answers on 36.2% of easy off-path turns. Seed ICC 0.95 (CI 0.938 to 0.963), CV under 4% | d04 | S |
| Verdicts often ignore the governing rule | 5 LLMs, 20 domains; general models 90 to 92% accurate; guard model 51%; deleting, swapping or negating the rule often leaves the verdict unchanged, mostly on easy cases | d15 (K23) | S (abstract only) |
| LLM legal formalisation is metric-sensitive | Term identification F1 0.70 to 0.82 (best: R1 with Claude Sonnet 4 refinement 0.82). Prior F1 86.74% recomputed 79.03% (recall 49/65 = 75.38%, not 90.78%). Deontic precision 100% | b25 c20 (K19) | E |
| LLM mock jurors: higher guilt probability, far fewer guilty verdicts | 2,304 responses, 2x2x2x3 design: mean guilt probability 63.56 (LLM) vs 58.82 (human); guilty verdicts 21% vs 49% | d12 (K22) | S (abstract only; standard-of-proof wording not seen) |
| No direct LLM test of moving burden or standard of proof | Searched; none found. Position paper only | d11 (K22) | G |

## 4. Mechanisms and models

These are written so an engineer can build them. Each is a plain program with the model filling slots (SCHEMA section 1).

### 4.1 Attack and defeat with three kinds of attack (ASPIC+ in small)

Data structure: an argument is `{id, premises[], rule, conclusion, rule_type: strict|defeasible}`. An attack is `{from, to, kind: rebut|undercut|undermine}`.

- Rebut: `from.conclusion` contradicts `to.conclusion` (and `to`'s last rule is defeasible).
- Undermine: `from.conclusion` contradicts a non-axiom premise of `to`.
- Undercut: `from.conclusion` says the rule used in `to` does not apply here. Always a defeat; no preference check.
- Rebut and undermine succeed as defeat only if the attacker is not weaker under the chosen ordering. Last-link for legal rules; weakest-link for empirical generalisations (a08).

The model's job: list candidate rules, list candidate exceptions for each rule (undercutters), and say which rule outranks which. Code: build the graph and compute the labelling.

### 4.2 Labelling algorithm for grounded semantics (an external table)

This is the table the large-graph tests suggest (K08, K09; no inference-time test exists yet).

1. Label all arguments UNDEC.
2. Repeat until no change: label IN every argument whose attackers are all OUT; label OUT every argument that has an attacker labelled IN.
3. Anything left stays UNDEC. This is the grounded extension, unique and sceptical (a04).

For preferred or CF2 semantics, use a solver; they differ on floating conclusions and odd cycles. The model should only supply the arguments and attack edges. Code computes the labels. In the Li et al. fine-tuning study (d09) models that wrote an explicit step per argument gained 0.17 to 0.22 over answer-only training on larger graphs; the table does that work in code instead.

### 4.3 Burden and standard of proof as an explicit parameter

Two-stage labelling (c19): first run 4.2 to get IN, OUT, UNDEC. Then a burden rule settles UNDEC. If party P has the burden of persuasion on statement s and s is UNDEC, s is treated as not established. Burden of production decides who must bring evidence first. Tactical burden is not fixed; the agent should not set it by rule.

Proof standards as thresholds (a09), weakest to strongest:
- Scintilla: some pro argument that is not defeated.
- Best argument: the best pro argument outweighs the best con argument.
- Dialectical validity: at least one pro and no con argument.

Preponderance and beyond reasonable doubt are not formally defined in Carneades. An engineer can map them to numeric thresholds on a probability, but that mapping is ours, not the literature's.

Implementation: before the verdict, write `{statement, who_must_prove, standard, evidence_for[], evidence_against[]}`. Code applies the standard. Run the same evidence under two standards and record the verdict flips.

### 4.4 Exception slots (Toulmin rebuttal)

For each rule the answer rests on, store `{rule, scope, known_exceptions[], exception_checked: bool}`. Ask the model for exceptions in a separate step. Test each proposed exception on cases it was not fitted to (G3). Prefer the narrowest exception that fits: "except penguins" over "except this penguin" (too narrow) or "except all birds" (too broad) (b12). Prefer an exception that leaves all protected predictions intact; a verifier checks this (b11).

Warning from K12: a generic "check every exemption independently" prompt cut false negatives 7 to 4 but added 20 false positives. Any exception check must be scored on both error types.

### 4.5 Belief-update loop (from DERELAB)

For each new fact: (1) label it strengthen / weaken / neutral for the standing conclusion; (2) code decides whether the conclusion must be re-derived; (3) re-derive from scratch with the new fact in the rule set. The failure to beat is "know but do not output": the model labels weakening and still keeps the old answer (d03). Question order changes the result, so the label step must be a separate call from the verdict step.

### 4.6 Rule priority

Store a priority relation between rules and a reason: specificity (more specific wins), recency, authority (higher source wins). Give it to the model as part of the context; GPT-4o improved when priorities were supplied (a17, b15). BoardgameQA uses recency or preference ordering for the same purpose (a14).

### 4.7 Critical-question operator (CQoT-style)

Ask the model eight questions about its own plan, taken from Toulmin elements: Is the data sufficient? Is the warrant valid? What is the backing? What qualifier? What rebuttal or exception? (c16) Then answer. Gains in the one study are 0.1 to 0.5 points on a 1 to 10 GPT-4o-judged scale, with no token accounting (d07). Treat as a candidate, not an established operator.

### 4.8 Rule-grounding probe

For any answer that cites a rule: delete, swap or negate the rule in a copy of the context and rerun. If the verdict does not change, the answer did not depend on the rule (d15). This is a cheap code-run check, in line with G3 (mutated input) and G10 (reasoning text is not evidence).

## 5. What holds up

**Established or consistent across several sources**
- The conceptual structure (three attack types, undercutting as exceptions, three burdens, proof standards that change outcomes) is stable across 20 years of formal work. (K01, K02)
- Reinstatement is judged weaker than a never-attacked argument. Bezou et al. replicated Rahwan et al. with N=103 vs 20 (t(102)=4.636). Bezou et al. themselves say this supports only "unattacked beats attacked", not gradual semantics. (b04, b06)
- LLM accuracy falls with conflict rate, reasoning depth, chain length and graph size. BoardgameQA (2023), attack-graph puzzles (2025) and abstract-framework tests (2025) agree in direction. (K08)
- Models over-universalise generics and ignore unlisted exceptions, and negation cues drive "weakens". Two benchmarks (Kirkpatrick and Sterken; DEFREASING). (K07)
- Valid exceptions are easy, minimal ones are hard. ABD and DeFAb agree that over-broad exceptions are the failure, even if DeFAb's panel is mostly a format test. (K14)
- Premise errors dominate step-by-step legal-style failures; correct answers hide flawed chains. (K18)
- Prompt format moves results by tens of points. (K13)

**Failures, boundary conditions and cautions**
- **No stable descriptive winner for human semantics.** Cramer and Guillaume find preferred/CF2 fits floating cases (97 to 100%), but 32% of 3-cycle answers fit nothing and context (news vs science) changed acceptance 67.5% vs 27.5%. A source-date confound is suspected. Bezou finds only a weak effect. (K04)
- **The CoT penalty has no independent replication.** Kirkpatrick and Sterken is one team on pre-2025 models. DERELAB shows thinking mode helps on multi-turn updating, so the penalty is task-specific. The explanations offered (overthinking, competence gap) were not tested against each other. (K06, d18)
- **2026 model numbers drift.** Simpson et al. report the same alias moving from 89.7% to 98.5% on spacecraft and 96.6% to 100% on insurance in a month, and withdrew one finding (7/11 became 11/11 on replication). Their own text says the 0/70 rerun "stands as a March finding". Vendor with a commercial interest; a claimed later withdrawal in v3.8 could not be confirmed on the arXiv page. DERELAB seed noise is small (ICC 0.95, CV under 4%), so repeat runs are informative. (K11, d04, d16)
- **Over-correction.** The "evaluate each exemption" prompt lowered net accuracy from 89.7% to 64.7%. (K12)
- **Metric traps.** Accuracy hid recall 38.15 on branching graphs. A prior F1 of 86.74% recomputed to 79.03%. CQoT's text percentages do not match its own table. (K10, K19, d07)
- **Scaffold gains are small and rarely at equal tokens.** ArgLLM +0.04 over direct on one dataset with a small open model; CQoT 0.1 to 0.5 judge points; LOGicalThought +4.41% with about 21.5% more steps and mode-level losses. (K16, K21)
- **Interventions that did not work.** Error-taxonomy feedback gave at most +4% and sometimes lowered accuracy (self-doubt). A format change (few-shot) took GPT-5.4 from 92.9% to 53.9%. Visual input to the graph models added nothing (0.98/0.87 vs 0.98/0.88). (b22, c05, d10)
- **Interventions that worked.** Fine-tuning on step-by-step explanations (0.97 and 0.95 grounded accuracy). A symbolic verifier rejecting over-broad exceptions (34 of 34). A deterministic rule engine on multi-prong tasks (up to +41 points; vendor). Extended thinking on belief updating (gap 0.670 to 0.008). Supplying rule priorities. (a21, b11, b20, d02, a17)
- **Sources not opened.** Ford (2005), Ford and Billington (2000), Hahn and Oaksford (2007), Rahwan et al. (2010), Mercier and Sperber (2011), Park et al. (2025), LLM-ASPIC+ (snippet figures 87.1% and 82.6%; do not cite), "Blind Refusal" (75.4% snippet; do not cite).

## 6. Language models

**Default and generic reasoning (single battery).** Strong 2024 models reach 93 to 96% zero-shot on 20 generic default patterns; weak models sit near or below the 50% chance line (GPT-3.5 48.00; 7 models near chance, 3 below). Differences are non-monotonic in size (Gemma 2 9B beat 27B; Gemini 1.5 Flash beat Pro). (a18, c10)

**What changes the result.**
- CoT: mean -11.14 points for models above 75%; some gain (GPT-4o). Do not assume CoT helps here. (K06)
- Few-shot: +16 to +29 for weak models, -6.81 for Claude 3 Opus. (K13)
- Wording: correlations between rephrasings of one pattern range from 0.99 to -0.05. One prompt is not a measurement. (a20)
- Order and negation: premise order and the word "not" shift answers where logic says they should not. (b09, b17)

**Conflict resolution.** BoardgameQA (2023): few-shot LLMs do poorly; more conflict means worse; models often write wrong proofs with right labels; more distractors hurt monotonically. A prompt-tuned model guessed "unknown" 268 times at depth 1 and twice at depth 2, so label distribution changes with depth. (a14, a15, a16)

**Attack graphs.** Without training, GPT-4o gets 0.54 on grounded extensions of abstract frameworks. Linear witness puzzles: 54 to 77% for non-reasoning models; o1-preview 100% on 75 prompts. Branching graphs: models mostly say "no", and recall is 15 to 38%. Odd and even chain length matter, because the answer depends on the parity of the chain. (c06, c07, c08, a21)

**Exception chains.** Flat rules: 100% (43/43). Three-level chains: 89.7%, then 98.5% a month later for the same alias. A revoking exemption: 64.7%. (c01, c02, b19)

**Late exceptions.** GPT-5.1 default BiasGap 0.935; GPT-5-mini says "weakening" 95.4% of the time and revises only 20.3%. Extended thinking nearly closes the gap for Qwen3-32B. Default reasoning is harder than inheritance for most models. (d01 to d04)

**Exception writing.** Validity 96 to 100% for strong models; one to 1.5 extra exceptions per world; gaps roughly double on holdout worlds. (a23, a24)

**Scaffolds.** Argument-tree scoring (ArgLLM): about the same accuracy as CoT, gains in explanation and contestability (formal monotone-change property, b24). CQoT: small judge-score gains. LOGicalThought: +4.41% over the best baseline, mostly on 7 to 8B models (+6 to +9 points on ContractNLI), and Claude 3.5 Haiku +0.5 to +2. Gains shrink for strong models. (K16, K21)

**Legal-flavoured tasks.** Civ Pro: 27% mean drop accuracy-to-correctness. LegalBench multi-prong tasks: engine beats models by up to 41 points. Rule grounding: verdicts persist when the rule is deleted. (b21, b20, d15)

**Caveats on all of this.** Most evidence is single-lab. Many model names are 2023 to 2024. 2026 results come from vendor or single-group preprints. No equal-token comparison of scaffold vs plain exists in this subfield. Our agent should treat each number as a prior and re-measure.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested. Under G7, an item enters the schema only if it wins at equal tokens against the plain model on our bench. The "Add now" items below are established findings that are cheap, add little or no token cost, or are measurement rules rather than new steps.

### Add now (established)

1. **Do not treat a stated rule as universal.** In S1 or S2, mark each rule as default or strict. Part: G. [E] K07; ev b09 b16 b17 c09.
2. **Premise check before inference.** Verify each premise the answer rests on, in code where possible, before building on it. Part: G / S4. [E] K18; ev b21 b22 c21. Measure correctness of the chain, not only the final answer.
3. **Make rule priority explicit.** When two rules conflict, state the ordering (specificity, recency, authority) as an input. Part: S2. [E] K15; ev a17 b15 c12 c13 a14.
4. **Calibrate format per task type; no fixed few-shot.** Check the yes-rate bias of any exemplar format against zero-shot. Part: G7 (calibration). [E] K13; ev b08 b20 c05 c11.
5. **Report recall and a chance-corrected metric for argument-resolution items, not accuracy alone.** Part: measurement. [S] K10, but the principle follows from skewed labels; ev c07.
6. **Pin model and date, repeat runs, report variance before claiming a scaffold gain.** Part: G7. [S] K11 (drift) with a low-cost principle; ev c02 d04 d16.
7. **Recompute any inherited metric ourselves.** Part: measurement. [E] K19; ev b25 c20 d07.
8. **Keep conclusions open to challenge.** Written answers carry a conclusion, its rule, and what would defeat it. Part: output format only; as a forced step it still needs its own test (see Test first). [E] as a concept, K01; ev a01 a03 a06 a07.
9. **Prefer the narrowest exception that fits held-out cases.** When revising a rule (S5), score exceptions on cases they were not fitted to. Part: S5, G3. [E] K14; ev a23 a24 b10 b11 b12 b13 b14 d14.

Do not add (consistent with section 4b): a generic "check every exemption" prompt (K12 over-correction; same family as "be careful"); agent debate to resolve attacks (G9).

### Test first

| Item | Part | Status | Evidence ids |
|---|---|---|---|
| Explicit exception/undercutter slot vs plain CoT on exception-chain items | S2 / S4, G | [S] K01 K21 | d05 d06 d13 c03 |
| Short direct answer plus one exception check, instead of long CoT, on default items | G11 / S0 mode | [S] K06 | a19 c10 d18 |
| External in/out/undecided labelling table (code computes) on attack graphs | S4 (code check) | [S] K08 K09 | d09 c06 c07 |
| Burden and standard of proof as a stated field before the verdict | S4 / S7 | gap K02 K22 | a09 a11 c19 d12 |
| Late-exception loop: label each new fact strengthen/weaken/neutral, then re-derive | S5 / O | [S] K20 | d01 d02 d03 |
| Critical-questions operator at an impasse | O (new) | [E] small gain K16 | c16 d07 b23 |
| Rule-swap probe on traces | S8 / G3 | [S] K23 | d15 |
| Held-out check of proposed exceptions | S5 / G3 | [E] problem, untested fix K14 | a24 b11 |
| Conditional exception slot (only when an exception is plausible) | S0 mode | [S] K21 | d05 d13 |

## 8. Concrete tests on our bench

All arms get equal tokens (the plain model gets the extra tokens as extra independent samples with a code-side majority vote, per G4 and G5). Use 20 repeats per item on a fixed model and date (K11, d04). Score false positives and false negatives separately (K12).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Exception slot | Rule-with-exception items, 1, 2, 3 nested levels (synthetic, BoardgameQA-style plus statute-style) | plain CoT; plain direct; CoT + forced warrant, exception, undercutter slots | accuracy per depth; false-positive and false-negative rates | Gain concentrated at depth 2 and 3; none at depth 1; risk of added FPs |
| T2 CoT vs direct on defaults | 20 generic default patterns (Kirkpatrick style) with 3 wordings each | zero-shot direct; zero-shot CoT; direct plus one exception check | accuracy; wording variance | CoT lower on strong models if the penalty reproduces; direct plus check at least equal |
| T3 Labelling table | Attack graphs of 5, 15, 25 arguments, linear and branching | free CoT; model lists nodes and edges and code returns grounded labels; model labels step by step | recall, MCC, accuracy | Code table near ceiling if edges are extracted correctly; edge extraction becomes the bottleneck |
| T4 Burden shift | 60 matched pairs: same evidence, standard set to preponderance vs beyond reasonable doubt; burden on plaintiff vs defendant | plain verdict; verdict with explicit burden/standard field; field plus code threshold | verdict flip rate on pairs where the standard should flip it; probability threshold | Plain model flips too rarely or too often; field raises correct flips |
| T5 Late exception | DERELAB-style multi-turn updates, question order swapped | plain; label-then-verdict in one call; label call and verdict call separate | entailment accuracy on weakening turns; BiasGap | Separate calls reduce the know-but-keep gap |
| T6 CQoT | 40 reasoning items from our bench with an executable check (no LLM judge) | self-consistency; CoT; CQoT | pass rate | Gain 0 to 3 points; may vanish at equal tokens |
| T7 Rule-swap probe | Statute items with a known governing rule | plain; plain + probe | verdict change rate when rule deleted/negated; accuracy after probe-triggered re-derivation | Probe exposes insensitivity; recovery size unknown |
| T8 Held-out exception check | ABD-style default theories with 5 holdout worlds | propose exception; propose then test on 1 held-out world and revise once; best-of-N by validity only | extra exceptions over minimum; holdout validity | Fewer extra exceptions with the check |
| T9 Priority supplied | Conflicting-rule items with and without stated priority | no priority; priority given; priority inferred by model first | accuracy on levels- type items | Large gain when supplied; inference step recovers part |
| T10 Format calibration | LegalBench-style tasks, few-shot vs zero-shot | zero-shot; few-shot | accuracy and yes-rate | Direction holds; size is model-specific |

## 9. What does not transfer, and why

- **Choosing a Dung semantics from human data.** Human data are small-N and contested. The agent is not trying to imitate human reinstatement judgments. Do not hard-code grounded, preferred or CF2. Keep "unattacked beats attacked" at most. (K03, K04, b06)
- **Fine-tuning gains.** 0.95 to 0.97 grounded accuracy needs training. Our scaffold cannot train. Only the idea (explicit step-per-argument trace, or a code table) transfers. (K09)
- **Vendor rule-engine margins.** The +41 point margin uses rules authored by the vendor's pipeline. Our agent does not have an expert-written rule base. (b20)
- **Court-process features.** Burden shifting during a hearing assumes a judge, two adversaries and a record. The agent solves tasks alone. Only the parameters (who must prove, which standard) carry over. Tactical burden does not. (a11)
- **Debate as a way to run attack and defence.** The field's model is adversarial, but G9 says multi-agent debate does not beat voting at matched cost. Run the attacks as operators and code, not as arguing agents.
- **Legal discretion and fairness.** Courts can depart from the allocation of burdens on fairness grounds. No programmable analogue. (a11)
- **Qualifier words.** "Probably" and "typically" have no calculus (a02). Do not rely on them to carry probabilities.
- **Synthetic worlds.** ABD, DeFAb, BoardgameQA and the graph puzzles are formal or stylised. Natural-language ambiguity is not tested there. (b13, c14, d10)
- **Civ Pro analogies.** The Mishra benchmark mixes in analogical reasoning, so the 27% drop is not purely defeasible-rule error. (c21)
- **Case-based reasoning.** Belongs to the analogy and precedent subfield.

## 10. Open questions

1. Does an exception slot raise accuracy at equal tokens over plain CoT, given that CoT alone may hurt default items? (partly informed by d05, d13; no equal-token test)
2. Is the CoT penalty reproduced by an independent team, on 2026 models, and does direct-plus-exception-check avoid it? (no same-task replication)
3. Does an external labelling table fix large-graph collapse without fine-tuning? Edge extraction from natural-language text is the unknown. (d10: authors admit text-to-argument mapping is not studied)
4. How much does moving the burden or standard of proof change LLM verdicts on identical evidence, and do models track it? (no direct test)
5. Do LLMs propose minimal exceptions on held-out cases, and can a model-side held-out check cut over-breadth? (only a symbolic verifier tested)
6. How many repeats are needed to trust a 2026 scaffold gain, given silent drift? (d04 low noise; d16 drift)
7. Does false-positive inflation from "check exceptions" prompts generalise beyond one vendor benchmark? (LogT shows false negatives fall 41% to 28%; no false-positive data)
8. Which human data should the schema follow when LLM and human semantics disagree? Is void precedence enough?
9. Do critical-question scaffolds keep their gains with a non-LLM judge and at equal tokens?
10. Does the "know but do not output" gap (d03) show up on legal items, not just synthetic graphs?
11. Does the rule-insensitivity result (d15) hold for hard cases, and what fixes it? Only the abstract was read.
12. No human-expert baseline for exception-chain items, and no legal-practitioner study of LLM burden-of-proof handling.

## 11. Sources

[V] = opened and read this session or earlier in this run; [M] = snippet or secondary mention only.

- [V] Prakken (2020) Historical overview of formal argumentation. https://webspace.science.uu.nl/~prakk101/pubs/history.pdf (a01 a03 a04)
- [V] Bench-Capon, Atkinson, Bex, Prakken, Verheij (2024) Computational models of legal argument (handbook chapter). https://webspace.science.uu.nl/~prakk101/pubs/LegalArgHB24.pdf (a02 a13)
- [V] Prakken and Vreeswijk (2002) Logics for defeasible argumentation. https://webspace.science.uu.nl/~prakk101/pubs/handbook.pdf (a05)
- [V] Prakken (2010) An abstract framework for argumentation with structured arguments. https://webspace.science.uu.nl/~prakk101/pubs/aspicAF.pdf (a06)
- [V] Modgil and Prakken (2014) The ASPIC+ framework: a tutorial. https://webspace.science.uu.nl/~prakk101/pubs/ASPICtutorial.pdf (a07 a08)
- [V] Gordon, Prakken, Walton (2007) The Carneades model of argument and burden of proof. https://webspace.science.uu.nl/~prakk101/pubs/GordonPrakkenWalton2007a.pdf (a09 a10)
- [V] Prakken and Sartor (2009) A logical analysis of burdens of proof. https://webspace.science.uu.nl/~prakk101/pubs/p+sbop09.pdf (a11)
- [V] Prakken and Sartor (2007) Formalising arguments about the burden of persuasion. https://webspace.science.uu.nl/~prakk101/pubs/icail07bop.pdf (a12)
- [V] Calegari and Sartor (2020) Burden of persuasion in argumentation. https://arxiv.org/abs/2009.10244 (c19)
- [V] Bex and Prakken (2026) Toulmin Argumentation Logic. https://webspace.science.uu.nl/~prakk101/pubs/comma26TAL.pdf (c18)
- [V] Cramer and Guillaume (2018) Empirical cognitive study on abstract argumentation semantics. https://icr.uni.lu/mcramer/downloads/2018_COMMA_empirical.pdf (b01 b02 b03)
- [V] Bezou Vrakatseli, Prakken, Janssen (2021) New experiments on reinstatement and argumentation semantics. https://webspace.science.uu.nl/~prakk101/pubs/BezouNMR21.pdf (b04 b05 b06)
- [V] Kazemi et al. (2023) BoardgameQA. https://arxiv.org/abs/2306.07934 (a14 a15 a16 c14)
- [V] Tachmazidis, Batsakis, Antoniou (2024) Benchmarking defeasible reasoning with LLMs. https://arxiv.org/abs/2410.12509 (a17 b15 c12)
- [V] Antoniou and Batsakis (2023) Defeasible reasoning with LLMs, initial experiments. https://ceur-ws.org/Vol-3485/paper7687.pdf (c13)
- [V] Kirkpatrick and Sterken (2025) Generics and default reasoning in LLMs. https://arxiv.org/abs/2508.13718 (a18 a19 a20 b07 b08 b09 c10 c11)
- [V] Li, Fang, Chen, Li, Liao (2025) Enhancing conflict resolution in language models via abstract argumentation. https://arxiv.org/abs/2412.16725 and https://arxiv.org/html/2412.16725v2 (a21 a22 c23 d09 d10)
- [V] Steging, Renooij, Verheij (2025) Parameterized argumentation-based reasoning tasks. https://arxiv.org/abs/2505.01539 (c06 c07 c08)
- [V] Allaway and McKeown (2025) DEFREASING. https://aclanthology.org/2025.naacl-long.529.pdf (b16 b17 c09)
- [V] Batzoglou (2026) ABD: default-exception abduction. https://arxiv.org/abs/2602.18843 (a23 a24 b13 b14 c25)
- [V] Cooper, Sadhu, Velasquez (2026) DeFAb. https://arxiv.org/abs/2606.18557 and https://arxiv.org/html/2606.18557 (b10 b11 b12 c24 d14)
- [V] Simpson, Kozak, Doake (2026) Confidently wrong: exception chain collapse. https://arxiv.org/abs/2607.23386 (b18 b19 b20 c01 to c05 d16)
- [V] Mishra et al. (2025) Shortcomings of LLMs in step-by-step legal reasoning. https://arxiv.org/abs/2502.05675 (b21 b22 c21)
- [V] Freedman et al. (2025) Argumentative LLMs for explainable and contestable decision-making. https://arxiv.org/abs/2405.02079 (b23 b24 c15)
- [V] Horner, Mateis, Governatori, Ciabattoni (2025) Toward robust legal text formalization. https://arxiv.org/abs/2506.08899 (b25 c20)
- [V] Castagna, Sassoon, Parsons (2024) Critical questions of thought. https://arxiv.org/abs/2412.15177 and https://arxiv.org/html/2412.15177v1 (c16 d07); earlier work https://arxiv.org/abs/2405.13036 (d08, abstract only)
- [V] Gupta, Zuckerman, O'Connor (2024) Harnessing Toulmin's theory for zero-shot argument explication. https://aclanthology.org/2024.acl-long.552 (c17)
- [V] Nananukul et al. (2025) LOGicalThought. https://arxiv.org/abs/2510.01530 and https://arxiv.org/html/2510.01530v1 (c22 d05 d06)
- [V] Prajescu and Confalonieri (2025) Argumentation-based explainability for legal AI. https://arxiv.org/abs/2510.11079 (c26)
- [V] Scheffers (2026) Argumentation-based system for fraud detection. https://ceur-ws.org/Vol-4253/paper4.pdf (c27)
- [V] Sadhu, Shahad, Marino (2026) DERELAB. https://arxiv.org/abs/2608.30413 (d01 to d04)
- [V] Sadhu et al. (2026) Verdict without the rule. https://arxiv.org/abs/2610.12313 (d15, abstract only)
- [V] Chen, Li, Wan, Yuan (2026) From statute to control flow (NormBench). https://arxiv.org/abs/2606.08932 (d13, abstract only)
- [V] Linna and Linna (2026) Challenges for generative AI in legal reasoning. https://arxiv.org/html/2508.18880v2 (d11)
- [V] Sun et al. (2025) LLMs as jurors. https://research.abo.fi/en/publications/large-language-models-llms-as-jurors-assessing-the-potential-of-l/ (d12, abstract page only)
- [M] Toulmin (1958) The Uses of Argument. https://doi.org/10.1017/CBO9780511840005 (a29 b30)
- [M] Reiter 1980, McCarthy 1980, Gelfond and Lifschitz 1988, read via secondary sources (a25)
- [M] Dung (1995). https://doi.org/10.1016/0004-3702(94)00041-X (b27)
- [M] Prakken and Sartor (1997). https://doi.org/10.1080/11663081.1997.10510900 (b28)
- [M] Rahwan, Madakkatel, Bonnefon, Awan, Abdallah (2010). https://api.philpapers.org/rec/RAHBEF (b26)
- [M] Ford (2005). https://link.springer.com/doi/10.1007/s11229-005-9071-z (a26)
- [M] Ford and Billington (2000). https://doi.org/10.1111/0824-7935.00119 (a27)
- [M] Hahn and Oaksford (2007). https://doi.org/10.1007/s10503-007-9022-6 (a28)
- [M] Mercier and Sperber (2011). https://doi.org/10.1017/S0140525X10000968 (b29)
- [M] LLM-ASPIC+ (2025). https://api.crossref.org/works/10.3233%2FFAIA250981 (c28; do not cite numbers)
- [M] Park, Choi, Park (2025) Objection, your honour. https://doi.org/10.1007/s10506-025-09432-2 (c29)
- [M] Blind Refusal (2026). https://arxiv.org/html/2604.06233 (d17; do not cite numbers)
