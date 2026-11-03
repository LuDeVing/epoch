# Paraconsistent logic: deep document

*Subfield D03.06. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K32), critique.md in this folder. Evidence ids (a01, b14, d11 ...) point to those files. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Classical logic has a rule called explosion (ex contradictione quodlibet, ECQ). From A and not-A, anything follows. One bad pair of beliefs then ruins the whole belief set. A paraconsistent logic is a logic where explosion fails. The agent can hold a contradiction and still reason about unrelated things. (a01, a02)

Two ideas must be kept apart.
- **Paraconsistent logic**: a formal system where contradictions do not explode. This is a design choice about inference rules.
- **Dialetheism** (Priest): the claim that some contradictions are true. This is a metaphysical position. An engineer does not need it. We only need the first idea. (a06)

Why this matters for our agent. At an impasse (S6) the agent often holds two candidate answers, or two sources, or a premise set that clashes. Today there are three common reactions: pick one silently, halt, or repair by deleting. A paraconsistent stance adds a fourth: keep both, mark the conflict, and keep working on everything that does not depend on it.

What the evidence says in one paragraph. The formal theory is mature and gives usable design patterns (bilateral records, consistency flags, retract-on-conflict, chunking). The human data on "true contradictions" is fragile and contested. The LLM data is almost all about detecting or reporting conflicts. It shows that unprompted models rarely notice or report conflicts, that a forced conflict check helps, and that reporting is cheap. No study tests the core S6 question: does an agent that keeps a flagged contradictory set solve more problems than one that repairs or halts, at equal tokens? We found one LLM paper that uses a Belnap-style scaffold (Allen et al. 2025). The search was rate limited, so this is weak evidence of absence (K25, d18).

## 2. History and theories in depth

### 2.1 The six families (a01)

| Family | Origin | How it blocks explosion | Engineering reading |
|---|---|---|---|
| Discussive | Jaskowski 1948, modal S5 | Premises are held by different "participants". Conjunction is split: A and-d diamond B | Keep claims from different sources in separate stores. Do not conjoin across stores |
| C-systems / LFIs | da Costa, from 1963; C1 hierarchy | A consistency operator oA. Explosion holds only for oA-marked formulas | A "verified, trusted" flag. Classical reasoning on flagged facts, contained reasoning elsewhere |
| LP (Logic of Paradox) | Priest 1979 | Third value b (both). Designated values t and b | Store a "both" state. Weaken modus ponens and disjunctive syllogism |
| FDE / Belnap-Dunn | Belnap 1977 | Four values: told-true only, told-false only, both, neither | Store (evidence for, evidence against) separately |
| Relevant logics | Anderson, Belnap, Routley-Meyer | Premises must be relevant to the conclusion | Block derivations that use irrelevant premises |
| Adaptive logics | Batens | Reason classically by default. Retract lines when an abnormality (A and not-A) involving them appears | Dependency-tracked retraction |

### 2.2 LP in detail (a02)
- Values t, f, b. Designated (acceptable as true): t and b. Negation swaps t and f, keeps b.
- Explosion fails. Counter-model: p = b, q = f. Then p and not-p are designated, q is not.
- Modus ponens fails for the material conditional. With p = b, q = f, the conditional p -> q has value b. Both premises are designated, the conclusion is not.
- Disjunctive syllogism (from A or B, and not-A, infer B) is not generally valid.
- Cost: LP keeps excluded middle but loses the rules that carry a contradiction onward. Weaker inference. This is the price of containment.

### 2.3 Belnap's four values and the two orders (a07, a08)
- Belnap's motivation was a computer fed by several sources. A source may say true, say false, say both, or say nothing. The four values are True, False, Both, None.
- Key idea (Jakl 2025 survey): two orders on the lattice. The truth order and the information order. "Both" is the top of information: it has the most information, not the least.
- Ginsberg bilattices generalise this. Fitting showed a fixed-point semantics for logic programs.
- Engineering reading: each claim carries two counters or flags, one for support and one for refutation. This is the cheapest paraconsistent data structure.

### 2.4 da Costa C-systems and LFIs (a03)
- C1 is positive classical logic plus double negation elimination plus axioms with a consistency operator: oA -> (A -> (not-A -> B)); (oA and oB) -> o(A and B); (oA -> oB) -> o(A -> B).
- Hierarchy C_i via A^1 = not(A and not-A).
- Explosion is restored only for formulas marked consistent. C-omega is not an LFI because it lacks classical positive logic.
- Engineering reading: a "verified" flag. Classical rules apply to flagged facts. Unflagged facts that clash are contained.

### 2.5 Adaptive logics (a04)
- Three parts: a lower-limit logic (paraconsistent), a set of abnormalities (often A and not-A), a strategy.
- The upper-limit logic adds rules like disjunctive syllogism. Lines derived with those rules are retracted if an abnormality involving their premises appears.
- Worked example in the SEP: premises {p, not-p or r, not-r or s, not-s, s or t}. A derivation of t by disjunctive syllogism is withdrawn when the chain clashes.
- The excerpt did not describe dynamic-proof marking in detail.
- Engineering reading: every derived line stores which premises it used. When a conflict among premises appears, only lines that depend on those premises are withdrawn. Others stay.

### 2.6 Chunk and permeate (a05)
- Keep consistent chunks Sigma_i and a permeability relation rho. Stage 0 is the closure of each chunk. Stage n+1 adds to chunk i the part of chunk j that rho(j,i) lets through.
- Consequences are read from one designated chunk.
- Limit: a hand-built permeability relation is needed.

### 2.7 Dialetheism and the Rationality Principle (a06)
- Priest's main argument: the liar and other self-reference paradoxes, under a principle of uniform solution. Curry's paradox forces dropping contraction.
- Consistency is one epistemic virtue among others (adequacy to data, simplicity, explanatory power). It can lose to them.
- The SEP entry does not cover empirical studies.

