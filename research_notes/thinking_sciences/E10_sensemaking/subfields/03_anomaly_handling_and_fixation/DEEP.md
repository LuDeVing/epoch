# Anomaly handling and fixation: deep document

*Subfield E10.03 of sensemaking. Written from evidence_a-d.jsonl, claims.jsonl (K01-K30) and critique.md in this folder. Evidence ids (a01-d22) point to the evidence files. Status marks: [E] established, [S] single-source, [C] contested. [V] = page or PDF text opened, [M] = snippet or memory only. Numbers marked "abstract only" were not checked against tables.*

*Honest note up front: the human core of this field (Chinn and Brewer 1998, Lord 1979, Dunbar 1993, De Keyser and Woods 1990, Feltovich shields, Klein data-frame) was not opened. It is known through the author's own 1993 seminar paper (d06), secondary papers that cite it, and memory. The LLM side is much better covered, but most 2026 papers are single-lab and unreplicated.*

---

## 1. What it is

An anomaly is an observation the current explanation did not predict. Anomaly handling is what a reasoner does next. Fixation is the failure case: the reasoner keeps an explanation after cues that should have changed it.

Three separate things are often mixed up. Keep them apart.

1. **Noticing.** Does the reasoner register the odd datum at all?
2. **Response.** Given that it was noticed, what is done: ignore, discount, patch, or revise the frame?
3. **Persistence.** After a hypothesis is dropped or retracted, does it keep steering later reasoning?

The evidence says humans are mostly fine at step 1 (K01), weak at step 2 (local patching, K02) and partly weak at step 3 (continued influence, K06). LLMs are different at each step. They also fail in the opposite direction: they drop a right answer under pushback or a planted tool error (K11, K16).

Related terms:

- **Fixation error** (De Keyser and Woods 1990, a19 [M]): keeping an erroneous assessment after cues to revise it. Forms: stuck on one explanation; "everything is fine"; hopping between explanations without testing any.
- **Garden-path fixation**: an early reading leads the reasoner down a path where each later step fits the first reading. Kegworth and the fuel-imbalance case are the standard examples (a01, a03).
- **Premature closure**: deciding early and stopping processing (a04). In LLMs, answering without enough information (c01, d12).
- **Einstellung**: a familiar pattern blocks a better solution (b22, b23, c19-c21).
- **Knowledge shield** (Feltovich et al., a21 [M]): a stock move that protects a simple, partly wrong model by explaining away what does not fit.
- **Continued influence effect**: a retracted claim keeps affecting judgement (b07-b13).
- **Belief inertia, contextual drag**: LLM versions, where a belief or a wrong draft in context keeps pulling (d10, d03).

Boundary: this subfield covers what happens when evidence conflicts with a held frame. Building the frame in the first place is the data-frame subfield. Picking probes is "probing and measurement selection". Hypothesis limits and debugging cognition are separate subfields. Links only.

## 2. History and theories in depth

### 2.1 Early lab work on confirmation

- **Wason 1960** (a18 [M]): the 2-4-6 task. People propose a rule that fits 2-4-6 and test with cases that fit their rule. Many never test a case that would break it. Recalled sample about 29. Not opened.
- **Klayman and Ha 1987** (a26 [M]): the positive test strategy (test cases the hypothesis says are positive) is often a sound heuristic. It fails when the hypothesis is too broad or too narrow. So the cure is not "always seek disconfirmation". It is "test a case where the rule and its main rival differ". This is the main competing account of Wason's result.
- **Lord, Ross, Lepper 1979** (a16, d20 [M]): about 48 undergraduates with opposing views on capital punishment read the same mixed evidence. Each side rated the agreeing study as better and reported more extreme views. Not opened. Later work (Jern, Chang and Kemp 2014; Cook and Lewandowsky 2016, titles only) argues that Bayesian models reproduce polarization, so it need not be irrational.
- **Anderson, Lepper, Ross 1980** (a17 [M]): writing an explanation for a link makes the belief outlast debriefing. Cited in a11. Not opened. Prediction for agents: explaining a hypothesis before testing it may entrench it.
- **Lord, Lepper and Preston 1984** (b14 [M]): "consider the opposite" reduced biased assimilation more than "be fair". Search summary only.

### 2.2 The anomaly literature

- **Chinn and Brewer 1993** (a13 [M] full review; d06 [V] the author's own seminar paper). Seven responses to data that contradict a theory: ignore, reject (doubt the data), exclude (outside theory's scope), hold in abeyance, reinterpret (keep theory, explain data as fitting), peripheral change to the theory, theory change. Only the last accepts the data fully. Nine hypothesised factors decide which response is used (entrenchment, ontological and epistemological commitments, background knowledge, quality of the data, availability of an intelligible alternative, and others). Deep processing (having to justify the evaluation) raises theory change. Independent replicated lines of evidence raise acceptance. Unambiguous demonstrations beat ambiguous ones. A Chinn quote: "It is often more rational to discount a piece of data than to accept it and change theories." (d06). The paper gives no response frequencies.
- **Chinn and Brewer 1998** (a14, d21 [M]): the empirical test with vignettes. Search summaries say results generally supported the taxonomy but needed an eighth response (uncertainty about validity). One secondary review says most undergraduate responses were rejection. No frequencies were recovered. This is the biggest hole in the document.
- **Dunbar 1993, 1997** (a24, d22 [M]): the goal given changes how conflicting data are used. Students told to find an explanation did better than students told to test a hypothesis (direction recalled). In lab-meeting studies scientists first checked method, then looked for patterns across several anomalies. Only secondary descriptions seen.
- **Trickett, Trafton, Schunn 2001** (b04, b05, d09 [V]): see section 3. Scientists notice anomalies, attend to them more, and explain them from the data display, not from theory.
- **Trickett et al. 2009** (b06 [M]): basic scientists resolved anomalies by mental simulation, applied scientists by manipulating the image; novice meteorologists used comparison. Strategy depends on goal and expertise.
- **Hemmerich, Van Voorhis, Wiley 2016** (d08 [V], abstract only): confidence in a theory falls in proportion to the amount of anomalous evidence; larger confidence drops predict theory change; convergent (varied) evidence and an offered alternative produce larger drops.
- **Adams and Barth-Cohen 2024** (a05 [V]): three steps: notice, explain the cause, decide keep/remove/recollect/mitigate. The explanation drives the decision.
- **Meister et al. 2021** (d07 [V]): small human replication of explain-as-method-error, with a boundary: conflict with one's own built model drives revision more.

### 2.3 Fixation in dynamic, risky work

- **De Keyser and Woods 1990** (a19 [M]). Defined fixation errors. Not opened.
- **Besnard, Greathead, Baxter 2004** (a01 [V]): Kegworth. The crew shut down the healthy engine. Vibration and smoke fell, which looked like proof. The faulty engine was not re-checked for about 20 minutes. Their "co-occurrence" account: two expected events are read as cause and effect, and trust in the model rises.
- **Rankin, Woltjer, Field 2016** (a02, a03 [V]): airline pilots, surprise, re-framing. Fuel-imbalance case: first officer says leak, leak checklist, healthy engine shut down; the true cause was a cross-feed valve.
- **Anaesthesia simulators** (d01, d02 [V] abstracts): Schwid and O'Donnell 1992, Gaba and DeAnda 1990. See section 3. Rudolph (b27, a27 [M]) argues the bigger failure is hopping between untested ideas, not fixation.
- **Klein et al. 2007 data-frame** (a20 [M]): a cycle between data and frame; preserving a frame includes explaining anomalies away. Another subfield reads this.
- **Feltovich et al. 2001, 2004** (a21 [M]): knowledge shields and the reductive tendency.

