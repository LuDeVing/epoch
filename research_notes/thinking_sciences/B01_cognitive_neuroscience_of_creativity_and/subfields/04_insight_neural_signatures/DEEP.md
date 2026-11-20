# Insight neural signatures: deep document

*Subfield B01.04. Scope: EEG alpha and gamma bursts before insight solutions, right-hemisphere and temporal activity. Key works: Bowden and Jung-Beeman 2003; Jung-Beeman et al. 2004; Kounios and Beeman 2009. Evidence ids (a01..d17) refer to evidence_a-d.jsonl; claim ids (K01..K20) to claims.jsonl in this folder. Verdict up front: this is background. A text model has no online neural signal, so almost nothing here is a direct add. The useful parts are the behavioural lessons and the LLM-side tests.*

## 1. What it is

Insight (the "Aha!" or Eureka moment) is a solution that arrives suddenly, after an impasse, with a feeling of certainty. In the lab it is defined by the solver's own report. After each correct solve the person presses "insight" or "no insight". There is no objective marker of insight in the problem or the answer.

The neural question is whether insight solutions have a distinct brain signature. The founding claim (Jung-Beeman et al. 2004) has three parts:
1. fMRI: more signal in right anterior superior temporal gyrus (RH aSTG) for insight solves.
2. EEG: a burst of gamma power (about 39 Hz) over right anterior temporal electrode T8, starting about 0.3 s before the button press, for insight solves only.
3. EEG: an earlier alpha increase over right parieto-occipital sites, read as gating visual input.

Around this core sit: a behavioural priming result (the right hemisphere holds weak solution activity before awareness), resting-state and pre-problem "prepared mind" differences, brain stimulation studies, and fMRI meta-analyses.

Why it matters for our agent: it does not matter directly. A model has no EEG, no hemispheres and no insight label with ground truth. What transfers is a set of design ideas (suddenness as a discontinuity, fixation, gating of distractors, monitoring as a separate step) and a warning (self-reported aha is a weak signal). The LLM literature on "aha moments" (section 6) is where testable claims live.

Status in one line: the founding numbers come from small samples (N=13 to 26), one lab, self-report labels and lenient statistics. No independent replication of the right-temporal gamma burst was found (K02).

## 2. History and theories in depth

**Gestalt and impasse (pre-1990s).** Insight problems are ones where the first representation is wrong. The solver reaches an impasse, restructures, and the answer appears whole. Ohlsson's constraint relaxation and representational change are the cognitive versions. The schema already uses them (O4, O6).

**Coarse semantic coding (Beeman).** The left hemisphere codes small, strong, fine semantic fields. The right hemisphere codes large, weak, overlapping coarse fields. Distant links need the coarse code. So the right hemisphere should hold weak solution activation that the left misses (a06).

**Behavioural root: Jung-Beeman and Bowden 2000; Bowden and Jung-Beeman 2003.** Solution words shown to the left visual field (right hemisphere) were primed. In 2003 (N=44, 7 s of effort, then naming, then insight rating 1-5), after unsolved problems the priming was 70 ms for left-visual-field/RH presentation versus 39 ms for right-visual-field/LH. The RH advantage was 33 ms, F(1,43)=4.4, p=.04. Priming was larger for solutions later rated insightful; correlation z' about .18 (lvf) vs .05 (rvf), t(39)=2.3, p<.03. The authors say both hemispheres contribute (d03, d04). Effects are 30-60 ms with p near .03-.05.

**Founding neuroimaging: Jung-Beeman et al. 2004 (PLoS Biol).** Exp 1 fMRI, Exp 2 EEG, both on compound remote associates (CRA). Numbers in section 3 (a01-a07, b01, b02, b25). The logic for gamma: sudden all-or-none emergence should show as a discrete high-frequency burst (a07).

**The prepared mind: Kounios et al. 2006, 2008.** The brain state before the problem appears predicts whether the next solution will be insight or analytic. EEG (N=19) and fMRI (N=25) in 2006; resting EEG with a median split (N=26) in 2008 (d01, d02, a08-a10). Insight is partly a trait and partly a pre-problem state. Kounios 2006 itself said its gamma effects could not be separated from muscle (EMG) artifact (d01). This is the earliest admission that scalp gamma is fragile.

**Competing decomposition: Sandkuhler and Bhattacharya 2008.** Independent lab, CRA with hints. They split "insight" into impasse, restructuring and suddenness. Gamma (38-44 Hz) appeared over parieto-occipital sites, tied to impasse and attention overload, not right temporal. Alpha was read as suppression of weak solution information (a13-a15, b03, b04).

