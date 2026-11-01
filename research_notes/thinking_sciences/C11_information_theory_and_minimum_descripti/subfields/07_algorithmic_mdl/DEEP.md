# Algorithmic MDL: deep document

*Subfield C11.07 of information theory and minimum description length. Folder: `research_notes/thinking_sciences/C11_information_theory_and_minimum_descripti/subfields/07_algorithmic_mdl`. Evidence ids (a01..d18) refer to `evidence_a-d.jsonl`; claim ids (K01..K31) refer to `claims.jsonl`. Corrections from `critique.md` are applied here. Evidence covers LLM work up to about early 2026 (ARC Prize 2025 report) but is thin for 2025-2026 reasoning models.*

## 1. What it is

Algorithmic MDL says: the best explanation of data is the shortest program that prints the data. The length of that program is the Kolmogorov complexity K(D). Solomonoff tied this to induction: weight every computable hypothesis by 2^-length, and predict with the mix. [a01, a07]

Three facts frame everything else.

1. It cannot be computed. No procedure returns the shortest program for every D. [a04]
2. It depends on the description language. Two general-purpose languages differ by a constant c that does not grow with the data. For short data, c can decide the answer. Grunwald calls this "arbitrariness". [a03, a04]
3. Statistical MDL (Rissanen 1978) is the practical sibling. It uses a restricted code that is not Turing-universal, so it is computable but cannot capture recursive processes. [a01]

Why it matters to us. Our agent cannot train. It can only run a scaffold. The scaffold touches algorithmic MDL in two places:

- **S2 REPRESENT.** Write the problem as a small program-like model (a rule, a DSL snippet, Python) rather than as prose.
- **S7 SELECT.** When several candidate rules all fit the examples, prefer the shorter one, or the one that compresses the examples best when read in order.

The honest summary of the evidence: program-like representation plus execution checks works and is well measured. A length-based selector is plausible and has theory behind it, but no paper tests it against a vote at equal tokens. That is the core open question (sections 7 to 10).

Terms used below:

- **Two-part code (crude MDL).** Score = L(H) + L(D|H): the rule's length plus the data's misfit given the rule. [a05]
- **Prequential (online) code.** Predict each example from the earlier ones; sum the log-loss. No separate model cost, because the model is built as you go. [b18, c19]
- **Induction vs transduction.** Induction: write a program, run it on the test input. Transduction: predict the test output directly. [b10]
- **Library learning.** Compress solved programs into reusable named helpers. [a12, c13]

## 2. History and theories in depth

**Foundations (1960s to 1978).** Solomonoff (1964), Kolmogorov (1965) and Chaitin (1969) found algorithmic complexity independently. Wallace and Boulton proposed MML in 1968. Rissanen gave the first statistical MDL in 1978 (Automatica 14(5):465-471). These originals were not opened in this research; the facts come from Grunwald's tutorial and Wikipedia. [a01, a03, c26]

**Grunwald's tutorial (2004) [V].** Key points an engineer needs:
- Crude MDL picks H minimising L(H)+L(D|H). L(H) is hard to define fairly.
- Refined MDL replaces it with one universal code per model class (normalised maximum likelihood), with a parametric complexity term COMP(H). It removes the arbitrary choice of L(H).
- For large samples crude MDL matches BIC.
- The claim "simpler generalises better" depends on the model class. [a05, a06]

**Grunwald and Roos (2019) [V].** Modern MDL uses "luckiness functions". MDL and Bayes can behave badly when all candidate models are wrong (misspecification). Lesson: shortest-fit is not safe if the hypothesis class does not contain the truth. Keep a held-out check. [b17]

**Universal induction and AIXI.** Rathmanner and Hutter (2011): the sum of Solomonoff's prediction errors is bounded by a constant that grows with the log of 1/(prior weight of the true source). So errors are finite for any computable world. They call the no-free-lunch assumption (simple and complex worlds equally likely) absurd for the real world. Solomonoff induction assumes only that some structure exists. [a07, a08] Hutter (2000) joined Solomonoff induction with decision theory to give AIXI. It is uncomputable; the time-bounded version AItl needs time of order t*2^l, which is not usable. [a09]

**Levin search and OOPS.** Schmidhuber (2002): test programs with a runtime cap proportional to program probability, doubling the budget each phase. It is a constant factor slower than the best program. OOPS adds reuse of earlier solutions. It solved Towers of Hanoi with 30 disks (solution above 10^9 moves); reusing a prefix sped search by 1000x. The constant factor can be huge; toy domains only. [a10]

**Short strings.** Gauvrit et al. (2014): Kolmogorov complexity fails for strings up to about length 50. A coding-theorem estimate from a universal distribution works better for human randomness data. Estimates depend on the reference machine class. Lesson: with few examples, do not use gzip length as the measure. [b23]

**Chollet (2019) [V].** Intelligence is skill-acquisition efficiency, defined with algorithmic information theory. Priors and experience must be controlled, since unlimited data can "buy" skill. ARC gives 2 to 5 demonstration pairs per task. [a11, c22]

**Human simplicity.** Feldman (2000, Nature): human difficulty on Boolean concepts rises with the length of the shortest equivalent formula, across 41 concept types in six families (abstract only read). Planton et al. (2021): memory for binary sequences follows description length in a small recursive language and beat six rival models (five experiments; abstract only read). Feldman (2016) frames simplicity as a balance between a bias to simple models and a demand to fit. Lake et al. (2015, Science) showed Bayesian program learning matched humans at one-shot character learning (numbers in section 3 are second-hand). Chater and Vitanyi (2003) argue simplicity is a unifying principle; critics say such frameworks fit any result (not opened). [d16, d17, d18, d15, b26]

**Neural networks and simplicity.**
- Valle-Perez et al. (2019): random-parameter nets prefer simple Boolean functions exponentially. [b19]
- Mingard et al. (2025): a Bayesian posterior built from a function prior plus the likelihood predicts SGD-trained net outcomes; the prior depends on architecture (the chaotic regime loses the bias), so simplicity bias is not universal. [b20]
- Blier and Ollivier (2018): variational and two-part codes give poor compression for deep nets, but prequential coding gives far shorter codes. MNIST: uniform code 199 kbits, prequential about 4.10 kbits (ratio 0.02) at 99.5% test accuracy. CIFAR10: uniform 166 kbits, prequential about 45.3 kbits. (Digits read from a garbled table; check before reuse.) [b18]
- Voita and Titov (2020): probe quality measured by total code length separates real from control tasks; accuracy often does not. Control-task code lengths are at least 2x the real-task ones. Seeds change accuracy but not code length. [c21]

