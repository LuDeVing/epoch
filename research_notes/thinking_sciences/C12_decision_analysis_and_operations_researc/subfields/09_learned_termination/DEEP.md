# Learned termination: deep document

*Subfield C12.09. Folder: `research_notes/thinking_sciences/C12_decision_analysis_and_operations_researc/subfields/09_learned_termination`. Built from evidence_a-d.jsonl, claims.jsonl (K01-K24) and critique.md. Evidence ids (a01, b05, d06 ...) refer to those files. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Date of the evidence: 2026-11-03.*

Ground rules for reading this document:
- Almost every result here is from 2023-2026 LLM work. There is no human-subject literature in this folder and no CaRT replication.
- Several papers were read in full (CaRT, DEER, ESC, Adaptive-Consistency, probing, Answer Convergence, ESTAR, Judged Useless). Others were read at abstract level only. Section 3 and section 11 say which.
- Evidence files overlap. a15/b08/c13 are one paper (ESC), a16/b06/c14 one paper (Adaptive-Consistency), a13/b10/c11 one paper (probing), a12/b12/c06 one paper (DEER), a14/b14/c12 one paper (Answer Convergence). Their agreement is not independent evidence. Independence counts here are by distinct paper.

## 1. What it is

Learned termination is the decision to stop: stop asking questions, stop thinking, stop sampling, stop refining, stop calling tools, and commit to an answer. The question is "do I know enough yet?"

Three things make it a separate topic from "get the answer right":
1. It is a different skill from solving. QuestBench (b22) shows models solve a fully specified problem at 80-90% but pick the one missing variable at only 40-50% on logic and planning items. Joren et al. (a20) show large models answer well when context is sufficient, but give wrong answers instead of abstaining when it is not.
2. Models are bad at it in both directions. They overthink (Chen et al., b16: first round correct in over 92% of cases on easy sets, yet far more tokens spent) and they underthink (Wang et al., b17: wrong answers use 225% more tokens and 418% more thought switches). A tool-using agent judges a failing source useless 97-100% of the time and still keeps querying it (d01).
3. It has a cost side. Every extra step costs tokens. The rational rule is the classical one: stop when the expected gain of one more step falls below its cost (Wald 1945; Chow and Robbins; a09, c23, not opened).

Formal statement used by CaRT (a01). At each step t the policy sees prompt x, thoughts z_0:t and observations o_0:t. It picks continue or terminate. The goal is to maximise the expected reward of the final answer, discounted by gamma per step:

    max E[ sum_t gamma^t * 1{a_t = terminate} * R(y, y*) ],  gamma in (0,1]

This is a value-of-continuing decision, not a confidence read-out.

Four kinds of unit that can be stopped, which later sections keep apart:
- A reasoning chain (stop thinking): DEER, Answer Convergence, probes, EAT, LYNX, S-GRPO, ESTAR, JET.
- A sampling run (stop drawing attempts): Adaptive-Consistency, ESC, BEACON, Pandora's Box.
- A set of parallel traces (stop single traces or the vote): DeepConf, short-m@k, PeerConf, MARS.
- An interaction (stop asking and answer): CaRT, MediQ, UoT, Judged Useless.

Where it sits in our schema: S0 (gate: how much thinking this class deserves) and S8 (verify and submit), plus the budget side of G7, G11 and G12. Our agent cannot be fine-tuned and often runs on a closed API model, so the transferable parts are the training-free ones and the design lessons of the learned ones.

## 2. History and theories in depth

**Classical sequential analysis and optimal stopping (a09, c23; not opened).** Wald's sequential probability ratio test (1945) stops when a likelihood ratio crosses a threshold set by the two error costs. Chow and Robbins give the general form: stop when the expected gain from one more observation drops below its cost. The secretary problem gives the 1/e rule for a single irreversible choice. Common assumption: known dynamics. CaRT's authors say this limits use in open-ended settings. None of this was verified from the original papers this session.

**Learned halting in neural nets, 2016-2021 (c20, c21; abstracts only).** Graves (2016) Adaptive Computation Time added a halting unit so a recurrent net chooses how many steps per input. Big gains on synthetic parity, logic, addition and sorting; little on character-level language modelling. PonderNet (Banino et al., 2021) made halting probabilistic and trainable end to end; it beat ACT on a synthetic task, matched state of the art on a QA set with less compute and extrapolated. These are ancestors of "learn when to stop", but they stop internal computation, not an agent's behaviour.

**Self-consistency and sampling-level stopping, 2023-2024.** Self-consistency draws N chains and votes. Adaptive-Consistency (Aggarwal et al. 2023, b06, b07) and Early-Stopping Self-Consistency (Li et al. 2024, b08) added a stop test on the answer distribution, with no training. These are the best-supported "when to stop" results for LLMs.

**Overthinking and underthinking, Dec 2024 to Jan 2025.** o1-like models arrived. Chen et al. (b16) named overthinking ("2+3=?" got 1,953% more tokens than a conventional model). Wang et al. (b17) named the opposite, underthinking. Together they say the stop point is wrong in both directions, depending on difficulty.

**Training-free early exit for reasoning models, 2025.** DEER (b12), Answer Convergence (b14), EAT (c08), thought calibration (c10), probing for self-verification (b10), LYNX (c09). Common idea: force or read a trial answer partway through the chain and stop when it is stable or confident.

**Training the stop decision, 2025-2026.** AdaptThink (b18) chooses think or no-think up front. S-GRPO (d04), JET (d03) and ESTAR (d05) train the exit with RL or SFT plus RL. CaRT (b01-b05) trains a separate stop judge on counterfactual pairs. The key CaRT idea is data design, not the learning algorithm: pair a prefix where stopping is right with a minimally edited copy where stopping is wrong.

**Interactive information seeking.** UoT (b21) picks the next question by simulated information gain. MediQ (c15) shows plain prompting to ask makes models worse and an abstention module repairs it. QuestBench (b22) shows the "what is missing" skill is weak. CaRT adds a trained stop decision. Its authors state that what to ask and when to stop should be learned together, and test only the stop side.

**Agentic stop rules outside the model, 2026.** Judged Useless, Queried Anyway (d01, d02) shows a harness-level rule (force an answer after 5 useless results in a row) beats the model's own judgment, with a pre-registered replication on 300 fresh questions. Semantic early-stopping (d07) stops writer-critic loops on embedding convergence.

