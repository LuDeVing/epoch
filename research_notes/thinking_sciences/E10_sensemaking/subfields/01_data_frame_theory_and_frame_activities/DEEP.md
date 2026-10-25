# Data-frame theory and frame activities: deep document

*Subfield E10.01. Built from evidence_a-d.jsonl (ids a01-a25, b01-b26, c01-c29, d01-d20), claims.jsonl (K01-K32) and critique.md in this folder. Schema references (G1-G12, S0-S9, O1-O8, section 4b) are to `research_notes/single_agent/SCHEMA.md` v0.2. Status marks: [E] established, [S] single-source, [C] contested.*

*Honesty note up front: the two founding texts (Klein, Moon and Hoffman 2006; Klein, Phillips, Rall and Peluso 2007) were never opened. Everything said below about what the theory claims is second hand, from papers that cite them. Where a number comes only from that second-hand chain (for example "up to 3 frames", "3-4 anchors") it is marked as such and must not be treated as a rule.*

---

## 1. What it is

Data-frame (D/F) theory is a model of how people make sense of a situation. It was proposed by Gary Klein and colleagues. Its core claim is simple.

- A **frame** is an explanatory structure. It defines entities by their relationships to other entities. It can be a story, a map, a script or a plan. A causal mental model is one kind of frame. (a19, second hand)
- **Data** are the observations. But what counts as data depends on the frame. Frame and data are built together. (a19)
- **Sensemaking** is fitting data into a frame and fitting a frame around the data.
- A first frame is built from a few **anchors**: a small set of key data. The second-hand figure is 3 to 4 anchors (a19, unverified). Militello et al. show anchors can be logged as a data type (a15).
- Sensemaking ends when no key data are unexplained and no key frame element is ambiguous (a19). Klein et al. 2023 say it ends when plausibility "is experienced as sufficient" (d01, b06).

### The frame activities

Per Pontis and Blandford, citing Klein et al. 2007 pp. 132-142 (a03): **mapping** data to a frame, plus six frame activities.

| Activity | Plain meaning | Machine reading (ours) |
|---|---|---|
| Elaborate | Add detail to the current frame, fill slots, add indicators | Fill a slot; list what the frame predicts |
| Question | Doubt the frame because data do not fit | A check failed; a prediction was violated |
| Preserve | Keep the frame by explaining away, discounting or ignoring anomalies | Log the anomaly as "not relevant" (a countable move) |
| Compare | Hold two or more frames and weigh them | Score two frames against the same evidence |
| Reframe | Replace the frame with another | Swap the rule/hypothesis set |
| Seek a frame | Build or find a new frame when none fits | Generate or retrieve candidate frames |

Other summaries say "six" or "seven" activities. The difference is whether mapping is counted. Use "six frame activities plus mapping" (critique correction 4).

Activities can start in any order. A sensemaker may use few or all (a03). The model has no start box and no stop box (a05, citing Moore and Hoffman 2011).

### Why it matters to us

We build one agent that thinks through a scaffold. D/F gives a vocabulary for the step the scaffold most needs: what to do when the first explanation is wrong. Our schema already has most of the control logic (S4 test, S5 revise, S6 impasse, O8 reframe). This subfield asks whether D/F adds anything beyond a vocabulary. The honest answer from the evidence is: it adds a few well-motivated design hints and one strong warning (reframing is rare and trigger-driven), but little that is quantitatively tested.

---

## 2. History and theories in depth

### 2.1 The founding papers (unread)

- Klein, Moon and Hoffman (2006), "Making sense of sensemaking 2: a macrocognitive model", IEEE Intelligent Systems 21(5):88-92. Short paper with the D/F diagram. About 570 citations (a21). Not opened. The diagram is reproduced in Lebiere et al. 2013 and Militello et al. 2018.
- Klein, Phillips, Rall and Peluso (2007), "A data-frame theory of sensemaking", in Expertise Out of Context (NDM6), pp. 113-155. About 326 citations (a22). Not opened. Cited details: 7 activities at pp. 132-142, up to 3 frames compared, 3-4 anchors, frame fixation, just-in-time frames, 8 functions of sensemaking (p. 117) (a19, a22, a03).
- Sieck, Klein, Peluso, Smith and Harris-Thompson (2007), FOCUS report, ARI technical report. Unread (403). Snippet only says the concept "appears supported" (b25, d02).

This is the largest hole in the subfield. Pontis and Blandford note that Klein gives no explanation for the limit of three frames (a03).

### 2.2 Intellectual neighbours

