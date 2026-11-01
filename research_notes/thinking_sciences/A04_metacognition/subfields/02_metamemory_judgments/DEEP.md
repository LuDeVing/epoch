# Metamemory judgments: deep document

*Subfield A04.02. Built from evidence_a-d.jsonl, claims.jsonl (K01-K42) and critique.md in this folder. Evidence ids (a01 ... d20) point to those files. Where a number was not checked in the source text, it is marked. Hart (1965) was never opened; do not cite Hart numbers.*

## 1. What it is

Metamemory is thinking about one's own memory. In this subfield it means four kinds of judgment, made at four moments.

| Judgment | When | Question the person answers | Criterion |
|---|---|---|---|
| Ease of learning (EOL) | Before study | Will this item be easy to learn? | Later recall |
| Judgment of learning (JOL) | During or just after study | Will I recall this later? | Later recall |
| Feeling of knowing (FOK) | After a recall failure, or before retrieval | Would I recognise the answer if I saw it? Do I know it? | Later recognition or recall |
| Knowing that you do not know | Before answering | Is this question answerable by me at all? | Whether an answer exists in memory |

Two measures matter.

- **Relative accuracy (resolution).** Do high ratings go with items that are later remembered? Usually scored with Goodman-Kruskal gamma. Gamma has known flaws (Spellman et al. 2008, snippet only, b10; Broder and Undorf 2019 as cited in a11): a person with perfect insight does not reach gamma 1, and gamma mixes skill with noise.
- **Absolute accuracy (calibration).** Does a rating of 70 mean 70% right? For LLMs this is ECE (expected calibration error). The LLM literature adds AUROC (can the rating separate right from wrong), which is the resolution measure.

Why it matters to our agent. The schema has an S0 gate: look up the problem class, estimate how hard it will be, and choose the mode (direct, short reason, step-by-step, checked, open). S0 is an ease-of-learning judgment made by a machine before it tries. G12 says to spend budget by difficulty. G6 says never abstain on the first pass. This subfield tells us how good such a pre-attempt judgment can be, what feeds it, what corrupts it, and whether a short attempt first (the delayed-JOL analogue) beats a prompt-only guess.

The short answer from the evidence: a pre-attempt guess from the question text alone is the weakest judgment in humans (d02). In LLMs it is weaker than a judgment made after a draft (d15, d11), but it is cheap and can be trained from the agent's own history (d13, d14). In humans a base rate by item beat the person's own feeling (d03).

## 2. History and theories in depth

### 2.1 Founding: Hart and the feeling of knowing

Hart (1965) is the founding FOK study (a01, b27). Procedure, as summarised in secondary sources only: people fail to recall an answer, rate whether they would recognise it, then take a recognition test. The feelings predicted recognition above chance, so a failed recall still leaves usable information. The 1965 paper was not opened and no numbers are available. The critique also found no Hart-era replication (Nelson and Narens 1980, Gruneberg and Monks, Schacter) and no pooled FOK-accuracy meta-analysis for young adults (b28, K34). The only meta-analysis found is about age differences (d10).

### 2.2 Nelson and Narens: monitoring and control

Nelson and Narens (1990, a02, secondary summary) give the frame. An object level does the cognition. A meta level holds a model of it. Information flows up (monitoring: EOL, JOL, FOK, confidence) and down (control: allocate study time, choose strategy, stop search). The frame covers acquisition, retention and retrieval. It gives vocabulary, not quantitative predictions. It is the direct template for S0: a monitor signal feeds a control choice.

Control evidence in humans (d04, abstract only): EOL and FOK are reliably linked to self-paced study time; more time goes to harder items. But large extra time sometimes gave little or no recall gain (Nelson and Leonesio 1988, "labor in vain"). So a hard flag should come with a spending cap, not just more spending.

### 2.3 Where the feeling comes from: the accounts

1. **Direct access.** The monitor reads the stored trace. The evidence below weakens this.
2. **Cue familiarity** (Reder and Ritter 1992, a03; Schwartz and Metcalfe 1992, d07). The feeling comes from how familiar the question terms are, before any retrieval. Schwartz and Metcalfe, four experiments (abstract only): priming the cue raised FOK; a manipulation that raised actual recall did not. Target priming helped in only one of the later experiments (Exp 3).
3. **Accessibility** (Koriat 1993, d06; a04). The feeling comes from how much related information comes to mind, right or wrong, from the same retrieval attempt used to find the target. Three experiments argue against a privileged monitor.
4. **Interactive view** (Koriat and Levy 2001, a04). Familiarity is used first and fast. Accessibility is added when familiarity is not enough.

Koriat's later work generalises this into the **Self-Consistency Model** (a05, b11, b12): any judgment (confidence, FOK, JOL) reflects how consistent the cues are that are sampled from a shared pool for that item. A consequence: judgments agree across people, because people share the pool ("consensuality").

### 2.4 Delayed JOLs and the retrieval-attempt account

Nelson and Dunlosky (1991, b08, snippet only) found that JOLs made after a delay, with the cue alone, predict later recall almost perfectly, while immediate JOLs do not. Explanations tested:

- **Memory-trace account (retrieval attempt).** At delay, the person tries to retrieve and rates the result. Kimball and Metcalfe (2003, b01-b03) support this.
- **Scale-use account.** Weaver and Kelemen (1997, b09, snippet only): delayed JOLs use the scale ends more; simulations suggested most of the effect stayed real.
- **Reactivity.** Making the JOL itself changes memory (section 5).

### 2.5 Surface cues: heuristic-based judgments

