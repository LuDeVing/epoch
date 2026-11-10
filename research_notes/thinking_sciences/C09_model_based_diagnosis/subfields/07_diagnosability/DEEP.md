# Diagnosability: deep document

*Subfield C09.07 of model-based diagnosis. Sources: evidence_a-d.jsonl (a01-a31, b01-b26, c01-c28, d01-d19), claims.jsonl (K01-K32), critique.md. Status marks: [E] established, [S] single-source, [C] contested. Honest limit: no paper tests diagnosability itself on an LLM (K32). Founding work is proofs, not experiments, so "replication" mostly does not apply. Most 2026 LLM numbers are single preprints.*

## 1. What it is

A system is diagnosable if every behaviour it can show gives one unambiguous diagnosis (a01). In plain terms: before you run any test, ask whether any test could ever separate the suspects.

Formal form (a03, a04): a system is diagnosable when every fault trace is followed, within a finite delay, by observations that only fault states can produce. The check runs on the model, off-line. It needs no data.

Two algorithm families exist (a01):
1. Decide whether a system is diagnosable.
2. Find a sensor (probe) set that makes it diagnosable, optionally at minimum cost.

Key idea for us: diagnosability is a property of the model plus the allowed probes, not of the reasoner. If two faults give identical observations on every allowed probe, no agent, however smart, can choose between them. The right output is "cannot tell, need another probe", not a guess.

Related terms:
- Detectability: a fault can be told from nominal.
- Isolability: fault f can be told from fault f'. Pairwise.
- Observability: the state can be inferred from outputs. Not the same as isolability (d15).
- I-diagnosability: detection only needed after an indicator event (a07).

Where it touches the agent: S0 (model of the task, design-time check), S7 (choose next test), the hypothesis set, and the rule on when to stop or ask for another probe.

## 2. History and theories in depth

**1995-1996, Sampath et al.** (a02 [M], a03-a08 [V]). Founding work on discrete-event systems (DES). The system is a finite automaton. Some events are observable, some not. Failures are unobservable events. They build a diagnoser: a finite state machine over observable events whose states carry labels (N normal, F failed, or uncertain sets of both). Diagnosability holds iff there is no cycle of "uncertain" diagnoser states that matches a real cycle in the system with the failure present. Checking is cycle detection (a04). Worked example: pump and valve HVAC with stuck-open and stuck-closed valves and pump failed-on and failed-off, two sensors (a05). Reported sizes: nitric acid cooling system 368 states and 1486 transitions as a component composition; 646 states and 1764 with a sensor model (a03). Diagnoser sizes 158, 97, 130, 245 states in small HVAC cases (a04).

Non-diagnosable example (a06): a controller failed-on with one flow sensor. Inside the loop the failure type never becomes certain. A stuck-open valve and a normally open valve look the same.

Design role (a08): the paper says diagnosability should be used at design time to decide which sensors to install. Indicator events (a07, K03): some failures only show after a command, so a system can look non-diagnosable because nobody triggered the test. They define I-diagnosability with a map from failure events to indicator events.

**2001, Jiang, Huang, Chandra, Kumar** (a09 [M]). Polynomial algorithm for testing diagnosability. It replaces the exponential diagnoser with a twin-plant style check (quadratic in states). Standard reference for the polynomial result.

**2007-2010, sensor placement and dynamic sensing.**
- Rintanen and Grastien (2007) (b13 [V]): SAT encodings of the twin plant. They find non-diagnosability witnesses in systems with 160-200 components where an explicit twin plant (6^(2C) states) cannot be built (K05).
- Cassez, Tripakis, Altisen (2007) (a13 [V]): minimum static sensor sets are NP-complete (clique and colouring reductions). Dynamic observers (sensors switched on and off) help. Cassez and Tripakis (2010) show diagnosability with a dynamic observer is in P (Theorem 1) (a12 [V]).
- Yassine, Ploix, Flaus (2008, 2010) (a15-a17 [V]): the structural, FDI-community view. Fault f is isolable from f' if some fault-MSO set contains f but not f'. Sensor placement by Dulmage-Mendelsohn decomposition with a per-variable cost. The FDI and DX communities developed the idea separately (K24).
- Su, Zanella, Grastien (2016) (b15): diagnosability with uncertain observations.

