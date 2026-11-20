# Computational design: deep document

*Subfield E05.10. Focus: function-behaviour-structure (FBS) models (Gero; Maher). Why it matters for our agent: state model ideas. Evidence ids (a01-a27, b01-b27, c01-c26, d01-d18) refer to evidence_a-d.jsonl in this folder; claim ids (E05.10-K01 to K23) refer to claims.jsonl. Status marks: [E] established, [S] single source, [C] contested, [U] unverified. The last search pass was limited (rate limits, blocked pages), so "not found" means "not found", not "does not exist".*

## 1. What it is

Computational design is the study of design as a process a machine could run or record. This subfield has two lines.

1. **Gero's function-behaviour-structure (FBS) framework.** A small ontology for what a designer thinks about, plus eight named moves between those things. It began as a knowledge-representation schema for AI (Gero 1990, "design prototypes"). It became the most used coding scheme for design protocols (a09, a10, b12).
2. **Maher's line**: case-based design, and co-evolution of problem and solution as two populations changed by a genetic-algorithm-like process (Maher and Poon 1996). Only a secondary description was read (d07). Maher's case-based design itself was never opened (c26, d18). This is a real hole.

The variables:

| Symbol | Name | Meaning |
|---|---|---|
| R | Requirements | what the client asks; outside the designer's control |
| F | Function | what the artefact is for |
| Be | Expected behaviour | what the structure should do to deliver F |
| Bs | Derived behaviour | what the candidate structure actually does |
| S | Structure | the elements and their relations (the candidate) |
| D | Design description | the documented result |

Key rule: a design description is never made directly from function. It comes from a chain of transformations among F, Be, S, Bs and D (a02).

For our agent the useful part is small. FBS gives a closed list of state variables and a closed list of moves. The move that matters most is "compare expected behaviour with derived behaviour". It maps onto our test step and onto G2 (revise only from real output).

## 2. History and theories in depth

**1990. Gero, Design prototypes (a01).** A prototype stores F, Be, S and knowledge in one schema. Designing is modelled as eight processes. The paper was not opened (403 error). Details come from papers that were opened (a02, a03).

**The eight processes (a02).**

| # | Process | Move |
|---|---|---|
| 1 | Formulation | F to Be |
| 2 | Synthesis | Be to S |
| 3 | Analysis | S to Bs |
| 4 | Evaluation | compare Be with Bs |
| 5 | Documentation | S to D |
| 6 | Reformulation I | change the structure space |
| 7 | Reformulation II | change the behaviour space |
| 8 | Reformulation III | change the function space |

The three reformulations break any linear waterfall order (a03). A ninth move, F to S, was added in 2019 as the fast, catalogue-lookup route with no verification (b16).

**2004. Situated FBS (Gero and Kannengiesser).** Adds three worlds (external, interpreted, expected), 12 categories and 20 processes. The 20 map onto the 8 fundamental steps (a03, c23). The 2004 paper was not opened (d17). Its processes are used as coding categories. No experiment found manipulates them to test a causal effect. So FBS is a descriptive coding scheme, not a tested performance theory.

**2009. Kannengiesser and Zhu (a03-a05).** FBS used to evaluate five software design methods (ADD, S4V, RUP, BAPO, Agile Alliance Approach) by which of the 20 processes each supports. Most support synthesis and analysis. Reinterpretation and reformulation are mostly implicit. The mapping was done by two authors from method text with no reliability check. They also describe a push-pull idea: interpretation is driven both by stored experience (push) and current expectations (pull), so the same input is seen differently at different times (a04).

**2011. Protocol toolkit (a06, a07).** One segment gets one FBS code. Transitions between segments define processes, either syntactic (adjacent segments) or semantic (linkograph backlinks). Measures: issue mix, first-order and second-order Markov matrices, first-passage time (segments until the same issue recurs), and linkograph entropy. Demo: one large industry team, 1280 segments over one hour. The authors call the syntactic version a weak model of processes.

**Meta-coding (a10).** Problem space = R, F, Be. Solution space = S, Bs. Plotting the two over time operationalises problem-solution co-evolution in the sense of Maher and Poon and of Dorst and Cross (a27). A second-order code marks "new" and "surprising" issues for creativity studies.

**2013. Ralph field test (a17, a18).** FBS was tested as a theory of software process against a rival, Sensemaking-Coevolution-Implementation (SCI). SCI won on a survey and on four case studies (section 5).