**Competing accounts of why stopping helps (b25, K09, K15).**
- (a) Answers converge early and later steps are redundant (Answer Convergence, Chen).
- (b) Long chains are worse: shorter chains in the same question are more often right (Hassid, a18).
- (c) Late reflection adds noise (DEER).
- (d) Bad runs switch thoughts too often (Wang).
- (e) Extra thinking adds output variance that first looks like gain and then hurts (c18, abstract only).
- (f) Inverse scaling on crafted tasks (c19, abstract only).
No experiment separates these. Length is confounded with difficulty; Hassid controls for it by comparing within one question.

## 3. Core findings with exact numbers

Status: [E], [S], [C] as above. Most rows give what was read; "abs" means abstract only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| CaRT: a stop judge trained on counterfactual pairs plus reasons beats base and plain SFT on stop timing | Medical arm: Qwen2.5-3B-Instruct; 1,233 problems before filtering, 1,133 train after (121 ID holdout, 93 OOD per appendix; main text says 100 ID and 200 dermatology). Labels: Llama-3.1-8B success over 50 generations per prefix; optimal stop = first turn where success rises by at least 0.5. CIs over 3 seeds x 30 evals. Success about 0.24-0.37. Bar values in figures only | Liu, Qu, Schneider, Singh, Kumar 2025 (a01-a05, b01, d19) | [S] |
| CaRT math arm | 2,000 DeepScaleR problems, Qwen3-1.7B traces, 10 episode prefixes each; eval AIME 2025 (30 items), 3 seeds x 16 evals; higher success at fewer tokens than base and SFT (figure only) | same (a06, b02) | [S] |
| Counterfactuals are the biggest ingredient; reasons add a smaller gain | Ablations: -CF, -reason, -both, SFT with 5/10/15/20% terminate ratio. Without CF, Qwen3-1.7B did worse than the fixed budget. Verbalised confidence (threshold 0.8) helped SFT and SFT+CF, no significant gain on full CaRT | same (a07, b03, c03) | [S] |
| Plain SFT learns a length shortcut | SFT stops more as the dialogue grows; CF makes stop probability spike at true information jumps | same (b03) | [S] |
| CaRT probe table (102 held-out counterfactual conversations, 70/30 split, about 31 test items) | Direct accuracy: base 0.567, CaRT minus reasoning 0.849, full CaRT 0.663. Logistic-probe test accuracy 0.581 (CI 0.408-0.736), 0.645 (0.469-0.789), 0.774 (0.602-0.886). Probe train accuracy 1.000, 1.000, 0.986. Reasoning raises probe accuracy but lowers direct accuracy vs CaRT minus reasoning | same (b04, c03; corrected in critique) | [S], weak |
| OOD collapse | On dermatology, base and SFT fell below a naive fixed-question-count stop; CaRT stayed above with a smaller margin | same (b04, c04, d19) | [S] for CaRT; wider picture in K03 |
| CaRT RL variant (GRPO, +1/-1 decision reward) | Longer conversations, no math gain | same (b05, c04) | [S] |
| Other RL rewards did work in math | S-GRPO: length -35.4 to -61.1%, accuracy +0.72 to +6.08. JET: 1.5B Olympiad +4.6% accuracy at -46.3% length; 1.5B average length -39.7%; 7B AIME24 54.0 (+2.7). ESTAR (Qwen3-8B): MATH500 93.8 at 635 tokens vs AdaptThink 93.8 at 2,130; GPQA transfer 98.9-100% accuracy retained over 6 models, length x2.0-x3.8 shorter. Steep length penalties truncate hard items: LCR1 on 7B MATH500 cut length over 50% and lost 4.4 points | Dai 2025 (d04, abs); Han 2026 (d03); ESTAR 2026 (d05) | [C] vs CaRT RL |
| ESTAR-LITE (classifier, tau 0.9) | USMLE 77.53 to 76.83, 2,412 to 549 tokens; MATH500 94.0 to 93.2, 3,951 to 2,019; AIME 70.00 to 66.67, 6,123 to 3,045 (95.2% retained). Lowering tau from .99 to .80 costs 3.8 points. No false-stop rate; no error bars | d05 | [S] |
| Overthinking | First round correct in over 92% of cases; first round under 60% of tokens; example 39 of 901 tokens (4.3%); 1,953% more tokens than a conventional model on "2+3"; self-training cut MATH500 tokens 48.6% on QwQ-32B-Preview at equal accuracy | Chen 2024 (a10, b16); the 92% and 1,953% figures were not re-checked | [E] direction |
| Answer is reached early | Final answer reached after about 60% of reasoning steps; consistency stop cuts over 40% of tokens on NQ and raises accuracy; one run 755.1 to 418.9 tokens (-44%) at 0.2% accuracy drop; GPQA -39.2%; window k 20-30 saturates accuracy, 10-20 balances cost. Smaller gains on MATH-500, GPQA, AIME | Liu and Wang 2025 (b14, a14) | [E] |
| Stop-quality taxonomy | Stop Late 63.6%, Stop Perfectly 18.2%, Unfaithful but Correct 3% (one model, one figure) | b15 | [S] |
| DEER: trial answer at "Wait"-type transitions, exit on confidence | 11 reasoning models, 10 benchmarks: CoT -19.1% to -80.1%, accuracy +0.3 to +5.0. Qwen3-14B 83.7 vs 82.8 at 57.1% of tokens; QwQ-32B 84.0 vs 82.6 at 80.9%. Math and science -61.5%, code only -19.9%. AIME24 43.35 to 51.05 on the R1-Distill series | Yang 2025 (b12, a12, c06) | [E] |
| Path-deviation paper: answer-confidence exit over-truncates (spurious confidence silences self-correction) | Eight models; compared mainly with vanilla and DEER; larger accuracy gain over vanilla, smaller token savings than aggressive methods | 2026 RPDI-E (c07) | [C] vs DEER |
| EAT: entropy after the stop token | 12-22% fewer tokens, no accuracy harm (MATH500, AIME2025); up to 21% with a proxy model for black-box reasoners | c08 | [S] |
| LYNX: probe at "wait"/"hmm" cue tokens plus conformal bound on premature exits | GSM8K -40-65% tokens; MATH-500 up to +12 points with -35-60% tokens; AIME24 baseline accuracy at over 50% saving | c09 | [S] |
| Hidden-state probe for correctness of intermediate answers | ROC-AUC above 0.7, ECE below 0.1 in distribution; early exit at threshold 0.85 gives 88.2% (same as no exit) with about 24% fewer tokens; threshold 0.9 gives 88.6% with 19% fewer; up to 5 points over static exit at matched tokens (87.4% vs about 82.5%). Degrades on short-CoT models and from logic to math | Zhang 2025 (b10, a13, c11) | [E] |
| Thought calibration | Up to 60% fewer thinking tokens in distribution, up to 20% OOD (three models, four datasets) | c10 | [E] with probe papers |
| Adaptive-Consistency | 17 datasets, 3 models: up to 7.9x fewer samples, mean accuracy drop under 0.1%. GPT-3.5-turbo 4.4x, Vicuna-13B 1.9x, Codex 3.4x. By task: math 3.3x (-0.1 pt), commonsense 2.9x (-0.2), symbolic 3.8x (0), code 2.4x (+0.4). Beat fixed-budget SC at equal average samples | Aggarwal 2023 (b06, b07) | [E] |
| ESC | Sample reduction MATH -33.8%, GSM8K -80.1%, StrategyQA -76.8%, CommonsenseQA -78.5%, Coin Flip -84.2%, Last Letters -67.4%; window 5 (8 for MATH); plain SC at the same average samples loses accuracy | Li 2024 (b08, a15) | [E] |
| Parallel-trace pruning | DeepConf: GPT-OSS-120B AIME 2025, @512 offline 99.9% vs 97.0% majority vote vs 91.8% pass@1; online up to 84.7% fewer tokens; DeepConf-low cuts 43-79% on four sets; accuracy drops in a few settings (Qwen3-32B BRUMO25 -0.9). short-m@k: up to 40% fewer thinking tokens, up to 33% less wall time | Fu 2025 (b20); Hassid 2025 (b19) | [E] |
| Shorter chains are more often right within one question | Shortest chain up to 34.5% more accurate than the longest (the "18.8% over random" in a18 is not verified) | Hassid 2025 (b19) | [C] on cause |
| Underthinking | Wrong answers: +225% tokens, +418% thought switches; a switching penalty (TIP) lifted accuracy on hard sets without fine-tuning | Wang 2025 (b17) | [S] |
| Think or no-think by difficulty | AdaptThink R1-Distill-1.5B: length -53%, accuracy +2.4% on three math sets. Contrast: NoThinking on Qwen3-14B AIME 26.7 vs 70.0 vanilla | Zhang 2025 (b18, a11); DEER (a12) | [E] |
| A premature-stop bound still leaves wrong answers | Premature-stop rate 0.083 GSM8K, 0.091 HotpotQA at delta 0.1 (GPT-4o, Llama-3-70B 0.079-0.092); sufficient-looking but incorrect 13.2% (ProofWriter) to 22.7% (LegalBench); correctness gate: 18.5% to 10.9% wrong, correctness 76.8% to 83.4%, overhead 12% to 16%; length -22-28% | Akter 2025 (d06) | [S] |
| Agents ignore their own "useless" verdict | Failing source judged useless 97-100% of the time; unaided Qwen3-8B answers on 1 of 292 questions after 5 useless judgments in a row. Success, none vs forced answer after 5: Qwen2.5-7B .192 vs .237; Llama-3.1-8B .263 vs .328; Qwen3-8B .448 vs .474; Qwen3-32B .509 vs .572; Haiku 4.5 .501 vs .598; Sonnet 5 .632 vs .653 (p=.051, not significant). Pre-registered replication on 300 fresh questions | Zhang et al. 2026 (d01) | [S] |
| A stated budget becomes a quota | Budget-cued 7-8B models answer on the last allowed action in 51-79% of answers on failing sources; doubling to 16 actions doubles calls with no gain (Qwen3-32B +46% calls, no gain); Qwen3-8B with permission to answer from memory answered before any real result on 55% of recoverable questions; Qwen3-32B thinking mode answered from memory on 97% of failing-source questions | d02 (about 60% of text read) | [S] |
| Question-asking without a stop rule hurts | MediQ: plain asking is worse than answering from initial info; best abstention expert +22.3% over BASIC, +12.1% over Initial, still 10.3% below full information; models over 70B beat Initial with the best abstention, smaller ones do not | Li 2024 (c15) | [E] with CaRT, UoT |
| Information gain for choosing questions | UoT: +38.1% average success over direct prompting (relative gains, simulated GPT-4 answerer); fewer questions | Hu 2024 (b21, a21) | [S] on stopping |
| Models cannot find what is missing | QuestBench: GSM-Q and GSME-Q near or above 80-90%; Logic-Q and Planning-Q 40-50%; Gemma 2 2B 0.09-0.26% on Logic-Q in some settings | Li, Kim, Wang 2025 (b22) | [S] |
| Context sufficiency | Selective generation raises the correct fraction among answered by up to 210% (abstract) | Joren 2025 (a20) | [S] |
| Embedding convergence for refinement loops | 60 HotpotQA questions: -38% operational tokens vs fixed max iterations, parity (delta Information Score -0.004, p=0.81); a per-round LLM judge erased savings; oracle best-round beats every practical policy by +0.115 | Shrivastava 2026 (d07), abstract-level | [S] |
| Refinement peaks early | Rice-cultivation case study: quality peaked at rounds 3-4 of 0-10, +30-33% over round 0; experts rated final rounds below the start; judges over-scored by 1.4-2.3 points but ranked rounds like experts (rho 0.58-0.90) | d16, abstract | [S] |
| Stopping sampling as optimal stopping | Pandora's Box UCB: win rate over fixed best-of-N above 54% at equal average compute; 15-35% fewer samples at acceptance targets 0.75 and above; 1,600 profiles, 4 models, 2 reward models. BEACON: up to 80% fewer samples | d10; d09 (abs) | [S] |
| More thinking is not monotone | Mirage of test-time scaling and inverse scaling (abstracts only) | c18, c19 | [C] |
| s1 budget forcing | Extending with "Wait" scaled AIME24 from 50% to 57% (abstract) | c17 | [S] |

