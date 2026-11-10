# Proof planning and repair: deep document

*Subfield C06.08. Evidence files: evidence_a-d.jsonl (ids a01-a25, b01-b27, c01-c28, d01-d18). Claims: claims.jsonl (K01-K25). Corrections from critique.md are applied here (for example Thor alone is 57.0%, not 58.0%; the 702 / 6.5% variant is PALM without backtracking).*

## 1. What it is

Proof planning and repair studies two linked questions.

1. **Plans over proofs.** Can a solver write a high-level plan first (a sketch, a list of lemmas, a decomposition) and then fill in the details?
2. **Fixing broken proofs.** When an attempt fails, what is the best way to repair it? Rewrite from scratch, patch the failing step, or change the plan?

The field has three eras.

- **Symbolic proof planning (1988 to 2000s).** Bundy and colleagues at Edinburgh. A proof is built from methods with declared preconditions and effects. When a method fails, a critic reads the failure and proposes a patch (a lemma or a generalisation).
- **Proof engineering and symbolic repair (2018 to 2021).** Ringer and others. Proof repair is program repair for proofs. The theorem statement is a built-in specification, so a patch can always be checked.
- **LLM proof generation with checker feedback (2022 to 2026).** An LLM writes a whole proof or a sketch. A proof checker (Isabelle, Coq, Lean) returns exact error text. The loop retries, repairs, keeps verified parts and re-prompts only for what failed.

Why it matters for our agent: this is the best-measured testbed for our state **S5 REVISE** (show the real failing output, fix, at most 2 rounds), for guardrail **G2** (revise only from real output) and for **O3** (decompose). A proof checker is an ideal verifier. The main question for us is what carries over to tasks where the verifier is weaker.

Main message of the evidence: **revision works when an external checker gives located, exact feedback. It does not work as blind self-review. Its gain at equal tokens is modest, front-loaded in the first round, and mostly fixes shallow failures.**

## 2. History and theories in depth

### 2.1 Bundy's proof planning (1988)
- Bundy (1988), "The use of explicit plans to guide inductive proofs" (CADE-9). Describes a proof strategy as a plan built from **methods**. Each method has declarative preconditions and effects, plus a tactic that carries out guaranteed inference steps. The CLAM planner implements it. [a04, c19; not opened, second-hand via a02 and the Ringer survey a05/a06]
- **Rippling** is the main induction method. It rewrites the step case so that the induction hypothesis can be used. The 1992 paper claims rippling is a rational reconstruction of Boyer-Moore (nqthm) heuristics. [a02, a25]

### 2.2 Critics: using failure (Ireland and Bundy 1992, 1996)
- Report RP 613 (1992) is the one founding text we read. [a01, a02]
- A **critic** is attached to a method. It has preconditions that name an interesting failure and effects that say how to patch it.
- Four critic kinds: lemma calculation, lemma speculation, generalisation, sink generalisation. Speculation can call calculation.
- Worked example: `rev(rev(v)<>w::nil) = w::v`. Plain induction gets stuck on partial terms. The fix needs one lemma and one generalisation: `forall v,w: rev(rev(v)<>w) = rev(w)<>v`.
- Evidence level: 5 example theorems (Table 1), a table of which critic each needed (Table 2). No timing, no failure counts, prototype in lambda-Prolog. The claim that critics let CLAM succeed where nqthm breaks down is a stated claim without counts. [a01, a02, a25]
- The 1996 journal version (J. Automated Reasoning) and Melis and Siekmann (1999, knowledge-based proof planning in OMEGA, AI 115) were **not read**. Publisher pages were blocked. [a03, a24, c20, d17]

### 2.3 Planning reaches interactive provers
- IsaPlanner (Dixon and Fleuriot 2003) brought rippling to Isabelle. [a06, c18]
- Ringer et al. (2020) "QED at Large" places critics as an early form of proof repair, and notes the key advantage: the theorem is a specification, so a patch can be checked. Program repair suffers from patches that pass tests but are wrong (Qi et al. 2015, cited second-hand). [a05, a23, c17]

### 2.4 Symbolic proof repair (PUMPKIN, Pumpkin Pi)
- Ringer et al. (PLDI 2021): when a Coq type changes, transport proofs along an equivalence and decompile the new proof term into a tactic script. [a07, b24]
- Eight case studies: ornaments (list to vector), unpack sigma types, tuples and records, permute constructors, add constructors, factor constructors, permute hypotheses, unary to binary. An industrial user rarely waited over ten seconds. [a07]
- Savings: minutes on small factor-out cases, hours instead of days for list to vector after massaging, none for constructor swap (the old tactics still worked) and none for added constructors (repaired terms were inefficient). [a08, b24]
- Evidence level: case studies, not counted trials. The REPLica user study was cited, not opened. [b25]

