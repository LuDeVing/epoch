# Modal and epistemic logic: deep document

Subfield D03.05. Focus: necessity, knowledge, belief. Key works: Kripke (1963), Hintikka (1962). Why it matters for our agent: background, plus a set of LLM belief-tracking results that bear on guardrails and memory.
Evidence: evidence_a-d.jsonl (a01-a27, b01-b29, c01-c27, d01-d21), claims.jsonl (K01-K33), critique.md (cross-check of 2026-11-19).

Read this first: nearly all LLM evidence here is from 2023 to mid-2024 models (GPT-4 class). Current reasoning models are barely measured. Every LLM claim is single-paper unless marked otherwise. Gettier and knowledge-luck sources were never opened (no numbers).

## 1. What it is

Modal logic adds "it is necessary that" (box) and "it is possible that" (diamond) to ordinary logic. Epistemic logic reads box as "agent a knows that" (K_a) or "a believes that" (B_a). Dynamic epistemic logic (DEL) adds events (announcements, private messages) that change what agents know.

Three layers matter for us:

1. **Formal core.** Possible-worlds semantics. An agent knows p if p is true in all worlds the agent cannot rule out. Settled and not empirical. [a01, a02, a06] (K01, established).
2. **Group and dynamic extensions.** Distributed knowledge, common knowledge, public announcements, action models. Puzzles: muddy children, coordinated attack. [a05, a08, a09, a12-a17] (K04, K05 established).
3. **Machine tests.** Benchmarks that ask LLMs the same kinds of questions: who knows what, who believes what, what follows from a modal premise. These are the only part with measured results for our agent. They overlap with theory of mind (ToM) work. This file covers the logic side and the belief-tracking tasks; clinical ToM is outside scope.

Links to other subfields in this run (not covered here): Autoformalisation, Argumentation and defeasible rules, Imprecise credences, Beliefs and affect, Simulation vs theory accounts, Evidence and probability reasoning.

## 2. History and theories in depth

**Kripke (1963) and Hintikka (1962).** Kripke gave relational semantics for modal logics: a model is M = (W, R, V), with W a non-empty set of worlds, R an accessibility relation, V a valuation. Box p holds at w iff p holds at every w' with wRw'. Hintikka applied this to knowledge and belief: w R_a w' means w' is compatible with what a knows at w. K_a p is true at w iff p holds at all such w'. [a01, a02, a06]

**Frame conditions link axioms to properties.** T (knowledge implies truth) = reflexive. 4 (positive introspection) = transitive. 5 (negative introspection) = Euclidean. B = symmetric. D (consistency) = serial. S5 = equivalence relation, usually used for knowledge. KD45 = serial, transitive, Euclidean, usually used for belief. Completeness results exist for K, K4, KD, KD4, KC4, KDC4, S5, GL. [a02, a06, a07]

**Disputes over which logic.** Hintikka accepted axiom 4 on an autoepistemic argument but argued against 5. Williamson (2000, ch. 5) rejects 4 using a margin-of-error argument. Others proposed S4.4 (von Kutschera 1976), S4.2 (Lenzen 1978), S4.3 (van der Hoek 1993). No logic is agreed. (K02, contested.) [a03]

**Logical omniscience.** Standard epistemic logic makes agents know all logical consequences. Hintikka himself said this fails for real agents. Critics: Chisholm 1963, Hocutt 1972, Jago 2007. So the formal systems are a specification of idealised information, not a model of how people or LLMs reason. (K03.) [a04]

**Group knowledge.** Distributed knowledge uses the intersection of the agents' relations. Common knowledge uses the reflexive-transitive closure of their union. Early work: Lewis 1969 (conventions), Aumann 1976 (agreeing to disagree), Lehmann 1984, Halpern and Moses 1984. [a05, a12]

**Halpern and Moses (1990).** In a system with unreliable message delivery, common knowledge cannot be reached by finite message passing. The coordinated attack problem is the standard case. Rubinstein's e-mail game is the economic version. [a14, a15, a17] (K04.)

**Muddy children.** With k muddy children and a public announcement "at least one is muddy", nobody moves for k-1 rounds of "I don't know", and all muddy children know at round k. The announcement adds information even when everyone already sees a muddy child (for k>=2) because it makes the fact common knowledge, restoring the nested level that was missing. [a13, a16] (K05.)

