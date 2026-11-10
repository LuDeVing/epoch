# Interactive theorem proving: deep document

*Subfield C06.04. Evidence: evidence_a-d.jsonl (a01-a26, b01-b26, c01-c26, d01-d20), claims.jsonl (K01-K25), critique.md. Evidence ids are cited in brackets. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Neural and LLM proof search, proof planning and repair, and autoformalization have their own parallel subfields; here we only note links.*

## 1. What it is

An interactive theorem prover (ITP) is a program in which a human or a machine writes a proof step by step and a small trusted kernel checks every step. Isabelle/HOL, Lean, Coq (now Rocq), HOL Light and Metamath are the main systems. The proof is a program in the system's language. The kernel either accepts it or rejects it. There is no partial credit and no opinion.

Three parts matter for our agent.

1. **The kernel.** In the LCF design only a few hundred lines of trusted code can create a theorem. HOL Light's kernel is "a few hundred lines of OCaml", and its logic was itself formally verified [a01, a02]. Tactics, search code and language models sit outside the kernel. They can be wrong without making a false theorem.
2. **Proposers.** Humans write tactics. Since 2020 language models also propose steps (GPT-f), whole proofs (Baldur, DeepSeek-Prover), lemma plans (Hilbert, Seed-Prover), and calls to symbolic tools (Thor, Sledgehammer).
3. **The loop.** Propose, check, read the checker's error, repair or backtrack. This is the cleanest example of schema state S8 VERIFY: an external, deterministic verdict that does not depend on the model's own judgement.

What the kernel does NOT check is the statement. A correct proof of a wrongly stated theorem passes. This is the largest remaining hole, and the 2026 audit shows it is real (section 5).

Why it matters for the schema: guardrails G2 (revise from real output), G3 (pass on something not fitted), G5 (code selects) and G10 (reasoning text is not evidence) all hold in their strongest form here. The open question is how much transfers to tasks with no kernel.

## 2. History and theories in depth

**Trust architecture.** The LCF idea of a small kernel plus untrusted tactics dates from the 1970s (background knowledge, not re-opened). Proof search can be arbitrarily clever and unsafe without risk. Hales et al. (2015) show the payoff: referees of the 1998 Kepler conjecture proof could not certify all the computer parts, so a team re-proved it in HOL Light and Isabelle. The main statement re-checks in about 5 hours on one 2 GHz CPU; some subclaims take over a day; the hardest about 5000 CPU hours [a01]. The project took over ten years.

**Proof engineering cost.** seL4's first correctness proofs took about 20 person-years and 480,000 lines of specification and proof by 2014. Csmith found 79 GCC bugs and 202 LLVM bugs and none in verified parts of CompCert [b22]. Across nine projects, effort is roughly linear in proof size (abstract-level only, no coefficient) [b23, b24]. This is why automation was wanted.

**Hammers (2010).** Sledgehammer sends a goal and selected facts to external provers and rebuilds the proof inside Isabelle's kernel, so the outside prover is never trusted. Original evaluation figures (about 1200 or 1240 goals, about 48% solved) were not opened and disagree between sources [b26, a11]; we do not use them.

**Learning to prove, 2019-2021.** CoqGym: ASTactic proves 12.2% of test theorems; CoqHammer 24.8% with extended time; combined 30.0%, +5.2 over the hammer [b25]. GPT-f (2020): a transformer proposes Metamath steps, best-first search with kernel checking assembles proofs. 56.22% of held-out set.mm theorems versus 21.16% for the prior prover; 23 shorter proofs were accepted into the real library [a04, a06, b01]. PACT (2021) added co-training on auxiliary tasks mined from proof terms: mathlib held-out 32% to 48.4% [a07, b04].

**Benchmarks.** miniF2F (488 problems, 244 valid and 244 test, from AMC, AIME, IMO and course material) gave a cross-system yardstick [a08, b06]. ProofNet gave undergraduate problems [b15]. PutnamBench (1692 formalisations of 640 Putnam problems across Lean 4, Isabelle, Coq) was nearly unsolved in 2024 [a23, b21].

**Tool integration, 2022-2024.** Thor lets the model decide when to call Sledgehammer [a10, b07]. DSP drafts an informal proof, turns it into a formal sketch, and lets mechanical tools fill the gaps [a13, b08]. Baldur writes whole proofs and repairs them from error messages [a12, b14]. LeanDojo adds premise retrieval and fixes the harness [a15, b12]. COPRA is an in-context GPT-4 agent with backtracking [c10, d14]. Lean Copilot puts the model inside the human's editor [a18, c09].