**fMRI diversification (2009-2020).** Subramaniam 2009 (anagrams, N=10): right insula, left BA45, angular gyri, ACC, right PFC, plus right temporal pole (a11, a12). Tik 2018 (7 T, N=29): left anterior middle temporal gyrus plus thalamus, hippocampus and dopaminergic midbrain (b08). Becker 2020 (N=30): early bilateral anterior insula activity predicts later Aha (b09). Ogawa 2025 (spatial matchsticks, N=16): default mode network for insight (a18). Meta-analyses find frontal, parahippocampal and amygdala regions, with task-type dependence (a20, b13, b14).

**Stimulation (2011-2024).** Chi and Snyder 2011 positive; Salvi 2020 positive; Santarnecchi 2019 gamma tACS positive; Aihara 2017 null (b05-b07, d05-d07). Ghani 2024 real-time EEG gating (d08).

**Theory since 2020.** Kim 2026 reads the data as precision reweighting in predictive processing (alpha down, gamma up, ACC surprise) (a22). Salvi 2026 finds left dorsal white-matter tracts relate to insight-style solving (a21, b17). Recent work treats the Aha rating as a metacognitive judgment that follows correctness and mindset (d15, d16).

**Net trajectory.** From "the right temporal lobe does insight" (2004) to "insight engages monitoring, salience, memory and frontal control, with task-specific patterns, and the Aha label is itself a judgment" (2018-2026). The original hemisphere claim is weakened, not refuted.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| About 56% of correct CRA/anagram solves are labelled insight | Jung-Beeman Exp1 N=13: 56% (SD 18.2) insight, 41% no, 2% other; Exp2 N=19: 56% vs 42%, t(18)=3.47, p=.003; Kounios 2006: 56.2% (SD 8.3) and 55.8% (SD 13.9); anagrams N=26: 56.1% (SD 19.2); 2024 EEG N=21: 55.6% | a01, b01, b02, d01, d02, a08, a16 | Established (3 independent designs) |
| Eureka also reported on wrong answers | 22.7% (SD 16.4) of incorrect trials, 2024 EEG | a16 (critique correction 3) | Single-source |
| fMRI: RH aSTG more active for insight | Peak diff 0.25% (6 s window), 0.30% at one TR; cluster 531 mm3, peak t=4.89 at (44,-9,-9); 12 of 13 subjects positive (0.03-0.35%); problem-onset cluster 469 mm3, t=4.37 | Jung-Beeman 2004 Exp1 (a02, b01) | Contested (not replicated as right-only) |
| fMRI secondary effects | left medial frontal 453 mm3 (0.15%); amygdala/parahippocampal 0.16%; IFG 0.21% at lenient p<.015; two foci had signal at only 72% and 83% of brain average | a03, b25 | Weak |
| EEG gamma burst, right temporal T8 | 39 Hz, window -0.30 to -0.02 s: t(18)=3.48, p=.003; window x hemisphere x insight F(1,18)=8.11, p=.011; none at -1.52 to -0.36 s; none at left T7; RT 9.94 vs 9.25 s | a04, b02 | Single-source (no independent replication) |
| EEG alpha before the burst | 9.8 Hz right parieto-occipital, -1.31 to -0.56 s window; paper text says onset about 1.4 s before solution; theta, beta null; 4 Hz frontal effect possibly eye movement | a05, b25 | Contested (direction differs elsewhere) |
| Behavioural RH priming | N=44; 70 vs 39 ms; advantage 33 ms, F(1,43)=4.4, p=.04 | Bowden and Jung-Beeman 2003 (d03) | Single-source |
| Pre-problem state predicts solution type | EEG N=19, 186 CRA, solved 46.2%: insight prep had less 9-10 Hz alpha mid-frontal; fMRI N=25, 135 CRA, 47%: more ACC, PCC, bilateral posterior temporal before insight; gamma not reported (EMG) | Kounios 2006 (d01, d02) | Single-source (same lab) |
| Resting EEG differs by insight style | N=26 (13 per group); HI ratio 3.5 (SD 2.3) vs LI 0.8 (SD 0.4); Beta-1 F(3,72)=7.011, p<.001; high-alpha F(3,72)=4.811, p=.004; equal accuracy 68.9 vs 70.9%, RT 5.19 vs 5.10 s; errors 3.7 vs 4.9%; timeouts 27.4 vs 25.2% | Kounios 2008 (a08-a10) | Single-source |
| Independent EEG: parieto-occipital gamma, sudden vs non-sudden | N=21; 302 vs 88 trials; gamma 38-44 Hz; suddenness vs restructuring rho=-0.39, t(18)=-5.17; 55.6% of hint-free solves high suddenness and low restructuring; 23.3% high on both | Sandkuhler 2008 (a13-a15, b03) | Contested (different site and timing) |
| Partial EEG replication, left temporal | N=21; accuracy 57.4%; RT 8.4 s; alpha cluster left central/temporal -1.96 to -1.55 s, 13 electrodes, sum(t)=1174, p corr=.01; association strength vs accuracy beta=.11, t(20)=12.04 | 2024 HBM (a16, a17, b10) | Contested (left, not right) |
| Perceptual Eureka EEG: no gamma difference | N=25, cluster-corrected; alpha/theta coherence mostly right hemisphere; gamma and theta power no difference | 2023 Cereb Cortex (d09) | Boundary result (not verbal) |
| fMRI left temporal, 7 T | N=29; left anterior MTG, thalamus, hippocampus, VTA, accumbens | Tik 2018 (b08) | Single-source |
| Anagram fMRI | N=10 usable; ACC 1,513 voxels t=6.08; right PFC 534 voxels t=4.77; temporal pole 164 voxels t=4.57; insula 333 voxels t=3.81 | Subramaniam 2009 (a11) | Single-source |
| Early insula predicts later Aha | N=30 plus 26 eye-tracking control | Becker 2020 (b09) | Single-source |
| Spatial insight fMRI | N=16; 2,780 trials: quick 1,686, analytical 735, insight 134; RT 8.61, 36.58, 114.44 s; hit rate 97.9, 96.7, 78.6%; uncorrected p=.001 | Ogawa 2025 (a18) | Weak |
| Meta-analysis of fMRI | 27 divergent-thinking and 30 insight studies; insight: IFG, MFG, parahippocampal, amygdala, precentral, superior parietal; no conjunction with DT | 2022 HBM (a20) | Single-source (abstract-level) |
| Left dorsal white matter relates to insight style | N=38; FA composites significant after FDR; MD p=.032, q=.081 | Salvi 2026 (a21, b17) | Single-source |
| tDCS right ATL helps | Chi and Snyder 2011: hardest matchstick 20% sham vs 60% L-minus/R-plus, Fisher p=.022, logrank p=.008, about 20 per group; Salvi 2020: 3 groups of 36, F(2,107)=3.64, p=.03, partial eta2=.064 | b06, d06 | Contested |
| tDCS right ATL null | Aihara 2017 N=66: RAT 7.34 vs 7.75, p=.43, g=-0.19 (CI -0.69 to 0.30); hard matchstick had 3 solvers | d05, a19 | Contested (underpowered) |
| Gamma tACS (40 Hz) | N=31; sham 8.25 correct (55%), 63% by insight; 40 Hz vs sham t(30)=3.54; CRA-specific t(30)=5.98; rebus t(30)=0.49; some p values inconsistent | Santarnecchi 2019 (d07) | Single-source |
| Alpha-gated hints | n=17 per condition; hints at high right-temporal alpha gave more insight reports (M=27.11); frequency x session F(1,32)=4.87, p=.035 | Ghani 2024 (d08) | Single-source |
| Aha label tracks correctness and style | N=377; Aha highest when first move correct; labels vary 8-14 SD points between people | d14, d15, d16 | Single-source |
| LLM mid-trace shifts rare and unhelpful | 6.31% of 1M+ traces; Qwen2.5-1.5B 2.57% correct with shift vs 16.44% without (N=723,200); strict detector 1.79% | arXiv 2601.00514 (c01, a23) | Single-source |
| Forced reconsideration under high entropy | MATH-500 32.21 to 40.62% (+8.41 pp; 50,574 vs 23,500 wins/losses); crosswords +0.45 pp; Rush Hour +0.01 pp; sign flips by model (+5.97 vs -4.19 pp) | c03, d11 | Single-source |
| Decoys fixate LLMs | GPT-4 on Only Connect: 6 walls original, 59 decoys diluted, 471 decoys removed (494 test walls) | b21, c14 | Established |
| Over-inventive reasoning on literal riddles | LLMs 84.9% genuine vs 50.7% literal riddle-riddles; humans 50.5% vs 80.5%; 90.8% of LLM errors inventive | d12 | Single-source |

