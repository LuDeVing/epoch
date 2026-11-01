# Expert-novice schemas: deep document

*Subfield E06.05. Focus: sorting by deep structure (Chi, Feltovich, Glaser 1981). Why it matters for our agent: the S0 gate and memory. Evidence ids (a01 to d20) and claim ids (E06.05-K01 to K26) refer to evidence_a-d.jsonl and claims.jsonl in this folder. The founding paper was never opened (paywall); its numbers are second hand through replications.*

## 1. What it is

The core claim: experts see a problem as an instance of a principle. Novices see its surface (the objects named in the text). Chi, Feltovich and Glaser (1981) asked physics PhD students (experts) and students who had finished one mechanics semester (novices) to sort textbook problems "by similarity of solution". Experts made groups like "energy conservation" and "Newton's second law". Novices made groups like "inclined plane", "pulley", "spring". The authors proposed that expert knowledge is stored in schemas keyed to principles, and that experts turn surface cues into principles early (a01, b01).

Three ideas sit under this one result.

1. **Sorting as a window.** What a person puts together shows how the problem is represented in memory. The sort is a measurement tool, not the thing that matters.
2. **Schema as index.** Knowledge is stored under deep features, so retrieval, method choice and checking start from the principle.
3. **Surface pull.** Novices (and, less, experts) are drawn to surface overlap. This causes wrong analogies, wrong equation choice and distraction by irrelevant detail.

Why it matters for us. Our agent has an S0 gate that must classify a problem before solving, and a memory that must return the right lesson for a new problem. Both are "sort by deep structure" tasks. If the model sorts like a novice, the gate misroutes and memory returns surface-similar but useless items.

Scope limit. The human sorting literature is mostly physics mechanics (plus some maths and biology). The LLM literature that tests surface pull is mostly arithmetic word problems (GSM8K family). The bridge between the two is analogy, not a direct test (critique, weak spots).

## 2. History and theories in depth

**Precursors.**
- Larkin, McDermott, Simon, Simon (1980): experts work forward from givens using principle-based chunks. Novices work backward by means-ends, equation by equation. Production-system models reproduced both (a14, not opened).
- Silver (1979, 1981): eighth graders sorted maths word problems by relatedness. Better solvers sorted more by mathematical structure, weaker ones by story content (a11, not opened).
- Gick and Holyoak (1983): a schema forms when a learner compares two analogous cases; comparing two stories raised transfer to the radiation problem more than reading one (a15, not opened).

**The founding study (1981).** Study 1 (as quoted in replications): 8 novices vs 8 experts. Novices: angular motion 87.5%, springs 75%, inclined plane 50%, kinetic energy 50%, pulleys 37.5%. Experts: Newton's second law 75%, energy principles 75%, angular motion 75%, circular motion 62.5%. Novices chose 0% for Newton's second law, energy, circular motion and linear kinematics (a03, b01). Study 2 crossed surface features with physical law over 20 problems. Gold labels came from one consulted expert, who solved some problems two ways and filed them under the law he judged "most elegant" (a27). Faculty later disagreed on "elegant" (b29). Problem counts per study are from memory.

**Theory built on it.** Chi, Glaser and Rees (1982) review: experts have more organised knowledge, spend relatively more time representing the problem and less calculating, and novices pick equations by surface cues (a13, not opened).

**Replications and critique (1986 to 2017).**
- Veldhuis (1986/1990): four problem sets, 94 intro students, 5 intermediate, 20 professors. Sets 1 and 2 (natural textbook problems) were inconclusive. Sets 3 and 4 (each problem had one principle and one surface feature, crossed) agreed with Chi for experts; novices behaved "more complexly" (a06, b06, d03; second hand through Wolf).
- Schoenfeld and Herrmann (1982): maths replication, plus training (b07, b08).
- Hardiman, Dufresne, Mestre (1989): similarity-judgment task with crossed items; sorting correlates with solving, but weakly (b09, b10).
- Mason and Singh (2011): 403 intro students, 21 graduate students, 7 faculty. Large softening of the novice picture (a02, a03, b02).
- Wolf, Dougherty, Kortemeyer (2012): two papers showing the sort measures style and problem choice as much as expertise (a05, b04, b05).
- Smith et al. 2013, Bissonnette et al. 2017, Hoskinson et al. 2017: crossed-feature sorting in biology with large samples (d05 to d07).

