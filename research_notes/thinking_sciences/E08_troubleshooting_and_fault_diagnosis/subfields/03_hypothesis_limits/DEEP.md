# Hypothesis limits in troubleshooting: deep document

*Subfield E08.03. Built from evidence_a-d.jsonl (a01-a29, b01-b31, c01-c25, d01-d19), claims.jsonl (E08.03-K01 to K29) and critique.md in this folder. Numbers marked "corrected" were re-checked against the source text in the cross-check pass. Raw line count overstates independence: Mehle appears in a01-a04, a13, a14, b10; Handler 2026 is b25/b26/c01/c02; Braitsch 2026 is a23/b31/c03/c04; McDuff is b23/c08; Ke is a24/b24; Goh is b22/c07. Count each as one source.*

---

## 1. What it is

The question. How many candidate causes does a troubleshooter hold in mind? Does that number limit how well they find the fault? What happens when the true cause was never on the list? What happens when someone hands them a list? And do language models share these limits?

Four linked problems sit under this one heading.

1. **Count.** People generate and hold few hypotheses, about 3 to 5, whatever their skill.
2. **Completeness illusion.** A short list feels complete. People assign high probability to "the cause is on my list" and too little to "something I have not thought of".
3. **Premature closure and anchoring.** The first hypothesis steers what is looked at next. Evidence that fits is counted. Evidence that does not fit is dropped. The search stops early.
4. **Supplied hypotheses.** Giving a person a list (from a colleague, a decision aid or a language model) can widen their view. It can also stamp approval on their first guess.

Why it matters for our agent. The agent is a language model inside a scaffold. A model has no 3-to-5 memory span for listing. It can write twenty candidates. But the effects that matter still appear in models in a different form:

- It commits to a listed option even when none fits (about 70 percent of the time on no-correct-option items, c01).
- It asks for less data each round and keeps its round-1 diagnosis (c03, c04).
- Its independent samples repeat the same few causes (d01, d03, d04).
- It accepts a wrong supplied hypothesis, more so when the hypothesis carries authority (d07).

The scaffold can take the "holding" job away from the model. Code holds the list. The model only proposes and checks one item at a time. The research question for us is which parts of the human pattern remain, and which structural steps remove them at equal tokens.

Scope notes.

- This document does not cover how to pick the next test (see Probing and measurement selection), the search order over a system (Troubleshooting search strategies), how debugging hypotheses are formed (Hypotheses in debugging, LLM debugging), anomaly fixation (Anomaly handling and fixation), or conflict generation (Consistency-based diagnosis). Links are noted where the overlap is direct.
- Rasmussen and Morris and Rouse, named in the brief, could not be opened in full. What was confirmed is thin and is reported honestly in 2.6 and 5.

---

## 2. History and theories in depth

### 2.1 The medical thread: early hypotheses, three to five at a time (1970s to 2009)

Elstein, Shulman and Sprafka (1978, book; not opened, known through a08, a09, b12) studied physicians solving simulated cases. Their core findings, as summarised by Elstein himself in 2009 (a08, opened):

- Physicians generate a small set of hypotheses from a few early findings. This happens very early in the encounter.
- They hold "between three and five" at once. Elstein calls this the "magic number 4 plus or minus 1".
- They could "easily enumerate more possibilities" if asked (a08). So the limit is on what is held and used, not on what is known.
- Experts, picked by peer rating, were not more accurate than others in that sample. The small case sample could not separate them.
- Strategy did not separate good from poor solvers. Both used hypothesis testing. Content knowledge mattered more (a09).

Elstein and Schwarz (2002, a09) list the error types that follow: the correct hypothesis is missing from the initial set; findings are read as fitting the favoured hypothesis; contradicting facts are forgotten; positive findings are over-weighted; adjustment from the anchor is too small. They write that many diagnostic problems are so complex that the correct answer is not in the initial set.

Barrows, Norman, Neufeld and Feightner (1982, a28, snippet only) watched 18 family physicians and 19 internists across 62 simulated encounters. Physicians formed several hypotheses early and used them to direct questions. Accuracy and promptness of generation went with diagnostic accuracy. So the first set is the bottleneck.

A McMaster follow-up reported in a 1980 Journal of Family Practice article found no difference between family physicians and internists in number or type of hypotheses (b12, second-hand). A patent text states a mean of 2 to 4 held at once. That figure is unverified and unattributed. Do not hard-code four from the secondary sources.

Graber, Franklin and Gordon (2005, a26, abstract only): among 100 internal-medicine diagnostic error cases (33 deaths), cognitive factors appeared in 74 percent. Premature closure was the single most common cognitive cause. Faulty knowledge was uncommon. Selection bias applies: cases came from autopsy discrepancies and incident reports. This is not an error rate.

### 2.2 Mehle and the Oklahoma programme: the car-trouble study (1980)

Mehle's 1980 dissertation (a01 to a04, a13, a14; opened in full, numbers re-checked) is the cleanest count in this subfield. It sits in an ONR-funded line by Gettys, Fisher, Manning, Baca and Mehle (a13).

Design. 12 subjects: 6 "experts" (1 ex-mechanic student and 5 motor-pool staff) and 6 novice undergraduates. Five car-trouble problems each. Subjects typed "all plausible hypotheses you would entertain". They also gave a probability that the true cause was in their list.

Results.

- Mean hypotheses per problem: novices 3.43, experts 3.36. No skill effect.
- Pooled over all 12 people: 17.8 distinct hypotheses per problem (novices alone 12.6, experts alone 11.2).
- One person produced only 19.2 percent of the pool.
- A sampling model (fixed N available, each person finds share S of the unfound) fit the pooling curve. Novice fit N=18.1, S=.179 (predicted 3.24 vs observed 3.43). Combined N=21.5. So even 12 people missed about 3.7 per problem. The pooling curve was still adding about 1 new hypothesis per added person at 12 people.
- Stated probability that the true cause is in the list: novices 69.2 percent, experts 67.5 percent. Treated as probabilities over exclusive causes and pooled, the estimates sum to 504 percent. The limit is 100.
- Only 7 unacceptable hypotheses in total, about 0.1 per person per problem. Subjects checked each hypothesis against the data as it came and threw out misfits (a04).
- Experts named specific parts (neutral safety switch). Novices named causal chains (alternator, voltage regulator) that link to the symptom only indirectly (a14).
- One expert's protocol suggests the probability came from how long the list looked ("a lot" was read as "very probable") (a14). This is two subjects' protocols and one coder. It is a guess, not a finding.

Mehle's reading: people stop when they have filled "a memory span". Caveats that matter for how far to push this: N=12; the "experts" are mostly motor-pool staff; typing costs effort and may cap the count; the instruction was "all plausible", which invites a short list. The pooled reference is the group, not an omniscient mechanic, so 19.2 percent is an upper bound on coverage.

The Oklahoma group's wider model (a13): Gettys and Fisher (1979) proposed an executive process that starts, steers and stops recursive memory searches, and restarts retrieval when the plausibility of the current set is low. Mehle et al. (1979) tied the overconfidence to availability. The DTIC final report (b11, snippet only) names the cause as a retrieval deficit, not a reasoning deficit. Fisher and Gettys (1987, quoted second-hand in a19) estimate people use about 2 cues when 3 are available and about 3 when 4 are.

### 2.3 Fault trees and what is out of sight (Fischhoff, Slovic, Lichtenstein 1978)

Fischhoff et al. (a05 to a07, a15, b01 to b04; full PDF opened, numbers re-checked) tested the completeness illusion directly. Subjects saw a "car won't start" fault tree and judged the share of failures due to each branch, including "all other problems". Some trees had major branches deleted.

Their three explanations (a15): credibility (spotting a gap discredits the tree and inflates "other"); availability (what is not shown is not thought of); accurate internal frequencies. The data fit availability best. Their rule of thumb: the missing share grows with how many missing things you can think of and with your unfamiliarity with the system. The rule was proposed, not tested.

Numbers are in section 3. The shape: "other" should have risen several-fold when branches were deleted. It rose by far too little. Telling people to focus on "other" helped a little. Experienced mechanics did no better than students. Splitting a branch into two parts raised its judged share.

### 2.4 HyGene and the memory-constraint account (2008 to 2014)

HyGene (Thomas et al. 2008; reviewed in Thomas, Dougherty and Buttaccio 2014, a17/b05, opened) is the model behind this literature. Three principles:

1. Data cue hypotheses from long-term memory.
2. The number held in working memory is limited by capacity and task load.
3. Held hypotheses drive probability judgment and information search.

Consequences.

- Fewer held hypotheses give higher probability per hypothesis. Judgments over exclusive options then sum above 100 percent (subadditivity). Support theory (Tversky and Koehler) supplies the comparison rule: a hypothesis is judged by its strength against the alternatives retrieved at that moment (a21).
- If one hypothesis is held, search must be confirmatory. With two or more, search can be diagnostic (a17, b06). The supporting study is cited as unpublished with no N (b06). Dougherty et al. 2010 and Navarro and Perfors 2011 argue confirmatory search can be reasonable in realistic domains.
- Individual differences: subadditivity correlates with working-memory capacity (Dougherty and Hunter 2003, b09, not opened; second-hand through a17).
- Order effects (Lange, Thomas and Davelaar 2012; Lange 2011; a12, a18, a19). The same datum changes which hypothesis comes to mind depending on where it sits in the sequence. Slow presentation gave recency, fast gave primacy. Inconsistent hypotheses are purged from working memory. People do not go back to long-term memory for new ones (Exp 2, a19).
- ACT-R account (Mehlhorn et al. 2011, a20, opened). Four models compared on two experiments with artificial chemicals and symptoms. The best treated all observed symptoms as equal activators with no decay. Fit R2: Exp 1 .85 (number model) vs .70 (constant); Exp 2 .71 vs .45. Human accuracy was high (95.5 and 95.9 percent), so errors were rare. The authors summarise earlier work as "up to four" hypotheses generated from memory.