**The "language modelling is compression" line (2023 to 2025).**
- Deletang et al. (ICLR 2024): a predictor plus arithmetic coding is a lossless compressor, so log-loss equals code length. [a15]
- Huang et al. (COLM 2024): compression ratio predicts benchmark score (section 3). [a20]
- Grau-Moya et al. (2024): networks trained on data from random universal-Turing-machine programs approximate Solomonoff induction. [a18]
- Elmoznino et al. (ICML 2025): next-token loss over in-context examples equals prequential code length, so in-context learning is pushed toward fit plus simplicity. [c19]

**Program-induction systems (2015 to 2026).**
- Lake 2015 BPL: hand-built stroke primitives, Bayes over programs.
- Ellis et al. DreamCoder (2020/2021): wake-sleep library learning with an MDL/Bayes objective. [a12]
- Wang et al. Hypothesis Search (ICLR 2024): LLM proposes English hypotheses, writes Python, checks on examples. [a26]
- Grand et al. LILO (ICLR 2024): LLM writes programs, Stitch compresses by MDL, LLM names and documents the helpers. [c13]
- Li et al. (ICLR 2025) and Akyurek et al. (2025): induction vs transduction; test-time training. [b10, b12]
- Liao and Gu CompressARC (2025): pure MDL at test time, 76K parameters, no pretraining. [a22]
- Pourcel et al. SOAR (2025): evolutionary program synthesis with a weighted-vote selector. [d05]
- ARC Prize 2024 and 2025 reports: the field moved from brute-force program search to test-time training and LLM-guided program synthesis. [b13, d01]

## 3. Core findings with exact numbers

