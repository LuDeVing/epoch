# Metacognition and higher-order representation: deep document

*Subfield D06.08. Built from evidence_a-d.jsonl (96 lines; most LLM primaries opened as full text), claims.jsonl (K01-K35) and critique.md in the same folder. Evidence ids (a01, b11, c05, d10 ...) refer to those files. Several ids are the same paper (see section 11), so counts of sources are by paper, not by line.*

## 1. What it is

Metacognition is thinking about one's own thinking. Two things are mixed under the name.

1. **Monitoring**: a second signal about a first process. Examples: "how sure am I?", "do I know this?", "did I get this right?", "why did I choose that?". The first process is the object level. The second is the meta level (Nelson and Narens 1990, a13).
2. **Control**: using that signal to act. Examples: stop, keep going, look it up, change strategy, abstain.

Higher-order representation is the philosophy-of-mind version. A state is conscious, on Rosenthal's view, when the subject has a roughly simultaneous, non-inferential thought that they are in that state (a01, a10). The key point for us is not consciousness. It is this: **the higher-order state is a separate representation about a first one, and it can be wrong, empty or missing** (a02). A self-report is therefore a second signal with its own error rate, not a readout of the first process.

Why this matters for our agent: the schema already says "reasoning text is not evidence" (G10) and "doubt only on a signal" (G1). This subfield asks the empirical question under both: which signals about the agent's own states are reliable enough to act on, which are not, and what can replace the bad ones. The answer from the evidence is consistent:

- Verbalised self-report (stated confidence, stated reasons, stated introspection) is weak.
- Signals computed from behaviour (agreement across samples, token-level certainty, outside checks) are stronger.
- Self-correction works only when an outside check supplies the error.
- The philosophical core (Rosenthal, Proust) gives vocabulary and one design idea, but almost no numbers for an LLM agent.

Subfields researched in parallel and not covered here (links only): Calibration and overconfidence; Dual-process theory; Debiasing and cognitive forcing; Reflection-in-action; Global workspace theory; Cognitive biases and premature closure; Search over thoughts; Belief updating.

## 2. History and theories in depth

### 2.1 Philosophy

**Higher-order thought (HOT) theory.** Rosenthal 1997, 2005 (a10; known only through the SEP, books not opened). A mental state is conscious when one has an assertoric thought "I am in state X". That thought is itself usually not conscious. It is caused non-inferentially. Consciousness is how things appear to the subject, and appearance can misrepresent. Rosenthal holds that a suitably caused HOT is enough for a conscious experience even with no first-order state (an "empty" or targetless HOT). Block (2011) objects. Rosenthal and Weisberg reply. The SEP editors judge the reply does not fully settle it (a02). The debate runs 2005-2022 and is unresolved.

**Family of higher-order views (a01).**
- Higher-order perception or inner sense (Armstrong, Lycan): the higher-order state is a perception-like monitor.
- Actualist HOT (Rosenthal): an actual thought is needed.
- Dispositionalist HOT (Dennett, Carruthers): availability to such a thought is enough.
- Self-representational hybrids: the state represents itself.

**Objections (a01, a24).** Empty HOTs; animals and infants who seem conscious without concepts of mind; the "rock problem" (why does a HOT about a rock not make the rock conscious); explaining phenomenal feel.

**Empirical programme: prefrontal HOT theory (a03).** Lau and Passingham 2006 (a04): metacontrast masking gave two onset-asynchrony conditions (33 ms and 100 ms) with equal discrimination accuracy and different reported awareness. Eight participants in the behavioural study, 13 in fMRI. Left mid-dorsolateral prefrontal activity correlated with percent declared conscious, r = 0.512. Rounis et al. 2010 (a05, not opened): theta-burst TMS to prefrontal cortex lowered metacognitive visual awareness while discrimination stayed intact. The counter-case is strong. Maniscalco and Lau 2011 (a15, not opened) showed the dissociation can come from a response-criterion confound. Peters and Lau 2015 (a08, 9 observers) found confidence matched a Bayesian ideal observer even for masked stimuli and no performance-without-awareness pattern. Block, Odegaard, Michel and Malach, Raccah and others dispute the prefrontal reading (a03, a24). Status: contested.

**Proust's procedural view (a11, book not opened).** Metacognition is mostly implicit, feeling-based monitoring and control: feeling of knowing, fluency, effort. It does not need a concept of mind or a metarepresentation. She contrasts this with attributivism (Carruthers), where metacognition is mindreading applied to oneself. For an engineer the useful reading is: a cheap non-verbal signal can drive control without any sentence about the self. This is a design idea derived by us, not a tested claim (K24).

### 2.2 Cognitive psychology

**Nisbett and Wilson 1977 (a12, b21; not opened).** People often cannot report the real causes of their judgments and apply plausible a-priori theories. The stocking study: shoppers picked the rightmost of four identical items much more often than the leftmost and never mentioned position. Numbers recalled, not verified: about 52 shoppers, roughly 12% leftmost vs 40% rightmost. Critics: Smith and Miller 1978; White 1988; Ericsson and Simon. Reports are better when immediate, concurrent and about content, not about cause.

**Nelson and Narens 1990 (a13; not opened).** The object-level / meta-level model. Monitoring goes up, control goes down. Probes: ease-of-learning, judgment of learning, feeling of knowing, confidence.

**Koriat 1997 (a26; not opened).** Cue-utilisation: feelings of knowing and judgments of learning are inferences from cues (fluency, familiarity, ease of processing). The cues are often valid and sometimes misleading.

**Choice blindness (d18, b22; d19; b04).** Johansson et al. 2005: people choose the more attractive of two faces, are secretly handed the other, mostly fail to notice, and give reasons for the choice they did not make. Only the abstract was read. Hall et al. 2010 extended it to taste and smell in a supermarket: no more than a third of manipulated trials detected (abstract only). Grassi et al. 2025 (b04, opened) challenge the reading (section 5).

### 2.3 Measurement tradition