Judgments also run on cheap cues that do not help memory. Font size raises JOLs without raising recall (a10, d08). Scene pictures are rated using intrinsic cues (peacefulness, people present) and extrinsic cues (presentation frequency, distinctiveness) (a11). When the answer is visible at study, learners overrate pairs with a strong pair link but a weak cue-alone link (Koriat and Bjork 2005, d05). Repetition raises recall but barely raises JOLs (Kornell et al. 2011, d08).

### 2.6 The machine line

- **Kadavath et al. (2022)** make the human distinction explicit for LMs: P(True) (a retrospective check of a sample) and P(IK) (a pre-answer "I know" value head), the machine versions of confidence and FOK/EOL (a14, c03).
- **Calibration by words** (Lin et al. 2022; Tian et al. 2023; Xiong et al. 2024).
- **Unknown-detection** (Yin et al. 2023; Cheng et al. 2024; Zhang et al. 2024 R-Tuning).
- **Internal-state readouts** (Azaria and Mitchell; Ferrando et al.; Orgad et al.; Zhang et al. 2025).
- **Self-knowledge** (Binder et al. 2024; Ji-An et al. 2025).
- **Pre-answer routing** (Mallen et al. 2023; Jeong et al. 2024 Adaptive-RAG; AdaptThink).

## 3. Core findings with exact numbers