### 2.8 Recent formal work (a27, c14)
- Dynamic epistemic paraconsistent logics (Ongaratto and van Ditmarsch 2026): action models over LFI1, paraconsistent public announcement, factual change. Sound and complete. Aim: formalise how provisional contradictions are handled over time.
- Bienvenu, Bourgaux, Kozhemiachenko 2024: four-valued querying of inconsistent ontologies; "exactly true" versus "has contradictory evidence". Tractable (data complexity) for Horn description logics. Not an LLM study.
- Older working systems not opened: 4QL (c23), Arieli and Avron 1996 (c24), Gao, Fodor, Kifer 2016 word puzzles (a29). Do not cite numbers.

### 2.9 The human data on true contradictions
This is the empirical side of dialetheism. People were asked whether "x is tall and not tall" is true for a borderline x.

**Alxatib and Pelletier 2011 (b01-b03, a10-a12).** N = 76 SFU undergraduates (63.2% native English speakers). 20 true / false / can't tell items, 4 per man, 5 men (5'4, 5'11, 6'6, 5'7, 6'2), no fillers, random order.
- At 5'11: "tall and not tall" true 44.7% (34 of 76), false 40.8%.
- "neither tall nor not tall" true 53.9% (41 of 76).
- Of the "neither" acceptors, 53.7% also accepted "both"; 31.7% rejected it; 14.6% can't tell. Of the "both" acceptors, 64.7% also accepted "neither".
- "tall" true: 1.3% at 5'4, 46.1% at 5'11, 98.7% at 6'6. "not tall" true 25.0%, false 67.1% at 5'11. Subjects deny more readily than they assert the negation.

**Replications and variants (b04-b07, b24).**
- Ripley 2011: no preference between gap and glut descriptions on a 1-7 scale; acceptance highest at middle distances. Means only in a figure.
- Serchuk, Hargreaves and Zach 2011 (table inside the Egre chapter, N = 350 responses per sentence): "x is P and x is not P" true 66, false 195, other 89 (about 19%). "x is P and it is not the case that x is P" true 25, false 247, other 78 (about 7%). "Either P or not P" true 113, false 137, other 100. Another sentence 141 / 88 / 121.
- Egre et al. (N = 148 MTurk, none excluded): both "and" (glut) and "neither" (gap) accepted above false controls, but "neither" preferred. Mixed-effects logistic regression, baseline Neither: intercept 3.60; And -4.35 (z = -8.98); control False -10.52; control True +4.24. Order effects (about 50% to 35%) and adjective effects (about 37% to 66%). More than 37% accepted "neither" and "and" together.

**Reading.** Acceptance of borderline glut sentences exceeds false controls in every study, but the rate ranges from 7% to 66% depending on wording, order and adjective. The 44.7% figure is a high outlier. The range is a method effect.

**Competing explanation (b08, b09).** Cobreros, Egre, Ripley and van Rooij 2015: strict-tolerant semantics plus a strongest-meaning hypothesis predict the acceptance data while explosion stays valid under st-consequence. Alxatib, Pagin and Sauerland 2013 reply: the pragmatic account predicts wrong readings for some disjunctive cases. Status: contested (K08). A "can't tell" explanation is rejected by Egre because it cannot explain "and" acceptance.

