# Non-monotonic and default logic: deep document

*Subfield D03.04. Built from evidence_a-d.jsonl (a01-a28, b01-b30, c01-c31, d01-d18), claims.jsonl (K01-K25) and critique.md in this folder. Evidence ids in brackets. Status tags: [E] established, [S] single-source, [C] contested. Many 2026 sources are single-lab preprints; model names in them could not always be checked.*

## 1. What it is

Classical logic is monotonic. If a conclusion follows from some premises, it still follows when you add more premises. Everyday reasoning does not work that way. "Birds fly" and "Tweety is a bird" give "Tweety flies". Add "Tweety is a penguin" and the conclusion goes away.

Non-monotonic logic studies reasoning where a conclusion can be withdrawn when new facts arrive. It is also called defeasible or default reasoning. The key idea is a default: a rule that holds "normally" or "unless there is a reason to think otherwise". The list of possible exceptions is open-ended. McCarthy called this the qualification problem: a rule like "a boat crosses a river" has endless unstated exceptions (leaky boat, missing oars, a bridge, a helicopter) [a01].

Three questions define the field.
1. What counts as a default and how is it written (a rule with a justification, a minimised "abnormal" predicate, a normality order over worlds)?
2. When two defaults clash, what do we conclude (both, one, neither)?
3. What happens to old conclusions when a new fact arrives (stay, go, get weaker)?

Why it matters for our agent. The schema has a revise state (S5) and a guardrail "doubt only on a signal" (G1). Default logic is the formal home of that idea. A default holds until a concrete blocker appears. The agent should not hunt for blockers on a schedule. But the human and LLM data say two things at once. First, models are often too stubborn: they keep a conclusion after a defeater arrives. Second, pushing them to re-check makes them drop correct conclusions. The schema needs a rule that gets the first without paying the second. This document collects what is known about that trade-off.

Scope boundary. Belief revision (AGM), argument schemes, and structure mapping are covered by parallel subfields and are only linked here. Human reasoning with "usually" statements overlaps with heuristics and biases and with ecological rationality; only links.

## 2. History and theories in depth

### 2.1 Why the field exists

Classical first-order logic cannot state "birds normally fly" without listing every exception as a new axiom. The frame problem is the same issue in action reasoning. The common-sense law of inertia says nothing changes unless there is evidence; classical logic cannot say this without one axiom per exception [a13]. Around 1980 three groups proposed fixes.

### 2.2 McCarthy: circumscription (1980, 1986)

- Idea [a01, a02]. Circumscription is a rule of conjecture: assume that the only objects with a property are those the known facts force to have it. It is "jumping to conclusions" in a controlled way.
- Mechanism [a02]. Predicate circumscription is a second-order schema added to a first-order theory A. A minimally entails q if q is true in every model of A that is minimal in P. The paper proves every instance of the schema is true in all minimal models (soundness). Example: from "A, B, C are blocks", circumscription gives "only A, B, C are blocks".
- Worked example [a01]. Missionaries and Cannibals: state (331) to (000), 11 steps. A bridge is excluded until the problem statement mentions one.
- Abnormality predicate [a04]. McCarthy 1986 writes defaults as: "bird x and not ab(aspect1 x) implies flies x". Circumscribing ab gives "as few abnormal things as the facts force". Aspects (ab(aspect1 x), ab(aspect2 x)) let a thing be abnormal in one respect only, so a bird abnormal for flying is not abnormal for everything. Example: canary Tweety flies, ostrich Joe does not. Without cancellation axioms only a disjunction is derivable.
- Nixon diamond [a05]. Quakers are normally pacifists; Republicans normally are not. Systems that infer negation from non-provability give a contradiction. Circumscribing ab gives only "Nixon is abnormal in aspect1 or aspect2". That is suspended judgment, with no contradiction.
- Limits [a02, a04]. Minimal models do not always exist (Davis 1980). No general proof procedure. Choosing which predicates to vary is a modelling step: the wrong choice gives only disjunctions. McCarthy says he knows no fully satisfactory unique-names treatment.
- Extra uses [a04]. A communication convention (if a bird cannot fly and it matters, the speaker must say so). A cheap stand-in for probability when numbers are missing.

### 2.3 Reiter: default logic (1980)

Opened only through reviews (SEP, Wikipedia); the 1980 paper was not opened [a06, a15, c23].

- A default theory is a pair (Gamma facts, Delta defaults) [a06].
- A default (gamma : theta)/tau reads: if gamma is known and theta is consistent with what is believed, conclude tau.
- An extension is a fixed point: Xi_0 = Gamma; Xi_{i+1} = Cn(Xi_i) plus tau for each default whose prerequisite is in Xi_i and whose justification is consistent with the final extension [a06].
- Normal defaults have justification equal to conclusion; normal theories always have an extension. General theories may have none [a06, a15].
- Conflicting defaults give several extensions. Nixon: two extensions (pacifist; not pacifist) [a07].
- Credulous reasoning accepts what holds in any extension. Skeptical reasoning accepts only what holds in all [a07]. Floating conclusions (two branches both imply "Nixon is political") split skeptical systems [a07].
- No built-in priority among defaults. Poole (1985) added specificity; Horty (2007) orders defaults by a strict partial order [a10].
- Pollock's point [a12]. Reiter-style logic cannot represent undercutting defeaters (a reason to doubt the link in this case, as opposed to a reason for the opposite conclusion). This matters for an agent: "this instrument is miscalibrated" undercuts; it is not a rebuttal.
- Complexity (propositional, from Wikipedia; attribution to Gottlob 1992 not verified) [a15]. Extension existence Sigma2P-complete. Skeptical entailment Pi2P-complete. Credulous entailment Sigma2P-complete. Consistency checks are not computable in general for first-order.

### 2.4 Moore and Lifschitz: autoepistemic logic and answer sets

- Moore's autoepistemic logic: a default means "unless I know otherwise". Extensions are stable expansions. The belief operator is indexical [a11].
- Gelfond and Lifschitz (1988) showed stable-model semantics of logic programs with "not" matches autoepistemic reasoning: "phi1,...,phin, not psi" maps to "phi1 & ... & phin & not-B psi implies phi" [a11].
- Stable-model recipe [a17]. Guess a set S; delete rules blocked by S; delete "not" from the rest; check S is the least model. Answer set programming (ASP) is the practical engine (smodels, clasp, DLV, gringo; the term dates from 1999) [a16]. Example from the source: choice rule 1{p,q,r}2 with "s :- not p" has six stable models.

