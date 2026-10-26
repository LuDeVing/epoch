# Intrinsic load and element interactivity: deep document

*Subfield A08.01 of cognitive load theory (CLT). Built from evidence_a-d.jsonl (a01-a33, b01-b25, c01-c25, d01-d20), claims.jsonl (A08.01-K01 to K28) and critique.md in this folder. Ids like a11 are evidence lines; K08 means claim A08.01-K08. Marks: [V] page or PDF text opened, [M] snippet or abstract only. Status: [E] established, [S] single-source, [C] contested.*

*Honest summary up front: the human theory is old, well cited and thinly tested. The LLM side has many papers that show "harder means worse", but almost none that measure element interactivity itself, and none that test a count-then-split gate at equal tokens. The schema should take a few cheap guardrails now and test the rest.*

---

## 1. What it is

**Intrinsic cognitive load** is the mental effort a task needs because of the task itself. In CLT it is set by **element interactivity**: how many elements must be held and related to each other at the same time to make sense of the material. (a01)

Three points define it.

1. **An element is anything the learner treats as one unit.** A letter, a word, a symbol, a formula or a whole schema can each be one element. What counts as one depends on what the person already knows. (a02)
2. **Interacting elements must be processed together.** Non-interacting elements can be learned one at a time, in any order. (a01)
3. **Size is not difficulty.** A long vocabulary list is big but low in interactivity. A single algebra step can be small but high. (a02, a03)

Worked counts from Sweller (1994) [V]:

- Multiplying out a denominator, a/b = c to a = cb, has about 5 interacting elements for a novice. (a02)
- A foreign-language noun pair has a count of 1. (a02)
- For an expert with an automated algebra schema, the algebra step is 1 element. For a learner missing the first schema it is 6 or more. So the count is **learner-dependent**. Sweller says a learner-free measure cannot be obtained. (a02)

**Total load = intrinsic + extraneous** (plus germane, redefined by Sweller in 2010 as working memory spent on the intrinsic load). (a01, a16)
- Intrinsic: from the content and the learner's knowledge.
- Extraneous: from how the material is presented (split attention, redundancy, missing worked examples).
- The claim that matters most for design: extraneous-load effects should matter only when intrinsic load is high, because with low intrinsic load the total stays under capacity. (a04)

**Why it matters for our agent.** The schema has an S0 gate (choose the mode) and an operator O3 (decompose into 2 to 4 sub-problems). Element interactivity says when to split: when a step relates more things at once than the solver can bind, and the split should leave each part with few interacting elements. The LLM literature gives evidence that accuracy falls with binding load, and that some splits help. It does not yet tell us how to count, where the threshold is, or whether a pre-solve load estimate beats cheaper gates.

**Two related formal ideas.**
- **Relational complexity (RC)** from Halford, Wilson and Phillips (1998): complexity is the number of variables related in parallel in one step. Soft human limit near four. This is the version two recent LLM papers (CogniLoad, REL) actually cite. (a17, a33)
- **Dependency load** for tool agents: a weighted sum over dependency edges of a task graph. (a26)

These three (Sweller's count, Halford's arity, graph load) agree on direction. They are not one measurable quantity. (critique.md)

---

## 2. History and theories in depth

### 2.1 Founding: Sweller (1988 to 1994)
CLT grew out of problem-solving work in the 1980s. It said working memory is small and that instruction should not waste it. The 1994 paper (Sweller, "Cognitive load theory, learning difficulty, and instructional design") [V] is the key source for intrinsic load. (a01 to a05)

What the 1994 paper does:
- Defines intrinsic load by element interactivity. (a01)
- Gives a counting method with worked examples (algebra step 5, vocabulary 1). (a02)
- Names paired-associate and vocabulary learning as the low-interactivity extreme. Hard because of volume, not interactivity. Sweller admits vocabulary stops being low once it has to be used in syntax. (a03)
- States the prediction: split attention, redundancy and missing worked examples hurt only with high interactivity. Stated as a hypothesis, with "initial data" cited. (a04)
- Separates "understanding" from "learning": failing to hold interacting elements together is a failure of understanding; losing one isolated element is forgetting. This is philosophical, with no test. (a05)
- Calls intrinsic load fixed for a given area and learner. This is contested (section 2.4).

It has **no experiment**. The data come from Sweller and Chandler (1994) and Chandler and Sweller (1996), which we only know through summaries. (a07, a08 [M])

### 2.2 The empirical pair: split attention and redundancy by interactivity
- Sweller and Chandler (1994): four experiments on learning computer equipment and procedures, with and without redesign to remove split attention. Redesign helped for high-interactivity material and not for low. Numbers not obtained. (a07 [M])
- Chandler and Sweller (1996): same pattern for split attention and redundancy. (a08 [M])
- Sweller's own later review names this the "element interactivity effect" and lists a few more studies (Tindall-Ford 1997 modality, Marcus 1996 diagrams vs text). It is a review by the original author, not independent. (a09 [V])
- Cooper, Tindall-Ford, Chandler, Sweller (2001): "imagine the procedure" beat "study it" only for learners with enough knowledge to hold all the elements. For complete novices it reversed. (a10 [M])

### 2.3 Formal models behind the idea
- Halford, Wilson, Phillips (1998), Behavioral and Brain Sciences [V]. Relational complexity is the number of arguments of a relation processed in parallel. Unary, binary, ternary, quaternary. Adults have a soft limit near one quaternary relation (example: proportion a/b = c/d). A small neural-net model fits: about five units active, so one quaternary relation fits (symbol plus four arguments). Children reach ternary relations by a median age near 5 years. Many commentators disputed the exact limit. (a17, b18)
- Halford's two ways past the limit. **Segmentation** splits the task into parts processed in series. **Conceptual chunking** collapses a structure into fewer dimensions but loses access to inner relations. Segmentation works only if the parts really can be processed serially. Transitive inference cannot be cut into binary parts without loss. (a18)
- Task complexity is the complexity of the *most complex step*, not the number of steps, and it depends on strategy: measure it with the least demanding strategy available. (a17)
- Premise-integration evidence (Maybery, Bain, Halford 1986): in transitive inference with segmented presentation, the probe reaction time peaked when the second premise had to be integrated with the first (a ternary step), not when premises were read. Models that counted negations did not predict this. We know it only second-hand. (a06 [M], a19)

### 2.4 Critique and revision
- **de Jong (2010)** [V] is the main critique. (a20, a21, a22, b13, b14)
  - Count is not the whole of difficulty. Tower of Hanoi variants with the same number of moves differ in difficulty (Klahr and Robinson 1981: all-pegs-occupied was harder). Changing ontological category is hard whatever the count (Chi 1992, 2005). Negative or ambiguous relations add difficulty.
  - "Intrinsic load cannot be changed" clashes with advice to sequence from simple to complex, part-whole training, or isolated-elements-first (Pollock et al. 2002). The CLT authors call both consistent. The effective load on the learner can change by splitting even if the content's interactivity does not.
  - Measurement: a one-item mental effort rating has no stable meaning. Pollock's best group rated load higher than Kablan and Erden's worst group. Post hoc labelling (germane if they did well, extraneous if badly) lets nearly any result fit, so the theory is hard to falsify.
- **Sweller (2010)** [M] ties germane load to intrinsic load and says element interactivity underlies extraneous load too. (a16)
- **Chen, Kalyuga, Sweller (2017)** [M] recasts the expertise reversal effect as the element interactivity effect seen through expertise. This re-describes more than it tests. (b22)
- **Chen, Paas, Sweller (2023)** [M] proposes defining task complexity by the count of interacting elements together with the person's long-term-memory knowledge. (b21)
- **Ayres et al. (2021)** [V]: interactivity is not the only cause of load. Recalling 12 numbers is harder than 5 with no interaction at all. (b17)

