# Network neuroscience of creative cognition: deep document

*Subfield B01.01. Evidence: evidence_a-d.jsonl (a01-a29, b01-b25, c01-c27, d01-d17), claims K01-K28, critique.md. Written 2026-11-03. Sample sizes are given everywhere because most brain results here come from very small studies.*

## 1. What it is

Network neuroscience of creative cognition asks which large brain networks work together when people produce new ideas. Three networks matter.

- **Default network (DMN).** Medial prefrontal cortex, posterior cingulate, precuneus, inferior parietal. It supports memory, self-generated thought and association.
- **Executive control network (ECN, also called frontoparietal).** Dorsolateral prefrontal cortex, inferior parietal. It holds goals, selects, and suppresses.
- **Salience network (SN).** Anterior insula and anterior cingulate. It detects what matters and is thought to switch between the other two.

The main claim, from Beaty, Seli and Schacter (2019, a18, b01): creative thought is not a default-network event. The default and control networks, which normally work against each other, work together. The review ties this to three mental operations: goal-directed memory retrieval, suppression of the obvious (prepotent) answer, and internally focused attention.

Why it matters to us. It gives a human-science reason for a two-phase agent: a loose generation phase, then a control phase. It also names specific control operations we could copy: retrieve on purpose, suppress the first answer, and shield attention from the outside. The evidence is mostly correlational, mostly small-sample, and says nothing direct about language models. We treat it as background that suggests tests, not as proof of any design.

## 2. History and theories in depth

**Before 2010: defocus and frontal views.** Early theory said creativity needs "defocused" attention and low frontal control. Dietrich and Kanso (2010, a23, abstract level) reviewed 72 experiments in 63 articles and found no reliable change beyond diffuse prefrontal activity. Creative thinking was tied to no single region or process, and not to defocused attention. This is the standing sceptical baseline (K21).

**2012: generation versus evaluation.** Ellamil, Dobson, Beeman and Christoff (a12, abstract only) alternated generating and evaluating book-cover designs. Generation recruited medial temporal lobe. Evaluation recruited executive and default regions together, plus rostrolateral prefrontal cortex, insula and temporopolar cortex. So the simple map "default = generate, control = evaluate" was already shaky.

**2014: rest and recall.** Two studies set the frame.
- Beaty et al. (2014, a06, b10): at rest, high divergent thinkers (n=12) had stronger coupling than low (n=12) between left inferior frontal gyrus and the default network. Groups were the top and bottom third of 91 people, matched on IQ, openness, age and gender.
- Benedek et al. (2014, a07, a08): people said ideas aloud in the scanner and labelled each as recalled or new. Recalled ideas came first and were faster. New ideas came later and were rated more creative. Divergent thinking activated left inferior frontal gyrus and right hippocampus and deactivated default regions (right TPJ, precuneus, PCC). This is the "controlled internal retrieval" reading, not "default drives generation".

**2015: cooperation during the task.** Beaty, Benedek, Kaufman and Silvia (a01-a05, b09): 25 people did the Alternate Uses Task (AUT) versus an object-characteristics control, 12 s per trial. Default hubs (PCC, precuneus, inferior parietal), executive hubs (right DLPFC) and salience hubs (ACC, insula) formed one connected network. At rest, in a separate sample of 42, the same hubs were anticorrelated. So the cooperation is task-dependent. Early windows showed PCC coupled with insula; later windows showed PCC coupled with DLPFC. This produced the "insula as switch" story.

**2015-2016: poetry and the founding model.** Liu et al. (2015, a11): 14 expert poets and 13 novices wrote poems in a scanner. Executive regions were attenuated during generation and re-engaged during revision, while medial prefrontal cortex was active in both. Beaty, Benedek, Silvia and Schacter (2016, a09, a10) put this into a model: the default network produces candidate ideas from memory; the control network evaluates and modifies them to fit the goal. Mayseless et al. (2015, a20) and Heinonen et al. (2016, a21) added small independent studies (n=30 and n=16, abstract only).

**2017-2018: constraint and prediction.**
- Beaty et al. (2018, a13, a14): after studying noun-verb pairs, people made verbs for studied nouns. A strong obvious answer pulled responses closer to it. Imaging showed more default, salience and left DLPFC activity.
- Beaty et al. (2018 PNAS, a16, a17, b06-b08): connectome-based prediction of AUT originality in 163 people, replicated in three external samples (n=39, 54, 405).

**2019: the key review.** Beaty, Seli and Schacter (a18, a19, b01-b03). Table 1 lists ten studies from 2017-2018, n from 22 to 1,277. It proposes three mechanisms (retrieval, inhibition, internal attention), notes lesion and dynamic-connectivity work, and says causality is untested and suggests brain stimulation. It has no effect sizes and no formal sequential model. It makes no independent claim about salience (b02).