### 2.4 Formal models

- **Thagard 1989, ECHO** (a22 [M]): hypotheses and data as nodes, explanation links excite, contradictions inhibit. A theory with many links survives one anomaly. A rival that explains the anomaly can win.
- **Kulkarni and Simon 1988, KEKADA** (a23 [M]): a surprise (violated expectation, set by the program) spawns a focused sub-goal until it is explained.
- **Gershman 2019, "How to never be wrong"** (a25 [M]): blame can go to an auxiliary hypothesis (instrument, assumption) instead of the main theory. This is a rational update, but with no limit on auxiliaries it excuses anything.

### 2.5 Continued influence and its correction

Misinformation research (Anderson et al. 1980; Chan et al. 2017; Walter and Tukachinsky 2020; Kan et al. 2021; Wood and Porter 2019; Mickelberg et al. 2025) shows retractions leave a residue unless a replacement explanation is given. The "backfire" idea was not supported in a very large replication.

### 2.6 The LLM turn (2023-2026)

Four lines of work:

1. **Knowledge conflicts** (Xie 2024, ClashEval, Astute RAG, survey): context versus stored belief.
2. **Self-correction** (Huang 2024, Tsui 2025, s1, Cheng 2026).
3. **Staged or multi-turn evidence** (Laban 2025, Braitsch 2026, MINT 2026).
4. **Tools, sources and abstention** (Zhao, Shapira, Yang, ToolBench-X, AgentAbstain, Agentic Abstention, Gulati).

Plus Einstellung benchmarks (Only Connect, M-ARC/mARC) and debiasing studies (Ke, Lou and Sun, Kenaston).

## 3. Core findings with exact numbers