## 4. Mechanisms and models

An engineer cannot implement the brain mechanisms. They can implement the functional analogues below. Each is a model of the human data, not a proven mechanism.

**M1. Coarse versus fine retrieval (Beeman).** Two retrieval modes over the same store: narrow (top-k strong neighbours) and broad (many weak neighbours, overlap counted). Insight is the broad mode finding the intersection of weak fields. Implementation: for a remote-associate item, take the three cue words, get a broad neighbour set for each (embedding or free-association graph), and rank candidates by how many cue fields they fall into. A heuristic search model over a free-association network matches human RAT accuracy, Pearson r=0.742 over 138 items (c20). This supports an associative-search account with no hemisphere-specific part.

**M2. All-or-none emergence.** The solution appears whole, not as partial outputs (Smith and Kounios 1996, quoted in a07). Model: confidence over candidate answers stays flat, then one candidate jumps. Implementation test: log per-step answer probability or entropy and look for a late discontinuity. Caution: in LLM math traces the nearest evidence says the opposite. Correct traces have smooth falling entropy; incorrect ones have unresolved spikes (d10, K18). So the analogue is unproven.

**M3. Gating of distraction (alpha story).** Jung-Beeman: alpha up over visual cortex gates input so weak associations can grow. Ghani 2024: hints delivered at high right-temporal alpha produced more insight reports (d08). Sandkuhler: alpha up in right temporal suppresses weak solution information, a different reading (a15). Kim 2026 reads alpha down (a22). Direction is unstable. Implementation analogue, if any: a step that blocks new context while an association develops. No test exists.

