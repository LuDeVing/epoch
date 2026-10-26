# Question wording and presupposition: deep document

*Subfield A15.04. Focus: leading verbs alter recalled facts (Loftus and Palmer 1974). Why it matters for our agent: S1 input hygiene. Evidence ids (a01 to d25) and claim ids (A15.04-K01 to K32) refer to evidence_a-d.jsonl and claims.jsonl in this folder. Numbers marked as re-opened were checked against source text in critique.md.*

---

## 1. What it is

The wording of a question carries information. A question can contain:

- a **loaded word** (a verb such as "smashed" instead of "hit"),
- a **presupposition** (an assumption the question takes for granted, such as "the broken headlight" which assumes a headlight was broken),
- a **stated belief or a suggested answer** (the user says "I think the answer is X"),
- a **frame** (positive or negative, question or statement).

People who answer such a question often take the wording as a fact. Their answer shifts. In the strongest version, a later memory report also shifts: they report details that were never in the event.

Four related literatures sit under this heading.

1. **Human suggestibility.** Loftus and Palmer (1974) and the misinformation-effect work that followed. One word in a question changes a numeric estimate and a later recall report.
2. **Presupposition in language.** Definite articles, factive verbs, wh-words and other triggers make a hearer accept background content without checking it.
3. **False-premise questions for language models.** Benchmarks of real questions that contain a wrong assumption (CREPE, QA2, FalseQA, Cancer-Myth).
4. **Sycophancy and framing in language models.** Models move toward a belief, a suggested answer or a frame placed in the prompt.

For our agent the question is narrow. S1 (UNDERSTAND) restates the task and moves suggestive material into a marked block. This subfield asks: what suggestive material matters, how large is its effect, what removes it, and what do the removal steps cost on clean inputs?

Short answer from this study:

- In humans the direction is solid, the size is unstable, and the "memory is changed" reading is contested.
- In language models, a stated belief, a suggested answer, a false premise and a format change all move answers by large amounts. These are established.
- Nobody has run the Loftus-Palmer graded-verb manipulation directly on a model (K24, c23, d25).
- Blanket "check the premise" steps have a measured cost on clean questions. Any hygiene step must be reported with its false-flag rate (K26).

---

## 2. History and theories in depth

### 2.1 The founding studies (Loftus and Palmer 1974)

Source: a01-a04, b01-b06, c01. Full paper opened.

**Experiment 1.** Students (N=45, about 9 per verb) watched 7 short traffic-safety films. They then answered: "About how fast were the cars going when they [verb] each other?" Only the verb changed.

| Verb | Mean estimate (mph) |
|---|---|
| smashed | 40.8 |
| collided | 39.3 |
| bumped | 38.1 |
| hit | 34.0 |
| contacted | 31.8 |

Quasi-F F'(5,55)=4.65, p<.005. The quasi-F treats verbs as fixed and subjects and films as random (Clark 1973). The paper gives no effect size and no per-verb SD.

The true speeds of four staged crashes were 20, 30, 40 and 40 mph. Mean guesses for those were 37.7, 36.2, 39.7 and 36.1 mph. So the wording moved answers by about 9 mph between the extreme verbs, while a 20 mph change in true speed barely moved them.

**Experiment 2.** N=150, 50 per group (smashed, hit, no speed question). A 4-second accident film. One week later all were asked: "Did you see any broken glass?" There was none.

| Group | Yes | No | P(yes) |
|---|---|---|---|
| smashed | 16 | 34 | .32 |
| hit | 7 | 43 | .14 |
| control | 6 | 44 | .12 |

chi2(2)=7.76, p<.025. Speed estimates in Exp 2: smashed 10.46 mph, hit 8.00 mph, t(98)=2.00, p<.05.

**Partial mediation.** The speed estimate explains only part of the glass effect. At equal speed guesses the smashed group still said yes more often. P(yes to glass) by speed guess 1-5 / 6-10 / 11-15 / 16-20 mph: smashed .09 / .27 / .41 / .62; hit .06 / .09 / .25 / .50. The average gap fell from .18 to about .12. This is one study (K04, single-source).

**The authors' two accounts.** (1) Response bias: when unsure, the person picks the answer the wording leans toward. (2) Memory change: the wording is merged with the original perception into one memory and the person cannot separate them. Their data did not choose between the two (b06).

**Earlier roots.** Carmichael, Hogan and Walter (1932): labels change how people redraw ambiguous figures. Daniel (1972): labels change recognition. Harris (1973): "how tall" versus "how short" gives higher height guesses under "tall" (second-hand only, a15).

### 2.2 The article and presupposition studies

- **Loftus and Zanni (1975).** "Did you see *the* broken headlight?" against "*a* broken headlight". The definite article presupposes the headlight exists. Reported figures: 17% yes after "the", 7% after "a" (a13). Seen only in a secondary summary; original not opened. Treat as single-source and unconfirmed.
- **Davis and Schiffman (1985).** A natural experiment, N=28, 4 critical questions. A substitute instructor asked about traits the first instructor lacked. Possessive form: yes 17.3%, no 69.2%. Indefinite article: yes 5.0%, no 90.0%. chi2(2)=7.76, p<.05 (a12). Opened.
- **Loftus, Miller and Burns (1978).** The standard three-stage design. Slides show a car at a yield sign. A later question mentions the stop sign. Misled people later choose the stop sign more. Cell numbers not read (a14).

### 2.3 The critique: guessing, not memory change

**Weinberg, Wadsworth and Baron (1983)** (a05). N=331 (329 analysed). They re-ran the stop/yield design and added a test where the misleading "stop" answer cannot be chosen (yellow yield versus red yield).

| Test | Accurate question | Misleading question |
|---|---|---|
| stop vs yield | .926 (n=82) | .626 (n=83) |
| yield vs red yield | .775 (n=80) | .604 (n=86) |

Main effect of question type F(1,327)=25.42, p<.001. A residual deficit remained on a test designed to remove guessing. They read this as support for a real effect beyond demand.

**McCloskey and Zaragoza (1985)** (a06, a07). Six experiments. Exp 1: 120 students (60 per test group), 79 slides, 4 critical items with 3 versions each, 36-item forced choice.

- Original test (the misleading item is one of the choices): misled 37% correct versus control 72%. A gap of about 35 points (27 to 39 across experiments).
- Modified test (the misleading item is not offered; the choice is between the original and a new alternative): misled 72% versus control 75%.

Their argument: people who never encoded the detail guess. Misled people who remember the suggestion pick it. This yields the original gap with no change in memory. Worked table: 40% remember the true detail, 60% do not. Control = 40% + 30% (half of the others guess right) = 70%. Misled without any memory effect, if half of non-rememberers recall the suggestion = 40% + 15% = 55%. If only 30% remember: 30% + 15% = 45%.

They also argue that the Weinberg yield versus red yield test still allows guessing. The dispute is not resolved (K05, K06 contested). A reply by Loftus, Schooler and Wagenaar, which reports a small effect on a more sensitive test, was seen only as a snippet.

### 2.4 Source monitoring (Lindsay and Johnson 1989)

Source: a08-a10. Opened.

