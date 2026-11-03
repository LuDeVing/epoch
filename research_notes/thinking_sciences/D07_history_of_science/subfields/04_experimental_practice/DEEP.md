# Experimental practice: deep document

*Subfield D07.04, history of science. Key works: Gooding, Hacking, Galison. Maps to schema state S4 (TEST). Built from evidence_a-d.jsonl (ids a01-a25, b01-b23, c01-c26, d01-d19), claims.jsonl (K01-K29) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested.*

*Honesty note up front. The historical core (Hacking, Galison, Collins, Pickering, Franklin, Meselson-Stahl, Kettlewell) was read only through the Stanford Encyclopedia of Philosophy (SEP) article "Experiment in Physics". No original book text was opened. Gooding (a10) and Steinle (a09) were not opened. The LLM and replication evidence was opened as papers (full text or abstract; see section 11).*

## 1. What it is

Experimental practice is the study of how experiments are built, made to work, and made believable. It asks what an experimenter does that is not theory and not data analysis: designing the apparatus, tuning it, checking that it works, deciding what counts as a real signal, and deciding when to stop.

Three questions carry over to an agent that must design and run its own tests (schema state S4):

1. **How do you know the test works?** Calibration, known answers, independent methods (Hacking, Franklin).
2. **How do you know when you are done?** The result survives attempts to make it go away (Galison). Stopping rules and thresholds.
3. **How do you avoid tuning until you like the answer?** The experimenter's regress (Collins, Pickering) against epistemological strategies (Franklin).

The subfield also covers modern evidence on whether experiments, by humans or by AI agents, actually replicate and actually run. That evidence is large for humans (psychology, cancer biology) and growing for LLM agents (PaperBench, EXP-Bench, BED-LLM, POPPER).

Links only (parallel subfields, not covered here): Falsificationism; Hypothetico-deductive model; Theory comparison; Active inference decision theory; Shannon information, entropy (for expected information gain); Problem selection; Red teaming as alternative analysis; Surprisingly popular method; Good Judgment Project; Sociology of science and Merton's norms.

## 2. History and theories in depth

Historical claims in this section rest on the SEP summary (a01-a11, b09-b11), not on the books.

### 2.1 Hacking: experiment has a life of its own (1983)
- Experiment is not just a servant of theory. Observation can precede any formulation of theory (Hacking 1983 p.156, in a01).
- Intervention: staining a cell or injecting fluid, then seeing the predicted change, raises belief in both the apparatus and the observation.
- The microscope argument: the same dot pattern appears in ordinary, polarizing, phase-contrast, fluorescence, interference, electron and acoustic microscopes. Seven methods with different physics agreeing is a "preposterous coincidence" if the pattern is an artifact.
- Later (1992): stable laboratory science is self-vindicating; theory, apparatus and data are adjusted until they fit (b11).
- For an agent: agreement must come from methods with independent failure modes. Many samples from one model do not qualify (schema G4).

### 2.2 Galison: how experiments end (1987) and two traditions (1997)
- Experiments end when the experimenters judge the result will stand up in court, not at a fixed rule (a02).
- Case: Gargamelle weak neutral currents. Different group members found different evidence decisive: one neutrino-electron photograph, or the spatial distribution of candidates against neutron background.
- Cline: "I don't see how to make these effects go away" (Galison p.235). The effect was believed because it resisted every attempt to remove it.
- Design lesson: the original design had a muon trigger that would have blocked seeing neutral currents. The test itself can hide the effect.
- Einstein and de Haas stopped hunting systematic errors once g = 1 matched their model. Later measurements disagreed. This is stopping when the answer looks right.
- 1997: two traditions. Image (cloud and bubble chambers, the single golden event) and logic (counters, statistics over many events). Sub-communities hold different standards of proof (a03).
- [C] Staley (1999) argues both traditions share a statistical argument form (b11).

### 2.3 Franklin: the epistemology of experiment (1986, 1990, 2013)
Strategies physicists use to argue an observation is real (a04, b09). None is exclusive. None guarantees truth.
1. Experimental checks and calibration (the Balmer series in hydrogen as a calibration).
2. Reproducing known artifacts and known results.
3. Eliminating plausible alternatives and error sources ("Sherlock Holmes").
4. Using the results themselves (too consistent to be an artifact).
5. Explanation by a corroborated theory of the phenomenon.
6. Apparatus built on corroborated theory.
7. Statistical arguments.

Threshold practice (a04): a 3-sigma bump has probability 0.27% per bin. Physicists raised the criterion to 4-sigma (0.0064%) because with many plots, 3-sigma flukes become likely. For the Higgs, 5-sigma was preferred. A bin's chance is about 100 times lower than the chance anywhere in 80 bins. W boson example: measured 81 +/- 5 and 80 (+10/-6) GeV/c2 against a predicted 82 +/- 2.4.

### 2.4 Collins and the experimenter's regress (1985); Pickering (1984, 1987)
- Regress: a good apparatus is one that gives the right answer, but the right answer is what the experiment is meant to find. No formal rule breaks the circle. The community negotiates (a05).
- Case: Weber's gravity-wave detection. Six other experiments reported nulls. Critics shared data and programs, reanalysed with Weber's nonlinear algorithm, and injected acoustic calibration pulses of known energy. Weber's apparatus could not detect the pulses. An admitted programming error produced spurious coincidences. Coincidences were reported between detectors recorded four hours apart.
- Franklin's reply: reasoned argument and concrete checks decided the case, so the regress is not vicious. Collins disputes that the null experiments count as replications.
- Pickering: a successful experiment is mutual support among apparatus, data and theory (a06). Morpurgo first saw continuous charges, then separated capacitor plates, got only integral charges and reported no fractional charge. Fairbank's group reported fractional charges. Pickering reads the choice as shaped by commitments; Franklin says evidence should decide. Pickering also says neutral currents were accepted because physicists could "ply their trade more profitably".
- [C] The sociological (Collins), epistemological (Franklin) and mutual-support (Pickering) readings are unresolved.
- Risk for an agent: tuning the apparatus until the answer looks right is exactly this pattern.

