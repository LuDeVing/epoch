# Candidate inferences: deep document

*Subfield C10.03 of analogy engines. Written from evidence_a-d.jsonl, claims.jsonl (K01-K21) and critique.md in this folder. Evidence ids (a01, b02, c12, d04 ...) point to those files. Schema part: O7 (map an analogue, then test). Search limits: web search quota ran out early; arXiv full texts were opened directly. Absence of a study means "not found here", not "does not exist".*

## 1. What it is

An analogy maps a base (a case we know) onto a target (the case we are working on). Some base facts have a partner in the target. Some do not. A candidate inference is a base fact that has no target partner yet, but is tied to the matched structure. The mapping says: "this might hold in the target too." It is a surmise, not a fact.

Three points define the idea.
- It is projected, not derived. The base fact is rewritten with target entities swapped in (a01).
- It is structurally grounded. It must connect to something that was matched. An isolated base fact is not a candidate (a01, a08).
- It can be false. Gentner and Markman state that candidate inferences are only guesses (b04). Falkenhainer's own output held a false item ("solid alcohol") and an invented object in one run (a02).

For our agent this is the transfer step of O7. The agent has a solved source problem and a new target. It carries a step across. The research says the carried step must be labelled a hypothesis and tested before it is adopted. No LLM study we found measures this step directly (K17, c26, d18). The strongest evidence is human work from 1991-2003 and a symbolic model from 1988-2012. LLM studies mostly test whether a model picks or maps the right analogue, not whether the projected step is true.

## 2. History and theories in depth

### 2.1 Falkenhainer 1988 (PHINEAS thesis) [a01-a07]
- Definition: candidate inference CI = M(I_B). Base information I_B is passed through the mapping function M. Entities in the base are replaced by their target partners.
- Two conditions: consistent with the substitutions of the mapping, and structurally grounded (a01).
- Three states (a03):
  1. Candidate: proposed by the mapping. Need not be usable. May need heavy adaptation.
  2. Usable: operational. No contradiction with the target, no unknown objects.
  3. Useful or adopted: tested by further problem solving and found satisfactory.
- Skolem entities (a02): if a candidate inference names a base entity with no target partner, the engine invents a hypothetical target entity written as a function of the base entity. Worked case: dissolving mapped to evaporation. Output held (:skolem water1) and the false (Solid alcohol1). Neither was usable until repaired.
- Repair in two phases (a04). Probe: look for an alternative in what is already derivable or assumable from target knowledge. Resolve: go beyond current knowledge, such as hypothesise a new object or predicate. If neither works, reject the analogy. Transfer may branch into several (mapping, inference) pairs.
- Validity problem (a05): "Not all candidate inferences are real inferences." A different retrieved target description might already contain the fact. Four ways to raise validity: representation, access, mapping, verification.
- Results (a06): about six physics examples (liquid flow to heat flow, dissolving to evaporation, spring-mass to LC circuit). The LC case needed a hint and tailoring. Verification by planned experiments was finished for only one example. So the model is a demonstration, not a tested success rate.

### 2.2 Falkenhainer 1990, map-and-analyze [a07]
Each candidate inference is checked in order: is it already known (ask); is there a functional analogue already believed; if not, is it consistent (abductive-ask) so it can be assumed; else look for a way to explain it. Some candidates are true facts that were simply not explicit in the target.

### 2.3 SME and the candidate inference rule [a08-a10, c25]
Falkenhainer, Forbus and Gentner (1989) built the Structure-Mapping Engine. It aligns base and target. Relations must match identically. Entities may differ. Every base predicate that belongs to the aligned structure but is missing from the target becomes a candidate inference. (c25 was not opened; the 1997 chapter a08 was.)
- Example: ATTRACTS(Sun, planet) can map to ATTRACTS(magnet, nail), never to COMPOSED-OF(nail, iron) (a08).
- Kepler case (a09): SME's inferences resembled what Kepler appears to have inferred (the force travels from Sun to planet). One inference clashed with Kepler's belief that light is instantaneous.
- Authors' caution (a10): not all SME inferences are correct. Semantic and pragmatic constraints are needed after mapping. Large restructuring from one analogy is rare and risky. Faraday's iron-filing model was overly concrete and partly wrong.

### 2.4 Human systematicity studies [b01-b05, b10]
Clement and Gentner (1991) showed that people choose candidate inferences by connected causal structure. Gentner and Markman (1997) summarised the principle: inference flows from the more systematic base to the less coherent target (b05). Lassaline (1996), Spellman and Holyoak (1996) and Markman (1997) are cited as convergent but were not read (b10).

### 2.5 Transfer in practice: Gick and Holyoak, Gentner et al. [b06-b09, d02]
Gick and Holyoak (1980, 1983): people rarely notice a useful analogue unaided, and a hint raises use. The 1980 numbers were not opened. The 1983 Exp 2 rates are known from a quote in a 2025 paper (d02). Gentner, Loewenstein and Thompson (2003) showed that comparing two cases produces transfer that studying them apart does not.

### 2.6 Cognitive-model era: transfer then test [a11-a13]
Klenk and Forbus (2009) built domain transfer via analogy (DTA). It maps worked examples from a known domain to a new one, then maps the domain theories to get conjectures. Loop: accept the transferred knowledge if the problem is solved correctly, otherwise forget it (a11). Friedman, Barbella and Forbus (2012) used analogy to revise a misconception and logged both useful and spurious candidate inferences (a13).