None of this is about reasoning performance. It shows only that human reasoners tolerate glut-like states.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Explosion is a design choice; six families block it differently | six families; LP counter-model p=b, q=f | a01-a04 (SEP) | [E] formal fact (K01) |
| Belnap four values give a cheap bilateral record | values T, F, Both, None; two orders | a07, a14, b10 | [E] (K02) |
| Humans accept borderline "tall and not tall" | 44.7% (34/76); "neither" 53.9% (41/76); N=76 | Alxatib & Pelletier 2011 (b01) | [S] (K05) |
| Glut acceptance is fragile | 66/350 (19%), 25/350 (7%); N=148 coef -4.35; order 50% to 35%; adjective 37% to 66% | Serchuk via Egre; Egre (b04, b06) | [E] (K06) |
| Gap and glut come from the same people | 53.7% of "neither" acceptors also accept "both" | b02, a11 | [E] (K07) |
| Pragmatic accounts explain the data without dialetheism | st-consequence keeps explosion | b08, b09 | [C] (K08) |
| Bilateral LLM judging raises F1 on answered items | GPQA flagship 0.699 vs 0.633; SimpleQA flagship 0.736 vs 0.657; mean +0.062 (p<0.01) | Allen 2025 (c02) | [S] (K09) |
| ...at a big coverage cost | coverage 0.499-0.589 vs 1.000; mean change -0.456 | c02, d11 | [S] (K30) |
| ...and about double the tokens | 4,782 vs 2,213 (GPQA flagship); 3,964-4,164 vs 2,100-2,167 (SimpleQA) | c03, a18 | [S] (K10) |
| LLM judges return gluts often | flagship GPQA glut 0.301, gap 0.110; GPT 59.0% glut, Claude 19.6% glut and 30.4% gap, Llama 52.9% glut | c04, a16, d12 | [S] (K11, K32) |
| Glut rate varies by topic | video games 63.6%, sports 47.3%, history 35.7% | d12 | [S] (K32) |
| Glut-tolerant KB reasoner localises contradictions | 940 statements (228 asserted + 712 derived), 92 gluts, 2 gaps, still satisfiable; LLM calls over 99% of runtime | a17, c05 | [S] (K12) |
| LLMs keep deducing from contradictions | GPT-4o halts on 56.0% of 800 items; Gemma-3-4B 43.9%; base accuracy 0.789 and 0.580 | Bao 2025 (b14, b15) | [S] (K13) |
| Trained halting reaches 1.000 on synthetic data | Qwen2-1.5B V3: SFT 0.210, CoT 0.510, RA-CoT 0.865, Fusion-LRA 0.972; Fusion-Conflict 1.000 | b16 | [S] (K14) |
| Unprompted conflict reporting is rare | WikiContradict no cue 2.1-10.4%; PCBench proactive 4.0% (o4-mini) to 40.5% (DeepSeek-V3) | a19, a21, c09 | [E] (K15) |
| Telling the model to check helps | WikiContradict cue 10.4-43.8%; PCBench assisted 53.5-77.9% | a19, c09 | [E] (K15) |
| Cue helps explicit conflicts more than implicit | Llama-3-70b explicit 13.3% to 60.0%; implicit 5.9% to 17.6%; GPT-4 6.3% to 10.4% | c11 | [S] (K16) |
| Conflict-type naming is hard | type accuracy 53.1-65.3%; oracle type +24 points; pipeline +9 | Cattan 2025 (c12) | [S] (K17) |
| Self-contradiction in documents is hard | binary accuracy 50.1-53.8%; GPT-4 recall 8.0% at 97% precision; evidence hit 70.2% | ContraDoc (b17) | [E] (K18) |
| Self-contradiction in one document is the hardest type | accuracy 0.006-0.456; cross-document pairs up to 0.893 | Gokul 2025 (d03) | [E] (K27) |
| Reasoning models overthink flawed premises and do not report | cost ratio up to 3.90 (o3-mini); R1 2.71 | PCBench, Fan (b19, c10) | [E] (K19) |
| A forced premise check raises reporting and cuts tokens | R1 19.6% to 67.7%, tokens 2590 to 1014; o3-mini 14.4% to 73.2%, tokens 1279 to 1023 | d13 | [E] (K28) |
| Models silently choose a side | resolve by chance 24% (Sonnet), 38% (Haiku) | ECon (d07) | [E] (K28) |
| Adjudication is order sensitive | answer flips 11.4-25.2% (mean 18.6%); accuracy gap 11.1 points; N=920 per model, 6 models | Han 2026 (d01) | [E] (K26) |
| Detection is much less order sensitive | F1 moves 0.4-2.8 points for strong LLMs | d06 | [E] (K26) |
| Premise order shifts deduction accuracy | up to 20-30% for GPT-4-turbo and PaLM 2-L | Chen 2024 (b22) | [S] (K20) |
| Keep-both-then-adjudicate beats plain prompts | GPT-4o about +20% relative F1; Open-Mistral-7B about 3x | XoT (d09) | [S] (K29) |
| Solver-backed repair raises cross-query consistency | SetCons deep subset no solver 0.52, check-only 0.84, repair without core 0.88, core-guided 0.91; overhead 1.51x | Salla 2026 (c15) | [S] (K21) |
| ...but plain self-consistency matches it | SC K=20 reaches 0.88-0.94 at 1.48-1.58x | c15, c25 | [S] (K21) |
| Accuracy gain from repair is small | R1 0.80 to 0.85; deep subset 0.77 to 0.81 | c16 | [S] (K22) |
| Logic checkers can hurt on defeasible items | only 1 of 7 models above 0.6 (chance 0.25); GPT-4o 0.0022 on MT categorical; best prompt +24.13 | Rulebreakers (c06-c08) | [S] (K23) |
| Belief revision after premise edit fails | Qwen3-1.7B initial 0.667, revised 0.467, inertia 0.600 | DeltaLogic (c18, d10) | [S] (K24, K31) |
| Save-time conflict check in agent memory | detected 66% of injected conflicts vs 14% best baseline (4.7x); LoCoMo 89.35% | MOSAIC (a25) | [S] |
| No LLM study tests paraconsistent scaffolds for agents | zero hits on two queries; one near hit | a28, d18 | [S] weak (K25) |

## 4. Mechanisms and models

Everything below is explained so that it can be built as plain code around a model that fills slots.

### 4.1 Bilateral claim record (Belnap/LP)
Data: for each claim c, two fields: `for(c)` and `against(c)`, each a list of (source, strength) pairs. Derived value:
- for non-empty, against empty: TRUE
- for empty, against non-empty: FALSE
- both non-empty: BOTH (glut)
- both empty: NONE (gap)

Rules:
1. Never overwrite. A new contradicting note is appended to the other field.
2. Do not chain through a BOTH claim by modus ponens or disjunctive syllogism (LP failures, a02). Code rejects a derivation step whose premise is BOTH, unless the step is marked "checked".
3. A BOTH claim is a task for S6: send it to external verification (tool, held-out check), not to a model vote.

How Allen et al. get the pair (c01, a14): call the model twice per claim. Prompt 1: can this be verified? Prompt 2: can this be refuted? The pair gives the value. Cost is about 2x tokens (c03). Their tableau reasoner (ACrQ, sound and complete with respect to LLM-grounded interpretations, Thm 10 and 11) runs in under 10 ms; the LLM calls are over 99% of runtime (c05).

### 4.2 Consistency flag (da Costa)
Add a boolean `ok(c)` per fact, set only by code when a check passes on something the answer was not fitted to (G3). Inference rule: the classical rule set is allowed only if all premises are `ok`. Any derivation touching a non-`ok` fact is stored as "provisional", with the list of non-`ok` premises it used. No source tested this (d19).

### 4.3 Dependency-tracked retraction (adaptive logic)
Each derived line stores `deps` = the set of premise ids used. On detecting a conflict among premises P_conf, mark every line whose `deps` intersects P_conf as retracted. Lines whose `deps` are disjoint remain. Compare with two common alternatives: re-solve from scratch, or halt. Salla et al. use a related idea: extract commitments, check with a solver, repair the smallest conflicting set (a minimal unsatisfiable core). Core-guided repair beats repair without a core (0.91 vs 0.88 on the deep subset) and check-only (0.84) (c15).

### 4.4 Conflict register at S6 entry
One line per detected conflict: `conflict: <claim A> vs <claim B>; type: explicit | implicit | self | cross-source; status: kept | resolved-by <check>`. The register is the engineering form of "notice and report". Evidence: forcing a premise check raised reporting from 19.6% to 67.7% (R1) and 14.4% to 73.2% (o3-mini), and cut tokens (d13). Reasoning text is a poor audit channel (d14: flip pairs keep 96% of same-answer reasoning similarity; confidence carries the signal). So the register must be filled by a code-triggered question with a structured answer, not read from free-form reasoning (G10).