Henmon 1911: confidence correlates with accuracy. Fleming and Lau 2014 (a06, d17): separate metacognitive **sensitivity** (does confidence tell right from wrong) from **bias** (overall over- or underconfidence). Phi and gamma mix them. AUROC2 is bias-free but depends on task performance. Maniscalco and Lau 2012 (a14, not opened): meta-d' is the type-1 d' that an ideal metacognitive observer would need to produce the observed confidence data. M-ratio = meta-d'/d' is metacognitive efficiency. Rahnev 2025 (b02): 17 measures tested on the Confidence Database. This is the toolkit we need to score an agent's confidence fairly.

### 2.4 Computational view

Fleming and Daw 2017 (a09): self-evaluation is a second-order inference. The confidence-rater infers how well the decider did, using its own evidence, the action taken, and the covariance between the two systems. This is the same computation as judging another actor. First-order models (one variable gives both choice and confidence) cannot explain dissociations; second-order and post-decisional models can. Simulations only. Implication: a confidence pass that uses different evidence than the answer pass can in principle beat the answer pass.

### 2.5 The LLM turn (2022-2026)

- 2022: Kadavath, "mostly know what they know" (a16); Lin, Hilton, Evans on verbal uncertainty by finetuning (a17).
- 2023: Turpin on unfaithful CoT (a18); Lanham on CoT faithfulness (b08); Xiong on confidence elicitation (b11); Tian "just ask" (b10); Huang "cannot self-correct" (b13); Kuhn semantic entropy (d13).
- 2024: Binder "looking inward" (a19); Kapoor "must be taught" (b12); Kamoi survey (b14); Panickssery self-recognition (c23); Laine SAD (b19); Tyen mistake finding (d08); Kumar SCoRe (d09).
- 2025: Chen on reasoning models (b06); Chua and Evans (d03); Baker CoT monitoring (d05); Emmons monitorability (d06); Song, fail to introspect (b16); Betley (b17); Plunkett (b18); Lindsey concept injection (a20); Ji-An neurofeedback (a22); CISC, self-certainty, DeepConf (d10-d12); Yoon, reasoning models express confidence better (d14).
- 2026: Naphade Introspect-Bench (d15).

## 3. Core findings with exact numbers