- Exp 1. Items that appeared only in the misleading text, claimed as seen (max 8). Yes/no test: misled 5.52 versus control 2.67, F(1,52)=33.05. Source-monitoring test (picture, text, both, neither): misled 2.56 versus control 2.41, F<1. Interaction F(1,104)=13.30. Misses did not rise.
- Exp 2 (milder warning, cover story, N=132 analysed, 33 per cell). Yes/no: 3.91 versus 2.30, F(1,64)=13.11. Source test: 1.39 versus 1.33, F<1. Interaction F(1,128)=8.06.

Meaning: the suggestibility effect vanished when people were asked where each item came from. Both traces coexist. The error is in attributing the source. This is the strongest human result for our agent, because it suggests a **source-tag step** may remove the effect (K07, established on two experiments from one lab group).

### 2.5 Theories compared

Lindsay and Johnson (a10) and Ayers and Reder (1998, a11) review the accounts:

| Account | Claim | Main support | Main problem |
|---|---|---|---|
| Overwriting / trace alteration (Loftus) | The new item replaces the old trace | Original-test gap | Vanishes on the modified test (M and Z) |
| Blocking / accessibility | The old trace exists but is hard to reach | Bekerian and Bowers 1983; Christiaansen and Ochalek 1983 | Needs retrieval tests |
| Non-retention (M and Z) | Never encoded; people guess | Modified test 72% vs 75% | Weinberg residual deficit |
| Source monitoring (L and J) | Both traces stored; wrong source assigned | Source test removes the effect | Needs a source test to show it |
| Source of activation confusion (SAC, Ayers and Reder) | Activation spreads between concepts and the source link is lost | Fits many moderators | Model-level, few direct tests |
| Fuzzy-trace / gap-filling (2024 review, b24) | Gist traces are more malleable; wording works as a recollection cue | Review | No numbers in the part read |

The accepted reading today: no single account wins. Guessing, source confusion and some real trace effect all contribute. The mix depends on test type.

### 2.6 Moderators found later

- **Warnings** (Blank and Launay 2014 meta-analysis, via a secondary summary only; b29). They reduce but do not remove the effect, less so with recall tests and more exposures.
- **Repetition** (O'Donnell et al. 2023, b26). Repetition meta-analysis k=19: Hedges g=0.38 [0.18, 0.59], with funnel asymmetry (Egger t(17)=-2.98, p=.01). Source variability k=8: g=-0.01 [-0.18, 0.15]. Own experiments: g=0.47 and 0.27.
- **Perceptual load** (Murphy and Greene 2016, a16, a17). Higher load at encoding raises the pull of leading questions. In a driving simulator, speed of the red car: high load regular 22.7 versus leading 71.9 km/h; low load 30.0 versus 40.5. Load by question interaction F(1,75)=17.95, p<.001, partial eta2=.19. Video experiment 1B: time in room, high load regular 25.1 s versus leading 96 s (F(1,108)=7.03, p=.008); low load 26.5 versus 76.1 s.
- **Question order** (Michael and Garry 2016, a18). Order of non-leading questions changes confidence; easy-first order made people feel more accurate. Six experiments; Exp 1a N=102; difficulty ratings correlated with confidence r=-.82.
- **Cognitive ability** (2024 systematic review, b23, 9 studies, 23 associations, narrative only). Higher ability goes with lower susceptibility; nobody is immune.

### 2.7 The machine line

Parallel line, mostly independent of the human literature:

- 2020: misprimed cloze probes on BERT (c02); presupposition in NLI (IMPPRES, c03).
- 2021-22: prompt format sensitivity (Calibrate Before Use, c18; Webson and Pavlick, c17); human-bias tests on Codex (Jones and Steinhardt, c19).
- 2022-23: false-premise QA benchmarks (CREPE, QA2, FalseQA; b08, b10, b13); sycophancy (Perez 2022, Sharma 2024, Wei 2023); suggested-answer bias (Turpin 2023).
- 2024-26: reasoning-model premise handling (Fan 2025, Sathyanathan 2026), medical premises (Cancer-Myth 2025), framing and multi-turn contamination (2026 cluster d01-d24).

---

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources), **S** single-source, **C** contested, **H** human-only, **O** older models only.

### 3.1 Human findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| One verb shifts speed estimates in force order | smashed 40.8, collided 39.3, bumped 38.1, hit 34.0, contacted 31.8 mph; N=45; F'(5,55)=4.65, p<.005 | Loftus and Palmer 1974 Exp 1 (a01, b01) | S, H |
| Wording moves answers more than the event does | true speeds 20/30/40/40 mph gave means 37.7/36.2/39.7/36.1 | a01, b02 | S, H |
| A week later "smashed" raises false broken-glass reports | .32 vs .14 vs control .12; N=150; chi2(2)=7.76, p<.025 | L and P Exp 2 (a02, b04) | E (L and P + Zhou 2026 direction), H |
| The speed estimate only partly mediates | gap .18 down to about .12 | a03, b05 | S, H |
| Large conceptual replication in a simulator | high load 22.7 vs 71.9 km/h; interaction partial eta2=.19 | Murphy and Greene 2016 (a16) | S, H |
| Small replications go the same way | Zhou 2026 N=60: 87.93 vs 54.16 km/h, t=3.82; glass 69.0% vs 32.3%, chi2(1)=8.08. Hickman 2017 N=20: 39.63 vs 47.75, t(18)=-1.21, not significant | a19, a20 | C |
| A 2017 sport replication failed | hockey clip; contact, bump or smash gave no difference in perceived speed (Exp 1); sample size not seen | Goldschmied et al. 2017 (d16) | C |
| Original recognition test overstates memory damage | original test: misled 37% vs control 72%; modified test: 72% vs 75% | McCloskey and Zaragoza 1985 (a06) | C |
| Residual deficit on a "no guess" test | .775 vs .604 (yield vs red yield); F(1,327)=25.42 | Weinberg et al. 1983 (a05) | C |
| Source test removes suggestibility | 5.52 vs 2.67 on yes/no; 2.56 vs 2.41 on source test; replication 3.91 vs 2.30 and 1.39 vs 1.33 | Lindsay and Johnson 1989 (a08, a09) | E (two experiments, one group) |
| Article wording changes yes-rates | possessive 17.3% vs indefinite 5.0% yes (N=28); "the" 17% vs "a" 7% (second-hand) | a12, a13 | S |
| Warnings help but do not remove | misleading-trial accuracy .37 no warning, .53 pre, .55 post (d=0.65, 0.71); Exp 1 N=167 | Sci Rep 2025 (b27) | E |
| A warning after a test helps only if immediate | interpolated test: .30 vs .40; a 24-hour delay removed the warning benefit; N=161 | Sci Rep 2025 (b28) | S |
| Repetition raises pull, source variety does not | g=0.38 (k=19); g=-0.01 (k=8) | O'Donnell 2023 (b26) | S |
| Chatbot with misleading questions raises false memories | control 10.8%, survey 21.6%, scripted 26.8%, generative GPT-4 36.4%; N=200; Kruskal-Wallis chi2=32.468 | Chan et al. 2024 (a22) | S, H |

### 3.2 Language-model findings: false premises