**Scale and reasoning models, 2024-2026.** DeepSeek-Prover V1 and V1.5, Kimina-Prover, Goedel-Prover V1/V2, DeepSeek-Prover-V2, Seed-Prover and Hilbert moved miniF2F-test from about 25% to about 99% and PutnamBench from about 1/640 to 331/657 and 462/660 [a19-a22, b16-b20, c21].

**Auditing the benchmarks, 2024-2026.** Autoformalised statements are often flawed [c15, d10]. A 2026 audit of 13 benchmark variants certified 398 faulty items [d08, d09].

**Competing explanations for the gains.** (a) Search and learning from kernel feedback (GPT-f, HTPS). (b) Scale and sampling budget (pass@k at thousands of samples). (c) Context and retrieval, not size (Baldur, LeanDojo, Rango). (d) A strong informal reasoner plus decomposition (Hilbert, DeepSeek-V2, Seed-Prover). (e) Contamination of public benchmarks. No paper separates these cleanly; section 5 says which comparisons come closest.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A small kernel gives full trust; HOL Light kernel is a few hundred lines | Kepler main statement re-checks in about 5 h on one 2 GHz CPU; hardest subclaim about 5000 CPU h | Hales 2015 [a01, a02] | [E] |
| LM step proposer plus kernel-checked search beats prior automation (Metamath) | 56.22% vs 21.16% held-out; search width 2,4,8,16,32: 42.90, 47.29, 51.26, 54.05, 56.50 (gains per doubling +4.39, +3.97, +2.99, +2.45) | GPT-f [a04, b01] | [E] |
| Pretraining on non-formal text helps | 700m: 31.58 to 42.56 with WebMath; 160m 28.96 to 34.79; 1.5B 42.39 (no gain over 700m) | GPT-f [b02] | [E] |
| Auxiliary-task co-training helps | mathlib 32% to 48.4%; sizes 121m 35.1, 163m 39.8, 837m 48.4; temporal hold-out 45.6 (1,350 theorems after Apr 2020), 43.3 (544 after Sep 2020); future-mathlib 37.1 (1043) vs tidy-bfs 21.8, refl 11.6 | PACT [a07, b04, b05] | [E] |
| Library score does not carry to competition problems | Metamath GPT-f 56.22 in-library vs 1.3 pass@1 on miniF2F; ReProver 51.2 random vs 26.3 novel-premises | miniF2F, LeanDojo [a09, b06, a15, b12] | [E] |
| Neural plus symbolic beats either | Thor PISA 39.0 to 57.0; Sledgehammer 25.7; union only 48.8; 8.2% solved only by Thor; Baldur+Thor 65.7 vs Thor 58.0; Cobblestone 48% vs Proverbot9001/CoqHammer 30%/27%; CoqGym combined 30.0 | [a10, b07, a12, b14, c12, b25] | [E] |
| LM premise selection is weak | only 1.9% of premise-bearing LM steps advanced the proof vs 28.2% of steps without premises | Thor [a10] | [S] |
| Context beats size | Baldur 8b+context 47.5, 62b+context 47.9 (+0.4); LeanDojo retrieval 51.2 vs 47.6; Rango proof retriever 22.2 to 32.0 (500 theorems) | [a12, b14, a15, d16] | [E] |
| Draft-sketch-prove lifts miniF2F-test | 20.9 (Sledgehammer+heuristics) to 39.3 (human drafts), 38.9 (LLM drafts); ablations valid/test: no informal -3.7/-5.3, no comments -4.9/-2.8, no automated provers -9.8 | DSP [a13, b08, c05] | [E] |
| DSP reproduced by another group | Lyra with GPT-4: 38.9 (GPT-4 drafts), 39.7 (human drafts) at 100 attempts | Lyra [d13] | [E] |
| Informal draft adds little over retrieval | COPRA 29.09 to 29.92 (+0.83) | [d14] | [S] |
| Bigger drafter did not help (unclear) | Minerva test 36.5/34.0/30.3 in one reading, 36.5/37.7/38.9 in another | DSP [a14, b09] | [C] |
| Feedback loop beats independent samples inside proofs | COPRA GPT-4: few-shot 1 sample 13.52, 60 samples 15.98, COPRA 60 queries 26.63; no backtracking 24.59; +retrieval 29.09; 100 queries 30.74. GPT-3.5 COPRA 9.02 | [c10, d14] | [E] |
| Self-correction from compiler output | Goedel-V2 32B pass@32 88.1 to 90.4; 92.7 at pass@32 with 5 rounds vs 92.2 at pass@8192 without | [a21, d06] | [S] |
| Repair step adds a small amount | Baldur repair +1.3 (24.9 to 26.2) | [b14] | [E] |
| Outside proofs, self-repair about zero at equal samples | GPT-4 on APPS: 10 initial + 1 repair each = 1.05x pass@20; 2 initial + 10 repairs each = 0.97x pass@22 | Olausson [d04] | [E] |
| Feedback quality limits repair | own explanation repairs 33.3% vs expert human 52.6% (1.58x, small study) | [d05] | [S] |
| Retrieval of similar proofs or lemmas | LEGO-Prover miniF2F-valid 47.1 to 50.4 (50 attempts); Hilbert retrieval: reasoner tokens 4.0M to 2.3M, miniF2F 97.9 to 99.2 | [d17, d12] | [E] |
| Decomposition plus informal reasoner | DeepSeek-V2 88.9 miniF2F-test (217/244), 47/658 PutnamBench; Seed-Prover 99.6, PutnamBench 331/657 (prior 86); Hilbert miniF2F 99.2, 462/660 (70.0%) vs Seed 331/657 (50.4%); Hilbert D=0 pass@4 75 vs D=2 98.36, D=3 98.7 | [a20, b20, c21, d11] | [E] |
| The reasoner dominates in Hilbert | Putnam: Gemini 2.5 Pro variant 462/660 vs gpt-oss-120b variant 88/660 (13.3%) | [d11] | [S] |
| CoT mode beats non-CoT at lower tokens for equal accuracy | DeepSeek-V2 671B CoT pass@32 82.4 (about 216k tokens, our arithmetic) vs non-CoT pass@1024 76.7 (about 780k tokens). Tokens per sample 761.8 non-CoT, 6751.9 CoT | [d02, d03] | [S] (not a clean ablation) |
| miniF2F-test pass@k, DeepSeek-V2 671B CoT | 61.9 / 82.4 / 86.6 / 88.9 at pass@1/32/1024/8192 | [d02] | [E] |
| miniF2F-test pass@k, Kimina-Prover Preview 72B | 52.94 / 65.16 (pass@8) / 68.85 (pass@32) / 77.87 (pass@1024) / 80.74 (pass@8192) | [d01] | [E] |
| Test-time scaling has diminishing returns | DeepSeek-Prover V1 30.03 greedy to 50.0 at 65,536 samples | [b16] | [E] |
| Tools misjudge good proofs | lean-gym misjudged 21.1% of correct human proofs; LeanDojo 1.4% | [a16, b13] | [E] |
| Statements are often flawed | at least 20% of autoformalised statements flawed; 118 of 371 (31.8%) Lean 4 ProofNet ports flawed; best autoformalisation 45.1% on ProofNet# vs 31.0% single sample | [c15, d10] | [E] |
| Benchmarks hold certified faults | 13 variants, 4,833 findings, 398 certified; an apply? bug passed 3 DeepSeek-Prover-V2 7B proofs with a hidden sorry | Faults in Our Formal Benchmarking [d08] | [S] |
| LLM auditors: high recall, low precision | Sonnet 4.5 recall 0.82, precision 0.30, accuracy 68.1%; GPT-5.2 recall 0.91, precision 0.24, accuracy 54.6% | [d09] | [S] |
| Contamination signals | Putnam-AXIOM o1-preview 41.94% original, 19.6 points lower on variations; Rango edge over Tactician shrinks to 30.1 vs 28.3 post-cutoff; Seed-Prover 81.8 on MiniCTX-v2 vs o4-mini 44.3 | [d18, d16, d07] | [C] |
| PutnamBench half-life | 2024: GPT-4 1, COPRA 1, ReProver 0 of 640 (Lean); DSP 4, Sledgehammer 3 (Isabelle); Tactician 0, CoqHammer 0 of 412 (Coq). 2025: 331/657 and 462/660 | [a23, b21, b20, c21] | [E] |
| Failure taxonomy (Coq, GPT-3.5, 520 errors) | wrong theorem application 49.6%, invalid reference 15.2%, incorrect rewrite 11.7%, redundant intros 10.8%, tactic misuse 8.5%, bullet misuse 3.7%; backtracking 6.5% to 40.4%; each rule-based repair +3.0 to +6.9 | PALM [c11, d15] | [S] |
| Human tooling saves steps | Lean Copilot automates 74.2% of steps vs 40.1% AESOP; manual tactics 2.08 vs 3.86 | [a18, c09] | [S] |
| Expert proof writing | N=8 (4 F*, 4 Verus), 4 tasks, about 90 min sessions; planners shortest median time, 100% success; sessions with 0-4 open errors did better | [d19] | [S] |
| General LLMs without proof training score low | GPT-4 few-shot miniF2F 13.52; LeanDojo zero-shot 29.0 vs 51.2; Selene GPT-4 ACC#1 one-line proofs 41.7, medium 7.7, hard 0 | [c10, a15, c16] | [E] |

