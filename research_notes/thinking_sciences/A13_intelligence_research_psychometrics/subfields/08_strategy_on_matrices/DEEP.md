# Strategy on matrices: deep document

*Subfield A13.08. Folder: research_notes/thinking_sciences/A13_intelligence_research_psychometrics/subfields/08_strategy_on_matrices. Built from evidence_a-d.jsonl (ids a01-a30, b01-b34, c01-c27, d01-d16), claims.jsonl (K01-K29) and critique.md. Status marks: [E] established (2+ independent sources), [S] single source, [C] contested.*

*Honesty note up front: the founding paper (Bethell-Fox, Lohman and Snow 1984) was never opened by any agent. Every number about it is second-hand. Several human-study numbers (Gonthier, Vigneau, Rivollier) were recorded by agents and not re-checked in the critique pass. The LLM numbers for Camposampiero, Hersche, Hu, Zhang and Gendron were re-opened and confirmed.*

## 1. What it is

Multiple-choice reasoning items (Raven's matrices, geometric analogies) can be solved in two main ways. Snow (1978, 1980) named them.

- **Constructive matching.** Study the problem. Build an ideal answer in your head. Then look for it among the options. Bethell-Fox et al. (1984) wrote that it "seems to involve the construction of an idealized answer which is compared to the response alternatives" (a01).
- **Response elimination.** Compare features of the stem with features of each option. Discard the options that do not fit. Stop when one is left. Bethell-Fox et al. (1984): it "involves a process of feature comparison between stem and alternatives" (a01).
- **Hybrid: isolate and eliminate.** Find one rule. Drop the options that break it. Find the next rule. Repeat. Found in think-aloud data (a08, b07, d08).

Why this matters for our agent. In the schema, S3 GENERATE writes attempts and S4 TEST checks them. Constructive matching is "S3 before options, S4 matches". Elimination is "S4 first, with options driving the search". The question is whether the agent should hide or delay options, build a candidate first, and only then compare. A second question is when it should fall back to elimination.

Scope. Human work is about 4-option analogies and 8-option 3x3 matrices, mostly the Raven Advanced Progressive Matrices (APM, 36 items). The LLM work covers matrices (symbolic, text, image) and, by extension, multiple-choice (MCQ) knowledge items, where "elimination" shows up as choices-only shortcuts.

## 2. History and theories in depth

**Before strategy.** Hunt (1974) split solvers into Gestalt (perceptual, extend the pattern) and Analytic (propositional, logical operations). Carpenter, Just and Shell (1990) modelled Raven solving with rules and goal management (cited in c23). DeShon et al. (1995): a visual strategy for easy items and a verbal strategy for hard items. Kunda et al. (2010): affine and fractal strategies from AI solvers (a02). Laurence and Macedo (2023) argue that the constructive/elimination pair won because it is easy to measure, not because it is the only valid split (a02).

**The founding study (1984).** Bethell-Fox, Lohman and Snow tracked eye fixations on A:B::C:D geometric analogies with multiple alternatives. Second-hand description: about 28 people, fixation counts and sequences (d09, d10). The reported pattern: higher-ability people use constructive matching, and strategy shifts toward elimination as items get harder (a01, b02). We have no sample statistics, no effect sizes and no switch point. Do not cite numbers from this paper.

**Eye-tracking indices (2006).** Vigneau, Caissie and Bors defined the standard indices on the APM (N=55): proportional time on the matrix, latency to first look at options, matrix-option toggles, and a matrix time distribution index (a03, b03). Four regression models explained 32%, 30%, 49% and 51% of score variance (b03, in-sample).

**Training and practice (2011-2015).** Hayes, Petrov and Sederberg (2011) used scanpath components to predict about 40% of APM variance (a15, b10). Hayes et al. (2015) tested 35 students twice: strategy change explained about a third of the retest gain, and with strategy partialled out the gain was no longer significant (b10). Loesche et al. (2015): teaching the rules shifts time to the matrix (b09).

**Format and validity (2013-2016).** Arendasy and Sommer (2013) and Becker et al. (2016) changed the answer format to block elimination (construction of the answer from parts) and found better construct and convergent validity (a11, b19, b20; second-hand). The Open Matrices Item Bank now has 220 construction-based items (a11).

**The working-memory dispute (2015-2019).** Gonthier and Thomassin (2015): forcing build-first weakened the working-memory (WM) link, and self-reported strategy fully mediated the WM-score link (b05). Jastrzebski et al. (2018) did not replicate the mediation in a larger time-limited sample (a09, b06). Jarosz et al. (2019), with think-aloud, found partial mediation (a08). Laurence and Macedo (2023) say it is still unclear whether the relation holds at all (a09).

**Strategy is not fixed (2020).** Gonthier and Roulin (2020): within one person, constructive matching falls and elimination rises as items get harder (b04). Only people high in both WM and need for cognition kept building late.

**Proxies come under attack (2020-2023).** Kucharsky et al. (2020) clustered gaze without prior labels and found row-wise vs column-wise scanning, not a clean elimination class (b22, a30). Rivollier et al. (2021) moved the paradigm to a mouse interface (a04). de Winter et al. (2023) showed that visual complexity and cell centrality explain fixation counts and response time (b34). Laurence and Macedo (2023) review the field and say the two-strategy paradigm still needs confirmation (b01).

**Machine shortcuts (2019-2025).** RAVEN (Zhang 2019) had an answer-set flaw: the correct option is the one most like the others. A model that sees only the options beats models that see the matrix (a21, c20). That is response elimination in pure form. I-RAVEN (Hu 2021) fixed it. The same pattern was then found in text MCQs: choices-only prompts beat the majority baseline (a27, a28, d03). Reasoning models were found to exploit options harder (d01, d02).

**LLM strategy tests (2023-2026).** Webb et al. (2023): GPT-3 on text digit matrices, generative and multiple-choice formats (a22). Hersche et al. (2024): a build-first ("predictive") format vs a candidate-in-view ("discriminative") format for GPT-4 and Llama-3 (c01). Camposampiero et al. (2025): reasoning models under perceptual noise (c04). Raman et al. (2025): reasoning before vs after seeing options (d01). Haznitrama et al. (2026): text matrices with and without options (d12).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Better scorers spend more of the item on the matrix, look at options later, toggle less | Vigneau N=55: time on matrix r=.48, time on options r=-.44, toggle rate r=-.43, latency to first toggle r=.41. Rivollier N=130: time on matrix r=.56, toggle rate r=-.55, latency r=.70. Each extra toggle per minute cuts success 3.5% (b=-0.14); +10% matrix time adds 5.8% | a03, a04 (Vigneau via Rivollier table) | [E] (3 samples, 2 labs) |
| Same direction in larger gaze samples | von Gugelberg N=210 (a12) and N=300 (b15): higher ability goes with lower toggle rate, more matrix time, later first look. N=34 WMT-2: toggle rate r=-.68 (45% of variance). N=192 APM: count of constructive items r=.31 with score | a12, a13, d09, d11 | [E] |
| Total toggle count alone is a weak index | Vigneau r=-.27 (N=55) vs Rivollier r=.02, n.s. (N=130). Rate, latency and matrix time are the robust ones | a03, a04 | [E] (contradiction recorded) |
| Forcing build-first raised APM score | 18 odd items, N=250. Constructive group (n=116, matrix alone 15+ s) 12.77 (SD 2.35) vs control (n=134) 10.45 (SD 3.70); F(1,246)=37.40, partial eta2=.13. WM-score r fell .34 to .20 (shared variance 11.6% to 4%). Interaction F=4.80, p=.029, eta2=.02 | b05 | [S] |
| Forced delay helps only if the build can succeed | Rivollier Exp 2: success at option onset .78 (constrained, n=29) vs .65 (n=33), p=.047. Benefit reverses for answers coming more than 49 s after options appear (16% of trials); interaction b=-0.013, p=.03 | a05 | [S] |
| Strategy shifts with item difficulty within a person | Two samples of 100. Item-level r(34): constructive with accuracy .82; elimination -.85; strategy index with accuracy .89 (78% of item variance). Spearman difficulty vs elimination .58 (N=192) | b04, b12 | [E] (self-report and gaze) |
| Gaze and self-report disagree on drift across the test | von Gugelberg N=210: toggle rate fell and matrix time rose (more building) but first look at options came earlier (more eliminating). Change tied to item position, not ability | a12, b14 | [C] |
| Strategy mediates WM-reasoning link: three answers | Full (N=250, N=93); partial (think-aloud); none (larger time-limited sample) | b05, a08, b06 | [C] |
| Pure elimination is rare | Think-aloud: over 50% constructive, about 3% pure elimination, rest hybrid or guess. No accuracy by strategy found | a08, d08 | [S] |
| Time pressure lowers accuracy and constructive matching | N=295 (97/99/99), d=0.35 with response time controlled; only untimed vs 20 min significant for accuracy; reliability under .70 at 10 min | b11 | [S] |
| Practice gain is partly strategy | N=35, cross-validated R2=.32 (fit .56); after partialling, retest gain t(34)=.30 | b10 | [S] (a16, b09 second-hand) |
| Children: same direction | 6 and 9 year olds and adults on 24 items: relations vs accuracy r=.58 (9y), .39 (6y); 6-year-olds below chance often picked a duplicate answer. N=67 aged 7-8: rows and columns count strongest predictor. Counter: Chen 2016 toggling r=.41 in children | b16, b17 | [E] with a counter-result |
| Construction format raises validity | Weber 2023: n=198 and 169, partial credit predicts GPA better, mainly at lower ability. Becker 2016, Arendasy 2013 second-hand | a19, a11, b19, b20 | [S] |
| Original RAVEN leaks the answer (machine elimination) | RAVEN: ResNet 53.4, CoPINet 91.4; context-blind ResNet 71.9, context-blind CoPINet 94.2. I-RAVEN: ResNet 40.3, CoPINet 46.1; context-blind 12.2 and 14.2 (chance 12.5). SRAN 60.8 vs 60.7 | a21, c20 | [E] |
| LLM choices-only shortcut on MCQ | Beat majority in 11 of 12 model-dataset cases, up to +0.33. Inferred question matched original 42% of 43 ARC cases. Reasoning helps full MCQ in 25 of 36 settings, choices-only in 15 of 36 | a27, b28, a28 | [E] |
| Reasoning after options adds points by exploiting options | Models above about 50B score 30 to 40 points higher with options before chain of thought. NOTA cuts the reasoning-model edge from 12.63 to 5.29 points; reasoning models picked NOTA 55.82% (true 25%) | d01, d02 | [S] (one team; related a28) |
| Predict-then-match beats show-candidates (GPT-4, I-RAVEN center) | Discriminative 56.0 to 60.0; predictive 74.8; per-attribute queries 91.4; n=7 self-consistency 93.2. Llama-3 70B: 22.4-22.8 discriminative, 79.0 predictive, 83.2, 84.8 | c01, c05 | [S] |
| Build-style output is fragile on arithmetic rules and wide ranges | GPT-4 arithmetic 27.1 entangled vs 73.6 disentangled; 8.4 at range 1000. Llama-3 31.0 vs 45.0. o3-mini 86.6 to 17.0 on I-RAVEN-X, R1 80.6 to 23.2, ARLC 98.6 to 88.0 | c02, c03, c04, a25 | [E] |
| Reasoning tokens did not rescue noisy input | o3-mini medium 5445 tokens (86.6), high 9867 tokens (92.6); R1 4486 (80.6); about 3.4x more reasoning tokens on the noisy version with no gain | c05, c04 | [E] (re-opened) |
| Direction of the "options help" effect varies by model | GPT-4 text RAVEN: open .410, MC .697. NeuroCognition: GPT-5 .540 MC to .605 Gen; Claude Sonnet 4 .560 to .385; Grok 4 Fast .690 to .555. Reasoning off helps text MC (p=.021) not Gen (p=.83) | c15, d12, d13 | [C] |
| Image VLMs near chance | GPT-4V Mensa .24, IntelligenceTest .16, RAVEN .12 (chance .16/.16/.12); Gemini Pro .15/.18/.11; humans 84.67% on RAVEN. MARVEL: humans 68.86%, models about 25% | a24, c07, c24 | [E] |
| Options help models that cannot build | GPT-4o MaRs-VQA 24.58 question only, 33.96 with options, 36.46 with option descriptions. Multi-round elimination with reflection 41.96; 1-shot 42.08; o1 52.29; humans 81.00 | c10, c11 | [S] |
| Chain of thought did not help on text RAVEN (2023 models) | GPT-4 open .385 vs .410; MC .596 vs .697 | c16 | [S] |
| Up-front hints hurt, corrective feedback helped | Relative gain up to 100% for GPT-4V on IQ50 (50 items) | c14 | [S] |
| Built answers generalise weakly | Seq2seq transformer: 96.9% token accuracy, 45.3% full-answer accuracy with a rule omitted in training. Qwen2-VL tuned: 72.71 on MaRs-VQA, 31.96 on RAVEN | c25, c12 | [E] |
| Forced pure elimination is weak for older LLMs; soft pruning can help | Two-option questions: reasoning toward the wrong option lost to direct answer in every model and dataset; 7B and 13B often below 50%. POE scorer (FLAN-T5-XL, 100 items/task): Logical Deduction 39.8 to 53.6; Conceptual Combinations 60.2 to 72.2; ANLI 57.8 to 55.0 | d05, d06 | [C] |

## 4. Mechanisms and models

Each mechanism is written so it can be coded.

**4.1 The two strategies as procedures.** Formal version from Yang, McGreggor and Kunda (c22):

- Constructive matching: infer a transformation T from the matrix, apply T to build answer A, then test A against the options.
- Response elimination: infer T1 from the matrix. For each option O, infer T2 using O. Compare T1 and T2. Eliminate O if they fail.
- Option-informed construction sits between: use the options to tune the parameters of the construction.

In an LLM pipeline: constructive = call 1 sees only the stem and writes a predicted answer; call 2 matches it to options. Elimination = one call sees stem and options together.

**4.2 Gaze and mouse indices (proxy for what the solver is doing).**

- Proportional time on matrix (PTM) = time on matrix / total item time. Higher means build.
- Latency to first toggle (LFT) = time before the first look at options. Longer means build.
- Toggle rate = matrix-option switches per minute. Lower means build.
- Rate of latency to first toggle (RLT) = LFT / item time.
- Random forest on 7 features picked PTM first, then RLT, then LFT (a14).

Agent analogues (not validated, K28 says no study exists): tokens before the first option is named; number of alternations between problem and option talk; share of tokens spent on the problem. Log them and see which predicts accuracy at equal tokens. Hand-code a sample to check the label (K07).

**4.3 Multi-strategy psychometric model (Liu et al. 2023, b13).** A strategy-selection part (which strategy on this item) plus a strategy-implementation part (success given strategy). Built-in assumption: constructive matching never yields lower success than elimination. That assumption is not tested. Use only as a template for a per-item logger: strategy choice, then success.

**4.4 Adaptive switch.** Human data: strategy moves from constructive to elimination as difficulty rises (b04), and forced delay backfires past about 49 s after options appear (a05). A rule consistent with both: build first, set a stall signal (for example no candidate after N tokens, or the build fails the check), and then allow option viewing. This is an inference, not a tested procedure.

**4.5 Predict-then-select (Hersche, c01).** Show only the context. The model writes attribute values of the missing panel. Code picks the candidate with the most overlap. Optional: one query per attribute (3x queries), then self-consistency n=7. Code does the selecting (fits G5).

**4.6 Machine elimination shortcut.** Option-set statistics: the right answer shares the most attributes with the others (central node of the candidate graph, c20). Detect it with a context-blind control: train or prompt on options alone and compare with the full condition. If the control beats chance, the set leaks.

**4.7 Two-stage MCQ (Raman, d01).** Stage 1: reason on the stem only. Stage 2: show options and pick. Compare with reasoning with options in view. The gap measures how much of the score comes from option exploitation.

**4.8 Soft elimination (POE, d06).** Score every option. Mask options below the average score. Choose among the rest. Likelihood scoring, not hard pruning.

**4.9 Hybrid isolate-and-eliminate (d08).** Per round: name one rule, strike options that break it, stop when one remains. Fixed procedure, easy to code. No accuracy figure exists for the human version.

## 5. What holds up

**Replicated in several samples.** The gaze signature of higher ability (more matrix time, later first look, lower toggle rate) holds from N=55 (2006) to N=300 (2026), across eye tracker, mouse and clustering (a03, a04, a12, a13, d09, d11). Independent labs: Vigneau, Rivollier, Laurence, Liu, von Gugelberg (the two von Gugelberg samples share a lab; Liu a14 and b12 share data). Strategy shifts with item difficulty holds in self-report (b04), clustering (b12, d11) and the 1984 report (second-hand). The RAVEN answer-set leak is a design fact confirmed by I-RAVEN (a21).

**Did not replicate or is contested.**

- Full mediation of WM by strategy: not found in a larger time-limited sample (b06). Disagreement is partly about method (questionnaire vs think-aloud vs eye).
- Toggle count as a predictor: r=-.27 in one sample, r=.02 in another.
- A clean elimination cluster: not found by unsupervised clustering (b22). Pure elimination is only about 3% in think-aloud (a08). Elimination may be "frustrated constructive matching" (a30).
- Drift toward elimination over the test: self-report says yes (b04). Gaze in N=210 says it depends on the metric (a12).
- Children: toggling correlated positively with accuracy (r=.41, Chen 2016, cited in b17), against the adult rule.

**Moderators.**

- Item difficulty: harder items bring more elimination (b04, b12).
- Working memory and need for cognition: only people high in both kept building late (b04).
- Time pressure: lowers constructive matching, confidence and accuracy (b11); time limits may suppress strategy variability (critique of b06).
- Representation: verbal-analytical puzzles show more saccades read as elimination (a17); visual complexity and centrality drive gaze (b34).
- Interface: mouse cuts toggles from about 21 to 2.3 per item but proportional time stays similar (76% vs 84%) (a04).
- Age and ability: young children and people with intellectual disability look at options sooner and toggle more (b16, b21).

**Interventions that worked (humans).** Hide options for 15 s or more (b05). Hide options until a keypress (a10, second-hand: improved monitoring). Teach the rules (b09). Construction answer format (a11, a19).

**Interventions that did not, or reversed.** Long forced delay for slow solvers (a05). Mediation did not hold when time-limited (b06).

**Interventions on LLMs.** Worked: predict-then-match for GPT-4 (c01); per-attribute disentangling for GPT-4 (arithmetic 27.1 to 73.6) but weaker for Llama-3 (31.0 to 45.0); multi-round elimination with reflection for GPT-4o (33.96 to 41.96, not separated from reflection); corrective feedback after a draft (c14). Did not work: chain of thought on text RAVEN for 2023 models (c16); extra reasoning tokens under noise (c04); up-front hints (c14); pattern hints on text RAPM (d13); oracle rationale after oracle description (c08); fine-tuning for transfer (c12).

**Weak spots in the evidence.** Almost all human data are university students on the APM with small N. Strategy labels are proxies (gaze, self-report). Founding paper unread. Two agents often recorded the same paper; count once (critique note 3).

## 6. Language models

**There is no study that does what we want.** Critique and d16 agree: nobody has run "build-first vs eliminate-first at equal tokens" on matrices for a reasoning model. Nearest are Raman (knowledge MCQ, d01), Hersche (GPT-4, symbolic, c01) and Haznitrama (text RAPM, d12).

**Machine elimination is real.** On original RAVEN, context-blind models beat full models (94.2 vs 91.4 for CoPINet). On I-RAVEN they fall to 12.2-14.2% (chance 12.5%) (a21). On text MCQ, choices-only beats the majority baseline in 11 of 12 cases (a27). Reasoning models eliminate, infer the missing question, and list option properties (a28). With options shown before reasoning, models above about 50B gain 30 to 40 points (d01). A NOTA option cuts the reasoning-model edge from 12.63 to 5.29 points (d02). Position bias is a related shortcut: gaps of 13% to 75% on reordering, up to 8 points regained by calibration (b30). Open-style questions drop 25 points on average for GPT-4: 88.69 MCQ vs 61.31 open (b29; part of this is a grading artefact).

**Build-first in an LLM.** Hersche (c01): on I-RAVEN center with symbolic attributes, GPT-4 predictive 74.8 vs 56.0-60.0 discriminative. Llama-3 70B 79.0 vs 22.4-22.8. With one query per attribute 91.4 and 83.2. n=7 self-consistency 93.2 and 84.8. The opposite choice: Camposampiero (c06) moved to candidate choice because free-building reasoning models found valid-looking but irrelevant relations (for example between binary encodings). No accuracy was given for that switch. Different models and prompts, so no head-to-head.

**Reasoning models under noise.** o3-mini 86.6 to 17.0; R1 80.6 to 23.2; ARLC (abduction plus symbolic) 98.6 to 88.0 (a25). Token counts: o3-mini medium 5445, high 9867, R1 4486, about two orders more than a plain LLM (c05). Arithmetic rules and wide ranges break build-style answers (GPT-4 73.6 to 8.4 at range 1000; o3-mini 60.8, R1 65.8 at 1000) (c05).

**Perception is the first bottleneck for images.** GPT-4V near chance (a24). Oracle text description lifts a lot (text-only in-context example 100%, image plus text 80%, image query 20%, three hand-built RPMs, c08). An oracle rationale on top does not help. MARVEL: with text descriptions on a subset, 11.57% to 44.21%, GPT-4V 65.26% (c24). For image matrices, test with text descriptions to separate perception from strategy.

**Options as a crutch.** MaRs-VQA: GPT-4o 24.58 without options, 33.96 with (c10). Fine-tuned model 26.32 without, 72.71 with. Authors read this as shallow matching against options. Multi-round elimination with reflection: 41.96 (c11). Gendron (c15): giving options helps all models systematically (GPT-4 .410 to .697) but the models cannot reliably recognise the right answer.

**Format reversals (fragile).** NeuroCognition (d12, d13): GPT-5 gains from generative format (.540 to .605); Claude Sonnet 4 loses (.560 to .385); Grok 4 Fast loses (.690 to .555). Single run, 15 items per format in the human pilot of N=9, Sonnet 4 with reasoning off. Switching reasoning off helped text MC (p=.021) and not text generation (p=.83). The authors' reading (MC rewards elimination, long chains get pulled to distractors) is untested.

**Elimination prompts.** Forced reasoning toward wrong options lost to direct answer on two-option questions in older models (d05). A soft scorer helped a 3B model on 5 of 8 tasks (d06). No reasoning-model test.

**Strategy observed in traces.** GPT-4V often used options and grid together to form and test hypotheses (c09): qualitative, three hand-built items, no coded sample. Neural RPM models almost all follow response elimination (c23).

**Generalisation.** Built answers fail on unseen rules: 96.9% per token vs 45.3% full answer (c25). Fine-tuned Qwen2-VL 31.96 on RAVEN (c12). Test our scaffold on held-out rule types.

**Chain of thought.** For 2023 models CoT did not lift text RAVEN (c16). Reasoning models since then reach 86.6-92.6 on symbolic I-RAVEN (c05). Whether scaffold reasoning pays on matrices is something we have to measure, not assume.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Run an options-only control (and a stem-only control where relevant) on every multiple-choice benchmark we use. Report the gap. Do not credit the scaffold with leaked gain. | G7 (pay for itself), eval | [E] | K10, K11; a21, c20, a27, a28, d01, d02, d03 |
| A2 | Prefer free-form or constructed-answer scoring (answer matching) when judging the agent, and add a NOTA slot where options must stay. | G7, eval | [E] for the leak; [S] for the NOTA fix | K11, K20; d02, d04, d07, b29 |
| A3 | Use an exact tool (code) for arithmetic and numeric rules instead of reasoning text. Decompose to per-attribute queries when no tool exists. | O3 Decompose, S5 | [E] | K14; c02, c03, c04, c05, a25 |
| A4 | Evaluate on held-out rule types and on perturbed inputs, not only in-distribution items. | G3 | [E] | K21; c25, c12, b25 |
| A5 | When labelling a trace as build or eliminate, hand-code a sample. Never trust one metric. | log section 6 | [E] | K07; a04, a30, b22, b34 |
| A6 | Log trace metrics on every item: tokens before the first option is named, number of alternations between problem and option talk, share of tokens on the problem. Logging only; no behaviour change. | log section 6 | measurement only (K28 open) | K01, K28; a03, a04, d09, d11 |
| A7 | Do not put pure elimination (reasoning toward wrong options) in as a default move. | S4 | [C] leaning no | K26; d05, d06 |
| A8 | For image items, test the text-description version first to separate perception from reasoning. | S0/S2 | [E] | K16; a24, c07, c08, c24 |
| A9 | Corrective feedback on a draft beats up-front strategy hints. This agrees with G2 (revise from real output). | S5 | [S], consistent with G2 | K18; a23, c14 |

### Test first (not yet established; each is in UNKNOWNS.md)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Build-first: S3 writes a predicted answer from the stem alone, then S4 matches options. Compare with stem and options together at equal tokens. | S3/S4 | [S] | K02, K13, K25; b05, c01, d01 |
| T2 | Adaptive switch: build first, allow option viewing only after a stall. | S3/S4/S6 | [S] human indirect | K03, K04, K28; a05, b04 |
| T3 | Hybrid isolate-and-eliminate as an explicit loop (one rule, strike options, repeat). | S4, O3 | [S] | K06, K27; a08, d08 |
| T4 | Soft pruning: score all, drop clear mismatches, then choose. | S4 | [C] | K26; d05, d06 |
| T5 | One query per attribute vs one entangled query. | O3 | [S] | K13; c01, c02 |
| T6 | Rule check: test every built rule against all rows before use (guard against valid-looking but irrelevant relations). | S4, G3 | [S] qualitative | K15; c06 |
| T7 | Trace metric as a stall detector (for G12 and S6 triggers). | S6, G12 | open | K28; d16 |
| T8 | Stored build-first routine as a lesson in memory. | memory | [E] in humans (practice), untested for agents | K09; a16, b09, b10 |
| T9 | Calibration under build-first. | S6/G10 | [S] human, unread | K23; a10, b08 |
| T10 | Hide options during long reasoning on MC items where chains are long. | S3 | [S] | K29; d13 |

Cross-links to other subfields in this run: Matrix tests and task analysis, Methods and measurement, Calibration and overconfidence, Working memory, Cognitive load, Search over thoughts, Priming of orientation. We only note links here.

## 8. Concrete tests on our bench

All arms get the same total token budget (stem + options + reasoning + output). Count setup and the extra call in the budget (G7). At least 3 runs per arm because single runs were the weak point in d12.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 build-first vs options-in-view | I-RAVEN center (symbolic), plus our MC items | A: call 1 stem only, writes predicted answer; call 2 shows options, code matches. B: stem and options together, one chain. | Accuracy; paired difference with bootstrap CI | Plus 5 to 15 points for A on a non-reasoning model (Hersche: +15-19); smaller or zero on a reasoning model (Raman suggests option exploitation drives much of the gap) |
| B2 leak controls | Every MC set in the bench | Full item; options only; stem only; options plus NOTA | Accuracy of each; gap full minus options-only | Options-only above chance means the set leaks; I-RAVEN should be near 12.5%, RAVEN-style sets not |
| B3 adaptive switch | I-RAVEN, I-RAVEN-X, and a hard subset | A: always build-first. B: build-first, allow options after stall (no candidate by N tokens, or failed rule check). C: options in view. | Accuracy by item difficulty; tokens | B at least equal to A on easy items and better on hard items, as in a05 and b04 |
| B4 hybrid loop | I-RAVEN center, 2x2, 3x3 | A: pure build-then-match. B: per round one rule, strike options, repeat. | Accuracy; tokens used | Unknown. Prior from humans only (hybrid exists, no accuracy figure) |
| B5 elimination variants | MC items with 4 and 8 options | Choose directly; prune clear mismatches then choose; reason toward the wrong options | Accuracy | Hard pruning no better than direct (d05); soft pruning perhaps plus 2 to 5 (d06, small model) |
| B6 per-attribute vs entangled | I-RAVEN with arithmetic rules; I-RAVEN-X range 100 and 1000 | One entangled query; one query per attribute; code tool for arithmetic | Arithmetic-rule accuracy | Large plus for decomposition and tool (27.1 to 73.6 for GPT-4); tool at range 1000 well beyond 8.4 |
| B7 trace metric | Same runs as B1 and B3 | Log tokens before first option mention and alternations | Correlation with accuracy at equal tokens, controlling for item difficulty | Negative for alternations and positive for stem-first share if the human pattern transfers (r of .3 to .5 in humans) |
| B8 option hiding during long reasoning | 8-option text items | Reasoning on; reasoning short; options hidden until the end | Accuracy | Short or hidden-option arm wins on MC, no change on generation (d13 pattern) |
| B9 calibration | Same runs as B1 | Stated confidence per arm | Brier score or ECE per arm | Better calibration for build-first (Mitchum and Kelley direction, unread) |
| B10 image vs text description | Image matrices | Image; oracle text description | Accuracy | Large gain for text (c08: 20 to 80 on three items) |
| B11 held-out rules | I-RAVEN, one rule type held out of any in-context examples or memory lessons | Scaffold with and without stored lessons | Accuracy on the held-out rule | Lessons help only for the same class (memory rule) |

## 9. What does not transfer, and why

- **Eye movements and toggling.** The indices are human proxies for working-memory-limited gaze. An LLM has the whole context at once. The nearest analogue is token order, and no study has validated it (K28).
- **Working-memory mediation.** The story that build-first helps because it lowers the memory load of holding options may not carry. Even in humans it is contested (K05). For LLMs the analogue is context length and distractors in context, which fits K29 only weakly.
- **Time pressure effects.** Human time limits suppress strategy variability and confidence (b11). Token budgets are a different resource. Cut the budget and measure; do not borrow d=.35.
- **Gains from teaching rules.** Loesche et al. taught the rules to people. In an agent the rules are already in the model or not. The nearest thing is memory lessons (K09).
- **Child and clinical results.** Different cognitive load profile and perception limits. Weak transfer (K22).
- **Interface effects.** A mouse changes the cost of switching. LLM option viewing has no such cost, so a rule like "make switching costly" has no agent counterpart except by prompt structure (separate calls).
- **Strategy self-report.** LLM reasoning text is not evidence of what drove the answer (G10). Strategy labels from traces need hand coding.
- **Hard-hiding options in all cases.** Rivollier shows reversal for slow solvers (a05). Camposampiero (c06) reports that free building sometimes finds irrelevant relations. Build-first is not a blanket rule.
- **The 1984 numbers.** Not read. Do not use.
- **Image-only results.** In 2024 vision models, perception error dominates, so strategy effects are not visible (a24, c08).

## 10. Open questions

1. What did Bethell-Fox, Lohman and Snow (1984) actually measure: N, effect sizes, the difficulty at which people switch? (Paywalled; stays open.)
2. Does forcing build-first raise accuracy of a reasoning model at equal tokens on I-RAVEN and on non-matrix MC? No study.
3. Is explicit elimination better, worse or equal to build-then-match for reasoning models, and does it depend on text vs image?
4. Is the hybrid (isolate one rule, eliminate, repeat) better than either pure strategy? No accuracy by strategy exists for humans.
5. Which agent trace metric corresponds to proportional time on matrix or toggle rate, and does it predict accuracy?
6. Does an adaptive build-then-fall-back beat always-build?
7. How much of reasoning-model gain on MC benchmarks is leakage vs real reasoning on our own benchmark?
8. Why did Claude Sonnet 4 lose and GPT-5 gain when options were removed in the 2026 text study? Replicate with more runs and a larger human sample.
9. Does build-first change calibration in LLMs? (Mitchum and Kelley 2010 unread.)
10. Do hard-rule failures need an exact tool in S5, or does decomposition close the gap at equal tokens?
11. Is the strategy construct one thing? Gaze metrics disagree (b14), clustering finds no clean elimination class (b22), and visual features confound the indices (b34).
12. Does full mediation by strategy hold anywhere with a large untimed sample? Three studies give three answers.

## 11. Sources

[V] = opened and read (as recorded in the evidence files). [M] = snippet or abstract only, or known only through a review.

**Founding and reviews**

- [M] Bethell-Fox, Lohman and Snow (1984), Adaptive reasoning: componential and eye movement analysis of geometric analogy performance. Intelligence 8. https://doi.org/10.1016/0160-2896(84)90009-6 (b02, d10; known through reviews)
- [V] Laurence and Macedo (2023), Cognitive strategies in matrix-reasoning tasks: State of the art. Psychonomic Bulletin and Review 30:147-159. https://doi.org/10.3758/s13423-022-02160-7 (a01, a02, b01, d08)
- [V] Laurence, Mecca, Serpa, Martin and Macedo (2018), Eye movements and cognitive strategy in a fluid intelligence test. Front. Psychol. https://doi.org/10.3389/fpsyg.2018.00380 (d09)
- [V] Gonthier (2022), Cross-cultural differences in visuo-spatial processing. https://pmc.ncbi.nlm.nih.gov/articles/PMC8816982/ (b23)

**Human strategy studies**

- [M] Vigneau, Caissie and Bors (2006), Intelligence. https://doi.org/10.1016/j.intell.2005.11.003 (a03, b03; numbers via Rivollier and the review)
- [V] Rivollier, Quinton, Gonthier and Smeding (2021), Looking with the (computer) mouse. Behav. Res. Methods. https://doi.org/10.3758/s13428-020-01484-3 (a04, a05, a30)
- [V] Gonthier and Thomassin (2015), Strategy use fully mediates the relationship between WM capacity and performance on Raven's matrices. J. Exp. Psychol. General. https://univ-rennes2.hal.science/hal-01725065/document (b05; a06 abstract only)
- [V] Gonthier and Roulin (2020), Intraindividual strategy shifts in Raven's matrices. https://hal.science/hal-03288841/document (b04; a07 abstract only)
- [M] Jastrzebski, Ciechanowska and Chuderski (2018), via Laurence and Macedo 2023 (a09, b06)
- [M] Jarosz, Raden and Wiley (2019), WMC and strategy use on the RAPM. Intelligence 77. https://ideas.repec.org/a/eee/intell/v77y2019ics0160289619301692.html (a08, b07, d15)
- [M] Mitchum and Kelley (2010), Solve the problem first. https://doi.org/10.1037/a0019182 (a10, b08)
- [M] Loesche, Wiley and Hasselhorn (2015), via the review (b09)
- [V] Hayes, Petrov and Sederberg (2015), Do we really become smarter when our fluid-intelligence test scores improve? https://pmc.ncbi.nlm.nih.gov/articles/PMC4226176/ (b10; a16)
- [M] Hayes, Petrov and Sederberg (2011), sequential eye movements. https://doi.org/10.1167/11.10.10 (a15)
- [V] Gonthier (2023), Should intelligence tests be speeded or unspeeded? https://hal.science/hal-04229851/document (b11)
- [V] von Gugelberg and Troche (2025), strategy and item-position effect. https://pmc.ncbi.nlm.nih.gov/articles/PMC12295732/ (a12, b14)
- [V] von Gugelberg (2026), problem-solving behavior in reasoning tests. https://pmc.ncbi.nlm.nih.gov/articles/PMC13608805/ (a13, b15)
- [V] Liu, He, Man and Zhan (2025), critical eye-tracking metrics. https://pmc.ncbi.nlm.nih.gov/articles/PMC11856599/ (a14, b12)
- [M] Liu et al. (2023), multi-strategy eye-tracking psychometric model. https://doi.org/10.1016/j.intell.2023.101782 (b13)
- [V] Liu, Man and Zhan (2024 preprint), clustering eye-tracking measures. https://osf.io/yb237 (d11)
- [M] Kucharsky et al. (2020), hidden Markov clustering. https://osf.io/wvzs9/ (b22; via review)
- [V] Srivastava, Jaarsveld and Sangani (2023), verbal-analytical solving. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10693350/ (a17, b33)
- [V] Laurence et al. (2023), eye gaze patterns. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10145645/ (a18)
- [V] de Winter, Dodou and Eisma (2023), visual complexity and centrality. https://pmc.ncbi.nlm.nih.gov/articles/PMC10469510/ (b34)
- [V] Niebaum and Munakata (2023), development of relational reasoning. https://pmc.ncbi.nlm.nih.gov/articles/PMC10320822/ (b16)
- [V] Hannon (2026), children's matrix problem solving. https://pmc.ncbi.nlm.nih.gov/articles/PMC13008366/ (b17)
- [M] Vakil and Lifshitz-Zehavi (2012). https://doi.org/10.1016/j.ridd.2011.11.009 (b21; via review)

**Answer format and validity**

- [M] Arendasy and Sommer (2013). https://doi.org/10.1016/j.intell.2013.03.006 (a11, b20)
- [M] Becker et al. (2016), via the review (b19)
- [V] Weber et al. (2023), log file analysis of partial solutions. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9961547/ (a19)
- [V] Weber, Koch, Spinath, Krieger and Greiff (2025), log file times. https://pmc.ncbi.nlm.nih.gov/articles/PMC12194016/ (b18)

**Datasets and machine solvers**

- [V] Zhang et al. (2019), RAVEN. https://arxiv.org/abs/1903.02741 (a20, c19)
- [V] Hu et al. (2021), Stratified Rule-Aware Network (I-RAVEN). https://arxiv.org/abs/2002.06838 (a21, b27, c20)
- [V] Yang, McGreggor and Kunda (2022), visual-imagery analogical construction. https://arxiv.org/abs/2208.13841 (c21, c22)
- [V] Generative inpainting RPM paper (2019). https://arxiv.org/abs/1911.07736 (c23)
- [V] Li (2025), rule omission in RPM. https://arxiv.org/abs/2510.03127 (a29, c25)
- [V] Hu, Storks, Lewis and Chai (2023), in-context analogical reasoning. https://arxiv.org/abs/2305.17626 (c18)

**LLM studies**

- [V] Webb, Holyoak and Lu (2023), emergent analogical reasoning. https://arxiv.org/abs/2212.09196 (a22, b24, c17)
- [V] Lewis and Mitchell (2024), counterfactual analogy tasks. https://arxiv.org/abs/2402.08955 (b25)
- [V] Gendron et al. (2023), LLMs are not strong abstract reasoners. https://arxiv.org/abs/2305.19555 (b26, c15, c16)
- [V] Ahrabian et al. (2024), nonverbal abstract reasoning with MLLMs. https://arxiv.org/abs/2401.12117 (a23, c13, c14)
- [V] Zhang et al. (2024), How far are we from intelligent visual deductive reasoning. https://arxiv.org/abs/2403.04732 (a24, c07, c08, c09)
- [V] Hersche et al. (2024), Towards learning to reason. https://arxiv.org/abs/2412.05586 (c01, c02, c03)
- [V] Camposampiero et al. (2025), Large reasoning models and analogical reasoning under perceptual uncertainty. https://arxiv.org/abs/2503.11207 (a25, c04, c05, c06)
- [V] Haznitrama, Ardi and Oh (2026), NeuroCognition. https://arxiv.org/abs/2603.02540 (a26, c26, d12, d13)
- [V] Cao et al. (2025), VCog-Bench / MaRs-VQA. https://arxiv.org/abs/2406.10424 (b31, c10, c11, c12)
- [V] Cai et al. (2025), MM-IQ. https://arxiv.org/abs/2502.00698 (b32)
- [V] Jiang et al. (2024), MARVEL. https://arxiv.org/abs/2404.13591 (c24)
- [V] Mitchell, Palmarini and Moskvichev (2023), ConceptARC. https://arxiv.org/abs/2311.09247 (c27)
- [M] Urgun and Ari (2025), RAVEN-FAIR architectures. https://arxiv.org/abs/2511.11916 (d14; abstract only)

**Multiple-choice shortcuts and elimination in LLMs**

- [V] Balepur, Ravichander and Rudinger (2024), Artifacts or abduction. https://arxiv.org/abs/2402.12483 (a27, b28, d03)
- [V] Balepur, Desai and Rudinger (2025), Test-time reasoners are strategic multiple-choice test-takers. https://arxiv.org/abs/2510.07761 (a28)
- [V] Raman, Lundy and Leyton-Brown (2025), Reasoning models are test exploiters. https://arxiv.org/abs/2507.15337 (d01, d02)
- [V] Balepur, Rudinger and Boyd-Graber (2025), Which of these best describes multiple choice evaluation with LLMs. https://arxiv.org/abs/2502.14127 (d04)
- [V] Balepur, Palta and Rudinger (2024), It's not easy being wrong. https://arxiv.org/abs/2311.07532 (d05)
- [V] Ma and Du (2023), POE. https://arxiv.org/abs/2310.15575 (d06)
- [V] Chandak et al. (2025), Answer matching outperforms multiple choice. https://arxiv.org/abs/2507.02856 (d07; exact MC figure not extracted)
- [V] Myrzakhan, Bsharat and Shen (2024), Open-LLM-Leaderboard. https://arxiv.org/abs/2406.07545 (b29)
- [V] Zheng et al. (2024), robustness of MC selectors; Pezeshkpour and Hruschka. https://arxiv.org/abs/2309.03882 (b30; abstracts and intros)
- [M] Search coverage note (2026-11-10): no study of build-first vs elimination for reasoning models found (d16)
