# Software, spreadsheet, KB debugging: deep document

*Subfield C09.10. Schema part: S5 REVISE. Evidence: evidence_a-d.jsonl (ids a01-a28, b01-b28, c01-c25, d01-d23), claims.jsonl (K01-K26), critique.md. Related subfields researched in parallel (links only): Diagnosability; Readings in model-based diagnosis; Complexity of expert troubleshooting; Cognitive biases in software work; Logic programming and knowledge representation; Epistemic value and curiosity; Search over thoughts; Debiasing and cognitive forcing; Calibration and overconfidence.*

## 1. What it is

Model-based diagnosis (MBD) treats a broken artefact as a set of parts plus a model of how they should behave. Something is observed to be wrong. The diagnoser finds which parts, if assumed faulty, would remove the contradiction. This subfield covers the artefacts people actually debug with that idea:

- **Spreadsheets.** Each formula cell is a component. The user gives an expected value for a wrong output cell. The tool finds formulas that could explain the gap.
- **Knowledge bases and ontologies.** Each axiom or constraint is a component. A domain expert answers yes/no questions ("should this entailment hold?"). The tool picks the next question.
- **Software.** Each function or line is a component. Failing tests are the observations. Fault localisation ranks suspects.
- **Related artefacts.** Formal specs (SMT, PDDL), optimisation models (LP/MILP), feature models, agent logs.

Why it matters to our agent: S5 REVISE is the step where the agent has a failed answer and must decide what to change. Classical MBD gives a recipe. (1) Compute the set of suspects by code, not by opinion. (2) Pick the next check that best separates suspects. (3) Change only what the failing output implicates. (4) Gate the change with an independent check. The LLM literature of 2023-2026 shows, again and again, that skipping steps 1 and 4 is where models lose.

Scope note: the formal theory of MBD (Reiter, de Kleer) and diagnosability are covered by sibling subfields. This document spends effort on what is new: applied studies on artefacts, human studies, and LLM studies.

## 2. History and theories in depth

**Foundations (1987).** Reiter's "theory of diagnosis from first principles" defines a diagnosis as a minimal set of components assumed abnormal that restores consistency with observations. It is computed as a minimal hitting set over conflict sets [a25, not opened; known via the DynamicHS paper, a12]. A conflict is a set of components that cannot all be right given an observation. A diagnosis must hit every conflict.

**Configuration and KB debugging (2000s).** Felfernig, Friedrich, Jannach, Stumptner (2004) applied consistency-based diagnosis to configuration knowledge bases using test cases [a26, not opened]. Junker's QuickXPlain (2004) finds minimal conflicts by divide and conquer using a black-box consistency checker [a27, not opened]. FastDiag finds one preferred minimal diagnosis by divide-and-conquer consistency checks, without computing conflict sets first [c21].

**Interactive ontology debugging (2010-2012).** Shchekotykhin, Friedrich, Fleiss, Rodler turned the debugger into a dialogue. The system keeps a set of candidate diagnoses. It builds a query (a statement about what the intended ontology entails). Each answer removes diagnoses. Each query must remove at least one candidate whatever the answer, and the lower bound is log2(n) queries [a03]. Choosing the query by entropy (expected information gain) needed more than 50% fewer queries than split-in-half or random when the true diagnosis had 2 axioms [a01]. RIO (2012) added a risk-aware switch between entropy and a safe split rule, because priors on faults can mislead [a04].

**Spreadsheet debugging (2008-2017).** Before MBD, Ayalew and Mittermeir (2008) traced faults by interval-based testing and dataflow [a19, skimmed]. Jannach and colleagues (2013-2016) recast the sheet as a constraint problem and used hitting sets [b05, b01]. Fragment-based diagnosis (2015-2016) grouped copy-equivalent cells so users could check small pieces [a18, b03]. The EXQUISITE add-in packaged this for Excel [b04]. A rival, GoalDebug (Abraham and Erwig), proposed repairs from hand-built change-inference rules [b27].

**Making it fast (2016-2022).** Rodler's DynamicHS reuses the search tree between questions [a12]. RBF-HS searches best-first in linear memory [a13]. A 2022 taxonomy sorts diagnosis algorithms (complete or incomplete; conflict-based or direct; black-box or glass-box) [a14]. A reduction result shows any MBD problem can be posed as a KB debugging problem, so one interactive loop serves many artefacts [a28, a15].

**Human studies (2019-2022).** Rodler, Jannach, Schekotihin, Fleiss ran user studies of the OntoDebug tool. They found that people err in the loop and are overconfident [a06-a08].

**LLM era (2023-2026).** Three strands. (a) LLM fault localisation in software (AutoFL, Wu et al., AgentFL, LLM4FL) [b08-b13, c14, c15]. (b) Self-correction research: models cannot repair from their own doubt, but can from external feedback [b15-b18, d18]. (c) 2025-2026 work that puts a solver or runtime check inside the repair loop (DRAGO, SemLoc, ORLoopBench, SymDiag) [c01-c03, c12, c18, c23]. The third strand is classical MBD in new clothes: code computes the conflict, the model proposes the fix, an independent check accepts it. Very few studies run a true hitting-set loop with an LLM; the evidence is adjacent.

**Competing views.**
- Rule-based repair (GoalDebug) versus model-based fault finding. The model-based method is domain independent but needs expected values [b27, b28].
- Spectrum-based fault localisation versus MBD. Authors name them as complements [b28].
- Agent view (an LLM chooses actions) versus fixed pipeline. Agentless showed a fixed localise-repair-validate pipeline matches open-source agents at $0.70 per issue [b14].

## 3. Core findings with exact numbers