Status key: **established** = at least 2 independent sources and numbers confirmed in text read by the cross-check; **single-source**; **contested**. "Second-hand" means not read from the original paper.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LM log-loss equals code length; an LLM plus arithmetic coding beats domain compressors | Chinchilla 70B: ImageNet patches 43.4% of raw vs PNG 58.5%; LibriSpeech 16.4% vs FLAC 30.3%; enwik9 raw: Chinchilla 70B 8.3%, Llama 2 7B 8.9%, gzip 32.3%, LZMA2 23.0% | Deletang 2024 [a15, b01, c01] | established |
| Counting model parameters changes the picture | Adjusted (two-part) rate for Chinchilla 70B: 21.9% enwik9 but 185.3% ImageNet and 228.9% LibriSpeech (table cells garbled; cite only the qualitative claim: adjusted rates above 100% off-domain) | Deletang 2024 [a15, b02] | contested (offline vs prequential) |
| Optimal model size depends on dataset size | Small Transformers (200K / 800K / 3.2M params) on enwik: raw rate 30.9 / 21.7 / 17.0; near 100% on random data; about 62% on ImageNet vs gzip 70.7% | Deletang 2024 [b03, c02] | single-source |
| Prequential coding makes deep nets cheap | MNIST 199 kbits uniform vs about 4.10 kbits prequential; CIFAR10 166 vs 45.3 kbits | Blier and Ollivier 2018 [b18] | single-source |
| Compression ratio predicts benchmark score across LLMs | 31 LLMs, 12 benchmarks; overall Pearson about -0.93, RMSE 3.1%; about -0.95 per domain; HellaSwag -0.881, TriviaQA -0.951, MMLU -0.890, DS-1000 -0.946 | Huang 2024 [a20, b04, c03] | single-source |
| That line breaks with leakage, mismatched corpus, non-base models | 3 Qwen models above the fit on GSM8K/MATH; corpus saturates at about 3M characters; base models only | Huang 2024 [b05, a21, c04, d14] | single-source |
| Prompted LLMs write long, wrong "shortest programs" | Length 128: Llama-3.1-405B fails 78%, GPT-4o 40% on natural data (average over modalities, high variance; abstract: 66% / 45% synthetic; body text: 65% / 55%); all prompted models precision above 1 (longer than gzip) | Yoran 2025 Kolmogorov Test [a24, c05] | single-source |
| Most correct programs on natural data just copy the input | Repetition: over 95% of correct programs on natural data, 20% on synthetic | Yoran 2025 [c06] | single-source |
| Length hurts accuracy | Llama-405B audio-8-bit accuracy 47.1% (len 32), 29.9% (64), 20.9% (128) | Yoran 2025 [c06] | single-source |
| CoT and execution feedback barely help; trained models do not transfer | CoT effect -1.3 (8B), -5.1 (70B), +2.1 (405B) points; synthetic-trained 1.5B beats prompted by over 40 points on synthetic, near zero on natural; programs from 10K / 100K / 1M-example models err in first 16 chars in 99% / 93.5% / 88.7% of cases | Yoran 2025 [c07, a25] | single-source |
| Reasoning model no better | o1-mini vs GPT-4o length 128: Accuracy 57.2 vs 56.5; executable 81.7% vs 89.9% (500 subsequences) | Yoran 2025 appendix [d13] | single-source |
| Library learning by compression | DreamCoder list tasks 3.7% to 79.6%, search 235 s to 40 s; CVC4 82.4% vs DreamCoder 84.3% (108 SyGuS, 1 h, 8 CPUs); LOGO/tower near 100% held out vs no baseline above 60%; 93% of 60 physics laws after 8 cycles; mean solve 54.1 s, median 15.0 s; memorise-without-compress solves fewer in every domain | Ellis 2020 [a12, a13, b08, c09, c10] | established |
| LLM plus MDL compression beats DreamCoder | LILO test solve rate vs DreamCoder +33.14 REGEX, +2.26 CLEVR, +20.42 LOGO; LLM solver alone +32.20, -5.83, +3.60; one LLM round costs about the same as 48 CPU-hours of DreamCoder search | Grand 2024 [c13] | established (same lab as DreamCoder) |
| Compressed but unnamed helpers hurt the LLM | Stitch without docs: -30.60 REGEX, -2.91 CLEVR, -11.11 LOGO; AutoDoc recovers +9.73, +2.27, +0.00 | Grand 2024 [c14] | single-source |
| Reuse may not drive LLM library gains | LEGO-Prover: 1,233 lemmas (6%) reach final prover, one reused once; TroVE: 3 reuses in 3,201 questions; no-sharing ablation lost 1 question (12-problem subset) | Berlot-Attwell 2024 [d11] | contested |
| ... but gradient-free helper libraries can help | ReGAL, CodeLlama-13B: +11.5 LOGO, +26.1 date understanding, +8.1 TextCraft; random curriculum order cost 18.7 points on LOGO | Stengel-Eskin 2024 [d12] | contested (prompt tokens not matched) |
| Levin-style reuse speeds search | OOPS prefix reuse 1000x; Hanoi 30 disks | Schmidhuber 2002 [a10] | single-source (toy) |
| Hypothesis-then-program beats direct on ARC | 100 tasks, GPT-4, 64 programs, 3 feedback rounds: direct 17%, program only 23%, summarised hypotheses 30%, human-selected 33%, human-written 45%; 33 of 49 (67%) selected hypotheses gave correct programs; SyGuS 94.3% | Wang 2024 [a26, b16, c11] | established |
| Fitting the examples usually means passing the test | Wang: exactly one exception; Li: about 9% of fitting samples miss the test output; our own data: 2 wrong fitting programs | Wang, Li, own [c12, b10] | contested |
| Narrow tests accept wrong programs | EvalPlus (HumanEval+, 764.1 tests per task): pass@1 down up to 19.3% (ChatGPT -12.6, GPT-4 -13.1, CodeGen-16B -18.5, CodeLlama-34B -17.6, StarCoder -14.1); pass@10 -24.9%; pass@100 -28.9%. CodeContests: over 4000 problems TPR <= 0.1 and TNR >= 0.9 | Liu 2023; Wang 2025 [d07, d08] | established (spec-to-code, 2023 models) |
| Induction and transduction are complementary | Potpourri: transduction with TTT, no rerank 56.75%; transduction reranked, no TTT 43.0%; induction 20k-vote 35.25%. ARC-Heavy: transduction TTT 43.25%, induction 19.25%, ensemble with TTT 38.00% (below transduction alone). Small-compute ensembles 26.50 vs 18.78 vs 15.25 and 19.50 vs 11.07 vs 13.50. Per-task assignment stable (p<.004). Best 56.75% vs average human 60.2%, best human 97.8% | Li 2025 [b10, b11, c16] | established |
| Test-time training lifts ARC | 80-task subset 17.5% to 45.0%; public val 47.1% own model, 53.0% BARC model, 61.9% ensembled with program synthesis; BBH 10-shot 50.5% to 57.8% | Akyurek 2025 [b12, c17] | established (shares models with Li) |
| LMs propose rules well, apply them badly | MiniSCAN: over 80% with interpreter, near zero when the LM applies its own rule; humans 45.9% List Functions, 90.9% ConceptARC | Qiu 2024 [b14, c18] | established |
| Pure MDL at test time | CompressARC (76K params): 34.75% ARC-1 train, 20% ARC-1 eval at pass@2; pass@1 30.25% train and 18.5% eval at 2000 steps; train pass@1 1.0% at 100 steps, 23.0% at 500, 28.0% at 1000; about 20 min per puzzle on RTX 4070; 4% on ARC-AGI-2 | Liao and Gu 2025 [a22, c24, d02] | single-source (same authors; blog and preprint) |
| ARC-AGI-2 winners are test-time-trained nets, not MDL | NVARC 24.03%, ARChitects 16.53%, MindsAI 12.64%, Lonnie 6.67%, Barbadillo 6.53%; 1,455 teams, 15,154 entries; top cost $0.20 per task | ARC Prize 2025 [d01] | established |
| Frontier reasoning models on ARC-AGI-2 | May 2025 semi-private (ARC-1 / ARC-2): o3 medium 53.0 / 3.0; ARChitects 56.0 / 2.5; o4-mini 41.8 / 2.4; Icecuber 17.0 / 1.6; Claude 3.7 8K 21.2 / 0.9. 2024 private: o1-preview 18%, Claude 3.5 Sonnet 14% pass@1 | Chollet 2025 [d04, b13, c23] | established |
| Harness cost-accuracy | Poetiq on Gemini 3 Pro: 31% at $0.81 per task to 54% at $31 per task on ARC-AGI-2 (Poetiq-reported; ARC Prize verified the Gemini run) | ARC Prize 2025 [d02] | single-source |
| Small recursive net, not MDL | TRM 7M: ARC-1 44.6, ARC-2 7.8; HRM 27M 40.3 / 5.0; direct prediction 27M 21.0 / 0.0; o3-mini-high 34.5 / 3.0; Gemini 2.5 Pro 32K 37.0 / 4.9; Grok-4-thinking 66.7 / 16.0 | Jolicoeur-Martineau 2025 [d03] | single-source |
| Selecting among executed programs leaves room | SOAR: 6k programs per task; vote vs oracle gap 9.5 points on average; all-model vote 52.00% vs oracle 57.25%; sample-only 3k 29.67% vs sample+refine 42.67-42.88% (Qwen2.5-Coder-14B, ARC-train); refinement without weight updates beats sampling by about 13 points; test-time 72B 25.62% to 44.87% (fine-tuned) | Pourcel 2025 [d05, d06] | single-source |
| Test agreement is a strong selector | CodeT: code-davinci-002 HumanEval pass@1 47.0% to 65.8%; MBPP 58.1% to 67.7%; Codex pass@100 77.4% vs pass@1 33.5% | Chen 2022 [d09] | single-source (2022 model) |
| Model log-prob is a biased length measure | Plain likelihood prefers short degenerate programs; length normalising overcorrects; Coder-Reviewer wins 43 of 48 dataset-model pairs | Zhang 2022 [d10] | single-source (2022 models) |
| Pretrained LLM did not show Occam behaviour on Mastermind | Prequential code length worse than the empirical-marginal baseline and worse than a small model trained on the family | Elmoznino 2025 [c20] | single-source (1 LLM, 1 puzzle) |
| English hypotheses fit humans better than Python | R2 = .81 with tuned prior, 50-100 proposals per problem, 8 people (number game); GPT-4's own judgments differed | Ellis 2023 [c15] | single-source |
| Universal-prediction nets work within trained length | Transformer-L matches Bayes-optimal CTW on variable-order Markov sources; 15 Chomsky tasks, 400 sequences each; fails at length 1024 after training at 256 | Grau-Moya 2024 [a18, a19, b06, b07] | established (synthetic only) |
| BPL one-shot (second-hand) | 20-way one-shot error: BPL 3.3%, humans 4.5% (upper bound), simple ConvNet 13.5%, Siamese ConvNet 8.0%; later nets 4.0-6.0% on related splits | Lake 2019 progress report [d15] | single-source |
| Brute-force DSL search overtaken | icecuber 20% private (2020 contest); 2024 private: ARChitects 53.5% (TTT), Greenblatt 43% (LLM program sampling), MindsAI 55.5% (ineligible); record 33% at end of 2023 | ARC Prize 2024 [b13, c23] | established |

