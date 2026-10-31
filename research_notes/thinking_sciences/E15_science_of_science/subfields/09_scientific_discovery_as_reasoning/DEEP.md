# Scientific discovery as reasoning: deep document

*Subfield E15.09. Focus: hypothesis and experiment spaces, anomalies. Key works: Klahr and Dunbar 1988; Langley's BACON. Schema link: S3 GENERATE, S4 TEST, S5 REVISE, S7 SELECT. Evidence ids a01-a29, b01-b27, c01-c29, d01-d22 are in evidence_a.jsonl to evidence_d.jsonl in this folder. Claim ids E15.09-K01 to K29 (written "K01" below) are in claims.jsonl. critique.md is the cross-check audit; its corrections are applied here.*

*Reading note.* Klahr and Dunbar 1988 was opened in full text for Study 1 and Study 2 (d01-d03). Klayman and Ha 1987 was opened (d04). Klahr, Fay and Dunbar 1993 is only second-hand through Klahr 1994 (a04, a05) and its group rates are unverified (K18). Wason 1960 was never opened; its numbers come from a 2026 paper. Almost all LLM evidence is 2026 preprints with no outside replication. Treat every LLM number as "one group, one benchmark" unless a line says more. Benchmarks mix 2022-2024 models with 2026 models, so scores do not compare across rows.

## 1. What it is

Scientific discovery as reasoning asks how a mind finds a rule it was not told. Klahr and Dunbar's answer: discovery is problem solving, with search in two linked spaces (a01).

- **H-space (hypothesis space).** All candidate rules or theories. The goal state is a hypothesis that accounts for the known facts in a more concise or universal form.
- **E-space (experiment space).** All tests you can run. Each test is a probe: set the world up, look at the result.
- **Evidence evaluation.** Compare what the hypothesis predicted with what happened. Decide: keep, change, or stop.

Two events matter most for an agent.

1. **Choosing a test.** Which probe, in which setting, separates the live rules?
2. **Meeting an anomaly.** A result that does not fit the held hypothesis. Keep it, patch it, or drop it?

Where it sits in our schema. S3 GENERATE makes hypotheses (H-space). S4 TEST runs candidates on checks (E-space plus evaluation). S5 REVISE handles a failed test. S7 SELECT holds the counterexample step: "if two rules still fit, run the one input where they differ." This subfield bears on how S3 and S4 are coupled, how S7 picks a discriminating test, and what S5 does with a result that contradicts the held rule.

Scope of this document:

- Human studies: BigTrak (Klahr and Dunbar 1988; Klahr, Fay and Dunbar 1993), MilkTruck (Schunn and Klahr 1992, 1995), Trickett et al. 1998, Dunbar and Schunn 1990, Wason 2-4-6, Klayman and Ha 1987.
- Machine discovery: BACON (Langley 1979), AI Feynman, LLM-SR, robot scientists.
- LLM studies 2022 to 2026: rule games (WILT, FalsifyBench, Failing to Falsify), discovery environments (ScienceWorld, DiscoveryWorld, NewtonBench, DiscoverPhysics, PhysGym, BoxingGym, Auto-Discovery-Bench), harnesses (SHELDON, EvoSCM, PiEvo, AutoSciLab, LLM-IDEA, Little Scientist), trace audits (Rios-Garcia et al.), hypothesis search (Hypothesis Search, HypoGeniC, Phenomenal Yet Puzzling), idea generation (Si et al., AI Scientist).

Links to other subfields (not covered here): Heuristic programming and machine discovery; Discovery case studies; Information-theoretic motivation; Expected value of sample information; Bayesian conditionalization; Systematicity; Debugging strategies; Framing and reframing; Model-based versus model-free control; Heuristic search (A*, best-first); Program induction, language of thought; Spectrum-based fault localisation; Metacognition and control.

## 2. History and theories in depth

### 2.1 Wason's 2-4-6 task and the confirmation story (1960 onward)

Wason's task. People see the triple 2-4-6 and are told it fits a hidden rule. They propose triples and hear yes or no. The true rule is "any increasing sequence." People test triples that fit a narrow guess (such as "even numbers going up by two"), always hear yes, and never learn the rule is broader (a09). The classic reading: people confirm, they do not try to falsify.

Wason 1960 was not opened. The only counts we have come from a 2026 paper that reports a human sample (a09, b20, c04, the same N=29 in all four lines): 6 of 29 announced the right rule first time; 21 of 29 found it eventually. Mean incompatible-to-compatible test ratio (I:C) was 1.79 for first-announcement-correct and 0.24 for first-announcement-wrong. Among the first-wrong, those right on the second announcement had I:C 0.50, the rest 0.19. Limits: tiny sample, ratios without significance tests, and it is not a replication of Wason's own numbers. No failed replication of the 2-4-6 result was found in any opened source.

### 2.2 Klayman and Ha (1987): positive testing is not always a bias

Primary text opened (d04). They split two things people had run together. A **positive test** is a case you expect to have the target property. A **negative test** is a case you expect not to. The question is which can falsify hypothesis H when the true rule is R.

- H broader than R (a superset): a positive test can falsify H.
- H a strict subset of R: a positive test can never falsify H. Only a test outside H can. This is the 2-4-6 situation.
- Target rare (p(t) < .5) and H about the right size (p(h) near p(t)): positive tests are more likely to falsify than negative ones (their Eq. 2). Examples they give: schizophrenia prevalence under 1%, AIDS incidence in the US.
- Tweney et al. (1980): telling people the data came from DAX (the rule) versus MED (everything else) greatly raised 2-4-6 success, because it induced tests of both.
- They list replications of the positive-test tendency (Mahoney, Mynatt et al., Taplin, Tweney et al., Wason and Johnson-Laird) and say people do not follow positive testing strictly when given enough test opportunities.

This is the central boundary condition for the whole subfield. "Confirm less" is not a law. The right test depends on how H sits inside R and how rare the target is (K23). The Wetherick/Wason 1962 exchange is cited only second-hand and was not read.

### 2.3 BACON and machine discovery (Langley 1979 onward)

BACON.3 (a07, a08) is a production system of about 86 OPS2 rules in seven sets. It looks for constancies and trends in data, defines new terms (products and ratios), and builds higher levels of description, so a hypothesis at one level becomes data at the next. It gathers data by a factorial design, varying one variable at a time.

- Rediscovered five laws: ideal gas, Kepler's third, Coulomb's, Ohm's, Galileo's.
- Ideal gas path: pV constant at fixed n and T; then pV/T slope 8.32; then pV/nT = 8.32.
- Productions fired: gas 1203, Kepler 1119, Coulomb 1297, Galileo 1150, Ohm 4593. Terms defined: 8, 17, 18, 9, 31 (redundant terms 2, 1, 12, 7, 84).
- Order of data collection changed the path, not the law. Pendulum: irrelevant variables varied first were found irrelevant at once; varied last, the same laws came with more computation. Heuristic use by task: "ignore differences" in 4 tasks, "collapse descriptions" in 5, "different experiments" in 2, "irrelevant variables" in 1.
- Limits: clean data, variables chosen by the programmer, no test on data BACON was not built for, one reorder per law, no statistics. Noise handling is a tolerance that ignores small differences. The ceteris-paribus assumption is a known weak point (c24).

Descendants. AI Feynman (c23) keeps the recursive cut-the-space idea (symmetry, separability, compositionality) with neural fitting: 100 of 100 Feynman Lectures equations versus 71 for earlier software, on clean noise-free data that LLMs have probably seen. Robot scientists (c25): Adam abduced hypotheses from a Prolog knowledge base and planned its next experiment (6 genes for orphan yeast enzymes); Eve used active learning with Gaussian process regression (TNP-470 against Plasmodium vivax). Modern LLM versions replace the fixed heuristics with an LLM that proposes forms and a numeric engine that fits them (section 4.7).

### 2.4 Klahr and Dunbar (1988): SDDS and the BigTrak study

Paradigm (a02). People learn a programmable toy tank, BigTrak, until all share a criterion. Then they must find what a new RPT key does by writing programs. They are never told if they are right. They decide when to stop.

**Study 1 (original paper opened, d01-d03).** N = 20 CMU undergraduates; 19 found the rule. They left the wrong frame ("RPT's number is a counter") by one of two routes.

| | Experimenters | Theorists | Test |
|---|---|---|---|
| Group size | 13 | 7 | |
| Time (min) | 24.46 | 11.40 | t(18)=3.97 |
| Experiments | 18.33 | 9.29 | t(18)=3.09 |
| Experiments with no stated hypothesis | 6.08 | 0.76 | t(18)=3.70 |
| Different hypotheses | 4.92 | 3.06 | ns, p<.08 |
| Hypothesis switches | 4.76 | 3.00 | ns, p<.07 |

Combined: 19.40 min, 15.20 experiments, 4.55 hypotheses, 4.15 switches. 364 programs were written, 304 were experiments. One Table 5 cell was garbled in extraction (Theorists, experiments with hypotheses); do not quote it.

Experimenters found the rule by running an experiment in the informative region ("region III") and reading the result. Theorists found it by searching memory for a new frame. Both work. The Theorist route took half the time and half the experiments (K22).

**Disconfirmation handling (Table 4, d02).** Across 220 outcomes with a stated hypothesis:

- 21 of 84 confirming outcomes led to rejection (25%).
- 76 of 136 disconfirming outcomes led to retention (56%). Only 60 of 136 (44%) led to a change.
- Chi-square 8.16, p<.005, so responses were not random.
- By group: Experimenters 17 reject-after-confirm, 43 retain-after-disconfirm, 44 reject-after-disconfirm; Theorists 4, 20, 16.
- The authors give reasons for retention: feedback was sometimes wrong (memory and observation errors), subjects repeated the same experiment to check, and some encoded disconfirming results as confirming. So not all retention is stubbornness.

**Positive testing (d03).** Subjects almost always used a positive test, yet about 60% of experiments disconfirmed the hypothesis. The authors tie this to Klayman and Ha: positive tests work when confirmation is unlikely. Study 1: 4.6 (SD 1.3) different hypotheses per subject; 55% of experiments ran under one of 8 common hypotheses, 3% under partial ones, 28% under no stated hypothesis.

**Study 2 (d03).** 10 adults, hypotheses stated first. 7 of 10 switched to the selector frame in phase 1; 5 of 10 proposed the correct rule; in phase 2 all 10 solved it (mean 6.2 min, 5.7 experiments, 2.4 hypotheses). Theorists (4): 3.3 min, 3.0 experiments. Experimenters (6): 8.2 min, 7.5 experiments. All 4 Theorists and 1 Experimenter had programming experience, so the split may reflect experience, not style. Groups are tiny.

### 2.5 Klahr, Fay and Dunbar (1993): children and plausibility

Second-hand from Klahr 1994 (a04, a05); group sizes unknown; unverified (K18). Subjects got a Given rule that was wrong; the Actual rule was plausible or implausible, and the Given was somewhat wrong (same frame) or very wrong (different frame).

- Actual rule discovered by 83% of CMU undergraduates, 65% of community college students, 53% of 6th graders (mean age 11), 33% of 3rd graders (mean age 9).
- Implausible actual rule: 56% of adults versus 13% of children; 0% of third graders.
- In the 1988 comparison, children mostly failed but most were sure they had the right rule and stopped satisfied. Time, hypotheses and experiments were similar to adults (a02).

**Four domain-general E-space heuristics (a05):**

1. Use the plausibility of the current hypothesis to choose a strategy (confirm or disconfirm).
2. Focus on one dimension of an experiment or hypothesis at a time.
3. Maintain observability: design runs whose outcome you can read.
4. Design experiments that give characteristic results (many distinct commands).

Adults used all four and handled conflicts among them. Children dropped them or let one dominate. Third graders did not try to keep experiments observable; sixth graders and adults did. Plausibility was set by a frame, so the effect is partly knowledge, not only domain-general skill.

### 2.6 MilkTruck, complexity management and the 4-space model (Schunn and Klahr 1992, 1995)

MilkTruck is a much harder BigTrak (b01-b04). 22 CMU undergraduates; 16 solved, mean 85 min (range 30-179 for solvers). 1103 experiments over 33 hours. It needed about 6 times the programs and 2.5 times the time of the BigTrak studies. Quit-group subjects ran slightly more experiments than Solve (Bonferroni t(19)=2.94, p<.05).

- **Small steps.** New programs changed on average 1.77 features versus the last program (a random experimenter 2.49; t(21)=-15.8, p<.0001). Versus the best of the last 7 programs: 1.33 (random 1.45; p<.002). Both still above 1 (p<.0001): people vary few features but too many to compare cleanly. Causal direction unclear; group differences overall not significant (F(2,19)<1).
- **PUSH (put upon stack heuristic).** When stuck on one case, switch to another and come back. Seen in all 3 Solve subjects among 5 protocol subjects, in none of the others. Anecdotal scale.
- **Growth.** Program length rose in 21 of 22 subjects (mean r=.56).
- **4-space proposal (1995).** Over 100 subjects. Two spaces (hypothesis, experiment) are not enough; add data representation and experimental paradigm. Subjects redescribed outcomes with new features and invented new kinds of experiment. This was a proposal; no direct test of 4-space against 2-space. Baker and Dunbar (1996) dispute the count; not opened.

### 2.7 Exploring the experiment space without hypotheses (Trickett, Trafton and Raymond 1998)

30 undergraduates, 3 binary variables, 8 possible experiments, chance of right answer .33 (b05, b06). Systematic coverage of the experiment space went with correct solutions. Only 3 people used explicit VOTAT (vary one thing at a time). Right answer plus right reason: identical-task condition .45, .36, .27, .36, .45 over five tasks (N=11, no learning); isomorph condition .29, .50, .42, .79, .71 (N=14, rising). Over 80% of identical-condition people were nearly always right or nearly always wrong from the start. Early representation errors were never revised. No feedback was given. Lesson: success can come from covering E-space, not from stated hypotheses; a hypothesis-first view is incomplete.

### 2.8 Transfer of disconfirmation experience (Dunbar and Schunn 1990)

60 McGill undergraduates in three groups of 20 (b08). Genetics mechanism found: No-Virus 7 (35%), Correlated-Virus 7 (35%), Negative-Virus 12 (60%). 12 of 16 who solved the virus problem solved genetics; 0 of 4 who did not. The initial negative-regulation hypothesis appeared in 4 (Correlated) versus 11 (Negative). Nobody mentioned the virus problem, so the authors read it as priming, not conscious analogy. The Correlated-Virus control argues against general skill transfer. Single study, biology-trained students.

### 2.9 Klahr's own critique and instruction follow-ups

Klahr (1994) says two spaces are not enough (a06). A full account needs an instrumentation space, a representation space and a communication space. Machine discovery systems assume data are given and ignore motivation and social context. This is a position statement, not a measured result. Klahr and Simon (1999, Psychological Bulletin 125:524), the review tying human studies to BACON-style systems, was not opened (a29). Klahr and Nigam (2004, direct instruction versus discovery for the control-of-variables strategy) and Alfieri et al. (2011, meta-analysis of discovery-based instruction) were not opened (b26, b27), so we have no number on whether telling a learner the design strategy beats letting it discover one. This matters for an agent (section 10).

### 2.10 Anomalies

The focus names anomalies. Dunbar's real-world lab studies, Kuhn, and Chinn and Brewer's response categories (ignore, reject, exclude, hold in abeyance, reinterpret, peripheral change, theory change) were not in the evidence. What we have for humans: Klahr and Dunbar's 56% retention of disconfirmed hypotheses, with part of it rational (d02). What we have for LLMs is in section 6.3: ignoring dominates. No source tests a Kuhn-style intervention (a contradiction log, forced decision per anomaly).

## 3. Core findings with exact numbers

