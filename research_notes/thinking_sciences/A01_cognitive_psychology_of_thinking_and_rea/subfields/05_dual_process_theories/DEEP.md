# Dual-process theories: deep document

Subfield 05 of A01 (cognitive psychology of thinking and reasoning). Written 2026-10-21 from `evidence_a-d.jsonl` (a01-a27, b01-b25, c01-c26, d01-d20), `claims.jsonl` (K01-K27) and `critique.md`. No new search was done. Where the critique corrected an evidence line, the corrected number is used here.

Status marks: [E] established, [S] single source, [C] contested. Evidence ids are in brackets. "Opened" means the page or PDF text was read in the research passes.

---

## 1. What it is

Dual-process theories say that reasoning, judgment and decision making come from two kinds of process. Type 1 is autonomous: it needs no working memory, it fires when a cue appears, and it hands over a default answer. Type 2 needs working memory and can hold a hypothetical apart from what is believed (cognitive decoupling), so it can test, reject or replace the default. The classic evidence is that people give a tempting wrong answer on problems such as the bat-and-ball item, and a minority stop, check and correct it. The theories differ on timing (fast first, or both at once), on how conflict is noticed, and on whether "two types" is a real division or a convenient label. The field has moved from long feature lists (fast, slow, unconscious, effortful) to a narrow, function-based definition, and from "System 1 is wrong, System 2 is right" to "the first answer is sometimes already correct, and the second pass is sometimes wrong." For a language-model agent, the useful part is not the two-box picture. It is the set of concrete findings on when a first answer can be trusted, what signals a wrong one, which cues fail to trigger checking, and when more deliberation costs accuracy or tokens.

---

## 2. History and theories in depth

### 2.1 Roots and early two-process accounts

- **Wason and Evans (1974).** Heuristic versus analytic processes on the Wason selection task. People pick cards that match the words of the rule (matching bias) and give reasons after the fact. This is the human form of "reasoning text is not evidence of the cause" (G10). Known only second-hand through Osman 2004 and Evans and Stanovich 2013. [a26, opened:false]
- **Evans and Over (1996).** System 1 implicit, associative, fast. System 2 explicit, sequential, working-memory heavy. Two kinds of rationality. [a05]
- **Sloman (1996).** Two systems running in parallel: associative (similarity, contiguity) and rule-based. Key test, "Criterion S": two answers conflict at once, and one is felt strongly even when the person knows the other is right. Example: people keep the conjunction fallacy after learning the rule. [a06, a22] Original not opened.
- **Tversky and Kahneman figures as cited by Osman:** naive, informed and sophisticated groups all broke the conjunction rule 85% to 89% of the time. [a06, secondary]
- **Stanovich and West (2000).** Individual differences: Type 2 performance tracks intelligence, Type 1 performance does not. [a03, a05]
- **Kahneman and Frederick (2002).** Attribute substitution: when the target question is hard, the mind answers an easier related one, and System 2 monitors and may endorse the swap. [a27, opened:false]
- **Frederick (2005).** The 3-item Cognitive Reflection Test (CRT): bat and ball, 5 machines, lily pads. Each has a strong wrong first answer (10, 100, 24). Among wrong answers, the intuitive one dominates. Correct solvers often crossed out the intuitive answer first, never the reverse. 3,428 respondents in 35 studies. MIT mean 2.18 (N=61), Princeton 1.63 (N=121), Toledo 0.57. Men 1.47, women 1.03. [a08]

### 2.2 The three architectures

| Theory | Claim | Key authors | Prediction for timing |
|---|---|---|---|
| Default-interventionist (DI) | Type 1 gives a default fast. Type 2 may or may not step in. Intervention depends on difficulty, novelty, motivation and the feeling of rightness. | Evans and Stanovich 2013; Kahneman | Wrong or right default first, then possible correction. Correct answers need extra time. |
| Parallel-competitive | Both types run at once. Conflict is resolved. | Sloman 1996; Smith and DeCoster 2000 | Correct and heuristic answers are both active from the start. |
| Three-stage / logical-intuition (hybrid) | Several Type 1 outputs are cued. Conflict is detected. Type 2 either rationalises the default or decouples from it. Detection and decoupling are separable. Intuitions can themselves be logical. | Pennycook, Fugelsang and Koehler 2015; De Neys | Correct answers can be fast. Detection happens even for wrong answers. |

Why DI was argued for: Type 2 uses scarce working memory and Type 1 is far faster, so a parallel design would make the fast process wait for the slow one. [a02] Evans and Stanovich also say it is a fallacy that Type 1 is always wrong and Type 2 always right. Type 1 fails mainly in "hostile" environments with misleading cues. [a04]

### 2.3 Feeling of rightness and conflict detection

- Thompson (2011): the feeling of rightness predicts how long people rethink and whether they change the answer. Confident intuitions are rethought less. Confidence can be unrelated to accuracy and still control rethinking. [a04, a21 (cited, not opened)]
- De Neys and Glumicic (2008): conflict items take longer and lower confidence even when the person answers wrongly. This is the basis of "implicit conflict detection." [a21, not opened]
- Gangemi et al. (2015) added a "feeling of error" measure on the bat-and-ball item. Self-report, higher on standard (wrong-answer) items than on isomorphic controls and higher in wrong solvers (M=16.52) than in correct solvers (M=8.79). [a12]

### 2.4 Logical intuitions and the two-response paradigm (De Neys group)

- **Two-response paradigm.** Give the first answer under a short deadline and a memory load (to block Type 2), then a free final answer. Direction-of-change codes for conflict items: 00 wrong-wrong, 11 right-right, 01 wrong then right, 10 right then wrong. DI predicts mostly 00 and 01. Logical intuition predicts a visible 11 share. [a18, a19]
- **Bago and De Neys 2017 "Fast logic?"** Four experiments (N=101, 104, 99, 115). Base-rate and syllogism tasks. They report that 74.8% (base-rate) and 87.6% (syllogisms) of final-correct conflict answers were already correct at the first response. Averages: base-rate 11=30%, 00=56.7%, 01=10.1%, 10=3.2%; syllogisms 11=42.3%, 00=48.1%, 01=6.0%, 10=3.6%. [a18, a19] The critique could not re-open this paper, so these figures are first-pass only.
- **Bago and De Neys 2019 "Smart System 1"** (bat-and-ball): only 20.1% correct at first response on conflict items versus 93.4% on no-conflict controls. Correct justifications rose from 20.7% (first-correct) to 60.6% (final-correct), so fast-correct answers are real but often have no stated rationale. [b20, text opened in the critique pass, not checked line by line]
- **Re-measured fast-correct share:** about 53% on the CRT (two-response, N=908; 11 = 28.35%, 01 = 25.33%) [d07]; about 56% and 78% in untrained bat-and-ball controls, about 84% after training [d06]. The fast-correct share is task and sample dependent. [K04]

### 2.5 The critics