### 2.5 KLM and preferential approaches

- Kraus, Lehmann, Magidor (1990) [a08]. Defeasible consequence |~ satisfies Reflexivity, Left Logical Equivalence, Right Weakening, Cut, Cautious Monotony and OR. Cut: if phi&psi |~ tau and phi |~ psi then phi |~ tau. Cautious Monotony: if phi |~ psi and phi |~ tau then phi&psi |~ tau. Semantics: models ordered by normality; keep the minimal ones.
- Rational Monotony is contested; Stalnaker (1994) gave a counterexample [a08].
- Rational closure (Lehmann and Magidor 1992) [a09]. Give each formula a rank (how exceptional it is). phi |~ psi holds if rank(phi&psi) < rank(phi&not psi). Known flaw, drowning: a subclass that is exceptional in one respect loses all defaults, even unrelated ones. Lexicographic closure was proposed as a fix.
- Specificity [a10]. More specific information overrides more generic (a baby bat does not fly although bats have default links to flying). Inheritance networks give different answers under different path semantics. No single winner.

### 2.6 The frame problem and Yale shooting

Hanks and McDermott (1985, 1987) showed that naive non-monotonic formalisms give a wrong answer on a simple scenario (Fred, gun loaded at 1, wait, shoot at 3). There are two minimal-change models: intended (Fred dies) and spurious (gun unloads by itself, Fred lives) [a13, a14]. Fixes include predicate completion, Sandewall's occlusion and Reiter's situation calculus [a14]. Lesson for an agent: "minimise change" is underspecified. You must say what may change, not only how much.

### 2.7 How the families relate

Circumscription, Reiter's logic, autoepistemic/stable models and KLM models all give "retract on new evidence". They agree on easy penguin cases and diverge on conflicting defaults, floating conclusions and priorities. Equivalences hold only for fragments [a28]. Which one is "right" is a design choice; the review does not resolve it [a07]. Nobody has run an empirical test that picks the family best matching human or LLM behaviour.

### 2.8 Psychology of defeasible inference

- Byrne (1989), suppression task. People withdraw a valid modus ponens conclusion when a second conditional names an extra requirement. Alternative-cause conditionals do not suppress. Numbers below come from a later paper's table; the original was not opened [b01].
- Dieussaert et al. (2000) replicated direction with smaller size [b02].
- Open-answer variants show suppression changes form: people mostly use closed-world logic plus strengthening ("if p then q" read as also "only if") [b03].
- Cognitive argumentation model (Dietz Saldanha and Kakas 2020) explains Byrne's twelve cases and minority answers, with some spread from prediction mode versus explanation mode [b07].
- Counterexample retrieval. When unsure, people cite concrete counterexamples more than probabilities [b04]. Known counterexamples reduce confidence less for valid than invalid arguments [b05].
- Debate: Oaksford and Chater say everyday inference is non-monotonic so classical logic fails as a theory of reasoning; Politzer and Braine say a conclusion's truth is defeasible but the inference's validity is not [b29, second-hand].
- Elio and Pelletier / Pelletier and Elio (1993-2005): people resist default inferences about individuals known to violate another default, and perceived answers in inheritance puzzles depend on whether exemplars are present. Not opened [b28, c22, d17].

### 2.9 Defeasible reasoning in NLP and AI (pre-LLM)

