# Troubleshooting search strategies: deep document

*Subfield E08.04. Evidence files: evidence_a-d.jsonl. Claims: claims.jsonl (K01 to K34). Corrections: critique.md. Ids such as a09 or K07 point into those files. Schema parts refer to research_notes/single_agent/SCHEMA.md (G1-G12, S0-S9, O1-O8, section 4b). Note: SCHEMA.md has no operator for test selection. Where this document says "test selection" it means a new code module that would sit at S7 (discriminating test) and S4 (test), plus a candidate ledger in memory.*

## 1. What it is

Troubleshooting search strategy is the question of which test to run next when something is broken and the cause is unknown. The system has many places the fault could be. Each test costs time or money. The searcher wants to find the fault with the fewest or cheapest tests.

The field has five strands.

1. **Half-split.** Test the middle of a chain. Keep the bad half. Repeat. For a chain of N units this needs about log2 N tests (a08). It is the textbook rule, taught since Miller, Folley and Smith (1953).
2. **Topographic versus symptomatic search** (Rasmussen). Two ways to use a reference. Topographic search uses a template of normal operation and looks for the mismatch. Symptomatic search uses the abnormal pattern and matches it to known faults (a17, a18). The names drift between papers (K02).
3. **Cost-weighted search.** When tests have different prices, rank them by probability of finding the fault per unit cost (Simon and Kadane, a14). Or rank by information gain per cost. Exact optimum is NP-hard. Greedy is the standard design (a21, b23).
4. **Functional versus structural search.** Follow what a part does (function) or where it sits and what connects to it (structure). The two papers that use these words mean different things (a02 versus a17).
5. **Efficiency studies, human and machine.** How good are people at this? How good are language-model agents? Can code that picks tests improve the agent?

The question for our project is narrow. Our agent is a language model inside a scaffold. It has no training. The scaffold can do the book-keeping in code. Does code-side test selection beat the model choosing its own tests, at equal tokens? The best answer found is: probably yes on closed, enumerable fault lists, and unknown on open ones. No study counts tests-to-solve at equal tokens (K23). That is the core test of this subfield.

## 2. History and theories in depth

### 2.1 Half-split and the 1950s training tradition

Half-split came from military electronics training in the early 1950s (Miller, Folley and Smith 1953). The rule set, as Burroughs 1979 reports it (a08, a13):

- Test the input and the output of a chain of units.
- If input is good and output is bad, test the middle of the bad half. Repeat.
- For N units in a chain, log2 N checks are enough. An 8-stage example needs 3 checks.
- For a divergent flow, the rule differs: if any output is normal, suspect the stage at the divergence point.
- If a reading is ambiguous, test another point as near as possible until a reading is unambiguous.

The log2 N claim has strict conditions: one fault, a linear chain, equal test cost, reliable tests (a08). Break any of them and half-split is no longer optimal.

The one direct experimental test of half-split, Goldbeck, Bernstein, Hillix and Marx (1957), could not be reached (b31, d16). We do not know its effect size. Treat "half-split is efficient for people" as untested here.

### 2.2 Bayesian model of the 1960s: BETS

Rigney and colleagues at USC built a Bayesian model (BETS) that picks each next test by the largest expected uncertainty reduction on a symptom-to-malfunction matrix (a10). Facts, second-hand through Burroughs:

- 39 trainees on one circuit, six malfunctions each. They were about one third as efficient as BETS.
- A follow-up with 36 advanced trainees did better on time, steps and correct solutions. Only a little over half behaved like Bayesian processors.
- Burroughs notes BETS did not separate skill groups (too insensitive) and judged it unrealistic for human memory limits.

So the "ideal" selector existed in 1966. It beat novices by about three times. Real technicians did not behave like it.

### 2.3 Field data: technicians do not half-split

Bryan and Schuster (1959) and Rigney et al. (1961), reviewed in a11: 422 records of real fault finding. 71 percent of first replacements were wrong. Technicians often held enough information to isolate the fault and did not notice. They kept making redundant checks. Evans and Smith (1953) saw perseveration: some kept testing stages that earlier results had already ruled out, mostly in the stage they knew least about (a12).

Burroughs 1979 (a09) coded two certified TV repairmen over 40 trials. Fault-localisation actions: half split 0, middle-to-trouble 0, output-to-input 0, input-to-output 1, anchoring and adjustment 8, schematics 5, senses 4. Senses were used first in 40 of 40 trials. Critique correction: the table counts trials where a heuristic appeared, not exclusive choices. So "mostly anchoring" is too strong (8 of 40 trials, 20 percent). The 0 of 40 for half split is solid. Weakness: 2 technicians, TV sets, one coder.

### 2.4 Rasmussen and Jensen 1974

The founding study of the topographic/functional distinction (a01 to a07). Think-aloud with six skilled repairmen at a nuclear research lab. 45 cases recorded, 30 analysed. 8 instrument types (22 analog systems, 8 digital). Each instrument had its own fault. All figures re-checked in critique.

They found fault finding is a search through a hierarchy: subsystem, stage, component. Three routines:

- **Topographic search**: trace the signal path and give each point a good/bad verdict. In 1974 this means scanning by position.
- **Functional search**: match a faulty feature of the response to the subsystem that produces that feature.
- **Search by evaluation of the fault mode**: reason from the faulty response to a cause and a location.

Counts across 30 protocols: 31 functional searches, 82 topographic, 87 evaluations of fault mode, 75 check measurements. 21 of 30 protocols have exactly one functional search and 5 have none, so functional search is the usual opening move (a02, a04). Nearly 70 percent of the 31 functional searches were sent to the next field by the failed function alone.

Of 75 check measurements: 45 percent confirm a fault location, 30 percent confirm a "what to look for" hypothesis, about 20 percent are individual points in an overall topographic search. That last 20 percent is the nearest thing to half-split (a05). No count of strict halving is given.

Other findings:

- About 70 percent of the 82 topographic searches took their search field from a previous search or a decision to repeat.
- Only about 40 percent of topographic searches succeeded and led to a local search.
- After a failed topographic search: 23 percent return to an earlier indication, 17 percent repeat the search, 10 percent take a break.
- Men prefer many cheap, independent good/bad checks over few well-chosen measurements plus reasoning. The authors call this informationally wasteful but rational if the aim is saving time and mental load (a03). The rationality claim is argued, not measured.
- When a routine fails, men repeat it with another parameter (DC voltage, then AC, and back) instead of reasoning from how the system works. Suggesting functional reasoning gave no significant change (a06).
- "Point of no return" (a07): once a familiar search field is chosen, the value of a reading is dropped after a good/bad verdict. Men did not check whether a measuring point was informationally redundant.

The word "symptomatic" does not appear in this paper (critique, K02). It comes from Rasmussen 1981 and 1986. The data are small: six men, coded by the authors, no efficiency scores on purpose.

### 2.5 Formal search theory: Simon and Kadane 1975