## 4. Mechanisms and models

Each mechanism is written so it can be coded.

### 4.1 Value-of-continuing stop (the general form)
- State: current best answer a_t and the history of answers a_1..a_t.
- Estimate p_change = probability that one more step changes the answer to a better one. Estimate gain = expected accuracy increase if it does. Estimate cost = tokens of one more step times the price of a token in accuracy units.
- Stop when p_change * gain < cost.
- Every practical rule below is a cheap estimate of p_change. None estimates gain directly. CaRT's label comes closest, because its oracle measures success rate at each prefix (a01, a02).

### 4.2 CaRT-style learned judge
1. Collect many trajectories on the task family (CaRT: 1,000+ problems).
2. For each prefix, estimate success rate by sampling many completions (CaRT: 50 generations scored by an external model, d19).
3. Label a prefix `terminate` if success is clearly higher than at earlier prefixes (medical: one Q/A raises success by at least 0.5). Otherwise `continue`.
4. Build a hard negative: copy the prefix but replace the last Q/A (medical) or remove a block of steps (math) so success falls below 0.3. Label it `continue`. This breaks the shortcuts "stop because the dialogue is long" and "stop because the last line sounds confident".
5. Add a written reason per label, generated by a stronger model, weighing what is known against what is missing (a "verbalised value function").
6. Fine-tune a small model on 80% continue and 20% terminate. Optional GRPO with +1/-1 decision reward (this drifted long in CaRT and did not help in math).
7. At run time, ask the judge after every step. Stop on `terminate`.
Cost: a success-rate oracle with many rollouts per prefix. This is the main barrier. No paper builds counterfactuals from cheaper signals.