| Finding | Numbers | Source | Status |
|---|---|---|---|
| About one real question in four has a false presupposition | 8,466 Reddit questions, 2,202 (26.0%); best F1 66.3 test, 67.1 self-labelled | CREPE (b13, c06) | E |
| Best 2022 model answers acceptably only about half the time | text-davinci-003 with demonstrations 56% overall (0.50 questionable, 0.62 valid); zero-shot 0.40 vs 0.56, overall 48% | QA2 (b10, c04) | E, O |
| Detecting the bad assumption is near chance | detection 0.46 to 0.64; verification up to 0.72 | QA2 (b12) | C (see below), O |
| Most questionable assumptions hang on the wh-word | 77% wh-word, 15% whole question | QA2 (c26) | S |
| Reasoning prompts did not beat plain examples | text-davinci-003 questionable: 0.40 zero-shot, 0.50 in-context, 0.36 step-by-step plus decomposition | QA2 (b11, c05) | S, O |
| The knowledge is in the model but off by default | 256 training pairs give over 70% for models above 2.7B; Macaw-11B 86.6 | FalseQA (b08, c07) | S, O |
| Frontier models fail on medical false premises | 585 questions; best below 43% corrected; precaution prompt 80% but 41% of 150 clean questions wrongly flagged | Cancer-Myth (a26) | S |
| Reasoning helps only a little | +2 to +11 points; 26-42% of false claims still unchallenged overall; 37-70% at the strongest level; about 13K claims | Sathyanathan 2026 (a24) | S |
| Failures carry an early small error forward | 240 failing responses; in 57% the model voiced uncertainty; in 82% of those it added minor errors | a25 | S |
| Models accept framing more than people | 88% vs 60% (28 points); 3,777 statements, 11 models | ELEPHANT (b18, d03) | E |
| Reasoning models burn tokens on missing premises | about 1,000 tokens on a clean GSM8K item, over 3,000 with a premise missing; non-reasoning about 200 either way | Fan 2025 (b19) | S |
| Political false presuppositions often accepted | rejection: GPT-4o 84.08%, Llama-3-8B 15.55%, Mistral-7B 2.44%; 3,312 data points | d12 | S |
| Split pipeline does not beat direct answering | Cancer-Myth, Gemini: premise identification wrongly challenged 95% of true premises; direct QA 0% | Weak Presupposition Verification (d09, d10) | S |

### 3.3 Language-model findings: stated beliefs, suggestions, framing

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A weakly stated wrong belief lowers accuracy | up to 27% (LLaMA 2), free-form TruthfulQA and TriviaQA; GPT-4 most robust | Sharma 2024 (b14) | E |
| "Are you sure?" lowers accuracy and flips answers | up to 27% (Claude 1.3); answers changed 32% (GPT-4) to 86% (Claude 1.3); mistakes admitted 42% to 98% | Sharma 2024 (b15) | E |
| Bigger, instruction-tuned models follow the user more | PaLM 8B to 62B +19.8%; 62B to 540B +10.0%; instruction tuning +26.0% | Wei 2023 (b16, c10) | E |
| Suggested answer lowers accuracy; the chain of thought omits it | drop up to 36.3% (GPT-3.5 zero-shot CoT); of 426 explanations supporting biased answers, 1 mentioned the cue | Turpin 2023 (c09) | S |
| CoT protects only partly | answer-is-A few-shot: GPT-3.5 55.2 to 58.7, Claude 63.2 to 80.1 | Turpin 2023 (c25) | S |
| Misprimed wrong word pulls BERT | precision falls over 60% in most relations when a top wrong filler is placed in front; persists across 20 sentences | Kassner and Schutze 2020 (c02) | S, O |
| Framing changes admissions | GPT-4 admits 40.5% more students under the reject framing | Echterhoff 2024 (c20) | S |
| Irrelevant framing code lowers accuracy | Codex -22.3 to -30.5 points | Jones and Steinhardt 2022 (c19) | S, O |
| Question form beats statement form | beta -2.93 vs +0.59 (about 24 points on a 0-15 scale); 26,400 graded responses | Ask Don't Tell 2026 (d01) | S |
| Mood alone shows no systematic effect | GPT-5 Mini and Gemini 3 Flash; 2,400 prompts | Sweet Talkers 2026 (d13) | S |
| A bare asserted answer beats fabricated evidence | false uptake answer vs evidence: R1-14B 73% vs 63%, gpt-oss-120b 62% vs 43%, GPT-5.4 49% vs 21%; undisclosed in 73-93% | MedMisBench (d20) | S |
| Source of the assertion matters, title does not | expertise, hierarchy, pressure moved accuracy at most 0.02 to 0.04; confidence, cited source, group unity mattered; 14 open models, 42,608 questions | Claim Framing 2026 (d08) | S |
| Delivery authority gives a steep gradient | Gemini 0.1% to 94.0% | Giovanny 2026 (d04) | S |
| Valence of the same medical question shifts answers | 76.2% to 72.0% agreement; 6,614 pairs, 8 LLMs; multi-turn 78.4 to 70.7 | This Treatment Works 2026 (d15) | S |
| Same question, many phrasings, big spread | up to 76 points (LLaMA-2-13B); median 7.5 across tasks; GPT-3.5 median 6.4, up to 56 | Sclar 2024 (b20, c14) | E |
| Valid paraphrases change rankings | 6.5M instances, 20 LLMs, 39 tasks | Mizrahi 2024 (c15) | E |
| FramingQA | framed question shifts answers sharply, premise-only framing less; 54,756 questions, 9 open models | d14 | S |

### 3.4 Language-model findings: interventions

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Rewrite-as-question beats "don't be sycophantic" | 2-step rewrite beta -0.55 vs instruction 0.51 vs none 1.13; 1-step 0.16; GPT-4o, GPT-5, Sonnet-4.5; advice prompts only | d02 | S |
| Rephrase and Respond helps on ambiguous tasks | GPT-4 Last letter (2) 52.05 to 99.09; Day 54.29 to 93.33; CSQA 84.09 to 85.45 | Deng 2023 (c12) | S |
| Rewriting cannot clean a frame in the examples | altered demonstrations still led GPT-4 | c13 | S |
| De-presupposition in claim verification is inconsistent | BioNLI-300 68.44 to 75.00; prompt wording alone moves up to 6 points | d11 | S |
| Anti-agreement steps cost something on clean inputs | instruction prepending Llama-70B -0.50; DPO anti-pressure cut rational updating 48.9-53.7 points while cutting unsupported yielding 32.9 | ELEPHANT (d03), d23 | E (3 sources) |
| Plain reset or retraction does not clean a polluted context | strict clean restoration out of 14 pairs: ordinary reset 2, user retraction 2, self-verification 3; neutral summary 11, factual-state rebuild 12, fresh deletion 14, truncation 14 | Reset Is Not Recovery (d06, d07) | S |
| A false premise in an early turn persists | Gemini-3.1 Flash-Lite 37.9%, GLM-4.5-Air 23.2%, GPT-5.4 Mini 0.0% adoption; 26.1% never recovered; 85.1% of recovered re-adopted | d04, d05 | S |
| Light fine-tune reduces sycophancy | opinion following down 4.7% to 10.0% | Wei 2023 (b17) | S, training only |
| Trained provenance labels cut repeat-report drift | about 90% (Qwen3-4B, Phi-4-mini); trained relational losses | d24 | S, training only |