**2017, Ibrahim, Dague, Grastien, Ye, Simon** (a18, b14, b25 [V]). Diagnosability planning for controllable systems. Diagnosability can fail after a fault or repair. A plan of actions that restores it exists, but finding one is PSPACE-complete. Key shift: diagnosability is a property of the current belief state and probe set (K06).

**2019-2026, theory consolidation.** Zhang et al. survey (a20, b16). Zhang and Raisch (2024) Dp-automata (a19, b12). Miao, Jancar, Komenda, Masopust, Lai (2026) preprint (a10, a11, b11): strong diagnosability of a monolithic automaton is quadratic and optimal under standard conjectures. Weak diagnosability, modular and succinct systems are PSPACE-hard or worse (K04). Hardness for modular and succinct systems is cited from Yin and Lafortune (2017), Masopust and Yin (2019), Rintanen (2007) (b17, b20 [M]).

**Link to Reiter's theory** (see earlier C09 subfields): a diagnosis is a minimal hitting set of conflicts. Diagnosability asks whether the set of minimal diagnoses can ever shrink to one under the allowed probes. Interactive debugging (c22, c23) is the dynamic side: pick the probe that best splits the candidate diagnoses.

**2024-2026, LLM era.** Three lines:
1. LLMs doing the formal steps (conflicts, hitting sets, MSO sets) (a21-a24, c01-c04).
2. LLMs choosing tests by information gain (UoT, BED-LLM, ACTMED, MAI-DxO) (c05-c10, c17-c19, d08-d12).
3. Diagnosis benchmarks that expose "right answer, wrong reason" and unseparable faults (Cloud-OpsBench, PAVE, ORCA, Gogleva et al.) (c11-c16, d01-d07, d13-d14).

