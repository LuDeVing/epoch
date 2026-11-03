# Fluid reasoning (Gf): deep document

*Subfield A13.02. Built from evidence_a-d.jsonl (a01-a26, b01-b26, c01-c25, d01-d16), claims.jsonl (K01-K23) and critique.md in this folder. Evidence ids are cited in brackets. Where a source was seen only as a snippet, the text says so. Gaps are named, not filled.*

---

## 1. What it is

Fluid reasoning (Gf) is the ability to reason, form concepts and solve problems with unfamiliar information or novel procedures. This is the Cattell-Horn-Carroll (CHC) definition [a03]. It is set against crystallised ability (Gc), which is applying learned relations and stored knowledge [a02].

In plain terms. Gf is what you use when no stored routine fits. Gc is what you use when one does.

Typical Gf tests: Raven's matrices, series completion, classification tasks, letter-string analogies, and (in AI) the Abstraction and Reasoning Corpus (ARC). In each, the rule must be induced from a few examples and then applied to a new case.

Why it matters for our agent. The schema has an S0 gate that must "sort problems by novelty". Gf research is the nearest science of what "novel" means and what solving it takes. It gives:

- A definition of novelty (no stored routine applies).
- Tasks that isolate novelty (counterfactual variants, fresh puzzle sets).
- Measured behaviour of language models on such tasks, 2020-2026.

Important limit up front. No source in this folder tests a novelty sort as a gate for an LLM agent. The S0 links in section 7 are inferred, not measured [critique.md]. Primary papers from 1943 and 1967 were not read (see section 2).

---

## 2. History and theories in depth

### 2.1 Origins (secondhand only)

- Cattell (1943), "The measurement of adult intelligence", Psychological Bulletin 40(3):153-193, first split general ability into fluid (gf) and crystallised (gc) [a01]. Only the citation was seen. No data was read. Do not quote results from it.
- Horn and Cattell (1967), "Age differences in fluid and crystallized intelligence", Acta Psychologica 26:107-129, is cited as showing opposite age trends: Gf peaks in young adulthood and then declines, Gc keeps rising until old age [a02, d15]. The Wikipedia summary gives a Gf peak near age 27, described as elusive and disputed. Gc is stable and declines after about 65 [a02]. Sample sizes and Gf loadings are not in any opened source [d15]. Status: [S], secondhand (K15).
- Secondary summaries say that an omnibus IQ hides these opposite trends [d15, snippet].

### 2.2 CHC theory

- Gf and Gc are both broad factors under general intelligence (g). Carroll (1993) reanalysed 461 factor-analytic datasets [a03]. The Wikipedia article gives no Gf-to-g loading and no narrow abilities for Gf. So the numbers behind the claim "Gf is nearly g" are not in this evidence set.
- Original Gf measures: Raven-type matrices, series completion, classification [c24, snippet].

### 2.3 Cognitive account of matrix tests

- Carpenter, Just and Shell (1990) built a computational account of Raven's Advanced Progressive Matrices. By its abstract, two abilities separate high from low scorers: inducing abstract relations, and managing many goals in working memory [a07]. Only the abstract was seen (full text returned HTTP 403). No numbers verified.
- Kyllonen and Christal (1990) report that latent working-memory and reasoning factors correlate very highly [a26]. Not read. Number not verified.
- Chuderski and Necka (2012) ask whether working-memory capacity, control or both feed Gf [a25]. Snippet only. A "62%" figure circulating in project notes is unverified.
- One eye-movement study (N=34) gives indirect support for the memory-and-comparison account. See section 4.1 [a06].

### 2.4 Working-memory training as a test of the theory

If working memory limits Gf, training it should raise Gf. Jaeggi et al. (2008) said it did. Later work did not confirm it. See section 5 [a04, a05, b21, b22].

### 2.5 The Flynn effect and schooling

- Raw scores on fluid-type tests rise about 2.31 IQ points per decade across 285 studies [b23].
- Education adds roughly 1 to 5 IQ points per extra year [b24, abstract only].
- Both are background for the claim that "Gf" is partly trainable by exposure to test-like material. Both are human findings with no direct lever on a frozen model.

### 2.6 Chollet and ARC: Gf as skill-acquisition efficiency

- Chollet (2019) defines intelligence as skill-acquisition efficiency over tasks unknown in advance, given priors and experience. He links CHC fluid versus crystallised to "efficiency versus stored skill" and proposes ARC as a Raven-like fluid test built on core-knowledge priors [a16, b20]. ARC format: a few demonstration grids, predict the output grid, three attempts allowed. No human norm data is in that paper [b20].
- This is the most useful bridge to our setting. It gives an operational test of "novel": a task whose answer cannot be retrieved from stored skill.
- Later reports show the test can be partly gamed by search, training and brute force. See section 5 and section 6.

### 2.7 Analogy as the core of Gf in AI studies

Webb, Holyoak and Lu (2023) tested GPT-3 on matrix-like (Digit Matrices), letter-string, verbal and story analogies [a08]. Their claim: emergent analogical reasoning. Critics replied with counterfactual versions (section 5). The dispute is the main live theory question for LLM Gf: reasoning versus reciting [a15].

---

## 3. Core findings with exact numbers

