# Transfer of learning: deep document

*Subfield A05.05. Evidence in this folder: evidence_a-d.jsonl (ids a01-d18), claims.jsonl (K01-K30), critique.md. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested. Evidence ids are cited in brackets.*

## 1. What it is

Transfer of learning is the effect of earlier learning on later performance in a new situation. It can help (positive transfer), hurt (negative transfer), or do nothing (zero transfer).

Standard distinctions used in the field:

- **Near vs far.** Near transfer: the new task is close to the trained one (same family, similar surface). Far transfer: the new task differs in domain, context, format or time gap.
- **Literal vs figural.** Literal: the same skill or fact is used again. Figural: a general idea is used as an analogy or metaphor for something else.
- **Low road vs high road** (Perkins and Salomon 1992). Low road: automatic, triggered by surface similarity after varied practice. High road: deliberate abstraction, forward-reaching (abstract now for later) or backward-reaching (look back from the new problem to old knowledge). [a04, a05; secondary summary only]
- **Hugging and bridging** (Perkins and Salomon). Hugging: make practice resemble the target situation. Bridging: prompt the learner to abstract and to connect. [a04]
- **Three bottlenecks** that recur across the lab work: noticing (retrieving the old case), mapping (aligning structure), abstraction (inducing a schema from cases). Hints fix noticing. Comparing two cases fixes abstraction. [a27]

Why it matters for our agent. The schema keeps a lesson line after each solved problem (S9) and uses analogues at impasses (O7). Both depend on transfer. If lessons only help on near copies of the problem they came from, a big lesson store is cheap and safe. If they must help across classes, we need a way to notice, map and check them. The human record says: near transfer is reliable, far transfer is rare without a prompt, and surface similarity drives retrieval. The LLM record says the same, with a steeper cliff.

## 2. History and theories in depth

**Formal discipline (before 1900).** The idea that Latin or geometry "trains the mind" for everything. It was discredited by the experiments below. [a05]

**Identical elements (Thorndike and Woodworth 1901).** They trained people to estimate areas of one set of shapes (rectangles 10-100 sq cm, 1,000-2,000 trials) and tested other shapes and other functions. Gains were larger for similar shapes than for different shapes in every subject but one. They concluded that practice spreads "only where identical elements are concerned in the influencing and influenced function". Mechanism they gave: a better mental standard for one shape helped others; the habit of correcting a known bias was shared. They also cited Wissler and Norsworthy for low correlations among different functions. Statistics were by probable error: in one series 31 differences were over twice the probable error and 9 over 3.5 times. [a01, a02, a03]
- Limits: tiny samples, no modern control group, graded not all-or-none results, and "element" was never defined, so any transfer can be named an identical element after the fact. [a02]
- Later check: Thorndike (1922) had skilled algebra students solve exercises in novel forms. About 50% were correct, so the strong surface-identity version does not hold either. (Second-hand.) [b13]

**Guthrie's contiguity view.** Expect little transfer. Train under the conditions of use. This is the root of "hugging". [a05]

**Production-rule version of identical elements (Singley and Anderson 1985, 1989).** Skill is a set of production rules. Transfer is proportional to shared rules. [a14, a15, b12]
- 24 computer-naive women, about 500,000 keystrokes. Learning one line editor gave near-total transfer to another line editor, moderate transfer to a screen editor (EMACS), and slight transfer from typing alone.
- Day-one savings: 150 s per edit (ED to EDT) vs 70 s (EDT to ED). The asymmetry is predicted: the ED rule set is nearly a subset of EDT. Line editor to EMACS saved about 35 s per edit, under half the line-to-line figure.
- Transfer by component: about 46% for the move-type component to EMACS vs 102% between ED and EDT; 89% for line-locating.
- In calculus they found no transfer among word-problem translation, operator choice and the like, where skills share little.
- Limits: small cells, one domain; total encapsulation of productions was too strong because they share a declarative base. A later model (Taatgen) fits transfer amount better (secondary).

**Analogical transfer and schema induction (Gick and Holyoak 1980, 1983).** The central human work on far transfer. Subjects read a source story (a general who splits his army to converge on a fortress) and then meet a target problem (Duncker's radiation problem, or Maier's two-cord problem). [a06-a10, b01-b06]
- Base rate: under 10% solve the radiation problem with no analogue.
- Memorise the story, no hint: about 30%. With a hint to use it: about 75-80%. Authors: only a third or less of those who could use the analogy noticed it. So noticing, not storage, is the bottleneck.
- Detail of each experiment is in section 3.

**Retrieval vs soundness (Gentner, Rattermann and Forbus 1993; MAC/FAC).** People retrieve old stories by surface similarity but rate relational analogies as better. Retrieval order: literal similarity > surface similarity > analogy >= first-order relations only. Soundness order: analogy > surface similarity > surface only. In experiment 3 the surface-similar cue was recalled 52%, purely relational analogy 7%. In a recognition choice task, people picked the literal match 82% of the time, so structure is stored; the bias is in retrieval. [a11, a12]
- The MAC/FAC model (Forbus, Gentner and Law) reproduces this with two stages. See section 4. [a13, c29]

**Taxonomy view (Barnett and Ceci 2002).** A century of dispute stalled because studies vary on many dimensions. They propose nine (content dimensions such as knowledge domain, and context dimensions such as physical and temporal setting) and argue one far-transfer effect size is misguided. Only the abstract was read here. [a16, b11, d12]

**Skeptic view (Detterman 1993).** Transfer is rare and weak unless situations are nearly identical. Not opened. [b26]

**Modern cognitive-training meta-analyses (2016-2019).** Working memory, music and chess training show real near transfer, and far transfer that shrinks to about zero as control quality rises. See section 5. [b07-b10, d11]

**The "abstract vs concrete" dispute (2008-2020).** Original: abstract training transfers better. Replications split. See section 5. [b14, b15]