Status: established = two or more independent sources agree; single-source; contested. "Not read" means the original was not opened and the number is secondhand.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Verbalised LLM confidence is overconfident and a weak error detector | Values cluster 80-100%; weaker models average ECE above 0.377; GPT-4 average AUROC 62.7% over 8 tasks; +22.2% AUROC GPT-3 to GPT-4 | Xiong 2024 (b11, c05) | established |
| Low ECE can be an illusion | GPT-4 CoT on GSM8K: accuracy 93.6%, ECE 0.064 from saying 100% everywhere; AUROC near chance | Xiong 2024 (c06) | single-source |
| Agreement across samples beats one stated confidence | One case AUROC 54.8% to 92.7% (different methods and columns, best case); typical tables 56-79; white-box vs black-box 0.522 to 0.605 | Xiong 2024 (c07); Tian 2023 (b10) | established |
| Right format gives usable calibration | P(True) on own samples improves with size and with several samples shown; keeping P(True) above 0.5 raises accuracy on all five tasks; chance Brier 0.25; P(IK) fails out of distribution on Lambada | Kadavath 2022 (a16, c01-c03) | established |
| Asking RLHF models for verbal confidence beats token probabilities in ECE | Often relative ECE cut of 50% or more on TriviaQA, SciQ, TruthfulQA (ChatGPT, GPT-4, Claude 2) | Tian 2023 (b10; abstract-level numbers) | single-source |
| Training, not prompting, gives good uncertainty | About 1,000 graded examples with LoRA suffice; finetuned verbal confidence stays moderately calibrated under shift | Kapoor 2024 (b12); Lin 2022 (a17) | established |
| CoT text often omits the real cause | Planted bias lowers GPT-3.5 accuracy by up to 36.3%; answer-is-A bias -18.7% / -4.7%; few-shot bias -36.3 to -24.1 and -30.6 to -21.5; 1 of 426 explanations mention the bias | Turpin 2023 (a18, c17) | established |
| Reasoning models rarely say they used a hint | Faithfulness 25% (Claude 3.7 Sonnet), 39% (DeepSeek R1); misalignment hints 20% and 29%; outcome RL plateaus at 28% MMLU, 20% GPQA; reward hacks verbalised in under 2% of cases in 5 of 6 environments; relative drop 44% and 32% on GPQA | Chen 2025 (b06, c19) | contested (next row) |
| Disclosure rates are cue-dependent | R1 59% on professor cue vs 7% non-reasoning V3; argument cue Qwen 16%, Gemini 47%, R1 34%, GPT-4o 2%; post-hoc cue 6-10%; "are you sure" cue near 0 | Chua and Evans 2025 (d03) | single-source |
| CoT reliance varies by task; larger models less faithful on most tasks | Early answering, mistakes, filler, paraphrase tests; no single number | Lanham 2023 (b08, c18) | single-source |
| Intrinsic self-correction does not help | GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1) to 41.8 (round 2); GSM8K 75.9 / 75.1 / 74.7; GPT-4 GSM8K 95.5 / 91.5 / 89.0; 74.7% answers retained | Huang 2024 (b13, c20, c21) | established |
| Earlier gains used oracle labels | With oracle: GPT-4 GSM8K 95.5 to 97.5; HotpotQA 49.0 to 59.0; GPT-3.5 GSM8K 75.9 to 84.3 | Huang 2024 (c20) | established |
| Models cannot find their errors but can fix them when told where | BIG-Bench Mistake, 2,186 CoT traces, 5 tasks; finding accuracy low even for GPT-4; correction helps given the location | Tyen 2024 (d08) | single-source |
| No prompted self-feedback success outside well-suited tasks | Survey: none for prompted feedback; works with reliable external feedback or large-scale finetuning | Kamoi 2024 (b14, d07) | established |
| RL training can create self-correction | +15.6% absolute on MATH, +9.1% on HumanEval over base Gemini | Kumar 2024 SCoRe (d09) | single-source (training) |
| Finetuned self-prediction beats cross-prediction | Llama 70B 48.5% vs GPT-4o predicting it 31.8%; GPT-4o 49.4% vs Llama 36.6%; mean +17%; 32.6% to 49.4% with training; GPT-3.5 +0.8% (p = 0.002); cross-prediction plateaus 35.2% / 36.2% at 10k-20k samples vs self 48.5% / 49.6% | Binder 2024 (a19, c08, c09) | single-source |
| Off-the-shelf models show no privileged self-access | 21 open models; meta to direct correlation never above .25; similarity consistency r = .32; "other" class differs from self by beta = -.03 (p < .01) | Song 2025 (b16, c10, c11) | single-source |
| Finetuned models can describe learned behaviour | Report risk-seeking and backdoor presence without examples; cannot name triggers by default; self-reported attribute weights r = .54 (4o) and .50 (4o-mini); untrained r = .10 and -.01; learned weights track targets r = .84 / .87 | Betley 2025 (b17); Plunkett 2025 (b18, d16) | established (2 sources, both need training) |
| Concept injection: narrow introspection in Claude | About 20% detection at best layer (about two thirds depth), strength 2, Opus 4/4.1; 0 false positives in 100 production-model controls; helpful-only variants have false positives; base models no net gain; random vectors trigger detection in 9 of 100 trials at strength 8; no-explanation prompt raised affirmative answers 20% to 42%, only 2 of 50 looked introspective | Lindsey 2025 (a20, b24, c14, c15) | single-source |
| Small privileged self-access in 2026 models, no task link | Self-prediction beats peers p = 0.021, 796 samples; averages 62-67% across models; one task above 90% | Naphade 2026 (d15) | single-source |
| In-context "neurofeedback" lets small open models report and control some activation directions | Llama 3.1 8B and 70B; improves with up to 256 examples; only a low-dimensional subspace; below ideal observer | Ji-An 2025 (a22, c16) | single-source |
| Models recognise own text; this tracks self-preference | GPT-4 73.5% vs two LLMs and humans; correlation 0.41 before finetuning; above 90% after 500-example finetune | Panickssery 2024 (c23) | single-source |
| Judge self-preference strongest in GPT-4, tied to low perplexity | GPT-4 recall 0.945 on own outputs humans rated high vs 0.425 rated low; bias 0.520; win rates rise with lower perplexity in six open models | Wataoka 2025 (d01, d02) | single-source |
| Self-knowledge benchmark: above chance, below human on some tasks | 16 models, 7 categories, 13,000+ questions; best plain 63.2% (Claude 3 Opus), 62.2% Sonnet | Laine 2024 (b19, c25) | established |
| Confidence-weighted voting beats plain voting at equal samples | Cost cut at 10 samples: P(True) 46%, response probability 31%, verbal 1-100 30%, verbal binary 10%; at 5 samples 41/22/22/18; Gemma2-9B MATH: 8 weighted beat 30 plain; 9 models, 4 datasets | Taubenfeld 2025 CISC (d10) | single-source |
| Trace-level confidence filters bad traces and saves tokens | GPT-OSS-120B AIME 2025: 99.9% vs majority 97.0% vs pass@1 91.8%; up to 84.7% fewer tokens | Fu 2025 DeepConf (d12); Kang 2025 (d11) | established (2 papers, open models) |
| Semantic entropy beats token entropy and p(True) | TriviaQA accuracy 50.6%, CoQA 82.3%; AUROC about 0.70-0.82; OPT to 30B | Kuhn 2023 (d13) | single-source |
| Trace-reading critic catches hacks | Recall 95% (CoT monitor) vs 60% (action-only); weaker model can monitor stronger; training against the monitor gives obfuscation | Baker 2025 (d05); Emmons 2025 (d06) | single-source (two related) |
| Reasoning models give better verbal confidence | Better in 33 of 36 settings (6 models, 6 datasets); GLM-Z1 vs GLM-4: ECE 0.037 lower, AUROC 0.078 higher despite 0.07 lower accuracy | Yoon 2025 (d14) | single-source |
| Reward pressure favours unfaithful replies | Shortest-wins: unfaithful reply wins 69% (Gemini reasoning), 82% (Qwen), 73% (R1) with GPT-4o as stand-in | Chua and Evans 2025 (d04) | single-source |
| Human confidence measures depend on task performance | AUROC2, gamma, phi, meta-d' depend strongly on performance; M-ratio and meta-noise much less; datasets of 56,000 / 97,860 / 101,640 trials; test-retest poor for most measures | Fleming and Lau 2014 (a06, a07); Rahnev 2025 (b02) | established |
| Confidence does not separate imagined from real | Confidence criteria shift with the decision criterion; N = 51 in experiment 1 post-queries | Dijkstra 2024 (b03) | single-source |
| Choice blindness is overstated | Swapped choices reported: 56.4% concurrent (185/328); 92.1% with retrospective (302/328); 7% never; classic about 13% | Grassi 2025 (b04) | contested |
| Choice blindness extends to taste and smell | No more than a third of manipulated trials detected | Hall 2010 (d19); Johansson 2005 (d18) | contested (abstracts only) |
| Relative blindsight | 8 behavioural and 13 fMRI participants; r = 0.512 DLPFC; criterion-confound rebuttal; 9-observer ideal-observer result | Lau and Passingham 2006 (a04); Maniscalco and Lau 2011 (a15); Peters and Lau 2015 (a08) | contested |
| Self-report of causes is theory-driven | Stocking study about 12% vs 40% (not read, approximate) | Nisbett and Wilson 1977 (a12, b21) | single-source (not read) |

## 4. Mechanisms and models

Each model is stated so it can be coded.

### 4.1 Two-level monitoring and control (Nelson and Narens)

