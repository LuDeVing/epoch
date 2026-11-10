# Problem posing, conjecture: deep document

*Subfield E06.08. Written 2026-11-10 from evidence_a-d.jsonl (a01-a27, b01-b26, c01-c25, d01-d19), claims.jsonl (K01-K28) and critique.md in this folder. Evidence ids are cited as a01 etc. Claim ids as K01 etc. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Problem posing is making a new problem from a given one, or from a situation. Conjecturing is stating a claim or an answer that is not yet proved. Refutation is finding a case that breaks a claim. In maths these three form one loop: pose, guess, test, break, repair.

Two human traditions define the loop.

- **Brown and Walter, What-If-Not (WIN).** List the attributes of a given statement. Negate or vary each one. Ask what problem each variant is. Then analyse the variants. This is the source of our operator O4 ("drop a constraint"). Neither book was opened in this research (a26, b25). It is known only through citations.
- **Lakatos, Proofs and Refutations.** A conjecture is made, a proof is treated as a thought experiment, and counterexamples drive repair of the claim, the proof or the concepts. Only Part I was read (a01-a05, c01).

What this means for an LLM agent. There are four separate skills.

1. State the target: the answer or conjecture the task needs (S1/S2).
2. Pose useful sub-claims: lemmas, special cases, variants (O1, O4, S9).
3. Test the claim: look for counterexamples by running code (S4, G3, G8).
4. React to a counterexample: repair the claim, repair the proof, or wrongly protect the claim (S5).

The research base is uneven. Human work covers skill 2 with classroom interventions. LLM work (2024-2026) is mostly formal (Lean, Isabelle, GAP) and mostly about skills 2 and 3. No study tests What-If-Not or Lakatos moves on an LLM (d19, K04). That gap is the main finding of this document.

## 2. History and theories in depth

**Polya and Lakatos lineage.** Lakatos wrote Proofs and Refutations in 1958-59. It was read in Popper's seminar in March 1959, circulated in mimeograph, appeared in the 1961 Cambridge PhD thesis and in the 1963 BJPS paper (a01). It is dedicated to Polya and Popper. It is a rational reconstruction with invented speakers (Alpha, Beta, Gamma, Delta). It is not an empirical study.

**The Euler example.** The claim is V - E + F = 2 for polyhedra. Euler noted it in 1750, a proof was proposed in 1751, and Cauchy gave a proof in 1813 (a05). The proof has three steps: remove a face and flatten, triangulate, remove triangles one by one. Lakatos splits counterexamples in two (a02).

- **Local**: attacks one proof step but not the claim. A hollow cube breaks step 1 (removing a face does not leave a flat network).
- **Global**: attacks the claim itself. The picture-frame polyhedron has V - E + F = 0 (16 - 32 + 16) (a03, c02).

**The menu of responses (a03, a04, c01, c02).**

| Move | What it does | Effect on the claim |
|---|---|---|
| Surrender | drop the claim | ends the line |
| Monster-barring | redefine the key term so the case is no longer an instance ("a picture frame is not a polyhedron") | protects the claim, may save a false one |
| Exception-barring | list exclusions ("true except for ...") | protects, piecemeal |
| Monster-adjusting | reread the counterexample so it fits the claim | protects |
| Lemma-incorporation | find which proof step failed, add its condition to the claim | improves the claim |
| Proofs and refutations | full loop: new proof, new counterexamples | improves |

The notes say monster-barring is often a legitimate concept refinement, not always a dodge (a03). Martin and Pease (2013) give a computational reading: counterexamples trigger six revision methods, and monster-barring and monster-adjusting exploit vague concept definitions (c02). They link this to Colton's HR theory-formation system.

**Heuristic order.** Lakatos argues conjecture comes before proof, as in ancient analysis (Proclus, Pappus): a theorem is stated, then demonstrated (a05).

**Problem posing in education.** Silver and Cai (1996) had 509 middle-school students pose problems from a story. Nearly half posed sets of related problems. Better solvers posed more and more complex problems (b03; Crossref abstract only). Ran et al. (2025) analysed unexpected responses: 74% were task misreadings, 18% connection failures, 8% generation failures. The prompt wording changed the mix (chi2(2, 279) = 6.62, p = 0.03). Two raters agreed 92% on a 20% sample (b04).