### 4.3 Answer-stability stop (training-free)
- After each step, or at "Wait"-type transitions, get a trial answer. DEER forces one and reads its token confidence (b12). Answer Convergence repeats the probe and stops when the last k trial answers agree; k is 10-30 depending on cost (b14).
- Stop when the last k agree, with larger k on hard classes.
- For closed models use only the text answer, not logits. Conservative rule from ESC: stop only on full agreement inside a window (b08, b09).
- Known failure: a repeated wrong answer locks in. Repeats from one model are correlated (G4).

### 4.4 Sampling-level stop
- Adaptive-Consistency: model counts of distinct answers with a Dirichlet; stop when the posterior probability that the leader stays the leader exceeds a threshold. Worked example: 9 of the first 10 agree gives over 99% that the majority holds after 40 samples (a model estimate, not a measured rate) (b07).
- ESC: draw in windows of 5 (8 for MATH). If all in a window are equal, stop; else draw the next window up to a maximum (b08).
- BEACON and Pandora's Box: stop when expected gain of one more sample is below its cost, with a Bayesian or UCB estimate of the reward distribution (d09, d10).
- Both agreement rules treat samples as independent. Per G4 they are not, so use a stricter threshold than the papers.

### 4.5 Trace-level stop in parallel runs
- DeepConf: track group token confidence over a window; kill a trace whose confidence falls below a threshold set from warm-up traces; weight votes by confidence (b20).
- short-m@k: launch k chains, stop when the first m finish, vote among those (b19).
- PeerConf and MARS (d11, second-hand): per-trace commit on a probe threshold estimated from peer traces; stop the vote when the leader is safe.
- DeepConf needs logprobs. The length-based short-m@k works with any API where parallel calls can be cancelled.

### 4.6 Probe-based stop (open weights)
- Train a linear probe on hidden states at intermediate-answer positions to predict "this answer is correct" (b10), or at cue tokens to predict "forced exit now would be right" (c09, LYNX). Calibrate the threshold. LYNX uses split conformal prediction for a distribution-free bound on premature exits.
- Stop when the probe score passes the threshold, ideally for several consecutive confirmations (BLADE, c25, snippet only).
- Not usable on closed API models. Does not transfer well across domains or to short-CoT models.

### 4.7 Entropy and logit signals
- EAT (c08): append the end-of-thinking token and watch next-token entropy; stop when its variance under an exponential moving average falls. A proxy model can supply the entropy for a black-box reasoner.
- Commitment boundary (d18): the step after which answer logits no longer move; up to 55% shorter CoT (abstract).

### 4.8 Harness-level integration rule (outside the model)
- Track consecutive "useless" results (no new information). After 5 in a row, remove the tools and force an answer (d01).
- Do not state a step budget in the prompt as a target (d02): it turns into a quota.
- Cheap, runs in code, tested on closed models (Haiku 4.5 and Sonnet 5).

### 4.9 Semantic convergence stop for loops
- Embed each draft. Stop when similarity between consecutive drafts exceeds a threshold for `patience` rounds (d07).
- Avoid a per-round LLM judge: it ate the savings. Call a judge only when cheap checks disagree.

### 4.10 Sufficiency certificate (statistics)
- Test whether the output carries more information than a weakened baseline, with a sequential test whose premature-stop rate is bounded by delta (d06).
- The guarantee covers information sufficiency, not correctness. Pair it with a correctness gate (an independent check) before commit.

### 4.11 Upfront mode choice
- AdaptThink-style: pick think or no-think per problem before starting (b18). This is our S0 gate. It needs a per-class table of plain pass rates; NoThinking collapses on hard items (a12: 26.7 vs 70.0 on AIME for Qwen3-14B).

### 4.12 Information-gain view for interactive tasks
- Keep a candidate set of hypotheses. Score each possible question by expected reduction in entropy (UoT, b21). Stop when the candidate set collapses to one, or when the best question's expected gain is below its cost.
- First ask "what is missing?" (QuestBench, b22). Then ask. Then stop.

## 5. What holds up

**Replications.**
- No independent replication, and no failed replication, of CaRT was found (a22, b26, K16). The forward-citation check was incomplete because APIs were rate-limited, so this is absence of evidence only.
- Related early-exit ideas agree in direction across many groups: DEER, Answer Convergence, EAT, probes, LYNX, thought calibration, S-GRPO, JET, ESTAR, BLADE. They differ in setups, with no shared benchmark and no head-to-head.
- ESC and Adaptive-Consistency report on different models and budgets; no paper ran both on one setup (b23).
- Judged Useless carried a pre-registered replication on 300 fresh questions (d01). It is the only explicit replication in the set, and it is internal to the paper.

**Well supported [E].**
1. Answers stabilise before reasoning ends, and later steps are often redundant (b14, b16; K04).
2. Training-free answer-based or probe-based early exit saves roughly 20-60% of tokens, with accuracy flat or slightly up, on math with open reasoning models (K05, K06).
3. Sample-level stopping for self-consistency beats a fixed N at equal mean samples (K07).
4. Question-asking agents need an explicit stop or abstain rule (K13), and sufficiency is a separate skill from answering (K14).
5. Think or no-think routing by difficulty helps, but a wrong call on hard items is costly (K12).