Status key: established (two or more independent sources agree), single-source, contested. "N" is sample size.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| FOK after recall failure predicts later recognition above chance | No numbers; Hart not opened | Hart 1965 (a01, b27) | single-source, secondary only |
| FOK driven by cue familiarity, not target retrievability | 4 experiments; priming cues raised FOK, recall boost did not; no effect sizes | Schwartz and Metcalfe 1992 (d07); Reder and Ritter (a03) | established (abstract level) |
| FOK driven by accessibility of partial information | 3 experiments; no numbers | Koriat 1993 (d06) | single-source |
| Consensual answers get stronger FOK | 91.2 vs 85.1, t(35)=8.91, N=36, 90 items | Koriat 2026 (b11) | single-source (one lab) |
| Consensual answers get stronger JOL | 78.67 vs 62.99, t(23)=9.27, N=24, 58 items | Koriat 2026 (b11) | single-source |
| Same in children | 73.22 vs 60.87, t(71)=8.24, N=72 usable of 100, grades 1-6; majority size 74.3% | Koriat 2026 (a05) | single-source |
| FOK higher than JOL; consensuality slope steeper for JOL | means 89.8 vs 74.7; slopes 6.06 (JOL) vs 3.48 (FOK) | Koriat 2026 (b12) | single-source |
| Confidence tracks accuracy with no knowledge (guessing word meanings across unknown languages) | correct matching 53% at rating 1 to 66% at rating 4 | Koriat 1975/76 as reported (a06) | single-source |
| Delayed cue-only JOL beats immediate JOL | gamma .76 vs .36 (Exp 3, N=40, F(1,35)=24.29); .72 vs .43 (Exp 2, N=72) | Kimball and Metcalfe 2003 (b01) | established |
| Advantage vanishes when targets are re-shown | .53 vs .43 n.s. (Exp 3); .39 vs .46 n.s. (Exp 2); Exp 1 N=36 .52 vs .41, t(34)=1.16, p>.25 | Kimball and Metcalfe 2003 (b01, b02) | established |
| Part of high delayed gamma is selection: low-JOL unretrieved, unre-shown items recalled worst | JOL format x level x re-exposure F(1,64)=10.60, p=.0018 | Kimball and Metcalfe 2003 (b03) | single-source |
| Delayed-JOL effect robust only if cue alone is the judgment cue | 45 of 45 subjects with stimulus-alone cue; small or none with whole pair | Dunlosky and Nelson 1992 (d09) | single-source (abstract) |
| Delayed JOL: large relative-accuracy gain, tiny memory gain | accuracy g=0.93 (4,554 participants, 112 effects); memory g=0.08 (3,807, 98 effects) | Rhodes and Tauber 2011 (d01) | established |
| The g=.70 (cue-target) and g=.03 (cue-only) values | quoted second-hand as recall outcomes; not in abstract | Tekin and Roediger 2021 (a07, a08, b07) | unverified; do not use |
| Delayed-JOL advantage does not carry to text | N=96 (4 x 24); F(3,92)=3.34; only immediate-predict/immediate-test gamma above zero; post-test confidence accurate in all conditions | Maki 1998 (b04, b05) | single-source |
| Delayed JOLs better when study technique makes target retrievable at JOL time | 2 experiments; 38 of 99 had a missing gamma for one item type | Hughes and Thomas 2022 (a09) | single-source |
| Font size raises JOLs without helping memory; moderated by word frequency | 70 pt vs 9 pt; beliefs mediate for low-frequency words only | Tian et al. 2021 (a10) | established with d08 |
| Making JOLs changes later recall (reactivity) | Exp 1 N=164: restudy .44, cue-target JOL .45, cue-only JOL .50, overt retrieval .52; Exp 2a N=53 d=.63; direct replication 2b N=41 diff .02, d=.11, p=.90 | Tekin and Roediger 2021 (b06) | contested |
| Reactivity depends on item type | related pairs up d=0.43/0.38; unrelated pairs down d=0.80/0.41 (N=193, N=200); imagery instruction raises unrelated recall d=1.15 / 0.54 | Ingendahl and Undorf 2026 (b14) | single-source, preregistered |
| JOLs do not change restudy choices | BF10=0.46 and 0.22; N=140, 202; negative reactivity b=-0.64 | Ingendahl and Undorf 2026 (b15) | single-source |
| Human EOL is the weakest judgment | no gamma in abstract | Leonesio and Nelson 1990 (d02) | single-source |
| Base-rate item difficulty beats own FOK, which beats normative FOK | no numbers | Nelson et al. 1986 (d03) | single-source |
| After recall failure, TOT or high FOK raises sensitivity of later recognition confidence | Exp 1 N=70 analysed, TOT 3.08 vs 1.48; Exp 2 N=47, 2.90 vs 1.76; no meta-d' values | Pournaghdali et al. 2025 (a13, b13) | single-source |
| Age effect on FOK | episodic g=0.53 [0.28, 0.78]; semantic g=-0.10 [-0.29, 0.10]; 20 studies, 922 young, 966 old; I2 79.09%; publication bias z=2.99 | 2023 meta-analysis (d10) | single-source |
| LLM: large models calibrated on lettered multiple choice and true/false | up to 52B; improves with size and few-shot | Kadavath 2022 (a14, b16) | single-source |
| LLM: P(IK) from bare question | TriviaQA-trained: LAMBADA .864, Python .928; all-task: .987 / .853 (Brier .151/.194 and .042/.108) | Kadavath 2022 (d16) | single-source |
| LLM: own vs other model P(IK) | .8633 (A on A) vs .8631 (B on A data): no self-advantage here | Kadavath 2022 Table 3 (d16) | single-source |
| LLM: verbalised confidence near chance on failure prediction | GPT-4 mean AUROC 62.7%; GPT-3/3.5/Vicuna mean ECE above 0.377 | Xiong et al. 2024 (a21, c09) | established |
| LLM: sample agreement beats single verbal confidence | GSM8K AUROC 54.8% to 92.7% (5 samples) | Xiong 2024 (c10) | established |
| LLM: trivial calibration trap | GPT-4 says 100% for all; ECE 0.064 at 93.6% accuracy | Xiong 2024 (c10) | established |
| LLM: verbal probability beats token probability for RLHF models | gpt-3.5 TriviaQA ECE .140 to .050, AUC .869 to .894; SciQ top-4 ECE .256 to .065; GPT-4 ECE .078 to .024 | Tian 2023 (a18, b21, b22) | contested (ECE yes, AUROC no) |
| LLM: adversarial data stays hard | TruthfulQA AUC .418 (label prob), .485 (verbal top-2), GPT-4 .622 | Tian 2023 | contested |
| LLM: fine-tune on about 1,000 graded examples | LoRA+Prompt AUROC 80.0 / 85.1 / 70.2 vs zero-shot 56.9 / 66.2 / 47.1 (coding shift; LLaMA-2-7B, Mistral-7B, Mistral-7B-Instruct); ECE worse for two of three | Kapoor 2024 (d13) | established |
| LLM: recognising unanswerable questions | 1,032 unanswerable + 2,337 answerable; GPT-4 F1 75.47 vs human 84.93; davinci +27.96% from in-context examples | Yin 2023 (a19, c07, c08) | single-source |
| LLM: known/unknown alignment | Idk set 45.05% known; Idk-SFT 74.75% truthful vs prompting 66.93%; alignment tax | Cheng 2024 (c17) | established |
| LLM: popularity predicts knowing | PopQA 14k; davinci-003 35% (15-shot); adaptive retrieval 46.5%, +5.3% over best non-adaptive | Mallen 2023 (c22) | established |
| LLM: hidden-state probe, early exit | at most 1,000 training examples; AUC above .7 in-distribution, above .9 for R1-Distill-32B on AIME; 24% token saving, 88.2 vs 88.6 accuracy | Zhang 2025 (d14) | established |
| Probe transfer | math to math AUC .76-.83; math to logic .56-.63; logic to math .74-.77 with ECE .17-.19; AIME ECE .25-.31 | Zhang 2025 (d14) | established |
| Probe location | exact-answer token AUC .83-.95 vs end-of-question .72-.80 (Mistral-7B-Inst: TriviaQA .85 vs .76, Winobias .92 vs .82, Math .92 vs .72) | Orgad 2025 (d15) | single-source |
| Reasoning models verbalise confidence better | better in 33 of 36 settings; six open 32B-class models | Yoon 2025 (d11) | contested |
| Reasoning models overconfident | often above 85% confidence on wrong answers; worse with deeper reasoning | Mei 2025 (d12) | contested |
| Pairwise relative confidence | +3.5% AUC over absolute, +1.7% over self-consistency; 5 frontier models, 14 tasks | Shrivastava 2025 (d19) | single-source |
| Difficulty linearly decodable | AMC human-difficulty rho about .88, 60 models; failure-based difficulty weaker, degrades under RL | Lugoloobi and Russell 2025 (d18) | single-source |
| Pre-answer think/no-think policy | length down 53%, accuracy up 2.4% (1.5B model, math) | AdaptThink (d20) | single-source |
| Learned complexity router | oracle 45.00 vs learned 37.17 F1 (one column) | Adaptive-RAG (c23) | single-source |
| Naming the skill first | +11.6% over CoT on MATH (3.5% over an ambiguously named baseline) | Didolkar 2024 (c27) | single-source |
| Certainty words in prompt shift accuracy | over 80% variation across 50 markers; high-certainty 7% lower | Zhou 2023 (c26); Yona 2024 (c25) | established |
| Self-prediction beats cross-prediction | 49.6 vs 36.2 and 48.5 vs 35.2 (plateaus); GPT-3.5 +0.8% (p=.002) | Binder 2024 (a24, d17) | contested |
| Humans over-trust LLM answers | human AUC .589/.602/.592 vs model .751/.746/.781; 301 participants (284 retained) | Steyvers 2025 (a22, c12) | established |
| LLM JOLs do not predict human memory | human B=.167 [.018, .316], N=78; GPT-4o B=.045 (CI includes zero); all LLM CIs include zero | Huff and Ulakci 2025 (b25) | single-source |

