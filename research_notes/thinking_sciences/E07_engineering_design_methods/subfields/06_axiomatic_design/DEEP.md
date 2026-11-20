# Axiomatic design: deep document

*Subfield E07.06. Focus: the independence axiom (Suh). Evidence ids a01-a28, b01-b26, c01-c25, d01-d18; claims E07.06-K01 to K19. Written from the evidence files and critique.md in this folder. Short version: the human evidence is one small experiment plus one partial replication, there is no LLM test of the independence axiom itself, and the closest LLM work is on design structure matrices.*

## 1. What it is

Axiomatic design (AD) is a design theory by Nam Suh (MIT). It was developed from the 1990s on. It treats design as a mapping between four domains: customer needs, functional requirements (FRs), design parameters (DPs) and process variables [a01, a20].

The design equation is FR = [A] DP. The matrix A says which DP moves which FR.

There are two axioms [a01, b21]:
- **Independence axiom.** Keep the FRs independent. Each FR should be settable by one DP without disturbing the others.
- **Information axiom.** Among designs that satisfy independence, pick the one with the least information content. Information is I = log2(1/p), where p is the chance the design meets the FR [a27, background knowledge, not verified].

The matrix gives three classes [a01]:
- **Uncoupled:** A is diagonal. Each DP moves one FR.
- **Decoupled:** A is triangular. A fixed order of setting DPs works.
- **Coupled:** anything else. One DP strongly moves two or more FRs.

Zigzagging is the method: write FRs (what), choose DPs (how), write the design equation, check independence, then decompose the next level and repeat [a04].

Why it matters to our agent: the independence check is a cheap, code-checkable test on a restated problem. It fits G5 (code selects) and S2 (represent). It does not help create the requirements. That part is the weak spot [a02].

Name clashes to avoid [a12, a18, b19]: the "axioms" in AssemCAD are engineering rules, and "axiomatic design" in the building-ontology paper means logical axioms. Neither is Suh.

## 2. History and theories in depth

**Founding texts.**
- Suh 1990, *Principles of Design*. Suh 2001, *Axiomatic Design: Advances and Applications*. Suh 2005, *Complexity: Theory and Applications* [a20].
- Suh (1995), "Axiomatic design of mechanical systems": domains, characteristic vectors, zigzagging, two axioms, corollaries and theorems for simple systems, large systems and organisations. About 56 Crossref citations [a21, M].
- Suh (1998), "Axiomatic design theory for systems": extends to large systems. About 433 citations [a22, M].
- Suh (1999), complexity, periodicity and the design axioms: links the axioms to a theory of complexity. Includes "imaginary complexity", uncertainty from the designer's lack of knowledge. About 137 citations [a23, M].

**Strong claims in the theory.** Suh Theorem 9 says coupled designs cannot be manufactured as stated. Theorem S3, as cited by Homay: if first-level FRs are wrong, no lower-level choice repairs it, and coupling at the top propagates through the whole decomposition [a03, b22]. These are theory claims. No measured test of S3 was found.

**Rival and neighbouring views.**
- Hazelrigg (1999): design is decision making under uncertainty. Eight axioms, three theorems, and the third theorem puts severe conditions on design methods [a24, M].
- QFD treats coupling as normal and even useful. A 1994 paper noted this conflicts with AD [b24, M].
- Design structure matrices (DSMs) are close cousins of the design matrix. Most LLM work near AD is on DSMs (section 6).
- Hetero-functional graph theory was derived from AD for large flexible systems [a19].

**Critiques of the axiom from inside the MIT group.** Two lines soften, not refute, it [b25]:
1. Frey and Hirschi (2002): coupling costs little at 2x2 and a lot from 3x3 up.
2. Goehler, Frey and Howard (2016): the robustness argument for independence holds only for nominal-is-best requirements.