### 2.7 LLM era (see section 6)
2023 onward: Webb, Holyoak and Lu (c01, c02) claimed emergent analogy in GPT-3. Hodel and West, then Lewis and Mitchell, challenged it (c03, c04). Yasunaga (2024) and Yu (2024) turned analogy into prompting recipes (c09, c14). Qin (2025) tested whether relevance matters (c12). 2026 work adds code-side mapping (YARN, c19) and a creative-transfer study (Shen, c22).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A candidate inference must be consistent with the mapping and structurally grounded | Formal definition CI = M(I_B) | Falkenhainer 1988 (a01) | Established (definition) |
| Raw SME-style output contains false and invented items | "Solid alcohol1" false; (:skolem water1) invented, same run | Falkenhainer 1988 (a02) | Established (one worked case) |
| Three states: candidate, usable, adopted-after-testing | No numbers | a03, a07, a11 | Established |
| Cross-domain transfer loop: accept only if the problem is then solved | Exp 1: 120 of 120 transfer attempts succeeded; 72 (60%) needed an extra retrieval | Klenk and Forbus 2009 (a11, a12) | Single model, clean domain |
| Analogy learner beat a step-by-step baseline early | Exp 2 problem 2: 60% vs 40%; problem 3: 90% vs 80%; both 100% on 4 and 5 | Klenk and Forbus 2009 (a12) | Single model |
| Simulated learner: analogy gave many spurious candidates | Best mapping gave 30 candidate inferences, some spurious (Earth has beef); six trials | Friedman et al. 2012 (a13) | Single model |
| People choose shared-causal-system facts (selection) | Exp 1 N=48: 3.17 vs 2.0 of 4 shared-system choices, F(1,44)=18.43, p<.001 | Clement and Gentner 1991 (b01) | Established |
| People predict the connected base fact | Exp 2 N=32: shared-system .53 vs .12 different-system (analogy); target-only .12 vs .12 | Clement and Gentner 1991 (b02) | Established |
| Same, Exp 3 | N=48: analogy shared .53, different-system .22; target-only mostly "other" (.62 to .96) | Clement and Gentner 1991 (b03) | Established |
| Comparison of two cases beats separate study | Exp 2 N=128: 48% vs 19%, chi2(1)=11.85, p<.01; linked cases 98% vs 16% | Gentner et al. 2003 (b06) | Established |
| Guided analogy beats no training | Exp 1 N=48: 15/32 (47%) vs 6% baseline, chi2=7.92 | Gentner et al. 2003 (b06) | Established |
| Graded transfer in live negotiation | Exp 3 N=158: contingent contracts 90% guided, 70% comparison, 55% separate, 37% baseline | Gentner et al. 2003 (b07) | Established |
| Case-comparison meta-analysis | 57 experiments (336 tests): d=.60, CI .47-.72, Q(56)=136.74, I2=59% (2011 abstract). Published d=.50 by snippet only | Alfieri et al. (d01, b09) | Established as "medium, about .5 to .6"; exact d unverified |
| Spontaneous analogue use is rare; a hint helps | Gick and Holyoak 1983 Exp 2: 29% (8/28) no hint, 50% (14/28) hint; HR problem 20.3% vs 37% (17/46); factory 6.3% vs 8.7% (4/46) | d02, c20 | Single-source for 1983 numbers (quoted) |
| Alignment focuses memory on aligned structure | Alignable recall m=2.35; incorrect recall 0.64 nonalignable vs 0.40; t(19)=3.79; 36 people | Markman and Gentner 1997 (a14) | Single-source |
| GPT-3 text matrices vs humans | N=40; generative OR=1.88 (CI 1.21-2.91, p=0.005); MC OR=6.27; item r(30)=0.39 | Webb et al. 2023 (c01) | Contested (training overlap) |
| GPT-3 on stories: humans win | Humans N=54; OR=0.37 p=0.0003; near p=0.0039; far p=0.065 (ns); 15/54 humans perfect | Webb et al. 2023 (c02, a15) | Established for GPT-3 |
| Counterfactual letter strings (accuracy) | Humans .753; GPT-3 .488; GPT-3.5 .350; GPT-4 .452 (1,876 human samples, 6,840 per model) | Lewis and Mitchell 2024 (b13) | Contested |
| Synthetic alphabet, GPT-3 | Below 0.1 on three variants; N=50 per condition | Hodel and West (c03, b15) | Contested; GPT-3 only |
| Counting explanation | GPT-4 with code vs humans: P=0.496 (no gap); 46% (23/50) of GPT-4 errors used a valid alternative rule vs 39% of human errors | Webb et al. 2024 (c05, a19) | Contested (authors' own rebuttal) |
| Order bias, story analogies (18 far problems) | GPT-4 correct-first 0.89 vs second 0.61 (Webb data); 1.0 vs 0.72 (their run); humans 0.78 vs 0.78 | Lewis and Mitchell 2025 (d15) | Single-source |
| Paraphrase hurts GPT-4 more | GPT-4 0.86 to 0.72; humans 0.78 to 0.70 | Lewis and Mitchell 2025 (d15, a20) | Single-source; gap not shown significant |
| Models over-trust a misleading source | Random Finals: humans fall about 0.5; GPT-4 falls 0.8 | Musker et al. 2025 (c08) | Single-source |
| Permuted pairs hurt models, not humans | Coefficients: Claude 3 -1.78, GPT-4 -1.68, Llama-405B -2.34, all p<.001 | Musker et al. (c07) | Single-source |
| ARN: far analogies fail | Humans 94.1-96.8% far; all-model far mean 39.6% = mean of far/far 45.3 and far/near-distractor 33.9; GPT-4 57.1 and 29.1; near: models 75.0%, humans 97.9% | Sourati et al. 2024 (d09, c18) | Established for 2023-24 models |
| 2026 frontier on ARN ranking | GPT-5.2, Claude Opus 4.5: MAP about 0.82, MRR 0.91; Llama 1B/8B about 0.35 | McGovern et al. 2026 (d10) | Single-source; far cell not split |
| StoryAnalogy picking | Humans 85.7%; ChatGPT 29-36%; text-davinci-003 37.1%; chance 25% | Jiayang et al. 2023 (b21, a27) | Established for older models |
| AnaloBench: length kills it | 1/10/30-sentence stories: GPT-3.5 71.8/51.2/31.5; humans 89.1/66.5/60.7; chance 25% | Ye et al. 2024 (c17, d17) | Established for older models |
| SCAR scientific mapping | GPT-4 about 65-69% (up to 77.17% with 1-shot plus background); ChatGPT 57.9-62.1; humans 85.9-88.5 (2 students) | Yuan et al. 2023 (c16) | Single-source |
| Analogical prompting (self-made exemplars) | GSM8K GPT-3.5 76.7 to 77.8; davinci-003 54.0 to 61.0; MATH 34.9 to 37.3; avg +4% | Yasunaga et al. 2024 (c09, a23) | Single-source |
| Number of exemplars | K=1: 76.1/34.8; K=3: 77.5/37.3; K=5: 77.8/37.1 (GSM8K/MATH) | Yasunaga (d03) | Single-source |
| Codeforces | 3-shot CoT 13%/25% (GPT-3.5), 17%/32% (GPT-4); ours 15%/29% and 19%/37% | Yasunaga (c11) | Single-source |
| How often self-made sources are wrong | Of 100 checked: 50 correct answers (6 irrelevant exemplar, 9 relevant but wrong solution, 35 relevant and right); 50 wrong answers (10 irrelevant, 12 relevant but wrong solution, 28 relevant and right but model still failed) | Yasunaga (d04) | Single-source (GPT-3.5) |
| Relevance not needed on maths | GSM8K/MATH: relevant 71.5/33.3; no-type 75.5/36.1; random-same 75.1/36.3; random-different 76.3/34.1 | Qin et al. 2025 (c12) | Contested vs Yasunaga |
| Example accuracy drives scores | MATH example accuracy: relevant 62%, none 72%, random-same 86% (n=50 each) | Qin (c13, d06) | Single-source |
| Qin on stronger model and BBH | GPT-4o-mini GSM8K: relevant 90.7, random-bio 93.2, ICL-math 94.2; BBH: relevant 63.2 vs 61.9 | Qin (d07) | Task-dependent |
| Thought Propagation (analogous subproblems) | Optimal rate: GPT-3.5 IO .33 to TP .65; GPT-4 .78 to .88; PaLM-2 .14 to .36 (CoT .24); ToT: .22 / .46 | Yu et al. 2024 (c14, d08) | Single-source |
| TP on ALFWorld | 134 environments; ReAct 57, best-of-6 71, Reflexion 79.1, TP 83.68-94.78; abstract +15% | Yu et al. (b19, c15) | Single-source |
| Matching, not recall, is weak | GPT-4 no hint: 1/15 used radiation story; hint: 15/15 used an analogy, precision .50-.52, recall 1.00; humans precision .67-.75, recall .26-.39 | Puranam et al. 2025 (d16, c20) | Single-source, n=15 per cell |
| Code-side mapping over LLM abstractions | MCQ chance .25: Qwen LLM-only .41 to YARN .46; Llama .28 to .45; unabstracted mapping .17; ARN far: Qwen .52 vs YARN .47, Llama .42 vs .46 | Khojasteh et al. 2026 (d12, c19) | Single-source |
| Reasoning models still brittle on Raven-type | o3-mini 86.6% to 17.0%; R1 80.6% to 23.2%; neuro-symbolic 98.6% to 88.0%; chance 12.5% | Camposampiero et al. 2025 (d11) | Single-source |
| Structure as text helps | GPT-3 Center 77.2%; 3x3Grid 86.4 to 93.2% with decomposition | Hu et al. 2023 (a22, c21) | Established (2 sources) |
| Analogy-guided generation: more novel, less valid | Binary novelty Claude 1.6/21.6/50.4%; GPT 8.8/27.2/58.8%; Gemini 8.6/37.9/68.8%. Humans: AR more novel 78% of 50 pairs, reasonable 67% vs 86% | Shen et al. 2026 (d13, d14) | Single-source |

## 4. Mechanisms and models

This section is written so an engineer can build it.

### 4.1 Data structures
- Case: a list of typed facts. Each fact is `(relation, arg1, arg2, ...)`. Relations of order 1 (attributes), 2 (relations), higher (causes, enables, implies).
- Mapping: a one-to-one dict from base entities to target entities, plus a score.
- Candidate inference record: `{fact, source_support[], status, test, result}`. Status is one of proposed, usable, adopted, rejected.

### 4.2 The SME-style procedure (a01, a08)
1. Build base and target fact lists (the LLM can extract them; code stores them).
2. Find local matches: pairs of facts with identical relation names (entities may differ).
3. Combine matches into kernels that keep one-to-one consistency (an entity maps to at most one partner).
4. Score kernels. Higher-order relations that tie many facts together score more (systematicity). This is what Clement and Gentner found in people (b01-b03).
5. For the best mapping, take every base fact that is not matched but shares an argument or parent with a matched fact. Substitute entities. That is the candidate set.
6. A base entity with no partner becomes a skolem placeholder (a02).

### 4.3 Validation ladder (a03, a04, a07)
For each candidate, run in order:
1. Already known in the target? Then it is not new. Drop it (confirmation only).
2. Contradicts the target? Reject.
3. Has a functional analogue the target already believes? Replace with that.
4. Has skolem entities? Probe (look for an existing target entity that fits). If none, resolve (propose a new entity, flag as a conjecture). If neither works, reject.
5. Consistent but unknown? Mark usable. Assume only as a hypothesis.
6. Test by problem solving (a11): use it in the solve, run the check, adopt only if the check passes. Otherwise forget it.

### 4.4 Test-then-keep loop (Klenk and Forbus 2009, a11)
Transfer, solve a problem with the transferred knowledge, compare to the correct result, keep if correct, forget if not. In Exp 1 all 120 attempts succeeded after transfer. This was a clean symbolic domain.

### 4.5 LLM versions of the same ideas
- Self-generated exemplars (c09): prompt the model to recall K=3 to 5 related solved problems, then solve. No explicit mapping, no test. A weak form of candidate inference (the solution method is the candidate).
- Solve analogous problems and aggregate (c14): generate neighbour problems, solve each, then use their solutions to fix the first answer. The aggregation module acts as a weak check.
- Code-side one-to-one mapping (c19, d12): the LLM extracts event units and abstractions. Code does the greedy one-to-one mapping. Mapping without abstraction is below chance (.17 vs chance .25), with abstraction .45-.46.
- Structured text encoding (a22): name attributes with ordinal numbers, decompose into separate prompts. This lifted GPT-3 from 28.2% (quasi-image) and 51.8% (random names) to 77.2% on Raven Center.
- Two-source comparison (b06): put two aligned solved cases in context and ask for their common principle before transfer. Not yet tested on LLMs.

### 4.6 Why the human selection rule works
People prefer the base fact connected by causal links to the matched part (b01-b03, 53% vs 12%). The rule: carry a step only if it sits in the same causal chain as something already matched. This is cheap to check in code if facts are typed. It is a filter on what to propose, not a test of truth.

## 5. What holds up

### 5.1 Replications and consistency
- Clement and Gentner: three experiments; selection (Exp 1) and prediction (Exp 2, Exp 3) point the same way (b01-b03). Convergent human work is cited by Gentner and Markman (b10) but unread.
- Comparison beats separate study: Gentner et al. found it in a lab task (48% vs 19%) and in negotiation (90% vs 55%). The meta-analysis (57 experiments) gives about d=.5 to .6, heterogeneous (I2=59%) (d01).
- Spontaneous analogue use is low and a hint helps: Gick and Holyoak 1983 (29% to 50%), and a 2025 rerun shows the same direction (HR 20.3% to 37%) (d02).
- Far analogies are hard for LLMs: ARN, StoryAnalogy, AnaloBench and Webb's own far condition (p=0.065) agree (K06).

### 5.2 Failures and contested results
- Webb et al. 2023 (GPT-3 matches people) was challenged by Hodel and West (GPT-3 below 0.1 on variants) and by Lewis and Mitchell (GPT-4 .452 vs humans .753). Webb et al. 2024 answered that the problem is counting: GPT-4 with code reached human level (P=0.496). The data fit both stories (K08, K09). Nobody tested a reasoning-trained model on letter strings.
- Yasunaga's relevance story: Qin et al. tested it on GPT-3.5 and found irrelevant or random self-made examples did as well or better on maths (GSM8K/MATH 75.5/36.1 no-type vs 71.5/33.3 relevant). The cause is example accuracy (62% vs 72% vs 86%). It holds for GPT-4o-mini on GSM8K but fails on BBH (relevant 63.2 vs 61.9). Yasunaga's own gain is small (+1.1 on GSM8K for GPT-3.5, near noise level) (K11, K12).
- The ARN "collapse" figure of 39.6% is a mean over models and two far cells. It includes a surface-similarity trap cell where picking the dissimilar story wins. Frontier 2026 models reach MAP 0.82 on a ranking version, so whether the collapse persists is open (K19).
- YARN is mixed: better on MCQ for both 8B models, better on far ARN for Llama, worse on far ARN for Qwen (0.47 vs 0.52) and on near ARN (0.69 vs CoT 0.79) (d12).
- Novelty is not validity: analogy-guided generation was judged "reasonable" 67% of the time vs 86% for a plain cross-domain baseline (d13).

### 5.3 Moderators
- Distance: near analogies work for models, far ones fail (ARN near 75.0 vs far 39.6).
- Length: AnaloBench accuracy falls from 71.8 to 31.5 (GPT-3.5, 1 to 30 sentences).
- Model size: self-generated exemplars help only above a size (davinci-002/003); small models prefer retrieved labelled examples (c10).
- Number of sources: K=1 worst, K=3 to 5 plateau (d03).
- Position: first-listed answer favoured (GPT-4 0.89 vs 0.61).
- Task: relevance helps on BBH, not on maths (d07).
- Distractors and surface similarity: people and models are drawn to surface match; models more so (b21).
- Hints: raise use in people (29% to 50%), and make GPT-4 always apply an analogy, about half the time the wrong one (d16).

### 5.4 Interventions that worked
- Comparing two aligned cases (humans): 48% vs 19%.
- Guidance on which cases to compare (humans): 90% vs 55% in negotiation.
- Test-then-keep in a cognitive model (a11).
- Text-structured relations in LLM matrices (a22).
- Solving neighbour problems then aggregating (GPT-3.5 .33 to .65 optimal rate).
- Code-side mapping on top of LLM abstractions for 8B models on MCQ (.28 to .45).
- Code execution for counting-bound analogies (c05).
- Verified or corrected exemplars: GPT-4-corrected examples beat uncorrected in every cell (c13).

### 5.5 Interventions that did not work, or are unproven
- Relevance prompting on maths (c12).
- K=1 self-made source (worse than several).
- More reasoning tokens on hard Raven variants (o3-mini flat; up to 31.0% at 53,596 reasoning tokens) (d11).
- Two-layer propagation (marginal gain over one layer at higher cost) (c14, d08).
- Hint alone (GPT-4 always applies; precision .50-.52) (d16).
- Mapping without abstraction (.17, below chance) (c19).

### 5.6 Gaps in this evidence
- Gick and Holyoak 1980 numbers, Lassaline and Spellman and Holyoak effects, and the published Alfieri d were never read.
- Thought Propagation and Yasunaga each have one source; no independent replication.
- Some 2026 entries come from abstract or skim (c23, c24).

## 6. Language models

### 6.1 Picking the analogue (not the same as projecting)
- GPT-3: story analogies worse than undergraduates (OR=0.37); far condition p=0.065 (c02).
- ChatGPT about 30% on 4-way multiple choice vs 85.7% for humans (b21). Chance 25%.
- ARN, GPT-4: 94.0 near/near, 57.1 far/far, 29.1 far/near-distractor, average 68.1, vs humans 96.0 (d09). Chain of thought and solved examples helped; the best few-shot run was still about halfway between chance and humans.
- AnaloBench: story length is the main killer (28.8 point human gap at 30 sentences vs 6.9 at 1 sentence) (c17).
- 2026 frontier models: MAP about 0.82 on ranking (d10). Not comparable to the 2023-24 binary far/near numbers.

### 6.2 Mapping
- SCAR scientific concept mapping: GPT-4 about 65-69% (77.17% best, one-shot plus background), humans 85.9-88.5% (c16).
- Letter-string and matrix counterfactuals: sharp drop for GPT-3/3.5/4; partly mechanical (counting), because code execution closes the gap (P=0.496) (K08, K09).
- Musker et al.: in default conditions GPT-4, Claude 3 and Llama-405B were not significantly worse than humans (p=0.097, 0.194, 0.097) but dropped under permuted pairs and distractors (c07).
- Reasoning models: o3-mini and R1 fall to 17.0% and 23.2% on I-RAVEN-X while a neuro-symbolic solver holds 88.0% (d11).

### 6.3 Projecting a step (the candidate-inference step)
- No direct test exists (K17). Proxies:
  - 21 of 100 checked GSM8K/MATH runs had a relevant exemplar with an incorrect solution (GPT-3.5) (d04).
  - GPT-4 given a hint applied the wrong analogue about half the time (precision .50-.52) (d16).
  - GPT-3 on the radiation problem: needed a prompt to consider earlier stories once distractors were added (b12). Single runs, no counts.
- Self-made exemplars: modest gains (+4% average; GSM8K +1.1 for GPT-3.5, +7.0 for davinci-003) and only for large enough models.
- Neighbour-problem propagation: strongest reported gain on shortest path (+32 points for GPT-3.5), but the analogues are built by the method, so it is closer to decomposition than far analogy (c14).
- Cross-domain creative transfer: novelty up a lot (Claude 1.6% to 50.4%), reasonableness down (67% vs 86%).

### 6.4 What changed performance, and by how much
| Change | Effect |
|---|---|
| Code execution (GPT-4, letter strings) | Closed gap to humans (P=0.496) |
| Text-structured relation encoding (GPT-3, Raven) | 28.2% / 51.8% to 77.2% |
| Ordinal attribute names plus decomposition | 86.4% to 93.2% (3x3Grid) |
| Solved examples plus CoT on ARN | Helped, not to human level |
| 1-shot plus background (SCAR, GPT-4) | 65-66% to 77.17% on one split |
| Code-side mapping over LLM abstraction | Llama MCQ .28 to .45 |
| Self-generated exemplars (K=3 to 5) | +1 to +7 points depending on model |
| Neighbour-problem aggregation | GPT-3.5 .33 to .65; GPT-4 .78 to .88 |
| Corrected (accurate) exemplars | Beat uncorrected in every Qin cell |
| More reasoning tokens (o3-mini, hard Raven) | Flat |

### 6.5 Competing explanations
1. Training-data similarity (Lewis and Mitchell, Hodel and West) against emergent abstraction with mechanical limits (Webb). Not resolved.
2. Relevance of recalled examples (Yasunaga) against accuracy of recalled examples (Qin). Task-dependent.
3. Retrieval failure against matching failure (Puranam: GPT-4 recalls well, matches badly).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)
1. **Label a transferred step as a candidate, not a fact (O7, G2, G3).** [E] Evidence: a01, a02, a05, a08, a10, b04, c25 (K01). The agent writes each carried step as "candidate: X, carried from source step Y". It is never reported as known.
2. **Three states for a carried step: proposed, usable, adopted (O7, S).** [E] Evidence: a03, a07, a11 (K02). Adoption needs a pass on something the answer was not fitted to (G3).
3. **Test after transfer, drop on fail (O7, G2).** [E] Evidence: a11, a12, a03 (K02). On failure, cite the failing output and forget the step. The support is a symbolic model; LLM evidence for the benefit at equal tokens is absent (see Test first, item 1 in section 8).
4. **Only carry steps that sit inside the matched causal chain (O7, code check).** [E] Evidence: b01, b02, b03, b04, b05 (K03). Code can enforce this when facts are typed. It filters what to propose. It does not prove truth.
5. **Do not assume unaided analogy happens; cue it (O7, S).** [E] for human data, [S] for LLM. Evidence: b08, d02, c20, d16 (K05). A cue to use earlier solved cases is needed, but a cue alone makes GPT-4 over-apply (precision .50-.52), so pair it with a match check.
6. **Make relations explicit before transfer (O7).** [E] Evidence: a17, a22, b25, c01, c21 (K14). List the relations as typed lines. Do not rely on free prose.
7. **Do not trust success on familiar surface forms (G3).** [C] but cheap to adopt. Evidence: b13, b15, c03, c04, d11 (K08, K21). Check any analogy result on a variant.
8. **Do not credit "analogy" for gains from recalled examples (G7).** [C] Evidence: c12, c13, d06, d07 (K12). Judge by accuracy against a plain arm at equal tokens.