- RuleTaker (Clark et al. 2020) [c01]. Fine-tuned RoBERTa under closed-world negation as failure. About 99% on in-distribution sets; near perfect on Sergot's hand-written Birds rulebase. Removing a critical context sentence: 81.2% vs 99.4%. Authors note a clash: from "if my car does not have gas then it is not working" the model infers "not working" because it cannot prove "has gas".
- ProofWriter (Tafjord et al. 2021) [c02]. Open and closed world; answer accuracy 99.3 / 99.2%, proof correctness 87.1 (PRover) vs 96.2 (ProofWriter).
- Defeasible NLI (Rudinger et al. 2020) [a26, b18, c04]. See section 3.
- BoardgameQA (Kazemi et al. 2023) [a24, b17]. Facts, rules and pairwise rule priorities (newer source beats older; "penguins do not fly" beats "birds fly").

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Humans suppress valid modus ponens with an added requirement | MP 96 / 96 / 38 (simple / alternative / additional); MT 92 / 96 / 33; DA 46/4/63; AC 71/13/54 | Byrne 1989 via Dietz Saldanha and Kakas [b01] (not opened) | [E] direction; size format-dependent |
| Replication smaller | MP 88 / 93 / 60; MT 69 / 44 | Dieussaert 2000 via same table [b02] | [E] direction |
| Open answers change the picture | N=10; MP 100 / 100 / 40; per subject: 5 closed-world+strengthening, 2 minor, 1 classical, 0 probabilistic | Trehan et al. 2005 course paper [b03] | [S] tiny N |
| Unsure people cite counterexamples | Exp1 N=20 MP: certain 30.9, counterexample 45.0, probability 24.2; Exp2 N=37: 28.0 / 45.6 / 26.4 | Knauff and Gazzo Castaneda 2026 [b04] | [E] with [b05, b07] |
| Known counterexamples lower confidence less for valid args | few vs many counterexamples: valid .831 vs .644 (d=.187); invalid .811 vs .486 (d=.325); Exp1 N=117 (100 kept), Exp2 N=245 | Schroyens et al. 2010 [b05] | [S] |
| Defeasible NLI: fine-tuned models near human | RoBERTa vs human: SNLI 81.6 vs 83.6; ATOMIC 78.3 vs 78.2; SOCIAL 86.2 vs 87.6; update-only baseline 65.1 / 65.2 / 71.6 | Rudinger et al. 2020 [a26, b18, c04] | [S]; artifacts |
| Inference graph first adds a little | +1.4 (ATOMIC), +3.4 (SNLI), +1.9 (SOCIAL) over end-to-end | Madaan et al. 2021 [b19, c05] | [S] |
| Generating exceptions is hard | Exception P@1 0.632 vs GPT-3 0.517; instantiations 0.911 vs 0.758; NLI filter lifts exceptions to 0.839 (+20.7) | Allaway et al. 2023 [a27, b20, c06] | [S] |
| One-step default inferences near ceiling for 2024 frontier models | Zero-shot, 15 patterns: Claude 3 Opus 96.51; Claude 3.5 Sonnet 96.01; GPT-4 0613 93.52; GPT-4 Turbo 92.69; Gemma 2 9B 92.69; GPT-4o Aug 89.03; Code Llama 34B 6.48; 28 models | Kirkpatrick and Sterken 2025 [a21, b09, c29] | [C] (format dependent) |
| Same models weaker on rule lists | LogicBench non-monotonic avg yes/no: Llama-2 57.8/43.7; Mistral 71.0/67.5; Gemini 67.8/69.7; ChatGPT 61.5/65.5; GPT-4 74.4/84.8; MCQ GPT-4 69.0 | Parmar et al. 2024 [a25, b16, c08] | [C] |
| Generics read as universals | Mean acc base / deductive-generic / deductive-universal: DMP 80.5 / 25.1 / 74.8; DMT 80.3 / 34.5 / 69.3; r(base,v) = -0.68 (DMP), -0.84 (DI); 28 models | Kirkpatrick and Sterken [a22, b12] | [E] |
| CoT hurts strong models on one-step defaults | Mean -11.14 (SD 15.74) among models above 75%; GPT-4 0613 -12.62; Gemini 1.5 Flash -18.77; Llama 2 70B -41.52; but GPT-4o May +17.44; Code Llama 34B 6.48 to above 62 | [a21, b10] | [C] |
| Few-shot helps weak, hurts strongest | Llama 2 Chat 7B +28.74; Haiku +25.08; GPT-4o May +16.27; Claude 3 Opus -6.81 | [b11] | [S] |
| Wording fragility | Variants correlate 0.99, 0.99, 0.88 with base but 0.54, 0.47, 0.43 and -0.05 for worst | [b11] | [E] with [c28] |
| Irrelevance handled by top models | Fact irrelevance: Haiku and GPT-3.5 75 to 100 few-shot; GPT-4o May at chance on basic default | [a23, b13] | [S] |
| Models drop agreement with generics after exceptions, and also after supporting/irrelevant exemplars | 7 open 7-13B models; exceptions p=0.01; to 0% for four models on GEN-abs; irrelevant exemplars below 50% | Leidinger et al. 2024 [b08, c07] | [E] |
| Models fail to retract on defeaters (Belief-R) | Llama-3 70B update/maintain/BREU 10.99 / 92.09 / 51.54; Mixtral 8x22B 35.38 / 36.57 / 35.98; Claude-3 Haiku 13.69 / 75.67 / 44.68; Claude-3 Sonnet 9.40 / 88.66 / 49.03; GPT-4 Turbo 19.65 / 82.69 / 51.17; best BREU about 50; 30 models | Wilie et al. 2024 [b25, d08] | [E] |
| Prompting does not fix it | CoT or plan-and-solve about +/-1 point; Llama-3 70B CoT 12.57/89.40; Mixtral CoT 27.28/34.93; extra unrelated premise lowers maintain accuracy on 378 matched queries | [b26, d08] | [E] |
| Confirmation-bias gap in multi-turn dialogues | 900 conversations, 18,390 turns; significant in 17 of 19 cells; GPT-5.1 gap 0.935 (OR 891 [586, 1498]), accuracy on defeating updates 3.5% | Sadhu et al. 2026 DeReLab [b22, c27] | [S] (single group) |
| Know-but-do-not-output | GPT-5-mini labels weakening 95.4% but revises 20.3%; Llama-3.1-70B 85.1 vs 14.9 | [b23, c28] | [S] |
| Question order drives the label | Effect-label accuracy standard to reversed: Gemma-4-31B 0.970 to 0.264; Gemma-4-12B 0.887 to 0.209; Gemma-4-MoE 0.732 to 0.288; Qwen3-32B 0.803 to 0.414; BiasGap Qwen3-32B 0.670 to 0.816 | [d04] | [S] |
| Thinking removes bias in one model | Qwen3-32B default gap 0.670 vs 0.008 with thinking (Holm p 0.015, OR 1.07); anchoring 0.032 / 0.004; overall acc 86.0 | [b24, d06] | [S] |
| Anchoring | Kept first answer after truth changed: GPT-5.1 0.433, Qwen3-32B 0.483; GPT-5-mini and Gemma-4-31B about 5% or less | [d06] | [S] |
| Overall DeReLab accuracy | Qwen3-32B thinking 86.0; GPT-5-mini 83.7; Gemma-4-31B 82.4; Gemma-4-12B 78.3; GPT-5.1 72.5; Llama-3.1-70B 53.2; Gemma-4-E4B 47.0 | [b24] | [S] |
| False revision on clean irrelevant updates is low for strong models | Intrusion easy/hard: GPT-5.1 0.9/1.2; Gemma-4-31B 0.3/1.4; Qwen3-32B thinking 0.2/2.6; Llama-3.1-8B 36.2/31.9; Llama-3.1-70B 15.2/8.1 | [d05] | [S] |
| Small models inertial, rarely over-flip | DeltaLogic: Qwen3-1.7B n=30 initial 0.667, revised 0.467, inertia 0.600, over-flip 0.000; Phi-4-mini n=20 inertia 0.200, over-flip 0.100 | Dhanda 2026 [d07] | [S] tiny N |
| Unconditional "Are you sure?" costs accuracy | 10 LLMs, 7 tasks: flip rate 46%, mean drop 17 pts; GPT-4 flips 12.8% (10.4 on correct); Claude V2 56.5; GPT-3.5 59.9; fine-tuning cuts drop about 60% | Laban et al. 2024 [d10] | [E] (2023 models) |
| Exception-aware prompt trades misses for false alarms | Opus 4.6, 68 scenarios: generic 61/68 (89.7%), 7 FN, 0 FP; enhanced 44/68 (64.7%, CI 52.8-75.0), 4 FN, 20 FP | Simpson et al. 2026 [d02] | [S] vendor |
| Frontier models ceiling on single-level exceptions, fail nested chains | 43/43 for Opus 4.6, Sonnet 4.6, GPT-5.4; GPT-5-nano 21/43; spacecraft: Opus 4.6 61/68 March, 67/68 April; GPT-5.4 68/68 | [d01] | [S] vendor |
| Adversarial extension | N=20: engine 20/20; Opus 4.7 fails 2; GPT-5.4 default 1; Sonnet 4.6 1; rule engine beats LLMs on LegalBench by up to 41 points (949 cases) | [d03] | [S] vendor |
| Explicit priority rules in prompt | HOLMES law: 63.33 to 86.33% verdict acc; recall of conflict-resolution rules falls as conflicts rise; finance best 52.1% | Wu et al. 2026 [d09] | [S] |
| BoardgameQA falls with conflict in older models | Conflict 0 / 0.2 / 0.5 / 0.8; BERT near random at medium and high; PaLM 540B few-shot poor | Kazemi et al. 2023 [a24, b17] | [E] for older models |
| BoardgameQA now saturated | Plain reasoning models 84.7%; LLM+ASP 82.4 (92.0 vs 88.0 among reasoning models); LLM+SMT 60.1 | Ishay and Lee 2026 [b15, c30] | [C] |
| Solver offloading helps | MultiLogicNMR 59.0/52.9 to 90.5/81.0 (skeptical/credulous); average 6 benchmarks 51.3 to 78.0; 54.6 without revisions; SMT 35.8/35.0 (chance 33.3); syntax errors 360 to 18; DeepSeek V3 only 45.0 | [b14, c30, b15] | [E] with caveats |
| bAbI with ASP | 80.34 (few-shot), 86.18 (CoT), 99.99 (GPT-3+ASP) | Yang et al. 2023 [a19, c12] | [S] same group as above |
| LOGicalThought | +11.84% overall; +5.5% defeasible; Mistral-7B 45.2 to 53.4; -0.8 ContractNLI defeasible | Nananukul et al. 2025 [c10] | [S] |
| Logic-LM | ProofWriter GPT-4 52.67 / 68.11 / 79.66; PrOntoQA GPT-4 CoT 98.79 beats Logic-LM 83.20 | Pan et al. 2023 [c11] | [E] general |
| LLMs poor at computing answer sets | ASPBench 14 LLMs: ASE F1 68.8 avg (peak 98.2); ASV 64.7 (peak 87.2); ASC exact match 23.2% synthetic, 8.6% real; deepseek-r1 55.7 vs v3 20.7 | Ren et al. 2025 [a18, d13] | [S] |
| Self-correction without a signal hurts | GPT-4 GSM8K 95.5 to 89.0; GPT-3.5 CSQA 75.8 to 41.8; GPT-3.5 keeps first answer 74.7% on GSM8K; oracle: GPT-3.5 84.3/89.7/29.0, GPT-4 97.5/85.5/59.0 | Huang et al. 2024 [c16] | [E] |
| Coherent counter-evidence accepted, substituted resisted | Evidence order changes results over 5 points, over 30 for PaLM2 and Llama2; memorisation ratio up to 80% for GPT-4 on popular entities | Xie et al. 2024 [c17] | [S] |
| Rule memory with votes | ExpeL ALFWorld "put": ReAct 50, insights-only 61, retrieval-only 73, full 83 | Zhao et al. 2024 [c15, d12] | [E] |
| Rule induction | HtT +10-30 over CoT; wrong rules cause 65% of CoT errors on CLUTRR, 81% on base-16 | Zhu et al. 2024 [c14] | [S] |
| Argumentation layer no better than CoT | Accuracy 0.54-0.81; best ArgLLM 0.81 vs CoT 0.79 | Freedman et al. 2025 [c18] | [C] |
| Structured defeasible tasks: partial far above complete | Best complete 82.4% (model name uncertain); GPT-OSS-120B 12.4 to 29.0 (low to high); Gemma-4-31B 14.4 to 27.3; Qwen 28.4 to 39.2; Qwen3.5-27B local 88.7 vs complete 35.8; last-link vs weakest-link 92.9 vs 71.8; strict-rule condition 50.8 to 11.7 with more effort | Deveci et al. 2026 ArgGYM [b30] | [S] |
| Exception proposal failures are format failures | 1,054 failures: 652 contract, 366 token cap, 36 semantic; Sonnet 5.5 133 direct vs 336 structured; simple symbolic repair solves all 336 | Cooper et al. 2026 DeFAb [c09, d16] | [S] |
| Tachmazidis defeasible theories | 8 theories x 4 variants with GPT-4o; levels-(5) wrong in all 4, levels(5) wrong in 2, dag(3,2) wrong in 1; an earlier count of 25/32 correct is the analyst's count, not the paper's | [a20, b27, c31] | [S] soft |
| Hearsay framing | Stated evidence moves posteriors 18-28 pts; reporting lowers it by 2-5 pts in all 7 configurations; five weighted estimates cut movement 43% and 68% in the two local models | Jhang 2026 [c20] | [S] |
| Moral exceptions | MoralCoT 64.47 F1 (+10.53 over base); human yes-rates 31.67-88.37% | Jin et al. 2022 [c19] | [S] |
| Irrelevant context erodes multi-step reasoning | Grok-3-Beta step acc 43% (1 irrelevant) to 19% (15); GPT-4.1 26% to 2% at depth 5 | Yang et al. 2025 [d11] | [E] general |
| Premise non-monotonicity in induction | GPT-4 matches humans except premise non-monotonicity; human Exp1 N=110 | Han et al. 2023 [b21] | [S] |