Status key. established = two or more independent sources; single = one source; contested = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Humans solve unfamiliar grid puzzles at high rates (H-ARC) | 1,729 people, 800 tasks. Training 76.2% [73.3, 77.2]. Public eval 64.2% [55.9, 68.9]. 790 of 800 tasks solved by at least one person in 3 tries | LeGris et al. 2024 [a17, c14] | established |
| ARC-AGI-2 first-party human test | 407 participants, 515 sessions, 1,848 test pairs, 13,405 attempts, 8,277 solved (62%), median 2.3 min. Every kept task solved by at least 2 non-experts | Chollet et al. 2025 [a19, b15, c16] | established |
| High-end humans on ARC-AGI-1 | Two testers on private tasks scored 97% and 98%. Over 97% for high-end humans. 99% of public eval tasks solved by at least 1 of 10 MTurk workers | ARC Prize 2024 report; ARC-AGI-2 paper [a18, a20, b13] | established |
| ConceptARC: humans vs machines | Humans 91% overall, 83-97% per concept. Kaggle first place 52%. GPT-4 about 25% (overall figure from paper prose, not table). GPT-4 under 30% on 15 of 16 concepts | Moskvichev et al. 2023 [a11, b09, c08] | established |
| ConceptARC per concept | Center 0.97 vs 0.20. Count 0.86 vs 0.03. Copy 0.93 vs 0.07. Inside/Outside 0.83 vs 0.27 (humans vs GPT-4) | [a22] | established |
| Richer prompt barely helps GPT-4 | One-shot 0.33 overall (zero-shot 0.19 at temp 0, 0.25 at temp 0.5). Minimal tasks (48): humans 0.95, GPT-4 text 0.69/0.65, GPT-4V 0.25 zero-shot, 0.23 one-shot | Mitchell et al. 2023 [b10, a12] | single |
| 2023 LLMs on open abstract reasoning | GPT-4 open QA: ARC-text 0.119, BIG-Bench-F 0.514, Evals-S 0.304, PVR 0.177, Raven text 0.410, symbolic 0.330. Multiple choice Raven (chance 0.125): GPT-4 text 0.697, symbolic 0.535 | Gendron et al. 2023 [a13, b05, c07] | established |
| Fine-tuning does not transfer | LLaMA2 fine-tuned on symbolic RAVEN: 96.5% in distribution, large drops on compositional OOD splits | [a14, b07, c21] | established |
| Early emergent-analogy claim | Digit Matrices, humans N=40: generative GPT-3 vs humans OR 1.88 (p=0.005, CI 1.21-2.91); multiple choice OR 6.27 (p=2.3e-8). Letter strings, humans N=57: OR 1.76 (p=6.3e-5). Item difficulty correlation r(30)=0.39 | Webb et al. 2023 [a08, c01, c02] | contested |
| Difficulty rises with rule count | Progression vs none: humans OR 0.41, GPT-3 0.07. Unique rules: humans 0.61, GPT-3 0.25. Permuted vs aligned: humans 0.52, GPT-3 0.06 | [a21, b02] | single |
| Counterfactual letter strings | Humans 0.753 [0.734, 0.773] (1,876 samples); GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (6,840 each; row-to-model assignment not independently certain). Humans flat across 0, 2, 5, 10, 20 permuted letters; GPT falls at each step and again with symbols | Lewis and Mitchell 2024 [b03] | established (with Hodel-West) |
| Synthetic alphabet collapse | GPT-3 generative accuracy below 0.1 on extend-sequence, successor/predecessor, fix-alphabetic tasks. Only remove-redundant and sort stayed near Webb's level | Hodel and West 2023 [c03] | established |
| Code execution closes the gap | Human vs GPT-4 alone: significant gap. Human vs GPT-4 + code: P=0.496 (no gap) | Webb et al. 2024 [a10] | single (authors defending own paper) |
| Counterfactual tasks, general | GPT-4 0-shot base-10 addition 2-digit 98.2% vs base 9 38.6%, base 8 60.2%, base 11 56.5%, base 16 74.0%. 4-digit: base 10 83.4%, base 9 14.6%, base 8 24.0%. GPT-3.5 parseable programs 99% default to 62-75% on flips and rotations | Wu et al. 2023 [a15, c06] | established |
| Children and adults vs LLMs on far transfer | Humans transfer Latin to Greek to symbol alphabets; LLMs do not | Stevenson et al. 2025 [c05] | single (exact N not copied) |
| Object description helps GPT-4 on ARC | 13/50 raw grid to 23/50 with object form (simplest tasks). 1D-ARC gains +4% to +96% by family | Xu et al. 2024 [c09] | established with d07 (direction depends on model type) |
| Hypothesis then program | 100-problem ARC subset, GPT-4: direct 17%, programs 23%, summarised hypotheses 30%, human-picked hypotheses 33%, language only 19% | Wang et al. 2024 [c10] | single |
| Induction and transduction differ | Each alone about 40%; static transduction without test-time training under 11%; ensemble 56.75% on public eval (61.9% with Akyurek TTT). Average human 60.2%, best human 97.8% | Li et al. 2024; ARC Prize 2024 [c11, d05, b12] | established |
| Test-time training | 80 tasks, pass@2: 17.5% to 45.0% (+27.5). 8B model 53.0%. With program synthesis 61.9%. BBH 10-shot 50.5% to 57.8% | Akyurek et al. 2025 [b17, c12, c23] | established |
| ARC Prize 2024 | Private top 33% to 55.5% (MindsAI, ineligible); ARChitects 53.5% (private set winner). Same team 56.0% on ARC-AGI-1 semi-private in the ARC-AGI-2 paper (different set, not one number). o1-preview 18%, Claude 3.5 Sonnet 14%, GPT-4o 5% semi-private. 2020 best 20%, but 49% of private set solved by at least one team | [a18, b11, b12, a20] | established |
| ARC-AGI-1 vs ARC-AGI-2 (May 2025, semi-private) | o3-medium 53.0 vs 3.0. o3-mini-high 34.5 vs 3.0. o4-mini 41.8 vs 2.4. o1-pro low 23.3 vs 0.9. Claude 3.7 8K 21.2 vs 0.9. ARChitects 56.0 vs 2.5. Icecuber 17.0 vs 1.6 | Chollet et al. 2025 [a19, b14, c15] | established |
| o3 preview cost | 76% at about $200 per task, 88% at about $20,000 per task (ARC-AGI-1) | [a19, b16] | established |
| ARC Prize 2025 | 1,455 teams, 15,154 entries. NVARC 24.03% (about $0.20 per task), ARChitects 16.53% (site lists 15.42%), MindsAI 12.64% | [c17, d01] | established |
| Prompt-level refinement harness | Gemini 3 Pro 31% at $0.81 per task to 54% at $31 per task (about 38x cost). Opus 4.5 similar accuracy at about $60 (Poetiq-reported, verified by ARC Prize) | [c18, d01, d02] | single (vendor-reported) |
| Program search with feedback (SOAR) | One-shot ARC-test: Qwen-Coder 1.00-2.25%, GPT-4.1 8.00%, Claude-4-Sonnet 20.75%, o3-mini 38.25%. GPT-4.1 Sample-6k 19.75, Sample&Refine 26.25, SOAR-6k 45.50. Peak 52.00% with voting (oracle 57.25%) | Pourcel et al. 2026 [d06] | established with d05, d01 |
| Small purpose-built models | TRM 7M params: 45% ARC-AGI-1, about 8% ARC-AGI-2 (Gemini 2.5 Pro 4.9%). CompressARC 76K params: about 20% ARC-AGI-1, 4% ARC-AGI-2. VARC 18M: 54.5% ARC-1; 73M ensemble 60.4% ARC-1, 11.1% ARC-2 (table scrambled, rows inferred) | [c20, d08, d07, d02] | single (trained on ARC data) |
| Reasoning-model collapse on harder Raven | o3-mini medium 86.6% to 17.0% (chance 12.5%), 2.7x-3.4x reasoning tokens; R1 80.6% to 23.2% (22.8% in one condition); o3-mini high 92.6% on I-RAVEN. Neuro-symbolic 98.6% to 88.0% | Camposampiero et al. 2025 [c13, c22] | single |
| Longer reasoning lowers accuracy | Distractor counting: R1 70% to 30% at 5 distractors (natural length). Claude Opus 4 near 100% to 85-90%. Zebra puzzles 200 items, up to 8x8: R1 inverse scaling at every size. Text Raven 8 options: reasoning off helps (p=.021) | Gema et al. 2025; NeuroCognition 2026 [d03, d04, d12] | established |
| Human difficulty vs model difficulty anti-aligned | Fine-tuned models beat humans on hardest 20% of ARC tasks, trail them on easiest 20% | Li et al. 2024 [d05, d16] | single |
| Working-memory training | Jaeggi 2008: N=70, trained d=0.65 vs control d=0.25, F(1,67)=5.27. Meta-analysis (87 pubs, 145 comparisons): nonverbal ability g=0.05 [-0.02, 0.13] k=67 vs treated controls; g=0.20 [0.11, 0.28] k=53 vs untreated | [a05, b21, b22] | established (not replicated) |
| Eye movements on matrix test | N=34, 18 items, mean accuracy 58.5% (SD 17.3). Toggling rate vs score r=-0.68 (45% variance). Latency to first toggle r=0.55. Reliability 0.70 | Laurence et al. 2018 [a06] | single |
| LLM general factor | 591 LLMs, 12 benchmarks. Mean inter-test r 0.73. g loading 0.81, g explains 65.6%. Parameters vs g score r=0.54 [0.48, 0.59] | Ilic and Gignac 2024 [b19] | single |
| NeuroCognition | One factor 75% of variance across 156 models, loadings above 0.76. Benchmark vs 11-benchmark average r=.86 (N=10 models) | Haznitrama et al. 2026 [d04] | single |
| Flynn effect | 2.31 points per decade [1.99, 2.64], 285 studies, N=14,031. Modern Stanford-Binet and Wechsler 2.93 [2.3, 3.5] | Trahan et al. 2014 [b23] | established |
| Multimodal puzzles | MARVEL: 770 puzzles, humans 68.86% (SD 9.74), nine models near random, gap about 40 points, panel counting below 45% | Jiang et al. 2024 [b18] | single |

