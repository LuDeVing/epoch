# Compression at inference time: deep document

*Subfield C11.09. Written 2026-11-10 from evidence_a-d.jsonl (ids a01-a27, b01-b25, c01-c29, d01-d17), claims.jsonl (K01-K25) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Linked subfields researched in parallel (not covered here): MDL and Bayes; Search over thoughts; Language Agent Tree Search; Scientific discovery systems; Aggregation and extremizing; Analogical prompting. Earlier series documents on test-time search and selection overlap with section 6; see 00_FIELDS.md.*

## 1. What it is

"Compression at inference time" means this: the system learns a short description of one task while it is solving that task, and the answer falls out of the short description. There is no pretraining, no dataset and no search over a program library. The learning signal is code length.

The one flagship system is CompressARC (Liao and Gu, 2025; a01). The facts:
- It is a tiny network (76K parameters) started from random weights, for each ARC-AGI-1 puzzle separately.
- It trains for 2000 Adam steps on that puzzle only (about 20 minutes on one RTX 4070).
- The loss is a code length: cross-entropy on the grids that are known (the demonstration pairs plus the test input) plus a KL term on a latent tensor z. The output grid we want is left unconstrained. The decoder fills it in.
- Result: 20% of the 400 public eval puzzles and 34.75% of the 400 training puzzles at pass@2 (two guesses). One paper, one team, no independent replication found (K01, K02).

The founding claim is that "lossless compression during inference time is sufficient to produce intelligent behavior" (a01, quote). Plainly: the shortest program that prints all the puzzle's grids should also print the missing one correctly.

Three related families are kept apart in this document.
1. Compression-driven solver (CompressARC). The objective is code length. Weights are learned per puzzle from scratch.
2. Test-time training (TTT) of a pretrained model on the demonstrations (Akyurek et al., 2025; a12). It is not compression-driven. It starts from pretrained weights. It is the dominant 2024-25 ARC method (K10).
3. Selection by code-length-like scores. A trained model scores candidate answers by likelihood over many augmented views (Product of Experts, Franzen et al.; b15). This is compression used as a selection rule.

For our agent the point is that we do not train weights. Our agent is a scaffold around a closed-API language model. Most of this subfield therefore does not transfer directly (section 9). What can transfer is the selection idea and a few prompt-level analogues (section 7). No published LLM-agent study uses description length itself as a stopping or selection rule (K22, established negative).

## 2. History and theories in depth

Items marked [background] come from general knowledge of the field and were not opened in this run. The evidence ids named were opened.

### 2.1 Roots: code length as a measure of simplicity [background]
- Kolmogorov complexity and Solomonoff induction: the best prediction comes from the shortest program that reproduces the data. It is not computable.
- Rissanen's minimum description length (MDL): pick the model that minimises (bits for the model) plus (bits for the data given the model). A practical, computable version.
- Chollet (2019, a26) defines intelligence as skill-acquisition efficiency, using algorithmic information theory, and introduces ARC (400 training tasks, 400 evaluation tasks, plus hidden tasks). This is why a solver that learns only from the given demonstrations is the fair comparison.

### 2.2 Neural network weights as code (1993-2019)
- Hinton and van Camp (1993): weights stored with noise cost KL(q||prior) bits (the bits-back argument). The ELBO is the negative description length. Read through Havasi et al. (2019, a24), not directly.
- Havasi et al. (2019) MIRACLE: encode a weight sample with a random code. Best test performance for a fixed memory budget on LeNet-5/MNIST and VGG-16/CIFAR-10 (a24). 1 nat = 1.44 bits.
- Kingma and Welling (2014, a25): the VAE loss is reconstruction plus KL to a prior, readable as a code length. CompressARC's decoder is a VAE decoder with a custom equivariant network.

### 2.3 Prediction is compression (2019-2024)
- Deletang et al. (2024; a22, b16): prediction and lossless compression are equivalent through arithmetic coding. Chinchilla 70B compresses ImageNet patches to 43.4% of raw size (PNG 58.5%) and LibriSpeech to 16.4% (FLAC 30.3%). On enwik9: Chinchilla 70B 8.3%, Llama 2 7B 8.9%, gzip 32.3%. When parameters are counted the adjusted rate is far worse. The best model size depends on dataset size (a23): on small data the model's own size outweighs its gain. For one puzzle the data are tiny, so the model must be tiny (CompressARC has 76K parameters).
- Huang et al. (2024; b17): across 31 public LLMs and 12 benchmarks, compression of external text correlates -0.93 (average) to -0.95 (per domain) with benchmark score. This is a correlation across models, not a test of per-task compression (K17).