## 4. Mechanisms and models

**4.1 Kernel-gated generate loop (the base pattern).**
```
state = goal
loop until budget gone:
  cand = model.propose(state, context)      # step, tactic, or whole proof
  verdict = kernel.check(state, cand)       # deterministic
  if verdict.accepted: record, advance
  else: keep verdict.error text
accept only a complete proof the kernel accepts, with no sorry/oops/extra axioms
```
Search wraps this: best-first with a value model (GPT-f width 2 to 32 [b01]), AND-OR hypertree (HTPS [a17, b10]), tree search with exploration bonus (RMaxTS 62.7 vs 60.2 single pass [b17]). For a scaffold the point is the gate, not the search algorithm.

**4.2 Checker-error repair.** Give the model the failing proof and the checker's raw output; ask for a fixed proof. Baldur: generate then repair, +1.3 [b14]. Goedel-V2: 5 rounds with compiler messages, 128k context; removing the error text lowers correction accuracy [d06]. COPRA keeps failed steps and error text in the prompt and backtracks [c10]. Feedback quality is the limit: own explanations 33.3% vs expert 52.6% [d05]. Implementation: code (not the model) selects the failing line and message; the model gets one slot "fix this".

**4.3 Hammer call (neural proposer plus symbolic closer).** At a step the model may emit a "call tool" action. Code runs premise selection and an external prover (python or solver in our case) and reconstructs the result inside the checker. Thor: 39.0 to 57.0, 8.2% only by Thor [a10]. The tool's output is accepted only after reconstruction by the kernel.