---

## 4. Mechanisms and models

Each item below is written so that an engineer could build it. None of it is a claim that humans work this way.

### 4.1 Constructive matching versus response elimination (human strategy)

- Two strategies on matrix items. Constructive matching: study the matrix, build the missing cell in mind, then look at the options. Response elimination: look back and forth between matrix and options and discard options that fail.
- Measure: toggling rate = number of gaze switches between matrix and options. People with lower toggling score higher (r=-0.68, N=34) [a06].
- Engineer's version. Make the model write the predicted answer BEFORE it sees the options. Then match options against that prediction in code. Fall back to elimination only if no option matches.
- Caveat. Small student sample. No working-memory measure. An older model (Vigneau 2006) did not replicate for the full test (R2=0.09) [a06]. For LLMs the effect on text Raven with eight options is mixed (section 6).

### 4.2 Two-ability account of matrix solving (Carpenter-Just-Shell)

- Ability 1: induce abstract relations from the rows. Ability 2: manage a growing goal stack in working memory [a07, abstract only].
- Engineer's version. Treat rule count as a difficulty counter. Webb finds accuracy falls as unique rules rise, for humans and GPT-3 [a21, b02, c02]. Count rules in code, then spend more samples as the count rises (G12).
- For LLMs the limit is not a fixed item count. Failures are in using supplied state and in run-to-run consistency [d10, d11]. So the fix is writing state down (notes, a running table), not capping items.

### 4.3 Induction by program, with execution as the check

- Loop (Wang 2024, SOAR, Li 2024) [c10, d06, c11]:
  1. Model writes several hypotheses in words.
  2. Model writes a program for each.
  3. Code runs each program on every demonstration pair.
  4. Keep programs that reproduce all pairs. Apply survivors to the test input.
  5. If none survive, show the failing output to the model and refine. Repeat.
- Measured: GPT-4 17% direct to 23% programs to 30% with summarised hypotheses [c10]. SOAR sample-and-refine lifts open models far above one-shot [d06].
- Known hole. The demonstration pairs are both fitting data and verifier. A program can fit all of them and still be wrong. This is the schema's G3 risk. Our own data: two ARC programs fit every example and were wrong (SCHEMA G3).

### 4.4 Induction plus transduction as two routes

- Induction = write a program. Transduction = predict the output grid directly. They solve different tasks. Induction is better at precise computation and composing concepts. Transduction is better at fuzzy perceptual concepts [d05].
- Ensemble rule (Li 2024): try induction first. If no candidate program fits, use the transduction answer [c11].
- Each route about 40% alone; ensemble 56.75% [c11, b12]. These systems are fine-tuned, so the gain from the ensemble rule alone in a prompt-only setting is untested.

### 4.5 Representation rewrite

- Flattened text splits objects across the token stream. An external tool that extracts objects (colour, position, size) and lists them nearly doubled GPT-4 on simple ARC tasks (13/50 to 23/50) [c09].
- Counter-evidence. A plain vision transformer on a pixel canvas wins for vision models (VARC 54.5% on ARC-1) [d07]. For text Raven, text beat the symbolic form for GPT-4 (0.410 vs 0.330) [b08]. For causal induction (ACRE), the symbolic form was better. No single rewrite is robust across model types and tasks [critique, claim K03].
- Engineer's version. Treat the representation as a swappable step. Generate two or three renderings in code (raw grid, object list, diff of input and output). Test each. Pick per task class from S9 records.

### 4.6 Test-time training (outside scope)