**2015-2018. Cross-domain and Pahl-Beitz tests (a12-a16).** Published design models were mapped to FBS processes and simulated. Then the Pahl-Beitz prediction was checked against 46 real student sessions.

**2019. Fast and slow (b16, d08).** A framework paper mapping four design instances (fixation, case-based design, pattern use and others) to FBS routes. The Design Science paper has no hypotheses or statistics. The conference version with H1 and H2 was not obtained (b17). A review says all student and professional designers show both system 1 and system 2 thinking (a11, b13), without numbers.

**2020. Gero and Milovanovic review (a09-a11, b12-b15).** FBS is the most used coding ontology. Over 3,500 citations for the two main papers by 15 Jan 2020. Over 10,000 hours of industrial systems design coded. Domains: architecture, engineering, software, systems design. Each protocol is coded by at least two coders. The review is by the authors' own group, and citation counts are not validity evidence.

**2022. Gero, Kannengiesser and Crilly (d04-d07).** First formal, FBS-measured definition of co-evolution: reciprocal exogenous change between categories (a change in one triggered by the other, then the reverse). Also the best description of Maher and Poon (1996) found: a co-evolutionary genetic algorithm with a problem population and a solution population, where a fitness check decides when to refocus.

**2023-2026. LLM era.** FBS appears in four ways: as a prompt chain (Chen 2024, d01-d03); as a label scheme LLMs must classify (Sahadevan 2024, Elhambakhsh 2025); as a knowledge-graph structure for retrieval (Fujiu 2025); and as background for LLM design studies that do not use FBS as an intervention (Ma 2023/2024, Tanaka 2026, Bruggeman 2025). See section 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| FBS has 6 variables and 8 processes that code any design protocol | R, F, Be, Bs, S, D; 8 processes; situated version 3 worlds, 20 processes | a02, a03, b18 (K01) | [E] as a coding scheme |
| FBS widely applied | over 10,000 hours coded; 3,500+ citations | a09, b12 (K02) | [E] use; weak proof of validity |
| Domain independence | only function shared a slope across models, F(2,5)=5.22, p=0.06 (not significant); Be differs, F(2,5)=101.5 | a12-a14 (K02) | [S], mostly figures |
| Pahl-Beitz fits real students only partly | 46 sessions (15 sophomore pairs, 45 min; 31 senior capstone pairs: brainstorming 10, morphological 11, TRIZ 10); Bs slope 0.065 in the model vs about 0.12 in the RUP data | a14-a16 (K03) | [C] |
| Expert decomposition and recomposition | decomposition: freshmen 15.13% (SD 2.66), seniors 15.22% (3.27), engineers 22.38% (3.01); recomposition 15.28, 15.31, 22.57; d up to 2.55; 50 people (tests on 10, 10, 5 dyads) | b06 (K04) | [C] |
| Experts at whole-system level | 61 teams (122 people): level-1 share .12 professionals, .14 seniors, .06 first-years; level 3 .46, .48, .64; partial eta squared 0.336; agreement 80%, kappa 0.78 | b08, b09 (K04) | [C] |
| Pre-engineering courses change nothing | 40 juniors in dyads, 45 min; synthesis t=-1.01, p=0.163; closest Be p=0.053; coder agreement 85-95% | b01, b03 (K04) | [S] null |
| Sophomore design education | 20 then 16 participants, 3 controls per semester; no significance test; correlation not causation | b04, b05 (K05) | [S] descriptive |
| Practitioners favour co-evolution over FBS rational plan | 1384 completers of 4410 visitors (31%), 65 countries, 13 items; 96.6% median agreement with SCI; p<0.001 each item; 4 cases | a17, a18 (K16) | [E] with a04, a27 |
| Co-evolution mainly Be-S, near continuous | one 1-hour session, 3 professional engineers; function-involving co-evolution rare | d06 (K20) | [S] |
| Switch counts overstate co-evolution | by about 50% (illustration 1) and about 100% (illustration 2) | d05 (K19) | [S] |
| LLM FBS classification needs tuned rules | experts 54%, 93%, 87%; ChatGPT about 78% then 100% on the tuning items; held-out classifier 71% (n=31); F1 function 85 (n=11), behaviour 57 (n=7), structure 64 (n=13) | a19, b21, b22 (K06, K07) | [S] |
| Off-the-shelf LLMs fail domain function labels | GPT-3.5 0.04, GPT-4 Turbo 0.27, GPT-4o mini 0.20; fine-tuned test 0.89 at 10% data (681 samples), 0.84, 0.75, 0.68, 0.63 at 30, 50, 75, 90% | a20, b24, c06 (K08) | [S] |
| FBS graph helps sparse retrieval | 165 nodes, 220 edges, 1176 records; hard case n=8 precision 1.0 vs 0.50, recall 0.625 vs 0.375; easy case about equal | a21, c04 (K09) | [S] |
| Few-shot lowers LLM novelty | cosine to crowd: few-shot 0.804, zero-shot plus "unique" 0.746, base 0.748; hull volume crowd 0.294, zero-shot-unique 0.266, few-shot 0.2; 600 solutions, 12 problems | a22, c07, c08 (K10) | [S] |
| Critique pass is the biggest LLM diversity gain | 4000 GPT-4 solutions, 5 topics, 8 temp/top-P pairs, 8 prompt styles; humans (100 per topic) beat every LLM setting; classifier recall LLM 1.00 vs human 0.25-0.80 | c09-c11, d11 (K11) | [S] |
| FBS prompt chain beats free prompting (human in loop) | weighted score FBS 3.31, fixed 2.94, free 2.90, no AI 2.63; 80 people, 20 per group; Fleiss kappa 0.66; gain over free 0.41 | d01-d03 (K17) | [S]; t-tests look inflated |
| Scaffold gain shrinks with skill | novice gain 0.51 and 0.68 over two controls; professionals 3.35 vs 3.33 free (0.02) | d03 (K18) | [S] |
| Stage prompts inconsistent | DPP diversity front porch A 83.1, B 68.8, C 122.3, D 96.4; judge ICC validity -0.52 to 0.72 | a25, c16, c17 (K12) | [S] |
| Multi-agent design costs more, compiles less | about 6 nodes vs 1-2.8; about 650 s vs under 40 s; compile 34.8% vs 100%; coverage at most 20%; 60 runs | c12-c14 (K13) | [S] |
| LLM spread narrower than humans | soundness 0.298 vs 0.42-0.495; variance 0.042 vs 0.102 | c18 (K14) | [S] |
| Designers use GenAI for ideas, not choosing | idea generation 86.7%, problem definition 73.3%, selection human-led 86.7%; n=15 | c22 (K15) | [S] |