**Competing explanations of the sort.**
- *Knowledge organisation* (Chi): experts hold principle-keyed schemas.
- *Task and cue account*: novices sort by surface because "similarity of solution" is vague and surface labels are easy to name; some students skip a principle as redundant, or want to name "friction" because "force" feels vague (a08).
- *Sorting style*: stackers (few big overlapping groups) vs spreaders (many small groups) explain more variance than expertise (a05, b04, d04).
- *Item design*: when textbook problems confound surface and principle, the sort cannot separate the two (K03).
- *Cueing vs knowing*: novices may hold the principle but not use it unless cued (Bissonnette, d06; Keith, b30).

**LLM-era reuse.** The same idea reappears in prompt and memory methods: Step-Back (name the principle first), skill-labelled exemplars, Buffer of Thoughts (thought templates), Self-Discover, ReasonFlux. And as a failure model: GSM-IC, GSM-NoOp and CatAttack show models pulled by irrelevant surface content.

## 3. Core findings with exact numbers

Status key: established / single-source / contested / human-only / older models only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Experts sort by principle, novices by surface (founding) | 8 novices vs 8 PhD experts; novices used principle categories 0% (Newton II, energy, circular motion, kinematics); springs 75%, inclined plane 50% | Chi et al. 1981 via a03, b01 | single-source (never opened) |
| Large replication: novices much less surface-bound | 403 intro students (109+114+180), 21 grad, 7 faculty, 25 problems; 18% to 44% of new students chose expert categories on Chi's 7 problems; good-category share 34.4% calculus vs 18.7% algebra | Mason and Singh 2011 (a02, a03, b02) | contested (human-only) |
| Faculty beat graduate students; grad students overestimate students | 7 faculty, 21 grad; faculty-grad gap larger than grad-calculus gap | a02, a07, b29 | established (human-only) |
| Sort results depend on which problems are used | 40,000 five-problem and 275,000 ten-problem subsets of a 50-card set; some separate groups almost totally, others not; problem features explain only 42.7% of discrimination variance | Wolf et al. 2012b (b05) | established |
| Style dominates expertise in sorts | 18 professors, 23 novices, 50 cards; first two components about 87% of variance; PC1 = stacker/spreader; expertise only in PC2; category counts do not separate | Wolf et al. 2012a (a05, b04) | single-source |
| Crossed-feature sets agree with Chi; natural sets do not | Veldhuis sets 1 and 2 inconclusive; sets 3 and 4 agree; 94 / 5 / 20 | a06, d03 (second hand) | established |
| Maths replicates | 9 professors vs 19 students, 32 problems; strong-agreement pairs 10 vs 4, t(26)=10.45, p<.01; deep-homogeneous clusters 8 of 11 (73%) vs 5 of 10 (50%) | Schoenfeld and Herrmann 1982 (b07) | established (small N) |
| A problem-solving course moves the sort | 11 trained vs 8 control; between-group r .650 to .492 (p<.01); deep clusters 6 of 8 (75%); solving F(1,17)=67.2 to 92.4; not randomised | b08 | single-source |
| Sort quality vs solving: weak link | r=.30, p=.042, 45 novices | Hardiman et al. 1989 Exp 1 (b09) | single-source |
| Experts also hit by surface lure | deep-match choice experts 78% vs novices 59%, F(1,53)=28.78; novices 40% correct with surface lure vs 77% neutral | b09 | established |
| Principle-reasoners solve more, even when naming wrongly | 44 novices, 7 experts; solving: surface group 14%, mixed 32%, principle group 57%; principles named wrongly 38% | b10 | established (correlational) |
| Training the sort does not guarantee solving gain | 42 students, 5 hours: tool group deep choices 56% to 66%, solving 29.4 to 41.3; textbook group solving 31.6 to 44.4 | Mestre et al. 1988 (b12) | contested vs b08 |
| Biology crossed set: wide extreme-group gap | faculty n=23: deep 71.7%, surface 8.6%; non-majors n=101: deep 29.2%, surface 40.8%; framed: faculty 83.1% deep, non-majors 39.6% | Smith et al. 2013 (d05) | established |
| Entering and advanced majors similar in free sort | n=185 entering, 109 advanced, 29 grad, 23 faculty; advanced majors used the deep framework once revealed | Bissonnette 2017 (d06) | single-source |
| One irrelevant sentence cuts LLM accuracy (GSM-IC) | code-davinci-002 CoT micro 72.4%, macro (all distractor types) under 30%; least-to-most macro 18.0; self-consistency (20 samples) +11 micro, +35.5 for 0-shot CoT; correct answer in samples 99.7%; best macro 45% | Shi et al. 2023 (a18, c07, c08) | established, older models only |
| GSM-NoOp drops (25 models, 5,000 per set) | Phi-3-mini -65.7; GPT-4o-mini -40.0; GPT-4o -32.0; o1-mini -29.1; o1-preview -17.5 | Mirzadeh 2025 (a17, b18) | established |
| Contamination check on GSM-Symbolic | GSM8K above symbolic centre for 21 of 25 models; only 8 of 20 open models drop significantly; integer size shift K-S 0.12; Haiku 4.5 -1.3 (97.9 to 96.6, n=1000) | b18, d15, d16 | contested (name/number variants); NoOp stands |
| Adversarial irrelevant text on reasoning models | R1 error 1.50% to 4.50% (3x); transfer to GSM8K up to 5.14x; responses over 1.5x length: o1 26.4%, o3-mini 16.8%, R1 28.0% | Rajeev 2025 (d08, d09) | established (worst-case triggers) |
| Step-Back (name principle first) | PaLM-2L physics 66.4 to 73.2, chem 70.9 to 81.8; GPT-4 physics 69.4 to 84.5 (CoT 82.9), chem 80.9 to 85.6 (CoT 85.3); fixes 20.5% of errors, adds 11.9%; over 90% of remaining errors at reasoning | Zheng 2024 (b24, c14, c15) | single-source |
| Skill-labelled exemplars | MATH GPT-4 CoT 42.2 to 53.88 (+11.6); +3.5 over Complex CoT; PAL +7.52; GSM8K CoT 93.00, random 92.87, skill 94.31; GPT-3.5 Retrieval-RSD 76.8 vs skill 82.03 | Didolkar 2024 (b26, c05, c06) | established (the "+3.5 over topic-based" figure unchecked) |
| Template store (BoT) | Game of 24 GPT-4 3.0 / CoT 11.0 / ToT 74.0 / BoT 82.4; MGSM 84.4 to 89.2; about 12% of cost of multi-query methods | Yang 2024 (a21, c11) | single-source (own benchmarks) |
| Abstract memory vs raw retrieval on AIME | Claude 3.5 Sonnet 2024: baseline 23.3, instruction-only 36.7, raw retrieval 43.3, curated 50.0; full history 26.7; 30 questions | Dynamic Cheatsheet (d11, d12) | single-source |
| Self-generated analogs | GPT-3.5 GSM8K 76.7 to 77.8; MATH 34.9 to 37.3; PaLM2 MATH 27.1 to 34.8 | Yasunaga 2024 (a22, c16) | established, small |
| Self-Discover structures | PaLM 2-L BBH 60 (CoT) to 67; 74.7% of MATH failures are computation errors | Zhou 2024 (c13) | single-source |
| Far analogy failure | ARN: far analogy 39.6% (chance 50%), humans 94.1%; counterfactual alphabets humans 75.3%, GPT-3 48.8, GPT-3.5 35.0, GPT-4 45.2 | b27, b28 | established, older models only |
| Syntax affects solving; restating helps | rephrasing failed items: Gemma-7B GSM8K 37.76 to 46.02; strongest model +0.5 to 7.8 | Williamson 2025 (c01, c02) | single-source (upper bound) |
| Premise order | drops over 30% on deductive tasks | Chen 2024 (c18) | established |
| Persona does not help accuracy | 162 roles, 2,410 MMLU items, in-domain coefficient 0.004 | Zheng 2024 (c19, c25) | established |
| First LLM card sort | GPT-5 Thinking sorted 60 exam items into topic-and-method groups; solved 27/30 and 25/30; one run, one author | Kortemeyer 2025 (d01, d02) | single-source |
| Physics errors are in reasoning not perception | first error in reasoning 79% to 96%; perception 4% to 21% (R1 4, o4-mini 6, GPT-4o 21) | PHYBench (d19) | single-source |