- Short weight update on the task's own examples, with augmented views (rotations, colour permutations) and hierarchical voting over views [b17, c23].
- Needs weights. A prompt-only agent cannot do it. Proxy: use augmented views of the task in context and vote in code. That proxy is not tested here.

### 4.7 Perturbation consistency as a memorisation probe

- Make perturbed copies of an item (changed alphabet, base, orientation, role flip). Score the original and the copies. Items solved only in the original form are flagged as likely recall [a15, c03, b03, d09].
- Knights and Knaves study: memorisation score above 50% on 8-person training puzzles under perturbation; near-zero accuracy on role-flipped puzzles; about 80% for Llama3-8B under role flip [d09]. That is fine-tuned models on synthetic puzzles, not ARC.

### 4.8 Reasoning-length control

- Longer model-chosen reasoning lowers accuracy on distractor and constraint tasks, and a forced cap beats the model's own length choice [d03, d12].
- Engineer's version. Fix a token cap per mode. Run several short independent attempts instead of one long one. Vote in code. Compare to a single long attempt at equal tokens.

### 4.9 Resource-efficiency view (Chollet)

- Score = accuracy per unit of compute and priors, not accuracy alone [a16]. In practice report accuracy per token or per dollar. Poetiq: 31% at $0.81 to 54% at $31 [c18]. NVARC: 24.03% at about $0.20 per task [c17]. A cost-blind score hides a 38x difference.

---

## 5. What holds up

### 5.1 Replicated or well supported

- Humans do well on novel grid puzzles. Four large samples agree: H-ARC (N=1,729), ARC-AGI-2 testing (407), ConceptARC (415 kept after exclusions), NYU MTurk (10 per task) [a17, b15, b09, b13]. Human numbers depend on filtering (crowd workers, attention checks).
  - Correction to b09. The ConceptARC paper excluded 55 of 482 participants for inadequate explanations and 12 more for failing minimal tasks: 67 excluded, 415 kept [critique.md].
- Unaided 2023 LLMs are far below humans on novel abstract tasks (GPT-4 about 25% on ConceptARC against 91% humans; ARC open QA 0.119) [a11, a13, b09].
- Counterfactual variants hurt LLMs and not humans: changed alphabets, bases, orientations [b03, c03, a15, c06, c05].
- Search plus execution plus refinement beats one-shot on ARC, in several labs [c10, d06, c11, c18].
- Induction and transduction are complementary [c11, b12, d05].
- Longer reasoning can lower accuracy [d03, d04, c13].
- Working-memory training does not reliably raise Gf [b21].

### 5.2 Failed replications and disputes

- Webb et al. 2023 versus Lewis and Mitchell 2024, Hodel and West 2023. On the unaltered problems the GPT models did not beat humans as Webb reported, and item-type results differed (Predecessor and Fix Alphabet for GPT-3; Remove Redundant, Fix Alphabet, Sort for GPT-3.5; Remove Redundant and Sort for GPT-4) [b04]. Lewis and Mitchell's human group scored higher than Webb's (Prolific versus students) [b03, c04]. Prompt wording moved scores [b04].
- Webb 2024 reply: GPT-4 with code execution matches humans on permuted alphabets (P=0.496). 46% of GPT-4 errors used a valid alternative rule, against 39% of human errors in Lewis and Mitchell [a10]. Alternate-rule errors in Lewis and Mitchell: GPT-3 5.81%, GPT-4 22%, GPT-3.5 38.59%, humans about 15% [c04]. Net: contested (K05). A fix that needs code is not the same skill humans use.
- Jaeggi 2008 (N=70; trained d=0.65 vs control d=0.25) was not replicated by Chooi and Thompson 2012 or Redick et al. 2012 (N not given) [a04, a05]. Controls gained d=0.25, so retest alone is large. Meta-analysis: g=0.05 against treated controls, g=0.20 against untreated, p-curve showed no evidential value for treated-control studies [b21]. Reading comprehension fell from g=0.15 to 0.08 when studies where controls declined were removed [b22].
- ARC-AGI-1 looked nearly solved (o3 preview 76% to 88%) while the same families score about 3% on ARC-AGI-2 [a19, c15]. Reasons offered: partial search or learnability of ARC-AGI-1 at high cost; public-vs-semi-private gap up to 15 points (Akyurek: 47.5% semi-private against 62.8% public) [b11]; the owners suspect knowledge-dependent overfitting but give no size [d01].
- Early GPT-3 emergent-analogy claim was not robust to alphabet changes [c03, b03]. GPT-3.5 and GPT-4 were no better than GPT-3 on the original task in the replication [c04].

### 5.3 Moderators and boundary conditions

- Input format. Text beats symbolic for Raven; symbolic beats text for ACRE backward blocking; objects beat raw grid for GPT-4 on ARC; pixels beat text for trained vision models [b08, c09, d07]. Human image norm (0.814) cannot be applied to text matrices (humans 0.430 in a text pilot, N=9) [d04].
- Answer format. Multiple choice versus free answer swings models in opposite directions (GPT-5 text 0.540 MC to 0.605 Gen; Claude 0.560 to 0.385) [d04].
- Task set. Kaggle first place scored 21% on the original ARC hidden set and 52% on ConceptARC [b25]. Difficulty depends on design.
- Compute. o3 preview 76% at $200 per task, 88% at $20,000; o3-medium 53% [a19, b16]. The released model did not match the preview configuration.
- Scores below 5% on ARC-AGI-2 are near noise [b14].
- Digit count. Counterfactual addition drop grows with digits (98.2% to 83.4% on base 10; 38.6% to 14.6% on base 9) [a15].
- Human versus model difficulty. Anti-aligned at both ends on ARC (models beat humans on the hardest 20%, trail on the easiest 20%) [d05, d16]. Fine-tuned code-trained transformers only.

### 5.4 What worked and what did not (interventions)

Worked:
- Execution check against examples with refinement (SOAR, Hypothesis Search, harness) [d06, c10, c18].
- Object representation for GPT-4 [c09].
- Program-first with direct-answer fallback (fine-tuned) [c11].
- Test-time training (needs weights) [b17].
- Code execution for GPT-4 on letter strings [a10].
- A forced token cap over model-chosen length [d12].