### 2.5 LLM era
- **DSP (Draft, Sketch, Prove, 2022/23).** An LLM drafts an informal proof, writes a formal sketch with gaps, and Sledgehammer plus heuristics fill them. This is a machine-made proof plan with holes. [a13, a14, b13, c07]
- **Baldur (2023).** Whole-proof generation plus a separate repair model that sees the failed proof and the Isabelle error. [a09, a10, b01-b05, c01-c03]
- **COPRA (2023).** GPT-4 proposes one tactic at a time, error goes back to the prompt, stateful backtracking. [a17]
- **Lyra (2023).** Two corrections on top of DSP: Tool Correction (swap a failing tool for a stronger one) and Conjecture Correction (regenerate the sketch from the error). [a16, b11, b12, c06, c24]
- **PALM (2024).** Coq. Generate, repair with hand-built rules and CoqHammer, backtrack. [a11, a12, b06-b10, c04, c05]
- **DeepSeek-Prover V1.5 (2024).** Truncate at the first error, resume, RMaxTS tree search. [c08, c26]
- **Cobblestone, APOLLO, ProofAug (2024 to 2025).** Keep verified parts, replace failing tactics with admit/sorry, re-prompt only the open goals. [a18, b17, c09, c10, c11]
- **Goedel-Prover-V2, Seed-Prover, Hilbert, Aristotle, DeepSeek-Prover-V2 (2025).** Trained self-correction against compiler feedback, lemma pools, hierarchical planner plus prover. [a20-a22, b14-b16, b19, c12-c15]
- **2026 gap-search papers.** Fix Not Just Resample (Lean step repair), CAPRI and Double-Tank (Isabelle, goal drift), LAMP (planner/builder split), P3 (joint program-and-proof plan). All single-group preprints. [d09-d16]
- **Outside proofs.** Self-Debug, Olausson (code), CRITIC (tools), Tyen (locating mistakes), Huang (intrinsic self-correction), Kamoi survey. [d01-d08, b20, c16, c27]