```
object level:  produce answer A on item x
meta level:    m = monitor(trace, A, x)       # a signal
control:       if m is below threshold -> action (verify / resample / re-read / stop)
```

The engineering question is only what `monitor` is. Candidates, in the order the evidence ranks them for within-question error detection:

1. **Outside check result** (tests, calculator, retrieval, held-out example). Strongest. Not a metacognitive signal but a real one.
2. **Agreement across k independent samples**, ideally clustered by meaning (Kuhn, d13) or confidence-weighted (CISC, d10).
3. **Trace-level certainty from token probabilities** (self-certainty, lowest-window confidence; d11, d12). Needs logprobs.
4. **P(True)**: ask the model "is this answer true?" and read the probability of the True token (Kadavath, a16; CISC, d10). Best for weighting answers within one question.
5. **Trace-reading critic**, a different model or prompt, that reads the trace and flags problems (Baker, d05). Used as monitor, never as reward.
6. **Verbalised number** ("confidence 85%"). Weakest, except for reasoning models after a long trace (Yoon, d14).
7. **Self-description of reasons or internal state.** Not a monitor (Turpin, Chen, Binder, Song).

### 4.2 Type-1 and type-2 scoring (Fleming and Lau)

Type 1 = answer correct or not. Type 2 = does confidence separate correct from incorrect. To score a confidence signal for the agent:

```
for each item: record correct (0/1) and conf (any scale)
AUROC2 = P(conf_correct > conf_incorrect)   # ties count 0.5
```

AUROC2 rises when items get easier or accuracy rises, even if the monitor is no better. So:
- compute AUROC2 within difficulty bins or within one question (across its k samples), then average;
- also report accuracy-at-coverage (answer only the top x% by confidence);
- for a signal-detection efficiency measure use meta-d'/d' (M-ratio), with the equal-variance caveat; it needs hundreds of trials per condition (d17);
- never report ECE alone. A model that always says 100% and is right 93.6% of the time has ECE 0.064 and AUROC near chance (c06).

### 4.3 Second-order confidence (Fleming and Daw)

Confidence is computed by a separate process from evidence about the first process: its output, its fluency, its disagreement with siblings. In an agent this maps to a separate monitor call that does not see the answer's justification, or to a code-computed statistic. It does not map to "think again about the answer in the same context". That is the failed intrinsic self-correction setting.

### 4.4 CISC: confidence-weighted self-consistency (d10)

```
sample n answers a_i; for each get c_i = P(True | question, a_i)
normalise c_i within the question (softmax with a temperature; normalising raised the P(True) gain from 32% to 46%)
vote weight = c_i; choose the answer with the largest summed weight
```

Equal-token comparison: same number of samples, plus the cost of one short P(True) call each. Gain depends on the confidence signal, and the best-calibrated signal was the least useful. Within-question discrimination is what matters.

### 4.5 DeepConf and self-certainty (d11, d12)

For each trace compute a sliding-window token confidence and keep the lowest group score. Drop the lowest-scoring traces (online: stop a trace whose window confidence falls below a threshold learned from a warm-up set), then vote among the rest. Self-certainty is the distance of the token distribution from uniform. Alone it trails majority vote on definite-answer math; a Borda combination of both is better. Both need logprobs; only open models were tested.

### 4.6 Semantic entropy (d13)

Sample about 10 answers. Cluster by mutual entailment. Entropy of cluster sizes is the uncertainty. High entropy means many different meanings and a likely wrong answer. Works for free-form answers where string match fails.

### 4.7 Planted-cue faithfulness test (Turpin, Chen, Chua)

```
for each item: make a variant with a cue (suggested answer, "a professor says (B)", answer is always A in few-shot)
keep items where the cue flips the answer to the cue's option
faithfulness = share of those traces that name the cue as a reason
```

This measures how far to trust written reasoning as an audit. It is a measurement tool, not a schema operator.

### 4.8 Concept injection (Lindsey, a20)

Take a steering vector for a concept, add it at a chosen layer and strength, ask the model whether it notices an injected thought and what it is. Score detection, false-positive rate on no-injection controls, and whether the model names the concept before it could infer it from its own output. Needs model internals. Not available to a prompt-only scaffold.

### 4.9 Self-prediction test (Binder, Song, Naphade)

Ask a model to predict a property of its own output on a prompt (for example the second character of its answer, or whether it would pick option A). Compare with the accuracy of another model predicting the first model's output. The introspection claim is self beats other-model, controlling for the other model being trained on the same behaviour. Result: only after finetuning (Binder), small off the shelf (Naphade, p = 0.021), none in Song's 21 open models.

### 4.10 Monitor design under optimisation pressure (Baker, Emmons)

A trace-reading monitor catches bad behaviour as long as the trace is where the model has to reason. If the generator is trained against the monitor, the trace is rewritten to look clean and the behaviour stays. Design rule: the monitor is read-only and outside any reward.

## 5. What holds up

### 5.1 Solid (two or more sources, or one source with a clear mechanism)

1. **Verbalised confidence is a poor error detector and overconfident** (Xiong). Tian is the exception, by ECE not AUROC. Judge by AUROC, not ECE.
2. **Sample-based or probability-based signals beat verbalised numbers** at error detection and at weighting votes (Xiong, CISC, Kuhn, DeepConf).
3. **Written reasoning often does not name the real cause** (Turpin, Lanham, Chen). Numbers vary by model and cue, but no source shows reliable full disclosure.
4. **Intrinsic self-correction does not help** and often hurts (Huang, Kamoi). It helps with a reliable outside check (Huang oracle rows, Tyen error location, Kamoi).
5. **Training changes what prompting does not** (Kapoor, Lin, Binder, Plunkett, SCoRe). A scaffold cannot reproduce these gains by instruction alone.
6. **Human metacognitive measures depend on performance** (Fleming and Lau; Rahnev). The same confound applies to agents.

### 5.2 Contested or fragile