**M4. Impasse as attention overload.** Sandkuhler: parieto-occipital gamma at impasse reflects over-focus on one representation; right parieto-occipital gamma was higher before the hint for impasse ending in timeout than for impasse ending in a solution (a14). Analogue: after repeated failure, force a representation change (schema S6, O6). Already in the schema.

**M5. Evaluation and monitoring as a separate step.** ACC and insula activity (a11, b09) is read as detecting a good solution. Early insula activity predicts later Aha (b09). Analogue: generation and "is this right?" are separate processes, which matches the LLM result that verification fails more than generation on riddles (c05, K12).

**M6. Prepared mind / trait.** Pre-problem or resting state sets insight versus analytic style (d01, a08). HI and LI solved equally well; HI had more omissions (timeouts), LI more commission errors (a09). Analogue: the model or prompt default (broad versus focused sampling) sets which problems get solved; sampling spread matters (lowering spread cut distinct words from 296 to 97, c17).

**M7. Predictive-processing view (Kim 2026).** Insight is a drop in prior precision after repeated prediction failure. Analogue: lower weight on the dominant first reading after failed checks. No data; theory only (a22).

**Aha as judgment (d15).** The Aha rating is a judgment made after the fact. It rises with a correct first move and with mindset. So "insight" in humans is not a clean mechanism label, and an LLM analogue built on self-reported aha inherits the same problem.

## 5. What holds up

**Holds up (with caveats)**
- The behavioural rate: about 56% of correct solves labelled insight across three independent designs (K01).
- Insight solves are not faster or more accurate in the founding data (RT 9.94 vs 9.25 s; accuracy equal in HI and LI). But correctness and style shape the label (d15).
- Pre-problem and resting differences by style: same lab, converging EEG and fMRI, never independently replicated (single-source).
- Insight involves more than one temporal region. Frontal, medial temporal, ACC, insula and default-mode regions recur across tasks (a11, a18, a20, b09).

**Does not hold up, or is unconfirmed**
- Right-temporal gamma burst: one lab, N=19, one planned test at one electrode pair. No independent replication. Kounios 2006 could not separate gamma from EMG (d01). The 2024 EEG found left, not right (a16). The 2023 perceptual study found no gamma difference with cluster correction (d09). Sandkuhler found gamma at a different site and time (parieto-occipital, about -1.5 to -1 s).
- Right-only locus: contradicted by Tik 2018 (left), the 2024 EEG (left), Salvi 2026 (left white matter), the meta-analyses (frontal, medial temporal), and Subramaniam 2009 (temporal pole present, but deactivated by search).
- Alpha: increase over right posterior (Jung-Beeman) vs increase in right temporal read as suppression (Sandkuhler) vs left central/temporal cluster (2024) vs decrease (Kim 2026 theory).
- tDCS: Chi and Snyder 2011 (about 20 per group) and Salvi 2020 (36 per group) positive; Aihara 2017 (N=66) null with CI -0.69 to 0.30, so a small positive effect is not excluded, and the hard problem had 3 solvers. Inconclusive, not absent. The positive studies are not independent of the founding framework.

**Moderators**
- Task type: verbal CRA, anagrams, matchsticks, riddles and perceptual tasks give different regions (a18, a20, b14).
- Hints and impasse design change the signature (Sandkuhler).
- Insight trial counts are small (about 30 per person in the 2024 EEG; 134 trials in 16 people in Ogawa).
- Statistics: lenient thresholds (IFG p<.015), uncorrected topographic t-maps (Kounios 2008), median splits.