### 2.6 Competing explanations
- **Checker signal vs second attempt.** Is the gain from the error text, or from a second try? Baldur's no-error-message arm separates them. [a10, b02, c02]
- **Repair vs resampling.** Olausson finds repair only sometimes beats resampling at equal budget. [d01]
- **Search vs retry.** RMaxTS (+2.5) vs ProofAug's claim of under 0.2% over naive retry. [c26, c08, c09]
- **Plan quality vs executor strength.** DSP: bigger informal model was worse; Hilbert: stronger planner helps. [a13, c14]

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Baldur repair uses the error text; the no-error arm does not beat resampling at equal cost | Fig. 5 (curve values not extracted). Repair adds 1.5 points cost-matched (abstract). Unmatched generate+repair: +266 theorems, 4.2% (two samples vs one; do not quote as matched) | a10, b02, c02, c01 | E |
| Second repair adds little | Cost 2: 24.9%. Second repair, cost 3: 26.2% (+1.3). Plain generation at cost 3: 25.4%. Margin 0.8 | b03, c03 | E (with d04, d10) |
| Baldur whole-proof generation | PISA test 6,336 theorems. 8B: 34.8% at 16 samples, 40.7% at 64. With theory-file context 47.5% at 64. 62B with context 47.9%. Sledgehammer 25.6%. Search-based LM 39.0% | a09, b01, b04 | S (leak risk) |
| Repair complements a symbolic searcher | Baldur+Thor 65.7% vs Thor alone 57.0%. Ensemble of 10 Baldur models 58.0% | b05, c01 (corrected) | E |
| PALM beats prior Coq tools | 10K+ theorems, 27 projects. PALM(GPT-3.5) 4,377 = 40.4%. Passport 14.4%, Proverbot9001 17.1%, DSP 22.9%. 1,270 proved by no baseline | a12, b07 | S |
| PALM ablation: backtracking dominates | Full 40.4%. No backtracking 702 = 6.5%. One repair rule removed: 39.2, 38.5, 39.0, 37.8. No premise retrieval 38.2%. CoqHammer is a large share too | b08, c05, a12 (corrected) | S |
| Scaffold gain exceeds model-size gain | Alone: GPT-3.5 3.7%, GPT-4o 6.4%, Llama-3-70B 3.6%, Llama-3-8B 0.1%. With PALM: 40.4, 42.6, 38.3, 31.7 | b09 | S |
| LLM Coq errors are mostly low-level | 520 errors (579 theorems): wrong theorem application 49.6%, invalid reference 15.2%, incorrect rewrite 11.7%, redundant intros 10.8%, tactic misuse 8.5%, bullet misuse 3.7%, other 0.6%. Dataset size varies in files (10,842 / 10,826 / "more than 10K") | a11, b06, c04 | E (one model family) |
| PALM residual failures are missing knowledge | 100 unproven: premise not retrieved 58, retrieved but unused 14, tactics not used 39 (overlap) | b10 | S |
| DSP plan-then-fill | miniF2F-test 20.9% to 39.3% (Codex, 100 attempts). Minerva informal: 8B 36.5, 62B 34.0, 540B 30.3 | a13, b13, c07 | E for gain; C for plan size |
| DSP ablations (valid/test drop) | In-line comments -4.9/-2.8. Informal proofs -3.7/-5.3. Automated provers (full formal proof instead) -9.8/-9.0 | a14 | S |
| Lyra clean gain from corrections | GPT-4 DSP re-run: 39.7% (100), 42.6% (200). Lyra: 47.1% (100), 51.2% (200) test. Clean gain at 200: +8.6 test (valid 50.4 to 55.3, +4.9). Headline +11.9/+12.7 vs Codex DSP mixes a formaliser swap | a16, b11, b12 (corrected) | S |
| Lyra components | Tool Correction +4.1 (GPT-4 proofs) / +3.3 (human) on test. Conjecture Correction +0.4 alone, +5.3 with Tool Correction | b12, c06 | S |
| Informal plan quality | Human informal 51.2% vs GPT-4 informal 47.9% test (valid 55.3 vs 54.9) | c24 | C |
| COPRA (Lean, GPT-4) | Few-shot 13.52%; COPRA 26.63%; minus backtracking 24.59%; plus retrieval 29.09%; ReProver 25.00%. Table row mapping reconstructed | a17 | S (check PDF) |
| Cobblestone vs baselines | CoqGym100: 48% vs CoqHammer 30%, CoT 25%, Proverbot 17%. Wigderson100: 38% vs 27/19/10. Tokens 59.3K vs 99.3K (LinearRegen, CoqGym100). Fail-safe mode in 43% of proofs. Average cost $1.25, 14.7 min; CoqGym100 $1.46, 15.3 min | a18, b21, c11 (corrected) | E with b17 |
| Cobblestone vs PALM | Beats PALM run 15x (token-matched) by 8, 9, 2 points on Wigderson100, PnVRocqLib100, BB5100. Not clearly on CoqGym100 | c11, c21 (corrected) | S; depends on matching |
| APOLLO | Goedel-SFT 64.7% at 25,600 samples vs 65.6% at about 362 samples. Kimina-7B 70.8% (1024 samples) to 75.0% (r=6, fewer tokens), +4.2. Goedel-V2-8B +0.9. o3-mini 3.3 to 40.2, o4-mini 7.0 to 46.7 (format fixes) | b17, c10 | S |
| Diminishing rounds (APOLLO) | DeepSeek-R1-Distill-7B: 57.6 (r=0), 60.7 (r=2), 63.5 (r=4), 65.6 (r=6); tokens 16.1K to 179K | b18 | E (with d10) |
| Goedel-V2 correction | miniF2F 88.1 to 90.4 (pass@32, 32B; about +2 both sizes). PutnamBench 43 to 57 (+14). 5 rounds, 128k context: 92.7 vs 92.2 for pass@8192 no correction (averaged-model setting). Removing error messages hurts clearly | a21, b14, b15, c12 | S |
| Seed-Prover | Light = 8-16 refinements, equal to Pass@64-256 budget. IMO 2022 P2 solved with refinement, else needs Pass@8192. MiniF2F-test 99.6%, PutnamBench 331/657. Heavy runs take days | a22, b19, c13 | S; not equal cost |
| Hilbert | miniF2F 99.2%; PutnamBench 462/660 (70.0%) vs Seed-Prover 50.4%. Goedel-V2-32B pass@4 74.6 to 90.8 with Hilbert. Gemini 2.5 Pro beats Flash by 3 to 4 points | c14 | S |
| Truncate-and-resume and tree search | DeepSeek-Prover-V1.5 miniF2F-test 60.2% single pass; RMaxTS 62.7% (+2.5). ProofAug: under 0.2% over naive retry at 3200 samples; ProofAug 52.5% at 100 queries | c08, c26, c09 | E that gain is small; C on exact size |
| Retrieval of own earlier proofs | Rango: 32.0%, +47% from adding relevant proofs. Baldur context 40.7 to 47.5 | b23, c23, b04 | E |
| Intrinsic self-correction | GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1; partly a prompt effect). GPT-3.5 GSM8K 75.8 to about 75 (rounds 1 and 2). GPT-4 GSM8K 95.5 to 91.5 to 89.0. Oracle: GPT-3.5 GSM8K 84.3, GPT-4 97.5 | b20, c16, c27 (corrected) | E |
| Self-repair in code at equal budget | GPT-4 APPS: 10 drafts + 1 repair = 1.05x pass@20; 2 drafts + 10 repairs = 0.97x pass@22. GPT-3.5 only marginal on HumanEval | d01 | E |
| Feedback quality is the bottleneck | 40 failing GPT-4 programs, 16 participants. Repair success 33.3% (GPT-4 feedback) vs 52.6% (human) = 1.58x. Competition tier 3.67 vs 14.67 | d02 | S |
| A stronger critic lifts weaker coders | Code Llama with GPT-3.5/4 feedback and GPT-3.5 with GPT-4 feedback beat i.i.d. and self-repair at all budgets | d03 | S |
| Execution is the signal | Self-Debug MBPP Codex 61.4 to 57.6 without execution; with unit tests up to +12 (abstract). One turn gives nearly all gain (later turns within 0.1%) | d04, d05 | E |
| Tool critique | CRITIC without tool 42.0/58.3 vs CoT 44.2/58.6; with search 50.0/64.9 (column mapping uncertain) | d06 | S |
| Locating the mistake | BIG-Bench Mistake, 2,186 traces, 5 tasks. Oracle-location backtracking gives large gains on incorrect traces (+23.5, +43.9 on two tasks) at small loss on correct ones (-11.1, -6.7) | d07 | S |
| Survey | No success for self-correction with prompted-LLM feedback on general tasks (to May 2024); works with reliable external feedback, with fine-tuning, and on decomposable tasks | d08 | E |
| Lean step repair vs sampling | 1,990 theorems. +2.3 to +4.1 pass@1 at K in {1,3,5,8}; +0.6 (100 s) to +2.8 (600 s) at K=8 matched wall-clock. First repair gives 84-96% of gain; marginal efficiency falls over 15-fold after round 1. Test gain rests on 11 theorems | d09, d10 | S |
| What repair fixes | Of 89,634 rejected tactics (K=8, R=1) one repair recovered 6.2%. No-progress/simp 14.6, apply/exact 13.2, rfl 11.0, rewrite 5.4, typeclass 4.7, syntax 2.0, type mismatch 2.0 (17,839 cases), timeout 1.8 | d11 | S |
| Looping on checker output (Isabelle) | 12 proofs x 3 replicates x 5 conditions = 180 runs. Valid out of 36: one shot 22; iterative 31 (full theory), 29 (proof body only), 32 (diagnostic delayed); one-shot with diagnostic 24. Paired p=0.03 for iterating | d12 | S |
| Goal drift in repair loops | 6 of 144 accepted candidates modified protected text (all in iterative full-theory runs: 6/69 = 8.7%). Proof-body-only: 29/36 valid, 0 violations. Drifted real project: 16 of 100 declarations materially changed, one theorem weakened | d13, d14 | S |
| Planner role (LAMP) | 90 Lean theorems, same 9-call budget. Full 96.7% (Hard 88.2%, 15/17). No Planner 85.6% (Hard 58.8%). No MCP tools 84.4%. Unscaffolded 58.9% | d15 | S |
| Joint plan (P3) | Verina best baseline up to 72.0 vs P3 72.0-77.2; AlgoVeri P3 39.0-48.1; Lean4Commit0 15.7-22.2. PLAN-SEQ 69.8/44.8/13.9 vs P3 74.6/48.1/22.2. Full restart rate 17-28% falls to 5-12% | d16 | S |
| Most failures are not plan errors | P3 on Verina: 4 of 48 failures plan errors; 15 proof elaboration; 26 timeout/tool fault. 131 of 141 successes (92.9%) kept the first plan | d16 | S |
| Founding critics claim | Design argument with 5 worked examples, no counts vs nqthm | a01, a02, a25 | S |
| Specification check avoids overfitting | Theorem statement always available to check patch | a05, c17 | E (conceptual) |