## 4. Mechanisms and models

Written so an engineer can build each piece. Items that need weight updates are marked and are out of scope for the prompt-only agent.

### 4.1 Log-loss as code length (Deletang; Elmoznino)
- Given a predictor P(x_t | x_<t), the code length of a sequence is the sum of -log2 P(x_t | x_<t). Arithmetic coding realises it to within a few bits. [a15]
- Prequential score of a rule: present examples in order e1..en. For each ei, compute the log-loss of predicting ei's output given the rule in context plus e1..e(i-1). Sum. This needs token log-probs from the model. [c19]
- Caveats: for an instruct model, log-probs are not calibrated codes (K30). A pretrained LLM failed to show the expected effect on Mastermind (c20). Run a calibration check before using it as a selector.

### 4.2 Two-part score for candidate programs (crude MDL)
```
score(p) = L(p) + lambda * misfit(p, examples)
L(p)     = token count or AST node count of p in ONE fixed language (e.g. Python AST nodes)
misfit   = number of example pairs p gets wrong (or bits to patch the residual)
```
- Fix the language and the length counter in code before seeing the data (Grunwald's arbitrariness defect). [a04]
- Never use the model's own log-prob as L(p). It prefers short degenerate programs; normalising overcorrects. [d10]
- With noisy examples, exact fit is wrong. Allow residual error and pay for it in misfit. Qiu et al. tested 0, 12.5, 25 and 50% perturbed examples (per-level numbers not read). [b15]
- Add a guard: reject a rule whose length is close to the length of the data (a copy rule). Over 95% of correct natural-data programs in the Kolmogorov Test were copies. [c06]

### 4.3 Propose, implement, execute (Hypothesis Search)
1. Ask for several abstract English hypotheses.
2. Optionally summarise them (30% vs 23% for raw, in the original setup).
3. For each, write Python.
4. Run on the given pairs; keep those passing all (3 feedback rounds, 64 programs per task in the paper).
5. Apply the survivor to the test input by running it, not by asking the model. [a26, c11, b14]

### 4.4 Induction first, transduction fallback (Li)
- Try program search under a budget. Check on the given pairs. If any program fits, use it. If none fits, answer directly.
- Without test-time training this router is untested. Li's own ARC-Heavy numbers show the ensemble can lose to transduction alone (38.00 vs 43.25). [b11]

### 4.5 Library compression (DreamCoder, LILO, Stitch)
- Wake: solve tasks, collect programs.
- Abstraction: find sub-expressions that repeat across solved programs; replace with a named function when total length (library + programs) drops. This is the MDL objective: L(library) + sum of L(program | library).
- Documentation (LILO): have the LLM write a name and a one-line docstring per abstraction. Without it, compressed names hurt (c14).
- Dreaming (DreamCoder): train a neural guide on replayed and imagined tasks. Needs training; out of scope.
- Agent analogue: a memory of verified helper functions with name and doc, reused in later tasks. Gains depend on task families that actually share subroutines (d11 vs d12).

### 4.6 Levin-style budget (OOPS)
- Phase k: give each candidate program a time cap proportional to its prior probability (short first) times 2^k. Double on failure. This is a mechanical, code-controlled budget. [a10]
- Agent analogue: try short rules with small token caps first; widen only if all fail (compatible with G12).

### 4.7 Test-time MDL (CompressARC)
- Train a tiny net from random initialisation on the one puzzle, minimising reconstruction cross-entropy plus the KL of a latent code. Read the answer from the compressed model. Needs a GPU and 20 minutes per puzzle. Out of scope for a prompt-only agent, but it shows a compression objective alone carries signal on repeated-structure puzzles. [a22, c24]

### 4.8 Verifier width (EvalPlus, CodeT)
- A rule that passes few checks is weakly supported. Widen the check set by generating extra or mutated inputs and compare outputs among candidates. [d07, d09]

## 5. What holds up

**Holds up (several sources, numbers confirmed).**
- Executing a program beats asking the model to apply a rule. MiniSCAN: over 80% with an interpreter, near zero when the LM applies its own rule (b14, c18). Hypothesis Search, Li, and the 2024 ARC leaders (Greenblatt 43%) all rely on running code. [K14, K10]
- Propose-then-implement beats direct answers: 17% to 23% to 30% on 100 ARC tasks. [K10]
- Compressing solved programs into a library speeds search and raises solve rates (DreamCoder 3.7% to 79.6%; LILO beats DreamCoder in three domains). The memorise-only control is worse. [K08]
- Induction and transduction are complementary, stable by task (p<.004). [K12]
- Narrow example checks overstate correctness (EvalPlus -12.6% to -18.5% at pass@1). [K25]
- Pure MDL at test time works on simple repeated structure (20% ARC-1 eval) and falls to 4% on ARC-AGI-2. [K23]
- The winning methods in 2024 and 2025 are test-time-trained neural models, not MDL and not plain prompting. [K22, K23]

**Failures and refutations.**
- LLMs cannot write short programs for real data: 78% and 40% failure; precision above 1; over 95% copies. The reasoning model o1-mini was no better (57.2 vs 56.5). CoT -1.3 / -5.1 / +2.1. [K06, K07, K29]
- A pretrained LLM did not lower prequential code length on Mastermind (worse than the marginal baseline). [K18]
- Compressed abstractions without names hurt the LLM solver (-30.60 REGEX). [K09]
- LLM library-learning systems in math barely reuse learned tools (1 reuse in LEGO-Prover; 3 in 3,201 TroVE questions). [K28]
- The induction-plus-transduction ensemble lost to transduction alone on ARC-Heavy with TTT (38.00 vs 43.25). [K12]
- Compression-predicts-intelligence breaks with contamination and non-base models. [K05, K30]
- Hypothesis Search: compositional search (Parsel) helped human-written hypotheses (47.5%) but hurt model-written ones. The 40-question appendix table reads: direct 12.5, program only 17.5, summarised 27.5, human-selected 37.5. The 37.5 that 47.5 beats is program generation from hypotheses without Parsel, not direct prompting.

**Moderators.**
- Data size: raw compression flatters big models; counting parameters flips the picture off-domain. [K03]
- Corpus match: likelihood tracks the skill only if the text matches the skill. [a21]
- Model type: base models only. [d14]
- Code type: prequential coding and two-part coding give opposite verdicts on whether deep nets compress. [K03]
- Length: learned compressors and universal-predictor nets fail beyond trained length. [K16]
- Number of samples: the false-positive rate of fitting programs rises with pool size (Li about 9% with up to 20k samples; Wang 1 exception in a small subset). [K11]
- Task family: library reuse works when subroutines are shared (ReGAL) and not otherwise (LEGO-Prover, TroVE). [K28]
- Hypothesis language: English fit humans better (Ellis); Python gave more correct execution (Wang, Li). Different goals. [K20]

**Interventions that worked.** Interpreter execution; hypothesis-then-program; summarising hypotheses; docs for helpers; refinement loops (SOAR, about +13 points with no weight update); generated-test agreement (CodeT, +18.8 points on HumanEval); widened tests.

**Interventions that did not work.** Chain of thought on the Kolmogorov Test; execution feedback on program length; synthetic training for real data; unnamed compressed abstractions; the model's own log-prob as a length score.

**Dependence and weak spots (from the cross-check).**
- DreamCoder and LILO share a lab and a library idea. Li, Akyurek and ARC Prize 2024 share the BARC models and the ARC benchmark. Akyurek's 61.9% uses BARC models, so it is not independent of Li.
- ARC subsets are small (80, 100, 40 tasks) with one model; no confidence intervals.
- No study tests a prompt-only scaffold with a code-length selector at equal tokens.
- Lake 2015, Feldman 2000 full text, Rissanen, Chater and Vitanyi were not opened. The human-simplicity findings have no replication data in this set.

## 6. Language models

**What the LLM evidence says in one paragraph.** LLMs are good at proposing rules and writing code that tests them. They are bad at applying their own rules in text, bad at writing short programs for raw data, and not clearly good at acting as a length-based compressor of their own context. The biggest measured gains come from adding execution (a code interpreter) and sampling, not from asking the model to prefer short rules.

**Log-loss as compression.**
- Chinchilla 70B compresses ImageNet patches to 43.4% of raw size (PNG 58.5%) and LibriSpeech to 16.4% (FLAC 30.3%). On enwik9 it reaches 8.3% raw (Llama 2 7B 8.9%, gzip 32.3%, LZMA2 23.0%). Once parameters are counted, off-domain rates exceed 100%. [a15, b01]
- Compression ratio on fresh text tracks benchmark score: Pearson about -0.93 over 31 base LLMs and 12 benchmarks, RMSE 3.1%. Per benchmark: HellaSwag -0.881, MMLU -0.890, DS-1000 -0.946, TriviaQA -0.951. Three Qwen models sit above the fit on math (leakage). Not shown for fine-tuned or reasoning models. [a20, b05, d14]

**Writing short programs.**
- Kolmogorov Test, length-128 natural data: Llama-3.1-405B fails 78%, GPT-4o 40% (averages; high variance). GPT-4o accuracy by modality: 35.6 (audio 16-bit), 15.0 (audio 8-bit), 29.6 (MFCC), 24.8 (DNA), 6.5 (text); Llama-405B 18.0 / 10.1 / 24.2 / 22.5 / 9.6. Precision 1.66 to 3.17 for GPT-4o (worse than gzip). [a24, b21]
- Over 95% of the correct programs on natural data copy the input. [c06]
- What changed it: a 1.5B model trained on synthetic data beat prompted models by over 40 points on synthetic data and fell to near zero on natural data. CoT gave -1.3 / -5.1 / +2.1 points. Execution feedback helped little. o1-mini: Accuracy 57.2 vs GPT-4o 56.5. [c07, d13]

**Rule induction with execution.**
- GPT-4 on 100 ARC tasks: direct 17%, program 23%, summarised hypotheses 30%, human-selected 33%, human-written 45%. [a26, c11]
- Greenblatt-style LLM program sampling scored 43% on the private set; o1-preview 18% and Claude 3.5 Sonnet 14% pass@1 without it. [b13, c23]
- Li et al.: induction rises with sample count (35.25% at 20k votes on Potpourri) but about 9% of fitting samples are false positives. [b10]
- SOAR: refinement alone (no weight update) raises Qwen2.5-Coder-14B from 29.67% (3k samples) to about 42.7-42.9% (3k sampled + 3k refined, ARC-train). The vote selector leaves 9.5 points to oracle. [d05]
- Qiu et al.: the same model collapses from over 80% to almost zero on MiniSCAN when it must apply its own rule. [b14]

**Frontier reasoning models on ARC.**
- ARC-AGI-2 semi-private, May 2025: o3 medium 53.0 on ARC-1 but 3.0 on ARC-2; o4-mini 2.4; Claude 3.7 8K 0.9. [d04]
- With a refinement harness: Gemini 3 Pro 31% at $0.81 per task to 54% at $31 per task on ARC-AGI-2 (vendor-reported; run verified by ARC Prize). Harness and verifier carry the gain. [d02]
- Test-time-trained neural models led ARC-AGI-2 in 2025 (NVARC 24.03%). [d01]
- Not MDL: a 7M-parameter recursive net scored 44.6% / 7.8% (ARC-1 / ARC-2), above o3-mini-high (34.5 / 3.0) and Gemini 2.5 Pro (37.0 / 4.9) on ARC-1. [d03]

**In-context learning as compression.**
- Theory: next-token loss on in-context examples is prequential code length (Elmoznino); trained meta-learners prefer simpler functions, most in low-data regimes. [c19]
- Test on a pretrained LLM: Mastermind prequential code length was worse than the marginal baseline. One LLM, one puzzle family. [c20]
- Model log-prob is a length-biased ranking score for code; Coder-Reviewer (adding a reviewer term) wins 43 of 48 pairs. 2022 models. [d10]

**Library and memory.**
- LILO (LLM + compression + docs): +33.14 REGEX, +2.26 CLEVR, +20.42 LOGO vs DreamCoder. Compression without docs hurts the LLM (-30.60 / -2.91 / -11.11). [c13, c14]
- ReGAL (no weight updates): +8.1 to +26.1 points for CodeLlama-13B. Library Learning Doesn't: near-zero reuse in LEGO-Prover and TroVE. [d11, d12]

**What is missing.** No 2025-2026 reasoning-model result on the Kolmogorov Test other than o1-mini. No test of o3-class, Claude or Gemini thinking models on compression-based selection. No test of a prompt-only code-length selector.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = the agent's stored items. Status: [E] established, [S] single-source, [C] contested. Evidence ids in brackets point to `evidence_a-d.jsonl`; K ids to `claims.jsonl`.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Apply a proposed rule by running code, never by asking the model to apply it. Rule appliers in text collapse (over 80% to near zero on MiniSCAN). | G2/G5, S4 | [E] | b14, c18, c11 (K14) |
| A2 | In S2/S3 for rule-like tasks: propose abstract hypotheses first, then implement each as code, then execute on the given examples. 17% to 23% to 30% on ARC (GPT-4). Already implied by the schema; confirm as the default for rule-induction items. | S2/S3/S4 | [E] | a26, b16, c11, b13 (K10) |
| A3 | A pass on the given examples is not proof. Add a held-out or mutated-input check before accepting a fitting program. Wide test suites cut measured pass rates 12.6-18.5% (pass@1); about 9% of fitting samples fail on the test output in large pools. This matches G3; the new part is to measure the false-pass rate and to widen checks. | G3, S8 | [E] | d07, d08, b10 (K25) |
| A4 | Fix the description language and the length counter in code before ranking by length. The result must not flip when the counter changes. Never use the model's own log-prob as program length. | G5, S7 | [E] for the language dependence; [S] for the log-prob warning | a03, a04, b23, d10 (K02, K27) |
| A5 | Keep a direct-answer fallback (G6): if no program fits within the budget, answer directly. Induction and transduction solve different tasks. Do not assume the combination always wins (ARC-Heavy: ensemble 38.00 below transduction 43.25). | S3/S7, G6 | [E] for complementarity; routing without TTT untested | b10, b11, c16 (K12) |
| A6 | Do not trust a self-claimed "shortest" or "simplest" rule. Check length with code and reject copy-the-data rules. | G10, S7 | [S] | a24, c06, c07 (K06, K07) |
| A7 | When a verified helper function is saved to memory, save a name and a one-line doc with it. Compression alone hurt a solver by up to 30.60 points; docs recover part of it. | memory | [S] | c14, c13 (K09) |
| A8 | Treat program sampling plus execution as the baseline to beat before adding any compression-based step. | G7 | [S] | b13, c23, d01 (K22) |
| A9 | Do not use model likelihood as a quality proxy for instruct or reasoning models. Do not count a frozen model's size as free. | G7 | [S] | d14, a15 (K30, K03) |

A1, A2 and A3 are already close to what the schema says (G2, G3, G5); this research adds numbers, not new rules. A4 to A9 are cautions that cost nothing.

### Test first (not established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Shortest consistent program (fixed-language length) vs weighted vote vs first-fit among programs that all pass the examples. Gap between vote and oracle in SOAR is 9.5 points, so there is room. | S7 | [C] open; no paper | d05, d09 (K24, K26) |
| T2 | Prequential score (summed log-loss over examples in order) as a selector for candidate rules; check it ranks like held-out accuracy before trusting it. | S7 | [S]; one LLM failed on Mastermind | c19, c20, c21 (K17, K18) |
| T3 | Mutated-input check at S8 and the count of programs it catches. | G3, S8 | [C] | d07, b10 (K11, K25) |
| T4 | Router: program first, direct answer as fallback, prompt-only. | S3/S7 | [E] complementarity, untested without TTT | b10 (K12) |
| T5 | Helper memory (named, documented, verified helpers) vs storing whole past solutions vs no memory, on a task family with shared subroutines. Includes a zero-reuse control and a break-even task count. | memory | [C] | c13, d11, d12 (K08, K28) |
| T6 | Length penalty (per-rule cost) on or off in ranking. | S7, G7 | [C] | a15, b18 (K03) |
| T7 | English vs Python as the S2 representation language. | S2 | [S] | c15 (K20) |
| T8 | Levin-style budget: short rules first with small caps, double on failure. | S6, G12 | [S] theory and toy domains | a10 (K02) |
| T9 | Reasoning-model write-short-program ability on our items (Kolmogorov-style). | S2, S7 | [S] | d13 (K29) |
| T10 | Noise tolerance: rank with residual error allowed instead of exact fit. | S7 | [S]; no numbers | b15, b17 |

Items that are out of scope for a prompt-only agent: test-time training (K13), CompressARC (K15), universal-predictor pretraining (K16), DreamCoder's neural guide.

## 8. Concrete tests on our bench

All tests: both arms use the same token budget (including setup, G7). Same items, same model, same seeds. Report mean and a bootstrap interval; at least 3 seeds. Items: rule-induction tasks with 2 to 5 examples, a hidden held-out input, and a way to run code. Use at least 100 items where the budget allows (the ARC subsets in the literature are 80 to 100 and gave no intervals).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Shortest vs vote | ARC-style grid tasks; list/string functions | Same pool of N programs per item. Arm A: weighted vote by output. Arm B: among programs fitting all examples, choose the shortest (fixed AST count). Arm C: first fit. Optional D: shortest, ties by vote. | Exact match on the held-out input; also gap to oracle | B within 0 to +5 points of A. SOAR leaves 9.5 points to oracle, so the cap is below that. If B is below A, length is not worth adding. |
| T2 Prequential selector | Rule families with several plausible rules | Rank by summed log-loss over ordered examples vs rank by held-out accuracy of the same candidates (oracle for the check), vs rank by length | Rank correlation of selector with held-out accuracy; top-1 accuracy | Moderate positive correlation on base models; low or negative on instruct models (K30, K18). |
| T3 Mutated-input check | Items where programs pass all examples | Arm A: accept first fit. Arm B: accept first fit that also agrees with the majority on 5 to 10 mutated inputs. | False-pass rate on held-out input; tokens spent | B cuts false passes by a few points at under 15% extra tokens. Literature: about 9% false-positive rate (Li), 12.6-18.5% overstatement (EvalPlus). |
| T4 Router | Mixed items | A: direct answer only. B: program only. C: program first, direct fallback. | Accuracy | C at or above max(A, B) at small budget (Li: 26.50 vs 18.78 and 15.25); may lose at large budget (ARC-Heavy). |
| T5 Helper memory | Task family with 30 to 60 items sharing 3 to 5 subroutines; plus a zero-shared-subroutine family | A: no memory. B: whole past solutions. C: named, documented helpers. D: unnamed compressed helpers. Libraries sized to equal prompt tokens. | Accuracy on later items; reuse count; tokens | On the shared family C above A and B and D (D hurts, K09). On the zero-shared family C equal to A (K28 shows reuse near zero). Find break-even item count. |
| T6 Length penalty | Same as T1 | Select by fit only vs fit plus length vs fit plus length plus rule-size penalty | Held-out accuracy | Small or zero effect when examples are many; larger when examples are 2 to 3. |
| T7 English vs Python | S2 representation | Hypothesise in English then code vs hypothesise in code directly | Accuracy; false-pass rate | Python direct does about equal on accuracy; English may help on human-like judgment tasks (K20). |
| T8 Levin budget | Items of mixed difficulty | Uniform token cap per candidate vs doubling cap, shortest first | Solve rate at fixed total tokens | Gain on easy items, no loss on hard ones; interacts with G12. |
| T9 Kolmogorov-style probe | Synthetic sequences, length 32 to 128 | Our reasoning model vs our plain model; program length vs gzip | Accuracy; precision; copy rate | No gain from reasoning (o1-mini 57.2 vs 56.5). A probe, not a schema test. |
| T10 Noisy examples | Rule items with 12.5, 25, 50% corrupted examples | Exact-fit filter vs residual-tolerant ranking | Held-out accuracy | Exact-fit fails as noise grows; tolerant ranking holds. No numbers in the literature. |

## 9. What does not transfer, and why

- **Test-time training (Akyurek 17.5 to 45.0; 47.1 / 53.0 / 61.9).** Needs weight updates on the task's own examples. Our agent does not train. Closest proxy is accumulating verified example pairs in the prompt.
- **CompressARC (20% ARC-1 eval, 4% ARC-AGI-2).** A per-puzzle neural net and 20 GPU-minutes. Not a scaffold. Shows only that a compression objective alone carries signal, and that it does not scale to ARC-AGI-2.
- **DreamCoder's dreaming and recognition model.** Needs a day on 20 to 100 CPUs and a hand-built starting language. We can borrow the memory idea, not the training.
- **Universal-predictor training (Grau-Moya).** Pretraining on random UTM programs. Fails beyond trained length (256 to 1024). Not a prompt method.
- **Compression-benchmark correlation (Huang).** Holds for base models only. Our agent runs instruct or reasoning models, where the line is unstudied. Also needs a matching corpus. Useful for choosing between base models, not for scoring one answer.
- **Ideal Kolmogorov/Solomonoff selection.** Uncomputable. Depends on the language. For 2 to 5 examples the language constant can dominate the choice. Use it as a ranking heuristic only.
- **Kolmogorov Test as a model of our tasks.** Raw data sequences, not task rules. Failure there (78% / 40%) does not say our tasks fail, only that "write the shortest program" cannot be trusted from the model's say-so.
- **Deep-net simplicity bias (Valle-Perez, Mingard).** About SGD-trained nets on Boolean tasks; the prior changes with architecture. Supports a short-rule default only as background.
- **Human simplicity results (Feldman, Planton).** Small fixed languages chosen by the authors, abstracts only read, no replications found. Support a short-rule tie-break as plausible; they do not show it helps an LLM.
- **Hand-built DSL search (icecuber 20% private).** Overtaken in 2024. Brute-force search is not our route.
- **Hypothesis Search's human-written and human-selected hypotheses (45%, 33%).** A human in the loop is not available.
- **Lake 2015 BPL.** Needs hand-built stroke primitives and a clean toy domain.

## 10. Open questions

1. Does the shortest consistent rule beat vote or first-fit at equal tokens? No paper tests it (gap 1). This is the core S7 question.
2. How often does a fitting program fail a held-out or mutated input in 2025-2026 frontier models, as a function of sample count? (Wang: 1 exception; Li: about 9%.)
3. Do o3-class, Claude and Gemini thinking models do better on the Kolmogorov Test than GPT-4o and Llama-405B, or do they still copy the input? Only o1-mini is tested.
4. Does an LLM's in-context loss behave like prequential code length across rule families? Elmoznino tested one LLM on one puzzle. If not, a log-prob-based selector is unsafe.
5. Does a named, documented helper memory help at equal tokens when no weights change? What is the break-even number of tasks?
6. What does a per-rule cost term do to selection when rules are English vs Python? Does the winner flip with the language (Grunwald's arbitrariness defect in practice)?
7. How much of the induction-transduction complementarity survives without test-time training?
8. Are Lake 2015 and Feldman 2000 replicated, and do human error patterns on Boolean concepts match LLM error patterns?
9. Does pure MDL at test time scale, or does it help only on puzzles with simple repeated structure? (CompressARC: 20% on ARC-1, 4% on ARC-AGI-2; no scaling study.)
10. Does the compression-benchmark line hold for fine-tuned and reasoning models?
11. Is the numerical gap between vote and oracle (9.5 points) closable by any selector, or is part of it noise?

## 11. Sources

Marking: [V] = opened (full text or the relevant page read by an agent in this research); [M] = snippet or memory only. Notes in brackets give the extent. Several [V] entries were re-opened in the cross-check (Deletang, Huang, Wang, Akyurek, Li, Ellis, Grand, Yoran, Liao and Gu); the others were opened by the earlier evidence agents and not re-opened.

- [V] Wikipedia, Minimum description length. https://en.wikipedia.org/wiki/Minimum_description_length (read through a fetch summary; background only)
- [V] Grunwald (2004) A Tutorial Introduction to the Minimum Description Length Principle. https://arxiv.org/abs/math/0406077
- [V] Grunwald and Roos (2019) Minimum Description Length Revisited. https://arxiv.org/abs/1908.08484
- [V] Rathmanner and Hutter (2011) A Philosophical Treatise of Universal Induction. https://arxiv.org/abs/1105.5721
- [V] Hutter (2000) A Theory of Universal Artificial Intelligence based on Algorithmic Complexity. https://arxiv.org/abs/cs/0004001
- [V] Schmidhuber (2002) Optimal Ordered Problem Solver. https://arxiv.org/abs/cs/0207097
- [V] Chollet (2019) On the Measure of Intelligence. https://arxiv.org/abs/1911.01547
- [V] Gauvrit et al. (2014) Complexity for short strings (coding theorem method). https://arxiv.org/abs/1106.3059
- [V] Deletang et al. (2024) Language Modeling Is Compression. https://arxiv.org/abs/2309.10668 (table cells garbled; abstract and enwik9 raw column safe)
- [V] Huang, Zhang, Shan and He (2024) Compression Represents Intelligence Linearly. https://arxiv.org/abs/2404.09937
- [V] Grau-Moya et al. (2024) Learning Universal Predictors. https://arxiv.org/abs/2401.14953
- [V] Yoran et al. (2025) The KoLMogorov Test: Compression by Code Generation. https://arxiv.org/abs/2503.13992
- [V] Liao and Gu (2025) ARC-AGI Without Pretraining (CompressARC), preprint https://arxiv.org/abs/2512.06104 and blog https://iliao2345.github.io/blog_posts/arc_agi_without_pretraining/arc_agi_without_pretraining.html (blog read through a fetch summary; numbers are the authors' own)
- [V] Ellis et al. (2020/2021) DreamCoder. https://arxiv.org/abs/2006.08381
- [V] Wang et al. (2024) Hypothesis Search: Inductive Reasoning with Language Models. https://arxiv.org/abs/2309.05660
- [V] Grand et al. (2024) LILO. https://arxiv.org/abs/2310.19791
- [V] Ellis (2023) Human-like Few-Shot Learning via Bayesian Reasoning over Natural Language. https://arxiv.org/abs/2306.02797
- [V] Li et al. (2025) Combining Induction and Transduction for Abstract Reasoning. https://arxiv.org/abs/2411.02272
- [V] Akyurek et al. (2025) The Surprising Effectiveness of Test-Time Training for Few-Shot Learning. https://arxiv.org/abs/2411.07279
- [V] Qiu et al. (2024) Phenomenal Yet Puzzling: Inductive Reasoning with Hypothesis Refinement. https://arxiv.org/abs/2310.08559 (noise-level numbers are in figures, not read)
- [V] Chollet et al. (2025) ARC Prize 2024 Technical Report. https://arxiv.org/abs/2412.04604 (read by an earlier agent; not re-opened)
- [V] Chollet, Knoop, Kamradt, Landers (2026) ARC Prize 2025 Technical Report. https://arxiv.org/abs/2601.10904
- [V] Chollet, Knoop et al. (2025) ARC-AGI-2. https://arxiv.org/abs/2505.11831
- [V] Jolicoeur-Martineau (2025) Less is More: Recursive Reasoning with Tiny Networks. https://arxiv.org/abs/2510.04871
- [V] Pourcel, Colas, Oudeyer (2025) SOAR. https://arxiv.org/abs/2507.14172
- [V] Liu et al. (2023) EvalPlus. https://arxiv.org/abs/2305.01210
- [V] Wang et al. (2025) CodeContests+. https://arxiv.org/abs/2506.05817
- [V] Chen et al. (2022) CodeT. https://arxiv.org/abs/2207.10397
- [V] Zhang et al. (2022) Coder-Reviewer Reranking. https://arxiv.org/abs/2211.16490
- [V] Berlot-Attwell, Rudzicz, Si (2024) Library Learning Doesn't. https://arxiv.org/abs/2410.20274
- [V] Stengel-Eskin, Prasad, Bansal (2024) ReGAL. https://arxiv.org/abs/2401.16467
- [V] Elmoznino et al. (2025) In-Context Learning and Occam's Razor. https://arxiv.org/abs/2410.14086
- [V] Voita and Titov (2020) Information-Theoretic Probing with MDL. https://arxiv.org/abs/2003.12298
- [V] Blier and Ollivier (2018) The Description Length of Deep Learning Models. https://arxiv.org/abs/1802.07044 (digits from a garbled table)
- [V] Valle-Perez et al. (2019) Deep learning generalizes because the parameter-function map is biased towards simple functions. https://arxiv.org/abs/1805.08522
- [V] Mingard et al. (2025) Deep neural networks have an inbuilt Occam's razor. https://arxiv.org/abs/2304.06670
- [V] Lake, Salakhutdinov, Tenenbaum (2019) The Omniglot challenge: a 3-year progress report. https://arxiv.org/abs/1902.03477
- [V] Feldman (2000) Minimization of Boolean complexity in human concept learning, Nature 407:630-633. https://pubmed.ncbi.nlm.nih.gov/11034211/ (abstract only)
- [V] Planton et al. (2021) A theory of memory for binary sequences. https://pubmed.ncbi.nlm.nih.gov/33465081/ (abstract only)
- [V] Feldman (2016) The simplicity principle in perception and cognition. https://pubmed.ncbi.nlm.nih.gov/27470193/ (abstract only)
- [M] Lake, Salakhutdinov, Tenenbaum (2015) Human-level concept learning through probabilistic program induction, Science 350:1332-1338. https://www.science.org/doi/10.1126/science.aab3050 (HTTP 403; do not cite numbers from it)
- [M] Chater and Vitanyi (2003) Simplicity: a unifying principle in cognitive science? https://doi.org/10.1016/S1364-6613(02)00005-0
- [M] Rissanen (1978) Modeling by shortest data description. https://doi.org/10.1016/0005-1098(78)90005-5
- [M] Gruenwald (2007) The Minimum Description Length Principle (book). https://mitpress.mit.edu/9780262072816/
- [M] Solomonoff (1964), Kolmogorov (1965), Chaitin (1969): original papers not opened; facts via Grunwald (2004).

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 10 established claims: 7 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C11.07-K12** (now single-source: the sources are not independent). Numbers and p<.004 verified, but every supporting source is the same paper (Li et al. 2024/2025); the ARC Prize report adds nothing on induction vs transduction.
- **C11.07-K17** (reworded: the sources support less). Voita and Titov say variational and online codes agree and are both more stable than accuracy; 'more stable than variational codes' is not supported (Blier and Ollivier show variational codes compress poorly, not that they are unstable). Corrected claim: Description length is a more stable probe of model complexity than accuracy: Voita and Titov find code lengths separate real from control tasks and ignore seed noise, with variational and online codes agreeing; Blier and Ollivier show prequential coding gives far shorter codes than variational or two-part codes for deep nets; Elmoznino et al. show prequential ICL prefers simpler functions.
- **C11.07-K19** (now single-source: the sources are not independent). Both papers come from Ard Louis's Oxford group (Valle-Perez is a coauthor of the 2025 paper), so they are one lab's line of work; content matches.
- **C11.07-K16** (now single-source: only one opened source, code check).
- **C11.07-K23** (now single-source: only one opened source, code check).