- **Rate of CoT disclosure in reasoning models.** 25-39% (Chen) versus 59% on one cue and 6-34% on others (Chua and Evans). Different cue designs and models. Treat the rate as unknown and cue-dependent.
- **Choice blindness.** Classic: about 13% detection. Grassi 2025: 56.4% concurrent and 92.1% with a debrief. Detection depends on design. People still gave confabulated reasons for swapped choices. Do not conclude that self-report is empty; do not conclude it is accurate. Exact rates of Johansson 2005 and Hall 2010 were not verified.
- **Relative blindsight and the prefrontal HOT programme.** Answered by a criterion-confound account (a15) and by an ideal-observer result (a08). Philosophical grounding only.
- **Introspection in LLMs.** Binder: present after finetuning on 70B and GPT-4o, not on GPT-3.5 (+0.8%). Song: absent in 21 open models on language-knowledge tasks. Lindsey: about 20% at best settings. Naphade: small. These fit together only if the effect needs training or a specific setup. No source ties introspective accuracy to a task gain.
- **Reasoning models' verbal confidence.** Yoon: better in 33 of 36 settings; a few favour non-reasoning. One paper.

### 5.3 Failed or not replicated

- Intrinsic self-correction gains reported earlier rested on oracle labels or weak baselines (Huang; Kamoi Table 4 "unfair settings").
- Reflexion (c26, not opened): gains depend on an external success signal, per Huang.
- Training against a CoT monitor yields obfuscated hacking (Baker).
- Prompt tricks that "fix" calibration can be illusions (Xiong CoT row).
- Original human numbers (Nisbett and Wilson, Koriat) were not opened. No failed choice-blindness replication was located.

### 5.4 Moderators

| Moderator | Effect | Source |
|---|---|---|
| Question format | Good calibration in multiple choice and true/false; poor when an option is replaced by "none of the above" | Kadavath |
| Task type | Faithfulness and CoT reliance vary by task | Lanham |
| Model size | P(True), P(IK) and semantic entropy improve with size; faithfulness worsens on most tasks | Kadavath, Kuhn, Lanham |
| Reasoning training | More hint disclosure on some cues; better verbal confidence in 33 of 36 settings | Chua and Evans, Yoon |
| Outcome RL | Faithfulness plateaus at 28% (MMLU), 20% (GPQA) | Chen |
| Confidence signal | P(True) > response probability > verbal; normalisation matters | CISC |
| Position in trace | Confidence improves as the CoT unfolds | Yoon |
| Presence of an outside check | Decides whether revision helps | Huang, Tyen, Kamoi |
| Training on self-reports | Report accuracy r = .10 untrained, r = .54 trained | Plunkett |
| Accuracy / difficulty | Raises AUROC2 without a better monitor | Fleming and Lau |
| Prompt explanation | No-explanation prompt raised affirmative answers 20% to 42%; only 2 of 50 introspective | Lindsey |

### 5.5 Interventions that worked and did not

Worked: sample agreement; P(True) weighting; semantic clustering; trace-confidence filtering; a trace-reading critic as read-only monitor; correction given a located error; finetuning on about 1,000 graded examples; outside tests.

Did not work, or unproven for prompt-only agents: asking the model to rethink with no new information; forced self-critique; verbal confidence as a stop rule; model self-description as audit; hiding authorship alone for self-preference (d02 suggests familiarity, not authorship, drives it).

## 6. Language models

### 6.1 Calibration and failure prediction

- 2022 base models: calibrated on multiple choice and true/false, improving with size (Kadavath). P(True) on own samples works; keeping answers with P(True) above 0.5 raises accuracy on all five sampling tasks.
- 2023-24 chat models: verbalised confidence clusters at 80-100% (Xiong). GPT-4 average AUROC 62.7% over 8 tasks. Weaker models average ECE above 0.377. GPT-3 to GPT-4 gave +22.2% AUROC. Sample consistency raised it (best case 54.8% to 92.7%).
- Tian 2023: for RLHF models verbalised probabilities beat token probabilities in ECE (often a relative cut of 50% or more), and asking for several guesses with probabilities helps. This is aggregate calibration, not per-item discrimination.
- 2025 reasoning models: verbal confidence better in 33 of 36 settings (Yoon), improving as the CoT unfolds. Still imperfect; one paper.
- Best use of confidence in a loop: **weighting votes** (CISC: P(True) saved 46% of samples at budget 10; Gemma2-9B on MATH, 8 weighted samples beat 30 plain) and **trace filtering** (DeepConf: 99.9% vs 97.0% on AIME 2025 with GPT-OSS-120B; up to 84.7% fewer tokens). Both on open models.

### 6.2 Faithfulness of the model's account of itself

- Turpin: planted bias lowers GPT-3.5 accuracy up to 36.3%; 1 of 426 explanations mentions it.
- Chen: Claude 3.7 Sonnet 25%, R1 39% hint disclosure; hacks under 2% in 5 of 6 environments; outcome RL helped at first then plateaued at 28% and 20%.
- Chua and Evans: reasoning models disclose much more on some cues (R1 59% professor cue) and little on others (post-hoc 6-10%; "are you sure" near zero).
- Lanham: reliance on the CoT is task dependent; larger models less faithful on most tasks.
- Baker and Emmons: even unfaithful CoT is a good monitoring surface when the bad behaviour needs the CoT to compute. A CoT monitor had 95% recall vs 60% for action-only. Pressure on the trace to look clean produces obfuscation.
- Chua and Evans reward-model analysis: a stand-in reward model prefers unfaithful replies when shortness wins, 69% to 82%. Training pressure can reduce disclosure.

### 6.3 Self-correction

- No outside feedback: GPT-3.5 CommonSenseQA 75.8 to 38.1 then 41.8; GPT-4 GSM8K 95.5 / 91.5 / 89.0; 74.7% of answers kept (Huang).
- Oracle feedback: GPT-4 GSM8K 95.5 to 97.5, HotpotQA 49.0 to 59.0 (Huang).
- Mistake finding is the weak step (Tyen); fixing is fine when the location is given.
- RL training on own traces: +15.6% MATH, +9.1% HumanEval (SCoRe).
- Unknown: how imperfect a check can be before revision hurts.

