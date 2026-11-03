# Intelligent tutoring and knowledge tracing: deep document

*Subfield A05.08. Evidence ids (a01-a26, b01-b28, c01-c28, d01-d23) refer to evidence_a-d.jsonl in this folder. Claim ids (K01-K25) refer to claims.jsonl. Corrections from critique.md are applied here. Status tags: [E] established, [S] single-source, [C] contested. Items marked "recalled" were not opened.*

## 1. What it is

An intelligent tutoring system (ITS) watches a learner solve problems step by step, checks each step, and keeps a running estimate of what the learner knows. It uses that estimate to choose the next problem and to decide when to stop practice. The estimate is called **knowledge tracing** (KT). The step check is called **model tracing**. Both come from Anderson's ACT-R work and the Carnegie Learning "Cognitive Tutor" line (a01, a02, a25).

Three things are bundled in this field:

1. **A student model.** A per-skill belief that the learner has mastered the skill. Classic form: Bayesian knowledge tracing (BKT), a two-state hidden Markov model (a01).
2. **A tutor policy.** Give feedback at once, show hints, pick the next item, stop at a mastery threshold (usually 0.95, recalled, a01/b22).
3. **A learning-science claim.** Step-based tutors with a student model help people learn about as much as human tutors (K14).

Since 2015 a fourth thread has grown: deep and language-model knowledge tracers, and LLM tutors. Most of the new evidence asks whether those beat the old simple models. The answer so far: often not, once baselines are fair (K01, K03, K04).

**Why it matters for our agent.** The agent is one language model run through a scaffold. The scaffold needs a cheap, honest way to know "how well can I do this kind of problem right now". That is the question KT answers for a human. The schema already has a "class record" (plain pass rate per problem class, SCHEMA section 5) and guardrails G1 (act on a signal), G3 (test on unfitted data), G7 (pay for itself at equal tokens), G12 (spend by difficulty). This subfield gives older, better-tested versions of those ideas.

Hard limit on transfer: **no study tests knowledge tracing on an LLM agent's own per-skill competence** (K25, gap 1). Everything below is transfer by analogy. The learning RCTs (Kestin, Bastani, Tutor CoPilot) test tutors, not student models. Nothing shows that a better student model causes better learning (critique.md).

## 2. History and theories in depth

### 2.1 ACT-R and the Lisp tutor (1980s to 1995)

Anderson's ACT-R holds that skill is a set of production rules. Practice makes a rule faster and more reliable, following a power law (a25, not opened). Tutors were built so each rule in the ideal model could be checked. Two ideas followed (a02, recalled, not opened):

- **Model tracing:** compare each learner step to the ideal rule model; give feedback immediately.
- **Knowledge tracing:** estimate a mastery probability per rule from the stream of right and wrong steps.

Recalled early results (a02): Lisp-tutor students needed roughly one third to one half less time with equal or better test scores; an algebra pilot gave about one standard deviation on locally built tests. Early tests were author-built and small. Later large trials found much less (2.7 below).

### 2.2 Bayesian knowledge tracing (Corbett and Anderson 1995)

BKT is a two-state hidden Markov model per skill (a01, not opened; content from citing papers). Four parameters: prior p(L0), learning p(T), guess p(G), slip p(S). After each answer the tutor updates P(learned). The learner moves on when P(learned) passes about 0.95. It assumes one skill per step, no forgetting, and one parameter set for all learners (a01 limits).

### 2.3 The deep-learning turn and its correction (2015-2016)

- **Piech et al. (2015), Deep Knowledge Tracing (DKT)** (a04, b11, opened). An LSTM reads the sequence of (skill, correct) pairs and outputs the chance of success on each skill. AUC: ASSISTments DKT 0.86 vs BKT 0.67 vs best BKT in the literature 0.69 (marginal baseline 0.62); Khan Math (47,495 students, 1.4M answers) DKT 0.85 vs BKT 0.68 (marginal 0.63); simulated data (4,000 students, 50 exercises) DKT 0.82. The authors called this a 25% AUC gain over the best prior result.
- **Khajah, Lindsey and Mozer (2016), How deep is knowledge tracing?** (a03, b01-b03, opened and re-checked). They re-ran BKT properly. About **31.6%** of the DKT-BKT gap came from a biased AUC procedure for BKT. Another **50.6%** vanished when BKT got forgetting. Classic BKT scored 0.73 (not 0.67) on ASSISTments; BKT with forgetting 0.83. Extended BKT (forgetting, learner ability, skill discovery) versus DKT: Synthetic +20.0% relative (0.05 AUC; 0.80 vs 0.75), Spanish +3.0% (0.846 vs 0.836; 182 students, 409 exercises), ASSISTments -8.3% (0.03 AUC), Statics -3.5% (0.01 AUC; BKT+FSA 0.75 vs 0.76). The "+20.0%" is relative, not AUC points.
- **Wilson, Karklin, Han and Ekanadham (2016), Back to the basics** (b04-b06, opened). Hierarchical IRT matched or beat DKT. About **25% of ASSISTments rows were duplicates** that leak the label in online prediction. Their RNN reproduced 0.86 on raw data. After cleaning: 346,740 interactions, 4,097 users, 26,684 items. KDD set: 3,679,198 interactions, 1,146 users. DKT could not be tuned to tens of thousands of items. On one commercial set an optimal history window existed; on ASSISTments and KDD longer windows were no better, so static models sufficed.

### 2.4 Benchmarks and honest comparison (2020-2022)