### Test first (not yet established for LLMs)
1. **Two aligned sources, not one (S, O7).** Human [E] (b06, b07, d01); LLM: no test. Indirect: K=1 worst (d03). K04.
2. **Verify the match before transfer (O7).** [S] Evidence: d16, c20, b21, c19 (K07, K18). Wrong-source rate about 50% when hinted.
3. **Code-side one-to-one mapping check (O7, G5).** [S] Evidence: c19, d12, d11 (K15, K21). Mixed; helps weak models on some splits.
4. **Self-generated source plus accuracy check (O7).** [S] Evidence: c09, c11, d03, d04, c13 (K11, K12). Qin's two cheaper methods (generate once, verify) matched or beat the original at lower cost (ICL-math 56.3 vs 52.4).
5. **Solve neighbour problems and aggregate (O7, S).** [S] Evidence: c14, d08, b18, b19 (K13). Match against best-of-N at equal tokens.
6. **Shuffle source order and vote (G4, G5).** [S] Evidence: d15, a20, c08 (K10). Order bias is large in GPT-4; reasoning models untested.
7. **Executable test after far-domain transfer (G8).** [S] Evidence: d13, d14, c22 (K16, K20). Novelty is not validity.
8. **Skolem-style probe and resolve (O7).** [S], from a model only. Evidence: a02, a04 (K01). No LLM study.

