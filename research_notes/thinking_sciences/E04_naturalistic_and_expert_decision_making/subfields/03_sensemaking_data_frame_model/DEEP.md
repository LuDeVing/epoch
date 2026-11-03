# Sensemaking, data-frame model: deep document

*Subfield E04.03. Written 2026-11-03 from evidence_a-d.jsonl (a01-a27, b01-b28, c01-c28, d01-d22), claims.jsonl (K01-K30) and critique.md in this folder. No new searching. Read this first: the two founding texts (Klein, Moon, Hoffman 2006; Klein, Phillips, Rall, Peluso 2007) were never opened. Every "Klein says" line is secondhand, mostly via Pontis and Blandford 2015. No LLM study tests the theory directly. All LLM evidence is analogous (anchoring, fixation, belief revision), and much of it is 2026 preprint evidence in medical multiple choice.*

Links to sibling subfields (not covered here): RPD and mental simulation (E04.01), conditions for valid intuition (E04.05), analyst sensemaking, ACH, premature agreement, pruning, abductive diagnosis, insight, Gestalt roots and fixation, belief revision and Dutch book work. Where they overlap, this file only notes the link.

---

## 1. What it is

**The data-frame theory of sensemaking** says people make sense of a situation by fitting data into a frame and fitting a frame around the data. Neither comes first. (a01, a02, a15)

Terms, as Klein uses them:
- **Data**: signals of events in the world. Not raw facts: what a person notices already depends on the frame.
- **Frame**: an explanatory structure that accounts for the data and guides the search for more data. It can be a story, a map, a script or a plan. (a02)
- **Anchors**: the few data points that hold a frame in place. (a09)
- **Elaboration**: adding detail to a frame as more data fit.
- **Conceptual strain / inconsistency**: data that do not sit well in the frame.
- **Frame fixation**: staying with one frame too long. (a11)

**The seven activities** (Klein et al. 2007, pp 132-142, as listed by Pontis and Blandford; a08):
1. Mapping data and frame (connect them).
2. Elaborating a frame (add detail, keep going until anomalies appear).
3. Questioning a frame (starts at inconsistency, before one is sure the frame is wrong).
4. Preserving a frame (inconsistencies judged too weak to drop it).
5. Comparing frames.
6. Reframing (replace the frame).
7. Seeking a frame (when none fits).

Claimed limit: a person tracks at most three frames at once (a08, secondhand, no reason given). Claimed expertise effect: experts own more and better frames and narrow to plausible ones fast; the same narrowing is their weakness (a12).

**Why it matters for our agent.** S2 (REPRESENT) writes 1 to 4 candidate rules. O8 (reframe the goal) is the operator that changes the frame. The theory says three things an engineer can use: the frame guides which cues are read; a frame is revised when data strain it, not on a timer; and early frames stick. The LLM evidence in section 6 confirms the stickiness and adds a warning: self-initiated revision hurts unless an outside signal triggers it. That matches G1 and G2.

Status in one line: **widely cited theory (Crossref: 395 citing works for the 2006 paper, a01), weakly tested in humans (one 11-person study), untested directly on LLMs.**

---

## 2. History and theories in depth

### 2.1 What it builds on
The 2006 macrocognitive paper cites 22 works. Resolved ones (a03): Feltovich 1997 (expert flexibility), Klein 1995 (mental simulation), Heuer 1999 (Psychology of Intelligence Analysis), Rudolph 2003 (Into the Big Muddy), Sieck (questioning strategies for a surprise), Cohen 2003 (critical thinking dialogue), Dreyfus 1979, Gentner 1983 (mental models), Klein 1998 (Sources of Power). Five empirical areas the paper reviews (b06, catalogue record only): causal reasoning, commitment to hypotheses, feedback and learning, sensemaking as a skill, confirmation bias.

Intellectual ancestors:
- **Weick (1995)**: sensemaking is driven by plausibility over accuracy, grounded in identity, social. A good story holds elements together "long enough to energize and guide action". Klein's theory is called an extension of Weick (a26).
- **Heuer (1999)** on mind-sets: data are assimilated into existing images, more so when ambiguous. The evidence needed to overturn an early impression exceeds the evidence needed to form it. Heuer draws on Bruner and Potter 1964: viewers who started with a very blurred picture needed a clearer picture to name it, and longer initial blur raised the clarity needed (a13, a14, d19). Heuer gives no sample sizes; the Science abstract has none either.
- **Rival sensemaking models**: Russell et al. 1993 (modelling with schemas); Pirolli and Card 2005 (information-foraging loop plus sensemaking loop for intelligence analysis). Klein differs by the two-way data-frame link and the explicit frame-questioning activities (a25).

### 2.2 Timeline
| Year | Event | Evidence |
|---|---|---|
| 1964 | Bruner and Potter: slow focus from blur delays recognition | d19 (abstract only) |
| 1984 | Lord, Lepper, Preston: "consider the opposite" beat "be fair" for biased assimilation | d20 (abstract only) |
| 1989 | Tolcott, Marvin, Lehner: analysts committing early weight later evidence in favour (recalled, not read) | b28, d21 |
| 1995 | Weick, Sensemaking in Organizations | a26 |
| 1999 | Heuer, Psychology of Intelligence Analysis | a13, a14 |
| 2006 | Klein, Moon, Hoffman, parts 1 and 2 (IEEE Intelligent Systems 21(4), 21(5)) | a01 (record only) |
| 2007 | Klein, Phillips, Rall, Peluso chapter; Sieck et al. FOCUS report (US Army Research Institute) | a27, a10 (neither opened) |
| 2008 | Lehner et al., confirmation bias in complex analyses (MITRE) | b07 (summary only) |
| 2013 | Lebiere et al.: ACT-R model with chunks as data frames, six IARPA tasks | c01 |
| 2015/16 | Pontis and Blandford: first empirical test on a new task type | a04-a07, b01-b04 |
| 2023 | Klein, Jalaeian, Hoffman, Mueller: plausibility transition model (successor) | b05 |
| 2024-26 | Tool papers, formal loop (Zheng 2025), position paper (2026), LLM analogues | section 6 |

### 2.3 The successor: plausibility transition model (2023)
Sensemaking is a story built from state transitions, judged for plausibility, and it stops when the story feels plausible enough (b05). It is built from cases, not experiments: 1,042 articles screened, 22 kept; a 73-case convenience corpus; 23 cases analysed, all by one coder (the senior author). Cases include AF447, USS Vincennes, Waco, AlphaGo, Royal Majesty. Zero experiments, no inter-rater check, two authors work at a firm that sells related training. Treat as a hypothesis generator. It matters here for one idea: **a stop rule based on plausibility, not on a check.** G3 and G10 say the opposite for our agent (stop on a check on unfitted data, not on a story feeling right).