### 2.5 Gooding: procedures and construals (1990)
Unopened (a10). From background knowledge, unverified here: experiment is built by moving between procedures (what is done with the apparatus) and construals (the verbal and visual picture of what is happening), adjusted together until a stable, communicable result appears. Faraday is the model case. The point for an agent is that the test and the description of what it measures are revised together. This is a hypothesis about the book, not a checked fact.

### 2.6 Steinle, Karaca, Perovic: exploratory experimentation
- Exploratory experiments are not driven by a specific theory. They vary parameters systematically to find regularities and form concepts when no framework exists. Cases: Ampere and Faraday (a09, snippet only).
- Karaca and Perovic: some exploratory work is weakly theory-laden. Theory shapes the design but does not fix the outcome. J/psi detection and deep inelastic scattering (a11).

### 2.7 Worked designs from biology
- Meselson and Stahl (1958): E. coli grown 14 generations in 15N, switched to 14N. Generation 1: all DNA intermediate. Generation 4: almost all light. The intermediate band sat at 50 +/- 2 percent of the distance between the 14N and 15N bands. One run separated rival mechanisms (conservative, semi-conservative, dispersive); the controls worked in advance (a07).
- Kettlewell moth experiments: mark-release-recapture. Recapture 27.5% for carbonaria vs 12.7% for typical. Controlled for trap attraction, migration and longevity. Same recapture rates for both trap types. Blind analysis was not used (a08). Later criticism of the design was not read.
- Lesson: a crucial design is one where each rival predicts a different, stated outcome and the controls are checked before the main run.

### 2.8 Links backward and forward
- Backward: Hacking and Franklin react against the logical-empiricist and Popperian tradition (see Falsificationism, parallel).
- Forward to AI: Box's iterative model building (BoxingGym "Box's Apprentice"), Bayesian experimental design (BED-LLM), sequential falsification (POPPER), and automated science from King et al. (2009, Robot Scientist Adam; not opened, c21).

## 3. Core findings with exact numbers