**Current advocacy.** Homay (2025, 2026) argues for AD in software and industrial control. He says coupling lives in the functional domain, not in code links [b14, b15]. He says first-level essential FRs should be the same for any designer, and disputes Ang Liu on this [a07]. He says LLMs are weak at abduction and so fail at essential FRs [a05, b12]. This is argument, not measurement. He cites an Amazon Prime Video move from microservices back to a monolith with a 90 percent cost saving, second-hand [b16].

**Application papers.** Applications are mostly worked examples: aerodynamic intake design with a lower-triangular matrix [a16, a17]; invariant derivation for a water treatment testbed [a14, a15]; splitting research problems into parallel sprints with a DSM [b20]; set-based design decomposition [d15]; Extenics-enhanced AD, where the authors note novices find AD hard [c24, M]. The information axiom is mostly used for fuzzy multi-criteria selection with no outcome test [a26, d17, K16].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Coupling at 2x2 costs little time | N=12; 2x2 coupled mean 40 s vs uncoupled 24 s (about 16 s more); target range 5% of gauge; 31 coupled 2x2 tasks; alpha 0.05. Authors call it practically small | Frey and Hirschi 2002 [b01, b04] | Single-source (human, one lab) |
| Coupled solve time grows geometrically with size, uncoupled about linearly | Coupled: time proportional to 3.4^n, n=2 to 5, adj R2 0.70 per subject, 0.99 on means. Uncoupled linear: adj R2 0.71 per subject, 0.90 on means. 6x6 dropped (subjects quit) | [b02, b03, d03] | Established (2 sources, same university) |
| Partial replication of geometric growth | 10 groups of 3 people, 42 design tasks each. Geometric growth confirmed for highly coupled tasks. Team size effect independent of problem size. Pairs spend 50-60% of time in collaboration (70-80% of cost); triads 60-80% (90% of cost) | Grogan and de Weck 2016 [d04] | Replication, same university, team variant |
| Humans use different strategies by structure | Uncoupled: one slider per output. Coupled and large: more iteration, non-converging moves, random-sampling-like search. Formal solve is order 2n^3+5n^2-7n operations; predictions differ from human 3.4^n by over 2x | [b03] | Single-source |
| Suh Theorem 9 (coupled = unmanufacturable) fails at n=2 | All 2x2 coupled tasks were finished | [b04, b22] | Single-source |
| Independence axiom's robustness claim holds only for nominal-is-best | Monte Carlo of 250 modelled architectures; for max/min-is-best, contradiction level dominates, p = 1.4e-36; a coupled machining design was more robust than its uncoupled twin | Goehler, Frey, Howard 2016 [d01] | Single-source; simulation; abstract only |
| Satisfying independence improved a simulated real system | Visual SLAM/AweSim, logistic regression, time in process and utilised capacity; no effect sizes seen | Mollajan et al. 2022 [d13] | Single-source; abstract only |
| Engineers misjudge coupling | More than 80% of over 100 software engineers called the two-knob faucet uncoupled. No sampling method | Homay 2025 [b14, d09] | Anecdotal |
| AD concepts are hard to annotate in text | 6,000 patent sentences (750 per IPC section A-H) from 14,417 US patents; 19,555 concepts; 1,200 double annotated; F1 Action 0.80, Receiver 0.68, Doer 0.66, DP 0.66, AXR 0.57, AXP 0.55, FR 0.52 (concept-to-number mapping partly uncertain) | Giordano et al. 2025 [a08-a10, c04, c05] | Established as a dataset result |
| Most patent sentences carry no FR or DP; explicit links are rare | 41.33% neither; explicit relation 3.77% (226), implicit 6.83% (410); FR 5,019, DP 3,169, relation 878 | [a09] | Established |
| Fine-tuned encoders beat prompted LLMs on FR/DP extraction | Up to 0.1 F1 on sentence classification, up to 0.4 F1 on NER; about 1,000 examples enough | Consoloni et al. 2026 [c07] | Single-source; abstract only |
| LLM fills a DSM at moderate accuracy | Auto-DSM (gpt-3.5-turbo) 357/462 = 77.3% entries; correctness 82.6 / 54.5 / 40.0% by source; direct ChatGPT 66.7-85.7%, so no clear gain from the workflow | [c13, c14] | Single-source |
| LLM plus search loop matches simulated annealing on DSM sequencing and modularization | Claude-3.5-Sonnet beat a GA and 5 deterministic methods, 10 runs, 20 iterations [c15]. Claude-Sonnet-4.6 within 1.3% of SA on Kodak, Brake, HeatEx; Helicopter (19 nodes) matched the reference in 10/10 runs at k=0 [c17, d06] | Jiang et al. 2024/25; Jiang and Luo 2026 | Established (same authors) |
| Injected domain knowledge can hurt on larger DSMs, for Claude | HeatEx (17 nodes) +5.4% gap; Helicopter +3.6%; Helicopter matched the SA reference in 0/10 runs at k=1 vs 10/10 at k=0. GPT-5.2 and Qwen-3.5-Plus gain early from knowledge and k=0 catches up later | [c18, d05-d07] | Single-source; model-dependent |
| Input format barely matters; edge direction does | Directed list, matrix and prose end similar; undirected list clearly worse; removing the cost formula changed nothing | [c19] | Single-source (UCAV only, Claude, k=1) |
| Verifier plus typed rules lifts LLM CAD assembly | Text-to-CAD success / assembly preservation: AssemCAD 89.17 / 87.50; GPT-5.5 79.17 / 66.67; Claude-4.8 85.00 / 0.83; backbone swap Claude 0.8 to 82.50 | AssemCAD 2026 [a12, a13] | Single-source; not Suh |
| AD-style decomposition gives checkable invariants | 8 FRs to 30 (level 2) to 44 concrete FRs; two invariants, decision trees 100%/100%, naive Bayes 100%/93.75% (93.75 not re-checked); no false positives | Yoong et al. 2020 [a14, b18] | Single-source; two invariants |
| Claimed gain from AD-constrained agentic design | Coupling down 34.2% (p<.01), iterations down 41%, three cases. Numbers credited to a separate self-cited work; no coupling measure defined | Joshi et al. 2026 [c22, d10] | Unverified |
| No LLM test of the independence axiom itself | 0 relevant hits in about 12 Crossref queries; 6 arXiv hits, 1 touching LLMs | [a28, b10, b26, d16] | Search finding; throttled |