Did not work or was small:
- Chain of thought, code refinement and many-shot examples gave little for abstract tasks in 2023 models, except GPT-4 and text-davinci-003 [b06, c07]. 16 examples reached about 0.6 on BIG-Bench-F; PVR stayed near 0.26.
- Richer one-shot prompt: GPT-4 0.19-0.25 to 0.33 on ConceptARC [b10].
- GPT-4V (image input) was worse than text-only GPT-4 on the minimal tasks [b10].
- Fine-tuning on one Raven-style set: near-perfect in distribution, drop out of distribution [b07].
- Working-memory training in humans [b21].
- Extra reasoning tokens on harder Raven variants: o3-mini used 2.7-3.4x more and still fell to 17.0% [c13, c22].

### 5.5 Gaps in the evidence base

- Several results rest on a single paper: hypothesis search, reasoning-model Raven collapse, eye movements, g in LLMs [critique.md].
- Human samples are crowd workers with exclusion rules.
- Most papers compare methods at unequal token cost.
- Primary 1943 and 1967 papers, Carpenter-Just-Shell, Kyllonen and Christal, Chuderski and Necka, Ritchie and Tucker-Drob not opened or only abstract [critique.md].

---

## 6. Language models

### 6.1 Trajectory by period

| Period | What happened | Numbers | Source |
|---|---|---|---|
| 2022-23, base models | Claim of emergent analogy on text matrices and letter strings | GPT-3 beat 40 students on Digit Matrices (OR 1.88); letter strings OR 1.76 | [a08] |
| 2023, same models, harder variants | Counterfactual tests break it | GPT-3 under 0.1 on synthetic alphabet tasks; GPT-4 0.452 vs humans 0.753 overall | [c03, b03] |
| 2023, GPT-4 on ARC-style | Far below humans | ConceptARC 25% overall (91% human); ARC-text 0.119; one-shot 0.33 | [a11, a13, b10] |
| 2023, multimodal | Images did not help | GPT-4V 0.25/0.23 on minimal tasks; MARVEL: models near random, human 68.86% | [b10, b18] |
| 2024, special-purpose search and training | Big jump on ARC-AGI-1 | Private 33% to 55.5%; ARChitects 53.5% | [a18, b11] |
| 2024-25, reasoning models | ARC-AGI-1 strong, ARC-AGI-2 near floor | o3-medium 53.0 vs 3.0; o3 preview 76-88% at $200-$20,000 | [a19, b16] |
| 2025, harder Raven | Reasoning models collapse | o3-mini 86.6% to 17.0%; R1 80.6% to 23.2% | [c13] |
| 2025, Kaggle ARC-AGI-2 | Refinement loops | NVARC 24.03% at about $0.20 | [c17] |
| 2025-26, harness on frontier | Prompt-only scaffold | Gemini 3 Pro 31% ($0.81) to 54% ($31) | [c18, d01] |
| 2026, program search with self-improvement | One-shot low, search high | GPT-4.1 8.00% one-shot, 19.75% sample, 26.25% refine, 45.50% SOAR | [d06] |

### 6.2 What changed performance, and by how much

- Execution plus a check on the examples: the largest prompt-level lever. GPT-4: 17% to 23% (programs) to 30% (summarised hypotheses) [c10]. Open models in SOAR: from 1-2% one-shot to 14-26% with search [d06]. Gemini 3 Pro: +23 points at 38x cost [c18].
- Representation: GPT-4 13/50 to 23/50 with objects [c09].
- Weights: test-time training +27.5 points on 80 tasks [b17].
- Reasoning mode: reasoning models help on ARC-AGI-1 (o3-medium 53.0) but not on harder variants [a19, c13].
- Scale: weak and diminishing. Parameters vs g-like score r=0.54 with diminishing returns [b19]. A 7M-parameter trained model reaches 45% on ARC-AGI-1 [d08].

### 6.3 Where reasoning hurts

- Zebra puzzles: R1 inverse scaling across grid sizes; Opus 4 non-monotonic [d03].
- Distractor counting: R1 70% to 30%; Opus 4 100% to 85-90% [d03].
- Text Raven, 8 options: reasoning off helps (p=.021). Text Gen p=.83 and Image MC p=.173 are not significant. Reasoning was disabled for Claude Sonnet 4 and Grok 4 Fast on RAPM because of overthinking [d04].
- I-RAVEN-X: more tokens, lower accuracy [c13, c22].
- Token spread on one ARC-AGI-1 task (4cd1b7b2): Gemini 3 Pro 96 reasoning tokens, Deep Think 138,000 [d02].
- No curve indexed by novelty level exists. This is gap 2 in critique.md.

### 6.4 General-factor findings about LLMs

- 591 LLMs: one factor explains 65.6% of variance; mean g loading 0.81 [b19]. But the Gf proxies were knowledge-heavy (Hellaswag, GSM8K-style). The authors say this may be achievement, not intelligence.
- NeuroCognition: 156 models, one factor 75% [d04]. Single source.

### 6.5 Working-memory-like behaviour

- LLM failures are in using state: answer drift as questions accumulate, probability mass over the state space not summing to one, ignoring supplied history [d10, d11].
- Spatial working memory with history in context: Gemini 3 Pro 1.00 easy, 0.79 hard; Gemini 2.5 Pro 0.41 easy over 3 runs; humans 0.963 and 0.878 (N=11). Model effect size eta-squared .88 vs human participant .47 [d11].
- The reading of n-back drops as human-like limits is disputed (Hu and Lewis, snippet only) [d13]. A backward-digit-span paper that links to text Raven and ARC-AGI-1 is a lead, unopened [d14].

### 6.6 Contamination

- ARC Prize authors say models trained on public data overfit both ARC-AGI-1 and -2, but give no size. The one anecdote: Gemini 3 Deep Think used correct ARC colour mappings (Green=3, Magenta=6) when the prompt gave only integer arrays [d01].
- Public-vs-semi-private gaps up to 15 points [b11]. No fresh-task counterfactual measurement on ARC exists [critique.md].
- Raven items: GPT-4 gains most on Raven-type items, which the authors suspect reflects training exposure [b05].

### 6.7 Small models

- TRM (7M) 45% and CompressARC (76K) about 20% on ARC-AGI-1 show that novelty skill on ARC is not tied to scale. They are trained on ARC-style data, so this is not zero-shot Gf [c20, d08].

---