## 4. Mechanisms and models

Each mechanism is stated so an engineer can build it.

### 4.1 Default rule with abnormality (McCarthy style)

- Store a rule as: `rule(id, if, then, ab_id)`. The rule fires when `if` holds and no recorded fact says `ab_id` is true.
- `ab_id` is true only when a located fact (observed output, test result, new observation) names the exception. Absence of evidence does not set it. RuleTaker's clash shows the failure to avoid: silence read as a negative fact [c01].
- Use one abnormality aspect per rule, not one global "abnormal" flag. This keeps an exception to "flies" from killing "has feathers" [a04].

### 4.2 Reiter default with justification

- `default(prereq : justification / conclusion)`.
- Procedure: (1) if prereq is known, (2) if the negation of justification is not derivable now, then (3) add conclusion and log the default as used.
- Log used defaults. When a later fact makes the justification inconsistent, the log tells you which conclusions to retract. Recompute from the facts plus the surviving defaults; do not patch the conclusion set in place (extension = fixed point) [a06].
- Normal defaults (justification = conclusion) are safe: an extension always exists [a06, a15]. Prefer them.

### 4.3 Conflict resolution

- Build a specificity order: rule A beats rule B if A's condition is a subset of B's, or the rule author said so (Poole 1985, Horty 2007) [a10].
- If two applicable defaults disagree and neither beats the other, apply skeptical mode: withhold the conclusion and record "undetermined" (Nixon diamond) [a05, a07]. Credulous mode (pick any extension) is for brainstorming, not for committing.
- Note the open design choice: floating conclusions [a07]. Our default: do not count them.
- Caveat. This exact "withhold" instruction has no LLM test (K24). It conflicts with G6 (never abstain on first pass), so the withhold applies to a single sub-conclusion, not the final answer.