### 2.4 Test-time training: learning at inference (2020-2025)
- Sun et al. (2020; c26): founding test-time training paper. Update the model on a self-supervised loss from a single test sample before predicting. On CIFAR-10-C level 5 it often gained over 10% over joint training and never hurt by more than 0.2%; online TTT gained over 24% on three noise types (figures read from text only).
- Sun et al. (2024; a27): TTT layers. The hidden state is a small model updated by a gradient step on each token. TTT-Linear and TTT-MLP keep lowering perplexity past 16k context where Mamba does not (125M to 1.3B parameters).
- Hardt and Sun (2024; c27): fine-tune on about 20 retrieved neighbours, one gradient step each. Bits per byte fell 20% on Pile tasks, more on code.
- MindsAI pioneered TTT for ARC from 2023. ARChitects won the 2024 Kaggle prize with it (c28). Akyurek et al. (2025; a12) published the clean study.

### 2.5 CompressARC (2025)
- Formal framing (a02): code golf. The shortest self-contained program that prints the whole dataset, with unsolved grids filled arbitrarily. Algorithmic information theory says a one-size-fits-all compressor is at most len(decoder code) bits worse than the best practical compressor.
- Practical form (a03): three code parts. Weights and z are sent with relative entropy coding (cost = KL to a reference Gaussian). Output corrections are sent with arithmetic coding (cost = cross-entropy on the given grids). With reference N(0, I/2 lambda) the weight cost would be L2 regularisation. The authors drop the weight term, so the practical objective is not a full MDL (a03, b09, c13).
- Symmetry-breaking costs (a11): the architecture starts fully symmetric (example order, colour, rotation, flip). Using z to break a symmetry costs bits, and larger symmetry groups cost more. The cheapest explanation breaks the fewest symmetries.
- Recognition: third place in the ARC Prize 2025 paper awards ($5k), behind TRM ($50k) and Pourcel/Colas/Oudeyer ($20k) (b10, c14).

### 2.6 Rivals and successors (2024-2026)
- Program-synthesis search with LLMs (Greenblatt style; SOAR, d10) and induction-plus-transduction ensembles (Li et al., a21).
- Small recursive networks trained on ARC data: HRM (a17), TRM (a18). The ARC Prize audit called HRM in effect zero-pretraining test-time training like CompressARC, and found the outer refinement loop, not the hierarchy, carried the gain (a16, c19).
- Latent program search (LPN, a19, a20): gradient search in a learned latent space at test time.
- LLM agents with a prompted simplicity step (Rodionov 2026; d06, d07). This is the closest 2026 LLM-agent use of an MDL proxy. It does not measure description length.

## 3. Core findings with exact numbers