**Moderators and boundary conditions.**
- Difficulty: gains are smaller on hard tasks. ESC saves 33.8% on MATH vs 80.1% on GSM8K. Answer Convergence gains less on MATH-500, GPQA and AIME. ESTAR lost 3.3 points on AIME. Hard items are where over-truncation bites (JET: steep penalties truncated hard items).
- Domain: DEER compresses math and science 61.5% on average but code only 19.9%. Probes trained on logic did not generalise to math; GSM8K and MATH probes were less calibrated on AIME.
- Model: probes degrade on short-CoT models; DEER is weak on Llama-3.1-Nemotron-Nano-8B; Qwen3-1.7B needed counterfactual data more than Qwen2.5-3B.
- Distribution shift: CaRT base and SFT fell below a fixed-count baseline on dermatology; thought calibration gains drop from 60% to 20% OOD. Counter-evidence: ESTAR retained 98.9-100% accuracy on GPQA after training on USMLE and deepscaleR; a feature-based decider transferred with calibration only. So collapse is not general, but nobody tested base and SFT stoppers in those settings (K03).
- Sample independence: agreement among samples of one model is correlated, so confidence from agreement is overstated.
- Model size: MediQ abstention only helped models over 70B; Joren found small models hallucinate or abstain even with sufficient context.
- Access: probes, logits and DeepConf need open weights or logprobs.

**Failures and costs.**
- CaRT's RL on the decision drifted to longer conversations and gave no math gain (b05). Other reward designs worked (d03-d05), so this looks like a reward-design failure, not "RL cannot do it" (K17 [C]).
- Confident-wrong traces exist (DeepConf). DEER's authors state that plain confidence averaging does not fix false positives (b13).
- The false-stop rate is almost never reported (critique). Best numbers: premature-stop 0.083-0.092 under a statistical bound, and 13.2-22.7% sufficient-looking but wrong outputs (d06). ESTAR's threshold sweep gives a cost: 3.8 accuracy points from tau .99 to .80. Nothing is split by problem difficulty.
- A per-round LLM judge removed the savings in the refinement-loop study (d07). Prompted judges over-score by 1.4-2.3 points (d16).
- Most learned stops are late (63.6% late, 18.2% perfect; b15), so even a trained stopper is far from optimal.

**Interventions that worked.**
- Counterfactual hard negatives (CaRT, K02).
- A harness rule forcing an answer after 5 useless results (d01).
- Windowed or Bayesian agreement stops for sampling (K07).
- Trial answer plus confidence at transitions (K05).
- A correctness gate after a sufficiency stop: wrong outputs 18.5% to 10.9% (K21).
- Embedding convergence for loops (d07).

**Interventions that did not work, or hurt.**
- Plain prompting to ask more questions (MediQ).
- Stating a step budget (becomes a quota, d02); giving a model permission to answer from memory (answers before evidence, d02).
- A per-round LLM judge for stopping loops (d07).
- Steep exponential length penalties and hard length caps (d03; CaRT also notes hard caps generalise poorly).
- CaRT's binary-reward RL (b05).
- A verbalised confidence score as an add-on to CaRT (redundant, a07). This agrees with SCHEMA 4b: do not use a model's verbal confidence to stop.
- Training on terminate ratios of 5-20% without counterfactuals (a07).

**Contradictions to keep in view (critique).**
- "Stop sooner because answers converge" (Chen, Liu and Wang, DEER) vs "models stop too soon on hard problems" (Wang). Both can hold if difficulty drives it. No paper tests one stop rule on both easy and hard items.
- Hassid (shorter is better) vs s1 (a "Wait" extension helps, 50 to 57 on AIME24). Boundary: s1 extends a model that stopped too soon; Hassid compares samples within one question.
- Path-deviation paper vs DEER on answer-confidence exit. No independent head-to-head.
- Stability stops (the answer stops moving) and sufficiency stops (information is enough) are used separately; nobody counts where they disagree (K24).

## 6. Language models

All results are on LLMs; there is no human comparison. No study was found of LLM stopping on classic human optimal-stopping tasks (secretary problem, costly sampling): zero arXiv hits, zero web hits (d15, K23). Behavioural journals were not searched.

**Default behaviour without help.**
- Reasoning models overthink easy items: first round correct in over 92% of cases yet long continuation (b16). On hard items wrong answers carry 225% more tokens and 418% more switches (b17).
- Even after learning, stops are mostly in the wrong place: 63.6% late, 18.2% perfect (b15).
- Interactive agents asked to ask questions do worse than answering at once (MediQ, c15). Most models rarely ask follow-ups.
- Tool agents label sources useless 97-100% of the time and still keep calling; unaided Qwen3-8B answers on 1 of 292 questions after 5 useless judgments (d01). Prompt cues change when they stop, not what they stop on.
- A stated budget becomes a quota: budget-cued 7-8B models answer on the last allowed action in 51-79% of answers on failing sources; doubling the budget doubles calls (d02).
- Permission to answer from memory, or thinking mode, causes early stops that ignore evidence: Qwen3-8B answered before any real result on 55% of recoverable questions; Qwen3-32B in thinking mode answered from memory on 97% of failing-source questions (d02).
- Large models answer well with sufficient context and answer wrongly instead of abstaining when it is missing; small models hallucinate or abstain even with enough context (a20).

**What changed it, and by how much.**

| Change | Effect | Source |
|---|---|---|
| Counterfactual-trained stop judge (3B, 1.7B) | Beat base and SFT; size in figures only; base and SFT fell below a fixed-count stop OOD, CaRT stayed above with a smaller margin | CaRT |
| Trial answer plus confidence at transitions | -19.1% to -80.1% CoT, +0.3 to +5.0 accuracy (11 models) | DEER |
| Answer agreement over last k probes | -44% tokens at 0.2% accuracy drop; over 40% on NQ | Answer Convergence |
| Hidden-state probe | -24% tokens, same accuracy; up to 5 points over static exit at matched tokens | Zhang 2025 |
| Probe with conformal bound | -40-65% tokens on GSM8K, up to +12 points on MATH-500 | LYNX |
| Window or Bayesian sampling stop | -33.8% to -84.2% samples at similar accuracy; 7.9x at most | ESC, Adaptive-Consistency |
| Confidence pruning of parallel traces | up to -84.7% tokens; 99.9% at @512 | DeepConf |
| First m of k chains | up to -40% thinking tokens | short-m@k |
| Forced answer after 5 useless results | +.021 to +.097 success depending on model; Sonnet 5 not significant | Judged Useless |
| Abstention module in interactive QA | +22.3% over BASIC, +12.1% over Initial | MediQ |
| Correctness gate after a sufficiency stop | wrong outputs 18.5% to 10.9% | Akter |
| Embedding convergence in loops | -38% tokens at parity | Semantic early-stopping |
| RL rewards (S-GRPO, JET, ESTAR) | -35% to -61% length with accuracy flat to +6 | various |