Two figures are uncertain: Shi et al. macro 6.0 for CoT (table column unclear; use "under 30%"), and the skills paper "+3.5 over topic-based" (the paper text confirms +3.5 over Complex CoT).

## 4. Mechanisms and models

Each is written so it can be built.

**4.1 Schema as principle-keyed index (Chi model).**
- Store: a set of schemas. Each has a principle name, applicability conditions (deep features that must hold), and a solution procedure.
- Recognition: extract features from the problem text. Match against conditions, not surface nouns. Experts do this fast and early, and add a secondary surface label next to the primary principle (a08).
- Failure mode: if matching uses surface nouns (ramp, pulley), retrieval returns the wrong schema. This is the novice path.

**4.2 Surface-pull measurement (crossed design).**
- Build items on a grid: rows = principle (Newton II, energy, momentum), columns = surface (ramp, spring, pulley). Each cell is one problem. Veldhuis set 3 was a 4x4 grid; set 4 a 2x2 (a06).
- Present triplets or sets. Score "deep match chosen" vs "surface match chosen". Include a neutral-surface control (Hardiman: novices 40% correct with surface lure vs 77% neutral, b09).
- For an LLM: same grid, as sort or as triplet choice. Report deep-match rate, group count and double-filing (stacker/spreader), so style is not mistaken for skill (K21).