Status: established = several independent sources or replicated; single = one source; preprint = 2026 single-lab, not replicated.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Entropy-based query choice beats split-in-half and random in KB debugging | More than 50% fewer queries (target diagnosis 2 axioms, 7 real ontologies); up to 60% saving in good and average cases | Shchekotykhin et al. 2012 [a01] | Established (a01, a04, a10, b06) |
| Same method scales | Ontology over 33,000 axioms: true diagnosis in 190 s, 5 queries on average | [a02] | Single |
| A wrong query rule is costly | Overhead about 100%, up to 250% oracle effort; better vs worse of entropy and split differed by 190% to 1145% on average, max 2300% | Rodler and Schmid 2018 [a10]; RIO [a04] | Established |
| Dissertation claim on effort | Bad priors plus poor strategy can cost over 2000% more effort; RIO at least as good as the best rule in 100% of hardest KBs; best case factor 23 | Rodler 2016 [b06] | Single (one author) |
| Best rule depends on prior quality | Misleading priors: random best. Vague: MPS. Good: BME, close to entropy | [a10] | Single |
| Best-first sampling of diagnoses is not always right | Best-first best for ENT and SPL rules; for MPS needed up to over 100% more measurements (58 vs 25) | Rodler and Elichanova [a11] | Single |
| Reusing the search tree saves time | Less time than HS-Tree in 96% of sessions; median saving 52%, max 75%; hard conflict calls cut by median 74%; a hard call costs median 19x an easy one | DynamicHS [a12] | Single |
| Linear-memory search | Memory down by up to several orders of magnitude; runtime lower in over a third of min-cardinality cases | RBF-HS [a13] | Single |
| Direct diagnosis when conflicts are many | 146 ontologies; both methods finished 133; 13 only the direct method solved | Inv-HS-Tree [a05] | Single |
| FastDiag faster than QuickXplain-based hitting set | 415 configurations; parallel version speedup 1.28-1.65 at 8 cores | [c21, c22] | Single each |
| Spreadsheet MBD helps people | N=24 students, 1 sheet, 16 formulas, 1 error. Tool: 100% success, 163 s. No tool: 67% success, 547 s among solvers. p<0.05 | Jannach and Schmitz 2016 [b01] | Single, preliminary, not replicated |
| Spreadsheet MBD is fast | Over 140 formulas under 0.5 s; 700+ formulas, 3 faults, depth 3 under 4 s; speed-ups over 70% (2.2 s to ~630 ms) | [b02] | Single |
| Fragment-level diagnosis shrinks the suspect set | Course-planning sheet: 11,903 ms and 2,304 diagnoses (cell) vs ~14 ms and 2 (fragment); extra fragment tests gave exactly 1 diagnosis in all 5 sheets | Schmitz et al. 2016 [b03] | Single, simulated perfect user |
| Model type: count similar, speed very different | Diagnosis counts within one order of magnitude; abstract models up to over 4 orders faster; qualitative model matched value model in about a third of cases | Hofer et al. 2022 [a16] | Single |
| Real users err in query-based debugging | Study 1 (29 students): 77% of faults found, 34% (10 of 29) found the full true diagnosis. Wrong inputs 24% for negative test cases vs 10% positive. Study 2 (23): about a quarter made at least one wrong input | Rodler et al. [a06, a07] | Single group |
| Query tool vs test-case tool | Faults found 91.3% vs 89.1% (not significant); time 24.9 vs 34.0 min (p=0.0418); clicks 64 vs 139 (p<0.00001) | [a06] | Single, small N |
| Debuggers are overconfident | Mean confidence 83% vs 34% who found the true diagnosis | [a08] | Single |
| Even experts miss inconsistency | 3-formula DL KB; reasoner developers failed to see it | Cited in [b07] | Second-hand |
| LLM tool navigation beats SBFL | 798 bugs; acc@1 +19.7% (Defects4J), +166.7% (BugsInPy, GPT-3.5), +233.3% (BugsInPy, GPT-4); one GPT-4 run beat five merged GPT-3.5 runs | AutoFL [b08, c14] | Established (b08, b11, b13, c15) |
| AutoFL explanations are weak | 300 explanations from 60 bugs: 20% accurate, 26.3% with an inaccurate statement, 46.7% bland | [b10] | Single |
| Error log and context size | ChatGPT-4 function level +46.9% acc@1 over SmartFL; class level -49.9%; no error log -25.6%; leak-free StuDefects +52.9% | Wu et al. 2023 [b11, b12] | Single paper |
| Multi-agent localisation | AgentFL Top-1 157/395 (Top-3 183, Top-5 187); LLM4FL 326/675 vs AutoFL 275 vs AgentFL 311. Different benchmarks | [b13, c15] | Single each |
| Coarse-to-fine localisation by LLM | Agentless: file-level contains the true file 81.7% (combined); skeleton view 58.33% at $0.02 vs full file 53.67% at $0.15 | [d11] | Established with b03 |
| Fixed pipeline competes with agents | SWE-bench Lite 96/300 fixed (32.00%), $0.70 each; audit: 4.3% leaked patches, 10.0% missing info, 5.0% misleading | Agentless [b14] | Single; model-era dependent |
| Gates lift correct fixes | Majority vote 77 (25.67%); + regression tests 81 (27.00%); + reproduction tests 96 (32.00%), cost $0.25; ceiling 126 (42.0%) | [d12] | Established with c01 |
| LLM-written tests are unreliable | 213 of 300 reproduction tests reproduced the issue; only 94 (44.1%) also passed after the true fix | [d13] | Single |
| Self-correction without external signal fails | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0 over two rounds; Self-Refine on Codex PAL 71.3 to 26.7 without a tool | Huang et al. [b15]; CRITIC [b18] | Established (b15-b18, d18) |
| External feedback quality is the bottleneck | GPT-4 repair 52.60% with human feedback vs 33.30% with own; competition level 14.67 vs 3.67 | Olausson et al. [b16] | Established |
| Execution evidence beats right/wrong signal | Spider +2 to 3% with explanation only; TransCoder GPT-4 77.3 to 90.4 with unit tests; MBPP 72.8 to 80.6 | Self-Debug [b17, c16] | Established |
| Solver diagnosis plus gate prevents breakage | Right-to-wrong regressions 1.3% vs 11.8%; +12.9 pp over zero-shot, +8.7 pp over LLM-diagnosis repair; 2,400 pairs: DRAGO 104 fixes vs 12 breaks, self-review 159 fixes vs 254 breaks | DRAGO 2026 [c01, c03] | Preprint |
| Diagnosis matters more than gate | Gate fixed: DRAGO beats LLM-diagnosis+gate in 16 of 20 configs, +7.1 pts; gating LLM review adds +1.1 | [c02] | Preprint |
| Sample-and-select weaker than diagnose-and-repair | FOL: zero-shot 78.6, sample-3 80.0, oracle-3 81.3, DRAGO 88.8 | [c04] | Preprint |
| Executable constraints beat free-form localisation | Where coverage ties, rank-1 in 40.9% vs 2.2% (SBFL) and 7.0% (Daikon); 68.4% verified, of which 93.6% correct | SemLoc [c12, c13] | Preprint |
| Stated confidence is a poor signal | LLMs state 0.9 or higher on 76.2% of answers; unverified third holds about three quarters of wrong answers; TRACE: 7 LLMs, 22,339 responses, confidence separates right from wrong poorly | [c13, d15, d16] | Established |
| Solver feedback inside the loop | ORLoopBench repaired within 5 steps 95.3% (Qwen3-8B-GRPO), about 86% for o4-mini and claude-sonnet-4; whole-model rewrite: MILP "Optimal" 85-90% but only 22-28% keep the correct objective | [c18, c19] | Preprint |
| Spreadsheet agents fail at debugging | SpreadsheetBench 2 (100 debug tasks): best 12% (Claude Opus 4.6), GPT-5.2 8%, Gemini 3.1 Pro 7%, DeepSeek-V3.2 10%, Qwen3.5 3%; error-value tasks best barely above 20%; one model fixed single errors in 34% of runs but passed 3% | Zhu et al. 2026 [a23, c10, c11] | Preprint |
| Real vs synthetic faults | FoRepBench execution match 0.80 (GPT-4.1) vs 0.41 on real seed set; GPT-4o 0.73 vs 0.35; Phi-3 0.58 vs 0.24; Mistral 0.51 vs 0.19 | Singha et al. 2025 [a21, a22, c05] | Single paper |
| General spreadsheet manipulation | 912 real questions: GPT-4o 18.35% single round, 16.96% multi-round; humans 71.33%; GPT-3.5 2.34 to 7.09 with rounds | SpreadsheetBench [b19, b20] | Single |
| Seeded-error detection varies widely | 12 seeded errors: Gemini 2.5 Pro 12; o3-mini-high and ChatGPT-4.5 11; GPT-4o-mini 2. On the 4-error Triangle sheet most models scored 0 | Thorne 2025 [c07, c08] | Single, one sheet, no repeats |
| Feature-model analysis by LLM | 12 LLMs, 16 operations: best 89.7%; reasoning 81.1% vs general 61.0%. FLAMA solver 18.45 s vs DeepSeek Reasoner 9,508 s | Le et al. 2026 [c20] | Preprint |
| Tool design shifts RCA | 375 cases: top-1 52.7% (L1), 68.8% (L2), 82.8% (L3), raw Python 85.4%; overrides of correct candidates outnumbered corrections | Luo et al. 2026 [c17] | Preprint |
| Failure attribution in agent logs | Best 53.5% agent-level, 14.2% step-level (Who&When, 127 systems). Hybrid 12.28% step at 149,177 tokens vs 4.39% all-at-once at 17,106. Bisection 6.90% at 34,659 tokens. A2P scaffold 47.46% / 29.31% | [b22, d01, d02, d03] | Established that LLM-only is poor; scaffold numbers share one small benchmark |
| EIG question choice for LLMs | UoT +38.1% relative success (5 datasets, 5 LLMs); FloDial troubleshooting GPT-4 closed-set 43.7% to 67.3%. BED-LLM +37.4 points over direct prompting, never decreased | [d09, d10] | Two sources, toy tasks, simulated answerers |
| LLMs trust prose over code | 7 LLMs, 456 Java bundles: doc faults caught 67-94%; detection falls 21-43 points when only the implementation changes | TRACE [d15] | Single |
| Multi-turn degradation | Average 39% drop across six generation tasks, 200,000+ simulated conversations | Laban et al. [d20] | Single, wide |