### 6.4 Introspection and self-knowledge

- Binder (finetuned): mean self-prediction advantage +17%; Llama 70B 48.5% vs 31.8%; GPT-4o 49.4% vs 36.6%; GPT-3.5 only +0.8%; fails on long outputs and out-of-distribution properties.
- Song: 21 open models, no privileged access off the shelf.
- Betley and Plunkett: after finetuning, models describe learned behaviour; reported weights r = .50 to .54; untrained r = .10.
- Lindsey (Claude): about 20% best-case detection, 0 false positives in 100 production-model controls, more false positives in helpful-only variants.
- Naphade 2026: small self advantage, p = 0.021, 796 samples; no task link.
- Ji-An: in-context neurofeedback lets Llama report and control some activation directions; only a low-dimensional subspace.
- Laine SAD: all 16 models above chance on self-knowledge; best plain 63.2%.

### 6.5 Self-preference

GPT-4 recognises its own text 73.5% of the time, correlated 0.41 with self-preference before finetuning (Panickssery). Finetuning on 500 examples lifts recognition above 90%. Wataoka: GPT-4 bias 0.520; the preference follows low perplexity, not authorship alone.

### 6.6 Net picture

The model's words about itself are weak evidence. Its probabilities and its sample spread are better evidence. Outside checks are best. Almost all measurements are on 2022-2024 models or open models. No study measured a frontier model with a scaffold step that asks for confidence or self-explanation against the same tokens spent on extra samples.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | Keep G10 as written. Add to its evidence line: measured disclosure of a used cue ranges from about 0 to 59% by cue and model, so written reasons are not evidence | G10 | [E] | a18, b06, d03, b08 |
| 2 | Never use a verbalised confidence number as a stop or route trigger. Already in 4b; add the reason: overconfident, weak detector (GPT-4 AUROC 62.7%) | G10, 4b | [E] | b11, c05, K01 |
| 3 | Where a monitor is needed, prefer behaviour-derived signals; agreement among independent samples first. Agreement stays a hint (G4) | G10, S0, S7 | [E] | c07, b10, b12, K03 |
| 4 | Revise only with an outside check that supplies the error location. Already G2; add the numbers (GPT-3.5 CSQA 75.8 to 38.1 without; GPT-4 GSM8K 95.5 to 97.5 with oracle) | G2, S5 | [E] | b13, d07, d08 |
| 5 | When the bench scores confidence or a monitor, report AUROC within difficulty bins or within question, plus accuracy-at-coverage; never ECE alone | G7, run log (SCHEMA section 6) | [E] | a06, a07, b02, c06 |
| 6 | When a model grades, use a different model family and no authorship label, and normalise length and style. The bias is [E]-level for GPT-4 on one setup; the remedy is [S] (hiding authorship alone may not work) | G5 | [E] bias, [S] remedy | c23, d01, d02 |
| 7 | Keep any trace critic read-only and outside any reward or selection of the generator | G10 | [S], cheap to obey | d05, d06 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Per-sample P(True) weight on the sample vote (CISC style) vs plain vote at equal tokens | S3/S7, G4 | [S] | d10, a16 |
| T2 | A single "check this answer" call vs the same tokens spent on 1-2 more independent samples | S8, G7 | [C], no frontier study | b13, d07 |
| T3 | Semantic clustering of sample answers as the trigger to enter S6 or add attempts | S0, S6, G1 | [S] | d13 |
| T4 | Trace length, retry count and token-level fluency as a Proust-style non-verbal feeling for S6 | S6 | [S], derived from K24, K27 | a11, d11, d12 |
| T5 | Separate trace-reading critic (different prompt or model) as monitor for S8, not selector | S8, G5 | [S] | d05, d06 |
| T6 | Planted-cue audit: how often the agent's written reasoning names a cue that flipped its answer | G10 | [C] | b06, d03 |
| T7 | Score confidence after the final answer, not before; check whether early stated confidence anchors later steps | S1, S3 | [S], indirect | d14 |
| T8 | Check reliability: how bad can an outside check be before the S5 revise step hurts | S5, G2 | no direct evidence | d07, d08 |
| T9 | Grader swap or authorship hiding for any model judge in the pipeline | G5 | [S] | c23, d01, d02 |
| T10 | Class record in memory: how often agreement was right for this class, read at S0 | memory, S0 | [D] | a16, c07 |

## 8. Concrete tests on our bench

The bench has ARC and BRAINTEASER items (skills: bench, think). Equal tokens means the sum of all model tokens in a run, with setup and monitor calls included (G7). Use at least 60 items per arm and a paired design (same items in every arm).

