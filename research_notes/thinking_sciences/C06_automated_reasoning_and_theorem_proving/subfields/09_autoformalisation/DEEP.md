# Autoformalisation: deep document

*Subfield C06.09. Text to formal statement. Founding work: Wu et al. 2022. Sources: evidence_a-d.jsonl (ids a01-a29, b01-b32, c01-c34, d01-d21), claims.jsonl (K01-K29), critique.md. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Autoformalisation means turning a natural-language statement (a theorem, a rule, a requirement, a puzzle) into a formal one that a machine can check. The formal target can be a proof assistant (Isabelle, Lean 3, Lean 4, Coq, Mizar), a logic (first-order logic, temporal logic), a solver input (SAT/SMT, PDDL, Prover9, constraint programs), or a code specification (Dafny postconditions, Lean specs).

Three distinct jobs sit under the name:

1. **Statement autoformalisation.** Informal statement in, formal statement out. Example: a MATH problem into an Isabelle lemma. The output is judged on faithfulness, not on truth.
2. **Proof autoformalisation.** Informal proof in, formal proof or proof sketch out (Draft, Sketch, Prove).
3. **Reasoning by formalisation.** The model translates a problem into a solver language, and a symbolic engine does the reasoning (LINC, Logic-LM, SatLM, LLM+P). Translation is the step that can go wrong.

The reverse direction, informalisation (formal to text), is also studied. It is much easier. It is used to make training data and as a round-trip check.

Why it matters for our agent. The schema (S2 REPRESENT, S4 TEST, S8 VERIFY, G2, G3, G5) wants checks that code can run. Formalisation is the strongest way to get such a check, but only if the formal statement says what the text says. The central lesson of the field: a formal statement that compiles is not a faithful statement. The agent needs a meaning check that does not rely on the compiler alone.

Scope notes. Training pipelines (Herald, Goedel-Prover, ATLAS, Lean Workbook) are covered as evidence on difficulty and errors. We do not train, so training results are motivation only. Neighbouring subfields researched in parallel (constraint satisfaction, argumentation and defeasible rules, RL on verifiable rewards, probabilistic programming, modal and epistemic logic, forward and backward reasoning, evidence and probability reasoning) are only linked, not covered.

## 2. History and theories in depth

**Pre-LLM roots (2018-2020).** Wang, Kaliszyk and Urban (2018) ran the first neural translation experiments from LaTeX to Mizar-style text [M, a27, not read]. Szegedy (2020) argued that autoformalisation could unlock self-improving reasoning systems [M, a28, not read]. This position paper is the framing most later papers cite. Its claim: if machines can read the large informal literature and formalise it, formal provers get unlimited training and checking material.

**Founding LLM study: Wu et al. 2022 (a01-a05, b01-b04, c01-c04).** Few-shot Codex and PaLM, no fine-tuning, translated MATH competition problems into Isabelle. The authors estimated Codex saw under 0.18% Isabelle data. Result: a human check of 150 random MATH problems (50 algebra, 50 number theory, 50 intermediate algebra) found 38 perfect translations, 25.3%. Failure analysis showed most failures were concept misalignment, not syntax. BLEU rose with PaLM scale (8B to 540B) and Codex beat PaLM 540B, probably from more code pretraining. The paper also showed the payoff: 3,908 autoformalised MATH statements, 3,363 syntactically correct, were used for expert iteration of a neural prover, lifting miniF2F from 28.3/29.9 (valid/test) to 37.3/35.2.

**Parallel threads, 2022-2023.**
- *Proof sketches.* Draft, Sketch, and Prove (Jiang et al. 2022) turned informal proofs into formal sketches with gaps closed by Sledgehammer (a06-a08, b29, c05-c06). Test 39.3% with human drafts versus 29.9% for the best neural baseline Thor.
- *Undergraduate level.* Agrawal et al. (2022) used input-dependent prompt selection with Codex on Lean (b20, b21). ProofNet (Azerbayev et al. 2023) gave 371 undergraduate problems and showed the jump in difficulty from competition level (a09, a10, b05-b07, c08-c09).
- *Logic and solvers.* Logic-LM, LINC, SatLM, LLM+P and nl2spec moved the idea out of mathematics (a22, a23, b25-b28, c25-c28, c31, d12). Here the formal artifact is a solver input.
- *Code.* Clover and nl2postcond treat formal specs as checks on code (c32, d02, d15).

**Data engines, 2023-2025.** MMA (332K pairs by informalising Isabelle and Lean libraries with GPT-4; a11, b13, c10), Lean Workbook (active-learning loop; a17, b14, b15, c11), FormL4 with compiler-based process supervision (a12, b19, c12), Herald (hierarchical informalisation of Mathlib; a25, b16-b18, c19), Goedel-Prover (1.64M statements; a18, c20, c21), ATLAS (c22), FormalMATH (b32, c17, c18, d21), StepFun-Formalizer (d08). Pattern: autoformalised data trains provers, and prover scores go up.

**Evaluation turn, 2024-2026.** The field found that its own yardsticks were weak.
- Poiroux et al. built BEq+ (symbolic equivalence), ProofNetVerif (3,752 human-labelled pairs), ProofNet# (corrected) and RLM25 (research level) (a14-a16, b08-b12, c13-c15).
- FormalAlign trained a 7B alignment scorer (a13, b23, c23).
- 2025-2026 papers measured compile-versus-faithful gaps with LLM judges and experts: Mathesis/LeanScorer (d01), Beyond Compilation (d04), Signal-Coverage Matrix (d05), SHADOWBENCH (d06), epistemic ensemble judging (d07).