## 4. Mechanisms and models

Each mechanism below is written so it can be coded.

### 4.1 Verify-and-revise loop with a located error (Baldur, Goedel, Seed-Prover)
1. Generate whole attempt `A0`. Run the checker.
2. If pass, stop. Else, extract the **first error**: its message, its location, the local state.
3. Prompt: task + `A0` + error text. Ask for one corrected attempt `A1`.
4. Re-run the checker. Cap rounds at 1 to 2.
5. Keep best-so-far.
- Why it works: the error is exact and located. The model fixes well and finds poorly (d07, d02).
- The control that proves the mechanism: the same loop with the error text removed gives no gain over resampling at equal cost. [a10]

### 4.2 Truncate and resume (DeepSeek-Prover-V1.5)
- Cut the attempt at the first error. Keep the verified prefix. Ask the model to continue from the last good state. [c08]
- Gain over naive retry is small (+2.5, maybe under 0.2%). [c26, c09]

### 4.3 Keep verified parts, redo failing subgoals (Cobblestone, APOLLO)
1. Run checker on the attempt. Find the longest verified prefix and every sub-block that checks.
2. Replace failing tactics with a placeholder (`admit`, `sorry`).
3. Each remaining open goal becomes a small prompt. Try cheap deterministic solvers first (CoqHammer, Sledgehammer, automatic tactics).
4. Call the LLM only on goals the solvers could not close. Small top-K.
5. Reassemble, re-verify the whole. Recurse to depth r.
- Cobblestone also has a fail-safe mode: if the proof has no structure, use bullets to find subproofs (43% of proofs). [a18, c11]
- Savings: 59.3K vs 99.3K tokens per theorem; APOLLO about 362 vs 25,600 samples. [c11, b17]

### 4.4 Backtracking with repair rules (PALM)
- Generate a proof. A rule-based repairer fixes each recognised error class (wrong theorem application, invalid reference, rewrite, intros, tactic misuse, bullets). CoqHammer is the fallback. If repair fails, backtrack and regenerate an earlier step. [a11, b08]
- The ablation says backtracking is the main part (40.4% to 6.5%). Single rules are worth 1.6 to 2.6 points each. [b08]