## 7. What our agent should take

Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| N1 | Cap reasoning length and prefer several short independent attempts over one long one; a model-chosen length is worse than a forced cap. Already in G11; this adds Gf-type evidence (constraint puzzles, distractors, 8-option text matrices). | G11 (confirm, widen) | [E] | d03, d04, d12, c13; K18 |
| N2 | Induction first with an execution check against the demonstration pairs, then refine from the actual failing output. Matches S4, S5 and G2. | S4/S5, G2 | [E] | d06, c10, d05, c18; K21 |
| N3 | Keep two routes: program (induction) and direct answer (transduction). Try program first; fall back to direct if no program fits. Maps onto the checked mode with a no-check fallback. | S3/S7, O3 | [E] for complementarity; [S] for the exact fallback rule | c11, b12, d05; K07 |
| N4 | Treat representation as a swappable step at S2/O6. Test raw grid, object list and diff; do not fix one rewrite. | S2, O6 | [E] that it matters; no single best | c09, d07, b08; K03 |
| N5 | Report accuracy per token on every Gf-type run; a cost-blind result hides up to a 38x difference. | G7, G12 | [E] | c18, c17, a19; K10 |
| N6 | Perturbed copies of test items (changed symbols, base, orientation) flag likely recall. A big drop on a perturbed copy means the item was solved by retrieval, not by induction. | S0 (flag), G (memorisation check) | [E] that counterfactual drops are real; the flag rule is untested | a15, c03, b03, c06; K04 |
| N7 | Never quote a human norm from a different format; run a matched baseline arm in the same format. | G7 (measurement) | [S] | d04; K23 |
| N8 | Do not rely on training-style "improvements" for a frozen model: working-memory training, fine-tuning on one set, extra "be careful" prompting. Consistent with section 4b of SCHEMA. | 4b | [E] | b21, a14, b06; K11 |

Notes. N1 and N2 repeat existing schema rules; the Gf evidence is an additional independent source, not a change. N3 and N4 do not need a new state. N6 and N7 are listed under "Add now" as measurement practice, not as new schema elements; the gate use of N6 is in Test first (T3).

### Test first

| # | Candidate | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Hypothesis-in-words then program, versus direct, at equal tokens | O (hypothesis then check), S2 | [S] | c10; K08 |
| T2 | Novelty gate built from pilot model attempts (agreement, disagreement across 2-3 cheap tries) instead of a human-style novelty rating. Human-rated difficulty is anti-aligned with model difficulty at both ends. | S0 | [S] | d05, d16; K19 |
| T3 | Perturbation-consistency check in S0 to separate recall from induction | S0, G | [C] | d01, d09; K20 |
| T4 | Hard cap on reasoning with restart, indexed by novelty level | G11, S0 | [S] for the novelty interaction | c13, d03; K09 |
| T5 | Write every held item to notes; run each item twice and flag disagreement | S1/S2 | [S] | d10, d11; K22 |
| T6 | Rule count as a difficulty tag that sets the sample budget | S0, G12 | [S] | a21, b02; K17 |
| T7 | Predict-before-options (constructive matching) on multiple-choice items | S2/S3 | [S] human only; mixed for LLMs | a06, d04; K12 |
| T8 | Prompt-only refinement harness at fixed cost per task | O (refine loop), G12 | [S] vendor-reported | c18, d01; K10 |
| T9 | Counterexample-seeking discriminating test between two fitting rules (guards the G3 hole in induction) | S7 | [S] here, [E] in schema (F08) | c10 limits, SCHEMA S7 |

Rule. Nothing in the Test first table goes into SCHEMA.md until its test passes (see UNKNOWNS.md).

---

## 8. Concrete tests on our bench

Common rule. Both arms get equal total tokens, setup cost counted (G7). Report accuracy per 1k tokens and the number of items where the arms disagree. Use at least 3 runs per item for a stable estimate, because LLM run-to-run consistency is poor [d10].

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 program vs direct | ARC-style grid items (H-ARC or ConceptARC slice; plus fresh generated items) | (a) plain direct chain of thought; (b) hypotheses then program then execution check then refine; same token total | Exact-match accuracy; accuracy per 1k tokens | Arm b wins by several points on rule-heavy items; ties or loses on easy items. Prior: +6 (17 to 23) up to +13 points (to 30) [c10] |
| B2 two routes | Same set | (a) program only; (b) direct only; (c) program first, direct fallback | Accuracy; share solved by only one route | Routes solve different items; (c) beats both. Prior: complementarity [d05] |
| B3 representation | ARC-style items; text Raven-style items | Raw grid vs object list vs diff vs symbolic, same prompt | Accuracy per format; which formats win per class | Object form gains on spatial simple items (13/50 to 23/50 prior [c09]); no format wins everywhere |
| B4 perturbation | Original and perturbed (alphabet, base, orientation, colour map) copies of 100 items | Plain; scaffold | Accuracy original; accuracy perturbed; share solved only in original | Large drop on items the model solved by recall; a scaffold should shrink the drop. Prior: humans flat, GPT 0.452 vs 0.753 [b03] |
| B5 reasoning length by novelty | Items tagged familiar vs novel (by perturbation drop) | Capped at 1k, 4k, 16k tokens vs model-chosen length; equal total via more short attempts at low cap | Accuracy curve by tokens and novelty | Accuracy flat or falling with length on novel and distractor items; short-attempts vote wins at equal tokens [d03, c13] |
| B6 pilot-attempt gate | 200 mixed items | (a) gate from 2-3 cheap pilot attempts (agreement, check failure); (b) gate from a model novelty rating; (c) no gate | Accuracy at fixed total tokens; correlation of gate score with outcome | (a) beats (b) and (c). Prior: human difficulty is anti-aligned with model difficulty [d16] |
| B7 state notes | Multi-step items needing 4+ held values | Free thought vs forced notes of every held value; run twice | Accuracy; disagreement rate across two runs | Notes lift accuracy and cut disagreement [d10, d11] |
| B8 rule count budget | Matrix-style items tagged by number of unique rules | Uniform samples vs samples scaled by rule count | Accuracy at equal total tokens | Scaled arm wins on multi-rule items [a21] |
| B9 constructive matching | Text Raven with 8 options | Answer shown with options vs prediction written first then matched in code | Accuracy | Small gain or none; 8-option text matrices improved when reasoning was off (p=.021) [d04] |
| B10 refine harness | ARC-style items | Single pass vs refine loop (check, show failing output, revise, up to N rounds) at 1x and 10x tokens | Accuracy per token | Gain with rising cost; find the knee. Prior: 31% to 54% at 38x [c18] |
| B11 counterexample | Items where two programs fit all examples | Pick by vote vs run a discriminating input | Accuracy of the final pick | Discriminating test wins (SCHEMA S7 prior) |