- **Osman (2004).** One graded system can explain the same data. Reviews Wason selection, conjunction fallacy and belief bias. Notes that belief-bias evidence suggests people start with some analytic work and the bias sits at evaluation, which conflicts with Sloman's "belief first, then analysis." [a05, a06, a07]
- **Keren and Schul (2009).** Three tests are needed to show two systems: dichotomy (not continuous), alignment of features, and separability (double dissociation). They say no paradigm passes all three. Alternatives: a many-parts model, or a unimodel where depth of processing varies continuously with perceived task relevance (Kruglanski). No new data. [d02, opened]
- **Melnikoff and Bargh (2018) "The mythical number two."** Features such as unintentional, uncontrollable, unconscious and efficient are assumed to line up, but alignment was never measured. With four binary features there are 16 cells and the typology says only 2 are common. Mixed cases exist (skilled typing is intentional but unconscious). Type 2 is not "good" and Type 1 not "bad." Advice: study each feature separately. No data of their own. A rebuttal by Pennycook and colleagues (2018) was seen only as a search summary. [d01, opened]
- **Evans and Stanovich (2013) reply.** Concede the feature lists are correlates. Keep two defining features: autonomy and no working-memory use for Type 1; working memory and decoupling for Type 2. Speed, capacity, consciousness and normative answers are "typical correlates." Individual differences lie on a continuum but the types remain distinct kinds. The move makes the theory harder to refute with a single misaligned correlate, which is the point Melnikoff and Bargh press. [a01, d03]
- **Critique of the conflict evidence.** Franssens and De Neys (2009) is cited for the claim that part of the base-rate response-time effect comes from extreme base rates. Snippet only, attribution unverified. [c19]

### 2.6 How the theories differ in what an engineer would build

- DI: a cheap default plus a trigger that sometimes calls an expensive check. Build: first pass, then gate.
- Parallel: run both and compare. Build: two answers, then a resolver.
- Three-stage: separate detection (is there conflict?) from decoupling (reject the default and find another). Build: two independent components with separate logs.
- Single-process / continuous (Keren and Schul): effort is a dial set by the task's demands. Build: several depths, not two.

No study tested whether a continuous-depth gate beats a binary gate. [K01]

---

## 3. Core findings with exact numbers

Status uses the claim ledger. "Human" findings come from mostly WEIRD online or student samples.

| # | Finding | Numbers | Source | Status |
|---|---|---|---|---|
| 1 | The CRT trap is one dominant lure, not scattered errors | Bat-and-ball 30.3% correct, 64.9% lure, 4.8% other wrong; widgets 30.3 / 58.4 / 11.3; lily pad 43.2 / 40.8 / 16.1 (N=372 of 497, naive only). 4-option version: 36% correct, 58% lure, 6% foils (N=131). 94.9% of wrong first responses were the lure | b10, b01, b13, a08 | [E] (K02) |
| 2 | Prior exposure inflates the CRT | Accuracy t(496)=5.53; intuitive responses t(496)=5.81 | b11 | [E] contamination matters |
| 3 | Conflict costs time and confidence even for lure answers | Base-rate answers t(59)=7.65, d=.99; stereotype answers t(57)=5.72, d=.75; RT cost 562 ms (N=62). Extreme base rates raise the stereotype-answer cost: 598 ms vs 120 ms. 17.2% took longer on congruent items (no detection) | a14, a15 | [C] (K03) |
| 4 | Conflict detection not found on the CRT with mouse tracking | Conflict vs no-conflict time t(7.4)=.55; heavy and light lure responders no different (all t<1, p>.4); correct answers 27.3 s vs intuitive 21.0 s, p=.019 (trial level: 181 correct vs 297 heuristic trials); cursor distance 49% vs 55.5%, p<.0001 | b01, b02 | [C] |
| 5 | Feeling of error tracks correctness (self-report) | Wrong solvers M=16.52 vs correct M=8.79, F(1,143)=66.29, partial eta squared .32 | a12 | [S] |
| 6 | Fast-correct share is task and sample dependent | Original two-response: 74.8% and 87.6% (unverified). CRT: about 53% (N=908). Bat-and-ball controls: 56% and 78%; after training 84%. Repeated 50-item bat-and-ball: 16% insight, 23% correct from start, 61% biased (N=62). First-correct on conflict: 20.1% (smart System 1) | a18, d07, d06, b13, b20 | [C] (K04) |
| 7 | Fast logic for simple belief-bias items, belief-dominance for complex | Simple: symmetric interference; accuracy conflict .68 vs no-conflict .92 (N=45). Complex syllogisms: belief .76 vs logic .50 on conflict items; logic cost .21 vs belief cost .09, p=.03 (N=84) | a16, a17 | [C] (K14) |
| 8 | Correction is rare, spoiling is not zero | Base-rate: 01=10.1%, 10=3.2%. Syllogisms: 01=6.0%, 10=3.6%. CRT: 01=25.33%, 10=9.33% | a19, d07 | [S] |
| 9 | Short logic training moves the first response | Base-rate +48.3 vs +6.2 points (F(1,99)=36.17); conjunction +58.3 vs +4.2 (F(1,98)=72.25, generalized eta squared .21). Bat-and-ball first-response +30.0 and +45.7 vs +11.9 and +6.1; lasted two months; carried to bat-and-two-balls, not to algebra word problems or other CRT-like items. Groups began 12.6 points apart on base-rate, so some gain is regression to the mean | a20, d06 | [S] (K05, one lab) |
| 10 | Repetition without feedback does not de-bias | 61% of 62 stayed biased over 50 items; insight came as one jump, always before trial 20 | b13 | [S] (K20) |
| 11 | Fast first answers are a clean probe | Order of fast and slow blocks did not change fast accuracy (N=123; slow 23.5% vs fast 19.9%) | b14 | [S] |
| 12 | Wrong reasoners still encode the relation | Recall of "more than" 69.7% vs 25.4%; recognition 82.4% vs 30.4%; confidence 0.889 vs 0.923, partial eta squared .02; time 34.0 s vs 21.2 s (N=382, 227 wrong) | b15 | [C] (K17) |
| 13 | Numbers lure mindless arithmetic | Empty box: 70% answer 27; empty hole: 42% say 27, 34% say 0. N=3,193 (3 studies) | b16 | [S] |
| 14 | The CRT carries numeracy and predicts beyond intelligence | Framing consistency: numeracy b=-0.16 (p=.002), reflection b=-0.01 (p=.81), N=1,413 and 1,478. CRT adds 11.2% unique variance after ability 17.3%, executive function +5.6%, dispositions +2.1%; r=.42 with heuristics-and-biases tasks (N=346) | a11, b12 | [C] (K15) |
| 15 | CRT base rates are sample bound | Argentina N=157: mean 0.80 men, 0.59 women (vs 1.47 and 1.03); sex gap not significant | a10 | [E] as a caution |
| 16 | Time pressure does not cause cooperation | RRR, 21 labs, N=3,596: intent-to-treat -0.37 points (CI -2.60 to 1.86) vs 8.6 in original data; compliant-only 10.37 vs 15.31; non-compliance 65.9% under pressure vs 7.5% under delay; Q(20)=16.84, I2=2.72% | b03, b22 | [refuted] (K16) |
| 17 | Original pooled effect | 15 studies, 6,910 decisions; 6 significant positive, 2 marginal, 6 non-significant positive, none negative; experience moderator post hoc | b04, b21 | contradicted by RRR |
| 18 | Disfluent fonts do not help | Original plus 16 replications: no effect on solution rates (abstract only) | b17 | [E] with K06 (abstract only) |
| 19 | Self-reported confidence is weakly tied to accuracy | Shynkaruk and Thompson (cited) | a04 | [S] |
| 20 | Heuristic tasks differ widely in difficulty | Hardest sample-size problem 15.6% correct; easiest 92.2%; 55.8% solved no CRT item, 6.6% all three | b23, b12 | [S] |

---

## 4. Mechanisms and models, explained so an engineer could implement them

### 4.1 Default-interventionist loop

```
answer = type1(problem)            # cheap, autonomous, no held hypotheticals
if trigger(problem, answer):       # conflict, novelty, low feeling of rightness
    answer = type2(problem, answer)  # holds answer apart, tests, may replace
return answer
```

The trigger is the weak point. In humans it is driven by the feeling of rightness: high confidence means less rethinking, even when confidence is not tied to accuracy [a04]. For an agent the trigger must be computed by code from checkable signals, not from the model's own feeling.