**Scale and model type.**
- Most early-exit results use open reasoning models (R1-Distill, QwQ, Qwen3, GPT-OSS). They save most on math, least on code, and little on hard sets.
- Closed API models: text-only rules were tested on Haiku 4.5 and Sonnet 5 in d01 only. EAT with a proxy model (up to 21%) is one route to a black-box reasoner.
- The harness rule's gain shrinks as the base gets stronger (Haiku +.097, Sonnet 5 +.021). This is a gradient across two models, not a proven law.

**Not yet known for LLMs.** Whether CaRT's data design works on a second model and domain; false-stop rate split by difficulty; judge vs probe head to head; trace-stop vs vote-stop at equal tokens (section 10).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single source, [C] contested. SCHEMA.md 4b already bans "using a model's verbal confidence to stop"; everything below respects that. Evidence ids refer to the evidence files; K-ids to claims.jsonl.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Stop sampling by code once the answer distribution is concentrated. Use a window rule (stop when a whole window agrees; window 5) or a Bayesian lead test. Use a stricter threshold than the papers because samples are correlated. Compare with a fixed N at equal mean samples in our harness before keeping (G7). | S3/S7, G4, G7 | [E] | b06, b07, b08, b09, b23 (K07) |
| A2 | Log, for every run, the earliest step at which the answer equals the final answer. Report the wasted-token share. It costs almost nothing and measures overthinking on our own tasks. | log (schema section 6), G11 | [E] | a10, b14, b16 (K04) |
| A3 | Stop by content, never by position or length alone. A stop rule must depend on whether the answer moved, not on step count. | S8, G11 | [E] direction (the CaRT shortcut finding itself is [S]) | b03, b17, b25 |
| A4 | In S0, route easy classes to a short or direct path, but measure accuracy by difficulty bin first. NoThinking is harmful on hard items. | S0, G12 | [E] | b18, a11, a12 (K12) |
| A5 | For any interactive or question-asking step, add an explicit sufficiency check ("what is still missing?") before answering, scored separately from solving. Compare ask-then-answer with answer-now at equal tokens. | S0/S1, S8 | [E] | c15, b22, a20 (K13, K14) |
| A6 | Keep the stop signal outside the model's own opinion. Use answer agreement and checks, not a verbal "I am sure" (consistent with 4b and G10). | G10, S8 | [E] | a07, d01, SCHEMA 4b |
| A7 | Record the false-stop rate (stopped, but continuing would have given a correct answer) next to every token saving. Never report savings alone. | log, G7 | [E] need (K11) | b13, d05, d06 |
| A8 | Re-validate every stop threshold per problem class; gains and thresholds do not carry across difficulty or domain. | S0, M class record | [E] | b24, b10, c10, b04 (K03) |

Related low-cost rule, single source [S]: do not state a step or tool budget in the prompt as a target; hold the budget in code (d02). Listed in "Test first" as T0 because it has one paper behind it.

### Test first (single-source or contested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T0 | Hold the step budget in code; never say it in the prompt. | G7, G12 | [S] | d02 |
| T1 | Harness rule: after k consecutive no-gain steps (no new evidence, no changed answer) force an answer. Start with k = 5. | S8, S6, G6 | [S] | d01, d02 (K19) |
| T2 | Trial-answer stop: at natural transition points ask for a trial answer; stop if the last k agree. Closed-model, text-only version of DEER and Answer Convergence. | S8 | [S] for text-only on closed models; [E] on open models | b12, b14, d01 (K05) |
| T3 | Counterfactual stop judge built from our own traces: pair a stop-right prefix with a minimally edited stop-wrong prefix and show the pairs as examples to a prompted judge (no training). | S8 | [S] | a02, b03 (K01, K02) |
| T4 | Call the judge only when cheap checks disagree (answer stability, embedding convergence). | S8, G5 | [S] | d07, d16 (K20) |
| T5 | Correctness gate after any sufficiency stop: an independent check on the unfitted part before commit. | S8, G3 | [S] | d06 (K21) |
| T6 | Value-of-continuing estimate: p(answer changes) times expected gain against token cost. | S8, M class record | [S] | a01, d09, d10 (K18) |
| T7 | Trace-level stop vs vote-level stop vs both, at equal tokens. | S3/S7 | [S] | d09-d11 (K22) |
| T8 | Separate "stability" and "sufficiency" stops; count their disagreements in interactive tasks before choosing one. | S8 | [S] | d18, d19 (K24) |
| T9 | Hard-class safeguard: no early stop while the answer is still changing or thought switching is high. | S6/S8, G1 | [S] | b17, c07 (K10) |
| T10 | Information-gain stopping for hypothesis-elimination tasks: stop when the candidate set collapses to one. | S8 | [S] | b21 (K13) |
| T11 | Fit the stop threshold per class in the class record, updated at S9. | M class record, S9 | [S] | b24 |

Not to add: RL or fine-tuning on the stop decision (we cannot train); hidden-state probes (closed API); a per-round LLM judge as the main stop signal (d07); verbal confidence as a stop signal (4b).

## 8. Concrete tests on our bench