### 2.4 Formalisations
- **Zheng, Miller, Bialkowski, Soyer, Janda (2025)** (a16, b14, c20): evidence extraction E_t from raw information; a retrieval function picks hypothesis set H_t; a scoring function s(E,h) in [0,1]; if the best score is below a threshold tau, extract more evidence, retrieve more hypotheses, or both; stop when some hypothesis has s >= tau; answer h* = argmax over H_T of s(E_T,h) subject to s >= tau. Prototype only (concept bottleneck model on derm7pt with 7 dermoscopy concepts). No user study. It narrows "frame" to "hypothesis".
- **Position paper "From sycophancy to sensemaking" (2026)** (b15): a break between expected and observed is the error signal; revise the premise that broke. Four premise statuses (draft, contested, committed, rejected); three typed breaks (goal break goes to reframe, evidence break to investigate, process break to negotiate). No experiments.
- **Lebiere et al. 2013** (c01): ACT-R model with chunks acting as data frames. On six IARPA ICArUS tasks with two human groups it reproduced four human biases without a bias module: confirmation, anchoring and adjustment, representativeness, probability matching. Anchoring came from blended retrieval (centroid blending); confirmation from regression to the mean. No numbers were recorded in our files.

### 2.5 Competing and neighbouring accounts
- Pirolli and Card: foraging loop plus sensemaking loop (a25; GLOSS and Sensecape build on it, c23).
- Bias view (Heuer; Tolcott; Lord): early commitment and confirmation as errors to be debiased. The LLM literature is split on whether positive tests are simply a flaw (K15, section 5).
- Plausibility view (Weick; Klein 2023): the goal is a story good enough to act on, not a true one.

---

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources agree), **S** single source, **C** contested. Evidence ids refer to the jsonl files.

### 3.1 Human and theory findings
| Finding | Numbers | Source | Status |
|---|---|---|---|
| Data-frame model fits most activities on a new task type; three activities not seen (seeking and inferring new relationships, tracking anomalies, seeking a new frame) | 11 people (6 novices, 5 experts with 10+ years), 4 influence tasks each, 44 task runs; 2 tasks in a familiar field (HCI), 2 in an unfamiliar one (chemistry) | Pontis and Blandford 2015/16 (a04, b01) | S |
| People kept a single frame, not up to three | 44 of 44 task runs used one frame; candidate people were "frame instantiations" | a05, b02 | S |
| Problem recognised and frame built before data search (theory says in parallel) | First action in all analysed chains (E2, E3, N4, N6) | a06 | S |
| Experts use prior knowledge as soft evidence, elaborate more, check source credibility more, discard more; novices want hard evidence and finish shorter journeys | Example task 3: novice N6 6 data points, expert E2 15 data points (two exemplars, no group stats) | a07, b03 | S |
| Authors had to add activities: preselecting candidates, final decision; quality and plausibility checks were frequent explicit steps | Counts not given | b04 | S |
| Early wrong impression persists; more evidence needed to overturn than to form | Ordering only, no N | Heuer 1999 via Bruner and Potter 1964 (a13, a14, d19) | E (direction); numbers missing |
| Considering the opposite beat "be unbiased" | Two experiments, N not in abstract | Lord, Lepper, Preston 1984 (d20) | S |
| Belief perseverance after debriefing | Sphere study: 19 scientists, 18 kept a spurious formula; calculator study: about half kept believing (encyclopedia summary) | b26 | S |
| ACH reduced confirmation bias only for people without intelligence experience; bias was in weighting, not interpretation | No figures read | Lehner et al. 2008 (b07) | C |
| Disinformation exploits plausibility-driven frames; amateurs lack frame repertoire | About 1,000 coded tweets: 5 rumours, 100 per rumour per election year, 2020 and 2022 | Prochaska et al. 2024 (a11) | S (qualitative) |
| Analyst survey: reasoning poorly documented | 48 analysts: 44 left reasoning undocumented, 33 had trouble weighing rival explanations, 32 rarely reviewed past conclusions, 29 restarted when reasoning failed | Huang et al. 2026 (a23, c21) | S (self-report) |

### 3.2 Tools built on the idea (human users; system comparisons, not tests of the theory)
| Finding | Numbers | Source | Status |
|---|---|---|---|
| Narrative Scaffolding: more alternatives, faster insight | Within-subject N=20: alternatives considered 8.75 (SD 3.03) vs 3.25 (SD 1.58), p<0.001; time per insight 2.31 min (SD 0.76) vs 4.62 (SD 1.22), p<0.001; consider-alternatives rating 5.80 vs 3.10; factors explored 7.0 vs 5.3 of 8. Authors say bias reduction is not shown | a23, c21 | S |
| Sensecape: more concepts explored | N=12 within-subject: concepts 68.3 (SD 49.1) vs 22.8 (SD 7.7), t(11)=3.1, p=0.01; hierarchy levels 4.3 vs 2.6, p=0.02; connections 14.3 vs 15.8, p=0.72 | c23 | S |
| GLOSS multi-LLM frame loop on sensor data | 60 objective queries: 87.93% accuracy vs 29.31% for plain RAG (paired t(59)=8.24); consistency 66.19% vs 52.85% (210 queries). Gain mostly from code generation; frame loop not ablated | a21 | S |
| Evidence trees for analysis | Relevant-report F1: clustering 0.65/0.72/0.56 vs augmentation about 0.80/0.80/0.64 on Crescent/Atlantic Storm/Manpad | c19 | S |
| Vital Insight | LLM summary 91.49% correct facts (215 of 235), 2.13% wrong; expert 83.82% (114 of 136), 11.03% wrong. No correctness difference when experts used the tool; 14.7 s slower | a22, c22 | S |