Simon and Kadane (a14 to a16) proved the rule for searching for any one goal when each site has probability p and cost c: the order that minimises expected cost is descending p/c. Proof by exchange argument. Extension to partially ordered search joins slices into indivisible blocs; the optimum is a sequence of maximal blocs with falling p/c ratios (a15). They separate best-value, shortest-path and satisficing search. Fault finding is satisficing: find the fault and stop (a16).

Limits. One goal, independent sites. It does not cover a test that splits many candidates at once. The scan is OCR-garbled, so the ratio is read from the proof structure.

### 2.6 Model-based diagnosis and active testing

- **Entropy selection (de Kleer, Raiman and Shirley 1992, second-hand).** Pick the measurement with the lowest expected entropy over candidate diagnoses. Siddiqi and Huang (c01) report that single-fault isolation cost is on average comparable to log2 of the number of measurement points on ISCAS-85 circuits. That is the half-split bound reached by a general method.
- **One-step lookahead is optimal at unit cost and equal priors** (Pattipati and Alexandridis 1990, cited in a21, not opened). In practice it is near optimal.
- **Feldman, Provan and van Gemund 2010 (a20, a22, b22).** Greedy active testing (FractalG). Remaining minimal-cardinality diagnoses fall geometrically with rate p about 0.7 (mean R2 0.88). Greedy differs from exhaustive search by 5.4 percent in decay rate on 74182, and is far faster. Exhaustive search timed out above 20 controls. The authors say greedy can be made arbitrarily bad by constructed models.
- **Pattipati et al. 1997 (b23).** Single-fault test sequencing with test costs is solved by dynamic programming or AND/OR search with entropy and Huffman lower bounds. Cost O(3^n) in tests. Multiple fault isolation is super-exponential. On the Graham and Garey pathological example, certainty-equivalence did better than information heuristics.
- **Siddiqi and Huang 2011 (c02).** Hiding sub-circuits (abstraction) always helps the compiler but does not always cut the measurement count. Coarse-to-fine pays an overhead: locate the cone, then measure its inputs.
- **Gonzalez-Sanchez et al. 2011 (a23).** Entropy-greedy test choice for software. Up to 80 percent fewer tests than random order on Siemens suite programs and 3 Unix programs, 100 runs per point. On tcas and tot_info it was worse than random, because intermittency was poorly estimated and ambiguity groups were large.

### 2.7 Topographic versus symptomatic: the later definition

Venkatasubramanian et al. 2003 (a17 to a19), attributing to Rasmussen 1986:

- **Topographic** search uses a template of normal operation. The fault shows as a mismatch located in the system. It can be structural (follow information paths; keep bad paths; remove parts that also sit on good paths) or functional (check the function of groups of parts down a hierarchy).
- **Symptomatic** search uses the abnormal observations as a template matched against known fault patterns.

Trade-off as stated: topographic needs no fault model, is insensitive to novel and multiple faults, but returns a set of hypotheses with poor resolution. Symptomatic is economical but needs a reference pattern for the actual abnormal state and struggles with novel or multiple faults (a18). This is a review claim, not measured head to head. In practice: use symptom matching for familiar faults; use normal-reference search for novel ones (b30, secondary).

The same words carry two meanings. In 1974, topographic is position-wise good/bad scanning and functional is feature-to-subsystem matching. In 2003, topographic is search against a normal template and functional/structural are two kinds of topographic. We name tests by what they need instead: a normal state, a symptom-to-part map, or a causal model (K02).

### 2.8 Teaching versus practice, and training results

- Electronics lab instructors (b04): 20 interviews, 18 institutions. They named two strategies: forward topographic (input to output) and split-half. About half stressed treating a circuit as testable subsystems. Almost all called troubleshooting important; only half directly assess it. Self-report only.
- Student pairs (b01 to b03): 8 pairs repaired a two-stage op-amp circuit. Five used split-half; it did not make repair faster or slower. All five had first built a two-subsystem model with a gain per stage and predicted stage outputs (b02). Two pairs repaired about twice as fast as the rest; only one of them used split-half. No statistics. The fault was in stage 2, so a midpoint test was easy.
- Morris and Rouse 1985 (b25, abstract only): procedures, principles or both raised written knowledge scores but did not improve diagnosis of unfamiliar failures. Procedures made control steadier.
- Schaafstal, Schraagen and van Berlo 2000 (b27, d15; abstract only): a general strategy plus multi-level functional breakdown. Trained technicians solved about twice as many malfunctions, in less time and with less training time. The bundle mixes strategy and decomposition, so the effect cannot be credited to half-split.
- Gugerty 2007 (b28, snippet): 50 students on digital networks. Both domain knowledge and a general elimination rule were needed to raise elimination use.
- Starr and Storey 2026 (b26): grounded theory from 27 interviews. Confusion is central; intuitive leads and wrong jumps are common. No half-split content in the part read.

### 2.9 Experts fail on rare faults that look common

Besnard and Bastien-Toniazzo 1999 (d05, d06). A rare fault (a short on condenser C7) looked like a common IC386 failure. N = 3 novices (2 years of school) vs 3 experts (19 to 20 years).

- Mean tests to the cause: experts 39.33, novices 13.
- Tests of IC386: experts 18.66, novices 2. Share of tests on IC386: 47.45 vs 15.38 percent.
- Chained IC386 tests: 5.36 vs 0.
- First IC test came at 3.03 percent of the diagnosis for experts, 23.07 percent for novices.
- One novice never found the fault. No statistics. One circuit built to trap symptom matching.

The authors explain this as schema perseverance: symptoms launch a stored symptom-to-fault rule and revising it is slow. The mechanism is argued, not tested. It matches the Rasmussen finding that people repeat a routine instead of switching (K03).

### 2.10 Human networks with computers

Rouse 1978 (b24, abstract only): as network problem size grew, human diagnosis drifted from optimal. Forced pacing pushed people to brute force. A computer aid for bookkeeping cut wrong diagnoses. Rouse 1987 (a27, progress report): time to locate a failure varied with topographic, symptomatic or serendipitous search, and transfer-function models explained over 80 percent of variance. No per-strategy times. This supports putting book-keeping in code.

## 3. Core findings with exact numbers