### 4.4 Preferential closure (KLM, rational closure)

- Rank every default by how exceptional its antecedent is. Rank 0 = fully normal. An exception in a rule's antecedent pushes it to rank 1 or higher [a09].
- Read a case as normally as possible: keep all defaults of the lowest rank not contradicted.
- Drowning warning: a subclass exceptional in one respect loses unrelated defaults under rational closure [a09]. For an agent, this means: when an exception is found, retract only the default it names, not every default about that object.

### 4.5 Answer set programming loop (LLM writes, solver checks)

From Ishay and Lee 2026 [b14, c30, b15]:
1. LLM translates the problem into an ASP program (facts, default negation `not`, exceptions).
2. Run clingo. Syntax or grounding errors go back to the LLM with the error text.
3. At most a few revision rounds. Self-revision lifted the six-benchmark average from 54.6% to 78.0%; syntax errors fell from 360 to 18.
4. Use a compact reference guide: 61.4% to 70.0% with a reference guide; verbose documentation hurt ("context rot").
5. Use reasoning-grade models. Non-reasoning DeepSeek V3 reached only 45.0%.
6. Monotonic SMT is not a substitute: 35.8 / 35.0 (chance 33.3) on nonmonotonic items.

Do not ask the LLM to be the solver for answer-set computation: exact match 23.2% (synthetic), 8.6% (real programs) [d13]. Ask it for entailment/verification only, and compute in the tool.

### 4.6 Defeater-gated revise (from the contrast of [c16] and [b14])

This is inferred, not tested as a unit.
1. Keep the current conclusion C and its defaults.
2. A new item arrives. Code (or a cheap model call that only classifies) tags it: supports, weakens, undercuts, irrelevant. Ask the conclusion question before the label question (order effect [d04]).
3. Only on "weakens/undercuts" re-derive C from the facts with the defeater included. On "irrelevant" do not touch C.
4. Log: stale (kept when should change), over-flip (changed when should not), abstain. Measure them separately [d07].
5. An external check (verifier output, failed test, new observation) is the best signal. A model's own doubt is not [c16].

### 4.7 Rule memory with vote counts (ExpeL)

- Insight list; ADD starts at importance 2; UPVOTE or EDIT +1; DOWNVOTE -1; remove at 0 [c15, d12].
- It is a frequency counter. It does not write exceptions. A common rule survives a rare exception; a single exception lowers the count by 1 [d12]. To store exceptions properly, add a second field `exceptions: [conditions]`, written only when a located failure names the condition. This is our extension; untested.

### 4.8 Exception generation with a filter

Generate candidate exceptions for a rule; filter by an entailment or consistency check. In the one study this lifted exception precision@1 0.632 to 0.839 [b20]. NLI labels are not clean here (generic-exception pairs are not always "contradiction") [b20, c06].

## 5. What holds up

### 5.1 Replications and failures

- Suppression effect (Byrne). Direction holds in replication (Dieussaert) but the modus ponens drop shrinks from 58 points to 28 [b01, b02]. With open answers N=10 the drop is 60 points (100 to 40) but mostly changes the form of answers [b03]. No large registered replication was found [d18]. All three sources are tables read second-hand or tiny samples.
- LLM single-lab results. DeReLab and DeFAb share a group; Ishay and Lee shares authors with Yang et al. 2023 [critique]. The 2026 preprints are unreviewed. A vendor paper (Aethis) withdrew a finding itself: GPT-5.4 low effort 7/11 became 11/11, and Opus 4.6 moved from 89.7% in March to 98.5% in April with no version change [d01, d02].
- Failed or null: layering a gradual argumentation framework over LLM arguments [c18]; ASP on saturated BoardgameQA [b15]; the ExpeL vote as an exception writer [d12]; hearsay/five-estimate elicitation in large models (change -3.7 to +0.5 points) [c20]; SMT for nonmonotonic items [b15].
- Extraction issues. LogicBench table column order is inferred; Belief-R appendix rows partly lost; ArgGYM model names inconsistent [critique].

### 5.2 Moderators and boundary conditions

- Format. 96% on one-step generic patterns vs 57-85% on rule lists [K01]. Answer format (closed vs open) moves human suppression size [b03].
- Model era and size. Rank is not tied to size: Gemma 2 9B beat 27B; Gemini Flash beat Pro [b09]. Claude 3.5 Sonnet CoT delta -0.33 vs GPT-4 -12.62 [b10].
- Question order. Label first vs conclusion first moves effect-label accuracy by up to 0.7 [d04].
- Wording. Some paraphrases correlate only 0.43-0.54 with base; one -0.05 [b11].
- Source. Hearsay framing lowers the update size by 2-5 points [c20].
- Evidence coherence and congruence. Models accept coherent and congruent evidence and resist incongruent [c17, b22].
- Edit type. Adding support is easy; removing support or adding a defeater is hard [d07].
- Depth. Nested exception chains fail; single-level at ceiling [d01].
- Conflict rate. Older models fall steadily; now saturated for strong ones [a24, b15].

### 5.3 Interventions that worked

- Solver feedback in an ASP loop (54.6 to 78.0) [c30].
- Oracle labels of wrongness (GPT-3.5 CSQA 41.8 up to 89.7 with oracle) [c16].
- Extended thinking in one model (Qwen3-32B gap 0.670 to 0.008) [b24].
- Few-shot for weak models (+28.74) [b11].
- NLI filter over generated exceptions (+20.7) [b20].
- Insight memory with retrieval (50 to 83) [c15].
- Explicit priority rules in prompt (63-86% verdict) [d09]. Not compared with a plain-language arm.
- Fine-tuning to resist "Are you sure?" (drop cut about 60%) [d10]. Not available to us.

### 5.4 Interventions that did not work, or backfired