**4.3 Four-stage word-problem pipeline (Qu and Gomes 2026, Llama-3.3-70B).**
Stages: schema abstraction, operation planning, operand binding, computation. Entity names stop being decodable at layer 22 (probe accuracy 0.78 falls to chance 0.53); numbers are decodable at layer 40; answer 0.93 at layer 80. NoOp failure arises at operation planning: a digit-bearing distractor draws attention heads (direct prompting: digit-free filler -0.004, digit-bearing -0.067, NoOp -0.101; with CoT NoOp -0.171) (a19, a25). One model; authors re-created NoOp. Engineering reading: the model strips surface early, but a plausible extra quantity corrupts the plan.

**4.4 Causal deep-structure dependence (Han et al.).** Causal mediation: change surface wording vs deep structure, measure answer shift. Closed models depend more on deep structure; open models more on surface, falling with scale; accuracy vs deep-structure effect R2>0.7 across models (c03, c04). The "12 models" count and the random-weight control (0) were not re-checked.

**4.5 Principle-first prompt (Step-Back).** Two calls. Call 1: "what principle or concept governs this?" with few-shot examples. Call 2: solve using the stated principle. Errors that remain come from reasoning after the principle (over 90%), not from the principle itself (b24).

**4.6 Skill-indexed exemplar memory (Didolkar).** Offline: a strong model labels training problems with fine skills (about 5,000), clusters them to 117. Online: a model names the test problem's skill, exemplars of that skill are fetched, then solve. The match drives the gain: random exemplars 92.87 vs skill 94.31 on GSM8K, GPT-4 (c06).

**4.7 Template buffer (BoT / ReasonFlux).** A distiller extracts task and constraints, a template is retrieved from a meta-buffer and instantiated, and a buffer manager adds new templates. Accuracy rises round by round with the manager and stays flat without (c12). ReasonFlux uses about 500 templates and trains a planner (c21; not a prompt-only result).

**4.8 Curated abstract memory (Dynamic Cheatsheet).** After each item the model rewrites a cheatsheet of strategies and code. AIME 2024, Claude 3.5 Sonnet: baseline 23.3, instruction-only 36.7, raw similarity retrieval 43.3, curated 50.0, full-history append 26.7 (d11, d12). A strong base model is needed; GPT-4o-mini fell below baseline.

**4.9 Canonical-form restate.** Rewrite the problem in simpler syntax, or with distractors flagged. Prompt-only evidence exists only for small models (c02). Trained versions work: AbstRaL GSM-Plus distractor 82.3 vs CoT-8S 76.3 (Qwen2.5-Math-7B); DAGGER 69.4% at 359 tokens vs a reasoning model's 71.4% at 3,128 (d17, d18). Prompt-only at frontier scale: untested.

## 5. What holds up

**Held up.**
- Experts (faculty, not just PhD students) prefer principle categories over surface categories, in physics (Chi, Mason-Singh, Veldhuis sets 3 and 4), maths (73% vs 50% deep clusters) and biology (71.7% vs 29.2% deep pairs). K06, K22.
- Experts are also pulled by surface (Hardiman: deep match 78%, not 100%). K08.
- Models are pulled by irrelevant detail: GSM-IC, GSM-NoOp, GSM-Plus (GPT-4 93.25 to 85.58; humans 96.77 to 98.75), MATH-Perturb (o1-mini -16.49 on hard variants), CatAttack. Smaller for stronger and reasoning models, still real. K09, K24.
- Skill/template-keyed exemplars beat random or generic exemplars. K12.

**Failed or weakened.**
- The sharp two-group split. Mason and Singh's intro students rarely chose surface labels; calculus students overlapped with graduate students. Offered reasons: curriculum change since 1981, concurrent course enrolment vs Chi's volunteers, different instructions, written vs card sort. Cause untested (b03). K02.
- Simple sort statistics. Number of categories does not separate experts from novices (Wolf). The authors note informal reports that most repeats of Chi fail and go unpublished (b04).
- Natural textbook sets. Veldhuis sets 1 and 2 were inconclusive. K03.
- Graduate student = expert. Faculty beat graduate students. K05.
- Training the sort improves solving. Schoenfeld's full course moved both (not randomised); Mestre's 5-hour tool raised categorisation but solving gain matched controls (29.4 to 41.3 vs 31.6 to 44.4). K07.
- Mirzadeh's name/number variant result. Only 8 of 20 open models drop significantly after re-analysis; Haiku 4.5 -1.3 (p=.096). GSM8K above centre for 21 of 25 models hints at contamination, but GSM1k found overfit mainly in Phi, Mistral and some Llama (up to 8%), little in GPT, Gemini, Claude (d14). K25.