### 3.3 LLM findings (all analogues; none tests the theory directly)
| Finding | Numbers | Source | Status |
|---|---|---|---|
| Blind self-revision lowers accuracy | GPT-3.5 CommonSenseQA 75.8 to 38.1 (call 3) to 41.8 (call 5); GSM8K 75.9/75.1/74.7; HotpotQA 26.0/25.0/25.0. GPT-4 GSM8K 95.5/91.5/89.0; CSQA 82.0/79.5/80.0; HotpotQA 49.0/49.0/43.0. GPT-3.5 kept its GSM8K answer 74.7%. Llama-2 GSM8K 62.0 to 43.5 to 36.5 | Huang et al. 2024 (a19, b09, c07) | E |
| With oracle labels revision helps (so earlier gains came from the oracle) | GPT-3.5 GSM8K 75.9 to 84.3, CSQA 75.8 to 89.7, HotpotQA 26.0 to 29.0; GPT-4 GSM8K 95.5 to 97.5, CSQA 82.0 to 85.5, HotpotQA 49.0 to 59.0 | a18, b08, c08 | E |
| Models cannot find the error but can fix it once located | BIG-Bench Mistake: GPT-4 step-level 52.87% direct, 43.40% CoT, trace-level 39.80%; GPT-3.5-Turbo 10.44-14.78%; backtracking with oracle location +18 to +44 points on originally wrong traces (tracking shuffled objects +43.92) | Tyen et al. 2024 (c09) | E |
| Reflexion works only with a real success signal | ALFWorld 130/134, +22% absolute over 12 trials; HotPotQA +20%; HumanEval 91.0% vs 80.1%; WebShop no significant gain; Rust ablation base 0.60, full 0.68 | Shinn et al. 2023 (c10, c11) | E |
| Revision helps when new evidence arrives | MINT: 1,035 cases, 11 LLMs; over 55.3% of first answers in the first two turns, 18.5% wrong; wrong-to-right up to 10.6x right-to-wrong; deferring the question raises first-commitment accuracy up to 62.6%; question-last beats question-first by 20.1% on average | Fang et al. 2026 (d08) | S |
| Coherent counter-argument flips correct answers | 7 frontier models, 57 MMLU subjects; flip rate 17.5% (Qwen3.5-35B) to 97.3% (Llama-3.1-8B), mean 48.7%, 55.7% if attributed to the model itself; GPT-5.1 23.4%, Llama-3.3-70B 75.8% | Nikeghbal et al. 2026 (d09) | S |
| Multi-turn fixation | 15 LLMs, 8 families, 200,000+ simulated conversations, 6 tasks; average drop 39% (about 90% to 60%); aptitude about -15 to -16%; unreliability +112%; same text concatenated 95.1% of full; best-to-worst run gap about 50 points; reasoning models (o3, R1) degrade as much, answers 33% longer | Laban et al. 2025 (a20, b11, b12, c05) | S (one paper) |
| Evolving intent in code/tool tasks | SWE-Bench Verified, BIRD-SQL (100 samples) and two more; six intent transitions; degradation up to about 30% from single-turn; function switches hardest | Tack et al. 2026 (d17) | S |
| Early ambiguity hardens; clarification does not correct | Gemini 2.5 Pro success full/clarified-first/ambiguous-first 54.2/50.0/42.8; Flash 62.3/55.4/45.7; ambiguous-first by task: writing 69.3% (contamination 0.125), planning 37.5% (0.141), coding 24.4% (0.256) | Lin et al. 2026 (d01) | S |
| Information seeking collapses after first diagnosis | 32 frontier models, 20 hematology cases; best accuracy 68.1%; information use predicts accuracy R=0.69; data requested 56.8% (R1), 56.7% (R2), 25.7% (R3); of 323 wrong or partial R1 diagnoses 65.6% stayed wrong (34.4% recovery); of 307 correct R1 diagnoses 50.8% became wrong | Braitsch et al. 2026 (c16) | S |
| Reasoning traces commit early | 8 open reasoning models; 1,146 base traces, 1.7 million resampled; 36% commit before halfway, 61% before three quarters; 96.1% put top probability on the diagnosis finally given | NeurIPS 2026 submission (b20) | S |
| Premature closure | 5 frontier models; MedQA n=500 and AfriMed-QA n=490; false-action about 70% (range 55-81%) down to 48% with a safety prompt; Gemini 2.5 Pro 55% to 48% on MedQA; HealthBench 861 questions 20.7-44.6% closure; 191 red-team queries 59.3-91.4% | Handler et al. 2026 (b21, c18) | S |
| Anchoring in LLMs | SynAnchors, 11 models, 100 questions x 30 samples: total anchored ratio Qwen2.5-0.5B 60.5%, Phi-3.5-mini 46.3%, Qwen2.5-7B 40.0%, GPT-4o-mini 37.0%, GPT-4o 27.3%, DeepSeek-R1 25.0%, Qwen3-235B thinking 22.0%. Echterhoff 2024: 13,465 prompts, GPT-4 anchoring distance 0.250, GPT-3.5 0.362. Valencia-Clavijo 2025: robust in Gemma-2B, Phi-2, Llama-2-7B | b16, c13, c14, c15 | E |
| Narrative voice shifts diagnosis | 12 open models (3B-24B), 1,000 MedQA vignettes x 3 voices: 0.635 clinical vs 0.546 and 0.531; pooled penalty -9.6 points; rewrite-then-reason gap 0.047 but broke 19.8% of correct items | b22 | S |
| Wanted conclusion shifts analysis | 14 models, 2,160 responses, 50 hospitals x 60 months; true effect about 1.8-2.2% | Allen and Peterson 2026 (c12) | S |
| Abandoned analysis leaves residue | 24 open models (124M-70B); residue about three quarters of a true-object effect; corrected statement still pulls in 8 of 9 models | b23 | S |
| Weak at updating a conclusion | Belief-R: 1,912 items (1,074 update, 670 maintain). GPT-4 Turbo direct update 16.76%, maintain 86.72%, mean 51.74; Llama-3 70B 10.99/92.09; Claude 3 Sonnet 19.65/82.69. CoT about +1 point. DeltaLogic: Qwen3-1.7B initial 0.667, revision 0.467 | c02, c03, c04 | E |
| Confirming tests | 11 LLMs on 2-4-6 task; counterexample prompts raised rule discovery 42% to 56% | b24 | C (b25 disputes) |
| Written reasoning does not guard the frame | 91.1% of 17-model evaluations scored 6+ on a reasoning rubric (mean 8.22, SD 1.59) while mean accuracy was 56.3% | c17 | S |
| Single-shot fixation on trap tasks | Only Connect walls: GPT-4 10-shot 6 of 494 walls vs 59 with herrings removed vs 471 WordNet; humans about 80%. mARC (about 100 items): physicians 0.66, most LLMs under 50% in early 2025; Claude 4.1 Opus 0.75 by 2026; on 20 physician-miss items the top 5 models 55-70% | d10, d12, d13 | E |
| Einstellung in medical LLMs | MedEinst 5,383 paired cases, 49 diseases, 17 LLMs; GPT-5 errors: key evidence ignored over 35%; of noticed-cue cases 43% underthinking, 22% overthinking | d11 | S |
| Code-held rebuild of the spec closes the multi-turn gap, a model recap does not | AC3 (GPT-5 family): database n=107 reset 75.7% vs full 56.1% (+19.6pp, p=0.0005), condenser 53.3%; code n=100 92.0% vs 83.0% (McNemar p=0.023); condenser flagged an assistant error in 0 of 340 summaries. Mediator rewrite 73.9 vs sharded 53.6, summary 54.7, Mem0 56.5 | d05, d06, d07 | E (4 sources, one lab cluster) |

---

## 4. Mechanisms and models

Written so an engineer could build them. Each is a design reading of the theory plus the LLM evidence. None is validated on our bench.

### 4.1 The data-frame record (S2 state)
Hold a frame as a record, not a paragraph. Fields:
- `frame_text`: one or two sentences, the candidate rule or explanation.
- `anchors`: the 2 to 4 cues that support it (cue ids from the ledger).
- `status`: draft, contested, committed, rejected (b15).
- `strain`: list of cue ids that do not fit, each with a short reason.
- `score`: a number from code (see 4.3), not from the model.

Rule from Klein via Pontis: a cue used as an anchor for frame A should not be reused as the sole anchor for frame B (a09). Implement as a code check that two live frames differ in at least one anchor.