**4.4 Draft, sketch, prove.** (1) Model writes an informal proof. (2) Model turns it into a formal skeleton with holes. (3) A mechanical prover plus heuristics closes each hole. (4) The kernel checks the whole. Drops: no automated provers -9.8; no informal proofs -3.7 valid / -5.3 test [b08]. Success plateaus after about 70 attempts [b09]. The mechanical closer mattered most.

**4.5 Recursive decomposition (Hilbert, Seed-Prover, DeepSeek-V2).** A reasoner writes a plan as lemma statements with the main theorem assumed from them. A prover attempts each lemma. Failed lemmas are split again to depth D. Solved lemmas go in a library. Hilbert: D=0 75, D=3 98.7 on miniF2F [d11]. Retrieval of earlier verified lemmas cut reasoner tokens 4.0M to 2.3M [d12]. LEGO-Prover keeps a growing library: 22,532 skills, +3.3 [d17].

**4.6 Retrieval.** Index prior verified material (premises, whole proofs). Rango: full 160 of 500 (32.0%); without lemma retriever 159 (31.8%); without proof retriever 111 (22.2%); no retrieval 89 (17.8%). Similar proofs matter, lemmas barely [d16]. LeanDojo retriever R@10 38.4 vs BM25 17.2 [c07].

**4.7 Statement guard.** Verify what is being proved. Controls: back-translation, a second formalisation checked for equivalence (BEq+), human audit of a sample. LLM auditors work only as a screen (recall 0.82-0.91, precision 0.24-0.30) [d09, d10].

**4.8 Verifier hygiene.** Count sorry, oops, timeouts and unsafe axioms as failure [c16, c26]. Pin tool versions (apply? bug in Lean before 4.20.0 [d08]). Test the harness on known-good proofs (lean-gym 21.1% false rejects [a16]).

## 5. What holds up

**Strongly supported (multiple sources).**
- Kernel-verified output has no false positives from the proof side. Every system relying on it benefits (K01).
- A learned proposer plus a checker beats classical automation alone: GPT-f, PACT, Thor, Baldur [a04, a07, a10, a12].
- Hybrids beat parts: Thor 57.0 vs 39.0 and 25.7; the union is only 48.8, so the gain is real combination, not just coverage [b07].
- Context and retrieval give more than scale: Baldur +0.4 from 8b to 62b with context [a12]; GPT-f 1.5B no better than 700m [b02]; retrieval +47% in Rango [d16].
- Scores do not transfer across libraries or splits [a09, b05, b12]. PACT's own temporal hold-out reports 45.6 and 43.3 against 48.4, a modest drop, and 37.1 on a newer split [b05].
- Scoring is fragile: harness errors (21.1%), flawed statements (20%, 31.8%), certified faults (398) [a16, c15, d10, d08].
- Benchmarks saturate within about a year (PutnamBench from about 0 to 50-70%) [a23, b20, c21].

**Replications.**
- DSP reproduced by Lyra with GPT-4 at 100 attempts: 38.9 and 39.7 against DSP's 38.9 and 39.3 [d13]. This is the only independent replication of a headline result in the evidence set.
- No independent re-run of Seed-Prover or Hilbert. No output audit of either [d08, d09].

