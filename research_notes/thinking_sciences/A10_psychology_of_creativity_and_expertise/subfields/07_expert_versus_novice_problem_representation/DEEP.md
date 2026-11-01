# Expert versus novice problem representation: deep document

*Subfield A10.07. Schema part: S2 REPRESENT (also S1 input hygiene, memory retrieval, O6/O7). Built from evidence_a-d.jsonl (a01-a27, b01-b26, c01-c26, d01-d18), claims.jsonl (K01-K22) and critique.md in this folder. Ids like [b09] are evidence ids; K-ids are claim ids (prefix A10.07-). Marks: [V] source text opened this session, [M] snippet, memory or second-hand only.*

**Read this first.** The famous result (experts sort by principle, novices by surface) is real in direction but weaker and more fragile than its citations suggest. The 1981 sample was 8 vs 8, and the experts were graduate students. Later work finds big overlap between groups, and sometimes no difference in standard metrics. The LLM evidence mostly shows that models are captured by irrelevant detail. It does not show that an explicit "type the problem" step helps a current reasoning model at equal tokens. That is the main open question for our S2.

---

## 1. What it is

**The claim.** Experts represent a problem by its deep structure: the governing principle and the conditions under which it applies. Novices represent it by surface features: the objects named in the story (springs, inclined planes, pulleys). The representation chosen decides which solution method is retrieved and tried.

**How it is measured.**
- Card sorting: people group problems "by similarity of solution". Groups are coded as principle-based or surface-based.
- Problem summaries: say what the problem is about in a few words.
- Similarity judgments or forced choice: given a target and two comparison problems (one sharing the principle, one sharing surface objects), pick the more similar. The comparison problems can cross principle and surface, which gives a clean test of capture by surface.
- Think-aloud interviews give the reasons behind each choice.

**Why it matters for our agent.** S2 REPRESENT is the step where the agent decides what kind of problem it has. If a wrong type is chosen, every later state works on the wrong thing. Two questions follow:
1. Does an explicit typing or principle step improve a language model? At equal tokens? For which models?
2. Does the model get captured by irrelevant surface content, and does a representation step stop that?

**What "representation" means in the studies.** Four separable things get mixed together, and the evidence differs by type.
- Categorisation: naming the problem type.
- Retrieval: which earlier problem or method comes to mind (surface-driven in humans, see K16).
- Quantity selection: which given facts matter and which are distractors.
- Applicability conditions: knowing when a principle holds (the Chi account says experts store these).

---

## 2. History and theories in depth

**Before 1981: expert-novice differences in solving.**
- Bhaskar and Simon (1977) [c22, M]: thermodynamics protocols; a semantically rich domain changes solving. Not opened.
- Larkin, McDermott, Simon and Simon (1980, Science) [a04, c20, M]: kinematics think-aloud. Experts work forward from givens in large chunks of equations. Novices work backward from the unknown by means-ends analysis. Small samples. Speed and chunk size differ. Not opened.

**Chi, Feltovich and Glaser (1981) [a01-a03, b01, d01]. The founding study.**
- Experiment 1: 8 novices (just finished one semester of calculus-based mechanics) and 8 physics PhD students sorted mechanics problems. Instruction: sort by similarity of solution, multiple categories allowed, no pencil.
- Novice categories (as reproduced by Mason and Singh [d01], second-hand, original paywalled and not opened): angular motion 87.5%, springs 75%, center of mass 62.5%, inclined planes 50%, kinetic energy 50%, pulleys 37.5%, Newton's second law 0%, energy 0%.
- Expert categories: Newton 2, energy, momentum and non-circular angular motion 75% each; circular motion 62.5%; center of mass 62.5%; statics 50%.
- Another account [b01] gives novices springs 75%, inclined plane 50%, kinetic energy 50%, pulleys 38% and experts springs 25% and none of the others on surface labels. The problem set is lost; only 7 problems are known.
- Later experiments (as recalled, not verified [a02]): experts' summaries state the principle and the conditions for applying it; novices state objects and given quantities.
- Theory [a03]: experts hold problem schemas that bundle a principle, its applicability conditions and the method. Novices index by surface entities. Representation decides the solution path. Qualitative; no formal model.

**Chi, Glaser and Rees (1982) [a05, M].** Summary chapter. Experts spend more time building the representation and less on calculation (exact times not verified).

**Adelson (1981) [a23, M] and Weiser and Shertz (1983) [a24, M].** Same direction in programming: experts group by function or structure, novices by syntax or surface. Not opened. K01 relies on them.

**Schoenfeld and Herrmann (1982) [a07, b15, M].** Mathematics faculty vs students, before and after a course. After a month-long problem-solving course, student sorting moved toward structure. Only citation context seen. This is the only training result in the series (K17).

**Gick and Holyoak (1980, 1983) [a21, M].** Spontaneous analogical transfer is rare (about 10% recalled) and jumps with a hint (about 75% recalled). Numbers unverified. Ross (1984) [a22, M]: reminders are driven by surface similarity, but learning also stores structure. Gentner, Rattermann and Forbus (1993) [a25, M]: surface similarity drives retrieval; structural similarity drives judged soundness. Forbus, Gentner and Law (1995) [c23, M]: MAC/FAC, a cheap surface-based first pass followed by a structural second pass.

**Hardiman, Dufresne and Mestre (1989) [a06, b09-b11].** Agent b marked it opened; the critique pass could not retrieve the paper. Numbers are reported by agent b: likely, not verified. It is the central complication. Novices are not pure surface sorters, and representation quality predicts solving among novices (section 3).

**The challenge phase (2009-2016).**
- Wolf, Dougherty and Kortemeyer (2012) [b06, b07, V]: 18 professors vs 23 novices, 50 problems. Standard metrics did not separate the groups. Sorting style dominated.
- Mason and Singh (2016) [b02-b05, d01, V]: large classes pick far more expert categories than Chi's novices did. Faculty beat graduate students by a wide margin, so Chi's "experts" were not at the top of the expertise range.
- Engle and Chi (2002) [b12, V]: separation scores in a related sorting task showed no reliable differences between doctoral students, single majors and double majors.

