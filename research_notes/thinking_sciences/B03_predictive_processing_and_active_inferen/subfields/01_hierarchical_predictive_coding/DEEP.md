# Hierarchical predictive coding: deep document

*Subfield B03.01. Sources: evidence_a-d.jsonl (ids a01-a26, b01-b27, c01-c25, d01-d18), claims.jsonl (K01-K24), critique.md. Relevance to our agent is background only; the nearest operational ideas are residual-only passing (K09, K21) and foresight reweighting (K17), and neither is specific to predictive coding. Corrections from the critique are applied throughout.*

## 1. What it is

Hierarchical predictive coding (PC) is a theory of how a stack of processing levels can work.

- Each higher level sends a prediction down to the level below.
- Each lower level compares the prediction with its own input.
- Only the mismatch (the residual, or prediction error) goes back up.
- Higher levels change their state to cut the error. Weights change to cut the error over time.

So predictions flow down and errors flow up. One objective (total squared error, or variational free energy) drives both inference and learning. It is a process theory: it says which cells or layers do what, so it can in principle be tested.

Three different things share this name. Keep them apart.

1. A neuroscience claim: cortex works this way. Evidence is mixed (section 5).
2. A machine-learning training method: PC networks learn with local rules and iterative inference. It matches backprop on small nets and fails at depth without fixes (section 3, 4).
3. A design metaphor: send the residual, not the signal; predict, compare, update. This is what could matter to a scaffold. No study tests it in an LLM loop (section 6, 10).

Status for our agent: background only. No schema element is justified by this field today. Two items go to the test list.

## 2. History and theories in depth

**Efficient coding roots (1982).** Srinivasan, Laughlin and Dubs (1982) described predictive coding in the retina: send what the neighbours cannot predict. [a02, via Millidge review]

**Mumford (1992), "On the computational architecture of the neocortex II".** Extended the retina idea to a general cortical theory. Higher areas send down templates. Lower areas send up only the residual after fitting the template. No simulations. Not opened by us; described second-hand. [a01, a02]

**Rao and Ballard (1999).** The first working network. Feedback carries predictions of lower-level activity. Feedforward carries residual errors. Trained on natural images, the hierarchy developed simple-cell-like receptive fields. The error units showed endstopping and other extra-classical effects: a bar that ends just outside a field raises error because the top-down prediction of continuation is violated. [a03, a04, b21, d07] Only the abstract was read. Methods numbers (patch size, unit count, image count) are not known to us. Feedforward models and sparse coding with normalisation can also give endstopping.

**Murray et al. (2002 PNAS; the V1/LOC paper is 2002, not 2004).** fMRI: coherent shapes raised activity in the object area LOC and lowered it in V1, read as higher areas "explaining away" lower input. [a05, d08] Abstract only. BOLD sums error and prediction units, and attention differs between conditions.

**Friston (2003-2008).** Recast the Rao and Ballard energy as variational free energy. Learning rules became approximate Bayesian inference. Precision (inverse variance) became gain on error units and was linked to attention. [a02, a11]

**Bastos et al. (2012), canonical microcircuits.** Turned the idea into a process theory with a laminar map. Superficial pyramidal cells (L2/3) carry forward errors. Deep pyramidal cells (L5/6) hold expectations and send feedback. L4 spiny stellate cells take feedforward input. Precision gates superficial error cells. Feedback should be inhibitory and modulatory. Supporting data cited: superficial layers carry more gamma, deep layers more alpha/beta; optogenetic L6 activation cut V1 responses about 80-84% (Olsen 2012). Read only the first 100k of 187k characters. [a11, a24]

**Machine-learning branch.**
- Whittington and Bogacz (2017): a PC net with local Hebbian updates approximates backprop. MNIST, 20 inference steps, validation error 1.7-1.8% for the comparison nets. [a14]
- Song et al. (2020): exact backprop weight updates with local plasticity (abstract only). [a15]
- Millidge, Tschantz, Buckley (2020): PC converges to backprop gradients on any computation graph. CNN, RNN, LSTM. [a16, b08, c02]
- Song et al. (2024), prospective configuration: settle activity first, then change weights. Less interference. [b18, c22]
- PredNet (Lotter 2017): a Rao-Ballard stack for video, with only errors passed forward. [a18, a19, c08]
- Scaling work 2022-2026: Pinchetti 2022 (transformer), Pinchetti 2025 (benchmark), muPC, ePC, DeltaNet-PC, tPC-RTRL. [b13, b09, c03, c04, c15, c16]

**Language branch.** Schrimpf et al. 2021: better next-word models fit brain data better. Caucheteux et al. 2023: forecasts of words up to 8 words ahead add to the fit. Heilbron et al. 2022: separate prediction signatures per linguistic level. Rival: Antonello and Huth 2024 say general feature transfer explains the same data. [b24, a20, b17, b16]

**Critics.** Walsh et al. 2020, Millidge et al. 2022, and Feuerriegel et al. 2021 all find the process theory hard to confirm or refute. Error units may be dendritic compartments, not cells, so failing to find them refutes nothing. [a13, b07, b01, d03] Position papers argue LLM next-token training is only partly PC (it lacks action-coupled generative models, compositional hierarchy, episodic memory). [c13, c18, c25]