## 4. Mechanisms and models

Each is written so an engineer can build it.

### 4.1 Two-level monitor and controller (Nelson and Narens)

- Object level: the solve loop (S1 to S8).
- Meta level: a small state record per problem: class label, pre-attempt rating, draft rating, tokens spent, outcome.
- Monitor: functions that read the object level and write a number.
- Controller: code (not the model, per schema section 1) that maps the number to a mode and a token cap.
- Rule from the labor-in-vain result: every "hard" flag gets a cap, and gain per token is logged so the cap can be tuned.

### 4.2 Three monitor signals, by cost

1. **Class base rate (cheapest).** A table of pass rate by task class from the agent's own history. Human analogue: base-rate item difficulty beat own FOK (d03). Update after every run. Needs no model call.
2. **Question-only rating (cue familiarity analogue).** One short call or a probe: "Will you get this right? Give 0-100" or a trained P(IK) value head. Fast, fooled by familiar-looking terms and surface features (K03, K11). Entity rarity is a cheap proxy feature (popularity, c22).
3. **Draft-then-rate (delayed-JOL analogue).** Make a short unaided attempt, then rate or compare samples. The human result says the retrieval attempt is the source of accuracy (K06, K07). The LLM analogues: probes at the answer token beat probes at question end (d15), and agreement over 5 samples took GSM8K failure-prediction AUROC from 54.8 to 92.7 (c10).

### 4.3 Consistency as confidence (Koriat's model, implemented)

1. Sample k answers (k=5 in Xiong) at nonzero temperature.
2. Cluster by meaning (semantic entropy, a20) or by exact match for short exact answers.
3. Confidence = size of the largest cluster / k.
4. Code does the clustering and the count (guardrail G5). The model never rates its own answer.

Caveat from G4: samples from one model are correlated, so agreement is a hint, not proof. Koriat's consensual answers are right more often only because the shared pool is mostly right. If the pool is wrong (a common misconception), consistency is high and the answer is wrong. This is a core failure of this cue.

### 4.4 Trained gate (P(IK) and probes)

- Label past runs correct or incorrect (about 1,000 are enough with LoRA, d13; probes on at most 1,000, d14).
- Features: question text only (P(IK)), or a hidden state at the answer token.
- Output: P(correct). Threshold set per task class, reset when the class changes (K37).
- Probes need white-box access. For an API-only agent, the substitute is a small classifier on cheap features (class, length, entity rarity, ratings) trained on logged outcomes. This is a design inference, not a tested result.

### 4.5 Pairwise comparison

Show the model two tasks and ask which it is more likely to solve; aggregate with Elo or Bradley-Terry in code (d19). Use to rank a new task against a bank of past tasks with known outcomes. Costs more calls.

### 4.6 Ease-of-processing correction

Surface cues (font, length, polish) change ratings but not outcomes. Implementation: strip formatting, rate the restated task (S1) rather than the raw prompt, and rate before any worked solution is visible (K33).

### 4.7 Calibration layer

Isotonic or Platt scaling fitted on logged (rating, outcome) pairs. It guards against the trivial-calibration trap (always say 100%): report AUROC and the rating distribution, not ECE alone (c10).

## 5. What holds up

### 5.1 Replications and meta-analyses

- **Delayed-JOL accuracy gain: replicated and meta-analysed.** g=0.93 over 112 effect sizes (d01). Reproduced in Kimball and Metcalfe's experiments (b01).
- **Mechanism qualified.** The gain depends on the retrieval attempt and on the cue being the stimulus alone. Re-showing the target removes it (b01, b02). Part is selection of recall outcomes (b03).
- **Memory effect of delaying: tiny.** g=0.08 (d01).
- **Cue-familiarity effect on FOK:** four experiments (d07) plus the Reder and Ritter line. No effect sizes obtained.
- **Surface-cue effects:** font size (a10), type size and repetition (d08), picture cues (a11). Several labs.

### 5.2 Failed or weak results

- **Text materials.** No delayed advantage (Maki 1998, b04). Pre-test predictions were not above zero in most conditions, while post-test confidence was accurate everywhere (b05). The gate fails where the thing judged is long. LLM analogue: Binder found self-prediction failed on long outputs (d17).
- **Reactivity.** Present in one within-subject experiment (Exp 2a, d=.63), absent in the direct online replication (Exp 2b, d=.11, p=.90). Later work says the sign depends on item type (b14).
- **Ease of learning.** Weakest human judgment (d02). Own FOK loses to base rates (d03).
- **Labor in vain.** More study time after a hard flag gave little recall gain (d04).
- **Human FOK accuracy.** No pooled number found. The only meta-analysis is on age (d10) and shows publication bias for episodic FOK. Do not quote a human FOK gamma.
- **Hart replications.** None retrieved.

### 5.3 Moderators

- Item relatedness (related vs unrelated pairs reverse the sign of JOL reactivity).
- Cue format (stimulus alone vs pair).
- Material (word pairs vs text).
- Word frequency (moderates font-size effect).
- Age (episodic FOK worse in old age; semantic FOK not).
- Measure choice (gamma vs Brunswik G, a11).

### 5.4 Interventions that worked and did not