Status key: established = two or more independent sources, numbers re-checked where possible. single = one source. contested = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Skilled technicians open with function search and run many cheap good/bad checks | 31 functional, 82 topographic, 87 fault-mode evaluations, 75 checks in 30 protocols; 21 of 30 protocols have exactly one functional search | a02, a04 (R&J 1974, 6 men) | established (K01) |
| Strict half-split is rare in practice | 0 of 40 trials (2 TV repairmen); about 20% of 75 checks are split-half style points | a09, a05 | established, small N |
| Technicians repeat a failed routine | after a failed topographic search 23% go back, 17% repeat, 10% break; only about 40% of topographic searches succeed | a04, a06 | established (K03) |
| Real fault records: wrong first repairs | 422 records, 71% of first replacements wrong | a11 | single, old |
| Trainees vs a Bayesian selector | 39 trainees about one third as efficient as BETS | a10 | single, second-hand |
| Half-split needs log2 N tests | 8 stages need 3 checks; holds only for single fault, chain, equal cost, reliable tests | a08 | established (K04) |
| Greedy information gain is near optimal | exact at unit cost and equal priors; greedy vs exhaustive 5.4% gap in decay rate; decay p about 0.7, R2 0.88 | a20, a21, b22, c01 | established; pathological cases exist |
| Under cost rank by p/c | exchange-argument proof; NP-hard in general | a14, a15, b23 | established (K05) |
| Greedy can lose to random if estimates are wrong | up to 80% fewer tests than random on most programs, worse than random on tcas and tot_info | a23 | established (K15) |
| Unaided LLM questioner wastes questions | 8 candidates: optimal 3.50, baseline 4.00, ChatGPT 7.24 questions (p<0.001); 73.77% vs 57.14% constraint-seeking questions; 56.67% of games kept asking after one candidate remained (29.29% of questions unnecessary); 39.44% of second-turn questions had zero gain | b15 | established (K06) |
| Best-split question chosen in a minority of turns | 19 to 36% of turns | b18 | single |
| Listing the candidate set each turn helps a little | 6.4 vs 7.24 questions; contradictory questions 13.50 to 8.42; spoiled games 12.22 to 7.78 | b16 | established (K09), not a cure |
| Code EIG planner: dialogue troubleshooting | FloDial (894 dialogues, 153 faults, 20 turns) GPT-4 43.7 to 67.3%, turns in successes 13.4 to 7.8 (the 13.4 is not cleanly confirmed); Claude-3-Opus 48.4 to 56.2; Gemini-1.5-Pro 30.1 to 53.6; Llama3-70B 28.8 to 47.1; Mistral-Large 14.2 to 30.1 | a24, b19, c03 | established (K07), simulated answerer |
| UoT headline | +38.1% average success across 5 datasets, 5 LLMs (probably relative, not points) | a24 | do not compare with BED-LLM units |
| Code EIG planner: 20 Questions | +37.4 percentage points over prompt-only across six models and three target sets; more than double in over half of setups; never lower; beats Split and Entropy ablation | a25, b20, c08 | established (K07) |
| Entropy-only vs Split vs full EIG | Entropy ablation is the strongest alternative, slightly above Split; both below full EIG. The "no gain" claim for entropy was not confirmed | a26, b21, critique | contested detail |
| Code layer in Battleship | targeting F1 Llama-4-Scout 0.367 to 0.764; GPT-4o 0.450 to 0.782; GPT-5 LM-only 0.716, little gain; win rate vs humans 8% to 82% (Scout); zero-gain questions 18.5% to 0.2% (Scout), 14.6% to 1.2% (GPT-4o) | c07, d13, d14 | single, strong |
| Most Battleship gain came from using the answers | question rule alone +0.021 to +0.026 F1; full Bayes about +0.4 F1 for weak models | d13 | single (K25) |
| Sample-and-score questions | k=5 matches mean human informativeness, k=10 beats it; 40% (CodeLlama) and 33% (GPT-4) of valid questions had EIG=0 | c05, c06 | single |
| Code selection beats LLM test choice at a fixed 3 tests | LLM chose global-best tests almost only; code Bayesian choice beat implicit, random and fixed-best sets on 3 tabular sets (GPT-4o, 4o-mini, 5 seeds). Accuracy values not read | d01 | single (K24) |
| Stop rule on belief change | about 50% fewer tests at equal or better accuracy than fixed 3 tests; GPT-4o-mini kidney 1.60, 1.48, 1.28 tests at thresholds 0.3, 0.5, 0.7; KL beat entropy 0.593 vs 0.572 (diabetes), 0.992 vs 0.972 (kidney) | d02 | single (K27), stop not separated from selection |
| BED costs time | 25 to 36 times slower than plain LLM questioner; only +4.2 and +1.8 points on 14B models | d03 | single (K34), workshop paper |
| Open answer spaces break planners | zero-shot DC/SP/GN: GPT-4o 54/63/35; UoT below zero-shot; ToT on 8B 45/53/2; SFT 0 on GN; rounds 5-10 add 7.7% process score, rounds 20-25 add 2.5% | c10, d04 | single/contested (K08, K28) |
| Reasoning mode: helps questioning | Qwen3-8B partly observable win rate 0.08 to 0.94, turns 29.60 to 15.82; Qwen3-30B Instruct 0.10 vs Thinking 0.93 | b17 | single |
| Reasoning mode: does not help isolation | HAProxy median 5xx reduction 86.6% no-think vs 86.3% think; completion tokens per step 157 to 1,546 (about 10x); GPT-OSS high effort 74.0% vs 88.5% low | c16 | contested (K11) |
| Cloud RCA agents: low full accuracy | OpenRCA 335 incidents, 5 models, 1,675 runs: 3.9% (Sonnet 4) to 12.5% (Gemini 2.5 Pro); 11.1 steps per run; 609.9 h; 1.38 B tokens | b05, c11 | established |
| Failure types in RCA | misread data 71.2%, incomplete exploration 63.9%, symptom as cause 39.9%, code error 27.2%, no cross-check 18.6% (overlap) | b06, c11 | single study; Table 3 inconsistent for code error, use 27.2% only |
| Prompt fixes failed, structure helped steps | hypothesis template and pitfall warnings: no meaningful gain (70 Bank tasks); shared code and errors: steps 11.9 to 9.2 (-22.1%), tokens per step +24.8%, total tokens -1.6%; perfect detections 0 to 2 of 41 | b07, b08 | established (K10), tiny counts |
| Right answer, no closed evidence | GPT-5 JRA 0.68 on both systems, evidence closure 0.21 and 0.15; best DeepSeek-V4-Flash JRA 0.76, ECR 0.38 | b09 | established (K12) |
| Ungrounded diagnoses | exact set 20.7%; any right service 76.0%; grounded in a path 61.5% | c12 (abstract+intro) | single |
| More steps are not better | steps GPT-5 5.56, Qwen3-8B 16.01; repeat rate 0.46 and 0.28 vs about 0; JRA 0.19 for Qwen3-8B; GPT-3.5 RCA 9.09% in 14.00 steps vs GPT-4 40.90% in 4.81; beyond 5 steps only token cost for GPT-3.5 | b10, b13, b14 | established (K14), confounded with model size |
| AIOpsLab | GPT-4 RCA 40.90%, ReAct 45.45%, FLASH 36.36%; localization top-1 61.54/53.85/46.15/30.77; FLASH 59.32% at 20 steps | b13, b14 | cells of 13 to 22 problems |
| No-fault exit missing | false fault on healthy networks SADE 24% (51/210), ReAct 16% (33/209), Claude Code 11% (21/198) | c13, d07 | single study (K30) |
| Vague tickets hurt | outcome 0.820 to 0.497; false-fault 47% for no-detail; 30 vs 13 tool calls; 549k vs 136k tokens; timeouts 9% of runs, 23% of spend | c14, d08 | single (K21) |
| Cost-aware ordering | MAI-DxO budgeted 79.9% at $2,396 vs o3 78.6% at $7,850; physicians (21) 19.9% at $2,963; 304 cases, test set 56 | c20, c21, d11 | single (K19, K31) |
| Bisect with LLM judge | 74.2% base, 80.6% fine-tuned, all-or-nothing, 32 questions; own arithmetic: about 94.3% per step if 5 steps | c17, d09, d10 | single (K32), d10 is arithmetic not data |
| Retrieved cases | JRA 0.70 to 0.79 (ICL), 0.76 (SOP) on OnlineBoutique; 0.58 to 0.56 and 0.62 on TrainTicket; closure not improved | b11 | single (K20) |
| Structured training | about twice as many malfunctions solved, abstract only | b27, d15 | single (K33) |
| DPO on high-EIG question pairs | 16 candidates: 44.4 to 51.1% success, questions 9.5 to 6.3; BigBench question count unchanged | c09 | single, needs training |
| Expert fixation on rare fault | 39.33 vs 13 tests; 47.45 vs 15.38% of tests on look-alike part | d05 | single (K29) |