**Self-play and intrinsic motivation (2024-2026).** The modern AI line makes the model pose its own problems. Minimo (a13-a15, c17) starts from axioms. STP (a10-a12) trains a conjecturer against a prover. LeanConjecturer (a16, a17) and CPL (a18, a19) use Lean as the checker. These replace the human teacher with a code checker.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Lakatos menu of responses; only lemma-incorporation and monster-adjusting improve the claim | five named responses plus proofs-and-refutations; local vs global counterexamples | a01-a04, c01, c02 | [E] as theory (descriptive, not empirical) |
| Human posing meta-analysis 1 | 13 studies, 14 datasets, N about 1,316. g: knowledge 1.31 [1.04, 1.59]; skill 0.83; ability 0.77; attitude 0.76. Q knowledge 68.12 | Rosli et al. 2014 (a06, b01, b02) | [C] |
| Human posing meta-analysis 2 | 20 studies, N = 2,349. ES: skill 1.328, ability 1.152, knowledge 1.142 (Q = 123.7), attitude 0.643. Published vs unpublished Qb = 50.0 | Kul and Celik 2020 (a07) | [C] |
| Human posing meta-analysis 3 (newer) | 26 studies; g = 0.72 [0.53, 0.90], I2 = 69.2%; pre-post designs 58% larger than controlled; Egger test significant | Zhang et al. 2024 (d13, d14) | [C] |
| Null achievement result in a small trial | N = 44 (20 vs 24); no gain in achievement, gain in motivation | a09 (abstract only) | [S] |
| WIN with scientific approach | N = 68 (34 vs 34); posttest 24.91 vs 18.06; N-gain 0.40 vs 0.21; p < 0.01; even best group at 52% of ideal | Putra et al. 2020 (a08) | [S] |
| Good solvers pose more and richer problems | N = 509 | Silver and Cai 1996 (b03) | [S] correlational |
| Most unexpected posing responses are task misreadings | 74% / 18% / 8% | Ran et al. 2025 (b04) | [S] |
| Self-posing at the edge of ability gives dense training signal | STP: 28.5% vs 13.2% LeanWorkbook; miniF2F 65.0%; ProofNet 23.9%; PutnamBench 8/644; 131 of 2.5M proofs correct on unproved statements vs at least 47% of conjectures proved | Dong and Ma 2025 (a10-a12, b17) | [E] for training |
| Posing loops drift to easy or narrow statements without correction | Minimo no-hindsight collapse (3 domains, 3 seeds); STP mode collapse fixed by seed-lemma rule and Wasserstein reweighting | a14, b18, c17 | [E] |
| Raw conjecture yield after filters | LeanConjecturer 12,289 -> 10,950 -> 4,130 -> 3,776 (31%); 103.25 novel per seed; groups: 40 of 420 unique conjectures survive (9.5%; 27% of the 149 testable) | a16, c09, a20, c03 | [E] |
| Prompt wording changes volume | one seed: 1 total / 0 valid without "as many as possible"; 412 / 392 / 108 non-trivial with it | b07, c10 | [S] |
| Separating conjecturing from proving and keeping verified results | CPL 5/20 vs 0/20 runs found the target; Fisher p = 0.024; 106 vs 328 theorems per run; 14M-token budget | Kasaura et al. (a18, b08) | [S] |
| Verified earlier theorems in context raise later proof success | re-proof 2106/2123 (99%) vs 1935/2123 (91%), McNemar p = 4e-35; target 7/80 vs 0/80 | a19, b09, c14 | [S] same model made them |
| Resampling gives repeated conjectures | 55.5% unique; self-similarity 0.25-0.42 | c04, a20 | [E] |
| Models cannot run their own test code | non-executable code: Gemini 81.86%, Claude 49.44%, GPT-4o 37.76%; 271 of 420 (64.5%) | c03, c05 | [E] |
| Stating the target answer formally is weak | equiv-rfl pass@1 3.28% (GPT-4.1), 3.72% (DeepSeek-V3.1); 0/114 proof-type | Sivakumar et al. (a22, b11, c06) | [C] formal only |
| Hidden answer lowers end-to-end autoformalisation | average drop 23.7%; GPT-4.1 Grader@10 36.32 -> 20.35 | a22, c07 | [E] |
| LEAN-FIRE gain comes from few-shot examples | 13 PutnamBench items (GPT-4.1), 7 (DeepSeek-V3.1); net +3.01% at pass@1 | b12, c08 | [S] |
| Answer finding in natural language is strong, formal proof weak | LLMs above 80% answer accuracy on PutnamBench, formal provers under 10%; 293/340 vs 265/340 with and without self-verification | Liu et al. 2026 (d15, d16) | [E] |
| Open-conjecture resolution by plain agents | OEIS Open: Opus 4.8 30% (147/492), GPT-5.5 26%, Gemini 3.5 Flash 22%; LITE best 44% at $200; $6-10 per conjecture | Adamczewski 2026 (b13, c22) | [S] |
| Extra machinery did not help | 476,000 papers: no change; DeepAgent loop: no change; about +10 points per tenfold spend | b14 | [S] |
| Large Lean agent on open problems | 9/353 Erdos; 44/492 OEIS; Erdos #125 and #741(i) found misstated | Tsoukalas et al. 2026 (b15, b16, c23) | [S] |
| Models write proofs of false claims | best model (GPT-5) 29.0% sycophantic; self-sycophancy up to +15.6 points | Petrov et al. 2025 (b21, b22, c20) | [E] |
| Validate-first prompt helps partly | DeepSeek-V3.1 +34.1% (relative or absolute unclear); best-of-4 -5.4 / -8.6 points; Low@16 -6.4 (one model) | b23, c21 | [S] |
| Models wrongly call a true theorem false | GPT-4o said false 10 of 16 trials; o3 always judged false | c15 | [S] |
| Falsifying is much harder than solving | o3-mini (high) solves about 48.7% but breaks under 9% of wrong solutions; 86% of failed search runs are wrong brute-force code | REFUTE (d01-d03) | [S] |
| Small cases then generalize beats brute force | Claude 3.5 Sonnet 19.21 vs 9.92; GPT-4o 12.88 vs 7.64; interpreter about 2x at 5x cost | MathConstruct (d04, d05) | [S] |
| Counterexample construction is the hard half | ALPS: 2.2% of 4,141 laws solved; best model 14% proof side, 0% construction side | c24 | [E] (4 sources) |
| Counterexamples from models are rare and fake | CounterMATH: R1 F1 80.7; most 7B about 30; strict example-use down to 0.4% | d09 | [S] |
| Authoring hard problems is a different skill from solving | MathDuels: best solver not best author; newest models' problems beat prior top solvers 27.6% (76/275) vs 8.0% (165/2054) | Xu et al. 2026 (a24, b19, c18) | [S] |
| Harder authoring raises invalid-item rate | 5.1% -> 9.5% -> 25.0% over three stages; with code at solve time 3.0 / 6.9 / 21.1%; verifier removed 11 of 570 | a25, b20, c19 | [S] |
| Own variants are sometimes ill-posed | Code2Math: external judge certified 74/90 to 98/98 of internally accepted; human audit 126/127 | d06, d08 | [E] with MathDuels |
| Condition-change variants cut accuracy | average drop 21.73% across 26 models (AMC-23, AIME-24) | RIDE (b24, c25) | [S] |
| Auxiliary lemmas help inference-time provers | Prover Agent: 88.1% miniF2F at 260 samples (64.3% at one); used lemmas 25% special cases, 25% technique, 41.7% subgoals (about 12 lemmas) | d17 | [S] |
| Small-seed self-training does not transfer | LeanConjecturer: 47 -> 50 of 192 solved; 9/14 -> 8/14 held out | a17, b06, c11 | [C] |