### 2.5 Measurement lines
- Subjective: Paas one-item scale (dominant), Leppink et al. (2013) 10-item scale (b16 [M]), Klepsch et al. (2017) (a23, b15 [V]). Klepsch: three-factor model fits far better than one factor (CFI 0.970 vs 0.612; RMSEA 0.021 vs 0.071). The germane scale is the weak one.
- Order bias: Krieglstein et al. (2025) [V], N=67 pre-study and N=100 main: the overall intrinsic rating follows the *first* unit seen (beta=0.70, 95% CI 0.60-0.80), not the hardest or last. (b19)
- Physiological: Ayres et al. (2021) review of 33 experiments; subjective ratings were most sensitive, eye measures led among physiological ones. (b17)
- Performance-based: item response modelling gives a "relative difficulty" index (Ehrich et al. 2021, N=91 Year 2 learners). (b24 [M])

### 2.6 The LLM turn (2023 to 2026)
Papers split into five groups by how they define "complexity". (critique.md)

| Group | What "load" means | Papers |
|---|---|---|
| Interacting entities and rules | entities, attributes, clauses per statement | CogniLoad (a24, b01), GSM-Symbolic (c12) |
| Relational arity | entities bound at once | REL (a32, c06) |
| Dependency graph | edge-weighted tool graph | ToolLoad-Bench (a26, b04) |
| Graph depth and width | computation graph | Faith and Fate (a30, b12) |
| Solution length | moves, steps | Illusion of Thinking (a29, b09), ZebraLogic (b11) |

Plus three "CLT-inspired method" papers: CLAI (a28, c10), CoThinker (a27, c23), and Cognitive Overload Attack (c11). They use CLT as design metaphor and rarely measure interactivity.

---

## 3. Core findings with exact numbers

Status legend: [E] two or more independent sources; [S] one source or one group; [C] contested. Evidence ids in the source column.

### 3.1 Human studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Intrinsic load is set by number of interacting elements, not amount of material | Algebra step 5 elements; vocabulary pair 1. No experiment in the paper | Sweller 1994 (a01, a02, a03) | [E] as concept (also Halford 1998 a17); counts are analyst-assigned |
| Relational complexity limit near four variables in parallel | Quaternary relation = one soft limit; children ternary by about age 5 | Halford et al. 1998 (a17, a18, b18) | [S] (one model school; disputed in commentaries) |
| Audio + diagram beats text + diagram on high-interactivity questions only (Exp 1) | N=48 Year 5 (24 per group). High: 34.26 vs 15.74 percent, t(46)=2.58, p=.014. Low: 73.33 vs 74.17, t(46)=0.124, p=.902. Group x interactivity F(1,46)=6.62, p=.013 | Leahy, Chandler, Sweller 2003 (a11) | [S] |
| Effect is a threshold, not a line | 8-element questions: A/V 8,9,8,9,10 vs visual-only 1,2,3,3,3 of 24. 7-element questions: 9 vs 7 and 8 vs 7, no difference. 1-element: 18 vs 19, 21 vs 23 | Leahy et al. 2003 (a12) | [S] |
| Redundant audio hurts more on high-interactivity items (Exp 2) | N=30 (15 per group). Group F(1,28)=9.18, p=.005; interaction F(1,28)=5.56, p=.026. High t(28)=3.03, p=.006; low t(28)=2.29, p=.030 (low also significant). Diagram-only studied 62.3 s vs 135 s audio. Counts (my calculation): high 74% vs 40%; low 94% vs 82% | Leahy et al. 2003 (a13) | [S] |
| Guidance helps on high-interactivity items, hurts on low (instructional guidance) | N=47 (22 high guidance, 25 low). Means low/high interactivity: high-guidance 71.4/90.9; low-guidance 80.9/85.6. Interaction F(1,45)=5.16, p=.028. Generation effect d=.57 (one-tailed p=.025); worked-example effect d=.46, p=.06 one-tailed, **not significant** | Chen, Kalyuga, Sweller 2016 (a14) | [S], weak |
| Split-attention, redundancy, modality effects shrink with low interactivity | Four to five studies from the Sweller school; no numbers retrieved | Sweller and Chandler 1994, Chandler and Sweller 1996, others (a07, a08, a09, a13, a14) | [C]: one school, small N, author-assigned counts |
| Second-hand pair for split attention by complexity | d=0.78 high vs d=0.28 low (p>.05); overall g=0.63 (worksheets 0.80, 2D pictures 0.71). The pair could not be traced to a table | Beege et al. 2019 quoting Ginns 2006, Schroeder and Cenkci 2018 (d01) | [C]; Beege's own experiments (N=98, N=85) used only high-complexity material and do not test the interaction |
| Imagining beats studying only with enough prior knowledge | Reversed for complete novices; no numbers retrieved | Cooper et al. 2001 (a10 [M]) | [S] |
| Expertise reversal meta-analysis | Reported d=0.505 (low prior knowledge) and -0.428 (high); about 60 studies, 176 effects, nearly 6,000 people. **Second-hand from a blog, not confirmed from the paper** | Tetzlaff et al. 2025 (b23, d02 [M]) | [S] unverified: do not cite numbers |
| Self-report load measures are weak | One-item rating has no stable meaning; first unit drives overall rating beta=0.70; three-factor questionnaire CFI 0.970 vs one-factor 0.612 | de Jong 2010 (a22, b14); Krieglstein 2025 (b19); Klepsch 2017 (b15) | [E] that single-item ratings are weak; the three-factor questionnaire is [S] |
| Interactivity is not the only source of difficulty | Same-move Hanoi variants differ; category change is hard regardless of count | de Jong 2010 (a20, b13) | [C] |