- CoT or plan-and-solve on Belief-R (about 1 point) [b26].
- CoT on strong models for one-step defaults (-11.14 mean) [b10].
- Unconditional re-check (46% flips, -17 points) [d10].
- Exception-aware prompt: 89.7 to 64.7 with 20 new false positives [d02].
- Label before conclusion (worse bias gap) [d04].
- Reflections added to ExpeL insight step (hurt) [d12].
- Verbose ASP documentation [c30].
- More thinking in a strict-rule ArgGYM condition (50.8 to 11.7) [b30].

## 6. Language models

### 6.1 What they do

1. One-step default inferences with common generics: strong. Frontier 2024 models 93-96% zero-shot [b09]. Weak models near chance.
2. They treat "usually" like "always" when asked about deductive validity. Defeasible accuracy and deductive-wording accuracy correlate negatively across models (r -0.68 to -0.84 in several patterns) [b12].
3. Retraction is the weak point. Belief-R update accuracy is 9-35% for the printed models while maintain accuracy is 36-92% [d08]. DeReLab GPT-5.1 correct on only 3.5% of defeating updates [d06].
4. The failure is stubbornness, not noise. Strong models almost never revise wrongly on a clean irrelevant update (0.2-1.4%) [d05]. Small models do (15-36%) [d05], although the DeltaLogic small models over-flip rarely (0 to 0.10) and mainly show inertia [d07]. These two readings fit if the stale answer, not the over-flip, is the main loss.
5. They can name the right label and still not act on it (95.4% vs 20.3%) but the gap depends on question order [b23, d04].
6. Priorities: models find the single decisive rule and skip the rest of the chain [d09]. Nested exceptions (UNLESS inside UNLESS) fail in some cells for Claude Opus 4.6 / 4.7, Sonnet 4.6 and GPT-5.4 [d01]; the failures are false negatives [d01].
7. Conflicts without specificity (Nixon): only an aggregate exists; Claude-family above 80%, GPT-4 family from below chance to 100% on forced yes/no [d14].

### 6.2 What changed it and by how much

| Change | Effect | Source |
|---|---|---|
| Solver in the loop | +20 to +30 points on nonmonotonic sets | [c30, a19] |
| Solver feedback vs none | 54.6 to 78.0 | [c30] |
| Extended thinking | Qwen3-32B bias gap 0.670 to 0.008; other tasks null or negative | [b24, b10, b26] |
| CoT | -11.14 mean (strong, one-step); about 0 (Belief-R) | [b10, b26] |
| Few-shot | +28.74 (weak) to -6.81 (strongest) | [b11] |
| Reversed question order | Effect-label 0.970 to 0.264 | [d04] |
| Exception-aware prompt | FN 7 to 4, FP 0 to 20 | [d02] |
| Re-check always | -17 points on average | [d10] |
| Oracle signal | GPT-3.5 CSQA 41.8 to 89.7 | [c16] |
| Rule memory + retrieval | 50 to 83 | [c15] |
| Priority rules in prompt | 63-86% verdict, shortcut traces | [d09] |
| Time (same prompt) | Opus 4.6 spacecraft 89.7% to 98.5% | [d01] |

### 6.3 What is missing

No run of 2025-2026 Claude or GPT-5 on Belief-R or the Kirkpatrick set was found. Claude data are Claude 3 / 3.5 (Belief-R: Haiku, Sonnet; Kirkpatrick: Opus, Sonnet) plus nested-exception data on 4.6/4.7 [critique]. DeReLab has GPT-5.1 and GPT-5-mini but no Claude.

## 7. What our agent should take

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Revise only from a located failure or a named defeater; do not re-check on a schedule. Unconditional "are you sure" costs 17 points on average; self-correction without a signal lowers accuracy | G1, G2 / S5 | [E] | c16, d10, c30, K08, K21 |
| Treat default rules as defeasible but hold them until a concrete defeater is present; keep the defeater named and located | G1 / S5 | [E] (design) with [S] test | a01, a06, K21 |
| Log stale, over-flip and abstain separately in the harness | S9 / harness | [E] | d05, d07, K20 |
| Add an external signal where one exists (verifier, solver error, failed test, new observation) as the trigger for S5 | S4-S5 | [E] | c30, c16, K08 |
| Distinguish a rebutting defeater from an undercutting one in the revise line ("this fact contradicts the answer" vs "this fact weakens the link") | S5 | [E] (concept) | a12 |
| Specificity rule: more specific wins; on a tie, mark that sub-conclusion undetermined, not forced | S5 / O | [E] formal, [S] LLM | a05, a07, a10, K18 |
| Evaluate with paraphrase and order checks before trusting a revise decision (wording variants as low as 0.43 correlation) | G (robustness) | [E] | b11, d04, K04 |
| Measure output-format failures before judging logic (652 of 1,054 failures were contract violations) | O (output contract) | [S] | c09, K16 |
| Pin model snapshots in any benchmark; re-run exception chains on the deployed model | G7 / bench | [S] | d01, K22 |
| Ask the conclusion question before the effect-label question; do not add a label-first step | S5 | [S] | d04, K03 |
| Memory: store defaults as rule + confidence count; downvote on located exception | memory | [E] for counts | c15, d12, K15 |
| Do not use LLM as answer-set solver; if ASP is used, call the solver | O (tool) | [S] | d13, K07 |
| Do not copy prompts across models; test few-shot per model | G7 | [S] | b11, K19 |
| Do not use debate or argumentation layers for this | G9 | [C] | c18, K17 |

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Gated revise (defeater named first) vs re-check always, at equal tokens, score misses and false revisions | G1 / S5 | [C] inferred | d02, d05, d10; U1 |
| Explicit exception field in memory vs flat count vs flat notes | memory | [S] | d12, c15; U3 |
| Defaults as explicit unless-rules with specificity order vs plain generics | S5 / O | [S] | d09, d02; U4 |
| Skeptical withhold instruction for tied conflicting defaults | S5 | [S] | d14; U5 |
| Small ASP/Prolog tool vs plain reasoning on nested exceptions | O | [C] | b15, d03, d13; U6 |
| Exception search then filter vs exception search alone | S5 / O | [S] | b20; U7 |
| Counterexample prompt only on a signal vs probability estimate step | S5 / O | [S] human only | b04, b05; U8 |
| Long thinking vs short at equal tokens on defeater items | G11 | [C] | b24, b10, b26; U2 |

## 8. Concrete tests on our bench

All arms get the same total token budget (including setup, G7). Report mean and an interval over at least 3 seeds; pin the model snapshot.