| Intervention | Worked? | Evidence |
|---|---|---|
| Delay the JOL and use cue alone | Yes, for word pairs | d01, b01 |
| Re-show the target before rating | No, removes the gain | b01 |
| Instruct imagery or strategy use on unrelated pairs | Yes, removes negative reactivity | b14 |
| Study technique that makes the target retrievable at JOL time | Yes, raises delayed-JOL accuracy | a09 |
| Show the user calibrated hedges (match explanation tone to model confidence) | Yes, narrows both gaps | a22 |
| Human-inspired prompts for LLM confidence | Reduced ECE, AUROC near chance | c10 |
| Multi-sample consistency | Yes, large | c10 |
| Fine-tune on about 1,000 graded examples | Yes | d13 |
| Extra study time on items judged hard | Little or no recall gain | d04 |

## 6. Language models

### 6.1 Verbalised confidence

- **Discrimination is weak.** GPT-4 mean AUROC 62.7% across eight tasks (Xiong). GPT-3, GPT-3.5 and Vicuna mean ECE above 0.377. Verbal values bunch at 80-100%.
- **Calibration can look good by accident.** GPT-4 got ECE 0.064 at 93.6% GSM8K accuracy by saying 100% for everything.
- **RLHF models do better when asked in words than from token probabilities** (Tian): gpt-3.5 TriviaQA ECE .140 to .050, AUC .869 to .894; GPT-4 ECE .078 to .024. On adversarial TruthfulQA, AUC stays .42-.62.
- **Reconciling Tian and Xiong.** Tian reports mostly ECE on factual sets where AUC was already good. Xiong averages over harder tasks including arithmetic and reports AUROC. Calibration improves, discrimination stays modest. This is our reading, not a tested explanation. Contested (K17).
- **Prompted ECE does not improve as base models get better** (Kapoor), while fine-tuning does.
- **Certainty words are not knowledge.** Putting "I'm sure" in the prompt shifts accuracy by over 80% across markers, and high-certainty ones lower it 7% (Zhou). Models do not hedge faithfully (Yona, c25).

### 6.2 What changed it

| Change | Effect | Source |
|---|---|---|
| 5 samples with consistency | AUROC 54.8 to 92.7 (GSM8K) | c10 |
| Asking top-k guesses first | ECE often cut by over 50% | Tian, c11 |
| Scale 800M to 52B | calibration and AUROC rise; P(IK) AUROC rises | Kadavath |
| Few-shot comparison samples | improve Brier, mostly calibration not discrimination | c02 |
| Fine-tune on about 1,000 graded examples | coding-shift AUROC 56.9 to 80.0 (LLaMA-2-7B) | d13 |
| Reasoning models | better in 33 of 36 settings (Yoon); overconfident above 85% on wrong answers (Mei) | d11, d12 |
| Alignment with Idk data | truthful 74.75 vs 66.93, with an alignment tax | c17 |
| Context or correct hint | P(IK) rises | Kadavath, a15 |
| Temperature fix on RLHF policy | repairs token-probability miscalibration | c05 |

### 6.3 Pre-answer knowing (FOK and EOL analogues)

- P(IK) works from the bare question and transfers partly (K13). Out of distribution it ranks but is miscalibrated.
- Self-access to P(IK) is small: models predicted their own P(IK) somewhat better than another model's (a15), but Table 3 gives .8633 vs .8631 (d16).
- Kapoor: Mistral-7B features beat LLaMA-2's own on LLaMA-2 data. Binder: self 48.5% vs cross plateau 35.2%, but absent for some properties and for GPT-3.5 (+0.8%). Privileged access is weak and task dependent (K29, contested).
- Difficulty is decodable from hidden states (rho about .88 on human-labelled AMC) but the failure-based version is weaker (d18).
- Entity-recognition latents are causal: steering gives almost 100% refusal (Gemma 2 2B). The unknown-entity latent fires 53% / 55% / 76% on post-cutoff songs (c19). Needs white-box access.

### 6.4 Placing the judgment: before, or after a draft

- Probes at the end of the question: AUC .72-.80. At the exact answer token: .83-.95 (d15).
- Reasoning-model confidence improves along the chain of thought (Yoon, d11). Counter-evidence: deeper reasoning more overconfident (Mei, d12).
- A trained pre-answer policy still works for efficiency: AdaptThink cut length 53% with accuracy +2.4% on a 1.5B model (d20).
- No head-to-head "gate vs short draft at equal tokens" for frontier models was found (K38). This is the main open item.

### 6.5 Do LLMs have human-like JOLs?

No evidence. LLM JOLs did not predict human recognition of garden-path sentences; all slope CIs include zero (Huff and Ulakci, b25). Different target (human memory), so not a conflict with Binder. Do not assume the model's difficulty ratings mirror human difficulty.

### 6.6 Humans reading LLM confidence

Human AUC on default explanations .589/.602/.592 vs model confidence AUC .751/.746/.781. Longer explanations raise confidence without raising accuracy (Steyvers). Relevant for any user-facing output.

### 6.7 Evidence limits