**2020-2026: tension and scale.**
- Meta-analysis (Cogdell-Brooke 2020, b11): 20 fMRI studies, 596 participants. Largest overlap was with the semantic control network, not the default network.
- Large resting-state study (Kenett et al. 2025, c21): N=2433 over 10 samples. The count of DMN-ECN switches predicted divergent thinking but not intelligence, with an inverted U.
- Opposite direction (Cerebral Cortex 2025, b17): creative achievement went with more separation between control and default networks.
- Replications: n=171 default-frontoparietal realignment (Beaty 2021, d13); a pre-registered replication (Sunavsky and Poppenk 2020, d14) found IFG-IPL connectivity among predictors that generalised.
- Time course doubt: Lloyd-Cox et al. (2022, d12) found executive classification accuracy above default already early, which does not fit a salience-then-executive order.
- Methods warning: Marek et al. (2022, d15, a24): brain-wide associations need thousands of people; the median neuroimaging study has n of about 25.
- LLM era: first LLM-brain alignment test during creative thinking (Ismayilzada et al. 2026, a25-a27) and reviews that use the network story as an analogy only (Huang et al. 2026, b20, c17).

**Competing theories in one table.**

| Theory | Claim | Main support | Main problem |
|---|---|---|---|
| Defocused attention | Low control helps | Older EEG work | Dietrich and Kanso found no support (a23) |
| Default engine + control editor (Beaty 2016) | DMN generates, ECN evaluates | a01, a09, a11, b19 lesions | Default deactivated in Benedek 2014; Cogdell-Brooke finds semantic control |
| Controlled internal retrieval (Benedek 2014) | Generation is focused, control-heavy | a08 | Single small study |
| Semantic control (Cogdell-Brooke 2020) | Overlap is with semantic control network | b11 | Activation meta-analysis, not connectivity |
| Switching balance (Kenett 2025) | Right amount of DMN-ECN switching | c21, N=2433 | Resting-state, correlational |
| Separation (2025 gradient study) | More control/default differentiation goes with achievement | b17 | Preliminary, two samples, most predictors did not replicate |
| Foraging (Ovando-Tellez 2025) | Creative search switches clusters faster, clusters slower | b14, b15 | Brain link in one sample only |

## 3. Core findings with exact numbers

Status key: established = two or more independent sources agree; single = one source; contested = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Default and executive hubs couple during creative generation though anticorrelated at rest | Task n=25 (3 of 28 excluded); rest sample n=42; MVPA p<.001 uncorrected | Beaty 2015 (a01-a03) | Established (K02), with caveats; later n=171 replication (d13) |
| High divergent thinkers show stronger IFG-default coupling at rest | 12 vs 12; left IFG-left IPL t=3.00, p=.008; PCC t=3.34, p=.005; DT composite 2.27 vs 1.88 | Beaty 2014 (a06) | Single small sample |
| Network efficiency relates to AUT creativity | r=.44, p=.02, N=25 | Beaty 2015 (a05) | Fragile; upper bound |
| Recalled ideas come first, new ones later | Old 6.69 s vs new 8.73 s; t(34)=6.83, d=1.16; new rated more creative d=1.46; 85.37 ideas per person; old 48.34 vs new 37.02 | Benedek 2014 (a07) | Single-source (K01) |
| New ideas need more inferior parietal activity | Left IPC signal 0.20 new vs 0.07 old; t=4.24; FWE | Benedek 2014 (a08) | Single |
| Serial order of idea raises ACC and default activity | n=16, abstract only | Heinonen 2016 (a21) | Single, weak |
| Strong obvious answer pulls ideas toward it | Semantic distance 0.76 vs 0.74; t(21)=2.12, p=.04; N=24 | Beaty 2018 (a13) | Tiny effect |
| Constraint raises default, salience, left DLPFC activity | Only precuneus survived FWE; rest p<.001 uncorrected | Beaty 2018 (a14) | Weak statistics |
| Early default-salience coupling, later default-executive | Five 2 s windows, N=25, FDR p<.05 | Beaty 2015 (a04) | Contested (K03); d12 conflicts |
| Executive above default early in classification | U-shape over three phases in both networks; abstract only | Lloyd-Cox 2022 (d12) | Contested |
| Executive attenuated in poetry generation, re-engaged in revision | 14 experts + 13 novices; correlation sign flip, P<.01 | Liu 2015 (a11) | Established with design work (K04) |
| Whole-brain connectome predicts originality | 224 edges; r(161)=.30, P=1.29e-4; low net 603 edges r=.22 | Beaty 2018 (a16, b06) | Single lab |
| External validation shrinks with sample size | High net r(37)=.35, r(52)=.28, r(403)=.13 | Beaty 2018 (a17, b07) | Replicated; effect near r=.1-.15 |
| Low-creative network weak | r=-.04, .02, .11 (only last, P=.03); Steiger z=0.83, p=.40 | Beaty 2018 (b07, b08) | Replicated in 1 of 3 |
| Prediction specific to divergent thinking | Control task r=.05; fluid intelligence r=.04 | Beaty 2018 (b08) | Single |
| DMN-ECN switching predicts divergent thinking, not intelligence; inverted U | N=2433, 10 samples; task fMRI N=31 | Kenett 2025 (c21) | Established (K06) |
| Meta-analysis: largest overlap with semantic control network | 20 studies, 596 participants; control>divergent 35 foci in 8 experiments | Cogdell-Brooke 2020 (b11) | Contested (K21) |
| Creative achievement tied to more control-default separation | Sample 1 n=236, sample 2 n=234; gradient similarity r=.81, .82; b=1.99 P<.01 falls to b=0.22 P=.11 without intelligence covariate | Cerebral Cortex 2025 (b17) | Contested (K07) |
| Lesion: medial PFC for remote concepts, rostrolateral PFC for combining | 29 patients vs 54 controls (review); 18 FTD + 27 controls (b19) | b04, b19 | Established, thin (K09) |
| Memory search: faster switching, slower clustering in creative people | Behaviour R2=.313 (n=86), .690 (n=92); CPM rs=.33 (perm p=.019, .024) | Ovando-Tellez 2025 (b14) | Behaviour replicated; brain single |
| Episodic vs semantic induction changes semantic distance | 0.84 vs 0.81; t(27)=3.11, p=.004; N=28 | Beaty 2020 (b12) | Single |
| Frontoparietal subnetworks realign toward default in divergent thinking | n=171 | Beaty 2021 (d13) | Replication (abstract) |
| Brain-wide effects are small and inflated at n of about 25 | About 50,000 people; median study n about 25 | Marek 2022 (d15) | Established (K08) |
| LLM representations align with DMN early; weaker during generation | r=.55 (size), r=.52 (AUT score); drops to .40 without Gemma-3 270M; 170 people | Ismayilzada 2026 (a25-a27) | Single, fragile |
| LLMs homogeneous | Variability 0.459 vs human 0.738; within-prompt similarity above 0.8 across 70+ models | Wenger and Kenett 2025 (a28); Jiang 2026 (c13) | Established (K14) |
| LLMs beat average, not top, humans on divergence | Hedges g 0.5-2.6; DAT vs top half g=-0.88 | Huang 2026 (b20, c16); Bellemare-Pepin 2026 (b21) | Established (K19) |
| Generate-prune scaffold beats chain of thought on a checkable task | Game of 24 GPT-4: IO 7.3%, CoT 4.0%, CoT-SC 9.0%, ToT b=1 45%, b=5 74% | Yao 2023 (c04) | Single (K12) |
| Over-generation saturates | About 200 of 4000 ideas non-duplicate (about 5%) | Si 2024 (c02) | Single (K13) |
| LLM judges rank ideas near chance | Best 53.3% vs human 56.1% | Si 2024 (c03) | Single |
| Verbalized Sampling raises diversity | 1.6-2.1x; recovers 66.8% of base diversity; joke 1.83 to 3.01 | Zhang 2026 (d01) | Single (K22) |
| Divergent and convergent breadth separable in LLMs | Weak Spearman everywhere; semantic entropy vs human novelty rho=.56 | Sen 2026 (d04, d05) | Single (K24) |
| LLMs fail the leap, not the fact | 2,061 puzzles; non-thinking under 30%; factual-vs-creative drop 6.08-17.21% | CresOWLve (d08, d09) | Single (K25) |