## 4. Mechanisms and models

### 4.1 The FBS state machine (implementable)

State: a record with list fields `R`, `F`, `Be` (expected behaviours, each linked to an F), `S` (current candidate), `Bs` (derived behaviours of S), `D` (output text). Lists, not prose, so code can count and compare.

Moves (a02, a03):

1. **Formulation**: the model reads F and writes Be items, each testable.
2. **Synthesis**: the model writes S meant to meet the Be list.
3. **Analysis**: derive Bs from S. In our schema this is a code run or check, not a model opinion (G2, G10).
4. **Evaluation**: code compares Be with Bs item by item. Output: the list of unmet items.
5. **Documentation**: write D from S.
6-8. **Reformulation I, II, III**: change S, Be or F when evaluation fails. Rule: pick the level by what failed. Structure-only miss: reformulate S. Be items unreachable by any S tried: reformulate Be. Be items that cannot satisfy F: reformulate F.

Control is by code. The next move follows the table, not the model's wish. Reformulation fires on a failed evaluation, never on a clock (G1). This follows Kannengiesser and Zhu: reformulation breaks the linear order only when needed (a03, a05).

### 4.2 Fast route (F to S)

Kannengiesser and Gero 2019 call a direct F-to-S jump system 1: catalogue lookup without verification (b16). In an agent this is "recall a known solution and answer". Rule: allow it only where the problem class has a high plain pass rate (S0 gate); otherwise force Be and Bs. Claim K20 suggests skipping Be marks fixation and error-prone runs, but that rests on one descriptive session.

### 4.3 Trace diagnostics (a06, a07)

Code tags each step of an agent trace R/F/Be/Bs/S/D and computes:

- issue mix (share of steps per code);
- first-order Markov matrix (what follows what); second-order (issue after process);
- first-passage time per issue (mean steps before the same issue returns);
- linkograph entropy (link density; the authors tie it to fixation and commitment, untested here).

Hypothesis only: low entropy plus long first-passage on S flags a stuck loop. In past work this toolkit found a lack of evaluation (process 4) in 3D virtual-world sessions (a07).