Most LLM work is 2022-2024 models. No 2025-2026 frontier AUROC above 62.7 was confirmed. No test of reactivity (does adding a self-rating step change accuracy). No test of fluency inflating LLM self-ratings. Several tables were garbled by extraction (Yoon, Kadavath Table 1).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Never use the model's verbalised confidence as a decision signal on its own. Mean AUROC 62.7 is near chance; ECE can be gamed by saying 100%. Report AUROC, not ECE alone. | G (new guardrail) | [E] | K16: a21, b20, c09, c25 |
| A2 | When a confidence signal is needed, use agreement over k samples counted by code (k=5 gave AUROC 92.7 vs 54.8 on GSM8K). Consistent with G4/G5; state it as the confidence rule, with the G4 caveat that agreement is a hint. | G/O | [E] | K15: a16, c02, c10, a21 |
| A3 | Do not put certainty words ("I'm sure", "definitely") in scaffold prompts. | G | [E] | K26: c26, c25 |
| A4 | Rate or classify before a worked solution is visible, and rate the restated task, not the raw prompt, because surface features move ratings and not outcomes. | S0/S1 | [E] | K11: a10, a11, d08 |
| A5 | S0 should use cheap features known to track knowing: entity rarity or popularity (E), and class pass rate from the agent's own log (S, human data). | S0 | [E] rarity / [S] base rate | K23, K31: c22, c18, d03 |
| A6 | Keep a per-class log of outcomes (the memory part) and fit a small calibration layer on about 1,000 graded runs. Reset thresholds per class, because ranking transfers within a family but calibration does not across skills. | memory/S0 | [E] | K18, K37: d13, d14, d15 |
| A7 | A hard flag must carry a token cap. Extra effort on hard items often returns little (labor in vain) and G11 already says to think briefly. Log gain per token to tune the cap. | S0/O | [S] in humans; consistent with G11/G12 | K32: d04 |
| A8 | Include unanswerable or underspecified items in the S0 classes and route them to "state the gap", while keeping G6 (never abstain on the first pass; submit the best attempt). | S0/G6 | [S] | K19, K20: a19, c17 |
| A9 | Treat human-facing confidence displays as a separate channel: show calibrated hedges, not default fluent text. | G | [E] | K27: a22, c12 |

Items A5 (base rate half), A7 and A8 are single-source in the evidence; they are listed here because they are low-cost and consistent with existing guardrails, but they should be checked by U2 and U11 in UNKNOWNS.md before they become schema text.

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | A short unaided draft, then rate (delayed-JOL analogue), beats a prompt-only pre-attempt gate at predicting failure at equal tokens. | S0 | [C] no direct test | K06, K07, K38: d01, b01, d15, d11 |
| T2 | Class base rate beats the model's own ease rating at routing. | S0 | [S] human data | K30, K31: d02, d03 |
| T3 | Trained P(IK)-style gate on the agent's own history, evaluated on a held-out task class. | S0 | [S] | K13, K37 |
| T4 | Pairwise "which task will I solve" against a bank of past outcomes. | S0 | [S] | K41: d19 |
| T5 | Adding a self-rating step changes accuracy (reactivity analogue). Sign unknown. | G | [C] human only | K10: b06, b14 |
| T6 | Rating after seeing a polished solution inflates self-ratings (fluency illusion). | G | [S] human only | K33: d05, d08 |
| T7 | Verbalised-confidence AUROC at several reasoning budgets. | G | [C] | K36: d11, d12 |
| T8 | Gate accuracy by output-length bucket (does it fail on long multi-step tasks, as Maki found for text?). | S0 | [S] indirect | K39: d17, b04 |
| T9 | Separate small judge model vs the main model's own estimate at equal cost. | S0 | [C] | K29: d13, d16, d17 |
| T10 | Naming the problem type before solving (typed retrieval). | S0/O | [S] | K25: c27 |
| T11 | Trained think/no-think policy or prompted equivalent at equal tokens. | S0 | [S] small model, math only | K42: d20 |
| T12 | Semantic clustering vs exact match in the sample vote. | O | [S] | K21: a20 |

## 8. Concrete tests on our bench

Rules for all: both arms get the same total token budget, setup cost counted (G7). Items are held out from any fitting. Report AUROC for the gate and final accuracy. Use at least 200 items per class to see an AUROC difference of about 0.05 (our estimate; check with a bootstrap).

