# Bias and debiasing: deep document

*Subfield D05.07. Question: does training or instruction cut biases? Written from evidence_a-d.jsonl, claims.jsonl (K01-K41) and critique.md in this folder. Evidence ids (a01, b12, c08, d06 ...) point to the jsonl files. Status marks: [E] established, [S] single-source, [C] contested. Where the critique pass corrected an earlier note, the corrected figure is used here.*

---

## 1. What it is

This subfield asks two linked questions.

1. **Humans.** Can you train people (or tell them) to avoid systematic errors such as anchoring, framing, confirmation bias and hindsight bias? Does the training last? Does it carry over to a new task?
2. **Language models.** Do LLMs show the same biases? Does telling them to avoid bias, showing examples, making them reason, or making them review their own answer reduce the bias? What does reduce it?

Why it matters for our agent. Our schema rests on one design claim: a scaffold, not training, makes one model think better. Section 4b of SCHEMA.md already says "do not add bias checklists and debiasing instructions". This subfield tests that claim against the founding human work and against 2022-2026 LLM studies.

Short answer, in one paragraph. Telling a person or a model to "be unbiased" or "be careful" does little, is uneven, and sometimes backfires. What works is changing the input or the procedure so the bias has nothing to grab: remove the planted cue, show both sides, restate the problem in a different format, test a case that can falsify the choice, and check results with code. Human training that shows lasting transfer is rare and comes mostly from one lab. For LLMs, almost every positive result removes a cue that the experimenters planted in the prompt. That is a real but narrow win. No study yet tests a debiasing step at equal tokens against a plain model on biases that were not planted, with a 2026 reasoning model. That is the gap our bench can fill.

Terms used here.
- **Bias score**: the shift in answers between a biased and a neutral version of the same item. Papers define it differently (rate gap, index, accuracy drop). Sizes across papers are not comparable (critique, weak spots).
- **Planted cue**: a biasing phrase the experimenter adds to the prompt (a suggested answer, an anchor number, a frame). Removing it is "input hygiene".
- **Debiasing instruction**: a line such as "Be mindful not to be biased by cognitive bias".

---

## 2. History and theories in depth

### 2.1 Heuristics and biases (1970s-1980s)

Tversky and Kahneman (1974, Science) named anchoring, representativeness and availability. In the anchoring study, a number from a wheel of fortune moved estimates of the share of African countries in the UN; the median estimate went from 25% to 45% depending on the anchor (as quoted in a04/a21; the original was not opened). Tversky and Kahneman (1981) showed framing: the Asian disease problem reverses the majority choice when outcomes are worded as lives saved or lives lost (a22, from memory: about 72% against 22% choosing the sure option; not verified). The heuristics-and-biases view says errors come from fast intuitive processes (later called System 1) that are usually useful and sometimes wrong. The sibling subfield "Heuristics and biases" covers this in depth; here it is the background.

### 2.2 Early debiasing: blame the judge, the task, or the mismatch

Fischhoff (1982, a23) gave the first taxonomy of debiasing: fault lies with the judge (train them), the task (redesign it), or the mismatch between them. His reading of the early work was that warnings and exhortation gave little, and that task redesign and feedback gave more. This chapter was not opened; the claim comes via Croskerry 2013 (a18, a19) and Sellier 2019 (b04).

### 2.3 Two camps on whether errors are fixable by training

- **Pessimists.** Training in one domain does not transfer (Fischhoff 1982; Kahneman and Egan 2011; Milkman, Chugh and Bazerman 2009, all as cited by Sellier, b04). Willingham (2007, a17; 2016, b05) argues critical thinking is not a general skill: it depends on domain knowledge and practice. Metacognitive strategies (consider both sides, look for deep structure) can be learned but are not enough because applying them needs knowledge of the domain. Evidence he gives: a cave-and-sand puzzle solved by about 75% of US students and 25% of Chinese students, reversing for a Chinese folk-tale puzzle; a hint that a band problem resembled the garden problem raised solving from 19% to 35% (a17). Thinking-skills programmes were mostly ineffective (b05: Tactics for Thinking sold 70,000 teacher guides, "not very effective"). No effect sizes are given; both are teacher-facing reviews.
- **Optimists.** Fong, Krantz and Nisbett (1986, a28) found that short statistical training (law of large numbers) improved everyday reasoning in a differently framed context, best when a rule was paired with varied examples. Larrick, Morgan and Nisbett (1990, a16) taught cost-benefit rules. Gigerenzer and Hoffrage (1995, a24) argued errors shrink without instruction when data are stated as natural frequencies. Sedlmeier and Gigerenzer (2001, a25) reported frequency-representation training lasted longer than rule training. Kahneman and Tversky (1996, a29) answered that single-event judgments stay error-prone even with frequency wording.

### 2.4 Consider the opposite, and when it backfires

Lord, Lepper and Preston (1984, a27): telling people to be fair and unbiased did not cut biased assimilation of mixed evidence; asking them to consider the opposite did. Sanna, Schwarz and Stocker (2002, a26): asking people to list many reasons the outcome could have been different can raise hindsight bias, because listing many is hard and the felt difficulty counts as evidence. So the number of alternatives asked for is a boundary condition. Neither paper was opened (K24).

### 2.5 The medical and applied turn

Croskerry, Singhal and Mamede (2013, a18, a19): biases have many causes, so there is no single cure per bias; one-shot interventions are unlikely to work; even aware clinicians may keep a biased conviction; cognitive forcing functions (rules that force a check of alternatives) are the favoured strategy, but evidence is sparse ("an inexact science"). A randomised trial of a checklist-style forcing tool with consider-the-opposite found no gain (b10).

### 2.6 Serious games and the field-transfer claim

From 2013 on, a US research programme (IARPA SIRIUS; Morewedge, Clegg, Dunbar, Veinott and others) built video games that train people on bias with feedback. Reported: games cut targeted biases right after play and at 8 and 12 week retests, and beat a matched training video (a13, a14). The key transfer test is Sellier, Scopelliti and Morewedge (2019, b01-b03): see section 3.

### 2.7 Systematic reviews: little evidence of retention and transfer

Korteling, Gerritsma and Toet (2021, a12): of 52 eligible studies, only 12 adequately tested retention (14 or more days) and only 1 tested transfer. Most positive results came from one programme, using questionnaires built by that group. A 2025 scoping review (b11) of 80 articles and 100 debiasing investigations says 80 reported success, 14 failure (12 no difference, 2 increased bias), 6 partial. But "success" meant one p<.05, with no effect sizes, no publication-bias test, and 33 student samples. A 2025 review in Personality and Social Psychology Review (a20) says strategies aimed at how people think show doubtful durability, while changes to decision structure (defaults, d = .68 in a meta-analysis; precommitment) are sturdier.

### 2.8 The replication crisis hits the baselines

Many Labs 2 (Klein et al. 2018, b06-b09) replicated 28 findings in 125 samples from 36 countries (15,305 participants). 15 of 28 (54%) replicated; median effect size fell from d = 0.60 to 0.15. Two bias-related lines matter: incidental anchors failed (original d = 0.30, N = 207; replication d = 0.04, N = 6,826), while the cheap-versus-costly item framing effect replicated at under half strength (OR 4.96 to 2.06). So the human effect sizes that LLM papers compare against are often inflated.

### 2.9 LLMs enter (2022 on)

- Binz and Schulz (2023, c22) and Jones and Steinhardt (2022, a04) borrowed human experiments to probe GPT-3 and Codex.
- Suri et al. (2023, b16) found GPT-3.5 showed anchoring and other heuristics at human-like size.
- Hagendorff et al. (2023, a07/b19) found GPT-3 fell for cognitive-reflection traps like people, while ChatGPT and GPT-4 mostly did not.
- Turpin et al. (2023, a08/b20) showed that written chain of thought does not reveal planted bias.
- BiasBuster (Echterhoff 2024, a01) made the first systematic prompt-debiasing comparison.
- From 2024 to 2026: large bias benchmarks (Malberg, Knipper, CogBias), prompt-text methods (SACD), judge-bias work, anchoring in agent tasks, and the first look at 2026 judges and reasoning models (d05-d17).