## 4. Mechanisms and models

### 4.1 Classifying a design matrix by program

Input: an explicit matrix A with FR rows and DP columns. Steps:
1. Drop entries below a threshold (the sensitivity cut-off).
2. If A is diagonal after dropping, label uncoupled.
3. Try to permute rows and columns to a triangular form. Do it with a topological sort on the graph "DP j affects FR i". If a sort exists, label decoupled and output the DP order.
4. Else label coupled. Output the strongly connected components. These are the knots.
5. Optional finer score: count off-diagonal entries inside the knots, or use the independence priority number idea [d14]. The three-class label cannot rank two designs in the same class.

This is a few lines of code. It is exactly the kind of check G5 wants in code, not in the model. It needs an explicit matrix. Making the matrix is the hard part (4.3).

### 4.2 Why coupling is costly: the search model

Frey and Hirschi model coupled search as random sampling inside a fixed-size target in n dimensions [b03]. If each added variable shrinks the hit volume by a roughly constant factor, expected tries grow as c^n. The fitted c is 3.4. For uncoupled tasks each output is tuned alone, so effort adds up and grows linearly in n.

An agent can break this cost if the map is linear and observable: probe each DP, estimate A from n+1 evaluations, solve it with Gaussian elimination (order n^3). The authors computed this and found it beats human behaviour by more than 2x at the sizes tested [b03]. Our agent can do this by program. Whether the agent reaches for it without being told is untested (gap 2).