**Dynamic epistemic logic.** Public announcement logic (PAL) updates a model by deleting worlds where the announcement is false. Reduction axioms rewrite every announcement formula into plain epistemic logic. Action models handle private and partly observed events. Complexity: single-agent satisfiability NP-complete, model checking in P for fixed formulas, iterated announcement logic not recursively axiomatizable. [a08, a09, a10] (K06.) Belief change links to AGM-style revision via plausibility orders. [a11]

**Fitch's paradox (1963).** If every truth is knowable, every truth is known. Several fixes (restricting the knowability principle), none agreed. [a18] (K07, contested.)

**Lay epistemology.** Gettier cases and knowledge-luck have been tested cross-culturally (Machery et al., Noûs 51(3), 2017; Seyedsayamdost; Turri, Buckwalter, Blouw; Nagel, San Juan, Mar 2013; Starmans and Friedman 2012). Only metadata or abstracts were read. We have no numbers and no verified replication story. [b23-b27, d21] (K23.)

**Developmental link.** Syntactic recursion helps second-order belief judgments in children: N=89 Turkish-speaking children, correct 46% and 56% (ages 4;6-6;5) vs 69% and 85% (6;7-8;10), B=1.29, p=.002. Correlational, ceiling in older group. [b22] (K22.)

## 3. Core findings with exact numbers