## 4. Mechanisms and models

Each model below is written so that an engineer can turn it into a scaffold step. The brain data do not prove the step works for a language model. Each is a hypothesis to test (see section 8).

### 4.1 Generate then control (Beaty 2016 model)
- **Brain version.** Default network proposes candidates from memory. Control network checks them against the goal, edits them, or rejects them. Both are active together.
- **Engineering version.** Pass A: produce N candidates from the bare task with no filter. Pass B: a separate call, with a goal description and checks, selects, edits or rejects. Code, not the model, decides which candidates go on.
- **Caveat.** Executive activity is not absent during generation in the AUT (d12, a04). Pass A may need light constraints rather than none (K27).

### 4.2 Obvious-first order and inhibition (Benedek 2014; Beaty 2018)
- **Brain version.** Recalled ideas dominate the first 15 s; new ideas need orbital inferior frontal gyrus and inferior parietal control. A strong stored answer pulls later answers toward it.
- **Engineering version.** Step 1: elicit the modal answer on purpose and record it. Step 2: exclude it (and its near duplicates by embedding) and regenerate. Step 3: repeat with the new exclusion list. Code keeps the exclusion list.
- **LLM parallel.** Typicality bias in preference data pushes models to the modal answer (d03). Early LLM samples are largely the same (c02, c13).

### 4.3 Salience switch (contested)
- **Brain version.** The insula detects the right moment to hand over from default to control.
- **Engineering version.** A code-side detector hands over, for example when the novelty rate of new candidates drops or when duplicates exceed a threshold, not on a fixed timer. This matches guardrail G1 (act on a signal). The neural basis is weak (a04, d12, b02), so the detector must be justified on its own.

### 4.4 Switching balance (Kenett 2025)
- **Brain version.** Number of DMN-ECN switches at rest predicts divergent thinking, with an inverted U.
- **Engineering version.** Treat the number of generate/control alternations as a tunable dial. Sweep 1, 2, 3, 4 alternations at equal tokens and look for a middle optimum.

### 4.5 Controlled retrieval (Cogdell-Brooke; Wu 2015; Benedek 2014)
- **Brain version.** The overlap is with the semantic control network: picking weak associates, suppressing strong ones.
- **Engineering version.** "Control" is mainly retrieval control. Prompt or code-force links across semantic clusters; use outside retrieval for distant material (Nova, d07). This is different from a critic that scores finished ideas.