### 4.4 Co-evolution measure (d04, d05)

Log every new problem-side item (R, F, Be) and every new solution-side item (S, Bs). Count only reciprocal triggers: a solution-side change that causes a new problem-side item, then the reverse. Do not count mode switches. Switch counts overstated co-evolution by about 50% to 100% in the one session tested.

### 4.5 Maher and Poon's algorithm (d07)

Two populations: problem space P and solution space S. Each generation, change one, check the fitness of the pair, and if fit is poor, refocus on the other. In the agent this is the O8 reframe operator plus a mutual-fitness check. No original numbers were found.

### 4.6 FBS-structured memory (c04, c05)

Store past cases as nodes in a realisation chain: a function failure comes from a behaviour failure, which comes from a structure failure. Retrieve by walking within a hierarchy level. The benefit shows only when records are scarce and differently worded (K09).

### 4.7 Design-by-analogy pipeline (a24, b27)

Five phases: retrieval, mapping, transfer, evaluation, storage. The problem is encoded as an FBS dependency graph, clustered into abstract functions, and analogues are retrieved by embedding similarity above a threshold. No experiment, one qualitative motorcycle case. Concept only.

## 5. What holds up

**Holds (established).**

- The FBS vocabulary codes protocols across domains and expertise levels, with human coder agreement of 80-95% and kappa 0.78 where reported (b01, b08). K01, K02. Caveat: coding takes two coders per protocol plus arbitration, so studies stay small (b02).
- Problem and solution co-evolve in practice. Fixed rational-plan models fit practitioners poorly (a17, a04, a27). K16. Two lines of support: the Ralph survey and cases, and Suwa and Guindon via secondary citation in a04.

**Contested.**

- **Expertise.** Song 2016: engineers decompose and recompose about 22% of the time against about 15% for students (d up to 2.55), and seniors look like freshmen. Luo 2021 (122 people): professionals and seniors look alike, first-years differ (level-1 share .12/.14 vs .06). Wells 2016: pre-engineering vs others, no difference on any FBS item (all p>0.05, N=40). Tasks, groups and measures differ, so this may not be a true conflict (b11). K04.
- **Pahl-Beitz as a predictive model.** Bs and S linear and F and Be nonlinear in all three datasets, but the model's Bs slope is far too low (0.065 vs about 0.12). The simulations are partly an unreviewed draft (a12-a14). K03.
- **Domain independence.** Only function shared a slope, p=0.06 (a13).

**Did not work or not shown.**

- Sophomore design education: only descriptive differences, 3 controls per semester, year 1 only (b04, b05).
- Elhambakhsh's fine-tuned test accuracy fell as training data grew (0.89 to 0.63). The first column of the paper's table is train accuracy, not test. Unexplained, treat as a fine-tuning artefact. No second study found (d12).
- Tanaka 2026: stage-style prompts changed diversity inconsistently, and judges barely agreed (a25, c17).

**Moderators.** Scaffold gain falls with skill (d03). An FBS memory helps when records are scarce, not when plentiful (c04). Few-shot raises fit and cuts novelty (c07).

**Missing.** Gero 1990 and Gero and Kannengiesser 2004 numbers. Kannengiesser and Gero 2019 H1/H2. Maher's case-based design. Replications of Maher and Poon. Any causal manipulation of the eight processes (d17, d18; K21, K22).

## 6. Language models

**1. FBS as a prompt scaffold (Chen 2024; d01-d03, b26).**

- Setup: a three-stage chain on gpt-3.5-turbo-0125: requirements to function, function to behaviour, behaviour to structure. A human picks among generated options at each hop. 80 participants in 4 groups of 20 (15 novices with 3-4 years of design education, 5 professionals with 8+ years each). 30 minutes each. 3 raters, Fleiss kappa 0.66.
- Result: FBS chain 3.31 (SD 0.58) vs fixed fine-tuned prompts 2.94 vs free ChatGPT 2.90 (SD 0.47) vs no AI 2.63. Gain over free prompting 0.41 on a 5-point scale. For the FBS group, novice/professional: novelty 3.53/3.60, feasibility 3.64/3.53, usability 3.58/3.00.
- Caveats: a human chooses words at every hop, so it is not an autonomous scaffold. No token control. The reported t of 6.64 implies about 60 scores per group, not 20 concepts, so the tests look inflated (d03, my arithmetic). Professionals gained 0.02 over free prompting. Single study.
- Earlier: Wang et al. 2023 used GPT-3 with FBS stage prompts (a26, details not seen).