- **Gervet, Koedinger, Schneider and Mitchell (2020), When is deep learning the best approach** (a06, a07, opened). On 9 datasets a logistic regression with good features (success and failure counts, recency) led DKT on 4 of 9. DKT's edge was largest on big, sequence-rich data: assistments17 DKT 0.770 vs best logistic 0.714 (+0.056 AUC; only +0.016 on first attempts). Other DKT gaps: +0.029 assistments15, +0.020 assistments12, +0.010 statics, +0.007 squirrel; algebra05 logistic 0.831 vs DKT 0.821. A feedforward net got +0.048 (assistments17) and +0.014 (assistments12) over logistic. Skill-ID features added 0.01 AUC or less on most sets and about 0.03 on the KDD Cup sets.
- **Pavlik, Eglington and Harrell-Williams (2021), Logistic Knowledge Tracing** (a08, opened). A constrained logistic framework; test AUCs seen 0.782 and 0.749 on ASSISTments and Andes (345,536 observations). Shows count and recency terms give a strong tracker.
- **Liu et al. (2022), pyKT** (b07-b10, d15, opened). Benchmark of deep tracers under 5-fold CV. Best model AKT, but its margin over second best is small: +3.06% AS2009, +1.50% AL2005, +1.62% BD2006, +1.60% NIPS34, +0.30% Statics2011, +1.08% POJ. **Label leakage** from multi-concept questions inflated results: mean +8.38% AUC (AS2009) and +13.09% (AL2005), about 0.1% on BD2006 and NIPS34 (about 1.01 concepts per question there, vs 1.20 and 1.36). Original code used future labels to predict current mastery. DKT on AS2009 leaked AUC 0.8262 (gain 0.0843). Math AUC about 0.8, programming (POJ) about 0.6.
- **Ghosh, Heffernan and Lan (2020), AKT** (b12, opened). Attention with a monotonic decay; up to 6% AUC over baselines. Their re-run found DKT beat DKVMN.

### 2.5 Identifiability and mastery thresholds

An older worry: BKT is "non-identifiable" (Beck and Chang 2007, not checked). **Doroudi and Brunskill (2017)** show this is misleading (d08, opened): BKT is identifiable under mild conditions. The real risk is **semantic degeneracy**. When learners follow a different true model (their test: a 10-level mastery model), fits on 500 sequences of 20 steps and on 100 sequences of 200 steps gave different degenerate parameters (P(S)=0.44 vs P(G)=0.49). The first fit implies a mastered student answers correctly only 56% of the time, against a true 90%, so the tutor stops practice too early or too late.

Our own simulation (d09, not literature): near-best parameter sets (L0 0.20-0.40, T 0.11-0.17, S 0.10-0.14, G 0.22-0.30) needed 3 to 4 correct answers to pass P >= 0.95 (truth 3), and 4 to 5 at 0.99 (truth 4). After C,C,I,C,C, 74% of near-best sets said "mastered" (truth 0.984). So in a well-specified world the threshold shifts by about one attempt. The 0.95 value is a convention. K16 is contested.

### 2.6 Worked examples and the cognitive tutor

Schwonke, Renkl, Krieg, Wittwer, Aleven and Salden (2009) added faded worked examples to the Cognitive Tutor Algebra (a24, d10). **We could not open the paper** (paywalled; evidence b28 pointed to a wrong DOI; the right one is 10.1016/j.chb.2008.12.011). From recall only: about 25% less learning time at equal procedural scores in a field study, with higher conceptual gains. N and p-values unverified. Related abstracts: Salden et al. (2010): adaptive fading > fixed fading > problem solving only, in two experiments. Booth et al. (2013): four groups did not differ on paper-and-pencil or delayed tests; the control group needed more learning time on examples (d10). Link: the Worked examples subfield is researched in parallel; not covered here.

### 2.7 Large-scale field results

- **VanLehn (2011)** (a23, d03; abstract only): human tutoring d = 0.79, step-based ITS d = 0.76; folk beliefs (0.3 / 1.0 / 2.0) not confirmed. The answer-based value (recalled 0.31) and substep-based (recalled 0.40) are not in the abstract.
- **Pane et al. (2014)**, RAND randomized trial of Cognitive Tutor Algebra I (a22, b24, d01, d02; abstracts): no effect in year 1; year 2 about +8 percentile points, +0.21 SD for high schools, not significant for middle schools. Recalled: about 147 schools.
- **Meta-analyses** (abstract level): Ma et al. 2014 (107 effect sizes, 14,321 learners): g = 0.42 / 0.57 / 0.35 vs various controls, -0.11 vs an individual human tutor, 0.05 vs small group (d05). Kulik and Fletcher 2016: median +0.66 SD over 50 evaluations, test-dependent and small in school settings (a21, d04). Steenbergen-Hu and Cooper 2013, K-12 maths: g = 0.01 to 0.09; short interventions larger than year-long ones; low achievers gained less (d06). A 2026 K-12 meta-analysis: g = 0.274 (SE 0.011), 18 studies, 79 effect sizes, 11 systems (d07).

Pattern: big effects on home-made tests in short lab studies; small and slow effects at scale in schools.

### 2.8 LLM era