**LLM era (2022-2026).** Analogical reasoning in LLMs (Webb et al. 2023), counter-evidence from altered forms (Lewis and Mitchell, Hodel and West, Wu et al., Stevenson et al.), narrative analogy (ARN), analogical prompting, and agent memory that stores lessons, workflows and skills. See section 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Transfer tracks shared elements; larger to similar shapes | Gain larger for similar shapes in every subject but one; ~125 pieces; 1,000-2,000 training trials | Thorndike and Woodworth 1901 [a01] | Established (small N) |
| Production overlap predicts skill transfer | Line-editor to line-editor ~100% (102% move-type); to EMACS ~46%; ED to EDT 150 s/edit saved vs 70 s reverse; N=24 | Singley and Anderson 1985/89 [a14, b12] | Established |
| Base rate of radiation solution with no analogue | Under 10% | Gick and Holyoak 1980/83 [a06] | Established |
| Memorised source, no hint | ~30% before hint, ~75-80% with hint | Gick and Holyoak 1983 [a06, b01] | Established |
| Same gap on a second problem (cord) | N=69. Before hint: analog groups 71% vs control 20%. Total: 98% vs 30%. Recall vs summary no difference | G&H 1983 Exp 1 [a07, b02] | Established |
| Principle sentence added to one story does not help | N=88. Before hint: analog+principle 32% (n=31), analog 29% (n=28), principle only 28% (n=29). Total 80/79/66%. G2(2)=2.05, p=.36 | G&H 1983 Exp 2 [a08, b03] | Single lab |
| Diagram does not help noticing | Diagram-only 1 of 15 (7%) before hint; 67% total vs 78% for analog groups | G&H 1983 Exp 3 [b04] | Single lab |
| Two analogues beat one | N=98. Before hint 45% (two) vs 21% (one + control); total 80% vs 53%. G2=6.35, p<.01 and 8.36, p<.003. Similar vs dissimilar pair: 39 vs 52%, ns | G&H 1983 Exp 4 [a09, b05] | Established (with MBA replication) |
| Schema quality predicts transfer | Good schema 21% of subjects, intermediate 20%, poor 59%. Good schema: 91% solved before hint | G&H 1983 Exp 4 [b05, a10] | Correlational |
| Principle helps once two cases exist | 62% vs 40% before hint (p<.01); total 82% vs 67%; good schemas 44% vs 10% | G&H 1983 Exp 5 [b06] | Single lab |
| Diagram helps after comparison | N=189. 57% vs 37% before hint; total 92% vs 79% | G&H 1983 Exp 6 [b06] | Single lab |
| Hint lift smaller in modern business problems | Factory 6.3% unhinted, 8.7% hinted (4 of 46); HR 20.3% unhinted, 37% hinted (17 of 46); humans n=199 | 2025 strategic-decision paper [c14] | Single source |
| Retrieval follows surface; soundness follows structure | Surface-similar recalled 52% vs relational analogy 7%; choice task picks literal match 82% | Gentner et al. 1993 [a11, a12] | Established |
| Compare-two-cases in negotiation | Contingent contracts: comparison 24/60 (40%), separate 8/37 (22%), baseline 50/213 (23%); chi-square(2, N=310)=7.08, p<.05; schema 21/38 vs 12/38 | Loewenstein, Thompson and Gentner 2003 [b16] | Established (comparison vs separate p=.06) |
| Abstract vs concrete training | Original: transfer 76% vs 44% (n=18, 20). 2020 replication: 38 per condition, no abstract transfer advantage (d=-0.176), concrete better in initial learning (95% vs 70%, d=1.276) and in concrete transfer (d=0.416) | Trninic, Kapur, Sinha 2020; De Bock 2011 [b14, b15] | Contested |
| WM training near transfer | g=0.80 [0.62, 0.97] vs treated controls, 1.88 vs untreated; 87 pubs, 145 comparisons. Sala and Gobet: 0.44 (active), 0.46 (passive) | Melby-Lervag et al. 2016; Sala and Gobet 2017 [b07, b09] | Established |
| WM training far transfer | Treated controls: nonverbal 0.05 [-0.02, 0.13] (k=67), verbal 0.05, decoding 0.08, comprehension 0.15, arithmetic 0.06. Large studies (k=34) g=0.01; small (k=25) g=0.26. Follow-up g=-0.05 | Melby-Lervag et al. 2016 [b07, b08] | Established |
| Music and chess far transfer | Music passive 0.25 [0.17, 0.34] k=64 vs active 0.03 [-0.07, 0.12] k=54. WM passive 0.18, active 0.05. Chess overall 0.34; only one study had an active control (0.10). Experts beat novices ~0.5 SD; best training study ~0.10 SD | Sala and Gobet 2017 [a17, b09, b10] | Established |
| Meta-meta-analysis | Near (k=99) naive g=0.32, corrected 0.21, active-control only 0.24. Far (k=119) g=0.12 [0.08, 0.16], about 0.01 after placebo and bias control, true variance zero. (0.27 / 0.121 is from a preprint; do not cite.) | Sala et al. 2019 [d11] | Established |
| GPT-3 matches students on original analogy forms | Digit matrices N=40: OR=1.88 [1.21, 2.91]; letter strings N=57: OR=1.76; story analogies N=54: humans better, OR=0.37 | Webb, Holyoak, Lu 2023 [a18, b19, c03] | Contested |
| GPT-3 on the radiation problem | Alone: direct-ray answer. With general story: convergence. With two distractors: lost; recovered when told to consider earlier stories. Single prompts, no rates | Webb et al. 2023 [a19, c01, c02] | Qualitative |
| Altered letter strings break models | Humans 0.753 (1,876 samples); GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (6,840 each; label order inferred). Comprehension check GPT-4 0.93-1.00 | Lewis and Mitchell 2024 [a20, c04, d13] | Established for 2023 models |
| Counterfactual tasks | 11 task families; GPT-3.5 parseable programs 99% default to 62%/71%/75% on rotated settings; above chance but well below default | Wu et al. 2024 [a22, c06] | Established |
| Children vs adults vs LLMs on alphabets | Latin/Greek/symbol: adults 0.88/0.91/0.89 (N=62); children 0.62/0.66/0.67 (N=42); GPT-4o 0.85/0.63/0.48; Claude-3.5 0.68/0.62/0.46; Llama-3.1 405B 0.79/0.74/0.27; Gemma-2 27B 0.60/0.39/0.14. Prompt template moved means 0.52 to 0.74 | Stevenson et al. 2025 [b21, c10] | Established |
| ARN near vs far | Zero-shot, chance 50%. Humans 96.0, models 57.3. Near: 97.9 vs 75.0. Far: 94.1 vs 39.6 (all-model average). Partitions (near,far / near,near / far,far / far,near): models 76.9/73.2/45.3/33.9; humans 98.6/97.2/96.8/91.4; GPT-4 94.0/92.5/57.1/29.1 | Sourati et al. 2024 [b17, c07, c08, d09] | Established for 2023-24 models |
| Demonstrations on ARN | GPT-3.5 and Llama-2 gain ~10 points on far, lose much near; GPT-4 stable | Sourati et al. [b18] | Single source |
| GPT-4 noticing in business problems | Radiation analogue for factory problem: 1 of 15 unhinted, 15 of 15 hinted; Dolphin source 14 of 15 unhinted. Recall near 1.0, precision ~0.5. Humans precision up to 1.0, recall 0.06 (Radiation), 0.22 (Dolphin) | 2025 strategic-decision paper [c15, c16] | Single source |
| Analogical prompting | GSM8K: GPT-3.5 0-shot 75.0, 0-shot CoT 75.8, 5-shot CoT 76.7, self-generated 77.8; davinci-003 14.8/50.3/54.0/61.0; PaLM2 60.8/78.2/80.7/81.7. MATH GPT-3.5 33.0/33.9/34.9/37.3. Codeforces GPT-3.5-16k 8/9/11/13%. Scale: curie 2%, davinci-001 9%, davinci-002 48%, davinci-003 61% | Yasunaga et al. 2024 [a23, a25, b22] | Single source |
| Why self-generated exemplars fail | 50 failures: 28 relevant and correct exemplars yet wrong (12 generalization gap, 8 over-reliance on one exemplar, 8 other); 12 relevant but wrong; 10 irrelevant. Of 50 solved: 35 relevant and correct | Yasunaga et al. [a24] | Single source |
| Agent workflows | WebArena +51.1% relative (12.0 absolute); Mind2Web step SR cross-task 36.2 to 45.1/43.6, cross-website 30.1 to 33.7/33.9, cross-domain 18.6 to 32.6/35.5. Full-task SR only 0.7-4.8% | AWM, Wang et al. 2024 [c19, c20, d08] | Established as a pattern; step level only |
| Insights beat raw trajectories | MTL (GPT-5-mini, six coding benchmarks, Pass@3): zero-shot 0.523; trajectory 0.534; workflow 0.538; summary 0.546; insight 0.560. ALFWorld A to B: raw -9.5, insight +6.5. LifeMem airline: ReAct 0.32, Synapse 0.26, ExpeL 0.26, LifeMem 0.38 | Kim et al. 2026; Hu et al. 2026; Qiu et al. 2026 [d01, d03, d04, d05] | Established (direction); not token-matched |
| Negative transfer from raw memory | ALFWorld baseline-fail items -26.1 points; BabyAI -12.7; harm to already solved items at most -2 | Hu et al. 2026 [d04, d17] | Established direction |
| Model-judged selection no better than embeddings | Reranking 0.598, rewriting 0.608, embedding 0.630, no memory 0.584 | Kim et al. 2026 [d02] | Single source |
| Reasoning models match humans on accuracy, not on rules | ConceptARC text: o3 77.1, Gemini 2.5 Pro 66.0, Claude Sonnet 4 60.2, humans 73.0; ~27% of o3 correct answers used unintended rules vs ~7% humans | Beger et al. 2026 [d10] | Single source |
| Lift shrinks with stronger backbone | LifeMem GPT-4o-mini 28.84 to 44.13 (+15.3); DeepSeek-v3.2-exp 41.14 to 48.02 (+6.9) | Qiu et al. 2026 [d05] | Single source |
| Math SFT transfer | Huan et al.: Qwen3-14B other-reasoning 30.2 base, 45.3 SFT, 60.0 RL; non-reasoning 45.7 / 21.1 / 53.2. Ren et al. 2026: verified long-CoT lifts MATH500 77.8 to 95.1, GPQA-D 44.1 to 63.3; Countdown traces lift AIME24 14.7 to 41.7 | Huan 2025; Ren 2026 [b24, c27, c28] | Contested |