**2. LLMs coding or classifying FBS.**

- Sahadevan 2024 (a19, b21-b23): humans wrote the rules over biweekly meetings and three expert reviews. The geometry case (structure or behaviour, since geometry assumes rigidity) shows fuzzy category edges. Experts 54/93/87%. ChatGPT with rules about 78%, then 100% on the tuning items only. Held out: 71% on 31 items, behaviour weakest (F1 57). Note: 100% is not held out; per-class n is 7-13.
- Elhambakhsh 2025 (a20, b24): off-the-shelf 0.04-0.27 on function labels of mechanical parts (7,568 parts). Fine-tuning on 681 samples gave 0.89 test accuracy. About 99% of generated labels fell in the predefined classes.
- Nearest held-out analogue outside design (Dunivin 2024; d09, d10): GPT-4 with a rationale, one code per call, kappa 0.68 vs 0.59 without rationale; 111 gold passages, 9 codes. Full codebook in one prompt 0.60 vs 0.46. GPT-3.5 0.34 vs 0.29. Rare codes were weakest. Rewording a definition fixed some items and broke others. Snippet only: decomposing the task reached kappa 0.744 (d16).
- Take: any tagger must be tested on held-out agent traces against human coders. Behaviour tags will be the least stable.

**3. FBS as a retrieval structure.** Fujiu 2025: the graph gained only when matching records were few (precision 1.0 vs 0.50 at n=8) (a21, c04). One toy domain (a LEGO assembly line).

**4. LLM behaviour on open design tasks (not FBS interventions).**

- Ma 2023 (a22, c07, c08): GPT-3 solutions rated more feasible and useful but less novel than crowd. Few-shot prompts raise similarity to crowd (0.804) and shrink hull volume (0.2 vs 0.294). The model repeats solutions with small edits.
- Ma 2024 (c09-c11, d11): GPT-4, 4000 solutions. Humans beat every setting on every diversity metric. No monotone effect of temperature or top-P. "Unique" scored lower than "creative" or "novel". A one-prompt critique-and-edit step gave the biggest gain. A persona line also helped. Classifier recall of LLM vs human origin: LLM 1.00, human 0.25-0.80.
- Tanaka 2026 (a25, c16, c17): GPT-4.1, temperature 0, 100 runs per prompt per problem, 4 prompts, 3 problems, 8 judges. A tree-of-thought prompt changed diversity inconsistently (front porch DPP 96.4 vs 122.3 for another prompt). Judge validity ICC -0.52 on one problem, so differences are not trustworthy.
- Bruggeman 2025 (c18, not re-read): GPT-4o soundness 0.298 vs 0.42-0.495 for humans; variance 0.042 vs 0.102.
- Ege 2025 (c19, not re-read): ChatGPT 4.0 directed two student builders in a 48-hour hackathon against 5 human teams and placed second of six. It dropped promising concepts early, added complexity and fixated. 116 prototypes overall; the LLM team built 15 at about 0.7 h each.
- Massoudi and Fuge 2025 (c12-c14): nine-role multi-agent system building a design-state graph. 60 runs. About 6 nodes vs 1-2.8 for a two-agent loop. Time about 650 s vs under 40 s. Code compile 34.8% vs 100% (DeepSeek R1 70B). Requirement coverage at most 20%. Temperature 0 to 1 never broke JSON but cut compilability (Llama 3.3 70B: 62.9, 94.7, 5% at T=0, 0.5, 1.0). Supports G7 and G9: more roles cost more and did not give quality.
- Zhang 2025 (c20, abstract only): FBS-inspired zero-shot chain of thought made an LLM mimic problem-driven vs solution-driven designers on static issue measures.
- Chen 2025 (c22): of 15 AI-group novices, AI helped idea generation (86.7%) and problem definition (73.3%); selection and evaluation seen as human-led (86.7%).
- Reviews and position papers with no data: the FMEA review claims FBS reduces conceptual errors (d13, b19, b20); Intelligent Design 4.0 (c15); Joshi analogy pipeline (a24); mechatronics agents (c24).

**What changed LLM output, by how much.** Critique pass: largest diversity gain, still below humans (c09). Few-shot examples: more fit, less novelty (c07). FBS stage chain with a human: +0.41 over free prompting (d02). Temperature: no monotone effect on diversity (d11). Fine-tuning: 0.04 to 0.89 on function labels (b24). Rules plus human tuning: 78% to 100% on tuning items, 71% held out (b21).