Status is the claim-level status from claims.jsonl, adjusted by the critique. "Human" rows come first.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Scientists notice anomalies and attend to them more | Later references per noticed item: anomalies 7.6 vs expected 1.5 (astronomy); 3.0 vs 1.25 (physics); t(28)=2.33, p<.05. 3 scientists, 2 datasets | Trickett 2001 (b04, d09) | [E] for noticing (K01); N tiny |
| Anomalies are explained locally from the display, not from theory | Hypotheses proposed more for anomalies: chi2(1)=7.5. Placed in local context: chi2(1)=9.21. 4 of 5 astronomy anomaly hypotheses from the display. Counts of 5 and 2 | Trickett 2001 (b05) | [S] |
| Students explain data as method error and rarely change assumptions | 11 teachers; 46 anomaly-vs-pattern situations: 20 method, 7 model, 2 changed assumptions. Vs own model (14): 1 method, 6 model explanation, 6 modified, 4 rejected | Meister 2021 (d07) | [S] (K02) |
| Plausible prior theory down-weights conflicting data | N=14. Interaction F(1,13)=10.48, eta2=.45. Data effect 1.29 rating points under plausible vs 0.57 under implausible theory. fMRI conflict network only for plausible theory, P=.001 uncorrected | Fugelsang and Dunbar 2005 (b01-b03) | [S] (K03) |
| Confidence falls with amount and variety of anomalous evidence; larger drops predict theory change | Three experiments; no figures read | Hemmerich 2016 (d08) | [S], abstract only |
| Symptom relief after an action read as proof of the action | Kegworth: 47 lives lost; relief lasted about 20 min; 64% of pilots said new display did not draw attention to rapid changes | Besnard 2004 (a01) | [S] (K04), one accident |
| Early salient distractor cuts accuracy more than late | Accuracy: none 0.269, early 0.110 (-61%), late 0.168 (-36%). F(2,693)=11.995. 58 students, 12 vignettes. Reading time drops only for early distractor | Al Essa 2026 (a04) | [E] (K05) with Saposnik review (b26) as weak second |
| Fixation in anaesthesia simulation | 63% of 30 subjects made at least one fixation error (per subject). 20.5% (27/132) of unplanned incidents in 19 simulations (per incident). Different denominators | Schwid 1992 (d01); DeAnda and Gaba 1990 (d02) | [E] that it is common (K22); do not compare the two numbers |
| Bias linked to diagnostic error in physician studies | 20 studies, 6,810 physicians; biases tied to inaccuracy in 36.5-77% of vignettes; 14 of 20 vignette-based; only 2 looked at patient outcomes | Saposnik 2016 (b26) | [E] as a review; thin on real harm |
| Correction with alternative cause beats bare retraction | Misinformation score (max 6): direct+alternative 0.20, indirect+alternative 0.22, direct only 0.81, indirect only 2.78 (equal to no correction, TOST p=.011). F(1,169)=26.19, partial eta2=.13. 248 usable students | Kan 2021 (b07, b08) | [E] (K06) |
| Debunking leaves a residue | k=52, N=6,878. Misinformation d=2.41-3.08; debunking d=1.14-1.33; persistence d=0.75-1.06. Own supporting reasons raise persistence | Chan 2017 (b09, b10) | [E] |
| Retraction of person impressions is inconsistent | Fully discounted in 2 of 3 experiments | Mickelberg 2025 (a11) | [E] as boundary |
| No backfire effect | 5 experiments, over 10,100 subjects, 52 issues, no backfire | Wood and Porter 2019 (b11, b12) | Refuted effect (K07) |
| Intrinsic self-correction does not help | GPT-3.5 GSM8K 75.9 -> 75.1 -> 74.7; CSQA 75.8 -> 38.1 -> 41.8; GPT-4 GSM8K 95.5 -> 91.5 -> 89.0; CSQA 82.0 -> 79.5 -> 80.0; HotpotQA 49.0 -> 49.0 -> 43.0. Oracle: GPT-3.5 CSQA 89.7. (Table columns are 1/3/5 calls, per critique) | Huang 2024 (a08, b17, c22) | [C] (K08) |
| LLMs fix an error in the user's turn, not in their own | Blind spot 64.5% over 14 models. "Wait" cuts it 89.3%; accuracy +156%. Correction markers +179.5% (GSM8K-SC), +73.6% (PRM800K-SC) | Tsui 2025 (c23) | [S] (K09) |
| Neutral "Wait" helps a reasoning model | s1-32B AIME24 50.0 -> up to 57.6, more tokens. "Alternatively" and no string stayed 50.0 | s1 (d17) | [S], not equal-token |
| Wrong draft in context pulls later answers even if labelled wrong | GPT-OSS-20B HMMT25: clean 58.63; one wrong draft 20.54; draft plus verification 42.26; REVISE 62.20; FILTER 45.83. GPQA: clean 46.97; draft 16.86; verified 26.66; REVISE 33.33; FILTER 43.70. Typical drop 10-20% across 11 models, 8 tasks | Cheng 2026, Contextual Drag (d03) | [S] (K23) |
| Cascade retraction beats local delete | Navigation SR: full 72.41; local delete only 70.85; no cascade 68.61; neither 63.42. Depth-1 cascades 72% | Chen 2026 (d11) | [S] (K24) |
| Conflicting evidence: models favour own prior when prior-consistent evidence is present | GPT-4 about 80% memorization on most popular questions; order swings above 30% for PaLM2 and Llama2-7B; GPT-4 and Vicuna-33B cling even at 2 of 3 counter items | Xie 2024 (a06, b15, b16, c26); survey Xu 2024 (b25, c27) | [E] (K10), old models |
| Wrong retrieved context overrides correct prior | Over 60% override, 1,200+ questions, 6 LLMs. Best (Claude Opus) accuracy 74.3%, context bias 15.7%, prior bias 2.1%. Each +10% prior probability lowers context-following by 4.5%. Token-probability fix: accuracy +14%, context bias -20% | ClashEval (a07); Astute RAG (c28) | [E] (K11) |
| Early commitment in staged information | Average drop 39% over 6 tasks, 15 models, 200,000+ conversations. Aptitude -15%, unreliability +112%. SNOWBALL recovers 15-20%. Answer attempt in first 20% of turns scored 30.9 vs 64.4 in last 20% | Laban 2025 (a09, b19-b21, c13, c14) | [E] (K12) |
| Same in diagnosis | MINT: 1,035 cases, 11 LLMs; over 55% answered in first two turns; avg loss 24.2%; question-last gives up to +62.6% first-commit accuracy; holding lab data prevents loss up to 23.3%; revisions wrong-to-right up to 10.6x right-to-wrong | Fang 2026 (d12) | [E] with Laban (K12, K28 single) |
| Early diagnostic errors persist over rounds | 32 models, 630 pairs. Of 323 wrong/partial at R1, 212 (65.6%) stayed wrong at R3. Of 307 correct, 156 (50.8%) got worse. Information use 57% -> 26%; R=0.69 with accuracy; 91% of traces above reasoning threshold. Best model 68% (abstract only for headline numbers; 65.6% and 50.8% not re-checked) | Braitsch 2026 (c06-c08) | [E] with Laban (K13); numbers partly unchecked |
| Premature closure when no option is correct | MedQA n=500, AfriMed n=490; false action 55-81%, mean about 70%. Underspecified low-risk 81% vs urgent 19%. Safety prompt: 70% -> 48%; adversarial n=191 best residual 50.8%; Grok 3 over-corrected | Handler 2026 (c01-c03) | [E] with agent work (K14) |
| Agents act when they should abstain | 263 paired tasks, 17 LLMs; best paired accuracy 59.5%; one scenario act 90% vs abstain 41% | AgentAbstain (d13) | [E] with d14 |
| Clarify timing | Goal clarification loses nearly all value after 10% of run (pass@3 0.78 to baseline); input clarification keeps value to about 50%; 6,348 runs. CONVOLVE timely recall 26.7 -> 57.4 (abstain-only data) | Gulati 2026 (d19); Luo 2026 (d14) | [E] timing (K29); cost on answerable items unmeasured |
| Tool outputs adopted when corrupted | Adoption: search 68.0%, sub-agent 40.1%, code 35.5% (14 models). Warning in 4.2% of adopting answers. VERIFY prompt: search 75.4 -> 70.0, accuracy on correct returns 94.2 unchanged. COMPARE: 67.6 but 90.9 on correct returns | Yang 2026 (d15) | [S] for mechanism; [E] with Zhao and Shapira for source-driven updating (K16) |
| Credibility drives updating; fixing one side breaks the other | Within-model correlation of drops in user-adoption and source-adoption r=0.87. Opus 5: user 21%, source 27%; Sonnet 5: user 78%, source 98%. Reflection frame flips 69.2% vs tool 49.8% vs context 44.1% vs tool+antidote 19.1% | Shapira 2026 (c11, c12); Zhao 2026 (c15, c16) | [E] (K16), new models unchecked |
| Tools hurt when the model is confident and right | Harmful flips 15.2% of confident-correct transitions vs 0.5% when support at least as strong (Qwen3-Coder-30B). CASE controller +3.80 pts (CI 3.54-4.05) over 53,184 instances | Zhao 2026 (c15, c17) | [S] |
| Tool hazards: noticing, not effort | Baseline-to-clean gap 35-50 pts; hints recover 60-80%; retry of same tool 44-76% after failure; 48.6% of failures were ineffective continuation | ToolBench-X (d16) | [S] (K26) |
| Predict-then-compare beats generic reflection | ALFWorld DeepSeek V3.2: 46.3 vs 49.8 with fewer reasoning tokens (garbled table). 95% of 100 neglect cases still inertial with 2-turn history | EVU, Wang 2026 (d10) | [S] |
| Falsifying hypotheses go with winning | 12 LLMs, 1,200 games. Confirmation bias vs success rho -0.779; vs conclusive falsification rho -0.937. Success: GPT-5.2-Chat 75% vs instruction-tuned 33-41% | FalsifyBench (c24, d05) | [C] (K17, K30), correlational |
| Bias prompts do not remove anchoring | 62 questions, GPT-4/4o: CoT, principles, ignore-anchor, reflection all still significant; both-anchors strategy helped | Lou and Sun 2024 (c25) | [E] with Shi and Huang (K18) |
| Einstellung gap with physicians, then closed | 2025: physicians 66% vs best model 50% (100 items). 2026: Claude 4.1 Opus mean 0.751 vs physicians 0.66 (CI 0.55-0.75); on 20 items physicians missed, top 5 models 55-70% | Kim 2025 (b23, c20); Shidara 2026 (c21) | [C] (K15) |
| Role-split debate recovers misdiagnoses | 80 simulations; 0/80 initially (selected); 57/80 (71.3%) top differential after; no control | Ke 2024 (c09) | [S] (K19) |
| Formal anomaly handling | DeFAb: solver 100%; CoT +56 and +79 pts on two models, -14 on Claude Sonnet 4.6; narrative 14.6-22.0% vs formal 72.8-94.1% | Cooper 2026 (c04, c05) | [S] |
| Cognitive inertia in reasoning models (small open models) | STARS: DeepSeek-7B tokens 9,825 -> 8,474, accuracy +6.54% | Lee 2026 (c18) | [S] (K21) |

## 4. Mechanisms and models

Each mechanism is written so it can be coded. "Code" means the program, not the model, does it (SCHEMA section 1).

### 4.1 The seven (eight) responses as a log code

Chinn and Brewer's list is a closed set of labels. For an agent run, label each reaction to a failed check or odd observation:

- ignore: no mention, answer unchanged
- reject / uncertain validity: says the data or tool is wrong, no test run
- exclude: says it is out of scope
- abeyance: "to be explained later"
- reinterpret: keeps the frame, new reading of the datum
- peripheral change: patches the rule (adds an exception) and keeps the core
- theory change: replaces the frame

Implementation: one cheap labelling pass per anomaly event on the trace, by a blind judge, validated against a human-coded sample. Caution: Kenaston (b24, c10) found automatic evaluators detect that an error exists but cannot reliably name the bias subtype. Use the label for analysis of logs, never as a control signal. Decisions use counts and checks.

### 4.2 Noticing versus response split (K01)

Two measurements per planted anomaly: was it mentioned (noticed), and what changed after (response). Humans score high on noticing and low on frame revision. LLMs may differ: Yang (d15) finds agents often state doubt in the trace and still pass the value on. The scoring has to keep the two apart or a noticing-only agent looks good.

### 4.3 Unexplained-cue ledger (frame confidence)

A running record, in code:

- the current frame (a rule in plain words) and its stated mechanism
- a list of anomalies seen: each with kind (different evidence types), time, and whether explained by a tested cause
- a frame-confidence score that unexplained anomalies of different kinds lower, and that an offered alternative lowers faster (Hemmerich, d08)

This is a small ECHO (Thagard, a22): count unexplained data per hypothesis. A rule with a named mechanism is harder to dislodge (Ahn et al., cited in b03), so the trigger for such a rule should be stricter than for a bare pattern. No threshold is validated (K25). Start with a trigger and tune on our logs.

### 4.4 Trigger candidates (K25), all code-computable

- **Streak**: two low-confidence or failed turns in a row, cooldown of 3 turns (Jung and Son, d04). Cheap. Not tuned. It misfired on three boards by over-revising a transient dip. LLM revision gate fired on 4.3% of turns.
- **Expected-versus-observed mismatch** (EVU, d10; KEKADA, a23): write the expected outcome before the action, compare after. Has a clean zero point.
- **Repeated failed action** (ToolBench-X, d16): after a failed call, retry of the same tool is 44-76% of next actions. Fire when the same action fails twice.
- **Held-out check fails** (Huang, a08): gains from correction appear when a true signal exists.
- **Disagreement between a before-evidence and an after-evidence answer** (CASE, c17).
- **Reduced effort after early hypothesis** (Al Essa, a04): time per word falls with an early distractor. Log tokens spent after the first hypothesis; use as a fixation detector, not a trigger yet.
- **Patch bloat** (Laban, b21): correct multi-turn code solutions were 27% longer in characters (850 vs 668), SQL 14% (129 vs 113). A length growth signal for an unreplaced frame. Untested as a trigger.

### 4.5 Retraction mechanism: replace, delete, cascade

Human data say a retraction with an alternative cause works (Kan, b07). LLM data say annotation is not enough (Cheng, d03): a draft labelled wrong still pulls. Filtering the draft text out recovered most of the loss (GPT-OSS-20B GPQA 16.86 -> 43.70, clean 46.97). Cascade retraction (Chen, d11) removes conclusions built on the dropped node and beat local delete.

Implementation:

1. Store hypotheses as nodes with dependents (conclusions that cite them).
2. On drop: write a replacement candidate (the alternative cause), remove the dropped text from the working context, invalidate dependents, and re-derive from the remaining facts in a fresh context.
3. Keep the ruled-out list outside the prompt, so the agent does not re-propose it.

Three arms to compare (K23): annotate; annotate plus replacement; delete plus re-derive.

### 4.6 Staged evidence handling

Two designs follow from Laban, MINT and Braitsch:

- **Withhold the commit slot** (MINT, K28): keep the agent in an open state with no stated leading hypothesis until a minimum evidence set is in. Instructing "wait" was not enough in MINT; moving the question was.
- **Clean restart** (Laban b19-b20): when new facts arrive, restate the full evidence set and start a fresh attempt instead of patching. SNOWBALL (repeat all shards each turn) recovered only 15-20% of the drop, so a fresh start is predicted to be stronger but is untested.

### 4.7 Evidence isolation and order control

Xie (a06, b16): prior-consistent text next to a counter-item lowers the weight of the counter-item, and order changes answers (above 30% swings for some models). Code should show an anomalous item alone in a fresh context, then combine, and randomise order across attempts.

### 4.8 Source authority frame

Zhao (c16): the same clue flipped a correct answer 69.2% when framed as reflection, 49.8% as a tool, 44.1% as context, and 19.1% with an authority-limiting "antidote". Shapira (c12) shows the cost: anti-sycophancy interventions cut useful updating almost as much as harmful updating (r=0.87). So any frame must be measured on both warranted and unwarranted updates. Yang (d15): a "Low" reliability label lowered adoption for all six models.

### 4.9 Prior-versus-context comparison in code

ClashEval (a07) and Astute RAG (c28): get the model's answer without the new evidence, then with it; compare the answers and their confidence in code. ClashEval's token-probability correction gave accuracy +14% and context bias -20% but needs probabilities. CASE (c17) picks between a no-tool and tool trajectory by answer certainty: +3.80 pts over a confidence baseline, protecting 86.5% of correct no-tool cases while rescuing 72.5% of tool-correct cases in the high-prior bin.

### 4.10 Recheck markers

Two designs, both untested together:

- Neutral continuation "Wait" (Tsui c23; s1 d17).
- Re-present the earlier step as another party's output (Tsui's contrast between user-turn and own-turn errors). This is a prediction from the blind-spot gap, not a tested method.

### 4.11 Falsifying probe choice

FalsifyBench (c24, d05): winners tested outside their hypothesis. Code can compute whether a candidate test separates the leading hypothesis from the main rival (Klayman and Ha, a26), and pick the test where the leading hypothesis predicts failure.

### 4.12 Abstain and clarify

Detect "no option fits" or "underspecified" with a code gate. Gulati (d19): ask about goals in the first 10% of a run. AgentAbstain (d13): evaluate on paired tasks so the cost on answerable items is scored.

## 5. What holds up

### 5.1 Replications and agreements

- **Noticing is not the problem.** Trickett (3 scientists) and Meister (N=11) agree in direction, and Adams (6 students) fits. Four tiny studies, all coded by hand. Medium confidence.
- **Early commitment hurts and sticks.** Laban, MINT and Braitsch use different tasks (generation, MCQ diagnosis, agentic diagnosis) and agree. This is the most solid LLM finding in the subfield.
- **Knowledge-conflict bias.** Xie, ClashEval, Astute RAG and the survey agree in direction, but models are 2023-2024 vintage.
- **Bare retraction fails, retraction with alternative works.** Kan, Chan (meta-analysis), Walter and Tukachinsky (snippet), Mickelberg agree. Chan's persistence d=0.75-1.06 shows the residue.
- **Source credibility drives updating.** Zhao, Shapira, Yang and Handler's work on trust show the same: the text frame and claimed reliability move the answer.
- **Prompt-only debiasing is weak.** Lou and Sun, Shi, Huang, Handler's safety prompt (70% -> 48%, not zero) and SCHEMA 4b agree.

### 5.2 Failed replications and null results

- **Backfire effect**: not found in 5 experiments, N over 10,100, 52 issues (b11). Do not design around it.
- **Fugelsang interpretation**: single small fMRI study, uncorrected threshold. No replication found.
- **Einstellung gap**: a 2025 gap to physicians (50% vs 66%) was closed in 2026 by stronger reasoning models (0.751 vs 0.66). A moving target.
- **LLM reframing and CoT**: DeFAb's chain-of-thought effect ranged from +79 to -14 points by model; its variance exceeded the gap between models.
- **Person-impression retraction** did not show the continued influence effect consistently (2 of 3 experiments fully discounted).

### 5.3 Contested points

- **Self-correction.** Huang: no gain without external signal. Tsui and s1: "Wait" gives gains. Likely reconciliation (critique): Huang tested prompts that say the answer may be wrong; Tsui and s1 used a neutral continuation, and many tested models are reasoning models. Never tested in one harness on staged-evidence tasks at equal tokens. s1 spends more tokens. SPARC (d18) is a theory fitted to Tsui, not a replication.
- **Debate.** Ke: 71.3% recovery with no control. Huang: debate no better than self-consistency at equal responses. G9 stands.
- **Confirmation bias versus positive test strategy.** FalsifyBench is correlational (n=12 models); it does not show forcing helps.
- **Notice more, confirm less (Trickett) versus treat conflict as error (Fugelsang, Lord).** Plausibly resolved by theory plausibility and expertise. Untested.