| Test | Item type | Arms (equal total tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 gate vs draft | mixed BRAINTEASER and ARC-like items with known answers | A: prompt-only difficulty rating, then spend remainder on solving. B: 200-token draft, rate from draft, then spend remainder. | AUROC of rating vs final correctness; final accuracy | B higher AUROC by 0.05-0.15; accuracy gain only if routing changes modes |
| T2 base rate vs ease rating | tasks grouped by class | A: model ease rating. B: class pass rate from log. C: both | AUROC; routing accuracy | B at least equal to A (human data say base rate wins) |
| T3 trained gate | 1,000 logged runs; hold out one class entirely | A: zero-shot rating. B: logistic gate on class, length, rarity, rating | AUROC on held-out class; ECE before and after threshold reset | B AUROC .70+ in-class, lower on held-out class; ECE bad until reset |
| T4 pairwise | 100 new tasks vs 50 banked tasks | A: absolute rating. B: pairwise Elo vs bank | selective-classification AUC | B +0.02-0.04 AUC at higher call cost; check equal tokens |
| T5 reactivity | same items | A: solve. B: solve then rate. C: rate then solve | accuracy | unknown; direction may depend on item type; use two item types |
| T6 fluency | same problems with and without a visible worked solution or polished rewrite | A: plain. B: polished or solved version shown before rating | mean rating and AUROC | B rating higher with AUROC lower |
| T7 reasoning budget | one item set | confidence read at 0, 1k, 4k thinking tokens | AUROC per budget | either rises (Yoon) or stays flat/overconfident (Mei); settles K36 |
| T8 length buckets | items bucketed by expected answer length | gate AUROC per bucket | AUROC gap | short bucket higher; tests the Maki analogue |
| T9 judge | same runs | A: main model self-rating. B: small cheaper judge, equal token cost | AUROC | roughly equal (Kadavath, Kapoor) |
| T10 typed prompt | MATH-like items | A: plain CoT. B: name skill, then CoT, same tokens | accuracy | small gain, if any |
| T11 think/no-think | easy and hard mix | A: always think. B: gate then think or not | accuracy, tokens | tokens down, accuracy flat or up on easy items |
| Entity rarity feature | factual items with entities of varied popularity | A: gate without rarity. B: with rarity | AUROC | B higher on factual items only |

## 9. What does not transfer, and why

- **Human FOK accuracy figures.** None established; do not import any.
- **Delayed-JOL gamma values** (.72-.76 vs .36). They come from word pairs with a cue-only format and no re-exposure. Our items are long and multi-step, and the "cue" is a whole problem. Maki's text result shows no delayed advantage.
- **Reactivity effect sizes.** Different mechanism (a learner's dual-task cost and strategy choice). An LLM has no study phase. Only the qualitative question (does the rating step change the task?) transfers.
- **Consensuality.** Koriat's majority-size effect rests on a shared human knowledge pool. For one LLM, samples are correlated (G4). The consistency signal transfers; the idea that consensus equals accuracy does not.
- **Cue familiarity and accessibility, taken as mechanisms.** In LLMs the evidence is only that popularity and context change P(IK). It is analogy, not proof of the same mechanism.
- **Human scale-use, gamma and TOT states.** No LLM counterpart tested.
- **Probe results (SAEs, hidden-state probes).** Need white-box access. Not usable on an API-only agent.
- **Alignment and fine-tuning remedies (Idk-SFT, R-Tuning, LoRA calibration).** We do not train. Only the data idea (log known/unknown outcomes) transfers.
- **Abstaining.** Idk-style refusal conflicts with G6 on the first pass.
- **Kadavath's P(IK) numbers** were on 52B models in 2022. Do not assume they hold for current models.
- **LLM judgments as proxies for human difficulty** (b25).

## 10. Open questions

1. Gate vs short draft at equal tokens, for current frontier models (not found anywhere).
2. Original Rhodes and Tauber values for the cue-target (g=.70) and cue-only (g=.03) subgroups.
3. Human FOK accuracy in meta-analysis (Hart, Nelson and Narens 1980, Gruneberg and Monks) and the size of the cue-familiarity effect.
4. Human EOL accuracy (Underwood 1966; Leonesio and Nelson numbers), and whether a prompted easy/hard rating predicts failure beyond prompt length and surface cues.
5. Size of the fluency illusion in humans (Koriat and Bjork; Kornell) and whether it exists in LLMs.
6. 2025-2026 reasoning-model verbalised-confidence AUROC, and the effect of reasoning budget (Yoon vs Mei).
7. Reactivity of self-rating in LLMs.
8. Transfer of a gate trained on about 1,000 own runs to new task classes.
9. Equal-cost small judge vs self-estimate.
10. Whether the gate fails on long multi-step tasks, tested directly.
11. Whether the Binder self-advantage is real and large enough to justify self-rating over an external judge.
12. Whether Koriat's consensuality results replicate outside his lab.
13. Several "opened" LLM sources were read only to abstract or intro level (critique): Ji-An, Yamato, Lin tables, Semantic Entropy AUROC; Yoon and Kadavath tables were garbled by extraction.
14. Hart (1965) itself has not been read.

## 11. Sources

[V] = full text or substantial text opened. [M] = abstract, snippet or secondary summary only. (Per the critique, some [V] items were read only to about 100,000 characters.)

**Human metamemory**
- [M] Hart (1965) Memory and the feeling-of-knowing experience. Seen only via https://en.wikipedia.org/wiki/Metamemory
- [M] Nelson and Narens (1990) Metamemory: a theoretical framework and new findings. https://en.wikipedia.org/wiki/Metamemory
- [M] Reder and Ritter (1992) What determines initial feeling of knowing? https://en.wikipedia.org/wiki/Metamemory
- [M] Koriat (1993) How do we know that we know? https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:8255951
- [M] Koriat and Levy (2001) interactive hypothesis, via secondary summary. https://en.wikipedia.org/wiki/Metamemory
- [M] Schwartz and Metcalfe (1992) Cue familiarity but not target retrievability enhances FOK. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=cue+familiarity+feeling-of-knowing
- [V] Koriat (2026) Confidence judgments, feelings of knowing and judgments of learning. https://europepmc.org/article/PMC/PMC13461756
- [M] Koriat (1975/1976) phonetic symbolism, as reported in Koriat 2026. https://europepmc.org/article/PMC/PMC13461756
- [M] Nelson and Dunlosky (1991) delayed-JOL effect (snippet). https://link.springer.com/content/pdf/10.3758/BF03196445.pdf
- [V] Kimball and Metcalfe (2003) Delaying judgments of learning affects memory, not metamemory. https://link.springer.com/content/pdf/10.3758/BF03196445.pdf
- [M] Weaver and Kelemen (1997) Judgments of learning at delays (snippet). https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.1997.tb00445.x/
- [M] Spellman, Bloomfield and Bjork (2008) gamma (snippet; download failed). https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/07/Spellman_Bloomfield_RBjork_2008.pdf
- [V] Maki (1998) Predicting performance on text: delayed versus immediate predictions. https://link.springer.com/content/pdf/10.3758/BF03201176.pdf
- [M] Dunlosky and Nelson (1992) Importance of the kind of cue for JOLs. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=delayed-JOL+effect+kind+of+cue
- [M] Rhodes and Tauber (2011) meta-analysis. https://pubmed.ncbi.nlm.nih.gov/21219059/ (abstract; subgroup values second-hand via Tekin and Roediger)
- [V] Tekin and Roediger (2021) effect of delayed JOLs on retention. https://pmc.ncbi.nlm.nih.gov/articles/PMC7912969
- [V] Hughes and Thomas (2022) When memory and metamemory align. https://europepmc.org/article/PMC/PMC9680448
- [V] Tian et al. (2021) Font size effect on JOLs. https://europepmc.org/article/PMC/PMC8452059
- [V] Undorf and Broder (2021) Metamemory for pictures of naturalistic scenes. https://europepmc.org/article/PMC/PMC8476480
- [V] Ingendahl and Undorf (2026) Instructed strategy use eliminates negative reactivity. https://pmc.ncbi.nlm.nih.gov/articles/PMC12804242
- [V] Ingendahl and Undorf (2026) Are restudy decisions reactively altered by JOLs? https://pmc.ncbi.nlm.nih.gov/articles/PMC13690918
- [V] Pournaghdali, Schwartz and Soto (2025) TOT and FOK effects on metacognitive sensitivity. https://pmc.ncbi.nlm.nih.gov/articles/PMC12047626
- [M] Leonesio and Nelson (1990) Do different metamemory judgments tap the same underlying aspects of memory? https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=Leonesio+Nelson+1990
- [M] Nelson et al. (1986) Three predictors of an individual's memory performance. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=feeling+of+knowing+normative+base-rate
- [M] Nelson and Leonesio (1988) Allocation of self-paced study time and the labor-in-vain effect. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=labor-in-vain+effect
- [M] Koriat and Bjork (2005) Illusions of competence in monitoring one's knowledge. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15755238
- [M] Kornell, Rhodes, Castel and Tauber (2011) The ease-of-processing heuristic and the stability bias. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=ease-of-processing+heuristic
- [V] Episodic and semantic FOK in aging: systematic review and meta-analysis (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10542372/
- [M] Yamato and Suzuki (2022) Evolution of metamemory (evolved networks). https://europepmc.org/article/PMC/PMC9042878

**Language models**
- [V] Kadavath et al. (2022) Language Models (Mostly) Know What They Know. https://arxiv.org/abs/2207.05221
- [V] Lin, Hilton and Evans (2022) Teaching models to express their uncertainty in words. https://arxiv.org/abs/2205.14334 (tables garbled)
- [V] Tian et al. (2023) Just Ask for Calibration. https://arxiv.org/abs/2305.14975
- [V] Yin et al. (2023) Do LLMs know what they don't know? https://arxiv.org/abs/2305.18153
- [M] Kuhn, Gal and Farquhar (2023) Semantic uncertainty. https://arxiv.org/abs/2302.09664 (AUROC read from text)
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063
- [V] Steyvers et al. (2025) What LLMs know and what people think they know. https://arxiv.org/abs/2401.13835
- [M] Steyvers and Peters (2025) Metacognition and uncertainty communication in humans and LLMs. https://arxiv.org/abs/2504.14045
- [V] Kapoor et al. (2024) LLMs must be taught to know what they don't know. https://arxiv.org/abs/2406.08391
- [V] Binder et al. (2024) Looking inward. https://arxiv.org/abs/2410.13787
- [M] Ji-An et al. (2025) LMs are capable of metacognitive monitoring. https://arxiv.org/abs/2505.13763
- [V] Huff and Ulakci (2025) JOLs distinguish humans from LLMs. https://pmc.ncbi.nlm.nih.gov/articles/PMC12504528
- [M] Cheng et al. (2024) Can AI assistants know what they don't know? https://arxiv.org/abs/2401.13275
- [M] Gekhman et al. (2024) Does fine-tuning on new knowledge encourage hallucinations? https://arxiv.org/abs/2405.05904
- [M] Ferrando et al. (2025) Do I know this entity? https://arxiv.org/abs/2411.14257
- [V] Orgad et al. (2025) LLMs know more than they show. https://arxiv.org/html/2410.02707v4
- [M] Azaria and Mitchell (2023) The internal state of an LLM knows when it's lying. https://arxiv.org/abs/2304.13734
- [M] Mallen et al. (2023) When not to trust language models. https://arxiv.org/abs/2212.10511
- [M] Jeong et al. (2024) Adaptive-RAG. https://arxiv.org/abs/2403.14403
- [M] Zhang et al. (2024) R-Tuning. https://arxiv.org/abs/2311.09677
- [M] Yona et al. (2024) Can LLMs faithfully express their intrinsic uncertainty? https://arxiv.org/abs/2405.16908
- [M] Zhou, Jurafsky and Hashimoto (2023) Navigating the grey area. https://arxiv.org/abs/2302.13439
- [M] Didolkar et al. (2024) Metacognitive capabilities of LLMs. https://arxiv.org/abs/2405.12205
- [M] Yoon et al. (2025) Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489
- [M] Mei et al. (2025) Reasoning about uncertainty. https://arxiv.org/abs/2506.18183
- [V] Zhang et al. (2025) Reasoning models know when they're right. https://arxiv.org/html/2504.05419
- [M] Lugoloobi and Russell (2025) LLMs encode how difficult problems are. https://arxiv.org/abs/2510.18147
- [M] Shrivastava, Kumar and Liang (2025) Language models prefer what they know. https://arxiv.org/abs/2502.01126
- [M] Zhang et al. (2025) AdaptThink. https://arxiv.org/abs/2505.13417