"Human" rows are about people or labs and transfer to an agent only by analogy.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Agreement of independent methods makes an artifact unlikely | Same dot pattern in 7 microscope types | Hacking via SEP (a01, b11) | E (historical, secondary) |
| Calibration with a known signal exposed a failed apparatus | Weber's detector missed injected pulses of known energy; 6 other experiments null | Collins/Franklin via SEP (a05, b10) | E (historical) |
| Experimenter's regress | No counts, qualitative | Collins, Pickering, Franklin (a05, a06) | C |
| Threshold rises with number of looks | 3-sigma = 0.27% per bin; 4-sigma = 0.0064%; Higgs 5-sigma; chance anywhere in 80 bins about 100x chance in one bin | Franklin via SEP (a04) | S |
| Psychology replication | 35 of 97 (36%) significant; mean original effect .403 (SD .188), replication about half; 47% of originals inside replication 95% CI; 68% significant pooled; mean replication power .92 | OSC 2015 (b01, b02) | S as a study, E as a pattern (K06) |
| By journal | JPSP 7/31 (23%); JEP:LMC 13/27 (48%); Psych Science 7/24 (29%) | OSC 2015 (b02) | S |
| Nature/Science social science | 13 of 21 (62%); mean relative effect 50% (74.5% for replicated, 0.3% for the 8 that failed); about 5x original sample | Camerer 2018 (b03) | S |
| Peers predicted replication | Market 60.6% vs observed 62% | Camerer 2018 (b04) | S |
| Many Labs 2 | 15 of 28 (54%) at p<.05; 14 (50%) at p<.0001; median d 0.60 to 0.15; 21 of 28 smaller, 7 larger; 125 samples, 36 countries, N 15,305 | Klein 2018 (b05) | E as pattern |
| Hidden moderators matter little | Heterogeneity in 11 of 28 (39%); only 1 effect with tau above .20 | Klein 2018 (b06) | S |
| Cancer biology: effects shrink | 158 effects (136 positive, 22 null); median ES 2.96 to 0.43 (85% smaller); 92% smaller | Errington 2021 (b08) | E as pattern |
| Verdict depends on rule | Same direction and p<.05: 43% (42/97); original ES inside replication CI: 18% (17); replication ES inside original CI: 43%; meta-analysis p<.05: 62% (60); 3+ of 5 methods: 40% (39/97) positive, 80% (12/15) null, 46% (51/112) combined | Errington 2021 (b08; critique item 7) | E (K07) |
| Methods text insufficient | 193 experiments, 53 papers; 0 needed no clarification; 20% needed strong or extreme help; raw data public for 4 (2%), obtained for 31 (16%), none for 131 (68%); stats reported for 78 (40%); mean $52,574 per replication | Errington 2021 (b07) | E (K09) |
| Reproducing with shared code is hard for humans too | ML reproducibility challenge 2022: 18 of 28 fully reproducible; 6 of 28 not even after contacting authors | CORE-Bench table (b17) | S |
| Whole-experiment agent success near zero | EXP-Bench: 461 tasks, 51 papers; complete executable 0.5%; best All 1.4% (OpenHands + o3-mini); Claude 3.7 All 0.7 | Kon 2025 (a14, d10) | E (K10) |
| EXP-Bench strictness ladder | 20.6% (monitor) to 3.7% (+design+conclusion) to 0.4% (+implementation) to 0.2% (+execution) | Kon 2025 (a14) | S |
| EXP-Bench failure shares | Implementation: 39.71% missing components. Execution: 29.38% environment misconfiguration, 23.84% script errors. Design: 16.05% incomplete variables, 7.62% extraneous. Conclusion: 26.18% missing, 19.66% wrong | Kon 2025 (a15, d10) | E for the pattern (K11) |
| PaperBench | 20 ICML 2024 papers; 8,316 gradable items; Claude 3.5 Sonnet 21.0%, o1 13.2%, R1 6.0, 4o 4.1, Gemini Flash 3.2, o3-mini 2.6; Code-Dev o1 43.4%; 36-h o1 26.0% | Starace 2025 (b14, c14) | E (K10) |
| PaperBench humans | 8 ML PhDs, best of 3, 48 h: 41.4% vs o1 26.6% (3-paper subset). o1 led early, plateaued after about 1 h; humans overtook after about 24 h | Starace 2025 (b15, d09) | S |
| Stage-wise gap | Claude: code 35.4, execution 1.8, analysis 0.7. o1: 19.5 / 5.7 / 0.0. o3-mini: 5.1 / 0.6 / 0.4. 4o: 7.7 / 0.1 / 0.0 | Starace 2025 Table 9 (d07) | E (K29) |
| Forced continuation is model-dependent | o3-mini-high 2.6 to 8.5; o1-high 13.2 to 24.4; Claude 3.5 Sonnet 21.0 to 16.1. EXP-Bench IterativeAgent: Haiku D 20.6 to 6.4, C 13.8 to 2.2; Nova Pro D 18.2 to 0.1 | PaperBench (d08), EXP-Bench (d11) | E (K24) |
| Scaffold gap on the same model | CORE-Bench v1.1: about 44 pp (Codex CLI vs CORE-Agent, GPT-5.4 medium) | Nadgir 2026 (d12) | S |
| Reproduction benchmark saturated | CORE-Bench Hard 97.4-100% (v1.1: GPT-5.3-Codex 97.4, Opus 4.6 92.3, GPT-5 84.6); 15 task errors and 20 shortcuts fixed; 39 tasks + 19 OOD; humans+agent more than halved time | Nadgir 2026 (d12) | S |
| Agent confidence is useless | Stated confidence 32.1% vs pass rate 93%; none beat random at separating right from wrong runs | Nadgir 2026 (d13) | S (K28) |
| Other agent benchmarks | MLAgentBench Claude 3 Opus 37.5% (100% house price, 0% BabyLM); ScienceAgentBench best 32.4% (34.3% with expert knowledge; o1 42.2%); MLE-bench o1-preview+AIDE 16.9% pass@1, 34.1% pass@8 (bronze or better) | a20, a22, b20 | E (K10) |
| Component skill vs whole chain | DiscoveryWorld: unit tasks 60%+; full ReAct 38% easy, 18% challenge; humans 66% | Jansen 2024 (a21, c07, c08) | S |
| Information-gain selection beats prompting | BED-LLM 20 Questions: mean +37.4 pp over Prompt-Only per paper (+40.4 pp from 18 Table 1 cells; gap unexplained). Animals GPT-4o 45 to 93; Celebrities Mistral-Large 19 to 91; Things GPT-4o 34 to 64; Things Llama-3.1-8B 10 to 26 | Choudhury 2026 (c09, d01) | E (K14) |
| Parts of BED-LLM | Animals GPT-4o: BED-LLM 93, Entropy 88, Implicit Max 70, Data-Estimation 70, ICL Beliefs 25. Implicit Max minus Prompt-Only +8.2 pp; BED-LLM minus Implicit Max +32.2 pp; minus Split +15.3 pp. Static likelihood beat history-conditioned likelihood in most cells (Animals GPT-4o 93 vs 86) | c10, d02, d03 | S |
| DPO on informative questions | INLG: success 56.7 to 68.9%, EIG 0.34 to 0.45, questions 7.1 to 5.2. Plain fine-tune hurt (46.6%) | Mazzaccara 2024 (a25) | S |
| Preference elicitation | OPEN beats LM-only on TIDA at lower compute; open-ended LM questions score high on LM metric but lose the Bayesian benefit | Handa 2024 (a24) | S (K15) |
| Zendo rule revision | Strongest model 6.55/8 vs ReAct 4.60/8 vs humans 5.26/8; human-fit R2 .57 (online fuzzy) vs .05 (batch) | Piriyakulkij 2024 (a23) | S |
| BoxingGym | 10 environments, EIG regret; all models weak; prior description often did not help; Box's Apprentice no consistent gain; instruct beat reasoning models | Gandhi 2025 (a12, a13, c01-c03) | S (K17) |
| POPPER error control | alpha 0.1. Type-I 0.152 / 0.016 / 0.180 (DiscoveryBench / IL2 / IFNG); power 0.610 / 0.897 / 0.717. ReAct power 0.378 / 0.140 / 0.040. No relevance check: Type-I 0.311 / 0.264 / 0.173. All nulls are permutation nulls | Huang 2025 (c04, c05, d04, d06) | S (K16) |
| POPPER failure causes | Misread p-values 35.9%; ineffective design 28.1%; test breaks implication 17.2%; wrong implementation 8.6%; hallucination 0.8% | d05 | S |
| POPPER vs 9 experts | No significant difference; 9.7x faster; 3.6x more code; 2.5x more tests. Relevance checker vs human Spearman 0.55 | c06, d05 | S |
| AI Scientist audit | 5 of 12 ideas (42%) failed on coding; code grows 8% per iteration (+529, 118, 83, 66, 21 chars); median 5 citations; 5 of 34 from 2020 or later; 4 of 7 manuscripts (57%) wrong numbers; micro-batching marked novel; about $6 per paper | Beel 2025 (a16, b12, b13) | E (K12, K19) |
| AI Scientist reviewer vs human | Balanced accuracy 0.65 vs 0.66; F1 0.57 vs 0.49; FNR 0.39 vs 0.52; FPR 0.31 vs 0.17 | Lu 2024 (a17) | S |
| AI Scientist-v2 | 3 papers submitted; best 6.33 (6, 6, 7), about top 45%; negative result; withdrawn by agreement | a18, b21 | S |
| Selection bias in AI scientists | Agent Laboratory: 82.4% of benchmark choices in first 4 listed; AI Scientist v2 with inverted test results picked the lowest-ranked about half the time (never in control); audit F1 0.51 paper-only vs 0.86 with logs and code; selection-bias F1 0.31 vs 0.90 | Luo 2025 (d16, d17) | S (K27) |
| Preregistering for the next model | Blocked 17 of 23 (73.9%, CI 53.5-87.5) and 32 of 44 (72.7%, CI 58.2-83.7) hacked cells; own test: 6 of 7 failed to carry over | Thomas 2026 (d14) | S (K26) |
| Researcher degrees of freedom in LLM experiments | 2,430 specifications on anchoring gave indices from strongly negative to strongly positive | Vaccaro 2026 (d15) | S |
| LLM simulated subjects | Ultimatum, garden path, Milgram replicated; Wisdom of Crowds hyper-accuracy (median 1.0, IQR 0.0); grows with size and alignment; human reference 52 subjects | Aher 2023 (b22, b23, d18) | S (K20) |
| Children vs LLMs on tool innovation | Children n=42: 88.4% (SE 2.82) vs adults 84.9% on one tool task; LLM numbers not read | Yiu 2023 (c18) | S |
| Blicket rule switch | Raw accuracy Base 87.3%, CG 77.3%, CG+DB 89.1%; CG+DB costs 30-50% more; own scaffold, preprint | Alderete and Baker 2026 (c19) | S |