### 3.2 LLM studies: complexity dial and accuracy

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Accuracy falls with intrinsic difficulty d (entities, attributes, clauses) | 22 reasoning models. By d=5, 12 of 22 below 50%. d=1 to 3: gpt-5 1.00 to 0.97, o3 0.96 to 0.93, small models lose 0.10 to 0.25. d=10: gpt-5 0.82, o3 0.80, gpt-5-mini 0.675, gemini-2.5-pro 0.654, o4-mini 0.646, DS-R1-0528 0.475. Decline flattens beyond d about 7 | CogniLoad (a24, b01, c01, d20) | [S] |
| Per-model capacity point ID50 | DS-R1-0528 19.07; gpt-5-mini 14.78; gemini-2.5-pro 12.74; gpt-5-nano 11.72; DS-Llama-70B 10.86; gemini-2.5-flash 8.56; QwQ-32B 4.08; o4-mini 2.87; Qwen3-8B 1.0; Qwen3-32B -0.55; Phi-4-mini-reasoning -3.95. Extrapolated past d=10 | CogniLoad (b02, d20) | [S]; not a "k" |
| Task length N hurts more than d | N=20 to 50: DS-Llama-70B 0.89 to 0.66; Qwen3-8B 0.71 to 0.40. gpt-5 1.00 to 0.98. ECL50 above 300 statements only for gpt-5 and o3 | CogniLoad (a24, a25, c02) | [S] |
| Failure type under load is wrong state tracking; small models drift to non-answers at long N | N=250: DS-Qwen-1.5B 605 "other"; DS-Qwen-7B 461; Gemini-2.5-flash 280 context-limit errors of 350 | CogniLoad (a25, c03) | [S] |
| Accuracy falls with relational complexity at fixed entity count and input size | RPM/tensors: -45% from RC 3 to 9. Phylogeny REL-B1: -93% from RC 5 to 20. Chemistry completion -39.7% C1 to C3. RC 1-2 about 91% even at 30x30. RC explains 24% (Claude), 32% (Gemini), 44% (GPT) of explainable variance in REL-B1 | REL (a32, c06, c08) | [S] |
| More tokens, one-shot, best-of-N, vote do not remove the high-RC drop | 4K to 16K tokens: about 2-3% on REL-A, about 0.4% on REL-C. One-shot +6.6/+3.4/+6.0 (C1-C3), same order. Best-of-5 46.7 to 60.0% at 4 hosts but 0 to 6.7% at 25 (15 questions per level) | REL (c07) | [S] |
| Adding clauses lowers accuracy and raises variance | Gemma2-9b-it: M1 84.4; Symbolic 79.1; P1 68.1; P2 41.8 (SD 6.0). NoOp drops up to 65% (Phi-3-mini over 65%) | GSM-Symbolic (c12, c13) | [S] |
| Tool-use accuracy falls with dependency-graph load | 500 tasks, 106 tools. xLAM2-32B 78.8; GPT-4o 68.0; Claude 3.7 64.8; Gemini 2.5 Pro 60.0; Qwen3-8B 38.6; Llama3.3-70B 17. Fitted k: xLAM2 0.034, GPT-4o 0.067, Claude 0.073, Qwen3-8B 0.085. Hosmer-Lemeshow p all above .05 | ToolLoad-Bench (a26, b04, c04, c05) | [S] |
| Theory-of-mind difficulty tracks number of state events | Correlation across five benchmark means; no coefficient read. State-event splitting (DWM) helped hard sets, slightly hurt short SocialIQa | Huang et al. 2024 (b08) | [S] |
| Logic grid puzzles: sharp drop with search-space size | o1 81.0%; R1 78.7%; o1-preview 71.4%; o1-mini 59.7%; Sonnet-3.5 36.2%; Llama-3.1-405B 32.6%. o1-preview 17.0% on X-Large. Oracle best-of-128 GPT-4o 69.1% (upper bound) | ZebraLogic (b11) | [S] |
| Equivalence-class (variable tracking) tasks | Non-reasoning error by depth: 4.4% / 58% / 85%. DeepSeek-V3 error above 90% at n=144; Gemini-3-Flash about 22%. Ten queries on one graph raised errors | Zheng et al. 2026 (c19) | [S] |
| Compositional tasks fail by error propagation | GPT-3.5 55%, GPT-4 59% on 3x3-digit multiplication. 82.3% of correct 4x2-digit answers had a wrong node | Dziri et al. 2023 (a30, b12, c16) | [E] direction (matches c19, c09); numbers are 2023 models |
| Information-bandwidth measure predicts failure independent of length | High accuracy on low-bandwidth tasks across n; fast failure on high-bandwidth tasks at small n. Numbers in figures only | BAPO, Schnabel et al. 2026 (d09) | [S] |