All arms run at equal mean tokens, with setup and judge calls counted (G7). For each test report accuracy, mean tokens and false-stop rate.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Items with a code check, mixed easy and hard (ARC-style, short-answer reasoning) | (a) fixed N attempts; (b) window-5 agreement stop; (c) Bayesian lead stop; (d) (b) with a stricter threshold | Accuracy at equal mean attempts; tokens saved | 30-70% fewer attempts at accuracy within 1 point on easy items; much smaller saving on hard. Threshold needs to be stricter than the paper's |
| B2 | Same items, single extended-thinking attempt | (a) full budget; (b) trial-answer stop at transitions, k = 3 and 5 | Accuracy; wasted-token share (earliest-correct step vs end) | 20-40% fewer tokens at flat accuracy on math-like items; little on code-like items |
| B3 | Tool or retrieval tasks with controlled failing sources | (a) no rule; (b) forced answer after 5 useless; (c) after 3; (d) stated budget in prompt | Success; calls; answer-on-last-action rate | (b) lifts success on weaker models; (d) causes the quota effect. Stronger models gain less |
| B4 | Question-asking diagnosis or 20-questions items with a known hidden answer | (a) answer-now; (b) ask a fixed number of questions; (c) ask, then sufficiency check; (d) stop on candidate-set collapse | Accuracy; questions asked | (c) and (d) beat (b); (a) is the baseline to beat, since MediQ shows plain asking can lose to answer-now |
| B5 | Easy and hard bins from our pass-rate table | One agreement-window stop applied to both | False-stop rate and savings by bin | Savings high on easy; false stops concentrate in the hard bin. First difficulty split nobody has run |
| B6 | Logged traces with a known earliest-correct step | Prompted counterfactual-example judge (T3) vs agreement stop vs fixed budget | Stop quality (late, perfect, early share), accuracy, tokens | The judge with hard-negative examples beats position-based stop; check that its stop rate does not track step count |
| B7 | Multi-trace runs | (a) full vote; (b) per-trace stop (first-m of k); (c) vote stop; (d) both | Accuracy at equal mean tokens | (d) at least equal to (c); gain over (a) is real only if the false-stop rate stays flat |
| B8 | Items where a stopped answer can be wrong | Stop rule with and without a correctness gate (G3 unfitted check) | Share of confident-wrong; overhead | Wrong share falls (paper: 18.5% to 10.9%) at 10-20% overhead |
| B9 | Loop tasks (draft, critique, revise) | (a) fixed rounds; (b) embedding convergence with patience; (c) per-round LLM judge | Quality; tokens | (b) saves about 38% at parity; (c) saves nothing |
| B10 | Domain shift: tune the threshold on one class, test on another | Fixed budget vs tuned stop | Margin over fixed budget on the new class | Margin shrinks or turns negative on a large shift; confirms A8 |
| B11 | (Optional) classic stopping task: secretary problem and a costly-sampling task | 3-5 models, 1/e rule as reference | Acceptance position vs 1/e; payoff | Unknown. Fills a gap nobody has measured; low priority for the agent |

## 9. What does not transfer, and why