Cross-links to subfields researched in parallel (not covered here): Readings in model-based diagnosis; Complexity of expert troubleshooting; Epistemic value and curiosity; Calibration and overconfidence; Cognitive bias and premature closure; Logic programming and knowledge representation; Software, spreadsheet, KB debugging.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Diagnosability is decided on the model by a diagnoser (exponential) or twin plant (quadratic); a cycle of uncertain states is the witness | Nitric acid system 368 states/1486 transitions; diagnosers 158, 97, 130, 245 states | a03, a04, a09, a19 | [E] K01 |
| Non-diagnosability has one structural cause: two faults give the same observations forever | Stuck-open valve vs normally open valve, one flow sensor | a05, a06, b15 | [E] K02 |
| Indicator events: some faults show only after a command | I_f map from failure to indicator events | a07 | [S] K03 |
| Strong diagnosability quadratic; weak, modular, succinct hard; minimum sensor set NP-complete | Miao 2026; Cassez 2007; clique and colouring reductions | a10, a11, a13, b11-b13 | [E] K04 |
| SAT twin plant finds witnesses at scale | 160-200 components; explicit twin plant 6^(2C) states | b13 | [S] K05 |
| Dynamic observer check is polynomial; planning to restore diagnosability is PSPACE-complete | Theorem 1 (P) | a12, a18, b14 | [E] K06 |
| Probing by expected information gain beats free choice (UoT, GPT-4) | Closed set success 71.2/37.5/97.0/88.0/67.3 vs direct 50.5/30.5/91.3/72.3/43.7; average gain 38.1% | c05, c06 | [E] K07 |
| BED-LLM on 20 Questions | +37.4 points; GPT-4o Animals 45 (prompt-only) / 83 (split) / 93 (BED-LLM); in-context beliefs 25 | c08, c09, d11 | [E] K07 |
| Open-set gains are smaller | GPT-4 DX 49.1 vs 44.2; Common 55.3 vs 48.6 | c06, c20 | [E] K08 |
| Matched-cost claim is weak | UoT 9.2k tokens 54.4/92.5/66.0 vs Adapted-ToT 4.5k 33.8/85.1/60.3 (2x tokens, not matched); BED-LLM 61.1x slower per game than a trained policy | c07, d08 | [C] K09 |
| MAI-DxO | 304 cases; 80% vs 20% (physicians); o3 alone 78.6% at $7,850 vs MAI-DxO 79.9% at $2,397 | c17 | [E] gain over o3 is cost, not accuracy |
| ACTMED | LLM picks the same global tests for every patient; halves tests at equal accuracy | c18, c19 | [E] K10 |
| 2026 models rarely prefer separating probes | 24.1% vs 19.2% random, 6,596 experiments, 43 organisms, t=4.6; 33 of 43 above chance | d03 | [E] K10 (one lab) |
| Both-direction perturbation of true cause | 0.71 vs 0.04 (one direction) vs 0.00 (never) | d06 | [S] K27, correlation |
| Explicit hypothesis state beats prompt-only belief | GPT-4o Animals 25 vs 93; Qwen2.5-72B Animals: ICL beliefs 46, filtered set + LLM judge 61, split 87, entropy 85, BED-LLM 95; GoS ablation Match 18.12 (no causal graph), 12.32 (no state machine) | c09, d11, a25, b10 | [E] K11 |
| Four abduction failures in plain CoT/ToT/GoT | Fabrication 22.22%, drift 41.32%, early stop 63.89%; with GoS 0 / 9.70 / 18.75; backtracking failures 30.90% | a25, a26, b09 | [S] K12 |
| GoS distributed systems | Match 70.67, Relevant 88.00 vs best baseline 34.00 (the 39.86 medical GoS figure is unsafe, see critique) | a25 | [S] |
| Right answer, ungrounded | GPT-5 33.1% (OnlineBoutique), 29.4% (TrainTicket); PAVE 76.0% correct service but 61.5% grounded; exact root-cause set 20.7%; 7 LLMs fixed more than diagnosed, Opus 4.6 1.00 vs 0.55, GPT-5.1 0.40 vs 0.15 | c11, c14, d01, d13 | [E] K13 |
| Pool-minus-final gap | SIA 10.0, THK-int 11.9, ReAct 17.5, ToT 22.5 | a28, b24 | [E] K14 |
| Structural non-diagnosability is rare in one domain | 7 of 60 organisms; diagnosis 0.31 / 0.30 / 0.12 for unambiguous / resolvable / structural | d02 | [S] K26 |
| SIA: separate the top two | Final 79.2 [72.7, 83.7] vs ReAct 69.0, ToT 61.5, THK-int 72.8, Ask-5 72.3, BAS 67.3 (100 cases); other backbones 75.4 vs 69.2, 76.1 vs 68.4; ablations -6.4 (structured investigation), -5.2 (counterfactual critique); 9.0 hypotheses and 5.2 questions vs ToT 21.0 hypotheses | a27, a29, a31, b06-b08 | [S] K15 |
| Plausible wrong user hint | SIA 80.0 to 76.0; selected in 2 of 10 pairs | a30 | [S] K16 (10 pairs) |
| LLMs collapse to a single fault | Double fault named by 1 of 13 models; hit rates 79.5/76.9/38.5%; hallucination 20.5/15.4/7.7/94.9% | a21, a23, b01, b02 | [S] K17 |
| Structural steps degrade with size | o3-mini conflicts F1 0.917, diagnoses F1 0.784; incidence matrix o1/o3-mini F1 1.00, 4o-mini 0.47 | c01-c03 | [E] K18 |
| Memorised textbook circuits inflate scores | Phi-2 1.05 powertrain vs 0.08-0.67 elsewhere | a24, b03, c04 | [E] K19 |
| Telemetry limit | GPT-5 JRA 0.00 on hard TrainTicket performance faults (0.88/0.89 on easier tiers) | c12, d13 | [E] K20 |
| LLMs seldom call a result uninformative | 0.30-0.53 accuracy on 43 items; predictions given 0.88-1.00, derived 0.51-0.74 | d04, d05 | [S] K28 |
| Confirmation bias | 11 LLMs: counterexample prompting lifts rule discovery 42% to 56% | c24 | [S] K21 |
| QuestBench | Logic-Q and Planning-Q all models under 50%; GSM-Q strong models above 80% | c20, c21 | [S] K22 |
| Entropy query selection in classic debugging | More than 50% fewer queries; 33,000-axiom ontology in about 5 queries (190 s); DynamicHS beats HS-Tree in 96% of sessions, median saving 52%; floor log2(n) | c22, c23 | [E] K23 |
| Code beats LLM at separability verdicts | Graph-search verifier 100% precision across three LLMs; LLM only labels roles | d15, d16 | [S] K29 (observability, not isolability) |
| Information-gain gain fades for strong or reasoning models | Reasoning lowered solve rate in Gemma-4-E4B; Qwen 7B Animals 7.6 to 21.0 vs 14B 35.0 to 39.2 (BED-LLM 26.4) | d08, d10, d12 | [C] K30 |
| No abstain option in benchmarks | 22% of audited weak-process cases ended with ambiguous observations; 95% from incomplete investigation; 73% stopped at a symptom log | d13, d14 | [S] K31 |