**Contested or failed.**
- Does repair beat resampling? Inside proofs, yes at equal query counts (COPRA 26.63 vs 15.98; Goedel-V2 92.7 at pass@32 with 5 rounds vs 92.2 at pass@8192, about 2% of the tokens by our arithmetic) [d14, d06]. Outside proofs at equal samples, about no (1.05x, 0.97x) [d04]. Hence K04 is [C]. COPRA and Goedel compare query or pass counts, not matched tokens.
- Size of the drafter in DSP: two readings of the same table [a14, b09]. [C].
- Contamination: indirect and mixed (Putnam-AXIOM -19.6 points; Rango edge 30.1 vs 28.3) [d18, d16]. No Lean prover has a published variant test.
- The Kimina vs DeepSeek number clash was a mislabel in our earlier notes; resolved [d01, d02].
- HTPS cumulative numbers (82.6% Metamath, 58.6% miniF2F-valid) include training on the statements; do not compare with test numbers [a17, b10].
- The Lean GPT-f counts in a08 (29/244, 43-44/244) are not in the paper; use 24.6 / 29.2 [b06].

**Moderators.**
- System: Metamath has no tactics and proofs of 10-20 steps; Lean/Isabelle/Coq 1-3 steps [a04]. Scores across systems are not comparable.
- Split: random vs novel premises (51.2 vs 26.3) [a15].
- Budget: pass@1 to pass@8192 spans 61.9 to 88.9 for the same model [d02].
- Mode: CoT vs non-CoT shifts both accuracy and tokens [d02, d03].
- Difficulty: Selene GPT-4 one-line proofs 41.7, mid-size 7.7, hard 0 [c16].
- Overlap of the library with pretraining data [a03].

**Interventions that worked.** Kernel gating; error text in repair; hammer or tool calls; retrieval of similar verified proofs; lemma decomposition; CoT mode; backtracking (COPRA +2.0; PALM 6.5 to 40.4); a growing verified skill library (+3.3).

**Interventions that did not.** A bigger model given good context (+0.4); synthetic data raised to 5% of the training mix (hurt [b03]); bigger drafter in DSP (not helpful in one reading); more sampling past a plateau (Lean GPT-f imax beyond 4 [a08]; DSP about 70 attempts [b09]); self-explanation without good feedback (33.3%) [d05]; LM premise selection inside steps (1.9% useful) [a10].

## 6. Language models

**Without proof-specific training.** Low on hard tasks: GPT-4 1/640 on PutnamBench Lean; 29.0 vs 51.2 on LeanDojo random; 13.52 few-shot on miniF2F-test; GPT-3.5 few-shot 2.8; GPT-3.5 in COPRA 9.02; CodeLlama in COPRA 5.73 [a23, a15, c10]. A scaffold (COPRA) roughly doubles GPT-4: 13.52 to 26.63 [c10]. Gemini 2.5 Pro alone: 49.1% on miniF2F at 16,384 attempts, against 99.2% inside Hilbert [c21].

**With training and test-time compute.** Timeline on miniF2F-test: GPT-f Lean 24.6 pass@1 [b06]; Thor 29.9 [b07]; DSP 39.3 [b08]; HTPS 41.0 pass@64 [b10]; DeepSeek-Prover V1 50.0 at 65,536 [b16]; V1.5 60.2 single pass, 62.7 with tree search [b17]; Kimina 72B 80.74 at pass@8192 [d01]; DeepSeek-V2 88.9 [d02]; Goedel-V2 92.7 [d06]; Seed-Prover 99.6 and Hilbert 99.2 [b20, c21]. PutnamBench: 1 (2024), then 47/658 (DeepSeek-V2), 86/657 (Goedel-V2), 331/657 (Seed-Prover), 462/660 (Hilbert) [a20, a21, b20, c21].

**What changed the numbers.**
1. Reinforcement learning on kernel feedback: V1 50.0 to V1.5-RL 60.2; RL worth +3.7 over SFT with CoT and RMaxTS (about 59.0) [b17].
2. Long chain of thought: 671B CoT beats non-CoT at every k (61.9 vs 59.5 at pass@1; 88.9 vs 78.3 at 8192) [d02]. It costs about 9x tokens per sample (6751.9 vs 761.8) [d03].
3. Decomposition and a strong informal reasoner (D=0 75 to D=3 98.7) [d11]. Swapping Gemini 2.5 Pro for gpt-oss-120b drops Putnam from 70.0% to 13.3% (88/660) [d11].
4. Retrieval: +47% relative (Rango) and token savings (Hilbert) [d16, d12].
5. Self-correction from compiler output: +2.3 (Goedel-V2), or matching 8192 samples at about 2% of tokens [d06].
6. Sampling: V1 greedy 30.03 to 50.0 at 65,536, with shrinking gain per doubling [b16, b01].