**Interventions in humans**: tDCS and tACS (mixed, above); hint timing by alpha (d08); REM sleep reshaped semantic networks but did not raise solving success (b19). None is usable for an agent.

**Source hygiene.** Duplicate evidence lines count as one source (critique correction 4). Seen only as snippets, not citable for numbers: a25-a28, b11-b15, c13, c23-c26. Kounios and Beeman 2009 could not be retrieved (d17); it is a review of the same primaries.

## 6. Language models

No LLM paper was found that tests an EEG-style or hemisphere signature of insight (K08, c13; search limited by the shared budget). The bridge is analogy only: suddenness, fixation, verification.

**Mid-trace "aha" shifts.** d'Aliberti and Horta Ribeiro 2026 (arXiv 2601.00514; 1M+ traces, hundreds of GRPO checkpoints, three domains; Qwen2.5 and Llama only). Shifts occurred in 6.31% of traces (Qwen2.5-1.5B about 7.6%). They did not grow with training. Qwen-1.5B pooled accuracy was 2.57% with a shift vs 16.44% without (N=723,200). A strict detector (prior failure, stability, gain) fires on 1.79%. Math average marginal effect -0.0615 (p=1.55e-4). Crosswords 0.201 vs 0.096 with a shift, but regression p=0.26. Judge kappa about 0.726 (0.79 against human majority). Entropy odds ratio for shifts: crosswords 2.05, Rush Hour 1.19, math 0.58. The authors limit results to tasks with well-defined correctness and a few families (c01-c04, d11).

**Forcing reconsideration.** The cue "Wait, we need to reconsider" under high entropy: MATH-500 32.21 to 40.62% (+8.41 pp, 50,574 wins vs 23,500 losses), crosswords +0.45 pp, Rush Hour +0.01 pp. On a MATH subset it gave +5.97 pp for Qwen2.5-7B and -4.19 pp for Llama 3.1-8B (c03, d11). Gain depends on model and domain. Not tested on insight items.

**Aha as decoration.** Under 10% of VLM responses show aha, with marginal gain; majority vote was steadier (+4.5%); self-verified best-of-N was sometimes down by up to 16.7% (c10). Base models such as DeepSeek-V3-Base already say "aha" and "wait" before RL, and in R1-Zero self-reflection is not linked to higher accuracy (c09). Over 30% of Kimi-K2.6 steps and nearly 60% of Qwen3.6-35B steps on one benchmark are decorative (true thinking score under 0.005). Removing the 50% lowest-score steps kept accuracy; self-training on pruned traces cut length 66% with no drop (c11). Distilled "aha" models differ by style (first-person tone), confounded by training data (c07). The R1-Zero visual replication (Qwen2-VL-2B, 59.47% on CVBench, about +30% over base and about +2% over SFT) counts reflection words and length as aha (b24, c12).

**Entropy and correctness.** Correct math traces show smooth falling entropy; incorrect ones show unresolved spikes. Choosing the smoothest of sampled traces raised accuracy (up to 32% relative; +33% AIME2025, +4% BRUMO, +25% HMMT, +3% Minerva as printed; non-math relative gains 5-13%). This is selection among samples, so compute is not matched to one sample (d10).

**Fixation on decoys.** GPT-4 on Only Connect walls: 6 of 494 on the original set, 59 with decoys diluted, 471 with decoys removed; best few-shot connection F1 41-45% vs human about 80% (b21, c14). Visual RAT (155 puzzles): humans 22.8% within three tries; one of 11 VLMs beat them (Claude-Opus-5.5 at 32.5%, as printed), no other above 12.5%; models echoed literal image content in 22.8% of wrong answers vs 8.9% for humans; models never abstain. Giving cues as text lifted every model 30.0 to 66.3 points (text-only Claude-Opus-5.5 90.0%), so the bottleneck is finding the concepts, not associating them (c18, c19, b22).

**Verification versus generation.** NazoNazo (201 Japanese riddles, 38 models): non-reasoning 7.6%, reasoning 17.6%, human mean 52.9% (n=126). Verification failures are 5-39% of wrong answers. The paper only proposes structured verification (c05, d13).

**Over-inventive reasoning.** Riddle Riddle: LLMs 84.9% on genuine riddles vs 50.7% on literal ones; humans 50.5% vs 80.5%; 90.8% of LLM errors on literal ones were over-inventive (d12). A reframing step can hurt when the literal reading is right.

**Semantic distance tests.** RAT validity against creative-writing benchmarks r=+0.62, +0.44, +0.51 across 55 models falls to +0.08 to +0.28 after controlling for general ability; DAT vs Hivemind r=+0.30 falls to -0.01 (c16, b20).