## 4. Mechanisms and models

Written so an engineer can build each piece. 4.1 to 4.6 are the core of a scaffolded S5.

### 4.1 Conflicts and hitting sets (the suspect list)
Inputs: a set of components C (formulas, axioms, functions, steps), a consistency check for any subset against the observations, and at least one wrong observation.
1. A conflict is a subset of C inconsistent with the observation. Find one minimal conflict with QuickXPlain: split the set in two, test each half, recurse into the half that still conflicts.
2. A diagnosis is a minimal set that intersects every conflict. Build a tree: take the first conflict, branch on each component in it (assume that component is the fault), find the next conflict that avoids the branch, repeat. Close branches that are supersets of a known diagnosis.
3. Rank diagnoses by prior fault probability (formula complexity, edit history) or by cardinality. Cap cardinality at 3; bigger sets are unreadable and costly [b02].
4. Keep the tree across steps (DynamicHS idea) instead of rebuilding after each answer [a12].
Direct alternative: FastDiag finds one preferred diagnosis without conflict sets [c21]. Use it when conflicts are very many [a05].
For an LLM agent, the consistency check is the expensive, unreliable part. Make it a code call (run the test, run the solver, evaluate the formula), never a model opinion (G2, G5).

### 4.2 Spreadsheet as constraint problem
Each formula cell becomes a constraint relating its output to its inputs. The user supplies test cases: input cell values and the expected value of an output cell. A value-based model uses exact values. A functional-dependency model says only "correct or faulty". A qualitative model says "too low" or "too high". Abstract models are much faster (up to over 4 orders) and return a similar number of diagnoses [a16]. Implementation: use the abstract model first; use the value model only to separate remaining ties.