### 4.5 Keep-both-then-adjudicate (XoT) (d09)
Stage 1: list every candidate answer, each with an explanation tied to its source. Stage 2: decide. This is a kept-both-sides record followed by one adjudication. It beat direct, CoT and conflict-aware prompts on text-versus-KG conflicts. It was not compared with retraction or halting and not at equal tokens.

### 4.6 Order-robust adjudication (d01, d06, d08)
Run adjudication in both orders (or randomise). Count a flip as a conflict signal. Han et al.: reversing two contradictory documents flips the answer in 11.4-25.2% of items (mean 18.6%). The sign of the order effect differs by model (ConflictQA TripleConf evidence-order gap in F1: Qwen3-8B +19.74, Open-Mistral-7B +9.79, GPT-4o +4.14, GPT-5.1 -4.82, DeepSeek-V3.2 -7.71, Llama-3.1-8B -4.72), so there is no universal "put the best first" rule. Reasoning models show smaller order gaps than general models.

### 4.7 Conflict score for abstention (d02)
Raw confidence is a poor abstention signal under conflict (selective-accuracy gain -1.2 to -2.1 points in the incorrect-only setting). A conflict-aware score (confidence drop against a no-context baseline) beat it (+33.4 points at 25% coverage, K32). Mean ECE: 0.057 with correct-only context, 0.456 with incorrect-only. Use as a trigger for external verification, not as a verdict.

### 4.8 Save-time conflict check for memory (a25)
MOSAIC: on writing a new fact, compare it with graph neighbours and update or delete contradicting entries. Detected 66% of injected conflicts vs 14% for the best baseline. This is the retract policy, not the keep-both policy. Single source.

### 4.9 Calibration per model
Glut rates differ by family (GPT 59.0%, Llama 52.9%, Claude 19.6%) and by topic (63.6% to 35.7%), so a fixed glut threshold cannot be universal. Calibrate on a small labelled set per model.

## 5. What holds up

### 5.1 Replicated or multi-source
- **Unprompted LLMs rarely report conflicts** (K15, K28). Independent sources: WikiContradict (a19), PCBench (a21, c09), ECon (d07), Fan et al. (b19). Different tasks, different models, same direction.
- **A forced check raises reporting** (K15, K28): WikiContradict cue, PCBench instructed, ECon forced conflict question.
- **Self-contradiction in one document is hard** (K18, K27): ContraDoc (b17), Gokul (d03), Self-Contra (a24: GPT-4 52.2% F1 vs 66.7% for humans). Precision is high (above 0.9, up to 97%); recall is low (8.0% for GPT-4 on ContraDoc).
- **Adjudication order sensitivity** (K26): Han et al., ConflictQA, ECon, Chen et al. (premise order).
- **Reasoning models notice but do not report** (K19): PCBench case study (a22), Fan et al. Second-hand data say thinking tokens acknowledge injected signals 87.5% vs 28.6% in stated outputs (d15, not opened).
- **Human glut acceptance above controls but unstable** (K06, K07): four human experiments.

### 5.2 Single-source (use with care)
Bilateral judging (K09), consistency repair (K21), halting (K13), XoT (K29), DeltaLogic (K24), conflict-type step (K17), glut-rate calibration (K32).

### 5.3 Failures and confounds
- **Bilateral judging is confounded with abstention** (K30). Unilateral coverage 1.000; bilateral 0.499-0.589. F1 is computed on answered items only. Authors frame the trade as selective classification. A unilateral judge that abstains at the same coverage was not tested. The 0.062 F1 gain cannot be credited to the paraconsistent structure.
- **Self-consistency matches the solver pipeline** (K21): SC K=20 gives 0.88-0.94 SetCons at 1.48-1.58x versus the solver pipeline 0.91 at 1.51x. The headline 0.56 to 0.94 is a no-CoT to SC jump, not a solver effect (critique item 8).
- **Accuracy gains from repair are small** (K22): 0.80 to 0.85 (R1) and 0.77 to 0.81 (deep subset).
- **Logic checkers hurt on defeasible items** (K23): LogicLM and SymbolicCoT lowered rulebreaker paired accuracy. More logic is not always better. Models hold a latent signal (higher confidence on valid than on rulebreaker cases, p < 0.0001) that outputs hide (c07).
- **Halting is not paraconsistency** (K14, critique): Bao counts "halt" as correct. A paraconsistent view would keep working on the consistent part. The benchmark cannot test that.
- **Chain of thought does not help type naming**: it lowers type-detection performance 8% (Claude) to 25% (Llama-70B) (d04), though CoT stabilises position effects (an 18.8-point near/far gap for Sonnet falls to 0.7).
- **Prompt effects are large and inconsistent** (a15): best GPQA is Llama 4 Maverick 0.774 (direct); worst GPT-4o Mini zero-shot 0.400.
- **Judge error**: the WikiContradict automatic judge over-rates Mistral-7b (39.6% vs 20.8% human) (a20). Human eval was only 48 instances and 5 models.
- **Synthetic data**: Allen negatives were partly generated by GPT-4o Mini; Bao tasks are synthetic; ConflictQA conflicts are built by corrupting one source.

### 5.4 Moderators
| Moderator | Effect | Source |
|---|---|---|
| Explicit vs implicit conflict | explicit 13.3-60.0% vs implicit 5.9-17.6% (Llama-3-70b); implicit about 3x worse | c11, d16 |
| Within-document vs cross-document | self 0.006-0.456; pair up to 0.893 | d03 |
| Reasoning hops | identification 74.73 (ECON), 69.93 (WikiContradict), 64.54 (MAGIC); localisation 57.09, 55.74, 40.51 | c13 |
| Model family | glut 59.0 / 19.6 / 52.9% | d12 |
| Topic | glut 63.6% to 35.7% | d12 |
| Prompt wording | recall varies; precision stable (Mixtral recall 23.35, SD 3.46) | d05 |
| Reasoning vs non-reasoning | reasoning models overthink and silently pick one side; non-reasoning ones fail to notice | b19, d08 |
| Evidence order | adjudication flips 11-25%; detection moves 0.4-2.8 F1 | d01, d06 |