## 4. Mechanisms and models

Each mechanism is written so it can be built.

### 4.1 Half-split on a chain

Input: ordered list of units u1..uN, a test function good(i) that says whether the signal after unit i is good, one fault, reliable tests.
Steps:
1. lo = 0 (known good point), hi = N (known bad point).
2. While hi - lo > 1: m = (lo + hi) // 2; run good(m). If good, lo = m. Else hi = m.
3. The fault is in unit hi.
Cost: ceil(log2 N) tests. In code the test function is a real run, not a model verdict, wherever possible (K18).
Breaks when: the chain is not linear (use the divergence rule, a08), tests are flaky or non-monotone (c18), there is more than one fault, or access cost differs per point.

### 4.2 Greedy information gain over a candidate ledger

State: a list of candidates h with prior p(h). A menu of tests t, each with a likelihood table p(outcome | h, t) and a cost c(t).
For each test t:
- predictive p(o | t) = sum over h of p(h) * p(o | h, t)
- expected gain G(t) = H(p(h)) minus sum over o of p(o | t) * H(p(h | o, t))
Pick the test with the largest G(t) (unit cost) or G(t)/c(t) (priced). Run it. Update p(h) by Bayes. Repeat until a stop rule fires.
With deterministic outcomes and equal priors this reduces to "pick the test that splits candidates most evenly", which is the Split baseline (b20). With noisy outcomes, entropy of the outcome alone is wrong. A test can have a balanced outcome and still tell nothing, because the noise is as large as the signal. True gain subtracts the conditional entropy (a26). So score gain, not marginal entropy.
Greedy is exactly optimal at unit cost and equal priors (a21) and near optimal in practice. It fails in constructed cases and when the likelihood table is wrong (K15).

### 4.3 The zero-gain filter

Before asking the model anything, code drops every test with G(t) = 0 given the current ledger, and every test once only one candidate remains. In Battleship this cut redundant questions from 18.5 to 0.2 percent and 14.6 to 1.2 percent (d14). In the human-like LLM game, unaided ChatGPT kept asking after one candidate remained in 56.67 percent of games (b15). This filter is cheap: it needs the ledger and a gain call, not a planner. Whether it alone captures most of the benefit is untested (K26, gap 2).

### 4.4 The p/c rule for priced tests

If the goal is any one fault, tests are independent sites, and each test checks one site: sort by p/c descending (a14). If tests have prerequisites (open the case before testing the board), group them into blocs and sort blocs by p/c of the bloc (a15). If a test splits many candidates at once, use G(t)/c(t) instead; p/c does not cover it. In SDBench the saving came from asking cheap questions before costly tests, and vetoing low-yield costly tests (c21, d11).

### 4.5 The model proposes, code scores (the common architecture)

Every successful LLM result in the sources has this shape (UoT, BED-LLM, LIPS/Battleship, ACTMED):
1. The model proposes k candidate tests (k = 5 to 10, c06).
2. Code or a simulation gives outcome likelihoods for each candidate.
3. Code scores the gain, drops zero-gain tests, picks one.
4. The test is run. The result goes into a ledger kept outside the model context.
5. Code updates the belief and checks the stop rule.
The model is used where it is strong: naming plausible tests and hypotheses. Code is used where the model is weak: counting, normalising and tracking.
Where likelihoods come from is the weak link. UoT and BED-LLM ask a model to simulate answers. ACTMED draws outcome tables from LLM simulation (d01). Nobody tested how much a wrong table costs (gap 3). Greedy with wrong estimates can fall below random (a23).

### 4.6 Stop rules

Four candidates, none compared against the others:
- Singleton: the candidate set has one member (and a verifying test passed).
- Belief change: stop when the best next test's expected shift in belief is below a threshold (ACTMED KL stop, about 50 percent fewer tests at equal or better accuracy, d02).
- Fixed cap: step cap tuned per model; past about 5 steps GPT-3.5 gained only tokens (b14).
- No-fault: all cheap normal-state checks pass, report no fault. No source tested this; agents lack it and report false faults on 11 to 24 percent of healthy networks (d07).

### 4.7 Choosing the grain: topographic first or symptom first

A rule as the literature states it, not measured: if the symptom matches a known fault and the cost of one confirming test is small, run the confirming test first. If two confirming tests on the same hypothesis fail, switch to a normal-reference or split test (inferred from d05, d06; no measured switch rule exists, K29). Coarse-to-fine pays an overhead and does not always lower the test count (c02). So the grain should be chosen by cost, not by dogma.

### 4.8 Repeat detector

Code tracks (test class, target, new evidence). If the same class on the same target repeats with no new evidence, force a different test class. This answers the human perseveration (a06, a12, d06) and the agent repeat-rate (b10: 0.46 and 0.28 for small models).

### 4.9 Bisect with a fragile oracle

Binary search over commits or stages with a model judging good/bad on each step is all-or-nothing. If steps are independent, 74.2 percent end to end for 5 steps implies 94.3 percent per step, and 10 steps would give about 55 percent (d10, own arithmetic with assumptions). Cheap checks to try: re-run the boundary pair at the end; vote of three on surprising splits; use a code test instead of a model verdict.

## 5. What holds up

### Replicated or multi-source

- Skilled people do not half-split. They anchor, run many cheap checks and repeat routines. Seen in R&J 1974 (6 men), Burroughs 1979 (2 men, 0 of 40), Dounas-Frazer 2016 (8 pairs; half-split label did not make repair faster), instructors teach it anyway (b04). Four small sources, all different tasks. Established, but every one has tiny N.
- Fixation after failure. Humans: a04, a06, d05. Agents: b10, c11, b12. Established (K03).
- Half-split and greedy gain bounds. Machine side is solid theory plus simulation (a08, a20, a21, c01). Established (K04).
- Unaided language models choose poor tests. ChatGPT (b15), Qwen3 (b18), Llama and GPT-4o in Battleship (c05, c07), ACTMED test popularity (d01). Four different task families. Established (K06).
- Code-side candidate tracking and gain scoring raises success on closed tasks. UoT, BED-LLM, Battleship, ACTMED. All use simulated answerers. Established, with that caveat (K07).
- In-context candidate tracking helps but does not remove failure (b16, c08, a07).
- Prompt-level fixes do not repair search errors in agents (b07, c10). Structure does a little (b08).
- Outcome accuracy overstates grounding (b09, c12).
- Stopping is weak in people and agents (a11, b12, b15, c13).
- More steps are not better (b10, b13, b14, c10, c16).