### 4.2 The cue ledger (the part with the best evidence)
A **cue ledger** is a list of facts from the task statement, the examples and the check outputs. Build it in code, from user and tool text only, never from the model's own earlier turns.
- Evidence: AC3 rebuilt the spec from user messages only and reset the context; it closed 55-84% of the gap to an oracle on 3 of 4 tasks (d05). A model-written summary gave no gain: 53.3% vs 56.1% full context, and 0 of 340 summaries flagged an assistant error (d06). A rewrite into explicit instructions gave 73.9 vs 53.6; summaries and Mem0 gave 54.7 and 56.5 (d07). "Pollution is contagious": an analyzer that saw the assistant's reasoning carried the errors forward (d06).
- Use: each new attempt gets the ledger plus the task, in a fresh context (S3 already does fresh contexts). Cues that arrive late are appended; the ledger is never summarised by the model.

### 4.3 Fit scoring in code (Zheng loop, adapted)
```
ledger = extract_cues(task, examples)          # code, or one model call per cue
frames = retrieve_frames(ledger, k)            # model proposes, k small
for f in frames: f.score = fit(f, ledger)       # code: share of cues explained, tests passed
best = argmax(frames, score)
if best.score >= tau: go to S3 with best
else: more cues (ask / run a probe) or new frames
```
The scoring step must be code: running the rule on the examples, counting cues explained. This follows G5 (code selects) and G10 (reasoning text is not evidence). Lin 2026 shows that naive multi-hypothesis prompting makes things worse (contamination 1.029 vs 0.177 for raw history, d02), and HypoSpace shows mode collapse in set generation (d15). So a list of rivals needs forced difference and a scorer.

### 4.4 Questioning versus reframing (when to leave a frame)
Theory: elaboration continues until anomalies force replacement; questioning starts at inconsistency; preserving is a choice (a08). Translation into the schema:
- **Question** (cheap): code detects strain, that is, a failing check, a cue left unexplained, or disagreement between attempts. This is G1's signal.
- **Preserve**: strain below a threshold; keep the frame, log the strain.
- **Reframe (O8)**: strain at or above threshold, or two S5 rounds with no change (S6 impasse). The model is shown the located failing output and asked to restate the goal (G2).
- **Seek a frame**: no frame explains the ledger. Run S6 operators.

The LLM evidence says the trigger must be external. Blind review hurts (Huang). A model-judged conflict is risky: a coherent counter-argument flips right answers 17.5-97.3% of the time (d09). A located failure or a tool-confirmed cue helps (Tyen, Reflexion, MINT).

### 4.5 Fresh context after reframe (residue control)
Abandoned readings leave residue in model outputs (b23: about three quarters of the true-object effect; d01). In Lin's small test an explicit rollback with rebuild from the clarified requirement raised success 17.5% to 27.5% and cut contamination 0.100 to 0.000; a two-phase policy gave 0.0 committed wrong and 0.00 contamination (d03). Implementation: after O8, start a new context from the ledger plus the new goal; do not include the abandoned frame text. Keep the abandoned frame in a code-held "rejected" list, outside the model context, so it is not retried (G4, S3 history).

### 4.6 Hold-and-ask before first commitment
MINT: deferring the diagnostic question raised first-commitment accuracy by up to 62.6% (d08). Lin: "ask first" gave 0.0% committed wrong vs 40.0% direct (d03). Braitsch: models request fewer cues each round, 56.8% to 25.7% (c16). A code step "name the missing cue, fetch it" before first commitment fits tasks where cues can be fetched (tools, examples to run). It must not turn into abstention (G6): the step is bounded to one fetch, then answer.

### 4.7 Input hygiene as frame control (S1)
Narrative voice changes accuracy from the same facts (0.635 vs 0.546/0.531, b22). A planted wanted conclusion shifts analysis (c12). Code moves suggestive material into a marked block (already in S1). The rewrite-to-neutral remedy helped the gap but broke 19.8% of correct items in the medical setting, so its net value is unknown on our tasks.

### 4.8 What ACT-R adds (memory side)
Lebiere 2013: anchoring and confirmation arise from blended retrieval (c01). Reading for engineers: if frames are retrieved by similarity from S9 memory and blended, the retrieved prior frame acts as an anchor. That is why the schema shows lessons after the first attempt (SCHEMA section 5). No LLM measurement of this exists (K21).

---

## 5. What holds up

### 5.1 Established (two or more independent sources)
1. **Self-revision without a signal does not help and often hurts** (K07): Huang 2024, Tyen 2024, Reflexion needing a success signal, MINT showing the contrast when evidence is new.
2. **Models fix located errors better than they find them** (K08): Tyen (+18 to +44 with oracle location), Reflexion (130/134 with signal, none where weak).
3. **Early information anchors LLMs** (K12): SynAnchors, Echterhoff, Valencia-Clavijo. Reasoning models are least anchored (22-25%) but not immune.
4. **LLMs under-update on changed premises** (K16): Belief-R (update 10.99-19.65% for three strong models), DeltaLogic, plus BeliefShift for opinion beliefs (retrieval helps: GPT-4o 0.71 to 0.83).
5. **Single-shot fixation on trap items is partly cured by reasoning models; sequential fixation is not** (K29): mARC 2025 vs 2026, versus Laban, Lin, AC3.
6. **A code-held cue rebuild beats a model recap** (K24): four sources, though one lab cluster uses GPT-5-family respondents.
7. **Early and wrong frames persist** (K04) is established in direction (Heuer, Bruner and Potter, Tolcott, belief perseverance) but the human numbers are missing from our files. Treat as direction only (K30).

### 5.2 Single-source or contested
- Founding structure (seven activities, three-frame limit, anchors): secondhand only (K01).
- Single frame in 44 of 44 tasks (K02): one 11-person study, structure tasks not story tasks. The theory also says frame and data search run together; Pontis saw frame first. Neither side wins.
- Multi-turn drop of 39% (K05): one paper, though AC3, Mediator, Tack and Luo (d18; loss up to 65%) corroborate the direction.
- Premature closure, early commitment in traces, narrative voice, residue after garden-path: single preprints (K10, K11, K13, K14).
- Confirming tests (K15): contested. Failing to Falsify says LLMs test confirming cases and counterexample prompts lift discovery 42% to 56% (b24). Wild Guesses says positive tests are not simply a flaw; information-maximising queries fail when the model proposes invalid programs (b25).
- ACH reduced bias only for non-experts (K22): summary only, contested.
- Plausibility stopping (K19): case-based, one coder.