Eval = 400 public ARC-AGI-1 evaluation puzzles; train = 400 public training puzzles. Pass@2 = two guesses (official metric).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| CompressARC solves a fifth of public eval puzzles with no pretraining | 76K parameters; 2000 Adam steps (lr 0.01, betas 0.5/0.9); 20% eval, 34.75% train pass@2; about 20 min per puzzle on one RTX 4070 | Liao & Gu 2025 (a01, b01, c01) | [S] single source |
| Accuracy grows with steps (eval pass@2) | 100 steps 1.25%; 300 10.75%; 500 15.0%; 1000 19.25%; 1500 21.5%; 2000 20.0%. Not strictly monotone | a04, b02, c03; critique note 2 | [S] |
| Accuracy grows with steps (train pass@2) | 100 steps 2.25%; 300 21.25%; 500 27.5%; 1000 31.75%; 2000 34.75% | c02 | [S] |
| Many guesses help: the right answer is sampled but not picked | Eval at 2000 steps: pass@1 18.5%, @2 20%, @10 26.0%, @100 31.25%, @1000 33.75%. Train: pass@1 30.25%, @10 41.5%, @100 48.5%, @1000 52.75% | a04, b02, b03, c02 | [S] |
| Compute is the boundary | Train 130 h, eval 138 h for 400 puzzles, one puzzle at a time (train 6 h at 100 steps, eval 7 h). Kaggle limit 12 h for the whole hidden set. Our arithmetic: about 100 GPU-minutes per solved eval puzzle (20 min / 0.20) | a04, b20, d04 | [S] |
| Compression plus priors, not the objective alone | Plain U-Net on the single puzzle: 0.75% eval (10000 steps; shape-change puzzles scored zero); 2.5% train without augmentation, 1% with | a09, c10, d03 | [S] |
| Worked example: the code is short and readable | Puzzle 272f95fa: KL goes to zero in all z tensors except four (rows, columns, direction-colour table, colour). Top principal components 1485x, 1253x, 829x the next. Correct colours near step 350; final by 1500; solved in about 150 steps in the blog run | a06, c12 | [S] one hand-picked case |
| Seed fragility | A needed tensor can fall to zero KL and never recover. Authors never saw recovery. No numeric seed variance | a07, c12, d03 | [S] |
| Abilities and failures follow hand-built layers | Can: colour assignment, infilling, cropping, line connection incl. 45 degrees, same-colour detection, adjacency, short translation. Cannot: two-colour mapping, serial repetition, counting, rotation, reflection, rescaling, duplication, connectivity, planning, long range | a08, b04, c06, c07 | [S] |
| Not competitive on ARC-AGI-2 | About 4% (private); o3 medium 3.0% vs 53.0% on ARC-1; ARChitects 2.5% vs 56.0%; o3-mini high 3.0% vs 34.5%; Claude 3.7 8K 0.9% vs 21.2% | b10, b19, d05 | [E] that adaptation systems drop sharply; CompressARC's 4% is a one-line summary |
| Humans | 76.2% average on train set, 98.5% experts (LeGris et al., as cited); ARC-1 validation average 60.2%, best 98% (Li et al.); on ARC-AGI-2 every task was solved by at least two non-expert humans, average 2.7 min per task | b08, a21, b19 | [S] |
| TTT on a pretrained LLM | 80-task subset: 18.3% to 47.1% (8B own fine-tuned); fine-tuned alone 5% vs TTT 29% on ablation subset (about 6x); 53.0% on public validation with BARC base; 61.9% ensembled with program synthesis; semi-private 47.5%; BBH 10-shot 50.5% to 57.8% | Akyurek et al. 2025 (a12, a13, b12, c23) | [E] (TTT dominant 2024: a14, c28) |
| TTT ablations | No geometric transforms -16 tasks (55%); direct input-output format -11 (38%); shared instead of per-task adapter -7 (24%); demo-output loss 26% to 29%; 1B and 3B match after TTT | a13 | [S] |
| Likelihood selection over views | 8B: 18.3 baseline, 44.5 TTT, 62.5 with 16 augmented samples, 67.6 with product of experts, 71.6 full system (286.5/400) at about 2 cents per task. 3B: 14.9, 40.9, 52.9, 59.5, 61.4. TTT about 51 s per task on RTX 4090; initial fine-tune 98 H100 hours | Franzen et al. 2025 (b15, c21, c22) | [E] (also d11, d12) |
| Selection transfers without TTT | Sudoku 3M: product of experts 53% top-1, above the highest-probability sample; if a correct solution is sampled it is consistently selected | b24 | [S] |
| Augmented voting needs a trained model | AIRV: base 5, AIRV only 13, TTFT+AIRV 39 (garbled table); best 58% private ARC 2024. 200M LongT5 with LoRA TTT, 18 views, 8 D4 transforms: 27% ARC-AGI-2 semi-private (12.08, 19.86, 25.00 in stages). SOAR voting 52% vs oracle 57.25% | d11, d12, d10 | [S] each; [E] as a family |
| Induction and transduction are complementary | Validation, 2 tries (later version): transduction 39.25%, with reranking 43.0%, TTT 56.75%, induction 20k samples 35.25%. Earlier version: transduction 37.50%, with TTT 43.25%, induction 10k 19.25%. Ensemble 56.75%; with Akyurek TTT 61.9% | a21, b13 | [S]; baselines vary by paper version |
| Small recursive models beat zero-pretraining | TRM 7M: 44.6% ARC-1, 7.8% ARC-2; HRM 27M: 40.3 / 5.0; direct-prediction transformer 21.0 / 0.0; Gemini 2.5 Pro 37.0 / 4.9; Sudoku-Extreme 87.4% vs HRM 55.0% | a17, a18, c16, c17 | [E] |
| HRM audit | ARC-1 semi-private (100 tasks) 32% vs 41% public claim; ARC-2 (120 tasks) 2%. 1 to 2 outer loops +13 points; 1 to 8 loops doubles the score. Training on eval tasks only: 31%. Plain transformer within about 5 points. A per-task-only run was guessed to match CompressARC (21%), not measured. $1.48 / $1.68 per task | a16, b11, c18-c20 | [E] outer loop matters; blog-level |
| Latent program search | ARC eval at 2e13 FLOPs: LPN 15.25% vs TTT 13.50%; 2e14 15.50 vs 16.00; 2e15 15.50 vs 15.25. Pattern task out of distribution: TTT 0.3-1.8%, LPN 88.0% (std 5.3, 3 seeds) | a19, a20, b14 | [S] |
| No-MDL per-task fitting mostly overfits | NCA, about 10,000 parameters: 23 of 172 feasible train tasks (13.37%); largest failure group fits training pairs but fails on new inputs | b18, c08 | [C] not a clean ablation |
| Prompted simplification in a coding agent | 25 public ARC-AGI-3 games, mean RHAE, textual / executable / simplification / verification: gpt-5.4 high 34.16/33.54/30.60/39.16; gpt-5.4 xhigh 40.67/44.72/53.10/53.72; gpt-5.5 high 58.85/51.16/58.35/65.64; gpt-5.5 xhigh 72.51/69.70/73.09/74.78. Simplification beat executable-only in 3 of 4 settings; 127-176M tokens (gpt-5.4) vs textual 63-98M | Rodionov 2026 (d06, d07) | [S] single runs, not equal tokens |
| Cost ladder on ARC-AGI-2 | NVARC 24.03% at $0.20 per task; ARChitects 16.53%; MindsAI 12.64%; Gemini 3 Pro 31% at $0.81; with Poetiq refinement 54% at $31; Opus 4.5 same harness about $60; Opus 4.5 thinking 64k 37.6% at $2.20 | d05, c15 | [S] |
| No LLM-agent study uses description length as a rule | SOAR: weight = count + 1000 x train accuracy; LLM-PV: held-out validation score; Rodionov: prompt schedule. Agent-framework study (22 frameworks, 12 consistent at 74.6-75.9%) tests no compression | d10, d14, d06, b23 | [E] negative (3 sources) |
| Language models are strong compressors | Chinchilla 70B ratios above; correlation -0.93 to -0.95 over 31 LLMs | a22, b16, b17 | [E] |