Boundary: this holds for the slider task with a smooth, near-linear map. It does not carry over to discrete, noisy or non-linear design problems without more work.

### 4.3 Building the matrix from text (the weak step)

Elements: FR extraction, DP extraction, FR-DP relation. Two trained annotators reach only F1 0.52 to 0.80 [a10]. LLM output is bounded by that. Practical design:
1. Slots. One FR per slot, solution-neutral, with a range (for example "level control 10 ms to 50 ms") [a04].
2. A DP per slot. A relation cell per FR-DP pair: "does changing this DP change this FR beyond the threshold, yes or no, and why in one line".
3. Program step: classify the matrix (4.1).
4. If coupled, run an operator at the knot (decompose, add a DP, drop a constraint), then rebuild.

Fine-tuned encoders beat prompted LLMs for extraction [c07]. We do not fine-tune, so slots plus a program check is the substitute.

### 4.4 Solution-neutral FR rewrite

A bad FR bakes in a solution: "make a call over electromagnetic waves" merges two ideas and couples FRs [a06, c02]. The rewrite step: strip any how-words and keep the what. Detecting solution-jumping in text was done on six hand-made antipatterns at 100% by a multi-agent Five Whys workflow plus a deterministic evaluator [d11]. No test shows that doing this rewrite improves final design quality (K06).

### 4.5 LLM as proposer, program as scorer (DSM)

The Jiang loop [c15, c17]:
1. The prompt holds the DSM as a directed edge list, the current best solutions and a few random earlier ones, plus the cost.
2. The LLM proposes a new ordering or clustering.
3. A program computes the cost (feedback marks for sequencing; a modularization cost for clustering).
4. Keep a pool of 5 best plus 5 random. Repeat 20 to 30 iterations.

Ablations: best plus random beats best-only or random-only; edge direction matters most; the cost formula in the prompt is not needed [c19]. Knowledge of what nodes mean is optional and can hurt on larger cases [c18].

### 4.6 DSM clustering for context budget

DSM clustering and sequencing was used to split a spacecraft design chat into pieces under a token budget, with a small local model (Mistral 7B) [c20]. It moves a design tool into LLM context management. The numbers are weak.

## 5. What holds up

**Holds up (human).**
- Coupled tasks get much harder as n grows from 3 to 5. Two sources: the original and Grogan and de Weck [b02, d04]. Same university. The replication used teams and a surrogate task.
- Coupling is hard to see. More than 80 percent misjudged the faucet [b14]. Anecdotal.

**Does not hold up.**
- Suh's strong claim that coupled designs cannot work. Contradicted at n=2 [b04].
- The axiom as a general robustness rule. Fails for max/min-is-best [d01].

**Moderators.**
- Problem size n: small effect at 2x2, large from 3x3.
- Requirement type: nominal-is-best versus max/min-is-best.
- Team size: independent of problem size [d04].
- For LLM DSM work: model strength and task size moderate the knowledge effect [d07, K19].

**Interventions that worked.**
- A code verifier plus typed rules for CAD [a12].
- A program-scored LLM search loop for DSMs [c15, c17].
- Fine-tuning over prompting for extraction [c07].
- Keeping edge direction explicit [c19].

**Interventions that did not, or did not clearly.**
- The Auto-DSM workflow did not clearly beat a direct ChatGPT prompt [c14].
- Domain knowledge hurt Claude on larger DSMs [c18].
- Removing the cost formula from the prompt changed nothing [c19], so it is not a lever.