## 3. Core findings with exact numbers

Status key: established / single-source / contested. "Re-checked" means the critique re-opened the number.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| PC with local rules gives backprop gradients on any graph | Exact gradients within 100 inference iterations at inference rate 0.1; CNN (6 and 16 filters, FC 200-150-10), 5 seeds, batch 64, SVHN/CIFAR-10/CIFAR-100, matches backprop; LSTM on Shakespeare matches; about 100x compute (re-checked) | Millidge 2020 [a16, b08, c02] | established (K01) |
| Small-net equivalence | MNIST, 20 inference steps, validation error 1.7-1.8% | Whittington and Bogacz 2017 [a14] | established, small MLP |
| PC works to depth 5-7, then fails | CIFAR-10 VGG-5: PC-CE 86.61, BP-CE 88.11, centered nudging 89.47. VGG-9: PC-CE 78.12 vs BP 89.18. ResNet-18: PC-CE 43.19, best PC (iPC) 70.44, BP 92.83. Tiny ImageNet ResNet-18 top-1: 9.52 vs 58.00; top-5 26.21 vs 79.94 (re-checked) | Pinchetti 2025 [b09, c05, b11] | established (K02) |
| Cause of depth failure | State rate 0.01: first-layer energy about 1e-6 of last layer; rate 1 balances energy but accuracy drops; AdamW unstable for wide layers (widths 32-4096) | Pinchetti 2025 [b10] | single-source (K03) |
| Speed of implementation | 5.5 s vs about 110 s per CIFAR-100 epoch (library vs a prior implementation) | Pinchetti 2025 [b11] | single-source |
| Error-based fix for depth | ResNet-18 CIFAR-10: ePC 92.17 +-0.26, BP 92.36 +-0.12; CIFAR-100 68.52 vs 69.94; VGG-7: ePC 88.98, sPC 77.79, BP 88.94. The "sPC 53.74" is the MSE column of Pinchetti, 43.19 is the CE column; not a conflict | Goemaere 2025 [c04] | single-source |
| Scaling to 128 layers | Residual PC nets, MNIST about 98% in 5 epochs (5x faster than the prior benchmark); toy classification only | Innocenti 2025 muPC [c03, d13] | single-source (K22) |
| PC language models (tiny) | Conditional LM test perplexity: BP 162.64, KL-PC 175.90, Gaussian PC 590.08 (1 block, 1 head, hidden 128, vocab 8001, 200k train). Row order inferred from text | Pinchetti 2022 [b13] | established that plain PC is unstable (K04) |
| iPC language models | Masked LM: iPC 106.19 (10/10 seeds converge), BP 120.02 (7/10), PC 523.08 (3/10). Conditional LM: iPC 142.54 (7/10) is WORSE than BP 113.32; PC 206.34. The first row alone is a cherry-pick | Salvatori 2024 [b12] | established but mixed |
| Other iPC rows | AlexNet CIFAR-10 with augmentation: BP 83.12, PC 71.99, iPC 80.11. CNN: BP 69.34, PC 70.84, iPC 72.54. MNIST iPC 98.45; FashionMNIST 89.90; VGG-7 iPC 80.15 vs BP 88.60 | Salvatori 2024, Pinchetti 2025 [b12, b11] | single-source |
| PredNet beats matched CNN-LSTM | Rotating faces MSE/SSIM: PredNet L0 0.0152/0.937, Lall 0.0157/0.921, CNN-LSTM 0.0180/0.907, copy-last 0.125/0.631. Caltech: 3.13e-3/0.884 vs 3.67e-3/0.865. Over four other hyperparameter sets L0 cut MSE 14.7% and SSIM error 14.9% on average | Lotter 2017 [a18, c08] | single-source (K09) |
| PredNet features for steering | 1K labels: linear readout explains 74% variance and beats CNN-LSTM by 35%; 25K labels: 2.14 deg^2 vs about 4 for a CNN trained on 396K | Lotter 2017 [a19] | single-source |
| Forecast hierarchy in the brain | fMRI, 304 listeners, 27 stories of 7-56 min, 4.6 h unique stimulus. GPT-2 layer 8 peak brain score R=0.23 in superior temporal sulcus, 60% of noise ceiling. Forecast gain 23% (+-9% across individuals). Best distance 8 words (3.15 s) semantic, 5 words syntactic. IFG forecasts 0.9 +-0.2 words farther than anterior STS (P<0.001). Angular gyrus vs Heschl 2.5 +-0.3 layers. Fine-tuning for deeper-layer 8-word forecasts: over 2% frontoparietal gain; no gain in auditory areas. Random features gave no gain | Caucheteux 2023 [a20, a21, b15, c01] (one study, four lines) | single-source (K10) |
| Brain-LLM fit may be transfer, not prediction | 97 representations, 5 subjects: r=0.847 with next-word prediction, r=0.864 with general transfer, not significantly different. Within a model, the best future-word representations were worse brain models | Antonello and Huth 2024 [b16] | contested (K11) |
| Cross-lingual check | 49 English, 35 Mandarin, 28 French listeners; brain scores stable across layers; context-sensitive embeddings do not beat static FastText (all p>0.95) | Yang 2026 [c11] | single-source, BERT-class |
| Hierarchical language predictions | EEG N=19, 1 h; MEG N=3, 9 h. Continuous prediction vs constrained guessing t(18)=3.18 p=5.2e-3; vs baseline t(18)=5.01 p=9.0e-5. Syntax category, phonemes, semantics dissociable | Heilbron 2022 [b17, d09] | single-source (K23) |
| BERT predictability vs N400 | N=29, EEG+MEG; pre-activation vs N400 EEG r2=0.56 p=0.0126; MEG r2=0.35 p=0.0708 (ns); replication subsets p=0.11 and p<0.05 | Kolbl 2025 [c12] | single-source |
| Expectation suppression needs attention | N=34 fMRI. Interaction F(1,33): V1 7.706 p=0.009 eta2=0.189; LOC 12.580 p=0.001 eta2=0.276; TOFC 16.955 p=2.4e-4 eta2=0.339. Behaviour RT F=37.543. Pupil N=32, no expectation interaction (F(1,31)=2.261) | Richter and de Lange 2019 [d01, d18] | contested (K24) |
| Suppression only for learned wholes | N=34. LOC whole displays t(33)=-3.44 dz=-0.60; mixed BF10=0.19; shuffled 0.25; omnibus P=0.06; V1 none; RT 905 vs 931 ms | Yan 2023 [d04] | single-source |
| Cueing does not sharpen representations | 75% valid cues, n=51 (58 recruited), EEG+pupil. Reproduction precision BF10 about 0.16. Response error visual F=16.996, eta2=0.250, BF10=245 | 2025 cueing study [b20] | single-source |
| Sharpening (Kok 2012) | V1 BOLD lower, decoding better. Numbers not read. Others found better decoding for unexpected stimuli; Rideaux 2026 prefers dampening | Kok 2012, Rideaux 2026 [b22, d05, d06] | contested (K13) |
| Laminar and cell-type | 7T: deep V1 layers up for illusory figures, superficial/middle dampened for predictable inducers. Mouse V1 layer 2/3 has error-like and prediction-like groups; division-based model fits rodent data better than subtraction models | Kok 2016, Fiser 2016 via Walsh [a10, b04] | contested (K07) |
| Hierarchy across adjacent levels | Evidence "scarcer"; most PP-like dynamics from simple stimuli | Walsh 2020 [b05, a25] | single-source (K08) |
| PC-motivated hallucination features | HaluBench subset N=200: theory baseline AUROC 0.8017; supervised base 0.8274; improved 0.8669 (paper says +4.95%, arithmetic +3.95 points); meta-ensemble 0.8414/0.8458; naive averaging 0.48. No CIs | Bhatt 2026 [c09, d12] | single-source (K15) |
| PC block in a 158M LM | Full 12.630; without PC 12.413 (better); without slow memory 12.671; without mHC 15.127 | Xie 2026 [c14] | single-source (K16) |
| Foresight resampling | Llama-3-8B: about 60% of examples myopic; 76.5% of GSM8K errors myopic (the 57.3% for correct samples is unverified). +7.2 GSM8K, +4.3 MATH; Mistral +13.3, +6.8. +25.3% AlfWorld; beats MCTS by 2.4% and guided decoding by 1.4% at about 50% FLOPs. HumanEval 57.3 vs 44.3 plain vs 53.5 beam (290e12 FLOPs); MBPP 38.4 vs 33.5; PDDL 38.3 vs 35.0. Mistral GSM8K: SC(8) 80.9 vs PD+SC 81.3 | Ma 2024 [c10, d10, d11] | single-source (K17) |
| PC memory | DeltaNet-PC 100% recall to L=D=1,024 (3 seeds). tPC-RTRL WikiText-103 byte 1.865 vs BPTT 1.864 BPC; BLEU 20.23 vs 20.29 | Morrill 2026, Potter 2026 [c15, c16] | single-source (K19) |
| Prospective configuration | Less interference, faster at small batch, fewer forgetting effects; margins not extracted | Song 2024 [b18] | single-source (K18) |
| Self-correction null | GPT-3.5 GSM8K 75.9 -> 75.1 -> 74.7; CommonSenseQA 75.8 -> 38.1 -> 41.8; GPT-4 GSM8K 95.5 -> 91.5 -> 89.0. Oracle: 95.5 and 97.5. SC 3/6/9 responses: 82.5/85.3/88.2 vs standard 76.7; debate at 9 about 83.0 | Huang 2024 [d14, d15] | established (K20) |
| Self-repair at equal budget | GPT-4 APPS: 10 initial + 1 repair = 1.05x pass@20; 2 initial + 10 repairs = 0.97x pass@22. Human feedback: repair success 33.3% -> 52.6% | Olausson 2024 [d16] | established with Huang (K20) |