### 4.6 Foraging policy (Ovando-Tellez 2025)
- **Brain version.** Creative people switch clusters fast but cluster slowly. Pre-switch timing predicts fluency (R2=.313 and .690).
- **Engineering version.** Force a topic switch after k items in a cluster, versus free switching. Cluster by embedding.

### 4.7 Internal attention (Beaty 2019)
- **Brain version.** Right posterior IPL couples with visual cortex when attention turns inward.
- **Engineering version.** The closest analogue is a short context that shields generation from noise. Input hygiene already covers this (S1). No new step.

### 4.8 Episodic specificity (Madore 2019, a15, abstract only)
- **Brain version.** A short induction to recall details raised hippocampal and frontoparietal coupling and idea production.
- **Engineering version.** Before generating uses, ask the model to list concrete specific episodes or instances, then generate from them. Cheap to test.

### 4.9 Lesion dissociation (b04, b19)
- Produce remote candidates (medial PFC) and combine them (rostrolateral PFC) are separable. In an agent this suggests two separate calls: one to produce remote items, one to combine pairs. Evidence is thin.

### 4.10 Output-side models for LLMs
- **Verbalized Sampling (d01, d02, d17).** One prompt asks for several answers each with a stated probability. It stacks with temperature. Large models gain more; small models lose quality with structured output.
- **Gacha Decoding (d06).** The model plans distinct modes in text. An external random number generator picks the mode. Code does the selection.
- **Nova (d07).** Iterated plan then retrieve outside knowledge. Reported 3.4x unique ideas; gains flat after step 3 without planning.

## 5. What holds up

**Replicated or consistent.**
1. **Default-control cooperation during idea generation.** Beaty 2015 (n=25), Beaty 2021 (n=171, abstract), Sunavsky and Poppenk 2020 (pre-registered, IFG-IPL connectivity), a rest-state group effect (n=12 vs 12), lesion work (b19, n=45), and several others. Shape holds; effect sizes in small studies are inflated.
2. **Prediction of originality from connectivity.** The high-creative network generalised to three external samples. Effects shrink: r=.35 (n=39), .28 (n=54), .13 (n=405). Real effect probably r=.1-.15.
3. **Switching and the inverted U.** Kenett 2025 at N=2433 across 10 samples, plus task-fMRI N=31.
4. **Specificity to divergent thinking.** Control task r=.05; fluid intelligence r=.04.
5. **Obvious first, new later.** Behavioural order effect (a07) matches the serial-order effect in a21. Only two independent labs and small n.
6. **Foraging behaviour.** Replicated in two samples (R2=.313 and .690).
7. **LLM homogeneity.** Four-plus sources: Wenger and Kenett, Jiang et al., Meincke et al. (GPT-4 pools 0.255-0.432 vs human groups 0.243), Padmakumar and He, Mohammadi.

**Failed, weaker, or contested.**
- **Low-creative network.** Replicated in only 1 of 3 external samples (r=.11 in n=405). Not significantly different from the high network (Steiger z=0.83, p=.40).
- **Salience-first order.** Based on one study, five windows, N=25. Lloyd-Cox 2022 contradicts it at abstract level. Marked contested.
- **Default as engine.** Default regions deactivated in Benedek 2014; the meta-analysis points to semantic control; Dietrich and Kanso found nothing beyond diffuse prefrontal activity.
- **Coupling vs separation.** Coupling in Beaty 2014, 2015, 2018; separation in the 2025 achievement study. The difference follows measure (ability vs achievement, task vs rest). Most predictors in the 2025 study did not replicate between samples; its main result vanished without the intelligence covariate.
- **Executive during generation.** Attenuated in poetry (Liu 2015) but present from early windows in the AUT (Beaty 2015, Lloyd-Cox 2022). Task type may decide.
- **Brain-behaviour link for foraging.** One MRI sample; 2 of 4 components survived permutation.
- **Statistics.** 2015 coupling findings are p<.001 uncorrected; in the 2018 constraint study only the precuneus survived FWE. Marek 2022 says effects at n of about 25 are unreliable.
- **Data reuse.** The 2026 LLM-brain study reuses the Beaty 2018 data.

**Moderators.** Task type (figural vs verbal, rest vs task) changes the network (b03). Sex (left IFG-MPFC coupling positive in females, negative in males, n=1,277 in review table; b05, snippet only). Openness link in one sample only (b18). Intelligence covariate removes an effect (b17). Age: adults show stronger cross-network coupling than children in a co-creative ChatGPT dialogue, but creativity scores were equal (n=15 and 16; c23).

**Interventions that worked (humans).** Episodic specificity induction raised coupling and idea production (a15, abstract). Divergent persona raised questioning (p=.034, n=59 vs 51) but not fluency; perceived best persona often differed from objective performance (d16). No brain-stimulation study had changed DMN-ECN interaction as of the 2019 review (b01).

**Interventions that did not work.** The schema already lists "creativity training prompts" under section 4b. Nothing in this subfield overturns that. Fluency did not rise with the persona coach (d16).

## 6. Language models