### 5.4 Moderators found

- Alternative explanation offered: raises correction (Kan) and confidence drop (Hemmerich).
- Own supporting reasons generated: raises persistence (Chan b10).
- Repetition and delay: weaken corrections (Walter and Tukachinsky, b13 [M]).
- Prior confidence: higher prior confidence lowers context-following (ClashEval, 4.5% per 10%); tools hurt when confident and right (Zhao).
- Low-risk look: premature closure 81% vs 19% for urgent cases (Handler c02).
- Reasoning mode: Einstellung traps improved with reasoning (Shidara); FalsifyBench reasoning models less confirmatory (24-39% positive tests vs 66-82%).
- Model: recovery varies (Braitsch: Opus 4.5 recovered 6/6, Qwen3 Next 1/14); Opus 5 vs Sonnet 5 adoption rates differ widely (Shapira).
- Time: goal clarification loses value after 10% of a run (Gulati).
- Denominator: fixation rates (63% of subjects vs 20.5% of incidents).

### 5.5 Interventions that worked

- Alternative explanation with the retraction (humans; Kan).
- Filtering the dropped draft out of context (Cheng: GPQA 16.86 -> 43.70).
- Cascade retraction (Chen: SR 72.41 vs 70.85).
- Withholding the commit question or evidence (MINT: up to +62.6%, loss prevented up to 23.3%).
- Hints that name the tool hazard (ToolBench-X: 60-80% of loss).
- Verify-by-tool-call prompt (Yang: adoption 75.4 -> 70.0, correct-return accuracy 94.2 unchanged).
- Authority-limiting frame (Zhao: 49.8% -> 19.1%).
- Predict-then-compare (EVU: 49.8 vs 46.3).
- Both-anchors strategy (Lou and Sun).
- Prior-versus-context calibrated rule (ClashEval +14% accuracy).
- Safety prompt for no-option items (Handler: 70% -> 48%), with over-correction in one model.
- Clarify early for goals (Gulati).

### 5.6 Interventions that did not work

- Telling the model the draft is wrong (Cheng: HMMT25 20.54 -> 42.26 with verification, still below clean 58.63; annotation alone not enough).
- "Review your answer" without a check (Huang: CSQA 75.8 -> 38.1 in GPT-3.5).
- CoT, "ignore the anchor", reflection for anchoring (Lou and Sun).
- More in-context examples for red herrings (Only Connect).
- Lower temperature for multi-turn reliability (Laban); restating all shards recovers only 15-20%.
- Instruction to wait (MINT).
- Anti-sycophancy prompts: cut warranted updating as much as unwarranted (Shapira).
- Compare-with-prior-knowledge prompt: cut adoption more but lowered accuracy on correct returns (Yang: search 90.9 vs 94.2).
- Fine-tuning for tool trust: limited gains (Yang).
- Extra test-time thinking on tool hazards: helped less than hints (ToolBench-X).

## 6. Language models

### 6.1 Summary of behaviour

- **They commit early and stay.** Average 39% drop in multi-turn tasks (Laban). In diagnosis, over 55% of answers committed within two turns, average loss 24.2% (MINT). A wrong first diagnosis stayed wrong 65.6% of the time over three rounds, and 50.8% of right ones got worse (Braitsch; these two figures not re-checked).
- **They resist their own text more than another's.** Blind spot 64.5% over 14 models (Tsui).
- **A wrong draft keeps pulling.** Even labelled wrong (Cheng). Typical drop 10-20% across 11 models, much larger in small open reasoning models; proprietary models on competition math dropped little (GPT-5 AIME24 88.75 -> 88.13).
- **They over-trust sources.** Corrupted tool returns adopted 35.5-68.0% (Yang); misleading clues flip correct answers 19-69% depending on frame (Zhao); wrong context overrides a correct prior over 60% (ClashEval).
- **They also over-trust themselves.** With memory-consistent evidence present, GPT-4 about 80% memorization on popular facts (Xie).
- **They rarely stop.** False action 55-81% when no option is right (Handler); best paired act/abstain accuracy 59.5% (AgentAbstain).
- **They notice and still pass on.** Agents state doubt in the trace and forward the corrupted value; warnings in 4.2% of adopting answers (Yang).
- **Reasoning text is a poor guide.** 91% of traces scored above a reasoning threshold while accuracy decorrelated (Braitsch). Matches G10.
- **They can drop a right answer too.** Harmful flips 15.2% in confident-correct cases (Zhao); Huang's right-to-wrong changes.

### 6.2 What changed behaviour and by how much

| Change | Effect | Cost or catch |
|---|---|---|
| Filter dropped draft from context | GPQA 16.86 -> 43.70 (clean 46.97); HMMT25 20.54 -> 45.83 | extra passes, no token count; filter assumed oracle in one analysis |
| Cascade retraction | SR 72.41 vs 70.85 local delete | navigation, explicit dependency graph |
| Question last / hold evidence | up to +62.6% first-commit accuracy; loss prevented up to 23.3% | changes the task, MCQ |
| Hints naming the hazard | recover 60-80% of 35-50 pt loss | hints may leak structure |
| Authority-limiting frame | flips 49.8% -> 19.1% | may cut valid updating (Shapira r=0.87) |
| Verify-by-tool-call | adoption 75.4 -> 70.0; correct-return accuracy 94.2 unchanged | only 5 points |
| Compare with prior | adoption 67.6 | correct-return accuracy 90.9 |
| Safety prompt | false action 70% -> 48% | not zero; Grok 3 over-corrected |
| Neutral "Wait" | blind spot -89.3% (Tsui); AIME24 50.0 -> up to 57.6 (s1) | tokens; injected errors; math only |
| Predict-then-compare (EVU) | 49.8 vs 46.3 success | embodied games, small models |
| Calibrated token-probability rule | accuracy +14%, context bias -20% | needs logprobs |
| CASE controller | +3.80 pts over confidence baseline | needs sampled certainty |
| Recap each turn (SNOWBALL) | recovers 15-20% | weak |
| Role-split debate | 71.3% recovery | no control, selected cases |
| Reasoning mode | mARC 0.751 vs physicians 0.66; FalsifyBench reasoning models 24-39% positive tests | cost; DeFAb CoT -14 to +79 |

### 6.3 What has not been done

No found LLM study (a) applies the Chinn and Brewer taxonomy, (b) tests a count threshold for reframing, (c) compares schemas at equal tokens, (d) tests a forced disconfirming test outside rule games, (e) tests Wait or other-party framing on staged-evidence tasks, (f) measures the cost of an abstain operator on answerable items in an agent setting. These are our tests.

## 7. What our agent should take

### Add now (established)