## 8. Concrete tests on our bench

All arms get equal total tokens, including setup (G7). The bench has items with a known answer, so a carried step can be scored true or false by execution.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Target problem plus a solved source whose steps are partly valid, partly not (hand-built, 60 to 100 items; label each step true/false in the target) | A: transfer-and-trust. B: transfer, then test each step on a held-out example before use | Share of adopted steps later found false; final accuracy | Fewer false adopted steps in B; accuracy up if the test is cheap |
| T2 | Same items | A: one source. B: two aligned solved sources with a "state what they share" step | Accuracy; false carried steps | B better by a few points (human d about .5; LLM unknown) |
| T3 | Items with a surface-similar wrong source and a structure-similar right source (ARN far/near-distractor style) | A: plain "pick the best source". B: LLM extracts typed facts, code does one-to-one mapping and scores | Right-source rate | B better if the model is weak; may be null for frontier models (YARN mixed) |
| T4 | Maths and one non-maths set | A: no exemplar. B: self-made relevant exemplar. C: random self-made exemplar. D: self-made then checked | Accuracy | Replicates Qin if C >= B on maths; D best |
| T5 | Items with 3 candidate sources, order varied | A: one fixed order. B: 3 shuffled orders, vote in code | Accuracy; first-vs-second gap | B removes the order gap at the cost of a 3-sample vote |
| T6 | Items where a base entity has no target partner | A: carry as-is. B: probe-then-resolve prompt | Rate of invented but wrong entities adopted | B reduces them |
| T7 | Counterfactual variants of the agent's own analogy items | A: no code tool. B: code tool | Accuracy gap original vs variant | Smaller gap with code (counting-bound only) |
| T8 | Cross-domain solution generation | A: plain. B: analogy-guided. C: analogy-guided plus executable test | Pass rate by execution (G8); novelty by run | B more novel, lower pass rate; C recovers |
| T9 | Neighbour-problem propagation vs best-of-N | A: best-of-N. B: propagation, same tokens | Exact-match or optimal rate | B wins only if neighbours are real analogues |
| T10 | Cue arms | A: no cue. B: "use earlier cases". C: cue plus mapping check | Use rate; precision of use | B raises use, lowers precision; C keeps precision |