### 4.3 Fragment (coarse-to-fine) diagnosis
Group cells into fragments: copy-equivalent formulas merge into one unit. Diagnose at fragment level first (2 diagnoses instead of 2,304 in the best case [b03]). Then ask for test cases only on the few suspect fragments. This works because people (and agents) can check a small piece even when they cannot state the whole output. The LLM equivalent is Agentless: file, then class/function skeleton, then lines [d11]. The Who&When hybrid does the same on logs: pick the agent, then scan that agent's steps [d02]. Skipping a level hurts [K21].

### 4.4 Query selection by expected information gain
Given candidate diagnoses D with probabilities p(d), a query q splits D into those predicting yes, those predicting no, and those silent. Choose q that minimises expected posterior entropy. With reliable priors this means yes-mass near 0.5.
1. Generate candidate queries from the current diagnoses (statements on which diagnoses disagree).
2. For each query compute the answer probability under each diagnosis, then the expected entropy after the answer.
3. Ask the best. Update p(d) by Bayes. Repeat until one diagnosis passes a probability threshold or the budget ends.
4. Guard against bad priors: RIO tracks how well past answers matched the prior and switches to a safe split rule when the prior misleads [a04]. A fixed wrong rule cost about 100% and up to 250% [a10].
5. Rule by prior quality: good priors, entropy or BME; vague priors, MPS; misleading priors, random or split [a10].
LLM version (UoT, BED-LLM): the LLM only supplies hypotheses, candidate questions and likelihoods P(answer | hypothesis). Code computes the information gain and picks the question [d09, d10]. In BED-LLM, real EIG with the LLM as likelihood model beat asking the LLM for a "good question" [d10]. This fits G5.

### 4.5 Oracle error model
Humans answer wrongly: 24% of negative test cases and 10% of positive ones, and about a quarter of participants made at least one wrong answer [a07]. An LLM oracle is also wrong: LLM-written reproduction tests verified the true fix only 44.1% of the time [d13]. Implementation: store each answer with its source and confidence; allow retraction; when the surviving candidate set empties, backtrack and re-ask the lowest-confidence answers first. Entropy methods assume reliable answers and fail with noisy ones [d10]. No study measures the damage at a 10-25% error rate (K23).

### 4.6 Repair gate (accept or reject a change)
Pattern from DRAGO and Agentless:
1. A solver or test produces the diagnosis (error message, unsat core, minimal conflict set, failing test).
2. The model proposes a minimal patch that cites that diagnosis.
3. Accept only if (a) the original failure is fixed, (b) the regression set still passes, and (c) intent is intact (objective unchanged for LP [c19]; examples not merely fitted).
4. If the gate fails, keep the old artefact; retry with the new diagnosis or stop.
Numbers: regressions 1.3% vs 11.8% [c01]; regression tests added 4 fixes and reproduction tests 15 more on SWE-bench Lite [d12]. Model-written tests are weak, so use an independent gate (the existing regression suite) first [K20].

### 4.7 Cardinality and cost control
Single fault first, then double, cap at 3. Cost grows fast with simultaneous faults [b02]. Hard consistency calls cost a median 19x an easy one and dominate runtime [a12]. For an agent this maps to tokens: spend on a few discriminating checks, not many easy ones.

### 4.8 Confidence by verification
Trust a located fault only if a counterfactual check agrees: change the suspect, re-run, see the failure change as predicted. SemLoc's verified answers were 93.6% correct; the unverified third held about three quarters of the wrong ones [c13]. Agreement among repeated runs (AutoFL) is a weaker, cheaper hint [b09].

## 5. What holds up

**Holds up (several sources).**
- Information-based query choice beats halving and random when priors are informative (a01, a04, a10, b06, a09). The gap is large (over 50% fewer queries).
- Without an external signal, LLM self-correction does not help and often hurts (b15-b18, c03, d18). With real execution, tests or a solver, it helps.
- Coarse-to-fine localisation cuts the suspect set and cost, for spreadsheets (b03) and LLM code localisation (d11).
- LLMs with navigation tools beat spectrum-based localisation in software (b08, b11, b13, c15), but explanations are poor (b10).
- Synthetic fault benchmarks overstate real ability (a21/a22: 0.80 vs 0.41; b14 audit).
- LLM-only failure attribution on long logs is poor (b22-b24, d01-d06).
- Verbalised confidence is unreliable (c13, d15, d16).

**Moderators.**
- Prior quality decides which query rule wins (a10).
- Context size: function level +46.9%, class level -49.9% against baseline (b11).
- Error log: -25.6% without it (b11).
- First-answer quality: more rounds helped weak models up to nearly tenfold and did not help GPT-4o (b20).
- Feedback quality: human feedback 52.60% vs own 33.30% (b16).
- Granularity: agent-level 53.5% vs step-level 14.2% (b22).
- Model size: CRITIC gains grow with size (b18).