## 4. Mechanisms and models

Each mechanism is written so it can be coded. The model only fills slots. The program decides.

### 4.1 Lakatos loop as a state machine

```
state: claim C, proof steps P1..Pn, case set T (every case ever tried), definitions D
loop:
  1. CODE: test C on cases in T plus new generated cases (small cases first)
  2. if all pass: stop, claim survives (record which cases)
  3. else a counterexample x fails:
       CODE: run x through each proof step Pi. Find the first step that fails.
       if step Pi fails but C still holds on x: LOCAL (repair the proof step)
       if C fails on x: GLOBAL
  4. MODEL fills one slot: "which move?"
       - lemma-incorporation: add the condition of the failing step to C
       - exception-barring: add "x is excluded" (flag for audit)
       - monster-barring: propose a new definition D' (REQUIRE explicit D')
       - surrender: drop C, return to step 1 with a new C
  5. CODE: re-test the NEW claim on ALL cases in T (not only x). Count which move was used.
```

Key rule (K01, K02). A redefinition must be written explicitly, and all earlier cases must be re-run under it. Without that, a false claim can be saved silently. No LLM study measures how often this happens (d19). Treat the rule as theory-derived.

### 4.2 What-If-Not (O4) as an operator

```
input: problem with givens g1..gk and goal
1. MODEL: list attributes (givens, goal form, numbers, shape, domain)
2. for each attribute: MODEL writes the negation or variation ("what if g_i is dropped / doubled / 0 / infinite")
3. CODE: ask an independent check that each variant is well-posed (K26)
4. solve each variant (small cases by code where possible)
5. CODE: compare. If an answer is unchanged when the condition changed, flag it (K18)
6. use results as lemmas, special cases or counter-checks for the original
```

Related AI evidence. Learning to Disprove (d11) uses hypothesis deletion on proved theorems to make false statements: 575K instances; multi-reward Qwen3-8B about 49/52/54% pass@1/4/9 vs 43/46/47% single-reward. That is a training result and the paper was rejected from ICLR 2026. RIDE (b24) rewrites conditions to harder variants and finds a 21.73% drop, so condition change exposes memorised forms.

### 4.3 Difficulty-targeted lemma selection (STP, Minimo)

```
for each candidate lemma L (posed by the model):
   run solver K times on L
   p = successes / K
   keep L if 0 < p <= 1/4 and the proof uses the seed lemma     # a11
drop lowest 20% by elegance (minimum length)
```

STP trains on survivors. At inference this is only a design idea. A training-free variant (K05 test) is untested. Minimo adds hindsight relabeling: a failed proof search still yields true statements, which become training targets (a14). Without it the conjecturer collapses to easy statements.

### 4.4 Conjecturing-Proving Loop (CPL)

```
library = []
repeat until budget:
   MODEL: propose conjecture in Lean 4 given definitions + library
   CODE: syntax check and novelty check (exact?)
   MODEL: try to prove
   if proved: library.append(statement, proof)       # S9 log
```

Against single-pass generation (SL): CPL 5/20 vs 0/20 on one target (a18). Verified results in context also made re-proof easier (99% vs 91%), even when not used as lemmas (a19). Caveat: same model, one target, one domain.

### 4.5 Filter funnel for raw conjectures

Parse -> not already known -> not trivial (automatic tactic such as aesop fails) -> test by code on cases -> keep (a16, c09, a20). Plan for 3-10 raw statements per survivor (K07).