### 2.10 Competing explanations for why debiasing is hard

1. **Biases are not one thing.** Different causes need different fixes (Croskerry, a18). This predicts per-bias, per-model results with no general sign, which is what the LLM data show.
2. **Knowledge and practice decide** (Willingham). A generic instruction cannot supply domain knowledge.
3. **Deliberate thinking is biased too** (Arkes, via a18). Slowing down does not remove the bias, because the bias enters through what is considered. This is why "think carefully" fails.
4. **Format matters more than rationality** (Gigerenzer vs Kahneman and Tversky). Changing how the problem is shown changes the error rate; whether this shows the mind is rational is disputed (K25).
5. **For LLMs, the prompt is the cue.** Many "biases" in LLM studies are prompt sensitivity: the model follows whatever is in its context. That makes the fix an input fix.

---

## 3. Core findings with exact numbers

Status uses the claims.jsonl labels. "Opened" is noted where it matters.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Human bias effects shrink on replication | Many Labs 2: 15 of 28 (54%) replicated; median d 0.60 to 0.15; 9 (32%) opposite direction; 16 (57%) d < 0.20; 15,305 participants, 125 samples | b06 (Klein 2018) | [E] K28 |
| Incidental anchors fail to replicate | Original N=207, d=0.30; replication N=6,826, d=0.04, CI [-0.01, 0.09]; paper-and-pencil only N=1,112, d=-0.01 | b07 | [E] K28 |
| Cheap-item framing shrinks | Original N=181, 68% vs 29%, OR 4.96; replication N=7,228, 49% vs 32%, OR 2.06, CI [1.87, 2.27] | b08 | [E] K28 |
| Human debiasing training: little proof of retention or transfer | 52 eligible studies; 12 tested retention; 1 tested transfer; retention periods 8-12 weeks | a12 (Korteling 2021) | [E] K23 |
| Best field-transfer test of human training | N=290 (182 trained, 108 untrained, not randomised); chose the confirming option 58.8% vs 72.2% (13.4 points; relative drop 19%; OR .549, CI [.33, .92], p=.022). Headline "29% less likely" is not derivable from these cells. 26 excluded for familiarity; 20.4% of untrained did not finish the gaming session | b01-b03, d01 (Sellier 2019) | [S] K22 |
| Sellier effect did not fade over a month | Short lag (<=11 days, n=125) 56.8% vs long lag (43-52 days, n=57) 63.2%; p=.419 (not significant). Narrow windows: 6-day n=94 48.0% vs 72.7%; 4-day n=75 48.0% vs 76.0%; 2-day n=50 50.0% vs 85.7% | b02 | [S] |
| Trained group was already higher on CRT | CRT 2.44 vs 2.18, d=.28 (a confound) | b01 | [S] |
| Extension to risk analysts has no control group | 71 analysts, 118 students; F(1,169)=20.744, partial eta2=.109; pre/post only; same lab | d02 | [S] K40 |
| Serious games beat video in same-lab tests | Retests at 8 and 12 weeks; at 12 weeks only projection stayed lower; Clegg 2015 anchoring scale unreliable | a13, a14 | [C] K21 |
| Sunk-cost training lifted the normative share, not trap-avoidance | Study 3 (N=89): normative personal choice 44% trained vs 28.6% untrained; pure trap answers 11.1% vs 13.1% (no difference) | a16 (Larrick 1990) | [S] |
| Natural frequencies help but most still fail | Meta-analysis (McDowell and Jacobs 2017, via Weber 2018): 24% correct vs 4% with probabilities; new sample of 180: 36% vs 20%; 49% given frequencies still calculated with probabilities | d03 | [C] K25 |
| Cognitive forcing checklist did not help | 2.8 vs 3.1 correct, CI -0.94 to 0.45, p=.49; 76 of 300 analysed | b10 | [S] K26 |
| Awareness line gives small, uneven effect on LLMs | GPT-4 framing gap: base -0.405, awareness -0.470 (worse), counterfactual -0.570 (worse), contrastive -0.410, self-help -0.010. GPT-3.5: base 0.165, awareness 0.035, self-help -0.080 | a01, b12 (BiasBuster) | [E] K01 |
| Debiasing instruction fixes response bias, hurts judgment bias | Response +40.5; Social +5.9 (partly more "cannot determine" answers); Information -1.1; Judgment -4.4 (three models, family level). Per-bias: helped illusion of control +7.0, in-group +6.6, framing +5.8; hurt attribution error -21.0, hyperbolic discounting -13.4. Per-bias table partly garbled | c08, c09 (CogBias 2026) | [S] K02 |
| Specific instruction beats general reminder | Naming the bias: GPT-4 79%, Gemini 1.0 Pro 80%, LLaMA3-70B 50.2%; abstention raised GPT-4 from 33.2% to 48.4%. Needs a detector; author-built dataset | a10 | [C] K19 |
| AwaRe helps some cells, SoPro hurts | AwaRe helped GPT-3.5 on 5 biases, GPT-4 on bandwagon and verbosity only; SoPro made bandwagon worse; order bias unchanged by any method | a05 (Sumita 2024) | [C] |
| Prompt detail has modest, per-bias effect | TELeR levels 3-4: +6.5 to +14.9% resistance; Overattribution -8.2% from level 1 to 2; 45 models, 2.8M responses; bias-consistent in 17.8-57.3% of instances | c11, c12 (Knipper 2025) | [C] |
| Ignoring the anchor does not work | GPT-4 and GPT-4o: CoT, principles, "ignore", reflection all left anchoring significant. Anchoring index ~0.45 (GPT-4) vs 0.61 humans | b18, c13 | [E] K03 |
| Showing opposing anchors helps when they bracket truth | GPT-4 near bias-free on 8 of 15 plotted questions | c14 | [S] K17 |
| Anchoring is common, shallow, least in reasoning models | 22-61% of questions anchored; DeepSeek-R1 25.0%, Qwen3-235B thinking 22.0%, GPT-4o 27.3%, Llama-3.1-8B 34.7%. Fixes on 7-8B: question-aware 36.8%, knowledge 50.5% (worse), Anti-DP 24.7% | c15, c16, d08 | [E] K16/K03 |
| Anchoring in agent self-play | Spearman rho opening to final price: Claude Sonnet 4.5 0.78; Gemini 2.5 Pro 0.91; N=100 games each | d07 | [E] K37 |
| A true specific warning helps reasoning models | Buyer utility loss to a seller anchor, uninformed (informed): GPT-4o 0.38 (0.32); o1 0.40 (0.20); Qwen2.5 0.41 (0.20); QwQ 0.26 (0.00); N=322 | d09 | [C] K38 |
| Rewriting the input cuts planted bias (SACD) | FOMC Llama3.1-8B: vanilla 0.3805, CoT 0.3425, Reflexion 0.3830, debate 0.5020, selfhelp 0.2100, SACD 0.1570. Medical (gpt-3.5) vanilla 0.6655, SACD 0.1585. Errors of the debiaser: finance selfhelp 257/500 vs SACD 61/500 | a06, c04-c07 | [S] K05; the principle [E] K04 |
| SACD first pass can be worse; gains flatten | Finance by pass: 0.2070, 0.1460, 0.1175 vs vanilla 0.1648. Medical: 0.2260, 0.1610, 0.1585 | c05 | [S] |
| Debate and reflection can amplify planted bias | Debate 0.5155 (FOMC gpt-3.5); Reflexion 0.5585 (PubMedQA Llama-70B) | c06 | [S] K06 |
| Self-help rewrite removes bias elements for strong models | GPT-4: group-attribution elements to 0%, framing to 2.7% (share of biased prompt elements left, not outcome gap); GPT-3.5 only 8.9% cut | c03 | [E] K04 |
| Writing neutral best practices first halves prompt-induced bias | Median sensitivity: control 12.9%; CoT 16.1%; bias warning 10.3%; both warnings 8.3% (not significant per bias); axioms plus warning 6.3% (p<.001, BH); axioms alone 7.2%. Anchoring p=.083; hindsight no help. Cheap models | d06 (Sovrano 2026) | [S] K34 |
| Baseline sensitivity on perturbed dilemmas | 6 models: mean sensitivity 5.9% (anchoring) to 35.3% (hindsight); up to 49% on harder items; sensitivity rose with reasoning depth for 5 of 8 biases; models often said they noticed the bias and still flipped | d05 | [S] |
| Cross-model audit of the reasoning trace | Qwen2.5-72B alone 0.805; best fixed auditor 0.824; per-bias selector 0.884; sycophancy 0.655 to 0.890 (GLM-5) but 0.640 with GPT-4o auditor; Kimi-K2.5 as auditor 0.400 on bandwagon. 25 items per cell | d11 | [S] K35 |
| Intrinsic self-correction lowers accuracy | GPT-3.5 CSQA 75.8 to 38.1 (after round 1 at 3 calls); GPT-4 GSM8K 95.5 to 89.0 (after round 2, 5 calls); with oracle labels GPT-3.5 GSM8K 75.9 to 84.3, CSQA 75.8 to 89.7 | c24 (Huang 2024) | [E] K07 |
| CoT does not guard against planted bias | GPT-3.5 biased context 39.5 to 23.3 with zero-shot CoT; Claude 1.0 37.3 to 34.7; accuracy drop up to 36%; 1 of 426 explanations named the bias | b20, a08 (Turpin) | [C] K08; the 1-of-426 [S] K09 |
| CoT made a child-learner bias larger | 20 of 23 conditions significant; accuracy down by more than 50 points for base LLaMA2 7B/13B, Mistral 7B | a03 (Opedal) | [C] K08 |
| CoT raises stereotype output | Abstract-level only: zero-shot CoT raised toxicity and stereotypes (text-davinci-003) | a09, b26 | [C] K08 |
| Trap items are solved by newer models; variants still bite | CRT correct: davinci-003 5%, ChatGPT-3.5 59%, GPT-4 96%, humans 38%. Intuitive error: 80%, 15%, 0%, humans 55%. GPT-3 with premise changed kept old answer (Cab problem 15% blue stated, answered 20%) | a07, b19, c20, c22 | [E] K15 |
| Reasoning suffix rescued an old model on traps | davinci-003 with "Let's use algebra": correct 5% to 28%, intuitive 80% to 29%; semantic illusions with "check for invalid assumptions": 18% to 54% | a07, c21 | [S] (old model) |
| Few-shot examples collapse or carry the bias | Llama-2 7B contrastive: admit rates 0.996 and 1.000; same-task examples cut belief bias less than format-only examples | c02, c18 | [E] K12 |
| Few-shot gains on traps are pattern copying | davinci-003 CRT type 2: 2% to 92% after 2 examples; type 1: 0% to 78% after 30 | c21 | [S] |
| Instruction tuning raised some biases | Certainty bias: DaVinci-002 0.24 to DaVinci-003 0.67; belief-invalid 0.00 / 0.55 / 0.65 | a02, c17 | [C] K13 |
| Backbone sets the bias pattern more than tuning | 32 biases; silhouette by pretraining 0.028 vs random 0.014; scenario-level 0.066 vs 0.034; seed-mean correlation 0.49 (OLMo), 0.59 (T5) | c19, d04 | [C] K13/K32 |
| Size does not reliably cut bias | 20 models: mean absolute bias 0.36 vs 0.54 random chooser; larger OpenAI models somewhat more biased; 1B Llama looked unbiased because it failed to decide in 33% of tests | a11, b17 | [C] K14 |
| Neutral earlier user turn raises bias | +0.086 (Llama-3.1-8B, about 25% of baseline), positive in 7 of 8 models; biased turn +0.022 to +0.051 in 6 of 8 | c26, d17 | [S] K18 |
| Irrelevant earlier code hurts, anchors copied | Codex accuracy down 22.3 to 30.5 points; verbatim copying 7-12% | a04, b15 | [S] K33 |
| LLM judges have position bias | Swap conflict rate GPT-4 46.3% and 5.0%; ChatGPT 82.5% and 52.5%; swap consistency GPT-4 65.0%, GPT-3.5 46.2%, Claude-v1 23.8%; calibration +9.8 (GPT-4), +14.3 (ChatGPT) agreement points; math grading failures 14 default, 6 CoT, 3 reference-guided | b21, b22 | [E] K10 |
| 2026 judges still flip | Order-flip, JudgeBench direct prompt: GPT-5.2 11.0%, Claude-Sonnet-4.6 14.9%, GPT-4o 24.0%, Gemini-2.5-Pro 56.0%; 7-17% of verdicts change on identical reruns at temperature 0; one-call rubric 77.9% trustworthy vs 28.9% direct for Gemini-2.5-Pro; four-call decomposition lowered trustworthiness for 5 of 6 judges | d14 | [E] K36 |
| Judge consistency table for 2024 judges | Position consistency GPT-4 0.82, Llama-3.3-70B 0.80, GPT-4o 0.76, GPT-3.5 0.70, Gemini-1.5-pro 0.62; position bias depends mostly on how close the two answers are | d12 | [E] K10 |
| Self-preference is mostly a label effect | Self-label +0.43 on 7-point scale (CI .39-.47); true source +0.02 (p=.689); with a deterministic checker, gap -5.1 points, CI [-12.9, +2.7] (underpowered). Older: models over 100B preferred own output over 50% of the time | d15, d16, c23 | [C] K11, [S] K39 |
| Reasoning judges still swayed | Targeted system prompt up to 19% (preference) and 14% (facts); in-context examples up to 27% (preference); self-reflection up to 10% and 16%; fake "wait, let me think" pushes toward later options | d10 | [S] K39 |
| Escalation of commitment depends on social setting | Alone: minimal (N=4,000); hierarchy 46.2%; symmetric peers 99.2% (N=500); compound pressure 68.95% (N=2,000) | d19 | [S] K41 |
| Contextual calibration fixes label/order bias | Up to 30.0 points accuracy gain, lower variance (GPT-3, GPT-2; needs logits) | b24 | [S] K29 |
| Activation steering | Bias scores down 26-32% on open models; Qwen capability loss up to -19.0 pp | c10 | [S] K30 (not usable) |
| Fine-tuning on balanced reasoning pairs | Choice-supportive bias improved 81.5% (memory) and 94.3% (evaluation); BBQ similar | d18 | [S] (not usable) |
| Sycophancy rises with scale and tuning | PaLM 8B to 62B +19.8%; 62B to 540B +10.0%; synthetic fine-tune cut it 4.7-10.0% | b25 | [S] (training only) |
| Structure beats instruction in humans | Defaults d = .68 (via a20); 80 of 100 investigations "effective" but by single p<.05 | a20, b11 | [S] K27 |
| Bias scores from one run are noisy | Seed-mean vs original-model bias correlation 0.49-0.59 | c19 | [S] K32 |