### 5.5 Interventions that worked and did not
- Worked: explicit conflict cue (WikiContradict, PCBench); forced premise check (also cut tokens for reasoning models); XoT list-then-adjudicate; core-guided repair (modest accuracy gain); fine-tuning for halting (synthetic only); MOSAIC save-time check; conflict-aware abstention score.
- Did not work or hurt: raw confidence as abstention signal; CoT for conflict-type naming; logic-enhanced pipelines on defeasible items; a written rationale as audit of why the model flipped (d14); reordering evidence as a universal fix (d08).

## 6. Language models

### 6.1 Behaviour on contradiction tasks
| Task | Models | Result |
|---|---|---|
| Contradictory premise set (Bao) | GPT-4o, Gemma-3-4B | halt 56.0% and 43.9% of 800; the rest continue deducing; with {A->B, A, not B}, GPT-4o concludes B (b15) |
| Conflicting passages, no cue (WikiContradict) | 5 models | 2.1-10.4% reflect both (a19) |
| Same, with cue | 5 models | 10.4-43.8% (a19) |
| Premise critique (PCBench) | 15 models | proactive 4.0-40.5%, assisted 53.5-77.9% (a21) |
| Self-contradiction in documents (ContraDoc) | GPT-3.5, GPT-4, PaLM2, LLaMA2 | accuracy 50.1-53.8%, GPT-4 recall 8.0%, precision 97% (b17) |
| Conflict detection (ECon) | 5 models | precision 95-99%, recall 23-70% (d05) |
| Resolution (ECon) | Sonnet, Haiku | chance pick 24% and 38% (d07) |
| Order reversal (HealthContradict) | 6 open models | 11.4-25.2% flips (d01) |
| Rule vs world knowledge (Rulebreakers) | 7 models | chance 0.25; only Llama-3-8B above 0.6 (c06) |
| Belief-inconsistent syllogisms (BIS) | many | GPT-5-mini 99.72%, Qwen3-32B 99.58%, GPT-4o 79.54%, GPT-4-turbo 59.48%; GPT-5-nano medium 98.84% vs minimum effort 69.22%; Claude-3-opus 7.18% (c17) |
| Belief revision (DeltaLogic) | Qwen3-0.6B to 4B, Phi-4-mini | inertia 0.600 for Qwen3-1.7B and 4B; Phi-4-mini 0.950 to 0.850 (c18) |
| Counterfactual premises (CounterLogic) | 11 LLMs | accuracy down about 27% on average (a30, snippet only) |

### 6.2 What changed behaviour, and by how much
- A conflict cue: +10 to +40 points on WikiContradict for stronger models; GPT-4 only +4.1.
- A forced premise check: reporting +48 to +59 points (R1, o3-mini); tokens down 61% for R1 (2590 to 1014) and 20% for o3-mini (1279 to 1023). Instructed o3-mini output (1023) is still above the unflawed task (328).
- Reasoning effort: GPT-5-nano 69.22% at minimum effort to 98.84% at medium on belief-inconsistent syllogisms (c17).
- Prompt wording for bilateral judging: macro-F1 swings from 0.400 to 0.774 on GPQA (a15).
- Fine-tuning with a symbolic reward (Bao): V3 halting from 0.000 to 0.972-1.000. Not available to our agent (no training).
- Solver-backed repair: SetCons 0.52 to 0.84 (check-only) to 0.91 (core-guided) on the deep subset. Self-consistency alone gives most of it.
- Scale does not fix it. Qwen3 8B to 235B non-thinking: assisted critique 59.9-70.0%, proactive only 20.6-24.7%. Qwen3-235B thinking: proactive 35.3%, assisted 70.1% at 3,629 tokens (c10).

### 6.3 Paraconsistent scaffolds for LLMs
- Allen et al. 2025 is the only direct one. It uses a model as the interpreter of a Belnap-style four-valued logic and a tableau prover with soundness and completeness proofs. Tested on judging factual claims, not multi-step proofs. 6 models, 3 prompt types, 14,400 calls.
- Claimed property: contradictions are "localized rather than causing logical explosion". Shown only in the medication KB demo: 92 gluts, theory satisfiable. No gold-standard accuracy for that demo; one judge (GPT-4o).
- Other near uses: Salla et al. (commitment store + solver), MOSAIC (memory conflicts), XoT (candidates plus source-tied explanations), KCR (a26: separate reasoning traces per conflicting context; a 7B model beats GPT-4o and GPT-5.1 on adjudication; RL-trained; no metrics in the abstract).
- Search status: arXiv, OpenAlex and Semantic Scholar returned HTTP 429 during search. "Zero hits" is weak evidence. Redo before claiming a research gap (critique GAP 7).

### 6.4 Why to handle these results with care
- Models span 2024-2026; many results come from small open models.
- Several papers use an LLM judge. Judge error enters the numbers.
- None of the studies compares keep, retract and halt on downstream problem solving.

## 7. What our agent should take

Schema fit: S6 is fired by code (no pass, two rounds with no change, same error twice, budget fraction spent). Relevant guardrails: G1 (doubt only on a signal), G2 (revise only from real output), G3 (pass on something not fitted to), G4 (samples not independent), G5 (code selects), G6 (never abstain on the first pass), G7 (pay for itself at equal tokens), G9 (no debate), G10 (reasoning text is not evidence), G11 (think briefly).

Conflict with G6: Allen's gain comes from abstaining on gluts. Our agent must not abstain on the first pass. So a glut is a trigger to check, not a trigger to give no answer.

### Add now (established)