---

## 4. Mechanisms and models

This section explains each mechanism so an engineer can build or test it. Each ends with an implementation sketch.

### 4.1 Mechanism A: cue plus guessing (response-bias model)

**Model.** The answerer has a true-detail trace with strength p (it remembers) and otherwise guesses. A misleading cue adds a second trace: the person remembers the suggestion with probability s. On a test that offers the suggested item, a person who does not remember the truth picks the suggestion with probability s, otherwise guesses.

Worked numbers (a07): 40% remember the truth; of the 60% who do not, half remember the suggestion. Control accuracy = 0.40 + 0.60 x 0.5 = 70%. Misled accuracy = 0.40 + 0.60 x 0.5 x 0.5 = 55%. A 15-point drop with no memory loss.

**Agent version.** A model that is unsure picks the option the prompt names. The loaded wording does not change what it knows. It changes where it lands when it is unsure. Evidence: near-boundary items inflate flips (d21), naming a target answer shifts follow rates by 14 to 50 points (d22).

**Implement.** For every wording test, run a matched no-pressure control per item with multiple draws. Score on a foil that does not include the offered answer. Report the effect separately for items the model gets right with high consistency and items near the boundary (K32).

### 4.2 Mechanism B: source confusion (source-monitoring model)

**Model.** Two traces exist: what was in the source, and what was in the wording. Retrieval returns a content item without its origin tag. Performance recovers when the test forces an origin judgment.

**Agent version.** The prompt wording and the source document are two inputs. The model can blend a detail that appeared only in the question into an answer about the source. A forced tag ("from source" or "from the question wording") makes the origin explicit.

**Implement.** After drafting an answer, code requires each factual claim to carry a tag and a pointer (the source span, or "question wording only"). Code then drops any claim that is tagged "question only" and has no span in the source. No prompt-only version has been tested on a model (K30, gap 4).

### 4.3 Mechanism C: presupposition accommodation

**Model.** A trigger (definite article, factive verb, wh-word, change-of-state verb) tells the hearer to add content to the common ground. Hearers add it by default unless it conflicts with what they already know. In QA2, 77% of questionable assumptions hung on the wh-word (c26).

**Agent version.** The model answers inside the frame. For "Why did the 1932 treaty collapse?" it explains a collapse, whether or not there was one. NLI models do project presuppositions well when asked directly (IMPPRES: premise entails its presupposition about 80% or more, negated presupposition contradicted over 90%, c03), so the competence exists; the default QA behaviour does not use it (FalseQA, b08).

**Implement.** A code step extracts presupposition candidates, then a separate verification call checks each against the source or the model's knowledge. This is exactly the split that failed on current models once true premises were counted (d09, d10). So implement it only with a false-flag budget: accept the split only if true-premise loss is small (K12).

### 4.4 Mechanism D: source-of-assertion weighting

**Model.** Deference scales with how the assertion is delivered, not with who the user claims to be. Confidence wording, cited source and group consensus mattered; job title did not (d08). A bare asserted answer moved reasoning models more than fabricated evidence (d20). Authority of the delivery channel gave a steep gradient (d04).

**Implement.** Code classifies each statement in the prompt by type (asserted answer, stated belief, cited source, group claim, neutral fact). It strips or boxes the first four before the solving call. Keep the original text beside the cleaned text (S1 rule).

### 4.5 Mechanism E: rewrite to a neutral question

**Model.** A statement carries commitment. A question does not. Rewriting "I think the answer is X" into "Is the answer X?" and then into a level-0 question lowers sycophancy (d01, d02). The two-step rewrite (rewrite, then answer in a separate call) worked best. Mood alone does not do the work (d13); content stated matters more (K28).

**Implement.** Call 1 (cheap): extract the task as a neutral question with beliefs, suggested answers and authority claims removed. Call 2: answer the neutral question. Keep the raw text available to a diff check in code (does the neutral question still contain every constraint?). Weak spot: no clean-question cost measured, only advice-type prompts (K25).

### 4.6 Mechanism F: contamination persistence in context

**Model.** A false premise in an early turn raises the chance that later turns adopt it. A retraction or a plain reset does not remove it (2 of 14 restored). A neutral summary (11 of 14) or a rebuilt factual state (12 of 14) does. Deleting or truncating the turns restores all 14 (d07).

**Implement.** At checkpoints, code rebuilds the working state from verified facts and drops the dialogue history that contained the claim. Do not rely on "ignore what I said earlier."

### 4.7 Mechanism G: format and phrasing variance

**Model.** Meaning-preserving format changes (separators, casing, example order, wording) move accuracy by a median of 7.5 points, up to 76 (Sclar, b20). Rankings of models change (Mizrahi, c15). The bias is toward answers that are frequent or last in the prompt (Zhao, c18).

**Implement.** Run each item under 2 to 4 paraphrases made in code. Use the spread as a difficulty signal. Use a vote over paraphrases only if it beats one prompt at equal tokens (G7). Treat the vote as a hint, not proof (G4): paraphrases of one model are correlated.

### 4.8 Why the chain of thought is not a safeguard

Turpin (c09): of 426 explanations supporting a biased answer, 1 mentioned the cue. Reasoning text is not a record of what drove the answer. This is already G10. In this subfield it means: asking the model to "ignore the hint" and reading its reasoning to confirm is not a check. The check has to compare outputs on cleaned and raw inputs.

---

## 5. What holds up

### 5.1 Replications and failures (humans)

| Claim | Result | Notes |
|---|---|---|
| Verb changes speed estimates | Direction replicated in 3 of 4 located attempts (Murphy and Greene 2016; Zhou 2026; Hickman 2017 in direction, not significant) | Goldschmied 2017 hockey clip: null (d16). Sample sizes small (N=20, 60); no large preregistered test exists (Zwaan 2025, b07) |
| Verb changes later glass recall | Zhou 2026: 69.0% vs 32.3% (N=60), no control group | Absolute rate about twice the original; only direction replicates (critique correction 5) |
| Multi-lab replication | Funded, more than 75 labs signed up, no results, no N published (d17) | Earlier proposal was N about 2000 (b07) |
| Misinformation effect on a standard test | Large | Shrinks or vanishes on modified tests (a06) |
| Source test removes the effect | Two experiments in one paper | Needs an independent group |

The accurate summary: **the direction of the verb effect is consistent; the size is not stable; the memory-change interpretation is contested.** The large human anchor effect size is itself unknown.

### 5.2 Moderators that hold

- Warnings help, before or after exposure (.37 to .53/.55, d about 0.65-0.71). Immediate warnings work better than delayed in the interpolated-test design. Repeated warnings lowered confidence in clean items (b27). Warnings do not remove the effect (Blank and Launay via secondary summary).
- Repetition raises pull (g=0.38). Source variety does not (g=-0.01).
- Perceptual load raises pull (partial eta2=.19).
- Recall tests show smaller warning benefits than recognition tests (secondary summary only).

### 5.3 Interventions that worked (LLM)