## 4. Mechanisms and models

**4.1 Fault models and observation maps.** Write each hypothesis h as a function from probes to predicted outcomes: pred(h, p). The system is a table. This is the S0/S2 object.

**4.2 Pairwise separability (isolability), one-step version.** For hypotheses H and probe set P:
```
for each pair (h1,h2):
    separable = any(|pred(h1,p) - pred(h2,p)| > noise for p in P)
unseparable_pairs = pairs where not separable
```
This is the one-step analogue of structural isolability (K24). With noise, use a threshold (Gogleva used 0.10 on a phenotype; d02).

**4.3 Sequential version (real diagnosability).** Probes change state. Build a twin plant: the product of the system with itself, synchronised on observable events. Two runs with the same observations but different fault labels, if they can continue forever (a cycle), witness non-diagnosability. In code: build the product automaton, search for a reachable cycle that contains a state pair with different labels. Quadratic in states (a09, b11). For large or modular systems use a SAT encoding (b13), not explicit enumeration (6^(2C) states).

**4.4 Diagnoser (older form).** Subset construction over observable events. Each state carries a set of (component, status) pairs. Diagnosable iff there is no cycle of uncertain states with F and N both reachable as a real cycle. Exponential worst case; used for online monitoring (a03).

**4.5 Structural isolability (FDI).** Build the equations-by-variables incidence matrix. Find MSO sets (minimal structurally overdetermined subsets). f is isolable from f' if some fault-MSO contains f and not f'. Sensor placement adds measured variables at a cost; Dulmage-Mendelsohn decomposition finds the overdetermined part (a15, a16). LLMs do the incidence matrix well with a reasoning model (F1 1.00) but not MSO enumeration at scale (c01, c02).

**4.6 Hitting-set diagnosis and probe choice.** Conflicts are sets that cannot all be normal. Minimal diagnoses are minimal hitting sets. With candidate diagnoses D, pick probe p to minimise expected remaining entropy: score(p) = sum over outcomes o of P(o) * H(D | o). With equal priors the best probe halves D. Lower bound: log2(n) probes (c22). DynamicHS reuses the hitting-set tree across a session (c23).

**4.7 Scaffolded information-gain loop (works on LLMs).**
1. LLM proposes candidates (closed set given, or generated; open set is harder, K08).
2. LLM proposes several candidate probes.
3. For each probe, the LLM (or a sampler) predicts the outcome under each live hypothesis. Weak step: deriving predictions (0.51-0.74 vs 0.88-1.00 when given; d05).
4. Code computes expected information gain (or the split balance) and picks the probe (G5: code selects).
5. Observe; filter hypotheses by consistency; repeat.

BED-LLM ablation (d11): keeping the filtered set but letting the LLM judge the best question gave 61; an even-split score gave 87; full EIG 95 (Qwen2.5-72B, Animals). Step 4 carries most of the gain.

**4.8 Top-two separator (SIA).** Keep a ledger of hypotheses. Ask a counterfactual question that makes the leading two hypotheses predict different answers. Fewer hypotheses (9.0) than ToT (21.0), better final choice (79.2 vs 61.5) (a27, a28).

**4.9 Diagnosability planning.** If after an observation some pair becomes inseparable, check whether an action exists that restores separability (PSPACE in general, a18). Heuristic: prefer a probe that does not shrink the separable pair set.

## 5. What holds up

**Holds (theory).** Diagnoser, twin plant and complexity results are proofs, stable since 1995-2001 (K01, K04). Not empirical, so no replication notion. The weak-diagnosability hardness result is one preprint (Miao 2026).

**Holds (LLM, several independent papers).**
- Free-form LLM test choice is poor; scaffolded information-gain choice helps. UoT, BED-LLM, ACTMED, MAI-DxO and Gogleva agree in direction (K07, K10). The 2026 probe audit (24.1% vs 19.2%) came from a different group than the 2024-25 papers.
- An explicit hypothesis set beats belief held in the prompt (K11): BED-LLM and GoS both show it, on different tasks.
- Right answer does not equal grounded diagnosis (K13): five sources.
- Memorisation inflates textbook circuits (K19).