1. **Conflict register: a code-triggered, mandatory one-line question at S6 entry** ("do any two of these claims or candidates conflict? name them"). Part: S6 / G. Status [E]. Evidence: a19, a21, c09, d07, d13, b19, c10 (K15, K19, K28). Unprompted models almost never report conflicts (2.1-40.5%); a forced check raises reporting to 67.7-77.9% and in reasoning models lowers tokens. It must be a structured slot read by code (G10), not mined from free-form reasoning (d14).
2. **Never silent-pick; record both sides of a conflict** (for, against) in memory instead of overwriting. Part: memory / S6. Status [E] for the failure (24-38% chance resolution, d07) and for the data structure being cheap (K02: a07, c05). Whether it pays off is not established (see Test first, T1).
3. **An explicit self-consistency pass over the agent's own trace at S6 entry** (code asks the model to list claims in the trace that contradict each other, quoting the lines). Part: S6. Status [E] that self-contradiction detection is the weak point (K18, K27: accuracy 0.006-0.456, GPT-4 recall 8.0%) and that precision is high, so flagged items are usually real. Evidence: b17, d03, d05, a24.
4. **Evidence localisation before the verdict**: the check must quote the two conflicting lines so that code can verify them (G2). GPT-4 found the evidence in its top 5 in 70.2% of cases (b17). Part: S6 / G2. Status [E] for the difficulty; the quoting rule is a design choice.
5. **Randomise or double-run order in any adjudication between two sources.** Part: G / S6. Status [E] (K26: flips 11.4-25.2%, mean 18.6%; also b22). A flip is itself a conflict signal.
6. **Use a model's glut or confidence only as a trigger for external verification, never as a verdict.** Part: G5 / G10. Evidence: d02 (raw confidence gain -1.2 to -2.1 points), d12. Status: [E] that confidence is a poor stop signal (already in the schema section 4b); the conflict-aware score is [S].

### Test first (not established)

| # | Candidate | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Keep a flagged (for, against) record and continue, vs retract-on-conflict vs halt, on injected contradictions | S6 / memory | [S] | d09, d07, b25 |
| T2 | Bilateral verify-and-refute judge vs unilateral judge with matched coverage and tokens | S6 / O | [S] confounded | a14, c02, c03, d11 |
| T3 | Dependency-tracked retraction vs full re-solve after a late contradiction | S6 / O | [S] | a04, c15, c18, d10 |
| T4 | Consistency flag (da Costa): classical inference only on code-verified facts | S6 / G | [S] no empirical source | a03, d19 |
| T5 | Core-guided minimal repair vs self-consistency at equal tokens | S6 / O | [S] | c15, c16 |
| T6 | Conflict-type step (explicit / implicit / self / cross-source) | S6 | [S] | c12, c11 |
| T7 | Conflict score as trigger for tool verification | S6 / G | [S] | d02, d12 |
| T8 | Keep-both-then-adjudicate (XoT-style) | S6 / memory | [S] | d09 |
| T9 | Save-time conflict check on memory writes | memory | [S] | a25 |
| T10 | Do not add a rigid classical logic checker; test a flag-only checker on defeasible items | S6 / G | [S] | c06-c08 |

Item T10 is a caution, not an established rule (single source, K23). It matches the spirit of G5 and G10.

## 8. Concrete tests on our bench

All tests: both arms get the same total token budget (G7). Count setup cost. Randomise premise order. Report accuracy on all items (not only answered), plus coverage, plus tokens.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T0 Conflict register | Multi-step items with one injected contradiction (explicit, implicit, self-contradiction in trace) | A: plain S6. B: S6 plus forced one-line conflict register | Conflict report rate; final accuracy; tokens | Report rate +40 to +55 points; tokens not up for reasoning models; accuracy gain small but positive (no direct accuracy data) |
| T1 Keep vs retract vs halt | Same items, plus a late contradiction injected after a partial solution | A: keep flagged (for, against) and continue on independent sub-goals. B: retract the conflicting premise by code and continue. C: halt and flag. D: plain model | Accuracy on questions that do not depend on the conflict; accuracy on dependent questions; wrong-answer rate | Keep >= retract on independent sub-questions; keep wins when the retracted side was the true one. No prior data |
| T2 Bilateral vs matched unilateral | 400+ factual claims, balanced correct and wrong | A: bilateral. B: unilateral with confidence-based abstention matched to A's coverage. C: unilateral with 2x self-consistency votes at A's token cost | Macro-F1 on answered items at equal coverage; tokens | If the bilateral gain is only selection, B and C match A. Credit the structure only if A beats both |
| T3 Dependency retraction vs re-solve | Premise sets with edits: support removal, defeating fact, support insertion (DeltaLogic style), N >= 100 per edit type | A: lines carry deps; only dependent lines retracted. B: full re-solve. C: no revision | Accuracy after edit; belief inertia; tokens | A cheaper than B at similar accuracy; both beat C on support-removal and defeating edits |
| T4 Consistency flag | Verified facts plus unverified claims, one injected contradiction | A: classical rules only on flagged facts. B: unrestricted | Error spread: wrong answers on questions touching only unrelated verified facts | A has less spread; size unknown |
| T5 Order flips | Pairs of contradictory sources, both orders | A: single order. B: both orders, flip = conflict signal, route to check | Accuracy; flips caught | B recovers part of the 11-25% flip loss at about 2x adjudication cost |
| T6 Conflict type | Items labelled explicit / implicit | A: plain register. B: register plus type step | Report rate by type; tokens | Oracle type +24 points, pipeline +9; test whether the cost is worth it |
| T7 Trigger calibration | Claims with known truth, per model | A: fixed glut threshold. B: per-model calibrated conflict score | Precision of the trigger for real errors | Calibrated beats fixed |
| T8 XoT list-then-decide | Conflicting source pairs | A: direct. B: list candidates plus source-tied explanations, then decide. C: conflict-aware prompt | F1; tokens | B > A, C if the +20% relative holds at equal tokens |
| T9 Memory write check | Long dialogues with injected fact changes | A: append only. B: save-time check with flag. C: save-time check with retraction | Conflicts detected; QA accuracy | B or C near MOSAIC's 66% vs 14% detection |
| T10 Defeasible items | Rulebreaker-style items | A: model alone. B: model plus flag-only checker. C: model plus classical checker | Paired accuracy | C hurts (as Logic-LM did), B does not |

## 9. What does not transfer, and why