**What no study tests.** (a) FBS-labelled reasoning vs plain chain of thought at equal tokens. (b) Forced decomposition-recomposition. (c) An expected-vs-derived behaviour check ablated in an LLM design loop. (d) An FBS reformulation step against narrow output spread (K22, d14, d15).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Treat problem and solution as co-evolving. Let S2 REPRESENT be revised when a real failing output exposes a new requirement. Log each requirement change with the output that triggered it. Count reciprocal triggers, not mode switches. | S2/S5, run log | [E] | a04, a17, a18, a27, d05 (K16) |
| A2 | Reformulation fires on a failed compare, never on a clock. FBS itself says reformulation breaks the linear order. This restates G1. | G1, O8 | [E] | a03, a05 (K01) |
| A3 | Do not freeze one linear stage order. Keep the loop-backs in the state graph. | S graph | [E] as "do not freeze"; fit of specific models is [C] | a14-a16 (K03) |

A1-A3 duplicate existing guardrails and add no new state or operator. Nothing in this subfield alone justifies a new element, because no study shows FBS tagging helps a model (K22).

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | F/Be/Bs/S tags on scratch state: write expected behaviours before the candidate, derive Bs by code, then compare | S3/S4 | [S] | a02, a03, d14 (K01, K22) |
| T2 | Itemised expected-vs-derived compare before revise | S4/S5, G2 | [U] | d13, d15 (K22) |
| T3 | Forced decompose-then-recompose pass (O3 plus recompose check) | O3 | [C] | b06, b08, b01 (K04) |
| T4 | FBS stage chain (R to F to Be to S), code selecting at each hop | S3 | [S] | d01-d03 (K17, K18) |
| T5 | F/B/S nodes in memory for differently worded past cases | memory | [S] | a21, c04 (K09) |
| T6 | Critique-and-revise pass for divergent output, measured per token | O | [S] | c09, d11 (K11) |
| T7 | Few-shot vs zero-shot novelty cue in the divergent operator | O | [S] | c07 (K10) |
| T8 | Tag reliability gate before tags drive control (kappa above 0.7 vs human coders) | S, G10 | [S] | a19, d09 (K06, K23) |
| T9 | Trace diagnostics (entropy, first-passage) as impasse signals | S6 | [U] | a06, a07 |
| T10 | Seed-variance monitor for mode collapse | G | [S] | c18, d11 (K14) |
| T11 | Skip-Be flag: a run going F to S directly gets a verify step | S, G3 | [U] | b16, d06 (K20) |
| T12 | Use the scaffold only where the plain pass rate is low (gain shrinks with skill) | G12, S0 | [S] | d03 (K18) |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup cost counted, G7). At least 10 seeds per item. Judges are code where possible (G5, G8).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) FBS-tagged scratch | design and planning items with checkable specs; ARC as control | plain chain of thought vs Be-first plus Bs-by-code state | pass rate on held-out checks; tokens to first pass | small gain where explicit behaviours exist; none on ARC; a null is likely (K22) |
| B2 (T2) Evaluation step | tasks where the first attempt is often wrong | revise from located failing output vs revise after an itemised Be-vs-Bs compare | rounds to pass; final pass rate | fewer rounds if the compare names which Be failed |
| B3 (T3) Decompose-recompose | multi-part problems | no forced pass vs breadth-first decomposition plus recomposition check | pass rate; token cost | gain on large problems; loss on small ones (G11) |
| B4 (T4) Stage chain | open design items with a code-checkable rubric | free prompt vs R-F-Be-S chain with code selecting | rubric score; diversity | below the +0.4 on a 5-point scale seen with a human (d02) |
| B5 (T5) FBS memory | retrieval on reworded past cases | free-text vs F/B/S nodes | recall at k=8 on hard cases | gain on sparse cases (c04: 0.625 vs 0.375) |
| B6 (T6, T7) Divergence | idea-generation items | zero-shot plus cue vs few-shot vs critique pass | DPP and hull diversity; share novel by running check | critique pass best per token; few-shot lowest novelty |
| B7 (T8) Tag reliability | 200 agent-trace segments | 3 human coders vs LLM tagger, rationale vs none | kappa per label | kappa 0.6-0.7 overall; behaviour lowest |
| B8 (T10) Spread | any open item | plain vs plain plus reformulation step | variance across 10 seeds; embedding spread | spread narrower than humans; reformulation may widen it a little |
| B9 (T12) Skill moderation | same items on weak and strong model | plain vs scaffold on each | gain per model | gain shrinks on the stronger model |

