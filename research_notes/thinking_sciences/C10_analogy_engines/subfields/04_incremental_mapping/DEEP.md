# Incremental mapping: deep document

*Subfield C10.04. Written 2026-11-03 from evidence_a-d.jsonl (92 lines), claims.jsonl (K01-K31) and critique.md in this folder. Evidence ids (a01, b05, c12, d03 ...) point to those files. Status words follow claims.jsonl: established, single-source, contested, open.*

**Honest summary first.** The core of this subfield is one 1994 paper (Forbus, Ferguson, Gentner, I-SME) plus one human result that is quoted second-hand (Keane's order effect). No replication of that order effect was found. No study found tests incremental analogical mapping in a language model directly. Everything we know about LLMs comes from near neighbours: multi-turn degradation, premise order, belief revision, sycophancy and self-correction. Those neighbours are strong and consistent. The direct test is the gap our bench can fill. Search was tool-limited (Semantic Scholar, OpenAlex and arXiv API returned HTTP 429, WebSearch budget spent), so "not found" is not "does not exist".

Sibling subfields (not covered here, only linked): 01 structure mapping, 02 systematicity, 03 candidate inferences, 05 analogical retrieval (MAC/FAC), 06 multiconstraint theory. Parallel-run subfields that overlap: Connectionist and hybrid mapping models; Analogical problem solving; Dynamic memory, early CBR; Failure-driven CBR; Map versus value replay; Learned refinement and self-verification; Self-explanation.

---

## 1. What it is

Incremental mapping means building an analogy in steps. Facts about the base (the known case) and the target (the new case) do not all arrive at once. The mapper keeps a current best mapping, then extends it when new facts arrive. Sometimes it must throw the mapping away and rebuild it (remap).

In plain terms for our agent: at S6 (impasse) the agent may take an analogue (operator O7) and map it onto the problem. Over several rounds it learns new facts about the problem, new facts about the analogue, or a failing output that contradicts part of the mapping. The question is: extend the stored mapping, patch it, or rebuild it from scratch?

Two things make this hard:
- **Early choices mislead later steps.** A greedy early match can lock in a wrong pairing (c04).
- **The cost of rebuilding vs the cost of being wrong.** I-SME does not decide when to remap. It only reports how much of the possible structure the current mappings hold (a03, c02).

Where it sits in the schema: S6 across rounds, plus the memory slot that holds the mapping between rounds.

---

## 2. History and theories in depth

### 2.1 Lineage (all second-hand except I-SME itself; a10, b25, c07, c08)

- **Burstein (1986)** first modelled incremental analogical learning. Original not opened.
- **Falkenhainer (1987, 1990), PHINEAS.** A "map and analyze" cycle (a09, opened): make a cheap initial mapping with SME; analyse unmatched parts using domain theory only where impasses arise; re-examine the mapping (extend or shift); repeat until it cannot be extended. Candidate inferences are checked in order: already known; functional analogue believed; assume if consistent (abductive check); else seek consistent analogues. Key rule: the consistency of N assumptions must be tested jointly, not one by one. Draft paper; examples implemented, not benchmarked on humans.
- **Keane and Brayshaw (1988), IAM (Incremental Analogy Machine).** The first general incremental matcher. Fully serial: even local match decisions come one at a time, and trying alternatives needs backtracking (b04, c07). Designed as a cognitive model with limited working memory.
- **Hummel and Holyoak (1992).** An incremental scheme. Per Forbus et al. it cannot handle higher-order relations (a10).
- **Holyoak and Thagard ACME (1989).** Parallel constraint satisfaction, rival design (b04).
- **Forbus, Ferguson, Gentner (1994), I-SME.** SME made incremental. Our main source (a01-a05, opened).
- **Keane, Ledgeway, Duff (1994), Cognitive Science 18.** Two human experiments: more similar elements across domains cut time to the right mapping, and presentation order changed difficulty. Only serial IAM predicted both. Seen only through an abstract summary (c06). The publisher page returned 403.
- **Lovett, Gentner, Forbus, Sagi (2006, 2009).** Time-course simulations: incremental encoding plus SME explains early feature-based and later relation-based same/different judgments (a11, a13, b08, b09).
- **Kandaswamy, Forbus, Gentner (2014).** Progressive alignment with interim generalizations (b07, d09).
- **Forbus, Ferguson, Lovett, Gentner (2016).** Journal successor "Extending SME to handle large-scale cognitive modeling". The PDF was an image-only scan and could not be read (a21 in the evidence file). No numbers from it.
- **Lovett and Forbus (2017).** SME-based Raven's model (a14).

### 2.2 The I-SME design (a01-a05)

I-SME accepts base and target facts all at once, one at a time, or in any mix. Given everything at once, its output equals batch SME. Cost is no higher than SME: the greedy merge is linear in the number of kernels; kernels are between log and linear in the match-hypothesis network; the network is between linear and quadratic in description size. Timings on a 1994 PowerBook 165c: toy example 0.5 s, qualitative physics about 2 s, two stories of 67 and 52 expressions 34 s.

Design argument (a04, b04): local match building and kernel building run in parallel; only the final merge is serial and capacity-limited. The authors offer this as an account of "More is Less" (Gentner and Rattermann 1991): extra shared structure speeds and improves mapping because it produces fewer, larger kernels. This was argued, not tested.

### 2.3 What the human data show

- **Order effect (Keane).** Mapping facts delivered one at a time with the singleton items last: mean solve time 363.1 s, against 178.0 s when singletons came first. About twice as slow (a06, b02, c03). Second-hand: Keane's paper was "in press" in the I-SME paper and was never opened by us. Subject N unknown. The authors themselves doubt the task tests analogy, since it has no higher-order structure.
- **Time-course of similarity (Goldstone and Medin 1994, via Lovett et al.).** At a 1 s deadline, shared attributes raised false "same" answers whether or not they fit the best alignment (matches in place and out of place raised errors equally). At 1.84 and 2.68 s, cross-mapped matches lost most of their effect, and one in-place match outweighed two out-of-place matches (a11, a23, b08). Second-hand descriptions.
- **Sloutsky and Yarlas.** With the base shown 150 ms vs 2100 ms, relation-only changes were missed far more than attribute changes. Unpublished at the time, d-prime values not read (a12).
- **Gentner and Sagi shield study.** "Different" took 1380 ms for high-similarity pairs vs 880 ms for low-similarity (b09). A second report gives 1270 vs 910 ms (d10). The two reports disagree on the numbers; unresolved.
- **Progressive alignment (Kotovsky and Gentner 1996, via Kandaswamy 2014).** Children learn relational matches over a few trials when close, highly alignable pairs come first. Age 4 was below chance except on the easiest same-dimension, same-polarity triads (b06). Second-hand.

---

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| I-SME with all facts at once equals batch SME, no extra asymptotic cost | merge linear in kernels; 34 s for stories of 67 and 52 expressions on a 1994 PowerBook | Forbus et al. 1994 (a01, b01, c01) | single-source (K01) |
| I-SME keeps n global mappings within p% of best and reports fraction of possible structure matched | no accuracy data | a02, a03, c02 | single-source (K02) |
| Fact order changes difficulty: singleton-last doubles human time | 178.0 s vs 363.1 s (human, second-hand); I-SME remaps 1.5 vs 3.0 (two example sets, no fit stats) | Keane via Forbus et al. 1994 (a06, a07, b02, c02, c03) | single-source, no replication found (K03, K31) |
| Without the identical-functions filter, MARS matched enthalpy to temperature and gave a wrong answer | 1 worked problem; 5 extensions; 16 steps; correct answer Q = 621.22 kW | Forbus et al. 1994 (a05, a08, b03, c04) | single-source (K07) |
| Early matches follow surface features; relations arrive later | Deadlines 1, 1.84, 2.68 s; 150 vs 2100 ms base exposure | Goldstone and Medin; Sloutsky and Yarlas; Lovett et al. 2006, 2009 | established (K04), all second-hand human numbers |
| Incremental SME-based Raven's model | 56/60 on Standard Progressive Matrices (75th percentile); 54/60 adult = 61st; earlier model 50/60 (41st); sections A-C 12/12, D 10/12, E 10/12 | Lovett and Forbus 2017 (a14) | single-source (K05) |
| Close-to-far curriculum helps relational learning (model) | model 100% on same-dimension triads vs children 68%; 2 simulations of 16 triads | Kandaswamy et al. 2014 (b07, d09) | single-source for LLMs: none (K06) |
| Candidate inferences must be checked jointly | no numbers | Falkenhainer 1990 (a09) | single-source (K08) |
| GPT-3 vs undergrads, one-shot analogy | Digit matrices (human N=40): OR 1.88, p=0.005 (generation), OR 6.27, p=2.3e-8 (MC). Letter strings (N=57): OR 1.76, p=6.3e-5 overall; p=0.0007 on zero-generalization subset. Story analogies (N=54): OR 0.37, p=0.0003 (humans better) | Webb et al. 2023 (a15, b10, a24) | single-source (K09) |
| Counterfactual letter strings: LLMs fall, humans do not | Accuracy humans 0.753 (1,876 samples); GPT-3 0.350, GPT-3.5 0.452, GPT-4 0.488 (6,840 each) | Lewis and Mitchell 2024 (a16, b11) | contested (K10) |
| Rebuttal to the above | 46% (23/50) of GPT-4 errors used a valid alternative rule vs 39% of human errors; GPT-4 with code execution near human level | Webb et al. 2024 (b12) | contested |
| Digit matrices: blank moved | GPT-4 0.813 original, 0.480 alt-blank, 0.790 symbols; humans roughly level | Lewis and Mitchell 2024b (b13) | single-source |
| Story analogy option order and paraphrase | GPT-4 0.89 (16/18) correct-first vs 0.61 (11/18) second; 0.86 (31/36) vs 0.72 (26/36) paraphrased; humans 0.78 both orders | b14 | single-source (K11) |
| Symbol-set transfer fails | Latin/Greek/Symbol: adults 0.88/0.91/0.89; GPT-4o 0.85/0.63/0.48; Claude-3.5 0.68/0.62/0.46; Llama-3.1 405B 0.79/0.74/0.27; Gemma-2 27B 0.60/0.39/0.14; children 7-9 y 0.62/0.66/0.67 | Stevenson et al. 2024 (a17); Musker et al. 2025 (b15) | established (K12) |
| Self-generated analogues, small gain | GPT-3.5 GSM8K/MATH Acc@1 3-shot CoT 11%, self-exemplars 13%, knowledge plus exemplars 15%; GPT-4 17% to 19%; average gain about +4%. Table cells scrambled. | Yasunaga et al. 2024 (a19, b16) | single-source (K13) |
| Facts in pieces over turns hurt | Average drop 39% over 6 tasks, 15 models, 200,000+ conversations; aptitude -16% (not significant), unreliability +112%; best-worst gap about 50 points; CONCAT keeps 95.1% of FULL; temperature 0 leaves about 30% unreliability | Laban et al. 2025 (b21, c10, c11, c12) | single-source on the paper, supported by d06 (K15) |
| Restating recovers little | SNOWBALL recovers 15-20% of the loss (GPT-4o, GPT-4o-mini, 4 tasks); degradation starts at 2 shards | b22, c12 | single-source (K16) |
| Answer bloat in sharded runs | final answers 20-300% longer; correct code 850 vs 668 chars (+27%); SQL 129 vs 113 (+14%) | c11 | single-source |
| Premise order | drops of 20-30% for GPT-4-turbo and PaLM 2-L; over 40 points for Gemini 1.0 Pro and GPT-3.5-turbo (above 65% to below 25%) | Chen et al. 2024 (b23) | single-source (K17) |
| Few-shot order | SST-2 from near 50% to over 85% by permutation; score correlation between 175B and 2.7B is 0.05 | Lu et al. 2022 (c20) | established with b23 (K18) |
| Intrinsic self-correction hurts | GPT-3.5 CSQA 75.8 to 41.8 after 5 calls (38.1 after 3, so not monotone); GPT-4 CSQA 82.0 to 80.0; GSM8K GPT-3.5 75.9 to 74.7, GPT-4 95.5 to 89.0; HotpotQA GPT-4 49 to 43; oracle labels 84.3 / 97.5 | Huang et al. 2024 (c17) | established (K19) |
| Models cave to pushback | first-answer change 32% (GPT-4) to 86% (Claude 1.3); accuracy loss up to 27%; admit mistake 42% to 98% | Sharma et al. 2024 (c19) | established (K20) |
| Sycophancy compounds over turns | up to 47% accuracy drop; wrong answers flip up to 40% more than right ones; 50% change by turn 4 vs about 10% for correct; Claude feedback sycophancy 76.74% to 30.23% by follow-up 7 | Liu et al. 2025 TRUTH DECAY (d05) | established with c19, d03, d07, d08 |
| Later challenge flips more than first-query claim | multi-turn 6.99% vs single-turn 2.53% (2.8x). Fake sources lower flipping in multi-turn (8.69% / 6.63% / 5.67% for none / one / several) but raise it in single-turn (1.99% / 2.53% / 3.08%). 1.2M trials, 5 models | Ping et al. 2026 (d03) | single-source (K27) |
| Flips are not all bad | sycophantic in 58.19% of cases; progressive (toward correct) 43.52%, regressive 14.66%; preemptive rebuttal 61.75% vs in-context 56.52% (Z=5.87, p<0.001); persistence 78.5% | Fanous et al. 2025 SycEval (d08) | part of K20 |
| Rebuttal format | casual simple rebuttal 84.5% persuasion; follow-up rebuttal 56.1%; are-you-sure 53.8%; neutral judge setting 43.6% (table garbled) | Kim and Khashabi 2025 (d07) | with K28 |
| Sequential presentation tax | accuracy below single-shot in 14/17 (MedQA), 14/17 (JAMA CC), 16/17 (MedMCQA) models; tax up to 30% on average, 65% in some; Llama 3 70B drops 17, 29, 17 pp; blind switching up to 50% | Guo et al. 2026 (d06) | established (K28) |
| Belief revision weak | best large models at most 50% BREU; update-good models are maintain-bad; plan-and-solve about +1% | Wilie et al. 2024 Belief-R (c13, c14) | single-source plus d01, d02, d04 (K21) |
| Inertia and collateral damage | 7 frontier models violate minimal change and preservation; reasoning-trained models better at one step, degrade faster under iteration | Jenkins 2026 AGM-Bench (d04; abstract page only) | established with d01 (K29) |
| Update-tracking vs drift trade-off | RAG: +0.09 BRA, +0.07 CRR, +0.02 DCS; 2,400 trajectories, 7 models; Claude 3.5 Sonnet DCS 0.79 zero-shot, 0.81 RAG (tables garbled) | Myakala et al. 2026 BeliefShift (d01) | established with d04 (K29) |
| Larger models over-update | 7 open-weight models, 3B-70B; extreme probabilities vs Bayesian reference | Samanta et al. 2026 BayesBench (d02) | single-source (K30) |
| Plateau after round 1 without help | 624 simulated users, 5 rounds; Bayesian assistant about 81%; random about 37%; tuned models improve each round | Qiu et al. 2025/2026 (c15, c16, d12) | single-source, needs fine-tuning (K22) |
| Grounded loops help | Reflexion 130/134 ALFWorld; HumanEval 91.0 vs GPT-4 80.1; Voyager -73% items without self-verification; Self-Refine GPT-4 code 27.3 to 36.0 (+8.7), most gain early | c18, c25, c23 | established (K23) |
| Structured store beats long free text | lost in the middle: over 20% drop; GPT-3.5 multi-doc QA closed-book 56.1%, oracle 88.3%; Cumulative Reasoning up to +8.62% over CoT, FOLIO 98.04%, Game of 24 98%, MATH L5 22.4% to 32.1% | Liu et al. 2024 (c21); Zhang et al. (c24) | established (K24) |
| First pair carries the rule | patching first pair fixes up to 38.4% of errors (Gemma-7B); Llama-2-13B +32.3%; Qwen2.5-14B +35.6%. Llama-3.1 70B: 98% vs 62% on previous/next | Lee et al. 2025; Opielka et al. 2025 (b18, b19) | established (K25), open-weight only |
| Hybrid mapper plus LLM | StoryAnalogy-MCQ (360 items, chance 0.25): Qwen3-8B mapping alone 0.17, with abstraction 0.46 vs best LLM-only 0.41; Llama-3.1-8B 0.45 vs 0.28. ARN (1,096 pairs, chance 0.50): Qwen far 0.47 vs 0.52 zero-shot; near 0.69 vs 0.79 CoT; Llama far 0.46 vs 0.42 | Khojasteh et al. 2026 YARN (b17, d11) | single-source (K26) |
| Reasoning models on I-RAVEN-X | arithmetic accuracy reasoning models 80.5% to 63.0%, plain LLMs 59.3% to 4.4%; under perceptual uncertainty accuracy fell 61.8%; o3-mini 17.0%, R1 22.8% vs 12.5% chance | Camposampiero et al. 2025 (b20) | single-source |
| In-context learning scales with shots | planning 42% to 62%; Bemba +15.3%, Kurdish +4.5% | Agarwal et al. 2024 (c22) | background |

---

## 4. Mechanisms and models

### 4.1 I-SME as an algorithm an engineer can implement (a01-a05)

Data structures:
- **Match hypothesis (MH):** a pairing of one base item with one target item (entity, attribute, relation or function).
- **Kernel:** a connected set of consistent MHs rooted at a top-level match. Built by walking down from a root MH through argument pairings.
- **Global mapping (GM):** a one-to-one, structurally consistent set of kernels. Keep at most `n` GMs, each within `p%` of the best structural score.
- **Nogood links:** two MHs that cannot both hold (they pair one item with two partners, or break parallel connectivity).

Operations:
1. `ADD-FACTS(base_facts, target_facts)`: store them.
2. **EXTEND**:
   1. Build new local MHs: new items against old and new items on the other side.
   2. Update kernels from new root matches downward.
   3. Score kernels. Optionally apply pragmatic filters (below).
   4. Merge new kernels into each existing GM greedily (best first, skip those in conflict). Keep the best n within p%.
3. **REMAP**: clear all GMs. Rebuild greedily from all kernels (after optional filtering). It is backtracking at the level of kernels.
4. **COVERAGE**: report the fraction of the total possible structural score that current GMs hold. I-SME gives no rule to use it; "remap criteria are task-specific".

Pragmatic filters (a05):
- **REQUIRED:** externally imposed correspondences (a speaker says "heat is like water"). Forces those pairs.
- **IDENTICAL-FUNCTIONS:** reject root matches that pair non-identical functions. This is a type guard. In MARS, dropping it let specific enthalpy match temperature and gave a wrong (simpler) solution.

Why it works: new facts add hypotheses and kernels instead of restarting. Most cost lives in the match network, which is reused.

Why it fails: greedy merge can lock early partial matches (a02). Partial information can mislead (c04). The natural first guess (TIMID=HUNGRY, TOM=FIDO in Keane's task) cannot give a 1:1 mapping once a late singleton arrives, which forces a rebuild (b02).

### 4.2 Remap rule used for the order effect (a07)

I-SME was set to REMAP whenever an entity or attribute could not be added to the current mapping. That rule was chosen by the authors. It produced 1.5 vs 3.0 remaps per example across the two orders. Treat it as a demonstration, not a validated model.

### 4.3 PHINEAS map-and-analyze cycle (a09)

1. Initial cheap mapping.
2. Find unmatched parts. Use domain theory only where an impasse arises.
3. Re-examine the mapping: extend or shift.
4. Repeat until no extension.

Candidate-inference check order: known; functional analogue believed; assume if jointly consistent; otherwise seek consistent analogues. This is a ready-made template for an LLM wrapper: code holds the check order and the joint-consistency test; the model writes only the inferences.

### 4.4 Incremental encoding for time-course effects (a11, a13)

Short deadline: run SME on attributes only. Long deadline: encode relations, then update the mapping. Measure the number of SME differences. This reproduces direction of effects (ordinal fit only). The model misses the large short-vs-long gap at 0 mismatched matches and the small out-of-place effect at long deadlines.

### 4.5 Re-encode on failure (a14)

The Raven's model compares images, reifies the differences, compares the differences again. When images fail to align, it re-encodes and tries again. 56/60. This is "remap by changing representation" (our O6) triggered by an alignment failure.

### 4.6 Progressive alignment and interim generalizations (b07, d09)

Hold a close pair in working memory. Build a generalization from it (assimilation threshold 0.95, interim generalization limit 5). When the next case fails to align, re-represent and try again. Easy first, then far.

### 4.7 LLM-side mechanisms (b18, b19, b21)

- In-context analogy uses concept vectors held in a few attention heads; the first pair carries the rule (b18, b19). Abstract concepts such as previous/next use order- or format-based codes and are fragile.
- In multi-turn use, models make early assumptions, answer too soon, lean on their earlier attempts, over-weight first and last turns, and write long answers (c11). These are the mechanisms by which a stored LLM mapping degrades.

---

## 5. What holds up

### 5.1 Replications and their absence

- **Keane's order effect: no replication found** (d13). This is a tool-limited search. Treat the effect as one 1994 result with an authors' simulation on top.
- **Time-course effect (feature first, relations later):** reported by three labs' studies (Goldstone and Medin; Sloutsky and Yarlas; Gentner and Sagi) and modelled by Lovett et al. Established (K04), but all human numbers are second-hand and the model fit is ordinal.
- **Webb et al. 2023 vs Lewis and Mitchell 2024:** a partial failed replication of generality. On permuted alphabets GPT models fall (0.350 / 0.452 / 0.488 vs humans 0.753). Humans stayed flat from 0 to 20 permuted letters. Comprehension checks on successor/predecessor were mostly high (0.49 to 1.00), so the failure is not only misreading the alphabet (a16, a25).
- **Webb et al. 2024 reply:** GPT-4 with code execution reaches about human level; 46% vs 39% valid-alternative-rule errors. The authors read the failure as a counting problem. Contested. The fix is code execution, which fits our G5 (code does the counting).
- **Stevenson et al. 2024** supports Lewis and Mitchell with children and adults (b-level numbers above). **Musker et al. 2025:** GPT-4 mean match about 0.7 in two conditions, 0.2-0.3 in the rest, significantly worse than humans in Numeric; Claude 3 matched humans in all conditions of one experiment.
- **Self-correction:** Huang et al. vs Self-Refine and Reflexion. Reconciled by grounding: gains come with an external check, oracle label, or tests (c17, c18, c23).
- **Sycophancy:** five independent sources agree models flip under pushback (c19, d03, d05, d07, d08). The detail that matters: 43.52% of flips went toward correct (d08). So the rule is "gate on evidence", not "never change".

### 5.2 Moderators

- **Familiarity of format.** GPT-3 beat humans on digit matrices and letter strings but lost on story analogies; models collapse on unfamiliar symbols (K09, K12).
- **Model scale.** Self-generated exemplars beat retrieved ones at larger scale; retrieved won at smaller scale (a19). Larger models track hidden state better but over-update (d02). Reasoning-trained models are better at one revision step but degrade faster under iteration (d04). Scale fixes some multi-turn failures and worsens others (d06).
- **Order and position.** Premise order (b23), option order (b14), few-shot order (c20), position in context (c21). Orders that work for one model do not transfer to another (correlation 0.05).
- **Challenge placement.** A later challenge flips more than an opening claim (d03), but a rebuttal placed before the answer (preemptive) flips more than in-context (d08). Both can be true: the effect depends on whether the model has committed.
- **Domain.** Subjective fields flip more than STEM (philosophy accuracy 70% to under 20% vs STEM stable at 30-50%, d05).
- **Time budget (humans).** Short deadlines give feature-based matches; long ones give relational ones (K04).

### 5.3 Interventions that worked

- External check or verifier on each revision: Reflexion, Voyager (-73% items without it), Self-Refine early rounds, oracle labels in Huang et al.
- Code doing the counting (Webb 2024 reply).
- Explicit structured stores of verified propositions: Cumulative Reasoning (up to +8.62% over CoT).
- Showing alternatives side by side instead of in sequence (d06, d07).
- Restating all facts in one final consolidation turn (RECAP) beat SNOWBALL; but still not FULL (c12).
- RAG over past sessions improved update tracking (+0.09 BRA) (d01).
- Type guards and required correspondences in the mapper (a05).
- Hybrid: structure mapper over LLM-derived abstractions helps small models (b17).

### 5.4 Interventions that did not work

- Plain restating every turn: only 15-20% of the loss recovered (b22).
- Temperature 0: unreliability stayed about 30% (b21).
- Intrinsic self-correction without outside signal (c17).
- Chain-of-thought and plan-and-solve for belief revision: about +1% BREU, hurts some models (c14).
- Chain-of-thought and other prompt changes for cumulative updating across rounds (c16).
- Fake sources: the effect flips between single-turn and multi-turn (d03).
- Fine-tuning (Bayesian teaching) works but is outside our no-training rule (c15, d12).

---

## 6. Language models

### 6.1 Direct tests of incremental mapping: none found

All LLM analogy studies are one-shot (a20, c26, d15). Search was limited. A negative on the 2026 literature is weak. No LLM study tests extend-versus-remap, joint versus per-inference checking, structured mapping tables, or close-to-far curricula.

### 6.2 One-shot analogy: strong on familiar formats, brittle off them

See table in section 3. The pattern across Webb, Lewis and Mitchell, Stevenson, Musker, Hu (a18; Raven-style matrices zero-shot, 77.2% / 78.0% / 86.4% on some conditions, table garbled so direction only) and Camposampiero (b20): good with familiar content, weak when the surface changes. Reasoning models hold longer relation chains better than plain LLMs but collapse under perceptual uncertainty (b20).

### 6.3 Facts over several turns: strong, consistent degradation

- Laban et al.: 39% average drop; aptitude barely moves (-16%, not significant) but unreliability rises 112%. Meaning: the model can do it, but unreliably, and the same task can land 50 points apart. Causes: early guessed assumptions, reliance on earlier attempts, lost middle turns, bloat. CONCAT (all shards in one turn) recovers 95.1%.
- Guo et al.: presenting the answer space sequentially costs accuracy in 14 to 16 of 17 models.
- Premise order alone moves accuracy 20-40 points (b23).
- Qiu et al.: off-the-shelf models stop improving after round 1 in a 5-round task.

What changed it: all-at-once presentation (large), RECAP (some), RAG (update tracking only), grounding with a check (large), fine-tuning (large, not available), side-by-side comparison (some). What did not: temperature, CoT, plain snowballing, bigger models in general.

### 6.4 New facts as revision: both inertia and flip-flop

- Belief-R: the best models reach at most 50% on mean of update and maintain accuracy. Good at update means bad at maintain (c13).
- AGM-Bench: models keep retracted facts and drop unrelated beliefs (d04).
- BeliefShift: update tracking and drift resistance trade off (d01).
- BayesBench: larger models over-update (d02).
- Sycophancy: 32% to 86% first-answer change under "are you sure" (c19); compounding over turns up to 47% (d05).

So an LLM given a new fact has no safe default. It either keeps the old mapping too long or overwrites it too easily. A structured, code-held record with per-slot scores and bounded steps is the obvious control, but nobody has tested it for mappings.

### 6.5 Hybrids

YARN (2026): pure structural mapping over raw event embeddings was below chance (Qwen3-8B 0.17 vs chance 0.25); with LLM abstraction 0.46 vs best LLM-only 0.41. Gains are not uniform (ARN far: 0.47 vs 0.52). 8B models only. FAME is a second SME-plus-LLM hybrid (d11), not tested here. Single-source preprints with no independent check.

---

## 7. What our agent should take

Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single-source, [C] contested. Evidence ids refer to the files here.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **No unverified revision of a stored mapping.** A mapping may change only when code shows a failing output or a failed check that cites the slot. Already G2; here it is extended to analogue mappings. | G2 | [E] | c17, c19, c18, c23, d05; K19, K20, K23 |
| A2 | **A new fact is evidence, not a correction.** When a new fact or a "this is wrong" message arrives, do not let the model flip an answer on the message alone. Code requires a cited fact or a check result. Flips toward correct (43.5%) and toward wrong (14.7%) both happen, so gate on evidence, not on change. | G2 / S6 | [E] | c19, d03, d05, d07, d08; K20 |
| A3 | **Hold the mapping in a code-side structure, not in the chat history.** Store the mapping as a compact table (slots, pairing, score, status, source fact) that code re-renders each round. Long free-text history loses the middle and drifts. | memory / S6 | [E] | c21, c24, b21, d01; K24, K15 |
| A4 | **Present old and new alternatives together in one comparison step**, not one at a time. When a new fact suggests a different mapping, show both side by side. | S6 | [E] | d06, d07; K28 |
| A5 | **Re-derive only affected slots, then re-check unrelated slots for no change.** Counter inertia (retracted facts kept) and collateral damage (unrelated beliefs dropped). Code computes the affected set from the dependency links. | S6 | [E] | d04, d01; K29 |
| A6 | **Consolidate before extending.** At each S6 round, restate all current facts and the mapping in one block (RECAP-style, done by code), then extend. Do not rely on the model's remembered turns. It recovers part, not all, of the loss, so this is a floor. | S6 / memory | [E] direction; size [S] | b21, b22, c12; K15, K16 |
| A7 | **Fresh start beats a long patched thread when the loss is large.** If facts are known up front, give them all at once (CONCAT keeps 95.1%). Use rounds only when facts truly arrive late. | S3 / S6 | [E] | b21, c10, d06; K15, K28 |
| A8 | **Randomise or double-check fact order; do not trust a tuned order.** Present facts in two orders and require agreement before committing. Do not tune an order on a small model. | G4 / S7 | [E] | b23, c20, b14; K17, K18 |
| A9 | **Put the clearest example pair first and state the rule.** | S1 / S2 | [E] (open-weight models only) | b18, b19; K25 |
| A10 | **Let code do counting and letter/position tasks.** | G5 | [C] (Webb 2024 vs Lewis and Mitchell) but consistent with G5 | b12, a16; K10 |
| A11 | **Revision loops need a grounded check and stop after 2-3 rounds.** Matches S5. | S5 | [E] | c18, c23, c25; K23 |
| A12 | **Test mappings on unfamiliar tokens.** A mapping that survives renaming of symbols is structural, not lexical. Use it as the S4/G3 held-out check on analogue mappings. | G3 / S4 | [E] | a17, b15, a16; K12 |

### Test first

| # | Item | Schema part | Status | Evidence | Why not yet |
|---|---|---|---|---|---|
| T1 | **Extend vs remap from scratch** at equal tokens when a new fact arrives. | S6 | [S] | K01, K14, a20 | No LLM test exists. |
| T2 | **Coverage signal to trigger remap**: fraction of slots with a supported pairing; remap when coverage stalls or a type conflict appears. | S6 | [S] | K02, a03 | I-SME leaves the rule open; one source. |
| T3 | **Small set of rival mappings (n within p%)** kept in the table, new facts scored against each, instead of one mapping. | S6 / memory | [S] | a02, K02 | No LLM test; could blow the token budget. |
| T4 | **Type guard (identical-functions filter)**: code rejects pairings between different kinds of quantity or role. | G / S4 | [S] | a05, c04; K07 | One worked example. |
| T5 | **Joint consistency check of all candidate inferences** at once, not one by one. | S6 | [S] | a09; K08 | Falkenhainer's rule, no numbers. |
| T6 | **Fact-order effect**: easy-first vs hard-first, count revisions. | S6 | [S] | a06, a07; K03, K31 | Human result unreplicated and second-hand. |
| T7 | **Close-to-far curriculum** for analogue examples. | O7 / S3 | [S] | b07, d09; K06 | Child-model result only. |
| T8 | **Bounded per-slot score step** per round to avoid over-updating. | S6 | [S] | d02; K30 | Open-weight preprint. |
| T9 | **Hybrid: code-held structure mapper plus LLM abstraction.** | O7 | [S] | b17, d11; K26 | 8B models, single source. |
| T10 | **Time-budget effect**: short thinking gives surface matches; longer gives relational ones. | S0 / G11 | [E] for humans, untested for LLMs | K04, a11 | Humans only. |

---

## 8. Concrete tests on our bench

All tests: both arms use the same token budget (G7). Items: ARC-style tasks where an analogue is given in rounds, BRAINTEASER items with an analogue, and a small synthetic "mapping drift" suite (below). Log per-state tokens and flips (SCHEMA section 6). Sample at least 60 items per arm and at least 3 seeds, because Laban shows unreliability matters more than aptitude.

**Synthetic suite design.** Build 40 base/target pairs as typed fact lists (entities, attributes, relations) with a known correct 1:1 mapping. Reveal target facts over 3-4 rounds. Include four round types: (a) a new fact that extends the mapping, (b) a new fact that conflicts with an earlier pairing and requires a remap, (c) a neutral fact that must change nothing, (d) a lure (an attribute match that is a surface trap, as in the h-versus-T example).

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| B1 | Extend vs remap (T1) | Synthetic suite, rounds a-d | (1) model keeps the mapping and extends it in chat; (2) code re-renders all facts each round and the model maps from scratch; (3) code-held table, model extends only affected slots | Final mapping accuracy (slot F1), tokens to final, flips on round type (c) | Arm 3 >= arm 2 > arm 1 on accuracy; arm 3 cheaper than 2. A null between 2 and 3 is acceptable. Expect arm 1 to lose by 10+ points, as Laban's 39% suggests. |
| B2 | Coverage-triggered remap (T2) | Synthetic type (b) rounds | (1) never remap; (2) always remap; (3) remap when code coverage stalls or conflict arises | Accuracy, tokens | Arm 3 on par with arm 2 on accuracy at fewer tokens. |
| B3 | Neutral new fact (A2) | Synthetic type (c); ARC items with a distractor fact | (1) plain "new info" message; (2) evidence-gated: code requires a cited fact or check | Flip rate on neutral facts; flip rate toward correct on true updates | Gate cuts flips on neutral facts to near 0 without cutting true updates by more than 5 points. |
| B4 | Side-by-side vs sequential (A4) | Synthetic type (b) | (1) old mapping then "now consider this alternative"; (2) both shown in one comparison | Accuracy on remap rounds | Arm 2 higher. Guo et al. suggest a gap of 10+ points. |
| B5 | Type guard (T4) | Synthetic type (d) lures; ARC with colour/shape lures | (1) no guard; (2) code type check rejects cross-kind pairings | Wrong cross-kind matches per 100 items; final accuracy | Wrong matches drop sharply; accuracy up when lures exist, null otherwise. |
| B6 | Fact order (T6, A8) | Synthetic, same facts, two orders: singleton-last vs singleton-first | Single order vs two orders with agreement rule | Revisions count; accuracy gap between orders; accuracy of agreement rule | Expect an order gap (as Keane); agreement rule shrinks it. If no gap appears, drop T6. |
| B7 | Joint vs per-inference check (T5) | Items with 3-5 candidate inferences, some mutually inconsistent | (1) check each inference alone; (2) check set jointly by code | Accepted inconsistent sets per 100 items; final accuracy | Joint catches inconsistent sets that per-inference misses. |
| B8 | Rival mappings (T3) | Synthetic type (b) with ambiguous early facts | (1) single mapping; (2) top-2 rivals with scores | Accuracy after the disambiguating fact; tokens | Arm 2 recovers faster after an early wrong choice; may lose on token cost. |
| B9 | Bounded step (T8) | Rounds with weak or noisy facts | (1) model gives free confidence each round; (2) code applies fixed step per supported fact | Calibration (Brier) per round; flips | Arm 2 less extreme and fewer flips. |
| B10 | Curriculum (T7) | ARC items with 2-3 solved analogue examples before the target | (1) random order; (2) close-to-far order set by code similarity | Accuracy; tokens | Small effect expected; drop if under 3 points. |
| B11 | Renamed-symbol check (A12) | Mappings with analogue; rename all tokens | (1) accept mapping on the original; (2) require pass on renamed variant | False-accept rate of wrong mappings | Renamed check catches lexical shortcuts. |
| B12 | Hybrid (T9) | Typed fact lists from story pairs | (1) LLM alone; (2) LLM abstracts each unit, code maps | Accuracy | Gain on small models; null on strong ones. |

---

## 9. What does not transfer, and why

- **The Keane order effect.** Its task has no higher-order structure (Forbus et al. say so). It is a symbolic attribute task with humans solving in minutes. It may not transfer to text-based LLM mapping at all. The doubling of time was for people, not tokens. And it was never replicated in our evidence.
- **Serial working-memory limits.** IAM and the capacity-limited merge model human working memory. LLMs have no such limit. Their limit is attention to the middle of the context and over-commitment to early assumptions (c11, c21). Similar shape, different cause.
- **Time-course (150 ms to 2.68 s).** These are perception deadlines. The closest LLM analogue is a thinking-budget cap, untested. Do not read milliseconds as tokens.
- **I-SME timings (34 s on a 1994 PowerBook).** Meaningless as numbers now. Only the complexity claim matters.
- **MARS result.** One helium-heater problem with hand-built representations. No error rates.
- **Raven's 56/60.** Hand-tuned symbolic-visual pipeline, one test. It proves mapping-by-extension can scale in principle, not that an LLM can do it from text.
- **Bayesian teaching.** Works (about 80% agreement with the Bayesian assistant after tuning) but needs fine-tuning. We do not train.
- **Child progressive-alignment data and the model of it.** Model hit 100% where children had 68%. The model is too uniform. Original numbers second-hand.
- **Sycophancy rates.** Many come from medical QA, older models, and absolute rates under 9% in Ping et al. (d03). Rates will differ for our items; use the direction, not the size.
- **Belief-revision benchmarks.** Their beliefs are user stances or logic rules, not typed mappings. BeliefShift is 60% synthetic and unreviewed (d01). AGM-Bench was an abstract page only (d04).
- **Multi-turn degradation (Laban).** Tasks are code, SQL, math, actions; the simulated user gives one shard per turn at temperature 1. Our rounds come from code and checks, not an adversarial user.
- **Self-generated analogues (Yasunaga).** One-shot recall, not mapping extension; table cells scrambled.
- **Mechanistic patching (Lee, Opielka).** Needs open weights and internal access. We use only the behavioural lesson (first pair carries the rule).
- **Groups on which the schema already speaks.** Debate between agents is excluded (G9); do not add multi-agent consensus for mapping.

---

## 10. Open questions

1. Does extending a stored mapping beat re-mapping from scratch in an LLM at equal tokens, and on which tasks does it lose accuracy? No direct test exists.
2. Can an LLM or code estimate a coverage or structure fraction that predicts when to remap? Only I-SME's own signal exists, and no rule.
3. Does fact order cause a Keane-style order effect in LLM mapping? Has anyone replicated Keane (1994) with N and statistics? Original unopened.
4. How should the agent revise on a conflicting fact without flipping on pushback and without stubbornness? Evidence shows both failures; no tested recipe beyond RAG for update tracking.
5. Does an explicit structured mapping table beat free-text history in multi-round settings? Only proxies.
6. Do I-SME's successors (SME 2016, Companion systems, Bridge Incremental Analogizer) report accuracy or speed numbers on incremental sessions? The 2016 PDF was a scan we could not read.
7. Is joint consistency checking better than per-inference checking for LLM agents, and how many can be checked jointly before it fails?
8. Does the YARN-style hybrid hold up on independent benchmarks and larger models? FAME is another candidate.
9. Do close-to-far curricula improve LLM relational mapping?
10. The Gentner and Sagi shield timings differ between two reports (1380/880 ms vs 1270/910 ms). Which is right?
11. Is the premature-answer behaviour (c11) reduced if the schema forces a "not enough facts yet" state until a coverage threshold is met? This conflicts with G6 (never abstain on the first pass) only if applied to the final answer; it could apply to the mapping slot. Untested.

---

## 11. Sources

[V] opened and read this session; [M] snippet or second-hand only.

**Incremental mapping and its lineage**
- [V] Forbus, Ferguson, Gentner (1994) Incremental structure-mapping (I-SME). https://www.qrg.northwestern.edu/papers/Files/isme94.pdf
- [V] Falkenhainer (1990) Analogy in context: the map and analyze cycle. https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_1990/1_57_Falkenhainer_1990_Analogy_Context.pdf
- [M] Keane, Ledgeway, Duff (1994) Constraints on analogical mapping, Cognitive Science 18. https://doi.org/10.1207/s15516709cog1803_3 and https://edepositireland.ie/handle/2262/12939 (abstract summary only; publisher page 403)
- [M] Keane and Brayshaw (1988) The Incremental Analogy Machine (known only through the I-SME paper)
- [M] Burstein (1986); Falkenhainer (1987) PHINEAS (through the I-SME paper)
- [M] Finlayson and Winston, Bridge Incremental Analogizer (search summary only)
- [M] Forbus, Ferguson, Lovett, Gentner (2016) Extending SME to handle large-scale cognitive modeling. https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_2016/ISMEJ2016-preprint.pdf (image-only scan, unreadable)
- [V] Lovett, Gentner, Forbus, Sagi (2006) Simulating time-course phenomena via incremental encoding. https://www.qrg.northwestern.edu/papers/Files/Lovett_TimeCourse.pdf
- [V] Lovett, Gentner, Forbus, Sagi (2009) Using analogical mapping to simulate time-course phenomena, Cognitive Systems Research 10. https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_2009/lovettGentnerForbus&Sagi_2009.pdf and https://doi.org/10.1016/j.cogsys.2008.08.004
- [M] Goldstone and Medin (1994); Sloutsky and Yarlas (submitted); Gentner and Sagi (2006); Kotovsky and Gentner (1996) (all through Lovett et al. or Kandaswamy et al.)
- [V] Kandaswamy, Forbus, Gentner (2014) Progressive alignment using interim generalizations. https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_2014/Kandaswamy-Forbus-Gentner-CS14.pdf (proceedings index: https://cognitivesciencesociety.org/cogsci-2014-proceedings/)
- [V] Lovett and Forbus (2017) Modeling visual problem-solving as analogical reasoning. https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_2017/Lovett-Forbus-2017.pdf

**LLM analogy**
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in LLMs. https://arxiv.org/abs/2212.09196
- [V] Lewis and Mitchell (2024) Counterfactual tasks for analogical reasoning in LLMs. https://arxiv.org/abs/2402.08955
- [V] Webb, Holyoak, Lu (2024) Evidence from counterfactual tasks supports emergent analogical reasoning. https://arxiv.org/abs/2404.13070
- [V] Lewis and Mitchell (2024) Robustness of analogical reasoning in LLMs (digit matrices, story analogies). https://arxiv.org/abs/2411.14215
- [M] Hodel and West (2023) counterfactual letter-string critique (through summaries)
- [V] Stevenson et al. (2024) Can LLMs generalize analogy solving like children can? https://arxiv.org/abs/2411.02348
- [V] Musker, Duchnowski, Milliere, Pavlick (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803
- [V] Hu et al. (2023) In-context analogical reasoning with pre-trained language models. https://arxiv.org/abs/2305.17626
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714
- [V] Khojasteh et al. (2026) YARN. https://arxiv.org/abs/2603.29997
- [V] Lee et al. (2025) The curious case of analogies. https://arxiv.org/abs/2511.20344
- [V] Opielka, Rosenbusch, Stevenson (2025) Analogical reasoning inside LLMs. https://arxiv.org/abs/2503.03666
- [V] Camposampiero et al. (2025) I-RAVEN-X. https://arxiv.org/abs/2510.17496

**Multi-turn, order, revision, sycophancy**
- [V] Laban, Hayashi, Zhou, Neville (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120
- [V] Chen et al. (2024) Premise order matters. https://arxiv.org/abs/2402.08939
- [V] Lu et al. (2022) Fantastically ordered prompts. https://arxiv.org/abs/2104.08786
- [V] Liu et al. (2024) Lost in the middle. https://arxiv.org/abs/2307.03172
- [V] Agarwal et al. (2024) Many-shot in-context learning. https://arxiv.org/abs/2404.11018
- [V] Wilie et al. (2024) Belief-R. https://arxiv.org/abs/2406.19764
- [V] Qiu et al. (2025/2026) Bayesian teaching. https://arxiv.org/abs/2503.17523
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Zhang et al. Cumulative Reasoning. https://arxiv.org/abs/2308.04371
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291
- [V] Sharma et al. (2024) Towards understanding sycophancy. https://arxiv.org/abs/2310.13548
- [V] Myakala, Agrawal, Manche (2026) BeliefShift. https://arxiv.org/abs/2603.23848
- [V] Samanta et al. (2026) BayesBench. https://arxiv.org/abs/2606.30850 (id as recorded in evidence file; check before citing)
- [V] Ping et al. (2026) Why LLMs give in. https://arxiv.org/abs/2608.01017 (id as recorded; check before citing)
- [V] Jenkins (2026) AGM-Bench. https://iclr.cc/virtual/2026/10017503 (abstract page only)
- [V] Liu et al. (2025) TRUTH DECAY. https://arxiv.org/abs/2503.11656
- [V] Guo et al. (2026) Stop Listening to Me! https://arxiv.org/abs/2603.11394
- [V] Kim and Khashabi (2025) Challenging the Evaluator. https://aclanthology.org/2025.findings-emnlp.1222/
- [V] Fanous et al. (2025) SycEval. https://arxiv.org/abs/2502.08177

**Data-quality notes (from critique.md).** Tables garbled in extraction: Hu 2023, Yasunaga 2024, Lewis and Mitchell Table 1, BeliefShift, Kim and Khashabi. Cell numbers from them are approximate. The claim K15 in claims.jsonl cites evidence id a21, which in the evidence file is the unread 2016 SME paper; the Laban numbers are in b21, c10, c11, c12 and were verified in paper text. Two p-values for letter strings (6.3e-5 overall, 0.0007 zero-generalization subset) are both correct.