Analysis notes. Split every result by item novelty (perturbation drop) and by rule count. Report the Wilson interval. Treat ARC-AGI-2 style scores below 5% as noise [b14].

---

## 9. What does not transfer, and why

- Working-memory training and Gf gains. A human learning claim with a null result in humans anyway [b21]. A frozen model has nothing to train.
- Age curves (Horn and Cattell, peak near 27). Biological. Not read in the original.
- Flynn effect and schooling gains (2.31 points per decade; 1-5 points per year of school). Human population effects [b23, b24].
- Test-time training. Needs weight updates. A scaffold-only agent cannot do it; only an in-context proxy is possible [b17].
- Fine-tuning on ARC-like synthetic data and tiny trained networks (TRM, CompressARC, VARC). They are trained on ARC-style data, so they show nothing about prompt-only Gf. Their value is as a reminder that ARC is partly solvable by narrow methods [c20, d08].
- Human strategy measures from eye movements (toggling rate). Not available for LLMs; only the idea (predict before looking at options) can be carried over, and it is untested [a06].
- Human norms of reliability and g loading for Raven. They do not carry to LLM scoring (format swings; contamination; tiny human text pilots) [d04].
- Human-style n-back and digit-span readings of LLM working memory. LLM failures look like state-use failures [d10, d11, d13].
- Vendor harness results. The ARC verifier is the training pairs. The harness is domain specific. Cost is unmatched across arms [d02].
- Human difficulty ratings as a novelty gate. Anti-aligned with model difficulty at both ends [d05, d16].
- The general factor in LLMs (g loading 0.81, 65.6%). The Gf proxies were knowledge-heavy. It is no basis for a schema element [b19].

---

## 10. Open questions

1. Does a novelty sort at S0 predict where scaffolding helps? No paper measures it at equal tokens (gap 1).
2. Does longer reasoning help or hurt on novel items, as a curve by novelty level at matched tokens? (gap 2)
3. How much of an LLM's ARC score is memorisation of public ARC-AGI-1 tasks? No fresh-task or counterfactual measurement exists (gap 3).
4. Which representation step is robust across models? Closed negatively so far: none is (gap 4).
5. Does hypothesis-then-program verification replicate for current reasoning models without fine-tuning? Fine-tuned systems replicate it; the original 100-problem GPT-4 setup has no independent replication (gap 5).
6. What do prompt-only scaffolds score on ARC-AGI-2 at fixed cost per task? One vendor data point only (gap 6).
7. What do Cattell 1943 and Horn and Cattell 1967 report? Sample sizes, Gf loadings, and the age curve are not read (gap 7).
8. Do LLM Gf scores track working-memory-like limits? Evidence suggests state use, not item counts, but the n-back reading is disputed and the backward-digit-span lead is unopened (gap 8).
9. Do human Raven reliability and g-loading figures transfer once contamination and format are controlled? (gap 9)
10. Why does the counterfactual gap vary by paper (Webb vs Lewis and Mitchell vs Hodel and West)? Prompt wording, human pool and tool access are all confounded.
11. Does the anti-aligned human/model difficulty result hold for prompt-only frontier models, or only for fine-tuned code-trained transformers?
12. Can an in-context proxy for test-time training (augmented task views plus code voting) recover any of the +27.5 points?

---

## 11. Sources

[V] = opened and read this session (full paper or page text; some PDF tables scrambled). [M] = snippet or citation only.