## 4. Mechanisms and models

Written so an engineer can implement them.

### 4.1 Core PC network (Rao and Ballard form)

Layers x_0 (input) ... x_L. Each layer l holds a state vector x_l. The prediction of layer l-1 from layer l is mu_{l-1} = f(W_l x_l). The error is e_{l-1} = x_{l-1} - mu_{l-1}. Energy: E = sum_l (1/2sigma_l^2) ||e_l||^2.

Inference (settling), repeat T times:
- Each state x_l takes a small step down the energy gradient: dx_l = -rate * (e_l - (W_l^T applied to e_{l-1}, scaled by the slope f' of the prediction)). In plain words: each state moves to cut its own error and the error it causes in the layer below.
- State step size (inference rate) 0.1 in Millidge 2020; 0.01 to 1 tested in Pinchetti 2025.
- Number of iterations T is 100-200 in the original, with the rule of thumb T between L and 2L for L layers. [a16, c06]

Learning: after (or during) settling, dW_l = lr * e_l-times-activation Hebbian product. Local: each weight sees only its pre- and post-synaptic quantities.

Supervised use: clamp x_0 to input and x_L to label (or nudge toward it), settle, update. With a feedforward initialisation and small errors, the first update equals backprop. [a16, a15]

### 4.2 Variants that matter

- **iPC (incremental PC).** Update weights at every inference step instead of after settling. More stable, no schedule. Best on small nets, weak on ResNet-18 (70.44). [b11, b12]
- **Centered nudging.** Best PC variant on VGG-5 (89.47). [b09]
- **KL (categorical) energy.** Needed for attention layers: Gaussian PC gave 590.08 perplexity, KL form 175.90. Use softmax outputs with KL divergence as the layer energy. [b13]
- **ePC (error-reparameterised).** Make the layer errors the free variables, not the states. This removes the exponential decay of signal with depth, so inference converges orders of magnitude faster. ResNet-18 92.17. [c04]
- **muPC.** Depth-muP scaling of residual blocks so learning rates transfer across width and depth. 128 layers on toy tasks. [c03]
- **Prospective configuration.** Infer the target activity first, then change weights toward it. [b18]
- **Activation relaxation.** No separate error units; 4-layer MLP, 100 iterations, 5 seeds. [a17]
- **Temporal PC with RTRL (tPC-RTRL).** Recurrent PC that recovers BPTT gradients under assumptions. [c16]
- **DeltaNet-PC.** Associative memory updated by prediction error: write only what is not already predicted. 100% recall to L=D=1,024. [c15]

### 4.3 PredNet (forward only errors)

Each layer has: a recurrent unit (ConvLSTM) R_l, a prediction A-hat_l from R_l, an input A_l, an error E_l = [ReLU(A_l - A-hat_l), ReLU(A-hat_l - A_l)] (two rectified halves, which solves the sign problem), and A_{l+1} = pool(conv(E_l)). R_l gets E_l plus the top-down state from R_{l+1}. Loss: weighted sum of errors, with weight on layer 0 only (L0) or all layers (Lall). L0 was better here. [a18, a19]

### 4.4 Process-theory map for testing

Prediction units in deep layers, error units in superficial layers, precision as gain on error units. Rival implementations: positive and negative error populations (Keller and Mrsic-Flogel 2018); multicompartment neurons with errors stored on apical dendrites; divisive instead of subtractive error (Spratling). Symmetric weights between prediction and error pathways are an open biological problem. [a24, b07, b04, b25]

### 4.5 Scaffold analogue (our own sketch, not tested)

A "PC step" in a prompt loop would be:
1. Draft h (a prediction of what the answer or the next step should be).
2. A check or critic produces a residual r (the part of the output that disagrees with the problem, as located by code).
3. The next attempt receives h-summary plus r only, not the full critic transcript.
4. Repeat only while r is non-empty and a code check keeps failing (this matches guardrails G1, G2).

This is not PC. It borrows one idea (pass the residual). Section 6 and 8 give the test.

## 5. What holds up

**Holds up (established).**
- Mathematical equivalence: PC approximates or equals backprop gradients on arbitrary graphs. Two or more independent sources. [K01]
- Depth limit: PC matches backprop only to about 5-7 layers in the standard form. Three sources: Pinchetti 2025, Salvatori survey, Innocenti thesis. [K02, c06, c17]
- Cost: about 100x compute for the CNN case; claimed speed advantages not consistently seen. [K05, c17, b14]
- Plain Gaussian PC is unstable for transformers. [K04]
- Self-correction without outside signal does not beat voting at equal calls. [K20]

**Does not hold, or is contested.**
- Expectation suppression is replicated in many studies, but a significant contingent failed to replicate (Walsh 2020). [b01]
- Kaliukhovich and Vogels (2011), macaque IT single cells: responses to deviants were indistinguishable from rare but conditionally probable stimuli. So frequency, not expectation, explained it. Boundary conditions: unfamiliar stimuli, passive fixation. Seen second-hand. [a08]
- Summerfield 2008 (fusiform face area; expected repeats gave smaller BOLD than unexpected repeats) is the key support beyond adaptation. Not opened. Later fMRI/MEG/EEG results are mixed. [a07, b02]
- Feuerriegel 2021: four confounds (surprise, attention, repetition/adaptation, novelty). Genuine suppression mainly after weeks of sequence learning; 1-2 session designs inconsistent. Abstract only. [d03]
- Attention: three result patterns across studies (interaction, suppression abolished, equal boost). Baseline choice matters: predicted vs unpredicted and predicted vs mispredicted gave opposite attention results (Hsu et al.). [b03] Richter and de Lange 2019 found suppression only when attended. [d01] Alink and Blank 2021 is a perspective with no data; PC can absorb the attention result through precision. So attention is an open rival, not a proven cause. [d02]
- Sharpening: Kok 2012 has no close independent replication found. Four studies cited by Alink and Blank found better decoding for unexpected stimuli (relayed). Rideaux 2026 preprint favours dampening. A 2025 cueing study found no sharpening (BF10 about 0.16). [b22, d02, d05, b20]
- Direction of effect: Bell et al. found raised responses to unexpected stimuli; macaque IT and rodent V1 studies found reduced responses. It is also disputed whether suppression tracks non-adjacent regularities. [a09]
- Hierarchy across contiguous levels is the least supported hypothesis. [b05]
- Aggregate BOLD cannot test the theory cleanly: error units fall, prediction units may rise, precision may boost error. [a12, b06]
- Brain-LLM alignment: the forecast hierarchy (Caucheteux) and the transfer account (Antonello and Huth) both fit; no test separates them. [K10, K11]
- Cross-lingual: layer-wise surprisal does not reproduce the layer profile; static embeddings equal BERT. [c11]

**Moderators found.** Attention; weeks of learning vs one session; whole learned displays vs single objects (Yan 2023); stimulus familiarity; passive vs task; baseline definition; precision (stable context gives stronger prediction in mouse V1). [b03, d03, d04, a08, b04]

**Interventions that worked.**
- Engineering fixes for PC depth: ePC, muPC, iPC on small nets, centered nudging, KL energy for attention.
- Foresight resampling in decoding (Ma 2024), on math, code and agent planning.
- External feedback in self-repair (human feedback 33.3% -> 52.6%).

**Interventions that did not work.**
- PC block inside a 158M LM: no loss gain. [c14]
- iPC on conditional LM: worse than backprop (142.54 vs 113.32). [b12]
- Intrinsic self-correction, debate, equal-budget self-repair. [K20]
- Raising state rate to 1 to balance layer energy: accuracy fell. [b10]
- Naive averaging of PC-motivated signals: AUROC 0.48. [c09]

**Independence caveats.** K06-K08 evidence is relayed through two reviews (Walsh, Millidge), so independence is partly illusory. The four Caucheteux lines are one study. Founding papers (Mumford 1992, Rao and Ballard 1999, Murray 2002, Kok 2012, Summerfield 2008) were not opened; their exact numbers are missing.

## 6. Language models

**No study found that runs a PC loop inside an LLM agent for reasoning.** An arXiv scan (50 results, 42 read, 2026-11-17) found only small 2025-2026 preprints. [c19] Everything below is adjacent.

**1. LLMs as models of the brain's predictions.**
- GPT-2 forecasts add 23% (+-9%) to fMRI brain scores; semantic forecast reach is 8 words, syntactic 5. [a20, a21]
- N400 tracks BERT and GPT-2 surprisal; EEG r2=0.56, MEG r2=0.35 ns (N=29). [c12, b17]
- Alternative: transfer explains the same data (r=0.864 vs 0.847). Cross-lingual BERT tests fail to show layer-specific prediction. [b16, c11]
- Net: LLM probability is a usable proxy for human surprise. It is not proof that brains or LLMs do hierarchical PC. [K12]

**2. Training LMs with PC.**
- Tiny transformers only. Gaussian PC 590.08 vs BP 162.64; KL-PC 175.90 (8% gap). [b13]
- iPC masked LM 106.19 vs BP 120.02 but conditional LM 142.54 vs BP 113.32. [b12]
- tPC-RTRL ties BPTT at byte level on WikiText-103 (1.865 vs 1.864 BPC) and BLEU 20.23 vs 20.29. [c16]
- No PC-trained LM beyond small scale. muPC goes to 128 layers on classification only. [K22]
- Practitioner statements: advantages not consistently observed; deep PC nets practically untrainable (Innocenti thesis). [c17]

**3. PC-like modules inside LMs.**
- LPC-SM 158M: removing the PC block improved loss (12.413 vs 12.630). Heavily undertrained (loss above 12), single author. [c14]
- DeltaNet-PC: memory write by prediction error; authors claim no accuracy gain over linear attention, only locality. [c15]

**4. PC-motivated signals as checks.** Surprise against context, plus context adherence and falsifiability features, give AUROC 0.8669 vs 0.8274 on 200 HaluBench items. Simple averaging gave 0.48. The "PC" is a label for features, not a PC implementation. [c09, d12]

**5. Nearest agent-loop analogue: foresight.** Sample future steps, reweight the current step. About 60% of examples myopic. +7.2 GSM8K at about 50% of MCTS FLOPs. The edge over equal-budget self-consistency is about 0.4 points in the one readable row. On the 70B agent runs the FLOPs are very large (224.1e13), so gains are not at equal cost. Not tested on open-ended tasks. [c10, d10, d11]

**6. The null baselines any PC-style loop must beat.**
- Intrinsic self-correction lowers accuracy (GPT-3.5 GSM8K 75.9 -> 74.7; CommonSenseQA 75.8 -> 38.1; GPT-4 95.5 -> 89.0). [d14]
- Self-consistency at 9 responses 88.2 beats debate about 83.0. [d15]
- Self-repair at equal budget 0.97x to 1.05x; feedback quality decides. [d16]
- Models are 2023-era; newer models may differ.

**7. Position papers.** LLMs lack action-coupled generative models, hierarchical compositional structure and episodic memory (Rao 2025). Murphy 2024: predictive mechanisms explain linear syntax but little compositional structure. Barenholtz 2025 (blog): LLMs do not predict in PC's sense. No data in any of these. [c13, c18, c25]

## 7. What our agent should take

Overall: this subfield is a design metaphor. No item is established for the agent. The established items are cautions (negative results). Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.

### Add now (established)

These add no new element. They confirm existing guardrails and block re-proposals.

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Do not add a self-generated "prediction error" critique pass without an outside signal. Intrinsic self-correction does not beat plain sampling at equal calls. Confirms G2 (revise only from real output) and the 4b row on unstructured reflection | G2, 4b | [E] | d14, d15, d16; K20 |
| Any new loop operator is compared with self-consistency at equal calls and counted setup cost. Confirms G7 | G7 | [E] | d15, d16; K20 |
| Feedback quality decides repair gains; code-located failing output is the right feedback. Confirms G2 | G2, S5 | [E] | d16 (33.3% -> 52.6%), d14 |
| Do not import PC training or PC "layers of error passing" as a scaffold design. PC as a learning rule is a way to compute backprop at about 100x cost and fails past depth 5-7. Keep the number of correction hops small | none | [E] | b08, b09, b10, c05, c17; K01, K02, K05 |
| Record in 4b: "Brain-score alignment of LLM layers is not evidence for layered thinking." Brain-LLM fit may reflect transfer | 4b | [C] as a fact, [E] as a caution | b16, c11, K11 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| T1. Residual-only passing: revise from the located delta (failing output plus the one failing check) vs revise from the full draft and full critic text, at equal tokens | O (S5 REVISE) | [S] | K09, K21; a18, d16 |
| T2. Foresight reweighting as a step operator at S3/S5: sample k short lookaheads, score by code check, keep the best first step; vs best-of-N at equal tokens | O (S3 GENERATE) | [S] | K17; c10, d10, d11 |
| T3. Surprise-against-context check as a verify (S8) gate: score how unexpected the answer is given the stated problem context, and flag for a second code-checked attempt | G5/S8 | [S] | K15; c09, d12 |
| T4. Delta-only memory write: store a lesson only if the first attempt's outcome was not already predicted by existing lessons (write by prediction error) | memory | [S] | K19; c15 (inspiration only) |
| T5. Precision weighting: weight a class prior by how stable the class record has been | S0/memory | [S] | b04; K07 |
| T6. Multi-horizon planning: separate near (syntax-like, local) and far (semantic) lookahead at different abstraction levels | O3 decompose | [S] | K10, a21 (brain only; no task result) |
| T7. Multi-level critique (more than one level) vs one-level critique at equal tokens | S5 | [S] | K08, b05 |
| T8. Settle before update (prospective configuration): decide the full plan edit before committing any memory or state change | S5/memory | [S] | K18, b18 |

Rejected for testing: PC-trained models (not relevant to a prompt scaffold), laminar/cell-type mapping (neuroscience only).

## 8. Concrete tests on our bench

All arms at equal total tokens (setup included, G7). Use the bench harness; N at least 200 items per arm, with bootstrap 95% CIs, which Bhatt 2026 lacked.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 residual-only | ARC items and code-with-tests items that fail the first attempt (code-located failure available) | A: revise with full draft + full critic text. B: revise with delta only (failing input, expected vs actual output, the one failing check). C: plain resample at equal tokens | Pass rate on held-out check (G3); tokens per solve | B at least equal to A with fewer tokens; B above C by 2+ points. No prior study, so expect 0 to 3 points. Null is plausible (Olausson: feedback quality dominates) |
| T2 foresight | GSM8K-style and ARC-subset items with a code check | A: plain best-of-N. B: foresight reweighting with k lookaheads of 2-3 steps. C: self-consistency at same tokens | Accuracy | Edge over C small (Ma: about 0.4 points on a math row). Expect 0 to 2 points. Needs the foothold rule (G12) |
| T3 surprise gate | Problems with a stated context (BrainTeaser-type and multi-fact items) | A: no gate. B: surprise-against-context score gates a second attempt. C: random gate at the same trigger rate | Final accuracy; gate AUROC for wrong answers; extra tokens | AUROC above 0.75 on N>=500 with CI lower bound above 0.70. Bhatt's gain was 0.827 -> 0.867 in a detector on N=200, not a solver |
| T4 write-by-surprise memory | Sequences of 50+ items per class | A: store every lesson. B: store only lessons not predicted by existing ones. C: store none | Accuracy on later items of the same class; memory size | Same accuracy at 30-50% fewer entries; a gain is not expected |
| T5 precision weighting | Mixed-class streams | A: fixed prior from class record. B: prior weight scaled by past pass-rate variance. | Calibration of the gate; accuracy | Small; only worthwhile if the class record is noisy |
| T6 multi-horizon | Multi-step planning items (PDDL-style, AlfWorld-like) | A: single horizon. B: near plus far lookahead | Success rate | 0 to 3 points; weak support |
| T7 multi-level critique | Items with a hierarchical structure (code with function + module level tests) | A: critique at one level. B: critique at two levels in order | Pass rate | Expect null (Walsh: contiguous-level evidence scarce) |
| T8 settle-then-commit | Continual item stream with drift | A: update memory after each attempt. B: settle (re-check all lessons against the new case) before committing | Interference: accuracy on earlier classes after later ones | Fewer regressions; effect size unknown |

Control for the null baselines: report self-consistency at equal calls in every test (d15), and an oracle-check arm to show the ceiling (d14: oracle 95.5 vs 74.7 without).

## 9. What does not transfer, and why

- **The learning rule.** PC training is a way to get backprop gradients with local rules. We do not train. It costs about 100x and fails past depth 7. [K02, K05]
- **Neural evidence.** Expectation suppression, laminar data, error units, sharpening: all contested and none predicts an LLM-agent result. BOLD and single-unit data do not map to token streams. [K06, K07, K13]
- **Brain scores as support.** Brain-LLM alignment may be transfer. Layers do not map to cortical hierarchy. [K11, c11]
- **Precision as attention.** In brains, precision gates errors; in a scaffold, the equivalent is a code-set threshold. No evidence that a model can set its own precision (G10 says reasoning text is not evidence).
- **Free-energy-style self-critique.** Asking the model to predict its own error is intrinsic self-correction, which fails. [K20]
- **Hierarchy of error messages.** The multi-level claim is the least supported part of the theory, and deeper error chains degrade (energy ratio about 1e-6). [K08, K03]
- **Memory by PC.** DeltaNet-PC and tPC-RTRL are model-internal mechanisms. They do not map to a prompt-level memory. [K19]
- **Action-coupled generative models.** A real PC agent acts to confirm predictions; this is active inference and belongs to the neighbouring subfields.
- **Time scales.** Settling takes 100-200 iterations of small steps; LLM calls are coarse. Cheap "iterate until settled" has no analogue unless each iteration is a code check.

## 10. Open questions

1. Does delta-only revision beat full re-read at equal tokens? No study found. [gap 1]
2. Does foresight resampling beat equal-token best-of-N and self-consistency on non-verifiable tasks? The readable edge on math is about 0.4 points. [gap 2]
3. Does a surprise-against-context signal detect hallucinations at N well above 200, on a second benchmark, with CIs? [gap 3]
4. What do Rao and Ballard 1999 and Murray 2002 report in numbers? Primary texts unread. [gap 4]
5. Is there an independent replication of Kok 2012 sharpening? Does attention explain suppression, or can precision absorb it? [gap 5]
6. Is there a three-or-more-level language test (syntax, semantics, discourse)? Heilbron 2022 has no discourse level. [gap 6]
7. Any pre-registered replication of expectation suppression after 2021? Yan 2023 may be pre-registered; unconfirmed. [gap 7]
8. Do PC transformers scale past 100M parameters? Leaning no; no result. [gap 8]
9. Is a PC-style step, as a prompt operator, separable from plain self-refinement? [gap 9]
10. Which test separates forecast-specific from transfer-general brain alignment (Caucheteux vs Antonello and Huth)? [gap 10]
11. Do the 2023 self-correction nulls (GPT-3.5, GPT-4) hold for current models?
12. Whether Salvatori's iPC advantage in masked LM is a seed-convergence effect (10/10 vs 7/10) or a real perplexity gain.

## 11. Sources

[V] = opened and read this session or in the critique pass. [M] = snippet, abstract, or relayed through another source only.

**Reviews and process theory**
- [V] Millidge, Seth, Buckley (2022) Predictive coding: a theoretical and experimental review. https://arxiv.org/abs/2107.12979
- [V] Walsh, McGovern, Clark, O'Connell (2020) Evaluating the neurophysiological evidence for predictive processing. https://pmc.ncbi.nlm.nih.gov/articles/PMC7187369/
- [V] Bastos et al. (2012) Canonical microcircuits for predictive coding (first 100k of 187k chars). https://pmc.ncbi.nlm.nih.gov/articles/PMC3777738/
- [M] Feuerriegel, Vogels, Kovacs (2021) Evaluating the evidence for expectation suppression. https://pubmed.ncbi.nlm.nih.gov/33836212/
- [V] Alink and Blank (2021) Can expectation suppression be explained by reduced attention? https://www.biorxiv.org/content/10.1101/2020.06.19.154427.full
- [M] Keller and Mrsic-Flogel (2018) Predictive processing: a canonical cortical computation. https://pmc.ncbi.nlm.nih.gov/articles/PMC6400266/
- [V] Evaluating the compatibility of predictive coding as a model of linguistic predictability (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13623734/

**Founding works**
- [M] Mumford (1992) On the computational architecture of the neocortex II (via Millidge). https://arxiv.org/abs/2107.12979
- [M] Rao and Ballard (1999) Predictive coding in the visual cortex. https://www.nature.com/articles/nn0199_79 ; https://pubmed.ncbi.nlm.nih.gov/10195184/
- [M] Murray et al. (2002) Shape perception reduces activity in human primary visual cortex. https://pubmed.ncbi.nlm.nih.gov/12417754/
- [M] Murray et al. (2004) Perceptual grouping and the interactions between visual cortical areas. https://pubmed.ncbi.nlm.nih.gov/15288893/
- [M] Summerfield et al. (2008) (via Walsh 2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7187369/
- [M] Kaliukhovich and Vogels (2011) (via Walsh 2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7187369/
- [M] Kok, Jehee, de Lange (2012) Less is more. https://pubmed.ncbi.nlm.nih.gov/22841311/
- [M] Kok et al. (2016) 7T laminar fMRI of Kanizsa figures (via Walsh 2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7187369/

**Neuroscience tests**
- [V] Richter and de Lange (2019) Statistical learning attenuates visual activity only for attended stimuli. https://pmc.ncbi.nlm.nih.gov/articles/PMC6731093
- [V] Yan et al. (2023) Humans predict the forest, not the trees. https://pmc.ncbi.nlm.nih.gov/articles/PMC7614728
- [M] Rideaux et al. (2026) sharpening vs dampening (preprint). Europe PMC PPR1272011
- [V] Cross-domain probabilistic cueing study (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12441825/
- [M] Huang (2025) Feature selective inhibitory mechanisms. https://pmc.ncbi.nlm.nih.gov/articles/PMC12738544

**PC as a learning algorithm**
- [V] Whittington and Bogacz (2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC5467749/
- [M] Song et al. (2020) Can the brain do backpropagation? https://pubmed.ncbi.nlm.nih.gov/33840988/
- [V] Millidge, Tschantz, Buckley (2020) PC approximates backprop along arbitrary graphs. https://arxiv.org/abs/2006.04182
- [V] Millidge et al. (2020) Activation relaxation. https://arxiv.org/abs/2009.05359
- [V] Pinchetti et al. (2025) Benchmarking predictive coding networks, made simple. https://arxiv.org/abs/2407.01163
- [V] Salvatori et al. (2024) iPC. https://arxiv.org/abs/2212.00720
- [V] Pinchetti et al. (2022) Predictive coding beyond Gaussian distributions. https://arxiv.org/abs/2211.03481
- [V] Alonso, Krichmar, Neftci (2023). https://arxiv.org/abs/2305.13562 (skimmed)
- [V] Song et al. (2024) Prospective configuration. https://pmc.ncbi.nlm.nih.gov/articles/PMC7615830/
- [V] Innocenti, Achour, Buckley (2025) muPC. https://arxiv.org/abs/2505.13124
- [V] Goemaere et al. (2025) ePC. https://arxiv.org/abs/2505.20137
- [V] Salvatori et al. survey (2023-2025). https://arxiv.org/abs/2308.07870
- [V] van Zwol et al. tutorial. https://arxiv.org/abs/2407.04117
- [V] Innocenti (2025) thesis (abstract and intro). https://arxiv.org/abs/2510.23323
- [V] Lotter, Kreiman, Cox (2017) PredNet. https://arxiv.org/abs/1605.08104
- [V] Morrill, Zemel (2026) DeltaNet-PC. https://arxiv.org/abs/2610.15185
- [V] Potter, Rhodes (2026) tPC-RTRL (abstract only). https://arxiv.org/abs/2602.18131

**Language and brain**
- [V] Caucheteux, Gramfort, King (2023) Evidence of a predictive coding hierarchy. https://pmc.ncbi.nlm.nih.gov/articles/PMC10038805/ ; preprint https://arxiv.org/abs/2111.14232
- [V] Antonello and Huth (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11025645/ (re-confirmed in critique)
- [V] Heilbron et al. (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9371745/
- [M] Schrimpf et al. (2021). https://doi.org/10.1073/pnas.2105646118
- [V] Yang et al. (2026) cross-lingual alignment. https://arxiv.org/abs/2605.21049
- [V] Kolbl et al. (2025). https://arxiv.org/abs/2506.08511
- [V] Rao et al. (2025) Lessons from neuroscience for AI. https://arxiv.org/abs/2512.22568
- [V] Murphy (2024) Shadow of the (hierarchical) tree. https://arxiv.org/abs/2412.01276
- [M] Barenholtz (2025) blog essay. https://elanbarenholtz.substack.com/p/predicting-the-demise-of-predictive

**LLM and agent studies**
- [V] Bhatt (2026) PCIB. https://arxiv.org/abs/2601.15652
- [V] Xie (2026) LPC-SM. https://arxiv.org/abs/2604.03263
- [V] Ma et al. (2024) Predictive-Decoding. https://arxiv.org/abs/2410.17195
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Olausson et al. (2024) Is self-repair a silver bullet. https://arxiv.org/abs/2306.09896
- [V] arXiv search listing (2026-11-17). https://arxiv.org/search/?query=%22predictive+coding%22+%22language+model%22&searchtype=all

**Not reachable:** the journal pages of Heilbron 2022 (PNAS, HTTP 403) and Caucheteux 2023 (Nature, login) were not used; the PMC and arXiv versions were. The evidence file c01 stated "70 min of stories"; this is wrong (27 stories, 7-56 min, 4.6 h unique stimulus).