**Weak spots in the evidence base** (critique.md):
- Almost all human evidence is one experiment, N=12, one lab, a slider task.
- Replications are partial. The citing list (77 works) was not retrieved [d18].
- Full texts of Goehler 2016 and the journal Hirschi and Frey were not read.
- Homay's papers are advocacy and self-cited. The Jiang papers share authors. The Giordano and Consoloni papers share authors.
- Snippet or abstract only: a21-a27, b05-b09, b24, c07-c09, c21, c22, c24, c25.
- Search tools were throttled during the gap search, so "no study exists" is weaker than it sounds.
- Correction history: an interim critique said Helicopter had 14 nodes. Table 1 gives N=19, E=109. Use 19 [d06].

## 6. Language models

**There is no LLM test of the independence axiom.** The only LLM text that touches AD is Homay's argument that LLMs are weak at abduction and so at essential FRs. It is cited, not measured [a05, b12, d09, K15]. Giordano et al. also say earlier LLM work on AD lacked scoring against the theory [a28]. Earlier NLP work was small: Li and Tate 2010 (15 FR-DP pairs), Akay and Kim 2020 (2 FRs, 4 DPs), Akay and Kim 2021 (88 FR-DP pairs from 11 abstracts, qualitative), Akay et al. 2023 chatbot [a11, c06]. A 2021 system was compared with 75 human designers; results unseen [c09].

**What LLMs do on adjacent tasks.**

| Task | Models | Result | Source |
|---|---|---|---|
| FR/DP extraction from patents | Prompted decoder LLMs vs fine-tuned encoders | Encoders ahead by up to 0.1 F1 (classification) and 0.4 F1 (NER). Human agreement is only F1 0.52-0.80 | [c07, a10] |
| Fill a DSM from text | gpt-3.5-turbo workflow vs direct ChatGPT | 77.3% of 462 entries; direct prompt 66.7-85.7% correctness, more stable, lower completeness | [c13, c14] |
| DSM sequencing | Claude-3.5-Sonnet best, Llama3-70B second, 4 backbones | Faster than a GA, better than 5 deterministic methods; domain knowledge helped every backbone | [c15, c16, c21] |
| DSM modularization | Claude-Sonnet-4.6, GPT-5.2, Qwen-3.5-Plus; 5 cases of 12-19 nodes; 10 trials x 30 iterations; T=1.0 | Claude reaches the SA cost in 30 iterations; GPT and Qwen vary more; knowledge hurts Claude on HeatEx (+5.4%) and Helicopter (+3.6%) | [c17, c18, d05-d07] |
| Truss design with FEM check | GPT-4.1, GPT-4.1-mini; temps 0.5/1.0/1.2; 10 runs | Feasible designs; the smaller model slightly better at constraints; lower temperature gave higher success; beat NSGA-II, which found no feasible truss unbounded in 100,000 evaluations | [c10-c12] |
| CAD assembly | GPT-5.5, Claude-4.8, Qwen3.7-Max, GLM-5.2, Gemini 3.5 Flash | Raw models often fail assembly preservation (Claude-4.8 0.83%); verifier plus rules lifts it to 87.5% | [a12, a13] |
| Requirement mismatch detection | Multi-agent Five Whys | 100% on 6 antipatterns | [d11] |
| Latent need discovery | LLM user agents (Elicitron) | More latent needs than human interviews in the authors' tests | [d12] |
| Enterprise agent design under AD | not stated | Claimed coupling down 34.2%, iterations down 41%. Unverified | [d10] |

**What changed results, by how much.**
- A program verifier or scorer: the largest effect (CAD assembly preservation for Claude rose from 0.8 to 82.5 with the pipeline [a13]).
- Edge direction in the prompt: removing it was the most damaging ablation [c19].
- Domain knowledge: the sign depends on model and size, so it is not a safe lever [d07].
- Temperature: lower gave more consistent truss results [c11].

**Caution.** All numbers come from a few labs and narrow task families. Nothing shows that an AD scaffold, or a requirement-first scaffold, improves general reasoning.

## 7. What our agent should take

### Add now (established)