---

## 4. Mechanisms and models

Each item below is written so an engineer could build it. For every mechanism, a note says what the evidence supports.

### 4.1 Why instruction fails

- A bias is a pull from something in the context (an anchor, a frame, a first option, a suggested answer, earlier turns). The model weighs it with everything else.
- An instruction adds more context but does not remove the pull. In humans, deliberate thinking is itself biased (Arkes via a18). In LLMs the effect of "ignore the anchor" is not significant on GPT-4 and GPT-4o (b18). Anchoring in LLMs acts in early layers (c15), before any later instruction can be weighed.
- A warning can also change the baseline in an unwanted way, such as raising refusals or "cannot determine" answers (c08 Social +5.9% is partly this) or collapsing answers to all-admit or all-reject (c02).

### 4.2 Why the same fix works for one bias and hurts another

CogBias (c08, c09): a single debias instruction fixed Response bias (+40.5) and hurt Judgment bias (-4.4). Response bias is a mechanical habit (first option, order). An instruction can shift a habit. Judgment bias comes from content (attribution, discounting), where the instruction may push the model to over-correct. The sign depends on the bias type, so a generic "debiasing" step has no safe default. Design rule: never ship an instruction without the per-bias signed delta on our model.

### 4.3 Input hygiene (what works, mechanism)