- **Dialetheism and true contradictions.** The agent works on problems with a fixed answer. Treating A and not-A as both true is not a goal. Paraconsistency is used only as containment.
- **Human borderline-contradiction data (K05-K08).** It concerns vague predicates like "tall". It says nothing about task performance. The rates (7% to 66%) vary with wording. A pragmatic reading explains them without any contradiction being believed.
- **Fine-tuning fixes (Bao, KCR).** Our agent is a scaffold, not trained. Halting at 1.000 is a synthetic result, and halting is not our goal at S6 (G6 forbids abstaining on the first pass).
- **The bilateral coverage trade.** Allen's gain is bought by abstention. We can use a glut only as a trigger for checks.
- **Formal completeness results.** Soundness and completeness of the tableau hold for a logical system, not for how well a language model plays the interpreter. The LLM glut rate shifts with family and topic.
- **Heavy solver pipelines.** Cross-query SAT/SMT repair assumes claims can be extracted as logical commitments. For open tasks (ARC, brain-teasers) that is costly, and plain self-consistency gets most of the gain.
- **Debate.** Keeping both sides must not turn into agents arguing (G9). The record is data, adjudicated by code or a blind check, not a dialogue.
- **LP's weakened modus ponens as a whole logic.** It would cripple ordinary derivations. We take only the idea: do not chain from a BOTH claim without a check.
- **Reasoning traces as evidence.** The "notice but not report" traces are a hint, not proof (G10).

## 10. Open questions

1. At equal tokens, does keeping a flagged contradictory set beat retraction and halting on downstream problem solving? No study (critique GAP 1).
2. Does bilateral judging beat a unilateral judge matched on coverage and tokens (GAP 2)?
3. Does a da Costa consistency flag limit error spread (GAP 5)? No source found.
4. Does dependency-tracked retraction beat full re-solve (GAP 6)? DeltaLogic tested only tiny models, N = 20-30, with no retraction method.
5. Are there LLM papers on LP, FDE, LFI or Belnap scaffolds that the rate-limited search missed (GAP 7)?
6. Do logic checkers hurt on defeasible items in general, and does a paraconsistent checker avoid the harm (GAP 10)?
7. Does a glut predict wrong answers? d12 reports rates only.
8. Why do reasoning models deliberate on a conflict and then drop one side silently (a22)? Does a forced conflict line fix it at no extra cost?
9. Do results hold for current frontier models? Most conflict benchmarks used 2024-era or small open models.
10. Is there an LLM analogue of the human order and adjective effects on glut acceptance?
11. How often does an impasse involve a real contradiction? The schema notes impasse may be only about 8% of problems, which caps the gain.

## 11. Sources

[V] opened (full text or page read in the search phase). [M] snippet only.

**Formal background**
- [V] SEP Paraconsistent Logic (Priest, Berto, Weber) https://plato.stanford.edu/entries/logic-paraconsistent/ (a01-a05)
- [V] SEP Dialetheism https://plato.stanford.edu/entries/dialetheism/ (a06)
- [V] Jakl (2025) Four imprints of Belnap's useful four-valued logic https://arxiv.org/pdf/2503.20679 (a07)
- [M] Belnap (1977) A useful four-valued logic https://link.springer.com/chapter/10.1007/978-94-010-1161-7_2 (a08, c20)
- [M] Priest (1979) The Logic of Paradox https://doi.org/10.1007/BF00258428 (a09, c19)
- [M] da Costa (1974) On the theory of inconsistent formal systems https://doi.org/10.1305/ndjfl/1093891487 (c21)
- [V] Ongaratto and van Ditmarsch (2026) The Dynamic Turn in Paraconsistency https://arxiv.org/abs/2607.19906 (a27)
- [V] Bienvenu, Bourgaux, Kozhemiachenko (2024) Queries with exact truth values https://arxiv.org/pdf/2408.07283 (c14)
- [M] Gao, Fodor, Kifer (2016) Paraconsistency and Word Puzzles https://arxiv.org/abs/1608.01338 (a29)
- [M] Maluszynski and Szalas, 4QL, IJCAI 2015 https://www.ijcai.org/Abstract/15/015 (c23)
- [M] Arieli and Avron (1996) four-valued approach for recovering consistent information (c24)

**Human studies**
- [V] Alxatib and Pelletier (2011) The psychology of vagueness https://sites.ualberta.ca/~francisp/Phil428.526/AlxatibPellVagueness2011Published.pdf (a10-a12, b01-b03)
- [V] Egre, Zehr et al. (2018 chapter) Are gaps preferred to gluts? https://hal.science/hal-03917664/document (b04-b07, b24)
- [V] Cobreros, Egre, Ripley, van Rooij (2015) Pragmatic interpretations of vague expressions https://pure.uva.nl/ws/files/10080016/Pragmatic_interpretation_of_vague_expressions.pdf (b08, b09)
- [M] Follow-ups on borderline contradictions (Ripley 2011 and others) https://isidore.science/document/10670/1.y1xk8d (a13)