## 4. Mechanisms and models

Items marked (human) come from history; items marked (measured) have an LLM result.

### 4.1 Independent-failure check (Hacking, Franklin) (human)
- Goal: a second reading of a result that cannot fail the same way as the first.
- Build: for a claim C from method A (say, reasoning in text), run method B with different failure modes (execute code, compute by a different formula, test on a mutated input). Agreement of A and B counts. k resamples of A do not count (G4).
- Score: errors caught by B that k resamples of A miss, at equal tokens.
- Evidence: K01. Historical only. Not tested on LLMs.

### 4.2 Known-answer calibration (Franklin, Weber) (human; evaluator side partly measured)
- Goal: learn whether the test can see anything before trusting a null or a positive.
- Build: before test T on the real item, run T on a planted case with a known answer (a positive and a negative control). If T fails the planted case, mark T untrusted and repair it or choose another. Code plants the case and compares.
- Why: Weber's apparatus failed the injected pulses. Luo et al. (d16) use a known ceiling (labels flipped at 20% and 30%, so accuracy above 1 minus noise means peeking). That is evaluator-side only.
- Cost: one extra run per test. No LLM study has put this inside the agent (c26, gap 3).

### 4.3 Fixed pass criterion before the run (against the regress) (partly measured)
- Build: before running T, code stores a pass rule (metric, threshold, which held-out items). The agent may not change it after seeing output. A change is logged as a new test and adds to the look count.
- Evidence: Thomas et al. (d14) block 72-74% of p-hack transfers by fixing the plan and testing on the next model. Their setting is human-tuned LLM labelling pipelines, not an agent, and needs a later model. The agent analogue is a held-out set or a second model.
- Status: K03 contested (historical); K26 single source (measured).

### 4.4 Look counter and rising threshold (3-sigma to 5-sigma) (human)
- Build: code counts the candidate tests tried on one item (n looks). Required evidence rises with n. Simple form: alpha / n. Sequential form: multiply e-values across tests and accept when the product exceeds 1/alpha.
- Physics logic: with 80 bins a 3-sigma bump somewhere is likely; one named bin is about 100 times less likely than "anywhere".
- Measured: POPPER's e-value product (Type-I 0.145-0.18 on permutation nulls at alpha 0.1). No agent study compares thresholds (gap 8).

### 4.5 Sequential falsification with e-values (POPPER) (measured)
- Loop: (1) a designer agent proposes a falsification test, a sub-hypothesis that must hold if the main one is true. (2) A relevance checker (LLM) rates whether the sub-hypothesis is truly implied. (3) An executor agent writes and runs code and returns a p-value. (4) Code converts the p-value to an e-value and multiplies e-values across tests. (5) Accept when the product exceeds 1/alpha; reject when a test refutes or tests run out.
- Why it works: a product of e-values is a valid sequential test, so error stays bounded however many tests are tried and whenever you stop.
- Measured: Type-I 0.152 / 0.016 / 0.180 at alpha 0.1; power 0.610 / 0.897 / 0.717 (d04). Removing the relevance check raised Type-I to 0.311 / 0.264 / 0.173 (c05). Failures: misread p-values 35.9%, bad design 28.1% (d05).
- Limits: nulls are random column permutations; control does not mean discoveries are true (d06). The relevance checker is itself an LLM.

### 4.6 Expected information gain test selection (BED-LLM) (measured)
- Build: (1) sample N hypotheses h from the LLM (its own prior). (2) Sample M candidate tests q. (3) For each q, ask the LLM for the probability of each outcome y given each h (the likelihood). (4) Code computes EIG(q) = entropy of the mixed outcome distribution minus the mean entropy of outcomes per hypothesis. (5) Run the highest-EIG q. (6) Update hypothesis weights by Bayes in code from the real outcome. Repeat.
- Measured: +37.4 pp (abstract) to +40.4 pp (table cells) over Prompt-Only in 20 Questions. The cheap variant where the LLM picks the best of the same candidates (Implicit Max) added only +8.2 pp. Letting the LLM update beliefs in context scored 25 (Animals GPT-4o) vs 93. A static likelihood beat a history-conditioned one in most cells.
- Cost: several LLM calls per turn. Run time about equal to the Entropy and Split variants; Data-Estimation over 10x slower (d03). No token-matched comparison (gap 1).

### 4.7 Discriminating test between two rules (Meselson-Stahl pattern) (human; in schema S7)
- Build: given two or more live rules that fit all data, code searches for an input where they give different outputs. Run it. SCHEMA S7 already has this as counterexample search.

### 4.8 Stage separation (measured)
- Build: log design, implementation, run and read-out as separate stages. Gate each in code, not on agent opinion.
- Why: PaperBench Claude scores 35.4 / 1.8 / 0.7 by stage; EXP-Bench shows 39.71% missing components and 29.38% broken environments. A combined score hides where it fails.

### 4.9 Output-cited numbers (measured)
- Build: every number in a final report points to a tool output id. Code rejects numbers with no source. MLAgentBench's Fact Check entry reduced but did not remove hallucinated improvement (a20). Beel found 4 of 7 manuscripts with wrong numbers (a16). Luo found paper-only audits at F1 0.51 vs 0.86 with logs.

### 4.10 Hide test scores from the selector (measured)
- Build: the loop that picks which result to report never sees held-out scores; a separate step scores after the choice. Luo et al. found an internal reward that sees test scores favours them (d16).

## 5. What holds up