**Baseline behaviour.**
- On the Alternate Uses Task, LLMs beat average humans in most comparisons (Hedges g 0.5 to 2.6; Hubert g=2.61 with post hoc fluency matching, Koivisto and Grassini g=0.70 with prospective matching, Bellemare-Pepin DAT g=0.52 over average and g=-0.88 against the top half) (b20, b21, c16). Top humans still win. The AUT items may be in training data.
- Across models, answers are alike. Originality LLM 0.711 vs human 0.695, yet variability 0.459 vs 0.738. A "very creative" system prompt lifted originality to 0.754 and variability to 0.576, still below human (a28). Within-prompt similarity above 0.8 even at temperature 2.0 (c13). RLHF models cluster tightly (c11). InstructGPT co-writing homogenised essays; base GPT-3 did not (c10).
- Doshi and Hauser (c09): N=293 writers; AI ideas raised novelty 6.7% and usefulness 6.4% but stories became more alike. The anchoring risk applies to our own scaffold when it shows earlier attempts.

**What changed output diversity, with numbers.**

| Lever | Result | Source |
|---|---|---|
| Temperature | Weak link to novelty, moderate to incoherence | c12; Sen 2026 d05 (raises semantic entropy) |
| Prompt structure (chain-of-thought steps) | Unique ideas about 3700 to 4700; pairwise similarity 0.377 baseline | c08 |
| Persona prompt | Little: 0.368 vs 0.377 baseline | c08 |
| Verbalized Sampling | 1.6-2.1x diversity; joke human-rated 1.83 to 3.01; quality up 25.7% | d01 |
| Sequence listing | Poem 2.07, story 2.76 vs VS 2.39, 3.06 | d02 |
| Gacha Decoding | 4.7x-11x fewer samples for same mode coverage; 7.1x quality-gated diversity at 256 generations | d06 |
| Retrieval planning (Nova) | 3.4x unique ideas | d07 |
| Model scale and reasoning | Raise convergent scores, not divergent breadth | d05 |

**Generate-then-control in LLMs.**
- Tree of Thoughts (c04): large gains on a checkable task, but the evaluator is the same model. Bottleneck was generation: GPT-4 generating plus GPT-3.5 evaluating gave 64%; the reverse gave 31%. So control quality was not the main driver (critique note 4).
- Same-model verifier on proofs (d10, d11): 5 of 6 IMO 2025 problems (85.7%) vs 21.4-38.1% for best of 32. Acceptance needed five passes in a row. Tokens not matched; no verifier accuracy reported.
- Creative tasks: stacking constraints (Denial Prompting) lowers correctness while raising divergence. GPT-4 pass@1 16.1 to 2.1; divergent creativity 4.5 to 15.3; convergent creativity 16.2 to 0.0 (c05). Accuracy-built reasoning strategies helped little; only tree search raised divergence (c06).
- Multi-agent diverge-discuss-converge (c07) won on originality and elaboration on 3 of 4 benchmarks, with LLM judges, personas, and no equal-token control. Guardrails G4 and G9 apply.

**Control quality.**
- Novelty judging by models is near chance: best 53.3% vs human reviewers 56.1%; GPT-4o 45.0-50.0% (c03). Experts judged LLM ideas more novel than expert ideas (4.84 vs 5.64; 5.81 with human rerank), feasibility 6.61 vs 6.34 (c01). Saturation: about 5% non-duplicates at 4000 (c02).
- LLM judges did not correlate positively with expert writers (c14).
- Failures on insight puzzles are missing links, not missing facts (d08, d09). More thinking effort gave more accuracy; GPT-5.4 nearly doubled from no thinking to medium.

**Brain alignment.**
- Ismayilzada et al. (a25-a27, 170 people): early-stage DMN alignment rises with model size (r=.55) and AUT score (r=.52), but these use different pooling methods, and the AUT correlation drops to 0.40 without the 270M model. Alignment weakens once the model generates. A creativity-optimised Llama-3.1-8B (CrPO) kept alignment with high-creativity human responses and lost it with low-creativity ones; a DeepSeek-R1 distilled model showed negative alignment. Single seeds, two families.
- Language-cortex alignment (c15) does not touch the creativity networks.
- No study found that builds or tests a DMN/ECN two-network architecture inside an LLM (c17, c27; absence is weak evidence because of search limits).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)
1. **Keep generation and control as separate passes, with code selecting.** G5, S3 then S4/S7. [E] Default-control cooperation across independent human studies (K02: a01-a03, a06, a09, b09, b10, a18, d12-d14), poetry and design generation then revision (K04: a11, a12), lesion split (K09: b04, b19). This is already in the schema; it needs no new element. Do not claim the brain data prove it helps an LLM.
2. **Do not hard-code one network per phase.** Control is part of generation (a04, d12, a12). S3 in open mode should carry light constraints, not none. Design note only; the control-free variant is a test (T9).
3. **Treat LLM samples as homogeneous.** S3 fresh context per attempt, history in code. G4. [E] K14: a28, c13, c10, c11, c08, c09, d01, d06, d03. Already in the schema.
4. **Temperature is not the diversity lever.** S3 open mode. [E] K15: c12, c08, d02, d05. Use structure, history and retrieval instead.
5. **Never use the model as the final judge of novelty.** G8. [E] c03, c14 plus the schema's existing sources. Already present. This subfield adds a near-chance number (53.3% vs 56.1%).
6. **Log both phases with separate metrics.** Section 6 logging. [S] for the claim (K24: d04, d05): divergent breadth (semantic entropy, rho=.56 with human novelty) and convergent fulfilment are weakly correlated, so one score hides trade-offs. Logging is free and needs no schema change.
7. **Treat small-N brain effects as upper bounds.** Evidence handling rule, not a schema element. [E] K08: d15, a24, a05, a17. Do not cite r=.44 or d=1.16 as expected agent effects.