## 9. What does not transfer, and why

- **Coder agreement figures** (80-95%, kappa 0.78) come from trained humans coding spoken protocols of 200-1280 segments. Our traces are text from one model, which may state things it did not do (G10). Tags from the model's own text are not evidence of the process behind it.
- **Expertise effects** describe human dyads on one window-opener task. Our agent has no expertise gradient, only different models. The scaffold-gain result (d03) is the nearest analogue and rests on 5 professionals.
- **Fast and slow design thinking** is a human theory. The F-to-S route is only an analogy to a plain model answer.
- **The Ralph survey** (1384 practitioners) is about software teams over months, not one run (a17).
- **Fine-tuning results** (Elhambakhsh) show tuning, not scaffolding (K08). We do not train.
- **Multi-agent role systems** (Massoudi and Fuge) conflict with G9; the cost and compile numbers argue against them.
- **Human-in-the-loop picks** (Chen 2024) are removed in our agent, so the effect size does not carry over.
- **FBS graph results** are on a toy line of 165 nodes (a21).
- **Pahl-Beitz simulations** show human students do not follow a fixed order. They do not say what an agent should do.

## 10. Open questions

1. Does labelling agent reasoning with F/Be/Bs/S beat plain chain of thought at equal tokens? No study (d14).
2. Held-out multi-coder kappa for LLM FBS coding of design protocols (d09 is only an analogue).
3. What do Gero 1990 and Gero and Kannengiesser 2004 report numerically? Does any experiment manipulate the eight processes?
4. Maher's case-based design and Maher and Poon 1996: numbers and replications (d18).
5. Does forced decomposition-recomposition help LLMs (d15)?
6. Does an itemised expected-vs-derived check reduce LLM design errors (d13, d15)?
7. Narrow LLM spread across seeds, and whether an FBS reformulation step restores it (c18, d11).
8. Is Elhambakhsh's falling test accuracy with more data reproduced (d12)?
9. Results of Kannengiesser and Gero 2019 H1 and H2 (d08, b17).
10. Is the Song vs Luo vs Wells expertise conflict real, or an artefact of task and measure?

## 11. Sources

[V] = opened and read in this run; [M] = snippet, abstract only, or secondary.