Sprenger et al. (2011, a11/a21/b07/b08) tested the chain "load, then fewer hypotheses, then inflated judgments". They found a small effect, and found the count mediates it. One HyGene prediction (that encoding load would not matter) was wrong. Details and a correction are in section 3.

### 2.5 Premature closure, anchoring and the bias-and-debias story (1990s to 2022)

The popular story: bias causes error; teach people about bias; error falls. The evidence is weaker than the story.

- Availability bias induced in residents (Mamede et al. 2010, b15, snippet): prior exposure to look-alike cases lowered second-year accuracy, reflection restored it. N=36, order confound (reflection always last), extra time uncontrolled.
- Failed replication (Staal et al. 2021, b16, opened): N=117 residents, no significant bias effect induced.
- Cognitive forcing training (Sherbino et al. 2014, b21, snippet): no effect.
- Knowledge-based "immunising" with contrasting cases and feedback (Mamede et al. 2020, b17, snippet): worked on biased vignettes.
- Norman et al. (2017, b20): biases can be induced in the lab but their share of real errors is not established. Teaching bias recognition does not reduce errors. Knowledge reorganisation gives small, consistent gains.
- Meta-analyses (b18, b19, snippets): guided reflection 0.38; reasoning tools g=0.20.

Kostopoulou's line on early suggestions. Earlier studies by the same group found accuracy gains from giving physicians early diagnostic suggestions (a22; figures not in the opened text). The 2022 follow-up (Kourtidis et al., a10, opened) tried to find the mechanism and mostly found nothing clear (numbers in section 3). Where the suggested list contained the physician's own first diagnosis, they were more certain and asked for less information. The authors say they "may become closed- rather than open-minded". The mechanism is unproven.

### 2.6 Rasmussen, Morris and Rouse: what could be confirmed

The brief names these as anchors. Full texts were behind bot walls. What was opened (d16 to d19):

- **Rasmussen and Jensen 1974** (abstract, d16). Skilled electronics repairers. Verbal protocols show search down a hierarchy of subunits as repeated routines, with fast good/bad judgments. When a routine failed they showed "a fixation... a tendency to rely on repetitions, rather than to generate specific procedures". No hypothesis count.
- **Rasmussen's two search strategies** (secondhand via Venkatasubramanian 2003, d19). Topographic search compares the system with a template of normal operation. Symptomatic search uses symptoms to point to the fault. This review cites Rasmussen 1985 and 1986, not the 1981 chapter. It says nothing about hypothesis counts. (The strategies belong to the Troubleshooting search strategies subfield.)
- **Morris and Rouse 1985** (abstract, d17). How explicitly instruction specifies action-related information strongly affects performance. Requiring trainees to apply system knowledge is promising but not yet supported by transfer studies. No count.
- **Rouse 1978** (a27, abstract): fault diagnosis in displayed networks. Performance fell short of optimal as problems grew. Forced pacing pushed people toward brute-force strategies. A computer aid that did the bookkeeping cut incorrect diagnoses substantially. No numbers read.
- **Georgia Tech aid, 1985** (d18, grant report). The aid "augments working memory with the display of hypotheses and data". Design intent only, no effect size. It is the earliest statement we found of an external hypothesis ledger.

Honest summary: the claim that Rasmussen or Morris and Rouse measured how many hypotheses operators hold is not supported by anything we opened. Do not cite either for a count (claims K28).

### 2.7 Models of the engineered-systems side

Classical decision-support systems (Berner, Jackson and Algina 1996, c21; abstract-level): across DXplain, Iliad, Meditel and QMR on 105 cases, producing the correct diagnosis was not related to how many diagnoses the system listed. It was related to knowledge-base coverage. Lesson: longer lists do not buy accuracy. Reach does. INTERNIST-1 (c22, snippet) was built on hypothesis lists and scoring; the weak spots listed (no anatomic or temporal reasoning) still appear in LLM failure lists.

### 2.8 Language-model era (2022 to 2026)

The question moved from "how many does a person hold" to three LLM questions: does the model's list contain the true cause, does it commit too soon, and does it hold on to its first answer? Evidence is mostly 2024 to 2026 preprints on medicine, with a small set from root cause analysis (RCA), hardware debugging and program induction. Detail is in section 6.

---

## 3. Core findings with exact numbers