**Moderators.**
- Problem set design (crossed vs natural).
- Sorting style (stacker/spreader).
- Who counts as expert (faculty vs PhD student).
- Framing/cueing: in biology the framed condition lifted faculty 71.7 to 83.1% but non-majors only 29.2 to 39.6%; advanced majors sorted like experts only once the framework was shown (d05, d06). Cole 2023: expert-style group names helped all groups (b14, abstract only).
- Model scale and mode: surface sensitivity falls with scale for name/number changes, not for distractors (reasoning models still lose 14 to 20 points on distractor sets, d17). K09.
- Base-model strength for memory methods (d12).

**Interventions that worked.**
- Ignore instruction, distractor exemplars, self-consistency (partial; best GSM-IC macro 45%). K10.
- Skill-matched exemplars (+11.6 on MATH, GPT-4, older baseline).
- Curated abstract memory (large over baseline, but the instruction-only control already reached 36.7).
- Comparing examples with different surfaces and the same structure teaches structural sorting (Quilici and Mayer; Gick and Holyoak; not opened).
- Trained abstraction (AbstRaL, DAGGER): works, but needs fine-tuning.

**Interventions that did not work.**
- 8 shots of the same NoOp question (within one SD, b19).
- Expert personas on accuracy (coefficient 0.004). K17.
- Uncurated full history in memory (26.7, hurt).
- Majority vote of 3 on AIME gave nothing where memory did (weak equal-compute control, d12).
- Code execution (PAL) for robustness to variants (Haiku 4.5, d16).
- Step-Back over strong CoT: GPT-4 +1.6 and +0.3, within spread (c14).

## 6. Language models

**Do LLMs sort by deep structure?** One direct test: Kortemeyer 2025, GPT-5 Thinking, 60 exam items; groups were topic-and-solution method, not surface (d01). One run, no human baseline, prompt already says "similarity of solution", cards not Chi's. It solved 27/30 and 25/30, so there was no headroom to link sort quality to accuracy (d02). Whether sort quality predicts solving item by item: untested (K20).

**Indirect probes of surface pull.**
- Analogy: ARN far analogies 39.6% vs chance 50% and humans 94.1%; counterfactual alphabets humans 75.3% vs GPT 35.0 to 48.8% (b27, b28). Webb 2023: GPT-3 beat students on matrices but was worse on story analogies (odds ratio 0.37) (a23). All older models; reasoning models not retested here.
- Distractors, in time order: davinci-002 macro under 30% (2023); Phi-3-mini -65.7, GPT-4o -32.0, o1-preview -17.5 (2024); R1 error 1.5% to 4.5% under searched triggers (2025). Trend: absolute loss falls with model strength, the relative error multiplier stays 3x to 5x, token use rises 1.5x to 3x.
- Premise order and syntax: over 30% drop on reordered deductive premises (smaller for stronger models); syntax complexity predicts errors in 7-8B models (c01, c18).
- Mechanistic: the model strips entity names by layer 22 and still fails at operation planning (a19). Causal mediation: closed models rely on deep structure (c03, c04). Both "pure pattern matching" (Mirzadeh) and "a schema stage that fails under distraction" (Qu and Gomes) fit; unresolved (K15).

**What changed behaviour, by how much.**
- Principle-first (Step-Back): PaLM-2L +6.8 physics, +10.9 chemistry; GPT-4 +15.1 physics over base but only +1.6 over CoT. It adds 11.9% new errors.
- Skill-labelled exemplars: +11.6 on MATH vs CoT (GPT-4-0613, 42.2 base).
- Abstract memory: AIME 2024 23.3 to 50.0, but 36.7 came from instructions alone.
- Reasoning models: plain CoT adds only marginal accuracy on GPQA Diamond for o3-mini and o4-mini (+0.056 at the 51% metric); Gemini Flash 2.5 fell at strict metrics (d10). Expect a small ceiling for principle-first prompting on frontier reasoning models.
- Trained abstraction: DAGGER cut tokens from 3,128 to 359 at similar accuracy (Bangla maths, small models).
- Rephrasing failed items in simpler syntax: +8 to 12 points on 7-8B models, a selection-biased upper bound.