See section 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| DKT beat BKT on ASSISTments in the original paper | AUC 0.86 vs 0.67-0.69; Khan 0.85 vs 0.68 | Piech 2015 (a04, b11) | [E] as a report; superseded |
| Much of that gap was an artefact | 31.6% from biased BKT AUC; 50.6% more gone with forgetting; BKT 0.73, BKT+F 0.83 | Khajah 2016 (a03, b01, b02) | [E] (K01) |
| Duplicate rows leaked labels | about 25% of ASSISTments rows; IRT matched or beat DKT | Wilson 2016 (b04-b06) | [S] (K02) |
| Extended BKT equals DKT on average | +20.0% rel. Synthetic, +3.0% Spanish, -8.3% ASSISTments, -3.5% Statics | Khajah 2016 (b03) | [E] (K03) |
| Logistic with counts and recency competes with DKT | logistic led on 4 of 9 sets; DKT edge +0.056 on assistments17, +0.007 to +0.029 elsewhere | Gervet 2020 (a06, a07) | [E] (K03) |
| Label leakage inflates KT benchmarks | +8.38% AS2009, +13.09% AL2005; under 1 point on BD2006, NIPS34 | Liu 2022 pyKT (b08, d15) | [S] (K04) |
| Newer deep models barely beat DKT | AKT best by +0.30% to +3.06% | pyKT (b07) | [S] (K04) |
| BKT is identifiable; the risk is semantic degeneracy | fit says master correct 56% vs true 90% | Doroudi 2017 (d08) | [C] (K16) |
| Threshold sensitivity (own simulation) | pass point moves about 1 attempt; 74% of near-best fits pass C,C,I,C,C | d09 | [C] (K16) |
| Zero-shot LLMs barely beat "always correct" | baseline 51.3%; GPT-OSS-120B 56.2% / AUC 0.559; Qwen3-80B-Thinking 55.8% / 0.555; Qwen3-80B-Instruct 54.0% / 0.539; Llama-3.3-70B 52.3% / 0.512; N about 27,700 | Worden 2026 (c01) | [E] (K05) |
| Optimism bias in LLM judges of learners | Llama-3.3-70B 85.4% right when student correct, 12.6% when wrong; Qwen3-Instruct 56.5 / 51.0; GPT-OSS 68.2 / 43.4; Qwen3-Thinking 63.6 / 44.6 | Worden 2026 (c02, d11) | [E] (K06) |
| Zero-shot Llama 3 8B vs DKT | AUC 0.69 vs 0.83; fine-tuned 0.77; accuracy 64% zero-shot, 75% DKT, 72% fine-tuned; low-performer recall 20 / 64 / 64; fine-tuning about 198 h | Hooshyar 2025 (c06, d12) | [E] (K05, K06) |
| LLM tracers cost far more | DKT/SAKT under 0.25 s per student; GPT-4o-mini 3.1 s; Gemini 128 s; Qwen2.5-7B 3,299 s; 600-12,000x | Bhattacharyya 2026 (c09) | [S] (K18) |
| On Eedi, specialised models about equal the best LLM tracer; prompted LLMs below baseline | LLM-KT 72.8%, SAKT 72.7%, DKT 71.8%; Gemini-flash-lite 66.5%, Qwen2.5-7B 64.6%, GPT-4o-mini 58.6%; per-question baseline 66.5% | Bhattacharyya 2026 (c08, d13) | [S] (K20) |
| Fine-tuned LLM with item text, large gain | Eedi AUC 90.32 vs DKT 72.37; ID-only 77.06, tags 84.59, text 90.32 | NTKT (c11, c12) | [C] (K07); no replication (K22) |
| Question text is the source of LLM edge | removing question info costs 3.08 AUC points on Assist2009 (0.8291 vs 0.7983) | LLM-KT (a12) | [E] (K08) |
| LKT ties DKT on the large set, loses on the small | XES3G5M-T: DKT 0.8480, DKVMN 0.8513, best LKT ERNIE 0.8508 (DeBERTa-v3 0.8468); DBE-KT22: AKT 0.7984 vs best LKT 0.7643 | LKT 2024 (a11, b17; c13 corrected) | [C] (K07) |
| Cold start: text tracers transfer, ID tracers do not | DKT 0.5 AUC with no target data | LKT (b18) | [E] (K08) |
| CLST cold-start gain | AUC gain up to 24.52% (8 students), 14.66% (16), 12.31% (32), 8.71% (64) | CLST (a13) | [S] |
| Few-shot cognition-guided prompts | FrcSub GPT-4 0.7968 vs DKT 0.7481; MOOCRadar GLM4 0.8489 vs 0.8210; XES3G5M GLM4 0.8491 vs DKT 0.8355 (AKT 0.8435); GLM3-6B 0.54-0.66; sparse XES3G5M 4 shots 0.4399, 8 shots 0.7057, 16 shots 0.7542 | Li 2024 (c15, c16) | [S] |
| Written profile refined by feedback | ASSIST2009 ACC CIKT 0.775 / 0.777 vs DIMKT 0.749, DKT 0.737, GPT-4o 0.732, DeepSeek-R1 0.669; without profile 0.755; without iteration 0.772; gains level off at about 3 rounds | CIKT (c17, c18) | [S] (K09) |
| Dialogue tracing | CoMTA AUC: LLMKT 65.79, DKT-Sem 61.82, DKT 53.20, BKT 52.50, majority 50.0; MathDial LLMKT 76.71 vs DKT-Sem 66.18, AKT 63.31 | Scarlatos 2025 (c19) | [S] (K10) |
| LLM label noise in dialogue | GPT-4o final-turn accuracy 75.82% (83.33% on human sample) vs teachers 85.56%; over 90% positive labels | Scarlatos (d17) | [S] (K23) |
| LLMs rank item difficulty, not discrimination | difficulty 68.6% (80.0% on large gaps); discrimination best 46.9%; rare distractor about 15 points below chance; Thinking model distractor 20.5% | Worden 2026 (c04, c05) | [S] (K17) |
| Simulated students need explicit profiles | r = 0.72 with real (45 simulated vs 100 real, 20 MCQs); random profile r = -0.16; alpha 0.6176 vs 0.559 vs 0.042 | Lu and Wang 2024 (c21) | [S] (K19) |
| Guarded AI tutor beat active class | N=194; post median 4.5 (n=142) vs 3.5 (n=174); effect 0.63 (regression), 0.73-1.3 SD (quantile); 49 vs 60 min | Kestin 2025 (a16, c24) | [E] (K11) |
| Unguarded GPT harmed unaided exam | about 1,000 students; practice +48%, exam -17%; GPT Tutor practice +127%, exam about 0 | Bastani 2025 (a18, d18) | [E] (K11) |
| ChatGPT hints lost to human hints | gain 11.14% vs 24.63% (Elementary), 1.7% vs 23.65% (Intermediate); N=77; 70% of hints passed check | Pardos 2023 (a20, b15, c23) | [S] (K12) |
| LLM help for human tutors | exit-ticket pass 62% to 66% (p<.01); +9 points for lower-rated tutors; about 20 USD/tutor/year; 700+ tutors, 1,000+ students | Tutor CoPilot (a19, c25) | [S] (K13) |
| ITS about equal to human tutors | VanLehn 0.76 vs 0.79; Ma -0.11 vs human | VanLehn 2011; Ma 2014 (d03, d05) | [E] (K14) |
| Field ITS effects are small | Pane: 0 year 1, +0.21 SD year 2 (high school); K-12 g = 0.01-0.09 and 0.274 | d01, d02, d06, d07 | [E] (K14) |
| How AI help is used decides outcome | Study 2 N=107 post-test not significant (p=0.206); Study 3 N=69 learning phase +4 questions (p=0.003); field N=113, 6,594 obs | Lehmann 2025 (d19) | [C] (K24) |
| Meta-analyses of ChatGPT | g = 0.573 (22 pubs); g = 0.577 (37 effects); mostly assisted or immediate tests | d23 | [C] (K24) |