**Weak or failed.**
- UoT matched-cost claim: 2x tokens, not matched (K09, critique).
- MAI-DxO headline: 80% vs 20% is against physicians. Against plain o3 the accuracy gain is about 1 point; the real gain is cost (c17).
- GoS medical 39.86 figure: layout issue in the table; do not quote.
- Information-gain gains fade as models get bigger (7B to 14B) and reasoning alone hurt a small model (K30, [C]). BED-LLM had no reasoning questioner (d12).
- SIA's misleading-hint stress test used 10 pairs; no significance (K16).
- No independent replication of SIA (critique gap 3 still open).
- LLM double-fault finding rests on one scenario (K17).

**Moderators.**
- Closed vs open candidate set (K08).
- Predictions given vs derived (d05).
- Size of the combinatorics: F1 falls as hypotheses rise (K18).
- Source access: removing source code hurt all models on Cloud-OpsBench and raised implausible causes (K20).

**Interventions that worked.** EIG or even-split probe selection by code; explicit hypothesis ledger; counterfactual separating question (single-source); counterexample prompting (42% to 56%, c24, single-source); probing the true cause in both directions (0.71 vs 0.04, correlation only); giving predictions rather than deriving them.

**Interventions that did not.** More hypotheses without selection (ToT); free-form reasoning alone (d08); plain chain, tree and graph prompting for abduction (K12); LLM-only separability verdicts (d04, d15).

**Non-diagnosability is not the main loss (one domain).** Only 7 of 60 cases were structurally non-diagnosable; diagnosis there 0.12 vs 0.30 on resolvable cases (d02). Most error is selection and evidence use (K14, K26).

## 6. Language models

What LLMs do on these tasks:
1. **Structure steps.** Reasoning models extract incidence matrices perfectly on small circuits (o1, o3-mini F1 1.00; 4o-mini 0.47) (c02). Conflicts F1 0.917 and diagnoses 0.784 for o3-mini (c03). Code is needed beyond small size.
2. **Enumeration.** They collapse to the most probable single fault. Double fault found by 1 of 13 models (a23). Hit rates 79.5/76.9/38.5%, hallucination up to 94.9% (a21).
3. **Test choice.** Without a scaffold: the same tests for every case (c19), redundant questions, weak preference for separating probes (24.1% vs 19.2%; d03). With a scaffold: UoT +38.1% average, BED-LLM +37.4 points, ACTMED half the tests.
4. **Calling a result uninformative.** When two predictions are within noise, models pick the closer prediction (0.30-0.53; d04). They are poor at deciding "cannot tell".
5. **Grounding.** Right root cause without evidence in about 30% of GPT-5 cases (c11). Across 7 LLMs fixing beat diagnosing (d01). Diagnosis varied about 7x across models; outcome prediction 1.4x (K25).
6. **Confirmation bias.** Confirming tests proposed; counterexample prompts lift rule discovery 42% to 56% (c24).
7. **Underspecified problems.** QuestBench: asking the one right question is below 50% on logic and planning (c20).

What changed it, by how much: code-side EIG selection (+20 to +50 points depending on task and model); explicit ledger (25 to 93 on GPT-4o Animals, d11); counterfactual separating question (+6 to +12 over baselines, -5.2 when removed); state machine plus graph (fabrication 22.22% to 0; a26); code-based verifier (precision 100%; d15).

Transfer caveats: UoT and BED-LLM used non-reasoning or small models. 2026 frontier reasoning models are not tested as questioners, and gains may fade with scale (K30). Cost: BED-LLM was 61.1x slower than a trained policy, and 25x to 36x in another paper (d08, d10).

No study asks an LLM to decide diagnosability from a model (K32).

## 7. What our agent should take

### Add now (established)