### Failures, boundaries, and contested points

- **Open answer spaces.** AR-Bench: UoT below zero-shot; ToT and SFT inconsistent; rounds beyond 20 added +2.5 percent process score (c10, d04). Authors blame large, infinite or non-eliminable answer spaces. That is their account, not a tested cause. No curve of benefit against fault-list size exists. Contested (K08).
- **Reasoning.** Big win in 20-Questions style (b17: 0.08 to 0.94 win rate for Qwen3-8B), none in HAProxy isolation at 10 times the output tokens (c16), small in AR-Bench. The task shape decides. Contested (K11).
- **Greedy vs pathological.** Greedy is near optimal in practice (a21, c01) and arbitrarily bad in constructed cases (b23, a20). Both are true. The guard is auditing the estimates.
- **Teaching vs practice.** Instructors teach forward trace and split-half (b04) but skilled technicians use almost none (a09). Structured method training doubled solves (b27, d15, abstract only) while knowledge instruction did not help unfamiliar faults (b25, abstract only). Contested (K17).
- **Compute cost of selection.** BED-LLM costs 25 to 36 times the inference time and gained only +1.8 to +4.2 points on 14B models (d03). An equal-token rule must charge for the selector.
- **Reward detail.** Plain information gain and the UoT uncertainty reward perform about the same (c04, 67.9 vs 67.1 on FloDial with GPT-3.5). The gain comes from simulation and propagation, not reward design. Differences of 1 to 3 points were not tested.
- **Entropy ablation.** Critique corrected an earlier claim: in 20 Questions the entropy ablation is the strongest alternative, slightly better than Split. The claim "entropy-only gives no gain" was not confirmed (a26, b21).
- **Coarse-to-fine.** Review recommends topographic narrowing then symptomatic matching (a18); an experiment shows abstraction adds overhead and does not always cut measurements (c02). Contested (K22).
- **Retrieval of past cases.** Weak transfer when keyed by symptom, because one symptom maps to several causes (b11). Abstracted runbooks do slightly more steadily. Single source.

### Interventions that worked

- Code ledger plus EIG selection (closed tasks).
- Zero-gain filter (redundant questions near zero).
- Belief-change stop (about half the tests).
- Passing raw code and errors between roles (steps -22.1 percent).
- Computer book-keeping for humans (b24, abstract).
- Asking cheap questions before costly tests (SDBench cost saving).
- Using answers in a Bayesian move choice (Battleship, +0.4 F1 for weak models).

### Interventions that did not work

- Hypothesis templates and pitfall warnings in prompts (b07).
- Suggesting functional reasoning to technicians (a06).
- Knowledge instruction for unfamiliar failures (b25).
- Plain tree search, SFT and UoT on open tasks (d04).
- Longer thinking on isolation (c16).
- Visual board format (c06: worse or no better than text).
- Strong reasoning models gained little from the code layer (d13: GPT-5 gained little; so scaffold value depends on the backbone).

## 6. Language models

### 6.1 How unaided models behave

- **Questioning games.** ChatGPT on 8 candidates: 7.24 questions against an optimal 3.50 and a simple baseline of 4.00. Its constraint-seeking questions were 73.77 percent against 57.14 percent for the optimal player, so it asks "narrow" questions but wastes them. In 39.44 percent of second-turn questions the gain was zero. In 56.67 percent of games it kept asking after one candidate was left (b15).
- **Best split.** Qwen3 models chose the max-gain question in 19 to 36 percent of turns (b18).
- **Waste.** In Battleship 33 to 40 percent of valid sampled questions had EIG = 0 (c05). Weak models front-load all 15 questions; strong players and GPT-5 use 8.0 to 8.2 against 14.1 to 14.9 for weak models (d14).
- **Test popularity.** In ACTMED, when the model picked tests itself it chose the globally best features almost exclusively. It did not tailor to the case (d01).
- **Agents in operations.** Full root-cause accuracy 3.9 to 12.5 percent in OpenRCA. Failures: misread data (71.2 percent), incomplete exploration (63.9 percent), symptom taken as cause (39.9 percent). Order of tests is not the main failure. Reading outputs is (b06, c11).
- **Process vs outcome.** GPT-5 JRA 0.68 but evidence closure 0.21 and 0.15 (b09). In OpenRCA 2.0, any right service in 76.0 percent, grounded path in 61.5 percent (c12).
- **Repetition and long runs.** Small models run 14 to 16 steps with repeat rates 0.46 and 0.28, and low accuracy (b10).
- **No-fault.** False faults on healthy networks 11 to 24 percent; vague tickets 47 percent; one in four dollars spent on timeouts (c13, d07, d08).

### 6.2 What changed behaviour, and by how much

| Change | Effect | Source |
|---|---|---|
| Model lists the live candidate set each turn | 7.24 to 6.4 questions; contradictions 13.50 to 8.42 | b16 |
| Code EIG planner (UoT) | FloDial GPT-4 43.7 to 67.3% | a24, c03 |
| Code EIG with outside belief (BED-LLM) | +37.4 points on 20 Questions | a25, c08 |
| Code Bayes layer, weak model | Scout F1 0.367 to 0.764; win rate 8% to 82% | c07, d13 |
| Code Bayes layer, strong reasoning model | GPT-5 0.716, little gain | c07, d13 |
| Question scoring alone | +0.021 to +0.026 F1 | d13 |
| Stop on belief change | about 50% fewer tests | d02 |
| Chain-of-thought reasoning, partly observable questioning | win rate 0.08 to 0.94 | b17 |
| Reasoning in fault isolation | no gain, 10x tokens | c16 |
| Prompt: hypothesis template, pitfall warnings | no meaningful gain | b07 |
| Shared code and errors between roles | steps -22.1%, total tokens -1.6% | b08 |
| DPO on EIG pairs (training, outside our rule) | 9.5 to 6.3 questions on 16 candidates | c09 |
| Panel of roles with budget tracker | same accuracy, about 3x cheaper than o3 | c20 |
| Past-case retrieval | +0.09 JRA on one system, -0.02 on the other | b11 |
| Fine-tuned bisect judge | 74.2 to 80.6% | c17 |

### 6.3 The measured-efficiency gap

The subfield focus was "LLM agents doing fault isolation with measured efficiency". The honest report: nobody has counted tests-to-solve for an agent choosing its own tests against a half-split or greedy selector, on known-fault systems, at equal tokens (K23, c25, critique gap 1). The closest are:

- ACTMED (d01): accuracy at a fixed 3 tests, tabular data, not tests-to-solve.
- Battleship (d13): moves and questions in a game with an exact world model.
- BED-LLM (c08): questions to success in games.
- Cloud-OpsBench (b10) and AIOpsLab (b14): steps, but agents read telemetry; they are not choosing between tests with known gain.

