# Dual-process view of creativity: deep document

*Subfield A09.02. Built from evidence_a-d.jsonl (a01-a30, b01-b29, c01-c27, d01-d17), claims.jsonl (K01-K25) and critique.md in this folder. "Opened" means the page or PDF text was read in a research session; snippet-only items are marked and not used for any established claim.*

## 1. What it is

The idea: creative thinking moves between two modes. A **generative** mode produces many candidate ideas. An **evaluative** mode judges, refines and selects them. Dual-process theory adds a second axis: thinking can be fast, associative and automatic (Type 1) or slow, effortful and working-memory bound (Type 2). The dual-process view of creativity asks how these two axes relate and how the mind shifts between modes [a01, c01].

The key review is Sowden, Pringle and Gabora (2015), arXiv 1409.2207, Thinking & Reasoning 21(1) 40-60 [a01]. Its main conclusion is a **negative** one for the naive story:

- Generation = Type 1 and evaluation = Type 2 does **not** hold. Generation can use both types. Exploration and evaluation look mainly Type 2 [b01].
- Divergent thinking can be deliberate and effortful. Convergent insight can arrive after unconscious incubation [a02].
- Dual-process theory itself is contested: System 1 is not one thing, and a third process may control the switch [b04].
- There is little empirical work on the shift itself. The authors call for chronometric and neuroimaging work [c02, a06].

Two separate dials follow, and they matter for engineering:

1. **Mode** (generate vs judge): who sets it, and when.
2. **Effort** (cheap vs costly processing): how much compute each step gets.

Our schema already puts the mode switch in code (the program decides transitions, the model fills slots). This document asks what the human and LLM evidence says about that design: how to alternate, how to diversify the generative stage, how to build the evaluative stage, and what not to do.

Scope. Overlaps are covered elsewhere and only linked: Geneplore and blind variation (parallel A09 documents), divergent thinking, conceptual blending, transformational creativity, insight as a process, novelty search, and Artificial Hivemind-type homogeneity (F01/F05 briefs). This document adds the mode-switch evidence and the LLM tests of two-stage designs.

## 2. History and theories in depth

### 2.1 Stage and cycle models (the "two modes" lineage)

- **Wallas (1926)**: preparation, incubation, illumination, verification. Incubation is the unconscious half; verification is conscious evaluation [a02, c21].
- **Guilford**: divergent vs convergent production. Divergent = many answers; convergent = one right answer. Used by CreativeDC and by the benchmarks C2-Eval and ConDiFi [c15, c22, c16].
- **Campbell (1960) and Simonton: Blind Variation and Selective Retention (BVSR)**. Ideas are produced blindly, then the fittest are retained. The review lists problems: successive ideas are not unrelated as BVSR assumes (Feinstein 2006; Nijstad and Stroebe 2006), and the theory has long-standing critics (Dasgupta, Eysenck, Gabora, Sternberg, Weisberg) [a04]. For an LLM, samples from one model are neither blind nor independent (guardrail G4).
- **Geneplore (Finke, Ward and Smith 1992)**: a generate phase (retrieve, associate, synthesise pre-inventive structures), then an explore phase (find attributes, test function). Ward's "path of least resistance": people copy features of known exemplars, e.g. imagined aliens get arms and legs [a05]. See the parallel Geneplore document.
- **Basadur's ideation-evaluation cycles**: problem finding is ideation-heavy; implementation is evaluation-heavy; problem solving mixes. People differ in how much they favour ideating over evaluating [a03]. (Secondhand; primary papers not opened.)
- **Howard-Jones (2002) Dual-State model and Gabora's Honing Theory**: associative (defocused) thought generates; analytic (focused) thought refines, iterating. These align most cleanly with dual-process cognition. Whether the two modes run in series or in parallel is unresolved [a06].

### 2.2 The dual pathway to creativity (Nijstad, De Dreu, Rietzschel and Baas 2010)

Originality comes by one of two routes [a10]:

1. **Flexibility**: many categories, broad associations, less executive control.
2. **Persistence**: deep systematic work in few categories, more executive control.

An "idea monitor" filters ideas entering working memory. The model covers intentional creative work only. A personal communication from Nijstad (reported in the review) says the two measures are unrelated and that people may entrench in one pathway over time [a09, b03]. This is weak evidence (unpublished, no numbers).

### 2.3 Individual-differences and executive-function accounts

- **Beaty et al. 2014**: remote association plus executive inhibition of common ideas. Used as the template by Chen and Ding [c06, c27]. Seen only as a citation.
- **Benedek et al. 2014**: divergent thinking depends on updating and inhibition, not on shifting [b11].
- **Lee and Therriault 2013**: associative fluency is the shared base of divergent and convergent thinking [b13].
- **Barr (2014 thesis; Barr et al. 2015 article)**: remote (cross-domain) analogies need Type 2 effort; a disposition toward analytic thinking predicts them [a17-a20].

### 2.4 Neural versions

- **Default network (generation) plus executive control network (evaluation), toggled by the salience network** (Menon and Uddin 2010, as reviewed) [a08]. Ellamil et al. 2012 complicate this: evaluation engaged executive and default regions together, and generation engaged the medial temporal lobe [a21].
- **Beaty, Benedek, Silvia and Schacter 2016 (TiCS)**: the default network supplies candidates; the control network couples with it to constrain them. Coupling is task-dependent and changes through a response. In poets, default-control correlation was negative during spontaneous generation and rose during revision [b14, b15].
- A 2024 fMRI story-creation preprint favoured alternation over parallel running [a23].

### 2.5 Computational and architectural proposals