Report per arm: tokens, accuracy, false adopted steps, source-choice precision. Use at least 3 seeds. Call a result null if the gap is below the seed spread.

## 9. What does not transfer, and why
- **Human systematicity numbers (53% vs 12%).** Short passages, undergraduates. They show a selection rule, not a rate for LLMs. Use the rule, not the numbers.
- **Comparison effect (d about .5).** Learners compared cases in instruction settings. An LLM has both cases in context at once, so part of the benefit may already be there. Unknown.
- **Hint effect (29% to 50%).** Humans forget a source or fail to notice it. An LLM with the source in context does not forget; its problem is over-application (precision .50-.52).
- **SME's pure symbolic output.** It needs hand-coded predicate structure. Our agent starts from free text. The extraction step is error-prone, and YARN shows mapping without good abstraction is below chance.
- **PHINEAS repair.** It works on small expert-written physics domains with a knowledge base to probe. The agent has no explicit target knowledge base.
- **Klenk and Forbus 100% transfer success.** A clean symbolic domain with the correct theory in the system. Not comparable to open tasks.
- **Self-generated exemplar gains.** Small on strong models (+1 point GSM8K). They may not survive on reasoning models, where plain thinking already covers the same ground (G11).
- **Thought Propagation numbers.** The analogous problems are neighbour sub-problems of the same task. Closer to decomposition (O3) than to a far analogue.
- **Novelty gains.** Scored by LLM-based judges, and reasonableness fell. G8 forbids model-judged novelty as proof.
- **Letter-string and Raven results.** Narrow rule induction. The brittleness shows risk, not its size on real problems.