## 4. Mechanisms and models

### 4.1 CompressARC, step by step (enough to re-implement)
Inputs: one puzzle. The known grids are the demonstration pairs plus the test input grid. The test output is unknown.
1. Make a multitensor latent z. Tensors have shapes over (example, colour, height, width, direction). Only 18 legal shape combinations are kept (a11). Example order is a symmetry axis, so the net treats examples exchangeably.
2. Decoder: an equivariant network built from custom layers (a11, c06). It is symmetric to example order, colour permutation, and rotation/reflection (8 directions). Layers were hand-designed to give specific skills. One decoding layer only; a hierarchical VAE gave all the KL to the first layer (a11, c09).
3. Loss = 10 x reconstruction cross-entropy on the known grids (blog, b21) + KL(q(z)||N(0, I)). The weight KL term is switched off (a03).
4. Optimiser: Adam, lr 0.01, betas 0.5 and 0.9, 2000 steps (b21). Fresh random weights per puzzle.
5. During training, sample the decoder output every step. The output grid is unconstrained: it is whatever the decoder produces for the unknown cells.
6. Answer choice (c04): the most frequent sampled grids over training. The blog adds an exponential moving average (decay 0.97) and downweights uncertain samples. The final answer is two guesses.
7. Inspect (optional): KL per tensor shows which parts of z carry information. Tensors at zero KL are unused.

Why it can work (a06, a11): to reproduce all known grids, z must carry the rule. Every symmetry the answer needs to break must be paid for in bits. So the cheapest z encodes a rule that uses few distinctions. The missing output is generated by the same rule.

What the paper does not show: that fewer bits correlates with a correct answer across puzzles (c05: case studies only), or that the MDL loss beats a reconstruction-only loss on the same network (d03, K24).