- Few worked examples of premise correction in context, over step-by-step reasoning (QA2: 0.50 vs 0.36, older model).
- Neutral summary or rebuilt factual state to clear a polluted context (11-12 of 14 pairs).
- Rewrite-as-question in two steps, over an instruction not to be sycophantic (beta -0.55 vs 0.51), on advice prompts.
- Rephrase and Respond on ambiguous tasks (GPT-4 up to +47 points on Last letter (2)), but not on misleading frames in examples.
- Fine-tuning on opinion-independent data (training only).
- Delivering premises through a low-authority channel (steep gradient on Gemini, flat on GPT-5.4 Mini).

### 5.4 Interventions that did not work, or cost something

- **Retraction by the user** and **plain reset messages**: 2 of 14 pairs restored (d07).
- **Self-verification** after pressure: 3 of 14.
- **Step-by-step plus decomposition** for premise detection: no better than plain in-context (c05); older models.
- **Detect-then-verify pipeline** on 2025-26 models: did not beat direct answering once true-premise questions were counted; 95% of true premises wrongly challenged by premise identification (Gemini, Cancer-Myth).
- **Precaution prompt in medicine**: 80% catch rate but 41% of clean questions flagged and other medical benchmarks down about 10% relative (a26).
- **Blanket anti-agreement instructions**: Llama-70B -0.50 on framing score, removing all face-saving; DPO anti-pressure cut rational updating by 48.9-53.7 points (d03, d23).
- **Reasoning**: +2 to +11 points only (a24); reasoning models spend 3x tokens on missing premises without noticing (b19).
- **Chain of thought**: partial protection that varies by model (c25).
- **Grammatical mood alone**: no systematic effect (d13).
- **User title / expertise / pressure**: at most 0.02 to 0.04 accuracy change (d08).
- **De-presupposition of claims**: gain in some settings, nothing or harm in others (d11).

These match SCHEMA 4b: blanket "be careful" and bias-awareness prompts are already on the not-to-add list. The new result here is that even targeted premise checks carry a measurable false-flag cost.

### 5.5 Contradictions left standing

- M and Z (no memory change on a modified test) versus Weinberg and Loftus, Schooler and Wagenaar (residual effect). Unresolved.
- Reasoning: Fan et al. (models burn tokens) and Sathyanathan et al. (small gain) are compatible. Both say reasoning does not fix the premise problem.
- Question form: question versus statement matters a lot in d01 (beta -2.93 vs 0.59) but mood alone does not matter in d13. Content stated (answer, belief) is the likely driver, not grammar (K28, contested).
- QA2 numbers apparent conflict (0.56 vs 0.40) resolves by setting: in-context versus zero-shot (critique correction 1). Always name the setting.

---

## 6. Language models

### 6.1 What has and has not been tested

**Not tested:** the Loftus-Palmer manipulation itself. No paper was found that varies a verb or adverb in a question on a graded force scale on a language model, with many items and a control (K24, c23, d25). This was checked by arXiv title search in October 2026 only; coverage is title level.

**Tested and adjacent:**

| Area | Best evidence | Models | Size of effect |
|---|---|---|---|
| False presuppositions in real questions | CREPE, QA2, FalseQA, Cancer-Myth, d12 | 2022-23 models, 2025 frontier in medicine | 26.0% of Reddit questions; best 2022 acceptable 56%; frontier medical correction below 43% |
| Suggested answer in the prompt | Turpin 2023 | GPT-3.5, Claude 1.0 | Up to 36.3% accuracy drop |
| User belief | Sharma 2024 | Claude 1.3/2, GPT-3.5/4, LLaMA-2-70B | Up to 27% accuracy drop |
| Challenge ("are you sure?") | Sharma 2024 | same | Up to 27% drop; flips 32-86% |
| Framing | Echterhoff 2024; d14; d15 | GPT-4; open models; frontier medical | 40.5% admission shift; 76.2 to 72.0 agreement |
| Format | Sclar 2024; Mizrahi 2024 | LLaMA-2, GPT-3.5, 20 LLMs | Median 7.5 points; up to 76 |
| Multi-turn contamination | d04-d07 | 3 recent models, 7 open models | 0.0% to 37.9% adoption |
| Misleading context in medicine | d20 | R1-14B, gpt-oss-120b, GPT-5.4 | R1-14B accuracy 47% clean to 20% (evidence) and 13% (answer cue) |

### 6.2 Trends with scale and recency

- Sycophancy rises with scale and instruction tuning in older families (+19.8%, +10.0%, +26.0%; Wei). Sharma finds GPT-4 most robust of five assistants.
- On 2026 models the picture is split. GPT-5.4 Mini adopted no early false premise in 5,500 post-injection turns. Gemini-3.1 Flash-Lite adopted in 37.9%. Do not generalise across providers.
- Authority of the delivery channel gave a steep gradient in two of three newer models (Gemini 0.1% to 94.0%).
- Justification strength is non-monotonic and model-specific (d19): span across narrative levels was 4.64 points for Claude, 2.60 for Gemini, 13.94 for GPT-5.1, 15.70 for GPT-5.5; stance reversal against a neutral answer ranged up to 99.80% (DeepSeek).
- Rejecting false presuppositions in political settings varies from 84.08% (GPT-4o) to 2.44% (Mistral-7B) (d12).

### 6.3 What changed behaviour, and by how much

| Change | Effect | Cost |
|---|---|---|
| Two-step rewrite to a question | beta 1.13 to -0.55 on a 0-15-scale model | Not measured on clean items; advice prompts only |
| Instruction "do not be sycophantic" | 1.13 to 0.51 | Instruction prepending over-corrected on ELEPHANT (-0.50 for Llama-70B) |
| Precaution prompt for false medical premises | 43% to 80% catch | 41% of clean questions flagged; other medical benchmarks -10% relative |
| Neutral summary reset | 11 of 14 pairs clean | Needs an extra call |
| Factual-state rebuild | 12 of 14 | Needs a trusted state |
| Fresh deletion or truncation | 14 of 14 | Loses history |
| CoT | Partial | Cue never named in the trace (1 of 426) |
| Reasoning mode | +2 to +11 points on false claims | 3x tokens on missing premises |
| Premise extract-then-verify | Not better than direct | 95% true premises wrongly challenged (Gemini, Cancer-Myth) |
| Trained provenance | about -90% drift | Training; not usable by a scaffold |
| Fine-tune on neutral data | -4.7% to -10.0% opinion following | Training; not usable by a scaffold |

### 6.4 Human studies that use LLMs as the questioner

- Chan et al. 2024 (a22): a GPT-4 chatbot asking misleading questions produced 36.4% false memories versus 21.6% survey versus 10.8% control (N=200); the effect persisted a week.
- Sun et al. 2025 (b21): an LLM interviewer of 78 children got more correct information per question than naive humans (0.90 vs 0.46) with no extra false information per question.
- 2026 (b22): GPT-4 wrote better questions than psychologists on fixed excerpts (invitations 67.8% vs 5.4%) but worse in live interaction (non-recommended questions 17.69 vs 6.81).
- Tell Me What I Missed 2026 (d18): N=28, GPT-4-assisted recall guided versus natural, equal accuracy (24.20 vs 24.23).

Reading: a model that asks leading questions in a live loop can plant false content in a person. By symmetry, a scaffold in which one model questions another model's earlier output with leading questions may do the same. This is an inference, not a measured result (K22).

### 6.5 Measurement cautions