### 5.3 Failures, null results and warnings
- **Naive listing of K rival frames does not help reliably.** Lin 2026 (d02): Gemini 2.5 Pro success 4.7/10.7/19.1% at K=1/3/5, Flash 22.6/5.8/5.0%. Model dependent, very low success levels, not token matched.
- **Summaries, CoT and a single-state ledger do not cure fixation** (d01): raw history 43.2% success, summary 48.7%, CoT 44.3%, single-state ledger 44.6%; contamination 0.177, 0.228, 0.182, 0.295. 62.5% of summaries collapsed the ambiguity.
- **Common debiasing does not remove anchoring** (b17): Llama-3.1-8B base 34.7%; question-aware 36.8%; knowledge enhancement 50.5%; self-improving 38.4%; adversarial finetuning 33.3%; Anti-DP 24.7%. Qwen2.5-7B: base 40.0%, Anti-DP 40.8%, self-improving 48.0%. In Echterhoff, self-help debiasing worked better than awareness warnings; zero-shot awareness left GPT-4 framing delta at -0.470 (no help); few-shot often broke the model (c15).
- **Commitment prompt** (d04): variability fell 28% vs a token-matched filler (d=0.33) but not vs the plain agent (-15%, p=0.088); accuracy 0.923/0.902/0.908 (n.s.).
- **Agreement across runs is not correctness** (d04); a model can fix an answer before reasoning and keep it at a 4,096-token thinking budget (85-100% wrong; d16, one small model, one item).
- **Low temperature** cut unreliability 50-80% in FULL and CONCAT but about 30% remained (c06).
- **Debate** in Huang: self-consistency 88.2 at 9 responses beat debate (about 83.0) on GSM8K with GPT-3.5 (b10; garbled table, direction only). Matches G9.

### 5.4 Moderators
- Model strength: reasoning models cure single-shot traps (d13) and anchor less (b16), but not multi-turn (b12).
- Task type: coding is the most contaminated family (0.256, d01); medical multiple choice dominates the rest.
- Whether new evidence arrives: decides whether revision helps (d08) or harms (Huang).
- Who supplies the signal: code or tools help; the model's own judgment does not.
- Expertise: human experts hold more frames; the model analogue is a frame library (K03), untested.

### 5.5 Interventions that worked and that did not
| Worked | Size | Did not work | Size |
|---|---|---|---|
| Code-side user-only spec rebuild + reset (d05, d06) | +9 to +19.6pp | Model summary (d06, d07) | -2.8 to +3pp |
| Rewrite to explicit instructions (d07) | 73.9 vs 53.6 | Memory store Mem0 (d07) | 56.5 vs 53.6 |
| Located-error backtracking (c09) | +18 to +44 points | Blind "rethink" (a19) | down to -37.7 points (GPT-3.5 CSQA) |
| Hold-and-ask (d03, d08) | 0.0% committed wrong vs 40.0%; up to +62.6% first-answer accuracy | Listing more hypotheses (d02) | model dependent |
| Counterexample prompt (b24) | 42% to 56% | Awareness warnings (c15) | none |
| Explicit rollback (d03) | contamination 0.100 to 0.000 | Single-state ledger (d01) | contamination 0.295 |
| Alternatives view for human analysts (a23) | 8.75 vs 3.25 alternatives | Safety prompt for closure (b21) | cut about a third, not to zero |

---

## 6. Language models

**No study tests data-frame predictions on an LLM agent directly** (K18; the search was limited, and a24 is the recorded negative result). The evidence is analogous, so each line below says what it actually measures.

### 6.1 Frame fixation across turns
Laban 2025 is the clearest. When the same instructions arrive in pieces instead of at once, 15 LLMs average a 39% drop. Aptitude falls only about 15-16% but unreliability rises 112%: models guess early and build on the guess. CONCAT (same text, one turn) scores 95.1% of full, so information loss is not the cause. o3 and DeepSeek-R1 degrade as much as others (b12). Tack 2026 (d17) finds up to about 30% drop on SWE-Bench and BIRD-SQL conversations with six intent changes. Luo 2026 (d18) reports loss up to 65% on sharded math and a trained rolling memory that helps (needs RL; not usable for us).

What changed it, by how much:
| Fix | Effect | Source |
|---|---|---|
| SNOWBALL (repeat all earlier cues each turn) | "on the order of 15-20%" improvement, GPT-4o and 4o-mini, 4 tasks; the checker notes the wording is ambiguous (share of the drop or points) | c06 |
| RECAP (final recap turn) | more, but unrealistic | b12 |
| Low temperature | unreliability -50 to -80% in FULL/CONCAT, about 30% left | c06 |
| Code-side user-only rebuild + reset (AC3) | closes 55-84% of the gap to oracle on 3 of 4 tasks; +19.6pp database, +9.0pp code on unselected pools | d05, d06 |
| Mediator rewrite | about +20 points performance, +15 reliability; DeepSeek-v3.2-Thinking +21.1 | d07 |
| Model summary / Mem0 | about +1 to +3 | d06, d07 |
| Clarification alone | does not correct: Pro 42.8% ambiguous-first vs 54.2% full; clarified-first 50.0% | d01 |

### 6.2 Anchoring and early commitment
SynAnchors: 22-61% of questions anchored; the best mitigation was reasoning, and the range tracks model size (b16). Echterhoff: GPT-4 anchoring distance 0.250 (c15). Braitsch (c16): on a multi-round diagnosis task, data requests fell from 56.8% to 25.7% and 65.6% of wrong or partial first diagnoses stayed wrong; 50.8% of right ones became wrong. NeurIPS submission: 36% of traces commit before halfway and 96.1% put top probability on the final diagnosis (b20). Handler: premature closure about 70% down to 48% with a safety prompt (b21). Allen and Peterson: telling a model the wanted conclusion shifts its analysis, and the most accurate models under neutral framing shifted most (c12).

### 6.3 Revision, over and under
Both failures exist. Huang: model-driven revision flips right to wrong (GPT-3.5 CSQA 75.8 to 38.1). Nikeghbal: a coherent wrong argument flips a correct answer in a mean 48.7% of cases (d09). Belief-R: models fail to update when they should (update 10.99-19.65%) while keeping conclusions well (maintain 82.69-92.09%) (c02). DeltaLogic: revision accuracy below first-pass (c04). MINT: when new evidence really arrives, wrong-to-right flips run up to 10.6x right-to-wrong (d08). The pattern: **model-initiated revision needs an outside signal; a rule of "revise more" or "revise less" is wrong.**

### 6.4 Residue
24 open models keep traces of abandoned garden-path readings (b23). Dialogue shows contamination that a clarification does not remove (d01). Explicit rollback helped in a tiny test (d03). Activation patching removes most residue in 32B and 70B models (b23), which is not usable for an API agent.

### 6.5 Multiple frames
No usable evidence that holding several frames beats one. Lin (d02) is negative for naive listing. Mini-ARC (d14): six hypotheses Solomonoff-weighted 64% vs Bayesian averaging 48% on one task, with no single-hypothesis baseline. HypoSpace (d15): mode collapse. Narrative Scaffolding (a23) shows more alternatives for humans, not better answers.