## 4. Mechanisms and models

### 4.1 BKT, implementable

State per (learner, skill): `p = P(learned)`. Parameters: `L0` (prior), `T` (learn rate), `G` (guess), `S` (slip).

```
update(p, correct):
  if correct: p_obs = p*(1-S) / (p*(1-S) + (1-p)*G)
  else:       p_obs = p*S     / (p*S     + (1-p)*(1-G))
  p_next = p_obs + (1-p_obs)*T
mastered if p_next >= 0.95
P(next correct) = p*(1-S) + (1-p)*G
```

Fit L0, T, G, S by EM or grid search per skill. Constrain G and S below 0.5 to avoid the flipped solution (semantic degeneracy, d08). Fit on whole sequences, not on the last window.

### 4.2 BKT extensions that carried the DKT gap (Khajah 2016)

- **Forgetting (BKT+F):** after a gap, `p` decays toward a floor. This one change recovered 50.6% of the DKT-BKT gap (b02).
- **Learner ability:** a per-learner offset on the logit of success.
- **Skill discovery:** cluster items into skills when the labelled skills are poor.
- **Recency:** one parameter was enough to fit ASSISTments reliably (a10). Forgetting did not help on synthetic data because simulated students never forget.

### 4.3 Logistic tracers (PFA, LKT, Gervet)

Predict `P(correct) = sigmoid(w0 + w_skill + a*successes + b*failures + c*recent_window_mean + d*time_since_last)`. Gervet found this beats or ties DKT on 4 of 9 sets and trails by 0.007-0.056 AUC elsewhere (a06). It trains in seconds and is readable. Features that mattered: counts and recency. Skill-ID features added 0.01 or less on most sets (a07).

### 4.4 DKT and attention tracers

DKT: input = one-hot of (skill, correct) per step, LSTM hidden state, output = P(correct) for every skill, loss on the next step's skill (a04). The "influence graph" derived from outputs (a05) gave a skill-to-skill dependence map, with no AUC attached. AKT adds a Rasch-style item-difficulty embedding and a decayed attention over past steps (b12). Evaluate with a leak-free split: never feed the current step's label, and for multi-concept items do not expand one question into several rows with the label visible (b08).

### 4.5 LLM tracers

Three recipes appear in the literature.

1. **Prompted zero-shot or few-shot:** put the history as text and ask for the next outcome. Weak: AUC 0.51-0.69 (c01, c06). Few-shot with a cognition-guided prompt can reach DKT level on 2 of 3 sets with 8-16 shots; 4 shots collapses (c16). Small models (GLM3-6B) break the output format (c15).
2. **Fine-tuned next-token prediction (NTKT, LKT, LLM-KT, CLST):** write each interaction as text including the question; predict the correctness token. Item text drives the gain: ID-only 77.06, concept tags 84.59, full text 90.32 AUC (c12).
3. **Profile loop (CIKT):** an LLM keeps a written learner profile, predicts, compares with the true outcome, rewrites the profile; a second model collaborates. About 3 rounds then plateau (c18, d16). Gain of +0.01 to +0.04 accuracy over classic models (c28).

For dialogue (Scarlatos, c19): label each tutor-student turn with knowledge components and correctness using an LLM, then fine-tune a tracer that reads the dialogue.

### 4.6 Step checking versus answer checking

Model tracing checks every step. VanLehn's comparison (d03) is why this matters: step-based tutors approach human tutors, answer-based tutors are much weaker (value recalled 0.31, unverified). This is the human-tutoring analogue of process versus outcome checking.

### 4.7 Guardrails of effective AI tutors

Kestin's tutor and Bastani's GPT Tutor shared a design: the model has the solution in its prompt, is told not to give it, asks the learner to try a step first, and gives staged hints (a16, a18). Bastani's unguarded GPT Base answered practice problems correctly only 51% of the time (42% logic errors, 8% arithmetic, a18), so the unguarded helper was wrong about half the time.

## 5. What holds up

**Replicated or multi-source (strong).**
- DKT's headline lead was mostly an artefact of baselines and metric (Khajah, Wilson, Gervet; 3 sources). Extended BKT or logistic with recency gets within a few AUC points of DKT, and sometimes beats it (K01, K03).
- Zero-shot LLMs are poor at predicting one learner's next answer (Worden, Hooshyar, Bhattacharyya; 3 sources; K05).
- LLM optimism bias (Worden, Hooshyar; K06). Model-specific: Qwen3-Instruct is near balanced (56.5 / 51.0); Llama-3.3 is extreme (85.4 / 12.6).
- Question text is the useful input for LLM tracers (LLM-KT, LKT, NTKT; K08).
- Step-based tutoring approaches human tutoring in studies (VanLehn, Ma; K14), but field effects are small and slow (Pane, Steenbergen-Hu; K14).