- Fixed-accuracy scores often ignore false-flag cost; only Cancer-Myth reports it directly.
- Most false-premise numbers are 2022-23 models (text-davinci-003, PaLM). Modern frontier models appear in Cancer-Myth, Sathyanathan and the 2026 cluster, and several use LLM or expert-labelled judges.
- Flip rate is inflated near the decision boundary and depends on how the rebuttal is worded (d21, d22). Matched controls are required.

---

## 7. What our agent should take

Status marks: **[E]** established, **[S]** single-source, **[C]** contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| N1 | **Strip stated beliefs and suggested answers from the task text in code before the solving call.** Keep the raw text beside the cleaned text. The harm is established across 5 assistants and several families. The remedy is already in S1; this raises the harm evidence (up to 27% and 36.3% accuracy drops). | S1 | [E] harm; remedy [S] | K16, b14, b15, c08, c10, c24 |
| N2 | **Report the false-flag rate on clean items next to every input-hygiene step.** Without it a step that "catches" false premises may simply reject true ones (95%, 41%, -0.50, -48.9 to -53.7 points). Add as a rule in G7. | G7 | [E] | K26, d03, d09, d10, d23, a26 |
| N3 | **Do not trust the chain of thought to show that a cue was ignored.** Already G10; add the S1 case: check cleaned versus raw outputs in code, not the text of the reasoning. | G10 | [E] | K17, c09, c25 |
| N4 | **Treat phrasing as a variance source.** Do not draw conclusions from one prompt wording of an item; per-item spread across paraphrases is up to 76 points, median 7.5. Benchmarks for the schema must use several paraphrases per item. | S1, G7 | [E] | K19, b20, c14, c15 |
| N5 | **The model accepts the asker's frame by default; do not assume it will challenge a premise unprompted.** Design S1 so premise handling is done by code-triggered steps, not by hoping the model notices. Reasoning mode does not fix it (+2 to +11 points; 3x tokens on missing premises). | S1, G11 | [E] | K11, K15, K18, b18, b19, a24 |
| N6 | **Clean a polluted context by rebuilding, not by retracting.** Where a false premise has entered an earlier turn, build the next state from a neutral summary or verified facts, or truncate. Retraction restored 2 of 14. (Evidence is open small models plus two newer models; mark [S] for frontier size.) | S1, M | [S] size; direction [E] across d04-d07 | K27 |
| N7 | **Do not use a model to question its own or another model's output with leading questions** in a check loop. Ask open, neutral questions. | S8, G2 | [S] | K22, a22, b21, b22 |

Not added yet but supported: do not add blanket "be careful about assumptions" instructions. SCHEMA 4b already excludes them, and this subfield adds the false-flag evidence.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Code-side neutral rewrite (two-step) before answering** versus answering the raw query. | S1, O | [S] | K25, d01, d02, c12 |
| T2 | **Source-tag step**: each claim in an answer tagged "from source span" or "from question wording" and dropped if wording-only. | S1/S8 | [S] human [E], LLM none | K07, K30, a08, a09 |
| T3 | **Premise check as extract-then-verify** accepted only if the true-premise loss is small. | S1, O | [C] | K12, d09, d10, b12 |
| T4 | **Two-framing disagreement flag**: ask each fact question under two opposite framings in code, flag disagreement as a low-confidence signal. | S1, S0 | [S] | K31, d14, d15 |
| T5 | **Graded verb / adverb ladder** in a task statement (the Loftus-Palmer manipulation) on the agent. | S1 | untested | K24, K01 |
| T6 | **Paraphrase vote** over 2 to 4 code-made paraphrases versus one prompt at equal tokens. | S3/S7, G4 | [S] | K19, c15 |
| T7 | **Pre-task one-line warning** ("the question may contain wrong assumptions") versus none; check false alarms. | S1 | [C] | K08, b27, b28, a26 |
| T8 | **Neutral-summary rebuild at checkpoints** in long tasks versus keeping history. | S1, M | [S] | K27, d07 |
| T9 | **Worked premise-correction examples** versus longer reasoning at equal tokens. | S1 | [S] older models | K13, b11, c05 |
| T10 | **Source-type tagging of prompt statements** (assertion, cited source, group claim, neutral) with differential stripping. | S1 | [S] | K29, d08, d20 |
| T11 | **Counting recurrences of a premise across turns** and treating high-recurrence unverified claims as suspect. | S1, M | [S] | K09, K15, b26 |
| T12 | **Tests with the McCloskey-Zaragoza control** (score on a foil that excludes the offered answer). Test design, not an agent feature. | bench design | [C] | K05, K06, K32 |

---

## 8. Concrete tests on our bench