### 6.6 Single-shot fixation and reasoning models
mARC: early-2025 LLMs mostly under 50% (physicians 66%, d12); by 2026 Claude 4.1 Opus reached 0.75 (d13). MedEinst: even accurate LLMs follow the common diagnosis when a key cue changes; key evidence was ignored in over 35% of GPT-5 errors. The benchmark authors' agent that forced explicit discriminating checks lifted Qwen3-32B base accuracy 40.25 to 69.49 and robust accuracy 11.86 to 24.21 (trap rate 43.46 to 33.75) (d11).

### 6.7 Human-AI sensemaking tools
Tool results (section 3.2) are for human users. Only GLOSS (a21) reports an LLM-system accuracy gain over a plain RAG baseline, and the authors credit code generation.

### 6.8 Caveats on this whole section
Many items are 2026 preprints without peer review (Braitsch, Handler, early-commitment, narrative anchoring, residue, Lin, AC3, MINT). Several use old models (GPT-3.5/4, Llama-2). Most are medical multiple choice. Nothing was run on ARC-like or program-synthesis tasks, which is where our agent works.

---

## 7. What our agent should take

Status marks follow SCHEMA.md. Evidence ids refer to jsonl lines; K ids to claims.jsonl.

### 7.1 Add now (established)
| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Reframe (O8) only from a located failing output or a tool-confirmed cue conflict; never on the model's own wish to rethink.** G1 and G2 already say this; this makes O8 follow it explicitly. | G1, G2, O8 | [E] | K07, K08; a18, a19, b09, c07, c09, c10, c11, d08 |
| A2 | **Keep the cue ledger in code from user and tool text only; give each fresh attempt the ledger, never a model recap of earlier turns.** Late cues are appended. | S2, S3, G4 | [E] | K24; d05, d06, d07, d01 |
| A3 | **Do not use model summaries, model-written "single-state ledgers" or Mem0-style stores as a fix for fixation.** Add to section 4b. | 4b | [E] | K24; d01, d06, d07 |
| A4 | **Do not use bias-awareness or generic debiasing instructions as the anchoring fix.** (Code-shuffled cue order is a test, not an addition.) | 4b, S1 | [E] | K12; b16, b17, c13, c14, c15 |
| A5 | **Written reasoning, rubric quality or sample agreement is no proof that the frame is right.** Already G10 and G4; add this subfield's numbers as support (91.1% rubric pass vs 56.3% accuracy). | G10, G4 | [E] | K20, K27; c17, d04 |
| A6 | **When a given cue is edited in a solved item, re-run the check instead of letting the old answer stand; add an inertia regression item to the bench.** | O8, S8 | [E] (the failure) | K16; c02, c03, c04 |

### 7.2 Test first (single-source, contested, or human-only)
| # | Item | Schema part | Status | Evidence | UNKNOWNS id (E04.03-U#) |
|---|---|---|---|---|---|
| T1 | Name 2 rival frames with a forced differing cue and a code-side score vs one frame | S2 | [S] | K02, K17, K28; d02, d14, d15, a05 | U1 |
| T2 | Frame record with status (draft, contested, committed, rejected) and anchors vs plain-text rules | S2, memory | [S] | K23; a16, b15 | U10 |
| T3 | Code-forced "name the missing cue and fetch it" before first commitment (one fetch, never abstain) | S2, G6 | [S] | K25, K09; d03, d08, c16 | U4 |
| T4 | O8 trigger: located failure only vs plus cue-conflict detector vs model-judged conflict; measure right-to-wrong flips | O8, G1, G2 | [S] | K26, K07; d09, a19, d08 | U3 |
| T5 | Cue order randomised in code vs fixed | S1, S2 | [E] for the effect, [S] for the fix | K12, K04 | U5 |
| T6 | Neutral restating of input (S1 hygiene) at equal tokens, non-medical | S1 | [S] | K13; b22, c12, d07 | U7 |
| T7 | Plausibility stopping vs check-based stopping | S2, S8, G3 | [C] | K19, K27; b05, d04, d16 | U8 |
| T8 | Frame library from S9 memory: shown after first attempt vs never | memory, S2 | [S] | K03, K21; a07, c01 | U9 |
| T9 | Forced disconfirming test beyond ARC: positive-test lean | S4, S7 | [C] | K15; b24, b25 | U11 |
| T10 | Code-forced "no frame fits" flag at S2 vs G6 never-abstain | S0, S2, G6 | [S] | K11; b21, c18 | U12 |
| T11 | Sequential-cue tasks: cue arrives after commitment | bench design | [E] for the failure | K29, K05; d10-d13 | U2 |

---

## 8. Concrete tests on our bench

All arms at equal total tokens (G7), counting setup cost. Items: our existing ARC and brainteaser suites plus the sequential variants below. Log per item: path, tokens per state, every doubt step and whether it flipped right-to-wrong or wrong-to-right (SCHEMA section 6).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | **Sequential cues.** Split each task statement into 3-5 shards revealed one per turn; a misleading first shard planted in half of the items | (a) full history; (b) model recap; (c) code-held cue ledger rebuild + fresh context; (d) all shards at once (ceiling) | Accuracy; unreliability (best minus worst of 5 runs); share of gap to ceiling closed | (c) closes over half the gap; (b) near zero (d05, d06) |
| B2 | **O8 trigger.** Items with a located failing output (an ARC example fails) and items with a plausible but false "cue conflict" (planted counter-argument) | (a) reframe on located failure only; (b) failure plus model-judged conflict; (c) reframe on request every round | Right-to-wrong flip rate; wrong-to-right rate; final accuracy | (a) lowest flips; (b), (c) higher (d09: mean 48.7% for a coherent wrong argument) |
| B3 | **One frame vs two.** Items whose rule is ambiguous between two readings that differ on a hidden test input | (a) one frame; (b) two unscored frames; (c) two frames forced to differ by one cue + code score + discriminating test (S7) | Accuracy on hidden input; tokens | (c) > (a) on ambiguous items only; (b) not better than (a) (d02) |
| B4 | **Misleading first cue.** Insert a cue consistent with a common wrong rule in first position | (a) fixed order; (b) code-shuffled order across attempts; (c) first cue moved to a marked block (S1) | Rate of the wrong common rule chosen; anchored share | (b) or (c) lower anchoring; size unknown (b16 base rates 22-61%) |
| B5 | **Fresh context after reframe.** Items where attempt 1's frame fails and the right frame differs | (a) abandoned frame text kept in context; (b) new context from ledger + new goal; (c) new context + rejected list held in code | Contamination (share of new attempts reusing the old rule, code-measured); accuracy | (b), (c) lower contamination, small accuracy gain (d03: 0.100 to 0.000) |
| B6 | **Hold-and-ask.** Tasks with fetchable cues (run a test input, show an extra example) | (a) answer first, then revise; (b) one forced "name missing cue and fetch" then answer; (c) unbounded asking | First-answer accuracy; final accuracy; abstain rate (must be 0) | (b) improves first-answer accuracy; (c) risks G6 |
| B7 | **Premise edit.** Take solved items, change one given example, ask for the updated answer | (a) plain; (b) code re-runs check on the changed item then S5; (c) model asked "does the old answer still hold?" | Update accuracy; maintain accuracy (control items with irrelevant edits) | (b) beats (c); (c) shows inertia like Belief-R (update 10-20%) |
| B8 | **Neutral restate.** Same task in three framings (leading hint, authority, neutral) | (a) raw; (b) code moves suggestive text to a marked block; (c) model rewrites into neutral voice | Accuracy gap between framings; share of correct items broken | (b) closes the gap cheaply; (c) breaks correct items (b22: 19.8%) |
| B9 | **Stop rule.** Items with plausible wrong stories | (a) stop when the attempt "looks done"; (b) stop when a check on unfitted data passes; (c) stop when 3 samples agree | Confident-wrong rate; tokens | (b) lowest confident wrong; (c) no better than (a) (d04) |
| B10 | **Frame library.** Problem classes with repeated rules | (a) no library; (b) library shown after first attempt; (c) shown before | First-pass rate; fixation on a library frame when it is wrong | (b) gain without fixation; (c) fixates (c01 blending) |
| B11 | **Disconfirming test.** 2-4-6 style rule-discovery items | (a) model proposes any tests; (b) forced counterexample tests; (c) code-chosen discriminating input | Rule-discovery rate | (b) near the 42% to 56% pattern (b24); (c) at least as good |