Status key: E = established (2+ independent sources), S = single source, C = contested. Claim ids K01-K29 are in claims.jsonl. Lines a09, b20, c04, b19 describe one human sample (N=29). Lines a11, b23, c05, c06, c07, c29, d05 are one source (Bertolazzi et al.).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Humans solve BigTrak by two routes | 19 of 20 solved; 13 Experimenters, 7 Theorists; 24.46 vs 11.40 min; 18.33 vs 9.29 experiments | d01, K22 | S (one lab; primary text) |
| Humans keep disconfirmed hypotheses | 76 of 136 disconfirming outcomes retained (56%); 21 of 84 confirming outcomes rejected (25%) | d02, K22 | S (primary text), partly rational |
| Positive tests still falsify when confirmation is unlikely | about 60% of BigTrak experiments disconfirmed | d03, d04, K23 | E |
| Positive testing is best for a rare target and right-sized H; only negative tests work for too-narrow H | Eq. 2 of Klayman and Ha | d04, a10, K23 | E |
| Success falls with younger age and implausible true rule (humans) | 83 / 65 / 53 / 33%; implausible 56% adults vs 13% children, 0% 3rd grade | a04, K18 | S, unverified |
| MilkTruck is hard; people change few features | 16 of 22 solved, mean 85 min; 1.77 features changed (random 2.49) | b01, b02, K19 | S |
| Covering E-space beats stated hypotheses | right answer and reason stays .45 over 5 identical tasks (N=11); .29 to .71 with isomorphs (N=14) | b05, b06, K19 | S |
| Disconfirmation experience carries to a new task | genetics solved 35 / 35 / 60%; 12 of 16 virus solvers vs 0 of 4 | b08, K20 | S |
| Human baseline on 2-4-6 | 6 of 29 right first time; 21 of 29 eventually; I:C 1.79 vs 0.24 | a09, b20, c04, K02 | S (small, 2026 restatement) |
| LLMs confirm more and find the rule less | rho = -0.779 (p=.003, 12 models) between confirming share and success; success 6% to 78% over 11 models | a11, c06, a12, K01 | E |
| Test strategy predicts conclusive falsification | rho = -0.937 (p<.001); best GPT-OSS-20B 59.2%, worst Llama-4-Maverick 18.0% | c07, d05, K02 | S, correlational (12 points) |
| Reasoning models confirm less | instruct 66-82% confirming; GPT-5-Mini 39.0%, GPT-5.2-Chat 27.3%, GPT-OSS-20B 24.2%; success GPT-5.2-Chat 75%, GPT-OSS-120B 68%, best instruct DeepSeek-V3.1 41%, others 33-35% | a11, c05, K01, K04 | C (see 5.4) |
| Small reasoning models can be worse than all instruct | GPT-5-Nano 12%, Qwen3.5-9B 21% | a11, c05 | S |
| Oracle errors do not explain it | 1,200 games; confirming coefficient -4.15 (OR 0.016); oracle error -0.12 (OR 0.885), interval spans zero | c06, d05, K15 | S |
| FalsifyBench tests only the "H inside R" case | H inside R in more than 50% of turns for almost all models | d05, c07, K23 | S (design caveat) |
| Counterexample prompts lift success on average | 42% to 56%; Think-in-Opposites up in 11 of 11 model-modes; Dual-Goal in 8 of 11; I:C up in 18 of 22 | a12, c02, b21, K03 | S |
| Prompt effect depends on model type | thinking: Dual-Goal +0.148 (p<2e-5), TiO +0.123; non-thinking: Dual-Goal -0.060 (p=.0065), TiO +0.063 (p=.0033) | b21, K03 | S |
| Prompts cost tokens | Qwen3-32B thinking 1029.8 to 1450.0 tokens per turn under TiO | d06, K03 | S (not equal-token) |
| Strong models gain little | Gemini-2.5-Pro 0.73 to 0.78 (TiO), 0.78 (Dual-Goal) | a12, d06 | S |
| Thinking gains are not mainly more falsifying tests | success rises without a steady rise in I:C | d07, a12 | S |
| Falsification behaviour can be distilled, weaker than prompting | Blicket: Qwen3-32B base 0.57, TiO prompt 0.86, distilled with base prompt 0.77; Qwen3-8B 0.32 to 0.34-0.38 (TiO prompt 0.40) | c03, d07, K17 | S |
| WILT: hidden-rule games are hard | Claude 3.5 Sonnet 14/50 (28%); o1-mini 13; o1-preview 12; chatgpt-4o-latest 11; GPT-4o 9; Llama 3.1 405B 8; Haiku 1; Gemini 1.5 Flash 8b 0 | a13, c08, b24, K04, K15 | S |
| Sycophantic partner suppresses human discovery | 557 recruited, 504 final; random control 29.5%; disconfirming 14.1%; agreeable 11.8%; confirming 8.4%; default GPT 5.9%; chi2(4)=28.02 | a14, K05 | S |
| Confirming vs disconfirming partner: not significant | 8.4% vs 14.1%, p=.143 | a14 | C |
| Hypothesis generation is the bottleneck | ARC 100 tasks, GPT-4: direct 17%, program-only 23%, summarised 30%, human-selected 33%, human-written 45%, Icecuber 43%; correct hypothesis on 49, of which 33 (67%) gave correct programs; 28 of 30 solved had a correct hypothesis before summarising | a16, c18, K07 | E |
| Hypothesis update against data helps | HypoGeniC update vs none +0.7, +5.8, +8.1, +7 points; pool of 20 beats 3; older models | b15 | S |
| At large pool size selection loss nearly equals generation loss | ARC-AGI-2 public, 167 instances: pool oracle 144 (86.23%), final 128 (76.65%); 22 generation misses, 17 selection misses | d15, K07 | S (heavy ensemble) |
| Propose with LLM, apply with code | MiniSCAN: LM as interpreter drops accuracy from over 80% to near zero; ACRE direct 28.0% to 59.0% with refinement | c19, c20, K14 | E |
| End-to-end discovery fails while single steps succeed | DiscoveryWorld challenge completion 18% (ReAct) vs humans 66%; unit tests ReAct .60, Hypothesizer .64; DiscoveryBench best 25%; ScienceAgentBench best 32.4% (42.2% o1-preview self-debug); ScienceWorld 0.17 | a15, b10, b11, a24, b14, a23, K06 | E |
| Explicit hypothesis memory alone: mixed | Hypothesizer knowledge .34 vs ReAct .25 easy, .19 vs .14 normal, .08 vs .10 challenge; completion .08 vs .18 challenge | a15, b10, c17, K08 | C |
| Separate observation store helps (own tasks) | SHELDON DiagnosisArena 84 to 70 without it; ORCA 66.67 to 53.33 | a21, c13, d14, K16 | S |
| Comparative analysis drives verdicts | comparative observations 16-17% of observations but 43-53% of verdicts; 93-98% cited later | c14, K16 | S |
| Agents ignore contradicting evidence | evidence non-uptake 68%; beliefs never updated 71%; refutation-driven revision 26%; untested claims 53%; 25,000+ runs, 8 domains | d09, d10, K24 | E in direction (two groups; LLM-assisted labels) |
| Base model dominates scaffold | variance: base model 41.4%, scaffold 1.5%, environment scope 30.1% | d09, K24 | S |
| Failure type differs by model | Opus 4.7 mostly experiment design (8) and noise dismissal (4); GPT-5.5 mostly hypothesis class (9) and ODE integration (8) | d10, K25 | S |
| Discriminating test choice beats random | EvoSCM GPT-5.5: 75.09 full vs 47.45 random action; population K=4 74.86 vs K=1 63.27; pass@1 7.27% to 56.36% | d11, d18, d10, K26 | E direction, S size (authors' own benchmarks) |
| Hypothesis-conditioned acquisition beats LLM-only | AutoSciLab GRN exact recovery 31.11% vs 0.00% (LLM-only, code-assisted), random 2.22%, uncertainty 4.44% | d18, K26 | S |
| Code tool hurts strong models, helps weak | NewtonBench GPT-5 75.9 to 73.3; Gemini-2.5-flash 50.6 to 40.9; DeepSeek-R1 43.4 to 37.4; GPT-4.1 5.8 to 18.9 | d08, c16, K09 | S |
| Tiny noise breaks law discovery | noise 0.0001 cuts accuracy 12-16%; data fit stays stable | c16, d08, K09 | S |
| More experiments is not better | GPT-4.1 80.6 experiments per task (5.8% accurate) vs Gemini-2.5-pro 15.3 (65.4%) | d08 | S |
| Test choice near ceiling, conclusion is the loss (causal graphs) | optimal target 93% vs heuristic 96%; restating the graph cost 0.32 F1; pre-computed z gives 94% vs rule 96% | d17, K27 | S (abstract only) |
| Computed identifiability check rescues explanation | 15 of 15 accurate-trajectory runs failed explanation in non-identifiable worlds vs 5 of 9 in identifiable (p=0.012); depth 3+ on 8/8 seeds vs 1/8 | d19, K27 | S |
| Priors help on average, can trap on some items | PhysGym Gemini-2.5-flash 65.98 / 49.48 / 36.08 / 30.93% from L1 to L4; env 716 solved only at L3-L4 | d16, K28 | C |
| BoxingGym: domain context often does not help | GPT-4o Error@10 with prior / without: Death Process -1.06/-1.04; Peregrines -0.57/-0.65; Hyperbolic Discounting 0.87/1.04; Location Finding 0.59/0.86 | a22, b12, c10, K10 | C |
| Prediction before run and forced reconcile | 49 straight no-gain runs under loose prompt; later 17 of 64 iterations improved (26.6%); five fixes changed at once | d13 | S (anecdotal) |
| Equation discovery: LLM prior plus numeric fit | LLM-SRBench best symbolic accuracy 31.5% / 28.1%; data-blind 2-7%; LLM-SR about 2.5K iterations vs 2M+; E. coli OOD NMSE 0.0037 vs above 1 | b18, c21, c22, K12 | E |
| BACON-style heuristics rediscover simple laws on clean data | 5 laws, 1119-4593 productions; AI Feynman 100/100 vs 71 | a07, c23, c24, K13 | E |
| LLM ideas rated more novel, not more feasible | novelty 4.84 human, 5.64 AI, 5.81 AI plus rerank (119 human / 109 AI reviews, p<0.05); feasibility 6.61 vs 6.34 (ns); about 200 of 4,000 seed ideas unique; best LLM judge 53.3% vs 56.1% human | a18, b16, K11 | S |
| Autonomous loops yield unchecked claims | reviewer 65% vs 66% balanced accuracy; early version hallucinated an ablation table | a19, c26, K21 | S |
| Static surprise bookkeeping overcounts novelty | 37.5% of claimed surprises derivable from earlier findings | d20 | S |
| History tracking is a separate bottleneck | small undirected graphs: Grok-4 and Gemini-2.5-pro 100%, GPT-4o 30%, Qwen2.5 0% as size grows | d21 | S (partly extracted) |

## 4. Mechanisms and models

Each model is described so an engineer can build it. Pseudocode is plain. Nothing here is a schema change until its test passes (see UNKNOWNS.md).

### 4.1 SDDS: dual search

State: hypothesis set H, experiment log E with results, focal hypothesis h.

```
loop:
  if no h: h = search H-space            # memory, analogy, or pattern in data
  e = search E-space for a test          # chosen by h and the heuristics in 4.2
  r = run(e)
  verdict = compare(predict(h, e), r)    # confirm, disconfirm, unclear
  if verdict == disconfirm: revise or replace h    # humans keep h about 56% of the time
  if verdict == confirm and no rival fits: stop
```

Two entry routes (d01):

- **Theorist route.** Search H-space first; take a hypothesis from memory; test it. Fast, cheap. Needs a frame in memory.
- **Experimenter route.** Search E-space first; run varied tests with no hypothesis (about 6 in Study 1); induce a hypothesis from the pattern. Slow, but works when memory offers no frame.

Implementation: make entry a code choice. If the problem class has a known frame library, hypothesise first. If not, run a short exploration set, then hypothesise from the pattern. Untested for LLMs.

### 4.2 Four E-space heuristics (a05) as code checks

1. **Plausibility switch.** Plausible h: allow a test that looks for confirmation of its core claim. Doubtful or implausible h: require a test that could break it.
2. **One at a time.** Count variables changed against the baseline or last run. Warn or reject if more than one changes, unless exploring. Humans change about 1.77 features per MilkTruck step, so this is an upper-end habit, not a rule (b02). Interaction effects need multi-factor tests (BACON varies one at a time and so cannot see them in one step).
3. **Observability.** Reject tests whose result cannot be read from logged output.
4. **Characteristic results.** Prefer tests whose outcome differs sharply across the live hypotheses.

No LLM study scores these. Treat as untested design.

### 4.3 Klayman and Ha test-type rule

Given H and a belief about R:

- H may be a strict subset of R (too narrow): only tests outside H can falsify. Force a negative test.
- H may be broader than R, or R is rare and H is about R's size: a positive test is at least as informative.
- General implementation that covers both cases without knowing the set relation: code enumerates candidate hypotheses that disagree, builds an input where two of them disagree, and runs it (a discriminating test).

```
def discriminating_test(H, pool):
    best = max(pool, key=lambda x: pairs_disagreeing([h.predict(x) for h in H]))
    return best if disagreement(best) > 0 else None   # None = H not identifiable on this pool
```

### 4.4 Discriminating-test selection (EvoSCM, AutoSciLab, BMD pattern)

```
H = small population of explicit candidate models        # K=4 beat K=1: 74.86 vs 63.27 (d11)
for x in candidate_experiments:
    preds[x] = [m.predict(x) for m in H]
    score[x] = expected_information_gain(H, preds[x])    # or count of disagreeing pairs
x_star = argmax(score)
r = run(x_star)
H = reweight_or_prune(H, r); if all fit poorly: add new model
```

The LLM proposes models and candidate experiments. Code scores and picks. In EvoSCM the two largest ablation losses were removing the explicit model (75.09 to 48.18) and removing discriminative action (to 47.45) (d11). AutoSciLab agrees: acquisition conditioned on rival hypotheses beat random, uncertainty, LLM-only and code-assisted LLM (d18). Caution: both ablations compare against random or free-form, not against a counterexample prompt, and budgets are in queries, not tokens.

### 4.5 Two-store design (SHELDON)

Keep two stores, hypotheses and observations, linked by evidence relations (supports, contradicts, unexplained). Add a drive: seek observations no current hypothesis explains. A comparison step marks which hypotheses an observation separates. This is a code data structure, not a prompt. Each part matters on some task (d14): observation store most on diagnosis (84 to 70), comparative analysis and observation store tie on ARC-AGI-2 (59.17 to 50.00 each), continued exploration most on circuit topology (1.00 to 0.733). Of 782 ARC hypotheses born after round 1, 204 cite an observation, 158 from testing a different hypothesis (c14). No outside replication; the paper's task counts differ by section.

### 4.6 Anomaly handling by prediction and reconcile (Little Scientist)

Before each run, write a numeric prediction and a falsification criterion. After the run, force a reconcile entry: prediction, result, gap, verdict. If the gap exceeds tolerance, the next step must address it (revise, or explain with a new test). Single author, five fixes changed at once, so the step is not isolated (d13). A related idea (PiEvo, d12): treat high-surprise results as a signal to add a new principle, not as noise; another group found no gain from PiEvo (d11).

### 4.7 BACON-style law search and its LLM form

```
for each group of variables with a controlled design (vary one at a time):
    if y is constant: record constant
    elif y is monotonic in x: define ratio or product; treat it as a new variable
    recurse on new terms
```

Modern form (LLM-SR, c21; Bayesian Model Discovery, a27): the LLM proposes equation skeletons from domain knowledge; a numeric optimiser fits constants; an experience buffer of best programs feeds the next prompt. In LLM-SR, dropping iterative refinement gave NMSE 1.01e-1 in-domain and 1.81e-1 OOD; dropping skeleton plus optimiser 3.78e-1 and 3.75e-1. A BACON-style constancy check (is a derived quantity nearly constant?) is cheap in code and could test numeric hypotheses, but no study of it with noise exists (K09, K13).

### 4.8 Identifiability check (LLM-IDEA)

Before concluding, compute whether the chosen measurements could separate the hypotheses at all (for example, whether two models give identical predictions on every measured quantity). If not, return a request for a new measurement instead of an explanation (d19). It is the only evidence that "what to measure" is its own step.

### 4.9 Compute the update in code (RAUMA)

In active causal discovery the model chose the right target and then misread the result. Supplying the computed statistic (z-score) gave 94% versus 96% for the rule (d17). Pattern: the program computes the posterior or the effect size; the model reads it.

## 5. What holds up

### 5.1 Replicated or multi-source

- **Confirming goes with failing, in LLMs.** Two groups (FalsifyBench; Failing to Falsify) plus WILT's failure types (repeating tests, confirmation, guessing without edge cases, overly complex rules; b24). Correlation is strong (rho -0.779, -0.937) but rests on 11-12 models.
- **Agents do not update on contradicting evidence.** Rios-Garcia et al. (68% non-uptake, 71% never updated) and DiscoverPhysics failure analysis (dismissal as noise; saw a contradiction, did not act) agree. Both use LLM-assisted labels (K24).
- **Discriminating test choice beats random.** EvoSCM, AutoSciLab, DiscoverPhysics (guided versus randomised for Opus 4.7 and GPT-5.5; open-source models show no gap).
- **End-to-end discovery is hard.** DiscoveryWorld, DiscoveryBench, ScienceAgentBench, ScienceWorld; single skills pass, the loop fails (K06).
- **Rules are proposed better than they are applied.** Hypothesis Search, Phenomenal Yet Puzzling (K14).
- **LLM judges of ideas are weak.** Si et al.; AI Scientist.
- **Positive testing is not a pure bias.** Klayman and Ha plus the BigTrak 60% disconfirmation rate plus FalsifyBench's own design caveat (K23).

### 5.2 Failed, null or contradicted

- **Dual-Goal prompt hurts non-thinking models.** Qwen3-32B 0.33 to 0.10; Qwen3-14B 0.23 to 0.13 (d06).
- **Sycophancy: confirming versus disconfirming partner.** 8.4% versus 14.1%, p=.143, CI -14.5 to 2.9. Default GPT versus disconfirming only p=.043 one-sided. The big gap is random sequences (29.5%) versus everything else.
- **Explicit hypothesis memory in DiscoveryWorld.** Hypothesizer did not raise completion and fell on challenge tasks (0.08 versus 0.18).
- **PiEvo's anomaly module on another group's test.** 28.18 versus 39.80 baseline (GPT-5.4); 48.18 versus 51.64 (GPT-5.5) (d11). PiEvo's own report: +29.7% to +31.1% on four tasks, and think-mode backbones lowered performance by about 26.35% (d12).
- **Box's Apprentice.** LM plus statistical model fitting did not reliably beat plain GPT-4o in BoxingGym and favoured overly simple forms.
- **Free code interpreter on strong reasoning models.** Lowered accuracy (d08).
- **Reasoning-tuned versus instruct.** WILT (o1-mini 26%, o1-preview 24% versus Claude 3.5 Sonnet 28%) and BoxingGym (instruct Qwen2.5 beat reasoning-tuned OpenThinker) show no reasoning edge; FalsifyBench and Jhaveri show a big one. Contested (K04).
- **Distilling for small models.** Qwen3-8B on Blicket 0.32 to 0.34-0.38 only (d07).
- **No failed replication of the 2-4-6 effect was found.** Klayman and Ha call the positive-test tendency widely replicated. "Not found" is not "does not exist"; the search was thin.
- **Top-line claims not verified.** Klahr, Fay and Dunbar 1993 rates (K18); SHELDON outside the authors' tasks; every 2026 preprint.

### 5.3 Boundary conditions and moderators

| Moderator | Effect | Source |
|---|---|---|
| H relative to R | too narrow: only negative tests falsify; right-sized with rare R: positive tests falsify | d04, d05 |
| Model type | thinking versus non-thinking flips the sign of the Dual-Goal prompt | b21 |
| Model size and quality | small reasoning models worse than all instruct (12%, 21%); 32B beats 7B | a11, a22 |
| Task | test choice near ceiling in causal discovery; test strategy predicts success in rule games | d17, d05 |
| Prior knowledge | roughly doubles success on average (PhysGym), yet some items solved only when stripped; BoxingGym null | d16, a22 |
| Model strength versus code tool | helps models below about 40% accuracy, hurts those above | d08, c16 |
| Identifiability | non-identifiable world: accurate fit still fails explanation | d19 |
| Variables, distractors, trajectory length | accuracy falls; weaker models collapse | d21 |
| Noise | 0.0001 noise cuts NewtonBench accuracy 12-16% | c16 |
| Base model versus scaffold | base model 41.4% of variance, scaffold 1.5% | d09 |
| Age and plausibility (humans) | success falls with younger age and implausible true rule | a04 |
| Domain (agents) | non-uptake workflow 82%, strategic 66%, hypothesis-driven 60% | d09 |

### 5.4 Competing explanations

- **Is confirmation the cause?** FalsifyBench shows correlation across 12 models. Failed games also had more disjoint or partly overlapping hypotheses, so part of the failure is bad hypothesis generation (d05). Treat as a mix. Thinking mode raises success without a steady rise in I:C (d07).
- **Why does thinking help?** Not mainly through more falsifying tests (d07). Better inference after each test is the natural candidate and was not isolated; RAUMA supports inference as the loss in causal discovery (d17). No task measures both.
- **Test choice or reading the result?** FalsifyBench finds oracle (outcome-reading) error does not matter, which shows the loss is not in the oracle; it does not say the player reads results well. RAUMA finds test choice fine and conclusion poor. DiscoverPhysics splits by model (K25). The tasks differ; do not assume one bottleneck. Log which of generate, select or revise failed.
- **Why do strong models lose with code?** The authors suggest they fit a function early and stop exploring (c16). Measured by signature words in two models only.
- **Why do humans keep disconfirmed hypotheses?** Noisy feedback, repeat checks, miscoding (d02). Some of it is rational.
- **Hypothesis list or none?** DiscoveryWorld Hypothesizer: no. SHELDON, EvoSCM: yes. Designs differ (memory only versus store plus discriminating action plus comparison). Not a true contradiction; the extra parts may carry the gain.
- **Domain prior?** BoxingGym says it often hurts after 10 experiments. Hypothesis-generation work uses priors as the source of candidates. The sign depends on whether a test follows.

### 5.5 Interventions: worked and did not work

| Worked | Did not work or mixed |
|---|---|
| Think-in-Opposites prompt (thinking models; +0.123 success) | Dual-Goal on non-thinking models (-0.060) |
| Distilling TiO traces (Qwen3-32B Blicket 0.57 to 0.77; Wason 0.41 to 0.64) | Distilling for Qwen3-8B on Blicket (0.32 to 0.34-0.38) |
| Code-chosen discriminating action (EvoSCM, AutoSciLab) | Free code interpreter on strong models |
| Computed identifiability check (LLM-IDEA) | Hypothesis memory alone (Hypothesizer, challenge level) |
| Observation store and comparison (SHELDON, own tasks) | PiEvo anomaly module on another group's test |
| Supplying a precomputed statistic (RAUMA, 94%) | Telling the model the rule without the number (about a third of the gap) |
| Rule application by code (Hypothesis Search, MiniSCAN) | Box's Apprentice in BoxingGym |
| Self-debug scaffold (ScienceAgentBench 16.7% to 32.4% for Claude 3.5 Sonnet, 17x cheaper than CodeAct 21.6%) | Heavier agent frame (OpenHands CodeAct) |
| Hypothesis update against data (HypoGeniC +0.7 to +8.1) | Simple "follow the scientific method" prompt (Little Scientist phase 1: 49 runs no gain) |

## 6. Language models

### 6.1 Rule discovery (the 2-4-6 family)

- **WILT (2024; a13, b24, c08, c09).** Hidden boolean rule over 3 numbers; up to 30 tests then one guess; 50 tasks per model. Claude 3.5 Sonnet 14/50 (28%), o1-mini 13, o1-preview 12, chatgpt-4o-latest 11, GPT-4o 9, Llama 3.1 405B 8, Haiku 1, Gemini 1.5 Flash 8b 0. Models differ in whether they are better at choosing tests or at deducing the rule: o1-mini was best at single-turn deduction from given tests but weaker in the full game; average guesses before final: o1-preview 2, Claude 3.5 Sonnet 3, GPT-4o 4.5. Authors suggest combining two models may beat one (not verified). No human score; small N.
- **FalsifyBench (2026; a11, c05-c07, d05).** 100 games, 5 domains, 12 LLMs, 20 turns, WordNet categories. Success: GPT-5.2-Chat 75%, GPT-OSS-120B 68%, DeepSeek-V3.1 41%, other instruct 33-35%, Qwen3.5-9B 21%, GPT-5-Nano 12%. Confirming share: instruct 66-82%; GPT-5-Mini 39.0%, GPT-5.2-Chat 27.3%, GPT-OSS-20B 24.2%. Conclusive falsification rate: GPT-OSS-20B 59.2%, GPT-OSS-120B 53.4%, GPT-5.2-Chat 49.5%, GPT-5-Nano 26.6%, Llama-4-Maverick 18.0%. Caveat: H sits inside R in more than 50% of turns, so only negative tests can falsify; the rare-target case where positive tests win was not run. GPT-5-Mini labels the H-R relation, each LLM is its own oracle (kappa 0.34 to 0.98).
- **Failing to Falsify (2026; a12, b19-b22, c01-c03, d06, d07).** 11 LLMs, 45 turns, success 6% to 78%. Counterexample prompts lifted success from 42% to 56%. Table 2, 80 episodes per cell: Qwen3-32B thinking 0.41 to 0.61 (TiO) at 1029.8 to 1450.0 tokens per turn; non-thinking 0.33 to 0.36 (TiO), 0.10 (Dual-Goal); Qwen3-8B thinking 0.21 to 0.36; Gemini-2.5-Pro 0.73 to 0.78. Thinking models allowed up to 16K tokens per turn, non-thinking 256. Blicket transfer (192 episodes per point): Qwen3-32B base 0.57 (I:C 0.54), TiO 0.86 (1.31); Qwen3-8B 0.32 to 0.40. Distilling TiO traces: Wason Qwen3-8B 0.21 to 0.36 (own teacher) or 0.59 (32B teacher), Qwen3-32B 0.41 to 0.64. Caveats: synthetic integer rules, LLM-generated rule sets, fixed alternation of guess and test turns, correlation not cause.
- **Sycophancy (2026; a14).** With humans: a default GPT partner behaved like a confirming partner; discovery 5.9% versus 29.5% for random-sequence evidence.

How much did changes matter? Model choice: instruct 33-41% versus reasoning 68-75% in FalsifyBench, about double. A prompt: about +14 points on average in Failing to Falsify, with a token cost and a model-dependent sign, and +0.05 for the strongest model. Model choice beats prompt. No equal-token comparison exists.

### 6.2 Discovery environments

- **ScienceWorld (2022; a23).** Best normalised score 0.17. A 1.5M-parameter DRRN was competitive. Models answer what a known material conducts but fail to run an experiment to find an unknown one.
- **DiscoveryWorld (2024; a15, a20, b10, b11).** 120 tasks, 8 topics, 3 levels, 5 seeds, GPT-4o. Completion (easy / normal / challenge): ReAct .38 / .18 / .18; Plan+Execute .18 / .18 / .15; Hypothesizer .28 / .23 / .08. Knowledge: ReAct .25 / .14 / .10; Plan+Execute .11 / .02 / .01; Hypothesizer .34 / .19 / .08. Scientists (11, normal and challenge only): procedure .79, completion .66, knowledge .55, about 717 steps. Unit tests (single skills): ReAct .76 procedure / .60 completion, Plan+Execute .66 / .44, Hypothesizer .77 / .64; dialog 1.00 for all. Hypothesizer costs about 2N calls for N steps. Easy tasks capped at 100 steps, others 1000.
- **NewtonBench (2026; c15, c16, d08).** 324 counterfactual law tasks, 12 physics domains, 11 LLMs, mean of 4 runs. Symbolic accuracy: GPT-5 75.9, Gemini-2.5-pro 65.4, GPT-5-mini 53.1, Gemini-2.5-flash 50.6, o4-mini 47.8, DeepSeek-R1 43.4, DeepSeek-V3 8.9, GPT-4.1 5.8, GPT-4.1-mini 5.1. Hardest setting: GPT-5 40.3%, Gemini-2.5-pro 16.7%, others under 6%. Experiments per task: GPT-4.1 80.6 versus Gemini-2.5-pro 15.3 and Qwen3-235B 8.2.
- **PhysGym (2025; d16).** About 97 environments, four prior levels. Gemini-2.5-flash 65.98 / 49.48 / 36.08 / 30.93%; o4-mini 62.89 / 41.24 / 31.96 / 27.84%. Experiments per solved task rise from 10.6 to 20.6 (Gemini) and 7.2 to 20.1 (o4-mini). Conventional 1/r form trapped one model at L3. No implausible-true-rule test.
- **BoxingGym (2025; a22, b12, c10, c11).** 10 environments, 5 runs, EIG regret. 32B beat 7B; closed beat open; instruct Qwen2.5 beat reasoning-tuned OpenThinker; GPT-4o lowest EIG regret. Good experiment choice and good prediction are related but not the same skill (Qwen-32B had higher regret yet good prediction in some). Authorship is credited to both "Gandhi et al." and "Gu et al." in our lines; check arXiv 2501.01540 before citing authors.
- **DiscoverPhysics (2026; d10, d11, d19).** 22 worlds with altered physics. In 11 paper worlds, 5 attempts each: Opus 4.7 passed 45% (30 failed), GPT-5.5 64% (20 failed). Primary gap per failed run, Opus versus GPT-5.5: consider the right law 6 versus 9; ODE integrator 2 versus 8; design discriminating experiments 8 versus 1; code does not match reasoning 5 versus 0; dismiss a real effect as noise 4 versus 0; act on fitter signals 2 versus 2; know when to stop 3 versus 0. Labels were assigned by Opus 4.7, one of the two models analysed. GPT-5.5 locks in a candidate law early.
- **Auto-Discovery-Bench (2026; d21).** Clean oracle. Performance falls as variables, trajectory length and distractors grow. Authors argue history tracking is a separate bottleneck; abstract claim stronger than the numbers read.
- **DiscoveryBench and ScienceAgentBench (a24, a25, b13, b14).** DiscoveryBench: 264 real plus 903 synthetic tasks, 6 domains, best about 25%. ScienceAgentBench: 102 tasks from 44 papers; Claude-3.5-Sonnet 16.7% direct to 32.4% self-debug; OpenHands CodeAct 21.6% at about 17x the cost ($0.958 versus $0.057 per task); o1-preview self-debug 42.2%; GPT-4o 22.6%, Mistral-Large-2 23.5%, Llama-3.1-405B 14.7%. Success is execution against a gold output.

### 6.3 Anomaly handling and belief updating

- **Rios-Garcia et al. (d09).** 25,000+ runs, 8 domains. Evidence non-uptake 68%; never updated 71%; refutation-driven revision 26%; convergent multi-test evidence 7%; untested claims 53% (63% in hypothesis-driven domains). Pass^k falls below 0.05 by k=4 to 6 in spectroscopic structure elucidation and inorganic qualitative analysis. Injecting near-complete successful traces did not fix hypothesis-driven domains. Scaffolds tested: ReAct and tool-calling only. Models are mid-2025 (GPT-4o, Claude Sonnet 4.5, GPT-OSS-120B); chemistry-heavy domains; LLM-assisted labels.
- **DiscoverPhysics (d10).** Self-monitoring failures (saw a contradiction, did not act): 8 for Opus versus 2 for GPT-5.5. Dismissal as noise: 4 versus 0.
- **Human baseline for comparison.** 56% retention of disconfirmed hypotheses (d02). LLMs look worse (71% never updated) but the metrics differ and domains differ.
- **Reported fixes (all authors' own).** EvoSCM structured revision (full 75.09 versus 70.73 without); PiEvo principle expansion (96.36 versus 85.87 static); Little Scientist prediction and reconcile; Agarwal et al. belief-update filter removes 37.5% of spurious surprise and raises accumulated non-stationary surprisal by 30.62% across five domains (d20; measured against the model's own belief, not truth).
- **No intervention study of a contradiction log exists.** The scaffolds in d09 did not include one (K24, K29).

### 6.4 Generation, selection and equations

- **Hypothesis Search (2023; a16, c18).** GPT-4 wrote 64 hypotheses, summarised to 8, wrote programs, up to 3 rounds of execution feedback. ARC 100 tasks top-1: direct 17%, program-only 23%, summarised 30%, human-selected 33%, human-written 45%. SyGuS: 94.3% with 4 hypotheses x 2 programs versus 74.8% CrossBeam. 1D-ARC program-only 61.1%. A 2025 follow-up (d22) reports about 0.49 versus 0.36 on list functions with GPT-4o; snippet only.
- **Phenomenal Yet Puzzling (2024; c19, c20).** Propose, select, refine with a symbolic interpreter. ACRE: direct 28.0%, refinement 59.0%. Replacing the interpreter with the LM dropped MiniSCAN from over 80% to near zero.
- **HypoGeniC (2024; b15).** Generate then update hypotheses against data beat few-shot on all 4 tasks (Shoe Sales +31.7, Deceptive Reviews +13.9, Headline +3.3, Tweet +24.9, the last inflated by safety refusals). Update versus no update +0.7, +5.8, +8.1, +7. Pool of 20 beats 3. Older models; lost to fine-tuning on Deceptive Reviews.
- **ARC-AGI-2 ensemble (2026; d15).** Pool oracle 86.23%, final 76.65% of 167 instances. Generation misses 22, selection misses 17. Judge uplift over majority vote +7 instances. Semi-private 72.9% at $38.99 per task. Early-stopped instances 36 of 37 correct versus 70.8% for full-coverage ones. One author; heavy ensemble.
- **LLM-SR and LLM-SRBench (2025; a17, b18, c21, c22).** About 2.5K iterations versus 2M+ for symbolic regression baselines. Best symbolic accuracy 31.5% (LSR-Transform, 111 problems) and 28.1% (LSR-Synth, 128 problems); best numeric Acc0.1 50.45% (LaSR). Data-blind: Llama-3.1-8B 3.61%, GPT-3.5 2.10%, GPT-4o-mini 7.21%. LaSR has Acc0.1 near 50% but symbolic accuracy only 5-13%. Perplexity analysis suggests Feynman equations are memorised. Weak 2024 backbones.
- **Bayesian Model Discovery (2026; a27).** LLM proposes families, a numeric engine scores by model evidence, EIG picks the next experiment. Abstract only, no numbers.
- **AutoSciLab (2026; d18).** GRN exact recovery 31.11% versus 0.00%; NewtonBench symbolic 67.6%; Chem 35.1%. Strongest active baselines need 2.60-3.10x (NewtonBench), 2.33-2.47x (Chem), 3.90-4.60x (GRN) queries to match it; LLM-only variants need 5.20-14.40x. Query-matched, not token-matched.

### 6.5 Idea generation and judgement

- **Si et al. (a18, b16).** 49 idea writers, 79 reviewers, 298 reviews (119 human-idea and 109 AI-idea reviews feed the novelty table; 49 ideas per condition is a separate count). Novelty human 4.84, AI 5.64, AI plus human rerank 5.81. Excitement 4.55 versus 5.19 / 5.46. Feasibility 6.61 versus 6.34 / 6.44 (not significant). Seed duplication: about 200 of 4,000 unique. Best LLM judge 53.3% (Claude-3.5 pairwise) versus 56.1% human-human; GPT-4o direct 50.0%, pairwise 45.0%. Ideas were not executed; NLP prompting topics only.
- **AI Scientist (a19, c26).** Under $15 per paper; reviewer 65% versus 66% balanced accuracy (AUC 0.65 both). Failure notes: ideas not implementable, wrong implementations hard to catch, too few experiments for fair controls, struggles to compare two numbers, hallucinated an ablation table.
- **Position and perspective pieces (no data).** Fa and Culjak (a26): falsification-first standard for agents. Jagadish et al. (c28): four problems in automating cognitive science. MOOSE (c27) and MOOSE-Chem2 (b17), HypoGeniC-style systems: abstract level only.
- **Continual discovery.** Agarwal et al. (d20): see 6.3.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, M = memory. Status: [E] established (2+ independent sources), [S] single-source, [C] contested. "Add now" items are either already in SCHEMA.md or are logging and routing rules that change no model behaviour. Anything that changes behaviour and is not [E] goes to "Test first" and must pass the equal-token rule (G7) before it enters SCHEMA.md.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep S7's rule: when two or more candidate rules still fit, code finds an input where they differ and runs it. Make it the default form of "counterexample search". Direction is [E] (discriminating choice beats random or free-form on three groups' benchmarks); the size at equal tokens is not known. | S7, S4 | [E] direction | K26, K07; d11, d18, d10 |
| A2 | Log, per run, every result that contradicted the held hypothesis and what the agent did next (ignored, patched, revised). Measurement only. Reason: default agents ignore contradicting evidence (68% non-uptake, 26% refutation-driven revision). | logging (section 6 of SCHEMA), G2 | [E] direction | K24; d09, d10 |
| A3 | Log pool recall (does any attempt match truth) separately from selection accuracy. Hypothesis generation is the first loss for a single model; selection becomes comparable only at large pool sizes. | S3, S7, logging | [E] | K07; a16, c18, d15 |
| A4 | Never let the generating model pick the final idea or rule in open mode; select by run results. Already G8. Judge accuracy 53.3% versus 56.1% human. | G8 | [E] (schema), [S] here | K11; a18, b16 |
| A5 | Model proposes rules; code applies and scores them wherever a rule can be written as a program. | G5, S4 | [E] | K14, K12; c19, c20, a16, c21 |
| A6 | The program, not the model, owns transitions between generate, test, revise. Single steps succeed; the loop fails. | section 1, S3-S5 | [E] | K06; a15, b11, a24, a25 |
| A7 | Choose the test type by the hypothesis-to-rule relation. Do not force negative tests everywhere: they are needed when H may be too narrow; positive tests are as good when R is rare and H right-sized. The general discriminating test covers both. | S4, S7 | [E] | K23; d04, d03, d05 |
| A8 | Keep the 4b ban on "be careful" and bias-awareness prompts. The failure here is ignoring evidence and bad test choice, not too little carefulness; the one prompt that helped (TiO) is model-dependent and costs tokens, so it is a test item, not a rule. | 4b, G11 | [E] | K03, K24; b21, d06, d09 |
| A9 | Record human facts as a baseline in logs: about 44% of disconfirming outcomes lead to a change in humans. Use as a reference, not a target. | logging | [E] fact (single study) | K22; d02 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Code-forced falsifying test (a test outside the current hypothesis when it may be too narrow) versus counterexample prompt (TiO) versus plain, per model, at equal tokens. The causal test the correlations cannot give. | S7, G7 | [S] | K01, K02, K03, K04, K29; a11, a12, d06 |
| T2 | Forced contradiction log: a result that contradicts the held rule must be answered (patch, revise, keep with a reason) before the next test. | S5, G2 | [S] | K24, K29; d09, d10, d13 |
| T3 | Prediction before the run and a forced reconcile entry. | S4, S5 | [S] | d13 |
| T4 | Separate store of unexplained observations, plus a drive to seek them; comparison marks which hypotheses an observation separates. | S2/S4, M | [S] | K16, K08; a21, c14, d14 |
| T5 | Code-scored experiment choice (disagreement among a small model population) versus free LLM choice, at equal tokens. | S4, G5 | [E] direction, [S] size | K26, K12; d11, d18 |
| T6 | Vary-one-thing and observability checks on proposed tests (Klahr heuristics); check also that a record of tested conditions is kept (Trickett: coverage of E-space). | S4 | [S] | K19; a05, b02, b05 |
| T7 | Identifiability check: can the chosen measurements separate the hypotheses at all? Returns "measure X" instead of a guess. | S2, S4, S8 | [S] | K27; d19 |
| T8 | Compute the update in code (statistic, effect size) and hand it to the model, instead of letting the model eyeball it. | S5, G5 | [S] | K27; d17 |
| T9 | Entry order: hypothesise first versus explore first. | S0, S2, S3 | [S] human only | K22; d01, d03 |
| T10 | Prior context on, stripped, and deliberately wrong (implausible true rule); anonymised retry on stall. | G1, S1, S3 | [C] | K28, K10, K18; d16, a22, a04 |
| T11 | Rare-target hidden rule: does forced negative testing lower success? | S7 | [S] | K23; d04, d05 |
| T12 | Score test informativeness separately from inference accuracy on the same task. | logging, S7/S8 | [C] | K15, K27; d17, c06 |
| T13 | Two model roles (test chooser and rule inferer). | S3/S4 | [S] | K15; c09, d17 |
| T14 | Code tool policy: mandatory check-only tool versus optional free interpreter versus none, by model strength. | G5, S8 | [S] | K09; d08, c16 |
| T15 | Noise: repeat a disconfirming test once before dropping a rule, on noisy-feedback items. | S5 | [S] | K22, K09; d02, c16 |
| T16 | Falsification prompt only in thinking mode, never in short-reasoning mode. | G11, S4 | [S] | K03; b21 |