Almost every result uses a simulated answerer and a closed candidate list, not real instruments with noisy readings. Step counts in RCA benchmarks are confounded with model size.

## 7. What our agent should take

Status codes: [E] established, [S] single-source, [C] contested. Part: G guardrail, S state, O operator, M memory, or "new module" where SCHEMA.md has no slot. Evidence ids refer to evidence_*.jsonl.

### Add now (established)

1. **Candidate ledger in code, not in the prompt.** For any problem of the form "find which of several things is faulty, or which answer is right, using tests", code holds the list of live candidates and updates it after each result. The model sees the list but does not own it. Part: M, G3 (revise only from real output), new module at S4. [E] K09, K07. Evidence: b15, b16, c08, a07, a12, b24.
2. **Filter: no test with zero expected gain, and no test once one candidate is left.** Code removes them from the menu. Part: G5 (code selects), new module at S4. [E] for the problem (K06); the filter as a sole fix is [S] (K26, d14). Treat the problem as established and the exact size of the benefit as a test. Evidence: b15, c05, c07, d14.
3. **Model proposes, code scores.** The model names k = 5 to 10 candidate tests; code scores by expected information gain (or gain per cost) and chooses. Part: G5, S7 discriminating test. [E] on closed candidate lists with simulated answerers. Add it on closed lists only. Evidence: a24, b19, c03, a25, b20, c08, c05, c06, c07. Charge the selector's tokens to the arm (K34, d03).
4. **Repeat detector and forced class switch.** Code flags the same test class on the same target with no new evidence and forces a different class. Part: G1 (doubt on a signal), S6 impasse trigger. [E] that fixation exists in people and agents (K03); the specific fix is untested. Evidence: a04, a06, a12, b10, c11, d05, d06.
5. **Raw output passes through, not summaries.** Show the failing code and raw error to whoever reads them. Part: G2, G10. [E] (K10). Evidence: b07, b08, c10, c11.
6. **Guardrails as code, not prompt rules.** Hypothesis templates and pitfall text were echoed, not obeyed. Part: G (all). [E] K10. Evidence: b07, b08, c10.
7. **Score evidence closure along with the answer in our logs.** Right answers without a closed evidence chain are common (GPT-5: 0.68 against 0.21 and 0.15). Part: S6 log; S8 verify. [E] K12. Evidence: b09, c12, c11.
8. **Do not tell the model to "use half-split".** The label did not make student repair faster, and experts in the field rarely use it. Teach the code to compute the split; do not teach the model the name. Part: 4b (not to add: label-only strategy instruction). [E] K01, K16 partly. Evidence: a09, b01, b02, b04.
9. **Cap steps per backbone; do not raise it for weak models.** Past a knee, more steps add tokens. Part: G12. [E] K14. Evidence: b10, b13, b14. The cap itself is tuned in test T9.
10. **Keep reasoning short by default; allow it only at the test-selection step if a test shows it helps.** Consistent with G11. Reasoning gave no isolation gain at 10x tokens. [C] K11. Evidence: b17, c16. This is a "do not add reasoning everywhere" rule and is already G11.

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Code half-split / greedy selector beats model-chosen tests at equal tokens (tests to isolation) | new module, S7 | [S] K23, K24 | d01, c25 |
| Zero-gain filter alone vs filter + scoring vs scoring alone | S4 | [S] K25, K26 | d13, d14 |
| Stop on singleton vs belief-change vs fixed cap | S9 / stop | [S] K27 | d02 |
| No-fault exit plus healthy-system checklist | stop, S0 | [S] K30 | c13, d07 |
| Symptom structuring at intake | S0, S1 | [S] K21 | c14, d08 |
| Price tests (tokens and seconds) and use gain per cost; cheap-first | O test selection | [S] K19, K31 | c20, d11 |
| Likelihood table from model simulation, and cost of a wrong table | G5 audit | [S] K15 | a23, d01 |
| Closed-list boundary: grow the fault list from small to open | scope of G5 | [C] K08, K28 | c10, d04 |
| Switch rule: confirm a symptom match with at most 2 tests, then normal-reference or split | O1 grain, fixation guard | [S] K29 | d05, d06 |
| Check at every bisect split | O verify | [S] K18, K32 | c17, d09, d10 |
| Predicted value per block before any split | O | [S] K16 | b01, b02 |
| Abstracted runbooks vs raw case retrieval | M | [S] K20 | b11 |
| Functional breakdown given to the agent as a system model | S1 | [S] K33 | d15 |
| Coarse-first vs cost-chosen grain | O | [C] K22 | a18, c02 |

## 8. Concrete tests on our bench

Common setup. Arms get the same total token budget, including selector tokens and setup tokens (G7). Seeds: at least 3 per item. Report with intervals. Use code-checkable truth (known seeded fault). Item types need to be built on our bench: we do not have a fault-chain generator yet; it is a small piece of code.

| ID | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 core | Seeded single-fault chain of N = 8, 16, 32 units; test = probe a point (deterministic, free of noise); 30 items per N | A: model chooses the next probe. B: code half-split, model only reports what it sees. C: model proposes 5 probes, code scores by gain | tests to isolation; success at token cap | B and C need near log2 N; A needs 1.5x to 2x more (ChatGPT needed 2.07x optimal, b15). Add if B or C wins by a clear margin |
| T2 | Same, with noisy probes (reliability 0.9) and 20 items | A: model; B: greedy gain with correct reliability; C: greedy with wrong reliability; D: random | tests to isolation, success | B wins; C may fall near or under D (a23). Measures the cost of a wrong table |
| T3 | Closed fault list, tabular symptom-to-test matrix, 12 faults, 30 items | A: model free choice. B: filter only (no zero-gain test, stop at singleton). C: scoring only. D: filter + scoring | wasted tests (zero gain or post-singleton); tests to isolation | B captures most of the waste cut; D best |
| T4 | Priced test menu (costs 1 to 20 in tokens and seconds), 30 items | A: model order. B: gain per cost. C: cheap-first then gain. D: gain only | total cost to isolation; success | B or C beat A by cost; D wins on test count but loses on cost |
| T5 | Healthy-system items (no fault) mixed with faulty ones, 40 items, 50 percent healthy | A: plain. B: explicit healthy checklist plus no-fault answer allowed | false-fault rate; missed-fault rate | false-fault rate falls from 11 to 24 percent toward 5 percent; missed faults must not rise by more than 2 points |
| T6 | Stop rules on closed lists | A: fixed cap. B: singleton. C: belief-change threshold 0.05 bit. D: B plus verifying test | tests after sufficiency; accuracy | B or C save about 30 to 50 percent of tests at equal accuracy (d02) |
| T7 | Open fault list growth: 8, 32, 128, 512 candidates, with test results that eliminate only partly | A: model free. B: code scaffold from T1 (C arm). | gap B minus A against list size | benefit shrinks as the list grows; find the size where it crosses zero (AR-Bench boundary) |
| T8 | Look-alike rare fault: a common symptom pattern with a rare real cause, 30 items | A: plain. B: switch rule (after 2 failed confirmations of a hypothesis, run a normal-reference or split test). C: repeat detector only | tests to cause; share of tests on the look-alike part | B reduces look-alike share from about 47 percent toward 15 percent (d05) |
| T9 | Step cap sweep (3, 5, 8, 12, 20) on T1 and T3 items for each backbone | one arm per cap | success per token | knee near 5 to 8 steps (b14); the cap is per backbone |
| T10 | Bisect over a 32-step history with a model judge with injected error rate 0, 3, 6, 10 percent | A: single pass. B: boundary re-test at the end. C: vote of 3 on splits with surprising result. D: code oracle | end-to-end success | A drops to about 55 percent at 6 percent error over 10 steps (d10); B or C recover most |
| T11 | Symptom intake: same faults described crisply, vaguely, with a wrong cause named | A: raw ticket. B: structure step first (what failed, when, what is normal) | success; false-fault rate; tokens | B reduces the vague-ticket drop (0.82 to 0.50 in c14) |
| T12 | Reasoning placement on T1 items | A: no reasoning. B: reasoning at test selection only. C: reasoning everywhere | tests to isolation per token | B at best equal to A at far fewer tokens than C (c16) |
| T13 | Prior knowledge: functional breakdown given vs not | A: strategy text only. B: functional breakdown plus strategy. C: breakdown in code as ledger structure | success; tests | C at least B, B above A (d15, abstract only) |
| T14 | Process audit | all arms above | evidence closure: share of correct answers with a closed evidence chain | closure rises when ledger is in code (b09) |