### 4.5 Plan with holes, then fill (DSP, Lyra, DeepSeek-Prover-V2, Hilbert)
1. Informal plan: a short statement of the proof idea.
2. Formal sketch: steps written as checked statements with holes.
3. A deterministic tool fills each hole.
4. Failure at a hole: Tool Correction (swap the tool), then Conjecture Correction (rewrite the sketch from the error). [b12]
- Hierarchical version: a planner splits into subgoals recursively, a prover solves leaves, verifier feedback drives refinement, a retriever adds lemmas. [c14, a20]

### 4.6 Error-type router (from d11, d16, a11)
- Shallow failures (no progress, apply/exact, rfl, wrong reference) are fixed by a local patch (11 to 15% recovery per round).
- Structural failures (type mismatch, syntax confusion, plan error) are rarely patched (2%).
- Implementation: tag each failure with a class from the checker message. Send shallow to patch. Send structural to re-plan or a fresh sample. This router is our inference from d11 and d16, not a tested design (K22 single-source).

### 4.7 Critic = failure-pattern to patch (Bundy)
- A table: `failure pattern -> patch type`. Examples: blocked rewrite -> speculate a lemma; stuck on a constant -> generalise. [a01]
- LLM version (untested): a lookup from the checker's error class to a short repair hint in the prompt, versus raw error text only.

### 4.8 Goal-lock guard (CAPRI)
- Before accepting a revision, diff the protected text (the theorem statement, the question) against the original. Reject on any change. Allow edits only inside the proof body. Gave 0 violations at 29/36 vs 31/36 valid. [d13]

### 4.9 Retrieval of earlier proofs
- Keep solved items by class. Show the nearest ones after the first attempt. Gains: +47% (Rango), 40.7 to 47.5 (Baldur theory-file context). [b23, b04]

## 5. What holds up

### 5.1 Held up
- **External feedback is the cause of repair gains.** Baldur's no-error arm, Goedel's error-removal ablation, Self-Debug without execution, CRITIC without tools, Huang's oracle explanation and Kamoi's survey all agree. [a10, b15, d05, d06, c16, d08] Counted as established.
- **First repair gets most of the gain.** Baldur second repair +1.3; APOLLO shrinking steps; Lean 84-96% in round 1; Self-Debug one turn. [b03, b18, d10, d04]
- **Local or partial repair saves tokens.** Cobblestone and APOLLO. Lean step repair beats sampling at matched wall-clock. [c11, b17, d09]
- **Deterministic tools add large gains.** Sledgehammer union (+8.7 over Thor alone), CoqHammer in PALM and Cobblestone, Tool Correction in Lyra. [b05, a12, b12]
- **Plan then fill beats direct proof.** DSP, LAMP, P3. [a14, d15, d16]
- **Retrieval of earlier solved items helps.** [b23, b04]

### 5.2 Failed or weak
- **Blind self-review.** Huang et al. GPT-4 GSM8K 95.5 to 89.0; CommonSenseQA collapse partly a prompt effect. [c16]
- **Conjecture Correction alone**: +0.4. [b12]
- **Large informal planner**: Minerva 540B scored worse than 8B in DSP. [a13]
- **Tree search over retry**: +2.5 at best, possibly under 0.2%. [c26, c09]
- **Symbolic repair time savings**: none for constructor swap or added constructors in Pumpkin Pi. [a08]
- **Critic counts**: never published in the texts we could read. [a25]

### 5.3 Moderators
- **Budget split.** Spend on first drafts: GPT-4 APPS 1.05x with 10 drafts + 1 repair, 0.97x with 2 drafts + 10 repairs. [d01]
- **Feedback strength.** Expert feedback 52.6% vs own 33.3%. Stronger feedback model helps all budgets. [d02, d03]
- **Model strength.** Gain from repair is smaller on stronger provers: APOLLO +0.9 on Goedel-V2-8B vs +4.2 on Kimina-7B. [c10] Large jumps (o3-mini 3.3 to 40.2) are format and syntax fixes. [b17]
- **Failure class.** Local fixes work on shallow errors only. [d11]
- **Whole-workflow, not single mechanism.** CAPRI says its comparisons are of workflows. [d12]

### 5.4 Cautions
- **Contamination.** Almost all LLM evidence is on miniF2F, PISA, CoqGym, PutnamBench. Only Cobblestone controls for leakage. miniF2F is near saturation (99%+). No post-cutoff rerun found. [b21, K20]
- **Token matching is rare.** Seed-Prover, Hilbert, Aristotle and DeepSeek-V2 compare heavy pipelines with light baselines. Cobblestone vs PALM depends on a 15x repeat. [c21]
- **Self-reported and same-lab.** Cobblestone shares authors with Baldur and Rango. [c21]
- **Recent preprints.** d09 to d16 are single-group preprints with small n (11 test theorems, 17 hard theorems, 12 tasks, one run per cell).

## 6. Language models