1. **Hypothesis ledger with per-hypothesis predictions.** Live hypotheses, what each predicts for candidate probes, support and refute marks. Part: S (ledger) and memory. [E]. Evidence: c09, d11, a25, b10, d05 (K11).
2. **Code-scored probe selection.** The model proposes probes and predicts outcomes; code picks the probe with the most even split or highest EIG. Part: O and S7, G5. [E] for non-reasoning and small models; reasoning models untested. Evidence: c05, c06, c08, c10, c18, c22, c23, d11 (K07, K23).
3. **Do not trust free-form test choice.** Log the redundant-probe rate (probes with zero split on the live set). Part: G. [E]. Evidence: c19, d03, c10 (K10).
4. **Score answer and evidence path separately.** A right answer without a verified evidence path is not a pass. Part: G2, G10, S8. [E]. Evidence: c11, c12, c14, d01, d13 (K13).
5. **Compute enumeration and separability by code beyond small sizes.** Hitting sets, isolability tables. Part: G5, tools. [E]. Evidence: a21, c01-c03, d15 (K18, K29).
6. **Report potential (oracle over pool) and final separately.** Part: bench design, G7. [E]. Evidence: a28, b24, d02 (K14).
7. **Use novel generated systems and private held-out sets.** Part: bench design. [E]. Evidence: a24, b03, b26, c04 (K19).
8. **Open set needs hypothesis generation first; expect smaller gains.** Part: S3. [E]. Evidence: c06, c20 (K08).

### Test first

1. **Separability check at S0.** A script says which hypothesis pairs no allowed probe separates; the agent may answer "need probe X" instead of guessing. [S]. d02, d04, d15 (K26, K29, K32). Note G6 (never abstain on the first pass): the proposal is to ask for a probe, not to refuse.
2. **Top-two separator operator (SIA).** [S]. a27, a29, a31 (K15). One group, one benchmark.
3. **Falsifying probe step** ("name a probe that would break the leader"). [S]. c24 (K21).
4. **Probe the suspected cause in both directions.** [S]. d06 (K27), correlational.
5. **Re-check separability after every observation** (diagnosability is a belief-state property). [E] in theory, untested on LLMs. a12, a18 (K06).
6. **Minimal candidate set (hitting set) by code before ranking**, to catch multi-fault cases. [S]. a21, a23 (K17).
7. **Indicator-event probe:** act to expose a fault that shows only after a command. [S]. a07 (K03).
8. **Information-gain gain with a frontier reasoning questioner at equal tokens.** [C]. d08, d10, d12 (K30).
9. **Abstain-with-cost option on provably non-diagnosable items.** [S]. d13, d14 (K31).
10. **Ablate ledger vs split step.** [S]. d11 (K11).

## 8. Concrete tests on our bench

All arms get the same token budget. Include a best-of-N or longer-CoT plain arm at the same tokens (G7).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 60 generated small systems (hidden fault among 6-12 candidates) with a computed isolability table, about 15% non-separable pairs | plain; plain + best-of-N; ledger + code-split probe | Accuracy after k probes; probes used vs log2(n); redundant-probe rate | Scaffold +10 to +25 points over plain; redundant-probe rate under 20% (K07, K10) |
| T2 | Same items | scaffold without separability check; scaffold with script check and "need probe X" verdict | Accuracy on separable pairs; correct "need probe" rate; wrong-confident rate on non-separable pairs | Fewer confident wrong answers on non-separable pairs; no loss on separable (K26, K29) |
| T3 | Items where the true cause is in the top two | free probing vs SIA top-two separator | Final accuracy; potential minus final gap | Gap drops by 5-10 points (K14, K15) |
| T4 | Multi-fault circuits (1-3 faults, 5-150 minimal diagnoses) | LLM enumerates; code hitting set then LLM ranks | Recall of minimal diagnoses; hallucinated diagnoses | Code arm recall near 1.0; LLM recall falls as diagnoses rise (K17, K18) |
| T5 | Items with a plausible wrong hint | scaffold with and without ledger | Hint-adoption rate over at least 100 pairs | Lower adoption with the ledger (K16) |
| T6 | Faults that show only after a command | observe-only vs allowed to act | Detection rate | Act arm better (K03) |
| T7 | Open-set vs closed-set versions | same scaffold | Gain over plain | Gain smaller open-set (K08) |
| T8 | T1 with a frontier reasoning model | plain reasoning vs reasoning + code-split | Accuracy at equal tokens | Unknown; K30 says the gain may fade. Add only if at least +5 points |
| T9 | Predictions given vs must be derived | LLM-derived vs code-simulated predictions | Accuracy | Given 0.88-1.00 vs derived 0.51-0.74 (d05); test whether a code simulator closes the gap |
| T10 | Answer plus evidence path | grounded score vs answer-only | Share of correct answers lacking a verified path | About 30% in plain arm (K13); scaffold should cut it |