## 9. What does not transfer, and why

- **Half-split's log2 N promise.** It needs a single fault, a chain, equal costs and reliable tests (a08). Most of our problems are not chains. Do not carry the name; carry the gain calculation.
- **Human strategy labels.** Rasmussen's 1974 routines describe six men on instruments. Topographic, functional, structural and symptomatic have changed meaning (K02). Our agent does not have eyes, hands or fatigue. The finding that technicians prefer many cheap good/bad checks is explained by saved time and mental load (a03). A model has no mental-load limit of that kind, but it has a token cost, so the cheap-check preference may still help. Not tested.
- **Fixation mechanism.** Schema perseverance in experts comes from stored rules and slow revision (d06). A model has no stored rules of this sort; it has priors from training and an anchored context. The behaviour looks similar (b10 repeat rates), the cause may differ. The fix (force a class switch) is cheap enough to try.
- **Human training results.** Structured method training doubled solves (d15), but that is training of memory and procedure over a course. We cannot train. The nearest equivalent is code that enforces the method, not text that describes it (K10, K17).
- **Simulated answerers.** UoT, BED-LLM and ACTMED use an LLM to answer questions and simulate outcomes. Real tests give real, noisy, sometimes surprising results. The gains may shrink. Battleship used a simulated spotter with fixed noise 0.1 (d13).
- **Dollar-priced tests.** SDBench prices are in dollars; inference was negligible ($0.15 per case). For us the selector costs tokens that are of the same order as the tests. The relation is reversed (K31). The 3x cost saving does not carry over.
- **Compute of BED.** 25 to 36 times slower per episode (d03). That is not affordable at equal tokens unless the scoring is done in cheap code and only the candidate proposal uses the model.
- **Telemetry RCA benchmarks.** Cloud-OpsBench, OpenRCA, AIOpsLab measure reading logs and metrics, not test choice. Their step counts are confounded with model size. Use them for failure modes, not for efficiency of search order.
- **Training-based fixes.** DPO on EIG pairs (c09), fine-tuned bisect judge (c17), amortised BED (d03) all train. They are out of scope under our no-training rule.
- **Strong reasoning backbones.** GPT-5 gained little from the Battleship code layer (d13). On strong backbones the scaffold's value is lower and the token cost is the same. Scaffold value depends on backbone strength (G12: search lifts a small model only where it has non-trivial success).
- **Medical panel.** The 304-case NEJM set has a 56-case test set, an LLM gatekeeper that may invent findings, and no healthy patients (c20, d11). The result is a hint on cost-aware ordering.

## 10. Open questions

1. Does an LLM that chooses its own tests need more tests than a code half-split or greedy selector, on known-fault systems, counted at equal tokens? No study (K23). Core test T1.
2. How much of the gain is the filter and how much the scoring? Battleship suggests the use of answers dominates (+0.4 F1) over question scoring (+0.02). No ablation separates filter from scoring (K25, K26).
3. Where do likelihoods and reliabilities come from, and how much does a wrong table cost against random? Nothing compares them.
4. How large and open can the fault list be before the scaffold stops helping? AR-Bench shows failure, with no size curve (K28).
5. How big are the structured-training effects (Schaafstal 2000, Gugerty 2007, Goldbeck 1957)? Only abstracts, one ratio (about twice), and one unreachable direct test.
6. When to start with symptom matching and when with a normal reference? No measured switch rule. Besnard 1999 shows the failure, N=3 vs 3, no statistics (K29).
7. What is the right stop rule? Singleton, cost-benefit, belief-change, or no-fault acceptance. Only the belief-change stop has a number (about 50 percent fewer tests) and it was not separated from selection.
8. Does cost weighting transfer from dollars to tokens and seconds, and does cheap-observation-first hold?
9. Does a model-as-oracle bisect need verification at every split, and what is the cheapest check?
10. Is half-split actually efficient for humans? The one direct test (Goldbeck 1957) was not reached. Burroughs found 0 of 40 use and no efficiency comparison.
11. Do prompt rules and code guardrails differ in violation counts? The evidence is indirect (b07, b08).
12. Which backbone strength makes the scaffold worthless? GPT-5 gained little in Battleship; the line is unknown.
13. Does the human preference for many cheap checks have an LLM analogue, where several cheap tests per step beat one costly well-chosen test at equal tokens?
14. Unchecked items. Not re-opened in the critique pass: Feldman 2010 details, Simon and Kadane (OCR), Venkatasubramanian, Siddiqi and Huang, Gonzalez-Sanchez. Snippet only: Morris and Rouse 1985, Goldbeck 1957, Gugerty 2007, Rouse 1978 and 1987, the DX 2025 diagnostic concepts study.

Links to other subfields in this run (not covered here): Means-ends analysis; Consistency-based diagnosis and conflict generation (formal side of 4.2); Probing and measurement selection (the closest sibling to this document, overlaps strongly on 4.2 to 4.5); Verification design (T10); Adaptive stopping and metareasoning (4.6); Hypothesis limits in troubleshooting; LLM debugging; Anomaly handling and fixation (3.1 repeat detector, 2.9); Progress monitoring theory.

## 11. Sources

[V] = opened and read as full text (PDF or HTML) in this research run. [M] = snippet, abstract or bibliographic record only.