### 4.2 The three-stage model (Pennycook, Fugelsang and Koehler 2015) [a13, a14, a15]

1. Cue several Type 1 outputs (for base rates: the stereotype answer and the base-rate answer).
2. Detect conflict between them.
3. If conflict: decouple (falsify the default) or rationalise (justify it after the fact).

Measure: reaction time on incongruent minus congruent items. Findings: extreme base rates (995/5) raise the detection cost but not the decoupling cost; showing base rates before the stereotype lowers detection and raises decoupling. Analytic thinking disposition goes with detection (r=.28, N=60), not with decoupling. Engineering reading: log detection and repair separately. A failed task could be a missed detection or a failed repair, and the fixes differ.

### 4.3 Two-response paradigm as a measurement protocol [a18, b14, d06, d07]

- Response 1: tight deadline (4 to 8 s) plus a memory load. Record the answer and confidence.
- Response 2: free time.
- Code the pair as 00, 01, 10, 11.
- For an LLM: response 1 is a short sampled answer under a hard token cap set by code; response 2 is the full-budget answer. Do not rely on a prompt that asks for a brief answer: with thinking off, DeepSeek-V4-Flash still showed visible reasoning in 99.9% of open-ended answers, and strict answer-only prompts cut mean accuracy by about 15 points on open-ended tasks. Boolean tasks comply best (80 to 100%). [d18, K24]
- Log the text before the answer so the "direct" arm is verified as direct.

### 4.4 Mouse-tracking time course [b01]

Four-option CRT. On correct trials, the cursor first drifted toward the intuitive option (closest approach 49% of display width). On lure trials, no drift toward the right option (55.5%). Reading: default-interventionist on the CRT. An engineer's analogue: log which candidate answers appear in a trace before the final one (the S4 "harvest").

### 4.5 Calibration signals from sample spread [d05, d04]

- Take n short samples. Compute agreement, entropy of the answer distribution, or first-second distance.
- Older models: GPT-4 Brier .116 (entropy), .119 (agreement), .114 (first-second distance) vs .154 (verbalised words) and .181 (verbalised percent). 3 to 5 samples already help a lot; saturation at 15 to 20. Consistency metrics more than doubled macro-F1 for finding wrong GSM8K predictions. [d05]
- Frontier model: gpt-4.1 had agreement of 0.8 or more on 77% of GPQA entries and was wrong on 48% of those (CI .40 to .56). Correlation with correctness was lower than for the mini model (-0.18 on GPQA, -0.26 on AIME). Brier 0.42 and ECE 0.41 for gpt-4.1 vs 0.26 and 0.22 for mini with chain-of-thought. A confidence-routed cascade lost to always using the mid-tier model. Exploratory Claude check (haiku-4.5, sonnet-4.6, opus-4.7) showed the same confident-wrong pattern. [d04] Data quality: class assignment, not preregistered.
- On a trap item every sample may share the lure, so agreement is high and wrong. Treat it as one logged input, not a gate. [K21]

### 4.6 Escalation by code-checked triggers: SwiftSage [c09, c10, d10]

- Fast module: flan-t5-large (770M) tuned on 62k oracle actions. Slow module: large LLM (SAGE), two calls producing an action buffer of about 5 actions.
- Switch to slow when any holds: (1) 5 consecutive steps with zero reward; (2) invalid predicted action; (3) critical decision, e.g. final answer; (4) unexpected observation. Return to fast when the buffer is empty; two consecutive invalid buffer actions send control back.
- Results (ScienceWorld, 30 task types, 270 variations): 84.7 vs SayCan 33.8, ReAct 36.4, Reflexion 45.3. Tokens per action 757.07 vs 1,855.84, 1,971.03, 2,983.46.
- Gaps: no trigger ablation; no always-slow arm at equal tokens; every baseline calls the LLM at every step; fast-only scored higher than the gated agent on short tasks (78.68 vs 72.81, ChatGPT backend); GPT-3.5 swap: ReAct 36.43 to 19.76, SwiftSage kept 62.22.
- Non-simulator stand-ins (from d10): no reward becomes no new verified evidence in N steps; invalid action becomes a tool or format error; critical decision becomes before the final answer or an irreversible action; unexpected observation becomes a tool result that breaks a stated expectation. [K13]

### 4.7 Learned switches (need training; shape only) [d11, d14, c08, c21, c20]

- ThinkSwitcher (7B, seven math benchmarks): short-only 46.0% at 1,079 tokens; long-only 64.6% at 7,617; learned switch 62.8% at 5,405 (about 90% of the long-vs-short gain at about 71% of tokens); random 25/75 mix 58.9% at 5,918; random 50/50 55.2% at 4,120; BERT classifier 60.7% at 6,021. [d11]
- Three-way mode (none / short / long, caps 1,024 / 3,000 / uncapped): MATH500 0.782 vs 0.796 base with 41% fewer tokens (4,796 to 2,811); GSM8K 76% fewer tokens. [d14]
- Dualformer (maze, 30x30): slow 97.6% optimal vs 93.3% baseline with 45.5% fewer steps; fast 80% vs 30%; auto 96.6% with 59.9% fewer steps. [c08]
- ACPO 1.5B on AIME 2024: 30.0% at 6,670 tokens vs 16,894 for the distilled base (60.5% fewer). [c21]
- DynamicMind (prompt-based Fast / Normal / Slow with a router): normal mode was most efficient on 80.52% of GSM8K samples; slow mode helped 3.11% of tasks (+53.84% accuracy on those) at about 233 extra tokens; router transfer changed accuracy by 0.3 to 6 points. Router trained on a self-built dataset. [c20]
- Our scaffold does not train weights, so it can copy only the shape: three depths, a per-family record of which depth was enough, and a gate. [K22]

### 4.8 System 2 Attention (input cleaning) [c06, c24, d09]

Same model, two calls: (1) rewrite the context keeping only relevant, unopinionated text; (2) answer from the rewrite only. LLaMA-2-70B-chat for both. TriviaQA with opinions (200 prompts, GPT-4 judge): baseline 62.8%, oracle 82.0%, S2A 80.3%, "ignore opinions" instruction 71.7%, S2A with the original text kept beside the rewrite 74.5%; adding "think step by step" made things worse. GSM-IC (100 problems, 3 seeds): 51.7% to 61.3% (about +12 random, +10 in-topic distractors). Long-form objectivity 3.82 vs 2.23 baseline vs 3.0 oracle. No replication found on current models. [K12]

### 4.9 Perturbation test for lure reuse [c17, d20, d16, d17]

Change the principle of a familiar item (additive to non-additive cost; worker-count dependent to independent; exponential to linear growth). A model that reuses the remembered method gives the old answer. Changing only numbers does not trigger the failure in strong models (o1-preview kept accuracy with number-only changes). Engineering rule: a perturbation check must change the principle.

---

## 5. What holds up: replications, meta-analyses, failures, moderators, interventions

### 5.1 Held up

- **A dominant lure exists** on conflict items (finding 1). Several independent labs and samples. [E]
- **The CRT is contaminated by exposure and numeracy** (b11, a11). [E as a caution]
- **Time pressure and disfluency cues do not reliably switch on analytic mode** (b03, b22, b17). The RRR is the strongest evidence: preregistered, 21 labs, N=3,596, heterogeneity I2=2.72%. [E] (K06)
- **Fast correct answers exist**, but their share is task dependent (about 53% on the CRT, 56% to 84% on bat-and-ball, 20% in one report). [C]
- **Training the logic moves the first response** inside a family (a20, d06). One lab. Lasted two months. Did not carry to other families. [S]