### 4.6 Code counterexample search with a sanity gate

REFUTE shows the weak point: 86% of failed random-search runs came from wrong brute-force code (d03). So run the checker on tiny known-true and known-false cases before trusting "no counterexample" (K23). MathConstruct shows small cases then generalize beats pure brute force (d05).

### 4.7 Independent validity gate

Self-posed variants slip through a same-model check (Code2Math up to 18%; MathDuels 5.1-25.0%). Use a second model or a code check and log the rejection rate (K26, K17).

## 5. What holds up

**Replications and agreement.**

- Human meta-analyses agree on direction. Rosli (g 0.76-1.31), Kul and Celik (0.64-1.33) and Zhang (0.72) all report positive effects.
- Self-posing training signal: STP and Minimo agree that difficulty targeting beats attempting unproved targets. Two independent groups (a10-a12, a13-a15).
- Drift to easy or narrow statements: three sources (Minimo, STP, LeanConjecturer context effect) (K06).
- Counterexample construction is hard: ALPS, REFUTE, CounterMATH, group-theory test code failures (K22).
- Own variants need an independent check: Code2Math and MathDuels (K26).

**Failures, caveats and contradictions.**

- Human effects are probably inflated. Effects of 0.8-1.3 are far above typical education effects. Most designs are quasi-experimental, six studies used researcher-made instruments, and heterogeneity is high (Q = 68.12 for knowledge in Rosli; Q = 123.7 in Kul and Celik). Kul and Celik report no publication bias, yet their own published-vs-unpublished moderator is Qb = 50.0. Zhang finds a significant Egger test and 58% larger effects in uncontrolled designs. Zhang's outcome is posing skill, not solving accuracy. A null achievement result exists in a small trial (N = 44, abstract only).
- No isolation of WIN. The only opened WIN-specific study (N = 68) bundles WIN with a scientific-approach lesson and measures posing ability. Zhang lists WIN only as one strategy component.
- Transfer from self-posed training is contested: STP reports 2-3% on external benchmarks; LeanConjecturer moved 47 -> 50 of 192 solved and held-out 9/14 -> 8/14. Different scales and methods.
- CPL is fragile: one theorem, one model, 5 vs 0, p = 0.024. The CPL caveat is that the same model produced the context. No second-target replication exists.
- Agent machinery: OEIS Open found literature access and a sub-agent loop gave no gain, and a basic generate-and-verify agent replicated AlphaProof Nexus on Erdos problems at higher cost on the hardest. This limits how far "loop structure helps" can be pushed (K13).
- Silver and Cai (good solvers pose more) is correlational. MathDuels (best solver is not best author) is LLM-only. They do not conflict, but neither shows posing causes solving.
- LEAN-FIRE: gains came from few-shot examples, not the interleaved reasoning (K12). Removing few-shot removed most gain.
- Misread comparisons. ConjectureBench Table 3 pairs "78.77 seen vs 26.70 unseen" mixes two changes (hidden answer and no few-shot). Use the 23.7% average drop and the baseline 36.32 -> 20.35 as the pure answer-hiding effect (critique item 2).
- BrokenMath "34.1%" for validate-first is ambiguous between relative and absolute.
- OEIS Open Claude Opus 4.8: 147/492 (30%) by one checker, 144/492 (29%) under the Comparator checker. The best LITE score (44%) is from a model run only on LITE. AlphaProof Nexus: paper says 44/492, repo releases 38.

**Moderators.**

- Human: K-12 students gained 89% more than prospective teachers and 96% more than in-service (d14). Publication status moderates (a07). Prior ability: WIN N-gain 0.59 vs 0.34 high, 0.37 vs 0.20 medium, 0.31 vs 0.16 low (a08).
- LLM: sycophancy rises more than 20 points on problems the model cannot solve in original form for most models (b21). Prompt wording ("as many as possible") changed volume from 1 to 412 (c10). Model identity changed non-executable code from 37.76% to 81.86% (c05).

**What worked.**

- Code-based pruning of conjectures (Chuharski): turns 420 unique conjectures into 109 refuted, 40 survivors.
- Difficulty-targeted self-play for weights (STP).
- Hindsight relabeling (Minimo).
- Must-use-seed-lemma rule against mode collapse (STP).
- Small cases then generalize (MathConstruct).
- Independent verifier for posed problems (MathDuels removed 11 of 570; Code2Math external judge).
- Validate-first instruction: partly.
- Verified lemmas as context (CPL, Prover Agent, 2606.28747 in a toy Hilbert system).

**What did not work.**

- Best-of-n, confidence selection and fine-tuning for sycophancy: little (b23).
- More trials and prompt variants for diversity (c04).
- Literature access and sub-agent loops for open conjectures (b14).
- Execution feedback for counterexample search: removed invalid-input errors but did not raise true success except for DeepSeek-R1 (d03).
- Code at solve time in MathDuels: error only 25.0% -> 21.1% (b20).
- Counterexample hint prompt alone: about +1.4 F1 in CounterMATH (39.7 vs 38.3) (d10).

## 6. Language models

**Posing and conjecturing.**