### 4.2 Code length is the same thing as selection by likelihood
Negative log-likelihood under a model is a code length in bits (arithmetic coding; a22). So these are one mechanism:
- Score a candidate answer by its summed NLL over many augmented views of the task (Product of Experts, b15, c21). Pick the lowest.
- Score the whole task, including the candidate, by how few bits a small model needs after a few gradient steps (CompressARC's loss, run once per candidate).
- Score a rule by its length (shortest consistent program).

PoE selector (b15, c21): for each of 16 or more views (D4 transforms, colour permutations), build the prompt, compute the candidate's log-probability under that view, sum, and take the best. It needs token-level probabilities of a model tuned on ARC-style data. With closed APIs that expose no log-probs this cannot be done directly. Depth-first sampling at T=9% finds 76.0% of correct candidates against 77.3% for 4x stochastic sampling, using a quarter of the time and half the false positives (c22).

### 4.3 Test-time training recipe (Akyurek; a12, a13)
1. Make leave-one-out tasks from the demonstration pairs (each pair as test, others as shots).
2. Apply geometric transforms (rotate, flip, transpose) and in-context formatting.
3. Train a per-task LoRA adapter, with loss on the demo outputs.
4. Infer on many transformed views, invert, and vote hierarchically. Hierarchical voting beat flat voting and approached the oracle (b25).
Each part counts: removing transforms loses 55% of the solved tasks.

### 4.4 Outer refinement loop
HRM/TRM style: feed the current answer and latent back in for several passes (a16, a18). Audit: 1 to 2 loops +13 points; 1 to 8 doubles the score. For a scaffold this reads as "propose, then refine from your own last output", but only with real feedback (G2).

### 4.5 Prompt-level simplification (Rodionov, d06, d07)
Schedule: one light simplification prompt early, three broader passes, then a planner refactor. The prompt asks for shared parameterised rules instead of special cases. No numeric target; advisory only. This is the only transferable prompt-level pattern found. It was tested only inside a long coding-agent loop (median 4 h 26 min per playthrough, max 53 h).

## 5. What holds up

### Replicated or independently audited
- Test-time training works on ARC. Several teams found it (Akyurek, ARChitects, MindsAI, Franzen, VARC, AIRV, the 200M LongT5 pipeline). Weights are updated per task. [E]
- Selection among candidates by likelihood over augmented views beats a single view and often majority vote (b15, d11, d12). Mostly with locally trained models. [E] as a family.
- Outer refinement loops carry the gain of small recursive models. The ARC Prize audit measured 32% (not 41%) on the semi-private set for HRM (a16, c18). [E]
- Every strong test-time-adaptation system falls hard on ARC-AGI-2 (b19, d05; TinyLM 96.1% train vs 21.7% eval, d13). [E]
- Language models compress well, and compression tracks benchmark score across models (b16, b17). [E], but across models, not per task.

### Not replicated
- CompressARC's 20% and 34.75% have no independent replication or failed replication. Checked: arXiv search, Semantic Scholar citing list (4 citing items), the repo README (no expected accuracy, no seeds, no ARC-AGI-2 support), an aggregator page (no follow-ups), web searches. Coverage was limited by rate limits (HTTP 429 on Semantic Scholar, OpenAlex, arXiv API). Absence is not proof (b22, c29, d01, d02, d17). [S]
- The ARC Prize 2025 report puts it at about 4% on ARC-AGI-2 (d05). This is a one-line summary with no table; the source run was not found.

### Failures and boundary conditions
- Posterior collapse: a necessary latent tensor drops to zero KL and never recovers. A KL floor did not help. No rate is reported (a07, c12).
- Reconstruction-only training can settle on memorisation: in puzzle 6d75e8bb information moved out of the latent into the nonlinear layers between steps 600 and 1000 with no output change (c08).
- Failed or weak ideas in Appendix K, qualitative only: hierarchical decoding, convolution-like copy layers (noise), tropical convolution (toy puzzles only), KL floor. Joint training across puzzles was not tried (c09).
- Augmentation made the U-Net baseline worse (2.5% to 1% on train), but augmentation in TTT is essential (55% of tasks lost without it). Different regimes (a09, a13).
- Train/eval gap: 34.75% vs 20% is a 14.75-point drop, so train numbers are optimistic (b03).
- No clean scaling law: eval pass@2 is 21.5% at 1500 steps and 20.0% at 2000 (critique note 2).
- LPN saturates near 2e13 FLOPs and TTT catches up at higher compute (a19).
- Lab-to-hidden gap: Akyurek 53.0% validation vs 47.5% semi-private; HRM 41% vs 32%.

### Competing explanations
- Compression as the mechanism (a06, c05) versus architecture as the mechanism (a09, b05, c06). The U-Net control gets 0.75% vs 20%, so the objective alone is not enough. The opposite control (same equivariant net, reconstruction only) was never run, so "compression causes the gain" is untested; only "compression plus these priors" is (critique, d03). [C]
- NCA (b18) is cited as a no-MDL contrast but differs in architecture, task filter (172 of 400 feasible) and metric. Weak support.
- The ARC Prize guess that a strict per-task HRM run would match CompressARC (c20) was not measured.

### Interventions that worked and did not
Worked: per-task adapters over shared ones (7 tasks, 24%); geometric augmentation (16 tasks); augmented-view sampling (+18 points at 8B, 44.5 to 62.5); product of experts (+5.1, 62.5 to 67.6); outer loops (+13 for the second pass); depth-first sampling (c22).
Did not work: plain single-puzzle U-Net (0.75%); hierarchical decoding; KL floor; adding augmentation to the U-Net; no-MDL NCA (13.37% of a filtered set).

## 6. Language models

| System | Learns weights per task? | Result | Notes |
|---|---|---|---|
| Direct LLM, no adaptation | no | Static transduction never above 11% on ARC-1 private (a14); o3 medium 53.0% ARC-1, 3.0% ARC-2 (b19); Claude 3.7 8K 21.2% / 0.9% | ARC-1 is public and near saturation |
| LLM writing programs (induction) | no (but fine-tuned in some) | Induction 35.25% (20k samples, vote); SOAR single Claude-4-Sonnet 20.75%, GPT-4.1 8.00%, o3-mini 38.25% (d10) | SOAR ensemble 52%, oracle 57.25%, about 30,000 attempts per task |
| TTT (Akyurek) | yes, LoRA | 18.3 to 47.1 (80 tasks); 53.0 validation; 61.9 with program synthesis | Needs weights |
| TTT + PoE (Franzen) | yes | 71.6% public eval at about 2 cents per task | Public eval; fine-tuned 8B |
| Compression solver (CompressARC) | yes, from scratch | 20% / 34.75% | About 4% on ARC-AGI-2 |
| Small recursive nets | trained on ARC | TRM 44.6 / 7.8 | Not compression |
| Frontier + refinement harness | no | Gemini 3 Pro 31% at $0.81; with Poetiq refinement 54% at $31 | Refinement is the 2025 theme (c15) |
| Coding agent with simplification prompt | no | Mean RHAE 53.10 vs 44.72 (gpt-5.4 xhigh); worse in 1 of 4 settings | ARC-AGI-3 games; not equal tokens |

Findings for LLMs specifically:
1. Learning at inference time is the main lever on ARC, but only when weights can move. Gains are about 6x on the ablation subset (5% to 29%) and 2.4x over a fine-tuned 8B (18.3 to 44.5).
2. Selection by likelihood over augmented views is the second lever, adding 18 points (44.5 to 62.5) then 5 more (to 67.6). This is where compression thinking meets LLMs: NLL is code length.
3. LLMs are good compressors in the raw sense, but that is not compressing a single puzzle. A big model's fit to one puzzle says little alone (a23).
4. There is no closed-API measurement of view-based selection. SOAR voting is 5.25 points below its oracle at 30k samples (K25).
5. Description length has not been tested as a rule inside an LLM agent loop (K22). The nearest is Rodionov's prompt (d06). Simplification helped in 3 of 4 settings but cost 1.6-2.4x tokens, had no textual-plus-simplification arm and used single runs. We cannot say simplicity itself did the work.
6. Cost: CompressARC is about 100 GPU-minutes per solved puzzle. TTT pipelines are about $0.20 per task on ARC-AGI-2 (d05). CompressARC is not cost-competitive there (K23).
7. TTT layers and nearest-neighbour fine-tuning lower perplexity (20% fewer bits per byte; a27, c27). That is memory and retrieval, not a reasoning gain.

## 7. What our agent should take

Our agent is prompt-only around a closed-API model. It cannot train weights and cannot rely on token probabilities. Honest summary: almost nothing here is "add now". The established parts (TTT, view-based selection) do not run on our stack, and the compression-specific parts are single-source.

### Add now (established)
These mostly confirm what SCHEMA.md already has.

1. Keep selection in code, by agreement plus a check, and treat agreement as a hint only. Schema part G4, G5, S7. [E] K12, K22 (selection in all strong systems is done in code by votes, train accuracy or likelihood). Evidence a05, b15, c04, d10. Already in the schema; no change.
2. Log the selection gap: the best candidate available against the one picked. Schema part S7 and section 6 logs. [E] pattern: pass@1000 33.75% vs pass@2 20% (CompressARC); SOAR 52% vs 57.25% oracle. Evidence a04, d10. Logging only, no new behaviour.
3. Refine from the model's own earlier output only with real feedback. Schema part S5, G2. [E] K15: the audit shows outer loops matter (+13 points for 1 to 2 loops). Evidence a16, c19. Already consistent with G2 and "at most 2 rounds".

### Test first (single-source or contested; details in UNKNOWNS.md)
4. Shortest-consistent-rule tie-break at S7. [S] K22; a02, a11. No measurement of length as a rule exists (U1).
5. Prompted simplification pass (fewer special cases, shared parameterised rules) before S7, or as an operator. [S] K21: 3 of 4 settings better, one worse; 1.6-2.4x tokens; single runs (U2).
6. Distinction counting in S2 REPRESENT: list the distinctions the answer needs and prefer rules that need fewer. [S] a11, a06. Analogy only; no LLM measurement (U3).
7. Stability-across-views selection (transform the puzzle, answer, invert, vote) at S7 / G4. [S] K25: only local trained models. Risk: views are still one model, so errors may stay correlated (G4) (U4).
8. Augmented view before prompting (rotate, recolour) as O6 change representation. [S] K11 (55% of tasks lost without transforms in TTT); different regime (U5).
9. Induction/transduction routing (write a program vs answer directly) at S0/S3. [S] K13; baselines vary by paper version (U6).
10. CompressARC as a side solver for grid puzzles, routed by class. Outside the text schema. [S] K01, K08, K13. Narrow, slow, unreplicated. Measure overlap with our scaffold first (U7, U8).
11. Log-probability scoring of candidates under views at S7. [S] K12 (trained models only); only if our model exposes log-probs (U9).
12. Record seconds and dollars per solved item. G7, G12. [S] K23; no cost to add the log (U10).

## 8. Concrete tests on our bench

All arms at equal total tokens (setup and all samples counted), at least 3 seeds, same items, same graders. Report the per-item flip rate, not only the mean.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-1 eval items we already run, plus word puzzles with a verifier | (a) majority vote; (b) shortest-consistent-rule tie-break among consistent candidates | Pass@2; gap to oracle | Small gain on ties only (we guess 1-3 points); none when there are no ties |
| T2 | Same items | (a) free-form; (b) free-form plus one simplification pass; (c) free-form plus one extra sample at equal tokens | Pass@2 at equal tokens; tokens per solved item | Rodionov saw +8.4 points in one setting and -3.0 in another; expect -3 to +5 |
| T3 | Grid items | (a) single view, 8 samples; (b) 8 transformed views (D4, colour permutation), invert, vote; (c) code-checked held-out pair | Pass@2; oracle gap | 3 to 8 points if views decorrelate errors; zero if the model is already invariant |
| T4 | Items with a verifier | (a) plain; (b) "list the distinctions your rule needs; choose the rule that needs fewest" in S2 | Pass@2; rule length; over-fit rate (passes demos, fails held-out) | Fewer over-fitted rules; size unknown |
| T5 | Items we solve at 20-60% | Induction-only, transduction-only, both at equal budget split | Union and intersection of solved sets; accuracy of the agreed pick | Complementary sets, as in Li et al. (a21) |
| T6 | 50 public ARC-1 eval puzzles, local GPU | Released CompressARC, 3 seeds, 2000 steps; intersect its solved list (list_solved_puzzles.py) with our scaffold's | Solve rate and seed variance; overlap; GPU-seconds per solved item | About 20% per puzzle with a visible flip rate; overlap decides routing |
| T7 | Same 50 puzzles | CompressARC with KL term vs reconstruction-only (same equivariant net) | Pass@2 | If MDL adds nothing, drop "compression" from the claim |
| T8 | All runs | Cost log | Seconds and dollars per solved item, per arm | Context for G7 |
| T9 | Items on a local open model with log-probs | NLL-sum over views vs vote vs single greedy sample | Pass@2 | About +5 over vote, as PoE in trained models |

## 9. What does not transfer, and why

- Gradient training per puzzle (CompressARC, TTT, per-task LoRA). Our agent has no weights it can change (K10, K01).
- Hand-built equivariant layers. The result depends on them (U-Net 0.75% vs 20%). A prompt cannot install symmetry or layers (K06).
- Time per puzzle. 20 minutes on one GPU is far over an interactive step (b20).
- Grid-only scope. Failures (counting, long range, planning, serial steps) are what many reasoning tasks need (K08). No data on non-grid tasks.
- Token-level likelihood selection. It needs a model tuned for the task and its log-probs. The gains (44.5 to 71.6) are with fine-tuned 8B models on RE-ARC data (b15).
- Headline scores. Public ARC-1 is public and near saturation. About 4% on ARC-AGI-2 shows the method does not extend to hard puzzles (d05).
- Raw language-model compression ratios (a22). They say nothing about per-puzzle reasoning.
- Weight counting. Deletang et al. show the adjusted rate counts model size (a22, a23). A big LLM's fit to one puzzle is not a short description, because its weights are not paid for.
- The cross-model correlation of -0.95 (b17) is not a per-task selection rule.
- Memory-level TTT (a27, c27) lowers perplexity, not reasoning error.

## 10. Open questions

1. Does CompressARC replicate on other hardware with 3+ seeds at about 20% eval, and what is the per-puzzle flip rate? (K02, K05)
2. Does the MDL objective or the equivariant prior carry the result? No reconstruction-only control exists (K24).
3. Does the weight-cost term matter? The authors call omitting it reckless and never tested it (a03, b09).
4. Does a prompt-level compression proxy help at equal tokens versus free-form reasoning? Only Rodionov's non-equal-token test exists (K21).
5. Do CompressARC and an LLM scaffold or TTT systems solve different puzzles? No overlap study. The repo has a solved-list script (d16).
6. Can a closed-API LLM do stability-across-views selection, and what is its gap to the oracle? (K25)
7. Is shorter-rule selection better than votes? Nobody measured it (K22).
8. Same-item cost curve: seconds per solved puzzle for CompressARC vs TTT vs a frontier LLM (K23).
9. What does a compression solver do on non-grid tasks (text puzzles, maths)? No data.
10. Is the 4% ARC-AGI-2 figure from a run or a summary? The source run was not found (c14, d05).
11. Does correctness track bits per puzzle across puzzles? Case studies only (c05).
12. Would a hypernetwork or shared puzzle embedding (the authors' untried ideas, b09) remove the 20-minute cost?

## 11. Sources

[V] = opened by a research agent in this run (critique.md re-opened Liao & Gu, Akyurek, Li, Jolicoeur-Martineau and Franzen against the PDF text). [M] = snippet only or not opened.

- [V] Liao and Gu (2025) ARC-AGI Without Pretraining (CompressARC). https://arxiv.org/abs/2512.06104 (HTML https://arxiv.org/html/2512.06104v1)
- [V] Liao (2025) author blog post. https://iliao2345.github.io/blog_posts/arc_agi_without_pretraining/arc_agi_without_pretraining.html
- [V] CompressARC code repository (MIT). https://github.com/iliao2345/CompressARC
- [V] Akyurek et al. (2025) The Surprising Effectiveness of Test-Time Training for Few-Shot Learning. https://arxiv.org/abs/2411.07279
- [V] Li et al. (2025) Combining Induction and Transduction for Abstract Reasoning. https://arxiv.org/abs/2411.02272
- [V] Franzen, Disselhoff, Hartmann (2025) Product of Experts with LLMs. https://arxiv.org/abs/2505.07859
- [V] Jolicoeur-Martineau (2025) Less is More: Recursive Reasoning with Tiny Networks (TRM). https://arxiv.org/abs/2510.04871
- [V] Wang et al. (2025) Hierarchical Reasoning Model. https://arxiv.org/abs/2506.21734
- [V] ARC Prize Team (2025) The Hidden Drivers of HRM's Performance. https://arcprize.org/blog/hrm-analysis
- [V] ARC Prize Foundation (2025) ARC Prize 2025 results and analysis. https://arcprize.org/blog/arc-prize-2025-results-analysis (one later line, d15, was snippet-only)
- [V] ARC Prize 2025 Technical Report. https://arxiv.org/html/2601.10904
- [V] Chollet et al. (2025) ARC Prize 2024 Technical Report. https://arxiv.org/abs/2412.04604
- [V] Chollet et al. (2025) ARC-AGI-2. https://arxiv.org/abs/2505.11831
- [V] Chollet (2019) On the Measure of Intelligence. https://arxiv.org/abs/1911.01547
- [V] Macfarlane and Bonnet (2024) Searching Latent Program Spaces. https://arxiv.org/abs/2411.08706
- [V] Deletang et al. (2024) Language Modeling Is Compression. https://arxiv.org/abs/2309.10668
- [V] Huang et al. (2024) Compression Represents Intelligence Linearly. https://arxiv.org/abs/2404.09937
- [V] Havasi et al. (2019) MIRACLE. https://arxiv.org/abs/1810.00440
- [V] Kingma and Welling (2014) Auto-Encoding Variational Bayes. https://arxiv.org/abs/1312.6114
- [V] Sun et al. (2020) Test-Time Training with Self-Supervision. https://arxiv.org/abs/1909.13231
- [V] Sun et al. (2024) Learning to (Learn at Test Time). https://arxiv.org/abs/2407.04620
- [V] Hardt and Sun (2024) Test-Time Training on Nearest Neighbors for LLMs. https://arxiv.org/abs/2305.18466
- [V] Xu and Miikkulainen (2025) Neural Cellular Automata for ARC-AGI. https://arxiv.org/abs/2506.15746
- [V] Pourcel, Colas, Oudeyer (2025/26) SOAR. https://arxiv.org/html/2507.14172v2
- [V] Hu et al. (2025) ARC Is a Vision Problem (VARC). https://arxiv.org/abs/2511.14761
- [V] Cole and Osman (2025) AIRV. https://arxiv.org/html/2506.14276v2
- [V] ARC-AGI-2 Technical Report (200M LongT5 pipeline). https://arxiv.org/html/2603.06590v1
- [V] Talley et al. (2026) Multi-Perspective Transformers in ARC-AGI-2 (abstract only). https://arxiv.org/abs/2605.01154
- [V] Rodionov (2026) Do Coding Agents Need Executable World Models, Simplification, and Verification. https://arxiv.org/html/2607.15439
- [V] Habr write-up of the ARC-AGI-3 coding agent (secondary). https://habr.com/ru/article/1081200/
- [V] Rasheed et al. (2026) Agentic Frameworks for Reasoning Tasks. https://arxiv.org/abs/2604.16646
- [V] LLM-PV (abstract). https://arxiv.org/abs/2510.14331
- [V] Emergent Mind page on CompressARC (aggregator). https://www.emergentmind.com/topics/compressarc
- [M] Hinton and van Camp (1993), Kolmogorov, Solomonoff and Rissanen background, and LeGris et al. (2024) human data (cited through b08). Not opened, no URL.