## 9. What does not transfer, and why

- **Discrete-event automata theory.** Our tasks are puzzles without a ready state machine. Exact diagnosers, twin plants and complexity results apply only if we write the model ourselves. Use the idea (pairwise separability on the probe set), not the algorithm (K04).
- **Sensor placement design (NP-complete, Dulmage-Mendelsohn).** The agent does not choose hardware sensors. The nearest analogue is choosing which probes to run; cheap heuristics are enough (K04, K24).
- **Infinite traces and finite delay.** Our agent has a token budget. "Eventually" becomes "within the budget".
- **Medical and cloud RCA numbers.** MAI-DxO and Cloud-OpsBench report cost and process, not isolability. MAI-DxO's gain is cost (c17).
- **20 Questions with a simulated answerer.** Closed set, noise-free, cooperative answerer. BED-LLM numbers will not carry to open-ended work (K08).
- **Hard abstaining.** G6 says never abstain on the first pass. The use here is "ask a probe", not "refuse".
- **Memorised textbook circuits.** Do not use them (K19).
- **Weak diagnosability results.** PSPACE-hard and not needed by us.

## 10. Open questions

1. Can an LLM decide whether two faults are inseparable from a small model (K32)? Nothing found.
2. Does SIA replicate by a different group at equal tokens vs best-of-N (K15)?
3. How much of the potential-final gap is true non-diagnosability vs selection error outside the one gene-network domain (K14, K26)?
4. Does information-gain probing help frontier reasoning models (K30)?
5. Does abstaining when provably non-diagnosable raise calibrated accuracy (K31)?
6. Does a cost-weighted probe order beat cheapest-first at equal budget? No source found.
7. Is the ledger or the information-gain step the source of the gain on our tasks? d11 says the split step; no ledger-only arm without scoring exists.
8. Multi-fault enumeration: LLM vs code beyond 150 diagnoses (K17, K18).
9. Does the 24.1% vs 19.2% separating-probe rate hold in other domains?

## 11. Sources

[V] = opened and read this session. [M] = snippet or citation only.