### 6.1 How they behave
- **They get structure right and details wrong.** In GPT-3.5 Coq proofs, wrong theorem application 49.6% and invalid references 15.2% dominate. [a11]
- **They fix errors better than they find them.** Given the location, models repair chain-of-thought traces they could not locate themselves. [d07]
- **They cannot judge their own reasoning.** The review prompt pushes switching. On CommonSenseQA GPT-3.5 fell 75.8 to 38.1 (partly a prompt effect); on GSM8K the GPT-3.5 drop was only about 1 point. [c16, c27]
- **Passing the checker is not the same as keeping the task.** 6 of 144 accepted repairs edited protected text. [d13]

### 6.2 What changed performance, by how much

| Change | Effect | Source |
|---|---|---|
| Error text in repair (vs none) | removes the gain at equal cost | a10 |
| One cost-matched repair (Baldur) | +1.5 points | c01 |
| Second repair | +0.8 over plain generation | b03 |
| Scaffold around a weak LLM (PALM) | GPT-3.5 3.7% to 40.4%; Llama-3-8B 0.1% to 31.7% | b09 |
| Backtracking removed | 40.4% to 6.5% | b08 |
| Trained correction (Goedel-V2) | +2.3 miniF2F pass@32; +14 PutnamBench | b14 |
| Partial repair (APOLLO) | +0.9 to +4.2 at matched budget | c10 |
| Partial repair (Cobblestone) | 40% fewer tokens (59.3K vs 99.3K) | c11 |
| Format fixer on reasoning models | o3-mini 3.3 to 40.2 | b17 |
| Plan with holes (DSP) | 20.9 to 39.3 | a13 |
| Planner role (LAMP) | -11.1 points without it; Hard 88.2 to 58.8 | d15 |
| Human feedback vs own feedback | 33.3% to 52.6% | d02 |
| Execution feedback removed | Codex MBPP 61.4 to 57.6 | d05 |
| Retrieval of earlier proofs | +47% (Rango) | b23 |

### 6.3 Gap: reasoning models
No source tests o3-class or R1-class models round by round. Evidence is from 2023 fine-tuned models, Codex, GPT-3.5/4, and small Lean models. Goedel-V2 and Seed-Prover train correction with reinforcement learning, so their results are about trained correction, not prompted revision. [b14, c12]

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Keep G2 and sharpen it:** revise only when code has produced a located failing output; the revise prompt must include the real checker text. No blind self-review round | G2, S5 | [E] | K01, K04; a10, b15, d05, d06, c16, d08 |
| A2 | **Cap revision at 1 to 2 rounds** (already in S5). The first round holds 84-96% of the gain in the Lean study. Put most budget into diverse first attempts | S5, G12 | [E] | K02, K19; b03, b18, d04, d10, d01 |
| A3 | **Give code-run tools a place in S5.** Where a deterministic solver exists (calculator, interpreter, search, constraint check), try it on the failing piece before asking the model | S5 | [E] | K06; b05, a12, b12 |
| A4 | **Keep passing parts; redo only the failing part** where the answer is made of separable parts and code can find which fail | S5, O3 | [E] | K07; c11, b17 |
| A5 | **Locate the failing step in code, not by the model** (models find errors poorly but fix them well) | G2, S5 | [E] | K21; d07, d02 |
| A6 | **Retrieve own earlier solved items** after the first attempt (matches the lessons rule) | M | [E] | K14; b23, b04 |
| A7 | **Do not add tree search over naive retry for revision;** the gain is small or nil | S5, 4b | [E] | K12; c26, c09 |
| A8 | **Spec check after every revision:** diff the revised answer against the original question and fixed constraints. Fail the revision if it changed. Cheap; the conceptual basis (K18) is established, the drift rate (K23) is single-source | G3, S8 | [E] basis, [S] rate | K18, K23; a05, d13 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Revise-with-error vs resample vs revise-without-error outside formal proofs (code with tests, arithmetic with a calculator, constraint puzzles) at equal tokens | S5 | [S] transfer unknown | K01; a10, d01 |
| T2 | Error-type router: shallow failures to patch, structural failures to re-plan or a fresh sample | S5, S6 | [S] | K22; d11, d16 |
| T3 | Backtracking as a distinct component (restart from an earlier verified step) vs only local patch | S5 | [S] | K05; b08, a17 |
| T4 | Plan with holes (sketch, then fill each hole by tool or fresh attempt) vs direct attempt | S3, O3 | [E] in formal proofs, untested for open tasks | K09; a13, d15, d16 |
| T5 | Plan-level revision vs step-level only; log failure cause first | S5, S6 | [S] | K11, K25; b12, d16 |
| T6 | Critic table: failure class to patch hint vs raw error text | S5 | [S] design only | K17; a01 |
| T7 | A stronger model writes the diagnosis, a cheaper model rewrites | S5, G5 | [S] | K21; d03 |
| T8 | Goal-lock guard measured on real revisions: how often does a passing revision change the question | G2, S8 | [S] | K23; d13 |
| T9 | Format-fix pass before repair, to see how much of repair gain is mechanical | S5 | [S] | K08; b17, d11 |
| T10 | Planner strength vs executor strength at equal tokens | O3 | [C] | K10, K13; a13, c14, d15 |
| T11 | Round-by-round gain for reasoning models | S5 | open | gap 2 |