Status: E established (two or more independent sources, or theory), S single source, C contested. Models are old unless stated.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Possible-worlds semantics is the standard base; S5 for knowledge, KD45 for belief | Frame conditions T reflexive, 4 transitive, 5 Euclidean, D serial | SEP entries [a01-a07] | E |
| Axioms 4 and 5 are disputed for knowledge | Hintikka accepts 4 not 5; Williamson rejects 4 | SEP [a03] | C |
| Common knowledge unreachable by finite messages | Coordinated attack | Halpern and Moses 1990 [a15, a17] | E |
| Muddy children: k muddy, act at round k | Needs public announcement | SEP, Halpern and Moses [a13, a16] | E |
| PAL complexity | Model checking P; single-agent SAT NP-complete; iterated PAL not r.e. axiomatizable | SEP DEL [a10] | S |
| LLMs on uncontroversial modal and conditional patterns | Llama 3.1 405B 89.50; GPT-4 Turbo (Apr) 87.17; Claude 3.5 Sonnet 85.33; GPT-4o mini 75.33; weakest of 29 models 45.33; chance 50; 20 instances per pattern | Holliday et al. 2024 [b01, c06] | S |
| Zero-shot CoT gain on modal patterns | Llama 405B +1.00; Sonnet +2.33; GPT-4 Turbo +4.33; GPT-4o mini +13.50 (up to +21.5); few-shot deltas -8.0 to +12.5 | Holliday et al. [b02, a23] | S |
| Modal skill tracks general benchmarks | r = 0.81 LMSYS Elo, 0.85 MMLU, 0.75 GSM8K, all p<0.01 | Holliday et al. [b01] | S |
| McGee-style modus ponens: top models judge it valid; related triads answered inconsistently | Qualitative; same context window | Holliday et al. [b03-b05, c07] | S |
| KaBLE: true vs false statement verification | 85.7 vs 74.5 average; 13 tasks, 13,000 questions, 1,000 seeds, 195,000 queries | Suzgun et al. 2024 [a24, b07, c01] | S |
| KaBLE: first-person false belief confirmation | Average 54.4 vs 92.1 for true belief. GPT-4o 98.2 to 64.4; GPT-4 93.4 to 22.0 (task mapping of the last two rows uncertain after PDF misalignment) | Suzgun et al. [a24, b08] | S |
| KaBLE: recursive knowledge | Verification 78.4, awareness 77.5; Claude 3.5 Sonnet 35.8 on recursive verification | Suzgun et al. [a26, c02] | S |
| KaBLE: CoT can lower accuracy | GPT-4o direct fact verification -6, first-person belief -4; a distractor sentence raised false-case accuracy 11.7 points | Suzgun et al. [a25, b10] | C |
| Hi-ToM order collapse | All four LLMs under 60; GPT-4 58.11 overall; joint accuracy about 0.95 at order 0 to about 0.05-0.16 at order 4; CoT no gain under deception (55.81 vs 55.72) | He et al. 2023 [b14, c10, c11] | S |
| Format dependence of order collapse | GPT-4 73-95% on orders 3-6 true/false statements, N=112 per order | Street et al. 2024 [d12] | S |
| Kosinski false-belief | GPT-4 75% of 40 tasks, CI 66-84; compared to 6-year-olds | Kosinski 2023 [b11, c16] | C |
| Trivial alterations break it | Transparent bag: model still gives P=95% chocolate belief (other cases 98%, 94%) | Ullman 2023 [b12, c15] | S |
| Stress tests | ToMi GPT-3.5 81 overall but 46 on false-belief; FauxPas-EAI best 27%; 97.5 and 83.3 in other conditions | Shapira et al. 2023 [b13, c17] | S |
| FANToM | Human 87.5 vs GPT-4 CoT 26.6 (June) and 14.8 (Oct) ALL score; 53.7 on a looser measure | Kim et al. 2023 [b15, c12] | E (with ToMBench) |
| ToMBench | Humans 85.4 vs GPT-4-1106 75.3; LLMs drop 20+ points on coherent tests vs 13.6 for humans | Chen et al. 2024 [b19, c21] | E |
| Response bias in human-LLM comparison | LLaMA2-70B beat humans on faux pas only by always answering "did not know"; GPT-4 said speaker knew in 2 of 349 responses; ExploreToM 22% yes vs 4% no | Strachan 2024 [b16, b17, c18]; Lu 2025 [d10] | S |
| Templated benchmarks reward training on the template | 0.5B-7B models with RL or SFT beat GPT-4o (69.00) and DeepSeek-V3 (70.17) on Hi-ToM, 84.5 to 86.5 for 7B | Lu et al. 2025 [d10, d11]; Riemer 2025 [d15]; Hu et al. 2025 [d16] | E |
| SymbolicToM tracker | +38 points for GPT-3 davinci on ToMi (to 92%); +62 first-order and +78 second-order false-belief points on other models; supervised baselines lose about 54 points under paraphrase | Sclar et al. 2023 [c13, c14] | S |
| ThoughtTracing | GPT-4o+TT 76.0 vs o1-high 73.0 and R1 68.3 on ParaphrasedToMi, at lower token cost | Kim et al. 2025 [d03, d05] | S |
| Perspective filtering (SimToM) | +16 to +47 on ToMi false belief, 2023 models | Wilf et al. 2023 [d13] | S |
| Reasoning models over-assume hidden info | o1-preview and o3-mini 90-100% on false-belief but 28-49% on easy true-belief items | Kim et al. [d04] | S |
| SimpleToM explicit vs applied | Mental-state accuracy 95-99%; behaviour prediction 49-84%; behaviour judgment 15-66% (o1 32.5, GPT-5 40.0, o3-mini 41.3, R1 65.8, o1-preview 59.5) | Gu et al. 2026 [d01] | S |
| Mental-state reminder | Behaviour prediction: Llama-405B 58.2 to 89.5; GPT-4o 49.5 to 82.8; Sonnet 67.0 to 96.9; generic CoT GPT-4o only 62.8; judgment gain small except Claude 24.9 to 84.1 | Gu et al. [d02] | S |
| DEL-based step verifier | Hi-ToM average: gpt-4o-mini 75.0 to 93.5 (N=4); gpt-4o 87.0 to 93.0; gpt-4.1 83.5 to 90.0; Qwen3-4B order 4 46.0 to 65.0; Qwen3-4B average 75.1 to 84.5 at N=1024 | Wu et al. 2025 [d06, d07] | S |
| Stipulated modal semantics | Four of five 2026 models 2.5-25.0% direct (below 50% baseline); Claude Sonnet 5 65.0; DeepSeek V4 Flash 4.4 to 88.1 with reasoning mode | Andrieu and Sileo 2026 [d08, d09] | S |
| History of beliefs | Trajectory questions 27.7% vs 44.7% standard false belief; update detection 67.5% | Nguyen et al. 2026 [d18] | S |
| MindGames (DEL puzzles) | Humans 94%; 400 test cases per setup; no clean scaling in GPT-3 family; helps 5-shot Pythia not 0-shot | Sileo and Lernould 2023 [a19, b18, c04] | S |
| Symbolic solver offload (Logic-LM) | +39.2 over standard, +18.4 over CoT on average; GPT-4 FOLIO 69.1/70.6/78.9, ProofWriter 52.7/68.1/79.7 (standard/CoT/Logic-LM); PrOntoQA CoT 98.8 beat Logic-LM 83.2 | Pan et al. 2023 [c22] | S |

## 4. Mechanisms and models

Each is described so it can be built in code.