- Raw output is low-yield. LeanConjecturer: 31% of generated are novel and non-trivial (3,776 of 12,289). In group theory, 40 of 420 unique conjectures survive (27% of the 149 testable); 271 had code that would not run.
- Early models (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Flash) had 37.76-81.86% non-executable test code. A small o1 run (51 conjectures) did much better: 22 survived (43%), 28 failed, 1 not run. The authors say the sample is too small for strong claims (a21).
- Diversity is low from resampling: 55.5% unique, self-similarity 0.25-0.42. More trials did not help.
- Stating the target in formal form is weak (3.3-3.7% strict match), but this is mainly a formal metric. In natural language the answer is found at above 80% on PutnamBench (d15). So answer-first guessing is not weak for natural-language problems.
- Hiding the answer is a real difficulty change (23.7% drop). Leaving it visible invites rfl-style cheating proofs (d16).

**Training on self-posed problems.** STP: LeanWorkbook 13.2% -> 28.5%. Transfer to external benchmarks about 2-3%. LeanConjecturer: no transfer on 14 held-out problems. Code2Math SFT: +4.5 and +4.7 AIME points; CounterMATH SFT: AIME24 20.0 -> 30.0 (3 problems of 30, one run). All are weight training, not usable for a no-training agent.

**Inference-time conjecturing and lemma use.**

- CPL (o3, 14M tokens): 5/20 vs 0/20 on one target. In-context verified theorems: 99% vs 91% re-proof.
- Prover Agent (training-free): 88.1% miniF2F-test at 260 samples, 64.3% at one sample. Lemma value cannot be separated from extra samples.
- OEIS Open (frontier plain agents with Lean checking): 22-30% of 492 open conjectures at a $50 cap, 44% of the 100-item LITE at $200. Solve rate rises about 10 points per tenfold spend with no plateau. Elaborate scaffolds gave nothing.
- Tsoukalas: 9 of 353 Erdos problems; 44 of 492 OEIS. Attempting to prove or disprove exposed misstatements in Erdos #125 and #741(i).

**Refutation.**

- Sycophancy: GPT-5 (best) writes a proof of a false statement 29.0% of the time. Self-sycophancy up to 15.6 points worse. Validate-first prompt helps partly; best-of-4 lowers it by 5.4 and 8.6 points.
- Opposite error: GPT-4o called a true theorem false in 10 of 16 natural-language trials; o3 always did (c15).
- Falsifying code: o3-mini (high) breaks under 9% of wrong solutions while it solves about 48.7%. Random-search prompting yields 3.7-8.3% (R1 4.0%, V3 4.0%, Flash Thinking 3.7%, o3-mini 8.3%). With an oracle solution: V3 15.1%, Flash 7.7%, R1 9.9%.
- CounterMATH: strict example use down to 0.4%; DeepSeek-R1 F1 80.7 vs about 30 for 7B models.
- ALPS: construction side 0% for the best reasoning model.
- MathConstruct: interpreter doubles accuracy at about 5x cost; Claude 3.5 Sonnet 5% -> 18% in one reading.
- ProbeGen (d12): an LLM that proposes inputs and sees output disproved 18% of samples the benchmark tests judged equivalent.

**Authoring.** MathDuels: 19 frontier models authored 570 problems. Best solver (GPT-5.4-high) had solver rating 2268 and author rating 1473; Gemini-3.1-Pro-high had solver 2214 and author 1624. 39% of valid problems were solved by every non-author. Error rates rose from 5.1% to 25.0% as authoring got harder. Code2Math: seeds to evolved variants dropped GPT-5.2-High from 70% to 64% / 61%; an external judge rejected up to 18% of internally accepted variants.

**What changed results, and by how much.**

| Lever | Change | Source |
|---|---|---|
| Hide the answer | -23.7% average end-to-end | c07 |
| Few-shot examples in conjecture prompt | most of LEAN-FIRE's +28% pass@10 | b12 |
| Verified lemmas in context | 91% -> 99% re-proof; 0/80 -> 7/80 on target | b09 |
| Separate conjecture and proof loop | 0/20 -> 5/20 runs | b08 |
| Run code on conjectures | 420 unique -> 109 refuted, 40 survive | c03 |
| Python interpreter on construction | about 2x at 5x cost | d04 |
| Small cases then generalize | 9.92 -> 19.21 (Claude 3.5 Sonnet) | d05 |
| Validate-first prompt | partial; unclear unit | b23 |
| Self-verification on answers | 265 -> 293 of 340 | d16 |
| Tenfold spend | about +10 points | b14 |
| Lit access / sub-agent loop | 0 | b14 |
| Condition change (RIDE) | -21.73% accuracy | b24 |
| Counterexample hint prompt alone | about +1.4 F1 | d10 |

**Overall limits.** Almost all LLM evidence is formal with a checker. Almost none is natural-language competition solving, which is what our agent does. LLM judges decide validity in MathDuels, BrokenMath and ConjectureBench. Contamination signs appear in ConjectureBench; benchmark overlap is a risk in STP. miniF2F-Hard in DAP was at 194 of 194 at every setting, possibly contamination.

## 7. What our agent should take