1. **Gated revise vs re-check-always.**
   - Items: 100 multi-turn default tasks (DeReLab-style entity graphs, Belief-R-style additional requirement vs alternative cause), half with a defeater, a quarter with a clean irrelevant update, a quarter with a plausible-but-misleading update.
   - Arms: (A) plain; (B) re-check every turn; (C) gated: tag update first, revise only on weakens/undercuts; (D) gated with an external verifier signal where available.
   - Metrics: stale rate, over-flip rate, balanced score (Belief-R BREU style), tokens.
   - Expected: C beats B on over-flip by at least 10 points and ties or beats A on stale. Based on [d10, d02, d05].
2. **Order of questions.** Same items; conclusion-first vs label-first vs label-then-restate. Metric: revised-conclusion accuracy. Expected: conclusion-first >= others [d04]. Cheap.
3. **Format sweep.** Same 30 default inferences as (a) one-step generic sentence, (b) rule list with "unless", (c) explicit specificity-ordered rules. Metric: accuracy and full-chain use. Expected: (a) near ceiling, (b)/(c) lower; show whether (c) closes the gap [K01, K23].
4. **Nested exceptions.** 60 "A UNLESS B, UNLESS C overrides B" scenarios with 1, 2, 3 levels. Arms: plain; short thinking; long thinking; ASP tool with compact reference guide. Metric: false negatives and false positives. Expected: tool wins at 3 levels, ties at 1 [d01, d03, b15].
5. **Nixon-style conflicts.** 20 items with two equally specific defaults plus 20 with a clear specificity winner. Arms: plain; "withhold on tie"; "pick the more plausible". Metric: correct withhold, wrong pick, over-withhold on the 20 clear items. Expected: instruction raises correct withhold without raising over-withhold above 5% [K24].
6. **Irrelevant context.** Defaults tasks with 0, 3, 10 irrelevant facts. Metric: accuracy drop. Expected: small for strong models [d05, d11].
7. **Memory exceptions.** Teach a default then an exception from one case; later items include the exception condition and non-exception look-alikes. Arms: flat notes; count+downvote; rule+exception field. Metric: correct exceptions applied, wrong exceptions applied.
8. **Paraphrase stability.** Run each item in 3 paraphrases and both orders; flag items with changing answers. Metric: agreement rate; require stable answers before a revise is trusted [b11].
9. **Human anchor.** A 16-item suppression set (additional vs alternative requirement). Compare our agent with the Byrne pattern (96/96/38) to see if it suppresses more or less than humans. Not a score to maximise.

## 9. What does not transfer, and why

- Formal completeness and complexity results (Sigma2P / Pi2P) [a15]. An agent does not compute extensions of arbitrary theories. It needs a small defeasible rule store, not a general prover.
- Circumscription's second-order schema [a02]. Not computable in general; the practical descendant is ASP.
- Exact Reiter semantics. No human or LLM study shows people or models follow extensions. Models follow surface cues (generic as universal [b12], irrelevant exemplars [b08]).
- Human suppression effect size (28-58 points) as an LLM target. Direction only; size depends on answer format [b03]. No item-level link to LLM error was found [d18].
- Old benchmark conclusions. BoardgameQA collapse (2023) is saturated by 2026 reasoning models [b15]; Kirkpatrick CoT harm is for 2023-2024 models.
- Fine-tuned delta-NLI scores [a26]. Pre-LLM and carry annotation artifacts (update-only 65-72%).
- Fine-tuning-based fixes (FlipFlop -60% drop) [d10]. We do not train.
- Solver results where rules are hand-written per task [a19]. The authoring cost and translation errors are the real cost; the translation is the weak link [c10].
- ExpeL numbers on ALFWorld [c15]: tasks with repeated structure; not exception learning.
- Vendor results (Aethis) as proof that a rule engine is needed: the group sells one [d03].
- Moral exceptions (MoralExceptQA) [c19]: different kind of defeasibility (norms, purposes).
- Inductive non-monotonicity (Han et al.) [b21]: similarity-based, not default logic.

## 10. Open questions

1. Does gated revise beat re-check-always at equal tokens, and what is the false revision cost on plausible-but-misleading updates? (No study.)
2. How do 2025-2026 Claude and GPT-5 models score on Belief-R and the Kirkpatrick-Sterken set, with and without extended thinking?
3. Is restate-after-label useful, or is the old gap an order artefact? (Only open Gemma and Qwen were order-tested.)
4. Do explicit Reiter-style rules with specificity beat plain-language generics, at equal tokens?
5. Where is the break-even for an ASP/Prolog tool, and what does one tool call cost in tokens?
6. What do LLMs do at a Nixon diamond with an abstain option, and does "skeptical: withhold" help or cause refusals?
7. Can memory learn exceptions from one case? (ExpeL votes cannot.)
8. How much does making every rule defeasible cost on plausible irrelevant facts (Leidinger: below 50% agreement with irrelevant exemplars, no 2026 retest)?
9. Does the human effect size predict LLM error item by item?
10. Can the original Elio and Pelletier / Hewson and Vogel numbers be opened and compared?
11. Is the March-to-April drift in a vendor benchmark (89.7 to 98.5) real model change or serving change? It affects how much any single-run scaffold effect can be trusted.
12. Are the 2026 preprints reproducible by an independent group?

## 11. Sources

[V] = opened and read this session or in the earlier research session; [M] = snippet or second-hand only.