**Error behaviour.** Coq with GPT-3.5: wrong theorem application is 49.6% of 520 errors; backtracking gave the largest scaffold gain [d15]. Selene: over half of errors were unfinished goals [c16]. LLM auditors of statements: recall 0.82-0.91, precision 0.24-0.30 [d09].

**Caveats.** Almost all headline numbers are lab self-reports at large budgets. PutnamBench is the only neutral check and was measured in 2024. Contamination for public benchmarks is not audited for provers [d18, d16].

**Outside formal proofs.** Olausson (GPT-4 on APPS): self-repair about equal to equal-sample resampling; good human feedback lifts repair from 33.3% to 52.6% [d04, d05]. This is the closest evidence for how the pattern behaves with a partial checker (unit tests): the checker helps selection, but self-generated feedback adds little.

## 7. What our agent should take

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Treat an executable checker's verdict as the only final accept; no accept on model opinion. Already G2/G3; the evidence is strongest here. | G, S8 | [E] | a01, a02, a04, b22 (K01) |
| A2 | Harden the verifier: reject empty or always-true checks, forbid escape hatches (the analogue of sorry/oops/extra axioms), count timeouts as failure, pin tool versions, test it on known-good answers for false rejects. | G, S8 | [E] | a16, b13, c16, c26, d08 (K10, K17) |
| A3 | Repair step shows the raw checker output, located by code, not a model-written summary. Already G2. Keep at most 2 rounds (repair gains are small: +1.3 in Baldur). | S5 | [E] | b14, a21, d06, d05 (K20) |
| A4 | Pair the model with a deterministic tool (code run, solver, symbolic check) and let the tool's output decide. | O, S4 | [E] | a10, b07, a12, c12, b25 (K03) |
| A5 | Memory holds checker-verified solved cases only, retrieved by similarity, shown after the first attempt (consistent with SCHEMA section 5). Strong in formal domains; transfer untested. | memory | [E] formal / untested elsewhere | d12, d16, d17, a15 (K05, K22) |
| A6 | Context and retrieval before scale or longer thinking. | memory, G12 | [E] | a12, a15, b02, d16 (K05) |
| A7 | Evaluate on held-out families and post-cutoff or perturbed variants; report budget with every number. | G | [E] | a09, b05, b12, d18 (K09) |
| A8 | Stop sampling when the gain per doubling falls under a threshold (+4.39 down to +2.45 in GPT-f). | G12 | [E] | b01, b16 (K11) |
| A9 | Keep the "try another branch after error" path in S5/S6. Backtracking: COPRA +2.0 (E); PALM 6.5 to 40.4 (single source). | S5, S6 | [E] / [S] | c10, d15 |
| A10 | Use an LLM audit only as a high-recall screen; flagged items go to an executable or human check. | G5, S8 | [S], low risk | d09 (K24) |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Verify-and-repair vs independent samples at equal total tokens on checkable non-proof tasks. Formal results favour repair; outside proofs it is a wash. Put most budget on first attempts. | S5/S8 | [C] | d04, d05, d06, d14 (K04) |
| T2 | Draft-then-checkable-plan: write the plan in prose, convert to steps each with a check, close gaps by tool. One lab plus one replication, 2023 models. | S3, O3 | [S] | a13, b08, d13, d14 (K07) |
| T3 | Lemma decomposition with a verified lemma library. Not token-matched in the literature. | O3, memory | [S] | d11, d12, d17, d03 (K13) |
| T4 | Verified-case retrieval for non-formal problems. | memory | [S] | d12, d16, d17 (K22) |
| T5 | Failure-category logging and targeted repair by category. | S5, S6 | [S] | d15, c16 (K21) |
| T6 | Statement guard: restate the task and check the restatement before accepting. | S1, S8 | [S] | d08, d10, d09 |
| T7 | Plan-first, few-open-errors discipline in the loop. | S5 | [S] | d19 (K25) |
| T8 | Long-CoT vs many short samples at equal tokens inside S3. Prover evidence says CoT wins; G11 says short attempts win elsewhere. | G11 | [C] | d02, d03 |

## 8. Concrete tests on our bench