1. **Compute coupling and triangularity by program from an explicit matrix; never ask the model to judge it.** Schema: G5, S4/S7. Status [E]. Evidence: b14, a10, c13, c14, K05, K07. Why: humans misjudge coupling (anecdotal), annotators agree only to F1 0.52-0.80, and an LLM DSM workflow did not beat a plain prompt. This is already covered by G5; the addition is a named check, used only where a problem has several interacting requirements.
2. **For structure tasks (ordering, clustering, assigning), let the model propose and a program score, with a pool of best plus random earlier candidates.** Schema: S3/S4, O3 (decompose). Status [E] for DSM-type problems. Evidence: c15, c17, c19, K11. Limit: same-lab authors; 12 to 19 node problems.

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Matrix-first scaffold: list FRs, map to DPs, program checks triangularity, then solve in the decoupled order | S2/S3, G5 | [C] no test; theory plus human cost data | K15, K18, b02 |
| Probe-then-solve for coupled numeric tuning (estimate A with n+1 probes, solve by program) vs plain trial and error | G5, G12 | [E] for humans; untested for LLMs | K02, b03, d04 |
| Solution-neutral FR restatement in S1 | S1, G2 | [S] argued, not measured | K06, a06, d11 |
| LLM classification of coupling from text against a program-computed matrix | S2 | [S] human only | K05, K18, b14 |
| Knowledge or hint injection off by default on large tasks | G8, memory | [S] model-dependent | K12, K19, d05-d07 |
| Explicit edge direction in matrix prompts | S3 | [S] | K13, c19 |
| Finer coupling score (off-diagonal count) over a three-way label | G5 | [S] | K17, d13, d14 |
| Information axiom as a tie-break between passing designs | S7 | [S] no outcome test | K16, a26, d17 |

## 8. Concrete tests on our bench

All tests: both arms at equal tokens, setup cost counted (G7), at least 3 seeds, report mean and spread.

1. **Matrix-first vs free design.**
   - Items: 40 multi-requirement design tasks with 4 to 8 requirements, some conflicting by construction (program-known ground-truth matrix).
   - Arms: plain model; scaffold that lists FRs and DPs, builds the matrix, and a program reports knots before the final answer.
   - Metric: count of violated requirements in the final design (program-scored), plus pass rate.
   - Expected: a gain on coupled items only, null on uncoupled items. If there is no gain, drop.
2. **Coupled numeric tuning, n=2 to 5.**
   - Items: slider-type tasks with a black-box evaluator, coupled and uncoupled, 20 per size.
   - Arms: plain trial-and-error loop; loop that probes, estimates the matrix by program and solves.
   - Metric: evaluator calls to hit a 5% target range; fit growth as c^n.
   - Expected: the plain loop shows geometric growth; probe-then-solve needs about n+1 calls plus a constant. Also shows whether the plain model reaches for linear algebra unprompted.
3. **Coupling classification from text.**
   - Items: 50 written designs with a program-computed class (uncoupled, decoupled, coupled), including faucet-type traps.
   - Arms: model labels directly; model fills cells and a program classifies. Tokens equal.
   - Metric: accuracy against ground truth, by class.
   - Expected: direct labels weak on coupled-looking-uncoupled items; cell-fill plus program better.
4. **Solution-neutral FR rewrite.**
   - Items: 40 tasks with framing traps (a solution baked into the stated need).
   - Arms: solve directly; restate as solution-neutral requirements first.
   - Metric: final answer correctness; rate of solution lock-in.
   - Expected: a small gain on trap items, none or a loss on plain items.
5. **Knowledge injection by size.**
   - Items: ordering or clustering tasks of 10, 15, 20, 30 nodes.
   - Arms: node meanings shown vs hidden, same budget.
   - Metric: final cost gap to a program reference, and early-iteration gap.
   - Expected: a sign flip with size for the model we use; if not, drop the rule.
6. **Edge direction ablation.** Directed list vs undirected list vs matrix vs prose, on 12 to 20 node tasks. Metric: gap to reference. Expected: undirected is worst.