**Replaying key conclusions.** Insight Replay (re-inserting key intermediate conclusions, 3 rounds): +1.65 points average over CoT across 24 settings; largest +9.2 on R1-Distill-32B LiveCodeBench v5. The paper's "insight" is not the neuroscience concept (c21).

**Summary of what changed behaviour, by how much.** Removing decoys: 6 to 471 solved walls. Forced reconsideration under high entropy: +8.41 pp on math, about 0 on puzzles, negative for Llama. Text instead of image cues: +30 to +66 points. Replay: +1.65 average. Self-verification: unreliable, sometimes -16.7%.

**Caveats.** Many 2025-2026 numbers are preprints. Judges are LLMs (kappa about 0.73). Models tested are small and RL-tuned.

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Do not treat a mid-trace "aha" or reflection phrase as a success signal. Decide from code checks. G10 already says this; add the aha-specific example. | G10 | [E] | c01, c09, c10, c11 (K09, K11) |
| A2 | Do not let the model's own stuck or insight report fire S6. Keep the code-fired impasse detector. | G1, S6 | [E] | K09, K11, a23 |
| A3 | Decoys fixate models (the fixation is established). Keep any surface-feature-removal remedy inside S6 or open mode only; the remedy itself is a test (T1). | S6 (O6, O8) | [E] fixation, [S] remedy | b21, c14, c18 (K13) |
| A4 | Do not build a hemisphere, alpha or gamma module. Nothing in the neural data is implementable and the locus is contested. | none | [E] | K04, K05, a19 |
| A5 | Do not use RAT or semantic-distance scores as creativity proxies. Consistent with G8. | G8 | [S] on LLM data | c16, b20 (K14) |

A1, A2 and A4 already agree with SCHEMA.md G1, G10 and section 4b. The only text change worth making is one sentence of evidence under G10.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Decoy-listing step (list the surface features driving the current answer, then require an answer avoiding them), gated behind a failed literal attempt. | S6 (O6, O8) | [S] | b21, c14, d12 (K13, K20) |
| T2 | Entropy-gated forced reconsideration (cue only when token entropy or attempt disagreement is high). | S5, S6 | [S] | c03, d11 (K10, K19) |
| T3 | Independent checker model for riddle-type answers. | S8, G5 | [S] | c05, d13 (K12) |
| T4 | Late-spike or smoothness signal of per-step entropy as a correctness predictor on RAT and riddle items. | S7 (selection by code) | [C] | d10 (K18) |
| T5 | Association-graph search for remote-associate items. | S3 (new operator) | [S] | c20, a17 (K16) |
| T6 | Replay of stored key conclusions at the final-answer step. | memory, S8 | [S] | c21 (K15) |
| T7 | Pruning low-contribution steps to save tokens. | G11 | [E] that steps are often decorative, [S] for the remedy | c11 (K11) |
| T8 | Broad versus focused sampling spread by problem class (trait analogue). | S0, S3 | [S] | a09, c17 (K07) |

## 8. Concrete tests on our bench

All tests compare arms at equal total tokens, setup cost included (G7). Use at least 3 seeds. Plain and best-of-N are always arms.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Only Connect walls, RAT and riddles with decoys; control: literal-answer riddle-riddles | plain; best-of-N; plain + always-on decoy step; plain + decoy step after a failed literal attempt | accuracy; accuracy on literal controls (harm) | Gated arm gains on decoy items and loses nothing on controls. Always-on arm loses on controls (d12: 90.8% of errors over-inventive). |
| T2 | RAT, matchsticks, riddles (insight-type) with MATH-500 as anchor | never-trigger; always-trigger; entropy-gated; best-of-N | accuracy at equal tokens; win/loss counts | About +5 pp on the math anchor for Qwen-like models (c03); about 0 on puzzles; possibly negative for Llama-like models (d11). |
| T3 | Riddle-type items (NazoNazo-style or English riddles) | plain; self-check; independent checker model; vote | accuracy; verification-failure share of wrong answers | Checker lowers the 5-39% verification-failure share. Size unknown. |
| T4 | RAT with 5 or more samples per item | per-step entropy logs vs self-consistency | AUC of spike/smoothness for correctness vs AUC of agreement | If AUC is not above agreement, drop. Prior is negative (d10). |
| T5 | Compound RAT (138-item style) | free generation; association-graph candidate list then model picks; best-of-N | accuracy | Graph arm helps small models; humans' agreement was r=0.742. |
| T6 | Multi-step reasoning with long traces (LiveCodeBench-like) | plain CoT; replay at final answer | accuracy | About +1.65 points, as in c21. |
| T7 | Any CoT set | full trace; trace with the 50% lowest-contribution steps removed | accuracy at lower tokens | Same accuracy at fewer tokens (c11). |
| T8 | Mixed insight and analytic items | narrow sampling; broad sampling; mixed | accuracy by item class | Broad helps remote items, hurts routine ones; spread matters (c17). |