Status key: **established** = two or more independent sources agree (claims.jsonl); **single** = one source; **contested** = sources disagree or controls are missing. "Opened" lines were read this session. Evidence ids in brackets.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Experts and novices list the same few causes | 3.43 novice, 3.36 expert hypotheses per car problem; N=12, 5 problems each | Mehle 1980 [a01] | single for the exact count; the 3-to-5 range is established across Mehle, Elstein, HyGene [a08, a17, a20] |
| Physicians hold 3 to 5 at once but could list more | "between three and five"; no per-physician means given | Elstein 2009 [a08] | established as a range; patent figure "2 to 4" unverified [b12] |
| Pooled over people, plausible causes are far more than any one list | 17.8 distinct pooled vs 3.4 each; one person found 19.2% of pool; model fit N=21.5; curve still +1 per added person at 12 | Mehle 1980 [a02] | single |
| Lists feel complete | stated P(true cause on my list) 69.2% novice, 67.5% expert; pooled adjusted sum 504% | Mehle 1980 [a03] | single in people; consistent with Fischhoff [a05] |
| Hidden branches are not moved into "other" | "other" should rise .078 to .468, rose to .140 (tree 1); should be .611, was .227 (tree 2); N=148 (93+29+26); 1 of 55 pruned-tree subjects gave "other" enough | Fischhoff et al. 1978 Exp 1 [a05, b01] | established with the mechanics replication |
| "Think about what is missing" helps only a little | Exp 2, N=82: tree 1 .140 to .217 (t(49)=1.88); tree 2 .227 to .346 (t(58)=1.81); still far below .468 and .611 | Fischhoff 1978 Exp 2 [a06, b02] | single |
| Experts are no better at noticing omissions | Exp 6: 29 of 60 mailed returned (16 pruned, 13 unpruned); target .441, mean .215 (U z=2.87); median .16 vs .47; experience tau=.058; 2 to 43 years | Fischhoff 1978 Exp 6 [a06, b03] | single; small, 48% return |
| Splitting a branch raises its share | +.066, about a third more; sign tests 20/27 (p=.010), 19/26 (p=.014), fused 24/33 (p=.007); N=115 | Fischhoff 1978 Exp 5 [a07, b04] | single |
| Cognitive load cuts hypothesis count and inflates judged probability | Exp 1 N=167: sums 261.8, 265.4, 264.7, 271.5; F(3,161)=3.13. **Corrected:** that is a rise of 3.7%, not the "about 10%" in the paper's text. Exp 3 count by attention F(1,97)=35.07; count vs sums r=-.47 (balanced) and -.33 (unbalanced); controlling count leaves F=0.00 and 0.04 | Sprenger et al. 2011 [a11, b07, b08] | established but small effect |
| Working-memory span relates to inflated sums | r=-.187 to -.284 (Exp 1); -.229 to -.476 (Exp 3) | Sprenger 2011 [b07]; Dougherty and Hunter 2003 [b09, not opened] | established |
| Cue order shapes what is generated | later cues weigh more at slow pace, earlier at fast; Exp 1 N=72, mean 1.67 to 1.89 hypotheses, no count difference by order (F(3,68)=0.567, p=.64) | Lange et al. 2012 [a12, a18] | contested: the weight effect holds, the count effect is null |
| Contradicted hypotheses are purged, not re-cued | clear purge evidence, no evidence of new long-term-memory search | Lange 2011 [a19] | single |
| A held hypothesis count of 1 forces confirming tests | no N reported | Thomas, Lange, Dougherty (unpublished) [b06] | single, second-hand |
| Supplying a hypothesis list to physicians: no clear benefit | Exp 2: 194 of 217 analysed; diagnosis changed 50.0% with list vs 46.9% without (OR 1.196, p=.389). Exp 3: 248 of 273 analysed; changed more when the likely diagnosis was left out of the list vs in (OR 2.143, p=.018), not vs control (OR 0.960, p=.769) | Kourtidis et al. 2022 [a10] | contested: earlier studies by the same group found accuracy gains [a22] |
| First impression steers diagnosis | odds of diagnosing cancer 4.90x (CI 2.72 to 8.84); referral odds 1.98; 90 physicians, 6 cases; 29% of effect mediated by cancer-related questions | Kostopoulou et al. 2016 [b14] snippet | single |
| Availability bias, reflection | N=36; second-years 1.55 vs 2.19 (P=.03); reflection 1.55 to 2.03 | Mamede 2010 [b15] snippet | contested (see Staal) |
| Availability induction failed to replicate | N=117 (113 analysed), no bias effect; correct 115 s vs incorrect 129 s (d=0.37); confidence-accuracy R2=0.03 | Staal et al. 2021 [b16] | single replication |
| Contrast-knowledge "immunising" worked | 91 residents; biased vignettes 0.40 vs 0.24 (diff 0.16, CI 0.05 to 0.27, p=.004); non-biased 0.36 vs 0.41 (p=.45) | Mamede 2020 [b17] snippet | single |
| Cognitive forcing training did nothing | 191 students; second search started 52% vs 48% (p=.91); found 54% vs 48% (p=.13); availability cases 45% both | Sherbino 2014 [b21] snippet | single |
| Guided reflection helps a moderate amount | 44 studies, 4380 professionals, 0.38 (CI 0.23 to 0.52) | meta-analysis [b18] snippet | single meta-analysis |
| Reasoning tools help a little | 29 studies, 2732 participants, g=0.20 (CI 0.10 to 0.29), I2 70% to 38% after removing 3 tool-training studies | meta-analysis [b19] snippet | single meta-analysis |
| Premature closure is the top cognitive cause of diagnostic error | 100 cases; cognitive factors in 74% | Graber et al. 2005 [a26] snippet | single; selection bias |
| LLMs commit when no option is correct | MedQA n=500 (250 no-correct-option), AfriMed n=490; false action about 70% baseline, about 48% with safety prompt; MedQA 55 to 81% across models. **Correction:** false action is measured on the no-correct-option items only (250/245), not on all items | Handler, Bedi, Shah 2026 [c01, b25] | established with Bedi 2025 |
| Replacing the correct option with "None of the other answers" | 68 items. DeepSeek-R1 92.65 to 83.82 (drop 8.82); o3-mini 95.59 to 79.41 (16.18); Claude-3.5-Sonnet 88.24 to 61.76 (26.47); Gemini-2.0-Flash 92.65 to 58.82 (33.82); GPT-4o 85.29 to 48.53 (36.76); Llama-3.3-70B 80.88 to 42.65 (38.24) | Bedi et al. 2025 [d06] | established with Handler |
| Models close early when nothing signals risk | HealthBench n=861: under-specified low-risk 73.2 to 96.1% (mean 81%); under-specified urgent 5.0 to 35.8% (mean 19%); overall 20.7 to 44.6%; safety prompt cuts overall by 4.2 to 7.9 points. Adversarial n=191: 59.3 to 91.4%, lowest residual 50.8%. Clarification rate on sufficient-context control 3.5% | Handler 2026 [c02, b26] | single |
| LLM agents anchor on round-1 diagnosis | 32 models, 20 cases, 3 rounds. Of 323 wrong or partial at round 1, 212 (65.6%) stayed wrong. Of 307 correct at round 1, 156 (50.8%) were wrong or partial by round 3. Recovery 100% (6/6, Opus 4.5) to 7.1% (1/14, Qwen3 Next 80B) | Braitsch et al. 2026 [c04, a23] | established with triage study [d12] |
| LLMs request less data each round | requests per round 7.5, 4.2, 1.8; share of data obtained 56.8%, 56.7%, 25.7%; utilisation vs accuracy R=0.69 | Braitsch 2026 [c03] | single |
| Differential reasoning is the weak step | diagnosis 66.6%, treatment 58.8%, differential 43.6%; gap 23.0 points; best overall 68.1% (Opus 4.6), mean 56.3 +/- 7.4 | Braitsch 2026 [c03] | established (list-contains vs top-1 gap in Brodeur [c09]) |
| The answer is in the list more often than first | NEJM CPCs: correct in differential 78.3% (CI 70.7 to 84.8); first suggestion 52%. 70 shared cases: exact or very close 88.6% vs 72.9% for GPT-4 (p=.015). ER, 79 cases: o1 65.8/69.6/79.7% across three touchpoints vs physician 54.4/60.8/75.9% | Brodeur et al. 2024 [c09] | established as a pattern (older: GPT-4 64% in differential, 39% top, unresolved denominator [c10]) |
| Chief complaint dominates in staged triage | 425 simulated plus 50 clinician-written conversations, five checkpoints; best QWK 0.295 vs clinicians 0.887 to 0.929; reasoning decoding and Plan-and-Solve did not remove the plateau | triage study 2026 [d12] | single, second source for anchoring |
| Independent LLM draws repeat; distinct causes grow sublinearly | unique programs at K=2,4,8,16,32: 1.40, 1.79, 2.92, 4.56, 7.89 (GPT-4o-mini, failed instances). Differential diagnosis, 302 NEJM cases: recall of reference concepts rises only +0.131 from 1 to 5 draws, recall at k=5 about 0.29 to 0.35. Top-5 configurations picked by single-draw quality had 13.8% mean regret on coverage and 0/5 overlap with the true top 5 | Lee et al. 2025 [d03]; Le Bronnec and Yokota 2026 [d01]; HypoSpace [d04] | established (3 sources) |
| A bare "give something different" step did not raise coverage | chain vs independent at k=5, 8 configs: mean relative coverage -7.9% (min -15.4, max +5.4), positive in 1 of 8; per-draw precision 0.090 vs 0.204 (DS-V4 no-think), 0.127 vs 0.264 (GLM-4.7 think). Other tasks: evidence search +8.3% (8/8), molecules +16.0% (6/8), repository repair -11.5% (0/8) | Le Bronnec and Yokota 2026 [d02] | contested (task-dependent) |
| Naming K concepts first, then one hypothesis each, helps | Mixture of Concepts: +4.5 points (GPT-4o-mini), +5.0 (Llama-3.1-70B) at 8 hypotheses; +0.37 to +1.00 unique of 8; no consistent gain with one greedy hypothesis | Lee et al. 2025 [d03] | single, program induction only |
| Forcing a differential-first prompt does not help | GPT-4: CoT 76%, differential 78% (+2.2, CI -1.4 to +5.8, p=.24); GPT-3.5: CoT 46%, differential 38% (-8, CI -13 to -4.5, p<.001); 518 items | Savage et al. 2023/24 [d05, c11] | single; 2023 models |
| Tracked-hypothesis ledger stops silent loss, costs top-1 | 10-case deep subset of 50: unscaffolded reached correct 9/10, kept 6/10; scaffold access 80%, final 80%, 0 loss; top-1 60% to 40%; access 90% to 80%; output tokens +28% | Wang 2026 [c05, d11] | single (**corrected**: earlier "0 regressions in 40 observations" omitted the top-1 cost) |
| Challenger roles improve LLM diagnosis | Ke: 16 cases, 80 runs, initial 0/80 (by selection), top 57/80 (71.3%), top two 64/80 (80.0%). MAI-DxO on o3: 81.9% at $4,735 vs o3 78.6% at $7,850, physicians 19.9% at $2,963; budgeted 79.9% at about $2,396; ensemble 85.5% | Ke 2024 [a24, b24]; Nori 2025 [c06] | contested: no same-token control in either |
| Debate does not reliably beat self-consistency | five MAD methods, nine benchmarks, four models: no reliable win over CoT or SC; at matched compute on MMLU-Pro (70B): CoT 64.3, SC 68.7, debate 70.0, mixture-of-agents 71.4 (the abstract says +1.3 for debate and the body +1.4) | Zhang 2025 [d13]; Pareto paper 2026 [d14] | contested; general reasoning only |
| LLM aid for physicians: null on reasoning, positive on list breadth | Goh: 50 physicians, 76 vs 74 (diff 2, CI -4 to 8, p=.60), 519 s per case, LLM alone +16 (CI 2 to 30, p=.03). McDuff: 302 cases, 20 clinicians, top-10 accuracy 51.7% (with LLM) vs 36.1% (without) vs 44.4% (search); LLM alone 59.1% vs 33.6% | Goh 2024 [b22, c07]; McDuff 2023/25 [b23, c08] | contested; different tasks and scoring |
| Wrong supplied option is accepted, more under authority | accuracy drop basic / expert nudge: GPT-4o -2.36 / -4.36; GPT-5.2 -1.94 / -11.17; DeepSeek V3.1 -4.22 / -19.79; Kimi K2 -2.41 / -10.86; Mistral Large 3 -7.48 / -19.27; GPT-OSS-120b -0.33 / -1.62 | Christophe et al. 2026 [d07] | established with BiasMedQA [c12] |
| Prompt defense depends on model strength | Med-Stress RBED: GPT-4o 41.50 to 92.79 (+51.29); Llama-3.1-8B 1.55 to 8.00 | Xiao et al. 2026 [d08] | single |
| Suggested wrong answer lowers accuracy | BiasMedQA 1,273 questions, 7 biases; GPT-4 0.727 baseline, false consensus 0.625; GPT-3.5 0.497 to 0.239; average drop largest for false consensus (24.9%), smallest for confirmation (8.1%); GPT-4 confirmation 0.2% (p=.91) | Schmidgall et al. 2024 [b27, b28, c12] | established |
| Anchoring in numeric answers; fixes weak | 162 comparisons, only 11 not following the hint; 12 of 12 questions followed a PTF-expert hint; CoT, principles, ignore-anchor, reflection did not remove it; both-anchors near unbiased on about 8 of 15 (GPT-4) | Lou and Sun 2024 [c14] | single |
| Self-debiasing flips decisions | change rates GPT-3.5 5.2%, GPT-4 17.5%, Llama-2-13b 52.1%, Llama-2-7b 39.9% (no ground truth, so "over-correction" is inferred); 13,465 prompts | Echterhoff et al. 2024 [c13, d09, b29] | single |
| Anchoring resistance is flat past a size | scores 0.49 to 0.78 across 45 models; prompt detail peaks at level 2 (0.649); above 32B bias fell in 39.5% of cases | Knipper et al. 2025 [c15] | single |
| LLMs test to confirm; counterexample prompting helps | 11 LLMs, 80 episodes per setting, success 6% to 78%; average discovery 42% to 56%; Think-in-Opposites helped in all 11 scenarios, Dual-Goal 8 of 11; thinking mode raised success but not the disconfirm ratio | Jhaveri et al. 2026 [d10] | single |
| Early commitment designs lose in RCA | GoS 48.2%, OpenRCA 46.6%, mABC 42.6%; 5,000 trajectories; incorrect runs 3.29 distinct failure modes vs 0.71 for correct | Lu et al. 2026 [c18] | single |
| A code-triggered audit and search-space wrapper helps RCA | DiagGuard Acc@1 gains +3.5 to +35.1 across 14 configs, median +10.5; ablation 400 incidents (Doubao, 5 runs): base 43.5, without Grounder 47.6, without Verifier 48.0, full 52.5; cost $0.16 vs $0.09 per incident | Lu et al. 2026 [c19] | single; authors built the tool from their own failure codes |
| Early-run similarity predicts low variability, not correctness | step-4 similarity vs variability r=-0.35 (CI -0.51 to -0.16, p=.0006); AUROC 0.81 from three partial runs; commitment prompt cut variability 28% vs filler but 15% vs standard (not significant); accuracy not improved (baseline 93.2%) | Mehta and Datta 2026 [c17] | single |
| Hardware-debug agent that marks, not drops, weak hypotheses | 38 real failures: hypothesis quality 95.6%, Pass@1 71.1%, Pass@5 86.8%; confidence below 0.2 after three iterations marked, not dropped | Bai et al. 2025 FVDebug [c20] | single; no ablation |
| A trained 7B model lists 7 to 10 diagnoses | binary reward: differential 62.4, final 31.4, length 9.56; tau 0.8: 65.2/32.5/8.66; tau 1.5: 57.2/31.6/7.25; dynamic tau 64.8/38.2/7.39 | pathology RL paper 2026 [d15] | single; training result |
| List length is unrelated to correctness in classic systems | 4 systems, 105 cases; correct diagnosis not related to number suggested | Berner et al. 1996 [c21] | single, abstract-level |