**Failures, boundary conditions, competing explanations.**
- Leakage depends on data. Large for multi-concept sets (+8.38%, +13.09%), under 1 point for single-skill sets (b08). So leakage does not explain the NTKT gap on Eedi (d14).
- DKT's edge is largest on big, sequence-rich data (assistments17) and smallest on first-attempt data (a06). Depth earns its keep only with much data.
- LLM-KT results flip with fine-tuning, item text and baseline: LKT ties DKT on XES3G5M-T (0.8508 vs 0.8480) and loses on DBE-KT22 (0.7643 vs AKT 0.7984); Hooshyar fine-tuned 0.77 vs DKT 0.83; Eedi benchmark specialised 72.7-72.8% vs LLMs 58.6-66.5%; NTKT 90.32 vs 72.37. K07 is contested.
- No independent replication of NTKT (AUC 90.32) or CIKT. NTKT baselines omit any per-question or logistic-with-recency model; CIKT uses an 8:1:1 split with no leakage audit (d14, d16; K21, K22).
- The 2015-16 story (baselines and leaks drove results) may repeat for 2024-26 LLM-KT claims (critique.md).
- AUC is not comparable across papers: different splits and metrics. DKT on Eedi is 71.8% accuracy in one paper and 72.37 AUC in another.
- A per-question average alone gets 66.5% on Eedi against 71.8-72.8% for the best trackers (d13). Item difficulty carries most of the signal (K20).

**Interventions that worked.** Guarded LLM tutoring with an unaided or delayed test: Kestin (0.63 by regression, 0.73-1.3 SD by quantile regression, vs active class, N=194); ChatTutor over plain ChatGPT in two experiments (N=175 and N=234; follow-up effect in Study 2 only; d20, abstract); a scaffolded LLM beat parent-led reading in a 67-child RCT with delayed tests (d21, abstract). LLM hints for human tutors (+4 points, Tutor CoPilot).

**Interventions that did not.** Unguarded GPT: practice +48%, exam -17% (a18). Bastani correction: the guarded GPT Tutor removed the harm but gave no positive unaided exam effect (d18). ChatGPT hints vs human hints (older model, N=77; 30% of hints failed a manual check). Lehmann: no overall effect; harm is in substitution use (asking for solutions), help in asking for explanations, and low-prior-knowledge learners lose most (d19). Booth 2013: worked examples gave no posttest or delayed difference (d10).

**Moderators.** Population (Harvard undergraduates vs MTurk adults vs high school), prompt design, outcome timing (immediate vs delayed, assisted vs unaided), model version, and test type (Kulik: test-dependent). Meta-analytic ChatGPT g about 0.57 mostly reflects assisted or immediate tests (d23).

## 6. Language models

**Behaviour on student-modelling tasks.**
- *Predict next-item correctness (FoundationalASSIST, 4 open models, N about 27,700, c01):* baseline 51.3%. GPT-OSS-120B 56.2% / AUC 0.559; Qwen3-Thinking 55.8% / 0.555; Qwen3-Instruct 54.0% / 0.539; Llama-3.3-70B 52.3% / 0.512. Context of 50-400 past interactions made no clear difference (d11). Exact-answer prediction: 35.5% to 44.3% (c03).
- *Optimism:* see section 3. Cognitive-modelling accuracy on incorrect answers only 14.5-19.8% (d11).
- *Hooshyar, Llama 3 8B (c06, c07, d12):* AUC DKT 0.83, zero-shot 0.69, fine-tuned 0.77. The fine-tuned model makes more errors early in a sequence. The zero-shot Youden-optimal threshold was 0.8789 (DKT 0.5782, fine-tuned 0.6211): the model must be pushed to be more pessimistic. Recall on high performers 83 / 95 / 78 (DKT / zero-shot / fine-tuned). Fine-tuning lifted AUC about 8% over zero-shot yet stayed about 6% below DKT.
- *Eedi benchmark (c08, c09, d13):* compute gap 600-12,000x; one cited LLM cost 11,991 USD per year at 100,000 students.
- *Item properties (c04):* relative difficulty fine, discrimination below chance. Reasoning ("Thinking") helped abstract judgment (46.9%) but hurt concrete prediction (distractor 20.5%, c05). This fits schema G11.

**What changed the result, by how much.**
- Giving item text: +7.5 AUC points from ID to tags, +5.7 more from tags to full text (77.06, 84.59, 90.32; c12). Removing question info: -3.08 AUC (a12).
- Fine-tuning: about +8% AUC for Llama 3 8B (c07); low-performer recall 20 to 64 (d12).
- A threshold shift undoes much of the optimism bias at no training cost (d12), but AUC does not change.
- A written profile with 3 refinement rounds: ACC 0.766 (no iteration and cooperation), 0.772 (no iteration), 0.775 (full); 0.755 without profile at inference (c18). Small.
- Few-shot count: 4 shots 0.4399, 8 shots 0.7057, 16 shots 0.7542 (GLM4 on sparse XES3G5M, c16). Many shots needed.
- Model size: GLM3-6B 0.54-0.66 and format failures vs GLM4 0.82-0.85 (c15). Llama-1B zero-shot 33.5% vs LoRA 71.0% (d13).

**LLMs as tutors.** Kestin (a16): AI tutor with pedagogical prompt, median post 4.5 vs 3.5 and 49 vs 60 minutes. Bastani (a18): unguarded GPT Base wrong on 51% of practice items. Pardos (a20): ChatGPT hints, older model, lost. Tutor CoPilot (a19): the LLM helps a human, with gain concentrated in weaker tutors. Lehmann (d19): use mode decides. Kosmyna (d22): essay writing with ChatGPT in 54 people; we found no delayed knowledge test with scores, so it is not used as evidence.