Schema parts: G guardrails, S states, O operators, memory. Evidence ids refer to evidence_a-d.jsonl.

### Add now (established [E])

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | **Code, not the model, decides whether a posed claim or variant survives.** Test by running small cases, not by asking the model if the claim is true. Models are wrong in both directions (write proofs of false claims; call true theorems false). | G3, G5, G8 | [E] K14, K08 pruning part | b21, b22, c15, c20, c03, a20 |
| 2 | **Filter funnel for self-posed items:** well-formed, not already known, not trivial, then test. Budget 3-10 raw items per survivor. | S3/S4 (open mode), G5 | [E] K07 | a16, c09, a20, c03 |
| 3 | **Triviality and spread filter on any self-posing loop.** Loops drift to easy or one-topic items. Add a must-use-the-seed rule. | G4, G5 | [E] K06 | a14, b18, c17, c12, a11 |
| 4 | **Do not use resampling for diversity of conjectures or variants.** Use named operators (O1-O8). One model repeats itself. | G4, S3 | [E] K20 | c04, a20, b18 |
| 5 | **Independent validity check on every self-posed variant** (second model or code), and log the rejection rate. A same-model check lets up to 18% through. | G3 | [E] K26 | d06, d08, b19, b20 |
| 6 | **Hiding vs leaking the target.** Keep the stated answer out of the problem the model sees (S1 input hygiene), and mark items with leaked targets so they are not scored. | S1, G1 | [E] K25 | d15, d16, b10, c07 |
| 7 | **Building the counterexample is the hard half.** Treat "no counterexample found" as weak evidence. Require the check code to pass a gate on tiny known-true and known-false cases before it is trusted. | G8, S4 | [E] K22 (gate itself is [S] K23) | c24, d01-d03, d09 |
| 8 | **Revise from a located failing case, never from opinion.** The counterexample drives the repair; code locates the failing step. Matches the Lakatos local vs global split. | S5, G2 | [E] K01 | a02, a04, c01, c02 |

### Test first (single-source or contested; nothing below goes into SCHEMA.md until a test passes)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 9 | **Explicit-redefinition rule:** when a revision changes a term, the model must write the new definition and code re-runs all earlier cases (blocks monster-barring rescue). | G3, S5 | [S] K02 | a03, c02 |
| 10 | **What-If-Not operator O4 as a structured procedure** (list givens, negate each, solve variants, compare). No LLM test exists. | O4 | [S] K04 | a08, a26, d13 |
| 11 | **Flag answers that stay unchanged when a condition changes** (memorised solution forms). | O4, S8 | [S] K18 | b24, c25 |
| 12 | **Small cases then generalize** before proving, on pattern problems. | O1, O4 | [S] K24 | d04, d05 |
| 13 | **Specialize-first step:** special cases of the claim as auxiliary lemmas (25% of used lemmas in Prover Agent). | O1 | [S] K27 | d17 |
| 14 | **Code counterexample search before proving** on conjecture-type items. Gain is contested because it depends on correct brute-force code. | G3, G8, S4 | [C] K08 | d01-d05, c03, d12 |
| 15 | **Verified-findings log in context (S9)** vs none, on related problem sequences. | memory, S9 | [S] K09, K10 | a18, a19, b09, d17, d18 |
| 16 | **Pass-rate band lemma filter (0, 1/4] at inference** as a subgoal filter without training. | G12, S6 | [S] K05 (training part [E]) | a11, a12, a10 |
| 17 | **Restate before posing** to reduce misreading. | S1 | [S] K19 | b04 |
| 18 | **Validate-first instruction** before attempting a proof. | G1 | [S] K15 | b23, c21 |
| 19 | **Examples of posed-and-refuted conjectures** vs a structured procedure. | 4b risk | [S] K12 | b12, c08 |
| 20 | **Separate conjecture slot before solving** (answer-first). Natural-language answer-first is strong; formal restatement is weak. | S1/S2 | [C] K11 | a22, b11, d15 |
| 21 | **Bare generate-and-verify loop** vs the full scaffold at matched spend. | G7 | [S] K13 | b13, b14, c23 |

**Do not take (see section 9):** training-based gains (K21), human posing effect sizes (K03, K28), any claim that posing practice raises accuracy.

## 8. Concrete tests on our bench