Run each on at least 2 model families and with thinking on and off. Report per-item flips, not only means.

---

## 9. What does not transfer, and why

- **The seven activities as seven steps.** They describe human activity, not a procedure. Several (preserving, comparing) are judgments that the schema gives to code. Do not add seven states.
- **Up to three parallel frames.** Never shown in a lab beyond Pontis's null (44 of 44 single frame). Our only LLM evidence on listing frames is negative or model dependent (d02). Samples from one model are not independent (G4).
- **Plausibility as the stop rule.** Weick and Klein 2023 describe how people stop in the field. A model's plausibility sense is the same signal that produces confident wrong answers (c17, d04, d16). G3 and G10 override.
- **Experts' large frame repertoire.** Humans build it over years of feedback. A model has a broad but unranked repertoire. The memory analogue (S9 lessons) is small and shown late.
- **Fast reframing by expert intuition.** The human expert feels strain through tacit pattern recognition. The model's "stuck" signal is unreliable (r = .17 in SCHEMA S6). Strain must be detected by code.
- **Human tool gains (Narrative Scaffolding, Sensecape).** They measure what a person does with a visual tool (more alternatives, faster insight), not answer accuracy. The authors say bias reduction is not shown (a23).
- **Medical LLM results as ARC results.** Braitsch, Handler, MINT, mARC and narrative voice are clinical multiple choice with cues to request. Our tasks have a check and no abstain option. The sign may carry; the size will not.
- **Garden-path residue fixes by activation patching.** Works on open 32B and 70B models only (b23). Not available for an API agent.
- **Trained rolling memory (d18).** Needs RL training. Not allowed.
- **Social frames (disinformation, rumour).** Prochaska's cases (a11) are social and adversarial; our single-agent tasks are not.
- **Field cases under time pressure and stakes** (AF447, Vincennes). Emotionally loaded and high-stakes; no analogue.

---

## 10. Open questions

1. What do the founding papers specify for the seven activities, the frame-count claim and the anchor rule? (Need a legal full text; K01, d22.)
2. Does holding 2 or 3 scored, forced-different frames beat one at equal tokens on ARC-like tasks? Evidence so far is negative for naive listing (d02) and absent otherwise.
3. Best O8 trigger. No study compares triggers on one task; the false-reframe rate per trigger is unknown.
4. Can a disconfirming-cue request be forced without breaking G6? Braitsch's 34.4% recovery is not tested against any fix.
5. Does a code cue ledger cure multi-turn fixation for reasoning models and on tool-result tasks? AC3 did not help tool-result tasks and its math gain is confounded (47% of analyzer outputs; d05).
6. Do the classic human findings (Bruner and Potter, Tolcott, Lord, Lehner) have usable N and effect sizes, and how well do they replicate?
7. Does neutral rewording at equal tokens help on non-medical tasks?
8. Does residue appear in agent traces after O8, and does a fresh context remove it?
9. Is plausibility-based stopping distinguishable from check-based stopping in logs?
10. Is there any 2025-2026 study measuring frame count, switching or anchoring in code or puzzle settings with current reasoning models? Only analogues were found (Only Connect, Mini-ARC, SWE-Bench evolving intent).
11. Why do Pro and Flash move in opposite directions with more hypotheses (d02)? Unexplained.
12. Single-shot fixation is cured by reasoning, sequential is not (K29). Where is the boundary (number of turns, size of the first commitment)?

---

## 11. Sources

[V] opened (page or PDF text read in some session), [M] snippet, record or memory only. Duplicate evidence lines of the same paper are listed once. Where an item was only partly read, it says so.

**Founding and theory**
- [M] Klein, Moon, Hoffman (2006) Making sense of sensemaking 2: a macrocognitive model. IEEE Intell Syst 21(5):88-92. https://doi.org/10.1109/MIS.2006.100 (Crossref record and reference list only; a01, a03, d22)
- [M] Klein, Phillips, Rall, Peluso (2007) A data-frame theory of sensemaking, in Expertise out of context. https://www.researchgate.net/publication/303171216_A_data-frame_theory_of_sensemaking (blocked; a27)
- [M] Sieck, Klein, Peluso et al. (2007) FOCUS: a model of sensemaking, ARI report. https://apps.dtic.mil/sti/pdfs/ADA469770.pdf (blocked; a10)
- [V] Gary Klein, Data-Frame Theory page. https://www.gary-klein.com/data-frame (a02)
- [V] Wikipedia, Sensemaking (information science). https://en.wikipedia.org/wiki/Sensemaking_(information_science) (a15)
- [M] Klein 2006 catalogue record. https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_pascalfrancis_primary_18155864 (b06)
- [V] Klein, Jalaeian, Hoffman, Mueller (2023) The plausibility transition model for sensemaking. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1160132/full (b05)
- [V] Pontis and Blandford (2015/16) Understanding "influence": an empirical test of the data-frame theory of sensemaking. https://discovery.ucl.ac.uk/1464567/1/asi23427.pdf (a04-a09, a25, b01-b04)
- [V] Prochaska, Vera, Tan et al. (2024) Misleading ourselves: how disinformation manipulates sensemaking. https://arxiv.org/pdf/2410.14858 (a11, a12, a26)
- [V] Heuer (1999) Psychology of Intelligence Analysis. https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf (a13, a14)
- [V] Bruner and Potter (1964) Interference in visual recognition, Science 144:424. https://pubmed.ncbi.nlm.nih.gov/14169336/ (abstract only; d19)
- [V] Lord, Lepper, Preston (1984) Considering the opposite. https://pubmed.ncbi.nlm.nih.gov/6527215/ (abstract only; d20; b27 from memory)
- [M] Tolcott, Marvin, Lehner (1989) Expert decision-making in evolving situations. https://doi.org/10.1109/21.31066 (b28, d21)
- [M] Lehner, Adelman, Cheikes, Brown (2008) Confirmation bias in complex analyses, MITRE. https://www.mitre.org/sites/default/files/pdf/04_0985.pdf (b07)
- [V] Belief perseverance summary. https://en.wikipedia.org/wiki/Belief_perseverance (b26)
- [V] Lebiere et al. (2013) A functional model of sensemaking in a neurocognitive architecture. https://pmc.ncbi.nlm.nih.gov/articles/PMC3835765/ (c01)
- [V] Zheng et al. (2025) Supporting data-frame dynamics in AI-assisted decision making. https://arxiv.org/abs/2504.15894 (a16, a17, b14, c20)
- [V] Position paper (2026) From sycophancy to sensemaking. https://arxiv.org/html/2602.02378v1 (b15)