**LLMs as simulated students.** Generative Students (c21, c22): profile-conditioned GPT-4 r = 0.72 with real per-question means; fails when the right answer is unknown and a confused rule is available (27.6% wrong when mastered but a confused rule was among the options).

**Open point.** None of these test an LLM's tracking of its own per-skill competence. The closest facts: LLMs are over-optimistic about others (K06), and the schema already says model confidence is a weak stopping signal (SCHEMA 4b).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = SCHEMA section 5.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Fair-baseline rule.** Before crediting a scaffold element, re-run the plain arm with the same cheap extras (recency, retry, same scoring rule) at equal tokens. DKT looked 25% better until BKT got forgetting and a fair AUC. | G7 (supports), G1 | [E] K01, K03 | a03, b01-b03, a06 |
| A2 | **Count-based class record.** Keep per problem class (and mode) success and failure counts plus a recency term; use these, not the model's own feeling, for S0 mode choice and G12 spending. A 3-feature logistic is within a few AUC points of deep trackers. | memory (class record), S0, G12 | [E] that simple trackers match deep ones in KT; transfer to the agent is analogy | K03, K05, K20; a06, c01, d13 |
| A3 | **Never let the model self-estimate competence by prompting alone.** LLM predictions of success sit near chance and are optimistic. Compare any prompted self-estimate with counts. | S0, G10 | [E] | K05, K06; c01, c02, c06 |
| A4 | **Measure and correct optimism.** Log recall on the agent's own wrong intermediate answers separately from right ones. Use a threshold shift, not a verbal instruction. | G3, G7, S4 | [E] for LLM optimism toward others; own-error detection is analogy | K06; c02, d11, d12 |
| A5 | **Leak audit.** No step may see the gold answer, future steps or duplicate test items. Report scores with and without suspected leaks. | G3 | [E] | b05, b08, b09, d15 |
| A6 | **Item text in memory, not only ids.** Retrieved experience should carry the task text. Text-based trackers transfer to new data; id-based ones drop to chance. | memory | [E] K08 | a12, c12, b18 |
| A7 | **Step-level checks beat answer-only checks** where steps can be run; keep checks as code. Matches G2. | G2, S4 | [E] K14 (answer-based d unverified) | d03 |
| A8 | **Guard helper tools.** If the agent can call a helper that gives solutions, force its own attempt first and give hints, not answers. Unguarded help harmed unaided results in humans. | G2 | [E] K11 for humans; agent transfer is analogy | a16, a18, d18, d19 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Count-based class tracker vs none for routing, mode choice and stopping at equal tokens | S0, G12, memory | [S], no direct study (K25) | d13, a06 |
| T2 | Margin or two-clean-runs stop rule vs fixed rounds; threshold sweep | G1, S8 | [C] K16 | d08, d09 |
| T3 | Item text vs id/tag in the tracker prompt | memory | [C] K07 | c12, a12 |
| T4 | Refined written state profile, up to 3 rounds | memory, O | [S] K09 | c17, c18 |
| T5 | Forgetting/recency decay on lesson trust and class record | memory | [S] from Khajah, human data | b02, a10 |
| T6 | Explanation-only vs solution-giving helper, scored unaided and delayed | G2, G9 | [C] K24 | d19, d20 |
| T7 | Gate generated hints/plans by a quality check | G7, S5 | [S] K12 | a20, b15 |
| T8 | Fade worked examples in the prompt as the tracker rises | memory, S1 | [S] K15, numbers unverified | d10, a24 |
| T9 | Weak-component assist (give the helper to the weaker mode) | O | [S] K13 | a19 |
| T10 | Model difficulty ordering as a cheap S0 signal, not discrimination or distractors | S0 | [S] K17 | c04, c05 |
| T11 | Per-step knowledge-component labels of agent runs predicting next-step success | S9, memory | [S] K10 | c19, d17 |
| T12 | LLM or fitted sequence tracer vs logistic with recency on the same split | research only | [C] K21, K22 | d14 |

T4 must not turn into unstructured self-reflection (SCHEMA 4b): the profile is rewritten from real outcomes (G2), not from opinion.

## 8. Concrete tests on our bench

All arms get equal tokens (G7). The tracker's own tokens are counted inside the budget.

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Mixed ARC and BrainTeaser items with a class label | (a) plain fixed mode; (b) mode and spend chosen by a count-based class record (success, failure, recency); (c) mode chosen by the model's own estimate | accuracy per 1,000 tokens; share of budget spent on items solved at first pass | b >= a by 2+ points; c <= b. Small: simple trackers carry most of the signal (K20) |
| T2 | Items with a code check | stop after fixed rounds vs stop when the margin rule (two clean checks) holds; thresholds 0.90, 0.95, 0.99 on a count-based belief | accuracy, tokens per correct answer, premature stops | margin rule gives fewer premature stops; threshold moves the pass point by about one attempt (d09) |
| T3 | Retrieval of lessons from memory | lesson keyed by task id vs concept tag vs full task text | accuracy on held-out classes | text > tags > id, direction as in c12; size unknown for agents |
| T4 | Multi-round items | no profile; profile of verified/confused sub-skills rewritten each round for 3 rounds; same for 6 rounds | accuracy, tokens | 3 rounds >= 0 by 1-2 points; no gain after 3 (c18) |
| T5 | Long runs with repeated classes | class record with no decay vs exponential decay of old outcomes | Brier score of predicted pass rate; accuracy | decay helps only if competence drifts (e.g., prompts change); null otherwise |
| T6 | Tasks with a helper tool | direct-answer helper vs attempt-first hint helper vs explanation-only helper; later no-helper run on matched items | unaided accuracy on the later run, split by the class's plain pass rate | attempt-first and explanation arms >= direct; harm shows on classes where the model is weak (d19) |
| T7 | Plan or hint generation | use every generated hint vs reject hints failing a code or small check | accuracy, rejection rate | gain only if rejection rate is high (30% in c23) |
| T8 | Few-shot tasks with worked examples | examples constant vs faded as the class record rises | tokens per correct answer | same accuracy, fewer tokens; unknown |
| T9 | Items split into two solver modes | helper hints to both modes vs only the weaker mode | accuracy by mode | gain concentrated in the weaker mode (cf. +9 points for lower-rated tutors) |
| T10 | 200 item pairs with known pass rates | model orders each pair by difficulty; model predicts discrimination | pair accuracy; correlation with class pass rate | difficulty ordering usable (about 68%); discrimination at chance |
| T11 | Logged runs, labelled step by step | LLM-labelled sub-skill per step; count tracker predicts next-step success | AUC of next-step success; label precision on "wrong" | AUC above 0.55 only if label noise is tolerable; report precision on wrong labels (d17) |
| T12 | Logged outcomes from T1 | logistic with counts and recency vs the model asked to predict its own success (prompted) vs a fitted sequence model | AUC on a held-out split with a leak check | logistic >= prompted by 5+ AUC points (c01, d13) |