**LLM phase (2022-2026).** Mostly not a replication of card sorting (only Kortemeyer 2025 [a10] tries it). It tests surface capture (GSM-IC, GSM-NoOp, cats, long irrelevant context), principle-first prompting (Step-Back), skill labels for exemplar selection, and abstraction under counterfactual changes.

**Competing explanations of the sorting gap.**
1. Schema theory (Chi): experts have principle-indexed schemas.
2. Task and item-set effects (Veldhuis [b08]; Wolf [b07]): which problems are on the cards decides the result. In Wolf's analysis, chapter, procedural task type and difficulty explained most of the explainable discrimination.
3. Personal sorting style (Wolf [b06]): the first principal component was "stacker vs spreader", not expertise.
4. Level of expertise ("experts" being grad students) (Mason and Singh [b03, b04]).
5. Instruction and intent: the instruction said "solution"; some students know the principle but choose a surface label on purpose (think-aloud [b05]).

---

## 3. Core findings with exact numbers

Status: **E** established (several independent sources, opened), **S** single-source, **C** contested, **U** unverified original (numbers second-hand or from memory).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Experts sort by principle, novices by surface (original) | 8 PhD vs 8 novices. Novices: angular motion 87.5%, springs 75%, center of mass 62.5%, inclines 50%, KE 50%, pulleys 37.5%, Newton 2 and energy 0%. Experts: Newton 2, energy, momentum 75% each | Chi 1981 via Mason and Singh [d01, b01] | C, U (original unopened) |
| Same direction in code and maths | not recorded | Adelson 1981, Weiser and Shertz 1983, Schoenfeld and Herrmann 1982 [a23, a24, a07] | U |
| Large intro classes pick expert categories far more than Chi novices | Chi novices 0% Newton 2; M&S version II: 18% Newton 2, 31% energy, 44% linear kinematics, 28 to 59% circular/angular. Classes 109, 114 (algebra), 180 (calculus) | Mason and Singh 2016 [b02, d01] | E (K02) |
| Standard sorting metrics do not separate experts from novices | Categories: experts 10.8 ± 4.5, novices 11.4 ± 4.4 (as reported by agent b; not found in the critique's text extract). KS tests on graph metrics: no difference. PCA first two components about 87% of variance; PC1 is stacker vs spreader | Wolf et al. 2012 [b06] | E (K02) |
| Problem features explain only part of the discrimination | 35.9% (5-problem subsets), 42.7% (10-problem). By feature: chapter 41.4%, procedural task type 30.4%, difficulty 22.8%, other 5.4%. Easy problems discriminate better than hard | Wolf et al. 2012 [b07] | S |
| Expertise is a distribution | Mean share of 25 problems in good categories: calculus group 34.4%, algebra group 18.7%. Two algebra classes did not differ (p=0.90). 21 grad students, 7 faculty. Faculty far above grad students; calculus students overlap grad students | Mason and Singh 2016 [b03, b04] | S (K03) |
| Deep-structure choice in forced similarity task | Experts 78%, novices 59% (F(1,53)=28.78, p<.0001). Neutral items: experts 91%, novices 87% | Hardiman et al. 1989 [b09] | S, U |
| Surface lures hurt both groups, novices more | Surface-trap items: experts 66%, novices 26% (95% CI 20-32%, well above the 0% a pure surface rule predicts) | Hardiman 1989 [b09] | S, U (K05) |
| Representation quality predicts solving among novices | Groups surface 17, mixed 16, principle 11 (N=44). Score 14%, 32%, 57%, F(2,41)=16.19, p<.0001. Principle use vs score r=.63; partial r=.505 (maths ability out); .613 (SAT-M). Categorisation correct 56%, 63%, 69%; experts 95% | Hardiman 1989 Exp. 2 [b10] | S, U (K04) |
| Naming a principle is not applying it | Principle users named an inappropriate principle 38% of the time; used a cited principle correctly about 60% of the time. Experts cited principles 93-98%; novices 70% (principle group), 23% (mixed), 6% (surface group) | Hardiman 1989 [b10, b11] | S, U |
| Other sorting domains show no reliable difference | Separation scores doctoral .58, single majors .53, double majors .73; no reliable differences | Engle and Chi 2002 [b12] | S (preliminary) |
| Analogical transfer is rare unprompted | about 10% spontaneous, about 75% with hint | Gick and Holyoak 1980/83 [a21] | U |
| Strong LLM sorts physics items by method | 60 items from two finals; one run; author-coded. Same model 27/30 and 25/30 on the exams, 24/26 (92.3%) on TUG-Kv4.0. Novice-role prompts changed tone, not method | Kortemeyer 2025 [a10, a11] | S (K06) |
| One irrelevant sentence wrecks consistency (2022 GPT-3 family) | GSM-IC-4K, code-davinci-002, CoT: micro 72.4%, macro 6.0% (macro = base problem solved under all distractors). Least-to-most: micro 77.5%, macro 18.0% (tripled) | Shi et al. 2023 [b19, c01, c02] | E (K07, K08) |
| Distractor fixes help, do not cure | Exemplars with irrelevant context: CoT micro 76.8%, macro 14.0%. Self-consistency (20 samples): micro +11 points. LTM + SC: micro 93.4%, macro 45.0%. Role-overlap distractors drove text-davinci-003 macro to 0 on problems with more than 2 steps | Shi et al. 2023 [b20, c02] | E (K08) |
| NoOp clauses cut accuracy in many models | Up to 65% drop (Phi-3-mini); o1-preview -17.5; Gemma-7b-it -20.6; Mistral-7b-v0.3 -24.0. Eight shots of the same question did not fix it. Best-to-worst instantiation gap above 12% for some models. More than 20 open models plus GPT-4o-mini, GPT-4o, o1-mini, o1-preview | Mirzadeh et al. 2025 [a17, b21, c03, c04] | E (K07) |
| Reasoning models: smaller absolute harm, still present | R1 error 1.50% to 4.50% with adversarial cat sentence (3.0x); R1-distill-Qwen-32B 8.00% (2.83x); trigger factors 5.14x (Qwen3-30B-A3B), 3.61x (Phi-4-reasoning), 1.15x (QwQ-32B), 7.21x (Mistral-Small-24B). Response length doubled in at least 16% of cases | Rajeev et al. 2025 [d03] | S |
| Long irrelevant context cuts accuracy and reasoning length | IMOAnswerBench drop: Qwen3.5-27B 12%, gpt-oss-120b 9%, Gemini 3 Flash 15%, Kimi K2 9%; reasoning length down up to 74%; a few hundred distractor tokens cut Qwen3.5-27B reasoning by 18%, larger inserts by 50% | Rodionov et al. 2026 [d02] | S |
| Distractor math in Bangla hurts small reasoning models | CoT Qwen2.5-3B 53.7% to 13.0% on MSVAMP (-40.7). Qwen3-8B 71.4% weighted accuracy, drop 14.2-19.9, 3,128 tokens/problem. Related-entity distractors give 46-94% error | Nazi, Dipta, Kar 2026 [d04] | S |
| A typed graph that marks distractor nodes (fine-tuned) cuts the drop and tokens | DAGGER Gemma-3 12B GRPO: 69.4%, 359 tokens (89% fewer). Distractor annotations +2.9 (4B), +5.0 (12B) on distractor split, +0.1/+0.6 on original | Nazi et al. 2026 [d04] | S |
| Perturbed math benchmarks | GPT-4 drop rate 8.23%; CodeLlama 7B/13B/34B 40.56/39.71/34.27% | Li et al. 2024 GSM-Plus [d16] | S |
| Step-Back (principle first) on MMLU physics | PaLM-2L 66.4 base / 65 CoT / 73.2 Step-Back. GPT-4 69.4 / 82.9 / 84.5. Llama2-70B 51.9 / 59.3 / 64.8. Fixes 20.5% of baseline errors, adds 11.9%; over 90% of remaining errors are in the reasoning step | Zheng et al. 2023 [b16, b17, c05, c06, critique] | S (K09) |
| Step-Back on MMLU chemistry | PaLM-2L 70.9 / 75.3 / 81.8. GPT-4 80.9 / 85.3 / 85.6. GPT-4 gain over CoT only +1.6 (physics) and +0.3 (chemistry) | Zheng et al. 2023 [critique] | S (K09) |
| Step-Back on knowledge tasks | TimeQA +27, MuSiQue +7 (PaLM-2L); TimeQA base GPT-4 45.6%, PaLM-2L 41.5% | Zheng et al. 2023 [c07, a12] | S |
| Skill-labelled exemplars beat topic labels | MATH GPT-4: CoT 42.2; +11.6 over CoT, +3.5 over Complex CoT and over topic-based. PAL variant +7.52. Mixtral MATH: topic-based 26.14 vs skill-based 28.44 (single sample); maj@4 30.75 vs 32.44 | Didolkar et al. 2024 [c08, c09, d09, d10] | S (K10) |
| Skill gains shrink as the base model strengthens | GSM8K GPT-3.5: retrieval 76.8 vs skill-based 82.03 (+5.2). GPT-4: CoT 93.00, random 92.87, skill-based 94.31 (+1.3), maj@5 95.38 | Didolkar et al. 2024 [d09] | S |
| Diverse (structure-covering) demonstrations beat similarity retrieval where similar examples are insufficient | Up to +23 absolute (SMCalFlow-CS 50.3 to 73.5, Codex), fewer demonstrations needed | Levy et al. 2023 [d11] | S |
| Self-generated analogues help a little | Average +4% over 0-shot and few-shot CoT. Codeforces GPT-3.5 Acc@1 8% to 15%; GPT-4 16% to 17%. MATH GPT-3.5 33.0 (5-shot) vs 33.9-37.3 | Yasunaga et al. 2024 [a14, b25, c10] | S (K11) |
| Structure-first decomposition and self-composed structure | Least-to-most 99%+ vs 16% CoT on SCAN with 14 exemplars. Self-Discover PaLM 2-L CoT 60/40/42 vs 67/69/50.5; GPT-4 75/52/71 vs 81/85/73 (BBH/T4D/MATH: +6, +33, +2). Beats CoT-SC by over 20% with 10-40x less compute | Zhou et al. 2023, 2024 [a15, c13, d08] | E (K12) |
| Buffer of Thoughts | GPT-4: +11% Game of 24, +20% Geometric Shapes, +51% Checkmate-in-One vs Meta-prompting; 12% of multi-query cost; distiller ablation lowers accuracy (bigger on Game of 24 and Checkmate) | Yang et al. 2024 [c14] | S |
| Cheap re-read or rephrase gives small gains | RE2 (davinci-003): vanilla arithmetic +3.81, commonsense +2.51, symbolic +1.85; with CoT +2.22, +1.23, +5.25. Rephrase and Respond: marginal where question is clear | Xu et al. 2024; Deng et al. 2024 [c11, c12] | E (K13) |
| Counterfactual variants hurt models, not humans | 136 human participants, 3 GPT models, 40 symbol-alphabet problems; humans above every GPT model on all alphabet types. GPT-3 beat humans on digit matrices (OR 1.88, p=0.005, N=40) and lost on story analogies (OR 0.37, p=0.0003, N=54); far-analogy choice not significant (p=0.065) | Lewis and Mitchell 2024; Webb et al. 2023 [c16, b24] | E (K14) |
| ConceptARC | Humans over 90% on 11 of 16 concepts, over 80% on the rest. First-place Kaggle program below 60% on 11 of 16. GPT-4 below 30% on 15 of 16 | Moskvichev et al. 2023 [c18] | S |
| Content leaks into logic in models and humans | Humans call invalid syllogisms valid 90% of the time when the conclusion is believable (as cited). Effects small in NLI, moderate in syllogisms, larger on Wason | Lampinen et al. 2024 [a20, b23] | E (K15) |
| Prompt format moves scores | Up to 76 accuracy points (LLaMA-2-13B), about 10 on average across 50+ tasks. Kendall's W across paraphrases about .71-.91 (175+ paraphrases) | Sclar et al. 2024; Mizrahi et al. 2024 [c19, d14] | E (K15) |
| Extra reasoning on easy items is waste | 1,953% more tokens on "2+3" for o1-like models; first round correct in over 92% of cases; QwQ ASDIV first round 287 tokens, 38.7% of the response | Chen et al. 2025 [d05] | E (K19) |
| Verbalisation can hurt on pattern tasks | Artificial grammar learning: GPT-4o 94.0% vs o1-preview 57.7% (-36.3, p<0.0001) | Liu et al. 2025 [d15] | S |
| CoT helps mainly on math and symbolic | Top three categories +14.2, +12.3, +6.9 points; average with CoT 56.9 vs 45.5 without | Sprague et al. 2025 [d06] | S |
| Stated reasoning is not always the cause | Reasoning models used planted hints at least 1% of the time yet verbalised them under 20% in most settings. Faithfulness varies by task and size | Chen et al. 2025; Lanham et al. 2023 [d13, d12] | C for our use (K21) |

---

## 4. Mechanisms and models

No formal computational model of the original sorting effect was fitted [a03]. These are the working mechanisms the evidence supports, written so they can be built.

### 4.1 Schema with applicability conditions (Chi account)
- Data structure: `Schema = {principle, conditions[], method, typical_surfaces[]}`.
- Matching: a problem matches a schema if its conditions hold, not if its objects resemble `typical_surfaces`.
- Expert summary = principle plus conditions. Novice summary = objects plus givens.
- Engineering version: S2 outputs a record `{type, why_it_applies (conditions checked), givens_used, givens_ignored}`. Code can check `givens_ignored` against the problem text.
- Evidence limit: Hardiman [b10] found that naming a principle is not enough (38% wrong-principle naming among principle users, about 60% correct application). The conditions field matters more than the label.

### 4.2 Forward vs backward search (Larkin et al.)
- Experts apply chunked rules forward from givens. Novices work backward from the unknown by means-ends analysis.
- Engineering: not an S2 feature. It is a solve-strategy choice and belongs with O5 (work backwards) and S3. Not tested in LLMs here.

### 4.3 Surface-driven retrieval, structure-driven judgment (MAC/FAC, Gentner)
- Stage 1 (MAC): cheap similarity on content vectors. Fast, favours surface overlap.
- Stage 2 (FAC): structural alignment over the shortlist. Slow, favours relational match.
- Engineering for agent memory: embed the problem, take top-k (k about 10-20), then re-rank by a structural label or a structure-mapping check. This is hypothesis K16 [M]; the Levy [d11] and Didolkar [d09] results point the same way but do not test it directly.

### 4.4 Distractor capture and input hygiene
- Failure: a quantity or entity from an irrelevant sentence gets used in the calculation (GSM-IC role-overlap distractors are worst [c02]).
- Counter 1, prompt level: "Feel free to ignore irrelevant information given in the questions" [c02]. Worked without hurting clean accuracy.
- Counter 2, structured extraction: list every quantity with its role (used / unused), then solve from the used list. DAGGER does this with a typed graph that includes distractor nodes; it is fine-tuned [d04].
- Counter 3, code check: code verifies that each number in the solution appears in the `givens_used` list and that nothing flagged ignored is used. No LLM study has tested this exact check. It fits G5 and G10.
- Counter 4, sampling: self-consistency lifted GSM-IC micro accuracy by more than 11 points [c02]. G4 says samples from one model are not independent, so treat as partial.

### 4.5 Principle-first abstraction (Step-Back)
- Two calls: (1) "What principle or concept governs this question?" (2) answer using that principle. Very few exemplars are needed [b18].
- Failure case: step 1 gives a wrong or irrelevant principle (11.9% new errors in physics). Over 90% of the residual errors lie in the reasoning step [b17]. Abstraction fixes a minority of errors.

### 4.6 Skill-labelled exemplars (Didolkar)
- Offline: a strong model labels each training problem with a fine-grained skill (not a topic). Build an index from skill to examples.
- Online: the model names the skills the new problem needs; fetch exemplars by skill; solve.
- Gain shrinks with a stronger solver (GPT-3.5 +5.2 vs GPT-4 +1.3 on GSM8K [d09]). Label quality depends on the annotator model (annotator comparison in the paper's appendix, not read [d10]).

### 4.7 Diverse structure coverage (Levy et al.)
- Choose demonstrations so each structural component of the target is covered, not just the nearest neighbours by text. Helps where similar examples cannot cover the target.

### 4.8 Self-composed structure (Self-Discover, Buffer of Thoughts)
- Self-Discover: select, adapt and implement generic reasoning modules into a plan; then follow the plan. 10-40x fewer calls than CoT-SC.
- Buffer of Thoughts: distil a thought-template from a solved problem; retrieve a template for new ones. Distiller ablation lowers accuracy [c14]. Template reuse can hit a poor match.

### 4.9 Gating
- Run the representation step only where it can pay: items where surface and structure can diverge, and where the plain pass rate is not high. Easy items waste tokens [d05], and verbalisation can hurt on pattern tasks [d15]. Gating by class pass rate is what S0 already does.

---

## 5. What holds up

**Holds up (several sources, opened).**
- The direction of the sorting gap exists in some item sets, but the size depends on items and coding rules (K01, K02).
- Expertise is graded. Faculty differ from grad students; strong calculus students overlap grad students (K03, single source).
- Surface lures hurt both experts and novices; novices are not purely surface-bound (K05; Hardiman numbers not re-opened in the critique).
- LLMs are captured by irrelevant material. Measured with GSM-IC (2022 models), GSM-NoOp (2024 models), cats (2025 reasoning models), long context (2026 models). The effect persists in reasoning models but is smaller in absolute terms (K07).
- Distractor fixes (ignore instruction, exemplars with distractors, self-consistency, least-to-most, typed graphs) help but never remove the problem (K08).
- LLM abstraction is tied to familiar content: counterfactual alphabets, arbitrary rules and story analogies hurt (K14).
- Prompt wording alone moves scores, up to 76 points (K15).
- Deliberation on easy items wastes tokens (K19).

**Failures and null results.**
- Wolf et al.: no difference between 18 professors and 23 novices in category counts or graph metrics [b06]. Sorting style dominated.
- Engle and Chi: no reliable group differences [b12].
- Mason and Singh: Chi's 0% Newton-2 novices are not representative; large classes choose Newton 2 18%, energy 31% [b02].
- Kortemeyer: the author calls the paradigm notoriously difficult to replicate [a10].
- Step-Back on GPT-4: +1.6 (physics) and +0.3 (chemistry) over CoT; physics introduces 11.9% new errors (relative to baseline errors) [critique].
- Eight shots of the same NoOp question did not fix NoOp [b21].
- Novice-role instructions changed tone, not method [a11].
- No exact replication rate for the original card sort has been found [a26]. The original paper could not be opened.

**Moderators.**
- Item set: whether principle and surface are crossed (Veldhuis rigged grids [b08]; Wolf features [b07]).
- Free vs forced choice: free sorting shows weaker effects; forced similarity choice shows novice deep-structure choices of 59% [b09].
- Expert definition: grad students vs faculty [b03].
- Course level and instruction.
- Model strength: Step-Back, skill exemplars and Self-Discover all gain less on GPT-4 than on weaker models [critique, d09, d08].
- Distractor type: role-overlap distractors are the worst [c02]. Related-entity distractors cause 46-94% error in small models [d04].
- Prompt format: up to 76 points [c19].

**Interventions that worked** (nearly all on older or weaker models).
- Ignore-irrelevant instruction, distractor exemplars, self-consistency, least-to-most for GSM-IC [c02, b20].
- Principle-first prompt for weak models on physics and chemistry (PaLM-2L, Llama2-70B) [c05].
- Skill-labelled exemplars on MATH [c08] and with GPT-3.5 on GSM8K [d09].
- Diverse demonstrations where similar ones are insufficient [d11].
- Typed distractor graph with fine-tuning [d04].
- Month-long training course moved human sorting toward structure [b15, unopened].

**Interventions that did not work or were marginal.**
- Plain "solve grade school math problems" instruction [c02].
- Re-read and rephrase: small gains (+1.2 to +5.3), marginal where the question is clear [c11, c12].
- Step-Back on strong models.
- Few-shot prompting for R1 (authors report it hurts; no number given) [d07].
- Role-playing as a novice [a11].

---

## 6. Language models

**Do models classify like experts?**
- Only direct test: Kortemeyer 2025 [a10, V]. GPT-5 Thinking clustered 60 multiple-choice items from two exams by solution method, in one run, coded by the author. The same model scored 27/30 and 25/30 on those exams and 24/26 (92.3%) on a separate concept test (TUG-K). Telling the model to behave like a novice changed tone, not the method. Limits: one model, one run, no matched human group, original Chi cards unavailable.
- No second LLM card-sort replication was found. The search budget ran out and the APIs returned 429 errors, so "none found" means "not located" [d18, c26, a27].

**Are models captured by surface?** Yes, and this is the best-measured part.
- GSM-IC (2022): CoT micro 72.4% vs macro 6.0%; LTM 77.5% vs 18.0%; best mix (LTM + SC) macro 45.0% [b19, b20].
- GSM-NoOp (2024): up to -65% (Phi-3-mini), o1-preview -17.5, Gemma-7b-it -20.6, Mistral-7b-v0.3 -24.0 [c03]. The authors' reading, "pattern matching rather than reasoning", is contested: o1-style models lose far less (critique).
- GSM-Plus (2024): GPT-4 drop 8.23%; CodeLlama 34-41% [d16].
- Reasoning models (2025-2026): R1 1.5% to 4.5% on adversarial cat sentences; relative multiple 3.0x but only +3 points absolute [d03]. Long irrelevant context: -9 to -15% on IMOAnswerBench with reasoning length cut up to 74% [d02]. Small multilingual reasoning models: -14 to -20 points [d04]. These use adversarial or very long inputs, so they are worst cases, not natural noise.

**What changed it, and by how much.**

| Intervention | Model | Change | Source |
|---|---|---|---|
| Ignore-irrelevant instruction | code-davinci-002 | helps; exact number not extracted | [c02] |
| Distractor exemplars | code-davinci-002 | CoT macro 6.0 to 14.0 | [b20] |
| Least-to-most | code-davinci-002 | macro 6.0 to 18.0; micro 72.4 to 77.5 | [b19] |
| LTM + self-consistency | code-davinci-002 | micro 93.4, macro 45.0 | [b20] |
| Step-Back | PaLM-2L physics | 66.4 to 73.2 (CoT 65) | [b16] |
| Step-Back | GPT-4 physics | 69.4 to 84.5 (CoT 82.9; +1.6 over CoT) | [critique] |
| Step-Back | GPT-4 chemistry | 80.9 to 85.6 (CoT 85.3; +0.3 over CoT) | [critique] |
| Skill exemplars | GPT-4 MATH | +11.6 over CoT, +3.5 over topic labels | [c08] |
| Skill exemplars | GPT-3.5 GSM8K | +5.2 over embedding retrieval | [d09] |
| Skill exemplars | GPT-4 GSM8K | +1.3 | [d09] |
| Self-Discover | GPT-4 | BBH +6, T4D +33, MATH +2 over CoT | [d08] |
| Self-generated analogues | GPT-3.5 Codeforces | 8% to 15% | [c10] |
| Diverse demonstrations | Codex | up to +23 where similar examples insufficient | [d11] |
| DAGGER typed graph (fine-tuned) | Gemma-3 12B | 69.4%, 359 vs 3,128 tokens | [d04] |
| RE2 | davinci-003 | +1.2 to +5.3 | [c12] |

**Where models behave unlike experts.**
- Counterfactual tasks: the human curve is flat, GPT curves fall [c16, c25]. Webb et al. found the opposite on some tasks (GPT-3 above humans on digit matrices, OR 1.88); samples, prompts and models differ.
- ConceptARC: GPT-4 below 30% on 15 of 16 concepts, humans above 80% on all [c18]. Text-only, no reasoning models.
- Analogy in context: GPT-3 missed the analogous story among distractors and found it once told to consider earlier stories (mirrors Gick and Holyoak) [d17, qualitative; supplementary not opened].
- Content effects in logic as in humans [a20].

**Is the representation causal for the answer?** Unknown for LLMs. A written label may not drive the answer: larger models rely less on stated chains [d12] and reasoning models verbalise planted hints under 20% of the time [d13]. No forced-wrong-label experiment was found (K21).

**Does S2 typing help a current reasoning model at equal tokens?** No direct test found (K18, contested). Indirect signals lean toward a small or zero effect: CoT helps mainly math and symbolic tasks [d06]; gains from structure steps shrink as the base model gets stronger [d08, d09]; the R1 authors say few-shot prompts hurt [d07]. No study here compares typing against a plain call at a matched reasoning-token budget.

---

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| N1 | **Input hygiene for distractors.** Code lists every number and entity in the problem; S1/S2 states which are used and which are irrelevant. Keep the original wording beside the restatement (already in S1). Add the "ignore irrelevant information" sentence to the S2 prompt. | S1 / S2 | [E] that distractors hurt (K07) and that fixes help but do not cure (K08). The specific wording effect is from older models only | b19, b20, c02, c03, d03 |
| N2 | **Code checks quantity use.** After a numeric solve, code confirms that the numbers used are in the `givens_used` list and that no ignored quantity appears. | S4 / G5 | [E] by construction (G5, G10); the specific check is untested | c02, d04, K08 |
| N3 | **Gate S2 by difficulty.** Skip the full S2 typing step in direct mode and on classes with a high plain pass rate. | S0 / G11, G12 | [E] (K19) | d05, d15 |
| N4 | **Report macro accuracy as well as micro** on perturbed items. A base problem solved under every variant is the real measure of robust representation. | bench | [E] | b19 |
| N5 | **Test across 2-3 wordings.** Meaning-preserving re-wording changes scores by up to 76 points on some models; flag answer disagreement rather than trusting one wording. | G | [E] (K15) | c19, d14 |
| N6 | **A cheap restate is a default, not a deep step.** Expect a small gain (+1 to +5). | S1 | [E] (K13) | c11, c12 |
| N7 | **Do not add novice-role or expert-role prompts.** Role prompting changed tone, not method. | S2 | [S], consistent with the spirit of 4b | a11 |
| N8 | **Do not claim S2 gains on item sets where surface and structure agree.** Build the principle-by-surface grid first. | bench design | [E] (K02) | b02, b06, b07, b08 |

### Test first (not yet in schema)

| # | Item | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|---|
| T1 | **S2 type-and-conditions step vs plain call at equal reasoning tokens**, on a current reasoning model. | S2 | [C] (K18) | d06-d09, b16 | Biggest gap. Prior gains are on weak or older models. |
| T2 | **Restate-and-strip vs plain CoT on distractor items** at equal tokens. | S1/S2 | [S] (K07/K08) | c02, d04 | Fixes were tested on 2022 models; DAGGER is fine-tuned. |
| T3 | **Forced S2 labels (right, wrong, absent)** injected by code. | S2 / G10 | [C] (K21) | d12, d13 | Is the label causal? Decides whether S2 is worth its tokens. |
| T4 | **Structure-labelled vs surface-embedding retrieval** of lessons and exemplars at equal context. Also broad retrieval plus structural filter. | memory | [S] (K10, K16) | d09, d11 | Gain shrank from +5.2 to +1.3 with a stronger model. |
| T5 | **Look-for-structural-match step** when a stored case exists among surface-similar decoys. | S2 / O7 | [S] (K22) | d17 | Mirrors Gick-Holyoak; only GPT-3 tested. |
| T6 | **Gated vs always-on S2** to find the break-even. | S0 / S2 | [S] (K19) | d05, d15 | Direction known; no threshold. |
| T7 | **Self-generated analogue with code verification** vs unverified. | O7 | [S] (K11) | c10, a14 | Self-generated exemplars can be wrong. |
| T8 | **Our own card sort**: several current models, repeated runs, fixed coding rules, crossed item set. | S2 (diagnostic) | [S] (K06) | a10 | Tells us whether models already represent by structure. |
| T9 | **Self-label quality on code tasks** vs human structural labels. | S2 | open | d10 | No data. |

---

## 8. Concrete tests on our bench

All arms at equal total tokens (reasoning plus output plus any setup call), counted per G7. Report cost per correct item. At least 3 repeats per arm and item; paired comparison by item.

**B1. S2 typing vs plain (T1).**
- Items: 60 or more problems from a principle-by-surface crossed set (math word problems, short physics items, code tasks). Half with a surface lure, half neutral.
- Arms: (a) plain call; (b) plain with the extra tokens given to a longer reasoning budget; (c) S2 step (type, conditions checked, quantities used) then solve.
- Metric: accuracy, macro accuracy over lure variants, tokens per correct.
- Expected: small positive on lure items, near zero on neutral items, based on GPT-4 +0.3 to +1.6 over CoT. If the current model matches arm (b), S2 fails G7.

**B2. Distractor handling (T2).**
- Items: base problems with 1 to 3 added irrelevant sentences, including role-overlap and related-entity distractors. Report micro and macro.
- Arms: plain; plain with "ignore irrelevant information"; restate and strip irrelevant clauses; code-checked quantity extraction.
- Metric: macro accuracy, tokens.
- Expected: the ignore instruction recovers part of the loss (older-model direction); extraction adds more on weak models; on strong reasoning models the baseline drop is small (+3 points for R1), so gaps may be within noise.

**B3. Forced-label test (T3).**
- Items: those from B1 with known correct type.
- Arms: code-injected correct type; code-injected wrong type (same surface, wrong principle); no type; model-chosen type.
- Metric: accuracy; share of solve steps that cite the label; accuracy when the label is wrong.
- Expected: if wrong labels cut accuracy sharply and the solve step cites the label, S2 is causal and label quality matters. If accuracy barely moves, S2 is decoration (G10).

**B4. Retrieval by structure (T4).**
- Items: tasks where a stored lesson or solved case could help; memory of 200+ solved cases, each with a surface embedding and a structural label.
- Arms: surface-embedding top-k; label top-k; embedding top-20 then structural re-rank to k; random.
- Metric: accuracy at equal context size.
- Expected: label or hybrid beats embedding by a few points on weaker models and about +1 on stronger ones.

**B5. Structural-match prompt (T5).**
- Items: problem pairs with a solved source problem hidden among 3-5 surface-similar decoys.
- Arms: unprompted; "check whether any earlier problem has the same structure; state the mapping" with code checking the mapping.
- Metric: rate of choosing the right source; downstream accuracy.
- Expected: large prompted gain, as in the Gick-Holyoak hint effect; size unknown for LLMs.

**B6. Gating (T6).**
- Items: stratified by plain pass rate (easy, medium, hard).
- Arms: always-on S2; never; gated by class pass rate below a threshold.
- Metric: accuracy and tokens by stratum.
- Expected: no gain on easy items, gain concentrated in the hard stratum.

**B7. Own card sort (T8).**
- Items: 50 problems on a 5x5 principle-by-surface grid.
- Arms: 3 or more current models, 5 repeats each, coding rules fixed before running, two independent coders or a code classifier.
- Metric: share of sorted groups matching principle; agreement with surface grouping; run-to-run variance; sensitivity to 3 wordings.
- Expected: models sort mostly by principle on clean items (as in Kortemeyer) and drift toward surface on lure items.

**B8. Counterfactual variants.** Re-run B1 items with changed alphabets, rules or units. Expect a drop for models and a smaller drop with S2. This checks K14.

---

## 9. What does not transfer, and why

- **Memory organisation.** Chi's account is about long-term memory structure built by years of study. A model has no equivalent schema build-up inside one episode. We can only mimic the output (a typed record), not the store.
- **Card sorting as a test.** Sorting is a similarity judgment without solving. Models do it in text, without cards or time cost, so the human effect size means little for them.
- **Novice behaviour as a model.** Prompting a model to act as a novice changes tone, not method [a11]. Models are not novices in the Chi sense.
- **The 8 vs 8 effect sizes.** They come from tiny samples with graduate students as experts. Do not use them as expected gains.
- **Forward vs backward search.** Larkin's strategy difference depends on practiced equations. Not shown to transfer to LLM chains of thought.
- **Training courses.** Schoenfeld and Herrmann's month-long course has no analogue for a frozen model. Our agent can only use lessons in memory, which is not changed knowledge.
- **Self-explanation as a driver.** In humans the stated reason is partly causal (Hardiman think-alouds). In models, stated reasoning is often not what drives the answer [d12, d13].
- **Older-model gains.** Step-Back on PaLM-2L, GSM-IC on code-davinci-002 and skill exemplars on GPT-3.5 are on models with weaker built-in structure use. Gains shrink on GPT-4-class models and are untested on 2025-2026 reasoning models.
- **Adversarial distractors.** Cat sentences [d03] are optimised against the model; natural distractors are milder.
- **Fine-tuned fixes.** DAGGER and Abstraction-of-Thought are trained; we use a scaffold, not training.

---

## 10. Open questions

1. Does a typing or principle step help a current reasoning model at equal tokens (K18)? No direct test.
2. Do several current models sort by method over repeated runs on crossed item sets (K06)? One model, one run so far.
3. Is representation causal in LLMs (K21)? No forced-label study found.
4. What are the true Chi 1981, Hardiman 1989, Gick-Holyoak, Ross and Schoenfeld-Herrmann numbers? Originals are unopened or paywalled.
5. Do self-generated type labels agree with human structural labels on code (Adelson, Weiser and Shertz analogues)?
6. Where is the break-even when surface and structure agree (Ross)? Direction known, no threshold.
7. Does structure-labelled retrieval beat embedding retrieval for agent memory at equal context?
8. Does distractor harm persist under natural (non-adversarial) conditions for 2025-2026 reasoning models, and is restate-and-strip worth its tokens there?
9. How robust is expert-like categorisation to prompt format (Sclar-style swings)? Not tested for sorting.
10. How much of the LLM distractor effect is pattern matching and how much is truncated reasoning (Rodionov: reasoning length falls up to 74%)?
11. Do models show a stable sorting style across runs (Wolf's stacker vs spreader)?
12. Does Webb's GPT-3 analogy result (above humans on matrices, below on stories) hold for recent reasoning models?

---

## 11. Sources

Marks: [V] opened (text enough to extract numbers) this session; [M] snippet, memory or second-hand only. Hardiman is marked [M] because agent b claimed it opened but the critique pass could not retrieve it.

**Human studies**
- Chi, Feltovich, Glaser (1981) Categorization and representation of physics problems. https://doi.org/10.1207/s15516709cog0502_2 [M] (numbers via Mason and Singh)
- Larkin, McDermott, Simon, Simon (1980) Expert and novice performance in solving physics problems. https://doi.org/10.1126/science.208.4450.1335 [M]
- Chi, Glaser, Rees (1982) Expertise in problem solving. https://doi.org/10.1007/978-1-4615-7284-9_2 [M]
- Bhaskar, Simon (1977) Problem solving in semantically rich domains. https://doi.org/10.1207/s15516709cog0102_2 [M]
- Schoenfeld, Herrmann (1982) Problem perception and knowledge structure. https://doi.org/10.1037/0278-7393.8.5.484 [M]
- Adelson (1981) Problem solving and the development of abstract categories. https://doi.org/10.3758/BF03197722 [M]
- Weiser, Shertz (1983) Programming problem representation. https://doi.org/10.1016/S0020-7373(83)80022-3 [M]
- Hardiman, Dufresne, Mestre (1989) The relation between problem categorization and problem solving. https://doi.org/10.3758/BF03202824 (agent a) and https://doi.org/10.3758/BF03197085 (agent b); the DOI differs between files, check before citing [M]
- Gick, Holyoak (1980, 1983). https://doi.org/10.1016/0010-0285(80)90013-4 [M]
- Ross (1984). https://doi.org/10.1016/0010-0285(84)90006-9 [M]
- Gentner, Rattermann, Forbus (1993). https://doi.org/10.1006/cogp.1993.1002 [M]
- Forbus, Gentner, Law (1995) MAC/FAC. https://doi.org/10.1207/s15516709cog1902_1 [M]
- Veldhuis (1986, 1990), Singh (2009), Lin and Singh (2010), as summarised in Wolf et al. https://doi.org/10.1103/PhysRevSTPER.8.010124 [M]
- Wolf, Dougherty, Kortemeyer (2012) Empirical approach to interpreting card-sorting data. https://doi.org/10.1103/PhysRevSTPER.8.010124 (arXiv 1201.6601) [V]
- Wolf, Dougherty, Kortemeyer (2012) Rigging the deck. https://doi.org/10.1103/PhysRevSTPER.8.020116 [V]
- Mason, Singh (2016) Categorization of mechanics problems by students. https://arxiv.org/abs/1602.08775 [V]
- Mason, Singh (2016) Assessing expertise in introductory physics using categorization. https://arxiv.org/abs/1602.08781 [V]
- Engle, Chi (2002) Categorization of emergent processes. https://escholarship.org/uc/item/0rw099pt [V]

**LLM and AI studies**
- Kortemeyer (2025) The Boiling-Frog Problem of Physics Education. https://arxiv.org/abs/2508.08842 [V]
- Zheng et al. (2023) Take a Step Back. https://arxiv.org/abs/2310.06117 [V]
- Shi et al. (2023) LLMs can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093 [V]
- Mirzadeh et al. (2025) GSM-Symbolic. https://arxiv.org/abs/2410.05229 [V]
- Li et al. (2024) GSM-Plus. https://arxiv.org/abs/2402.19255 [V]
- Rajeev et al. (2025) Cats confuse reasoning LLM. https://arxiv.org/abs/2503.01781 [V]
- Rodionov et al. (2026) Reasoning Shift. https://arxiv.org/abs/2604.01161 [V]
- Nazi, Dipta, Kar (2026) DAGGER. https://arxiv.org/abs/2601.06853 [V]
- Chen et al. (2025) Do not think that much for 2+3. https://arxiv.org/abs/2412.21187 [V]
- Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183 [V]
- DeepSeek-AI (2026 v2) DeepSeek-R1. https://arxiv.org/abs/2501.12948 [V]
- Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620 [V]
- Zhou et al. (2023) Least-to-most prompting. https://arxiv.org/abs/2205.10625 [V]
- Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271 [V]
- Hong et al. (2024) Abstraction-of-Thought. https://arxiv.org/abs/2406.12442 [V]
- Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714 [V]
- Didolkar et al. (2024) Metacognitive capabilities of LLMs. https://arxiv.org/abs/2405.12205 [V]
- Levy, Bogin, Berant (2023) Diverse demonstrations. https://arxiv.org/abs/2212.06800 [V]
- Deng et al. (2024) Rephrase and Respond. https://arxiv.org/abs/2311.04205 [V]
- Xu et al. (2024) Re-reading (RE2). https://arxiv.org/abs/2309.06275 [V]
- Lewis, Mitchell (2024) Counterfactual tasks. https://arxiv.org/abs/2402.08955 [V]
- Webb, Holyoak, Lu (2023) Emergent analogical reasoning. https://arxiv.org/abs/2212.09196 [V]
- Wu et al. (2024) Reasoning or reciting. https://arxiv.org/abs/2307.02477 [V]
- Moskvichev et al. (2023) ConceptARC. https://arxiv.org/abs/2305.07141 [V]
- Lampinen et al. (2024) Content effects. https://arxiv.org/abs/2207.07051 [V]
- Sclar et al. (2024) Spurious features in prompt design. https://arxiv.org/abs/2310.11324 [V]
- Mizrahi et al. (2024) State of what art. https://arxiv.org/abs/2401.00595 [V]
- Liu et al. (2025) Mind your step (by step). https://arxiv.org/abs/2410.21333 [V]
- Lanham et al. (2023) Measuring faithfulness in chain-of-thought. https://arxiv.org/abs/2307.13702 [V]
- Chen et al. (2025) Reasoning models don't always say what they think. https://arxiv.org/abs/2505.05410 [V]

**Related subfields run in parallel (links only, not covered here):** Expert-novice schemas; Expert-novice differences; Chunking and templates; Schemas; Analogical retrieval (MAC/FAC); Analogical inference; Candidate inferences; Retrieval and similarity; Einstellung effect; Fixation and ideation; Representational change theory; Worked-example effect; Expertise reversal; Transfer of learning; Decomposition (Fermi-ize); Hierarchical task networks; Overthinking; Test-time compute scaling; External representations and diagrams.