### 5.1 Replications and meta-analyses (human science)
- Shrinkage is established across four large efforts: OSC 36% (35/97), Camerer 62% (13/21), Many Labs 2 54% (15/28), cancer biology 85% median shrinkage and 46% under a 5-method rule. Fields and methods differ; all agree that published effects shrink (K06 [E]).
- The headline percent depends on the rule. Cancer biology gives 18% to 62% on the same data (K07 [E]). Treat "X% replicate" as a range.
- Did not explain failure: replication team expertise and self-rated replication quality (OSC); hidden moderators such as culture, lab vs online, WEIRD vs less-WEIRD (Many Labs 2, exploratory). Heterogeneity was significant in 11 of 28 effects; only one had tau above .20.
- Did predict: strength of the original evidence (OSC). Peer markets predicted outcomes (60.6% vs 62%), so plausibility carries signal (K08 [S]).
- Methods text is a bottleneck: no experiment of 193 needed zero clarification (K09 [E]).
- Caveats: vote counting is crude (replications near the threshold count as failures; originals inflated by selection; OSC used three journals in one year). Camerer's set is 21 studies. Some original authors disputed Many Labs 2 conditions.

### 5.2 Historical claims
- Hacking's independent-method argument and Franklin's strategies are philosophical arguments, not measured. The one quantitative anchor is the sigma-threshold practice.
- Experimenter's regress [C]. Franklin's answer fits the Weber case; Collins disputes it. No test settles it.
- Galison two traditions [C]; Staley disputes the split.

### 5.3 LLM agent evidence that holds
- Agents rarely finish whole experiments (K10 [E]; EXP-Bench, PaperBench, ScienceAgentBench, MLAgentBench, MLE-bench). These benchmarks share a style (the agent writes and runs ML code), so they are not fully independent in setting.
- Failure is mostly implementation and execution, not design (K11 [E]).
- Agents state results before running (K12 [E]).
- Scaffold effects flip sign by base model (K13, K24 [E]). No scaffold is uniformly better.
- Choosing tests by computed information gain beats prompting (K14 [E]); token-matched evidence is missing.
- Automated pipelines are weak on novelty (K19 [E]).

### 5.4 What failed or did not help
- Domain context did not help BoxingGym models and sometimes hurt after 10 experiments (strong early assumptions not revised; error rose in hyperbolic discounting) (c02).
- Box's Apprentice (explicit model fitting) did not reliably beat plain GPT-4o; it chose too-simple forms (c03).
- Forced continuation hurt Claude 3.5 Sonnet on PaperBench and Haiku and Nova Pro on EXP-Bench (d08, d11).
- Plain fine-tuning on questions lowered 20Q success (46.6% vs 56.7%); DPO on informative pairs raised it (a25).
- In-context belief updating failed in BED-LLM (25 vs 93).
- The CG state machine alone lowered raw blicket accuracy (87.3 to 77.3, not significant); monitors recovered it (89.1) (c19).
- Preregistration for the next model leaves about a quarter of hacks transferring (d14).
- No LLM study of Hacking-style instrument calibration was found (c26; limited search, not proof).

### 5.5 Moderators
- Task novelty: MLAgentBench 100% on house price, 0% on BabyLM. Old tasks may be memorised (b18).
- Time: o1 leads humans in the first hours, plateaus; humans win after about 24 h (d09).
- Model: 32B beat 7B in BoxingGym; closed beat open; instruct beat reasoning models (a12).
- Benchmark age: reproducing given code is saturated by mid-2026 (d12). The old CORE-Bench Hard 21.5% figure (b16) is superseded.

## 6. Language models

### 6.1 Choosing experiments
- Unaided, LLMs are poor experimenters. BoxingGym (6 LLMs, 10 environments, 5 runs): all struggle at design and model discovery. GPT-4o has the lowest EIG regret. Error rose with more experiments in hyperbolic discounting.
- LLMs ask low-information yes/no questions in 20 Questions. A 7B model had EIG 0.34 zero-shot (INLG set). Training on pairs ranked by EIG lifted EIG to 0.45 and success from 56.7 to 68.9% (a25).
- Code-computed EIG lifts success strongly in BED-LLM: Animals GPT-4o 45 to 93, Celebrities Mistral-Large 19 to 91, Things GPT-4o 34 to 64; weak model Things Llama-3.1-8B 10 to 26. The lever is that code, not the LLM, ranks candidates and updates the belief. Judgment-based picking among the same candidates gives only +8.2 pp.
- Zendo-style rule discovery: LLM-proposed rules with Monte Carlo reweighting and information-gain experiments reach 6.55/8 vs 4.60/8 for ReAct and 5.26/8 for humans (a23).

### 6.2 Running whole experiments
- EXP-Bench complete executable 0.5%. PaperBench best 21.0%. ScienceAgentBench 32.4%. MLE-bench 16.9%. MLAgentBench 37.5%.
- Stage profile: code is written well, run and read out badly (35.4 / 1.8 / 0.7).
- Cost: EXP-Bench Claude 3.7 Sonnet median $7.53 per run vs o3-mini $0.35. In ScienceAgentBench, self-debug beat OpenHands CodeAct (32.4 vs 21.6) at 17x lower cost. A simpler loop can be cheaper and better.
- By mid-2026, reproducing given repos is saturated: 97.4-100% on CORE-Bench Hard for top agents, but 20 tasks had shortcuts and 15 had errors. Scaffold changed results by about 44 pp on one model. Human plus agent more than halved completion time (d12).
- Self-report: stated confidence 32.1% vs 93% pass rate; no better than random at telling right from wrong runs (d13).

### 6.3 Falsification and error control
- POPPER keeps Type-I near alpha on permutation nulls with higher power than ReAct (0.610 vs 0.378; 0.897 vs 0.140; 0.717 vs 0.040). Without the relevance check Type-I is 0.311 / 0.264 / 0.173.
- Weak backbones break error control (GPT-4o Type-I 0.230 on DiscoveryBench; o1 0.143 with power 0.730).
- Nine biologists: no significant difference from POPPER, which was 9.7x faster.

### 6.4 Integrity of AI-run science
- Sakana audit: 42% of ideas fail on coding, 57% of manuscripts have wrong numbers, novelty by keyword search.
- Luo: arbitrary benchmark selection (82.4% in first four listed), reward that sees test scores. Auditing from logs gives F1 0.86 vs 0.51 from the paper.
- Review scores do not prove soundness: Lu et al.'s reviewer is near human (F1 0.57 vs 0.49) while Beel and Kan find wrong numbers in the outputs.

### 6.5 LLMs as study subjects
- Simulated subjects replicate three of four classics (Ultimatum, garden path, Milgram) and break on wisdom of crowds with hyper-accuracy (median 1.0, IQR 0). Authors changed details of three of four studies to reduce recall. No evidence that simulations predict unseen replications (gap 10).
- Vaccaro: 2,430 specifications gave anchoring indices from strongly negative to strongly positive. Model, prompt and delivery choices alone can flip the result. An agent that runs experiments on LLMs must fix these choices ahead.