Algorithm (planted-cue case), as in BiasBuster self-help and SACD (a01, a06):
1. Code splits the input into task text and suggestive material (stated guess, authority claim, frame words, unrelated number, prior verdict).
2. A model call writes a neutral restatement of the task from the task text alone; the suggestive material is held in a marked side block, not deleted from the log.
3. Attempts see the restatement and the side block marked as "not evidence".
4. SACD loop: for each sentence, a model flags "biased or not"; for flagged sentences, analyse the bias; rewrite only those sentences; repeat until none is flagged or 3 passes are used. Gains flatten after pass 2 or 3 (c05). Finance pass 1 can be worse than vanilla (0.2070 vs 0.1648).
5. The debiaser makes its own errors. SACD errors mostly confuse bias types (61/500 in finance), self-help mostly under-debiases (257/500) (c07).

What this does and does not show. It shows planted text can be found and removed. It does not show anything about biases that arise inside the model. Author-planted cues are also easier to detect than natural ones (critique, weak spots).

### 4.4 Neutral-rules-first (Sovrano 2026, d06)

Step 1: ask the model to write the best practices or axioms that should govern this kind of decision, without showing the biased wording. Step 2: answer with those axioms in context. Median sensitivity 12.9% to 6.3% with warning, 7.2% without. It works because the axioms are generated before the cue is read, so they anchor the decision to principles, not to the cue. Cost: one extra generation. Not tested against best-of-N at equal tokens.

### 4.5 Show both sides

Lou and Sun (c14): present a low and a high anchor together. GPT-4 landed near the bias-free value on 8 of 15 plotted questions. Mechanism: two opposing pulls cancel. Implementation in code: generate an opposite reference point (for a number, a value on the other side of the plausible range; for a choice, the rival option stated as the default) and show both. Fails when the truth is outside the bracket. Human analogue: consider the opposite (Lord 1984). Boundary: ask for one opposite, not five (Sanna 2002).

### 4.6 Representation change

Restating probabilities as natural frequencies (a24, d03) is a code transform. Result in people: 36% vs 20% correct in a 180-student sample; 49% still converted to probabilities. For an LLM the transform could be applied by code before the model sees the item.

### 4.7 Judge debiasing

- Position bias: run each pair in both orders in code and aggregate (b21: +9.8 and +14.3 agreement points). Require evidence before verdict. Provide a reference answer (math failures 14 of 20 to 3 of 20, b22).
- Measure the flip rate of the judge first. Accuracy is capped at 1 - flip/2 (d14). If the flip rate is 56% the judge is almost useless in single-call mode.
- Hide authorship and strip filler (d15, d10): a label alone moves scores by 0.43 points on 7.
- Prefer one-call rubric scoring over multi-call decomposition (d14: decomposition hurt 5 of 6 judges).
- Where a deterministic checker exists, use it, not a judge (d16).

### 4.8 Context hygiene

Weerasekara (c26, d17): any earlier user turn raised measured bias, even a neutral one, in 7 of 8 models. Code design: keep a clean copy of the task; for each decision-making attempt, build the context from the task, the restatement, and the minimum state needed. Do not carry prior conversation or tool text unless needed. Pruning has not been tested (d17).

### 4.9 Why debate and peer review can make it worse

Debate scored 0.5020 and 0.5155 on planted-bias cells, worse than vanilla 0.3805 (c04, c06); the authors say agents learn from biased feedback (untested). Escalation of commitment reaches 99.2% among symmetric peers and is minimal alone (d19). Pattern: a second voice that sees the first voice's answer defers to it. This supports G4 and G9, and says a critic must not see the proposed answer.

### 4.10 Cross-model audit and its limit

Chain-of-Models (d11): a second model from another family audits the trace. Gain 0.805 to 0.884 only if the auditor is picked per bias, and a strong solver may be a poor auditor (Kimi-K2.5, 0.400 on bandwagon). The single-agent design uses one model, so the only testable analogue is a same-model fresh-context audit that sees only the task and the chain, not the proposed answer.

### 4.11 Contextual calibration

Estimate the model's prior with a content-free input ("N/A") and subtract it from label scores (b24). Up to 30 points in GPT-3 classification. It needs log-probabilities, which closed APIs may not give. Possible with counted samples instead of logits, but untested.

### 4.12 Measurement mechanics (this matters for our bench)

- Score per bias as a paired shift: same item with the cue and without it. Report signed delta, not just accuracy.
- Run at least 5 samples per item; single-run bias scores correlate only 0.49-0.59 with the seed mean (c19).
- Include perturbed variants. Famous items (CRT) are solved by memory (K15).
- Compare effect size with Many Labs 2 sizes (median d 0.15), not with 1970s sizes.

---

## 5. What holds up

### 5.1 Replications and failed replications

| Result | Verdict |
|---|---|
| Incidental anchors (Critcher and Gilovich 2008) | Failed to replicate (d = 0.04, N = 6,826). |
| Cheap-item framing (T and K 1981 study 10) | Replicated at under half strength (OR 4.96 to 2.06). |
| Whole Many Labs 2 slate | 54% replicated; median d 0.60 to 0.15. Heterogeneity across samples was significant for 11 of 28 (39%); only one had tau above 0.20. (The critique could not confirm "19 of 28 near zero heterogeneity" and "13 of 14 reliable in WEIRD and less-WEIRD"; treat those as unverified.) |
| Explicit numeric anchors | Not in the ML2 slate. The cheap-anchor failure does not show numeric anchoring is fragile. LLM and human data both show numeric anchoring. |
| Sellier 2019 field transfer | No independent-lab replication found (d01, K40). The 2025 extension shares authors and has no control group. |
| Serious games (Morewedge 2015, Clegg 2014/2015) | No independent replication found; some outcome scales unreliable (a13). |
| Sedlmeier 2001 retention | Not opened, not independently checked. |
| Unconscious-thought effects | Failed to replicate (in 4b; F03/F04). |

### 5.2 Meta-analyses and reviews

- Korteling 2021: weak evidence for retention and transfer (52, 12, 1).
- Dharanikota 2025: 80 of 100 "effective" by p<.05 only; inflated.
- McDowell and Jacobs 2017: frequency format 24% vs 4% correct (via Weber 2018).
- Defaults d = .68 (Jachimowicz 2019, via a20).
- No meta-analysis of LLM debiasing exists in our sources. Sumita 2024 (a05) is a survey of 30 studies plus small experiments.

### 5.3 Moderators and boundary conditions

- **Bias type.** Response and order biases respond to instructions; judgment biases can get worse (c08).
- **Model capability.** Self-help rewriting works for high-capacity models (GPT-4: elements to 0-2.7%), not low-capacity ones (a01, c03). Reasoning models are least anchored but not zero (22-25%).
- **Model age.** Many sources use GPT-3.5, Claude 1.0, Llama-2, Codex. Instructions rescued davinci-003 on traps, but ChatGPT-3.5 and GPT-4 do not need them (a07).
- **Number of alternatives.** Few help, many backfire (humans, a26).
- **Anchors must bracket the truth** for the both-anchor fix (c14).
- **Warning specificity.** A true warning that names the actual cue helped o1 (0.40 to 0.20) and QwQ (0.26 to 0.00); a generic one barely moved GPT-4o (0.38 to 0.32) (d09).
- **Social context.** Escalation: minimal alone, 99.2% among symmetric peers (d19).
- **Prior turns.** Any prior user turn raises measured bias (c26).
- **Retention interval and test format.** Humans trained and tested in the same format look better; transfer is the hard part (a12, b04).