### Test first
1. **Discard-the-obvious step.** S3 open mode, new operator. [S] K01, K23: a07, a13, a14, d03. Elicit the modal answers, exclude them, regenerate. Compare with plain resampling and Verbalized Sampling at equal tokens.
2. **Verbalized Sampling style generation as a loose-phase operator.** S3 open mode. [S] K22: d01, d02, d06, d17. Large-model benefit; small-model quality cost.
3. **Retrieval-grounded generation to beat saturation.** S3 open mode (the schema already says "grounded in retrieved analogues"). [S] K13: c02, d07. 3.4x unique ideas from Nova.
4. **Semantic-control critic: forced cross-cluster linking instead of an evaluator.** S3 / O7. [C] K21, K25: b11, a22, d08, d09. Compare with a standard scoring critic.
5. **Number of generate/control alternations.** S3-S4 loop control. [S] K06 (the human result is established, the transfer is untested): c21. Sweep 1-4.
6. **Forced cluster switching.** O (switch between semantic clusters). [S] K10: b14, b15, b24.
7. **Episodic specificity pre-step.** S2/S3. [S] a15 (abstract only).
8. **Control-free versus lightly constrained generation.** S3. [C] K27: d12, d13. Includes a salience-style "notice" step (K03) as a variant.
9. **Handover signal.** S3 to S4 trigger, for example duplicate or novelty rate. [C] K03: a04, a10, d12. A G1-consistent trigger, not a neural claim.
10. **External check for ranking ideas** (executed code, retrieval). G8, S7. [S] K13, K26: c03, d10, d11.
11. **Brainstorm then select versus one-pass.** Cited second-hand (Summers-Stay 2023 via b22). [S]
12. **Constraint ladder with a selection step.** S3/S4. [S] K11: c05, c06.

## 8. Concrete tests on our bench

All arms get the same token budget, counting every pass. Setup tokens count (G7). Run at least 3 seeds, report bootstrap intervals, use two models if possible.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | AUT-style uses; NoveltyBench open prompts | (a) plain K samples; (b) K samples then a separate control pass chooses the final set; (c) code-only selection by embedding distinctness | Distinct-answer count at 0.8 cosine; fixed-rubric originality; NoveltyBench score (our earlier run: 3.18 plain, 9.63 scaffold) | (b) no better than (c); if (b) beats (c), a model critic adds value. Expect a few points at most |
| T2 | Same | (a) plain; (b) elicit modal answer, exclude it by embedding, regenerate, 3 rounds; (c) Verbalized Sampling; (d) Sequence listing | Share of non-duplicates at equal sample count; mean pairwise cosine | (b) beats (a); relation to (c) unknown. VS paper reports 1.6-2.1x |
| T3 | Same | Alternations 1, 2, 3, 4 of generate N/k then control | Unique ideas and rubric originality | Inverted U, optimum at 2-3. Nova gains flat after step 3 (44.1 vs 42.4) |
| T4 | CresOWLve-style insight puzzles (checkable) | (a) one long thought; (b) generate then critic scoring; (c) forced cross-domain link then check; (d) extended thinking | Accuracy | (c) above (b); (d) is the bar. Failures are the leap, so link forcing should matter more than scoring |
| T5 | Idea ranking | Self-judge pairwise; embedding-novelty code; retrieval-based prior-art check | Balanced accuracy against held-out human rank (human reviewers 56.1%) | Self-judge near 50%; retrieval check above 56% |
| T6 | AUT; open prompts | Free clustering vs forced switch after k items (k=3, 5) | Unique clusters, rubric originality | Small gain for forced switching; k matters |
| T7 | AUT | Episodic specificity pre-step vs none | Originality, fluency | Small gain in humans; untested in models |
| T8 | Code tasks with constraints (NeoCoder style) | Constraint ladder alone vs ladder with selection | pass@1 and divergent creativity | Ladder lowers correctness (GPT-4 16.1 to 2.1); selection should recover some |
| T9 | Ideation | Control-free generation vs light-constraint generation | As T1 | Tests K27. A null is plausible |
| T10 | Checkable task with plain pass rate 30-70% | Generate pass plus same-model verifier vs best-of-N vote | Accuracy at equal tokens | Verifier helps only on checkable; the IMO result is not token-matched |

## 9. What does not transfer, and why