**Where physics fails.** PHYBench: the first error is a wrong relation or wrong conservation assumption (79% to 96%), not misreading the scene. The weak step is applying the principle, not naming it (consistent with Step-Back's 90%). Wrong-named principle vs none was not measured (K26).

**Memory.** On web tasks distilled strategies beat raw trajectories: WebArena Gemini-2.5-flash 40.5 (no memory), 42.1, 44.1, 48.8 (ReasoningBank), 51.8 with test-time scaling (d13). No study compares skill-key vs surface-key retrieval directly at matched tokens (K23).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Input hygiene is needed for reasoning models too.** Code (not the model) moves numbers or clauses not tied to the question into a marked block before attempts. S1 already says this; the new evidence is that the need persists (error multiplier 3x to 5x, tokens +1.5x to 3x). The prompt-only remedy is not established (see Test first). | S1 | [E] need; [S] remedy | K09, K24; a17, b18, d08, d09 |
| A2 | **Do not read a clean benchmark score as a robustness score.** When measuring S0 or memory, add a NoOp-style distractor variant and a fresh set. Use NoOp, not name/number swaps. | G7 (bench design) | [E] | K09, K25; b18, d14, d15 |
| A3 | **Memory keyed by problem-class label, not by surface text.** Skill-labelled exemplars beat random exemplars; labels from a strong model transfer to weaker ones. Store class label plus a one-line abstract strategy, not the raw problem. Keep lessons shown after the first attempt (existing rule). | memory | [E] direction, [S] size | K12, K19; b26, c06, d11, d13 |
| A4 | **Curate memory. Never append full history** (26.7 vs 50.0). | memory | [E] direction; one setting | K23; d12 |
| A5 | **No expert persona.** Add to 4b: persona prompts do not raise accuracy (coefficient 0.004). | 4b | [E] | K17; c19, c25 |
| A6 | **Test S0 on crossed items.** Natural problem sets cannot separate principle from surface. | G7 (bench) | [E] | K03, K21; a06, b05, d03 |
| A7 | **The "ignore irrelevant information" line is cheap and helps partly. It is not a fix.** Do not rely on same-question shots. | S1 | [E] (old models) | K10; b17, b19 |
| A8 | **Do not add thinking to cure distraction.** Reasoning-model distraction costs 1.5x to 3x tokens; consistent with G11. | G11 | [E] | K24; d09, d17 |

### Test first (goes to UNKNOWNS.md)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Principle-first step (name the governing principle, then solve) at equal tokens vs plain CoT on frontier models. Expect a small ceiling; Step-Back adds 11.9% new errors. | S2 / S0 | [S] | K11; b24, c14, c15, d10 |
| T2 | Cue-then-solve: label the class first, then solve with the label. Cueing (revealing the framework) moved humans; training the sort did not clearly move solving. | S0 | [C] | K07; d06, b12, b08 |
| T3 | Restate in canonical form with distractors flagged (prompt only, current reasoning model). Trained versions work; prompt-only on small models gives +8 to 12 (upper bound). | S1 | [S] | K16, K24; c02, d17, d18 |
| T4 | Class-label key vs surface-similarity key in memory on hard maths at equal tokens. | memory | [S] | K23; d11, d13 |
| T5 | The agent sorts a crossed surface-by-principle set; test per-item link between sort and solve. | S0 | [S] | K18, K20; d01, d02 |
| T6 | Log named principle and its correctness per attempt; compare wrong-named, none, right-named. Human data: 38% wrong names, yet principle users solved 57% vs 14%. | S0 / S6 | [S] | K08, K26; b10, d19 |
| T7 | Self-generated related problems vs retrieved ones in O7. | O7 | [E] small gain | K13; a22, c16 |
| T8 | A strong model labels classes, a weak model uses them. | memory | [S] | K19; c06, c24 |

## 8. Concrete tests on our bench

All arms get the same total tokens, including S0 and setup cost (G7). Use the HTSA harness. Report pass rate with confidence intervals; use 100 or more items per test.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Crossed grid, 5 principles x 5 surfaces, many items per cell; chosen so the plain model fails about half. Include a surface-lure version. | (a) plain CoT; (b) name principle, then solve; (c) sort the set first, then solve with the sort as cue | Accuracy; deep-match rate in the sort; per-item correlation of sort-correct with solve-correct | Small (0 to 4 points) for (b), no more than Step-Back's GPT-4 gain over CoT (+1.6); (c) uncertain |
| B2 | 25 fresh mechanics or maths problems in Mason-Singh / Schoenfeld-Herrmann style, with gold labels from two raters | Agent sorts by "similarity of solution"; compare to gold | Share of items in good categories (human anchors: faculty above grad above calculus 34.4% above algebra 18.7%); group count; double-filing | High agreement with gold (as in Kortemeyer). If not, S0 labelling is unreliable |
| B3 | NoOp-style distractor variants of our math items, plus a fresh set | (a) plain; (b) ignore instruction; (c) code moves flagged clauses to a marked block; (d) restate then solve | Accuracy loss vs clean; tokens | (c) and (d) recover part of the loss; (b) small. Reasoning-model tokens rise 1.5x to 3x under distractors |
| B4 | 100+ hard sequential items (not GSM8K) | (a) no memory; (b) raw-case similarity retrieval; (c) class-label key plus abstract line; (d) instruction-only text of equal length | Pass rate on later items; tokens | (c) above (b); (d) shows how much is the instruction alone (36.7-type effect) |
| B5 | Hard variants where surface suggests the old method (MATH-Perturb style) | (a) plain; (b) show original solution; (c) name method class first | Accuracy on hard variants | (b) misleads; (c) neutral to small gain |
| B6 | Any set with logged principle names | Plain run with a required "state the principle" field | Accuracy for right / wrong / no principle | Human data: wrong-named still above none; LLM unknown |

## 9. What does not transfer, and why

- **Human expertise-gap sizes (78% vs 59%; 71.7% vs 29.2%).** They describe learners with years of different schooling. A model has no such continuum. Use them for item design, not as targets.
- **Stacker/spreader style.** An LLM can be told how many groups to make. Control it by fixing the instruction.
- **"Experts spend more time representing."** For the agent, longer representation costs tokens; G11 says think briefly. The human finding does not justify a longer S2.
- **Training the sort (Schoenfeld course, 5-hour tool).** Our agent has no weight updates. Only the cueing version (show the framework) maps; human evidence on it is mixed anyway (b08 vs b12).
- **Experts add a secondary surface label.** A design hint (keep surface tags as secondary index), untested in models.
- **Persona as "expert".** Did not raise accuracy (K17).
- **"Wrongly named principles still help."** Correlational human data with self-selected groups. For an LLM a wrong name may anchor later attempts (G4, G10). Not established.
- **GSM-Symbolic name/number variance as a surface measure.** Contested after re-analysis (K25).
- **Prompt-paper gains.** Reported numbers, older models, different token budgets. No equal-token comparison exists anywhere in this literature. Gains for GPT-4-class models over CoT are small.

## 10. Open questions

1. Does an LLM sort the Chi and Mason-Singh problems like faculty, and does sort quality predict solving per item? (K20; never tested.)
2. At equal tokens, does a principle-first step beat CoT on frontier reasoning models? (K11; no test found.)
3. Does class-keyed memory beat surface-keyed memory on hard maths at matched tokens, on 100+ items?
4. Does a prompt-only canonical-form step recover NoOp losses on current reasoning models, and at what token cost?
5. Does the sort gap reproduce in non-extreme groups and in maths with crossed items?
6. What is the cost of a wrongly named principle vs naming none? (K26)
7. Does surface sensitivity fall with reasoning mode in 2026 models? Name/number: yes. Distractors: still 14 to 20 points. Frontier 2026 NoOp numbers not found. (K09)
8. Which results survive contamination controls? (GSM8K above centre for 21 of 25 models.)
9. Pattern matching or a failing schema pipeline? (K15; Mirzadeh vs Qu and Gomes.)
10. Why did 2011 intro students sort less by surface than Chi's 1981 novices (curriculum, enrolment, instructions)?
11. Does training the sort transfer to solving (Schoenfeld vs Mestre), and what is the no-training analogue?

## 11. Sources

[V] = full text or substantial text opened this session. [M] = abstract, snippet or second-hand only.

- [M] Chi, Feltovich, Glaser (1981), Cognitive Science 5:121-152. https://doi.org/10.1207/s15516709cog0502_2 (numbers via replications)
- [V] Mason and Singh (2011), Phys Rev ST PER 7, 020110. https://arxiv.org/abs/1602.08781 and https://journals.aps.org/prper/pdf/10.1103/PhysRevSTPER.7.020110
- [V] Mason and Singh (2010), conference version. https://arxiv.org/abs/1602.08775
- [V] Mason and Singh (2016), categorization as instruction. https://arxiv.org/abs/1602.07680
- [V] Wolf, Dougherty, Kortemeyer (2012), empirical approach to card-sorting data. https://arxiv.org/abs/1201.6601 and https://journals.aps.org/prper/pdf/10.1103/PhysRevSTPER.8.010124
- [V] Wolf, Dougherty, Kortemeyer (2012), Rigging the deck. https://journals.aps.org/prper/pdf/10.1103/PhysRevSTPER.8.020116
- [M] Veldhuis (1986/1990). https://eric.ed.gov/?id=EJ409276 (detail via Wolf)
- [M] Singh (2009); Lin and Singh (2010) (via Wolf et al.)
- [M] Keith (via Mason and Singh)
- [V] Schoenfeld and Herrmann (1982). https://files.eric.ed.gov/fulltext/ED200609.pdf
- [V] Hardiman, Dufresne, Mestre (1988/1989). https://files.eric.ed.gov/fulltext/ED294753.pdf (journal DOI https://doi.org/10.3758/BF03197085 not opened)
- [V] Hardiman (1988) fraction word problems (skimmed). https://files.eric.ed.gov/fulltext/ED299146.pdf
- [V] Mestre, Dufresne, Gerace, Hardiman (1988). https://files.eric.ed.gov/fulltext/ED294751.pdf
- [M] Silver (1979, 1981). https://doi.org/10.2307/748918
- [M] Chi, Glaser, Rees (1982). https://doi.org/10.4324/9781315746951
- [M] Larkin et al. (1980). https://doi.org/10.1126/science.208.4450.1335
- [M] Gick and Holyoak (1983). https://doi.org/10.1016/0010-0285(83)90002-6
- [M] Quilici and Mayer (1996). https://doi.org/10.1037/0022-0663.88.1.144
- [M] Rottman, Gentner, Goldwater (2012). https://eric.ed.gov/?id=EJ972104
- [M] Cole et al. (2023). https://eric.ed.gov/?id=EJ1410149
- [V] Smith et al. (2013) biology card sorting task. https://doi.org/10.1187/cbe.13-05-0096
- [V] Bissonnette et al. (2017). https://doi.org/10.1187/cbe.16-09-0273
- [V] Hoskinson et al. (2017), skim. https://doi.org/10.1187/cbe.16-05-0175
- [V] Mirzadeh et al. (2025) GSM-Symbolic. https://arxiv.org/abs/2410.05229
- [V] Shi et al. (2023) GSM-IC. https://arxiv.org/abs/2302.00093
- [V] Li et al. (2024) GSM-Plus. https://arxiv.org/abs/2402.19255
- [V] Huang et al. (2025) MATH-Perturb. https://arxiv.org/abs/2502.06453
- [V] Rajeev et al. (2025) CatAttack. https://arxiv.org/abs/2503.01781
- [V] Zhang et al. (2024) GSM1k. https://arxiv.org/abs/2405.00332
- [V] Dlugosz et al. (2026). https://arxiv.org/abs/2605.28700
- [V] Kutakh (2026). https://arxiv.org/abs/2605.26414
- [V] Qu and Gomes (2026). https://arxiv.org/abs/2609.17804
- [V] Han et al. (2024) causal assessment. https://arxiv.org/abs/2411.19456
- [V] Williamson, Ji, Dwyer (2025) syntactic blind spots. https://arxiv.org/abs/2510.01831
- [V] Chen et al. (2024) premise order. https://arxiv.org/abs/2402.08939
- [V] Zheng et al. (2024) Step-Back. https://arxiv.org/abs/2310.06117
- [V] Didolkar et al. (2024) metacognitive capabilities. https://arxiv.org/abs/2405.12205
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271
- [V] Yang et al. (2025) ReasonFlux. https://arxiv.org/abs/2502.06772
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620
- [V] Yasunaga et al. (2024) analogical prompting. https://arxiv.org/abs/2310.01714
- [V] Yu, He, Ying (2024) Thought Propagation (abstract and intro only). https://arxiv.org/abs/2310.03965
- [V] Webb, Holyoak, Lu (2023). https://arxiv.org/abs/2212.09196
- [V] Lewis and Mitchell (2024). https://arxiv.org/abs/2402.08955
- [V] Sourati et al. (2023) ARN. https://arxiv.org/abs/2310.00996
- [V] Zheng et al. (2024) personas. https://arxiv.org/abs/2311.10054
- [V] Xu et al. (2023) ExpertPrompting. https://arxiv.org/abs/2305.14688
- [V] Kortemeyer (2025) GPT-5 Thinking physics. https://arxiv.org/abs/2508.08842
- [V] Meincke et al. (2025) Prompting Science Report 2. https://arxiv.org/abs/2506.07142
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952
- [V] Ouyang et al. (2026) ReasoningBank. https://arxiv.org/abs/2509.25140
- [V] Al Nazi, Dipta, Kar (2026) DAGGER. https://arxiv.org/abs/2601.06853
- [V] Gao et al. (2026) AbstRaL. https://arxiv.org/abs/2506.07751
- [V] Qiu et al. (2025) PHYBench. https://arxiv.org/abs/2504.16074
- [V] Yang et al. (2025) GSM-DC (numbers in figures, not extracted). https://arxiv.org/abs/2505.18761
- [M] Search finding c23: no LLM replication of Chi found in one completed search.