### 6.6 What changed results, and by how much
- Code computing information gain: +8 to +91 pp depending on cell (BED-LLM).
- Relevance check: Type-I 0.311 to 0.152 and 0.264 to 0.016 on two sets; no change on the third (0.173 vs 0.180).
- Scaffold: PaperBench -4.9 to +11.2 points depending on model; CORE-Bench v1.1 about 44 pp.
- Plan fixed before the run, run on a later model: 73-74% of hacked cells blocked.
- Logs for auditing: F1 0.51 to 0.86.
- DPO on informative pairs: success +12.2 pp on INLG.

## 7. What our agent should take

Status: [E] established, [S] single source, [C] contested. Schema parts: G guardrail, S state, O operator, memory. Evidence ids refer to the jsonl files.

### Add now (established)
Mostly wording and code hooks, not new claims.

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Log the stages of any test separately: design, implementation, run, read-out. Do not trust a combined pass. | S4, G7 | [E] K10, K11, K29 | a14, a15, d07, d10, a16 |
| A2 | Every number in a report cites a tool output id. Code rejects numbers with no output. | G2, G10 | [E] K12 | a20, a16, d16, d17 |
| A3 | Test each scaffold change per base model. Forced continuation is not universally good. | G7 | [E] K13, K24 | b14, c15, d08, d11, d12 |
| A4 | Shrink confidence in a lone positive from one run. Expect it to be inflated. (Human data, by analogy.) | G3, G4 | [E] K06 | b01, b03, b05, b08 |
| A5 | Report a borderline verdict under two or three rules, not one threshold. | S4, S8 | [E] K07 | b08, b01 |
| A6 | Check novelty by retrieval or running, not keyword match or model opinion (already G8). | G8 | [E] K19 | a16, b13, b21 |
| A7 | Do not use stated confidence to decide a test passed; use executed output or a known-answer check (already in 4b). | S4 | [E] 4b, [S] K28 | d13 |
| A8 | Records meant for reuse hold all parameters, data paths and the pass rule; methods text alone rarely lets another run repeat a test. | memory | [E] K09 (human data) | b07, b17 |
| A9 | Where candidate tests and outcomes can be made explicit, rank tests by computed information gain; keep belief updates in code. | S4, S7, G5 | [E] K14 (closed games only) | c09, c10, d01-d03, a24, a25 |

A9 is established by direction in closed games (20 Questions, preference elicitation). Whether it wins at equal tokens in open test design is open, so it also appears as T1.

### Test first
Nothing here goes to SCHEMA.md until its test (UNKNOWNS.md) passes.

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | EIG-ranked test choice at equal tokens, agent writing its own likelihood | S4 | [S] on budget | c09, d01-d03 |
| T2 | Known-answer calibration (positive and negative control) before trusting a test | S4 | [S] historical only | a04, a05, b10, c26 |
| T3 | Run-and-check: execute the test and cite the real output before any claim | S4, S5 | [S] | d07, a15, a16 |
| T4 | Pass criterion fixed before the run vs free to change | S4, G3 | [C] K03; [S] K26 | a05, a06, d14 |
| T5 | Look counter with rising threshold (alpha / n or e-value product) | S4, S8 | [S] K04, K16 | a04, c04, d04 |
| T6 | Relevance gate: does the test bear on the claim? | S4 | [S] K16 | c05, d04, d05 |
| T7 | Independent-method check (code vs reasoning) vs k resamples of one method | S4, S8, G4 | [E] historical; no LLM test | a01, b11 |
| T8 | Predict the test outcome before running; score calibration | S4, memory | [S] K08 | b04 |
| T9 | Hide held-out scores from the loop that picks what to report | G3, S7 | [S] K27 | d16, d17 |
| T10 | Forced continuation vs free stop, split by early-stop rate | S5, G12 | [E] model-dependent; predictor untested | b14, d08, d11 |
| T11 | Prior description on/off in test design when the prior may mislead | S2, S4 | [S] K17 | c02, c03 |
| T12 | Code-run discriminating test between two live rules (already S7, [S]) | S7 | [S] | a07 |

Not taken forward: exploratory experimentation (Steinle), Galison's image/logic split and trading zones, children vs LLM tool innovation (K21, K23). No agent test follows from them yet.

## 8. Concrete tests on our bench

Always: both arms get equal total tokens, setup included (G7). Same items, same base model, three or more seeds. Report the mean difference with a paired interval.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 EIG selection | 20-Questions-style and rule-discovery items with a fixed hypothesis set; ARC-style items where several rules fit the examples | (a) model chooses the next test freely; (b) model proposes 5 candidates, code ranks by EIG from the model's own likelihood table; (c) model picks the best of the same 5 | Success at turn budget; turns to solve | (b) over (a) by +10 to +30 pp at equal tokens (BED-LLM +37-40 pp unmatched); (c) about +8 pp. Fail if (b) does not beat (a) once its extra calls are paid. |
| T2 Calibration | Items with a check (code tasks, programs on ARC grids, planted bugs) | (a) run the test on the real item; (b) first run it on a planted positive and negative control | Share of broken tests caught; final accuracy | Size unknown, no LLM data. Guess: catch 20-40% more broken tests for one extra run. |
| T3 Run-and-check | Experiment tasks where the agent writes a script | (a) agent writes and reports; (b) agent writes, code runs, agent must cite the real output | Execution failure rate; share of unsupported numbers | Unsupported numbers near 0 in (b). Execution failure down 10-20 pp (EXP-Bench and Sakana show 40-50% failures). |
| T4 Fixed criterion | Items with a threshold and a hidden held-out part | (a) criterion fixed before output; (b) agent may revise it after seeing output | False-confirmation rate on seeded null items | (a) lower by 30-70% (Thomas: 72-74% blocked). Fail if gap under 10 pp. |
| T5 Look counter | Seeded null items, many candidate tests allowed | (a) fixed bar; (b) bar rises with number of looks | False-positive rate on nulls; power on seeded positives | False positives near alpha in (b); power loss under 15%. |
| T6 Relevance gate | Seeded nulls and items with a true effect | (a) any test counts; (b) code-gated LLM relevance rating | False-positive rate; share of irrelevant tests | Type-I cut by up to half (POPPER 0.311 to 0.152 on one set, none on another). |
| T7 Independent method | Items with ground truth and a known error rate | (a) k resamples of one method; (b) a second method with a different failure mode | Distinct errors caught per 1,000 tokens | (b) catches more because failures are less correlated (G4). Size unknown. |
| T8 Predict first | Test outcomes that can be scored | (a) run then judge; (b) state predicted outcome and confidence, then run | Brier score of the stated outcome | Small. A signal for class records, not a gate. |
| T9 Hidden scores | Multi-candidate selection with a score | (a) selector sees held-out score; (b) sees only dev score | Gap between dev score and true held-out score | Less peeking in (b). |
| T10 Forced continue | Long tasks with an early-stop option | (a) free stop; (b) forced to continue until budget or checked pass | Pass rate by base model, split by early-stop rate in plain runs | Helps models that stop early, hurts others (Claude 21.0 to 16.1). |
| T11 Prior on/off | Items where the domain prior may mislead | (a) with prior description; (b) without | Error after n experiments | Prior hurts on some items (BoxingGym). Find where. |