## 8. Concrete tests on our bench

All arms use the same token budget per item. Count setup and critic tokens. Use fresh or private items to avoid contamination (K20).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 error vs no error | ARC-style items with executable checks on held-out examples; code puzzles with tests | (a) N resamples; (b) 1 draft + revise with real failing output; (c) 1 draft + revise without output | Pass rate at held-out check | (b) over (a) by 1 to 3 points; (c) not above (a) |
| B2 round cap | Same items | 1, 2, 3 repair rounds, budget fixed by reducing first drafts | Marginal pass gain per round | Round 1 over 80% of the total |
| B3 error router | Items with failures classified from checker text | patch all; re-plan all; routed | Pass rate | Routed above both by 1 to 3 points |
| B4 partial repair | Items with separable parts (multi-test code, multi-step arithmetic with checkable steps) | full regeneration vs keep passing parts and redo failing | Pass rate and tokens per solved item | Same pass rate with 30 to 40% fewer tokens (Cobblestone-sized) |
| B5 tool fallback | Items where a solver exists (arithmetic, constraint, search) | LLM only vs LLM then tool on the failing piece | Pass rate | Tool arm clearly ahead |
| B6 plan with holes | Multi-step problems where steps can be checked | direct vs plan with holes filled by independent attempts | Pass rate | Plan arm ahead by 3 to 10 points on hard items; none on easy |
| B7 plan vs step revision | Same items | step-level only vs allow plan rewrite after 2 failures | Pass rate; log plan-error share | Plan rewrite helps only if plan errors exceed about 20% of failures |
| B8 critic strength | Hard code items | same-model critic vs stronger-model critic, same writer | Repair success rate | Stronger critic ahead, as in d02/d03 |
| B9 goal lock | Revision runs on tasks with fixed constraints | accept any passing revision vs diff guard | Share of accepted revisions that changed the question; pass rate | Guard removes violations at small cost |
| B10 format-fix | Reasoning-model outputs that fail parsing | repair loop vs format fixer then repair | Share of gain that is mechanical | Over half of a headline gain may be mechanical |
| B11 retrieval | Items in classes with earlier solved cases | none vs nearest solved cases after first attempt | Pass rate | Ahead on repeated classes |

## 9. What does not transfer, and why

- **Exact checker text.** Isabelle, Coq and Lean give exact, located error messages and a complete specification. Open-domain reasoning rarely has this. Evidence supports "revise only with a checker" and is weak for plain reasoning (critique.md).
- **Library or specification change.** The classic proof-repair task (Pumpkin Pi) has no LLM study. Our agent does not face this task.
- **Trained correction.** Goedel-V2 and Seed-Prover train correction with reinforcement learning. We use prompting, not training.
- **Heavy compute.** Seed-Prover heavy runs take days; Hilbert and Aristotle are not token-matched. Their headline numbers do not fit our budget.
- **Symbolic critics.** Bundy's critics depend on a formal method language (rippling, higher-order unification). Only the idea of a failure-class to patch table carries over. [a01]
- **Hammers.** CoqHammer and Sledgehammer are large shares of PALM and Cobblestone gains. Our equivalent exists only where a solver exists.
- **Small and older models.** Many numbers are from fine-tuned or 2023 models. Reasoning models may behave differently.
- **Benchmarks.** miniF2F is saturated and likely contaminated.
- **No-check tasks.** The schema already uses the first natural answer and agreement there (S0 no-check route). Nothing here argues for a revision round.

## 10. Open questions

1. Does error-guided revision beat resampling at equal tokens outside formal proofs, with constraint puzzles and maths with a calculator? (d01 to d06 are partial.)
2. What is the marginal gain per round for o3-class and R1-class models?
3. Is the Cobblestone saving real beyond Coq, and is it contamination-free?
4. How much of the APOLLO, Goedel and o3-mini repair gain is only syntax or format fixing?
5. Does plan-level revision replicate beyond Lyra and P3? (Only 4 of 48 P3 failures were plan errors.)
6. Do LLMs repair proofs after a library or specification change? No study found.
7. Do Bundy-style critics (failure pattern to patch) help an LLM versus raw error text? No study found.
8. What are the actual counts in Ireland and Bundy 1996 and Melis and Siekmann 1999?
9. Planner strength vs executor strength at equal tokens.
10. How large is the contamination effect on repair gains (post-cutoff rerun)?
11. The PALM dataset size (10,842 / 10,826 / more than 10K) is unresolved.

## 11. Sources

[V] opened and read (by finders or in the critique pass). [M] snippet, abstract or second-hand only. Seed-Prover, Hilbert, Aristotle, DeepSeek-Prover-V2/V1.5, LEGO-Prover, COPRA and Rango numbers were taken from the finders' reading and not re-opened in the critique pass.