## 9. What does not transfer, and why

- **The human 3.4^n number.** It comes from 12 people moving sliders. An LLM does not tire or quit, and it can write a solve. The shape may not appear, or may appear at other sizes.
- **Strong reading of the axiom.** Coupled designs work, at least at n=2 [b04]. The agent should not reject a coupled design outright. It should cost it.
- **Robustness argument.** Holds only for nominal-is-best requirements [d01]. Many agent tasks have max or min goals.
- **Information axiom.** Used mostly as fuzzy ranking, with no outcome test [K16]. Our G5 and G8 already say how to select.
- **Axiomatic design as a method for reasoning tasks.** AD is built for physical and software artefacts. Puzzles and forecasts on our bench have no FR-DP matrix. The independence check applies only where a task has several interacting requirements and controllable choices.
- **Advocacy claims.** Joshi's 34.2% and 41%, Homay's LLM-abduction claim, and Homay's survey are unverified or untested [d10, d09].
- **AssemCAD "axioms".** Engineering rules, not Suh [a12].
- **Knowledge benefit for DSM.** Reversed for Claude on large problems [c18].
- **Zigzagging as a procedure.** Its cost is unmeasured, and it would add states beyond S1 to S3. G7 says every element must pay for itself. Do not add it as a state.

## 10. Open questions

1. Does a matrix-first scaffold beat free design for an LLM at equal tokens? No study exists [d16].
2. Does the geometric blowup replicate with LLM agents, and does a linear solve remove it?
3. How accurately can an LLM classify coupling from text, against a program?
4. What do the full texts of Goehler 2016 and Hirschi and Frey 2002 give beyond the abstracts (effect sizes, robustness conditions)?
5. Is Joshi's claim supported in full text, and how is coupling measured?
6. Do solution-neutral FR rewrites improve LLM design quality? Only detection tests exist [d11].
7. Why does knowledge hurt Claude on larger DSMs? The authors' hypothesis (semantic misalignment) is untested. Is it general to scaffolds that add guidance?
8. Independent replication of Frey and Hirschi in other labs: the 77 citing works were not read.
9. Does the information axiom pick better designs in any outcome test?
10. Dubois, Tate et al. 2012 compared AD with other methods. It was seen by title only [a25]. The result is unknown.

## 11. Sources

Marks: [V] opened (page or full text read), [M] snippet, abstract or metadata only.

**Human evidence and theory**
- [V] Frey and Hirschi (2002), The effects of coupling on parameter design, ICAD. https://www.axiomaticdesign.com/wp-content/uploads/icad2002_021.pdf
- [V] Hirschi and Frey (2002), Cognition and complexity, journal abstract. https://link.springer.com/article/10.1007/s00163-002-0011-3 (full text [M])
- [V] Grogan and de Weck (2016), Collaboration and complexity. https://link.springer.com/article/10.1007/s00163-016-0214-7
- [V] Goehler, Frey, Howard (2016), abstract. https://link.springer.com/article/10.1007/s00163-016-0236-1 ; full text [M] https://dspace.mit.edu/handle/1721.1/107683
- [V] Mollajan et al. (2022), abstract. https://doi.org/10.1177/00375497211062892
- [M] Alarm icon study, NYCU (N=96 from snippet). https://ir.lib.nycu.edu.tw/bitstream/11536/107770/1/10239863-01602-122.pdf
- [M] Suh (1995). https://doi.org/10.1115/1.2836467
- [M] Suh (1998). https://doi.org/10.1007/s001639870001
- [M] Suh (1999). https://doi.org/10.1007/PL00003883
- [M] Hazelrigg (1999). https://doi.org/10.1115/1.2829466
- [M] Dubois, Tate et al. (2012). https://doi.org/10.3233/jid-2012-0018
- [M] Kulak et al. (2005). https://doi.org/10.1016/j.jmatprotec.2005.03.030
- [M] Independence axiom and QFD (1994). https://doi.org/10.1115/detc1994-0007
- [V] Independence Measure / IPN (2015), abstract. https://doi.org/10.1115/imece2015-50553
- [M] Mobile-phone ergonomics, information axiom (2006). https://doi.org/10.1142/9789812774118_0051
- [V] OpenAlex citation count for Hirschi and Frey. https://openalex.org/W2145964432
- [V] Wikipedia, Axiomatic design. https://en.wikipedia.org/wiki/Axiomatic_design