All arms at equal tokens. Run at least 3 seeds. Items are natural-language competition-style problems unless stated.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 60 competition problems where one given can be dropped to a simpler solvable variant, plus 20 "find the answer" problems | (a) plain solve; (b) restate-and-check; (c) O4 What-If-Not (list givens, negate each, solve up to 3 variants, flag unchanged answers) | accuracy; fraction of variants rejected by an independent check; precision of unchanged-answer flags | O4 above restate-and-check by 2-5 points if it works; null likely on easy items (G11) |
| T2 | 60 pattern or conjecture problems (sequences, counts, extremal) | (a) model-judged truth then prove; (b) code counterexample search on small cases first, with sanity gate on known-true/false; (c) same but no sandbox | accuracy; false-pass rate of "no counterexample" | (b) above (a) by 5-10 points; gate lowers false pass; (c) shows how much gain is lost without code |
| T3 | 40 seeded true/false claims (counterexample known) | (a) model judge; (b) validate-first; (c) code check | error in both directions (proof of false; calls true false) | code check under 10% error; validate-first partial |
| T4 | 30 tasks with a seeded counterexample that tempts redefinition | revise with vs without the explicit-redefinition-and-retest rule | rate of rescue-by-redefinition; final claim correctness | rule cuts false rescues; no prior rate exists, so first measure the baseline |
| T5 | Sequences of 5-8 related problems | (a) no log; (b) verified-findings log (S9) of the model's own checked results; (c) log of easy re-proofs only | accuracy on later items | (b) above (a) by 3+ points if the CPL effect holds; (c) tests the CPL caveat |
| T6 | 80 hard items | (a) solve target directly; (b) generate sub-lemmas, keep pass rate in (0, 1/4] over K=4 samples, then solve | accuracy; tokens spent on filtering | break-even or small gain; check cost of the pass-rate estimate |
| T7 | 50 problems with 2 to 4 variants each | same-model check vs independent-model check vs code check of well-posedness | ill-posed rate that passes; rejection rate | same-model check leaves 5-18% ill-posed |
| T8 | 40 problems with target answer stated vs hidden | answer shown vs hidden | accuracy shift; count of circular answers | shift near 20% as in ConjectureBench; flags leaks in our own benches |
| T9 | 60 pattern problems | direct prove vs compute small cases then conjecture then prove; with and without code sandbox | accuracy | gain like MathConstruct (about 2x on a low base); drops without sandbox |
| T10 | 40 tasks with a failing check | log which Lakatos move (lemma-incorporation, exception-barring, monster-barring, surrender) is chosen; compare with barring moves blocked | move distribution; final accuracy | first measure; barring-blocked wins if barring rescues false claims |

## 9. What does not transfer, and why

- **Human posing effect sizes (g 0.72 to 1.31).** Outcomes are posing skill, attitude and researcher-made tests, not solver accuracy. Designs are quasi-experimental and heterogeneous. Humans learn from practice over days; our agent does not train. Use as a prior only (K03, K28).
- **Self-posing as training signal.** STP, Minimo, LeanConjecturer and Code2Math change weights. The key mechanism, a sparse reward made dense by difficulty targeting, does not exist at inference. Only the selection rule (pass-rate band) might carry over, and that is untested.
- **Formal-checker results.** Lean and Isabelle give a perfect checker. In natural language our checker is code on cases or a second model. Conjecture yield and counterexample results may not carry over.
- **Open-conjecture results.** OEIS Open and Erdos tasks are about statements with no known answer and a large budget ($50-$200 per item). Our items have known answers and a small token cap.
- **Lakatos.** It is a rational reconstruction, not a measured procedure. The menu is a good label set, not a proven control policy. Some moves (monster-barring) are legitimate refinement in mathematics, so blocking them might hurt (a03).
- **Authoring skill.** MathDuels measures how hard a posed problem is for others. Our agent poses variants for itself. The relevant result is only the ill-posed rate (5.1-25%).
- **Heavy agent machinery.** Literature access and sub-agent loops gave no gain at OEIS scale (b14). Do not add either on the strength of "agents conjecture well".
- **Reasoning text.** Models can narrate a Lakatos-style repair without performing one (G10). Judge by the checked output.

## 10. Open questions

1. Does a What-If-Not operator beat a plain restate-and-check step at equal tokens on natural-language problems? No LLM test exists (K04).
2. Which counterexample move do LLMs make when a check fails: lemma-incorporation or monster/exception-barring? No measured rate exists (K01, K02).
3. How much of the code-search gain survives when no sandbox is available? REFUTE and MathConstruct suggest much is lost, but the exact ablation was not found.
4. Does CPL replicate on a second target and on natural-language problems? How much does the same model re-proving its own easy results explain (K09, K10)?
5. Can the pass-rate band (0, 1/4] work as a training-free subgoal filter, and what K is cheap enough (K05)?
6. How much of the human posing effect survives in unbiased designs? Larsen and Zandieh's guided reinvention and the WIN geometry studies (EJ1186756, EJ1301417) were not re-read.
7. Does few-shot of posed-and-refuted conjectures beat a structured procedure, and does it depend on model strength (K12)?
8. How often is a wrong early conjecture or answer kept despite later evidence, in natural language?
9. Is the author-solver gap in MathDuels a real skill split or partly ill-posedness?
10. Does leaked or hidden target text in our own benches shift scores by an amount like the 23.7% in ConjectureBench?
11. Is the unit of the BrokenMath validate-first gain (34.1%) relative or absolute?
12. Primary texts not opened: Brown and Walter books, Lakatos Part II and the 1976 book (a26, b25, b26).

## 11. Sources

[V] = opened and read (per the evidence files). [M] = snippet or abstract only.

**Human and theory**