- **Neural effect sizes.** r=.44, d=1.16 and the extreme-group t-values come from n of 12-35. They are upper bounds even for people (K08).
- **Network labels.** Our agent has no default, salience or executive network. The alignment paper (a25) reports correlational similarity over a modest model set, not architecture. Do not build a "DMN module" and an "ECN module".
- **Salience switch.** One small study; the 2019 review itself makes no salience claim (b02); later time-course work disagrees (d12).
- **Timing.** 2 s fMRI windows with BOLD lag; ordering is inferred from connectivity differences, not causal flow. The order of hand-over in an agent is a design choice.
- **Resting-state findings.** Kenett's switching count is a trait measured at rest. Our agent has no rest state and no trait to measure. The inverted U transfers only as a dial to test.
- **Insight problems.** Beaty's model excludes insight (a09). Our checkable puzzles are insight-like; use CresOWLve results there.
- **Flow.** Nine heterogeneous studies; no LLM equivalent (K20).
- **Human fatigue, motivation, prior knowledge.** Absent in a prompted model.
- **Reverse inference.** "Region X was active, so function Y" is loose, especially in meta-analyses (a22).
- **Anchoring.** In humans an AI idea raises novelty but lowers collective diversity (c09). Showing a model its earlier attempts has the same risk; schema S3 already isolates attempts.
- **Scaling of control.** More reasoning raises convergent scores and not divergent breadth (d05). A heavier control phase may not help open tasks.
- **Brain stimulation.** No study had changed DMN-ECN coupling causally (b01).

## 10. Open questions

1. Does a generate pass plus a separate control pass beat one-pass generation at equal tokens on creative tasks? No equal-token test exists (ToT, LLM Discussion and the IMO pipeline do not match tokens).
2. What is the best number of alternations? No LLM sweep.
3. Does discarding the first k obvious answers help beyond what saturation implies (about 5% unique at 4000)? No direct test.
4. Can an external check (executed code, retrieval) repair the control phase for novelty? Self-verification works for proofs; novelty ranking has no repair.
5. Is "control" best modelled as semantic control (retrieving weak associates) rather than evaluation? Indirect support only.
6. Which human result survives a large pre-registered study: coupling or separation? Salience-first or executive-first?
7. Does creativity post-training change internal representations once pooling and model size are controlled? Not researched.
8. Does cross-model homogeneity (above 0.8) persist under VS, Gacha or retrieval scaffolds? Not measured across models.
9. Do results carry from the AUT to tasks with a correct answer? Partly: CresOWLve and IMO suggest the leap is the bottleneck.
10. Is there a layer-wise LLM analogue of generate versus control? Nobody has tested it.
11. How big are scaffold effects when blind humans, not LLM judges, rate at equal tokens?

## 11. Sources

[V] = opened (full text or full page read this session). [M] = abstract, snippet or second-hand only. Evidence ids in brackets. Several brain items (b13, b23, c21, c22) were opened at abstract and introduction level only; effect sizes were not extracted.