### 5.4 Interventions that worked

1. Removing or rewriting the cue in the input (self-help, SACD) on planted cues (K04, established but narrow).
2. Writing neutral rules first (d06, single-source).
3. Both-side anchors that bracket the truth (c14, single-source).
4. Swapping order and aggregating for judges, with evidence first or reference answers (b21, b22).
5. One-call rubric scoring for judges (d14, single-source).
6. A specific, true warning about a real cue for reasoning models (d09, contested).
7. Format change to natural frequencies (d03, contested).
8. Structure changes for humans: defaults and precommitment (a20, secondary).
9. Human serious-game training: positive in same-lab tests; transfer to a field case at 59% vs 72% (b01).
10. Cross-family audit on planted cues (d11), not available to a single-model agent.
11. Training-time routes (steering, fine-tuning on balanced pairs, synthetic anti-sycophancy data, contextual calibration): positive but unavailable or unproven for a scaffold (c10, d18, b25, b24).

### 5.5 Interventions that did not work

1. Generic "be unbiased" / awareness lines (K01, established): inconsistent sign; GPT-4 framing gap worse (-0.470 vs -0.405).
2. Ignore-the-anchor, thoughts-of-principles, CoT, reflection on anchoring (K03).
3. Few-shot debiasing examples (K12): answers collapse or new bias appears.
4. Intrinsic self-correction (K07).
5. Debate and Reflexion-style review under planted bias (K06).
6. Chain of thought as a bias guard (K08, contested): it helped davinci-003 on CRT but hurt GPT-3.5 in biased context (39.5 to 23.3), enlarged the consistency bias, and raised stereotype output.
7. Cognitive forcing checklist with consider-the-opposite (b10, underpowered).
8. Knowledge enhancement for anchoring (c16: 34.7% to 50.5%, worse).
9. Thinking-skills programmes and general critical-thinking training (K31).
10. "Be fair and unbiased" in humans (Lord 1984, a27, secondary).

### 5.6 Reconciling the contradictions

- Awareness prompts: harmful on GPT-4 framing, helpful on GPT-3.5, helpful 6.5-14.9% at Knipper levels 3-4, harmful on judgment biases, sign flips with persona (c27). Net: no reliable direction. Treat as per-bias, per-model, per-wording.
- SACD works while Huang says self-correction fails. Likely reconciliation (critique): SACD edits visible cues in text the model can see. Huang asks the model to judge the truth of its own reasoning, which it cannot. Same split as G2: locate by code or by visible text, then fix.
- Itzhak 2024 vs 2025: 2024 shows tuning shifts certain biases; 2025 shows the overall pattern across 32 biases follows the backbone. Different questions. Both cover 7-11B models and supervised tuning only. RLHF and reasoning RL are untested (d04).
- Scale: Malberg says larger OpenAI models are somewhat more biased; Knipper says over 32B reduces bias in some cases; SynAnchors says reasoning models are least anchored. Different bias sets and metrics.

---

## 6. Language models

### 6.1 Do LLMs show the human biases?

Yes, for most, at roughly human size on many tasks.
- Anchoring in GPT-3.5: low-anchor mean 20.83 vs high 105.97, t(58) = 8.78; humans 22.50 vs 80.50 (b16, 30 trials per condition).
- Anchoring index 0.45 (GPT-4) vs 0.61 in the human study (c13, approximate).
- 30 biases appear in at least some of 20 models (b17); mean absolute bias 0.36 vs 0.54 for a random chooser. Some go opposite to humans (status quo -0.42, disposition effect -0.6).
- Knipper: bias-consistent behaviour in 17.8-57.3% of instances across 45 models (c11).
- CogBias: all three models biased in all four families (c08); first-option pick 77-79% vs 36.8% chance.
- Frontier agents: opening-to-final price rho 0.78 (Claude Sonnet 4.5) and 0.91 (Gemini 2.5 Pro) (d07). Some link is rational in bargaining, and there is no human baseline.
- Code: irrelevant earlier code lowered Codex accuracy by 22.3-30.5 points (a04).
- Perturbed dilemmas: sensitivity 5.9% (anchoring) to 35.3% (hindsight), up to 49% on harder items (d05).
- Escalation of commitment is minimal alone and large in groups (d19).

### 6.2 Did the famous trap items stop working?

Mostly yes, probably from training exposure. CRT correct: davinci-003 5%, ChatGPT-3.5 59%, GPT-4 96%; intuitive-error 80%, 15%, 0% (a07). But reworded or perturbed items still catch models: GPT-3 answered 20% on a Cab problem stated as 15% (c22), and a CRT item with changed premise kept the old answer. Newer models also still fail on harder perturbed sets (d05). Lesson: bench items must be mutated (K15).

### 6.3 What changed LLM bias, with numbers

| Lever | Result | Evidence |
|---|---|---|
| Generic awareness line | GPT-4 framing worse (-0.405 to -0.470); GPT-3.5 better (0.165 to 0.035); judgment bias -4.4 points average | a01, c08 |
| Name the specific bias | Better than general reminder, needs detector | a10 |
| Cue-named true warning | o1 loss 0.40 to 0.20; QwQ 0.26 to 0.00 | d09 |
| Think carefully (semantic illusion suffix) | davinci-003 18% to 54% correct | a07 |
| CoT | Mixed: davinci-003 CRT 5% to 28%, but GPT-3.5 biased context 39.5 to 23.3; stereotypes up | a07, b20, a09 |
| Ignore anchor / principles / reflection | No significant change | b18 |
| Few-shot | Collapse or new bias | c02, c18 |
| Self-help rewrite | GPT-4 biased prompt elements to 0-2.7% | c03 |
| SACD | FOMC 0.3805 to 0.1570 (Llama3.1-8B); medical 0.6655 to 0.1585 | a06 |
| Neutral rules first | 12.9% to 6.3% sensitivity | d06 |
| Both anchors | 8 of 15 near bias-free | c14 |
| Cross-model audit | 0.805 to 0.884 | d11 |
| Intrinsic self-correction | Accuracy down (75.8 to 38.1) | c24 |
| Debate | Worse than vanilla under planted bias | c04, c06 |
| Instruction/RLHF tuning | Certainty 0.24 to 0.67; backbone dominates pattern | c17, d04 |
| Activation steering | Bias scores -26 to -32% (open models, capability cost) | c10 |
| Fine-tune on balanced pairs | Choice-supportive bias -81.5%/-94.3% | d18 |
| Prior user turn | Bias up (+0.086 neutral, Llama-3.1-8B) | c26 |

### 6.4 LLM-as-judge

- 2023 judges: 40% of comparisons biased (b23); swap consistency GPT-4 65.0%, GPT-3.5 46.2%, Claude-v1 23.8% (b22); conflict rate 5.0-82.5% (b21).
- 2024 judges: consistency 0.62-0.82 pairwise (d12); robustness to position GPT-4o 0.776, Claude-3.5 0.832 (d13).
- 2026 judges: GPT-5.2 flips 11.0%, Claude-Sonnet-4.6 14.9%, GPT-4o 24.0%, Gemini-2.5-Pro 56.0% on JudgeBench (d14). Reruns change 7-17% of verdicts at temperature 0. Self-label shifts scores +0.43 on 7 (d15). Self-preference vanishes when blind, and is not seen with a deterministic checker (d16, underpowered).

### 6.5 Reasoning models

Reasoning models are least anchored (22.0% and 25.0% of questions vs 27-61% for others) but not unbiased (c15, d08). o1 lost as much as GPT-4o to a seller anchor unless warned (d09). Reasoning judges still follow bandwagon, authority, position and distraction cues, and a pasted "wait, let me think" pushes them toward later options (d10). Sensitivity rose with reasoning depth for 5 of 8 biases in PROBE-SWE (d05). DeepSeek-R1-distill showed gains from the axioms step (6.6-7.9%) (d06).