### 5.2 Failures and refutations

- **Time pressure makes people cooperative:** refuted under intent-to-treat (-0.37 vs 8.6). Selection by compliance explains the original pattern (65.9% non-compliance under pressure). This tests "intuition is prosocial," not dual-process theory itself. [K16]
- **Rand 2014 experience moderator:** post hoc. The authors said online workers became experts at lab games (median MTurk worker had done 300 academic studies vs 15). The RRR found compliance and selection explained the pattern better. [b04, b21]
- **Disfluent fonts:** 16 replications, none helped (abstract only). [b17]
- **Frederick's sex difference:** not supported in Argentina (t(155)=1.36, p=.175), though it replicated in b10 (men more correct, t(369)=4.39). [a10, b10]
- **Strict DI for simple items:** Trippas 2017 supports parallel processing for simple belief-bias syllogisms. [a16, a17]
- **Pure substitution:** Hoover and Healy found wrong reasoners remember the relational wording better than controls. Effects on confidence are tiny. [b15]

### 5.3 Moderators and boundary conditions

- **Task complexity:** parallel at low complexity, belief dominates at high complexity. [a17]
- **Signal strength:** extreme base rates increase the conflict cost; conflict can be missed when presented weakly. [a15]
- **Numeracy and mindware:** mindware instantiation, conflict detection and related variables explained about 10% of the variance in intuitive accuracy; technical training raised the 01 corrections. [d07, a11]
- **Practice:** repetition without feedback does not help. Training with an explanation does. [b13, a20]
- **Sample:** CRT means vary widely by population (0.57 at Toledo, 2.18 at MIT; 0.80 in Argentina). [a08, a10]

### 5.4 Interventions that worked and did not (humans)

| Worked | Did not work |
|---|---|
| Short explanation of the problem logic (first-response gain +30 to +58 points; lasted 2 months) | Repetition without feedback (61% stayed biased) |
| Showing base rates before the stereotype (lowers detection, raises decoupling) | Time pressure (null under intent-to-treat) |
| | Disfluent fonts (16 replications) |
| | Carrying the trained fix to another family (no transfer to algebra or other CRT-like items) |

---

## 6. Language models: behavior and what changed it

### 6.1 The old trap-falling model and its disappearance (Hagendorff, Fabi and Kosinski 2023; same paper counted once) [c01, c02, c03, a23-a25, d08]

- 10 OpenAI models, 150 CRT-style items (3 types x 50) plus 50 semantic illusions; humans N=455 (500 recruited, 45 excluded).
- CRT: intuitive (lure) rate: davinci-003 80%, humans 55%, ChatGPT-3.5 15%, GPT-4 0%. Correct: davinci-003 5%, humans 38%, ChatGPT-3.5 59%, GPT-4 96%. Semantic illusions: davinci-003 18% correct (72% lure), ChatGPT-3.5 74%, GPT-4 88%.
- "Let's use algebra" suffix on davinci-003: chain-of-thought 0% to 100%, correct 5% to 28%, lure 80% to 29%, atypical 15% to 43%.
- Told to answer briefly: ChatGPT-3.5 CoT 97% to 0%, correct unchanged (P=0.49); GPT-4 CoT 84% to 0%, correct 95% to 88%, lure 0% to 10%.
- Few-shot, same type: CRT type 2: 2% to 92% after 2 examples; type 3: 12% to 92% after 7; type 1: 0% to about 78% after 30. "Check the question for invalid assumptions" on semantic illusions: 18% to 54% (lure 72% to 28%); 10 or more examples: over 64%.
- Limits: items may be memorised; authors say RLHF or exposure explanations are untested; same-type examples may be pattern copying. Binz and Schulz 2022: original GPT-3 gave the lure on all three CRT items; small vignette rewordings broke it. [c04]

### 6.2 The trap returns when the principle changes [c17, d20, d16, d17, K11] [E]

- Ma et al. 2025 (5 LLMs on 50 CRT3 items; human comparison is 5 lab researchers, each answering 20% of items):
  - Number changes only (Exp I): average accuracy 86.8% on type A, 68.5% on type B, 53.1% on C, 20.9% on algebra version D.
  - Principle changes (Exp II): original 99.1% to modified 1.5% average; 95.9% of errors reused the old method on CRT1 (52.8% on CRT2); on modified CRT3, 71.5% to 85.7% treated the problem as exponential growth. Claude 3 fell 62.0% to 22.0% on modified CRT2 (chi-square(1)=14.82, p<.001). Human accuracy fell only 14%.
  - Exp III: o1-preview kept accuracy under number-only changes but averaged 10.0% on principle-changed items; 82.5% of its wrong answers reused the original solution.
- Phantom Recall (Mukhopadhyay et al. 2025): 25 famous puzzles, 149 perturbations, 11 LLMs near-perfect on originals. Human-checked accuracy on perturbed items: o3 59.73%, Gemini 2.5 Pro 58.39%, Claude Sonnet 4 54.36%, Gemini 2.5 Flash 48.32%, Claude 3.5 Sonnet 46.31%, GPT-4o 29.53%. A prompt of prohibitions ("do not use external knowledge, do not make assumptions") added 4.7 to 10.1 points on five open models and about 10% on closed models. Judge agreement with humans 71% (humans among themselves 90.7%).
- Unpuzzles (Malek et al. 2025): puzzle vs trivial version, o3 87.6 vs 74.2, Gemini 2.5 Pro 93.8 vs 62.9, o1 86.7 vs 59.8, Claude 3.7 Sonnet 77.3 vs 48.5, Claude 3.5 Sonnet 63.9 vs 27.8, GPT-4o 75.3 vs 19.6. Gap from 9.1 points (o3) to 54. Context-shifted wording (same logic, new surface) did better than the trivial version, so similarity to the famous original is part of the cause. 97 puzzles, 64 in the shifted subset; text of one sentence contradicted its own table (table used).
- Newest model tested in these sources: mid-2025. No 2026 model on CRT-style items.

### 6.3 When step-by-step reasoning (the LLM "System 2") helps and when it hurts