Also a free measurement: count self-reported mid-trace shifts in our agent's traces and compare accuracy with and without a shift (K09).

## 9. What does not transfer, and why

- EEG alpha and gamma, hemispheres and brain regions. A transformer has no sensor, hemisphere or gamma band. Entropy and attention are not oscillations.
- The Aha label itself. Humans give a post-solution report that tracks correctness, mindset and slowness (d14-d16). A model's "aha" text is a style artefact (c07, c09). A human-style insight rating cannot be the target.
- Resting and pre-problem state. A fresh prompt has no resting state. The only analogue is the prompt prefix or sampling setting.
- tDCS and tACS. No stimulation analogue.
- Timing (0.3 s before the press). Token position is not time, and the burst timing was never independently replicated.
- Human numbers as targets. The 56% insight rate is a label rate, not a solve rate, and is not ground truth for models.
- Small RL-tuned model results (2601.00514) may not hold in closed or frontier models.
- Sleep and incubation. Incubation by distraction already sits in section 4b as not working; REM changed semantic networks without raising success (b19).

## 10. Open questions

1. Is there any independent replication (other lab, N over 30, corrected statistics) of the right-temporal gamma burst? None found.
2. Do LLM traces show a sharp confidence or entropy jump before correct answers on RAT or riddles? The nearest evidence says no (smooth for correct, spikes for wrong), but it is math only.
3. Do rare shifts and entropy-gated reconsideration hold in larger or closed models and on insight-type items? The sign flipped between Qwen and Llama.
4. Does a decoy-listing step beat best-of-N at equal tokens?
5. How much of the 55-56% insight rate is problem difficulty or solving style? Between-subject SDs of 8-14 points show style matters; no quantitative split exists.
6. Do riddle verification failures come from checking or from generation? Would an independent checker fix them?
7. Are the tDCS nulls absence or low power? Aihara g=-0.19 (CI -0.69 to 0.30) does not exclude a small effect.
8. Does the Sheth critique (post-solution gamma stronger) hold? Seen only in a snippet.
9. What do Kounios and Beeman 2009 add beyond the primaries? Not retrieved.

## 11. Sources

[V] opened and read this session; [M] snippet or abstract only.