Items below are [E] by claim status. Most already sit in the schema as guardrails; the new part is the specific rule or log. Per SCHEMA section 8 any new element still enters marked [S] or [D] until our equal-token test passes. "Add now" here means: low risk, matches existing guardrails, may be implemented as logging or as a default.

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Do not let a retraction be bare: when a hypothesis is dropped, require a named replacement cause. | S5/S6, O8 | [E] humans (K06); LLM transfer [S] | b07, b08, b09, b13, a11 |
| A2 | Keep an anomaly log with two fields: noticed (yes/no) and response (Chinn-Brewer code). Logging only; it does not trigger anything. | Section 6 log | [E] that the split matters (K01) | b04, b05, a05, d07, d09 |
| A3 | Randomise evidence order in code and show each anomalous item alone in a fresh context before combining. | S3, G4, G5 | [E] (K10) | a06, b15, b16, c26, b25 |
| A4 | Hold the leading answer: no committed diagnosis or answer until a minimum evidence set exists; staged evidence triggers a re-derivation from the full restated set, not a patch. (Withholding the slot itself is [S], K28; the early-commit harm is [E].) | S0, S1, S3 | [E] harm (K12, K13) | a09, b19-b21, c13, c14, d12, c06-c08 |
| A5 | Compare with-evidence and without-evidence answers in code; do not let the model rank its own prior against new evidence. | G5, S4 | [E] (K11) | a07, c28, c15, c17 |
| A6 | Tool outputs are evidence, not authority: score them by check results and source reliability, not by how authoritative they sound. Measure the cost on valid updates. | G4, G6 | [E] (K16) | c11, c12, c15, c16, d15 |
| A7 | No bias instruction, no "ignore the anchor", no "be careful" prompts. Already in 4b. Add anchoring to the list. | 4b | [E] (K18) | c25, c29, b24, c10, a08 |
| A8 | A no-option / underspecified gate in code, with a time window: goal questions in the first tenth of a run. Measure cost on answerable items. | G1, new O-clarify | [E] timing (K29); operator cost unknown | c01-c03, d13, d14, d19 |
| A9 | Report fixation per run and per incident, never mixed. | Section 6 | [E] (K22) | d01, d02 |
| A10 | Do not design around backfire. | none | refuted (K07) | b11, b12 |
| A11 | Early salient items bias later processing; log tokens spent after the first hypothesis appears as a fixation detector (log only). | S3/S4 log | [E] (K05) | a04, a12, b26 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | On drop of a hypothesis: annotate vs annotate plus replacement vs delete plus re-derive (fresh context). | S5, O8 | [S] (K23, K24) | d03, d11, b07 |
| T2 | Cascade: invalidate dependents when a hypothesis is dropped. | S5, memory | [S] (K24) | d11 |
| T3 | Trigger for O8 reframe: streak, mismatch, repeat-failure, unexplained-cue ledger, never. | S6 | [C] (K25) | d04, d10, d16, d08 |
| T4 | Expected-outcome-before-action step, compare after (EVU). | S4/S5 | [S] | d10 |
| T5 | "Wait" marker and other-party framing of the agent's own earlier step, in the same harness as a "review your answer" prompt. | S5 | [C] (K08, K09) | c23, d17, a08 |
| T6 | Repeat-failure operator: after the same action fails twice, ask what could be wrong with the source, not the call. | S6 | [S] (K26) | d16 |
| T7 | Authority-limiting frame for tool outputs; score warranted and unwarranted updates. | G4/G6 | [S] mechanism; [E] direction | c16, c12, d15 |
| T8 | Forced disconfirming test: the test the leading hypothesis predicts will fail. | S7, O-test | [C] (K17, K30) | c24, d05, a26 |
| T9 | Withholding the commit slot vs an instruction to wait. | S0/S3 | [S] (K28) | d12 |
| T10 | Noticed-but-passed-on detector: log explicit doubt statements and whether the flagged value reached the final answer. Target zero. | S4/S8, G10 | [S] (K27) | d15 |
| T11 | Ledger of unexplained cues with mechanism-weighted threshold. | S2/S6 | [S] | a22, d08, b03 |
| T12 | Patch-bloat length signal on multi-turn runs. | S5 | [D] | b21 |
| T13 | Auxiliary-excuse price: each "the test may be broken" must be paid for by a check of the test. | G3 | [D] | a25 |
| T14 | Test goal given: "explain this mismatch" vs "confirm the rule" after a failed check. | S5 | [S] | a24 |
| T15 | Prior-vs-context confidence rule from sampled agreement (no logprobs). | G5 | [S] | a07, c17 |
| T16 | Role-split devil's advocate at equal tokens against self-consistency. | O8 | [S] and G9 prior against | c09, a08 |

## 8. Concrete tests on our bench

All arms at equal tokens (including setup cost, G7). For each, the plain arm gets the saved tokens as extra samples or longer reasoning. Report accuracy, and for operators also the cost on items where nothing is wrong.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Planted anomaly: one odd datum in 20 tasks (rule puzzles, ARC-like, small diagnosis cases) | plain; plain plus anomaly log only | noticing rate (mentioned) separately from response (patch vs reframe) | high noticing, low reframing; gap is the target (K01, K02) |
| B2 | Hypothesis drop: tasks where the model's first hypothesis is refuted mid-run | annotate wrong; annotate plus replacement; delete plus re-derive from fresh context | lingering use of dropped claim in later steps; final accuracy | delete plus re-derive best (Cheng: 16.86 -> 43.70 pattern); replacement adds on top (K23) |
| B3 | Multi-step diagnosis with dependency chains | drop-only; cascade invalidation | final accuracy, revisits to the dead branch | cascade helps (Chen, +1.6 SR) |
| B4 | Staged evidence: same facts all at once vs sharded | patch from earlier answer; restate-all (SNOWBALL); fresh restart with all facts; withhold commit slot | accuracy per arm vs the all-at-once ceiling; unreliability (best-worst run gap) | restart and withhold beat restate (15-20% recovery) (K12, K28) |
| B5 | Staged diagnosis with a lure (strong early lab result) | instruction to wait; question held back; plain | first-commit accuracy | held-back beats instruction (MINT) |
| B6 | Reframing trigger comparison: planted drift in a rule mid-run | never; streak>=2 + cooldown 3; expected-vs-observed mismatch; repeat-failure; unexplained-cue ledger | time to reframe, false reframes on transient noise, final accuracy | mismatch or ledger best on false reframes; streak fastest (K25) |
| B7 | Self-review vs recheck marker on own earlier error (injected) | "review your answer"; neutral "Wait"; earlier step presented as a colleague's; external check | correction rate; right-to-wrong flips | colleague framing and Wait above review; external check best (K08, K09) |
| B8 | Corrupted tool output (graded deviation) | plain; verify-by-tool-call; authority-limiting frame; compare-with-prior; own-answer-first | adoption of corrupted value; accuracy on correct returns | frame and verify cut adoption by 5-30 pts; compare-with-prior hurts correct returns (Yang) |
| B9 | Mixed set: valid and corrupted returns, 50/50 | all B8 arms | warranted-update rate and unwarranted-update rate, both | no arm cuts one without the other (Shapira r=0.87); find the arm that breaks the trade |
| B10 | No-option and underspecified items, paired with answerable twins | plain; no-fit operator; early goal clarification | commit rate on unanswerable; abstain rate on answerable | commit rate falls from ~70% toward 48% or lower; answerable cost under 1-2 points (Handler) |
| B11 | Rule-discovery (2-4-6 style) and a diagnosis analogue | free test choice; forced test where leader predicts failure | success, conclusive falsification rate | success up if the diagnosis analogue holds; may not (K30) |
| B12 | Einstellung items (familiar pattern wrong) | reasoning off; reasoning on; thinking mode vs graph | accuracy on physician-missed subset | reasoning-on higher (Shidara); tells us when G11 must yield (G12) |
| B13 | Noticed-but-passed-on: trace judge on B8 runs | none vs detector-then-regenerate | rate of final answers using a value flagged as suspect | falls toward zero (Yang 4.2% warned) |
| B14 | Early distractor vs late (same prompt) | distractor first; distractor last; input hygiene (distractor moved into a marked block) | accuracy, tokens after first hypothesis | hygiene recovers part of the early-distractor loss (-61% vs -36%) (K05) |
| B15 | Code-run discriminating test between two rules that both fit examples | free; forced split test | rule accuracy on held-out inputs | gain consistent with S7 counterexample result |
| B16 | Goal framing after a failed check | "confirm the rule" vs "explain this mismatch" | revision rate, final accuracy | explain framing higher (Dunbar, human) |