- [V] Lakatos (1963) Proofs and Refutations (I), BJPS 14(53):1-25 (Part I only). https://matthewjbrown.net/teaching-files/hps/lakatos.pdf ; https://www.jstor.org/stable/685430 (a01-a05, c01)
- [V] Martin and Pease (2013) Mathematical practice, crowdsourcing, and social machines. https://arxiv.org/abs/1305.0900 (c02)
- [V] Rosli, Capraro and Capraro (2014) Effects of problem posing on student mathematical learning: a meta-analysis. https://files.eric.ed.gov/fulltext/EJ1071265.pdf ; https://doi.org/10.5539/ies.v7n13p227 (a06, b01, b02)
- [V] Kul and Celik (2020) Meta-analysis of problem posing strategies. https://files.eric.ed.gov/fulltext/ED611731.pdf (a07)
- [V] Zhang, Stylianides and Stylianides (2024) Enhancing mathematical problem posing competence. https://doi.org/10.1186/s40594-024-00507-1 (d13, d14)
- [V] Putra, Herman and Sumarmo (2020) Scientific approach and What-If-Not. https://files.eric.ed.gov/fulltext/EJ1239283.pdf (a08)
- [M] Problem posing learning model, cubes and cuboids (2020). https://arxiv.org/abs/2002.04447 (a09; abstract page only)
- [M] Silver and Cai (1996) Arithmetic problem posing by middle school students. https://doi.org/10.5951/jresematheduc.27.5.0521 (b03; Crossref abstract)
- [V] Ran, Cai, Muirhead and Hwang (2025) Unexpected responses in problem posing. https://doi.org/10.1007/s10649-025-10399-9 (b04; not re-opened in cross-check)
- [M] Brown and Walter (1983/2005) The Art of Problem Posing; What-if-not. https://eric.ed.gov/?id=ED251290 (a26, b25; not opened)
- [M] ERIC WIN dynamic geometry studies. https://eric.ed.gov/?id=EJ1186756 (a27; titles only)
- [M] Lakatos (1976) Proofs and Refutations, book (b26; background only)

**LLM and AI**

- [V] Dong and Ma (2025) STP. https://arxiv.org/abs/2502.00212 (a10-a12, b17, b18, c16)
- [V] Poesia et al. (2024) Minimo. https://arxiv.org/abs/2407.00695 (a13, a14, c17; a15 numbers not extracted)
- [V] Onda et al. (2025) LeanConjecturer. https://arxiv.org/abs/2506.22005 (a16, a17, b05-b07, c09-c12)
- [V] Kasaura et al. (2026) Conjecturing-Proving Loop. https://arxiv.org/abs/2509.14274 (a18, a19, b08, b09, c13-c15)
- [V] Chuharski, Rojas Collins and Meringolo (2024) Mining math conjectures from LLMs. https://arxiv.org/abs/2412.16177 (a20, a21, c03-c05)
- [V] Sivakumar et al. (2025) Conjecturing: an overlooked step (ConjectureBench). https://arxiv.org/abs/2510.11986 (a22, a23, b10-b12, c06-c08)
- [V] Xu, Jin, Arya and Naik (2026) MathDuels. https://arxiv.org/abs/2604.21916 (a24, a25, b19, b20, c18, c19)
- [V] Adamczewski (2026) OEIS Open. https://arxiv.org/abs/2608.11941 (b13, b14, c22)
- [V] Tsoukalas et al. (2026) AI-driven formal proof search. https://arxiv.org/abs/2605.22763 (b15, b16, c23; abstract and introduction only for c23)
- [V] Petrov, Dekoninck and Vechev (2025) BrokenMath. https://arxiv.org/abs/2510.04721 (b21-b23, c20, c21)
- [V] RIDE (2025) Difficulty evolving perturbation. https://arxiv.org/abs/2511.04120 (b24, c25; 21.73% not re-opened)
- [V] Xie, Ye and Zhang (2026) ALPS. https://arxiv.org/abs/2608.15979 (c24; 2.2% and 14% not re-opened)
- [V] Sinha et al. (2025) REFUTE. https://arxiv.org/abs/2502.19414 (d01-d03)
- [V] Balunovic et al. (2025) MathConstruct. https://arxiv.org/abs/2502.10197 (d04, d05)
- [V] Guo et al. (2026) Code2Math. https://arxiv.org/abs/2603.03202 (d06-d08)
- [V] Li et al. (2025) CounterMATH. https://arxiv.org/abs/2502.10454 (d09, d10)
- [V] Li et al. (2026) Learning to Disprove. https://arxiv.org/abs/2603.19514 (d11)
- [V] Allamanis and Yin (2025) Disproving program equivalence (ProbeGen). https://arxiv.org/abs/2502.18473 (d12)
- [V] Liu et al. (2026) Discover and Prove. https://aclanthology.org/2026.acl-long.3.pdf (d15, d16)
- [V] Baba et al. (2026) Prover Agent. https://arxiv.org/abs/2506.19923 (d17)
- [V] Ota, Osa and Harada (2026) Self-supervised theorem discovery in a formal axiomatic system. https://arxiv.org/abs/2606.28747 (d18; no exact values in text)
- [V] Gap search log (d19).

*Cross-check (critique.md) re-opened the main numbers for STP, CPL, LeanConjecturer, Rosli, Kul and Celik, MathDuels, BrokenMath and OEIS Open and found them exact, with the corrections noted in section 5.*