### 6.6 What the LLM literature cannot yet say

- Almost all studies plant the cue in the prompt (critique). Debiasing there means detecting and deleting text.
- Models are mostly 2022-2024. The only 2026-vintage rows are judges (d14, d15), a few agent tasks (d07, d09) and PROBE-SWE mitigation on cheap models (d06).
- No study compares a debiasing step against plain model and best-of-N at equal tokens.
- Bias scores differ by paper; cross-paper sizes are not comparable.

---

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested. Schema part: G, S, O, or memory.

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Keep 4b as written.** Do not add bias checklists, awareness lines or "be unbiased / be careful" instructions. Add to 4b the new evidence: GPT-4 framing worse under awareness; CogBias Judgment -4.4 and per-bias drops of 13-21 points are single-source and must not be quoted as established. | 4b / G7 | [E] | K01 (a01, b12, c02, c08, c09, c12, c27, a05, d06, d09) |
| A2 | **Do not add "ignore the anchor", principles, CoT or reflection as anchoring guards.** | 4b / G1 / G2 | [E] | K03 (b18, c13, c16, a04, d08) |
| A3 | **Do not add few-shot debiasing exemplars.** | 4b | [E] | K12 (a01, c02, c18, a02, c06) |
| A4 | **Revise only from real output; intrinsic second look lowers accuracy.** G2 stands. | G2 | [E] | K07 (c24, c16, b18) |
| A5 | **Input hygiene may be marked [E] for planted-cue text.** Keep S1 as is: code moves suggestive material into a marked block; the model writes a neutral restatement. Scope the mark to planted cues. The remedy for unplanted bias stays [S]. | S1 | [E] (planted cues only) | K04 (a01, b12, c03, c04, c05, a06, d06, d11) |
| A6 | **Judge step, if used: both orders aggregated by code, evidence before verdict, reference answer when available, authorship hidden, filler stripped, and the judge's flip rate measured before use.** Add the measured flip rate (2026 judges 11-56% on JudgeBench) to G5's text. | G5 | [E] (swap and aggregate, flip rate); label hiding [S] | K10, K36 (b21, b22, d12-d14); K39 (d15, d10) |
| A7 | **Never let the model's reasoning text stand in for evidence of no bias.** G10 stands. Planted-bias evidence: 1 of 426 explanations named the cue [S]. | G10 | [E] G10; the count [S] | a08, b20, c25 |
| A8 | **No debate, no deferring critic.** G9 stands. Add: critics must not see the proposed answer. | G9 / G4 | [E] G9; mechanism [S] | K06, K41 (c04, c06, d19) |
| A9 | **Bench design rules:** use mutated variants, not famous items; score bias as a paired signed delta; use 5 or more samples per item; compare with Many Labs 2 sizes (median d about 0.15) not 1970s sizes. | G3 / G7 | [E] | K15, K28, K32 (c20, c22, a07, b06-b08, c19) |
| A10 | **Human-training results are no support for a "train the agent" step.** Transfer needs a changed procedure or input, not memory. Willingham: domain knowledge and practice decide, so use domain checks in the gate rather than a general "think critically" line. | 4b / memory / S0 | [E] | K20, K23, K31 (a12, b04, b05, a17, a23, a27, a18, a19) |
| A11 | **Account for contextual drift:** record in S9 whether a decision was made in a clean context or one with prior turns. | log | [S] | K18 (c26, d17) |

A11 is [S] and is listed here only as a cheap log field; the effect itself goes to Test first.

### 7.2 Test first (not established)

| # | Candidate | Schema part | Status | Evidence | Why not yet |
|---|---|---|---|---|---|
| T1 | Neutral rules or best practices written before the answer, for open or judgment items. | S1 / S2 | [S] | K34 (d06, d05) | Cheap models, planted cues, extra tokens, no best-of-N arm. |
| T2 | Neutral restatement vs raw input on cues the authors did not plant (natural wording cues). | S1 | [S] for the unplanted case | K04, K05 (a06, c05) | All evidence is planted. |
| T3 | Both-sides reference: a code-made opposing anchor or rival option shown with the original. | S1 / O6 | [S] | K17 (b18, c14) | Two models, 15 questions; needs bracket. |
| T4 | Consider-the-opposite with 1 vs 3 vs 5 counter-reasons. | O4 / G1 | [C] | K24 (a26, a27) | Humans only; both papers unopened. |
| T5 | Cue-named warning from a code detector vs generic reminder vs nothing. | S1 / G5 | [C] | K19, K38 (a10, d09, d08) | Detector cost; author-built data. |
| T6 | Natural-frequency or format restatement in code (probabilities to counts). | O6 | [C] | K25 (a24, d03) | Human data, immediate tests only. |
| T7 | Forced disconfirming test (P and not-Q) chosen by code; link to S7 counterexample search. | S7 / G3 | [S] | K22 (b01, b02) | Single quasi-experiment. |
| T8 | Clean-context vs history-loaded context; pruning in code. | S1 / memory | [S] | K18 (c26, d17) | 2024 models, user turns only. |
| T9 | Same-model fresh-context audit that sees task and chain but not the proposed answer. | S8 / critic | [S] | K35 (d11) | Original used a second model family. |
| T10 | Judge: swap-and-aggregate (2 calls) vs one-call rubric score vs fixed order, at equal tokens. | G5 | [E] direction, cost unknown | K10, K36 (d14, b21) | Cost at equal tokens unmeasured. |
| T11 | Deferring critic vs independent critic on sunk-cost items. | critic design | [S] | K41 (d19) | Abstract-level numbers. |
| T12 | Baseline bias size of our own model (and a 2026 reasoning model) on a perturbed battery, with a generic reminder arm to look for backfire. | S0 | [S] / [C] | K02, K14, K16, K37 | No frontier 2026 test of judgment-bias instructions. |
| T13 | Null-input prior subtracted from label scores, from sampled answers. | G5 | [S] | K29 (b24) | Needs logits in the original. |
| T14 | Structure-change fixes (defaults, ordering of options by code, shuffled options) vs instruction fixes. | S1 / G5 | [S] | K27 (a20, b11) | Human secondary evidence. |

Not usable in a scaffold-only agent: activation steering (c10), fine-tuning on balanced pairs (d18), synthetic anti-sycophancy training (b25), cross-family auditor (d11, unless a second model is allowed).

---

## 8. Concrete tests on our bench