**LLM and AI studies**
- [V] Allen, Chhikara, Ferguson, Ilievski, Groth (2025) Sound and Complete Neurosymbolic Reasoning with LLM-Grounded Interpretations https://arxiv.org/abs/2507.09751 ; journal version https://neurosymbolic-ai-journal.com/system/files/nai-paper-932_0.pdf (a14-a18, b10-b13, b25, c01-c05, d11, d12)
- [V] Bao, Fu, Witbrock (2025-26) Conflict-Aware Fusion https://arxiv.org/abs/2512.06393 (b14-b16)
- [V] Li, Raheja, Kumar (2024) ContraDoc https://arxiv.org/abs/2311.09182 (b17, b18)
- [V] Hou et al. (2024) WikiContradict https://arxiv.org/abs/2406.13805 (a19, a20, c11)
- [V] Li, Li, Chang, Wu (2025) Premise Critique Bench https://arxiv.org/abs/2505.23715 (a21, a22, b20, b21, c09, c10, d13)
- [V] Fan, Li, Sun, Zhou (2025) Missing premise exacerbates overthinking https://arxiv.org/abs/2504.06514 (b19)
- [V] Chan, Gaizauskas, Zhao (2025) Rulebreakers https://arxiv.org/pdf/2410.16502 (c06-c08)
- [V] Liu et al. (2024) Self-Contra https://arxiv.org/abs/2311.09603 (a23, a24)
- [V] Chen, Chi, Wang, Zhou (2024) Premise order matters https://arxiv.org/abs/2402.08939 (b22)
- [V] Cheng (2025) position paper on relevant logic for LLMs https://arxiv.org/abs/2508.10265 (b23; no experiments)
- [V] Cattan et al. (2025) DRAGged into CONFLICTS https://arxiv.org/pdf/2506.08500 (c12)
- [V] MAGIC (2025) https://arxiv.org/pdf/2507.21544 (c13)
- [V] Salla, Amancherla, Saravanan (2026) Cross-query contradictions https://arxiv.org/pdf/2604.14525 (c15, c16)
- [V] Nguyen et al. (2026) BIS Reasoning 1.0 https://arxiv.org/pdf/2506.06955 (c17)
- [V] Dhanda (2026) DeltaLogic https://arxiv.org/pdf/2604.02733 (c18, d10)
- [V] Han, Lan, Kilicoglu (2026) When Evidence Conflicts https://arxiv.org/abs/2605.14115 (d01, d02)
- [V] Gokul, Tenneti, Nakkiran (2025) Contradiction Detection in RAG Systems https://arxiv.org/abs/2504.00180 (d03, d04)
- [V] Cheng Jiayang et al. (2024) ECon https://arxiv.org/abs/2410.04068 (d05-d07)
- [V] Zhao et al. (2026) ConflictQA / XoT https://arxiv.org/abs/2604.11209 (d08, d09)
- [V] Jeripity Venkata (2026) Do models know why they changed their mind? https://arxiv.org/abs/2605.27773 (d14)
- [V] Zhao et al. (2026) MOSAIC https://arxiv.org/abs/2607.16211 (a25)
- [V] Zheng et al. (2025) KCR https://arxiv.org/abs/2508.01273 (a26; abstract only)
- [V] arXiv scan for "paraconsistent" https://arxiv.org/search/?query=paraconsistent&searchtype=all&order=-announced_date_first (a28)
- [M] CounterLogic https://arxiv.org/abs/2505.22318 (a30)
- [M] Pan et al. (2023) Logic-LM https://arxiv.org/abs/2305.12295 (c22)
- [M] Wei et al. (2022) CoT and Wang et al. (2022) self-consistency https://arxiv.org/abs/2201.11903 (c25; numbers via c15)
- [M] AGM-Bench, ReviseQA, LogicVault (78% figure, snippet only; do not cite) https://www.iclr.cc/virtual/2026/10017503 (c26)
- [M] Su et al. (2024) ConflictBank https://arxiv.org/abs/2408.12076 (d17)
- [M] Yuksel et al. (2026) thinking-token vs stated-output acknowledgment (d15, second-hand)
- Syntheses, not sources: c27, d16, d18, d19.

Priest 1979, Belnap 1977 and da Costa 1974 were not opened as originals; formal claims rest on the SEP and Jakl 2025.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 8 established claims: 4 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D03.06-K02** (reworded: the sources support less). LP 'both' value and Belnap's four values are real, and Allen et al. use a bilateral (verify/refute) record, but no source calls this cheap: Allen et al. report macro-F1 +0.062 at a coverage cost of -0.456, and a14/b10 are the same paper. Corrected claim: LP-style 'both' (glut) values and Belnap's four values let a record keep evidence for and against a claim separately instead of a single truth value; in Allen et al. (2025) a bilateral verify/refute judge raised macro-F1 by about 0.06 but lowered coverage by about 0.46, so it is not free.
- **D03.06-K07** (reworded: the sources support less). 53.7% (22 of 41) verified in Alxatib and Pelletier, but that means about half, not that gap and glut answers come from the same people; the Egre et al. 37% figure could not be opened (HAL blocked; abstract found says 'neither' is preferred to 'and', i.e. gaps over gluts); a11 and b02 are one paper. Corrected claim: In Alxatib and Pelletier (2011), 53.7% (22 of 41) of those who judged 'neither tall nor not tall' true of the 5'11 man also judged 'tall and not tall' true, so gap and glut answers often come from the same people; Egre et al. report that 'neither' descriptions are nonetheless preferred to 'and' descriptions.
- **D03.06-K26** (reworded: the sources support less). Han et al. numbers (11.4-25.2%, mean 18.6%, gap 11.1, 920 per model, six 4B-14B models) verified; but the ECon '0.4-2.8 F1' comes only from the first dataset column of Table 16 and 2.8 is Mixtral, not a strong LLM (strong models there move 0.4-1.8); other columns of the table show drops of about 3-6 points. Corrected claim: LLM conflict adjudication is order sensitive: reversing two contradictory documents flips the answer for 11.4-25.2% of items (mean 18.6%, accuracy gap 11.1 points, 920 paired predictions per model, six 4B-14B open models). Conflict detection in ECon changes less on the first dataset (about 0.4-1.8 F1 points for Claude 3 Sonnet, Llama-3 70B, GPT-4 and Llama-3 8B), but the paper says most detectors are order sensitive and larger drops appear in other columns of its Table 16.
- **D03.06-K28** (reworded: the sources support less). ECon 24%/38% chance and PCBench R1/o3-mini token numbers and 4.0-40.5% unprompted range are correct, but instructed critique rates across PCBench models range 53.5-77.9%, not 67.7-77.9% (e.g. Qwen3-8B-thinking 57.2, Llama-4/others 53.5-61.8). Corrected claim: Unprompted LLMs often silently choose a side in conflicts (ECon: 24% of Sonnet and 38% of Haiku responses resolve by chance; PCBench unprompted premise critique 4.0-40.5%). An explicit premise-check instruction raises reporting to 53.5-77.9% across PCBench models (R1 67.7%, Gemini-2.0-flash-thinking 77.9%) and for some reasoning models cuts tokens (R1 2590 to 1014; o3-mini 1279 to 1023 on the easy set).
- **D03.06-K01** (now single-source: only one opened source, code check).
- **D03.06-K06** (now single-source: only one opened source, code check).