### 3.3 LLM studies: collapse, context and scaffolds

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Three regimes: plain wins low, thinking wins medium, both collapse high | Hanoi collapse N=7-8 (255 moves at N=8); failure near move 40 (about 15%); River Crossing fails from N=3 while Hanoi N=5 (31 moves) is near perfect; 25 samples per cell. Temperature 0 R1 collapses at N=8; with sampling keeps 18.2% at N=8, collapses at N=9 | Illusion of Thinking (a29, b09, b25, c14) | [C] |
| Part of the collapse is output format and unsolvable instances | River Crossing N>=6 with boat 3 has no solution. About 10 tokens per move, solvable listing caps near N=12-13. Lua function for 15-disk Hanoi: "very high accuracy" in under 5,000 tokens (no table) | Lawsen 2025 (b10, c15, d06) | [C]; non-peer-reviewed |
| Chunked output still fails; collapse is partly format, partly state loss | Stepwise prompting beat one-shot, but fails near N=8 (Gemini, 10 trials per N). Standard Hanoi saturated: R1 24/25, Kimi-K2-Think 23/25, gpt-oss-120b 25/25. Flat-to-flat: Qwen3.6-27B optimal 4/33 at n=6, 2/33 at n=7. State steering lifts 33 to 59 of 81 (41 to 73%) | Dellibarda Varela 2025 (d05); Pereira and Zuidema 2026 (d07) | [S] |
| Irrelevant context costs more at higher step count | code-davinci-002 GSM-IC micro: CoT 73.5 (2-step) vs 70.8 (>2 steps); least-to-most 74.9 vs 81.5. Overall CoT 72.4, L2M 77.5. Macro CoT 6.0 vs L2M 18.0. text-davinci-003 macro 0 on >2-step role-overlap | Shi et al. 2023 (d04) | [S], 2023 models |
| Context length alone hurts even with perfect retrieval | Drop 13.9 to 85% across 5 models up to 30K tokens; still hurts with whitespace or masked filler. Recite-then-solve: Mistral-7B GSM8K at 26,250 tokens 35.5 to 66.7 (+31.2); GPT-4o up to +4 on RULER QA2 | Du et al. 2025 (d03) | [S] |
| Distractor curve is U-shaped in CogniLoad | gpt-5 0.97 / 0.89 / 0.91 and o3 0.93 / 0.89 / 0.88 across low/mid/high needle ratio. Widest at d=5 and N=20; flat by N=250. Five models have a non-significant ratio term | CogniLoad (b03, c03, d20) | [S]; no mechanism; possibly an effective-chain-length confound (my reading, untested) |
| Extra context on a hard multi-hop task | Llama-3-8B, Llama-3-70B, Mistral-7B all 0% on 2/3-hop even clean. Gemini-2.0-Flash 0.85 control, 0.82 at 20%, 0.78 at 50%, 0.72 at 80% irrelevant tokens (beta -0.003 per %, p<0.001). Long control 0.82 equals control (p=0.45) | Adapala 2025 (c09) | [S], independent author, 2024 models |
| Least-to-most beats CoT where the split is clean | SCAN length split code-davinci-002: standard 16.7; CoT 16.2; L2M 99.7. Last-letter length 12: CoT 31.8 vs L2M 74.0 (another model row: 38.4 vs 74.0); length 4: 84.2 vs 94.0 | Zhou et al. 2023 (a31, c17) | [E] (with Decomposed Prompting c18, and GSM-IC d04) |
| Splitting contexts helps beyond shortening the chain | Two independent coding problems in one context need up to 10-20x more generations than the product of the parts (Llama-3-8B); 5-10x for four problems (Llama-3-70B) | Wolf et al. 2025 (d08) | [S] |
| Load-aware prompt cut tokens about 35% at equal accuracy | Llama-3-70B GSM8K 92.5 at 485 tokens vs 92.3 at 310 (-36.1%); MATH 53.9 at 812 vs 53.5 at 525 (-35.3%; the CoT row was not re-read) | CLAI (a28, c10) | [S]; single author, no ablation of the load step |
| Multi-agent split of load: gains on reasoning, loss on instruction following | LiveBench Gemini-1.5-Pro: Math 60.9 vs 75.3; Data 40.7 vs 47.3; Reasoning 43.0 vs 44.7; Language 37.4 vs 52.6; Instruction-following 84.4 vs 81.8. Normalised average gain +0.04 to +0.24. Ablations mixed: GPT5-Nano math 55.97 full vs 62.36 without memory | CoThinker (a27, b06, c23, c24) | [S] |
| Failure-gated as-needed decomposition beats always- and never-plan | GPT-3.5. ALFWorld: ReAct 43.3; Plan-and-Execute 43.3; Reflexion 57.5; ADaPT 71.6. WebShop 32.0 / 17.0 / 44.0. TextCraft 19.0 / 27.0 / 52.0. TextCraft depth 3: 1.8 vs 38.7 | ADaPT (d10) | [S]; gate is failure, tokens not matched |
| CoT helps on symbolic and math tasks, almost nowhere else | +14.2 symbolic, +12.3 math, +6.9 logic. Top three 56.9 vs 45.5; all others 56.8 vs 56.1. Over 100 papers + 20 datasets + 14 models | Sprague et al. 2025 (d11) | [E] direction (with a29, d12) |
| Scaffolds can hurt | GPT-4o artificial grammar: direct 87.5 vs CoT 64.4 (-23.1); Claude 3 Opus -8.0; Gemini 1.5 Pro -6.05; Llama 3.1 70B -8.8. Face recognition GPT-4o 64.0 to 51.2. R1: few-shot reported to degrade (one sentence, no table) | Liu et al. 2024 (d12); DeepSeek-R1 report (d13) | [S] |
| Self-rated effort or ability predicts the model's own errors | 12 LLMs, 38 tasks. Best dimension beats confidence by 10.1 / 8.4 AUROC points on standard tasks and 6.7 / 8.9 on hard tasks. Subset AUROC 0.83 to 0.89 | Bhattacharyya et al. 2026 (d14) | [C] with d15 |
| Asking the model how hard an item is for humans aligns weakly | 20+ models. Spearman averages below 0.50 (SAT Math about 0.41; USMLE about 0.13; GPT-5 0.34 vs GPT-4.1 0.44). Self-error AUROC near 0.5 for most. Pairwise or IRT-based simulation does better (rho up to 0.75, 0.76, 0.82) | Li et al. 2026 (d15); Kolesnikova 2026 / Acquaye 2026 (d16) | [C] |
| Demonstration order by difficulty: large on one study, near zero on another | ICCL +9% F1 over random on instruction-tuned models (base models: none; one decline 7.16%). Step-count ordering on Llama3-8B +0.24 (70.79 vs 70.55) | Liu et al. 2024 (d17); Ma et al. 2025 (d18) | [C] |
| Working-memory capacity claims for LLMs | gpt-3.5 n-back capacity about 3 (d' about 1 at n=3). Re-run: poor scores partly reflect task misunderstanding | Gong et al. 2024 (c20); Hu and Lewis 2025 (c21) | [C] |

---

## 4. Mechanisms and models

This section is written so an engineer can build each piece.

### 4.1 Counting interacting elements (the human recipe)
Chen, Kalyuga, Sweller (2016) give a transparent recipe. (a15)
1. List the items the solver must hold *at one time* to take the next step.
2. Treat any familiar unit (a formula the solver already owns) as **one** element.
3. Add one element for each operation or recognition that must be coordinated with the others.
4. Count the number alive in the same step, not across the whole task.

Example: area of a rhombus plus trapezium figure. Recognise rhombus (1), recognise trapezium (2), total area (3), addition (4), the two areas (5, 6). Total about 6. Formula recall: 1.

Rules from the theory that an implementation must respect:
- The count is relative to a **solver**. For the agent it means "what is a single chunk for this model class". A step a strong model does by recall counts 1; the same step for a small model may count 5.
- The count is for the **hardest step**, not the sum over steps (Halford). (a17)
- Pick the least demanding strategy available (Halford). (a17)
- Raters assign counts by judgement. No study validated them with a second rater. (a15, K17)

### 4.2 Relational complexity (the arity version)
For a step that applies a relation R to variables x1...xn, RC = n. Examples (a17, c06):
- unary: a property. binary: a > b. ternary: a > b > c integration. quaternary: a/b = c/d.
- REL's operational definition: the minimum number of independent entities that must be bound at once. (c06)

Implementation: for each candidate step, list the variables that the step jointly depends on. If the list is longer than the solver's measured limit, split so each sub-step has fewer. Halford's two methods map to operators:
- **Segmentation** = O3 decompose into serial parts. Works only if parts really can be done in series.
- **Conceptual chunking** = write a compact rule or helper, then reason on the helper. Cost: lose access to inner relations.

### 4.3 Step-success models (how load becomes accuracy)
**Exponential success.** ToolLoad-Bench: per-step success is exp(-(k * load + b)), with k the model's sensitivity and b its baseline. Load = sum over dependency edges of (turns between producer and consumer) x (1 + lambda x same-type distractors). Fits held for 9 models; Hosmer-Lemeshow p from 0.11 to 0.77. (a26, b04, c05) Assumes independent steps. The distractor weight is a free parameter. A non-significant calibration test is not proof of a good model.

How to use: fit k and b per model on our own tasks. Then predicted success of an n-step chain with step loads L_i is the product of exp(-(k L_i + b)). Splitting is worth it when the product after splitting (with each part's lower load, plus the cost of passing results) beats the product before.

**Logistic capacity points.** CogniLoad fits a logistic regression in d, N and distractor ratio and reports ID50 and ECL50, the points where accuracy is 50% at mean values of the other knobs. (b02) Implementation: run a grid on d, fit, read off the d that gives 50%. Use it as a per-model-class threshold; do not read it as a count of items (it bundles entities and attributes). (d20)

**Error propagation.** In a computation graph, one wrong node makes the final answer wrong unless a later step is wrong in a compensating way. 82.3% of correct 4x2-digit answers had a wrong node (so right answers often hide wrong steps). Local per-node accuracy is high; composition is the problem. (a30, b12)

### 4.4 Why splitting helps (four candidate mechanisms)
Evidence does not yet separate these. (K24, critique gap 5)
1. **Lower arity per step** (Halford segmentation). Predicts gain only when the step's RC exceeds the model's limit. REL supports a binding limit that more tokens and voting do not fix. (c07)
2. **Shorter chains per context.** Less state to track; avoids the state loss seen in flat-to-flat Hanoi (d07) and in CogniLoad's wrong-state errors (a25).
3. **Separate contexts.** Wolf et al.: two independent problems in one context cost 10-20x more generations than separate runs, with no dependency between them. (d08)
4. **Easier verification per node.** Error propagation can be caught at each node. Not tested in the studies above.

### 4.5 Gating (the S0 logic in the literature)
- **Failure-gated** (ADaPT): try the task directly, split only on failure, recurse to depth limit. TextCraft 52.0 vs 19.0 and 27.0. Mean max depth used 1.9 at recipe depth 2, 2.8 at depth 3. So the split depth adapts to task depth. (d10)
- **Load-gated** (CLAI): the model rates load, then decides. The load step was never ablated. (a28)
- **Task-class gated** (Sprague): use CoT for symbolic, math and logic tasks; skip it for the rest. (d11)
- **Self-rating gated**: self-rated effort or ability predicts the model's own failure (AUROC up to 0.83 to 0.89), but asking for human difficulty does not. (d14, d15)

### 4.6 Two guard mechanisms for context
- **Distractor cost grows with step count** for CoT and stays flat for least-to-most (GSM-IC). (d04)
- **Recite then solve**: the model first copies the needed evidence, then solves from a short prompt. +31.2 points for Mistral-7B at 26K tokens. This turns a long-context task into a short one. (d03)

### 4.7 Sequencing and expertise (adaptive scaffolding)
- Humans: guidance helps novices, hurts experts, because the same material has fewer interacting elements for experts. (b22, a14, a10)
- Model-level cousins: CoT hurts where deliberation does not help (d12); R1 does worse with few-shot (d13); CoT gains concentrate in symbolic tasks (d11).
- Implementation idea: bin items by predicted load, measure scaffold-on vs scaffold-off accuracy per bin at equal tokens, and turn the scaffold off in bins where it does not pay.

---

## 5. What holds up

### 5.1 Human evidence
**Holds up (as concept):**
- Difficulty is about interactions among parts, not volume. Two independent lines agree: Sweller's count and Halford's arity. (K01, [E])
- Single-item self-report of load is a poor measure. Three sources agree. (K07, [E])

**Weak or contested:**
- **The interaction (extraneous-load aids help only at high interactivity)** is the core prediction and has the thinnest base. It rests on a handful of small studies from one research group, with counts assigned by the authors and no second rater. (K03, [C])
  - Leahy 2003 Exp 1: N=48, effect only on 8-element questions, not 7; 7-element questions showed no gap. So not smooth in the count. (a12)
  - Leahy 2003 Exp 2: N=30, the low-interactivity gap was also significant (t(28)=2.29, p=.030). The pattern is "larger on high", not "absent on low". (a13)
  - Chen 2016: N=47; the worked-example simple effect was not significant (p=.06 one-tailed); the interaction p=.028 is carried partly by a non-significant effect; one-tailed tests; same pupils took both phases 4 hours apart; the authors say it could be expertise reversal. (a14)
  - Beege 2019 chose only high-complexity material on purpose, so it cannot test the interaction. No preregistered independent test of the interaction was found. (d01)
- **Expertise reversal meta-analysis** (Tetzlaff 2025): the paper exists (Learning and Instruction 98:102142) but the effect sizes we hold came from a blog summary. Not usable until opened. (d02)
- **Fixed intrinsic load** is a terminology conflict: content interactivity may be fixed, but the effective load on the learner is changed by sequencing and splitting. (a21)
- **Theory falsifiability**: germane/extraneous labels can be fitted after the fact. (b14)

### 5.2 Moderators found
- Learner knowledge: the count depends on the learner (a02, a10).
- Presentation type: audio/visual, text, diagrams (a11, a13).
- Order of presentation: first unit drives the overall rating (b19).
- Content type: ontological category, relation type (a20).

### 5.3 LLM evidence that holds
- **Harder (more interacting parts) means worse, across many designs.** Direction agrees in CogniLoad, REL, GSM-Symbolic, ToolLoad, ZebraLogic, Faith and Fate, equivalence class. (K08 to K11, K16)
- **Compositional errors propagate.** (K16, [E])
- **Least-to-most helps when the split is clean.** (K14, [E])
- **CoT helps on symbolic tasks and not much elsewhere.** (d11, d12, a29: three sources)
- **High RC is not repaired by more tokens, one-shot, best-of-N or vote** (REL, one paper but several arms). (c07)

### 5.4 LLM evidence that fails, is disputed, or is confounded
- **Illusion of Thinking.** Part of the collapse is output length and unsolvable River Crossing instances (Lawsen). Stepwise output still fails near 8 disks, so it is not all artefact. Lawsen is a short comment, not peer reviewed, and the first version had a wrong token-limit argument. (b10, c15, d05, d06)
- **Solution length is confounded with interactivity.** A 255-move list is long and also needs state maintenance. Flat-to-flat Hanoi suggests state tracking is the real limit: standard Hanoi is saturated while flat-to-flat is not. (d07)
- **CogniLoad d is a bundle**, not a count. The U-shaped distractor curve contradicts CLT and may be a generator artefact. (a24, d20)
- **Working-memory capacity claims** (n-back) are partly task-understanding failures. (c20, c21)
- **CLAI**: single author, preprint, no seeds or intervals, no ablation of the load step, model-judged load (G5 and G10 warn against this). Treat as unverified. (a28)
- **CoThinker**: single group, small gains, instruction following got worse, ablations mixed, and the intrinsic load was never measured. (c23, c24)
- **Demonstration ordering**: +9% F1 in one study, +0.24 in another. (d17, d18)

### 5.5 Interventions that worked and that did not

| Intervention | Worked? | Evidence |
|---|---|---|
| Least-to-most decomposition (clean splits, hand-written demos) | Yes: SCAN 99.7 vs 16.2; letters 74.0 vs 31.8 | a31, c17 |
| Failure-gated recursive decomposition | Yes on 3 text environments (GPT-3.5, tokens unmatched) | d10 |
| Recite evidence, then solve from short prompt | Yes: up to +31.2 (Mistral-7B), +4 (GPT-4o) | d03 |
| State steering inside the model (white box) | Yes: 41 to 73% on flat-to-flat Hanoi (one thesis, two open models) | d07 |
| Procedure or function instead of move list | Yes on Hanoi only; no numbers | d06 |
| Chunked output (next p moves) | Partly; fails near N=8 | d05 |
| Ask model to ignore irrelevant information | Small gain: CoT micro 77.8, macro 15.0 (vs 72.4 and 6.0) | d04 |
| More thinking tokens on high-RC items | No: 0.4 to 3% | c07 |
| Best-of-N / majority vote on high RC | No: collapses at many hosts | c07 |
| One-shot examples on high RC | Small (+3.4 to +6.6), order unchanged | c07 |
| Few-shot examples for R1 | Reported harmful | d13 |
| CoT on implicit-pattern tasks | Harmful: up to -23.1 | d12 |
| Multi-agent split on instruction following | Harmful | c23 |
| Multi-agent debate baselines | Lower than CoThinker on most tasks | a27 |
| Tool use (RDKit) for high-RC chemistry | No: recall 0.094 on REL-C3 | a32 |
| Fine-tuning for function calling | Resisted load best (xLAM2 above 60% in high-load third) | b05 |
| Prompt-only load-aware inference (CLAI) | About 35% fewer tokens at equal accuracy, unreplicated | a28, c10 |

---

## 6. Language models

### 6.1 How models behave as interactivity rises
- **Smooth decline then plateau, with model-specific ceilings.** CogniLoad: 12 of 22 models below 50% by d=5. gpt-5 holds 0.82 and o3 0.80 at d=10. DS-R1-0528 is 0.475 at d=10 but has the highest ID50 (19.07), which shows the ID50 fit and the raw d=10 mean can rank models differently (the ID50 is fitted at mean N and ratio). Beyond d about 7 the decline flattens. (a24, b02, d20)
- **Sharp cliffs for binding.** REL: RC 1-2 is near perfect even at 30x30 (about 91%); accuracy then falls by 45% from RC 3 to 9 and 93% from RC 5 to 20. Input size is not the cause. (c06, c08)
- **Clauses that add interacting quantities.** GSM-Symbolic: Gemma2-9b-it 84.4, 79.1, 68.1, 41.8 as clauses are added. (c12)
- **Dependency load in tool use.** Every model falls. Slope k ranges 0.034 (fine-tuned) to 0.085 (Qwen3-8B). (a26)
- **Small models fail early or entirely.** Llama-3-8B, Llama-3-70B and Mistral-7B scored 0% on 2/3-hop questions even clean. (c09)
- **Reasoning models improve but do not escape.** o1 81.0% overall on ZebraLogic yet 17.0% on X-Large. (b11)

### 6.2 What is worse than load alone
- **Length is a stronger stressor than d in CogniLoad.** Failure is mostly wrong state tracking. (a24, a25)
- **Pure context length hurts even with perfect retrieval and masked filler.** 13.9 to 85%. (d03)
- **Sharing one context between independent problems** costs 10-20x in generations. (d08)

So a "decompose" operator probably gains from three things at once: lower arity, shorter state, and cleaner context. We cannot say which. (K24)

### 6.3 What changed it, and by how much

| Change | Size of effect | Model class | Evidence |
|---|---|---|---|
| Least-to-most vs CoT | +83.5 points on SCAN length; +42.2 on last letters length 12 | code-davinci-002, GPT-3 class | a31, c17 |
| Load-aware meta-prompt (CLAI) | -35% to -36% tokens at -0.2 to -0.4 points | Llama-3-70B | a28, c10 |
| CoThinker | Math +14.4 (60.9 to 75.3); Language +15.2; Instruction following -2.6 | Gemini-1.5-Pro | a27 |
| ADaPT vs best baseline | ALFWorld +14.1 over Reflexion; TextCraft +25 over plan-and-execute | GPT-3.5 | d10 |
| Recite-then-solve | +31.2 | Mistral-7B at 26K tokens | d03 |
| State steering | +32 points (41 to 73%) | Qwen3.6-27B | d07 |
| One-shot on high RC | +3.4 to +6.6 | frontier (Claude, Gemini, GPT) | c07 |
| 4x token budget on high RC | about 0.4 to 3% | frontier | c07 |
| Fine-tune for function calling | above 60% in high-load third vs general models collapsing | 32B | b05 |
| CoT overall | +14.2 symbolic / +12.3 math / +6.9 logic; +0.7 elsewhere | 14 models, 2024 | d11 |

### 6.4 Model-class warnings
- Most decomposition numbers are from 2022 to 2024 models (code-davinci-002, GPT-3.5, Llama-3). Gains on current reasoning models are not measured at equal tokens. (K14, K19)
- Reasoning models spend more tokens on harder items, then fewer near collapse, even with budget left. (b25, a29)
- Frontier models are almost flat on the distractor U-curve. (d20)
- Self-estimates of load or effort carry signal for the same model's own failures but depend on how they are elicited. (d14, d15)

### 6.5 What is missing
No study measures element interactivity inside an LLM's own prompt and tests a count-then-split gate at equal tokens. No study compares a rater-made count with length, steps or depth as predictors of LLM failure on the same items. (K23, critique.md)

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established [E])

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| N1 | **Define difficulty by interacting parts held at once, not by length or amount.** Use this wording in S0's notes so the gate looks at interaction, not size. | S0 (wording only) | [E] | K01; a01, a02, a03, a17, a18, b18 |
| N2 | **Decompose when the clean split exists and sub-steps are easy**, solving sub-questions in order, each seeing earlier answers. Do not claim a gain where the split is fuzzy. | O3 | [E] | K14; a31, c17, c18, d04 |
| N3 | **Expect errors to propagate across steps; check each node of a decomposition** (code-checked where possible), not only the final answer. | O3, S4 | [E] | K16; a30, b12, c16 (also c19, c09) |
| N4 | **Do not use self-rated difficulty or effort as a gate unless it was calibrated on performance.** Single-item ratings have no stable meaning and are order-biased. Calibrate S0 on item pass rates. | S0, G5 | [E] | K07; a22, b14, b19, a23, b15 |
| N5 | **Counts are analyst-assigned: the element count is a hypothesis until two raters agree.** Do not put an unvalidated count in a gate. | S0 | [E] | K17; a15, a33, c06, c01 |
| N6 | **Do not buy high-arity items with extra tokens alone.** More thinking tokens, best-of-N and vote did not fix high RC (single paper but consistent with G11 and G12). Route such items to decompose or to a different representation. | G11/G12 note; O3 | [S] but consistent with established G11, G12 | c07, K09 |
| N7 | **Scaffolds have a cost where they are not needed.** CoT gains cluster in symbolic, math and logic items; the schema's "step-by-step" mode is justified there, and "direct" for the rest. | S0 modes | [E] direction (three sources) | d11, d12, a29; K25 |

N6 and N7 add nothing new to the schema (they restate G11 and G12 with extra support). Only N1 to N5 add information, and N3 is the only one with a new check. Keep them short.

### Test first (not yet established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | **Load-gated decomposition**: estimate load before solving and decompose only above a threshold. Closest evidence is failure-gated ADaPT (not load, not equal tokens, 2023 models). | S0 gate, O3 | [S] | K19; d10, d19, d11 |
| T2 | **Split until each part has at most k interacting elements, k per model class.** Only CogniLoad ID50 gives per-model thresholds (below 0 to 19.07), and it is not a k. | O3 | [S] | K28; d20, b02, K02 |
| T3 | **Model- or rater-made element count predicts failure better than length, steps or depth.** No study. | S0 | [S] | K23; d09, d15, d16 |
| T4 | **Self-rated effort/ability before solving as the load signal.** AUROC 0.83 to 0.89 for self-failure prediction; human-difficulty asks fail. | S0 | [C] | K22; d14, d15, d16 |
| T5 | **Extra context guard**: cost grows with step count (CoT) and with d; hold helper context for low-load items only. The "only low-load items" version is not supported; the cost is larger at high load. So the guard is: keep context short everywhere, more so on hard items. | G (context), O3 | [S] | K20; d04, d20, d03 |
| T6 | **Recite-then-solve for long inputs.** +31.2 on Mistral-7B at 26K; +4 on GPT-4o. | S1 input hygiene, memory | [S] | K20; d03 |
| T7 | **Separate contexts for independent sub-problems.** 5 to 20x generations saved in code tasks. | O3, S3 | [S] | K24; d08 |
| T8 | **Procedure instead of enumeration for long outputs.** Only Hanoi tested. | O3, output format | [S] | K26; d05, d06, b10 |
| T9 | **Adaptive scaffold depth** (shrink scaffolds on items the model already handles; expertise-reversal analogue). | S0 | [S] | K25, K05; d11, d12, d13 |
| T10 | **Isolated-elements-first sequencing** inside a problem. | O3 | [C] | K27; a21, d17, d18, d03 |
| T11 | **Load-aware prompt cutting tokens by 35%.** Unreplicated; single author. | S0, O3 | [S] | K12; a28, c10 |
| T12 | **Split across agents for load.** Helps reasoning, hurts instruction following; modest gains. G9 forbids debate; CoThinker is a structured split, not debate, but needs matched cost. | S0 | [S] | K13; a27, b06, c23, c24 |

Each T row has a matching row in UNKNOWNS.md.

---

## 8. Concrete tests on our bench

All arms get **equal total tokens** (setup, calls and verification counted, G7). Report accuracy with a confidence interval over at least 3 seeds. Use items with a code check where possible.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Synthetic state-tracking puzzles with a load dial (our own generator: entities, attributes, clauses per statement; plus length N). Grid d in {1,3,5,7,10} x N in {20,50,100}. | (a) plain; (b) always decompose; (c) never decompose with extra samples; (d) load-gated decompose (threshold from pilot) | Accuracy by d, N; tokens per item; break-even d | Gate beats always at low d, matches decompose at high d. Plain wins low d (Illusion regime 1). If (d) does not beat both, T1 fails |
| B2 | Same items, steps whose RC is varied while entity count and length are fixed (REL-style: tensor or matrix with RC 1 to 9) | (a) plain; (b) plain with 4x tokens; (c) decompose to RC <= k for k in {2,3,4}; (d) best-of-5 | Accuracy by RC; best k | (b) and (d) flat at high RC (c07); (c) lifts high RC; the best k differs by model class |
| B3 | 100 mixed items from our bench classes (ARC-like, word puzzles, math) counted by two raters and one model for interacting elements | Predictors in logistic regression: element count (each rater), item length, number of steps, depth | Cohen's kappa or ICC between raters; AUC or deviance explained for predicting plain failure | Raters agree (kappa >= 0.6); count adds AUC >= 0.03 over length plus steps. Otherwise T3 fails |
| B4 | Same 100 items | Elicit model's own effort/ability rating before solving (3 prompt forms), and human-difficulty ask | AUROC against own failure; Spearman with pass rate | Effort form AUROC >= 0.65; human-difficulty ask near 0.5 (d14, d15) |
| B5 | Items with two independent sub-problems of known difficulty | (a) both in one context; (b) separate contexts; (c) one context with arity-reduced steps | Success vs product of single success rates | (a) below product (d08); (b) matches product; (c) separates arity from context sharing (K24) |
| B6 | Items with irrelevant clauses (GSM-NoOp style) at two load levels (2 steps vs 6 steps) | (a) CoT; (b) decompose; (c) relevance filter then solve; (d) "ignore irrelevant" instruction | Accuracy drop from clean to distractor, by load level | Drop larger at high load for CoT, flatter for decompose (d04, d20). Tests the interaction direction |
| B7 | Long-input items (10K to 30K tokens) | (a) plain; (b) recite-then-solve; (c) summarise first | Accuracy; tokens | (b) beats (a) for small models; small or zero for frontier (d03) |
| B8 | Long-output items with and without a compact rule (Hanoi, path enumeration, plus 2 non-Hanoi) | (a) enumerate; (b) chunked next-p; (c) ask for procedure/function and run it | Exact-match rate; tokens | (c) wins when a rule exists; no gain when none exists (K26) |
| B9 | Items binned by predicted load (low/mid/high) | scaffold-on vs scaffold-off, per model class | Accuracy by bin at equal tokens | Scaffold-on loses or ties in low bin; wins in high bin (d11, d12) |
| B10 | Same sub-steps, three orders: isolated-elements-first; given order; reverse | each with decompose | Accuracy | Isolated-first >= +3 points if sequencing changes effective load; otherwise K27 stays contested |
| B11 | Hand-written vs model-written decomposition on real tasks | (a) hand-written exemplars; (b) model-written split; (c) plain | Accuracy; bad-split rate | Model-written split loses some of the hand-written gain; measures how much (K14) |

---

## 9. What does not transfer, and why

1. **Human working-memory capacity of about four.** The LLM has no fixed slot count. Capacity claims from n-back are partly task-set failures (c20, c21). Use measured thresholds on our tasks, not 4.
2. **Learner-dependent counts.** Humans have schemas that make an element a single chunk. A model's chunks depend on training. The same step can be 1 for a strong model and 5 for a weak one. The rater must count for the model class. (a02)
3. **Split-attention and modality effects.** These are about two sensory channels and visual search. Text-only LLM prompts have no analogue unless we show a diagram or table next to text. No LLM test exists.
4. **Germane load.** Weakly defined even for humans; the questionnaire items are weak (a23). Not usable.
5. **Subjective ratings of effort.** Humans report them; for the agent, self-report is not evidence (G10), except where a calibrated self-rating predicts its own failure (d14). Even there it is a signal to test, not a measure of load.
6. **Physiological measures** (blinks, pupil, heart rate). No counterpart. Attention entropy and perplexity are proxies used by CoThinker; perplexity needs the ground truth and cannot be used at inference. (c25)
7. **Fixed intrinsic load argument.** A schema-level agent can change the effective load by decomposing, so the "cannot be changed" claim is irrelevant to operators.
8. **Learning vs solving.** CLT studies measure learning from instruction, with tests after a study phase. Our agent solves one item and does not learn from it. The expertise-reversal and worked-example links (adjacent subfields) are about learning. Only the *difficulty-by-interaction* part transfers to in-context solving.
9. **Prompt order of demonstrations.** Human sequencing helps learning across trials. In-context order effects are small or mixed (d17, d18).
10. **Solution length as complexity.** Hanoi N shows collapse by length and state, not by element interactivity. Do not read it as evidence for a count-based threshold. (a29, d07)
11. **Multi-agent splitting as "CLT".** CoThinker's CLT link is an analogy; the authors say proxies are not proof. The gain may come from structure, not agents. (a27, b06)

---

## 10. Open questions

1. Does a rater-made or model-made element count predict LLM failure better than length, steps or depth? What is the inter-rater agreement? (K23; B3)
2. At equal tokens, does gating decomposition on estimated load beat always-decompose and never-decompose? Where is the break-even load? (K19; B1)
3. What is the best k (interacting elements per part) per model class? (K28; B2)
4. Is the human interaction (extraneous-load aids help only at high interactivity) replicable at larger N by independent labs, preregistered? (K03; human side still open)
5. Is the benefit of decomposition due to lower arity per step, shorter chains, separate contexts, or easier per-node verification? (K24; B5)
6. Does the model's own load estimate correlate with true difficulty, and which elicitation works? CLAI never ablated its load step. (K22; B4)
7. Why is the CogniLoad distractor curve U-shaped? Is it a generator confound with effective chain length? Does it appear on current frontier models (almost flat for gpt-5 and o3)? (K21)
8. How much of the Hanoi/long-output collapse is output format vs state loss, and does a procedure format restore scaling outside Hanoi? (K15, K26)
9. Is there an LLM expertise-reversal: should scaffold depth shrink for items the model already handles, and what does over-scaffolding cost at equal tokens? (K25)
10. Can intrinsic load be changed by restructuring (isolated-elements-first, sequencing) beyond plain decomposition? (K27)
11. Is the expertise-reversal meta-analysis (Tetzlaff 2025) number reliable? Open the paper. (d02)
12. Do Sweller 1994's and Halford's counts agree on the same item? No cross-check was found.

---

## 11. Sources

[V] = opened (page or PDF text read this session or by the evidence agents). [M] = snippet, abstract, or second-hand only. Critique.md re-opened the numbers from CogniLoad, CLAI (GSM8K row; MATH CoT row not re-read), GSM-Symbolic, Least-to-most and Illusion of Thinking. The rest are carried as reported by the evidence agents; REL and ToolLoad-Bench tables were not independently re-read (a damaged PDF for 2601.20412 could not be parsed). Do not cite c22 (CausalBN-Bench) at all.

### Human and theory
- [V] Sweller (1994) Cognitive load theory, learning difficulty, and instructional design. https://mrbartonmaths.com/resourcesnew/8.%20Research/Explicit%20Instruction/CLT,%20learning%20difficulty%20and%20instructional%20design.pdf (a01 to a05)
- [M] Sweller and Chandler (1994) Why some material is difficult to learn, Cognition and Instruction 12(3). https://www.e-teaching.org/materialien/literatur/sweller_chandler_1994 (a07)
- [M] Chandler and Sweller (1996) Cognitive load while learning to use a computer program. https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1099-0720(199610)10:2%3C151::AID-ACP380%3E3.0.CO;2-U (a08)
- [V] Sweller (c. 2002) Visualisation and instructional design. https://nielsolson.us/STLHE020409/SwellerVisualizationAndInstructionalDesign.pdf (a09; also a10 via Cooper et al. 2001 [M])
- [V] Leahy, Chandler, Sweller (2003) When auditory presentations should and should not be a component of multimedia instruction. https://tecfa.unige.ch/tecfa/teaching/methodo/Leahy_etal03.pdf (a11, a12, a13)
- [V] Chen, Kalyuga, Sweller (2016) When instructional guidance is needed. https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/309693C5A83EB7485D536B5A2408B22B/S2059077616000169a.pdf/when-instructional-guidance-is-needed.pdf (a14, a15)
- [M] Sweller (2010) Element interactivity and intrinsic, extraneous and germane cognitive load. https://doi.org/10.1007/s10648-010-9128-5 (a16)
- [V] Halford, Wilson, Phillips (1998) Processing capacity defined by relational complexity. https://www.cmu.edu/dietrich/psychology/memorylab/publications/98_jra_cl_mcl_lmr.pdf and https://staff.aist.go.jp/steven.phillips/papers/relational_complexity.pdf (a17, a18, a19, b18)
- [M] Maybery, Bain, Halford (1986) and Halford, Maybery, Bain (1986), transitive inference, as cited in Sweller 1994 and Halford 1998 (a06)
- [V] de Jong (2010) CLT, educational research, and instructional design: some food for thought. https://ris.utwente.nl/ws/files/6597420/Jong10cognitive.pdf (a20, a21, a22, b13, b14)
- [V] Klepsch, Schmitz, Seufert (2017) Two instruments measuring intrinsic, extraneous, germane load. https://www.frontiersin.org/articles/10.3389/fpsyg.2017.01997/pdf and https://pmc.ncbi.nlm.nih.gov/articles/PMC5696680/ (a23, b15)
- [M] Leppink et al. (2013) Instrument for measuring intrinsic, extraneous, germane load. https://repub.eur.nl/pub/63158 (b16)
- [V] Ayres, Lee, Paas, van Merrienboer (2021) Physiological measures of intrinsic load. https://pmc.ncbi.nlm.nih.gov/articles/PMC8461231/ (b17)
- [V] Krieglstein et al. (2025) Primacy effects in reporting cognitive load. https://doi.org/10.1007/s10648-024-09980-0 (b19, b20)
- [M] Chen, Paas, Sweller (2023) Defining and measuring task complexity through element interactivity. https://ro.uow.edu.au/test2021/8616 (b21)
- [M] Chen, Kalyuga, Sweller (2017) Expertise reversal as a variant of element interactivity. https://link.springer.com/10.1007/s10648-016-9359-1 (b22)
- [M] Tetzlaff, Simonsmeier, Peters, Brod (2025) Meta-analysis of the expertise reversal effect. https://doi.org/10.1016/j.learninstruc.2025.102142 (b23, d02)
- [M] Ehrich et al. (2021) Item response modelling of cognitive load. https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2021.648324/full (b24)
- [V] Beege et al. (2019) Spatial continuity effect vs spatial contiguity failure (with Schroeder and Cenkci 2018 sheet). https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2019.00086/pdf (d01)

### LLM studies
- [V] Kaiser et al. (2025) CogniLoad. https://arxiv.org/abs/2509.18458 (a24, a25, b01, b02, b03, c01, c02, c03, d20)
- [V] Fesser et al. (2026) REL. https://arxiv.org/abs/2604.12176 (a32, c06, c07, c08)
- [V] Wang et al. (2026) ToolLoad-Bench. https://arxiv.org/abs/2601.20412 (a26, b04, b05, c04, c05)
- [V] Shang et al. (2026) CoThinker. https://arxiv.org/abs/2506.06843 (a27, b06, b07, c23, c24, c25)
- [V] Zhang (2025) CLAI. https://arxiv.org/abs/2507.00653 (a28, c10)
- [V] Shojaee et al. (2025) The Illusion of Thinking. https://arxiv.org/abs/2506.06941 (a29, b09, b25, c14)
- [V] Lawsen (2025) The Illusion of the Illusion of Thinking. https://arxiv.org/abs/2506.09250 (b10, c15, d06)
- [V] Dellibarda Varela et al. (2025) Rethinking the Illusion of Thinking. https://arxiv.org/abs/2507.01231 (d05)
- [V] Pereira and Zuidema (2026) Transformers struggle to use their emergent world models: revisiting the Tower of Hanoi. https://arxiv.org/abs/2608.07077 (d07)
- [V] Dziri et al. (2023) Faith and Fate. https://arxiv.org/abs/2305.18654 (a30, b12, c16)
- [V] Zhou et al. (2023) Least-to-most prompting. https://arxiv.org/abs/2205.10625 (a31, c17)
- [V] Khot et al. (2023) Decomposed Prompting. https://arxiv.org/abs/2210.02406 (c18)
- [V] Mirzadeh et al. (2025) GSM-Symbolic. https://arxiv.org/abs/2410.05229 (c12, c13)
- [V] Shi et al. (2023) GSM-IC. https://arxiv.org/abs/2302.00093 (d04)
- [V] Lin et al. (2025) ZebraLogic. https://arxiv.org/abs/2502.01100 (b11)
- [V] Huang et al. (2024) Complexity of Theory-of-Mind tasks and Discrete World Models. https://arxiv.org/abs/2406.11911 (b08)
- [V] Zheng et al. (2026) Equivalence class problem. https://arxiv.org/abs/2605.06882 (c19)
- [V] Adapala (2025) Cognitive load limits in LLMs (ICE). https://arxiv.org/abs/2509.19517 (c09)
- [V] Upadhayay et al. (2024) Cognitive Overload Attack. https://arxiv.org/abs/2410.11272 (c11)
- [V] Gong, Wan, Wang (2024) Working memory capacity of ChatGPT. https://arxiv.org/abs/2305.03731 (c20)
- [V] Hu and Lewis (2025) N-back investigations. https://arxiv.org/abs/2412.18120 (c21; abstract and intro only)
- [M] CausalBN-Bench (search summary). https://arxiv.org/abs/2404.06349 (c22: do not cite)
- [V] Du et al. (2025) Context length alone hurts. https://arxiv.org/abs/2510.05381 (d03)
- [V] Wolf et al. (2025) Compositional hardness of code in LLMs. https://arxiv.org/abs/2409.18028 (d08)
- [V] Schnabel et al. (2026) Lost in transmission (BAPO). https://arxiv.org/abs/2505.08140 (d09)
- [V] Prasad et al. (2024) ADaPT. https://arxiv.org/abs/2311.05772 (d10)
- [V] Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183 (d11)
- [V] Liu et al. (2024) Mind your step (by step). https://arxiv.org/abs/2410.21333 (d12)
- [V] DeepSeek-AI (2025) DeepSeek-R1 technical report. https://arxiv.org/abs/2501.12948 (d13)
- [V] Bhattacharyya et al. (2026) Beyond confidence. https://arxiv.org/abs/2605.07806 (d14)
- [V] Li et al. (2026) Can LLMs estimate student struggles? https://arxiv.org/abs/2512.18880 (d15)
- [V] Kolesnikova et al. (2026) and Acquaye et al. (2026) item difficulty with LLMs. https://arxiv.org/abs/2605.18562 (d16; Acquaye abstract and first page only)
- [V] Liu et al. (2024) In-context curriculum learning. https://arxiv.org/abs/2402.10738 (d17)
- [V] Ma et al. (2025) Problem-solving logic guided curriculum ICL. https://arxiv.org/abs/2502.15401 (d18)
- [V] Kang et al. (2024) Empirical complexity of reasoning and planning in LLMs. https://arxiv.org/abs/2404.11041 (d19; abstract and intro only)

### Links to parallel subfields (not covered here)
Worked-example research; Cue overload and fan effect; Problem finding; Item difficulty modelling; Value of information; Plans and schemas; Functional decomposition; Planning by tree search with pruning; Expected value of control; Generation versus evaluation; Reflective reasoning and second look; Bias and debiasing. The ones that bear most directly on this document: Item difficulty modelling (how to predict difficulty from item features, T3), Functional decomposition and Plans and schemas (how to split, T2), and Expected value of control (when the gate should spend).