---

## 4. Mechanisms and models

Each mechanism is stated so an engineer could build it. The model is the proposer. Code is everything else.

### 4.1 The capacity-limited retrieval model (HyGene)

Components.

- Long-term memory: traces of past cases (data plus the hypothesis that explained them).
- Working memory: a buffer holding at most k hypotheses. k is 2 for low capacity or high load and 4 for high capacity (the values used in the simulations, a11, b05).
- Retrieval: observed data (cues) are matched to memory. Traces most similar to the cues are activated. Hypotheses are sampled from the activated set in proportion to activation. Stop after k are held, or after a number of failed retrieval attempts.
- Judgment: P(h) is the strength of h divided by the total strength of the held set plus a residual. A small held set means a large share for each member (subadditivity).
- Search: with one hypothesis held, tests are chosen to confirm. With two or more, tests are chosen that separate them (a17).
- Update: when new data contradict a held hypothesis, it is purged. No new retrieval is triggered unless plausibility of the set is low (Gettys and Fisher, a13). Lange found no new retrieval after purging (a19).

What this predicts and what it got wrong. It predicts load at judgment raises sums (confirmed). It predicted encoding load would not matter (wrong, a11). It predicts the count mediates the bias (confirmed by statistical control, not manipulation, b08).

Implementation for our agent. Do not copy the buffer. Copy the failure modes and fix each in code:

| Human failure | Agent equivalent | Code-side fix |
|---|---|---|
| Buffer holds 3 to 5 | Model writes a short list, then stops; each independent draw repeats the same few (d01, d03, d04) | Ledger object outside the context. Union across independent draws. Dedupe by cause, not by wording |
| Judge against only the retrieved set | Model gives high probability to its listed items | Code normalises probabilities across listed items plus a reserved "other" bucket. Raise the reserve when the class is unfamiliar |
| One hypothesis makes tests confirmatory | Model proposes tests that fit its guess (d10) | No test is chosen unless at least two live candidates exist; the test must split them |
| Purge, no re-cue | After a failed test the model prunes and keeps going with the survivors | A failed check triggers fresh generation (S3) and checks whether the true cause was dropped earlier |
| Order of cues changes what comes to mind | Order of facts in the prompt changes proposals (inferred from a12, a18) | Run independent draws with facts permuted. Merge candidates in code |

### 4.2 The "other" bucket model (Fischhoff availability account)

State: a tree of causes, each with a judged share; a residual "all other".
Observation: the residual does not grow when branches are hidden. The share moves to visible branches.
Implementation as a check:

1. Take any model-stated probability table over exclusive candidates plus "other".
2. Test A: sum equals 100 (code normalises; flag if the raw sum exceeds 100 by a set margin, per Mehle's 504 percent).
3. Test B: "other" at least a floor (set by class familiarity; see Test U2 below). The Fischhoff rule of thumb says the missing share rises with how many missing things you can imagine and falls with familiarity (a15, untested).
4. Test C: shuffle partitions. Present the same space as coarse and as fine. If the judged share of a branch moves by more than a set amount, average over partitions (b04: finer splitting raised a branch's share by about a third).

### 4.3 Pooled-sample capture model (Mehle)

Model. N hypotheses exist for the problem. Each independent sampler finds each unfound hypothesis with probability S. Expected found after j samplers: N(1 - (1-S)^j). Fit N and S to the pooling curve.

Mehle's fit: N=21.5 and S=.179 for combined data (a02). One person found 19.2 percent of the pool.

Use. Apply the same curve to the agent. Draw K independent generations (with facts permuted). Track cumulative distinct causes. Fit N and S. Read off (a) how many a single draw misses, (b) how many draws it takes to reach 80 percent of the estimated N. Model results so far suggest S is small and the curve is flatter than hoped: 1.40 to 7.89 unique programs from 2 to 32 draws (d03), +0.131 recall from 1 to 5 draws (d01). Caveat: the model assumes equal chance per hypothesis. Strong hypotheses are found first. Real curves are heterogeneous, so fit a two-class model (common and rare) if the single-rate fit is poor.

Equality of causes must be judged by cause, not wording. That needs a dedupe step. In program tasks equality is checked by output (d03). For faults, use a taxonomy slot (subsystem, failure mode) as the key, or have a separate, blind model call assign "same cause as X?" with code counting.

### 4.4 Ledger with accountability (Wang SIPS, FVDebug, Georgia Tech)

Structure (merging c05/d11, c20, d18).

```
ledger[h] = {
  text, source (self / supplied / retrieved), first_seen_stage,
  status (live / demoted / removed), confidence,
  evidence_for[], evidence_against[], removal_reason,
  untested_frontier (what test would separate h from the leader)
}
```

Rules.

- Nothing is deleted. Low-confidence items are marked (FVDebug: below 0.2 after three iterations).
- A removal needs a stated reason that cites a located observation (G2).
- At each new stage, code compares the best-seen hypothesis to the current leader. If the best-seen is not the leader, log it. The Wang result: without a ledger the right answer was reached in 9 of 10 and kept in 6 of 10. With the ledger: 0 lost, but top-1 fell from 60 to 40 percent.
- Report top-1 and top-k separately. The ledger buys retention at the cost of slower commitment.

What is not known: whether a ledger with a promotion rule can get retention without the top-1 loss. Wang's design forced a re-ranked differential at each stage with removal reasons; no arm re-ranks from scratch; no arm adds a promotion rule.

### 4.5 Convergence monitor (Mehta and Datta)

Idea. Across repeated runs of the same agent, track how similar their early states are. High similarity at step 4 predicts low variability of the final result (r=-0.35). It does not predict correctness. They had hidden-state access.

Black-box version for us. Compare the first-hypothesis set across K runs by overlap of the cause key. If overlap is high at the first step, the hypothesis space has collapsed. Use it only as a trigger for widening (a doubt signal under G1), never as a verdict (G4).

### 4.6 Concept-first generation (Lee et al.)

Procedure. Step 1: ask for K distinct concepts (not hypotheses), one line each. Step 2: for each concept, generate one concrete hypothesis. Result in program induction: +4.5 and +5.0 points at equal K of 8, and 0.37 to 1.00 more unique hypotheses of 8. With one greedy hypothesis no consistent gain.

Why it might work. It forces distinctness at the concept level before wording enters. It matches the Mehle point that the filter and the retrieval are separate steps.

Why it might not transfer. Fault causes are not programs; equality is harder. The bare chained version ("give something different") was negative for differential diagnosis (d02). Concept-first has not been tried on faults.

### 4.7 Structural versus instruction-level fixes

The pattern in the LLM data: instruction fixes work for strong models and fail or over-correct for weak ones.

- RBED prompt: GPT-4o 41.50 to 92.79; Llama-3.1-8B 1.55 to 8.00 (d08).
- Self-debias: Llama-2 changed 40 to 52 percent of decisions; GPT-3.5 changed 5.2 percent (d09).
- Differential-first prompt: GPT-4 +2.2 (not significant), GPT-3.5 -8 (d05).
- Counterexample prompting: 42 to 56 percent (d10); no structural arm.

A structural fix does not ask the model to resist. It changes what the model sees or what code allows. Examples: strip authorship and status from supplied hypotheses; present competing hypotheses together (c14: both-anchors strategy); allow a switch only on a named new observation. No head-to-head of structure against instruction exists for diagnosis (gap in critique).

---

## 5. What holds up

### 5.1 Replicated or supported by two or more independent sources

1. **Few hypotheses held, skill does not raise the count.** Mehle 3.4 vs 3.4; Elstein 3 to 5; HyGene and ACT-R "up to four" (a01, a08, a17, a20). The sources are linked (Mehle is cited in a20) so the independence is partial. Boundary: Mehle's typing effort; Elstein's small sample; no study varies output cost (gap).
2. **Short lists feel complete.** Mehle's 504 percent and Fischhoff's pruned trees point the same way in different tasks (a03, a05). Fischhoff replicated in mechanics (a06).
3. **Fewer generated, higher judged.** Sprenger plus Dougherty and Hunter, with a small effect (a11, b09).
4. **LLMs under-use "none of the listed".** Handler (about 70 percent false action) plus Bedi (all six models lose 8.8 to 38.2 points). Reasoning models lose least (d06).
5. **LLMs anchor on early evidence.** Braitsch (65.6 percent stuck) plus the triage study (d12).
6. **LLMs accept a wrong supplied option.** BiasMedQA (c12) plus M42 (d07).
7. **Independent LLM samples repeat.** Three sources in different tasks (d01, d03, d04).
8. **Answer in the list more often than first.** Brodeur (78.3 vs 52 percent) plus Braitsch (gap 23 points between diagnosis and differential, odd phrasing but same direction: the weak step is the differential and ranking).

### 5.2 Failures and nulls

- **Staal 2021:** availability bias could not be induced in 117 residents (b16). The Mamede 2010 result may be fragile (N=36, order confound).
- **Cognitive forcing training** gave no effect (b21).
- **Kourtidis 2022:** supplying a list had no clear effect on certainty, search or diagnosis changes in three experiments (a10). Earlier work by the same group found accuracy gains (a22).
- **Goh 2024:** physicians given GPT-4 did not improve (b22, c07).
- **Savage 2023:** differential-first prompt did not help GPT-4 and hurt GPT-3.5 (d05).
- **Chained "give something different"** lowered coverage in 7 of 8 configurations on differential diagnosis (d02).
- **Zhang 2025:** debate methods did not reliably beat CoT or self-consistency (d13).
- **Commitment prompt (Mehta):** reduced variability but not accuracy (c17).
- **Reasoning prompts and Plan-and-Solve** did not lift the early-evidence plateau in triage (d12).
- **Fischhoff Exp 2:** "focus on other" raised "other" only to .217 and .346, t about 1.8 each (a06).

### 5.3 Moderators and boundary conditions

- **Presentation pace** flips recency to primacy (a18).
- **Model strength.** Instruction fixes help strong models, harm or do nothing for weak ones (d05, d08, d09, b28). Bias warnings gave GPT-4 small gains and some weaker models refused or produced nonsense (PaLM-2 non-response 94.4 to 99.5 percent, b28).
- **Authority.** Expert-framed wrong nudges cost 1.6 to 19.8 points vs 0.3 to 7.5 for plain nudges (d07). Thinking variants of Qwen-3 collapsed more than instruct variants.
- **Task type for chaining.** The same chained step helped evidence search (+8.3 percent) and molecules (+16.0 percent) and hurt differential diagnosis and repository repair (d02).
- **Risk cue.** Models close early on harmless-looking under-specified items (81 percent mean) and rarely on urgent ones (19 percent) (c02). They react to danger, not to missing information.
- **Reasoning mode.** Reasoning models lose least in NOTA (d06), but thinking Qwen-3 is more vulnerable to expert nudges (d07), and thinking mode raised rule discovery without raising disconfirming tests (d10). So the effect of thinking is not uniform across bias types.
- **Task ceiling.** Mehta's HotpotQA accuracy was 93.2 percent, so a lack of accuracy gain may be a ceiling effect.

### 5.4 Interventions that worked

- Contrast-knowledge training in residents (0.40 vs 0.24, b17; abstract only).
- Guided reflection (0.38 pooled, b18; abstract only); reasoning tools (g=0.20, b19; abstract only). Realistic ceiling for a checklist-style aid is small.
- Instruction prompts in capable LLMs: counterexample prompting 42 to 56 percent (d10); RBED on GPT-4o (d08); GPT-4 few-shot bias education (75.2 percent best average, b28).
- Concept-first generation +4.5 to +5.0 (d03).
- Ledger with removal reasons stopped silent loss (d11), at a top-1 cost.
- Code-triggered self-audit, search-space profile and verdict check, additive: +4.1 and +4.5 each, +9.0 together (c19).
- Presenting two opposite anchors brought answers near unbiased on about 8 of 15 questions (c14).
- Computer bookkeeping cut incorrect diagnoses in humans in a network fault task (a27, Rouse 1978, abstract only).

### 5.5 Interventions that did not work, or are unproven

- Telling the model to avoid bias (c13: GPT-4 framing delta worsened to -0.470 under an awareness prompt).
- Cognitive forcing training (b21).
- Generic reasoning prompts for early-evidence anchoring (d12).
- CoT, principles, ignore-anchor and reflection prompts for numeric anchoring (c14).
- Debate roles at equal compute (d13). Possibly +1 to +3 points when tuned (d14).
- Safety prompt for premature closure: halves but does not remove (c01).
- A commitment prompt that stabilises runs without improving accuracy (c17).

### 5.6 Competing explanations

- **Memory span vs effort vs instruction.** The 3-to-5 count may reflect the task and the typing effort, not a memory limit. Elstein says physicians could list more. No study varies output cost.
- **Bias vs knowledge.** Norman (b20) argues that errors come more from knowledge gaps than from bias. Berner (c21) agrees that coverage, not list length, drives correctness. A scaffold that targets bias only may miss the main source.
- **Anchoring vs resolution.** Braitsch's anchoring is mostly at the level of diagnostic resolution (a disease family), not a specific disease (c04). It may reflect that models never go finer rather than that they fixate on a wrong disease.
- **Autoregression.** A commentary says LLMs anchor because earlier text weighs more (b30). The mechanism is stated, not tested.
- **Stability vs correctness.** Early similarity across runs is stability, not error (c17).
- **Sycophancy as rationalisation.** The authors of M42 suggest the reasoning trace "facilitates sycophancy by logically rationalizing" the wrong suggestion (d07). A guess, not a test.

### 5.7 Corrections made in this study (carry forward)

- Sprenger: use 3.7 percent, not "about 10 percent".
- Wang: the 40-observation "0 regressions" came from a 10-case subset and left out the top-1 drop.
- Echterhoff: the 40 to 52 percent range is two Llama-2 rows; GPT-4 changed 17.5 percent; no ground truth.
- Handler: false action is for no-correct-option items only; DeepSeek R1 dropped 25 points in the table (text says 24).
- Bedi: use the table's model order.
- Ke: initial 0 percent is by case selection, so 71.3 percent is not evidence that the multi-agent form beats one agent.
- McDuff / Goh / Braitsch / Handler: multiple lines are one source each.

---

## 6. Language models

### 6.1 Breadth

- **Lists contain the answer more often than the top item.** o1-preview: correct in differential 78.3 percent, first suggestion 52 percent on NEJM CPCs (c09). GPT-4 earlier: 64 percent in differential, 39 percent top, denominator unresolved (c10). Breadth is not the weak step in these tasks. Ranking is.
- **Differential reasoning is the weakest scored component.** Braitsch: 43.6 percent against 66.6 percent for diagnosis (gap 23.0) across all 32 models (c03). Scored by an LLM judge checked against one haematologist.
- **Independent samples repeat.** Differential diagnosis, 302 NEJM cases: only +0.131 recall from 1 to 5 draws (d01). Program induction: 7.89 unique at K=32 (d03). Enumerated hypothesis spaces: duplicates are the main failure; validity stays high, uniqueness and recovery fall as the valid set grows; reasoning models do better but do not remove the collapse (d04).
- **Choice of configuration matters.** Picking by single-draw quality gave 13.8 percent coverage regret and no overlap with the true top 5 (d01).
- **Spontaneous list length is unmeasured.** No study varies requested N for a prompted model. A trained 7B model lists 7 to 10 when length is free (d15). A prompted study capped lists at 7 (d01). Nothing shows a human-like plateau at 3 to 5, and nothing rules it out.

### 6.2 Commitment

- Handler 2026: 70 percent false action baseline (n=500 / 490); about 48 percent with a safety prompt; model range 55 to 82 percent (c01). Claude Opus 4.7 highest on MedQA (81 to 65). Grok 3 fell 75 to 29 but lost accuracy on intact items.
- Bedi 2025: NOTA drops 8.8 to 38.2 points (d06).
- HealthBench: under-specified low-risk 73.2 to 96.1 percent premature closure (c02).
- Agent runs: requests per round 7.5, 4.2, 1.8 (c03). Utilisation correlates with accuracy (R=0.69) while fluent reasoning does not (91 percent of traces above threshold, decorrelated from accuracy).

### 6.3 Anchoring

- Round 1 to round 3: wrong stays wrong 65.6 percent; right turns wrong 50.8 percent (c04). Recovery varies from 100 percent (6 of 6) to 7.1 percent (1 of 14) by model.
- Chief-complaint turns control the label at every checkpoint; later turns do not (d12).
- Prompt-borne hints shift answers (162 comparisons, 11 exceptions, c14; BiasMedQA drops 10 to 26 percent, b27). Bigger models help a little and then flatten (c15).
- RCA: agents that fix hypotheses up front or commit as soon as they can answer scored 48.2 / 46.6 / 42.6 percent, below others (c18).
- Group chat does not clear the model's own prior (c23; weak link, numbers approximate).

### 6.4 What changed behaviour, by how much

| Change | Effect | Model note |
|---|---|---|
| Safety prompt allowing abstention | false action about 70% to about 48% | five frontier models; Grok 3 loses intact accuracy [c01] |
| Expert-framed wrong nudge | -1.6 to -19.8 points vs -0.3 to -7.5 | six models [d07] |
| System-prompt defense (RBED) | GPT-4o +51.29 points; Llama-8B +6.45 points | [d08] |
| Counterexample prompting | discovery 42% to 56% | 11 models [d10] |
| Differential-first prompt | GPT-4 +2.2 (ns); GPT-3.5 -8 | 2023 [d05] |
| Self-debias rewrite | change rate 5.2% to 52.1% | no ground truth [d09] |
| Chained "something different" | coverage -7.9% mean | differential diagnosis [d02] |
| Concept-first | +4.5 / +5.0 points | program induction [d03] |
| Hypothesis ledger | retention 6/10 to 10/10 (access 8/10); top-1 60 to 40 | one model, 10 cases [d11] |
| DiagGuard wrapper | +9.0 points on 400 incidents; median +10.5 over 12 configs | RCA [c19] |
| Multi-role (MAI-DxO) | 81.9% vs 78.6% (o3 alone) | no same-token control, no per-role ablation [c06] |
| Debate at matched compute | +1.3 to +2.7 points | MMLU-Pro [d14] |
| Commitment prompt | variability -28% vs filler; accuracy unchanged | HotpotQA near ceiling [c17] |

### 6.5 Cautions for reading the LLM data

- Most is 2026 preprints with new models. Not peer reviewed.
- Most LLM scoring uses LLM judges.
- MedQA no-correct-option items are artificial; the real fault task never gives a closed option list.
- Medical bias dominates. Engineering, software and mechanical fault diagnosis are thin (Lu RCA, FVDebug).
- Almost nothing measures the breadth an LLM generates per cue set against tokens.
- No source tests a Soar-like or schema-like external ledger at equal tokens.

---

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Status: [E] established (two or more independent sources, per claims.jsonl), [S] single source, [C] contested.

### Add now (established)

Only items that are both [E] and consistent with existing guardrails go here. Most of these are code rules, not new states.

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Code holds the candidate list.** The model proposes; code stores, dedupes, scores and decides. The model is never asked to remember what is on the list. | G (section 1 rule), S3, S4 | [E] (supported by the 3-to-5 count, the completeness illusion and the 1985 aid design) | a01, a08, a17, a20, a27, d18; K01 |
| A2 | **Keep a reserved "none of these" slot that code checks.** Every probability table over exclusive candidates includes "other". Code normalises to 100. Flag a raw sum far over 100. A closed list is never assumed complete. | G5 (code normalises), S4, S7 | [E] | a03, a05, a06, b03, c01, d06; K03, K10, K23 |
| A3 | **Put the NOTA check in S4/S8.** Before the answer is accepted, test the case "the true cause is not among the live candidates", as an explicit branch in the check (not as a prompt asking the model to feel unsure). | S4, S8 | [E] that models under-use NOTA (c01, d06); the form of the check is [S] | c01, d06, b25 |
| A4 | **Keep removed candidates in a log with a located reason.** Nothing is deleted. A removed candidate can return if its reason proves wrong. | memory, G2 | [E] for the failure (silent loss, c05/d11 plus the human purge a19); [S] for the exact ledger | a04, a19, c05, d11, c20 |
| A5 | **No test is picked with fewer than two live candidates.** The model writes a test; code runs it and checks that it separates at least two live candidates. | S4, S7 | [E] for the direction (one hypothesis forces confirming tests; LLMs confirm); the code gate is design | a17, b06, d10 |
| A6 | **Treat a supplied hypothesis as one candidate, never as a premise.** Strip author and status. Mark source. Test it like the rest. Do not show the model its own first guess in the check step. | G5, S1 input hygiene | [E] (accepting wrong supplied options is measured in two sources) | c12, d07, c24 (snippet), a10 |
| A7 | **Do not rely on "be careful about bias" or "consider what else".** Use structural steps. | 4b (confirms existing row) | [E] | b21, c13, c14, a06, d09 |
| A8 | **Independent re-sampling widens slowly; do not budget on it for breadth.** Expect about +0.13 reference recall from 1 to 5 draws and 7.89 unique from 32. Run draws with facts permuted and judge union by cause key. | S3, G4, G12 | [E] | d01, d03, d04; K20 |
| A9 | **Track information requests per round and distinct live candidates as run metrics.** Fluent reasoning is not a signal. Utilisation is (R=0.69). | log (section 6) | [E] for the fact; the log fields are design | c03, a23 |
| A10 | **Report top-1 and top-k separately in every log.** The list contains the answer more often than the first item; ranking is the weak step. | log, S7 | [E] | c09, c03, d11 |
| A11 | **Let evidence move the leader.** Do not fix hypotheses up front and test only the leader. Keep a live list. | S4/S5, G1 | [E] direction (RCA designs that commit early lose); [S] for the size | c18, a09, a16 |

### Test first (single-source or contested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Forced "what is not on this list" step** (an explicit question whose answer code checks against an untried-axis taxonomy) vs free-form lists, at equal tokens. | S3, S4, G | [S] direction; the bare exclusion prompt was negative (d02) | d02, d06, c01; K21, K23 |
| T2 | **Concept-first generation** (name K distinct concepts, then one hypothesis each). | S3 | [S], program induction only | d03; K21 |
| T3 | **Requested list size N (3, 6, 12).** Does coverage rise, or only cost? Does the model plateau? | S3 | untested [S] | d15; K29 |
| T4 | **Ledger with removal reasons vs from-scratch re-rank vs free update** in staged disclosure. Score retention and top-1 together. | memory, S5 | [S] | c05, d11; K18, K11 |
| T5 | **Forced refute-the-leader step** (write and run the test most likely to falsify the leader) vs counterexample instruction. | S7, O | [S] | d10; K25 |
| T6 | **Probability floor for "other"** scaled by class familiarity. | G5, S0 | [S] mechanism, untested in models | a15; K03 |
| T7 | **Partition-averaging** of candidate lists (coarse vs fine) to cancel the splitting effect. | S1/S2 | [S] human only | a07, b04; K04 |
| T8 | **Fact-order permutation across independent draws** then union. | S3 | [S] human order effect; no LLM test | a12, a18, a19; K06 |
| T9 | **Wrong and right supplied hypothesis in an agentic fault task**: count information requests and switches; add a forced refute-the-leader step. | S1, S4 | [S] | a10, d07, d08; K07, K24 |
| T10 | **Challenger scaffold vs same-token self-consistency** on faults. Keep the hypothesis tracker and falsification step if they win; drop persona wording. | O, G9 | [C] | a24, c06, d13, d14; K13, K26 |
| T11 | **Convergence monitor** (early overlap across runs) as a trigger for widening. | G1 trigger | [S] | c17, c18; K16 |
| T12 | **Evidence-gated change rule** (switch only on a named new observation) vs "be careful about bias". | G1, G2 | [S] | d09, d08; K27 |
| T13 | **Differential-first instruction on current models and a weak model.** | S1 | [S] | d05; K22 |
| T14 | **Mark-not-drop vs drop for low-confidence hypotheses** (FVDebug). | memory | [S], no ablation | c20; K17 |
| T15 | **Convergence of a wrapper that profiles the search space** (DiagGuard "Grounder") at equal tokens on our fault set. | S2/S3 | [S] | c19; K16 |

Items that should NOT be added on current evidence:

- Debate or persona roles as such (G9 holds; d13).
- A "slow down" rule (b16: correct diagnoses were faster; K19).
- A fixed hypothesis-count target taken from humans (the 3-to-5 range may be an effort artifact; b12 numbers unverified).
- A rule to include a supplied list early on the strength of the 2015-2017 Kostopoulou results (a22); the 2022 follow-up failed to find the mechanism (a10).

---

## 8. Concrete tests on our bench

General rules for all tests (from G7 and section 8 of SCHEMA.md): both arms get the same total token budget, including setup and any ledger overhead. Report mean and spread over at least 5 seeds. Score true-cause coverage (is the true cause ever in the live list), top-1 and top-3 separately. Log the information requests and the switches per item. Test one weak and one strong model where cost allows, because instruction effects flip with model strength.

Item types needed. We need fault items with a known true cause and a cause space we can enumerate. Three sources:

- **Synthetic fault items**: a small simulated device or service with a known fault list, a symptom generator and a test oracle. Cause space is known, so true-cause coverage is exact.
- **Closed-option items**: existing multiple-choice items with the correct option replaced by "none of the above" (Bedi style) for the NOTA tests.
- **Staged disclosure items**: the same fault case released in three or four stages; some where the first stage points to a wrong cause.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| **B1 Ledger plus forced NOTA step** (U1) | synthetic faults where the true cause is deliberately absent from the first draw; plus NOTA multiple-choice | (a) free list; (b) list plus forced "is the true cause missing" step against an untried-axis taxonomy; (c) list plus independent re-sampling | true-cause coverage; false-commit rate on absent-cause items; top-1 | (b) beats (a) on false-commit rate by 10 or more points. Based on 70 percent baseline false action (c01) and about 20-point gain from a prompt. Risk: d02 suggests (c) may beat bare exclusion |
| **B2 Breadth curve** (U2) | 40 synthetic faults with known cause set | K independent draws, K = 1, 2, 4, 8, 16, with facts permuted vs fixed order | cumulative distinct causes by cause key; fit N and S as in Mehle | permuted order gives higher S than fixed; curve flatter than Mehle's (S below .179). Expected from d01/d03 |
| **B3 List size N** (U3) | same 40 items | request N = 3, 6, 12; same total tokens (fewer draws at larger N) | coverage, top-1, tokens | coverage rises from N=3 to 6 and flattens at 12; top-1 flat or lower. From d15 |
| **B4 Concept-first** (U4) | same items | independent draws vs chained exclusion vs concept-first, equal K and tokens | true-cause coverage, not surface novelty | concept-first +3 points or more over independent; chained is below independent (d02) |
| **B5 Staged anchoring** (U5) | 3-stage disclosures where stage 1 is misleading in half the items | (a) free update; (b) ledger with removal reasons; (c) from-scratch re-rank each stage | retention of best-seen, top-1 at the end, recovery rate | (c) or (b) raises recovery above Braitsch's 34.4 percent. (b) retains best-seen, but may cost top-1 (Wang: 60 to 40) |
| **B6 Supplied hypothesis** (U6) | agentic faults with information requests; three conditions | no supplied hypothesis; wrong supplied hypothesis; right supplied hypothesis; each with and without forced refute-the-leader | information requests; switches; final accuracy | wrong supplied lowers requests and switches; forced refute-the-leader removes most of it |
| **B7 Refute-the-leader vs instruction** (U7) | rule-discovery items and fault items | counterexample instruction vs forced refute-the-leader step with code-run test | disconfirming-test ratio, success | structure beats instruction by 5 or more points on weak models |
| **B8 Challenger vs self-consistency** (U8) | fault set | one agent with SC at N tokens; hypothesis-tracker plus challenger at N tokens | coverage, top-1 | difference within 3 points (per d13/d14); if the challenger wins, ablate tracker vs challenger vs personas |
| **B9 "Other" floor** (U9) | fault items with trees; pruned vs full list | model free probabilities vs code floor (0.15, 0.30) scaled by unfamiliarity | "other" mass on pruned lists; calibration against absent-cause rate | a floor lifts "other" mass toward the true share; check whether it hurts top-1 |
| **B10 Partition averaging** (U10) | same hypothesis space presented as coarse and fine | single partition vs averaged over 3 partitions | shift in judged share between partitions; top-1 | shift falls by half; top-1 unchanged |
| **B11 Differential-first on current models** (U11) | MedQA-like plus fault items | CoT vs differential-first; weak and strong model | accuracy | strong: within 2 points; weak: lower (d05) |
| **B12 Convergence monitor** (U12) | fault set, K=3 runs | fixed budget vs budget that widens on high early overlap | coverage at equal tokens | widens only on genuine collapse; gain is small |

Log fields to add for these tests: candidate count per stage; distinct cause keys across draws; probability mass on "other"; information requests per stage; best-seen vs final; supplied-hypothesis source flag; switch events with the cited observation.

---

## 9. What does not transfer, and why

- **The memory-span limit itself.** The model has no 4-slot buffer. It can list fifty. The human count of 3 to 5 does not describe model capacity (a08: even physicians could list more). What transfers is the uses of the list (judgment and test choice), not the count.
- **Typing effort.** Mehle's subjects typed. A model's cost is tokens. The relevant cost for us is budget (G12), not effort.
- **Expertise effects.** Experts did not list more (Mehle) and were no better at spotting omissions (Fischhoff Exp 6). Scaling a model does not map to expertise. Anchoring resistance flattens past about 32B (c15) but this is not a skill effect.
- **Student samples and artificial ecologies.** Most HyGene results use learned stimuli (menus, artificial diseases); the encoding-load prediction failed (a11). Real expertise does not enter.
- **Order effects.** Recency vs primacy depends on presentation pace (a18). A model reads the whole prompt at once. Position effects in prompts exist, but pace does not.
- **Bias induction in vignettes.** Availability-bias induction failed to replicate in humans (b16), and the LLM bias tests inject framing into the prompt (b27, c14). That is not the same as a model forming its own early hypothesis. The autoregression mechanism (b30) is untested.
- **Medical content.** Most LLM evidence is medical, with closed options, vignettes, simulated stages and LLM judges. The fault item in our bench has an oracle test and no closed options.
- **Physical and organisational parts of troubleshooting.** Dials, parts access, plant downtime, intermittent faults, hands-on skill, and stakeholder norms are outside the scope (see SUBFIELDS.md "Does not transfer").
- **Human-AI interaction results (Goh, McDuff, automation bias).** They concern whether a person uses a list. Our agent uses its own list through code. Only the lesson that a list shown as text is not used transfers: make the list drive the next test.
- **Rasmussen skill-rule-knowledge.** The sources we opened give no hypothesis count (d16 to d19). Nothing transfers from them beyond "change method after a routine fails" and "display hypotheses to offload memory".
- **Training-based fixes.** The pathology 7B RL result (d15) and Med-Stress fine-tuning (d08) are training results. We do not train.

---

## 10. Open questions

1. At equal tokens, does an external ledger with a forced "what is not on this list" step beat free-form lists on absent-cause tasks and on true-cause coverage? The nearest test (chained draws) was negative (d02). No direct test.
2. How many hypotheses does a prompted model list per cue set? Is there a plateau? Does asking for N change accuracy or only cost? No prompted study varies N.
3. What is the pooled-sample curve for a model on real fault cause spaces, against a pooled-people baseline like Mehle's? Three sources show sublinear growth on other tasks.
4. Does a supplied hypothesis (wrong or right) make an LLM seek less information and switch less? Acceptance of a wrong option is measured. Information seeking is not.
5. Which structural step removes the supplied-hypothesis effect, and does it beat an instruction? No head-to-head.
6. Does a from-scratch re-rank each stage cure early-evidence anchoring, or does a best-seen ledger? Wang has the ledger only, with a top-1 loss.
7. Does the 3-to-5 count depend on output cost or response format? No study varies cost.
8. Do multi-role scaffolds beat one agent at equal tokens on diagnosis? No matched control exists. On general reasoning gains are 1.3 to 2.7 points.
9. Do the Savage 2023 prompt results hold for current models and non-medical faults?
10. What did Rasmussen (1981 to 1986) and Morris and Rouse (1985) find about hypothesis generation and discarding, and with what numbers? Full texts not opened.
11. Are there mechanical, electronic or software fault studies of hypothesis count with real expertise? Mehle's car study is the only one; the E09 software debugging study (about two hypotheses per defect, cross-linked in SUBFIELDS.md) was not re-read here.
12. Is the human tendency to purge without re-cueing (a19) mirrored in models? Does a failed test trigger new candidate generation in an unscaffolded model?
13. Is Braitsch's anchoring at the level of diagnostic resolution (disease family) a different failure from fixing on a wrong specific disease? Does going finer matter?
14. Does the 3.7 percent Sprenger effect matter at all in practice, or is it a laboratory artefact?
15. Does thinking mode help or hurt breadth? Mixed data: reasoning models lose least on NOTA (d06) but are more vulnerable to expert nudges (d07) and do not test more disconfirming cases (d10).

Links to parallel subfields (not covered here): Probing and measurement selection (test choice with two or more live candidates); Troubleshooting search strategies (topographic vs symptomatic search); Hypotheses in debugging and LLM debugging (E09 count of about two hypotheses per defect); Anomaly handling and fixation (fixation after a routine fails); Consistency-based diagnosis and conflict generation (formal candidate sets); Data-frame theory and frame activities (first frame steers cue use); Progress monitoring theory and Adaptive stopping and metareasoning (when to stop widening); Verification design (the NOTA and soundness checks); Soar impasses and Soar chunking (impasse-driven candidate generation, learning from impasses).

---

## 11. Sources

[V] = opened and read this session (full text or abstract page as noted); [M] = search snippet or secondary summary only.

**Human studies and reviews**

- [V] Mehle (1980) Hypothesis generation in an automobile malfunction inference task, PhD dissertation, Univ. of Oklahoma. https://shareok.org/handle/11244/4727 (a01-a04, a13, a14; b10 was the abstract only)
- [V] Fischhoff, Slovic, Lichtenstein (1978) Fault trees. J Exp Psychol HPP 4(2):330-344. https://www.gwern.net/doc/statistics/prediction/1978-fischhoff.pdf (a05-a07, a15, b01-b04)
- [V] Elstein (2009) Thinking about diagnostic thinking: a 30-year perspective. https://www.cebm.net/wp-content/uploads/sites/4/2013/06/arthur-s-elstein.pdf (a08, a16)
- [V] Elstein and Schwarz (2002) Clinical problem solving and diagnostic decision making. BMJ 324:729-732. https://www.bumc.bu.edu/facdev-medicine/files/2010/06/CPS-BMJ.pdf (a09)
- [V] Kourtidis, Nurek, Delaney, Kostopoulou (2022) Influences of early diagnostic suggestions on clinical reasoning. https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-022-00453-y (a10, a22; abstract re-checked in cross-check)
- [V] Sprenger et al. (2011) Implications of cognitive load for hypothesis generation and probability judgment. Front Psychol 2:129. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2011.00129/full (a11, a21, b07, b08)
- [V] Lange, Thomas, Davelaar (2012) Temporal dynamics of hypothesis generation. https://pmc.ncbi.nlm.nih.gov/articles/PMC3386498 (a12)
- [V] Thomas, Dougherty, Buttaccio (2014) Memory constraints on hypothesis generation and decision making. https://shareok.org/handle/11244/25198 and https://doi.org/10.1177/0963721414534853 (a17, a18, b05, b06)
- [V] Lange (2011) Hypothesis generation: temporal dynamics, PhD dissertation. https://shareok.org/handle/11244/319365 (a19)
- [V] Mehlhorn, Taatgen, Lebiere, Krems (2011) Memory activation and the availability of explanations in sequential diagnostic reasoning. https://doi.org/10.1037/a0023920 (a20)
- [V] Staal et al. (2021) Time to diagnose and diagnostic accuracy among residents. https://doi.org/10.1186/s12909-021-02671-2 (b16; abstract level)
- [V] Berner, Jackson, Algina (1996) Performance scores of four diagnostic decision support systems. https://pmc.ncbi.nlm.nih.gov/articles/PMC116302/ (c21; abstract level)
- [V] Rasmussen and Jensen (1974) Mental procedures in real-life tasks. https://orbit.dtu.dk/en/publications/mental-procedures-in-real-life-tasks-a-case-of-electronic-trouble/ (d16; abstract only)
- [V] Morris and Rouse (1985) Review and evaluation of empirical research in troubleshooting. https://doi.org/10.1177/001872088502700502 (d17; abstract only)
- [V] Rouse et al. (1985) NASA grant NAG 2-123 progress report. https://ntrs.nasa.gov/api/citations/19860021746/downloads/19860021746.pdf (d18)
- [V] Venkatasubramanian et al. (2003) Process fault detection and diagnosis, part II. https://www.ece.lsu.edu/mcu/lawss/add_materials/FaultDetectionPart2.pdf (d19)
- [M] Weber, Boeckenholt, Hilton, Wallace (1993) Determinants of diagnostic hypothesis generation. https://doi.org/10.1037//0278-7393.19.5.1151 (a25, b13)
- [M] Graber, Franklin, Gordon (2005) Diagnostic error in internal medicine. https://doi.org/10.1001/archinte.165.13.1493 (a26)
- [M] Rouse (1978) Human problem solving performance in a fault diagnosis task. https://ntrs.nasa.gov/citations/19780048764 (a27)
- [M] Barrows et al. (1982) Clinical reasoning of randomly selected physicians. https://experts.mcmaster.ca/scholarly-works/837888 (a28)
- [M] Sprafka (1973) dissertation record. https://d.lib.msu.edu/etd/41739 (a29)
- [M] Dougherty and Hunter (2003) Hypothesis generation, probability judgment, and working memory. https://api.openalex.org/works?search=Dougherty+Hunter+hypothesis+generation+working+memory+capacity (b09)
- [M] Mehle, Gettys, Fisher et al. (1980) DTIC final report. https://apps.dtic.mil/sti/pdfs/ADA091681.pdf (b11; 403)
- [M] Elstein, Shulman, Sprafka (1978) Medical Problem Solving, via snippets. https://oeaw.ac.at/resources/Record/9780674189089 (b12)
- [M] Kostopoulou et al. (2016) First impressions. https://doi.org/10.1177/0272989x16644563 (b14)
- [M] Mamede et al. (2010) JAMA 304:1198. https://doi.org/10.1001/jama.2010.1276 (b15)
- [M] Mamede et al. (2020) Immunising physicians. https://doi.org/10.1136/bmjqs-2019-010079 (b17)
- [M] Reflective strategies meta-analysis (2019). https://doi.org/10.1080/0142159x.2018.1497786 (b18)
- [M] Cognitive reasoning tools meta-analysis (2022). https://doi.org/10.1136/bmjqs-2022-014865 (b19)
- [M] Norman et al. (2017) Causes of errors in clinical reasoning. https://pubmed.ncbi.nlm.nih.gov/27782919/ (b20)
- [M] Sherbino et al. (2014) Cognitive forcing strategies. https://pubmed.ncbi.nlm.nih.gov/24423999/ (b21)
- [M] Miller, Pople, Myers (1982) INTERNIST-1. https://www.neonatology.net/biblio/bib214.html (c22)

**Language-model studies**

- [V] Handler, Bedi, Shah (2026) Quantifying and mitigating premature closure in frontier LLMs. https://arxiv.org/abs/2605.15000 (c01, c02, b25, b26; re-opened in cross-check)
- [V] Braitsch et al. (2026) Information-seeking failures of LLMs in agentic clinical reasoning. https://arxiv.org/abs/2607.10275 (a23, c03, c04; b31 was abstract only; re-opened in cross-check)
- [V] Bedi et al. (2025) Fidelity of medical reasoning in LLMs. https://pmc.ncbi.nlm.nih.gov/articles/PMC12334947/ (d06)
- [V] Goh et al. (2024) LLM influence on diagnostic reasoning, randomized trial. https://www.medrxiv.org/content/medrxiv/early/2024/03/14/2024.03.12.24303785.full.pdf and https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395 (b22, c07)
- [V] Ke et al. (2024) Multi-agent conversations to mitigate cognitive bias. https://arxiv.org/pdf/2401.14589 (b24; a24 flagged unopened, b24 opened)
- [V] Nori et al. (2025) Sequential diagnosis with language models. https://arxiv.org/abs/2506.22405 (c06; through a summariser)
- [V] Brodeur et al. (2024) Superhuman performance of an LLM on physician reasoning tasks. https://arxiv.org/abs/2412.10849 (c09)
- [V] Savage et al. (2024) Diagnostic reasoning prompts. https://arxiv.org/abs/2308.06834 (c11, d05)
- [V] Schmidgall et al. (2024) Cognitive biases in medical LMs. https://doi.org/10.1038/s41746-024-01283-6 and https://arxiv.org/abs/2402.08113 (b27, b28, c12)
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811 and https://arxiv.org/html/2403.00811v3 (b29, c13, d09)
- [V] Mahajan et al. (2025) Cognitive bias in clinical LLMs. https://doi.org/10.1038/s41746-025-01790-0 (b30; commentary)
- [V] Lou and Sun (2024) Anchoring bias in LLMs. https://arxiv.org/abs/2412.06593 (c14)
- [V] Knipper et al. (2025) The bias is in the details. https://arxiv.org/abs/2509.22856 (c15)
- [V] Jones and Steinhardt (2022) Capturing failures of LLMs via human cognitive biases. https://arxiv.org/abs/2202.12299 (c16; abstract only)
- [V] Mehta and Datta (2026) When agents commit too soon. https://arxiv.org/abs/2606.22936 (c17)
- [V] Lu et al. (2026) Beyond fault localization: microservice root cause analysis. https://arxiv.org/abs/2608.21310 (c18, c19)
- [V] Bai et al. (2025) FVDebug. https://arxiv.org/abs/2510.15906 (c20)
- [V] Pokharel and Dantu (2026) Hidden anchors in multi-agent LLM deliberation. https://arxiv.org/abs/2606.19494 (c23; numbers approximate)
- [V] Wang (2026) Measuring the unmeasurable. https://www.medrxiv.org/content/10.64898/2026.03.27.26349583v2.full-text (c05, d11; first 100k characters)
- [V] Le Bronnec and Yokota (2026) VTC-Bench. https://arxiv.org/pdf/2608.24228 (d01, d02)
- [V] Lee et al. (2025) Generating diverse hypotheses for inductive reasoning. https://arxiv.org/pdf/2412.13422 (d03)
- [V] Chen et al. (2026) HypoSpace. https://arxiv.org/html/2510.15614v1 (d04; per-cell numbers not extracted)
- [V] Christophe et al. (2026) Overalignment in frontier LLMs (M42). https://arxiv.org/html/2601.18334v1 (d07)
- [V] Xiao et al. (2026) Med-Stress. https://arxiv.org/html/2605.23932 (d08)
- [V] Jhaveri et al. (2026) Failing to falsify. https://arxiv.org/pdf/2604.02485 (d10)
- [V] LLMs anchor on chief complaint in sequential clinical triage (2026). https://arxiv.org/html/2609.22904 (d12)
- [V] Zhang et al. (2025) If multi-agent debate is the answer, what is the question? https://arxiv.org/abs/2502.08788v2 (d13; abstract only)
- [V] Multi-agent reasoning improves compute efficiency (2026). https://arxiv.org/html/2605.01566 (d14)
- [V] Pathology evidence-seeking RL paper (2026). https://arxiv.org/html/2607.02983 (d15; title not recorded)
- [M] McDuff et al. (2023/2025) Towards accurate differential diagnosis with LLMs. https://arxiv.org/abs/2312.00164 and https://doi.org/10.1038/s41586-025-08869-4 (b23, c08; abstract through summariser; one study)
- [M] Kanjee, Crowe, Rodman (2023) JAMA. https://jamanetwork.com/journals/jama/article-abstract/2806457 (c10; denominator unresolved)
- [M] A mechanistic view of authority hierarchy in LLM sycophancy (2026). https://arxiv.org/abs/2607.00415 (c24; snippet figures not verified)
- [M] Randomized trial of physician automation bias with erroneous ChatGPT-4o suggestions (2026). https://clinicaltrials.gov/study/NCT07328815 (c25; snippet; attribution of results uncertain)