**LLM studies**
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/pdf/2310.01798 (a18, a19, b08-b10, c07, c08)
- [V] Laban et al. (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120 (a20, b11-b13, c05, c06)
- [V] Braitsch et al. (2026) Information-seeking failures of LLMs in agentic clinical reasoning. https://arxiv.org/pdf/2607.10275 (c16, c17)
- [V] Huang et al. (2026) Understanding the anchoring effect of LLM with synthetic data (SynAnchors). https://arxiv.org/pdf/2505.15392 (b16-b18, c13)
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/html/2403.00811v3 (c15)
- [V] Valencia-Clavijo (2025) Anchors in the machine. https://arxiv.org/abs/2511.05766 (c14)
- [V] Shaikh, Dandekar et al. (2024) CBEval. https://arxiv.org/pdf/2412.03605 (b19, c24)
- [V] Early diagnostic commitment in LLM clinical reasoning (NeurIPS 2026 submission). https://neurips.cc/virtual/2026/177226 (b20; abstract page only, not re-opened by the checker)
- [V] Handler, Bedi, Shah (2026) Quantifying and mitigating premature closure in frontier LLMs. https://arxiv.org/pdf/2605.15000 (b21, c18)
- [V] Same facts, different diagnosis: narrative anchoring (2026). https://www.alphaxiv.org/abs/2607.27384.md (b22; not re-opened by the checker)
- [V] Language models keep abandoned analyses (2026). https://arxiv.org/abs/2610.36797 (b23)
- [V] Failing to falsify (2026). https://arxiv.org/abs/2604.02485 (b24)
- [V] Wild guesses and mild guesses in active concept learning (2026). https://arxiv.org/abs/2602.06818 (b25)
- [V] Wilie et al. (2024) Belief-R. https://arxiv.org/html/2406.19764v2 (c02, c03)
- [V] Dhanda (2026) DeltaLogic. https://arxiv.org/abs/2604.02733 (c04)
- [V] Myakala et al. (2026) BeliefShift. https://arxiv.org/html/2603.23848v1 (c25)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors but can correct them. https://arxiv.org/html/2311.08516v2 (c09)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/html/2303.11366v4 (c10, c11)
- [V] Allen and Peterson (2026) Intelligence without integrity. https://arxiv.org/html/2602.20440v1 (c12)
- [V] Lin et al. (2026) Clarification is not correction. https://arxiv.org/abs/2609.25337 (d01-d03)
- [V] Preprint (2026) When agents commit too soon. https://arxiv.org/abs/2606.22936 (d04)
- [V] Ho et al. (2026) Agentic Conversation Context Curation (AC3). https://arxiv.org/abs/2611.00518 (d05, d06)
- [V] Liu et al. (2026) Intent mismatch causes LLMs to get lost in multi-turn conversation. https://arxiv.org/abs/2602.07338 (d07)
- [V] Fang et al. (2026) MINT: hold, lure, and self-correction. https://arxiv.org/abs/2604.04325 (d08)
- [V] Nikeghbal et al. (2026) Who flips? https://arxiv.org/abs/2606.16011 (d09)
- [V] Naeini et al. (2023) LLMs are fixated by red herrings: Only Connect walls. https://arxiv.org/abs/2306.11167 (d10)
- [V] Chen et al. (2026) MedEinst. https://arxiv.org/abs/2601.06636 (d11)
- [V] Kim et al. (2025) M-ARC, inflexible reasoning. https://arxiv.org/abs/2502.04381 (d12)
- [V] Shidara et al. (2026) Advances in LLM reasoning enable flexibility in clinical problem-solving. https://arxiv.org/abs/2601.11866 (d13)
- [V] Barber et al. (2025) Solomonoff-inspired hypothesis ranking with LLMs. https://arxiv.org/abs/2512.17145 (d14)
- [V] Chen et al. (2026) HypoSpace. https://arxiv.org/abs/2510.15614 (d15; partial)
- [V] Jo (2026) Committed before reasoning. https://arxiv.org/abs/2607.16451 (d16)
- [V] Tack, Laban, Neville (2026) LLMs get lost in evolving user intent. https://arxiv.org/abs/2607.20734 (d17; abstract, intro, captions)
- [V] Luo et al. (2026) Multi-turn reasoning when context arrives in pieces. https://arxiv.org/abs/2606.12941 (d18; partial)
- [V] Yousuf et al. (2024) LLM augmentations to support analytical reasoning. https://arxiv.org/pdf/2411.16116v1.pdf (c19)

**Tools for humans**
- [V] Choube et al. (2025) GLOSS. https://arxiv.org/pdf/2507.05461 (a21)
- [V] Li et al. (2025) Vital Insight. https://arxiv.org/abs/2410.14879 (a22, c22)
- [V] Huang, Fatir, Luo et al. (2025/26) Narrative Scaffolding. https://arxiv.org/pdf/2512.18920 (a23, c21)
- [V] Suh et al. (2023) Sensecape. https://arxiv.org/pdf/2305.11483v2.pdf (c23)

**Seen only in snippets, or opened without using the theory**
- [V] Bamman et al. (2024) classification with LLMs in cultural analytics. https://arxiv.org/pdf/2410.12029v1 (a24: read, does not use the theory; c26: snippet only)
- [M] Moell et al. (2025) DeepSeek R1 diagnostic failure analysis. https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1616145/pdf (c27)
- [M] Rao et al. (2026) 21 LLMs on differential diagnosis, JAMA Network Open, via news summary. https://www.epocrates.com/online/article/llms-struggle-with-clinical-reasoning-despite-strong-final-answers (c28; collapse to one answer, accuracy about 80-90%)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 7 established claims: 6 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E04.03-K04** (now single-source: the sources are not independent). The key sentence appears only in Heuer (1999), listed twice from the same chapter, where it is an extrapolation ('presumably happens in real life') from Bruner and Potter 1964 (original not opened); Prochaska and the Wikipedia belief-perseverance page do not state it, so there is one source, not independent support.