## 10. Open questions
1. How often is a step an LLM carries from a solved source to a new target false, and does test-before-adopt cut that at equal tokens? (No direct data.)
2. Does a code-side one-to-one mapping beat prompting for choosing which source steps to carry, at matched compute?
3. Do two aligned sources beat one for LLM transfer? Human: 48% vs 19%.
4. Does accuracy beat relevance as the driver for frontier and reasoning models, and on non-maths tasks?
5. Does the ARN far-with-near-distractor failure persist in 2025-2026 frontier models? (GPT-4: 29.1.)
6. Can an LLM detect and repair missing-entity candidates (skolem) as PHINEAS does?
7. Is order and paraphrase sensitivity present in reasoning-trained models, and does shuffle-and-vote remove it?
8. What are the exact Gick and Holyoak 1980 numbers, the published Alfieri d, and the Lassaline and Spellman and Holyoak effects?
9. Does the cross-domain novelty gain survive a blind expert correctness check?
10. Is brittleness training-data similarity or mechanical weakness? The data fit both.
11. Does the human "connected causal chain" preference predict which LLM-projected steps are correct?

## 11. Sources

[V] = opened this session (full text or PDF). [M] = snippet or memory only.

- [V] Falkenhainer (1988) PhD thesis, PHINEAS. https://www.qrg.northwestern.edu/papers/Files/Falkenhainer_PhD_Thesis_1988.pdf
- [V] Falkenhainer (1990) Analogy in Context (draft). Qualitative Reasoning Group, Northwestern.
- [M] Falkenhainer, Forbus, Gentner (1989) The structure-mapping engine. https://www.sciencedirect.com/science/article/pii/0004370289900776
- [V] Gentner, Brem, Ferguson, Markman, Levidow, Wolff, Forbus (1997) Analogical reasoning and conceptual change: a case study of Johannes Kepler.
- [V] Klenk and Forbus (2009) Domain transfer via cross-domain analogy. Cognitive Systems Research.
- [V] Friedman, Barbella, Forbus (2012) Revising domain knowledge with cross-domain analogy.
- [V] Markman and Gentner (1997) The effects of alignability on memory. Psychological Science.
- [V] Clement and Gentner (1991) Systematicity as a selection constraint in analogical mapping. Cognitive Science.
- [V] Gentner and Markman (1997) Structure mapping in analogy and similarity. American Psychologist.
- [V] Gentner, Loewenstein, Thompson (2003) Learning and transfer: a general role for analogical encoding. J. Educational Psychology.
- [M] Gick and Holyoak (1980, 1983). Known through quotes in Puranam et al. 2025 and Webb et al. 2023.
- [V, 2011 abstract only] Alfieri, Nokes, Schunn (2011 abstract of the 2013 meta-analysis). https://files.eric.ed.gov/fulltext/ED528947.pdf (published 2013 abstract: [M])
- [M] Lassaline (1996); Spellman and Holyoak (1996); Markman (1997). Cited by Gentner and Markman 1997.
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196
- [V] Hodel and West (2023/24) Response. https://arxiv.org/abs/2308.16118
- [V] Lewis and Mitchell (2024) Counterfactual tasks. https://arxiv.org/abs/2402.08955
- [V] Webb, Holyoak, Lu (2024) Evidence from counterfactual tasks. https://arxiv.org/abs/2404.13070
- [V] Lewis and Mitchell (2025) Robustness of analogical reasoning. https://arxiv.org/abs/2411.14215
- [V] Musker, Duchnowski, Milliere, Pavlick (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714
- [V] Qin et al. (2025) Relevant or random. https://arxiv.org/abs/2404.12728
- [V] Yu, He, Ying (2024) Thought propagation. https://arxiv.org/abs/2310.03965
- [V] Yuan et al. (2023) SCAR, Beneath surface similarity. https://arxiv.org/abs/2305.12660
- [V] Ye, Wang, Khashabi (2024) AnaloBench. https://arxiv.org/abs/2402.12370
- [V] Sourati, Ilievski, Sommerauer, Jiang (2024) ARN. https://arxiv.org/abs/2310.00996
- [V] Jiayang et al. (2023) StoryAnalogy (evidence a27, b21; url in evidence files).
- [V] Khojasteh et al. (2026) YARN. https://arxiv.org/abs/2603.29997
- [V] McGovern, Craig, Lippincott, Sirin (2026) When models know more than they say. https://arxiv.org/abs/2604.03877
- [V] Puranam, Sen, Workiewicz (2025) Can LLMs help improve analogical reasoning for strategic decisions? https://arxiv.org/abs/2505.00603
- [V] Hu, Storks, Lewis, Chai (2023) In-context analogical reasoning with pre-trained language models. https://arxiv.org/abs/2305.17626
- [V] Camposampiero et al. (2025) Can large reasoning models do analogical reasoning under perceptual uncertainty? https://arxiv.org/abs/2503.11207
- [V] Shen, Druckmann, Zou (2026) Unlocking LLM creativity in science through analogical reasoning. https://arxiv.org/abs/2605.11258
- [V, abstract and skim] Chang et al. (2025) BioSpark. https://arxiv.org/abs/2503.09838

Note: critique.md re-opened and confirmed the Webb 2023, Lewis and Mitchell 2024, Yasunaga, Yu and Qin numbers. ARN was rechecked in d09. Puranam, Clement and Gentner, Gentner et al. 2003, SCAR, AnaloBench, YARN and Shen rest on the earlier agents' reading and were not independently re-confirmed in the critique pass.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 7 established claims: 2 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C10.03-K03** (now single-source: the sources are not independent). All three experiments are one paper (Clement and Gentner 1991) and the review (Gentner and Markman 1997) only cites it; numbers (.53 vs .12, N=32; Exp 3 N=48) match, but this is a single study from one lab.
- **C10.03-K04** (number corrected). The 90% contract rate is the guided-analogy condition; the plain comparison condition formed 70% vs 55% for separate cases (Exp 3, N=158); 48% vs 19% (Exp 2, N=128) is correct. Corrected claim: Comparing two cases beats studying them separately for transfer (48% vs 19%, N=128); in live negotiations contingent contracts formed in 70% of comparison dyads vs 55% for separate cases (guided analogy 90%, baseline 37%; N=158). A meta-analytic effect of about d=0.5 to 0.6 (Alfieri et al.; SREE report d=.60) is not checked here.
- **C10.03-K06** (number corrected). 39.6% is the all-model average on ARN far analogies, not GPT-4; GPT-4 scored 57.1 and 29.1 on the two far partitions (about 43), and ARN used 2023 models. Corrected claim: Models in 2023 to 2024 tests find near story analogies but fail on far ones: on ARN the all-model average on far analogies is 39.6% (below the 50% chance level; GPT-4 about 43%) vs humans 94.1%; ChatGPT scored about 30% on StoryAnalogy multiple choice (humans over 85%); GPT-3 was above chance on near story analogies but not on far ones (p=0.065).
- **C10.03-K07** (reworded: the sources support less). Single study (Puranam et al. 2025, 60 GPT-4 runs, two source stories supplied); 'recall' there means using the relevant story when given, not retrieval from a bank; other listed sources do not separate recall from matching. Corrected claim: In one small study (Puranam et al. 2025; 60 GPT-4 runs, 199 students, two supplied source stories) GPT-4 almost never missed the relevant analogy but often applied the wrong one (high recall, low precision), while humans showed the reverse; this suggests matching may be a weak step but is untested at scale.
- **C10.03-K14** (reworded: the sources support less). Hu et al. say GPT-3 at 77.2% on Center is only 'nearing' human performance; beating humans holds for the 2x2Grid and 3x3Grid sub-tasks (93.2% with decomposition), and for Webb et al.'s digit matrices. Corrected claim: Re-encoding Raven-style matrices as text lets GPT-3 reach 77.2% on the Center sub-task (nearing human performance) and exceed human performance on the 2x2Grid and 3x3Grid sub-tasks (3x3Grid 93.2% with attribute naming and decomposition); GPT-3 also beat the human average on Webb et al.'s text digit-matrix task, so explicit structure aids inference.