- [V] Beaty, Seli, Schacter (2019) Network neuroscience of creative cognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC6428436/ [a18, a19, b01-b03]
- [V] Beaty, Benedek, Kaufman, Silvia (2015) Default and executive network coupling. https://pmc.ncbi.nlm.nih.gov/articles/PMC4472024/ [a01-a05, b09]
- [V] Beaty et al. (2014) Creativity and the default network at rest. https://pmc.ncbi.nlm.nih.gov/articles/PMC4410786/ [a06, b10]
- [V] Benedek et al. (2014) To create or to recall? https://pmc.ncbi.nlm.nih.gov/articles/PMC3991848/ [a07, a08]
- [V] Beaty, Benedek, Silvia, Schacter (2016) Creative cognition and brain network dynamics. https://pmc.ncbi.nlm.nih.gov/articles/PMC4724474/ [a09, a10, a29]
- [V] Liu et al. (2015) Brain activity and connectivity during poetry composition. https://pmc.ncbi.nlm.nih.gov/articles/PMC4581594/ [a11]
- [M] Ellamil et al. (2012) Evaluative and generative modes of thought. https://pubmed.ncbi.nlm.nih.gov/21854855/ [a12]
- [V] Beaty et al. (2018) Creative constraints. https://pmc.ncbi.nlm.nih.gov/articles/PMC6083214/ [a13, a14]
- [M] Madore et al. (2019) Episodic retrieval support for divergent thinking. https://pubmed.ncbi.nlm.nih.gov/29161358/ [a15]
- [V] Beaty et al. (2018) Robust prediction of individual creative ability, PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC5798342/ [a16, a17, b06-b08]
- [M] PNAS landing page (HTTP 403). https://www.pnas.org/doi/10.1073/pnas.1713532115 [c26]
- [M] Mayseless, Eran, Shamay-Tsoory (2015). https://pubmed.ncbi.nlm.nih.gov/26003860/ [a20]
- [M] Heinonen et al. (2016). https://pubmed.ncbi.nlm.nih.gov/27627760/ [a21]
- [M] Wu et al. (2015) ALE meta-analysis. https://pubmed.ncbi.nlm.nih.gov/25891081/ [a22]
- [M] Dietrich and Kanso (2010). https://pubmed.ncbi.nlm.nih.gov/20804237/ [a23]
- [M] Marek et al. (2022) Reproducible brain-wide association studies. https://pubmed.ncbi.nlm.nih.gov/35296861/ [a24, d15]
- [V] Ismayilzada et al. (2026) LLM-brain alignment during creative thinking. https://arxiv.org/pdf/2604.03480 [a25-a27]
- [V] Wenger and Kenett (2025) Creative homogeneity across LLMs. https://arxiv.org/pdf/2501.19361 [a28]
- [M] Lesion and sex-difference studies as tabulated in the 2019 review. https://pmc.ncbi.nlm.nih.gov/articles/PMC6428436/ [b04, b05]
- [V] Cogdell-Brooke et al. (2020) Meta-analysis of fMRI studies of divergent thinking. https://pmc.ncbi.nlm.nih.gov/articles/PMC7643395/ [b11]
- [V] Beaty et al. (2020) Default network contributions to episodic and semantic processing. https://pmc.ncbi.nlm.nih.gov/articles/PMC7056499/ [b12]
- [V] Barnett and Vasiu (2026) Flow, DMN-ECN connectivity. https://pmc.ncbi.nlm.nih.gov/articles/PMC12827708/ [b13, c24]
- [V] Ovando-Tellez et al. (2025) Switching, fast and slow. https://pmc.ncbi.nlm.nih.gov/articles/PMC12628016/ [b14, b15, b24]
- [M] Lloyd-Cox, Chen, Beaty (2022) Time course of creativity. https://doi.org/10.1016/j.cortex.2022.08.008 [b16, d12]
- [V] Functional differentiation of default and frontoparietal control networks (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC11890067/ [b17, b18, b25]
- [V] Rostral prefrontal gradient in frontotemporal dementia (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13548864/ [b19]
- [V] Huang, Liu, Yang (2026) LLMs as tools, models and partners in creativity. https://pmc.ncbi.nlm.nih.gov/articles/PMC13608707/ [b20, c16-c20]
- [V] Bellemare-Pepin et al. (2026) Divergent creativity in humans and LLMs. https://pmc.ncbi.nlm.nih.gov/articles/PMC12824279/ [b21, b22]
- [V] Khalil et al. (2025) Adaptive decision-making fast and slow. https://pmc.ncbi.nlm.nih.gov/articles/PMC11892090/ [b23]
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109 [c01-c03]
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 [c04]
- [V] Lu et al. (2025) NeoCoder / Denial Prompting. https://arxiv.org/abs/2407.09007 [c05, c06]
- [V] Lu et al. (2024) LLM Discussion. https://arxiv.org/abs/2405.06373 [c07]
- [V] Meincke, Mollick, Terwiesch (2024) Prompting diverse ideas. https://arxiv.org/abs/2402.01727 [c08]
- [V] Doshi and Hauser (2024) Generative AI enhances individual creativity but reduces collective diversity. https://arxiv.org/abs/2312.00506 [c09]
- [V] Padmakumar and He (2024) Does writing with language models reduce content diversity? https://arxiv.org/abs/2309.05196 [c10]
- [V] Mohammadi (2024) Creativity has left the chat. https://arxiv.org/abs/2406.05587 [c11]
- [V] Peeperkorn et al. (2024) Is temperature the creativity parameter? https://arxiv.org/abs/2405.00492 [c12]
- [V] Jiang et al. (2025/2026) Artificial Hivemind. https://arxiv.org/abs/2510.22954 [c13]
- [V] Chakrabarty et al. (2024) Art or Artifice? https://arxiv.org/abs/2309.14556 [c14]
- [V] Mischler et al. (2024) Contextual feature extraction hierarchies converge. https://arxiv.org/abs/2401.17671 [c15]
- [V] Kenett, Yoed et al. (2025) Dynamic switching between brain networks. https://pmc.ncbi.nlm.nih.gov/articles/PMC11733278/ [c21]
- [V] Neural dynamics of creative idea generation and evaluation (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12669686/ [c22]
- [V] Horowitz-Kraus et al. (2026) Co-creative dialog with ChatGPT. https://pmc.ncbi.nlm.nih.gov/articles/PMC13641069/ [c23]
- [M] Hubert et al. (2024), Koivisto and Grassini (2023), Organisciak et al. (2023), via Huang 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13608707/ [c18-c20]
- [V] Zhang et al. (2026) Verbalized Sampling. https://arxiv.org/abs/2510.01171 [d01-d03, d17]
- [V] Sen et al. (2026) Automated creativity evaluation. https://arxiv.org/abs/2606.11762 [d04, d05]
- [V] Geng et al. (2026) Gacha Decoding. https://arxiv.org/abs/2610.01382 [d06]
- [V] Hu et al. (2024) Nova. https://arxiv.org/abs/2410.14255 [d07]
- [V] Ismayilzada et al. (2026) CresOWLve. https://arxiv.org/abs/2604.03374 [d08, d09]
- [V] Huang and Yang (2025) IMO 2025 verification pipeline. https://arxiv.org/abs/2507.15855 [d10, d11]
- [M] Beaty et al. (2021) Functional realignment of frontoparietal subnetworks. https://pubmed.ncbi.nlm.nih.gov/33895837/ [d13]
- [M] Sunavsky and Poppenk (2020) Neuroimaging predictors of creativity. https://pubmed.ncbi.nlm.nih.gov/31654758/ [d14]
- [V] Rosenbaum et al. (2025) Scaffolding creativity. https://arxiv.org/abs/2510.26490 [d16]
- [M] Beaty, Seli, Schacter (2019) Curr Opin Behav Sci landing page. https://doi.org/10.1016/j.cobeha.2018.12.016 [c25]