| Source | Mark | URL | Evidence ids |
|---|---|---|---|
| Ireland and Bundy (1992) Using failure to guide inductive proof, RP 613 | [V] | https://www.dai.ed.ac.uk/daidb/papers/documents/rp613.html | a01, a02, a25 |
| Ireland and Bundy (1996) Productive use of failure in inductive proof, JAR | [M] | https://link.springer.com/article/10.1007/BF00244470 | a03, c20, d17 |
| Bundy (1988) The use of explicit plans to guide inductive proofs, CADE-9 | [M] | https://link.springer.com/chapter/10.1007/BFb0012858 | a04, c19, b26 |
| Ringer et al. (2020) QED at Large | [V] | https://arxiv.org/abs/2003.06458 | a05, a06, c17, c18 |
| Qi et al. (2015) Analysis of patch plausibility (cited in survey) | [M] | https://arxiv.org/abs/2003.06458 | a23 |
| Ringer et al. (2021) Proof repair across type equivalences | [V] | https://arxiv.org/abs/2010.00774 | a07, a08, b24 |
| REPLica user study of proof engineers (cited) | [M] | https://arxiv.org/abs/2010.00774 | b25 |
| Melis and Siekmann (1999) Knowledge-based proof planning | [M] | https://doi.org/10.1016/S0004-3702(99)00076-4 | a24 |
| First et al. (2023) Baldur | [V] | https://arxiv.org/abs/2303.04910 | a09, a10, b01-b05, c01-c03 |
| Lu et al. (2024) PALM | [V] | https://arxiv.org/abs/2409.14274 | a11, a12, b06-b10, c04, c05 |
| Jiang et al. (2023) Draft, Sketch, and Prove | [V] | https://arxiv.org/abs/2210.12283 | a13, a14, b13, c07 |
| Wang et al. (2023) LEGO-Prover | [V] | https://arxiv.org/abs/2310.00656 | a15 |
| Zheng et al. (2024) Lyra | [V] | https://arxiv.org/abs/2309.15806 | a16, b11, b12, c06, c24 |
| Thakur et al. (2024) COPRA | [V] | https://arxiv.org/abs/2310.04353 | a17 |
| Kasibatla et al. Cobblestone | [V] | https://arxiv.org/abs/2410.19940 | a18, b21, b22, c11, c21, c22 |
| Thompson et al. (2025) Rango | [M] | https://arxiv.org/abs/2412.14063 | a19, b23, c23 |
| Ren et al. (2025) DeepSeek-Prover-V2 | [V] | https://arxiv.org/abs/2504.21801 | a20 |
| Lin et al. (2025) Goedel-Prover-V2 | [V] | https://arxiv.org/abs/2508.03613 | a21, b14-b16, c12 |
| ByteDance Seed (2025) Seed-Prover | [V] | https://arxiv.org/abs/2507.23726 | a22, b19, c13 |
| Ospanov et al. (2025) APOLLO | [V] | https://arxiv.org/abs/2505.05758 | b17, b18, c10 |
| Xin et al. (2024) DeepSeek-Prover-V1.5 | [V] | https://arxiv.org/abs/2408.08152 | c08, c26 |
| Xin et al. (2024) DeepSeek-Prover | [M] | https://arxiv.org/abs/2405.14333 | b27 |
| Liu (2025) ProofAug | [V] | https://arxiv.org/abs/2501.18310 | c09, c25 |
| Varambally et al. (2026) Hilbert | [V] | https://arxiv.org/abs/2509.22819 | c14 |
| Achim et al. (2025) Aristotle | [V] | https://arxiv.org/abs/2510.01346 | c15 |
| Huang et al. (2024) LLMs cannot self-correct reasoning yet | [V] | https://arxiv.org/abs/2310.01798 | b20, c16, c27 |
| Olausson et al. (2024) Is self-repair a silver bullet | [V] | https://arxiv.org/abs/2306.09896 | d01, d02, d03 |
| Chen et al. (2023) Self-Debug | [V] | https://arxiv.org/abs/2304.05128 | d04, d05 |
| Gou et al. (2024) CRITIC | [V] | https://arxiv.org/abs/2305.11738 | d06 |
| Tyen et al. (2024) LLMs cannot find reasoning errors but can correct them | [V] | https://arxiv.org/abs/2311.08516 | d07 |
| Kamoi et al. (2024) When can LLMs correct their own mistakes | [V] | https://arxiv.org/abs/2406.01297 | d08 |
| Deng et al. (2026) Fix, Not Just Resample | [V] | https://arxiv.org/abs/2610.26942 | d09, d10, d11 |
| Woodcock et al. (2026) CAPRI | [V] | https://arxiv.org/abs/2608.13459 | d12, d13 |
| Woodcock et al. (2026) Double-Tank rescue | [V] | https://arxiv.org/abs/2608.18822 | d14 |
| Srinivasan and Patawar (2026) LAMP | [V] | https://arxiv.org/abs/2606.28841 | d15 |
| Li et al. (2026) P3 | [V] | https://arxiv.org/abs/2608.09277 | d16 |

Linked subfields researched in parallel (not covered here): Interactive theorem proving; Neural and LLM proof search; Tree of Thoughts; Language Agent Tree Search; Software, spreadsheet, KB debugging; Cognitive conflict and impasse; Reflection-in-action; Debiasing and cognitive forcing.