**Competing views.**
- *Autoformalisation as translation.* The text has a fixed meaning; the model must map it. Failure is mismatch. Evidence: BLEU, back-translation, alignment scorers.
- *Autoformalisation as knowledge retrieval.* Many errors are missing or hallucinated library items. Evidence: retrieval helps (b22, d11); hallucinated Mathlib identifiers are 34-50% of paraphrase failures (d09); the "linear f" case (a03).
- *Autoformalisation as underspecified design.* Informal text hides assumptions and conventions, so several formal statements can be legitimate. Evidence: human reviewers disagree (kappa 0.18-0.28, pairwise 68-70%; d04, d07). Gold labels are themselves wrong (31.8% of ProofNet Lean 4 port entries, b10).
- *Formalise versus just reason.* Neurosymbolic work claimed solvers beat CoT. Later work with reasoning models found formalising loses in most pairs (d13). Contested (section 5).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Few-shot Codex formalises a quarter of competition statements perfectly | 38 of 150 = 25.3% (13/17/8 by subject: algebra, number theory, intermediate algebra) | Wu 2022 (a01, b01) | [E] 2022 model only; no modern rerun (gap 7 open) |
| Failure types on Wu's 150 | Fail to align definitions 10/18/18; wrong function use 6/13/16; missing assumption 8/9/9; syntax/type 7/2/11; missing Isabelle definition 0/12/3; unclear prompt 9/3/14 | Wu 2022 (b01, c02) | [E] |
| Scale and code pretraining raise BLEU | Algebra/number theory: PaLM 8B 31.49/22.10; 64B 43.13/31.43; 540B 50.30/36.16; Codex 57.13/43.33 | Wu 2022 (a02) | [E] BLEU is a weak metric |
| Autoformalised statements improve a prover | miniF2F valid/test 28.3/29.9 to 36.1/34.0 (iter 1) to 37.3/35.2 (iter 2); proofs found 782 of 3,363 then 1,011 | Wu 2022 (a04, b03) | [E] |
| Back-translation (formal to text) is easy | 76% (29 of 38) more or less correct; 36 of 38 coherent; ProofNet informalisation 62.3% vs formalisation 13.4% | Wu 2022; ProofNet (a05, b04, c09) | [E] |
| Plain few-shot fails at undergraduate level; retrieval rescues it | ProofNet 371 Lean 3: few-shot Codex typecheck 4.3%, accuracy 0; prompt retrieval 23.7% typecheck, 13.4% accuracy; distilled back-translation 45.2% typecheck, 16.1% accuracy | ProofNet (b05-b07, c08) | [E] measured against a faulty reference set (31.8% errors in Lean 4 ports) |
| Type-check is a weak proxy | 45.2% typecheck vs 16.1% accuracy; benchmark-level Pearson with human accuracy 0.655 (typecheck) vs 0.974 (BEq+) over 65 points | ProofNet; Poiroux (b06, b08) | [E] |
| Compile-vs-faithful gap in 2026 | Gap 1.3 to 29.5 points across 8 systems (227 statements); agent compiles 87.2%, accepted 57.7%; SA-PASS: 61.8% compile vs 11.2% aligned on research level (178 problems) | Beyond Compilation; SHADOWBENCH (d04, d06) | [E] |
| Public benchmark errors | 118 of 371 (31.8%) Lean 4 ProofNet port entries wrong; Lean Workbook sample 93.5% accurate; E3 checker false negatives about 15.8% | Poiroux; Lean Workbook; LeanEuclid (b10, b14, a19) | [E] |
| Sampling plus type-check filter plus selection | GPT-4o ProofNet# 31.0% to 45.1% (50 samples); Llemma 7B BEq+ pass@n 4.11% (n=1) to 40.54% (n=1000); GPT-4 pass@1 to pass@10 gap 19.5-26.5 points | Poiroux; Li 2024 (a15, c14, a20) | [E] |
| Symbolic-equivalence selection vs simple selection | Poiroux: no better than Self-BLEU or majority vote. Li 2024: SymEq best 1@k 46.1% (Codex, MATH), 41.1% (GPT-4, miniF2F); SemCo adds 0.8-3.9 points | Poiroux; Li (a15, a20) | [C] |
| Equal calls: retry vs sample-filter vs typed-IR | 4 calls, DeepSeek V4-Pro, ProofNet# n=186: true successes 131 / 131 / 129 vs 95 one-shot; type-only error recovery 23 of 61 for every method | Signal-Coverage Matrix (d05) | [S] calls, not tokens |
| Compile feedback fixes type errors, not meaning | About 64% of gain is type-stratum recovery; semantic errors flat on net (14 of 16 rescued, 8 new created); GPT-4o refinement helps, DeepSeekMath-7B hurt by binary feedback | d05; Zhang 2025 (a24) | [E] |
| Critic in the loop | Kimina-7B human accuracy: single pass 38.0%, compiler loop 54.0%, compiler plus CriticLeanGPT loop 84.0% (N=100 sample); 500 problems: 12.6% first try, 52.8% within 200 attempts | CriticLean (a26) | [S] authors' own critic |
| Context in the prompt | RLM25 (619 pairs): GPT-4o BEq+ 1.50% (12-shot) vs 20.64% (full file) vs 24.56% (file minus proofs) vs 17.20% (minus theorems and proofs); Llemma 34B 0.79 / 25.99 / 30.33. miniCTX: GPT-4o 11.72% to 27.08% with file context | Poiroux; miniCTX (b12, d10) | [E] |
| Dependency hallucination | Retrieval precision/recall 0.8-0.9 (DDR) vs 0.2-0.5 (prompted); hallucination 0.22-0.36 per sample vs about 0 | Wang 2025 (d11) | [S] |
| Fine-tuning on formal data does not always transfer | MMA and Lean Workbook models did not beat base on RLM25; MMA lifts LLaMA-33B from 0% to 16-18% acceptable on 100 problems | Poiroux; MMA (b12, a11) | [C] |
| Real-world definitions are harder | GPT-4o success 13.78 points lower and first error 31.90 points earlier than on miniF2F-Test | Zhang 2025 (a24) | [S] |
| Prompt sensitivity | "linear f" case: wrong without example, perfect after one tangential example. Lean 4 fixed prompts: none of 15 completions elaborated in a worked example. Paraphrase surface consistency 19.1-49.5% (ProofNet#), 44.5-55.5% (miniF2F) | Wu; Agrawal; Lou (a03, b20, d09) | [E] (paraphrase figure [S]) |
| Frontier failure types, 2026 | DeepSeek V4-Pro, ProofNet#, n=186: type-only 61, semantic-only 16, both 14, success 95 | d05 | [C] one model, one benchmark |
| Semantic slips are real but few | Examples: hard-coded field size, Summable for a limit, reversed inequality, dropped hypothesis, iff vs one direction | d05, d08 | [E] |
| Round-trip vs other judges | On Gaokao-Formal human labels: re-informalisation precision 93, recall 50, F1 0.65; LLM judge 73/100/0.85; LeanScorer 94/89/0.92. Clover: 0 false accepts on 240 adversarial code variants, accepts up to 87% of correct | Mathesis; Clover (d01, d02) | [C] |
| LLM judges vs experts, 2026 | Two cross-family judges plus compile: 54 of 59 = 91.5% (CI 81.6-96.3) with human majority; SA-PASS 98.8%; FormalAlign 65.0% vs GPT-4o 47.5% vs humans 79.58% (kappa 0.49, N=80) | d04, d06, a13 | [C] small samples |
| Human labels are noisy | Reviewer kappa 0.18-0.28 (d04); human-human pairwise 70.00% (miniF2F), 68.67% (ProofNet); exact match 38.00% and 22.00% | d04, d07 | [E] |
| Formalise-then-solve on logic | ProofWriter: LINC GPT-4 98.3%, GPT-3.5 96.4%; FOLIO GPT-4 LINC 72.5% vs CoT 75.3% (McNemar p=0.58); Logic-LM GPT-4 PrOntoQA 83.2 vs CoT 98.79; SatLM GSM-Sys 69.4 vs CoT 46.5 | LINC; Logic-LM; SatLM (a23, c25, c27) | [E] mixed |
| Formalise vs solve with reasoning models | Formaliser below solver in 12 of 16 reasoning-model/dataset pairs, 4 of 8 non-reasoning pairs (abstract says 15 of 24) | Chen 2025 (d13) | [S] |
| Errors of symbolic and CoT overlap little | Similarity 0.14-0.22 vs 0.52-0.56 among in-context methods | LINC (b26) | [S] |
| Syntax errors fall with model size | FOL syntax errors 38% StarCoder+, 24% GPT-3.5, 13% GPT-4 | LINC (c29) | [E] |
| Verify answers by formalising | DTV average solve: single sample 42.8, majority vote 61.5, DTV 65.0 (Minerva 62B), 68.2 (GPT-3.5 formalising); GSM8K 79.4 vs 67.2 | DTV (a21, c24) | [S] |
| Informal drafts help formal proofs even when wrong | DSP: 39.3% test; 50 checked Minerva drafts: 29 correct, 21 wrong yet still gave proofs; no prover costs 9.0-9.8 points; no informal draft costs 3.7/5.3 | DSP (a06-a08) | [E] |
| Specs from text for code | nl2postcond GPT-4 correct postconditions @1/@5/@10 0.32/0.57/0.66 (prompt 1); 64 real Defects4J bugs caught. Verina best o3: code 72.6%, spec 52.3%, proof 4.9% | d15, d14 | [E] |
| Planning with a solver | LLM+P: GPT-4 direct planning mostly 0% in most of 7 IPC domains; about 90% in Blocksworld with PDDL solver; fails without an example problem file | LLM+P (d12) | [S] |
| Temporal logic with interaction | nl2spec 36 expert instances: Codex minimal 44.4%, with in-distribution examples 58.3%, interactive 86.11% (31 of 36) | c31 | [S] |
| Competition benchmarks saturate | Herald miniF2F-test 93.2% (abstract) or 96.7% (body); graduate level 22.5-23.5%; ATLAS ProofNet pass@1 39.46% vs Herald 31.43% | Herald; ATLAS (a25, c22) | [E] self-reported; versions disagree |
| Cost of validated statements | FormalMATH: 6.89 USD per statement, 12 annotators, 22 days; 72.09% kept at human stage; 21.7% of starting problems end in set | d21 | [S] human cost only |
| Contamination | Putnam-AXIOM: best model 41.9% on originals, minus 19.6 points (46.8% relative) on fresh variants. No fresh-problem autoformalisation test found | d19, d20 | [S] indirect |

## 4. Mechanisms and models

These are the working parts an engineer can build. Each is tied to evidence.

### 4.1 Plain few-shot translation
Prompt: k worked pairs (informal, formal) plus the new informal text. The model emits the formal text. Wu 2022 used 10 pairs per subject. This gives 25% perfect on competition level and about 0% on undergraduate Lean without retrieval (b05). Output depends heavily on which examples are in the prompt (a03, b20).

### 4.2 Retrieval-augmented translation (memory)
- Draft a formalisation, embed it, fetch the 4 nearest library statements from Mathlib (90,530 in the base) and add them to the prompt (ProofNet; b05).
- MS-RAG: BM25 top-3 exemplars per input, denoising and syntax-error feedback. Mistral 7B with MS-RAG beat Mixtral 8x7B with fixed prompts (b22).
- Dependency retrieval: have the model write candidate dependency names, then check each name against the library with an exact lookup (suffix array). This gave precision and recall 0.8-0.9 and near-zero hallucinated names (d11).
- Implementation note: the library lookup is a code step. The model proposes names; code accepts only names that exist. This is G2 and G5 in practice.

### 4.3 Context packing
Give the file or blueprint context: definitions and lemma statements preceding the target. Drop proofs (they add length). GPT-4o: 1.50% to 24.56% on RLM25 (b12). Dropping theorem statements as well lowered it to 17.20%, so statements help; proofs do not.

### 4.4 Sample, filter, select
1. Draw n candidates (n=50 helped GPT-4o; up to 1000 for a 7B model).
2. Drop candidates that fail to type-check. Poiroux found this the critical step (a15).
3. Pick one: Self-BLEU centre, majority vote over normalised outputs, or symbolic-equivalence clustering (candidates provably equal to each other cluster; largest cluster wins). Add semantic consistency: informalise each candidate and score embedding similarity to the source (Li 2024, a20).

Selection by agreement is a hint only (G4). Candidates from one model share blind spots. FormalMATH's semantic voting cut compile-passing statements from 92.4% to 32.7% (c17), so most compile-passing outputs were not faithful.

### 4.5 Compiler-feedback repair
Loop: formalise, compile, feed the exact error message back, repair. Use detailed errors, not a binary pass/fail (a24). Expect gains mainly on type and library errors (d05: 23 of 61 type-only errors recovered by every method). Cap rounds. Accuracy plateaus while executability keeps rising (Logic-LM, b27).

### 4.6 Critic in the loop (semantic repair)
Add a second step that judges faithfulness and returns a specific complaint (which object, which hypothesis). CriticLean: 54.0% to 84.0% human accuracy on a 100-item sample when a trained critic was added to the compiler loop (a26). A cheaper variant uses a general LLM judge with fine-grained criteria. Atomic criteria (objects, conditions, conclusion, logical structure, types, names) beat one coarse score, and a small model with fine-grained criteria beat a larger one with a coarse score (d07).

### 4.7 Two-judge plus compile gate
Accept only if the statement compiles and two judges from different model families agree. This matched the human majority on 54 of 59 (91.5%) (d04). Caution from the same line of work: for the newest models most automatic rejections were judge errors (4 of 54 real), so rejections need a second look. Judge-only gating is unreliable at the frontier (d05, K22).

### 4.8 Shadow (sub-statement) check
SA-PASS: split the informal statement into atomic "shadow" claims. Full credit only if the formal statement implies each shadow claim and is implied by their conjunction. 98.8% agreement with experts on outputs of six agent configurations (d06). Build: the model lists atomic claims; a prover or model checks each implication in both directions.

### 4.9 Symbolic equivalence (BEq+)
Prove statement A from statement B and B from A using Lean tactics. High precision (98.0) but recall 48.3 on ProofNetVerif; recall falls from 62.5% on short to 29.6% on long statements (b09). Use as a pass filter, never as a reject filter.

### 4.10 Round-trip checks
Formalise, informalise, compare with source. Cheap, but recall 50 at precision 93 (d01). Clover uses six directed consistency checks among code, docstring and formal annotation, with one hard check (the verifier), and got zero false accepts on adversarial variants (d02). The statutory paper adds an SMT equivalence check after a second formalisation; failing rules showed 1.4-2.5 times more NLI drift than passing ones (d03). Use round trip as a prefilter that flags, not a gate that proves.

### 4.11 Formalise then solve (neurosymbolic)
LLM writes solver input (FOL for Prover9, SAT/SMT, PDDL for a planner, a constraint program). The engine returns an answer or a proof. Add self-refinement on solver errors (Logic-LM). Add multi-sample voting over translations (LINC). Add a pruning step that drops programs that run but are contradictory or ambiguous (Draft-and-Prune, d16, abstract only). Give a worked example of the target format; LLM+P failed without one (d12).

### 4.12 Draft, sketch, prove (proof level)
Informal proof draft, formal sketch with open gaps, automated prover (Sledgehammer) closes gaps. Keep in-line informal comments in the sketch (removal costs 4.9/2.8). Wrong drafts still gave proofs 21 of 50 times (a08). The automated prover is the largest contributor (9 points).

### 4.13 Verify-by-formalisation (DTV)
Formalise problem and an LLM solution; try to prove; reject solutions that fail. Two guards against unfaithful formalisation: a vacuity check (the statement should not be trivially true) and self-critique (a21). Compare to majority vote at equal budget.

### 4.14 Negation filter
Try to prove the negation of the formal statement. If provable, the statement is false and so probably unfaithful. Removed 1.6% in FormalMATH (c18). Cheap, low yield.

### 4.15 Separate translate and solve
Reasoning models tend to solve instead of formalise. In constraint tasks they hard-code the solution into the formal program (d13). In training, reasoning traces that solved the problem hurt a formaliser (d08). Rule: the formalising state gets the statement only and must not output an answer; check that the formal text contains no computed result.

## 5. What holds up

**Replications and agreement across independent sources**
- *Type-check overstates success.* Seen in ProofNet (45.2 vs 16.1), Poiroux (r=0.655 vs 0.974), Agrawal (30 of 33 elaborated theorem statements correct, but 21 of 32 for false statements), Beyond Compilation, SHADOWBENCH. Best-supported finding. [E]
- *Informalisation is easier than formalisation.* Wu 76% vs 25%; ProofNet 62.3% vs 13.4%. [E]
- *Sampling gains.* Poiroux and Li 2024 both find large pass@k over pass@1 gaps. [E]
- *Context helps.* RLM25, miniCTX, DDR, LLM+P agree. Only Verina disagrees at one boundary: true code as context did not help spec writing (d14). [E]
- *Compile feedback repairs type errors, not semantics.* d05, d04, a24, Logic-LM. [E]
- *Benchmarks are flawed.* ProofNet 31.8% error, Lean Workbook errors that pass NLI, E3 false negatives, human noise. [E]

**Contradictions and failed or weak results**
- *LINC versus Logic-LM versus CoT.* Symbolic translation wins on synthetic ProofWriter (98.3% GPT-4) and loses or ties on natural data: FOLIO LINC 72.5 vs CoT 75.3 (p=0.58); PrOntoQA 83.2 vs 98.79. Gains depend on rigid data and a weak model. [C]
- *Reasoning models.* Formalising underperformed solving in 12 of 16 pairs (d13). Pre-reasoning-model results (SatLM, Logic-LM) may not hold. [S]
- *Symbolic-equivalence selection.* Li 2024 gains versus Poiroux no gain over Self-BLEU or vote. [C]
- *Compiler feedback.* Helps GPT-4o, hurts DeepSeekMath-7B with binary feedback (a24). Logic-LM accuracy stagnates while executability climbs. [C]
- *Fine-tuning on formal data.* Herald and Goedel gain in-distribution; MMA and Lean Workbook did not beat base on RLM25 (b12). [C]
- *Round trip.* Good for adversarial code variants (Clover), weak for maths recall (F1 0.65). [C]
- *Reported numbers drift between versions.* Herald 93.2% vs 96.7%; CSP abstract 15 of 24 vs body 12 of 16 plus 4 of 8. The critique also found two mis-copied ProofNet rows (a09, c07), now corrected: plain few-shot Codex typecheck was 4.3% with accuracy 0, and the 23.7/25.1/13.4 row is prompt retrieval.
- *Failed replication of Wu's 25.3%:* none found with modern models on the same 150 problems (gap 7 open). There is also no replication that was reported as failed; the absence is a gap, not a result.

**Moderators**
- Domain: competition maths easy (miniF2F near 97%); graduate level 22.5-23.5%; research level 1.5% without context; real-world definitions 13.78 points lower.
- Model class: syntax errors fall with size (38/24/13%); reasoning models solve instead of formalise.
- Context and retrieval: the largest single lever for weak and mid models.
- Wording: paraphrase consistency 19-56%.
- Language: Lean 4 vs Isabelle vs Lean 3 differ; joint training helps (MMA).
- Statement length: BEq+ recall 62.5% short vs 29.6% long.
- Task rigidity: formalisation pays on small rigid logic and planning with a solver; not on open natural problems.

**Interventions that worked**
Retrieval of similar or dependency items; file context without proofs; sample plus type-check filter; detailed compiler errors; semantic critic added to compile loop; cross-family two-judge gate; atomic-criteria judging; informal drafts for proofs; verifier-feedback refinement for proofs at matched query counts (d14).

**Interventions that did not work or are unproven**
Binary pass/fail feedback; plain round-trip as sole gate; compile as sole gate; symbolic equivalence as reject filter; natural-language solution guidance (linked to worse proof success in FormalMATH, c18); fixed few-shot prompts at undergraduate level; fine-tuned formal models on research-level text; heavy iterative repair on hard items (Verina gains saturate: 3.70% on the hard subset).

**Weak spots in the evidence**
Many human-graded accuracies use N=38, 50, 80, 100, 150 with no confidence intervals. Metrics are not comparable across papers (typecheck, BLEU, human-perfect, BEq+, pass@k). Many 2025 results are self-reported by model authors. Several tables were read from garbled text (critique.md); some papers are abstract-only (d16-d18).

## 6. Language models

**Base rates by era**
- 2022 Codex/PaLM few-shot: 25.3% perfect on MATH-to-Isabelle (N=150); 0% on ProofNet-level Lean without retrieval.
- 2023-24 GPT-4 era: LeanEuclid 5-shot 18.9% (GPT-4), 21.0% (GPT-4V), zero-shot about 3.0% and 2.3% (a19). FormL4 compile, greedy, Real test: GPT-4o 5.85%, GPT-4 up to 10.20% by a second table (a12, b19). LLaMA-33B from 0% to 16-18% after MMA fine-tuning.
- 2024 GPT-4o: ProofNet# 31.0% single, 45.1% with 50 samples and selection. RLM25 research level 1.50% without context.
- 2025 specialised formalisers: Herald 93.2-96.7% on miniF2F-test, 22.5-23.5% graduate; Goedel formalizer B CC+FC Pass@1 76.41% vs A 45.72%; ATLAS ProofNet pass@1 39.46%; StepFun-Formalizer-32B BEq@1 40.5% on FormalMATH-Lite, 26.7% on ProverBench (d08).
- 2026 frontier: DeepSeek V4-Pro one-shot on ProofNet# n=186: 95 successes (type-check rate 59.7%, semantic-faithful rate 51.1%); with 4 calls 131 (about 70.4% faithful). Four frontier models in the paraphrase stress set compiled only 6.8-24.2% (d09). Agents on research-level problems: 61.8% compile, 11.2% SA-PASS (Claude Code with Opus 4.8 and Numina-Lean-Agent, d06). Statutory rules: equivalence 44.7% to 67.1% without repair (Claude Opus 4.6, GPT-5.2; d03).

**What changed behaviour, and by how much**

| Lever | Effect | Where |
|---|---|---|
| Retrieval of examples | 0 to 13.4% (Codex ProofNet) | b05 |
| Distilled back-translation | 13.4 to 16.1 (Codex); 0 to 3.2 (proofGPT) | b05 |
| File context (no proofs) | 1.50 to 24.56% BEq+ (GPT-4o RLM25) | b12 |
| Sampling n=50 with filter | 31.0 to 45.1% | a15 |
| Sampling n=1000, 7B model | 4.11 to 40.54% | c14 |
| Compiler loop | 38.0 to 54.0% (7B, N=100) | a26 |
| Compiler plus critic loop | 38.0 to 84.0% | a26 |
| Mixed-style training data | miniF2F 56.5 to 57.6; ProofNet 13.8 to 15.2 | a18 |
| Dependency retrieval (DDR) | TypeC 0.385 to 0.770 on one bin | d11 |
| Judge: cross-family pair plus compile | 91.5% agreement vs 76.3% for a rule | d04 |
| Reasoning-model formaliser | below solver in 12 of 16 pairs | d13 |

**Behaviours to expect**
- Compiles but says the wrong thing. For one frontier model type-only failures (61) outnumber semantic-only (16, d05); semantic errors dominate for weaker models and for gold-label errors.
- Invents library names. Hallucinated Mathlib identifiers are 34-50% of failures on ProofNet# paraphrases (d09).
- Silent weakening: hard-codes a field size, uses Summable where a limit is meant, reverses an inequality, drops a hypothesis, proves one direction of an iff (d05, d08).
- Wording sensitivity: rewording the same theorem changes the Lean; where both outputs compile they are nearly equivalent (GTED median at least 0.943) (d09).
- Reasoning models solve inside the formalisation (d13, d08).
- Judges lean permissive in some settings (plain judge precision 73, recall 100 in d01). Two judges disagree by 26-37 points on some elaboration-failure strata (d05).
- Models trained on in-distribution formal data do well there and less well on new domains (Herald miniF2F 93-97% vs graduate 22-24%).

**Cost.** Verina runs cost up to 1197 USD per model (d14). Human validation 6.89 USD per statement (d21). No study gives cost at equal faithfulness for an automated pipeline.

## 7. What our agent should take

Our agent has no theorem prover in its default bench. The transferable ideas are: check meaning, not only form; use code checks where a formal check exists; never let the generator grade its own translation alone.

### Add now (established)

1. **Report compile pass and independent faithfulness separately; treat a gap above 2x as an alarm.** Part: G (verify before trust), S8 VERIFY. Status [E]. Evidence: b06, b08, a14, d04, d05, d06 (K02, K22).
2. **Meaning check at translation: a six-item checklist (objects, conditions, conclusion, logical structure, types, library or tool names).** Part: S2 REPRESENT, checked before S3. Status [E] for the error types; the checklist as an intervention is untested (see T1). Evidence: d05, d08, d09, b01 (K24). It must be a structured step, not free reflection (section 4b says unstructured self-reflection fails).
3. **Names and library items must exist: accept a formal name only after a lookup.** Part: O (check), G2. Status [E]. Evidence: d09, d11, a03 (K05).
4. **Compiler or solver feedback goes back as the exact error text, never as binary pass/fail; expect it to fix form, not meaning.** Part: S5 REVISE, G2. Status [E]. Evidence: a24, b27, d05 (K10).
5. **Give surrounding definitions and context (statements, not proofs); retrieve analogous solved translations as examples.** Part: memory (subgoal library), S2. Status [E]. Evidence: b12, d10, d11, b05, b22 (K07, K08). Note: SCHEMA memory shows lessons only after the first attempt to avoid fixation; retrieved translation exemplars are a different thing and their order should be tested (UNKNOWNS).
6. **Keep translate and solve apart: the translating state must not output the answer, and its output is scanned for hard-coded results.** Part: S2 vs S3 separation, G10. Status [E]. Evidence: d13, d08 (K25).
7. **Audit a random 50 of our own checker-passed items by hand before trusting the checker.** Part: G (do not trust own checker), G3. Status [E]. Evidence: b10, b14, a19 (K09).
8. **Multi-sample then filter with a hard check, selecting in code.** Part: S3, S4, S7, G5. Status [E] for the gain; the selection rule is [C]. Evidence: a15, c14, a20 (K03).
9. **Gate any semantic claim on the hard check plus two judges from different model families; give automatic rejections a second look.** Part: G5 exception, S8. Status [E] on direction; numbers are from small audits (54/59). Evidence: d04, d05, d06 (K18, K22).
10. **Informal draft then formal check beats direct proof even when the draft is wrong.** Part: S/O draft-then-verify. Status [E]. Evidence: a06-a08, b29 (K14).

### Test first (not established for our agent)

| Item | Part | Status | Evidence ids |
|---|---|---|---|
| Round-trip check (formalise, informalise, compare) as a flag | O verify, S8 | [C] | d01, d02, d03 (K06, K21) |
| Atomic shadow-claim check (SA-PASS style) | S8 | [S] | d06, d07 |
| Sample-and-filter versus retry versus critic repair at equal tokens | S3-S5 | [S] | d05, d14 (K23) |
| Formalise-and-check a step versus majority vote (DTV) | S8 | [S] | a21, c24 (K13) |
| Route to solver by item type (rigid, small, solver available, weak model) | S0 gate, O6 change representation | [C] | a23, c25, c27, d12, d13 (K11) |
| Paraphrase consistency alarm (3 paraphrases; disagreement among compiling outputs) | O multi-sample consistency, G4 | [S] | d09 (K26) |
| Combine solver answer and CoT answer by agreement | S7 | [S] | b26 (K12) |
| Retrieve past formalisations from a lesson memory | memory | [S] no transfer study | b22, d11 (K07) |
| Negation check (try to prove the negation) | O verify | [S] | c18 |
| Definitions-heavy item split reporting | S0 gate | [S] | a24 (K16) |
| Fresh-variant protocol to bound contamination | evaluation | [S] indirect | d19 (K28) |

## 8. Concrete tests on our bench

All tests: both arms at equal tokens (include setup and judge tokens, G7). The plain arm is the same model with a plain prompt, one attempt or best-of-n at the same budget. Report the plain pass rate, not only the gain. Use human grading on a sample of at least 100 where faithfulness is the metric. Report precision and recall, not only accuracy.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 100 NL statements (competition or textbook level) to a formal target we can check (Lean if available; otherwise Python assertions or SMT) | A: plain few-shot. B: plain plus six-item meaning checklist at S2 | Human-graded faithful rate and compile rate; report gap | Faithful rate up a few points; compile rate flat; gap shrinks |
| T2 | Same 100 | A: n samples + compile filter + code selection. B: single-chain compile retry. C: compile retry + semantic critic. Equal tokens | Faithful rate per token | A and B tie on compile; C higher on faithful if the critic is cross-family (K10, K23) |
| T3 | Same 100 plus 50 definitions-heavy items | A: no context. B: definition context (no proofs). C: B plus retrieved analogous solved pairs | Faithful rate; hallucinated-name rate | B large gain; C smaller extra gain; weaker on definitions-heavy |
| T4 | 100 known-wrong formalisations (inject reversed inequality, dropped hypothesis, iff to one direction, wrong constant) mixed with 100 correct | Detectors: compiler only; round trip; one LLM judge; two cross-family judges + compile; atomic shadow check. Equal tokens per detector | Precision, recall, F1 against labels | Compiler alone: near-zero recall on semantic errors. Round trip: precision high, recall about 50. Two judges: F1 near 0.9. Shadow: highest |
| T5 | 60 rigid logic items (FOLIO-like, ProofWriter-like, constraint puzzles) and 60 natural reasoning items | A: CoT. B: formalise + solver. C: route by S0 rule to A or B. Equal tokens | Accuracy by type | B wins on rigid items with a weak model; loses with a reasoning model; C beats both if routing works |
| T6 | 60 math word problems with step-level claims | A: majority vote at n. B: DTV-style formalise-and-check of each solution, reject failures, then vote. Equal tokens | Solve rate | B above A by 2-6 points on number theory and arithmetic (K13); none on non-math |
| T7 | 100 statements, 3 paraphrases each | A: take first output. B: flag when compiling outputs disagree and re-sample. Equal tokens | Faithful rate; flag precision | Flag catches many errors; the paraphrases cost 3x |
| T8 | 50 formalisation outputs from a reasoning model | A: standard prompt. B: translate state forbidden from computing the answer + scan for hard-coded results | Hard-coded-result rate; faithful rate | Fewer hard-coded results; faithful rate up |
| T9 | Fresh-variant set: 50 newly written statements after the model cutoff vs 50 public benchmark statements | One arm; compare sets | Faithful-rate drop | Drop of several points to tens of points if contaminated |
| T10 | 50 items audited by hand from the checker-passed set | n/a | Fraction not faithful | If above 15%, add an external-audit guardrail |

## 9. What does not transfer, and why

- **Training results.** Herald, Goedel-Prover, ATLAS, Lean Workbook, MMA, FormL4, CriticLean, StepFun-Formalizer use fine-tuning or RL. We do not train. They are motivation and a source of error taxonomies only.
- **Theorem-prover context.** Most numbers use Lean and Isabelle libraries that the bench lacks. The mechanism (check, retrieve, compare) transfers; the figures do not.
- **miniF2F scores.** Saturated near 97%. They say little about difficulty now.
- **BEq+ itself.** It needs a prover and tactic library. Use the idea (prove both directions) where a solver exists.
- **Human-expert grading at scale.** FormalMATH cost 6.89 USD per statement with olympiad-medalist annotators. The bench needs cheaper labels. Two judges plus compile is the substitute, validated only on 59-item audits.
- **Code-specification results (Clover, nl2postcond, Verina).** Strong for code tasks, but our bench items are mostly puzzles and reasoning items. Transfer limited to items with a code or test oracle.
- **Statutory text (d03).** SMT equivalence of rules is domain-specific; use only for rule-like items.
- **Logic-LM and LINC numbers.** Gains were reported with GPT-3.5, GPT-4 and StarCoder+. With reasoning models the same approach underperformed (d13). Do not assume they hold.
- **Multi-agent formalisation (TOMAP, MAD-LOGIC).** The schema forbids debate (G9). TOMAP's idea of spending test-time budget at the bottleneck agent (abstract only, d18) could be tested later as a budget rule under G12. It is not evidence.
- **Persona judges.** G4 forbids persona voters. Cross-family judges are different models, not personas, but T4 should check whether they are independent enough.

## 10. Open questions

1. At equal tokens, is sample-and-filter better than critic-guided repair? Sources compare at equal calls (d05) or equal queries for proofs (d14). No token-matched study.
2. Does the Wu 25.3% rate move for modern models on the same 150 MATH problems? No rerun found.
3. How much of the benchmark gain is contamination? No fresh post-cutoff autoformalisation result; only indirect Putnam-AXIOM (minus 19.6 points).
4. Does retrieval from a memory of past formalisations transfer across problem classes? No study found.
5. What is the full failure taxonomy of frontier models in 2026, including silent weakening? One model and benchmark (d05) plus an error analysis of about 10K outputs (d08).
6. What is the cost per verified statement for an automated pipeline at equal faithfulness?
7. Do DTV-style verifiers help outside maths (open-ended reasoning)? Nothing found.
8. Is the two-judge gate stable at larger N and across domains? 54 of 59 has a CI of 81.6-96.3. SA-PASS 98.8% used six configurations on one benchmark.
9. When does formalise-then-solve beat direct reasoning? Hints: weak model, rigid small problem, solver available, in-context example. No routing rule found.
10. Do the version discrepancies (Herald 93.2 vs 96.7; CSP 15 of 24 vs 12 of 16 plus 4 of 8) change any conclusion? Probably not, but cite the version.
11. FormalAlign's first author is given as Lu or Ye in different notes; check the paper header (critique item 4).

## 11. Sources

Marks: [V] opened (full text or PDF read in this series), [M] snippet, abstract or citation only. Evidence ids in brackets.

- Wu et al. 2022, Autoformalization with Large Language Models [V] https://arxiv.org/abs/2205.12615 [a01-a05, b01-b04, c01-c04]
- Jiang et al. 2022, Draft, Sketch, and Prove [V] https://arxiv.org/abs/2210.12283 [a06-a08, b29, c05-c06]
- Azerbayev et al. 2023, ProofNet [V] https://arxiv.org/abs/2302.12433 [a09, a10, b05-b07, c08, c09]
- Jiang et al. 2023, Multilingual Mathematical Autoformalization (MMA) [V] https://arxiv.org/abs/2311.03755 [a11, b13, c10]
- Lu et al. 2024, Process-Driven Autoformalization in Lean 4 (FormL4) [V] https://arxiv.org/abs/2406.01940 [a12, b19, c12]
- FormalAlign (Lu or Ye et al. 2024) [V] https://arxiv.org/abs/2410.10135 [a13, b23, c23]
- Poiroux et al. 2024/2025, Reliable Evaluation and Benchmarks for Statement Autoformalization [V] https://arxiv.org/abs/2406.07222 [a14-a16, b08-b12, c13-c15]
- Ying et al. 2024, Lean Workbook [V] https://arxiv.org/abs/2406.03847 [a17, b14, b15, c11]
- Lin et al. 2025, Goedel-Prover [V] https://arxiv.org/abs/2502.07640 [a18, c20, c21]
- Murphy et al. 2024, Autoformalizing Euclidean Geometry (LeanEuclid) [V] https://arxiv.org/abs/2405.17216 [a19, b24, c16]
- Li et al. 2024, Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency [V] https://arxiv.org/abs/2410.20936 [a20]
- Zhou et al. 2024, Don't Trust: Verify [V] https://arxiv.org/abs/2403.18120 [a21, c24]
- Pan et al. 2023, Logic-LM [V] https://arxiv.org/abs/2305.12295 [a22, b27, c25, c26]
- Olausson et al. 2023, LINC [V] https://arxiv.org/abs/2310.15164 [a23, b25, b26, c28, c29]
- Zhang, Valentino, Freitas 2025, Autoformalization in the Wild: Real-World Definitions [V] https://arxiv.org/abs/2502.12065 [a24]
- Gao et al. 2024, Herald [V] https://arxiv.org/abs/2410.10878 [a25, b16-b18, c19]
- Peng et al. 2025, CriticLean [V] https://arxiv.org/abs/2507.06181 [a26]
- Wang, Kaliszyk, Urban 2018, First experiments with neural translation of informal to formal mathematics [M, citation only] https://doi.org/10.1007/978-3-319-96812-4_22 [a27]
- Szegedy 2020, A promising path towards autoformalization and general AI [M, citation only] https://doi.org/10.1007/978-3-030-53518-6_1 [a28]
- Weng/Zhao et al. 2025, Autoformalization in the Era of LLMs: A Survey [M, abstract and intro only] https://arxiv.org/abs/2505.23486 [a29, b31, c34]
- Agrawal et al. 2022, Towards a Mathematics Formalisation Assistant using LLMs [V] https://arxiv.org/abs/2211.07524 [b20, b21]
- Zhang et al. 2024, Consistent Autoformalization for Constructing Mathematical Libraries [V] https://arxiv.org/abs/2410.04194 [b22]
- Ye et al. 2023, SatLM [M first pass; numbers via c27] https://arxiv.org/abs/2305.09656 [b28, c27]
- Zheng et al. 2022, miniF2F [V] https://arxiv.org/abs/2109.00110 [b30]
- Yu et al. 2025, FormalMATH [V] https://arxiv.org/abs/2505.02735 [b32, c17, c18, d21]
- Liu et al. 2025, ATLAS [V, not re-opened in critique] https://arxiv.org/abs/2502.05567 [c22]
- Xu et al. 2024, Symbolic Chain-of-Thought [V, not re-opened] https://arxiv.org/abs/2405.18357 [c30]
- Cosler et al. 2023, nl2spec [V, not re-opened] https://arxiv.org/abs/2303.04864 [c31]
- Sun, Sheng, Padon, Barrett 2023, Clover [V] https://arxiv.org/abs/2310.17807 [c32, d02]
- Zheng et al. 2023, Lyra [V, not re-opened] https://arxiv.org/abs/2309.15806 [c33]
- Mathesis 2025, Towards Formal Theorem Proving from Natural Languages (LeanScorer) [V] https://arxiv.org/abs/2506.07047 [d01]
- Amrollahi, Lopez, Barrett 2026, Faithful Autoformalization via Roundtrip Verification [V] https://arxiv.org/abs/2604.25031 [d03]
- Beyond Compilation 2026, Evaluating Faithful NL-to-Lean Statement Formalization [V] https://arxiv.org/abs/2606.31002 [d04]
- Dai et al. 2026, The Signal-Coverage Matrix [V] https://arxiv.org/abs/2606.28013 [d05]
- SHADOWBENCH 2026 [V] https://arxiv.org/abs/2608.29270 [d06]
- Zhang, Valentino, Meadows, Freitas, Beyond Gold Standards: Epistemic Ensemble of LLM Judges [V] https://arxiv.org/abs/2506.10903 [d07]
- Wu et al. 2025, StepFun-Formalizer [V] https://arxiv.org/abs/2508.04440 [d08]
- Lou et al. 2026, Characterizing Paraphrase-Induced Failures in Lean 4 Autoformalization [V] https://arxiv.org/abs/2604.23135 [d09]
- Hu et al. 2025, miniCTX [V] https://arxiv.org/abs/2408.03350 [d10]
- Wang et al. 2025, Direct Dependency Retrieval [V] https://arxiv.org/abs/2511.11990 [d11]
- Liu et al. 2023, LLM+P [V] https://arxiv.org/abs/2304.11477 [d12]
- Chen et al. 2025/2026, A Reality Check of Language Models as Formalizers on Constraint Satisfaction Problems [V] https://arxiv.org/abs/2505.13252 [d13]
- Ye et al. 2026, VERINA [V] https://arxiv.org/abs/2505.23135 [d14]
- Endres et al. 2024, Can LLMs Transform NL Intent into Formal Method Postconditions? [V] https://arxiv.org/abs/2310.01831 [d15]
- Ni et al. 2026, Draft-and-Prune [M, abstract only] https://arxiv.org/abs/2603.17233 [d16]
- Monotonic Reference-Free Refinement for Autoformalization 2026 [M, abstract only] https://arxiv.org/abs/2601.23166 [d17]
- TOMAP 2026 [M, abstract only] https://arxiv.org/abs/2607.11307 [d18]
- Miranda et al. 2025, Putnam-AXIOM [V] https://arxiv.org/abs/2508.08292 [d19]
- Tsoukalas et al. 2024, PutnamBench [V] https://arxiv.org/abs/2407.11214 [d20]

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 16 established claims: 13 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C06.09-K01** (number corrected). ProofNet Table 3 and section 5.1: the 13.4% is Codex few-shot (in-context baseline) with no retrieval, retrieval raises it to 16.1% (+2.7), and the 0% figure belongs to the proofGPT models, not 'few-shot without retrieval' generally; 25.3% on 150 MATH-to-Isabelle statements is right. Corrected claim: Few-shot LLMs formalise only a minority of competition or undergraduate statements perfectly: 25.3% (Codex, MATH to Isabelle, N=150), 13.4% (Codex few-shot, ProofNet Lean 3, N=371; 16.1% with retrieved prompts); the small proofGPT models score 0% few-shot on ProofNet.
- **C06.09-K07** (number corrected). In ProofNet (Table 3, section 5.2) retrieval, not distilled back-translation, takes Codex from 13.4 to 16.1 (+2.7 accuracy, typecheck +21.5 points); distilled back-translation applies to proofGPT-1.3B (3.2%, above its few-shot 0); '0 to 13.4' is wrong, and Codex is not a weak model. MS-RAG (Mistral 7B beats Mixtral 8x7B standard prompting) and the MMA/Lean Workbook finding are supported. Corrected claim: Retrieval of similar examples helps: ProofNet Codex 13.4 to 16.1 with retrieved prompts (typecheck 23.7 to 45.2), and distilled back-translation lifts proofGPT-1.3B from 0 to 3.2; MS-RAG with Mistral 7B beats Mixtral 8x7B with standard prompting; but fine-tuned MMA and Lean Workbook models did not beat the base few-shot models on RLM25.
- **C06.09-K10** (number corrected). CriticLean human evaluation used 50 Omni-MATH problems, not N=100 (38.0 / 54.0 / 84.0 are right); also Logic-LM says self-refinement raises final accuracy by 5.01 on average (GPT-3.5 FOLIO Exe_Acc 61.8 to 64.3) and only stagnates over additional rounds, so 'accuracy stagnates' overstates it; binary feedback hurting DeepSeekMath-7B, 64% type-stratum recovery with flat semantic errors, and nearly half of the agent compile gain failing the semantic criterion are supported. Corrected claim: Self-refinement with compiler feedback raises executability more than accuracy: Logic-LM executable rate up (GPT-3.5 FOLIO 66.7 to 84.3) with only modest accuracy gains that stagnate over further rounds; binary feedback hurt DeepSeekMath-7B (Isabelle definitions); a critic-in-loop raised human accuracy 38.0 to 54.0 (compiler) to 84.0 (compiler plus CriticLeanGPT, 50 Omni-MATH problems). Compiler-feedback methods recover about 64% of type-stratum errors with semantic errors flat on net (d05); nearly half of an agent's compile gain fails the semantic criterion (d04).
- **C06.09-K14** (now single-source: only one opened source, code check).