- Wikipedia, Diagnosis (artificial intelligence) [V] https://en.wikipedia.org/wiki/Diagnosis_(artificial_intelligence) (a01)
- Sampath et al. (1995) Diagnosability of Discrete-Event Systems, IEEE TAC 40(9) [M] https://dblp.org/rec/journals/tac/SampathSLST95 ; https://doi.org/10.1109/9.412626 (a02, b18)
- Sampath et al. (1996) Failure Diagnosis Using Discrete-Event Models [V] https://teneketzis.engin.umich.edu/wp-content/uploads/sites/370/2018/01/ (a03-a08)
- Jiang, Huang, Chandra, Kumar (2001) A polynomial algorithm for testing diagnosability [M] https://researchr.org/publication/JiangHCK01/bibtex ; https://doi.org/10.1109/9.940942 (a09, b19)
- Miao, Jancar, Komenda, Masopust, Lai (2026) Diagnosability verification for automata [V] https://apollo.inf.upol.cz/~masopust/pubs/Preprint/wd-draft.pdf (a10, a11, b11)
- Cassez and Tripakis (2010) Fault diagnosis with dynamic observers [V] https://arxiv.org/pdf/1004.2810 (a12)
- Cassez, Tripakis, Altisen (2007) Sensor minimization problems [V] https://franck44.github.io/publications/papers/acsd07.pdf (a13)
- Cassez and Tripakis (2008) Fundamenta Informaticae 88(4) [M] https://content.iospress.com/articles/fundamenta-informaticae/fi88-4-05 (a14)
- Yassine, Ploix, Flaus (2008) Structural approach for sensor placement [V] https://skoge.folk.ntnu.no/prost/proceedings/ifac2008/data/papers/0070.pdf (a15)
- Yassine, Ploix, Flaus (2010) Optimal sensor placement algorithm [V] https://orbilu.uni.lu/bitstream/10993/4482/1/05520799.pdf (a16, a17)
- Ibrahim, Dague, Grastien, Ye, Simon (2017) Diagnosability planning for controllable DES [V] https://ojs.aaai.org/index.php/AAAI/article/view/10694/10553 (a18, b14, b25)
- Zhang and Raisch (2024) Diagnosability of labeled Dp-automata [V] https://arxiv.org/pdf/2109.07125 (a19, b12)
- Zhang et al. (2019) Estimation and verification of partially-observed DES [V] https://arxiv.org/pdf/1903.11413 (a20, b16)
- Rintanen and Grastien (2007) Diagnosability testing with satisfiability algorithms [V] https://ijcai.org/proceedings/2007/84 (b13); Rintanen (2007), Yin and Lafortune (2017), Masopust and Yin (2019), Cao et al. (2021) cited inside it [M] (b17, b20, b21)
- Su, Zanella, Grastien (2016) Diagnosability of DES with uncertain observations, IJCAI 2016 [V] (b15)
- Plank and Wotawa (2026) Using SLMs and LLMs for diagnosis, DX 2026 [V] https://doi.org/10.4230/OASIcs.DX.2026.14 (a21-a24, b01-b04, b22, b23)
- Sztyber-Betley et al. (2025) Are diagnostic concepts within the reach of LLMs? DX 2025 [V] https://drops.dagstuhl.de/entities/document/10.4230/OASIcs.DX.2025.2 (b05, b26, c01-c04)
- Luo et al. (2026) Graph of States [V] https://arxiv.org/pdf/2603.21250 (a25, a26, b09, b10)
- Marozzo and Lio (2026) LLM-as-an-Investigator [V] https://arxiv.org/pdf/2606.13220 (a27-a31, b06-b08, b24)
- Hu et al. (2024) Uncertainty of Thoughts [V] https://arxiv.org/html/2402.03271v2 (c05-c07)
- Choudhury and Williamson (2025) BED-LLM [V] https://arxiv.org/abs/2508.21184 (c08, c09, d11, d12)
- Shoot first, ask questions later? [V] https://arxiv.org/html/2510.20886v1 (c10)
- Cloud-OpsBench (2026) [V] https://arxiv.org/abs/2603.00468 (c11-c13, d13, d14)
- OpenRCA 2.0 PAVE (2026) [V] https://arxiv.org/abs/2606.27154 (c14)
- ORCA-bench (2026) [V] https://arxiv.org/abs/2607.28545 (c15)
- How far can RCA go on real-world telemetry (2026) [V] https://arxiv.org/abs/2607.13548 (c16)
- Microsoft AI (2025) MAI-DxO, Sequential diagnosis with language models [V] https://arxiv.org/abs/2506.22405 (c17)
- Estevez, Astorga, van der Schaar (2025) ACTMED [V] https://arxiv.org/pdf/2510.18988 (c18, c19)
- Google DeepMind (2025) QuestBench [V] https://arxiv.org/pdf/2503.22674 (c20, c21)
- Shchekotykhin et al. interactive ontology debugging [V] https://arxiv.org/pdf/1107.4303 (c22)
- Rodler (2020) DynamicHS [V] https://arxiv.org/pdf/2012.11078 (c23)
- Failing to falsify (2026) [V] https://arxiv.org/abs/2604.02485 (c24)
- Separable pathways for causal reasoning (2026) [V] https://arxiv.org/abs/2604.20039 (c25)
- LLM-based RCA of hardware design failures (2025) [V, abstract level] https://arxiv.org/abs/2507.06512 (c26)
- Search summary, blicket-task biases and sequential BED [M] (c27); GALA multi-agent RCA [M] https://arxiv.org/pdf/2508.12472v1 (c28)
- Gogleva et al. (2026) Treating the symptom, missing the cause [V] https://arxiv.org/abs/2611.04473 (d01-d06); LUCA synthetic world [V] https://arxiv.org/abs/2611.03100 (d07; same authors, not independent)
- Kriz et al. (2026) Amortizing sequential experimental design [V] https://arxiv.org/abs/2610.20832 (d08, d09)
- Hartmann et al. (2026) Amortising Bayesian experimental design [V] https://arxiv.org/abs/2607.03426 (d10)
- Jaradat et al. (2026) NetFlow-DSR [V] https://arxiv.org/abs/2611.07040 (d15, d16)
- DistDebug-Bench (2026) [V, abstract only] https://arxiv.org/abs/2611.03523 (d17)
- Sequential Bayesian optimisation with five frontier LLMs (2026) [V, abstract only] https://arxiv.org/abs/2609.33061 (d18)
- Adaptive group elicitation via multi-turn LLM interactions (2026) [V, abstract only] https://arxiv.org/abs/2602.14279 (d19)