- [V] Jung-Beeman et al. 2004, PLoS Biol. https://pmc.ncbi.nlm.nih.gov/articles/PMC387268/ (a01-a07, b01, b02, b25; re-opened in critique)
- [V] Bowden and Jung-Beeman 2003, Psychon Bull Rev. https://link.springer.com/content/pdf/10.3758/BF03196539.pdf (d03)
- [V] Jung-Beeman and Bowden 2000. https://link.springer.com/content/pdf/10.3758/BF03211823.pdf (d04; sample sizes not extracted)
- [V] Kounios et al. 2006, The prepared mind (NBER conference copy). https://conference.nber.org/confer/2006/ICCs06/kounios.pdf (d01, d02, d14)
- [V] Kounios et al. 2008, Neuropsychologia. https://pmc.ncbi.nlm.nih.gov/articles/PMC2293274/ (a08-a10)
- [M] Kounios and Beeman 2009, Curr Dir Psychol Sci. https://journals.sagepub.com/doi/10.1111/j.1467-8721.2009.01629.x (a28, d17; not retrieved)
- [V] Sandkuhler and Bhattacharya 2008, PLoS ONE. https://pmc.ncbi.nlm.nih.gov/articles/PMC2180197/ (a13-a15, b03, b04)
- [V] Subramaniam et al. 2009, Hum Brain Mapp. https://pmc.ncbi.nlm.nih.gov/articles/PMC6870806/ (a11, a12)
- [V] 2024 Hum Brain Mapp EEG, creative problem-solving with insight or remote thinking. https://pmc.ncbi.nlm.nih.gov/articles/PMC10789201/ (a16, a17, b10)
- [V] Tik et al. 2018, 7 T fMRI. https://pmc.ncbi.nlm.nih.gov/articles/PMC6055807/ (b08)
- [V] Becker et al. 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7267914/ (b09)
- [V] Ogawa, Aihara and Yamashita 2025, Sci Rep. https://pmc.ncbi.nlm.nih.gov/articles/PMC12318010/ (a18, b16)
- [V] Aihara et al. 2017, PLoS ONE. https://pmc.ncbi.nlm.nih.gov/articles/PMC5597234/ (a19, b05, d05)
- [V] Chi and Snyder 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3032738/ (b06)
- [V] Salvi et al. 2020, Sci Rep. https://pmc.ncbi.nlm.nih.gov/articles/PMC6976642/ (b07, d06)
- [V] Santarnecchi et al. 2019, gamma tACS. https://pmc.ncbi.nlm.nih.gov/articles/PMC6453961/ (d07)
- [V] Ghani et al. 2024, real-time alpha gating. https://bura.brunel.ac.uk/bitstream/2438/27819/4/FullText.pdf (d08)
- [V] 2023 Cerebral Cortex, Dynamic signatures of the Eureka effect. https://pmc.ncbi.nlm.nih.gov/articles/PMC10321100/ (d09)
- [V] 2022 Hum Brain Mapp fMRI meta-analysis, divergent thinking and insight. https://pmc.ncbi.nlm.nih.gov/articles/PMC9582370/ (a20; abstract and results summary only)
- [M] Dietrich and Kanso 2010. https://pubmed.ncbi.nlm.nih.gov/20804237/ (b11)
- [M] Mihov, Denzler and Forster 2010. https://doi.org/10.1016/j.bandc.2009.12.007 (b12)
- [M] 2018 meta-analysis, neurodynamics of insight. https://doi.org/10.1016/j.biopsycho.2018.08.018 (b13)
- [M] 2016 meta-analysis, is insight task-specific. https://doi.org/10.1016/j.ijpsycho.2016.10.001 (b14)
- [V] Salvi et al. 2026, white matter of Aha moments. https://pmc.ncbi.nlm.nih.gov/articles/PMC12866244/ (a21, b17)
- [V] Kim 2026, Illumination Onset. https://pmc.ncbi.nlm.nih.gov/articles/PMC13701766/ (a22, b18)
- [V] REM and restructuring, Commun Biol 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13542217/ (b19)
- [V] Aha ratings as metacognitive judgments, J Intell 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13608503/ (d15)
- [V] Comparing Aha moments in problem solving and ideation, J Intell 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13514830/ (d16)
- [V] d'Aliberti and Horta Ribeiro 2026, Illusion of Insight. https://arxiv.org/abs/2601.00514 (a23, b23, c01-c04, d11)
- [V] Wu et al. 2025, Aha Moment Revisited. https://arxiv.org/abs/2506.17417 (a24, c10)
- [V] Zhou et al. 2025, R1-Zero's Aha Moment in Visual Reasoning. https://arxiv.org/abs/2503.05132 (b24, c12)
- [V] Zhou et al. 2025, Understanding Aha Moments. https://arxiv.org/abs/2504.02956 (c07, c08)
- [V] Liu et al. 2025, Understanding R1-Zero-Like Training. https://arxiv.org/abs/2503.20783 (c09)
- [V] Zhao, Sun et al. 2026, Can Aha Moments be Fake. https://arxiv.org/abs/2510.24941 (c11)
- [V] NazoNazo benchmark 2025. https://arxiv.org/abs/2509.14704 (c05, c06, d13)
- [V] Samuel et al. 2023, Only Connect red herrings. https://arxiv.org/abs/2306.11167 (b21, c14, c15, c22)
- [V] CREATE visual RAT 2026. https://arxiv.org/abs/2610.18569 (b22, c18, c19)
- [V] Semantic distance tests and LLM creativity 2026. https://arxiv.org/abs/2605.13450 (b20, c16, c17)
- [V] Valba et al. 2020, free association network and RAT. https://arxiv.org/abs/2008.12219 (c20)
- [V] Lei et al. 2026, Stateful Reasoning via Insight Replay. https://arxiv.org/abs/2605.14457 (c21)
- [V] Gwak, Son and Kim 2026, Uniform Information Density in LLM reasoning. https://arxiv.org/pdf/2510.06953 (d10)
- [V] Fascendini et al. 2026, The Riddle Riddle. https://arxiv.org/pdf/2606.27103 (d12)
- [M] arXiv search listing of aha-moment papers (Reasoning Theater 2603.05488, EvolMathEval 2508.13003 and others). https://arxiv.org/search/?query=%22aha+moment%22+reasoning+models&searchtype=all&size=25 (a25)
- [M] EvoThink 2607.19962 (c24); From Aha Moments to Controllable Thinking 2508.04460 (c25); Geometric Interleaved Reasoning 2603.01070 (c26). https://arxiv.org/abs/2607.19962
- [M] Hofstadter and Mitchell, Copycat and Metacat (c23).
- [M] Sheth critique (post-solution gamma stronger): seen only in a search snippet; not cited for numbers.