## 9. What does not transfer, and why

- **Human fMRI and conflict-monitoring regions** (Fugelsang): there is no brain region to read. Only the finding that clash detection requires a confident belief carries over, and that is one N=14 study.
- **Student vignette responses** (Chinn and Brewer 1998): the responses depend on background knowledge, identity, and course context. An agent has none of the ontological commitments the taxonomy assumes. The codes are useful for logs, the factors are not.
- **Backfire and polarization**: the agent has no attitudes to defend. Its fixation is local to its context and its own drafts, which is why Cheng's context-pulling mechanism fits better than motivated reasoning. Mickelberg and Chan use student samples and misinformation, a loose analogy to an agent's own hypothesis.
- **Memory decay and delay effects in continued influence**: the agent's context is verbatim. A dropped claim does not fade; it stays in the window and keeps pulling (Cheng). Delay moderators do not apply the same way. Removal from context is possible for an agent, impossible for a person. This is the main place the agent can beat the human pattern.
- **Anaesthesia and aviation fixation under stress, fatigue, workload, team hierarchy**: absent in an agent. Base rates (63% per subject, 20.5% per incident) are not predictions for our agent, only a signal that fixation is not a novice problem.
- **Expertise and intuition** (Rankin, Klein): human experts use pattern recognition built over years. An LLM has a different, shallower route to familiar patterns (Einstellung results). Do not assume "expert" behaviour.
- **Lord-style polarization rationality debate**: the Bayesian account is about priors held by people. Our agent has an explicit code-held frame and no prior to defend.
- **Hidden-state steering (STARS)**: needs weights access; API-only agent cannot use it. Only the idea (detect a pivot, then act) moves over.
- **Token-probability fixes (ClashEval)**: need logprobs; use sampled agreement instead (untested).
- **Checklists and procedures**: Rankin's pilots say checklists "encourage you to keep moving, not to understand". An agent with a checklist-like schema has the same risk. Our S5/S6 must include a step that can split rival hypotheses, not only confirm.
- **Multiple-choice and QA benchmarks**: most LLM numbers here (Handler, MINT, Xie, ClashEval, Yang) are MCQ or short factual QA. Open-ended agent runs may differ.
- **Model-specific numbers**: 2023-2024 models (Huang, Xie, Only Connect) are weak guides to current behaviour. The Einstellung gap closed within a year. Several 2026 papers use model names that cannot be cross-checked here.

## 10. Open questions

1. What are the Chinn and Brewer 1998 response frequencies, and which responses predict later theory change? (Needs the JRST paper; blocked here.)
2. Is there a measurable trigger for reframing in people or LLMs (number or variety of unexplained cues), and what threshold works at equal tokens?
3. Does a forced alternative-explanation step before discard (Kan) transfer to LLM dropped hypotheses, and how much does it cut lingering use?
4. Does "Wait" or other-party framing help reasoning models on staged-evidence tasks, against Huang's null?
5. How much of staged-evidence fixation does a restart operator remove, and at what token cost?
6. Do abstain and clarify operators fix premature closure without hurting answerable items, with agent tools rather than MCQ?
7. What do knowledge shields look like in LLM text, and can explaining-away phrases be detected automatically?
8. Are Rudolph's simulator figures (about 23% correct diagnosis; 28% fail to abandon early diagnosis; 44% hop untested) real? Source is a conference snippet.
9. Does source-credibility updating hold for our own tool outputs, and does an authority-limiting frame keep valid updates?
10. Does a forced disconfirming test help outside rule games?
11. Is the human "local patching from the data display" finding (Trickett) the same as an agent patching from its recent output?
12. Do dependent-conclusion cascades matter at the depth our agent reaches?
13. Does Cheng's drag hold for proprietary frontier models in agent loops (only small drop on competition math so far)?
14. Does the unexplained-cue ledger, with mechanism weight, outperform a plain streak?
15. How many of the "sticks in staged evidence" failures are anchoring at a finer grain (kept the broad disease, missed the subtype, per Braitsch)? Does matching new evidence at the same grain help?

## 11. Sources

Marked [V] opened (page or PDF text read this session or by the evidence agents) or [M] snippet or memory only. Notes on partial reads are in brackets.

**Human core**