All arms run at equal total tokens. Setup and rewrite calls are counted. A plain arm gets the saved tokens as extra samples (best-of-N by code) so the comparison is fair. Items are built in pairs: cue present and cue absent. 5 samples per item minimum. Report the signed bias delta, accuracy, and tokens.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 Instruction null | Paired items for 3 biases: anchoring (numeric), framing (A/B decision), suggested-answer (multiple choice) | (a) plain; (b) plain plus one-line awareness; (c) plain plus best-of-N using spare tokens | Signed bias delta (biased minus neutral accuracy); items changed; per-bias sign | (b) within +-3 points of (a) overall; sign differs by bias; confirms 4b. If (b) beats (c), reopen 4b. |
| B2 Anchoring guards | 40 numeric estimates with seeded anchors, plus unanchored twins | plain; ignore-the-anchor; short CoT; both-sides reference (T3) | Anchoring index; mean absolute error | Ignore and CoT near zero change; both-sides reduces index where anchors bracket truth. |
| B3 Neutral restatement | Items with a suggested answer, authority claim or stated guess; one set with cues we plant, one set with cues taken from real text | raw input; neutral restatement in S1; neutral restatement plus 2 samples vs plain 3 samples | Accuracy; flip rate against cue-free twin | Large gain on planted set; smaller (maybe none) on natural set. Add if the natural-set gain is at least 3 points and holds at equal tokens. |
| B4 Neutral rules first | 40 dilemmas in the PROBE-SWE style, 6 biases | control; CoT; bias warning; rules-first; best-of-2 control | Sensitivity (share of decisions that flip with cue); per-bias | Rules-first about half of control sensitivity if d06 transfers; check anchoring and hindsight separately (they did not improve). |
| B5 Opposites count | Hindsight and confirmation items | no opposite; 1 counter-reason; 3; 5 | Drift from neutral twin | U-shaped: 1-3 help, 5 may backfire (Sanna). |
| B6 Disconfirming test | Wason-style and hypothesis-confirming business cases, mutated | plain; code-selected P-and-not-Q test; model-chosen test | Share choosing the confirming option | Code-selected test lowers confirming choice by 5-15 points; model-chosen about the same as plain. |
| B7 Format restatement | Bayesian base-rate items with probability and frequency versions, mutated numbers | probabilities; code converts to natural frequencies; plain with CoT | Accuracy; exact-answer rate | Gain on older or smaller models; little on a 2026 reasoning model (ceiling). |
| B8 Context hygiene | Same bias items alone vs after 3-6 neutral turns vs after tool output | full history; code-pruned context | Bias magnitude (paired delta) | Neutral turns raise bias a few points; pruning removes it. |
| B9 Judge reliability | 100 pairs with known winner, plus order-swapped copy | fixed order; swap and aggregate; one-call rubric; labeled vs blind authorship | Flip rate; accuracy; trustworthy rate; tokens | Flip rate between 10% and 50% for our judge; swap-and-aggregate removes most of it at 2x cost; rubric one-call cheaper. |
| B10 Critic independence | Sunk-cost and escalation items, planner plus critic | no critic; critic sees proposed answer; critic sees only task and chain | Escalation rate; accuracy | Critic that sees the answer defers (rate up); independent critic about the same as no critic. |
| B11 Backfire sweep | 10 judgment biases (attribution, discounting, disposition, etc.) with 5 samples each | plain vs generic debias line | Per-bias signed delta | Mixed signs. If any bias drops by 10 or more points, G7 stays. This checks CogBias on our model. |
| B12 Self-correction control | Items with checks | second look with no failing output; second look with code-located failing output | Right-to-wrong and wrong-to-right counts | First lowers net accuracy; second raises it (G2). |

---

## 9. What does not transfer, and why

1. **Human training with memory and practice.** Games, lectures and feedback change what a person remembers and notices. Our agent has no cross-run memory except lessons shown after the first attempt. Only the procedure the training teaches can be copied (for example "test the case that could prove you wrong").
2. **Human consider-the-opposite and the "difficulty of listing" effect (Sanna).** The felt-difficulty mechanism needs a person's metacognitive feeling. An LLM has no such signal. Number of counter-reasons may matter for other reasons; untested.
3. **Awareness and motivation.** "Try harder" and "be fair" rely on effort and values. A model has neither in the same sense; an instruction is just more context.
4. **Willingham's knowledge point only partly transfers.** The model has broad knowledge. Domain-specific checks still help; the gate can supply them.
5. **Planted-cue removal does not show internal debiasing.** SACD and self-help results are about text in the prompt. They say nothing about biases from weights (the authors admit this, a06).
6. **Training-time fixes.** Activation steering (c10), fine-tuning on balanced reasoning pairs (d18), synthetic anti-sycophancy data (b25) and contextual calibration with logits (b24) need weights, training, or probabilities. Our agent is scaffold-only.
7. **Cross-family auditing** (d11) needs a second model. The single-agent design has one.
8. **Human sample effect sizes (1970s-80s).** Replication sizes are far smaller (median d 0.15). Do not use old human sizes as the target for the agent.
9. **Famous trap items.** Models likely saw them. Success there says nothing about debiasing.
10. **Bias scores across papers.** Rate gaps, indices and accuracy deltas cannot be compared. Only same-paper deltas are safe.
11. **Social-bias benchmarks (stereotypes, toxicity, BBQ).** These measure fairness behaviours tied to alignment training. The cognitive-bias results here do not carry over (a09, b26 are social-bias, not decision-bias).

---

## 10. Open questions

1. Does any scaffold-level debiasing step (neutral restatement, opposing references, forced disconfirming test) beat a plain model at equal tokens on unplanted biases, for a 2026 reasoning model? (Critique gap 1; partly informed by d06, which has no equal-token arm.)
2. How big is the baseline bias of frontier reasoning models on perturbed items, compared with Many Labs 2 sizes? No paper makes this comparison (gap 2).
3. Does a generic debiasing instruction backfire on frontier models for judgment biases, and is the sign stable across wordings? (gap 3; CogBias tested GPT-4o-mini, Llama-3.3-70B, Qwen2.5-72B only.)
4. Where does Sellier's "29%" come from, and has anyone outside the lab replicated it? (gap 4; a guess is the .29 odds ratio in the 4-day window.)
5. Does the number of counter-reasons matter for LLMs (1 vs 5)? No LLM study varies it (gap 5).
6. How much of SACD's gain survives on cues the authors did not plant, and against best-of-N? (gap 6)
7. What does swap-and-aggregate cost at equal tokens for 2026 judges? (gap 7)
8. Is bias in an agent's own history and tool outputs measurable and removable by pruning? User turns only have been tested (gap 8).
9. Do independent labs reproduce serious-game and frequency-training retention? (gap 9)
10. Does RLHF or reasoning RL add or remove bias in 2025-2026 models? The two Itzhak papers cover supervised tuning at 7-11B only (gap 10).
11. Is the sign of CoT effects (rescue on davinci-003, harm on GPT-3.5, enlarged consistency bias) a function of model age, task, or planted cue? We have no 2026 measurement.
12. What explains the Knipper 39.5% figure: share of cases or size of reduction? The abstract and the body differ.
13. Is a self-label effect (+0.43) present in a single-agent system where the judge reads its own earlier attempt?

---

## 11. Sources

[V] = opened and read (page or full text this session); [M] = snippet, abstract, or secondary text only. Where a source is [V] but describes another work second-hand, that is said.