**4.1 Kripke model as a data structure.**
- Worlds: a list of dicts mapping fact names to true or false.
- Relation per agent: a set of (w, w') pairs.
- Evaluate K_a p at w: all(p(w') for w' in R_a[w]).
- Everyone knows (E_G p): the check for all agents in G. Common knowledge: BFS over the union of relations; p must hold at every reachable world.
- For small puzzles (up to 5 agents, 2^5 worlds) this is trivial. Worlds grow as 2^n.

**4.2 Public announcement update.** Given announcement phi: delete all worlds where phi is false, restrict every relation to the survivors. Repeat per announcement. Muddy children: start with 2^k worlds, announce "at least one muddy", then each round announce "nobody knows", which removes worlds where some muddy child would have known. A child acts when its own status is fixed in all remaining accessible worlds. [a08, a13]

**4.3 Action model update (private events).** Events have preconditions. The product update creates (world, event) pairs. Agent a cannot distinguish pairs whose events a cannot tell apart. Use for "A leaves the room, B moves the object". [a09]

**4.4 Practical belief table (what the LLM-facing studies implement).** A per-agent record: for each agent, for each fact, the last observed value and the time. Nesting: belief[a][b][fact] for depth 2. Update rule: when an event is observed by agent set S, update belief[s] for s in S, and update nested entries for agents who know S saw it. SymbolicToM builds this graph per character pair and filters the story to what each character witnessed, then answers from the filtered story. [c13] SimToM does the same with a prompt (filter to what X saw, then answer). ThoughtTracing samples hypotheses about X's mental state and reweights them after each observation. [d13, d03]

**4.5 DEL verifier (DEL-ToM).** A simulator labels each step of a belief trace by whether the DEL model agrees. A process belief model is trained on 20k labelled Hi-ToM stories. At inference, sample N reasoning traces, score steps, choose the best. Gains need the trained verifier and many samples (N up to 1024 for small models). [d06, d07]

**4.6 Mental-state reminder.** Two calls. Call 1: "Does X know Y?" Call 2: the behaviour question, with the answer to call 1 restated. This lifted behaviour prediction about 30 points while generic CoT did less. [d02]

**4.7 Frame-condition checking for modal inference.** An inference is valid only if the conclusion holds in all models of the stipulated frame class. A countermodel search (build a tiny Kripke model where premises hold and conclusion fails) is the proof method for invalidity. Models often ignore stated frame conditions and fall back on default logics (K or T). [d08, d09]

**4.8 Offloading to a solver.** Translate to first-order or modal formulas, call a solver, return the result (Logic-LM). Translation errors are the failure point. [c22]

## 5. What holds up

**Holds up (two or more independent lines).**
- Standard theory: Kripke semantics, muddy children, coordinated attack (K01, K04, K05).
- Interaction-style belief tracking stays far below humans on harder benchmarks: FANToM and ToMBench agree (K20). Models tested are 2023-2024.
- Templated ToM scores are weak evidence: RL on templates beats GPT-4o, answer priors are imbalanced, literal ToM accuracy does not predict functional adaptation (K32, three sources).
- Emergent-ToM claims fail under perturbation: Kosinski's 75% (40 tasks) breaks under Ullman's alterations and Shapira's stress tests (K19, contested; the disagreement is about item difficulty, not data).

**Failures and contradictions.**
- Kosinski vs Ullman, Shapira, Hi-ToM, FANToM, ToMBench: narrow template vs perturbed items. Not a data conflict.
- Order collapse depends on format: Hi-ToM question answering under 60% overall vs Street 2024 true/false statements at 73-95% for orders 3-6 (K33).
- MindGames shows no clean scaling in the GPT-3 family while Kosinski reports gradual gain in the same family. Different tasks and prompts.
- Holliday: modal skill tracks general benchmarks (r about 0.8). KaBLE: large gaps between true and false belief within strong models. Different capabilities, so both can hold.

**Moderators.**
- Model strength: CoT helps weak models (+13.5 to +21.5) and barely helps strong ones (+1 to +4) on modal patterns. [b02]
- Item type: true-belief and no-asymmetry items are hard for reasoning models (28-49%) while false-belief items are easy (90-100%): a bias toward assuming hidden information. [d04]
- Perspective: first-person false belief (average 54.4; GPT-4 22.0 on the worst row) is harder than third-person. The 54.4 vs 80.7 contrast mixes task sets, so it is indicative only. [critique]
- Explicit vs applied: knowing what X knows (95-99%) does not carry to predicting X's behaviour (49-84%) or judging it (15-66%). [d01]
- Stipulated semantics: direct prompting ignores frame conditions; reasoning mode fixes it for one model (4.4 to 88.1). [d08]
- History: current belief is easier than the belief before an update. [d18]

**Interventions that worked (single-source each).**
- External per-character belief tracker (SymbolicToM): +38, +62, +78 points on ToMi, old models. [c13]
- Prompted perspective filtering (SimToM): +16 to +47 on ToMi false belief. [d13]
- Mental-state reminder: about +30 on behaviour prediction. [d02]
- ThoughtTracing: beats o1, o3-mini, R1 on ParaphrasedToMi at lower cost. [d03, d05]
- DEL-grounded verifier: 75.0 to 93.5 (gpt-4o-mini). [d06]
- Solver offload: +39.2 (Logic-LM). [c22]

**Interventions that did not work or hurt.**
- Plain CoT under deception on Hi-ToM: 55.81 vs 55.72. [c11]
- CoT on KaBLE: -6 and -4 for GPT-4o. [a25]
- Reasoning models on easy true-belief items: 28-49%. [d04]
- Reasoning-token count does not predict accuracy. [d04]
- Logic-LM on PrOntoQA: worse than CoT (83.2 vs 98.8). [c22]
- Supervised baselines under paraphrase: about -54 points. [c14]

**Caveats on the evidence base.**
- KaBLE's 92.1 and 85.7 figures each appear twice in the paper with different meanings, so the "I know marker vs none" contrast is unreliable and was dropped. [critique]
- Several tables came out misaligned from pdftotext; only text-verified numbers are used.
- DEL-ToM test sets are about 40 items per order and the Hi-ToM format is in-distribution for the verifier.
- Andrieu and Sileo 2026 is one preprint.
- Hi-ToM order 4 joint accuracy is about 0.05-0.16 (not "near zero"). [critique]

## 6. Language models

**Modal and conditional inference (Holliday et al., 29 models).** Strong models do well on clear patterns: 75-89% zero-shot against chance 50. The weakest model got 45.33. They over-accept some fallacies, accept McGee-style modus ponens uniformly, and answer related triads inconsistently within one context window. Accuracy correlates with MMLU (0.85) and Elo (0.81). CoT gives +1 to +4 for strong models, +13.5 for GPT-4o mini. [b01-b06]

**Epistemic verification (KaBLE, GPT-4 class).** Verification of true statements beats false (85.7 vs 74.5 average). First-person false belief is the worst case (average 54.4; GPT-4 down to 22.0). Recursive knowledge averages 78.4 and 77.5. CoT slightly lowers GPT-4o. KaBLE has only a v1 on arXiv with no reasoning models; no re-run on current models was found. [a24-a27, d20]

**Belief tracking in stories.**
- Old models: Hi-ToM under 60% overall, order 4 joint accuracy about 0.05-0.16. FANToM GPT-4 CoT 26.6 and 14.8 vs human 87.5. ToMBench GPT-4-1106 75.3 vs human 85.4.
- Perturbation: Ullman's transparent bag still gives 95% chocolate; Shapira ToMi GPT-3.5 81 overall vs 46 on false belief.
- Bias: LLaMA2-70B's "human-beating" faux-pas score came from always answering "did not know".
- Reasoning models (2025-26): false-belief items 90-100% but true-belief 28-49% (o1-preview, o3-mini). SimpleToM: mental-state questions 95-99% but behaviour judgment 32.5 (o1), 40.0 (GPT-5), 41.3 (o3-mini), 65.8 (R1). So the gap between knowing and using a belief remains, but is narrower than for GPT-4o. [d01, d04]
- Dynamics: trajectory questions 27.7% vs 44.7% standard. [d18]

**What changed performance, and by how much.**

| Change | Effect | Model class |
|---|---|---|
| Symbolic belief tracker | +38 to +78 points on ToMi | 2023 |
| Perspective filtering prompt | +16 to +47 | 2023 |
| Mental-state reminder | +30 behaviour prediction | GPT-4o, Llama 405B, Sonnet 3.5 |
| Hypothesis tracing | Beats o1, o3-mini, R1 on ParaphrasedToMi | 2025 |
| DEL verifier, trained | 75.0 to 93.5 (gpt-4o-mini) | 2025, needs training |
| Reasoning mode on stipulated semantics | 4.4 to 88.1 | 2026, one model |
| Generic CoT | -6 to +21.5; sign depends on model and task | mixed |
| RL on templated data | 7B beats GPT-4o on Hi-ToM | 2025, shortcut risk |

**MindGames.** GPT-3 family and Pythia: humans 94%, no emergent jump with scale. Not re-run on current models. [a19, b18]

**Epistemic structure as a model default.** When frame conditions are stipulated, four of five 2026 models scored 2.5-25.0% under direct prompting, below the 50% baseline. The authors note default logics (K or T). [d08, d09]

**Agents under information asymmetry.** Peng et al. 2026 uses an environment verifier (not DEL); numbers not read. No LLM epistemic-planning paper was found. [d19]

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrails, S states, O operators, memory.

### Add now (established)

1. **Do not hard-code an epistemic logic (S5 or other) into the scaffold.** The theory is contested (axioms 4, 5, omniscience) and the formal systems are specs, not models of LLM reasoning. Part: none (negative rule). [E for theory; C for axiom choice] ids a03, a04; K02, K03.
2. **Epistemic test hygiene for our own bench (G7 support).** Any in-house belief or ToM item set includes true-belief and no-asymmetry controls, balanced yes/no, and perturbed variants; report both classes. Reason: always-answer-no beat humans on faux pas, 22% yes vs 4% no priors, templates are trainable, reasoning models fail true-belief items. Part: G (bias and shortcut controls). [E] ids b16, b17, c18, d10, d11, d15, d16, d04; K21, K28, K32. K32 is established with three sources; K21 and K28 are single-source but consistent.
3. **Name the item format when reading a belief result.** Do not conclude "LLMs fail at order-k belief" without stating QA vs true/false. Part: none (reading rule). [S] ids d12, b14; K33. Cheap, so listed here, but it only changes how we read results.
4. **Common knowledge and muddy-children structure are background only.** No schema change. [E] a13, a16, a17.

Everything operational about LLM interventions is single-source and old, so it goes to Test first.

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Record the belief without endorsing it: write "user believes X; X may be false" before answering | G, memory | [S] | a24, d02; K13, K27 |
| T2 | Mental-state reminder: restate "what does X know" before predicting X's action | G, O | [S] | d01, d02; K26, K27 |
| T3 | Per-agent belief table (who observed what, dated, not overwritten) for multi-party items | S3, memory | [S] | c13, d13, d03, d18; K17, K31 |
| T4 | Nesting operator (explicit depth-k belief list) for orders 3-4 | O | [S] | b14, d06, d12; K16, K29 |
| T5 | Consistency check on related modal questions in one context | G | [S] | b03-b05; K10 |
| T6 | State frame conditions and require a countermodel check for knowledge or belief inference | G, O | [S] | d08, d09; K30 |
| T7 | No default CoT on belief items; compare with direct on true-belief controls | O, G11 | [C] | a25, d04, d08, c11; K14, K28 |
| T8 | Offload nested-belief or modal checks to a small program | O (formal tool) | [S] | c22, d06; K24, K29 |
| T9 | Perturbation check (transparent-bag style alteration) before trusting a belief answer | G3 | [C] | b12, b13; K19 |
| T10 | Spend no scaffold budget on a special modal-logic module | G7, G12 | [S] | b01; K11 |

T10: Holliday found modal skill tracks general ability (r 0.75-0.85), so a dedicated module has little to fix. Revisit only if our bench shows a gap.

## 8. Concrete tests on our bench

All arms at equal total tokens (setup counted, G7). Report both classes (true and false belief; belief and no-asymmetry).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| E1 (T1) | KaBLE-style first-person belief ("I believe p", p false), 100 per cell with matching true-belief items | plain; generic CoT; record-belief step | Accuracy on false belief and on true belief, separately | Gap closes by 10+ points on false belief with no loss on true. Current-model prior unknown. |
| E2 (T2) | SimpleToM-style behaviour prediction and judgment, 200 items | plain; generic CoT; mental-state reminder | Prediction accuracy; judgment accuracy | About +20 to +30 prediction for non-reasoning models (d02); smaller for reasoning models. |
| E3 (T3) | Hi-ToM orders 0-4 and FANToM-style stories | plain; CoT; belief table in code with LLM fill | Per-order accuracy; ALL score on FANToM | +10 or more at orders 3-4. SymbolicToM size (+38 to +78) not expected on current models. |
| E4 (T4) | Nested belief depth 1-4, balanced true/false statements | plain; explicit nesting list | Accuracy by depth | Gain grows with depth; flat at depth 1. |
| E5 (T5) | Triads (DSmu, DSmi, MiN style) and McGee-style modus ponens | plain; consistency-check step | Count of jointly inconsistent triples | Fewer inconsistent triples. |
| E6 (T6) | Stipulated-frame modal problems, balanced pairs | direct; frame conditions restated plus countermodel; reasoning mode | Accuracy vs 50% baseline | Direct below 50% for some models; check step reaches 80+ if d08 generalises. |
| E7 (T7) | Belief items with true-belief controls | direct; CoT; reasoning | True-belief and false-belief accuracy | CoT and reasoning lose 20+ points on true-belief controls (d04). |
| E8 (T8) | Muddy children k=2..5, public announcement puzzles | free text; world table updated in code; solver | Round of first correct answer; exact accuracy | Table beats free text at k>=4. |
| E9 (T9) | False-belief items with perturbations (transparent bag, informed protagonist) | plain; perturbation check step | Accuracy on altered vs original items | Check cuts altered-item failures. |
| E10 (T3) | Belief history: question about the belief before an update | overwrite memory; dated log | Trajectory accuracy | Dated log beats overwrite by 10+ points (d18 baseline 27.7%). |

## 9. What does not transfer, and why

- **Formal axiom choices (S5, KD45).** An LLM is not an ideal reasoner with logical omniscience; Hintikka said real agents fail it. No benefit from hard-coding.
- **Common knowledge and coordinated attack.** Our agent is a single agent with a program-controlled loop. G9 forbids multi-agent debate anyway.
- **Trained verifiers (DEL-ToM, Process Belief Model).** Need 20k labelled stories and N up to 1024 samples. Not cheap at our budget; test a prompted version only.
- **Benchmark scores on templated ToM sets.** In-distribution shortcuts; 7B RL models beat GPT-4o without human-like reasoning.
- **Developmental findings (Turkish children, recursion).** Human background, no agent implication.
- **Gettier and knowledge-luck folk epistemology.** Unverified. Relevant only if the agent must model how lay users use "know".
- **Fitch's paradox, Williamson's margin-of-error.** Philosophical; no agent test.
- **EpiK-Eval.** A training-format effect (unsegmented stories), not a scaffold-level lever. [c27]
- **Magnitudes from 2023 models.** SymbolicToM sizes (+38 to +78) and CoT figures come from models far weaker than what we run; do not carry the sizes over.

## 10. Open questions

1. How do current reasoning models score on KaBLE first-person false-belief tasks? The 54.4 and 22.0 figures may be obsolete.
2. Does a record-the-belief step close the first-person gap on KaBLE itself at equal tokens? (SimpleToM suggests yes on an adjacent task.)
3. Does a per-agent belief table still help at Hi-ToM orders 3-4 and FANToM at equal tokens? ThoughtTracing and DEL-ToM need extra machinery.
4. Why does CoT hurt on belief tasks? Over-reasoning on no-asymmetry items is suggested, not proven.
5. Do current models show McGee and triad inconsistency, and does a consistency step fix it? No paper found.
6. Do muddy-children and public-announcement puzzles at depth 4 or more work on current models? MindGames has not been re-run.
7. What are the real numbers and replication status in Gettier and knowledge-luck studies?
8. Is there an LLM epistemic-planning paper with measured gains? Only DEL-ToM is direct.
9. Do balanced-scoring controls change the ranking of current models on ToM benchmarks?
10. Why does format (QA vs true/false) change order collapse so much (under 60 vs 73-95)?
11. Does the reasoning-mode jump on stipulated semantics (4.4 to 88.1) replicate beyond one model and one 2026 preprint?

## 11. Sources

[V] opened, [M] snippet or abstract only.

- [V] Stanford Encyclopedia of Philosophy, Epistemic Logic: https://plato.stanford.edu/entries/logic-epistemic/ (a01-a05)
- [V] SEP Modal Logic: https://plato.stanford.edu/entries/logic-modal/ (a06, a07)
- [V] SEP Dynamic Epistemic Logic: https://plato.stanford.edu/entries/dynamic-epistemic/ (a08-a11)
- [V] SEP Common Knowledge: https://plato.stanford.edu/entries/common-knowledge/ (a12-a14)
- [V] SEP Fitch's Paradox of Knowability: https://plato.stanford.edu/entries/fitch-paradox/ (a18)
- [V] Halpern and Moses (1990), Knowledge and Common Knowledge in a Distributed Environment: https://arxiv.org/abs/cs/0006009 (a15-a17, c23)
- [V] Sileo and Lernould (2023), MindGames: https://arxiv.org/abs/2305.03353 (a19-a21, b18, c04, c05)
- [V] Holliday, Mandelkern, Zhang (2024), Conditional and Modal Reasoning in LLMs: https://arxiv.org/abs/2401.17169 (a22, a23, b01-b06, c06-c09)
- [V] Suzgun et al. (2024), Belief in the Machine (KaBLE): https://arxiv.org/abs/2410.21195 (a24-a27, b07-b10, c01, c02, d20)
- [M] KaBLE leaderboard: https://vinid-kable-leaderboard.hf.space/ (c03)
- [V] Kosinski (2023), Evaluating LLMs in theory of mind tasks: https://arxiv.org/abs/2302.02083 (b11, c16)
- [V] Ullman (2023), LLMs fail on trivial alterations: https://arxiv.org/abs/2302.08399 (b12, c15)
- [V] Shapira et al. (2023), Clever Hans or neural ToM: https://arxiv.org/abs/2305.14763 (b13, c17)
- [V] He et al. (2023), Hi-ToM: https://arxiv.org/abs/2310.16755 (b14, c10, c11)
- [V] Kim et al. (2023), FANToM: https://arxiv.org/abs/2310.15421 (b15, c12)
- [V] Strachan et al. (2024), Nature Human Behaviour: https://www.nature.com/articles/s41562-024-01882-z (b16, b17, c18; numbers not re-opened in the cross-check)
- [V] Chen et al. (2024), ToMBench: https://arxiv.org/abs/2402.15052 (b19, c21)
- [V] Gandhi et al. (2023), Understanding social reasoning in LMs: https://arxiv.org/abs/2306.15448 (b20, c19; numbers not re-opened)
- [M] Xu et al. (2024), OpenToM: https://arxiv.org/abs/2402.06044 (b21, c20)
- [V] Arslan, Hohenberger, Verbrugge (2017), PLoS ONE: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169510 (b22)
- [M] Machery et al., Gettier across cultures, Noûs 2017: https://doi.org/10.1111/nous.12110 (b23, d21)
- [M] Seyedsayamdost, epistemic intuitions: https://doi.org/10.2139/ssrn.2168530 (b24)
- [M] Turri, Buckwalter, Blouw, Knowledge and luck: https://doi.org/10.3758/s13423-014-0683-5 (b25)
- [M] Nagel, San Juan, Mar (2013), Cognition: https://doi.org/10.1016/j.cognition.2013.02.008 (b26)
- [M] Starmans and Friedman (2012), Cognition: https://doi.org/10.1016/j.cognition.2012.05.017 (b27)
- [V] Sclar et al. (2023), SymbolicToM: https://arxiv.org/abs/2306.00924 (c13, c14)
- [V] Pan et al. (2023), Logic-LM: https://arxiv.org/abs/2305.12295 (c22)
- [M] Moghaddam and Honey (2023): https://arxiv.org/abs/2304.11490 (c24)
- [M] Dissing and Bolander (2020), IJCAI: https://www.ijcai.org/proceedings/2020/ (c25)
- [M] Unverified 2026 probability-operator benchmark (not used): https://www.alphaxiv.org/abs/2607.27405 (c26)
- [V] EpiK-Eval (2023): https://arxiv.org/abs/2310.15372 (c27)
- [V] Gu et al. (2026), SimpleToM: https://arxiv.org/abs/2410.13648 (d01, d02)
- [V] Kim et al. (2025), ThoughtTracing: https://arxiv.org/abs/2502.11881 (d03-d05)
- [V] Wu et al. (2025), DEL-ToM: https://arxiv.org/abs/2505.17348 (d06, d07)
- [V] Andrieu and Sileo (2026), Same formulas, different semantics: https://arxiv.org/abs/2608.05097 (d08, d09)
- [V] Lu et al. (2025), Do ToM benchmarks need explicit human-like reasoning: https://arxiv.org/abs/2504.01698 (d10, d11)
- [V] Street et al. (2024), LLMs achieve adult human performance on higher-order ToM: https://arxiv.org/abs/2405.18870 (d12)
- [V] Wilf et al. (2023), Think twice (SimToM): https://arxiv.org/abs/2311.10227 (d13)
- [V] Xu et al. (2025), EnigmaToM: https://arxiv.org/abs/2503.03340 (d14)
- [V] Riemer et al. (2025), ToM benchmarks are broken: https://arxiv.org/abs/2412.19726 (d15)
- [V] Hu, Sosa, Ullman (2025), Re-evaluating ToM evaluation: https://arxiv.org/abs/2502.21098 (d16)
- [V] Nickel et al. (2026), Understanding artificial theory of mind: https://arxiv.org/abs/2602.22072 (d17)
- [V] Nguyen, Phan, Gonzalez (2026), Dynamic ToM as a temporal task: https://arxiv.org/abs/2603.14646 (d18)
- [V] Peng et al. (2026), Communication and verification in LLM agents: https://arxiv.org/abs/2510.25595 (d19; numbers not read)