All arms use the same total token budget, counting setup, retries and checker overhead. At least 3 seeds; report pass rate with a 95% interval.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | ARC-style items with a held-out check; code tasks with unit tests | (a) k independent attempts, select by check; (b) 1 attempt plus up to 2 repairs showing raw failing output, remaining tokens on first attempts | pass rate on unfitted part | repair about equal (0.97-1.05x); above 1.10x, add T1 to S5 |
| B2 | Same items | repair with raw checker output vs repair with a model-written critique | pass rate; right-to-wrong flips | raw output higher (33.3 vs 52.6 pattern) |
| B3 | Algebra or numeric items with a symbolic checker | plain; checker-select; checker plus repair | pass rate | checker-select gains; repair adds little |
| B4 | Multi-step items | flat reasoning vs decompose into checkable lemmas (O3) with a lemma library | pass rate; tokens per solved item | gain on long items, none on short |
| B5 | Items with prior solved cases | no memory vs retrieved verified cases vs retrieved unverified cases | pass rate; tokens per solve | verified > none > unverified |
| B6 | Reworded or perturbed items | with restatement guard vs without | rate of passes on the wrong problem | guard cuts mis-specified passes at under 10% token cost |
| B7 | Mixed set | prose plan then check vs direct answer | pass rate | small gain on long items; none on easy |
| B8 | Verifier audit | 50 known-good, 50 known-bad, and vacuous answers (empty check, always-true) | false-reject rate; vacuous-pass rate | false rejects under 2% (LeanDojo 1.4%); vacuous passes 0 |
| B9 | Mixed difficulty | one long CoT vs n short samples at equal tokens | pass rate by difficulty | CoT wins hard items; short wins easy |
| B10 | Failure log | tag each failed step by category | share per category | shows which scaffold fix to build first |

## 9. What does not transfer, and why

- **The kernel itself.** Most real tasks have no complete checker. A kernel is sound for a closed logic. Unit tests, symmetries and held-out examples are partial and can pass wrong answers. This is why G3 requires an unfitted check.
- **Training effects.** RL on kernel feedback, co-training on proof artifacts, WebMath pretraining and expert iteration are training. We do not train (K06).
- **Large sampling.** pass@8192 and 65,536 samples are not affordable here; G11 and G12 stand [b16, d02].
- **Pass numbers across systems.** Metamath 56.22 vs miniF2F 1.3; library vs competition; random vs novel premises [a09, b12].
- **Decomposition gains in headline form.** Hilbert and Seed-Prover use millions of tokens per problem and strong proprietary reasoners [d11]. Matched-token benefit is unmeasured.
- **Proof error taxonomies.** PALM's categories are Coq tactic errors with GPT-3.5 [d15].
- **Library retrieval.** Premise names have clean identity; free-text problems do not. Retrieval of similar solved problems may be noisier.
- **Statement fidelity.** A formal statement has one meaning once written; natural tasks have none fixed.
- **Human-in-the-loop efficiency (Lean Copilot).** Not a user study and not our setting [a18].

## 10. Open questions

1. Does verify-and-repair beat independent sampling at equal tokens for algebra with a symbolic check? No study found.
2. How much of the 2025 headline scores (Seed-Prover, Hilbert) is inflated by flawed statements or checker loopholes? No output audit exists [d08, d09].
3. Does draft-then-formalise hold with 2025 reasoning models as drafters? Hilbert hints that the reasoner dominates (70.0 vs 13.3), but there is no clean ablation.
4. Decomposition at matched tokens against flat prompting. Hilbert D=0 pass@4 vs D=3 is not matched [d11].
5. User studies of humans with LLM copilots (time, error rate, trust). Only expert telemetry without LLM help (N=8) [d19].
6. Contamination of provers on public benchmarks: no variant test for any Lean prover; IMO 2025 was formalised by the lab itself and not independently re-run [d07].
7. Does retrieval of verified prior cases help non-formal tasks?
8. Which failure categories can a scaffold fix with a 2025 model? PALM's taxonomy is GPT-3.5 and Coq only.
9. A Lean kernel bug (July 2026) is only a search snippet [d20]. How often do kernels accept false statements in practice?
10. Does the Goedel-V2 token advantage (about 2% of tokens) hold under identical sampling settings?

## 11. Sources

[V] opened (full text or page read). [M] snippet or secondary only.