**Human studies and reviews**
- [M] Tversky and Kahneman (1974) Judgment under Uncertainty: Heuristics and Biases. Via Jones and Steinhardt. https://arxiv.org/abs/2202.12299 (a21)
- [M] Tversky and Kahneman (1981) The framing of decisions and the psychology of choice. https://doi.org/10.1126/science.7455683 (a22; numbers from memory)
- [M] Fischhoff (1982) Debiasing. https://doi.org/10.1017/CBO9780511809477.032 (a23)
- [M] Lord, Lepper, Preston (1984) Considering the opposite. https://doi.org/10.1037/0022-3514.47.6.1231 (a27)
- [M] Fong, Krantz, Nisbett (1986) Statistical training and everyday thinking. https://doi.org/10.1016/0010-0285(86)90003-X (a28)
- [V] Larrick, Morgan, Nisbett (1990) Teaching cost-benefit reasoning. https://www.gwern.net/doc/psychology/cognitive-bias/sunk-cost/1990-larrick.pdf (a16)
- [M] Gigerenzer and Hoffrage (1995) Frequency formats. https://doi.org/10.1037/0033-295X.102.4.684 (a24; numbers from memory)
- [M] Kahneman and Tversky (1996) On the reality of cognitive illusions. https://doi.org/10.1037/0033-295X.103.3.582 (a29)
- [M] Sedlmeier and Gigerenzer (2001) Teaching Bayesian reasoning. https://doi.org/10.1037/0096-3445.130.3.380 (a25)
- [M] Sanna, Schwarz, Stocker (2002) When debiasing backfires. https://doi.org/10.1037/0278-7393.28.3.497 (a26)
- [V] Willingham (2007) Critical thinking: why is it so hard to teach? https://www.aft.org/sites/default/files/media/2014/Crit_Thinking.pdf (a17)
- [V] Willingham (2016) Knowledge and practice. https://onlit.org/wp-content/uploads/2023/08/Willingham-Knowledge-and-Practice-The-Real-Keys-to-Critical-Thinking.pdf (b05)
- [V] Croskerry, Singhal, Mamede (2013) Cognitive debiasing 1. https://pmc.ncbi.nlm.nih.gov/articles/PMC3786658/ (a18)
- [V] Croskerry, Singhal, Mamede (2013) Cognitive debiasing 2. https://pmc.ncbi.nlm.nih.gov/articles/PMC3786644/ (a19)
- [V] Korteling, Gerritsma, Toet (2021) Retention and transfer of bias mitigation. https://pmc.ncbi.nlm.nih.gov/articles/PMC8397507/ (a12, a13, a15)
- [M] Morewedge et al. (2015) Debiasing decisions, as described by Korteling 2021 and a 2025 review. https://pmc.ncbi.nlm.nih.gov/articles/PMC11734358/ (a14; secondary)
- [V] 2025 review, Personality and Social Psychology Review, debiasing and discrimination. https://pmc.ncbi.nlm.nih.gov/articles/PMC11734358/ (a20; effect sizes quoted from other papers)
- [V] Sellier, Scopelliti, Morewedge (2019) Debiasing training transfers to improve decision making in the field (author manuscript). https://openaccess.city.ac.uk/id/eprint/22233/ (b01-b04, d01)
- [V] Heerma van Voss et al. (2025) Debiasing training in national risk analysts, Scientific Reports. https://www.nature.com/articles/s41598-025-28794-w (d02)
- [V] Weber, Binder, Krauss (2018) Why only 24% solve Bayesian problems in natural frequencies; quotes McDowell and Jacobs (2017). https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01833/full (d03; meta-analysis itself not opened)
- [V] Klein et al. (2018) Many Labs 2. https://osf.io/9654g/ (b06-b09; abstract numbers confirmed, some secondary rows unverified)
- [V] Cognitive forcing tool randomised trial, BMC Medical Education (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6325867/ (b10)
- [V] Dharanikota et al. (2025) Debiasing judgements, distributed cognition scoping review. https://pmc.ncbi.nlm.nih.gov/articles/PMC12049587/ (b11)

**LLM studies**
- [V] Echterhoff et al. (2024) BiasBuster. https://arxiv.org/abs/2403.00811 (a01, b12, b13, c01-c03)
- [V] Itzhak et al. (2024) Instructed to Bias. https://arxiv.org/abs/2308.00225 (a02, b14, c17, c18)
- [V] Opedal et al. (2024) Do language models exhibit the same cognitive biases as human learners. https://arxiv.org/abs/2401.18070 (a03, c28)
- [V] Jones and Steinhardt (2022) Capturing failures via human cognitive biases. https://arxiv.org/abs/2202.12299 (a04, b15)
- [V] Sumita, Takeuchi, Kashima (2024) Survey and mitigation experiments. https://arxiv.org/abs/2412.00323 (a05)
- [V] Lyu et al. (2025) SACD. https://arxiv.org/abs/2504.04141 (a06, c04-c07)
- [V] Hagendorff, Fabi, Kosinski (2023) Thinking fast and slow in LLMs. https://arxiv.org/abs/2212.05206 (a07, b19, c20, c21)
- [V] Turpin et al. (2023) Language models don't always say what they think. https://arxiv.org/abs/2305.04388 (a08, b20, c25)
- [V] Shaikh et al. (2023) On second thought, let's not think step by step. https://arxiv.org/abs/2212.08061 (a09; b26 abstract and first page only, so exact rates are [M])
- [V] Zhong et al. (2025) Balancing rigor and utility. https://arxiv.org/abs/2406.10999 (a10)
- [V] Malberg et al. (2024/2025) Comprehensive evaluation of cognitive biases in LLMs. https://arxiv.org/abs/2410.15413 (a11, b17; the critique re-checked the abstract only)
- [V] Suri et al. (2023) Decision heuristics in GPT-3.5. https://arxiv.org/abs/2305.04400 (b16)
- [V] Lou and Sun (2024) Anchoring bias in LLMs. https://arxiv.org/abs/2412.06593 (b18, c13, c14)
- [V] Wang et al. (2023) LLMs are not fair evaluators. https://arxiv.org/abs/2305.17926 (b21)
- [V] Zheng et al. (2023) Judging LLM-as-a-judge. https://arxiv.org/abs/2306.05685 (b22)
- [V] Koo et al. (2024) COBBLER. https://arxiv.org/abs/2309.17012 (b23, c23)
- [V] Zhao et al. (2021) Calibrate before use. https://arxiv.org/abs/2102.09690 (b24)
- [V] Wei et al. (2024) Synthetic data reduces sycophancy. https://arxiv.org/abs/2308.03958 (b25)
- [V] Huang et al. (2026) CogBias. https://arxiv.org/abs/2604.01366 (c08-c10; per-bias table partly garbled)
- [V] Knipper et al. (2025) The bias is in the details. https://arxiv.org/abs/2509.22856 (c11, c12)
- [V] Huang et al. (2026) SynAnchors. https://arxiv.org/abs/2505.15392 (c15, c16, d08; the critique could not re-open the table; model totals beyond the two lowest are not quoted)
- [V] Itzhak, Belinkov, Stanovsky (2025) Planted in Pretraining, Swayed by Finetuning. https://arxiv.org/abs/2507.07186 (c19, d04)
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (c22)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (c24)
- [V] Weerasekara, Kamarthi, Isaacs (2026) Conditional cognitive biases. https://arxiv.org/abs/2608.05166 (c26, d17)
- [V] Investigating the impact of LLM personality on cognitive bias (2025). https://arxiv.org/abs/2502.14219 (c27)
- [M] Heuristics and biases in AI decision-making: implications for responsible AGI (2024). https://arxiv.org/abs/2410.02820 (c29; abstract and introduction only)
- [V] Sovrano, Dominici, Sevastjanova, Stramiglio, Bacchelli (2025) PROBE-SWE. https://arxiv.org/abs/2508.11278 (d05)
- [V] Sovrano, Dominici, Bacchelli (2026) Mitigating prompt-induced cognitive biases. https://arxiv.org/abs/2604.16756 (d06)
- [V] Rios et al. (2025) The Illusion of Rationality. https://arxiv.org/abs/2512.09254 (d07)
- [V] Takenami et al. (2025) Anchoring in price negotiation simulations. https://arxiv.org/abs/2508.21137 (d09)
- [V] Wang et al. (2025) Judging bias in large reasoning models. https://arxiv.org/abs/2504.09946 (d10)
- [V] Wang et al. (2026) Chain-of-Models. https://arxiv.org/abs/2607.28636 (d11)
- [V] Shi et al. (2025) Judging the Judges. https://arxiv.org/abs/2406.07791 (d12)
- [V] Ye et al. (2024) Justice or Prejudice (CALM). https://arxiv.org/abs/2410.02736 (d13; the Claude-3.5 bandwagon figure is 0.610, GPT-4o 0.791)
- [V] Kumar, Rathore, Moitra (2026) All verdicts are not equal. https://arxiv.org/abs/2610.12083 (d14)
- [V] Chae et al. (2026) Self- and other-labels in LLM judges. https://arxiv.org/abs/2608.18091 (d15)
- [V] Guey and Bougault (2026) Self-preference is weak in verifiable revision. https://arxiv.org/abs/2606.20093 (d16; abstract and introduction)
- [M] Zhuang et al. (2025) Reasoning dependency generation for choice-supportive bias. https://arxiv.org/abs/2512.03082 (d18; abstract and introduction)
- [M] Escalation of commitment in LLMs, "Getting out of the Big Muddy" (2025). https://arxiv.org/abs/2508.01545 (d19; abstract-level numbers)

Cross-subfield links (not covered here): Heuristics and biases; Worked-example research; Diagnosticity of evidence; Alternative-explanation controls; Reflective reasoning and second look; Generation versus evaluation; Outside view and base rates; Crowd within; Question wording and presupposition; Ecological rationality.