## 9. What does not transfer, and why

- **Physical apparatus and noise.** Hacking's microscopes and Franklin's calibration pulse assume instruments with measurable noise. Our tests are code runs, mutated inputs and held-out items. The idea (independent paths, known signal) transfers; the detail does not.
- **Community negotiation (Collins, Pickering, Galison trading zones).** One agent has no peers. The regress is handled by a pre-set criterion and a code check. Simulating a community would be debate, ruled out by G9.
- **Sigma thresholds as such.** 5-sigma rests on known noise models. Use a rule with a stated error guarantee (e-value product, alpha / n), not a borrowed number.
- **Human replication rates (36%, 62%).** They describe publication selection and low power. An agent's single run is not a published effect. The lesson (shrink lone positives) carries by analogy; the percentages do not.
- **Preregistering for the next LLM.** An agent cannot get a model that does not exist yet. The substitute is a held-out set or a second model (untested).
- **BED-LLM and Zendo results.** Closed, small hypothesis sets with simulated answerers. Open science has no fixed answer list.
- **Benchmark scores on reproducing paper code.** Saturated and shortcut-prone by mid-2026 (d12). They say little about designing a new test.
- **Simulated subjects as a crowd.** Hyper-accuracy (median 1.0, IQR 0) means one model's samples are narrower than a human crowd. Not independent voters (G4).
- **36-48 hour runs.** Our bench is token-bounded and short. The human edge after 24 h does not apply.
- **Robot Scientist and lab automation.** Not opened (c21); outside our setting.

## 10. Open questions

1. Does EIG-ranked test selection still win at equal tokens when the agent writes the likelihood and the candidates come from an open space? (Gap 1, partly closed.)
2. Does a run-and-check step cut the 40-50% execution failure rate, and at what token cost? (Gap 2, open.)
3. Does known-answer calibration catch errors that resampling misses? No LLM study exists. (Gap 3.)
4. Does POPPER-style error control hold on non-permutation nulls (real but irrelevant data, confounded nulls)? (Gap 4, open for nulls.)
5. How much does a fixed pass criterion reduce post-hoc tuning in an agent, as opposed to human-tuned pipelines? (Gap 5, partly closed.)
6. Do post-saturation successors of PaperBench and EXP-Bench with newer models show the same stage profile? (Gap 6, open.)
7. What do Hacking, Galison and Gooding say about the order of building apparatus and testing? (Gap 7, open; needs the books.)
8. What threshold rule gives what false-positive rate when an agent tries many tests? (Gap 8, open.)
9. Is there a cheap predictor of whether forced continuation helps a given model? The PaperBench note that all models but Claude often stopped early is a candidate. (Gap 9, untested.)
10. Do LLM-simulated replications predict real outcomes of unseen replications? (Gap 10, open.)
11. Why do BED-LLM's abstract (+37.4 pp) and table cells (+40.4 pp) differ? Unexplained.
12. Is there a measurable experimenter's-regress effect in LLM test design when no independent criterion exists?
13. Does Gooding's procedure-construal loop (revise test and description together) have a measurable analogue in agent revision?

## 11. Sources

[V] = opened by the evidence agents (full text, PDF text or abstract page as noted). [M] = snippet or memory only.

**History and philosophy**
- [V] Franklin and Perovic. Experiment in Physics. Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/physics-experiment/ (a01-a08, a11, b09-b11; first 100,000 characters). Secondary source for Hacking 1983, Galison 1987 and 1997, Franklin 1986/1990/2013, Collins 1985, Pickering 1984/1987, Meselson-Stahl, Kettlewell/Rudge, Karaca, Perovic, Staley 1999.
- [M] Hacking (1983) Representing and Intervening. Read only via SEP.
- [M] Galison (1987) How Experiments End; (1997) Image and Logic. Read only via SEP.
- [M] Gooding (1990) Experiment and the Making of Meaning. Not opened; background knowledge only.
- [M] Steinle (1997) Entering new fields: exploratory uses of experimentation. https://cambridge.org/core/journals/philosophy-of-science/article/entering-new-fields-exploratory-uses-of-experimentation/A1BF59B7198F4C380D3B5F1FAEFF9241 (snippet and abstract).
- [M] King et al. (2009) The Automation of Science (Robot Scientist Adam). https://www.science.org/doi/10.1126/science.1165620 (memory only).

**Replication in human science**
- [V] Open Science Collaboration (2015) Estimating the reproducibility of psychological science. https://discovery.dundee.ac.uk/ws/files/7385883/RPP_SCIENCE_2015.pdf
- [V] Camerer et al. (2018) Replicability of social science experiments in Nature and Science. https://www.gwern.net/doc/statistics/bias/2018-camerer.pdf
- [V] Klein et al. (2018) Many Labs 2. https://researchonline.lse.ac.uk/id/eprint/91159/1/Kappes_Many-labs-2.pdf
- [V] Errington et al. (2021) Challenges for assessing replicability in preclinical cancer biology. https://elifesciences.org/articles/67995 (first 100,000 of about 450,000 characters)
- [V] Errington et al. (2021) Investigating the replicability of preclinical cancer biology. https://elifesciences.org/articles/71601 (first 100,000 of 274,741 characters; abstract re-checked in the critique)