- [V] Hales et al. (2015) A formal proof of the Kepler conjecture. https://arxiv.org/abs/1501.02155 (a01, a02)
- [V] mathlib Community (2020) The Lean mathematical library. https://arxiv.org/abs/1910.09336 (a03)
- [V] Polu and Sutskever (2020) Generative language modeling for automated theorem proving (GPT-f). https://arxiv.org/abs/2009.03393 (a04-a06, b01-b03, c01)
- [V] Han et al. (2021/22) Proof Artifact Co-Training. https://arxiv.org/abs/2102.06203 (a07, b04, b05, c02)
- [V] Zheng, Han and Polu (2021/22) miniF2F. https://arxiv.org/abs/2109.00110 (a08, a09, b06, c03)
- [V] Jiang et al. (2022) Thor. https://arxiv.org/abs/2205.10893 (a10, b07, c04)
- [M] Bohme and Nipkow (2010) Sledgehammer: judgement day. https://isabelle.in.tum.de/~nipkow/pubs/ijcar10.html (a11, b26; numbers disagree, not used)
- [V] First et al. (2023) Baldur. https://arxiv.org/abs/2303.04910 (a12, b14)
- [V] Jiang et al. (2023) Draft, Sketch, and Prove. https://arxiv.org/abs/2210.12283 (a13, a14, b08, b09, c05)
- [V] Yang et al. (2023) LeanDojo. https://arxiv.org/abs/2306.15626 (a15, a16, b12, b13, c07)
- [V] Lample et al. (2022) HyperTree Proof Search. https://arxiv.org/abs/2205.11491 (a17, b10, b11, c06)
- [V] Song et al. (2024) Lean Copilot. https://arxiv.org/abs/2404.12534 (a18, c09)
- [V] Xin et al. (2024) DeepSeek-Prover. https://arxiv.org/abs/2405.14333 (b16, c15)
- [V] Xin et al. (2024) DeepSeek-Prover-V1.5. https://arxiv.org/abs/2408.08152 (a19, b17, b18)
- [V] DeepSeek-AI / Ren et al. (2025) DeepSeek-Prover-V2. https://arxiv.org/abs/2504.21801 (a20, c19, d02, d03)
- [V] Lin et al. (2025) Goedel-Prover. https://arxiv.org/abs/2502.07640 (c17)
- [V] Lin et al. (2025) Goedel-Prover-V2. https://arxiv.org/abs/2508.03613 (a21, d06)
- [V] ByteDance Seed (2025) Seed-Prover. https://arxiv.org/abs/2507.23726 (a22, b20, c20, d07)
- [V] Kimina-Prover team (2025) Kimina-Prover Preview. https://arxiv.org/abs/2504.11354 (b19, c18, d01)
- [V] Varambally / Wang et al. (2025-26) Hilbert. https://arxiv.org/abs/2509.22819 (c21, d11, d12)
- [V] Tsoukalas et al. (2024) PutnamBench. https://arxiv.org/abs/2407.11214 (a23, b21, c14)
- [V] Ringer et al. (2020) QED at Large. https://arxiv.org/abs/2003.06458 (b22)
- [V] Staples et al. (2014) Productivity for proof engineering. https://trustworthy.systems/publications/nictaabstracts/Staples_JAMKK_14.abstract (b23; abstract page only)
- [V] Matichuk et al. (2015) Leading indicator for cost of formal software verification. https://trustworthy.systems/publications/nictaabstracts/Matichuk_MAJKS_15.abstract (b24; abstract page only)
- [V] Yang and Deng (2019) CoqGym. https://arxiv.org/abs/1905.09381 (b25)
- [V] Azerbayev et al. (2023) ProofNet. https://arxiv.org/abs/2302.12433 (b15, c22)
- [V] Welleck and Saha (2023) LLMSTEP. https://arxiv.org/abs/2310.18457 (c08; no user-study numbers)
- [V] Thakur et al. (2024) COPRA. https://arxiv.org/abs/2310.04353 (c10, d14)
- [V] Lu, Delaware, Zhang (2024) PALM. https://arxiv.org/abs/2409.14274 (c11, d15)
- [V] Kasibatla et al. (2024) Cobblestone. https://arxiv.org/abs/2410.19940 (c12)
- [V] Thompson et al. (2024/25) Rango. https://arxiv.org/abs/2412.14063 (c13, d16)
- [V] Zhang et al. (2024) Selene. https://arxiv.org/abs/2401.07663 (c16, c26)
- [M] Sanchez-Stern et al. (2020) Proverbot9001. https://arxiv.org/abs/1907.07794 (c24; cited secondhand)
- [V] Olausson et al. (2024) Is self-repair a silver bullet for code generation? https://arxiv.org/abs/2306.09896 (d04, d05)
- [V] Ammanamanchi, Bhat, Biderman (2026) Faults in Our Formal Benchmarking. https://arxiv.org/abs/2606.29493 (d08, d09)
- [V] Poiroux et al. (2024/25) ProofNet# and BEq+. https://arxiv.org/abs/2406.07222 (d10)
- [V] Zheng et al. (2023) Lyra. https://arxiv.org/abs/2309.15806 (d13)
- [V] Wang et al. (2023/24) LEGO-Prover. https://arxiv.org/abs/2310.00656 (d17)
- [V] Gulati et al. (2025) Putnam-AXIOM. https://arxiv.org/abs/2508.08292 (d18)
- [V] Jain et al. (2025) What's in a Proof? https://arxiv.org/abs/2508.02733 (d19)
- [M] Lean community Zulip thread on a kernel bug (2026, search snippet). https://leanprover-community.github.io/archive/stream/219941-Machine-Learning-for-Theorem-Proving/topic/DeepSeek-Prover.20V2.20TODO.20List.html (d20)
- Our own syntheses a24-a26 and c25 are derived from the lines above, not independent sources.