- **Helps on math, symbolic, logic** (Sprague et al. 2025 meta-analysis of over 100 papers plus 20 datasets and 14 models): mean CoT gain 14.2 (symbolic), 12.3 (math), 6.9 (logical) points; top three categories 56.9 with CoT vs 45.5 without; all others 56.8 vs 56.1. Best model gains up to 41.6 (MATH) and 66.9 (GSM8K), not averages. On MMLU, CoT matches direct unless the question or answer contains an equals sign. Plan plus tool solver beat plan plus CoT solver. Prompt-based CoT, mostly 2023-2024 models; compute matching is rare. [b05, b24, c13, b06] [E]
- **Hurts where thinking hurts people** (Liu et al. 2025, ICML; 2024-era models): artificial grammar (4,400 problems): GPT-4o 87.5% to 64.4% (-23.1 points); o1-preview 57.7% vs GPT-4o zero-shot 94.0% on a subset (that gap is 36.3 points; b08's wording as a CoT drop was wrong and is corrected here); Claude 3 Opus 70.7 to 62.7; other CoT drops reported 8.0 (Opus), 6.05 (Gemini), 8.8 (Llama 3.1 70B) on a 440-problem subset. Face recognition (500 problems): GPT-4o 64.0 to 51.2, Claude 3 Opus 44.0 to 29.6, Gemini 1.5 Pro 66.0 to 54.6, Claude 3.5 Sonnet 97.8 to 94.8; all six models worse. Classification with exceptions: rounds to learn labels GPT-4o 2.9 direct vs 12.5 CoT; Claude 3.5 Sonnet 2.3 vs 6.4; up to 331% more rounds. Claude 3.5 Sonnet was flat on grammar learning (65.9% vs 67.7%). [b08, c12, d15] [E] for the pattern, caveat on the human-to-model map.
- **The map failed in 3 of 6 tasks**, with a post hoc pattern: model has trained logic humans lack (logical inconsistency: GPT-4o 53.2% to 93.9% with CoT), lacks motor priors (spatial intuition: no significant change, GPT-4o 38 vs 40), or has more working memory (CoT helped, Claude 3.5 Sonnet 81 to 95). Bootstrap against 378 comparisons from Sprague: none of 100,000 resamples of 50 comparisons had a larger average drop. [d15, K26]
- **More thinking tokens lowers accuracy on some tasks** (Gema et al. 2025; constructed tasks; mid-2025 models): counting with distractors, regression with spurious features, deduction with constraint tracking, AI-risk probes. Claude models get more distracted; OpenAI o-series resist distractors but overfit to framing; few-shot largely fixes spurious-feature drift; all models lose focus on constraint-tracking (zebra puzzles). Tests one long attempt at various lengths, not several short ones at equal tokens. [c16, d19]
- **Three regimes in puzzles** (Shojaee et al. 2025): low complexity, non-thinking models match or beat thinking ones with fewer tokens; medium, thinking helps; high, both collapse. The collapse claim is disputed (token limits, unsolvable instances); the replies were not opened. [b09] [C]

### 6.4 Overthinking and cost [E] (K09)

- o1-like models used 1,953% more tokens on "2 plus 3"; one example produced 13 solutions; later solution rounds add little accuracy or strategy diversity; 2 to 4 rounds in 76-80% of QwQ cases and 59-63% of DeepSeek-R1 cases. Self-training cut tokens 48.6% on MATH500 with accuracy kept. [b07, b25, c14, c26] (one source, four lines)
- S1-Bench (Zhang et al. 2026): 422 simple questions (220 English, 202 Chinese, average 14.46 tokens), 28 reasoning models. Closed-source models used over 3x the tokens of small non-reasoning models. Weak models under 90% pass@1 (instruction-following 76.7%, knowledge 78.6%, reasoning 88.1%). 18 of 23 reasoning models did not shorten answers when they called the question easy. Length-reduction methods cut AIME tokens about 50% but only about 25% on S1-Bench. [c15]
- DynamicMind: normal mode was most efficient on 80.52% of GSM8K samples; slow helped 3.11%. [c20]

### 6.5 Shortest-of-k and parallel versus sequential [d12, d13, K23, K27]

- Hassid et al. 2025 (six reasoning models; AIME 2024/2025, HMMT 2025, GPQA-Diamond 198 questions): within one question the shortest chain beats a random one by up to 18.8 points and the longest by up to 34.5; shortest chains are 50% and 67% shorter. short-m@k (run k in parallel, stop when the first m finish, vote). At matched total thinking tokens short-1@k beat majority@k at low budgets (up to about 45k, 60k, 100k tokens for R1-32B, QwQ-32B, R1-670B) and lost at larger budgets. short-3@k beat majority at all budgets (+2% at 80k for QwQ-32B, about +4% at 100k for R1-670B). Up to 40% fewer thinking tokens for short-1@k at equal accuracy. The authors say harder questions still need longer reasoning.
- Gu et al. 2026 (DeepMind): at the same number of solutions, independent parallel samples with vote beat sequential refinement on AIME 2025 for Qwen3-14B, R1-distill-Qwen-14B and Gemini 2.5 Flash, and on coding. Aggregation and context length were ruled out; lack of exploration was the cause. Matches number of solutions, not total tokens.

### 6.6 System 1 / System 2 in agent designs

- SwiftSage (section 4.6). [c09, c10, d10]
- Tree of Thoughts: Game of 24, GPT-4 CoT 4% vs ToT 74% (model self-evaluates, which G5 distrusts). [c22]
- Talker-Reasoner: no benchmark numbers. Do not cite as a performance gain. [c11]
- Distilling System 2 into System 1 (Llama-2-70B-chat): last-letter task 30.0% zero-shot, 44.5% two-step Rephrase-and-Respond, 98.0% distilled direct answer (about 25 tokens); TriviaQA with opinion 51.6% (System 1), 76.0% (S2A), 81.3% (distilled S2A); GSM8k: System 1 zero-shot 9.40%, CoT zero-shot 36.39%, distilled CoT 7.13% (distillation fails on multi-step arithmetic; teacher targets only 56.81% accurate). Needs weight training. [c07]
- Lampinen et al. 2024 (mostly Chinchilla-family): content effects in NLI, syllogisms and Wason; models exceed humans in accuracy and in size of content effect on Wason; model answer probabilities line up with human response times; few-shot gives mild gains. [c05, c25]
- Beucler et al. 2025 (CCN abstract, N=151 humans): LLMs used to measure the pull of the base-rate heuristic. Snippet only. [c18]

### 6.7 Calibration and the stated "I am sure"

- Stated confidence is worse than sample consistency on older models (d05) and consistency itself is weak on a frontier model (d04). A model's remark that a question is easy does not predict shorter answers (18 of 23). [c15, K10]

---

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, M = memory (section 5 of the schema).

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence | Note |
|---|---|---|---|---|---|
| A1 | Do not use "slow down / be careful / think analytically" prompts or time-pressure style cues to switch modes. Mode is set by code. | G7, section 4b (already listed) | [E] | b03, b22, b17, a20 (contrast) | Cue families failed or were null under intent-to-treat (K06). Already in 4b; add the RRR and font evidence as support. |
| A2 | Keep a plain, short-answer arm as the baseline. Think briefly by default; deliberate on task type. | G11, S0 | [E] | b05, b24, c13, c12, d15, b07, c15, c14 | CoT gain is concentrated in symbolic and math (14.2, 12.3, 6.9 points); other categories 56.8 vs 56.1. |
| A3 | Gate S0 on separately logged task cues (has a computation or equals sign, multi-step, has a candidate to test, known family), not on the label "hard" or "slow". | S0 | [E] for the cue; gate design [C] | b05, b24, c13, d01, d02, d03 | The equals-sign cue captured most MMLU benefit. Whether it matches a trained switch is untested (K22). |
| A4 | Keep a no-deliberation arm for pattern, perception, rule-with-exceptions and distractor-heavy tasks. | G11 | [E] | b08, c12, d15, c16, d19 | Our ARC-like tasks are closest to the harmed classes. The human-to-model map failed in 3 of 6 tasks, so it is a prior only (K26). |
| A5 | Stop after the first passing S4 check on easy items. Do not add scheduled rechecks. | G1, G12, S4 | [E] | b07, b25, c14, c26, c15, c20 | Log the index of the first correct solution. |
| A6 | Known-lure list per problem family. Code flags any attempt that equals a lure and routes it to a check. | S4, M | [E] | b10, a08, b01, b13 | 64.9% of bat-and-ball answers are the one lure; 94.9% of wrong first responses. |
| A7 | Test the base model on principle-changed items before adding a deliberation operator. Treat famous-item success as possible memory. Any perturbation in S4 must change the principle, not the numbers. | G3, S4 | [E] | c01, c04, c17, d20, d16, d17, b11 | o1-preview 10.0% on principle-changed items; o3 59.73% on perturbed puzzles. |
| A8 | Mode choice is an output-style toggle controlled in code (template per class, hard token cap, answer parsed from a fixed slot). Log the text before the answer. | S0 | [E] for toggle in older models; [S] for current | c02, a24, d18 | The direct arm is partly a step-by-step arm unless capped. |
| A9 | Plan with the model, execute symbolic steps in a program. | G1 | [E] | b06, b05, c13 | Plan plus tool solver beat plan plus CoT. |
| A10 | Fix revisions to outside signal. Repeated practice without outside feedback does not de-bias; a spoiled right answer (10) costs 3.2% to 9.3% against 6.0% to 25.3% corrections. | G2 | [E] with G2 | b13, a19, d07 | The ratio of 01 to 10 changes by task, so log it per family. |
| A11 | Log fast and slow arms separately: 00 / 01 / 10 / 11 per item per family; log detection and repair separately. | Section 6 logging | [E] as method | a18, a19, a13, d07 | Gives first-pass accuracy per family (K04). |
| A12 | Count unfinished items as failures; randomise assignment of items to arms in every fast-vs-slow test. | G7 | [E] | b03, b22 | The RRR conditioned on compliance and got a false effect. |

### 7.2 Test first

| # | Item | Schema part | Status | Evidence | Test |
|---|---|---|---|---|---|
| T1 | Sample disagreement over 3 short samples as an error signal. | S0, S6 | [C] | d05, d04 | Test vs stated uncertainty and vs the family running pass rate (K21). Log only until it beats the base rate. |
| T2 | A cheap structural gate recovers most of the best-mode gain. | S0 | [C] | d11, d14, b24 | K22: mixed set, equal tokens. |
| T3 | Per-family learned direct route (use direct mode where first-pass accuracy is already high). | S0, M | [C] | d07, d06, b21 | K04: check the skip loses no accuracy. |
| T4 | Verified worked example per family in the first-pass prompt. | S9, M | [C] | a20, d06, d08, a25 | K25: test on number-changed, principle-changed and different-family variants. |
| T5 | S1 input hygiene (cleaned text only to the solver). | S1 | [S] | c06, c24, d09 | K12: with and without the block visible. One lab, one model. |
| T6 | SwiftSage-style triggers as the impasse detector. | S6 | [S] | c09, c10, d10 | K13: trigger set vs always-deliberate at equal tokens. |
| T7 | Independent retries (fresh context) after a flagged first answer, not retries that see the earlier answer. | S6, S3 | [S] | d13, d12 | K27, K23. |
| T8 | A few short independent attempts with early stop and a code selector vs one long attempt. | G11, S6 | [C] | d12, d13, d19 | K23: fixed total tokens, split by class. |
| T9 | Constraint prompt ("no external knowledge, no assumptions") on trap-prone items. | S1 | [S] | d16, c03 | Gave +4.7 to +10.1 points on open models and about +10% on closed in one study. Check at equal tokens against a generic careful line. |
| T10 | Restating a perturbed problem in new surface form before solving (context shift). | S1, S4 | [S] | d17 | Context-shifted wording did better than the trivial version, but not tested as an agent step. |
| T11 | Counterexample search / abstract variables to remove content bias on logic items. | S7, S4 | [S] | c05 | Content effects exist in models. |
| T12 | Whether a continuous-depth dial (direct, one check, full steps) beats a binary gate. | S0 | [C] | d02, d14 | No study tested it (K01). |

---

## 8. Concrete tests on our bench

All tests: both arms get the same total tokens, setup cost included (G7). Items are novel variants, never the famous forms. Unfinished items count as failures. Items are randomly assigned to arms. Log the text before the answer and the path through the graph.

**Test 1. Perturbation of CRT-style traps (K11, K24).**
- Item type: 40 items. 10 famous CRT/puzzle originals, 10 number-changed, 10 principle-changed (additive to non-additive cost; worker-dependent to independent; exponential to linear), 10 new-family trap items.
- Arms: (a) plain short answer with a hard code cap, (b) plain plus S4 perturbation check that changes the principle, (c) step-by-step.
- Metric: accuracy per item class; lure rate; first-pass accuracy per class.
- Expected effect: near-ceiling on originals and number-changed; lure reuse on principle-changed in (a) (Ma 2025: o1-preview 10.0%; Phantom Recall: 54% to 60% at best for 2025 models); (b) and (c) help on principle-changed if the check changes the principle. Unknown for current models; run before building anything.

**Test 2. Gate on structural cues vs fixed modes (K07, K22, K26).**
- Item type: mixed set: arithmetic, multi-step word problems, grid pattern, perceptual match, rule learning with exceptions, distractor items.
- Arms at equal total tokens: always-direct, always-steps, hand-rule gate (numbers, equals sign, multi-step cue, known family), family pass-rate gate.
- Metric: accuracy per class and overall; tokens; share of the best-mode gain recovered ((gate - worst) / (best - worst)).
- Expected effect: hand-rule gate recovers most of the best-mode gain on math classes (ThinkSwitcher recovered about 90% at about 71% of tokens on math); steps hurt on pattern, perception and exceptions classes (GPT-4o 87.5% to 64.4% on grammar).

**Test 3. Sample-disagreement signal (K21, K03).**
- Item type: perturbed trap items plus ordinary items.
- Arms: 3 short samples per item; predict a wrong first answer from (a) disagreement, (b) stated uncertainty, (c) the family running pass rate, (d) constant rule.
- Metric: AUROC; accuracy of the routed result at equal tokens.
- Expected effect: disagreement beats stated uncertainty (older models); may fail on traps because all samples share the lure (gpt-4.1: 48% wrong at agreement of 0.8 or more). If (c) matches (a), drop (a).

**Test 4. Length caps and parallel short attempts (K23, K27).**
- Item type: per class (math, symbolic, pattern, distractor, constraint tracking).
- Arms at fixed total tokens: (a) one long attempt, (b) 3 short independent attempts plus code selection, (c) 4 short attempts with early stop, (d) 2 attempts where the second sees the first.
- Metric: accuracy per class.
- Expected effect: (b) and (c) beat (a) at low to medium budgets on hard math (Hassid: +2% to +4%); (a) may win on the hardest classes; (d) loses to (b) (Gu 2026).

**Test 5. Worked example per family (K05, K25).**
- Item type: one family; held-out variants: numbers changed, principle changed, different family.
- Arms: verified worked example in the first-pass prompt vs a generic "think carefully" line vs plain.
- Metric: first-pass accuracy per variant type.
- Expected effect: large on numbers-changed (davinci-003 2% to 92%), small or none on principle-changed and different-family (d06, d20).

**Test 6. Input hygiene (K12).**
- Item type: opinion QA and arithmetic with irrelevant sentences, plus items with a stated guess.
- Arms: (a) raw, (b) cleaned text only, (c) cleaned beside original, (d) code filter that moves the guess to a marked block.
- Metric: accuracy; sycophancy rate.
- Expected effect: (b) above (a) and above (c) (62.8 to 80.3; 74.5 with original kept); unknown for current models.

**Test 7. SwiftSage-style triggers (K13).**
- Item type: stepwise tool task set.
- Arms: always-deliberate vs triggered (no new verified evidence in N steps, tool or format error, before final answer, unexpected tool result) vs fast-only.
- Metric: accuracy and tokens per task; per-trigger firing log and ablation.
- Expected effect: fewer tokens at similar accuracy; fast-only may win on short tasks (78.68 vs 72.81 in the original).

**Test 8. Fast-correct share per family (K04).**
- Item type: each task family in the bench.
- Arms: first pass capped short vs full-budget pass.
- Metric: 00 / 01 / 10 / 11 shares per family; skip rule: if 11 share is high and 10 share low, route direct.
- Expected effect: share varies by family; do not assume a constant.

**Test 9. Prompts that claim to switch modes (K06).**
- Item type: mixed set.
- Arms: plain vs "think carefully / be analytic" prefix vs "be fast".
- Metric: accuracy at equal tokens.
- Expected effect: no reliable gain (section 4b already says so); confirm on our model.

---

## 9. What does not transfer, and why

1. **Time pressure and cooperation findings.** They tested whether fast decisions make people prosocial. The causal claim was refuted (-0.37 vs 8.6), and it is not about reasoning accuracy. [K16]
2. **Working-memory load as a mechanism.** The two-response paradigm uses load and deadlines to block Type 2. An LLM has no working-memory load switch; a token cap is a different intervention, and visible reasoning can persist (99.9% in one model with thinking off). [d18]
3. **Feeling of rightness, feeling of error, response times.** Human self-report and reaction time. For models the only analogues are sample spread and token statistics, and those are weak on frontier models (d04). [a12, d04]
4. **Human training effects (explanation of logic).** The model analogue is a same-family worked example, which may be pattern copying (d08). Human transfer failed across families (d06). [K25]
5. **The CRT as a clean measure.** It mixes numeracy and exposure. For an LLM, items are contaminated by training data; use perturbed items. [a11, b11, c04]
6. **Mapping from human harm of deliberation to model harm.** Worked for 3 of 6 tasks; failed where the model has trained logic, lacks motor priors, or has more working memory. Pattern is post hoc. [d15]
7. **Methods that require training.** Dualformer, ACPO, ThinkSwitcher, distillation, self-training for overthinking, learned three-way router. They show difficulty-aware allocation is possible but not how to get it from prompts. [c08, c21, d11, d14, c07, b07]
8. **Talker-Reasoner.** No results. [c11]
9. **Population claims from WEIRD online and student samples** (bat-and-ball, base-rate items). Transfer to a coding or science agent is by analogy only.
10. **Persona-style dual-process prompts** ("you are System 2"). No evidence in this folder; G4 already bars persona voters.
11. **The strict DI time order.** A fast-then-slow order is not a fixed fact: the CRT mouse-tracking data fit DI, simple belief-bias data fit parallel processing, and fast-correct answers fit neither cleanly. Do not hard-wire the order. [K14]

---

## 10. Open questions

From the critique and gap search (some partly informed):

1. Does a model's own first-pass signal (disagreement across 3 short samples, token entropy, stated doubt) predict a wrong first answer better than the class pass rate or a constant rule on perturbed items in a modern model? Partly informed: sample disagreement beat stated confidence on older models (d05); agreement is weak and over-confident on gpt-4.1 (d04). Nobody compared it to the class base rate. [K21]
2. How much of the best-mode gain does a cheap structural gate recover at equal tokens on a mixed set with pattern, perception and distractor items? Only math data exist (d11, d14). [K22]
3. Do 2026 frontier models, brief-prompted, still fall for principle-changed CRT-style traps, and does an S4 perturbation check that changes the principle fix it? No 2026 source. [K11, K24]
4. One long attempt versus 3 to 4 short independent attempts at fixed total tokens, split by class. Nearest: d12, d13, d19. [K23]
5. What is the real fast-correct share? Bago and De Neys 2017 (75% to 88%) was not re-verified; re-measures give about 53% on the CRT and 56% to 84% in bat-and-ball; one report gives 20.1%. The "20% to 39%" figure in the gap text was not found in a source opened. [K04]
6. Is System 2 Attention reproduced on current models or by other labs, and does it hold when the cleaning is done by a different model or a code filter? No replication found. [K12]
7. Do the single-process and multi-dimensional critiques predict a different design than a task-feature gate? Both are conceptual (d01, d02). Pennycook and colleagues' reply to Melnikoff and Bargh and Osman 2004 follow-ups were not read. [K01]
8. Does the SwiftSage trigger set work as an impasse detector on non-simulator tasks, and which trigger matters? No ablation. [K13]
9. Does a verified worked example raise first-pass accuracy on principle-changed held-out variants in a modern model, or only on items that look like the example? [K05, K25]
10. Which of the six Liu 2025 tasks are close to our task classes, and can a rule predict the three exceptions in advance? [K26]
11. Is a continuous-depth dial better than a binary gate? No head-to-head test. [K01]
12. Shojaee 2025 three-regime result: the dispute (token limits, unsolvable instances) was not examined. [b09]
13. Does the Rand/RRR experience moderator (practice changes the default) apply to a model that sees the same family often? Only the post hoc human story. [b21]

---

## 11. Sources

[V] = opened (page or PDF text read in a research pass). [M] = snippet or abstract only, or cited second-hand. The critique notes that Bago and De Neys 2017 (a18, a19) could not be re-opened, and Frederick 2005, Toplak 2011, Shojaee 2025 (equal-budget pairing), Gema 2025, and Rand 2014 were not re-opened in the cross-check; they are [V] from the first pass.

**Theory and review**
- [V] Evans and Stanovich (2013), Dual-process theories of higher cognition: advancing the debate. https://scottbarrykaufman.com///wp-content/uploads/2014/04/dual-process-theory-Evans_Stanovich_PoPS13.pdf (a01-a04, d03)
- [V] Osman (2004), An evaluation of dual-process theories of reasoning. https://link.springer.com/content/pdf/10.3758/BF03196730.pdf (a05-a07)
- [V] Keren and Schul (2009), Two is not always better than one. https://pluto.huji.ac.il/~mschul/yaacov_schul_files/2009-keren&schul-2systems.pdf (d02). Earlier lines b19 were [M] (title and count only).
- [V] Melnikoff and Bargh (2018), The mythical number two. https://acmelab.yale.edu/sites/default/files/melnikoff_bargh_2018_mythical_number_2_0.pdf (d01). Earlier line b18 was [M]; DOI https://doi.org/10.1016/j.tics.2018.02.001
- [M] Sloman (1996), The empirical case for two systems of reasoning. https://doi.org/10.1037/0033-2909.119.1.3 (a22)
- [M] Wason and Evans (1974); Evans and Over (1996). https://doi.org/10.1016/0010-0277(75)90001-6 (a26)
- [M] Kahneman and Frederick (2002), Representativeness revisited. https://doi.org/10.1017/CBO9780511808098.004 (a27)
- [M] Thompson, Prowse Turner and Pennycook (2011); De Neys and Glumicic (2008); De Neys (2012), cited in opened papers. https://link.springer.com/content/pdf/10.3758/s13421-016-0680-1.pdf (a21)
- [M] Franssens and De Neys (2009), search snippet. https://faculty.weber.edu/eamsel/Research%20Groups/Dual%20PRocess%20Research/New%20Papers/Franssens&DeNeys%20(2009).pdf (c19)
- [M] Pennycook and colleagues' 2018 reply to Melnikoff and Bargh, search summary only (mentioned in d01).

**Human experiments, replications, individual differences**
- [V] Frederick (2005), Cognitive reflection and decision making. https://pdf.stafforini.com/frederick-2005-cognitive-reflection-and.pdf (a08, a09)
- [V] Campitelli and Labollita (2010). https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2EA5389B4D2E8840B485E55BD3ED0B47/S1930297500001066a.pdf/div-class-title-correlations-of-cognitive-reflection-with-judgments-and-choices-div.pdf (a10)
- [V] Sinayev and Peters (2015). https://www.frontiersin.org/articles/10.3389/fpsyg.2015.00532/pdf (a11)
- [V] Toplak, West and Stanovich (2011). https://link.springer.com/content/pdf/10.3758%2Fs13421-011-0104-1.pdf (b12, b23)
- [V] Pennycook, Cheyne, Koehler and Fugelsang (2016). https://link.springer.com/content/pdf/10.3758/s13428-015-0576-1.pdf (b10, b11)
- [V] Gangemi, Bourgeois-Gironde and Mancini (2015). https://apc.it/wp-content/uploads/2014/10/Feelings-of-error-in-reasoning-rev.pdf (a12)
- [V] Pennycook, Fugelsang and Koehler (2015), three-stage model. https://zenodo.org/records/1067049/files/article.pdf (a13-a15)
- [V] Trippas, Thompson and Handley (2017). https://link.springer.com/content/pdf/10.3758/s13421-016-0680-1.pdf (a16, a17)
- [V first pass, not re-verified] Bago and De Neys (2017), Fast logic? https://sapere-aude.group/read/_graduated/wangmeng/Source_Files/2021-04-25-WM1.pdf (a18, a19)
- [V] Boissin, Caparos, Voudouri and De Neys (2022), Debiasing System 1. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3CF9452965581BDFD9A697C5B9F2E6AD/S1930297500008895a.pdf/div-class-title-debiasing-system-1-training-favours-logical-over-stereotypical-intuiting-div.pdf (a20; full text via HAL in the critique)
- [V] Boissin, Caparos, Raoelison and De Neys (2021), From bias to sound intuiting. https://hal-univ-paris.archives-ouvertes.fr/hal-03161167/file/preprint_training_batandball.pdf (d06)
- [V] Buric and Konradova (2021), Mindware instantiation. https://journals.savba.sk/index.php/studiapsychologica/article/download/216/61 (d07)
- [V, text opened in critique pass] Bago and De Neys (2019), The smart System 1. https://hal.science/hal-02106554 (b20); full text https://hal.science/hal-02106554/document
- [V] Travers, Rolison and Feeney (2016). https://pureadmin.qub.ac.uk/ws/files/37661618/Travers_Rolison_Feeney_Cognition_2016.pdf (b01, b02)
- [V, web summary tool] Raoelison and De Neys (2019). https://dlab.sauder.ubc.ca/sjdm/journal/18/181112/jdm181112.html (b13)
- [V] Raoelison, Keime and De Neys (2021). https://link.springer.com/content/pdf/10.3758/s13421-021-01140-x.pdf (b14)
- [V, web summary tool] Hoover and Healy (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6800670 (b15)
- [V] Lawson, Larrick and Soll (2022). https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F7FDED785C4695924D6D52C6D5830A2D/S1930297500009396a.pdf/div-class-title-when-and-why-people-perform-mindless-math-div.pdf (b16)
- [V] Bouwmeester et al. (2017), RRR of Rand, Greene and Nowak. https://www.stir.ac.uk/research/hub/file/1084325 (b03, b22)
- [V] Rand et al. (2014), Social heuristics shape intuitive cooperation. https://www.nature.com/articles/ncomms4677.pdf (b04, b21)
- [M] Meyer et al. (2015), Disfluent fonts. https://digitalcommons.chapman.edu/cgi/viewcontent.cgi?article=1095&context=esi_pubs (b17, abstract only)
- [M] Beucler et al. (2025), CCN abstract. https://2025.ccneuro.org/abstract_pdf/Beucler_2025_Computational_Modeling_Heuristic_Base-rate_Integration_Reasoning.pdf (c18)

**Language-model studies**
- [V] Hagendorff, Fabi and Kosinski (2023), Thinking fast and slow in large language models / Human-like intuitive behavior and reasoning biases emerged in LLMs but disappeared in ChatGPT (one paper). https://arxiv.org/pdf/2212.05206 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC10766525 ; https://arxiv.org/pdf/2212.05206v2 (a23-a25, c01-c03, d08)
- [V] Binz and Schulz (2022). https://arxiv.org/abs/2206.14576 (c04)
- [V] Lampinen et al. (2024). https://arxiv.org/abs/2207.07051 (c05, c25)
- [V] Weston and Sukhbaatar (2023), System 2 Attention. https://arxiv.org/abs/2311.11829 ; https://arxiv.org/pdf/2311.11829 (c06, c24, d09)
- [V] Yu et al. (2024), Distilling System 2 into System 1. https://arxiv.org/abs/2407.06023 (c07)
- [V] Su et al. (2025), Dualformer. https://arxiv.org/abs/2410.09918 (c08)
- [V] Lin et al. (2023), SwiftSage. https://arxiv.org/abs/2305.17390 ; https://arxiv.org/pdf/2305.17390 (c09, c10, c23, d10)
- [V, abstract and introduction only] Christakopoulou et al. (2024), Talker-Reasoner. https://arxiv.org/abs/2410.08328 (c11)
- [V] Sprague et al. (2025), To CoT or not to CoT. https://arxiv.org/pdf/2409.12183 ; https://arxiv.org/abs/2409.12183 (b05, b06, b24, c13)
- [V] Chen et al. (2025), Do NOT think that much for 2+3=? https://arxiv.org/pdf/2412.21187 ; https://arxiv.org/abs/2412.21187 (b07, b25, c14, c26)
- [V] Liu et al. (2025), Mind your step (by step). https://arxiv.org/pdf/2410.21333 ; https://arxiv.org/abs/2410.21333 (b08, c12, d15)
- [V; equal-budget pairing not re-read] Shojaee et al. (2025), The illusion of thinking. https://arxiv.org/pdf/2506.06941 (b09)
- [V] Zhang et al. (2026), S1-Bench. https://arxiv.org/abs/2504.10368 (c15)
- [V] Gema et al. (2025), Inverse scaling in test-time compute. https://arxiv.org/abs/2507.14417 ; https://arxiv.org/pdf/2507.14417 (c16, d19)
- [V] Ma et al. (2025), Do LLMs truly grasp mathematics? https://arxiv.org/abs/2410.14979 ; https://arxiv.org/pdf/2410.14979 (c17, d20)
- [V, abstract, introduction and results text] Li et al. (2025), DynamicMind. https://arxiv.org/abs/2506.05936 (c20)
- [V] Cheng et al. (2025), ACPO. https://arxiv.org/abs/2505.16315 (c21)
- [V] Yao et al. (2023), Tree of Thoughts. https://arxiv.org/abs/2305.10601 (c22)
- [V] Ding (2026), When LLMs agree, are they right? https://arxiv.org/pdf/2607.08065 (d04)
- [V] Lyu et al. (2025), Calibrating LLMs with sample consistency. https://object.cloud.sdsc.edu/v1/AUTH_da4962d3368042ac8337e2dfdd3e7bf3/ml-papers-txt/AAAI/2025/calibrating_large_language_models_with_sample_consistency__c93d278a.txt (d05)
- [V] Liang et al. (2025), ThinkSwitcher. https://arxiv.org/pdf/2505.14183 (d11)
- [V] Hassid et al. (2025), Don't overthink it. https://arxiv.org/pdf/2505.17813 (d12)
- [V] Gu et al. (2026), parallel vs sequential sampling. https://arxiv.org/pdf/2604.05868 (d13)
- [V] Kassenaar et al. (2026), Learning when to think. https://arxiv.org/pdf/2608.20256 (d14)
- [V] Mukhopadhyay et al. (2025), Phantom Recall. https://arxiv.org/pdf/2510.11812 (d16)
- [V] Malek et al. (2025), Frontier LLMs still struggle with simple reasoning tasks. https://arxiv.org/pdf/2507.07313 (d17)
- [V] Lei et al. (2026), Thinking inertia. https://arxiv.org/pdf/2610.11765 (d18)

Data-quality notes: d04 is course-assignment data without preregistration; d17 contains a sentence that contradicts its own table (table used); d16 and d17 test mid-2025 models; Ma 2025 human comparison is five researchers; b13 and b15 were read through a web summary tool, not the PDF; c20 router dataset is self-built; several "agent relevance" lines in the evidence state schema rules as if the study tested them, which the studies did not.