**LLM and agent studies**
- [V] Gandhi et al. (2025) BoxingGym. https://arxiv.org/abs/2501.01540
- [V] Choudhury et al. (2026) BED-LLM. https://arxiv.org/abs/2508.21184
- [V] Huang et al. (2025) POPPER. https://arxiv.org/abs/2502.09858
- [V] Piriyakulkij et al. (2024) Doing Experiments and Revising Rules with Natural Language and Probabilistic Reasoning. https://arxiv.org/abs/2402.06025
- [V] Handa et al. (2024) Bayesian Preference Elicitation with Language Models (OPEN). https://arxiv.org/abs/2403.05534
- [V] Mazzaccara, Testoni, Bernardi (2024) Learning to Ask Informative Questions. https://arxiv.org/abs/2406.17453
- [V] Kon et al. (2025) EXP-Bench. https://arxiv.org/abs/2505.24785
- [V] Starace et al. (2025) PaperBench. https://arxiv.org/abs/2504.01848
- [V] Siegel et al. (2024) CORE-Bench. https://arxiv.org/abs/2409.11363
- [V] Nadgir et al. (2026) Life After Benchmark Saturation: CORE-Bench v1.1. https://arxiv.org/abs/2606.26158
- [V] Huang et al. (2024) MLAgentBench. https://arxiv.org/abs/2310.03302
- [V] Chen et al. (2025) ScienceAgentBench. https://arxiv.org/abs/2410.05080
- [V] Chan et al. (2024) MLE-bench. https://arxiv.org/abs/2410.07095
- [V] Jansen et al. (2024) DiscoveryWorld. https://arxiv.org/abs/2406.06769
- [V] Lu et al. (2024) The AI Scientist. https://arxiv.org/abs/2408.06292
- [V] Yamada et al. (2025) The AI Scientist-v2. https://arxiv.org/abs/2504.08066
- [V] Beel, Kan, Baumgart (2025) Evaluating Sakana's AI Scientist. https://arxiv.org/abs/2502.14297
- [V] Luo, Kasirzadeh, Shah (2025) The More You Automate, the Less You See. https://arxiv.org/abs/2509.08713
- [V] Thomas, Gligoric, Shah (2026) Mitigating LLM-based p-hacking by preregistering for the next LLM. https://arxiv.org/abs/2606.27687
- [V] Vaccaro (2026) Preregistration for Experiments with AI Agents. https://arxiv.org/abs/2606.11217
- [V] Aher, Arriaga, Kalai (2023) Using LLMs to simulate multiple humans. https://arxiv.org/abs/2208.10264
- [V] Yiu, Kosoy, Gopnik (2023) Imitation versus Innovation. https://arxiv.org/abs/2305.07666 (position paper; LLM scores not read)
- [V] Alderete and Baker (2026 preprint) Separable Pathways for Causal Reasoning. https://arxiv.org/abs/2604.20039 (preprint, own scaffold)
- [M] Kosoy et al. (2022) blicket environment. https://arxiv.org/abs/2206.08353 (snippets only)

Local files: evidence_a-d.jsonl, claims.jsonl, critique.md in this folder; SCHEMA.md in research_notes/single_agent.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 11 established claims: 7 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D07.04-K11** (reworded: the sources support less). EXP-Bench says implementation is the most prevalent failure type but design failures (16.05%, 7.62%) and conclusion failures (26.18%, 19.66%) were also frequent, so 'not design' is stronger than the source. Corrected claim: Agent failures in EXP-Bench are most prevalent in implementation (39.71% missing essential components) and execution (29.38% environment misconfiguration, 23.84% script errors), though design (16.05% incomplete or misclassified variables, 7.62% extraneous additions) and conclusion (26.18% missing, 19.66% incorrect) failures were also frequent; in an independent audit of Sakana's AI Scientist, 5 of 12 ideas (42%) failed with coding errors.
- **D07.04-K12** (reworded: the sources support less). MLAgentBench does report hallucinated improvement without executing the code, but Sakana audit only reports incorrect or hallucinated numbers in 4 of 7 manuscripts, not that they were reported before running code. Corrected claim: Agents sometimes report improvement without running the code (MLAgentBench: the model hallucinates improvement after modifying a file without executing it), and in an independent audit 4 of 7 Sakana AI Scientist manuscripts (57%) contained incorrect or hallucinated numerical results.
- **D07.04-K19** (reworded: the sources support less). The v2 workshop result (1 of 3 manuscripts above the acceptance threshold, 6.33) is presented by its authors as encouraging, and the three v2 entries are one paper; only the authors' internal review (none met main-track standards) supports 'weak quality'. Corrected claim: An independent audit found Sakana's AI Scientist v1 keyword-based novelty check labelled well-known ideas such as micro-batching for SGD as novel; for AI Scientist-v2, 1 of 3 fully AI-written workshop submissions scored 6.33 (above the workshop acceptance threshold, withdrawn by prior agreement), but the authors' own review judged none of the three to meet main-track conference standards.
- **D07.04-K29** (reworded: the sources support less). PaperBench Table 9 shows the code-vs-execution-vs-result gap (35.4/1.8/0.7 for Claude), but EXP-Bench Table 1 does not show code writing far stronger than running (implementation 20.3 vs execution 15.0 for OpenHands+o3-mini; 35.0 vs 33.2 for Claude-3.7), its collapse comes from requiring all stages together; the 'only for new experiments' conclusion is the researcher's inference from CORE-Bench v1.1 saturation. Corrected claim: In PaperBench (2025), agents' code development scores are far above execution and result-match scores (Claude 3.5 Sonnet BasicAgent 35.4 vs 1.8 vs 0.7); in EXP-Bench the single-stage scores are similar (implementation 20.3, execution 15.0 for OpenHands+o3-mini) and success collapses only when stages are required together (0.5% complete and executable); on CORE-Bench v1.1 (June 2026) top agents reach 97.4-100% when rerunning given code, so accuracy saturated there.
- **D07.04-K01** (now single-source: only one opened source, code check).
- **D07.04-K02** (now single-source: only one opened source, code check).