None conflicts with 4b: T1, T2 and T15 fire only on a signal (the hypothesis may be too narrow; a result contradicts it), in line with G1.

## 8. Concrete tests on our bench

All tests: arms at equal total tokens (G7); same items; same model; at least 3 seeds; report success, tokens, and the section 6 log fields. Effects are expectations from the evidence, not results.

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Hidden-rule games (WILT-style number triples and FalsifyBench-style categories), H inside R | plain loop; counterexample prompt (TiO); code-forced negative test when H may be too narrow | success rate; share of conclusive falsifying tests; tokens per game | code-forced beats plain by 10+ points for instruct-style models; versus TiO at equal tokens unknown (the open gap) |
| B2 | Same games, rare-target variant (R small, H about R's size) | plain; always-negative forced; code-chosen discriminating test | success rate | forced negative loses to plain or to discriminating test; discriminating test never worse |
| B3 | Hidden-rule games with a contradicting result planted mid-run | plain; contradiction log with required response; prediction-and-reconcile | share of contradictions followed by revision; final success | revision rate rises above the 26% level; success up on planted-anomaly items |
| B4 | ARC-style items | single model, S3 with N isolated hypotheses | pool recall (any hypothesis matches truth) versus top-1 selection accuracy | locates the larger loss; expect generation loss larger for a single model |
| B5 | Law discovery with 2 to 3 candidate laws (NewtonBench-style or synthetic) | LLM-chosen experiment; random; code-scored disagreement among candidates | symbolic accuracy; experiments to solution | code-scored beats LLM free choice and random (EvoSCM direction: 75.09 versus 47.45) |
| B6 | Same law tasks, with and without a Python tool | no tool; optional tool; mandatory check-only tool | accuracy by model strength | optional tool lowers strong-model accuracy; mandatory check-only does not |
| B7 | Discovery in a simple simulator with observations | flat history; two-store (hypotheses plus unexplained observations) | success; share of final hypotheses citing an observation | helps on diagnosis-type items; small or none elsewhere |
| B8 | Items where only some variables are visible | no check; computed identifiability check | explanation correctness; rate of correct "cannot tell, measure X" | check lifts explanation on non-identifiable items |
| B9 | Law tasks with and without domain context, plus an implausible true law | context on; context stripped; context wrong | success by plausibility | context helps on average, hurts on implausible truth |
| B10 | Hypothesise-first versus explore-first | S3-first; explore-first | tokens to success; success | hypothesise-first cheaper when a frame exists; explore-first better when none |
| B11 | Hidden-rule games with logging of test informativeness (hypotheses eliminated) and inference accuracy | all arms | both scores | separates test-choice loss from inference loss per model |
| B12 | Multi-variable simulator | free design; code-enforced vary-one | success; tests to solution | helps on interaction-free tasks; hurts on interaction tasks |
| B13 | Noisy law tasks (noise 0.0001 to 0.1) | model-only fitting; code BACON-style constancy check with tolerance; code fit with held-out check | exact-form recovery; held-out fit | code check recovers part of the 12-16% noise loss; fit alone hides form errors |
| B14 | Statistic handed over versus eyeballed (edge orientation, effect size) | model reads raw data; code gives z-score or likelihood ratio | decision accuracy | gap closes toward 94% (RAUMA direction) |
| B15 | Rule games with a planted wrong partner (agrees with the wrong rule) | plain; evidence only from run outputs (S1 input hygiene) | success; confidence | agent that cites only run outputs resists the confirming partner |

## 9. What does not transfer, and why

- **Human age and plausibility effects.** Children failing implausible rules (13%) reflects knowledge and development. An LLM has no development; its analogue is the training prior. Only the lock-in idea transfers (d16), and no LLM study with implausible rules exists.
- **BACON's clean data and given variables.** Real tasks have noise (0.0001 noise cut NewtonBench accuracy 12-16%) and unknown variables. BACON shows an algorithm class, not a performance level.
- **Wason confirmation as a universal bias.** Klayman and Ha show positive testing is often right. Forcing negative tests everywhere would be wrong. Transfer the discriminating test, not "falsify always".
- **The human Theorist/Experimenter split.** It describes people with different memory and programming experience (all 4 Study-2 Theorists had programming experience). An LLM always has its "memory"; the useful part is the order choice, untested for LLMs.
- **Dunbar's real-world labs and Klahr's communication space.** No counterpart in a single-agent bench.
- **Study scales.** Many LLM results are on authors' own testbeds with simulator oracles and query-matched budgets, not token-matched.
- **Prompts that name the bias.** The 4b ban on bias-awareness prompts stands. The Failing to Falsify prompts change what the model does each turn, gains are model-dependent and cost tokens.
- **Distillation.** Falsification behaviour trained into a model transferred to Blicket (0.57 to 0.77) but stayed below prompting; our agent is scaffold-only, so this is a limit, not an option (K17).
- **Full autonomous papers.** Only the AI Scientist failure list (too few controls, hallucinated tables) carries over to a closed bench.
- **Idea novelty ratings.** Human novelty ratings are not run results; G8 already forbids model opinion as selection.
- **Human-subject sycophancy effect.** The 29.5% versus 5.9% result is about people reading AI partners; for our agent the analogue is feeding its own confirming outputs back as evidence (input hygiene), not the numbers.

## 10. Open questions

1. Does a code-forced falsifying test beat counterexample prompts at equal tokens, per model? No paper compares them (K29).
2. How do LLMs handle anomalies in Chinn and Brewer's sense (discard, patch, revise)? Only coarse rates exist (d09, d10), with LLM-assigned labels. No LLM replication of Dunbar's lab findings.
3. Does SHELDON replicate outside its authors' tasks, and which part matters? Task counts are inconsistent across sections. No outside run.
4. Would an LLM behave like a Theorist or an Experimenter, and does order matter? No LLM test.
5. Do LLM agents search E-space with Klahr's four heuristics? Does variables-changed-per-test predict success? Unscored.
6. For a single current model on ARC-AGI-2, is the loss mostly generation or selection? Only the heavy-ensemble figure (22 versus 17).
7. When does a prior help and when does it lock in a wrong model? PhysGym and BoxingGym conflict with LLM-SR. No test with an implausible true rule.
8. Why does thinking help: test choice or inference? Jhaveri: not mainly test choice. RAUMA: inference is the loss. No task measures both.
9. Is "what to measure" a separate bottleneck by default, not only in purpose-built testbeds (LLM-IDEA, AutoSciLab)?
10. LLM result in the rare-target case where confirming should win? FalsifyBench built only the subset case.
11. Failed replication of the 2-4-6 effect or larger-sample human replications? None found; the search was thin and APIs were rate-limited.
12. Are the 2026 preprint numbers stable on rerun? None has been independently replicated.
13. Does the Theorist/Experimenter timing difference (24.46 versus 11.40 min) hold outside BigTrak? One lab, one device.
14. Do the Klahr, Fay and Dunbar 1993 rates (83 / 65 / 53 / 33%; 56% versus 13%) hold? Unverified.
15. Direct instruction versus discovery for an LLM agent (Klahr and Nigam; Alfieri analogue): is it better to put the design strategy (vary one thing at a time) in the prompt than to let the agent search? No source.
16. Where in a chained discovery task does the loop break? DiscoveryWorld unit tests pass at about 60%+, full tasks at 18%; no transition-level breakdown.
17. Does the benefit of a code-level constant-ratio (BACON-style) check survive noise?

## 11. Sources

[V] = opened and read this session (some only the abstract and introduction, noted). [M] = snippet, abstract page or metadata only; no numbers taken from it.

| Mark | Source (evidence ids) | URL |
|---|---|---|
| [V] | Klahr (1994) Children, Adults, and Machines as Discovery Systems (a01-a06) | https://link.springer.com/article/10.1007/BF00993981 |
| [V] | Klahr and Dunbar (1988) Dual Space Search During Scientific Reasoning, full text of Studies 1 and 2 (d01-d03) | https://users.cs.northwestern.edu/~paritosh/papers/sketch-to-models/klahr-dunbar-dual-space-search-cogsci-1988.pdf |
| [M] | Klahr and Dunbar (1988) Wiley version (a28; 403, metadata only) | https://doi.org/10.1207/s15516709cog1201_1 |
| [M] | Klahr and Simon (1999) Studies of Scientific Discovery (a29; metadata only) | https://doi.org/10.1037/0033-2909.125.5.524 |
| [M] | Klahr, Fay and Dunbar (1993) via Klahr 1994 only (a04) | https://link.springer.com/article/10.1007/BF00993981 |
| [V] | Klayman and Ha (1987) Confirmation, disconfirmation, and information (d04) | https://pages.ucsd.edu/~mckenzie/KlaymanHaPsychReview1987.pdf |
| [V] | Langley (1979) Rediscovering Physics with BACON.3 (a07, a08) | https://www.ijcai.org/proceedings/1979/0113.pdf |
| [V] | Schunn and Klahr (1992) Complexity management in a discovery task (b01-b03) | https://escholarship.org/uc/item/94n547fj |
| [V] | Schunn and Klahr (1995) A 4-space model of scientific discovery (b04, b25) | https://escholarship.org/uc/item/40q1p8f6 |
| [V] | Trickett, Trafton and Raymond (1998) Exploration in the experiment space (b05, b06) | https://escholarship.org/uc/item/9v5771xr |
| [V] | Dunbar and Schunn (1990) Temporal nature of scientific discovery (b08) | https://escholarship.org/uc/item/57c1f8xx |
| [M] | Klahr and Nigam (2004) direct instruction versus discovery (b26; not opened) | https://doi.org/10.1111/j.0956-7976.2004.00714.x |
| [M] | Alfieri et al. (2011) discovery-based instruction meta-analysis (b27; not opened) | https://doi.org/10.1037/a0021017 |
| [V] | Jhaveri, GX-Chen, Sucholutsky and Choi (2026) Failing to Falsify (a09, a12, b19-b22, c01-c04, d06, d07; use the PDF, the HTML drops numbers) | https://arxiv.org/abs/2604.02485 |
| [V] | Bertolazzi, Tentori and Bernardi (2026) FalsifyBench (a10, a11, b23, c05-c07, c29, d05) | https://arxiv.org/abs/2606.04751 |
| [V] | Banatt, Cheng, Vaidyanath and Hwu (2024) WILT (a13, b24, c08, c09) | https://arxiv.org/abs/2410.10998 |
| [V] | Batista and Griffiths (2026) A Rational Analysis of the Effects of Sycophantic AI (a14) | https://arxiv.org/abs/2602.14270 |
| [V] | Jansen et al. (2024) DiscoveryWorld (a15, a20, b10, b11, c17) | https://arxiv.org/abs/2406.06769 |
| [V] | Wang et al. (2023/2024) Hypothesis Search (a16, c18) | https://arxiv.org/abs/2309.05660 |
| [V] | Shojaee et al. (2025) LLM-SR (a17, c21) | https://arxiv.org/abs/2404.18400 |
| [V] | Shojaee et al. (2025) LLM-SRBench (b18, c22) | https://arxiv.org/abs/2504.10415 |
| [V] | Si, Yang and Hashimoto (2024) Can LLMs Generate Novel Research Ideas? (a18, b16) | https://arxiv.org/abs/2409.04109 |
| [V] | Lu et al. (2024) The AI Scientist (a19, c26) | https://arxiv.org/abs/2408.06292 |
| [V] | Joshi, Shethia and Lam (2026) SHELDON (a21, c12-c14, d14) | https://arxiv.org/abs/2610.18025 |
| [V] | BoxingGym (a22, b12, c10, c11; authors listed as Gandhi et al. and Gu et al. in different lines, check) | https://arxiv.org/abs/2501.01540 |
| [V] | Wang et al. (2022) ScienceWorld (a23) | https://arxiv.org/abs/2203.07540 |
| [V] | Majumder et al. (2024) DiscoveryBench (a24, b13; abstract-level) | https://arxiv.org/abs/2407.01725 |
| [V] | Chen et al. (2024/2025) ScienceAgentBench (a25, b14) | https://arxiv.org/abs/2410.05080 |
| [M] | Fa and Culjak (2026) Sound Agentic Science Requires Adversarial Experiments (a26; position paper, abstract and introduction only) | https://arxiv.org/abs/2604.22080 |
| [M] | Yuh et al. (2026) Bayesian Model Discovery with Language Models (a27; abstract and introduction only) | https://arxiv.org/abs/2610.25747 |
| [M] | Piriyakulkij et al. (2024) Doing experiments and revising rules (b09; abstract page only) | https://arxiv.org/abs/2402.06025 |
| [V] | Zhou et al. (2024) HypoGeniC (b15) | https://arxiv.org/html/2404.04326 |
| [M] | Yang et al. (2025) MOOSE-Chem2 (b17; abstract only) | https://arxiv.org/abs/2505.19209 |
| [M] | Yang et al. (2024) MOOSE (c27; skimmed) | https://arxiv.org/abs/2309.02726 |
| [M] | Jagadish et al. (2026) Toward an automated science of the mind (c28; perspective, skimmed) | https://arxiv.org/abs/2603.20988 |
| [V] | Zheng et al. (2026) NewtonBench (c15, c16, d08) | https://arxiv.org/abs/2510.07172 |
| [V] | Qiu et al. (2024) Phenomenal Yet Puzzling (c19, c20) | https://arxiv.org/abs/2310.08559 |
| [V] | Udrescu and Tegmark (2020) AI Feynman (c23) | https://arxiv.org/abs/1905.11481 |
| [V] | Kramer et al. (2025) Automated Scientific Discovery: From Equation Discovery to Autonomous Discovery Systems (c24, c25) | https://arxiv.org/abs/2305.02251 |
| [V] | Rios-Garcia et al. (2026) AI scientists produce results without reasoning scientifically (d09) | https://arxiv.org/abs/2604.18805 |
| [V] | Wiemann et al. (2026) DiscoverPhysics (d10) | https://arxiv.org/abs/2605.26087 |
| [V] | Zhao et al. (2026) EvoSCM (d11) | https://arxiv.org/abs/2609.01526 |
| [V] | PiEvo (2026) Principle-evolvable scientific discovery (d12) | https://arxiv.org/abs/2602.06448 |
| [V] | Smith (2026) The Little Scientist (d13) | https://arxiv.org/abs/2608.16951 |
| [V] | Land (2026) Modality-driven search with holistic trace judging for ARC-AGI-2 (d15) | https://arxiv.org/abs/2606.31543 |
| [V] | Chen et al. (2025) PhysGym (d16) | https://arxiv.org/abs/2507.15550 |
| [V] | RAUMA (2026) LLMs can choose what to test, but not what to conclude (d17; abstract page only) | https://neurips.cc/virtual/2026/156578 |
| [V] | Kabra et al. (2026) LLM-AutoSciLab (d18; ablation figure not extracted) | https://arxiv.org/abs/2605.24043 |
| [V] | Shetty and Braga-Neto (2026) LLM-IDEA (d19) | https://arxiv.org/abs/2610.11253 |
| [V] | Agarwal et al. (2026) Evidence-informed LLM beliefs for continual scientific discovery (d20) | https://arxiv.org/abs/2606.29182 |
| [V] | Chen et al. (2026) Auto-Discovery-Bench (d21; numbers partly not extracted) | https://arxiv.org/abs/2502.15224 |
| [M] | 2025 error-source study of LLM hypothesis search for rule induction (d22; snippet only) | https://arxiv.org/abs/2509.01016 |

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 9 established claims: 6 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E15.09-K12** (now single-source: the sources are not independent). Numbers confirmed (31.5%/28.1%, data-blind 3.61/2.10/7.21%, 2.5K vs 2M+ iterations), but LLM-SR and LLM-SRBench are the same lab (Shojaee, Reddy et al.), and NewtonBench tests different things; also in LLM-SRBench Appendix F PySR is competitive or better on numeric accuracy (Acc0.1) and only worse on symbolic accuracy, so 'beats search without LLM priors' is not unqualified.
- **E15.09-K13** (reworded: the sources support less). Numbers confirmed (Langley productions 1203/1119/1297/1150/4593; AI Feynman 100/100 vs 71), but 'no noise handling was seen in the sources read' is false: Langley says noise handling is by a tolerance parameter, Kramer et al. say BACON uses a tolerance for noise, and AI Feynman has a section testing dependence on added Gaussian noise. Corrected claim: Classic heuristic data-driven systems rediscover simple laws from clean data: BACON.3 rediscovered five laws (ideal gas, Kepler, Coulomb, Ohm, Galileo) with 1,119-4,593 production firings each, and AI Feynman solved 100/100 Feynman-lecture equations vs 71 for earlier public software. Both address noise only partly: BACON uses a tolerance parameter, and AI Feynman reports how success degrades as Gaussian noise is added.
- **E15.09-K15** (reworded: the sources support less). Numbers match (OR 0.885 spanning zero for oracle error, OR 0.016 for bias; WILT best 14/50 = 28%), but oracle error is mistakes by the feedback-giving oracle, not the player misreading outcomes, so it does not show the failure is 'not in reading outcomes'; WILT itself finds models differ in whether they are better at choosing tests or at deducing the rule. Corrected claim: In FalsifyBench, noise in the oracle's feedback does not explain failure (oracle error OR 0.885, interval spans zero), whereas the share of confirming tests strongly predicts it (OR 0.016), so the failure is tied to test choice. WILT reports that models strong in single-turn tests do poorly in the multi-turn game (best 14/50 = 28%), with some models better at choosing tests and others at deducing the rule from them.
- **E15.09-K22** (now single-source: only one opened source, code check).