- [M] Gero (1990) Design prototypes, AI Magazine 11(4). https://core.ac.uk/download/229585332.pdf (a01, c25, d17; blocked)
- [V] Gero, Kan, Pourmohamadi (2011) Analysing design protocols. https://human.designsociety.org/download-publication/32332/Analysing+Design+Protocols%3A+Development+of+Methods+and+Tools (a02, a06-a08)
- [V] Kannengiesser and Zhu (2009) Ontologically-based evaluation of software design methods. https://www.cambridge.org/core/journals/knowledge-engineering-review/article/abs/ontologicallybased-evaluation-of-software-design-methods/ (a03-a05)
- [V] Gero and Milovanovic (2020) A framework for studying design thinking through measuring designers' minds, bodies and brains. https://www.cambridge.org/core/journals/design-science/article/framework-for-studying-design-thinking-through-measuring-designers-minds-bodies-and-brains (a09-a11, b12-b15)
- [V] Kannengiesser and Gero (c.2015 draft) Is designing independent of domain? https://www.tmci.minesparis.psl.eu/wp-content/uploads/2015/02/Is-Designing-Independent-of-Domain.pdf (a12-a14)
- [V] Can Pahl and Beitz' systematic approach be a predictive model of designing? Design Science (2018). https://www.cambridge.org/core/journals/design-science/article/can-pahl-and-beitz-systematic-approach-be-a-predictive-model-of-designing/ (a15, a16)
- [V] Ralph (2013) Software engineering process theory: SCI vs FBS. https://arxiv.org/abs/1307.1019 (a17, a18)
- [V] Sahadevan et al. (2024) Automated extraction and creation of FBS design knowledge graphs. https://arxiv.org/abs/2412.05868 (a19, b21-b23, c01-c03)
- [V] Elhambakhsh, Grandi, Ko (2025) Domain adaptation of LLMs for classifying mechanical assembly components. https://arxiv.org/abs/2505.01627 (a20, b24, b25, c06)
- [V] Fujiu et al. (2025) FBS model-based maintenance record accumulation. https://arxiv.org/abs/2510.11003 (a21, c04, c05)
- [V] Ma, Grandi, McComb, Goucher-Lambert (2023) Conceptual design generation using LLMs. https://arxiv.org/abs/2306.01779 (a22, c07, c08)
- [V] Ma et al. (2024) Exploring the capabilities of LLMs for design idea generation. https://arxiv.org/abs/2405.02345 (c09-c11, d11)
- [V] Chen, Zuo, Cai, Yin, Zhang et al. (2024) Towards controllable generative design (FBS prompts). https://spiral.imperial.ac.uk/entities/publication/583ee167-d56c-4594-a835-4d71092801cd (a23, b26, d01-d03); [M] https://doi.org/10.1115/1.4065562 (c21)
- [V] Joshi et al. (2025) LLMs for design by analogy. https://www.cambridge.org/core/product/2E3BE1BB69B975B1FA5FDFF8BB634B44/core-reader (a24, b27)
- [V] Tanaka, Nomaguchi, Fujita (2026) Design ideation through LLM-driven design thinking. https://www.cambridge.org/core/product/D09904A568B7FD59FFF3293D349B0A42/core-reader (a25, c16, c17); Wang et al. 2023 [M], cited only there (a26)
- [V] Gero, Kannengiesser, Crilly (2022) Abstracting and formalising the design co-evolution. https://doi.org/10.1017/dsj.2022.10 (d04-d07); Dorst and Cross (2001) and Maher and Poon (1996) [M] via Gero and Milovanovic (a27); Maher case-based design: no source opened (c26, d18)
- [V] Wells et al. (2016) pre-engineering vs non-engineering students. https://scholar.lib.vt.edu/ejournals/JTE/v27n2/wells2.html (b01-b03)
- [V] Williams, Paretti, Lee, Gero (2012) design education and sophomore design cognition. https://peer.asee.org/exploring-the-effect-of-design-education-on-the-design-cognition-of-sophomore-engineering-students (b04, b05)
- [V] Song et al. (2016) problem decomposition and recomposition. https://scholar-dev.cloud.lib.vt.edu/ejournals/JTE/v27n2/pdf/song.pdf (b06, b07)
- [V] Luo et al. (2021) systems thinking and FBS. https://www.ijee.ie/1atestissues/Vol37-5/20_ijee4113.pdf (b08-b11)
- [V] Kannengiesser and Gero (2019) Design thinking, fast and slow. https://www.cambridge.org/core/product/A200DC637BBDC982D288FC4F8A112DE7/core-reader (b16, d08); [M] conference version https://par.nsf.gov/servlets/purl/10095085 (b17)
- [V] Wikipedia, Function-Behaviour-Structure ontology. https://en.wikipedia.org/wiki/Function-Behaviour-Structure_ontology (b18, c23)
- [V] AI- and ontology-based enhancements to FMEA. https://arxiv.org/abs/2511.17743 (b19, b20, d13)
- [V] Massoudi and Fuge (2025) Agentic LLMs for conceptual systems engineering. https://arxiv.org/abs/2507.08619 (c12-c14)
- [V] Jiang et al. (2025) Intelligent Design 4.0. https://arxiv.org/abs/2506.09755 (c15)
- [V] Bruggeman et al. (2025) probabilistic methods for design cognition. https://www.cambridge.org/core/product/A4AEC038573F521DF5808BFFB6D9C67E/core-reader (c18; not re-read in the critique)
- [V] Ege et al. (2025) ChatGPT as an inventor. https://www.cambridge.org/core/product/1796F76E5B42020B42DCE586CF11E59B (c19; not re-read)
- [M] Zhang et al. (2025) emulating problem- vs solution-driven designers. https://openaccess.cms-conferences.org/publications/book/978-1-964867-39-7/ (c20, abstract only)
- [V] Chen et al. (2025) How generative AI supports human design. https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/6B60B59DF0CBE7 (c22)
- [M] Wang et al. (2025) LLM-enabled multi-agent mechatronics. https://arxiv.org/abs/2504.14681 (c24; abstract page, no numbers)
- [V] Dunivin (2024) Scalable qualitative coding with LLMs. https://arxiv.org/abs/2401.15170 (d09, d10); [M] https://arxiv.org/abs/2507.14384 (d16)