- **Helie and Sun 2010 (CLARION, EII theory)**: implicit associative plus explicit rule processes across Wallas' stages. The oldest runnable dual-process creativity system. Seen only in a secondary summary [c23, snippet].
- **Chavez 2025 "Generative System 3"**: high-entropy generator (default-like), learned critic (control-like), adaptive gain controller that moves sampling entropy from a surprise signal. No experiments; predictions untested [a27, c08].
- **TinyTim 2025**: a 1.1B model fine-tuned on Finnegans Wake as a divergent specialist, paired in theory with an instruction-tuned convergent evaluator [c13].

### 2.6 What changed in 2023-2026

LLM studies moved from "are LLMs creative?" (DAT scores [c03, b16]) to "does a structural split of generate and converge help?" (CreativeDC, LLM Discussion, ReDNA, Verbalized Sampling [a26, c09, c17, d01]). In parallel came the finding that model outputs are homogeneous within and across models [c19, d03]. No paper yet controls token parity for the two-stage design (critique.md, gap 1).

## 3. Core findings with exact numbers

Status key: **established** = two or more independent sources; **single** = one source; **contested** = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Generation/evaluation do not map to Type 1/Type 2 | Narrative review, 7,474 words; no new data | Sowden et al. 2015 [a01, b01] | single (review) |
| Flexibility predicts originality more than within-category fluency | r = .34 vs .12; flexibility vs within-category fluency r = .01; fluency-flexibility r = .72 (k=17, N=1858); fluency-originality r = .22 (k=13, N=1699); 20 studies, N = 2118 | Nijstad et al. 2010 chapter [a11] | single (authors' own studies, not a systematic search). Sowden quotes .36; the table reads .34 |
| Originality and feasibility trade off in humans | r = -.42 (k=8, N=610) | Nijstad 2010 [a11] | single |
| Narrow topic raised originality (persistence) | N=102; M 2.33 narrow vs 2.18 broad (5-pt); fluency-originality r = .28 narrow vs -.06 broad | Rietzschel 2005 via Nijstad [a12] | single, small effect |
| Priming a sub-topic raised share and originality in it | N=75; r = .36 (nutrition), .61 (sports) | Rietzschel et al. 2007b via Nijstad [a13] | single, correlational |
| A strict idea monitor kills originality | Need for Structure helps only when Fear of Invalidity is low; Study 1c N=102, Study 2 N=240 replicated | Nijstad 2010 [a14] | single (internal replication) |
| Activating moods raise originality | N=58: originality anger 2.73, happy 2.77, sad 2.06, relaxed 2.26; flexibility prediction failed (power under .20) | De Dreu et al. 2008 via Nijstad [a15] | single, small |
| Remote analogies need more Type 2 capacity | Cross-domain 52.6% vs within 89.3% (N=41, t=11.28); more time: 52.6 to 64.6 (+12) vs 89.0 to 93.3 (+4.3) | Barr 2014 thesis [a17, a18] | single, between-experiment comparison |
| Cueing analytic vs intuitive style did not help remote analogies | 69.9% vs 69.0% (N=76, t<1); within-domain analytic 93.6 vs 91.1 (p<.01); cross-domain non-analogies reversed 73.8 vs 78.9 | Barr [a19] | single; a failed prediction |
| Incubation gives a small gain | g = 0.29 (CI .21-.39), 117 effects, 3,606 people, 85 of 117 positive; unweighted .36; Q = 173.99, df 113, p<.001 | Sio and Ormerod 2009 [b05] | contested (heterogeneous; sibling unconscious-thought effect failed) |
| Creative problems gain most; low-load fillers beat high-load | high-load vs low/rest difference about 0.91 (p<.05) and 0.79 (p=.08) | Sio and Ormerod [b06, b07] | single |
| Unconscious thought advantage failed to replicate | N=399; 55.61% vs 55.17%; BF about 7.83 for null; 61 studies, 16 significant (12 pro, 4 against); pooled g = .15 (CI .03-.26) before bias correction | Nieuwenstein et al. 2015 [b08-b10] | established as a failure (choice tasks, not creativity) |
| Divergent thinking needs updating and inhibition, not shifting | b = .29 (p<.001), .20 (p=.04), ~0 shifting; Gf-creativity r .45; executive functions explain 43% (r .45 to .34); openness b = .36 | Benedek et al. 2014 [b11, b12] | single; differs from Lee |
| Associative fluency underlies both divergent and convergent | N=265; b = .56 divergent, .82 convergent; divergent-convergent latent r = -.52 ns; IQ to fluency b = .84 | Lee and Therriault 2013 [b13] | contested vs Benedek |
| Neural alternation between states | fMRI N=41: rating t = 13.01; transitions t = 14.99; alternating beat parallel (p = 1.4e-32, 2.4e-47) | bioRxiv 2024 [a23] | single, preprint |
| EEG separates generate, evolve, evaluate | N=28; alpha drop smaller in evolution; upper-alpha larger in evaluation | Sci Rep 2021 [a22] | single, small |
| Evaluating earlier ideas raises later originality | Alternative Uses with EEG; N not read | Brain & Cognition 2016 [a24] | single (abstract only) |
| LLMs beat the human DAT average | GPT-4 greedy DAT 89.1, above 96.1% of humans; GPT-3.5 80.8; a random WordNet sampler also beat most | Chen and Ding 2023 [c03] | established (rare-word caveat) |
| GPT-4 DAT rises with temperature (disputed) | T 0.5/1.0/1.5, n=500 each; top mean 85.6, above 72% of humans; "microscope" in 70% of GPT-4 sets | Bellemare-Pepin 2024 [b16, b17] | contested (Chen and Ding: no gain for GPT-4) |
| Temperature is a weak creativity dial | Llama 2 70B, 100 stories per temperature; weak positive link with novelty, moderate negative with coherence | Peeperkorn 2024 [c11] | contested/weak |
| Novelty is U-shaped in temperature | originality up, quality down; peak varies; T 0.5-2.0 on OLMo-7B, Pythia-12B | Padmakumar 2026 [b22] | single |
| Prompting for novelty or denial gives small, uneven gains | TinyStories +6.9% (OLMo), +6.3% (OLMo-2); CoPoet +9.6%, +4.9%; MacGyver -18%, +3.7% | Padmakumar [b23] | single (consistent with b24, a19) |
| Accuracy-style reasoning does not raise divergence | self-correction and planning lowered divergent creativity (as low as -1.2); only MCTS helped | Lu et al. 2025 [b19] | single |
| Two-stage prompt raises diversity | Qwen3-235B, T 1.0, K=50: about 12-13 distinct (12 high-utility) vs about 8; Vendi p<.001; novelty win 96.67%; validity 1.00 vs 0.78; Vendi +24.0% at K=10, +72.0% at K=100 | CreativeDC [a26, d07] | single (one paper, four ids) |
| Fixed diverge-discuss-converge lifts judged originality | gpt-3.5, 4 of 4 benchmarks; 1,406 responses, 42 annotators | LLM Discussion [c09] | single, same-family judge |
| Code-separated diverge then converge fixes fixation in agents | path discovery GPT-5.4 48.2 to 67.9; Claude Sonnet 4.6 53.6 to 73.2; Llama-4 23.2 to 51.8; Qwen3 39.3 to 64.3; human 79.9; Self-Refine cut Claude to 44.6 | ReDNA [c17] | single, 10 scenarios |
| Structural k-candidate call beats direct and sequence | diversity 1.6-2.1x; poem 1.90 to 2.39; story 2.74 to 3.06; joke 1.83 to 3.01 (sequence 2.93) | Verbalized Sampling [d01] | single |
| Reasoning models are as collapsed and respond to the same fix | poem R1 12.4 to 33.6; o3 13.2 to 28.0; story R1 24.8 to 49.0 | VS appendix [d02] | single |
| LLM outputs are homogeneous; decoding barely helps | 79% of cases with similarity above 0.8; min-p T 2.0: 61.2% of pairs above 0.8; cross-model 0.71-0.82 | Artificial Hivemind [c19, d03] | established (with d06, d10, d09) |
| GPT-4 temperature diversity non-monotonic; extra critique step best | 4,000 solutions, 8 temp/top-P combos, 8 prompt methods | Ma and Grandi 2024 [d06] | established (with d03) |
| LLM critics judge creativity unlike people | novelty-fit r: humans -.39, GPT-3.5 -.67, GPT-4 .13, GPT-4o .16 | Zhang et al. 2025 [d05] | established (with d04, d13) |
| Judge-human agreement falls on near-equal answers | drops "significantly" in similar-quality and high-entropy subsets; r in figures | Hivemind [d04] | single |
| LLM judge matches human inter-rater agreement on originality | Kendall tau .5213 vs humans' .5094 (originality); elaboration .2753 vs .4753 | LLM Discussion [c10] | contested (c18: OCSAI r .28 on mixed data) |
| Elaboration biases automatic originality raters | 4,813 responses; OCSAI vs humans r = .28 overall, .59 human only | Italian AUT study [c18] | single |
| Semantic entropy is a cheap diversity measure close to human | kappa .56 (entropy) vs .49 cosine, .35 Self-BLEU | Sen et al. 2026 [d13] | single |
| Tree of Thoughts on a closed task | Game of 24: CoT 4% vs ToT 74% (GPT-4) | Yao et al. 2023 [d11] | single (search with evaluator) |
| Diverse generation improves math training data | MATH500/Olympiad/Minerva mean: direct 30.6, VS-Standard 36.1, VS-CoT 36.9, VS-Multi 37.5 | VS appendix [d02] | single |
| Humans fixate on shown AI images | N=60; fixation GenAI .32 (BF 124); variety -.29; originality -.03 | Wadinambiarachchi 2024 [d08] | single |
| LLM guidance changed later human output | Exp 2 N=640: guidance vs none -10.6 points [-18.6, -2.7] on RAT; Exp 1 N=460 | Kumar et al. 2025 [c20] | single |

## 4. Mechanisms and models

### 4.1 The control structure (what to implement)

A mode switch is a small finite-state machine run by code. Minimal form:

```
mode = GENERATE
while budget:
    if mode == GENERATE:
        pool += generate(task, constraints_hidden=True, ban=history_of_used_ideas)
        if len(pool) >= quota or stalled(pool): mode = CONVERGE
    elif mode == CONVERGE:
        survivors = filter_by_check(pool)      # code check first
        ranked = rank_in_code(survivors)       # semantic entropy, dedup, run tests
        if good_enough(ranked): return ranked[0]
        mode = GENERATE; feed(failing_output)  # revise from real output (G2)
```

Design rules taken from the evidence:

1. **The switch is set by counters and checks in code, not by the model.** The dual-process literature itself needs a third controller process [b04]. LLM self-judgement is unreliable [d05, d04]. An instruction to think analytically did not change human behaviour [a19].
2. **Hide the constraints in the generate step.** CreativeDC brainstorms "on the theme alone with no judgement", then picks one idea and binds it to the target concept, retrying on failure [c15, d07].
3. **Judge after the quota, not inside it.** A strict internal monitor killed originality in humans [a14]. Cycling too fast makes people judge before ideas mature [a07].
4. **Keep earlier candidates out of the generate call** (mismatch hazard, fixation) [a07, d08]. This is contested for LLMs: NoveltyBench's abstract says re-asking with earlier answers shown raised diversity [d10]. See 4.4.
5. **Ban what was used** (denial prompting). Code holds a history of used techniques or concepts and writes a "forbid these" line [b20]. The gain is small and trades quality [b23], so add a quality gate.
6. **Pick breadth or depth by a signal.** Flexibility predicts originality more [a11]. Persistence (many ideas inside one frame) helps when the topic is narrow or primed [a12, a13]. Code rule: if the last m candidates fall in one cluster, force a new category; if a category yields valid novel candidates, sample more inside it.
7. **Separate novelty from validity.** Score each in its own call or in code (embedding distance from the pool for novelty; run the check for validity), and combine in code [d05, c14].

### 4.2 Diverge-step variants that were tested

- **Verbalized Sampling**: one call asks for k candidates with verbalized probabilities (k=5, N=30 samples, 100 prompts per task). Better than direct and than a sequence baseline at the same number of responses [d01]. Quality drops if k is too large. Small models lose quality. Larger models gain 1.5-2x more.
- **Two-phase prompt (CreativeDC)**: explore with the requirement hidden, then converge [a26].
- **Critique-and-edit second pass** (Ma and Grandi): one extra step gave the largest diversity gain of 8 prompt methods for GPT-4. A persona "excellent at far-fetched ideas" gave a considerable gain. The word "unique" gave lower diversity than "creative" or "novel" [d06].
- **Strategy lens** (Bellemare-Pepin): telling the model to use an etymology or thesaurus strategy beat the plain DAT prompt for GPT-4 [b18].
- **Denial prompting** [b20, b23].
- **MCTS**: the only reasoning strategy that raised divergent creativity [b19].
- **Fixed discussion rounds with personas**, then a code-set final converge round [c09].
- **Agent-level divergence (ReDNA)**: unconstrained divergent candidate paths, then constrained selection [c17].

### 4.3 Evaluate-step variants

- **Code-side diversity measures**: semantic entropy (kappa .56 with humans), Vendi score, embedding similarity, Self-BLEU [d13, a26].
- **Retrieval-based LLM judge**: 84.7% vs ChatEval 76.7% on MacGyver, 83.0% vs 73.3% on BookMIA; about 63% fewer tokens per pair (23,758 in / 3,796 out vs 66,944 / 8,634) [d13].
- **Novelty as originality times quality**: harmonic mean of unseen n-gram fraction and task quality [b21].
- **Run the code** where a check exists. Lu et al. use human solutions as the reference pool [b19, b20].

### 4.4 Open mechanism question: fixation by shown candidates

Humans fixate on shown examples [a07, d08]. For models the evidence points both ways: re-asking with earlier outputs shown helped in NoveltyBench's abstract [d10]. The pipeline we want uses isolated attempts (S3). Test before choosing (UNKNOWNS).

## 5. What holds up

### 5.1 Replications and failures

- **Held up**: incubation is small but robust, with no funnel-plot bias (g .29, k=117) [b05]. LLM output homogeneity is shown across 25 to 70 models in one large study and corroborated by NoveltyBench, Ma and Grandi, and the design-fixation papers [c19, d03, d06, d10, d09]. Temperature as an unreliable dial has four supporting sources [c04, c11, d06, d03] and one dissent [b17].
- **Failed**: the unconscious thought advantage (N=399, BF 7.8 for null; only 16 of 61 studies significant) [b08, b09]. The moderator account was tested under supposedly optimal conditions and still failed [b10]. Analytic-style cueing did not help cross-domain analogies in Barr's Exp 4 [a19]. The mood-flexibility prediction failed in Study 1 (power under .20) [a15].
- **No failed replication of the dual pathway model itself** was found. But its evidence is mostly the authors' own studies, not a systematic search, and the fluency-flexibility link (r .72) is partly definitional [a11, critique].
- **Different latent structures**: Benedek (executive functions, no shifting) vs Lee and Therriault (associative fluency shared, divergent and convergent unrelated). No preregistered replication found [b26].

### 5.2 Moderators and boundary conditions

- **Problem type**: creative multi-solution problems gain most from incubation. Longer preparation gives larger effects. Low-load fillers beat rest for linguistic problems [b06, b07].
- **Distance of the link**: more time helps remote analogies (+12) much more than near ones (+4.3) [a18].
- **Easy vs hard items**: people expecting evaluation did better on easy RAT items and worse on hard ones because they searched systematically (Harkins, as reported; no numbers) [a16].
- **Topic width**: narrow topics raised originality a little (+0.15 points) [a12].
- **Temperature**: depends on model, task and prompt. Weak models gain on DAT; GPT-4 may not [c04, b17]. Novelty is U-shaped [b22].
- **Model size**: larger models gain more from structural diversification (1.5-2x) [d01]. Yet within a family larger models are often less diverse [d10].
- **Domain**: gains are shown in educational Python tasks, story, poem, joke, AUT, design and one agent benchmark. Creativity scores do not transfer across tasks (CreativityPrism: 17 LLMs, 8 tasks) [d12].

### 5.3 Interventions that worked

- Phase split with the requirement hidden (CreativeDC) [a26].
- Structural k-candidate calls (Verbalized Sampling) [d01].
- Code-separated diverge then converge in agents (ReDNA) [c17].
- Critique-and-edit extra pass (GPT-4 design solutions) [d06].
- Retrieval judge and semantic entropy for scoring [d13].
- Evaluating earlier ideas before generating more (humans) [a24].
- A strategy lens in the prompt (DAT) [b18].
- A "far-fetched" persona (design) [d06].

### 5.4 Interventions that did not work, or backfired

- Temperature alone [c04, c11, d03, d06].
- Min-p at T 2.0: still 61.2% of pairs above 0.8 [d03].
- Cross-model mixing: similarity 0.71-0.82 across models [d03].
- Self-correction and planning for divergence (lowered it) [b19]. Self-Refine cut Claude's path discovery to 44.6% in ReDNA [c17].
- Plain chain of thought for diversity: CoT = Base in CreativeDC [b24].
- Asking for novelty or denial prompting without a quality gate: -18% on MacGyver for OLMo [b23].
- "Think analytically" cues [a19].
- Distraction before choice [b08-b10].
- LLM strategy lists given to humans lowered later diversity [c20].

## 6. Language models

### 6.1 Baseline behaviour

- **Remote association (DAT)**: GPT-4 89.1 greedy, above 96.1% of about 100,000 humans; GPT-3.5 80.8; no LLM matched the top humans [c03, b16]. With word surprisal controlled, GPT-4 and GPT-3.5 still beat the average human, but GPT-4's lead shrank (appendix numbers not extracted) [c05]. A random WordNet sampler also beat most humans and models [c03]. Across-run repetition is severe: "microscope" in 70% of GPT-4 sets; "ocean" in over 90% of GPT-4-turbo sets; humans' top word "car" 1.4% [b16]. The per-sample score hides low diversity.
- **Other tasks**: GPT-3.5, GPT-4 and GPT-4o beat humans on divergent and convergent output tasks, but evaluate unlike humans and have lower forward flow [d05]. A Dec 2025 Scientific Reports item (snippet only, unverified) says GenAI ideas beat human ones on AUT and RAT [c24].
- **Divergent and convergent skill are separable**: weak correlation across models and domains. Convergent improves with size and recency; divergent breadth does not [a29]. ConDiFi: divergent ranking (cohere_command_a 8.04, deepseek_r1 8.03, gpt4o 6.92) differs from convergent (llama4_maverick 72.32%, o1 71.41%) [c16]. CreativityPrism: no significant frontier lead on divergent thinking [d12].
- **Search style**: embedding jump profiles show each LLM leans to a flexible or persistent path depending on task. Flexible LLMs score higher, while in humans both styles score alike (abstract only) [c07].

### 6.2 Homogeneity

79% of cases show mean within-model similarity above 0.8 (top-p 0.9, T 1.0). Cross-model similarity is 0.71-0.82. 31,250 human annotations [c19, d03]. Direct prompting of reasoning models gives poem diversity 13.2 (o3) and 12.4 (R1) [d02]. Designers using GPT-4o and Midjourney produced less diverse chairs than award entries: text novelty proportion 67.4% vs 78.2%; 7 of 10 designers saw text repetition and 8 of 10 saw image repetition (N=10) [d09].

### 6.3 What changed it, and by how much

| Intervention | Model | Result | Token parity? | Id |
|---|---|---|---|---|
| Two-phase prompt | Qwen3-235B | about 13 vs 8 distinct at K=50; Vendi +72.0% at K=100 | no | a26, d07 |
| Verbalized sampling | GPT-4.1, Gemini-2.5, Claude-4, Llama-3.1-70B, Qwen3-235B, o3, R1 | 1.6-2.1x diversity; joke 1.83 to 3.01 | matched responses, not tokens | d01 |
| Diverge-discuss-converge | gpt-3.5-turbo-0125 | judged originality up on 4 of 4 benchmarks | no | c09 |
| ReDNA | GPT-5.4, Claude Sonnet 4.6, Llama-4, Qwen3-235B | path discovery +19.7, +19.6, +28.6, +25.0 points | no | c17 |
| Critique-edit pass | GPT-4 | largest gain of 8 prompt methods | no | d06 |
| Strategy lens | GPT-3.5, GPT-4 | significant over the original DAT prompt | n/a | b18 |
| Novelty prompt / denial | OLMo, OLMo-2 | +3.7% to +9.6%, one -18% | n/a | b23 |
| Temperature | GPT-4 | mixed; best at T1/top-P1 in design; DAT 85.6 at top T elsewhere | n/a | b17, d06 |
| Min-p T 2.0 | many | still 61.2% of pairs above 0.8 | n/a | d03 |
| Self-Refine | Claude Sonnet 4.6 | 53.6 to 44.6 (worse) | n/a | c17 |
| Tree of Thoughts | GPT-4 | Game of 24: 4% to 74% | no | d11 |
| Diverse data generation (VS) | various | math accuracy 30.6 to 36.1 / 36.9 / 37.5 | n/a | d02 |

ReDNA also moved AUT originality from 2.91 to 3.77, but Claude's AUT originality fell 2.764 to 2.616. Judge is an LLM; 10 scenarios [c17]. The 2026 preprints use the newest models (GPT-5.4, Sonnet 4.6) but are one-off and author-judged.

### 6.4 Judging

LLMs agree with each other on Alternative Uses ranking (Spearman above .7; against the oracle above .77; four models), but the oracle ordering was easy to rank [a28]. They separate common from highly creative ideas fairly well, but not near-equal ones [d04]. They lack the novelty-fit trade-off [d05]. Elaboration biases automated originality scoring (OCSAI-human r .28 on mixed data, .59 on human only) [c18]. A 2026 snippet reports LLM ratings less sensitive to context than human ratings [c26, snippet]. Judge families often match the generator [c09, c10].

### 6.5 Dual-process framing in LLM work

Most LLM papers use dual-process only as a label. CreativeDC cites Wallas and Guilford, not dual-process [c15]. Chen and Ding read stability under sampling as "implicit control" [c06]. No study tests Type 1 vs Type 2 compute directly on creative output. A brain-alignment preprint suggesting chain-of-thought training moves models away from creative structure [c25, d16] could not be identified or opened. Do not use it.

## 7. What our agent should take

Status marks: **[E]** established (two or more independent sources), **[S]** single source, **[C]** contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

These are mostly "keep" and "do not add" items. None changes a guardrail; they sharpen S3 open mode and S7.

1. **Keep mode in code; treat mode and effort as two dials** (G1 / S0 / S3-S4). Status [S] for the literature claim (one review, K01), but it is already our design, so no schema change. Evidence a01, a02, b01, b04.
2. **Do not use temperature as the diversify dial; diversify by structure** (S3 open mode). [E] four sources [c04, c11, d03, d06] against one dissent [b17] (K21 established; K06 contested). Structure means separate calls, a code-held ban list, and a k-candidate batch.
3. **Do not count on more plain draws or cross-model mixing for diversity** (G4 / S3). [E] homogeneity within and across models [c19, d03, d06, d10, d09] (K09). Reinforces G4 and the S3 rule "forced untried directions".
4. **Do not use instruction-only mode changes** ("be creative", "think analytically") (section 4b). [E]-leaning: Barr Exp 4 null (69.9 vs 69.0) [a19]; novelty prompts small and uneven [b23]; plain CoT equals Base on diversity [b24]. Consistent with existing 4b entries.
5. **Any novelty-pressure step (ban list, avoid-the-prototype, far analogue) needs a quality gate in code** (S4 / S7). [E] K08: originality rises and quality falls [b21, b22, b23, c14]; humans show originality-feasibility r = -.42 [a11].
6. **Judge novelty and validity separately; do not trust one LLM critic to weigh them** (G5 / S7). [E] K24: GPT-4 r .13 and GPT-4o r .16 vs human -.39 [d05]; agreement falls on near-equal items [d04]; gaps against humans [d13]. Rank among near-equal candidates by code-side semantic entropy, dedup and coverage rules.
7. **Do not use self-refine as a diversifier** (S5). [S] for the divergence result [b19, c17], consistent with the existing 4b entry on unstructured self-reflection. Treat as "do not add".
8. **Do not add an idle or distraction "incubation" state** (S). [C] incubation g .29 is real in humans, but the unconscious-thought choice effect failed [b05, b08-b10]. No LLM analogue (K10, K25). Keep it out until the context-reset test passes.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Diverge with constraints hidden, then bind-and-check in code, vs one prompt and vs best-of-N at equal tokens | S3 open mode, S4, S7 | [S] | a26, d07, c17 (K04, K18) |
| T2 | Structural k-candidate batch call (verbalized sampling) vs k separate calls | S3 | [S] | d01, d02 (K20) |
| T3 | Code-held ban list of used concepts (denial) plus quality gate vs no history | S3 / M | [S] | b20, b23 (K08) |
| T4 | Breadth/depth rule: force a category switch after m same-cluster candidates; deepen a category that gave valid novelty | O / S3 | [S] | a11-a13 (K02) |
| T5 | Interleaved generate-judge cycles vs one generate then one judge | S3-S4 loop | [S] | a24, a23 (K13, K14) |
| T6 | Show prior candidates in the generate call vs withhold | S3 | [C] | a07, d08, d10 (K16) |
| T7 | Diverge stage on closed verifiable items (ARC, math) vs best-of-N | S3 / G12 | [S] | d11, d02, d14 (K23); G12 says search only with a foothold |
| T8 | Context-reset regeneration as an incubation analogue | S | [C] | b05 (K10) |
| T9 | Non-reasoning model for generate mode vs reasoning model | S3 | [S] | d02, c25 snippet (K22) |
| T10 | Code-side semantic entropy filter vs LLM critic ranking | S7 | [S] | d13, d04 (K17, K24) |
| T11 | More thinking tokens on remote links (by code-measured distance), not near ones | G11 / G12 | [C] | a18, a19 (K15) |

The one possible schema edit is to S3 open mode: split it into two code-switched sub-steps, "diverge with constraints hidden" and "bind". It stays a test (T1) until it wins at equal tokens (SCHEMA rule 8.3).

## 8. Concrete tests on our bench

Both arms always get the same total token budget. Log tokens per state (SCHEMA section 6).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | NoveltyBench-style prompts; open design or story tasks with a rubric; code tasks with tests | A: one plain prompt. B: best-of-N at equal tokens. C: diverge (constraints hidden), then bind-and-check in code | distinct valid outputs per token (Vendi on valid items); pass rate; blind judge from another family | C above A by about 1.3-1.6x distinct valid; vs B small (0 to 1.2x). C must beat B to count |
| T2 | same prompts | A: k separate calls at T 1.0. B: one call asking for k candidates with probabilities | semantic entropy; valid fraction | B ahead by 1.3-2x in diversity; equal quality |
| T3 | tasks where the typical answer is known | A: no ban list. B: code-held ban list, 3 rounds. C: B plus quality gate | novelty = originality x quality | B raises originality 4-10% but quality dips; C keeps net novelty up |
| T4 | open tasks with measurable categories (AUT-like, design) | A: free sampling. B: forced category switch. C: depth inside the best category. D: signal-driven mix | originality of valid ideas; valid ideas per token | D at least equal to B; B above C on broad topics; C above B on narrow or primed topics |
| T5 | open tasks with a checker | A: generate all, then judge. B: 2-3 interleaved cycles with a separate judge call fed only failing output | best valid novel score at equal tokens | B above A by a small margin; none if the judge is noisy |
| T6 | same | A: isolated attempts. B: attempts shown earlier ones with "differ" | semantic entropy; repeated-answer rate | NoveltyBench suggests B above A; human data suggest A above B. Direction unknown |
| T7 | ARC and math items with known plain pass rates | A: best-of-N with code selector. B: diverge-then-converge (different framings, then test all) | pass rate at equal tokens, by plain pass-rate band | B no better than A on easy and hard bands; maybe a gain on the middle band (G12) |
| T8 | as T1 | A: continue same context. B: reset context, restate task, regenerate with earlier answer withheld | distinct valid per token | small gain (human g .29 analogue) or none |
| T9 | open and closed items | A: reasoning model generates. B: non-reasoning model generates; same selector | semantic entropy; valid fraction | unknown; run only if cheap |
| T10 | pools with human or run-based labels | A: LLM critic scalar. B: code-side semantic entropy / dedup / coverage | chosen-vs-best-available regret | B at least equal on near-equal pools |
| T11 | analogy items split by link distance | A: fixed budget. B: more tokens on remote links | accuracy by distance | gain on remote items, none on near |

Use a non-same-family judge or a human sample for open tasks (c09 and c10 used same-family). Length-normalise scores (G5). Log the selector's pick against the best candidate available.

## 9. What does not transfer, and why

- **Type 1 / Type 2 as compute classes.** An LLM has no fast and slow system. Short vs long output is the nearest analogue, and reasoning-trained models show no clean divergence advantage [d02, d12]. The review itself says the labels do not map to generate/evaluate [b01].
- **Neural network labels** (default, control, salience). Loose analogy only [a08]. Small N (28-41), not about LLMs [a22, a23].
- **Incubation and unconscious thought.** A model has no background processing, so "sleeping on it" cannot be run. The only analogue is a context reset or different sampling, untested [b05].
- **Mood and personality** (anger, openness, need for structure) [a14, a15]. No model equivalent beyond prompts or sampling entropy.
- **Fixation by shown examples** (Jansson and Smith 1991; Wadinambiarachchi 2024) [a07, d08]. This is a human memory effect. For an LLM it is a context-design question.
- **Time limits and fatigue.** Barr's presentation time does not map to token budgets without a test [a17, a18].
- **DAT, AUT and RAT scores as proof of useful creativity.** Semantic distance is nearly saturated by frontier models and rewards rare words [c03, b16]. Do not use them as our success metric.
- **LLM judge as final selector of ideas.** Violates G8 and the evidence [d04, d05].
- **Flexibility vs persistence as personality traits.** Transfers only as a code rule, not as a trait.
- **Human help effects** (Kumar et al.) concern people's later behaviour, not the agent [c20].

## 10. Open questions

1. Does a code-set diverge-then-converge pipeline beat a single prompt or best-of-N at equal tokens? No paper controls this (critique gap 1).
2. Does the diverge stage help or hurt on closed tasks (math, ARC)? Only search with an evaluator and many calls [d11], and training-data gains [d02].
3. Is structure better than temperature at equal tokens for 2026 frontier models? Direction mostly closed, size open.
4. Same-family and length bias in LLM creativity critics. Do separate calls for novelty and validity fix the missing trade-off [d05]?
5. Best switching schedule: one cycle or interleaved. Only indirect support [d06, a24].
6. Does showing earlier candidates cause fixation in models? Counter-signal in NoveltyBench [d10].
7. Flexibility vs persistence in LLM search. Does the breadth route give more valid originality? Abstract only [c07].
8. Is there an incubation analogue for LLMs? No source found [d17].
9. Does the Hivemind persist under multi-stage scaffolds? Plain mixing does not help [d03].
10. Are reasoning-trained models worse at divergence than their bases? No paired data [d02, c25].
11. Will the 2026 preprints replicate (ReDNA, 10 scenarios)?
12. Searches for gaps 5, 7, 8 hit rate limits (HTTP 429). Absence of evidence there is not confirmed absence [d17].

## 11. Sources

[V] = opened and read (page or PDF text) in a research session. [V*] = abstract page only. [M] = snippet only.

- [V] Sowden, Pringle and Gabora (2015) The shifting sands of creative thinking. https://arxiv.org/abs/1409.2207 (PDF https://arxiv.org/pdf/1409.2207) [a01-a09, b01-b04, c01, c02]
- [V] Nijstad, De Dreu, Rietzschel and Baas (2010) The dual pathway to creativity model. https://pure.rug.nl/ws/portalfiles/portal/156012256/The_dual_pathway_to_creativity_model_Creative_ideation_as_a_function.pdf [a10-a16]
- [V] Barr (2014) Reasoned connections (Univ. Waterloo thesis). https://uwspace.uwaterloo.ca/handle/10012/8732 [a17-a20]
- [V*] Ellamil, Dobson, Beeman and Christoff (2012) NeuroImage 59(2). https://pubmed.ncbi.nlm.nih.gov/21854855/ [a21]
- [V] EEG idea generation, evolution, evaluation (2021) Sci Rep. https://pmc.ncbi.nlm.nih.gov/articles/PMC7822831/ [a22]
- [V] Dynamic cycles between idea generation and evaluation (2024 preprint). https://www.biorxiv.org/content/10.1101/2024.09.04.611311v1.full [a23]
- [V*] Reflection enhances creativity (2016) Brain and Cognition. https://pubmed.ncbi.nlm.nih.gov/?term=Reflection+enhances+creativity%3A+Beneficial+effects+of+idea+evaluation+on+idea+generation [a24]
- [V*] Jazz improvisation SPM-EEG (2020) NeuroImage. https://pubmed.ncbi.nlm.nih.gov/?term=Dual-process+contributions+to+creativity+in+jazz+improvisations+SPM-EEG [a25]
- [V] Nguyen, Tschiatschek and Singla (2025-26) CreativeDC. https://arxiv.org/abs/2512.23601 ; https://arxiv.org/html/2512.23601 [a26, b24, c15, d07]
- [V] Chavez (2025) Artificial creativity: Generative System 3. https://pmc.ncbi.nlm.nih.gov/articles/PMC12568592/ ; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1654716/full [a27, c08]
- [V] Al Rabeyah et al. (2025) Do LLMs agree on creativity evaluation of alternative uses? https://computationalcreativity.net/iccc25/papers/iccc25-rabeyah2025do.pdf [a28]
- [V] Sen et al. (2026) Automated creativity evaluation of language models. https://arxiv.org/pdf/2606.11762 ; https://www.alphaxiv.org/abs/2606.11762 [a29, d13]
- [V*] Bellemare-Pepin et al. (2024) Divergent creativity in humans and LLMs. https://arxiv.org/abs/2405.13012 ; https://arxiv.org/pdf/2405.13012 [a30, b16-b18]
- [V] Sio and Ormerod (2009) Does incubation enhance problem solving? https://www.Gwern.net/doc/psychology/writing/2009-sio.pdf [b05-b07]
- [V] Nieuwenstein et al. (2015) Unconscious thought advantage replication. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A31405A97BC221C10153E9CF78A94DB6/S1930297500003144a.pdf [b08-b10]
- [V] Benedek et al. (2014) Intelligence, creativity, and cognitive control. https://capacio.com/wp-content/uploads/Benedek-intelligence-creativity-EF-2014.pdf [b11, b12, b26]
- [V] Lee and Therriault (2013) Cognitive underpinnings of creative thought. https://www.Gwern.net/doc/iq/2013-lee.pdf [b13]
- [V] Beaty, Benedek, Silvia and Schacter (2016) Creative cognition and brain network dynamics. https://sites.harvard.edu/schacter-memory/files/2022/08/1-s2.0-s1364661315002545-main.pdf [b14, b15]
- [V] Lu et al. (2025) Benchmarking LM creativity: code generation (Denial Prompting). https://arxiv.org/pdf/2407.09007v2 [b19, b20]
- [V] Padmakumar et al. (2026) Measuring LLM novelty. https://arxiv.org/pdf/2504.09389 [b21-b23]
- [M] Nusbaum and Silvia (2011). https://core.ac.uk/download/149241632.pdf [b27]
- [M] Said-Metwaly et al. (2017) meta-analysis of instructions on divergent thinking (no URL verified) [b28]
- [M] Gerwig et al. (2021). https://www.mdpi.com/2079-3200/9/2/23 (HTTP 403) [b29]
- [V] Chen and Ding (2023) Probing the creativity of LLMs. https://arxiv.org/pdf/2310.11158 [c03-c06]
- [V*] Nath, Dayan and Stevenson (2024) Characterising the creative process. https://arxiv.org/abs/2405.00899 [c07]
- [V] Lu et al. (2024) LLM Discussion. https://arxiv.org/pdf/2405.06373 [c09, c10]
- [V] Peeperkorn et al. (2024) Is temperature the creativity parameter? https://arxiv.org/pdf/2405.00492 [c11, c12]
- [V] TinyTim (2025). https://arxiv.org/html/2508.11607v1 [c13]
- [V] Suzuki and Banaei-Kashani (2025) Universe of Thoughts. https://arxiv.org/html/2511.20471v2 [c14]
- [V] ConDiFi (2025). https://arxiv.org/html/2507.18368 [c16]
- [V] MUTATE and ReDNA (2026). https://arxiv.org/html/2605.28465 [c17]
- [V] Effect of idea elaboration on automatic originality assessment (2026). https://arxiv.org/html/2604.20569 [c18]
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/html/2510.22954 ; https://arxiv.org/pdf/2510.22954 [c19, d03, d04]
- [V] Kumar et al. (2025) Human creativity in the age of LLMs. https://arxiv.org/html/2410.03703 [c20]
- [V] Nair, Gizzi and Sinapov (2024). https://arxiv.org/pdf/2405.01453 [c21]
- [V*] C2-Eval (2025). https://arxiv.org/abs/2510.04009 [c22]
- [M] Helie and Sun (2010). https://ccn.psych.purdue.edu/papers/pp772-helie.pdf [c23]
- [M] Scientific Reports Dec 2025 GenAI vs human on AUT and RAT (title and URL unverified) [c24]
- [M] Brain alignment of creative thought vs chain-of-thought training (2026 preprint). https://arxiv.org/pdf/2604.03480v1 [c25, d16]
- [M] Cross-study alignment of LLM and human originality ratings (2026). https://www.alphaxiv.org/abs/2607.22218.md [c26]
- [M] Beaty et al. (2014) associative and executive processes (cited only) [c27]
- [V] Zhang et al. (2025) Verbalized Sampling. https://arxiv.org/html/2510.01171v1 [d01, d02]
- [V] Zhang et al. (2025) AI delivers creative output but struggles with thinking processes. https://arxiv.org/pdf/2503.23327 [d05]
- [V] Ma and Grandi et al. (2024) Diverse design solutions. https://arxiv.org/pdf/2405.02345 [d06]
- [V] Wadinambiarachchi et al. (2024) Generative AI and design fixation. https://arxiv.org/html/2403.11164v1 [d08]
- [V] Understanding design fixation in generative AI. https://arxiv.org/html/2502.05870v1 [d09]
- [V*] NoveltyBench (2025). https://arxiv.org/abs/2504.05228 [d10]
- [V*] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 [d11]
- [V*] CreativityPrism (2025). https://arxiv.org/abs/2510.20091 [d12]
- [M] GenSelect and best-of-N selectors. https://arxiv.org/abs/2504.16891 [d14]
- [M] NexusAI and Conversational Agents as Catalysts. https://arxiv.org/pdf/2604.10575 [d15]
- [M] Search log, incubation and interleaved schedules in LLMs (no source found) [d17]

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 6 established claims: 5 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A09.02-K08** (now single-source: the sources are not independent). All numbers come from Padmakumar et al. alone (listed twice); Lu et al. only introduced denial prompting and reports no matching result. Numbers do match (OLMo-Instruct, asking-for-novelty and denial prompting pooled).