**Failures and tensions.**
- b15 says self-correction hurts; b16-b18 say it helps with external feedback. They agree once the split is "external signal". Even then, Self-Debug without unit tests gained only 2-3% on Spider (b17).
- AgentFL Top-1 157/395 and LLM4FL 326/675 are different benchmarks and not comparable (b13, c15).
- Detection is not repair: Gemini 2.5 Pro found 12 of 12 seeded errors (c07) while most models scored 0 on the Triangle sheet (c08).
- End-to-end sheets (600+ cells, best 12%, a23) versus small constraint sets (up to 89.7%, c20) differ in task shape.
- Tool design: structured tools raised top-1 from 52.7% to 82.8%, but raw Python reached 85.4%, and overrides of correct candidates outnumbered corrections (c17).
- Bisection did not improve step accuracy (6.90 vs 4.39 all-at-once, about 2x tokens) (d01). The hybrid reached 12.28% at about 9x tokens (d02). Scaffolds did better (A2P 47.46% / 29.31%, d03), but Who&When and A2P share one small benchmark where annotators were uncertain on 15-30% of items (b22).

**Interventions that worked.** Solver or runtime check as diagnosis plus gate (c01-c03, c12); regression plus reproduction tests (d12); stronger or human feedback (b16); coarse-to-fine (b03, d11); information-gain question choice (a01, d09, d10); abstract models for speed (a16).

**Interventions that did not work or are doubtful.** Gating an LLM's own critique (+1.1 points, c02); sample-three-and-select (c04); bisection for step accuracy (d01); reasoning models for failure attribution (R1 beat GPT-4o in 1 of 4 cells, b23); more interaction budget for spreadsheet agents (a24); extra rounds when the first answer already runs (b20).

**Replications.** The central human spreadsheet result (b01) has no replication: one sheet, 16 cells, one fault, 24 students (K24). The leakage check for LLM localisation (StuDefects, b12) is the authors' own. Most KB-debugging results use simulated oracles and injected faults (a01, a02, a04); the one real-user study shows oracle errors and overconfidence (a06-a08). Classic critiques of fault localisation (Parnin and Orso 2011; Pearson 2017) were recalled from memory and are not used (b25, b26).

## 6. Language models

**Locating the fault.** With tool navigation and real tests, LLMs beat spectrum-based localisation on real bugs: acc@1 +19.7% (Defects4J) to +233.3% (BugsInPy, GPT-4) [c14]. GPT-3.5 loses at acc@3 and acc@5 [b08]. Agent pipelines reach Top-1 157/395 [b13] and 326/675 [c15]. Leakage is not fully ruled out; a post-cutoff set still showed +52.9% [b12].

**What changed it.**
- Real failing output: removing the error log cost 25.6% [b11].
- Narrow scope: class level fell 49.9% below baseline [b11].
- Repo navigation by function calls (AutoFL), staged multi-agent work (AgentFL), graph retrieval plus reflection (LLM4FL; segmentation and prompt chaining add up to 22% Top-1) [b13, c15].
- Executable constraints (SemLoc): 40.9% vs 2.2% (SBFL) where coverage ties [c12].

**Explaining the fault.** Weak. 20% of explanations accurate; 46.7% bland; developers were misled by wrong suggestions [b10].

**Self-repair.** Without external feedback it degrades (CommonSenseQA 75.8 to 38.1, GPT-3.5 [b15]). With execution feedback it improves (TransCoder GPT-4 77.3 to 90.4 [b17]). The bottleneck is diagnosis quality, not the number of samples [b16]. On formal specs LLM self-review made 254 breaks against 159 fixes [c03].