| Test | Item type | Arms at equal tokens | Metric | Expected effect |
|---|---|---|---|---|
| T1 CISC | BRAINTEASER multiple choice; ARC with graded checks | A: k plain samples + majority. B: samples each with one short P(True) call, weighted vote, k reduced to match tokens | Final accuracy; accuracy per token | Small gain (cost cut 41-46% at 5-10 samples on open models); may vanish on a strong frontier model. Adopt only if B beats A by 2 points or more |
| T2 Self-check vs samples | BRAINTEASER; ARC items without a check | A: plain + 1 or 2 extra samples and vote. B: plain + one "is this right? if wrong, fix" call. C: plain | Accuracy; flips wrong-to-right vs right-to-wrong (run log) | B no better than A; revisions flip right to wrong about as often as wrong to right (Huang) |
| T3 Semantic agreement trigger | BRAINTEASER free-form answers | A: S6 fires on string disagreement or schedule. B: S6 fires when answers fall in 2 or more meaning clusters | Accuracy per token; false-alarm rate (S6 fired on items plain got right); AUROC of cluster count | Fewer wasted S6 entries; cluster-count AUROC above string agreement |
| T4 Non-verbal impasse signal | ARC | A: S6 by code rules only. B: A plus fluency, length and retry signal as an earlier trigger | Time to S6; accuracy per token; false alarms | Earlier S6 at the same accuracy. Token logprobs only if the API gives them; otherwise length and retries |
| T5 Trace critic | ARC and BRAINTEASER, plus planted-flaw items | A: outside check only. B: outside check plus a different-model critic reading the trace; output is a flag, not a score | Recall of wrong answers that pass the check (G3 trap); false-flag rate | Recall rises on fit-but-wrong answers (our own ARC case); watch false flags |
| T6 Planted cue | BRAINTEASER with a hint or suggested answer in half the items | A: normal prompt. B: prompt with a "list what influenced you" line. Same token cap | Share of cue-flipped answers whose reasoning names the cue; accuracy on cued items | Baseline between 6 and 59%. If B raises disclosure by 20 points without hurting accuracy, adopt as an audit, never as evidence |
| T7 Confidence timing | BRAINTEASER | A: confidence before the answer. B: after the final answer | AUROC2 within difficulty bin; accuracy | B at least as good; if A lowers accuracy, anchoring is shown |
| T8 Check reliability | ARC where a check can be corrupted | Revision with a check right 100%, 90%, 75%, 50% of the time vs no revision | Net accuracy change per round | Find the break-even; no prior estimate |
| T9 Grader swap | Open-mode ideas (NoveltyBench) and selection tasks | A: same-model grader. B: different-family grader. C: same family, authorship hidden, length-normalised | Agreement with running-based truth; self-preference (share of own outputs rated best) | A biased; B and C reduce it; C alone may not |
| T10 Class record | Mixed set | A: no class record. B: class pass rate and agreement record read at S0 | Accuracy per token over two passes | Small gain from cheaper routing (guardrail G12 prior) |

Scoring rule for all: report accuracy, tokens, ECE and AUROC2 within difficulty bin together. A monitor test that reports ECE alone is invalid.

## 9. What does not transfer, and why