**Advocacy and application papers**
- [V] Homay (2026), Deep Dive into AD Part I. https://arxiv.org/abs/2605.25735
- [V] Homay (2025), Complexity and Coupling. https://arxiv.org/abs/2507.09599
- [V] Homay (2025), The Mythical Good Software. https://arxiv.org/pdf/2507.09596
- [V] Homay (2025), Defining design in industrial control. https://arxiv.org/pdf/2507.09594
- [V] Yoong et al. (2020), SWaT invariants. https://arxiv.org/abs/2007.03651
- [V] Sandhu et al. (2024). https://arxiv.org/abs/2401.16750 ; (2025). https://arxiv.org/abs/2503.02912
- [V] Panarotto, Brahma, Isaksson (2023). https://research.chalmers.se/publication/542070/file/542070_Fulltext.pdf
- [V] Khayal and Farid (2019). https://arxiv.org/abs/1910.09104
- [V] Sun et al. (2026), functional decomposition for set-based design. https://doi.org/10.1017/dsj.2026.10053
- [M] Li, Suh, Xu, Song (2022), Extenics AD. https://doi.org/10.1017/s0890060422000075

**LLM and AI studies**
- [V] Giordano et al. (2025), Decoding the grammar of design theory. https://doi.org/10.1017/pds.2025.10126
- [M] Consoloni et al. (2026), SSRN. https://doi.org/10.2139/ssrn.6835336
- [M] Akay and Kim (2020). https://doi.org/10.1016/j.procir.2020.02.210
- [M] Akay, Yang, Kim (2021). https://doi.org/10.1115/detc2021-66898
- [V] AssemCAD (Dong et al. 2026). https://arxiv.org/abs/2607.05123
- [V] Auto-DSM. https://arxiv.org/abs/2312.04134
- [V] Jiang, Xie, Luo (2024/25). https://arxiv.org/abs/2411.12571
- [M] Jiang, Xie, Luo (2026) journal version. https://doi.org/10.1007/s00163-026-00494-0
- [V] Jiang and Luo (2026), DSM modularization. https://arxiv.org/abs/2604.28018
- [V] Jadhav and Barati Farimani (2025), truss agent. https://arxiv.org/abs/2404.17525
- [V] Garcia Alarcia and Golkar (2024). https://arxiv.org/abs/2410.00749
- [V] Joshi, Shukla, Gandhi (2026), abstract via Crossref (full text blocked; earlier snippet c22). https://doi.org/10.2139/ssrn.7341198
- [V] RM-ODP, LLMs and DSM migration. https://arxiv.org/abs/2608.23146
- [V] O'Hara (2025), agentic architecture mediation. https://doi.org/10.36227/techrxiv.176583345.56962463/v1
- [V] Ataei et al. (2025), Elicitron, abstract. https://doi.org/10.1115/1.4067388
- [M] Lee et al. (2025), reasoning abilities of LLMs. https://doi.org/10.1145/3712701

**False friends and search records**
- [V] Qiang et al. (2026), building ontologies. https://arxiv.org/abs/2603.14374
- [V] arXiv search record. https://arxiv.org/search/?query=%22axiomatic+design%22&searchtype=all
- [M] Crossref search record. https://api.crossref.org/works?query.bibliographic=axiomatic+design+large+language+model