Corrections to carry forward (from critique.md): use 29% unaided and 79% total for Gick and Holyoak Exp 2, not "50% with a hint" (50 points was the hint's added share); GSM8K GPT-3.5 rows are 75.0 / 75.8 / 76.7 / 77.8; Lewis and Mitchell model row order is inferred from the extraction.

## 4. Mechanisms and models

### 4.1 Three-stage transfer pipeline (noticing, mapping, abstraction)

Treat reuse of a prior case as three separate steps. Each can fail alone.

1. **Notice.** Find the stored case that applies to the new problem. Humans do this badly for far cases (10% to 30%). GPT-4 reached 1 of 15 unhinted for the factory problem but near-perfect recall when asked to match. [a06, c15, c16]
2. **Map.** Align parts of the old case with parts of the new one (which object plays which role). LLMs fail here even with relevant, correct exemplars (28 of 50 failures). [a24]
3. **Abstract.** Induce a schema (rule with slots) from two or more cases. [a09, b16]

Implementation: log each step separately in the agent trace so a failure can be assigned to a step.

### 4.2 MAC/FAC two-stage retrieval (implementable)

- Memory holds each case as (a) a content vector (counts of predicates, object types, relation names) and (b) a structured representation (predicates with typed arguments).
- **MAC stage.** Dot product of the probe's content vector with every stored vector. Keep the best and anything within 10% of the best. Cheap, runs over the whole store, surface-biased.
- **FAC stage.** Run structural alignment on the survivors only. Accept the best structural match above a threshold.
- In the 36-story simulation (9 sets x 4 match types), MAC returned about 3.3 items on average, FAC accepted fewer, and the order LS > SS > AN matched humans. [a13]
- For our agent: MAC = embedding or tag match on problem class and shared-step signature, done in code. FAC = a typed mapping (see 4.3) checked by code. The only LLM comparison found: LLM reranking and rewriting lost to embedding similarity (0.598 and 0.608 vs 0.630). A code-checked structural stage has not been tested for LLM agents. [d02, c29]

### 4.3 Typed mapping with a code check (O7 as designed)

Given a lesson with a precondition and a target problem:
1. Lesson stores: class tag, a one-line principle, a list of role slots with types (e.g. {sequence}, {operator}), a precondition, and one or two solved instances.
2. The model proposes a role-to-object binding for the target.
3. Code checks: every slot filled, types match, the precondition predicate evaluates true on the target (where it can be computed), and the bound lesson reproduces its own source answer when run on the source instance with slots substituted.
4. If the check fails, drop the lesson. Do not let the model argue it back in.

This follows from the findings that (a) GPT-4 false-positive matching is about 50% (precision about 0.5), (b) correct-looking misaligned cases mislead (agents copy the most similar stored case), and (c) models can be right for the wrong reason (27% of o3's right answers used unintended rules). [c16, d07, d10]

### 4.4 Production-overlap model (identical elements made computable)

Skill = set of rules. Predicted transfer from A to B = |rules(A) intersect rules(B)| / |rules(B)|. It is asymmetric: transfer to the larger set is lower. For the agent: tag each lesson with the sub-operations it uses (e.g. "parse list", "binary search on answer") and rank reuse by overlap with the target's sub-operations. The 46% / 102% / 89% component figures give a rough scale of what to expect. [a15, b12]

### 4.5 Induction by comparison

Take two solved instances of the same class. Ask for what they share, written as a rule with slots. Store that, not either instance. Human effect: 45% vs 21% unaided. [a09, b16] It needs the written similarity description; in the lab, schema quality predicted transfer (good schema 91% solved). [b05]

### 4.6 Bridging as a code-triggered step

The hint effect is large (30% to 80%). An LLM has no experimenter to hint it, but code can issue the same cue: "list the stored lessons whose class tag or precondition could apply". Webb et al. saw GPT-3 recover the convergence solution after such a cue, in one qualitative run. [a19, c02] The cue costs tokens only when fired; fire it at impasses (S6), not on routine problems (consistent with G1, G11).

### 4.7 Abstraction into slots

AWM replaces example-specific values with placeholders ({product-name}). MTL found task-agnostic insights beat task-specific ones by 1.1 points (0.534 vs 0.523). [c19, d03] The mechanism: the stored text stays valid as the surface changes. Cost: less detail, so execution on the target may need the model to refill the slots.

### 4.8 Surface-feature mutation as a transfer probe

Lewis and Mitchell and Wu et al. give a ready test design: keep structure, change surface (new alphabet, base-9, rotated grid). A model that keeps accuracy has abstracted; one that drops had recited. [a20, a22] Use the same re-skin on lessons.

## 5. What holds up

### 5.1 Replicated and robust

- **Near transfer inside a trained family** is reliable. WM training near g = 0.44-0.80 depending on control type and study pool; meta-meta-analysis near g = 0.21-0.32. [b07, b09, d11]
- **Shared-element prediction** works for procedural skill (editors), with a clear asymmetry. [b12]
- **Noticing is the human bottleneck.** The 10% / 30% / 75% pattern recurs across radiation and cord problems and has a modern echo (business problems, though weaker). [a06, a07, c14]
- **Surface retrieval bias** is a stable finding (52% vs 7%; 82% choice). [a11, a12]
- **Comparison helps**: Gick and Holyoak (45% vs 21%) and MBA negotiation (40% vs 22%, N=310). Two labs and two domains. [a09, b16]
- **Far transfer from general training shrinks as controls improve**: music 0.25 to 0.03; WM large studies g=0.01; meta-meta far g about 0.01 after bias control. [b07, b09, d11]
- **LLMs lose accuracy as surface moves away**: Lewis and Mitchell, Wu et al., ARN, Stevenson et al. Four independent groups. [a20, a22, b17, b21]
- **Abstracted lessons beat raw traces for agents across classes**: three independent agent studies, small differences. [d01, d04, d05]
- **Raw-trace memory harms hard items**: -26.1 points on baseline-fail items. [d04]

### 5.2 Failures, contested results and moderators

- **Abstract vs concrete training** (contested). Original 76% vs 44%; the 2020 replication (38 per condition) found no abstract transfer advantage and a concrete advantage in learning. The 2011 replication split by target domain: abstract better for abstract targets, concrete better for concrete. The 2020 paper itself cites 76% / 75% / 79% for abstract-training transfer across studies, so cells are not all comparable. [b14, b15]
- **Principle and diagram add-ons** failed on single stories (Exp 2, 3) but worked after comparison (Exp 5, 6). Moderator: whether two cases are present. One lab only. [b03, b04, b06]
- **Modern hint lift is weaker**: factory 8.7% hinted (not 75%). The 1983 rates are not universal; the specific problem pair matters, and the added matching step makes it harder. [c14]
- **Webb et al. vs Lewis and Mitchell**: GPT-3 beats students on original forms; the same models fall below humans on altered forms. Task familiarity and training-data overlap are the likely moderators. Not settled. [a18, a20, a21]
- **Hodel and West** (rebuttal, second-hand): GPT-3 falls on shuffled-alphabet variants. [a21, c12]
- **Math SFT transfer**: Huan et al. say it mostly fails; Ren et al. say verified long-CoT works on strong base models and low-quality data hurts (LCB 37.5 to 20.4). Moderators: data quality and model strength. Not our scope (no training). [b24, c27]
- **Near-transfer size** differs by meta-analysis: 0.80 vs treated controls (Melby-Lervag) vs 0.44-0.46 (Sala and Gobet) vs 0.21-0.32 (Sala 2019). Different study pools. [b07, b09, d11]
- **AWM gains by distance** are not monotonic in full-task success: step success +8.9 / +3.6 / +14.0, but task success 0.7-4.8% in all buckets. [d08]
- **Stronger models gain less from stored experience**: +15.3 vs +6.9. [d05]

### 5.3 Interventions

| Worked | Did not work or backfired |
|---|---|
| Hint to use the source (humans 30% to 75-80%; GPT-4 1/15 to 15/15) [a06, c15] | Diagram or principle on a single story [b03, b04] |
| Compare two cases and write what they share [a09, b16] | Assumption that abstract training always wins [b14] |
| Principle or diagram after two cases are present [b06] | Raw trajectory memory on a related, harder task (-9.5; -26.1 on fail items) [d04] |
| Insight or skill memory over raw trace [d01, d05] | LLM reranking or rewriting of retrieved memories [d02] |
| Reconstruct memory against the current state (MemHarness 85.9 vs 82.4 unadapted) [d06] | Unadapted memory under layout shift (82.4 vs 83.0 no memory) [d06] |
| Selective add and history-based delete of memories (about 10% gain, authors' figure) [d07] | Naive growth of the store [d07] |
| Analogical prompting on mid/large models (+1-2 points GPT-3.5, +10.7 davinci-003) [a23] | Analogical prompting on weak models (curie 2%) [a25] |
| Demonstrations on far ARN items (+~10 for GPT-3.5, Llama-2) [b18] | Same demonstrations on near items (accuracy lost) [b18] |

## 6. Language models

### 6.1 Analogy and transfer behaviour

- **Original-form tasks: strong.** GPT-3 (text-davinci-003) beat UCLA undergraduates on digit matrices (OR 1.88, N=40) and letter strings (OR 1.76, N=57). On story analogies humans won (OR 0.37, N=54). [a18]
- **Altered forms: weak.** Letter strings in permuted or symbol alphabets: humans 0.753 overall; GPT models 0.35-0.49. Humans did not fall with more permuted letters; model accuracy fell, with a second sharp drop for symbols. GPT-4 passed comprehension checks (0.93-1.00), so the failure is not misunderstanding the alphabet. [a20, d13]
- **Children, adults and 2024 models** (Latin/Greek/symbol). Adults flat at 0.88-0.91; children flat at 0.62-0.67; every LLM dropped (alphabet effect F=29.5 to 135, all p<.001). GPT-4o 0.85 to 0.48; Llama-3.1 405B 0.79 to 0.27. Prompt template alone moved means from 0.52 to 0.74. Rule novelty drives part of it: item 5 (predecessor rule) GPT-4o 0.39, Claude-3.5 0.20, children 0.38, adults 0.81. [b21, c10, c11]
- **Counterfactual tasks.** 11 families; above chance but well below default; default and counterfactual accuracy correlate (memorisation-like). [a22, c06]
- **Story analogy (ARN).** Near: models 75.0 vs humans 97.9. Far: 39.6 vs 94.1. Hardest cell, far analogy vs near distractor: 33.9 vs 91.4 (GPT-4 29.1). SBERT alone gets 77.9 on near and 1.0 on the hardest cell. So much of "near analogy" success is surface match. [b17, c07, c08, d09]
- **Story mapping (given the pair).** Human 0.847; GPT-4o 0.823; Llama-3.1-70B 0.854; GPT-4o-mini 0.701. But GPT-4 86% on originals fell to 72% on paraphrases (humans 78% to 70%). [d14]
- **Raven-like symbolic tasks.** Reasoning models degrade less with longer relations (arithmetic accuracy 80.5% to 63.0% vs 59.3% to 4.4% for plain LLMs) but lose 61.8% task accuracy under perceptual uncertainty. [d15]
- **Reasoning models on ConceptARC (2026).** o3 77.1, Gemini 2.5 Pro 66.0, Claude Sonnet 4 60.2 vs humans 73.0 on text. About 27% of o3's correct answers rest on unintended rules (humans about 7%). Accuracy alone overstates abstraction. No reasoning-model result on ARN-style far narrative analogies was found. [d10]
- **Noticing with a context-window analogue.** GPT-3 solved the radiation problem when the story was present; with two distractor stories it lost the solution until told to consider earlier stories. GPT-4 used the radiation analogue for the factory problem in 1 of 15 unhinted runs and 15 of 15 hinted; it used the Dolphin source unhinted 14 of 15. Recall near 1.0, precision about 0.5; its errors came from surface similarity. [a19, c15, c16]
- **Content effects.** LMs, like people, reason better when meaning supports the logical answer (NLI, syllogisms, Wason). Content leaks into abstract reasoning. Accuracies not extracted. [a26]
- **Why the Webb-vs-Lewis split matters.** Differences in model version, prompt, original vs altered form and human sample (Lewis's humans scored higher) explain much. Training-data exposure is argued, not shown. [a21, a28, c05]

### 6.2 What changed performance, and by how much

| Change | Effect | Source |
|---|---|---|
| Hint or cue naming the source | GPT-4 1/15 to 15/15 (factory problem) | [c15] |
| Solved demonstrations (ARN) | ~+10 on far for GPT-3.5, Llama-2; loses near; GPT-4 stable | [b18] |
| Self-generated analogues (analogical prompting) | +1.0-2.0 GSM8K GPT-3.5; +10.7 davinci-003; MATH +3.4; average ~+4 | [a23, b22] |
| Model scale | Self-generation: curie 2%, davinci-002 48%, davinci-003 61% | [a25] |
| Prompt template (letter strings) | Total mean 0.52 to 0.74 | [b21] |
| Stronger backbone | Memory lift smaller (+15.3 vs +6.9) | [d05] |
| Reasoning models | Degrade less on long relations; match humans on ConceptARC accuracy but with unintended rules | [d10, d15] |

### 6.3 Agent memory, the applied form of transfer

| System | What is stored | Result | Caveat |
|---|---|---|---|
| ExpeL | Natural-language insights from past tasks | ALFWorld ReAct 40.0, Reflexion 54.4, ExpeL 59.0. HotpotQA to FEVER: ReAct 58 (63 in a second table), ExpeL transfer 65 | Source and target both QA; text and tables disagree slightly [b23, c21] |
| Voyager | Executable skill library | New world: all four tasks 3/3 with library, 18-21 iterations vs 26-36 without; baselines solved none in 50 iterations | Minecraft only; 3 trials [c23] |
| Buffer of Thoughts | High-level thought templates | GPT-4 Game of 24 3.0 standard, 74.0 ToT, 82.4 BoT; Checkmate-in-One 36.4 to 86.4; ~12% of multi-query cost | Buffer built on same task families; probably near transfer [c24] |
| AWM | Workflows with slots | WebArena +51.1% relative (12.0 absolute); Mind2Web step SR +8.9 / +3.6 / +14.0 by distance | Task SR 0.7-4.8% [c19, d08] |
| ReasoningBank | Strategies from successes and failures | WebArena +8.3, +7.2, +4.6; SWE-Bench-Verified flash 34.2 to 38.8, pro 54.0 to 57.4 | Authors' benchmarks [c25] |
| MTL (Memory Transfer Learning) | Memories from other coding benchmarks | GPT-5-mini Pass@3 average +3.7 (insight); DeepSeek V3.2 +2.6; Qwen3-Coder +1.8 (up to +8.3 MLGym, 0.0 Aider-Polyglot). Cross-domain pool of 431 beat in-domain ReasoningBank (97 memories) and AgentKB (5,899): 0.630 vs 0.601 / 0.613 (zero-shot 0.584) | Not token matched; Pass@3; small n [d01, d02, d16] |
| LifeMem | Environment-invariant skills | GPT-4o-mini: FEVER ReAct 0.40 to 0.49 (+22.5%); airline 0.32 to 0.38 (+18.8%) | Authors' method; mid-tier backbones [d05] |

Pattern across all: gains of a few points on mid-tier models; abstraction beats raw traces; none is token-matched; none separates cross-class transfer from near-duplicate reuse (except MTL and the AWM re-bucketing). Negative transfer is real on hard items (-26.1) and small on solved ones (at most -2). Agents copy the most similar stored case, so wrong stored cases propagate (error propagation, misaligned replay). [d04, d07]

### 6.4 Training-time transfer (out of scope)

Math SFT transfer to other tasks is contested (section 5.2). Included only as a warning that transfer depends on data quality and model strength. [b24, c27, c28]

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = the lesson store written at S9.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Reuse lessons inside the problem class first. Near transfer is the safe bet; do not expect lessons to help across unrelated classes. | memory / S0 | [E] | K01, K10; a14, b07, b09, d11 |
| A2 | Tag every stored lesson with its class and its sub-operation signature (shared elements). Rank reuse by overlap of signatures, not by topic label. | S9 / memory | [E] | K01; a01, a15, b12 |
| A3 | Do not rely on spontaneous noticing. Where far analogues are wanted (impasse, open mode), code fires an explicit "check the stored lessons" cue. Not on routine problems. | O7 / S6 | [E] for the human bottleneck; the cue effect in LLMs is [S] (U-list) | K02, K04; a06, b01, b04 |
| A4 | Retrieve in two stages in code: cheap class/surface match to a few survivors, then a structural check. Surface similarity alone is not enough, because humans and models both retrieve by surface and surface-similar wrong cases wreck accuracy (33.9% vs 91.4% on ARN). | O7 / memory | [E] on the mechanism; the code-checked second stage for LLMs is untested | K05, K14; a11, c08, d07 |
| A5 | Store lessons as abstracted insights (principle line plus precondition), not raw trajectories. Raw traces can cost up to -26.1 points on items the plain agent fails. | S9 / memory | [E] on direction; effect small, not token-matched | K25, K27; d03, d04, d05 |
| A6 | Require a stated precondition check before applying any stored lesson, and log lesson-on vs lesson-off outcomes. | O7 / G2 / G3 | [E] | K27; d04, d06, d07 |
| A7 | Report lesson reuse by distance bucket (same class, sibling class, other domain), never one pooled rate. | S0 / bench | [E] as method (AWM step vs task success diverged; one far effect size misleads) | K23, K19; d08 |
| A8 | Treat analogy claims as accuracy plus mapping. When the agent claims an analogy, require the mapping to be stated and checked, not only the answer. | O7 / G10 | [E] for G10; the 27% figure is [S] | K29; d10, c16 |
| A9 | Keep far analogues for impasses and open mode only (already in SCHEMA O7). The evidence confirms it: far transfer is rare without a cue and unaided models fall below chance on far narrative analogies. | O7 | [E] | K11; b17, d09 |
| A10 | Cap the lesson store: selective addition and deletion by outcome, not unlimited growth. | memory | [S] (about 10%, authors' figure) | d07 |

Note: A10 is listed here as a low-risk hygiene rule; it stays [S] and should be confirmed by test E1 before it is treated as established.

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Compare-two-cases lesson distillation: a lesson written from two solved instances vs one. | O7 / S9 | Human [E]; LLM: no test found | K06; a09, b16 |
| T2 | Abstract principle line vs full worked lesson, at equal tokens. | S9 | [C] | K08, K07; b14, b15, b06 |
| T3 | Code-checked typed mapping vs model-judged matching for lesson reuse. | O7 | [S] | K16, K28; a24, d02 |
| T4 | Slot abstraction (placeholders) vs literal values, by distance. | S9 / O7 | [S] | K19; c20, d08 |
| T5 | Cross-class lesson store vs no store, token-matched, for a current frontier model. | memory | [S] | K26, K30; d01, d05 |
| T6 | Explicit cue ("consider the stored lessons") vs no cue at impasses. | S6 / O7 | [S] | K20; c15, c02 |
| T7 | Self-generated analogues vs plain short reasoning, token-matched. | O7 | [S] | K15; a23 |
| T8 | Distance gate for demonstrations. | S0 | [S] | K17; b18 |
| T9 | False-match cost: distractor lesson with matching surface and wrong structure. | O7 / G2 | [E] mechanism; size for our agent unknown | K14, K27 |
| T10 | Re-skin robustness: does lesson gain survive a surface mutation? | G3 / O7 | [C] | K12, K13; a20, b21 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (lesson text, retrieval and mapping tokens are counted in the lesson arm; the plain arm gets the same budget as extra independent attempts). Report by distance bucket. At least 3 seeds. Primary metric is pass rate on held-out items from the target class. "Class" means a bench problem class (for example an ARC rule family or a puzzle type).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| E1 Held-out-class lessons (T5) | Lessons written from solved items of classes A-C; targets from class D (sibling) and class E (other domain) | (a) no lessons, extra attempts; (b) insight lessons from A-C retrieved by embedding | Pass rate on D and E, 95% CI over items | +0 to +4 points sibling, about 0 far (MTL +3.7 on mid-tier; LifeMem shows less for stronger backbones) |
| E2 Raw trace vs insight (A5) | Same A-C to D split | (a) raw worked trace; (b) principle line + precondition | Pass rate overall and on items the plain arm failed | Insight above raw by 1-6 points; raw negative on plain-fail items |
| E3 Compare-two-cases (T1) | Pairs of solved items from one class; test on a third member | (a) lesson from one instance; (b) lesson from two instances plus "what do they share" step | Pass rate on third member | Human effect +19-24 points unaided; for an LLM expect +0 to +5 |
| E4 Principle vs worked (T2) | Same class, near and far members | (a) principle line only; (b) worked example only; (c) both | Pass rate; tokens per success | No assumed winner. Concrete may win near, principle far. |
| E5 Typed mapping gate (T3) | Targets with a distractor lesson (surface match, wrong structure) and a true lesson (different surface) | (a) embedding top-1; (b) LLM judge chooses; (c) embedding top-3 then code check of slots, types and precondition | Reuse precision, reuse recall, pass rate, tokens per accepted match | (c) precision above 0.8 vs about 0.5 for (b); small pass-rate gain only if distractors are common |
| E6 Cue at impasse (T6) | Impasse-state problems only (S6 fired) | (a) no cue; (b) code cue listing top-3 lessons' principle lines | Fraction of impasses resolved | Positive if library lessons are relevant; zero if not |
| E7 Slot abstraction (T4) | Lessons with literal values vs placeholders; targets by distance bucket | Same lessons, two forms | Pass rate per bucket | Gap grows with distance (AWM step +3.6 to +14.0); check task level |
| E8 Re-skin (T10) | Each target in original and surface-mutated form (renamed entities, new symbol set, reordered fields) | Lesson on vs off | Lesson gain on original minus lesson gain on re-skin | If the gain falls by more than half on re-skins, lessons cue on surface |
| E9 Distance gate for examples (T8) | Near vs far targets | (a) always show solved example; (b) show only when distance estimate is high | Pass rate by bucket | ARN: examples help far, hurt near, for weaker models; GPT-4-class near flat |
| E10 Self-generated analogue (T7) | Class where plain pass rate is 30-70% | (a) plain short reasoning; (b) "recall 2 relevant solved problems then solve" | Pass rate at equal tokens | +0 to +2 for strong models (GSM8K GPT-3.5 +2.0) |
| E11 Negative transfer (T9) | Items the plain arm solved vs failed | Lesson store on/off | Lesson-induced loss on solved items; gain on failed items | Loss at most 2 points on solved items (Hu et al.); larger on failed items without a precondition check |

## 9. What does not transfer, and why

- **General cognitive training to unrelated skills.** Far g about 0.01 after placebo and bias control; true variance zero. For the agent: do not expect a generic "reflection" warm-up or general lessons to help across classes. [d11, b07]
- **Skills with few shared rules.** Calculus sub-skills (word-problem translation, operator choice) did not transfer to each other. Typing alone gave only slight transfer to editors. [b12, a14]
- **Surface-identical, structure-different items.** Same words, different procedure (ALFWorld "put X in Y" vs "put a clean X in Y"): raw memory hurt (-9.5; -26.1 on fail items). [d04, d17]
- **A single story's lesson, uncued, to a far problem.** About 30% even after memorising the story. [a06]
- **Single story plus a principle sentence or diagram.** No added noticing. [b03, b04]
- **Rules learned on altered symbols.** Models did not carry rules across alphabets; humans did. [a20, b21]
- **Raw, unadapted memory under distribution shift.** 82.4 vs 83.0 without memory; adapted memory 85.9. [d06]
- **Self-generated analogues from weak models.** Invalid exemplars (curie 2%). [a25]
- **Math SFT, mostly.** Non-reasoning average 45.7 to 21.1 under SFT-think. Depends on data quality. [b24, c27]

Why, in three lines: (1) retrieval is driven by surface cues, so the right case is not found; (2) mapping needs structure and models align it poorly; (3) a schema needs two or more cases, and one case gives only a concrete memory.

## 10. Open questions

1. How much does a lesson written for one class lift accuracy on a different class at equal tokens, for a current frontier model? No study isolates this from near-duplicate retrieval.
2. Does a code-checked typed mapping raise the precision of lesson reuse above model-judged matching, and at what token cost?
3. Do reasoning models (o-series, Claude 4+, Gemini 2.5+) still fall below chance on far narrative analogies (ARN), or did test-time compute close the gap?
4. Is lesson abstraction (slots, principle line) better than concrete worked lessons for LLM agents at equal tokens? Human evidence is contested.
5. Does comparing two solved cases raise LLM transfer as it does for people? No LLM test found.
6. How large is negative transfer from surface-based retrieval on tasks the plain model would have solved? The "at most -2" figure comes from one study.
7. Are agent-memory gains from cross-class transfer or same-template reuse? Only AWM and MTL were re-bucketed.
8. What does the full Barnett and Ceci nine-dimension table imply for where the cheapest reliable agent gains sit? Paper not opened.
9. Lewis and Mitchell table row order and model confidence intervals remain unresolved. [d13]
10. Can "identical elements" be defined for LLM lessons in a way that predicts transfer? The theory is unfalsifiable until elements are defined. [a02]
11. Does the GPT-3 radiation-problem recovery after a cue (single qualitative runs) hold as a rate in current models?

## 11. Sources

[V] = opened and read in this subfield's research. [M] = snippet, abstract only, or second-hand.

- Thorndike and Woodworth (1901). https://psychclassics.yorku.ca/Thorndike/Transfer/transfer1.htm [V]
- Perkins and Salomon (1992), via the Wikipedia summary. https://en.wikipedia.org/wiki/Transfer_of_learning [M for Perkins and Salomon; the page itself V]
- Gick and Holyoak (1983). https://gwern.net/doc/psychology/1983-gick.pdf [V]; DOI https://doi.org/10.1016/0010-0285(83)90002-6 (Exp 2 re-check not reopened) [M]
- Gentner, Rattermann and Forbus (1993). https://groups.psych.northwestern.edu/gentner/papers/GentnerRattForbus93.pdf [V]
- Forbus, Gentner and Law (1995), MAC/FAC. https://www.qrg.northwestern.edu/papers/Files/macfac91(searchable).pdf [M]
- Singley and Anderson (1985). https://www.gwern.net/doc/psychology/1985-singley.pdf [V]
- Singley and Anderson (1989). https://www.gwern.net/doc/psychology/1989-singley-thetransferofcognitiveskill.pdf [V]
- Barnett and Ceci (2002). https://pubmed.ncbi.nlm.nih.gov/12081085/ [M abstract only]; https://doi.org/10.1037/0033-2909.128.4.612 [M]
- Detterman (1993). https://apps.dtic.mil/sti/tr/pdf/ADA286008.pdf [M]
- Loewenstein, Thompson and Gentner (2003). https://business.illinois.edu/loewenstein/papers/Loewensteinetal%20AMLE03.pdf [V]
- Trninic, Kapur and Sinha (2020). https://edrl.berkeley.edu/wp-content/uploads/2020/08/Trninic-2020-CogSci.pdf [V]
- De Bock et al. (2011). https://repository.uantwerpen.be/link/irua/87703 [M, via Trninic]
- Melby-Lervag, Redick and Hulme (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4968033 [V]
- Sala and Gobet (2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC5724589 [V]
- Sala et al. (2019). https://doi.org/10.1525/collabra.203 [V, full text in the gap search]
- Webb, Holyoak and Lu (2023). https://arxiv.org/abs/2212.09196 [V]
- Hodel and West (2023/24). https://arxiv.org/abs/2308.16118 [M]
- Lewis and Mitchell (2024). https://arxiv.org/abs/2402.08955 [V]; https://arxiv.org/abs/2411.14215 [V]
- Wu et al. (2024), Reasoning or reciting. https://arxiv.org/abs/2307.02477 [V]
- Stevenson, Pafford, van der Maas and Mitchell (2025). https://arxiv.org/abs/2411.02348 [V]
- Sourati, Ilievski, Sommerauer and Jiang (2024), ARN. https://arxiv.org/abs/2310.00996 [V]
- Yasunaga et al. (2024), analogical prompting. https://arxiv.org/abs/2310.01714 [V]
- Lampinen et al. (2024), content effects. https://arxiv.org/abs/2207.07051 [V, numbers not extracted]
- Strategic-decisions analogy paper, humans vs GPT-4 (2025). https://arxiv.org/abs/2505.00603 [V]
- Inani et al. (2025), story analogies. https://arxiv.org/abs/2507.10957 [V]
- Camposampiero et al. (2025), I-RAVEN-X. https://arxiv.org/abs/2510.17496 [V, abstract and introduction]
- Beger et al. (2026), performance vs competence. https://arxiv.org/abs/2510.02125 [V]
- Zhao et al. (2024), ExpeL. https://arxiv.org/abs/2308.10144 [V]
- Wang et al. (2023), Voyager. https://arxiv.org/abs/2305.16291 [V]
- Yang et al. (2024), Buffer of Thoughts. https://arxiv.org/abs/2406.04271 [V]
- Wang, Mao, Fried, Neubig (2024), Agent Workflow Memory. https://arxiv.org/abs/2409.07429 [V]
- Ouyang et al. (2026), ReasoningBank. https://arxiv.org/abs/2509.25140 [V]
- Kim et al. (2026), Memory Transfer Learning. https://arxiv.org/abs/2604.14004 [V]
- Hu, Long, Wang (2026), experience reuse. https://arxiv.org/abs/2604.27003 [V]
- Qiu et al. (2026), LifeMem. https://arxiv.org/abs/2609.12655 [V]
- Wu et al. (2026), MemHarness. https://arxiv.org/abs/2607.28272 [V]
- Xiong et al. (2025), memory management in agents. https://arxiv.org/abs/2505.16067 [V]
- Huan et al. (2025), math reasoning transfer. https://arxiv.org/abs/2507.00432 [V]
- Ren et al. (2026), reasoning SFT generalisation. https://arxiv.org/abs/2604.06628 [V]

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 12 established claims: 9 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A05.05-K05** (now single-source: the sources are not independent). Numbers verified in Gentner et al. 1993 Exp 3 (SS 52%, object-attribute-only 17%, purely relational AN 7%; soundness AN 3.85 > SS 2.38 > OA 1.76) but a11/a12/a13 are one paper and one lab, and the ARN/LLM sources do not test human retrieval, so the claim rests on a single study.
- **A05.05-K11** (reworded: the sources support less). ARN figures verified (near 97.9 vs 75.0, far 94.1 vs 39.6) but they are averages over 11 systems incl. SBERT and old UnifiedQA/FlanT5/Llama-2, 'halfway between random and human' is not 'fine' on near, and GPT-4 scored 57.1 on (far,far) and 29.1 only on (far,near); the 39.6% mixes both far partitions; 2024 LLM letter-string study shows steep drop on unfamiliar alphabets but not chance. Corrected claim: On ARN narrative analogies (Sourati et al. 2024), the average over eleven tested models, mostly 2020-2023 systems, was 75.0% on near analogies (humans 97.9%) and 39.6% on far ones (humans 94.1%, chance 50%); GPT-4 was near humans on near analogies (about 93%) but 57.1% on far analogies against far distractors and 29.1% against near distractors. A separate letter-string study (Stevenson et al. 2025) shows four LLMs losing accuracy as the alphabet becomes less familiar while adults and children do not.
- **A05.05-K25** (reworded: the sources support less). Numbers verified (MTL insight +3.7 vs trajectory +1.1 over zero-shot 0.523; Hu ALFWorld A to B raw -9.5 vs insight +6.5; LifeMem airline Synapse 0.26 vs ReAct 0.32), but in the same LifeMem table the insight-based baseline ExpeL also fell below no-memory (airline 0.26 vs 0.32; FEVER with DeepSeek 0.32 vs 0.39), and in Hu's reverse direction raw and insight were similar (+7.0 vs +7.5), so 'abstracted lessons transfer more safely' is not uniform. Corrected claim: In LLM-agent memory studies, abstracted insights and skills usually transferred better than raw trajectories (Memory Transfer Learning, GPT-5-mini: insight +3.7 vs trajectory +1.1 average points over zero-shot; ALFWorld A to B: raw -9.5 vs insight +6.5 points; LifeMem on tau-bench airline: the trajectory-memory baseline Synapse 0.26 vs 0.32 without memory), but not uniformly: LifeMem's insight-based ExpeL baseline also fell below the no-memory agent on airline (0.26) and on FEVER with DeepSeek (0.32 vs 0.39), and raw and insight memory gained alike in the reverse ALFWorld direction. Differences are small and not token-matched.
- **A05.05-K02** (now single-source: only one opened source, code check).