## 9. What does not transfer, and why

- **Training.** DKT, AKT, NTKT, LKT, CLST all train on thousands to millions of interactions. Our agent has hundreds of items per run and no training (project rule). Only the cheap parts transfer: counts, recency, decay, text-keyed memory.
- **Learner-specific histories.** KT predicts one human's next answer from their history. The agent has class-level pass rates, not a long per-learner stream. "Skill" maps to problem class, not to a person.
- **Learning during practice.** BKT assumes the learner moves from unlearned to learned through practice. A frozen model does not learn within a run. Learning shows up only through memory and lessons, so P(T) is not a natural parameter. Forgetting as decay of lesson trust is the nearest analogue, and it is untested.
- **Mastery thresholds as stopping rules.** The 0.95 convention rests on a human learning model and has a semantic-degeneracy risk (d08). For an agent, stopping is governed by checks and budget (G1, G6, G12), not by an inferred state.
- **Learning RCTs.** Kestin and Bastani measure human gains from an AI tutor. They support "do not hand over solutions" for human-in-loop use, but say nothing about an LLM's competence. Our agent has no delayed human test.
- **Human tutor effect sizes.** Effects are test-dependent (Kulik), small at scale (Pane, Steenbergen-Hu), and unverified at exact-number level for VanLehn's answer-based value and Pane's per-level sizes.
- **Dialogue tracing** depends on teacher or human outcomes; the agent's "dialogue" is its own trace, whose text is not evidence (G10).
- **LLM cost.** LLM tracers cost 600-12,000x more compute than DKT (c09); under G7 a tracer must win at equal tokens. A count-based tracer costs almost nothing.
- **Worked-example gains** (Schwonke) are unverified here and rest on human cognitive load; see the Worked examples subfield.

## 10. Open questions

1. Does a tracker of the agent's own per-class competence improve routing or stopping at equal tokens? No direct study (gap 1, K25).
2. Do LLM tracers with item text beat logistic regression with recency (not only DKT) on the same split? Nobody has run it (gap 2, K21).
3. Can the 85.4% vs 12.6% optimism be removed by calibration or a verifier, and does it map to the agent's weak detection of its own errors? Partly closed: model-specific, threshold shift helps, no verifier tested (gap 3).
4. Do NTKT (90.32 AUC) and CIKT replicate independently with leakage checks? None found (gap 4, K22).
5. What are Schwonke et al. (2009) exact numbers: N, time saved, procedural and conceptual scores? Open the paper (gap 5, K15).
6. Pane's per-level and per-year effect sizes and VanLehn's answer-based d: verify from full text (gap 6).
7. How much does the mastery threshold matter when the learner model is wrong, not just under-fit? Our simulation covers only the well-specified case (gap 7, K16).
8. Does the attempt-first guardrail effect hold on non-maths tasks and delayed tests? Partly closed by coding (Lehmann), ChatTutor and a child reading RCT; the last two are abstracts only (gap 8).
9. What does label noise cost in dialogue tracing? Noise is measured (75.82% vs 85.56%), cost is not (gap 9, K23).
10. Why does the Eedi gain from 72.37 (DKT) to 90.32 (NTKT) not show in the independent Eedi benchmark (72.8% best)? Different metrics, splits and data cuts are possible; unresolved.
11. Is "reasoning hurts concrete prediction" (c05) specific to student modelling or a general LLM effect? One source.

## 11. Sources

[V] = opened and read (text or PDF) in this study. [M] = snippet, abstract or recall only.