**Spreadsheets.** Real data is hard: SpreadsheetBench GPT-4o 18.35% vs humans 71.33% [b19]. FoRepBench execution match fell from 0.80 to 0.41 from synthetic to real [a22]. SpreadsheetBench 2 debugging best 12%; failures are insufficient inspection and wrong target-cell choice; agents spend over 60% of the trajectory inspecting [a23, a24, c11]. Error-value tasks (#REF!, #NUM!) are hardest, best barely above 20% [a23]. Repairs succeed when a local patch is enough (wrapping a VLOOKUP) and fail on whole-logic rewrites [c06]. A 60M-parameter model trained on formulas beat larger models in 10 of 14 settings on last-mile repair [b21, d21]. Seeded-error detection ranged 17% to 100% across 20 models on one small sheet [c07].

**Knowledge-base and formal artefacts.** Reasoning models beat general ones on feature-model analysis (81.1% vs 61.0%) but cost about 500x the runtime of a dedicated algorithm (9,508 s vs 18.45 s) [c20]. Whole-model regeneration in optimisation repair makes the solver say Optimal while solving the wrong problem (22.4-28.2% keep the right objective for GPT-5.4 and Claude Sonnet 4.6) [c19]. Constraint-level repair with an IIS conflict set as feedback kept the objective and repaired in 5 steps for 86-95% [c18].

**Attribution in logs.** LLM step-level 4-14% on Who&When [b22, b23, d02]. A scaffold lifted it to 29-47% [d03]. A trained 8B tracer beat prompted frontier models by up to 18.18% [d04]. Smaller method changes give +2.2 to +11.1 points (BLADE, d05) and +3.45 / +4.40 (EMFA, d06).

**Question selection.** UoT +38.1% relative; BED-LLM +37.4 points, never decreased [d09, d10]. Only toy tasks with simulated answerers.

**Trust and confidence.** Models trust prose over behaviour: detection drops 21-43 points when only the implementation changes [d15]. Stated confidence is 0.9 or higher on 76.2% of answers regardless of correctness [c13]. Verbalised confidence beats token probabilities for RLHF models (about 50% relative cut in calibration error, d17), but the white-box edge is small (AUROC 0.522-0.605, d16). Multi-turn tasks lose 39% on average [d20], which argues for compact state kept in code, not long chat histories.

**Cost.** Agentless: $0.70 per issue, plateau at about 40 samples [b14, d12]. Skeleton context $0.02 vs $0.15 [d11].

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Revise only from a failing check that code produced, and cite it.** Part: G2, S5. [E] Evidence b15, b16, b17, b18, c01, c03, d12, d18. Already G2; this subfield adds numbers (self-review 159 fixes vs 254 breaks; solver gate 1.3% vs 11.8% regressions).
2. **Accept a revision only through an executable gate: existing regression checks first, then a new reproduction check.** Part: S5 then S4/S8, G3. [E] d12, c01, c02, d13. Order matters because model-written checks verify the true fix only 44.1% of the time.
3. **Diagnose coarse to fine; never skip a level.** Part: S5, O3 Decompose. [E] b03, d11, d02. Pick the region (file, fragment, agent), then the unit inside it. Use a cheap skeleton view first ($0.02 vs $0.15).
4. **Narrow the context before asking the model to locate a fault, and include the real failing output.** Part: S5, G2. [E] b11 (class level -49.9%; no log -25.6%), b22, d11.
5. **Do not trust the model's own confidence or fault explanation.** Part: G10, G4. [E] b10, c13, d15, d16. Verify by a counterfactual check (change the suspect, re-run).
6. **Choose the next check by information gain computed in code, with the model supplying hypotheses and likelihoods; fall back to a plain split when weights look unreliable.** Part: O (select probe), S5, G5. [E] for KB debugging with reliable oracles (a01, a04, a10, b06); LLM versions d09, d10 on toy tasks. Treat the real-fault LLM case as a test (below).
7. **Keep intent fixed during revision; patch constraints, do not regenerate the artefact.** Part: G3, S5. [E, thin] c19 (22.4-28.2% keep the correct objective after rewrite), c06. Two sources, one a preprint; adopted because it matches G3.
8. **Test on real or post-cutoff failures, not only injected ones.** Part: G3, G7. [E] a21/a22 (0.80 to 0.41), b12, b14.
9. **Do not force revision loops when the first answer already passes its checks.** Part: G1, G7. [E] b20 (GPT-4o 18.35 to 16.96 with more rounds).

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Code-computed ranked suspect list given to the model vs free-form "find the bug" | S5 | [S] | b01 (N=24, one sheet), b02, c12, c01 |
| Fault cardinality cap: single, then double | S5, G12 | [S] | b02 |
| Information-gain probe choice vs halving vs free-form, equal tokens, real faults | O select probe | [S] | d09, d10, K19 |
| Oracle noise handling: answers stored with source, retraction, re-ask lowest-confidence | S5, memory | [S] | a07, d13, d10 |
| Counterfactual verification as the trigger to re-open S5 | S6, G1 | [S] | c12, c13 |
| Agent-then-step hybrid vs single pass on long traces | S5, memory | [C] (about 9x tokens for +7.9 points) | d01, d02, d03 |
| Small specialist formula repairer as a tool after the cell is located | S5, tools | [S] | b21, d21 |
| Solver diagnosis for spec or LP artefacts instead of model self-review | S5 | [S] preprint | c01-c03, c18 |
| Keeping two-fault candidates alive in the loop | S5 | open | b02, d07, K26 |
| Dependency-graph tracing tool for spreadsheet error values | S5, tools | open | a24, K25 |

## 8. Concrete tests on our bench

All tests: both arms at equal tokens (setup and tool tokens counted, G7). At least 3 seeds, paired difference.

1. **Suspect list vs free-form (S5).** Items: 30 programs or small sheets with one planted fault, plus 10 real regressions. Arm A: model alone. Arm B: code runs each check and ddmin over lines or cells, gives a ranked suspect list. Metric: fault at top-1; final pass rate. Expected: B higher (literature: 100% vs 67% for humans, b01; SemLoc 40.9% vs 2.2% on ties, c12).
2. **Gate vs no gate on revision (S5).** Items: 40 where half the first answers are already right. Arm A: model self-review then revise. Arm B: diagnosis from failing output only; accept a patch only if earlier-passing checks still pass. Metric: right-to-wrong regressions; final accuracy. Expected: regressions about 1-2% vs about 12% (c01).
3. **Coarse-to-fine vs flat (S5, O3).** Items: 30 long artefacts (multi-file code, long traces, wide sheets). Arm A: whole artefact. Arm B: skeleton or region first, then units. Metric: location accuracy; tokens. Expected: equal or better accuracy at a fraction of tokens (d11).
4. **Information-gain probe vs halving vs free-form (O).** Items: 30 hidden-fault games, 8-30 candidates, a cheap code oracle. Arm A: model picks next check. Arm B: code scores model-proposed checks by expected entropy. Arm C: split in half. Metric: checks to isolate the fault; tokens. Expected: B at most C at most A in checks (a01, d10).
5. **Oracle noise sweep.** Same items as 4. Inject wrong oracle answers at 0%, 10%, 25%. Arm A: trust all. Arm B: re-ask the lowest-confidence answer when the candidate set empties or answers conflict. Metric: correct isolation rate. Expected: A degrades sharply at 25%; B slowly (d10). Fills K23.
6. **Verification vs self-consistency as re-open trigger (G1, S6).** Items: 60 located faults, half wrong. Arm A: re-open if 5 samples disagree. Arm B: re-open if a counterfactual patch-and-rerun does not change the failure as predicted. Metric: share of wrong localisations caught; tokens. Expected: B catches more (c13).
7. **Hybrid vs single pass on long traces (S5).** Items: 30 long agent logs with a known fault step. Arms: all-at-once; agent-then-step; agent-then-step plus final counterfactual check. Metric: step accuracy per token. Expected: hybrid gains at about 9x tokens (d02); the third arm shows whether the check is a cheaper route.
8. **Objective-preserving repair (G3).** Items: 20 optimisation or spec items with known objective. Arm A: regenerate. Arm B: patch constraints, check objective vs original. Metric: share keeping the right objective. Expected: B far above the 22-28% seen for rewrites (c19).
9. **Spreadsheet error-value faults with a tracing tool.** Items: 20 multi-sheet workbooks with #REF!/#NUM! faults. Arm A: cell-read tool. Arm B: plus precedent-trace tool for the failing cell. Metric: target cell correct; final pass. Expected: B up (a24). Fills K25.
10. **Double fault.** Items: 20 with two planted faults. Arm A: single-fault loop. Arm B: keeps cardinality-2 candidates. Metric: both found. Expected: A fixes one and declares success (K26).

## 9. What does not transfer, and why

- **Human time numbers (163 s vs 547 s).** They measure human search under a 15-minute cap on one sheet. Our cost is tokens (b01).
- **Interactive expert questions.** In KB debugging the oracle is a human expert and each query is costly. Our agent has a code oracle for most items. Query minimisation matters only when probes cost tokens or are capped (a01, a06).
- **Hitting-set engineering (DynamicHS, RBF-HS, FastDiagP).** Gains are time and memory, not reasoning quality (K02). Our candidate sets are tens, not thousands.
- **Scale numbers (33,000 axioms, 146 ontologies).** Not our artefacts (a02, a05).
- **Formula-only fault model.** Jannach and Schmitz cover formulas, not data errors, layout or missing cells, and need an expected value (b28). Without a trusted expected output S5 cannot run. For open-ended tasks with no oracle this machinery does not apply.
- **Student participants.** CS students on a 16-cell sheet are not practising users or LLM agents (b01).
- **Injected-fault benchmarks.** Cleaner than real faults (a22, b14).
- **Software-only signals (coverage, stack traces).** No equivalent in ARC or riddle items, where the check is a held-out example (G3).
- **Model-era numbers.** AutoFL, Wu et al., Agentless used GPT-3.5/4. The 2026 results (DRAGO, SemLoc, SpreadsheetBench 2, ORLoopBench, SymDiag, c17, c20) use newer models but are single-lab and unreplicated.
- **Trained components (AgenTracer-8B, GRPO model, FLAME).** We do not train; only the prompting or tool pattern transfers.

## 10. Open questions

1. Does the Jannach and Schmitz spreadsheet result replicate with more sheets, more fault types and practising users? Nothing found (K24).
2. Does an LLM that proposes ranked candidates and picks the next probe by information gain beat free-form debugging at equal tokens on real faults? Only toy tasks so far (K19).
3. How much does a 10-25% wrong-answer rate hurt entropy probing vs re-ask strategies with an LLM or flawed-check oracle? (K23.)
4. What is real LLM performance on error-value spreadsheet cases, and which tool pattern lifts it? (K25.)
5. Does keeping several faults in play help or hurt LLM repair loops? (K26.)
6. Which gate removes right-to-wrong regressions at the lowest token cost? Regression tests first is the best current answer; no direct token-cost comparison with a counterfactual check.
7. Is counterfactual verification better than self-consistency as the trigger to re-open S5, and at what cost?
8. Does best-first sampling matter when candidates come from an LLM, not a hitting-set tree (a11)?
9. What happens when the LLM itself runs the hitting-set loop? No direct study; DRAGO, SemLoc, ORLoopBench are adjacent.
10. Do attribution gains (A2P, hybrid) hold outside the small Who&When benchmark?

## 11. Sources

[V] = opened and read this session (full text or abstract page; see caveat). [M] = snippet or memory only.

- [V] Jannach and Schmitz (2016) Model-based diagnosis of spreadsheet programs. https://web-ainf.aau.at/pub/jannach/files/JOURNAL_ASE_2014.pdf (b01, b02, b27, b28)
- [M] Jannach and Schmitz (2016) Springer page, blocked. https://link.springer.com/article/10.1007/s10515-014-0141-7 (a17, c24)
- [V] Schmitz, Hofer, Jannach, Wotawa (2016) Fragment-based diagnosis of spreadsheets. https://web-ainf.aau.at/pub/jannach/files/Workshop_SEMS_2016.pdf (b03)
- [V] Schmitz and Jannach (2017) EXQUISITE. https://web-ainf.aau.at/pub/jannach/files/Conference_VLHCC_2017.pdf (b04)
- [V] Jannach, Baharloo, Williamson (2013), skimmed. https://web-ainf.aau.at/pub/jannach/files/Conference_ENASE_2013.pdf (b05)
- [V] Jannach and Schmitz (2015) Calculation fragments. https://arxiv.org/abs/1503.03267 (a18)
- [V] Ayalew and Mittermeir (2008), skimmed. https://arxiv.org/abs/0801.4280 (a19)
- [V] Shchekotykhin et al. (2012) Interactive ontology debugging. https://arxiv.org/abs/1107.4303 (a01, a02)
- [V] Shchekotykhin et al. (2010) Query strategy. https://arxiv.org/abs/1004.5339 (a03)
- [V] Rodler et al. (2012) RIO. https://arxiv.org/abs/1209.3734 (a04)
- [V] Shchekotykhin et al. (2012) Direct computation of diagnoses. https://arxiv.org/abs/1209.0997 (a05)
- [V] Rodler et al. (2019/2022) Are query-based ontology debuggers really helping? https://arxiv.org/abs/1904.01484 (a06-a08)
- [V] Rodler (2020) Expert behaviors and question types. https://arxiv.org/abs/2001.05952 (a09)
- [V] Rodler and Schmid (2018) Active learning heuristics. https://arxiv.org/abs/1807.03083 (a10)
- [V] Rodler and Elichanova (2020/2022) Do we really sample right? https://arxiv.org/abs/2009.12178 (a11)
- [V] Rodler (2020) DynamicHS. https://arxiv.org/abs/2012.11078 (a12)
- [V] Rodler (2020/2022) RBF-HS. https://arxiv.org/abs/2010.04282 (a13)
- [V] Rodler (2022) Taxonomy of diagnosis computation. https://arxiv.org/abs/2207.12583 (a14)
- [V] Rodler (2023) Habilitation thesis; also logged as the source of a16 and a28. https://arxiv.org/abs/2306.12850 (a15, a16, a28; a16 is Hofer et al. 2022, check the exact record before citing)
- [V] Rodler (2016) Interactive debugging of knowledge bases. https://arxiv.org/abs/1605.05950 (b06, b07)
- [V] Lambrix (2019/2020) Completing and debugging ontologies. https://arxiv.org/abs/1908.03171 (a20)
- [M] Reiter (1987) Theory of diagnosis from first principles. https://doi.org/10.1016/0004-3702(87)90062-2 (a25)
- [M] Felfernig et al. (2004) Consistency-based diagnosis of configuration KBs. https://doi.org/10.1016/S0004-3702(03)00117-6 (a26)
- [M] Junker (2004) QuickXPlain; Rodler (2020) explanation. https://arxiv.org/abs/2001.01835 (a27)
- [V] Felfernig, Schubert, Zehentner, FastDiag. https://arxiv.org/abs/2102.09005 (c21)
- [V] Le et al. (2023) FastDiagP. https://arxiv.org/abs/2305.06951 (c22)
- [V] Kang, An, Yoo (2024) AutoFL. https://arxiv.org/abs/2308.05487 (b08-b10, c14)
- [V] Wu et al. (2023) LLMs in fault localisation. https://arxiv.org/abs/2308.15276 (b11, b12)
- [V] AgentFL (2024). https://arxiv.org/abs/2403.16362 (b13)
- [V] Rafi et al. (2025) LLM4FL. https://arxiv.org/abs/2409.13642 (c15)
- [V] Xia et al. (2024) Agentless. https://arxiv.org/abs/2407.01489 (b14, d11-d13)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b15)
- [V] Olausson et al. (2024) Is self-repair a silver bullet? https://arxiv.org/abs/2306.09896 (b16)
- [V] Chen et al. (2024) Self-Debug. https://arxiv.org/abs/2304.05128 (b17, c16)
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 (b18)
- [V] Ma et al. (2024) SpreadsheetBench. https://arxiv.org/abs/2406.14991 (b19, b20, d22)
- [V] FLAME (2023). https://arxiv.org/abs/2301.13779 (b21, d21)
- [V] Zhang et al. (2025) Who&When. https://arxiv.org/abs/2505.00212 (b22-b24, d01, d02)
- [M] Parnin and Orso (2011). https://dl.acm.org/doi/10.1145/2001420.2001445 (b25, not used)
- [M] Pearson et al. (2017). https://dl.acm.org/doi/10.1109/ICSE.2017.62 (b26, not used)
- [V] Singha et al. (2025) FoRepBench. https://arxiv.org/abs/2508.11715 (a21, a22, c05, c06)
- [V] Zhu et al. (2026) SpreadsheetBench 2. https://arxiv.org/abs/2606.29955 (a23, a24, c10, c11)
- [V] Vaccarino et al. (2026) DRAGO. https://arxiv.org/abs/2610.22568 (c01-c04)
- [V] Thorne (2025) LLMs for spreadsheets (FLARE). https://arxiv.org/abs/2506.17330 (c07, c08)
- [V] Thorne (2023) ChatGPT for spreadsheet formulas. https://arxiv.org/pdf/2309.00095 (c09)
- [V] Yang et al. (2026) SemLoc. https://arxiv.org/abs/2603.29109 (c12, c13)
- [V] Luo et al. (2026) Tool design for agentic RCA. https://arxiv.org/abs/2610.05009 (c17)
- [V] Ao, Simchi-Levi, Wang (2026) ORLoopBench. https://arxiv.org/abs/2601.21008 (c18, c19)
- [V] Le et al. (2026) Product line validation with LLMs. https://arxiv.org/abs/2604.20523 (c20)
- [V] Cui et al. (2026) SymDiag. https://arxiv.org/abs/2608.08786 (c23)
- [M] Huang; Stechly; Tyen as cited by DRAGO. https://arxiv.org/pdf/2610.22568 (c25)
- [V] West et al. (2025) Abduct, Act, Predict. https://arxiv.org/abs/2509.10401 (d03)
- [V] Zhang et al. (2025) AgenTracer. https://arxiv.org/abs/2509.03312 (d04)
- [V] Guo et al. (2026) BLADE. https://arxiv.org/abs/2610.18780 (d05)
- [V] EMFA (2026). https://arxiv.org/abs/2610.11600 (d06)
- [V] Hou et al. (2026) EDGE. https://arxiv.org/abs/2609.01360 (d07)
- [M] Listing of 2026 failure-attribution preprints. https://arxiv.org/search/?query=failure+attribution+multi-agent+LLM&searchtype=all&order=-announced_date_first (d08)
- [V] Hu et al. (2024) Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271 (d09)
- [V] Choudhury et al. (2026) BED-LLM. https://arxiv.org/abs/2508.21184 (d10)
- [V] Wang and Hong (2025) Time Travel. https://arxiv.org/abs/2511.18854 (d14)
- [V] Ulfat et al. (2026) TRACE. https://arxiv.org/abs/2604.03447 (d15)
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (d16)
- [V] Tian et al. (2023) Just ask for calibration. https://arxiv.org/abs/2305.14975 (d17)
- [V] Kamoi et al. (2024) When can LLMs correct their own mistakes? https://arxiv.org/abs/2406.01297 (d18)
- [V] Chen et al. (2022) CodeT. https://arxiv.org/abs/2207.10397 (d19)
- [V] Laban et al. (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120 (d20)
- [V] Chopra et al. (2024) Interaction patterns for debugging with LLMs. https://arxiv.org/abs/2402.06229 (d23)

Caveat on [V]: critique.md notes that many [V] items were abstract-page reads only (d03-d08, d14-d23). Numbers from b01, a06-a08, a23, c01-c03, c12-c13 are one-read and not re-verified. Treat them as single-read.