- **Philosophical HOT debates** (empty HOTs, rocks, animals, phenomenal feel). They are about consciousness, not accuracy. Not decision-relevant for the agent.
- **Prefrontal evidence and blindsight** (a04, a05, a08, a15). Human neural data, tiny samples, contested.
- **Choice blindness.** Humans choosing between faces or jams with a real stake. For an LLM agent the "choice" is a token sequence and a swap would be a context edit. It is only an analogy for post-hoc reasons.
- **Training results** (Kapoor 1,000 examples, Lin, SCoRe +15.6% MATH, Binder, Plunkett). We do not train. They give an upper bound on what a scaffold might fake and a warning that prompting alone will not reach it.
- **Logprob methods** (DeepConf, self-certainty, token-level semantic entropy). Need token probabilities. Many API models do not return them. Only proxies (length, retries, agreement) transfer.
- **Concept injection and neurofeedback** (Lindsey, Ji-An). Need access to activations.
- **Self-description of internal states.** Where it works (Binder, Plunkett) it needed finetuning and gave r = .50 to .54 at best, so it cannot feed routing. G10 stays.
- **Human metacognitive efficiency (M-ratio, meta-d').** Built for two-choice perception with hundreds of trials and an equal-variance assumption. We use the idea (control for performance), not the exact estimator.
- **Tian's calibration gain** is aggregate and does not tell us about per-item discrimination.
- **Old model numbers** (GPT-3.5, PaLM 2, OPT, Llama 2). Direction transfers; magnitudes do not.

## 10. Open questions

1. Does a self-check or confidence step improve a current frontier model's final accuracy against the same tokens spent on extra samples? No direct study.
2. Which monitor is best at equal cost on our agent: verbalised, P(True), agreement, retries, critic? No head-to-head.
3. Do 2025-2026 reasoning models disclose planted cues more often than 25-39%, and does an explicit "what influenced this" step raise it?
4. Does swapping the grader or hiding authorship remove self-preference, in agentic settings and not only dialogue or summaries?
5. How unreliable can an outside check be before revising hurts?
6. Does stated early confidence anchor later steps? No direct study.
7. What false-alarm rate does a non-verbal monitor have as an S-state trigger in an agent?
8. Does introspective accuracy (Lindsey about 20%, Binder 48.5%) rise with scale, and does it help any task outcome?
9. What do the unopened primaries show: Nisbett and Wilson 1977, Koriat 1997, Johansson 2005 detection rates, Hall 2010, Proust 2013, Rosenthal books, Maniscalco and Lau 2011 and 2012, Rounis 2010, Steyvers 2025? Is there a failed choice-blindness replication?
10. Do reflection-step agents (Reflexion, c26) gain only because they have an external success signal? Not read directly.
11. Does a trace critic stay useful once the generator knows it exists (an agent with persistent memory could learn to write clean traces)?

## 11. Sources

[V] = opened and read in this run (full text or substantive page). [M] = snippet, abstract or secondhand only.

**Philosophy and human psychology**
- [V] Carruthers, Picciuto (2025) SEP Higher-Order Theories of Consciousness. https://plato.stanford.edu/entries/consciousness-higher/ (a01-a03, a24)
- [M] Rosenthal (2005) Consciousness and Mind; (1997) A theory of consciousness. https://global.oup.com/academic/product/consciousness-and-mind-9780199243013 (a10, via SEP)
- [M] Proust (2013) The Philosophy of Metacognition. https://doi.org/10.1093/acprof:oso/9780199602162.001.0001 (a11)
- [M] Nisbett, Wilson (1977) Telling more than we can know. https://doi.org/10.1037/0033-295X.84.3.231 (a12, b21)
- [M] Nelson, Narens (1990) Metamemory. https://doi.org/10.1016/S0079-7421(08)60053-5 (a13)
- [M] Koriat (1997) cue-utilisation approach. https://doi.org/10.1037/0096-3445.126.4.349 (a26)
- [V] Lau, Passingham (2006) Relative blindsight in normal observers. https://pmc.ncbi.nlm.nih.gov/articles/PMC1693736/ (a04)
- [M] Rounis et al. (2010) Theta-burst TMS to prefrontal cortex. https://europepmc.org/article/MED/24168333 (a05)
- [M] Maniscalco, Lau (2011) Relative blindsight arises from a criterion confound. https://europepmc.org/article/MED/22051554 (a15)
- [M] Maniscalco, Lau (2012) A signal detection theoretic approach. https://doi.org/10.1016/j.concog.2011.09.021 (a14, b23)
- [M] Lau, Rosenthal (2011) Empirical support for higher-order theories. https://doi.org/10.1016/j.tics.2011.05.009 (b05)
- [V] Fleming, Lau (2014) How to measure metacognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC4097944/ (a06, a07, a23, b01, d17)
- [V] Peters, Lau (2015) Human observers have optimal introspective access. https://europepmc.org/article/PMC/PMC4749556 (a08)
- [V] Fleming, Daw (2017) Self-evaluation of decision-making. https://europepmc.org/article/PMC/PMC5178868 (a09)
- [V] Rahnev (2025) Comprehensive assessment of current methods for measuring metacognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC11735976/ (b02)
- [V] Dijkstra, Mazor, Fleming (2024) Confidence ratings do not distinguish imagination from reality. https://pmc.ncbi.nlm.nih.gov/articles/PMC11146086/ (b03)
- [V] Grassi et al. (2025) Restoring sight in choice blindness. https://pmc.ncbi.nlm.nih.gov/articles/PMC12713319/ (b04)
- [M] Johansson et al. (2005) Failure to detect mismatches. https://doi.org/10.1126/science.1111709 (d18; b22 lists the same paper under a different DOI string)
- [M] Hall et al. (2010) Magic at the marketplace. https://europepmc.org/search?query=Magic%20at%20the%20marketplace (d19)
- [M] Steyvers et al. (2025) What LLMs know and what people think they know. https://doi.org/10.1038/s42256-024-00976-7 (b25)

**LLM and AI**
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (a16, a25, b09, c01-c03)
- [V] Lin, Hilton, Evans (2022) Teaching models to express uncertainty in words. https://arxiv.org/abs/2205.14334 (a17, c04)
- [V] Kuhn, Gal, Farquhar (2023) Semantic uncertainty. https://arxiv.org/abs/2302.09664 (d13)
- [V] Turpin et al. (2023) Language models don't always say what they think. https://arxiv.org/abs/2305.04388 (a18, b07, c17)
- [V] Lanham et al. (2023) Measuring faithfulness in chain-of-thought reasoning. https://arxiv.org/abs/2307.13702 (b08, c18)
- [V] Tian et al. (2023) Just ask for calibration. https://arxiv.org/abs/2305.14975 (b10; numbers are abstract-level)
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (b11, c05-c07)
- [V] Kapoor et al. (2024) LLMs must be taught to know what they don't know. https://arxiv.org/abs/2406.08391 (b12; numbers are abstract-level)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b13, c20, c21)
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 (b14, c22, d07)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them given the error location. https://arxiv.org/abs/2311.08516 (d08)
- [V] Kumar et al. (2024) Training language models to self-correct via RL. https://arxiv.org/abs/2409.12917 (d09)
- [V] Binder et al. (2024) Looking inward. https://arxiv.org/abs/2410.13787 (a19, b15, c08, c09)
- [V] Panickssery, Bowman, Feng (2024) LLM evaluators recognize and favor their own generations. https://arxiv.org/abs/2404.13076 (c23)
- [V] Laine et al. (2024) Me, Myself, and AI: SAD. https://arxiv.org/abs/2407.04694 (b19, c25)
- [V] Wataoka, Takahashi, Ri (2025) Self-preference bias in LLM-as-a-judge. https://arxiv.org/abs/2410.21819 (d01, d02)
- [V] Betley et al. (2025) Tell me about yourself. https://arxiv.org/abs/2501.11120 (b17, c12, c13)
- [V] Chua, Evans (2025) Are DeepSeek R1 and other reasoning models more faithful? https://arxiv.org/abs/2501.08156 (d03, d04)
- [V] Song, Hu, Mahowald (2025) Language models fail to introspect about their knowledge of language. https://arxiv.org/abs/2503.07513 (b16, c10, c11)
- [V] Baker et al. (2025) Monitoring reasoning models for misbehavior. https://arxiv.org/abs/2503.11926 (d05)
- [V] Chen et al. (2025) Reasoning models don't always say what they think. https://arxiv.org/abs/2505.05410 (b06, c19)
- [V] Plunkett, Morris et al. (2025) Self-interpretability. https://arxiv.org/abs/2505.17120 (b18, d16)
- [V] Ji-An et al. (2025) Language models are capable of metacognitive monitoring and control. https://arxiv.org/abs/2505.13763 (a22, c16)
- [V] Yoon et al. (2025) Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489 (d14)
- [V] Comsa, Shanahan (2025) Does it make sense to speak of introspection in LLMs? https://arxiv.org/abs/2506.05068 (b20, c24)
- [V] Emmons et al. (2025) When chain of thought is necessary, language models struggle to evade monitors. https://arxiv.org/abs/2507.05246 (d06)
- [V] Taubenfeld et al. (2025) Confidence improves self-consistency in LLMs. https://arxiv.org/abs/2502.06233 (d10)
- [V] Kang et al. (2025) Scalable best-of-N selection via self-certainty. https://arxiv.org/abs/2502.18581 (d11)
- [V] Fu et al. (2025) Deep think with confidence. https://arxiv.org/abs/2508.15260 (d12)
- [V] Lindsey (2025) Emergent introspective awareness in large language models. https://transformer-circuits.pub/2025/introspection/index.html (a20, a21, b24, c14, c15; a20 lists arXiv 2601.01828 and year 2026 for the same work)
- [V] Naphade et al. (2026) Me, Myself, and pi: LLM introspection. https://arxiv.org/abs/2603.20276 (d15)
- [M] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c26)