- [V] McCarthy (1980) Circumscription: a form of non-monotonic reasoning. http://www-formal.stanford.edu/jmc/circumscription.pdf (a01-a03)
- [V] McCarthy (1986) Applications of circumscription to formalizing common sense knowledge. http://www-formal.stanford.edu/jmc/applications.pdf (a04, a05)
- [V] Stanford Encyclopedia of Philosophy, Non-monotonic Logic. https://plato.stanford.edu/entries/logic-nonmonotonic/ (a06-a11, a28)
- [V] SEP, Defeasible Reasoning (Koons). https://plato.stanford.edu/entries/reasoning-defeasible/ (a12)
- [V] SEP, The Frame Problem. https://plato.stanford.edu/entries/frame-problem/ (a13)
- [V] Wikipedia, Yale shooting problem. https://en.wikipedia.org/wiki/Yale_shooting_problem (a14)
- [V] Wikipedia, Default logic. https://en.wikipedia.org/wiki/Default_logic (a15)
- [V] Wikipedia, Answer set programming. https://en.wikipedia.org/wiki/Answer_set_programming (a16)
- [M] Reiter (1980) A logic for default reasoning. https://doi.org/10.1016/0004-3702(80)90014-4 (c23, not opened)
- [V] Ren et al. (2025) Can LLMs solve ASP problems? (ASPBench). https://proceedings.kr.org/2025/60/kr2025-0060-ren-et-al.pdf and https://arxiv.org/pdf/2507.19749 (a17, a18, d13)
- [V] Yang, Ishay, Lee (2023) Coupling LLMs with logic programming. https://arxiv.org/pdf/2307.07696 (a19, c12)
- [V] Ishay, Yang, Lee (2023) Leveraging LLMs to generate answer set programs. https://arxiv.org/abs/2307.07699 (c13, skimmed)
- [V] Tachmazidis, Batsakis, Antoniou (2024) Benchmarking defeasible reasoning with LLMs. https://arxiv.org/pdf/2410.12509 (a20, b27, c31)
- [V] Kirkpatrick and Sterken (2025) Generics and default reasoning in LLMs. https://arxiv.org/pdf/2508.13718 (a21-a23, b09-b13, c29, d14)
- [V] Kazemi et al. (2023) BoardgameQA. https://arxiv.org/pdf/2306.07934 (a24, b17; exact accuracies only in figures, not read)
- [V] Parmar et al. (2024) LogicBench. https://arxiv.org/pdf/2404.15522 (a25, b16, c08, c26)
- [V] Rudinger et al. (2020) Thinking like a skeptic. https://aclanthology.org/2020.findings-emnlp.418.pdf (a26, b18, c04)
- [V] Allaway et al. (2023) Penguins don't fly. https://arxiv.org/abs/2205.11658 (a27, b20, c06)
- [V] Madaan et al. (2021) CURIOUS. https://arxiv.org/abs/2110.12349 (b19, c05)
- [M] Byrne (1989), Dieussaert et al. (2000), figures via Dietz Saldanha and Kakas. https://arxiv.org/abs/2002.10149 (b01, b02); the later paper itself is [V] (b07)
- [V] Trehan et al. (2005) The Suppression Task Revisited. https://eprints.illc.uva.nl/id/document/9419 (b03)
- [V] Knauff and Gazzo Castaneda (2026) Reasoning beyond clicks. https://pmc.ncbi.nlm.nih.gov/articles/PMC13132893/ (b04)
- [V] Schroyens, Fleerackers, Maes (2010). https://pmc.ncbi.nlm.nih.gov/articles/PMC3019985/ (b05; Exp 2 beyond abstract not read)
- [V] Lopez-Astorga, Ragni, Johnson-Laird (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8231749/ (b06; tables not read)
- [V] Leidinger, van Rooij, Shutova (2024). https://arxiv.org/abs/2406.06590 (b08, c07; per-model figures not individually re-read)
- [V] Ishay and Lee (2026) LLMs as ASP programmers. https://arxiv.org/pdf/2604.27960 (b14, b15, c30)
- [V] Han, Ransom, Perfors, Kemp (2023) Inductive reasoning in humans and LLMs. https://arxiv.org/pdf/2306.06548 (b21)
- [V] Sadhu, Shahad, Marino (2026) DeReLab. https://arxiv.org/pdf/2608.30413 (b22-b24, c27, c28, d04-d06)
- [V] Wilie et al. (2024) Belief-R. https://arxiv.org/pdf/2406.19764 (b25, b26, d08)
- [V] Deveci et al. (2026) ArgGYM. https://arxiv.org/pdf/2609.38409 (b30; model names inconsistent)
- [M] Elio and Pelletier (1993, 1996); Pelletier and Elio (1997, 2005); Hewson and Vogel (1994). Via Kirkpatrick, Allaway, and a repository snippet (b28, c22, d17)
- [M] Oaksford and Chater (1998); Politzer and Braine (1991), via Schroyens (b29)
- [V] Clark, Tafjord, Richardson (2020) RuleTaker. https://arxiv.org/abs/2002.05867 (c01)
- [V] Tafjord, Dalvi Mishra, Clark (2021) ProofWriter. https://arxiv.org/abs/2012.13048 (c02)
- [V] BoardgameQA second-read (c03), same URL as Kazemi
- [V] Cooper, Sadhu, Velasquez (2026) DeFAb, v2. https://arxiv.org/abs/2606.18557 and https://arxiv.org/pdf/2606.18557 (c09, d16)
- [V] Nananukul et al. (2025) LOGicalThought. https://arxiv.org/abs/2510.01530 (c10)
- [V] Pan et al. (2023) Logic-LM. https://arxiv.org/abs/2305.12295 (c11)
- [V] Zhu et al. (2024) Hypotheses-to-Theories. https://arxiv.org/abs/2310.07064 (c14; abstract and introduction only)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 (c15, d12)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (c16)
- [V] Xie et al. (2024) Adaptive chameleon or stubborn sloth. https://arxiv.org/abs/2305.13300 (c17)
- [V] Freedman et al. (2025) Argumentative LLMs. https://arxiv.org/abs/2405.02079 (c18)
- [V] Jin et al. (2022) MoralExceptQA. https://arxiv.org/abs/2210.01478 (c19)
- [V] Jhang (2026) Hearsay or fact. https://arxiv.org/abs/2610.27745 (c20)
- [M] Han et al. (2024), Shi et al. (2023), Wang et al. (2023), Kazemi et al. (2024) as cited in Leidinger (c21, c24, c25)
- [V] Simpson, Kozak, Doake (2026) Confidently Wrong (Aethis, vendor). https://arxiv.org/pdf/2607.23386 (d01-d03)
- [V] Dhanda (2026) DeltaLogic. https://arxiv.org/pdf/2604.02733 (d07)
- [V] Wu et al. (2026) HOLMES. https://arxiv.org/pdf/2606.23238 (d09)
- [V] Laban et al. (2024) FlipFlop. https://arxiv.org/pdf/2311.08596 (d10)
- [V] Yang et al. (2025) GSM-DC. https://arxiv.org/pdf/2505.18761 (d11)
- [V] Schuster, Gautam, Markert (2026) Whose facts win. https://arxiv.org/pdf/2601.03746 (d15; negative use only)
- [M] Search note on large replications of Byrne. https://eprints.illc.uva.nl/1529/ (d18)