1. [M] Cattell (1943) The measurement of adult intelligence, Psychological Bulletin 40(3):153-193. https://en.wikipedia.org/wiki/Fluid_and_crystallized_intelligence
2. [V] Wikipedia, Fluid and crystallized intelligence (citing Horn and Cattell 1967): https://en.wikipedia.org/wiki/Fluid_and_crystallized_intelligence
3. [V] Wikipedia, Cattell-Horn-Carroll theory: https://en.wikipedia.org/wiki/Cattell%E2%80%93Horn%E2%80%93Carroll_theory
4. [M] Horn and Cattell (1967) Age differences in fluid and crystallized intelligence, Acta Psychologica 26:107-129 (Crossref metadata only): https://doi.org/10.1016/0001-6918(67)90011-X
5. [V] Jaeggi, Buschkuehl, Jonides, Perrig (2008) Improving fluid intelligence with training on working memory, PNAS: https://pmc.ncbi.nlm.nih.gov/articles/PMC2383929/
6. [V] Laurence et al. (2018) Eye movements and cognitive strategy in a fluid intelligence test, Front. Psychol. 9:380: https://www.frontiersin.org/articles/10.3389/fpsyg.2018.00380/full
7. [M] Carpenter, Just, Shell (1990) What one intelligence test measures, Psych. Review 97(3):404-431 (abstract only; full text 403): https://apps.dtic.mil/sti/pdfs/ADA221448.pdf
8. [M] Kyllonen and Christal (1990) Reasoning ability is (little more than) working memory capacity?!, Intelligence 14 (no URL; not read)
9. [M] Chuderski and Necka (2012) Contribution of working memory to fluid reasoning: https://researchgate.net/profile/Adam-Chuderski/publication/225051454
10. [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models: https://arxiv.org/abs/2212.09196
11. [V] Webb, Holyoak, Lu (2024) Evidence from counterfactual tasks supports emergent analogical reasoning: https://arxiv.org/abs/2404.13070
12. [V] Hodel and West (2023) Response: Emergent analogical reasoning in large language models: https://arxiv.org/abs/2308.16118
13. [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning in LLMs: https://arxiv.org/abs/2402.08955
14. [V] Stevenson, Pafford, van der Maas, Mitchell (2025) Can LLMs generalize analogy solving like children can?: https://arxiv.org/abs/2411.02348
15. [V] Wu et al. (2023) Reasoning or reciting? Counterfactual tasks: https://arxiv.org/abs/2307.02477
16. [V] Moskvichev, Odouard, Mitchell (2023) The ConceptARC benchmark: https://arxiv.org/abs/2305.07141
17. [V] Mitchell, Palmarini, Moskvichev (2023) Comparing humans, GPT-4, and GPT-4V on abstraction and reasoning tasks: https://arxiv.org/abs/2311.09247
18. [V] Gendron, Bao, Witbrock, Dobbie (2023) Large language models are not strong abstract reasoners: https://arxiv.org/abs/2305.19555
19. [V] Chollet (2019) On the measure of intelligence: https://arxiv.org/abs/1911.01547 (opened per a16 and b20; c25 lists it as not opened, so treat as opened only for the definition and ARC format)
20. [V] LeGris, Vong, Lake, Gureckis (2024) H-ARC: https://arxiv.org/abs/2409.01374
21. [V] Chollet et al. (2025) ARC Prize 2024 technical report: https://arxiv.org/abs/2412.04604
22. [V] Chollet et al. (2025/2026) ARC-AGI-2: a new challenge for frontier AI reasoning systems: https://arxiv.org/abs/2505.11831
23. [V] Chollet et al. (2026) ARC Prize 2025 technical report: https://arxiv.org/abs/2601.10904
24. [V] Kambhampati (2024) Can large language models reason and plan?: https://arxiv.org/abs/2403.04121
25. [V] Xu et al. (2024) LLMs and the Abstraction and Reasoning Corpus: https://arxiv.org/abs/2305.18354
26. [V] Wang et al. (2024) Hypothesis Search: https://arxiv.org/abs/2309.05660
27. [V] Li et al. (2024) Combining induction and transduction for abstract reasoning: https://arxiv.org/abs/2411.02272
28. [V] Akyurek et al. (2025) The surprising effectiveness of test-time training for few-shot learning: https://arxiv.org/abs/2411.07279
29. [V] Camposampiero et al. (2025) Can large reasoning models do analogical reasoning under perceptual uncertainty?: https://arxiv.org/abs/2503.11207
30. [V] Pourcel, Colas, Oudeyer (2026) SOAR: https://arxiv.org/abs/2507.14172
31. [V] Hu et al. (2025) ARC is a vision problem! (VARC): https://arxiv.org/abs/2511.14761
32. [V] Jolicoeur-Martineau (2025) Less is more: recursive reasoning with tiny networks: https://arxiv.org/abs/2510.04871
33. [V] Xie et al. (2025) On memorization of LLMs in logical reasoning: https://arxiv.org/abs/2410.23123
34. [V] Gema et al. (2025) Inverse scaling in test-time compute: https://arxiv.org/abs/2507.14417
35. [V] Haznitrama, Ardi, Oh (2026) NeuroCognition: https://arxiv.org/abs/2603.02540
36. [V] Huang, Sun, Wang, Dredze (2026) On the failure of latent state persistence in LLMs: https://arxiv.org/abs/2505.10571 (abstract, setup and part of results)
37. [M] Hu and Lewis (2025) n-back critique: https://aclanthology.org/people/xiaoyang-hu
38. [M] Backward digit span benchmark with text Raven and ARC-AGI-1 correlation: https://escholarship.org/uc/item/28m3k4g4
39. [V] Jiang et al. (2024) MARVEL: https://arxiv.org/abs/2404.13591
40. [V] Ilic and Gignac (2024) Evidence of interrelated cognitive-like capabilities in LLMs: https://doi.org/10.1016/j.intell.2024.101858
41. [V] Melby-Lervag, Redick, Hulme (2016) Working memory training does not improve performance on measures of intelligence: https://doi.org/10.1177/1745691616635612 (numbers not re-opened in the cross-check pass)
42. [V] Trahan et al. (2014) The Flynn effect: a meta-analysis: https://doi.org/10.1037/a0037173
43. [M] Ritchie and Tucker-Drob (2018) How much does education improve intelligence?: https://doi.org/10.1177/0956797618774253 (abstract only)

Cross-check status (critique.md, 2026-11-03): ARC-AGI-2 human numbers and table, H-ARC, Camposampiero, Akyurek, ConceptARC per-concept and Lewis-Mitchell totals were re-opened and confirmed. The GPT-3 0.488 / GPT-3.5 0.350 / GPT-4 0.452 row assignment is not independently certain because the PDF text scrambles row labels.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 10 established claims: 5 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A13.02-K03** (reworded: the sources support less). The final sentence (best representation depends on model type, pixel canvas for vision models, so no single rewrite step is robust) is not shown by VARC (one vision model trained from scratch, no cross-representation comparison). Corrected claim: Part of the gap is representation: an object-based representation raises GPT-4 on the simplest ARC tasks from 13/50 to 23/50, and giving GPT-4 code execution removes the significant gap to humans on letter-string tasks (P=0.496). A vision-only model (VARC) using a pixel canvas reaches 54.5-60.4% on ARC-1, suggesting representation matters, but no source compares representations across model types.
- **A13.02-K04** (reworded: the sources support less). Human accuracy staying flat was tested only for the permuted-alphabet letter-string tasks (Lewis and Mitchell); Wu et al. (base, orientation) tested no humans, and indeed discuss that humans may also do worse under unfamiliar conditions. Corrected claim: Counterfactual variants of letter-string analogies (permuted alphabets) lower LLM accuracy while human accuracy stays roughly flat (Lewis and Mitchell), and counterfactual tasks with changed base or code orientation also reduce LLM performance (Wu et al., no human comparison); early claims of emergent analogical reasoning in GPT-3 were not robust to these variants.
- **A13.02-K06** (now single-source: the sources are not independent). Numbers are correct, but three of the four evidence lines are the same Akyurek et al. paper and the fourth (Li et al.) only repeats the 61.9% figure from it, so there is a single independent source.
- **A13.02-K07** (reworded: the sources support less). The ~40% single-method figures are private/Kaggle leaderboard scores (Chollet et al.) while 56.75% is Li et al.'s ensemble on the public validation set, so they are not one like-for-like comparison; Li's own validation singles are about 35% (induction) and 43-57% (transduction). Corrected claim: Induction (program writing) and transduction (direct answer) solve substantially different ARC tasks; the best single induction-only and transduction-only Kaggle submissions each score around 40% on the private set, and Li et al.'s ensemble of both reaches 56.75% on the public validation set (2 tries), so combining them beats either alone.
- **A13.02-K10** (now single-source: the sources are not independent). Numbers check out (o3-medium 53.0 vs 3.0; NVARC 24.03%; Gemini 3 Pro harness 31% to 54% at $0.81 to $31), but both papers are by the same ARC Prize authors, so there is one independent source; also 'near saturated' is the authors' framing, not a measured result.
- **A13.02-K14** (now single-source: only one opened source, code check).