- **CaRT's training.** We use scaffolds, not fine-tuning. Only the data-design idea (hard negatives) can be borrowed, as examples in a prompt, and that is untested [S].
- **Hidden-state probes and logit signals** (probing, LYNX, thought calibration, DeepConf, EAT, commitment boundary). They need open weights or logprobs. Closed API models give neither. EAT with a proxy model is the only partial bridge.
- **Success-rate oracles for labels.** CaRT needs many rollouts per prefix and an external model for scoring. Too expensive for routine use. It also tests only against one fixed question-asking policy.
- **RL reward designs** (S-GRPO, JET, ESTAR, CaRT RL, AdaptThink). Not available without training.
- **Token-saving figures from open reasoning models on math.** Our agent uses several short attempts (G11), not one long chain, so percentages will differ. Savings on code were only 19.9% (DEER).
- **Human optimal-stopping theory.** Secretary-problem and sequential-test results assume known dynamics and independent draws. LLM samples are correlated (G4). No LLM-vs-human study exists to calibrate against (d15).
- **Stated confidence.** On the "not to add" list (4b). In CaRT it was redundant.
- **Small-model findings.** CaRT used 3B and 1.7B models and a GPT-4o simulated patient. The OOD collapse and the need for counterfactuals may be small-model effects (Qwen3-1.7B needed CF more than Qwen2.5-3B).
- **Hard-set benchmarks as proof.** AIME has 30 items, so a few points are noise. Do not copy thresholds from such tables.
- **Sampling savings that assume i.i.d. rewards** (Pandora's Box used reward-model scores, not task correctness).

## 10. Open questions

1. Does a CaRT-style judge hold when trained and tested on a different base model and domain (code, planning, tool use), and does it beat a fixed budget at equal mean tokens? No replication exists.
2. What is the false-stop rate of confidence, probe and prompted-judge rules, split by problem difficulty? Only partial numbers exist (d05, d06), none split by difficulty.
3. How much of CaRT's gain comes from counterfactuals, and can they be built without a success-rate oracle, for example from the agent's own answer-change history? Open (d19).
4. Do stopping and question selection need to be learned jointly? The authors say yes; there is no test beyond UoT and MediQ.
5. Trace-level vs vote-level stopping at strictly equal tokens: open. PeerConf and MARS numbers are second-hand and unopened.
6. What does an LLM do on classic human stopping tasks, and how does it compare with human thresholds? Zero hits found (d15); behavioural venues not searched.
7. Is the OOD collapse of base and SFT stoppers general or specific to CaRT's dermatology shift? ESTAR argues not (98.9-100% retained on GPQA) but did not test base or SFT stoppers.
8. Do stability stops and sufficiency stops agree in interactive tasks? Nobody counts the disagreements (K24).
9. Can a prompted judge on a closed model match probe-based stopping? The judge-vs-probe head-to-head is missing; text-only rules work in d01 and d07.
10. When does early stopping hurt where extended thinking helps (s1 "Wait", inverse scaling)? How to tell the two regimes apart in advance is not known (K15 [C]).
11. CaRT's test sets are 100/200 in the main text and 121/93 in the appendix. Which were used?
12. Does reasoning help CaRT's direct accuracy? In its Table 1, CaRT minus reasoning had higher direct accuracy (0.849) than full CaRT (0.663), while the probe was better with reasoning (0.774 vs 0.645, CIs overlap).

## 11. Sources

[V] = opened this session (full text, HTML or PDF; "abstract page" where only that was read). [M] = snippet, memory, or abstract in an earlier pass only.

- [V] Liu, Qu, Schneider, Singh, Kumar (2025) CaRT: Teaching LLM Agents to Know When They Know Enough. https://arxiv.org/abs/2510.08517 (PDF re-read and cross-checked in the critique)
- [V] Aggarwal, Madaan, Yang, Mausam (2023) Let's Sample Step by Step: Adaptive-Consistency. https://arxiv.org/abs/2305.11860
- [V] Li, Yuan, Feng et al. (2024) Escape Sky-high Cost: Early-Stopping Self-Consistency (ESC). https://arxiv.org/abs/2401.10480
- [V] Zhang, Chen, Pan et al. (2025) Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification. https://arxiv.org/abs/2504.05419
- [V] Yang, Si, Duan et al. (2025) Dynamic Early Exit in Reasoning Models (DEER). https://arxiv.org/abs/2504.15895
- [V] Liu and Wang (2025) Answer Convergence as a Signal for Early Stopping in Reasoning. https://arxiv.org/abs/2506.02536
- [V] Chen, Xu, Liang et al. (2024) Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs. https://arxiv.org/abs/2412.21187 (abstract confirmed; 92% and 1,953% figures from the body, not re-checked)
- [V] Wang, Liu, Xu et al. (2025) On the Underthinking of o1-Like LLMs. https://arxiv.org/abs/2501.18585
- [V] Zhang, Lin, Hou et al. (2025) AdaptThink: Reasoning Models Can Learn When to Think. https://arxiv.org/abs/2505.13417
- [V] Hassid, Synnaeve, Adi, Schwartz (2025) Don't Overthink It: Preferring Shorter Thinking Chains. https://arxiv.org/abs/2505.17813 (the 34.5% figure confirmed from the abstract; 18.8% not)
- [V] Fu, Wang, Tian, Zhao (2025) Deep Think with Confidence (DeepConf). https://arxiv.org/abs/2508.15260
- [V] Hu, Liu, Feng et al. (2024) Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271
- [V] Li, Kim, Wang (2025) QuestBench. https://arxiv.org/abs/2503.22674
- [V] Li et al. (2024) MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning. https://arxiv.org/abs/2406.00922
- [V] Joren et al. (2025) Sufficient Context: A New Lens on Retrieval Augmented Generation Systems. https://arxiv.org/abs/2411.06037
- [V] Aggarwal and Welleck (2025) L1: Controlling How Long A Reasoning Model Thinks. https://arxiv.org/abs/2503.04697
- [V] Mitigating Overthinking in LRLMs via Reasoning Path Deviation Monitoring (2026). https://arxiv.org/abs/2603.14251
- [V] Entropy After </Think> (EAT) (2025). https://arxiv.org/abs/2509.26522
- [V] Akgul et al. (2025) LYNX: Learning Dynamic Exits for Confidence-Controlled Reasoning. https://arxiv.org/abs/2512.05325
- [V] Thought calibration: Efficient and confident test-time scaling (2025). https://arxiv.org/abs/2505.18404
- [V] Zhang, Wan, Yu et al. (2026) Judged Useless, Queried Anyway. https://arxiv.org/abs/2610.06191 and https://arxiv.org/html/2610.06191 (about 60% of text read)
- [V] Han et al. (2026) Your Models Have Thought Enough (JET). https://arxiv.org/pdf/2509.23392
- [V] Dai et al. (2025) S-GRPO. https://arxiv.org/abs/2505.07686 (abstract page)
- [V] Early-Stopping Token-Aware Reasoning (ESTAR). https://arxiv.org/html/2602.10004v1
- [V] Akter, Shihab, Sharma (2025) Anytime-Valid Answer Sufficiency Certificates for LLM Reasoning. https://arxiv.org/html/2510.06478v2
- [V] Shrivastava (2026) Semantic Early-Stopping for Iterative LLM Agent Loops. https://arxiv.org/abs/2606.27009 (abstract-level)
- [V] Hammar, Alpcan, Lupu (2026) Optimal Stopping of Self-Refining Foundation Models. https://arxiv.org/abs/2608.10729 (abstract only)
- [V] Wan et al. (2025) BEACON: Bayesian Optimal Stopping for Efficient LLM Sampling. https://arxiv.org/abs/2510.15945 (abstract only)
- [V] Optimal Stopping vs Best-of-N for inference-time optimization (Pandora's Box). https://arxiv.org/html/2510.01394v1
- [V] Does Your Reasoning Model Implicitly Know When to Stop Thinking? (SAGE). https://arxiv.org/abs/2602.08354 (abstract only)
- [V] Zhu, Xie, Rao (2026) Stopping and Routing LLM Judge Panels. https://arxiv.org/abs/2608.19802 (abstract only)
- [V] Agentic XAI case study in decision support for rice cultivation: refinement rounds. https://arxiv.org/abs/2512.21066 (abstract page)
- [V] Learning When to Sample: Confidence-Aware Selective Sampling. https://arxiv.org/abs/2603.08999 (abstract only)
- [V] Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought. https://arxiv.org/abs/2606.13603 (abstract only)
- [V] arXiv abstract search for "secretary problem" + LLM, zero results, 2026-11-03. https://arxiv.org/search/?query=%22secretary+problem%22+LLM&searchtype=abstract
- [M] Muennighoff et al. (2025) s1: Simple test-time scaling. https://arxiv.org/abs/2501.19393 (abstract)
- [M] Does Thinking More always Help? Mirage of Test-Time Scaling in Reasoning Models. https://arxiv.org/abs/2506.04210 (abstract)
- [M] Inverse Scaling in Test-Time Compute (2025). https://arxiv.org/abs/2507.14417 (abstract)
- [M] Graves (2016) Adaptive Computation Time for Recurrent Neural Networks. https://arxiv.org/abs/1603.08983 (abstract)
- [M] Banino, Balaguer, Blundell (2021) PonderNet. https://arxiv.org/abs/2107.05407 (abstract)
- [M] Stop Overthinking: A Survey on Efficient Reasoning for LLMs (2025). https://arxiv.org/abs/2503.16419 (abstract)
- [M] BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit. https://arxiv.org/pdf/2607.28966 (search snippet only)
- [M] PeerConf and MARS (NeurIPS 2026 page returned 404; numbers second-hand). https://neurips.cc/virtual/2026/159157
- [M] Wald (1945) Sequential tests of statistical hypotheses; Chow and Robbins optimal stopping; secretary problem (classical background, from memory). https://doi.org/10.1214/aoms/1177731118
- Rejected: arXiv id 2503.12434 was given by a web summary as a sales-call stopping paper; the id does not match. Do not cite that paper (d14).