- [V] Rasmussen, Jensen (1974) Mental procedures in real-life tasks: a case study of electronic trouble shooting, Ergonomics. https://backend.orbit.dtu.dk/ws/files/105037994/TROUB.PDF (a01 to a07). Publisher record [M]: https://www.tandfonline.com/doi/abs/10.1080/00140137408931373 (b30)
- [V] Burroughs (1979) An investigation of mental coding mechanisms and heuristics used in electronic troubleshooting (thesis). https://shareok.org/bitstream/handle/11244/4635/8003800.PDF (a08 to a13)
- [V] Simon, Kadane (1975) Optimal problem-solving search: all-or-none solutions. https://ndownloader.figshare.com/files/12098960 (a14 to a16; OCR garbled)
- [V] Venkatasubramanian et al. (2003) A review of process fault detection and diagnosis, Part I. https://www.ece.lsu.edu/mcu/lawss/add_materials/FaultDetectionPart2.pdf (a17 to a19)
- [V] Feldman, Provan, van Gemund (2010) A model-based active testing approach to sequential diagnosis, JAIR. https://jair.org/index.php/jair/article/download/10671/25504 (a20 to a22, b22)
- [V] Gonzalez-Sanchez et al. (2011) Spectrum-based sequential diagnosis, AAAI. https://ojs.aaai.org/index.php/AAAI/article/download/7844/7703 (a23)
- [V] Hu et al. (2024) Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271 (a24, b19, c03, c04)
- [V] Choudhury et al. (2025/2026) BED-LLM. https://arxiv.org/abs/2508.21184 (a25, a26, b20, b21, c08)
- [M] Rouse (1987) Human problem solving in complex dynamic environments, Georgia Tech progress report. http://repository.gatech.edu/bitstreams/33ea8edd-3862-4725-8cf9-4b3474afb828/download (a27; progress report read only)
- [M] Morris, Rouse (1985) Review and evaluation of empirical research in troubleshooting. https://instructionaldesign.org/?p=306 (a28)
- [M] Goldbeck, Bernstein, Hillix, Marx (1957) Application of the half-split technique to problem-solving tasks. https://dc2.philarchive.org/rec/GOLAOT (b31; a29 not found)
- [V] Dounas-Frazer, Van De Bogart, Stetzer, Lewandowski (2016) Investigating the role of model-based reasoning while troubleshooting an electric circuit. https://arxiv.org/abs/1603.03684 (b01 to b03)
- [V] Dounas-Frazer, Stetzer, Lewandowski (2016) Electronics lab instructors' approaches to troubleshooting instruction. https://arxiv.org/abs/1610.01564 (b04)
- [V] Kim, Park, Yun, Lee (2026) Why do AI agents systematically fail at cloud root cause analysis? https://arxiv.org/abs/2602.09937 (b05 to b08, c11)
- [V] Wang, Yu et al. (2026) Cloud-OpsBench. https://arxiv.org/abs/2603.00468 (b09 to b12)
- [V] Chen, Shetty et al. (2025) AIOpsLab. https://arxiv.org/abs/2501.06706 (b13, b14)
- [V] Bertolazzi, Mazzaccara, Merlo, Bernardi (2023) ChatGPT's information seeking strategy. https://aclanthology.org/2023.inlg-main.11 (b15, b16)
- [V] Do reasoning models ask better questions? (2026) https://arxiv.org/abs/2601.17716 (b17, b18; text and Table 2 disagree on some figures)
- [V] Pattipati et al. (1997) Multiple fault isolation in redundant systems (NASA report). https://ntrs.nasa.gov/citations/19980096374 (b23)
- [M] Rouse (1978) Human problem solving performance in a fault diagnosis task. https://ntrs.nasa.gov/citations/19780048764 (b24; abstract page)
- [M] Morris, Rouse (1985) Effects of type of knowledge upon human problem solving in a process control task. https://ntrs.nasa.gov/citations/19860033033 (b25; abstract page)
- [V] Starr, Storey (2026) Theory of troubleshooting. https://arxiv.org/abs/2602.10540 (b26; first 100,000 of about 210,000 characters)
- [M] Schaafstal, Schraagen, van Berlo (2000) Cognitive task analysis and innovation of training: the case of structured troubleshooting. https://research.utwente.nl/en/publications/cognitive-task-analysis-and-innovation-of-training-the-case-of-st/ (b27, d15; abstract only)
- [M] Gugerty (2007) Cognitive components of troubleshooting strategies. https://dc2.philarchive.org/rec/GUGCCO (b28; blocked, d16)
- [V] Besnard, Bastien-Toniazzo (1999) Expert error in trouble-shooting. https://hal.archives-ouvertes.fr/hal-00691823 (b29, d05, d06)
- [V] Siddiqi, Huang (2011) Sequential diagnosis by abstraction. https://arxiv.org/abs/1401.3892 (c01, c02)
- [V] Grand et al. (2024) Loose LIPS sink ships. https://arxiv.org/abs/2402.19471 (c05, c06)
- [V] Grand et al. (2025) Shoot first, ask questions later? https://arxiv.org/abs/2510.20886 (c07, d13, d14)
- [V] Mazzaccara, Testoni, Bernardi (2024) Learning to ask informative questions. https://arxiv.org/abs/2406.17453 (c09)
- [V] Zhou et al. (2025) From passive to active reasoning (AR-Bench). https://arxiv.org/abs/2506.08295 (c10, d04; first 100,000 characters in the first pass, appendix tables in the gap pass)
- [V] OpenRCA 2.0 (2026). https://arxiv.org/abs/2606.27154 (c12; abstract and introduction only)
- [V] Tseng et al. (2026) FaulT-Bench. https://arxiv.org/abs/2608.27021 (c13, c14, d07, d08)
- [V] Chauhan, Pendyala (2026) Benchmarking LLM-guided control-plane policies for backend fault isolation (HAProxy). https://arxiv.org/abs/2608.10532 (c15, c16)
- [V] Wang, Hong (2025) Time Travel: LLM-assisted semantic behavior localization with git bisect. https://arxiv.org/abs/2511.18854 (c17, c18, d09)
- [V] Kim, Chen, Wang (2025) LLM4FL. https://arxiv.org/abs/2409.13642 (c19; Table 4 not extracted)
- [V] Microsoft AI, Nori et al. (2025) Sequential diagnosis with language models (SDBench, MAI-DxO). https://arxiv.org/abs/2506.22405 (c20, c21, d11, d12)
- [M] DX 2025 "Are diagnostic concepts within the reach of LLMs?" https://www.sri.com/?p=84982 (c22)
- [M] OpenRCA (Xu et al., ICLR 2025), ORCA-bench snippets. https://arxiv.org/abs/2501.06706 (c23)
- [M] SIGMA (2025) AI-empowered training stack on early-life hardware. https://arxiv.org/abs/2512.13488 (c24; PDF downloaded, results not read)
- [V] ACTMED (2025) Adaptive clinical test selection via model-based experimental design. https://arxiv.org/abs/2510.18988 (d01, d02)
- [V] Hartmann et al. (2026) Amortising Bayesian experimental design for sequential information gathering (ASIG). https://arxiv.org/abs/2607.03426 (d03; workshop paper)
- Own arithmetic from Time Travel (d10): not a source. Gap note c25: absence in a limited search only. Reproducibility note d17: extracted text files were deleted after reading because the disk filled; re-open sources to re-check any figure.