| Source | Mark | URL |
|---|---|---|
| Corbett and Anderson (1995) Knowledge tracing (a01, b22) | [M] | https://doi.org/10.1007/BF01099821 |
| Anderson, Corbett, Koedinger, Pelletier (1995) Cognitive tutors: lessons learned (a02) | [M] | https://doi.org/10.1207/s15327809jls0402_2 |
| Anderson (1993) Rules of the Mind; ACT-R (a25) | [M] | https://act-r.psy.cmu.edu/ |
| Piech et al. (2015) Deep Knowledge Tracing (a04, a05, b11) | [V] | https://arxiv.org/abs/1506.05908 |
| Khajah, Lindsey, Mozer (2016) How deep is knowledge tracing? (a03, a09, a10, b01-b03) | [V] | https://arxiv.org/abs/1604.02416 |
| Wilson, Karklin, Han, Ekanadham (2016) Back to the basics (b04-b06) | [V] | https://arxiv.org/abs/1604.02336 |
| Gervet, Koedinger, Schneider, Mitchell (2020) When is deep learning the best approach (a06, a07) | [V] | https://zenodo.org/records/4143614 |
| Pavlik, Eglington, Harrell-Williams (2021) Logistic Knowledge Tracing (a08) | [V] | https://arxiv.org/abs/2005.00869 |
| Liu et al. (2022) pyKT (b07-b10, d15) | [V] | https://arxiv.org/abs/2206.11460 |
| Ghosh, Heffernan, Lan (2020) AKT (b12) | [V] | https://arxiv.org/abs/2007.12324 |
| Doroudi and Brunskill (2017) Misidentified identifiability of BKT (d08) | [V] | https://files.eric.ed.gov/fulltext/ED577166.pdf |
| Beck and Chang (2007) identifiability of BKT (b23) | [M] | https://educationaldatamining.org/ |
| Baker, Corbett, Aleven (2008); Pardos and Heffernan (2010); Yudelson et al. (2013) (a26) | [M] | https://educationaldatamining.org/ |
| Own simulation, BKT threshold sensitivity (d09) | local, not literature | D:/research_scratch/A05.08/ |
| Schwonke et al. (2009) Worked-example effect (a24, b28, d10) | [M] | https://doi.org/10.1016/j.chb.2008.12.011 |
| Salden et al. (2010); Booth et al. (2013), abstracts only (d10) | [M] | see d10 in evidence_d.jsonl |
| VanLehn (2011) Relative effectiveness of human tutoring, ITS (a23, b25, d03) | [M] | https://doi.org/10.1080/00461520.2011.611369 |
| Pane et al. (2014) Cognitive Tutor Algebra I at scale (a22, b24, d01) | [M] | https://doi.org/10.3102/0162373713507480 |
| Pane et al. (2014) RAND addendum (d02) | [M] | http://www.rand.org/pubs/working_papers/WR1050.html |
| Kulik and Fletcher (2016) meta-analysis (a21, b26, d04) | [M] | https://doi.org/10.3102/0034654315581420 |
| Ma, Adesope, Nesbit, Liu (2014) meta-analysis (d05) | [M] | http://dx.doi.org/10.1037/a0037123 |
| Steenbergen-Hu and Cooper (2013) K-12 maths meta-analysis (d06) | [M] | http://dx.doi.org/10.1037/a0032447 |
| 2026 K-12 ITS meta-analysis (d07) | [M] | https://eric.ed.gov/?id=ED682145 |
| Secondary review PMC12078640 (context for Kulik and Pane) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC12078640/ |
| Lee et al. (2024) LKT (a11, b17, b18, c13, c14) | [V] | https://arxiv.org/abs/2406.02893 |
| LLM-KT (2025) (a12) | [V] | https://arxiv.org/abs/2502.02945 |
| CLST (2024) (a13) | [V] | https://arxiv.org/abs/2406.10296 |
| CIKT, Li et al. (2025) (a14, c17, c18, d16) | [V] | https://arxiv.org/abs/2505.17705 |
| Li et al. (2024) Explainable few-shot KT (c15, c16) | [V] | https://arxiv.org/abs/2405.14391 |
| Systematic review of KT and LLMs (2024) (a15) | [M] | https://arxiv.org/abs/2412.09248 |
| Norris, Gal, Bulathwela (2025) NTKT (c11, c12, d14) | [V] | https://arxiv.org/abs/2511.02599 |
| Worden et al. (2026) FoundationalASSIST (c01-c05, d11) | [V] | https://arxiv.org/abs/2602.00070 |
| Hooshyar et al. (2025) Problems with LLMs for learner modelling (c06, c07, d12) | [V] | https://arxiv.org/abs/2512.23036 |
| Bhattacharyya et al. (2026) Faster, cheaper, more accurate (c08, c09, d13) | [V] | https://arxiv.org/abs/2603.02830 |
| Eedi blog (2026) (c10) | [M] | https://eedi.com/news/we-benchmarked-llms-against-purpose-built-models-it-wasnt-close |
| Scarlatos et al. (2024/2025) KT in tutor-student dialogues (b19, b20, c19, c20, d17) | [V] | https://arxiv.org/abs/2409.16490 |
| Sonkar et al. (2023) CLASS framework (b21) | [V] | https://arxiv.org/abs/2305.13272 |
| Lu and Wang (2024) Generative Students (c21, c22) | [V] | https://arxiv.org/abs/2405.11591 |
| Kestin et al. (2025) AI tutoring outperforms active learning (a16, a17, b13, b14, c24) | [V] | https://www.nature.com/articles/s41598-025-97652-6 and https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/ |
| Bastani et al. (2025) Generative AI without guardrails (a18, b27, d18) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/ |
| Wang et al. (2024, rev. 2026) Tutor CoPilot (a19, b16, c25) | [V] | https://arxiv.org/abs/2410.03017 |
| Pardos and Bhandari (2023) ChatGPT vs human hints (a20, b15, c23) | [V] | https://arxiv.org/abs/2302.06871 |
| Lehmann, Cornelius, Sting (2025) AI meets the classroom (d19) | [V] | https://arxiv.org/abs/2409.09047 |
| ChatTutor, Beyond the Wow factor (2025) (d20) | [M] | http://dx.doi.org/10.1007/s10648-025-10039-x |
| Parent-led vs AI-guided dialogic reading RCT (2025) (d21) | [M] | http://dx.doi.org/10.1111/bjet.13615 |
| Kosmyna et al. (2025) Your brain on ChatGPT (d22) | [V] | https://arxiv.org/abs/2506.08872 |
| ChatGPT meta-analyses (ERIC EJ1501298; EJ1478249) (d23) | [M] | http://dx.doi.org/10.1111/jcal.70096 |

Note on versions: critique.md corrections are folded in above (LKT table rows in c13; Scarlatos columns in b19, use c19; "+20.0%" is relative; Bastani GPT Tutor gave no positive unaided gain; b28 DOI). Evidence lines c13 and b19 stay in the jsonl files as written; do not cite them for those numbers.