- [M] Chinn and Brewer (1993) The role of anomalous data in knowledge acquisition. Review of Educational Research 63(1). https://doi.org/10.2307/1170558
- [V] Chinn (1993) The role of anomalous data in theory change: a cognitive analysis (author's seminar paper). https://mlrg.org/proc3pdfs/Chinn_TheoryChange.pdf
- [M] Chinn and Brewer (1998) An empirical test of a taxonomy of responses to anomalous data in science. JRST 35(6). https://doi.org/10.1002/(SICI)1098-2736(199808)35:6<623::AID-TEA3>3.0.CO;2-O
- [M] Chinn and Brewer (2001) Models of data / responses to anomalous data on controversial topics. https://doi.org/10.1016/s0959-4752(00)00042-6 (title only)
- [M] Lord, Ross, Lepper (1979) Biased assimilation and attitude polarization. https://doi.org/10.1037/0022-3514.37.11.2098
- [M] Anderson, Lepper, Ross (1980) Perseverance of social theories. https://doi.org/10.1037/h0077720
- [M] Lord, Lepper, Preston (1984) Considering the opposite. https://causeweb.org/cause/node/7638
- [M] Wason (1960) On the failure to eliminate hypotheses. https://doi.org/10.1080/17470216008416717
- [M] Klayman and Ha (1987) Confirmation, disconfirmation, and information. https://doi.org/10.1037/0033-295X.94.2.211
- [M] Dunbar (1993) Concept discovery in a scientific domain. https://doi.org/10.1207/s15516709cog1704_3 (and Dunbar 1997, secondary only)
- [V] Trickett, Trafton, Schunn (2001) That's odd! https://conferences.inf.ed.ac.uk/cogsci2001/pdf-files/1054.pdf
- [M] Trickett, Trafton, Schunn (2009) How do scientists respond to anomalies? https://www.lrdc.pitt.edu/Schunn/papers/trickett-trafton-schunn2009.pdf (PDF not retrievable)
- [V] Fugelsang and Dunbar (2005) Brain-based mechanisms underlying complex causal thinking. https://uwaterloo.ca/reasoning-decision-making-lab/sites/default/files/uploads/files/FugDun2005a.pdf
- [V] Hemmerich, Van Voorhis, Wiley (2016) Anomalous evidence, confidence change, and theory change. https://pubmed.ncbi.nlm.nih.gov/26423213/ [abstract only]
- [V] Adams and Barth-Cohen (2024) Student sensemaking with anomalous data. https://pmc.ncbi.nlm.nih.gov/articles/PMC11659860/
- [V] Meister et al. (2021) Pre-service biology teachers' responses to first-hand anomalous data. https://link.springer.com/article/10.1007/s11165-020-09929-7
- [M] Gershman (2019) How to never be wrong. https://doi.org/10.3758/s13423-018-1488-8
- [M] Thagard (1989) Explanatory coherence. https://doi.org/10.1017/S0140525X00057046
- [M] Kulkarni and Simon (1988) KEKADA. https://doi.org/10.1207/s15516709cog1202_4
- [M] Klein, Phillips, Rall, Peluso (2007) A data-frame theory of sensemaking. https://doi.org/10.4324/9780203810088
- [M] Feltovich, Hoffman, Woods, Roesler (2004) Keeping it too simple. https://doi.org/10.1109/MIS.2004.17
- [M] De Keyser and Woods (1990) Fixation errors. https://doi.org/10.1007/978-94-009-0431-5_12

**Fixation in operations and medicine**

- [V] Besnard, Greathead, Baxter (2004) When mental models go wrong. https://hal.science/hal-00691813v1/document
- [V] Rankin, Woltjer, Field (2016) Sensemaking following surprise in the cockpit. https://link.springer.com/content/pdf/10.1007%2Fs10111-016-0390-2.pdf
- [V] Schwid and O'Donnell (1992) Anesthesiologists' management of simulated critical incidents. https://pubmed.ncbi.nlm.nih.gov/1550273/ [abstract only]
- [V] DeAnda and Gaba (1990) Unplanned incidents during comprehensive anesthesia simulation. https://pubmed.ncbi.nlm.nih.gov/2363534/ [abstract only]
- [M] Rudolph conference abstract on simulated OR crisis. https://smdm.confex.com/smdm/2010on/webprogram/Paper5967.html (not used for numbers)
- [V] Al Essa et al. (2026) Premature closure underlies bias in medical diagnosis in students. https://pmc.ncbi.nlm.nih.gov/articles/PMC13569390/
- [V] Saposnik et al. (2016) Cognitive biases associated with medical decisions. https://pmc.ncbi.nlm.nih.gov/articles/PMC5093937/
- [V] Croskerry, Singhal, Mamede (2013) Cognitive debiasing 1. https://pmc.ncbi.nlm.nih.gov/articles/PMC3786658/ [skimmed]
- [M] Mamede et al. (2010) Availability bias and reflective reasoning. https://psnet.ahrq.gov/issue/effect-availability-bias-and-reflective-reasoning-diagnostic-accuracy-among-internal-medicine

**Continued influence**

- [V] Kan et al. (2021) Factors that mitigate the continued influence of misinformation. https://pmc.ncbi.nlm.nih.gov/articles/PMC8627545/
- [V] Chan et al. (2017) Debunking meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC5673564/
- [M] Walter and Tukachinsky (2020) Meta-analytic examination of continued influence. https://digitalcommons.chapman.edu/comm_articles/61
- [V] Wood and Porter (2019) The elusive backfire effect. https://www.gwern.net/doc/psychology/cognitive-bias/2018-wood.pdf
- [V] Mickelberg et al. (2025) Mixed evidence for continued influence on person impressions. https://pmc.ncbi.nlm.nih.gov/articles/PMC12058158/

**LLM studies**

- [V] Xie et al. (2024) Adaptive chameleon or stubborn sloth. https://arxiv.org/abs/2305.13300
- [V] Wu, Wu, Zou (2024) ClashEval. https://arxiv.org/pdf/2404.10198
- [V] Wang et al. (2025) Astute RAG. https://arxiv.org/abs/2410.07176
- [V] Xu et al. (2024) Knowledge conflicts survey. https://arxiv.org/abs/2403.08319
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (tables re-read in critique)
- [V] Tsui (2025) Self-correction bench. https://arxiv.org/abs/2507.02778
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393 [table garbled]
- [V] Petrova and Vejsiu (2026) Spectral origins of the self-correction blind spot. https://arxiv.org/abs/2607.09803 [abstract and intro]
- [V] Cheng et al. (2026) Contextual drag. https://arxiv.org/abs/2602.04288
- [V] Laban et al. (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120
- [V] Braitsch et al. (2026) Information-seeking failures in agentic clinical reasoning. https://arxiv.org/abs/2607.10275 [abstract; 65.6% and 50.8% not re-checked]
- [V] Fang et al. (2026) MINT. https://arxiv.org/abs/2604.04325
- [V] Handler, Bedi, Shah (2026) Premature closure in frontier LLMs. https://arxiv.org/abs/2605.15000
- [V] Liu et al. (2026) AgentAbstain. https://arxiv.org/abs/2607.10059
- [V] Luo, Wen, Wang (2026) Agentic abstention. https://arxiv.org/abs/2606.28733
- [V] Gulati et al. (2026) Ask early, ask late, ask right. https://arxiv.org/abs/2605.07937
- [V] Yang et al. (2026) Agents' overreliance on unreliable tools. https://arxiv.org/abs/2609.05587
- [M] "When agents trust the wrong tool output" (NeurIPS 2026 listing). https://neurips.cc/virtual/2026/166680 (search summary)
- [V] Tian et al. (2026) ToolBench-X. https://arxiv.org/abs/2606.25819
- [V] Zhao et al. (2026) When tools hurt LLM reasoning. https://arxiv.org/abs/2508.15754 [0.5% figure not re-seen]
- [V] Shapira, Cheng, Orgad (2026) Is sycophancy a form of in-context updating? https://arxiv.org/abs/2610.28325
- [V] Sharma et al. (2024) Towards understanding sycophancy. https://arxiv.org/pdf/2310.13548 [abstract and intro]
- [V] Abtahi et al. (2026) MEDLEY-BENCH. https://arxiv.org/abs/2604.16009
- [V] Wang et al. (2026) Seeing isn't believing (EVU). https://arxiv.org/abs/2604.17252 [table garbled]
- [V] Chen et al. (2026) Hypothesis graph refinement. https://arxiv.org/abs/2604.04108
- [V] Jung and Son (2026) Agent harness residual role. https://arxiv.org/abs/2604.07236
- [V] Bertolazzi, Tentori, Bernardi (2026) FalsifyBench. https://arxiv.org/abs/2606.04751
- [V] Lou and Sun (2024) Anchoring bias in LLMs. https://arxiv.org/abs/2412.06593
- [V] Shi et al. (2023) LLMs easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093
- [V] Samadarshi / Alavi Naeini et al. (2023-24) LLMs are fixated by red herrings (Only Connect Wall). https://arxiv.org/abs/2306.11167 [author list uncertain; table garbled]
- [V] Kim et al. (2025) Inflexible reasoning in clinical problem solving (M-ARC). https://arxiv.org/abs/2502.04381
- [V] Shidara et al. (2026) Advances in LLM reasoning enable flexibility in clinical problem-solving. https://arxiv.org/abs/2601.11866 [abstract]
- [V] Kenaston et al. (2025) Cognitive bias in LLM reasoning, oncology notes. https://arxiv.org/abs/2511.20680 [abstract and first pages]
- [V] Ke et al. (2024) Multi-agent conversations to mitigate cognitive bias. https://arxiv.org/abs/2401.14589
- [V] Cooper et al. (2026) DeFAb. https://arxiv.org/abs/2606.18557
- [V] Lee, Kim, Lee (2026) STARS, cognitive inertia. https://arxiv.org/abs/2601.22484