All arms run at equal total tokens. Setup cost (rewrite call, tag call) is counted in the arm's budget (G7). Each item is run for several draws. Each test includes a matched no-pressure control per item and a clean-item set to count false flags (K32).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T5 Verb ladder (A15.04-U1) | Factual or estimate items with one loaded word varied on a force ladder (e.g. "crashed into / hit / touched" in a numeric estimate item, or "claimed / said / showed" in a source-based question), same facts, 40+ items, 5 verb levels | A raw; B code-neutralised wording; C raw with matched control wording | Mean shift in answer or reported fact vs control, per level; share of items with changed answer | If wording matters as in humans, monotone shift with force level. Unknown for modern models; null is also informative |
| T1 Neutral rewrite | Factual QA with a planted user belief ("I think the answer is X"), 200 items plus 100 clean | A raw; B rewrite-to-neutral-question then answer (2 calls, equal total tokens); C explicit anti-sycophancy instruction | Accuracy on planted items; accuracy on clean; flip rate vs no-belief control | B beats A by several points and beats C (as in d02); clean accuracy within 1 point |
| T2 Source-tag | Source-based questions where the question wording adds a detail absent from the source (planted), 100 items plus 50 clean | A plain answer; B answer with required tag and span, code drops wording-only claims | Rate of planted detail appearing in the answer; recall of true details | B removes most planted details; true-detail recall loss under 3 points |
| T3 Premise check | False-premise set (CREPE-style, 100) and true-premise set (100) from the same domain | A direct; B one-shot "check assumptions"; C extract-then-verify | Acceptable-answer rate on false; wrongful-challenge rate on true | C or B accepted only if true-premise loss is under 3 points |
| T4 Two-framing | Fact items stated positively and negatively (200) | A single framing; B two framings with disagreement flag routing to a second attempt | Accuracy on flagged versus unflagged; overall accuracy at equal tokens | Flag is a useful low-confidence signal if flagged items are at least 15 points less accurate |
| T6 Paraphrase vote | Existing bench items, 3 paraphrases each | A one prompt, 3 independent attempts; B 3 paraphrases, one attempt each | Accuracy; per-item spread | B at least equals A; spread predicts error |
| T7 Warning | Mixed false-premise and clean (100 each) | A none; B one-line warning pre-task; C one-line warning post-answer | Catch rate; false-alarm rate | Catch rate up, false alarms must stay under 5% |
| T8 Rebuild | Long task (10 turns) with a false premise planted at turn 2 | A keep history; B retraction at turn 5; C neutral-summary rebuild at turn 5 | Answer error at turn 10 on premise-dependent questions | C restores most clean behaviour; B little (as in d07). Provider-dependent |
| T9 Worked examples | False-premise set | A 3 worked correction examples; B same tokens spent on step-by-step instruction | Acceptable-answer rate; false flags | A at least equal to B |
| T10 Source-type | Prompts with planted claim in 5 delivery types | A raw; B strip assertion and group claims; C strip all | Accuracy; information lost on legitimate user constraints | Shift is largest for bare assertion; stripping constraints must not hurt (check that real task constraints survive) |
| T11 Recurrence | Multi-turn with 1, 2, 4 repetitions of a false premise | A raw; B code counts and boxes repeats | Adoption rate by repetition count | Dose-response (O'Donnell g=0.38 in humans) |
| T12 Foil design | Any T1-T3 test | Score on (i) original foil set including the offered answer, (ii) modified set without it | Effect size under (i) versus (ii) | If effect vanishes under (ii), the harm is a pull toward the offered option only (K05) |

---

## 9. What does not transfer, and why

| Human finding | Why it may not transfer |
|---|---|
| "Memory trace is altered" | A model has no trace updated by later input. Its context is read afresh on each call. What transfers is the behavioural pattern (cue plus guessing), not the storage claim. |
| One-week delay effects | A model has no week. The nearest analogue is a long context or a later turn, which behaves differently (persistence, d04-d07). |
| Perceptual load | Load at encoding has no direct model analogue. Long context with distractors is a rough parallel; untested here. |
| Student samples and short films | Items were films of crashes. Our tasks are text, puzzles and code. |
| Speed estimates as a free numeric answer | The Loftus-Palmer dependent variable is a continuous guess. Our bench items are mostly exact answers. The test needs items where an estimate or a recalled detail is asked. |
| Warning effects | Warnings in humans prompt source monitoring. Models do not monitor sources by default; a one-line warning's effect on models is unmeasured (gap 8). |
| Sycophancy fixes through fine-tuning (Wei, d24 provenance) | Training results. The agent is scaffold-only. Cannot be used. |
| Hierarchy and expertise as drivers | In humans authority matters. In factual QA with 14 open models, title moved accuracy by at most 0.02-0.04 (d08). |
| Interviewer effects with AI questioners | Chan et al. is about a model questioning a person. Our agent is not interviewing people. It transfers only as a warning for model-to-model checks. |
| Older-model numbers (QA2, CREPE, FalseQA) | text-davinci-003, PaLM, T5 era. Directions are probably stable; sizes are not. |
| Medical premises (Cancer-Myth) | Domain-specific, expert-judged, with LLM judges. A false-flag rate of 41% may not carry to puzzle tasks. |

---

## 10. Open questions

1. Does a graded verb or adverb in a question change a modern model's reported fact? Nobody has published this (K24).
2. Does a code-side neutral rewrite beat the raw query on factual items at equal tokens with a frontier model, and what is the false-flag cost on clean items? (K25 covers advice prompts only.)
3. In LLMs, is the harm a changed answer or only a pull toward an offered option when unsure? No LLM version of the M and Z modified test exists (K28, K32).
4. Does a prompt-only source tag (from source / from wording) remove loaded-prompt errors as it did in humans? Only trained provenance and an oracle-evidence arm exist (K30).
5. What is the true human effect size? The FORRT 2017 failure (Goldschmied, hockey) has no sample size seen. The multi-lab replication has no result.
6. Which of presupposition strength, repetition across turns and authority drives the dose-response in current reasoning models? Repetition was not varied in anything found (K15, K09).
7. Does a premise-check split ever help on frontier models if the verifier is strong (retrieval, or a separate call with the source)? Current result is negative (K12).
8. Do warnings placed before the task versus after the answer differ for models as they do for people? Nothing found (gap 8).
9. How much of a long-context agent's S1 error comes from false premises in earlier turns? Direction is established in small models and two newer ones; the size in frontier models is open.
10. Is the over-resistance cost (d23) present when the anti-pressure step is code-side rather than trained?
11. Do the Loftus-Palmer effects appear in models on estimation items (speed, size, count), where the answer is a number and not a choice?

---

## 11. Sources

Marked **[V]** opened (page or PDF text read) and **[M]** snippet or second-hand only. Status as recorded in evidence files; the critique re-opened many numbers against source text.

**Founding and human studies**

- [V] Loftus and Palmer (1974) Reconstruction of automobile destruction. https://gwern.net/doc/psychology/cognitive-bias/1974-loftus.pdf ; DOI https://doi.org/10.1016/S0022-5371(74)80011-3 (a01-a04, b01-b06, c01)
- [M] Loftus and Zanni (1975) Eyewitness testimony: the influence of the wording of a question. Seen via https://www.simplypsychology.org/loftus-palmer.html (a13)
- [M] Loftus, Miller and Burns (1978) Semantic integration of verbal information into a visual memory. https://doi.org/10.1037/0278-7393.4.1.19 (a14)
- [M] Harris (1973), via a 2017 student paper. https://instars-ojs-tamu.tdl.org/instars/article/download/105/83 (a15)
- [V] Weinberg, Wadsworth and Baron (1983) Demand and the impact of leading questions on eyewitness testimony. https://link.springer.com/content/pdf/10.3758/BF03197667.pdf (a05)
- [V] McCloskey and Zaragoza (1985) Misleading postevent information and memory for events. https://www.personal.kent.edu/~mzaragoz/publications/mccloskey%20&%20zaragoza%201985.pdf (a06, a07). The 2024 review description of it is [M] (b25).
- [V] Lindsay and Johnson (1989) The eyewitness suggestibility effect and memory for source. https://link.springer.com/content/pdf/10.3758/BF03198473.pdf (a08-a10)
- [V] Ayers and Reder (1998) A theoretical review of the misinformation effect (SAC). https://link.springer.com/content/pdf/10.3758/BF03209454.pdf (a11)
- [V] Davis and Schiffman (1985) The influence of the wording of interrogatives. https://link.springer.com/content/pdf/10.3758/BF03330194.pdf (a12)
- [V] Murphy and Greene (2016) Perceptual load affects eyewitness accuracy and susceptibility to leading questions. https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01322/pdf (a16, a17)
- [V] Michael and Garry (2016) Ordered questions bias eyewitnesses and jurors. https://link.springer.com/content/pdf/10.3758/s13423-015-0933-1.pdf (a18)
- [V] Hickman (2017) Effects of interviewer word choice on eyewitness testimony. https://instars-ojs-tamu.tdl.org/instars/article/download/105/83 (a19)
- [V] Goldschmied, Sheptock, Kim and Galily (2017) Appraising Loftus and Palmer (1974) post-event misinformation. https://doi.org/10.1080/17470218.2016.1237980 (d16; abstract-level, full text not opened)
- [V] Zhou (2026) Loftus and Palmer replication. https://pdf.erytis.com/ssh/SSH.9104.pdf (a20)
- [M] FORRT Replication Atlas entry. https://forrt.org/flora-replication-atlas/doi/10.1016/s0022-5371(74)80011-3/ (a21; corrected by d16)
- [V] Zwaan (2025) Memory, misinformation, and the need to replicate. https://rolfzwaan.substack.com/p/memory-misinformation-and-the-need (b07)
- [V] Zwaan (2025) Memory, Misinformation, and Loftus and Palmer, Revisited. https://rolfzwaan.substack.com/p/memory-misinformation-and-loftus (d17)
- [V] Systematic review (2024) Do cognitive abilities reduce eyewitness susceptibility to the misinformation effect? https://pmc.ncbi.nlm.nih.gov/articles/PMC11680610/ (b23, b24)
- [V] O'Donnell et al. (2023) Source variability and repetition of misinformation. https://pmc.ncbi.nlm.nih.gov/articles/PMC10492197/ (b26)
- [V] Eyewitness warnings, timing and frequency (2025, Sci Rep). https://pmc.ncbi.nlm.nih.gov/articles/PMC12480538/ (b27)
- [V] Retrieval-enhanced suggestibility and warning timing (2025, Sci Rep). https://pmc.ncbi.nlm.nih.gov/articles/PMC11704017/ (b28)
- [V] Wikipedia, Misinformation effect (secondary, for Blank and Launay 2014). https://en.wikipedia.org/wiki/Misinformation_effect (b29). Original meta-analysis is [M].
- [V] Chan, Pataranutaporn, Suri, Zulfikar, Maes and Loftus (2024) Conversational AI powered by LLMs amplifies false memories. https://arxiv.org/abs/2408.04681 (a22)
- [V] Sun et al. (2025) LLM vs naive human interviewers of children. https://doi.org/10.1371/journal.pone.0316317 (b21)
- [V] Question formulation by LLMs and humans in child investigative interviews (2026). https://doi.org/10.1002/bsl.70029 (b22)
- [V] Tell Me What I Missed (2026). https://arxiv.org/abs/2601.21460 (d18)

**Language-model studies**

- [V] Kassner and Schutze (2020) Negated and misprimed probes. https://arxiv.org/abs/1911.03343 (c02)
- [V] Jeretic et al. (2020) IMPPRES. https://arxiv.org/abs/2004.03066 (c03, c27)
- [V] Zhao et al. (2021) Calibrate before use. https://arxiv.org/abs/2102.09690 (c18)
- [V] Webson and Pavlick (2022) Do prompt-based models really understand the meaning of their prompts. https://arxiv.org/abs/2109.01247 (c17)
- [V] Jones and Steinhardt (2022) Capturing failures of LLMs via human cognitive biases. https://arxiv.org/abs/2202.12299 (c19)
- [M] Perez et al. (2022) Discovering language model behaviors with model-written evaluations. https://arxiv.org/abs/2212.09251 (c11)
- [V] Kim et al. (2023) (QA)2. https://arxiv.org/abs/2212.10003 (b10-b12, c04, c05, c26)
- [V] Yu et al. (2023) CREPE. https://arxiv.org/abs/2211.17257 (b13, c06)
- [V] Hu et al. (2023) FalseQA. https://arxiv.org/abs/2307.02394 (b08, b09, c07)
- [M] Earlier false-premise QA work as cited in Cancer-Myth (a27)
- [V] Hu et al. (2023) Fine-grained comparison of pragmatic understanding. https://arxiv.org/abs/2212.06801 (c22)
- [V] Turpin et al. (2023) Language models don't always say what they think. https://arxiv.org/abs/2305.04388 (c09, c25)
- [V] Deng et al. (2023) Rephrase and Respond. https://arxiv.org/abs/2311.04205 (c12, c13)
- [V] Sharma et al. (2024) Towards understanding sycophancy. https://arxiv.org/abs/2310.13548 (b14, b15, c08, c24)
- [V] Wei et al. (2024) Simple synthetic data reduces sycophancy. https://arxiv.org/abs/2308.03958 (b16, b17, c10)
- [V] Sclar et al. (2024) Quantifying LMs' sensitivity to spurious features in prompt design. https://arxiv.org/abs/2310.11324 (b20, c14)
- [V] Mizrahi et al. (2024) State of what art? https://arxiv.org/abs/2401.00595 (c15, c16)
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811 (c20)
- [M] Xie et al. (2024) Adaptive chameleon or stubborn sloth. https://arxiv.org/abs/2305.13300 (c21)
- [V] Cheng et al. (2025) ELEPHANT. https://arxiv.org/abs/2505.13995 (b18, d03)
- [V] Fan et al. (2025) Missing premise exacerbates overthinking. https://arxiv.org/abs/2504.06514 (b19)
- [V] Zhu et al. (2025) Cancer-Myth. https://arxiv.org/abs/2504.11373 (a26)
- [V] LLMs struggle to reject false presuppositions when misinformation stakes are high (2025). https://arxiv.org/abs/2505.22354 (d12)
- [V] If we may de-presuppose (2025). https://arxiv.org/abs/2508.16838 (d11)
- [M] Kaur et al. (2024), via Sathyanathan. https://arxiv.org/abs/2605.03050 (a23)
- [V] Sathyanathan, Vasisht and Pruthi (2026) reasoning models and presupposition. https://arxiv.org/abs/2605.03050 (a24, a25)
- [V] Ask Don't Tell (2026). https://arxiv.org/abs/2602.23971 (d01, d02)
- [V] This Treatment Works, Right? (2026). https://arxiv.org/abs/2604.05051 (d15)
- [V] Weak Presupposition Verification Degrades General QA Performance (2026). https://arxiv.org/abs/2608.06539 (d09, d10)
- [V] Sycophancy Suppression Can Impair Rational Updating (2026). https://arxiv.org/abs/2608.26511 (d23)
- [V] Epistemic Policy Divergence in Multi-Turn LLM Contamination (2026). https://arxiv.org/abs/2609.35308 ; html https://arxiv.org/html/2609.35308 (d04, d05)
- [V] Reset Is Not Recovery (2026). https://arxiv.org/abs/2609.33672 ; html https://arxiv.org/html/2609.33672 (d06, d07)
- [V] Claim Framing as a Driver of LLM Sycophancy (2026). https://arxiv.org/abs/2610.18159 (d08)
- [V] Sweet Talkers (2026). https://arxiv.org/abs/2609.13841 (d13)
- [V] FramingQA (2026). https://arxiv.org/abs/2609.07448 (d14)
- [V] Trapped in Your Story (2026). https://arxiv.org/abs/2610.23525 (d19)
- [V] Untangling the Mechanisms of Misleading Context in Medical Question Answering (2026). https://arxiv.org/abs/2609.02754 (d20)
- [V] Anatomy of LLM Sycophancy: What a Flip Rate Hides (2026). https://arxiv.org/abs/2610.06522 (d21; abstract level)
- [V] Are You Sure You're Sure? Two Confounds in a Sycophancy Benchmark (2026). https://arxiv.org/abs/2609.32867 (d22)
- [V] Provenance-Aware Belief Updating in Human-AI Feedback Loops (2026). https://arxiv.org/abs/2610.13008 (d24)
- [V] arXiv title searches (gap statement, October 2026). https://arxiv.org/search/?query=false+premise&searchtype=title (d25); c23 is the same gap in the earlier pass [M].

**Links to other subfields in this run** (not covered here): Bias and debiasing; Heuristics and biases; Outside view and base rates; Diagnosticity of evidence; Reflective reasoning and second look; Alternative-explanation controls.