- **Piaget**: assimilation (fit data into the frame) and accommodation (change the frame). Wikipedia notes the parallel as unsourced (a20).
- **Recognition-metacognition model** (Cohen et al. 1996): flagged as a parallel (a20). Not read.
- **Pirolli and Card (2005)**: foraging loop plus sensemaking loop; the frame is roughly their "schema". Not opened (a23, c25). Used as the staged template in Mooney et al. 2026 (c24).
- **Chinn and Brewer (1993)**: seven responses to anomalous data (ignore; reject; exclude from the theory's domain; hold in abeyance; reinterpret keeping the theory; reinterpret with a peripheral change; accept and change the theory). Only the last is theory change; the other six protect the old theory. Original not opened; known from Carmichael et al. 2010 and snippets (d16, b16, a24).
- **Fixation error** in cockpit and process-control research (De Keyser and Woods 1990; Sarter et al. 1997): mentioned in Rankin et al., not opened (a09).
- **Heuristics-and-biases**: Militello et al. chose D/F over it because no normative standard could be defined for their task (a15).

### 2.3 Applications of D/F (breadth, not tests)

Earlier work listed by Pontis and Blandford (a25): intelligence analysis (Moore and Hoffman 2011), Bosnia peacekeeping and navigation (Sieck et al. 2007), medical operative sensemaking (Stewart et al. 2011), problem detection (Klein et al. 2005), incident analysis. All opened by nobody here. Pontis and Blandford say very few studies had examined structure tasks. The evidence for D/F is breadth of application, not tests that could refute it (a25).

### 2.4 Empirical tests and extensions, in order

1. **Pontis and Blandford (2015, 2016)**. The one independent test. Think-aloud with 11 academics judging who is influential in a familiar and an unfamiliar field. All activities appeared in outline, but the model missed relevance judgment, data analysis and decision making, so the authors added two cycles (3 to 5) and explicit start/end boxes (a01, a02, a05, b01, b02). Details in section 3.
2. **Rankin, Woltjer and Field (2016)**. Critical-incident interviews with 20 pilots, 48 surprise cases, 9 analysed. D/F activities visible in messy sequences. Authors add two activities: rapid frame switching and abandoning the search for a frame (a06-a10).
3. **Militello et al. (2018)**. D/F as a coding scheme for 10 clinicians and 30 chronic-pain patients (a15).
4. **Lebiere et al. (2013)**. An ACT-R model of the AHA tasks that cites D/F and reproduces four biases without coded rules (a13, a14).
5. **Klein, Jalaeian, Hoffman and Mueller (2023)**, plausibility transition model. Klein's own update. Adds plausibility judgment at each story state and a strain account of reframing. Built from 23 of 73 cases, one reviewer, no tests (a16, a17, b05-b07, d01).
6. **Evaluative AI** (Miller 2023, built on D/F) and its first behavioural test (Kornowicz 2024, c03). Zheng et al. 2025 give a formal D/F sketch for AI decision support (a11, a12, c01, c02).
7. **LLM sensemaking and fixation studies, 2023-2026**. Mostly about bias and premature closure, not frames by name (section 6).

### 2.5 The plausibility transition model in more detail

Key points (a16, a17, b05-b07, d01):

- People test a causal story state by state. A plausibility gap appears when known causes do not explain the next state.
- Gaps cause strain. Strain drives information search or dismissal of anomalous data.
- Four ways to reduce strain: gather more data, doubt the anomalous data, make assumptions, expand the story. Three of the four are preserve moves (b07).
- Reframing happens when the effort of explaining away anomalies grows too large. Example: USS Vincennes airliner story rejected (a17).
- Two predictions, never tested: closing a gap is abrupt; strain rises before reframing.
- No numeric rule: no anomaly tolerance, no strain threshold, no frame limit, no hypothesis limit (d01, K25). Only count of rival stories in the paper: 2.
- Rival accounts: surprise as estimated effort to explain (Foster and Keane 2015) versus surprise as prediction failure (Reisenzein 2019). The authors admit retrieval and integration difficulty might fully explain the strain, so the story account may add nothing (b06).
- Stopping may be too early because of the illusion of explanatory depth (Rozenblit and Keil 2002) (b06).
- Quote: "statistical analysis of outliers is a misleading and insufficient treatment of anomaly detection" (a16).

### 2.6 Where the theory is thin

- It describes; it does not predict outcomes. No study shows a frame-activity pattern that causes better or worse accuracy.
- Activities overlap and are hard to code (b01, a07).
- No start rule, no stop rule, no order (a05).
- No numeric triggers (d01).
- Experts and novices "share the reasoning process" and differ in knowledge (a10, a19). This makes the process claims hard to separate from knowledge claims.

---

## 3. Core findings with exact numbers

Status here follows claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| In structure tasks nobody reframed. People grew one frame by adding indicators. | 44 tasks, 11 people, 0 reframings. 3 model activities unseen: seeking/inferring relationships, tracking anomalies, seeking a new frame. | Pontis and Blandford 2016 (a02) | [S] one study, qualitative (K01) |
| Model needed extra activities and cycles | 11 activities coded = 9 from Klein 2007 + 2 new (preselecting candidates, making the final choice). Cycles 3 to 5. | a02, a05, b02 | [S] |
| Sample of the one independent test | 11 participants (6 novices, 5 experts), 4 tasks each, 16 tasks from 4 people coded in depth, two coders. Expert years unresolved (">5" vs ">10"). | a01, b01 | [S] |
| Experts questioned source quality, discarded data, elaborated longer; novices named fast | Task 3: novice N6 used 6 data points, 6 preselected names; expert E2 used 15 data points. 3 to 8 candidates preselected per task. | a04, b03 | [E] (K03; 2 sources but same study plus Rankin's restatement) |
| Pilots used question, preserve, elaborate, compare in messy sequences; two new activities | 20 pilots, 48 cases, 9 detailed, 9 challenge categories. Rapid switching cases 2,5,7; abandoning search cases 1,3,7,8. | Rankin et al. 2016 (a06-a08) | [E] for "not cleanly separable" (K04) |
| Slow changes and non-salient cues give no surprise, so no questioning | Case 1: crew forgot second autopilot. | a09 | [S] (K05) |
| Plausibility model has no tested predictions | 23 of 73 cases, 1 reviewer, 1,042 articles screened, 18 strong +4 added | Klein et al. 2023 (a16, d01) | [S] (K18) |
| ACT-R reproduces confirmation, anchoring, representativeness, probability matching | R2 .645 vs 45 people; .591 on new students; per task S1 R2 .929, .313, .001 | Lebiere et al. 2013 (a13, a14) | [S] (K24) |
| Layout of evidence changed confirming choice | N=161. Confirming hypothesis chosen: hypotheses in columns 61.8%, rows 39.2%, text 67.3%. chi2(2)=9.43, p=.009, phi=.24 | Dhami et al. 2024 Study 1 (b08) | [E] as part of K16 |
| Trained analysts mostly not biased | N=62: 66.1% balanced, 19.4% confirming, 14.5% inconsistent. 83.3% credibility-sensitive. | Dhami 2024 Study 2 (b09) | [E] as part of K16 |
| ACH did not improve coherence | N=227, F=0.002, p=.85. Lehner N=24 null. 50-analyst trial null (second hand). Law students N=191 null (second hand). | Karvetski and Mandel 2020 (b11, b12, b10) | [E] (K16) |
| Prompted question-first-diagnosis raised accuracy (humans) | N=61. Final 49.7% vs 38.4%, d=0.84, p=.002. Easy cases 76.8% vs 60.1% (p=.004). Hard 22.7% vs 16.7% (p=.080). No calibration gain (p=.19). | Costa Filho et al. 2019 (b13, b14) | [E] (K06), quasi-experiment |
| Reflection removed availability bias in residents | N=36; similar-case items 1.55 vs 2.19, p=.03; with reflection 2.03/2.31, p=.006 | Mamede et al. 2010 (b15, snippet) | [E] with b13, snippet only |
| Intrinsic self-correction hurt (2023 models) | CommonSenseQA GPT-3.5 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-3.5 GSM8K 75.9, 75.1, 74.7; with oracle labels GPT-3.5 GSM8K 75.9 to 84.3, GPT-4 95.5 to 97.5 | Huang et al. 2024 (b20, c18, critique) | [E] (K07) |
| 2026 models gain from intrinsic revision on checkable tasks | 5 models. SAT Haiku 4.5 75.64 to 93.59; Mistral 34.62 to 64.96. Gain vs baseline accuracy rho 0.05; vs verifiability rho 0.65 (p<.001). Right to wrong up to 13.25%. One model changed 98.7% of Codenames clues. | Stav et al. 2026 (d14) | [E] jointly with K07 |
| Tools beat no-tool critique | ChatGPT HotpotQA F1: CoT 42.8, no tool 46.1, CRITIC 52.9. AmbigNQ 64.3/67.3/74.9. GSM8k 72.5/77.0/78.2. Toxicity 0.325/0.339/0.173. | Gou et al. 2023 (d13) | [E] (K26) |
| Model-only check fails on graph coloring | 100 instances. Direct 16%; self-critique 1/100; external verifier ~40%; sampling ~40%; accepted 2 of 100 optimal; invented conflicts in 39 | Stechly et al. 2023 (d12) | [E] (K26) |
| Reflect-and-retry task dependent | Sonnet 4.5 iAgentBench 0.584 to 0.648 (retrieval) to 0.682 (reflection); SimpleQA 0.740 to 0.716 | Dammu et al. 2026 (c22) | [S] (K08) |
| Red herrings cause wrong group frames | GPT-4 0-shot: 6 walls/239 groups original, 59/595 with red herrings removed; GPT-3.5 0/114 vs 5/274; humans 285/494 walls, 1405/1976 groups | Alavi Naeini et al. 2023 (b17) | [S] (K09) |
| LLMs confirm more than falsify on rule discovery | 11 LLMs, success 6-78%; counter-example prompt 42% to 56%; Think-in-Opposites up in 11 of 11, Dual-Goal 8 of 11; Qwen3-32B thinking 41 to ~60; Blicket Qwen3-32B 0.57 to 0.86, Qwen3-8B 0.32 to 0.40; TiO tokens per turn ~1.4x (1030 to 1450) | Jhaveri et al. 2026 (b21, c11, c12, d05, d06) | [E] (K10) |
| Negative testing drives success | 12 models; instruction-tuned 33-41%, reasoning 68-75%; Spearman of positive-test share vs falsification rate -0.937 | Bertolazzi et al. 2026 (c14) | [E] with above |
| Opposites step carries the human effect | N=120: 78.3% vs 36.7%, chi2=22.07; N=180: opposites 78.33%, properties-only 38.33%, control 36.66%, chi2=27.99 | Branchini et al. 2023, 2025 (d07, d08) | [E] human |
| Counterfactual critique in open troubleshooting | 100 cases. Final score SIA 79.2; without counterfactual critique 74.0; ReAct 69.0; ToT 61.5. Hypotheses held: SIA 9.0, ReAct 12.7, ToT 21.0. Cost not reported. | SIA, arXiv 2606.13220 (d09) | [S] |
| Prompt-only anchoring fixes weak | CoT, ignore-anchor, reflection no significant gain; both-sides anchors helped on 8 of 15 questions. More thinking tokens: delta +0.031, p=.157; 12,350 calls. | Lou and Sun 2024 (c19); Kraishan 2026 (b22) | [E] (K12), both small |
| Premature closure | MedQA 500 items, AfriMed 490: false action ~70% baseline, ~48% with safety prompt. Underspecified low-risk 73.2-96.1% closure; urgent 5.0-35.8%. | Handler et al. 2026 (c07, c29) | [E] (K13) with Yuan |
| Narrative closure default | 72 responses, 12.5% (9) held ambiguity open; narrative closure 29/72; presupposed reading 63/72; false epistemic signalling 63/72 | Yuan et al. 2026 (c06) | [S] alone; [E] with Handler |
| Early commit and no recovery | 15 models, 200,000+ conversations: 39% drop, aptitude -15%, unreliability +112%; answer in first 20% scored 30.9 vs last 20% 64.4; snowball recovers 15-20% | Laban et al. 2025 (c09, c10) | [E] (K14) |
| Clinical information seeking: wrong frames stay wrong | 32 models, 20 cases. Best 68.1%, mean 56.3. 212 of 323 (65.6%) wrong first diagnoses stayed wrong. 156 of 307 (50.8%) right ones turned wrong. Information use 56.8% round 1 to 25.7% round 3 (R=0.69 with accuracy). Differential 43.6% vs diagnosis 66.6%. Recovery Opus 4.6 7 of 8, Qwen3 Next 1 of 14. | Braitsch et al. 2026 (c08, c28) | [E] with Laban (K14) |
| Fixation on familiar pattern: generation effect? | Dec 2024 best 50% (Gemini 1.5 Pro), o1 48%, physicians 66% (n=5). 2026: Claude 4.1 Opus 0.751 (CI 0.738-0.763) vs physicians 0.66 (CI 0.55-0.75). Hard 20 items: model 55% right, 25% decisively wrong; humans 36%. | Kim 2025 (b18, d04); Shidara 2026 (b19, d03) | [C] (K15) |
| Evaluative AI no gain | N=375 of 439. Brier: recommendation only 0.173, evidence only 0.185, control 0.200, both 0.201, evaluative 0.230; model 0.178; Kruskal-Wallis p=.154. Time 51.7 s vs 41.2 s. | Kornowicz 2024 (c03, c27) | [C] (K17); Le et al. 2024a claims gain, unopened |
| Separating facts from interpretations | Distortion recognition GPT-3.5 0.425 to 0.956 with Diagnosis of Thought; CoT 0.395; o1 0.560; GPT-4o 0.597 | Qi et al. 2025 (c20) | [S] (K19) |
| Staged sensemaking | 120K trajectories, gain 2.0% quality, highest diversity; True Detective GPT-4 0.38 (CoT) to 0.83 with golden reasoning | Mooney et al. 2026 (c24); Del and Fishel 2023 (c21) | [S] (K20) |
| Wording sets the closure | First-person alignment 13/36 vs third person 7/36; teacher-student 4/9 vs 0/9 | Yuan 2026 (c26) | [S] (K21) |
| Frames cluster around a deep story | ~1,000 tweets, 5 rumours, 2020 and 2022 | Prochaska 2024 (a18) | [S] (K22) |
| Commit gate | SWE-bench Verified 500: GPT-5-mini 56.2 to 68.0 (+11.8), MiniMax 75.8 to 80.6 (+4.8); tokens 179K to 157K (-12.1%). Ablation 100 items: full 68, no commit check 58, NL instead of structured 58, baseline 47 | ECLoop, arXiv 2607.28815 (d10) | [S] (K27) |
| Controller-held belief state | ITBench SRE 35 scenarios x3: GPT-5.1 ReAct 8.6 vs 86.1; GPT-OSS-120B 5.7 vs 79.4; Gemini 3 Flash 74.3 vs 92.1; Kimi K2 28.6 vs 83.0. ReAct told the algorithm in prose: recall 2.9, 0.0, 0.0. | EoG, arXiv 2601.17915 (d11) | [S] (K28) |
| Agents notice conflicts then drop them | Mentions peak in first 10% of trajectory; TMD conflict accuracy 3.0-6.5% vs 39.0-65.0%; prompting escalation GPT-5 MoNaCo 1.6 to 60.7 with accuracy 30.1 to 23.2 | arXiv 2610.12360 (d18) | [S] (K29) |
| Thought switching cost | Wrong responses: +225% tokens, +418% thought switches; >70% of wrong responses contain a correct thought; TIP AIME24 QwQ-32B 38.3 to 44.1 | Wang et al. 2025 (d19) | [S] cost side of K02 |
| Hypothesis diversity scoring | 1,500 problems, 9 models, 50,340 hypotheses, 17,835 consistent (~20% for 70B class) | GEAR (d20) | [S] (K31) |

---

## 4. Mechanisms and models

Each model below is written so an engineer can build it. Where the source gives no number, the parameter is marked TUNE.

### 4.1 The base loop (Zheng et al. 2025, a11, c01)

Three functions and one rule.

```
extract(raw)            -> evidence e_t        # code or model slot
retrieve(e_t)           -> hypothesis set H_t  # model slot or library lookup
score(e_t, h) in [0,1]  -> per hypothesis      # code check where possible
loop:
  if max_h score(e_t, h) >= tau: accept (elaborate / commit)
  else: extract more evidence OR retrieve more hypotheses; repeat
```

- tau has no source value (K23, K25). TUNE it.
- This covers fit, elaborate and seek. It has no explicit preserve, compare or reframe operator. Reframe = replace the whole H_t.
- Per G5 the score and threshold must be code. The model fills the extract and retrieve slots only. If the score is a model's opinion, it is a judged step and adds noise.

### 4.2 The frame as an object

Combine the fields that several sources imply (a15, c02, a19, d18, d10):

```
Frame {
  id, statement (one line rule/hypothesis),
  anchors[]            # the 3-4 facts that built it (a15, a19; number unverified)
  predictions[]        # what must be true if it holds
  expected_data[]      # observations that would confirm, with status: seen / not yet
  supporting[]         # evidence ids
  contradicting[]      # evidence ids, kept apart from supporting (c02)
  open_anomalies[]     # unexplained items; each with how it was handled
  assumptions[]        # stated assumptions (needed to judge a reframe, K22)
  verified flags       # confirmed vs unverified evidence (c02)
}
```

Three ways to hold it, and what the evidence says:

1. Free text in context. Baseline.
2. Object written in context. Untested for frames. Prompting the same procedure in prose failed in EoG (recall 2.9, 0.0, 0.0) (d11). Structured conditions beat prose conditions in ECLoop (68 vs 58 of 100) (d10).
3. Object held and checked by code, model only fills slots. Best-supported direction: EoG 8.6 to 86.1 (GPT-5.1) (d11); ECLoop commit gate (d10).

No study tests arms 1 vs 2 vs 3 for a frame object at equal tokens (K28). This is the single best candidate test (section 8).

### 4.3 Activity-to-operation map

| Activity | Trigger (code-checked) | Operation | Output logged |
|---|---|---|---|
| Elaborate | Frame accepted, no open anomaly | Fill a slot; list predictions; run one prediction check | predictions checked / failed |
| Question | A check failed or a prediction was violated (G1, G2) | Show the failing output; ask what it says about the frame | anomaly record |
| Preserve | Anomaly judged minor by a rule | Park, discount a source, or patch (Chinn-Brewer classes, d16) | handling class; running anomaly count |
| Compare | Two frames alive | Lay every evidence item against every frame in code (row layout, b08); score in code | score matrix |
| Reframe | Strain trigger crossed (see 4.4) | Replace frame; new frame must differ in a stated assumption (a18, K22) | new frame + assumption diff |
| Seek a frame | No frame passes tau | Generate candidates from the bare task and from retrieved analogues (S3, O7) | candidate list |
| Abandon search | Budget fraction spent, no plausible frame (a07, a08) | Switch goal from explaining to controlling: known procedure, submit best attempt (G6) | fallback flag |
| Rapid switch | Time short and a stored alternative exists (a07) | Swap to stored alternative frame at once | switch log |

This follows Pontis and Blandford's suggestion (a03) and Rankin's two added activities (a07, a08).

### 4.4 The strain trigger (Klein 2023, a16, a17, b05, b07)

The theory says reframe when effort to explain away grows too large. Two computable proxies, both untested:

- **Anomaly count**: number of unexplained or explained-away anomalies against the current frame. Reframe when count >= k (TUNE).
- **Explain-away effort**: tokens or steps spent justifying failed checks. Reframe when effort >= e (TUNE).

Klein gives no numbers (d01). The two proxies compete (a17). Test both against a fixed-step and an always-reframe arm (section 8).

Cost side: always-reframe resembles underthinking. Wrong reasoning traces have 418% more switches (d19). One model rewrote 98.7% of answers on a revise prompt (d14).

### 4.5 Mechanisms behind the biases (Lebiere et al., a13, a14)

- Blended retrieval over past instances regresses to the mean. Result: anchoring at high probabilities, confirmation at low ones.
- Centroid-of-centroids anchors on early judgments.
- Negative feedback on winner-take-all leads to probability matching.
- Confirmation = a distribution peakier than the Bayes optimum. Anchoring = flatter. These are measurable on any probability output.

Engineering reading: early experience fixes later bias. Do not show a first answer to later attempts (S3 rule, G4). If memory retrieves similar past cases by blending, check it for anchoring.

### 4.6 Compare, done so it helps (b08, b11, b12, c19)

What did not work: asking people (or a model) to fill in an ACH matrix. What did: a layout with hypotheses in rows (39% vs 62-67% confirming choice, N=161). Both-sides anchors partly worked on GPT-4 (8 of 15 questions). So compare should be a format change done in code, not a judged scoring step. Display alone is not enough either (Kornowicz, c03): users engaged with evidence only a little and decisions did not improve.

### 4.7 The disconfirming step (Jhaveri, Bertolazzi, Branchini)

Think-in-Opposites: pick one feature of the last test and test its opposite (c12). Dual-Goal: state the rule and its complement. Code-side measure: the incompatible-to-compatible test ratio (I:C). Humans who found the rule first had I:C 1.79 vs 0.24 (c17, second hand). Boundary: "opposite" is undefined for open hypotheses (d06). In debugging or diagnosis one must define the opposite as "an input that differs from the hypothesis assumption in exactly one stated assumption".

Klayman-Ha logic (c15, second hand): positive tests can falsify a hypothesis broader than the truth, never one narrower. Choose test type from the set relation between frame and evidence so far. Bertolazzi found hypotheses narrower than the true rule in over 50% of turns for almost all models (c14). So the common failure is a frame that is too narrow. That calls for a broaden-the-frame operator, which is different from replacing the frame.

### 4.8 Commit gate (ECLoop, d10)

Hold an edit or answer until listed observations are present. A held action is retried at most 3 times, then an audited fallback. Structured evidence state. This is the only measured commit rule. The same model writes conditions and acts, so blind spots are shared. It gates edits, not frames.

### 4.9 Rejected as stop signal

Self-agreement between runs. Step-4 hidden-state similarity predicted later stability (r=-0.35 with variability, AUROC 0.81) but stability is not correctness; a commitment prompt cut variability 28% without raising accuracy (d17).

---

## 5. What holds up

### 5.1 Strongest findings

1. **Reframing is rare and trigger-driven** [E]. 0 of 44 tasks (a02); surprise-driven in pilots (a07-a09); pilots abandon a search when no frame fits (a08).
2. **A bare reconsideration without an outside signal is unreliable** [E]. 2023: Huang (b20), Stechly (d12), CRITIC (d13), Kamoi review (d15). 2026 update: checkable tasks gain (d14).
3. **Models close early and stay closed** [E]. Laban (c09), Braitsch (c08), Handler (c07, c29), Yuan (c06).
4. **Forced disconfirming tests help** [E] on rule discovery: LLMs (b21, c12, c14) and humans (d07, d08).
5. **ACH-style comparison does not help** [E]: b11, b08/b09, b10, b12, b26.

### 5.2 Failures, nulls and failed replications

- ACH null: N=227 (F=0.002); Lehner N=24 null; analyst RCT N=50 null (second hand); law students N=191 null (second hand); Whitesmith snippet null (b26).
- Evaluative AI: first behavioural test null (N=375); a rival report claims gain (Le et al. 2024a, unopened) (c03, c04). [C]
- Prompt-only anchoring fixes: CoT, ignore-the-anchor, reflection all no significant gain (c19). Extra thinking tokens no gain (b22).
- 2023 self-correction collapse (b20) is partly reversed by 2026 models (d14). Gains tracked checkability, not difficulty.
- Debate and "be careful" instructions are already in SCHEMA 4b and G9. Nothing new here.
- Always-revise costs: up to 13.25% of right answers flipped (d14); 50.8% of right round-1 diagnoses turned wrong in the clinical task (c08).
- Prompting for conflicts raised escalation but lowered accuracy (30.1 to 23.2; 29.4 to 23.5) (d18).
- Safety prompt left about 48% false action (c07). Grok 3 overcorrected and lost accuracy on answerable items (c07).

### 5.3 Moderators

| Moderator | Effect | Source |
|---|---|---|
| Case difficulty (humans) | Question step helps easy cases (76.8 vs 60.1, p=.004), not hard (22.7 vs 16.7, p=.080). When the right frame is not in the repertoire, a second look cannot create it. | b14 |
| Checkability (LLMs) | Gain from no-tool revision rho 0.65 with verifiability, 0.05 with baseline accuracy | d14 |
| Outside tool or test | Beats no-tool critique in every CRITIC row | d13 |
| Model type | Counter-example prompts significant for thinking models, mixed for non-thinking; Dual-Goal slightly hurt non-thinking | b21, c11 |
| Model generation | Fixation gap closed from 50% to 75% on mARC | d03, d04 [C] |
| Per-model recovery | Opus 4.6 7 of 8 vs Qwen3 Next 1 of 14 | c28 |
| Task structure | Narrative vs structure tasks; multi-solution tasks have short reflection then keep or drop | b04, a02 |
| Presentation | Hypotheses in rows reduce confirming choice | b08 |
| Urgency cues | Closure 5.0-35.8% when urgent vs 73.2-96.1% underspecified low-risk | c29 |
| Expertise | Experts question sources, discard data; share the process | a04, b03, a10 |
| Wording | First vs third person shifts alignment | c26 |

### 5.4 Interventions that worked

- Outside tool in the check step (d13, d12, d15).
- Structured, code-held state: controller belief state (d11), structured conditions (d10).
- Disconfirming test: Think-in-Opposites, 11 of 11 settings (c12); counterfactual critique about 5 points on open troubleshooting (d09).
- Separate facts from interpretations: 0.425 to 0.956 (c20), single source, narrow task.
- Hypotheses in rows (b08).
- Snowball / restate all facts: recovers 15-20% of the multi-turn drop (c10).
- Restate the anchor: lowered anchoring but not significantly (p=.057, 5 items) (b22).

### 5.5 Interventions that did not

- ACH matrix, bias-awareness style instructions, ignore-the-anchor, CoT for anchoring, extra thinking tokens, 1 to 10-shot examples (no consistent gain on red herrings; GPT-4 randomized rows 59, 57, 62, 68 walls) (b17, critique 3), commitment prompt (stability up, accuracy not) (d17).

### 5.6 Weak spots of this literature

- Only one independent empirical test of the theory (11 people, 4 in depth). Rankin et al. is a fit to interviews, not a test.
- Founding texts unread.
- Many LLM studies measure bias, not frames. The link from "confirmation bias in Wason" to "frame questioning" is our inference.
- Most 2026 LLM numbers are preprints. Yuan 2026 has 72 responses.
- Plausibility model: 23 cases, one reviewer.
- Pontis and Blandford, Karvetski, Costa Filho, Dhami numbers were not re-opened in the critique pass (first-pass flag).

---

## 6. Language models

No study tests D/F by name on an LLM. Evidence is indirect, from fixation, premature closure, confirmation bias, self-correction and hypothesis-state studies.

### 6.1 Fixation on a first frame

- Red herrings: GPT-4 0-shot solved 6 walls (239 groups) on the original set and 59 walls (595 groups) on the randomized set. Few-shot examples gave no consistent gain (b17). 2023 models. Confounded: walls with distractors are harder for other reasons too.
- Clinical fixation (mARC): Dec 2024 best 50% vs physicians 66% (b18, d04); 2026 best 0.751 vs physicians 0.66 (b19, d03). Same group, same 100 items, 5 physicians, possible contamination. 25% decisively wrong on the hardest 20 items. [C]
- Multi-turn: 39% average drop, unreliability up 112% (c09). Reasoning models degrade the same way and write about 33% longer answers. Final answers 20-300% longer than first attempts. Temperature 0 does not fix it (c10).
- Clinical information seeking: wrong first frames mostly stay wrong (65.6%), right ones turn wrong half the time (50.8%) (c08). Reasoning rubric score 91.1% at 6 or above but decorrelated from accuracy: reasoning text is not evidence (G10).

### 6.2 Premature closure

- 70% false action when the right answer is absent; 48% with a safety prompt (c07).
- Closure depends on missing-information signals: 73.2-96.1% on underspecified low-risk cases vs 5.0-35.8% on urgent ones (c29).
- Social ambiguity: only 12.5% held ambiguity open (c06).
- Conflicts are noticed early (first 10% of a trajectory) and dropped (d18).

### 6.3 Confirmation vs falsification

- Rule discovery success 6-78% (11 models). Disconfirming ratio tracks success (b21, c11).
- Think-in-Opposites up in 11 of 11 settings; tokens per turn about 1.4x for Qwen3-32B thinking (c12).
- Distillation raised Qwen3-8B 0.21 to 0.59 (c13). We do not train, so this is a ceiling only (K11).
- FalsifyBench: reasoning models 68-75% vs instruction-tuned 33-41% (c14).
- Human effect is bigger when training bundles the opposites step (N=180, 78.33% vs 36.66%) (d08).
- Transfer to open diagnosis: unmeasured except SIA's ~5-point ablation (d09).

### 6.4 Self-check

See 5.1 and 5.3. Short version: bare re-check 2023 hurt; 2026 mixed and checkability-driven; tool-based check consistently better.

### 6.5 Frame objects and structured state

- Controller-held belief state: F1 gains of 17.8 to 80 points (d11). ReAct prompted with the same procedure failed.
- ECLoop commit gate: +4.8 to +11.8 pass@1 and up to 12.1% fewer tokens (d10).
- SIA (competing hypotheses plus counterfactual critique): 79.2 vs ReAct 69.0 vs ToT 61.5. ToT held 21 hypotheses and scored lowest, so a bigger hypothesis set is not better (d09).
- Cognitive reframing: separating facts from interpretations beat reasoning models (c20). Free-text reframing differences small (c20).
- Staged sensemaking: 2.0% gain, higher diversity (c24). True Detective: finding the frame is the bottleneck, GPT-4 0.38 to 0.83 with golden reasoning (c21).
- Mixed evidence on explicit conflict surfacing: it raises escalation but lowers accuracy (d18).

### 6.6 Cost warnings

- Always-reframe may resemble underthinking: wrong traces have 418% more switches and 225% more tokens (d19).
- One model changed 98.7% of answers when asked to revise (d14).
- Chain of thought, more tokens and reflection did not fix anchoring (c19, b22).

---

## 7. What our agent should take

Each item: schema part, status, evidence ids. The strict rule from SCHEMA section 8: moving to [E] needs two independent sources, and an element enters as [S] or [D] with an equal-token test.

### Add now (established)

These mostly confirm or sharpen existing schema text. None needs a new state.

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Reframing fires only on a signal (failed check, anomaly, strain), never on a schedule. | G1, O8 | [E] | K02: a02, a07-a09, b04, d19, d14 |
| A2 | A question step must use an outside check (run, lookup, test) where one exists. A bare "reconsider" is not verification. | G2, G3, S5, O (question) | [E] | K07, K26: b20, c18, d12-d15 |
| A3 | Log right-to-wrong flips on every revise step, and judge revise by checkability of the item, not difficulty. | Section 6 logging | [E] | K07: d14 |
| A4 | Do not copy the ACH matrix. If a compare step exists, build it in code with hypotheses in rows. | S7 compare, 4b | [E] | K16: b08, b11, b12, b10 |
| A5 | Anchor handling: do not rely on "ignore the anchor", CoT or more thinking. | S1 input hygiene | [E] | K12: c19, b22 |
| A6 | Add an explicit "no frame fits: ask, abstain or fall back to a known procedure" exit. Do not make it the first-pass default (G6 stays: never abstain on the first pass). | S6, G6 | [E] | K13: c07, c29, c06; a08 |
| A7 | Keep all facts visible each step (restate or re-send the full data list). | S3, memory | [E] | K14: c09, c10, c08 |
| A8 | Disconfirming step: after a test supports a hypothesis, run one test designed to fail it. Count disconfirming vs confirming tests in code. Start on rule-discovery and debugging items. | S4, S7 counterexample search | [E] on rule discovery; contested transfer to open tasks | K10: b21, c12, c14, d07, d08 |
| A9 | Question step for humans helps easy items; do not expect a reflection to repair a frame the model cannot produce. A new frame needs a source (seek a frame, O7, S3 open mode). | S3, O7, O8 | [E] | K06: b13, b14 |
| A10 | Guard against over-revision. Cap rounds (already 2). Track how often the revise prompt changes an answer. | S5 | [E] | d14, c08 |
| A11 | Do not use model-felt plausibility as a stop rule. | S4, S8 | [E] (agrees with G10 and 4b) | b06, d17, c08 |

### Test first (single-source or contested)

| # | Item | Schema part | Status | Evidence | Why not yet |
|---|---|---|---|---|---|
| T1 | Strain counter as reframe trigger: count unexplained anomalies and trigger seek-a-frame at a tuned threshold. | S6 trigger, O8 | [S] | K18, K23, K25: a16, a17, b05, d01 | No number in the source; no test |
| T2 | Frame object (anchors, predictions, expected data, open anomalies) held by code vs written in context vs free text. | S (state), memory | [S] | K28: d11, d10, c02, a15 | No test of a frame object; prompt-only arm of EoG failed |
| T3 | Evidence-conditioned commit gate as the stop rule. | S8, S4 | [S] | K27: d10 | One domain; gates edits |
| T4 | Open-anomaly list that persists across steps. | S state | [S] | K29: d18, a09 | Surfacing can lower accuracy |
| T5 | Reframe must differ in a stated assumption; score by prediction dissimilarity. | O8 | [S] | K22, K31: a18, d20 | Untested |
| T6 | Chinn-Brewer operators: park (abeyance), discount source, patch, reframe. | S6, O (anomaly handling) | [S] | K30: d16 | Original unread; no LLM use |
| T7 | Data vs inference split inside elaborate (S1/S2). | S1, S2 | [S] | K19: c20 | Narrow task |
| T8 | Alternative-groupings step on distractor-heavy items. | S2 | [S] | K09: b17 | Old models |
| T9 | Trigger-based reframe vs plain CoT vs always-reframe at equal tokens. | G1, O8 | [S] gap 1 | K02 | No study at all |
| T10 | Minimum elaboration before commit (list predictions, check one). | G, S2-S4 | [S] | K03, K32: a04, b03 | Process correlates with expertise; no accuracy test |
| T11 | Neutral third-person restatement, compare answers in code. | S1 | [S] | K21: c26 | 9-response cells |
| T12 | Staged sensemaking states. | S | [S] | K20: c24, c21 | 2.0% gain, trained models |
| T13 | Fixation re-measure on our base model before building anything. | S0 | [C] | K15: b18, b19, d03, d04 | Generation effect probable |
| T14 | Counterfactual critique on open diagnosis/debugging. | S5, S7 | [S] | K10 part: d09 | Cost not reported |
| T15 | Check blended retrieval of past cases for anchoring in our memory design. | memory | [S] | K24: a13, a14 | Model-based only |

---

## 8. Concrete tests on our bench

All arms get equal total tokens (G7). Log mode, path, tokens per state, every transition and trigger, doubt steps and their flips (SCHEMA section 6). Report right-to-wrong and wrong-to-right counts separately.

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T9) | Items with a misleading first frame: red-herring puzzles (Only Connect style), mARC-style trap items, our own ARC items where the obvious rule is wrong | (a) plain CoT; (b) trigger-only reframe (fires on a failed check); (c) always-reframe every k steps | Accuracy; reframe count; right-to-wrong flips; tokens | b >= a by a few points; c below b (cost of switching: d19). If c matches b, drop the trigger machinery |
| B2 (T1) | Same set | Strain thresholds k = 1, 2, 3, 5 anomalies; and explain-away-effort threshold; plus fixed-step reframe | Accuracy; time to first reframe; false reframes (reframe when first frame was right) | Inverted-U in k. Pick k at the knee |
| B3 (T2) | Multi-step diagnosis and debugging with a hidden cause | (a) free text; (b) frame object in context; (c) frame object held and checked by code (model fills slots) | Accuracy; consistency across 3 runs; tokens | c > b ~ a. EoG suggests c large (d11); b may equal a |
| B4 (A2, K26) | Items split by checkability (has a runnable test vs none) | (a) no re-check; (b) re-check in text; (c) re-check with run or lookup | Gain by checkability; right-to-wrong flips | c > a; b small positive on checkable, negative on non-checkable (d14) |
| B5 (A8, T14) | Debugging items, diagnosis items, rule-discovery items | (a) plain; (b) forced disconfirming test (opposite = flip one stated assumption); (c) forced extra confirming test (token-matched filler) | Disconfirming ratio; success; tokens | b > a, c. Rule discovery +10 to +15 points (b21). On open tasks maybe +3 to +5 (d09) |
| B6 (T3) | Coding or multi-step tasks with a listable evidence set | (a) fixed-step stop; (b) self-agreement stop; (c) evidence-conditioned gate (structured) | Pass rate; tokens | c > a, b; tokens -5 to -12% (d10) |
| B7 (T4) | Tasks with a slow drift planted partway | (a) none; (b) per-step "frame predicts X, observed Y" check in code; (c) persistent anomaly list | Detection step; accuracy | b, c > a (K05). Watch for accuracy loss from over-surfacing (d18) |
| B8 (T5) | Items needing a new frame | (a) rewording reframes; (b) assumption-changing reframes | Prediction dissimilarity (Jaccard); accuracy | b > a in diversity; accuracy gain unknown |
| B9 (T6) | Items with anomalies | (a) preserve/reframe only; (b) + park, discount, patch | Accuracy; anomaly resolution rate; tokens | Small positive if any; first label what the agent already does |
| B10 (T7) | Interpretation items with an emotional or leading story | (a) CoT; (b) data/inference split first | Accuracy | Large only on narrow tasks (c20) |
| B11 (T10, K32) | Same labelled set | Ablate each expert step alone: source check, discard-data, elaborate-before-commit | Accuracy at equal tokens | Unknown. Do not assume gain |
| B12 (T13) | mARC items and ours | Our base model plain | Accuracy vs published 0.751 | If at or above physicians, skip fixation scaffolds on easy traps |
| B13 (T11) | Social and ambiguous items | (a) as told; (b) neutral third-person restatement; compare in code | Answer shift rate; closure rate | Shift 10-20% on first-person items (c26) |
| B14 (T15) | Our memory module | Blended vs single-case retrieval | Anchoring index (flatter than Bayes) | Detect anchoring (a13) |

Measurement note: when logging, label each doubt step using the six activity names plus mapping so the log stays comparable with Pontis and Blandford, but score only on outcomes (K01).

---

## 9. What does not transfer, and why

- **Human narrative sensemaking to single-answer tasks.** D/F was built from field cases (pilots, clinicians, analysts). Pontis and Blandford found no reframing at all in multi-solution structure tasks (a02, b04). Our tasks often have one exact answer and a check.
- **Felt plausibility as a stop signal.** For people plausibility is a feeling. For a language model fluent text always feels plausible. Use external checks (b06).
- **Expert behaviour.** Experts question sources and discard data because they hold a richer cue repertoire (a10). The model cannot copy the behaviour without the knowledge. No accuracy test exists (K32).
- **The "3 frames" and "3-4 anchors" limits.** Second hand, no explanation, human memory limits. Do not impose them on an agent (d02, d01, a03).
- **Human reflection results (d=0.84).** Students reflecting with new time on 12 images. A model reflecting on its own answer gets no new input (b20). The two look opposed but differ in who reflects and whether new input arrives (critique contradictions).
- **Quasi-experiment details.** Costa Filho's reflection group had higher baseline (d=0.42); reflection was always applied, not signal gated (b13).
- **Evaluative AI.** An interface question for people (what to display). Low priority for a single agent (K17).
- **Training results.** Distillation of falsification (0.21 to 0.59) is outside scope (c13).
- **Cognitive reframing (therapy).** Reframing a thought is not the same as replacing an explanatory frame; the dataset is short texts scored by overlap (c20).
- **ACT-R biases.** The model fits synthetic map data. It supports a design hint (early experience fixes later bias) but not a prescription (a13).
- **The ACH procedure.** Failed in humans; do not port the matrix as is (K16).
- **2023 conclusions on self-correction.** Partly outdated for 2026 models on verifiable tasks (d14).

---

## 10. Open questions

1. At equal tokens, does a trigger-based reframe beat plain CoT and an always-reframe loop on tasks with a misleading first frame? No LLM study. (gap 1)
2. What are the exact trigger rules in Klein 2007? The 2023 paper has none. (gap 2, partly closed in the negative)
3. Does the question-first-answer gain split by difficulty for LLMs? Only checkability is measured (rho 0.65 vs 0.05). (gap 3)
4. Is LLM fixation still present in current reasoning models on an independent benchmark? (gap 4, contested)
5. Does a forced disconfirming step carry to open diagnostic and debugging tasks, and at what token cost? (gap 5)
6. Do the Chinn-Brewer seven responses give a better operator set? Original unread. (gap 6)
7. What is the stopping rule? Klein gives "plausibility feels sufficient". ECLoop gives one gate. Link to adaptive stopping and metareasoning. (gap 7)
8. Does an editable frame object in context beat free text at equal tokens, and does code-held beat in-context? (gap 8)
9. Do assumption-changing reframes beat rewordings? (gap 9)
10. Do experts' extra steps improve outcomes or only correlate with expertise? (gap 10)
11. Do the plausibility model's two predictions (abrupt closure; strain before reframing) hold at all?
12. What is the unit of an anomaly for an LLM: a failed check, a contradicted prediction, an unexpected tool output? How should minor anomalies be separated from fatal ones?
13. Why did the Le et al. 2024a evaluative AI study find a gain while Kornowicz found none? Unopened.
14. Pontis and Blandford expert-years: ">5" or ">10"? Unresolved.
15. Does surfacing conflicts help when the agent has a check to resolve them, versus when it does not? (d18 suggests the latter hurts.)

Links to parallel subfields: Means-ends analysis; Progress monitoring theory; Adaptive stopping and metareasoning (stopping rule); Soar impasses and chunking (impasse types, learning from impasse); Consistency-based diagnosis and conflict generation (conflict sets); Anomaly handling and fixation (Chinn-Brewer, fixation); Hypothesis limits in troubleshooting (frame limit); Troubleshooting search strategies; Verification design (outside check); LLM metacognitive harness; Representational change (constraint relaxation).

---

## 11. Sources

[V] = opened and read this session or in a prior pass (text read). [M] = snippet, abstract only, or second hand only.

### Theory and human studies
- [M] Klein, Moon and Hoffman (2006) Making sense of sensemaking 2. https://doi.org/10.1109/mis.2006.100 (a21; not opened)
- [M] Klein, Phillips, Rall and Peluso (2007) A data-frame theory of sensemaking. https://doi.org/10.4324/9780203810088-13 (a22; not opened)
- [M] Sieck et al. (2007) FOCUS: a model of sensemaking, ARI report. https://apps.dtic.mil/sti/tr/pdf/ADA469770.pdf (b25, d02; 403)
- [V] Pontis and Blandford (2016) Understanding influence: an empirical test of the data-frame theory (JASIST). https://discovery.ucl.ac.uk/id/eprint/1464567/ and https://discovery.ucl.ac.uk/id/eprint/1464567/1/asi23427.pdf (a01-a05, a25, b01-b04). Numbers not re-opened in critique pass.
- [M] Pontis and Blandford (2015) exploratory study, snippet. https://collaborate.princeton.edu/en/publications/understanding-influence-an-exploratory-study-of-academics-process/ (b24)
- [V] Rankin, Woltjer and Field (2016) Sensemaking following surprise in the cockpit. https://link.springer.com/content/pdf/10.1007/s10111-016-0390-2.pdf (a06-a10)
- [V] Militello et al. (2018) Understanding how primary care clinicians make sense of chronic pain. https://pmc.ncbi.nlm.nih.gov/articles/PMC6398613/ (a15)
- [V] Klein, Jalaeian, Hoffman and Mueller (2023) The plausibility transition model for sensemaking. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1160132/full (a16, a17, b05-b07, d01). Page read to character 100000 of 104726.
- [V] Lebiere et al. (2013) A functional model of sensemaking in a neurocognitive architecture. https://pmc.ncbi.nlm.nih.gov/articles/PMC3835765/ (a13, a14)
- [V] Prochaska et al. (2024) Misleading ourselves. https://arxiv.org/abs/2410.14858 (a18)
- [V] Matuschak reading notes on Klein et al. 2007 (secondary). https://notes.andymatuschak.org/zYUYmp1aA5TQxpBuS5JsTri (a19)
- [V] Wikipedia, Sensemaking (information science). https://en.wikipedia.org/wiki/Sensemaking_(information_science) (a20)
- [M] Pirolli and Card (2005) The sensemaking process and leverage points (a23, c25; no URL; memory and citation only)
- [M] Chinn and Brewer (1993) The role of anomalous data in knowledge acquisition. https://www.ideals.illinois.edu/items/17657 (a24, b16; 403, snippet)
- [V] Carmichael et al. (2010) NARST paper, secondary description of Chinn and Brewer. https://perg.phys.ksu.edu/papers/2010/Carmichael_NARST10.pdf (d16)
- [V] Dhami, Belton, De Werd, Hadzhieva and Wicke (2024) Effects of task structure and confirmation bias in alternative hypotheses evaluation. https://cognitiveresearchjournal.springeropen.com/counter/pdf/10.1186/s41235-024-00560-y.pdf (b08, b09); [M] second-hand claims inside it (b10)
- [V] Karvetski and Mandel (2020) Coherence of probability judgments from uncertain evidence: does ACH help? https://dlab.sauder.ubc.ca/sjdm/journal/20/200430/jdm200430.html (b11, b12)
- [M] Whitesmith (2019/2020) ACH and confirmation bias. https://strathprints.strath.ac.uk/69049/ (b26)
- [V] Costa Filho et al. (2019) Effects of deliberate reflection on diagnostic accuracy in dermatology. https://repub.eur.nl/pub/118085/Repub_118085_O-A.pdf (b13, b14)
- [M] Mamede et al. (2010) Availability bias and reflective reasoning, JAMA. https://pubmed.ncbi.nlm.nih.gov/20841533/ (b15)
- [V] Branchini, Burro and Bianchi (2023) Training people to think in opposites. https://pmc.ncbi.nlm.nih.gov/articles/PMC10219317/ (d07)
- [V] Branchini, Bianchi and Burro (2025) Thinking in opposites improves hypothesis testing (Memory and Cognition). https://pmc.ncbi.nlm.nih.gov/articles/PMC12402026/ (d08)
- [M] Wason (1960) 2-4-6 study, as summarised in Jhaveri et al. (c17)
- [M] Klayman and Ha (1987), as described in Bertolazzi et al. (c15)

### Decision support and formal models
- [V] Zheng, Miller, Bialkowski, Soyer and Janda (2025) Supporting data-frame dynamics in AI-assisted decision making. https://arxiv.org/abs/2504.15894 (a11, a12, b23, c01, c02)
- [V] Kornowicz (2024) An empirical examination of the evaluative AI framework. https://arxiv.org/abs/2411.08583 (c03, c27)
- [M] Le et al. (2024a) evaluative AI vs recommendation-driven support, as reported by Kornowicz. https://arxiv.org/abs/2411.08583 (c04)
- [V] Jain (2025) Collaborative causal sensemaking. https://arxiv.org/abs/2512.07801 (c05)
- [V] Tang et al. (2025) VIS-ReAct. https://arxiv.org/abs/2510.02157 (c23)

### LLM studies
- [V] Alavi Naeini et al. (2023) Large language models are fixated by red herrings. https://arxiv.org/abs/2306.11167 (b17)
- [V] Kim et al. (2025) Limitations of LLMs in clinical problem-solving arising from inflexible reasoning. https://arxiv.org/abs/2502.04381 and https://arxiv.org/html/2502.04381v1 (b18, d04)
- [V] Shidara et al. (2026) Advances in LLM reasoning enable flexibility in clinical problem-solving. https://arxiv.org/abs/2601.11866 and https://arxiv.org/html/2601.11866v1 (b19, d03)
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b20, c18)
- [V] Jhaveri, GX-Chen, Sucholutsky and Choi (2026) Failing to falsify. https://arxiv.org/abs/2604.02485 and https://arxiv.org/pdf/2604.02485 (b21, c11-c13, d05, d06)
- [M] Banatt et al. (2024) multi-turn 2-4-6 benchmark, as described in Jhaveri (c16)
- [V] Bertolazzi, Tentori and Bernardi (2026) FalsifyBench. https://arxiv.org/abs/2606.04751 (c14)
- [V] Kraishan (2026) The long road to the same answer. https://arxiv.org/abs/2610.10049 (b22)
- [V] Lou and Sun (2024) Anchoring bias in large language models. https://arxiv.org/abs/2412.06593 (c19)
- [V] Qi, Lee, Breazeal and Park (2025) Does reasoning with LLMs improve recognizing, generating and reframing unhelpful thoughts? https://arxiv.org/abs/2504.00163 (c20)
- [V] Del and Fishel (2023) True Detective. https://arxiv.org/abs/2212.10114 (c21)
- [V] Dammu, Palkhiwala, Roosta and Shah (2026) iAgentBench. https://arxiv.org/abs/2603.04656 (c22)
- [V] Mooney, Kim, Lee and Kang (2026) Structure liberates. https://arxiv.org/abs/2605.00557 (c24)
- [V] Yuan, Han, Ling and Ruan (2026) What did they mean? https://arxiv.org/abs/2604.23942 (c06, c26)
- [V] Handler, Bedi and Shah (2026) Quantifying and mitigating premature closure in frontier LLMs. https://arxiv.org/abs/2605.15000 (c07, c29)
- [V] Braitsch et al. (2026) Information-seeking failures of LLMs in agentic clinical reasoning. https://arxiv.org/abs/2607.10275 (c08, c28)
- [V] Laban, Hayashi, Zhou and Neville (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120 (c09, c10)
- [V] SIA, LLM-as-an-Investigator, arXiv 2606.13220. https://arxiv.org/html/2606.13220v2 (d09)
- [V] ECLoop, Preventing premature commitment in coding agents, arXiv 2607.28815. https://arxiv.org/html/2607.28815v1 (d10)
- [V] Think Locally, Explain Globally (EoG), arXiv 2601.17915. https://arxiv.org/html/2601.17915v2 (d11)
- [V] Stechly, Valmeekam and Kambhampati (2023) GPT-4 doesn't know it's wrong. https://arxiv.org/html/2310.12397 (d12)
- [V] Gou et al. (2023) CRITIC. https://arxiv.org/html/2305.11738 (d13)
- [V] Stav, Berlowitz, Orner and Kraus (2026) When does intrinsic self-correction help? https://arxiv.org/html/2606.23196 (d14)
- [M] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 (d15; abstract page only)
- [M] When agents commit too soon, arXiv 2606.22936. https://arxiv.org/abs/2606.22936 (d17; abstract page only)
- [V] Accurate but not humble, arXiv 2610.12360. https://arxiv.org/html/2610.12360v1 (d18)
- [V] Wang et al. (2025) Thoughts are all over the place: underthinking of o1-like LLMs. https://arxiv.org/html/2501.18585v2 (d19)
- [V] GEAR: a general evaluation framework for abductive reasoning, arXiv 2509.24096. https://arxiv.org/html/2509.24096 (d20)
