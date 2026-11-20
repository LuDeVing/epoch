# Cognitive control and creativity: deep document

*Subfield B01.08. Sources: evidence_a-d.jsonl (ids a01-a25, b01-b25, c01-c28, d01-d18), claims.jsonl (K01-K19), critique.md. Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrails, S states, O operators, memory.*

## 1. What it is

The question: does prefrontal cognitive control help or hurt creative idea generation? The classic "trade-off" says lateral prefrontal control (rules, inhibition, working memory) and default-network free association pull in opposite directions. Strong control suppresses the obvious but also blocks loose associations. Weak control lets associations flow but gives no steering.

Three rival readings are in the literature (b25, a08):

1. **Control blocks creativity** (hypofrontality). Lower prefrontal control helps generation.
2. **Control is a business-as-usual helper.** It helps rule-bound, convergent steps and adds little to open idea lists.
3. **Creativity is general parts combined.** Default, salience and executive networks co-operate. No see-saw.

Current data favour readings 2 and 3 for most tasks. Reading 1 survives in narrow cases: implicit or open generation, novices, and fluency (speed and count) rather than originality.

Why it matters for our agent: the agent has no prefrontal cortex. The nearest analogues are program-side control (checks, monitors, constraint statements) and model-side freedom (loose prompts, temperature, fresh context). The operator O4 (drop a constraint) and the split between a generate state (S3) and a test state (S4) are the places this theory touches the schema. The theory is a design hypothesis. It is not a proven rule (K01 [C]).

## 2. History and theories in depth

**Dietrich 2003, transient hypofrontality (a03, abstract only).** Altered states (dreaming, running, meditation, hypnosis) share temporary prefrontal down-regulation. Lower control frees associative processing. Later applied to flow and improvisation. Evidence is a literature integration with no single effect size.

**Limb and Braun 2008 (cited via b04, c28).** Jazz improvisation showed prefrontal deactivation compared with memorised playing. Seen only second-hand.

**Chrysikou and Thompson-Schill 2011 (a02, abstract only).** fMRI, N = 24. Retrieving a common use of an object recruited lateral prefrontal cortex. Generating an uncommon use recruited occipito-temporal cortex. Closed versus open task flipped the anterior-posterior balance. The two tasks differ in more than control demand, and reverse inference is weak.

**Chrysikou 2013 tDCS (b02, c27, second-hand).** Inhibitory (cathodal) stimulation of left prefrontal cortex sped up and increased creative-use output compared with right-side or sham stimulation. The review gives no numbers.

**Chrysikou, Weber, Thompson-Schill 2014, the matched filter hypothesis (b01, b24, c27).** Control is "a tool adapted to a subset of common challenges". High control suits explicit, rule-based, verbal tasks that fit in working memory. Low control suits implicit, reward-based, non-verbal tasks that exceed working memory. Example: in probability matching, adults pick the 75% option 75% of the time (62.5% expected success). Children pick it 100% of the time (75% expected success). Children also show less functional fixedness. Dopamine follows an inverted U, so "less prefrontal" is not always better. The review says idea evaluation returns to frontal control and that transitions between states are not specified. It is a review without new effect sizes. It is hard to falsify without an independent measure of task type.

**Benedek et al. 2012 (a07, a08).** Frames three positions: inhibition helps, disinhibition helps, adaptive control helps. Their own data supported inhibition helping fluency.

**Beaty et al. 2015 (a05, a06, c26) and Beaty et al. 2016 review (a04, abstract only).** Default and executive networks, usually anti-correlated at rest, couple during idea generation. This is the main challenge to a pure see-saw. The authors argue the usual antagonism may come from externally focused paradigms.

**Weinberger, Green, Chrysikou 2017 (a10) and Lucchiari et al. 2018 (b17).** Reviews of tDCS. Pattern: cathodal left inferior frontotemporal helps idea generation. Anodal left DLPFC or frontopolar helps idea selection. Lucchiari reviewed 18 studies and called results "confusing and inconsistent". They proposed an "on/off" model: relax inhibitory control to generate, engage DMN and DLPFC to select.

**Two-stage view (a15, Zhang 2016).** Generation is bottom-up with diffuse attention. Evaluation is top-down with focus. Same as our draft-then-check split.

**LLM turn, 2023-2026.** Researchers moved the question to models: executive-function batteries on LLMs (c04-c10), brain alignment (c01-c03), temperature as a "hypofrontality dial" (a16, c14), prefrontal-style modular agents (a22, c25), and generate-then-select loops (d01, d02).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Common use recruits lateral PFC; uncommon use recruits occipito-temporal cortex | fMRI N = 24; no further numbers read | Chrysikou and Thompson-Schill 2011 (a02) | [S] abstract only |
| Matched filter: best control level depends on task | Review, no new data. Probability matching 62.5% vs 75% expected success (adults vs children) | Chrysikou et al. 2014 (b01) | [C] theory, untested at scale |
| Left PFC inhibition speeds and increases creative-use output | Cathodal left vs right or sham; no numbers in review | Chrysikou 2013 via b02 | [S] no preregistered replication |
| Same-lab extension: left ventrolateral PFC inhibition raises fluency, not originality | 246 participants, 4 experiments, 12 montages | Chrysikou et al. 2021 (d06) | [S] fluency yes, originality no |
| DMN and executive coupling during idea generation | N = 25; global efficiency vs creativity r = .44, p = .02; resting check n = 42; rater alpha .87 | Beaty 2015 (a05, c26) | [E] with ALE meta (b18) |
| ALE meta: creative tasks overlap with semantic and control regions | 787 experiments, 10,357 foci, 17,228 adults | Chan et al. 2026 (b18) | [E] abstract only |
| Inhibition predicts fluency and flexibility; intelligence predicts originality | N = 104; inhibition to flexibility .55; intelligence to originality .51; mediation .23, CI .04-.42 | Benedek 2012 (a07) | [C] |
| Inhibition predicts AUT originality, not fluency or flexibility | Exp 1 N = 55: originality b = 1.77, p = .013, R2 = .16; fluency p = .908. Exp 2 N = 49: flanker RT cost explained 56% of CRAT variance and 52% of originality | 2026 flanker study (b14, b15) | [C] unusually high R2 for N about 50 |
| Divergent thinkers switch attention faster; real achievement shows no such effect | Two ERP studies; sample sizes not read | Zabelina 2018 (a09) | [S] abstract only |
| Working memory vs creativity is weak | k = 28, n = 3104, r = .083, CI .050-.115, I2 = 55%; Egger p = .350 | Gong 2023 (b05, b06) | [E] |
| Culture moderates WM-creativity link | Asian r = .126 vs Western r = .061, Q = 4.26, p = .039; age ns | Gong 2023 (b07) | [S] small k |
| Memory and creativity meta | 79 studies, 525 effects, N = 12,846; r = .19; semantic .25, WM .17, episodic .16, short-term .15; Egger p = .76 | Gerver 2023 (d03, b08) | [E] |
| Rosen: anodal right DLPFC helps novices, hurts experts | 17 pianists, 102 rated improvisations; interaction -0.24, SE 0.08, p = .002 (fitted term); omnibus chi2(4) = 9.84, p = .043; least experienced +0.91 (p = .004), most experienced -0.54 (p = .007) | Rosen 2016 (a11, b03) | [S] no replication |
| Rated creativity, aesthetics and technique are nearly one score | r(100) = .96, .91, .93 | Rosen 2016 (a25) | [S] |
| Khalil: left-cathodal right-anodal IFG raises AUT originality, only when inhibition also improved | N = 19 vs 21; originality F(1,35) = 5.47, p = .025, partial eta2 = .135; flexibility p = .062 | Khalil 2020 (a13) | [S] mediation failed |
| Mindset and inhibition moderate IFG effects; originality unaffected | N = 40; b = 0.477, p = .034 (high mindset, left IFG) | Khalil 2023 (b12, d08) | [S] |
| Pena: tDCS and tRNS mostly null | N = 66; picture completion F = 3.35, p = .042; tRNS vs sham p = .004; unusual uses F = 0.61, p = .546; Stroop p = .711; side effects tDCS M 2.18 vs sham 1.29 | Pena 2022 (b10, b11) | [S] weak blinding |
| Anodal left lateral frontal helps | Divergent d = .540, CI [.00004, 1.08], p = .0498; convergent d = .401, CI [.026, .776]; 20 creativity studies, 591 effect sizes in all; visual funnel check only | Chan et al. 2025 preprint (d05) | [C] CI touches zero |
| tDCS meta-analysis: anodal helps convergent, not divergent overall; left IFG anodal hurts | 32 studies, 125 effects, 1,538 participants; no g values seen | Chen 2024 (b09, d04) | [C] abstract only |
| COMT x DAT dopamine genes: best control is non-monotonic | N = 100; ATTA F(2,67) = 4.28, p = .02; achievement F(2,69) = 4.21 | Zabelina 2016 (b16) | [S] candidate-gene design |
| LLM executive control is weak | WCST accuracy 0.29-0.53 vs 0.77 human; perseverative 0.20-0.33 vs 0.12; Flanker incongruent 40-60% vs 93-96%; WCST falls with dialogue length r -0.28 to -0.51 | de Langis 2025 (c04, c05) | [E] 4 sources |
| Stroop collapse with list length | GPT-4o 91% at 5 words, 1% at 20 and 40; Claude 3.5 Sonnet 10% at 40 | Patel et al. 2026 (c09) | [S] press report |
| Squared conflict breaks VLMs | 108 VLMs; congruency t = 17.88, 16.85, 8.99; below chance on fully incongruent squared tasks | Machine Psychophysics 2025 (c10) | [S] |
| Chain of thought plus text lifts WCST | Categories 0.02 to 1.00 (Claude-3.5), 0.08 to 0.96 (Gemini-1.5), 0.06 to 0.92 (GPT-4o); humans 4.73 of 5; dropping rule exclusivity: Gemini 4.8 to 2.6 | Visual-LLM WCST 2025 (c07, c08) | [C] conflicts with c06 |
| Reasoning mode helps Flanker, not WCST | Llama-3.1-8B 0.471 to 0.910; Qwen2-32B 0.638 to 0.985 | de Langis 2025 (c06) | [C] |
| Larger LLMs align more with DMN on the creative task only | r = .55 (CI .24-.77) vs control task r = .09 (p = .66); 24 models; DMN-AUT score r = .52; FPN r = .46, corrected p = .079; Gemma-3 within-family r = .90 | Ismayilzada 2026 (c01, c02) | [S] correlational |
| Temperature is a weak creativity dial | Llama 2-Chat 70B; 31 rated stories, 36 raters; novelty slope .308 (SE .138); coherence slope .240 (SE .122); alpha .639 | Peeperkorn 2024 (a16, c17) | [E] with b22, d01 |
| GPT-4 DAT rises with temperature | 85.6 at T = 1.5, above 72% of humans; n = 500 per temperature; top-decile humans above all models | Bellemare-Pepin 2025 (a18, c13, c14) | [E] with c16, b22 |
| LLMs are homogeneous | 22 LLMs vs 102 humans; T = 2.0 gibberish. Top-10 words = 25.5% of tokens | Wenger 2026 (b22); Schapiro 2026 (a21) | [E] |
| Weight steering raises DAT, costs MMLU | Up to +14 human percentiles; human eval N = 720; top-10 share -10.2 points; entropy +0.59 nats; MMLU -3.13 pp, protected masks a further -0.71 pp | CreativityNeuro (a20, a21, c22, d17) | [S] six open models, 3B-14B |
| Modular planner with Monitor | Tower of Hanoi 3-disk about 7x zero-shot; no Monitor: 31% invalid moves vs 0%; PlanBench Mystery BW 27.4 vs CoT 10.6 | Webb, Mondal, Momennejad 2025 (a22, c25) | [S] closed tasks, GPT-4 |
| Goal-free diverge call then constrained select call | GPT-5.4: paths 27/56 (48.2%) to 38/56 (67.9%); AUT originality 2.91 to 3.77 | MUTATE and ReDNA 2026 (d02) | [S] not equal tokens |
| Selector design drives generate-then-select outcome | Creativity 3.921/3.835/3.927 at 5/15/30 iterations; smaller selector beat larger | Anderson et al. 2026 (d01) | [S] pilot, LLM judges |
| Reasoning training narrows output | Think-SFT loses 62% of base diversity; no-CoT at inference does not restore it; 28 LLMs: human continuations 2-4x higher entropy | d10, d11 | [C] vs d12 |
| Prompted CoT reduces fixation | Slope 1.023 to 1.354 (p < .001); humans no change (p = .70); unique combinations 85 to 152 | d12 | [S] model-dependent |
| Random context raises novelty or category spread | 4 open models, 6 objects; flexibility gain 10.117 vs 3.889 | d13 | [S] LLM-judged |

## 4. Mechanisms and models

Each model is written so an engineer can wire it into the scaffold.

**4.1 Matched filter (task decides control level).** Inputs: task features. Output: a constraint level per step.
- Closed step (rule, verification, one exact answer): high control. Tight instructions, explicit rules, code checks.
- Open step (idea generation, no single right answer): low control. Fewer stated constraints, a named strategy, fresh context.
- Store one control level per step type. Do not hold one global dial. The dopamine inverted U (b24, b16) says too much or too little both hurt, so the level must be tuned, not pushed to an extreme.

**4.2 Two-phase loop (generate loose, select strict).** Support: a15, b17, a10, b02, c22, d02.
1. Call A (generate): show the bare task. Optionally hide goal and failure context (ReDNA, d02). Ask for N distinct candidates. No evaluation, no ranking.
2. Code: de-duplicate, tag by category, drop repeats of earlier attempts.
3. Call B or code (select): reintroduce constraints and checks. Run checks where possible (G8). If a model must judge, it sees no authorship and no majority (G5).
4. Selector quality is the outcome variable (d01): a selector that rewards the wrong thing reduces novelty, and a bigger selector was not better.

**4.3 Co-operation, not see-saw.** Beaty 2015 (a05): early in a task default regions couple with salience regions. Later they couple with executive regions. Machine reading: control joins late as a steering and evaluation function. It does not have to be absent at the start. A loop where drafts are evaluated by a program, not by a free model call, matches this.

**4.4 Expertise gating (Rosen).** Hypothesis: imposed structure helps those whose associative knowledge is not automatic, and can hurt those whose routines are strong (a11, a12). Machine reading: the scaffold level depends on the class pass rate (S0). Low pass rate: more structure. High pass rate: less. Single source, so test only (K06).

**4.5 Conflict monitor (MAP).** A separate call, or code, checks each proposed step against the rules and returns pass or fail with the violated rule. Removing it raised invalid moves from 0% to 31% (c25). It checks. It does not create. Suited to closed, rule-bound steps, which the matched filter says need control.

**4.6 Set-shift trigger.** LLMs perseverate (WCST perseverative 0.20-0.33 vs 0.12 human, c05) and get worse with dialogue length (r -0.28 to -0.51). Fix: code detects the same wrong answer or rule twice, then forces a rule restatement in a fresh context. A chain-of-thought prompt with an explicit, exclusive rule set lifted WCST from about 0.02-0.08 to 0.92-1.00 (c07, c08). Without told exclusivity it dropped (c08).

**4.7 Sampling temperature as hypofrontality dial.** Higher temperature widens wording and the chance of an early novel hit. It does not widen the idea range much (a17: weak negative trend in cosine similarity). It breaks coherence at T = 2.0 (b22). On a single-word DAT it helps (a18). Use only with a filter, and expect little.

**4.8 Path style tracker.** Humans reach high originality by deep search or broad jumping. LLMs score higher on the flexible path (c18). Code can count jumps between semantic categories and push a flexible path if jumps are low. Temperature did not change the path (c19), so change the frame, not the sampling.

**4.9 Brain alignment (c01-c03).** Alignment with DMN responses is clearer while the model reads the prompt, and fades during response generation (DMN minus somatomotor +0.15 at prompt stage, 18 of 23 models, p = .002). Weak reading: the framing step matters more than the output step. Background only (K13 [S]).

## 5. What holds up

**Holds up.**
- Working memory capacity has a small link to creativity: r = .083 (k = 28) in the WM-specific meta, and r = .17 for working memory inside the 79-study memory meta (r = .19 overall, no small-study bias). Semantic memory is stronger (r = .25). [E] (K02)
- Default and executive networks co-operate during creative generation. Small fMRI plus a 787-experiment ALE meta. [E] (K03)
- LLM sampling temperature is not a creativity dial. Weak novelty gain, real coherence cost. Three or more sources. [E] (K07)
- LLMs are homogeneous in open-ended output. [E]
- LLMs have weak executive control on classic tasks (WCST, Flanker, Stroop). [E] (K10)
- GPT-class models match or beat the average human on the DAT, and the top human decile stays above them. [E] (K08)

**Contested.**
- Does less prefrontal control help? Matched filter, Chrysikou 2013 and Khalil 2020 say yes in narrow cases. The 2026 flanker study, Benedek 2012 and the Chan 2025 meta (anodal left frontal helps, divergent d = .54, CI touching zero) say control helps. The 2024 tDCS meta found convergent gain, no divergent gain, and a loss for left IFG anodal. [C] (K01, K04, K05)
- Reasoning and originality in LLMs. Trained reasoning narrows output (d10, d11, c03). Prompted CoT reduced fixation (d12). Different things, so the evidence conflicts only on the surface. [C] (K11, K17)

**Failures and weak spots.**
- Chrysikou 2021 (d06) reproduced the fluency gain from left ventrolateral inhibition but not an originality gain. Same lab. No preregistered replication of Chrysikou 2011 or 2013 exists (d18).
- Rosen 2016 has no replication in two searches (d07). N = 17. Ratings of creativity, aesthetics and technique correlate .91-.96, so the effect may be about general quality.
- Khalil 2020 tested inhibition as a mediator and it failed. Originality moved only when inhibition also moved.
- Pena 2022 (N = 66, sham-controlled): mostly null. Stroop flexibility did not change. Side effects broke blinding.
- A larger, cleaner picture on stimulation is missing. Chen 2024 effect sizes and bias tests were not seen (abstract only).
- No study found links LLM Flanker or WCST scores to originality across models (K19). CreativityPrism (d15) shows one creativity skill rarely carries to another.

**Moderators.** Task type (open vs closed), expertise (Rosen), baseline inhibition (Khalil), mindset (Khalil 2023), dopamine genotype (Zabelina 2016), culture (Gong 2023, Q = 4.26), stimulation site and polarity (Weinberger 2017). Age: no WM-creativity effect (Q = 1.822, p = .177). In a very small fMRI study (15 children vs 16 adults) children used less control with similar scores (b23).

**Interventions that worked (human).** Cathodal left PFC for fluency. Anodal left DLPFC for selection and, in the preprint meta, for both thinking types. Right-anodal left-cathodal IFG for AUT originality (one study).
**Did not work or mixed.** Anodal right DLPFC as a general boost. Left IFG anodal (meta: lower). tDCS on unusual uses (Pena). WM training claims are covered in another subfield.

**LLM interventions that worked.** CoT plus text input with exclusive rules on WCST. Reasoning mode on Flanker. Monitor module in planning. Goal-free diverge then constrained select (d02). Named strategy prompts on DAT (c15: etymology beat plain prompt for GPT-3.5 and GPT-4). Chain of Verification kept divergence while reducing hallucination (d14). Random or unrelated context raised judged novelty (d13, LLM-judged).
**Did not work.** Temperature as a creativity dial. More generate-select iterations (d01). Repetition penalty (c19). Switching off CoT at inference to restore diversity (d10). Role-played impairments are not a real mechanism (c08).

## 6. Language models

**Executive-function batteries.**
- Six instruction-tuned open models (Gemma-2, Llama-3.1, Qwen2, 30 prompt variants each) beat human norms on working memory (backward digit span length 15: 0.00-0.83) but are weak on control (c04). Parameter count vs span r = .82. Working memory did not predict executive scores.
- WCST 0.29-0.53 vs 0.77 human (3,060 trials per model). Flanker incongruent 40-60% vs 93-96%. Longer dialogue lowers WCST (c05).
- Reasoning models: Flanker incongruent up to 0.910 and 0.985. WCST no better, and thought strings often ran past 30,000 tokens (c06).
- Frontier models with CoT and text input reach human WCST level, with no significance tests (c07). The conflict with c06 comes from prompt format (text vs visual, explicit exclusivity) and model.
- Stroop: GPT-4o 91% at 5 words and 1% at 20 and 40 words (c09, press report). 108 VLMs break on squared conflict (c10). A GPT-4o battery summary (c11) and ExProf-Bench (c12) were snippets only.
- Reading: memory is cheap and control is scarce. The scaffold must supply the control from outside.

**Creative output.**
- DAT: GPT-4 at T = 1.5 scored 85.6, above 72% of humans. Chen and Ding 2023 reported greedy GPT-4 above 96% of humans (c16, abstract only). Bellemare-Pepin found weaker ranks with other prompts. Top-decile humans stay above all models through June 2025 releases. GPT-4-turbo used "ocean" in over 90% of sets (c13).
- Wenger 2026: 22 LLMs more alike than 102 humans, with originality similar or slightly higher on AUT and DAT, lower on forward flow (b22).
- Huang 2026 review: LLM advantage Hedges' g = 0.52 to 2.61 on divergent tests, humans win at the peak. Human variables (WM, openness) map inconsistently onto LLMs (b20).
- Creative-process style: 8 LLMs, 440 sequences, flexible-path outputs scored higher (p < .01). Humans showed no difference. Test-retest jump count r = .42 humans vs .22 LLMs (c18).

**What changed output, and by how much.**

| Change | Effect | Source |
|---|---|---|
| Temperature up (Llama 2-70B stories) | Novelty slope .308, coherence cost .240 | a16 |
| Temperature up (GPT-4 DAT) | to 85.6 at T = 1.5 | a18 |
| Strategy prompt (DAT) | etymology beat plain for GPT-3.5 and GPT-4, effect size not read | c15 |
| Weight steering (CreativityNeuro) | up to +14 human percentiles on DAT; MMLU -3.13 pp. Prompting alone about the 88th percentile | a20, c20, c22 |
| Activation steering | matched on DAT, did not transfer to AUT or Task Task | a20 |
| Goal-free diverge then constrained select (GPT-5.4) | AUT originality +0.86; paths 48.2% to 67.9% | d02 |
| More generate-select iterations | no gain | d01 |
| Prompted CoT in ideation | fixation slope 1.023 to 1.354; in a second model run it narrowed first-idea diversity (7.11 vs 9.14) | d12 |
| Reasoning post-training | Think-SFT loses 62% diversity; 28 LLMs show wider gap to human entropy | d10, d11 |
| Reasoning-distilled Llama 8B | negative alignment with high-creativity brain responses (not in Qwen) | c03 |
| Random or unrelated context | judged novelty and category spread up (metric-specific) | d13 |
| Chain of Verification | raised divergent creativity; DoLa lowered it; RAG minimal | d14 |
| Modular planner with Monitor | invalid moves 0% vs 31% without | c25 |

**Caveats.** All of the creativity numbers use LLM judges or embedding scores, except CreativityNeuro (human N = 720) and Peeperkorn (36 raters). No study varies a control-like variable at equal tokens (gap 1 only partly closed). The generate-select results use extra calls. Open 3B-14B models dominate the steering work. Brain-alignment is correlational and confounded with size. LLM self-judgment is poor: Llama3-8B rates its own stories near 7 of 9 (c23).

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Do not use sampling temperature as the way to relax constraints. Use it only with a filter and expect a small gain. Keep T below the coherence break. | O4, S3 | [E] | a16, a17, c17, b22, d01 |
| A2 | Control (checks, monitors) belongs on closed, rule-bound steps. Do not spend extra control tokens on open idea lists. | S0, S4 | [E] (human: control predicts convergent more than divergent; agent: Monitor) | b14, b15, d03, b05, c25 |
| A3 | Supply control from outside the model: code detects repeats, perseveration and rule violations. The model does not police itself. | G2, S4, S6 | [E] | c04, c05, c10, c09 |
| A4 | Keep a controlled evaluation step after any loose generation (the creative cycle includes control). Do not build a separate creativity module. | S3, S4, S7 | [E] on co-operation, [S] on the loop gain | a05, c26, b18, a15 |
| A5 | Samples from one model are not independent. Do not expect more samples to widen ideas. Use frames and history, and a banned-answer list. This confirms G4. | G4, S3 | [E] | a21, b22, c24, c13 |
| A6 | Keep an external, code-side scorer for novelty. Self-judging by small models is poor. | G8 | [E] | c23, b20 |
| A7 | Reset context between failed tries on set-shifting problems. Dialogue length hurt WCST (r -0.28 to -0.51). | S5, S6 | [E] | c05 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Goal-free diverge call, then constrained select call, versus single call at equal tokens | O4, S3/S4 | [S] | d02, d01, K15 |
| T2 | Selector strictness and size in the select step; score novelty and correctness separately | S7 | [S] | d01, K16 |
| T3 | Relaxation by dropping one stated constraint (O4) on open items vs tight prompt; matched-filter crossover on closed items | O4 | [C] | a01, b01, K01 |
| T4 | Make the relaxation depend on class pass rate (novice-like vs expert-like) | S0, O4 | [S] | a11, b03, K06 |
| T5 | Explicit rule restatement plus exclusive-rule CoT on rule-switching tasks; code-triggered set shift | S6, G1 | [C] | c07, c08, c06 |
| T6 | Named search strategy chosen by code (etymology, opposites) in generate | O4, S3 | [S] | c15 |
| T7 | A path-style tracker: count jumps between categories, force flexible path if low | S3 | [S] | c18, c19 |
| T8 | One off-topic seed in the generate pass only | O4 | [S] | d13 |
| T9 | Reasoning-mode model vs instruct sibling on open items; do not rely on a no-think switch | G11, O4 | [C] | d10, d11, d12 |
| T10 | Conflict monitor ablation on planning-type items | S4 | [S] | c25 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup cost counted, G7). Report novelty and correctness separately. Use blind scoring with code where possible.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | Open items (AUT-style uses, NoveltyBench prompts) and a closed control set | Single-call "be creative and correct" vs two-call (loose generate, strict select), same total tokens | Unique-answer rate, distinctness by embedding, plus correctness on the closed set | Gain on open items about the size seen in d02 (ReDNA); no loss on closed items. If the gain vanishes at equal tokens, drop |
| B2 (T3) | Matched-filter crossover: closed items (rule puzzles with checks) and open items | Tight-constraint vs relaxed-constraint prompt on each | Pass rate on closed; unique-answer rate on open | Tight wins closed, relaxed wins open. A crossover supports O4. No crossover: O4 stays unproven |
| B3 (T2) | Generate-then-select on open items | Select strictness: lenient, strict, size-reduced | Novelty of chosen idea vs correctness | d01 predicts selector design moves the result more than iteration count |
| B4 (T5) | Rule-switching (WCST-like text) and ARC-like rule changes | Plain vs exclusive-rule CoT vs code-triggered restatement | Perseverative error rate, categories completed | Large gain where baseline is low (0.02 to 0.9 in c07). Check on our own models |
| B5 (T4) | Problem classes grouped by plain pass rate | Same relaxation on low-pass and high-pass classes | Gain or loss by group | Rosen predicts gain on low-pass, loss on high-pass. Single source, so expect a null |
| B6 (T6/T7) | Open items | Code-picked strategy or forced flexible path vs plain | Unique-answer rate, category count | Small to medium gain |
| B7 (T8) | Open items plus relevance rating | One random seed in generate vs none | Novelty (blind judge) and relevance | Novelty up, relevance down. Net must be positive at equal tokens |
| B8 (T9) | Open items | Reasoning model vs instruct sibling at equal tokens | Unique-answer rate | Reasoning model narrower (d10, d11) |
| B9 | Temperature check | T up vs structured relaxation at equal tokens | Novelty and coherence | Structured relaxation beats temperature (K07) |
| B10 (T10) | Planning/closed items | With vs without monitor call | Invalid moves, pass rate | Fewer invalid moves; tokens cost counted |

## 9. What does not transfer, and why

- **tDCS results.** They change human neural excitability. Nothing in an LLM is excitable in that sense. The site, polarity and expertise effects have no direct mapping. Only the task-dependence idea carries over.
- **Prefrontal "control" as a single resource.** In an LLM, "control" is a bundle of choices: prompt strictness, checks, sampling, context length. Each must be tested on its own. Control tasks in LLMs split too (c11, c12: separable dimensions).
- **Working memory.** WM predicts creativity at r = .08-.17 in humans. LLM memory is already strong (c04) and did not predict executive scores. More context will not buy originality.
- **Brain alignment (c01-c03).** Correlational across model size. Models have no prefrontal system. It gives no knob.
- **CreativityNeuro and activation steering.** Weight edits are not available to a scaffold-only agent (K09). The entanglement finding (MMLU cost) is useful as an argument for stage separation, not as a method.
- **Expertise-by-stimulation (Rosen).** N = 17, no replication. An agent's "expertise" is a measured class pass rate. Link is a design guess.
- **Flow and hypofrontality on running, meditation, dreaming.** No analogue in a token generator.
- **Incubation and sleep.** Not supported in the schema anyway (section 4b).
- **Culture and age moderators.** Not relevant to an agent.
- **Human DAT and AUT norms.** DAT measures word distance, not useful creativity (c13). Do not use it as the bench metric alone.

## 10. Open questions

1. Is there any equal-token test of loose generate then strict select against a single pass? (Gaps 1 and 7 partly closed.)
2. What are Chen 2024's effect sizes and bias tests? Does Chan 2025 survive Egger and trim-and-fill? Divergent CI touches zero.
3. Does the Rosen expertise interaction replicate in any domain, and does it map onto agent familiarity?
4. Is there a preregistered replication of Chrysikou 2011 or 2013? Only the same lab's 2021 extension exists; originality was not reproduced.
5. Do LLM scores on Flanker, WCST and Stroop correlate with AUT or DAT originality across models? No study found (K19).
6. Do reasoning-trained models lose originality at equal tokens relative to their instruct siblings, outside the Olmo 3 family?
7. Does CreativityNeuro replicate on larger or closed models, and what is the cost on correctness tasks beyond MMLU?
8. Does leaky attention (Zabelina) in LLMs, meaning distractor material in context, give better creativity without a correctness cost?
9. Do selector rewards (what the select step optimises) matter more than selector size, and how should a code selector score novelty?
10. Do the Stroop collapse numbers (c09, press only) hold in the full paper and for newer models?
11. Is path style (deep vs flexible) a stable per-model trait that code can read and steer?

## 11. Sources

[V] = opened and read (page or PDF text). [M] = snippet, abstract, or second-hand only.

| Source | Mark | URL |
|---|---|---|
| Chrysikou, Weber, Thompson-Schill 2014, matched filter (a01 [M] in first pass, b01/b02/b24/c27/c28 [V], first 100k of 233k characters) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC4010565/ |
| Chrysikou and Thompson-Schill 2011, common and creative object use (a02) | [M] | https://pmc.ncbi.nlm.nih.gov/articles/PMC3846690/ |
| Dietrich 2003, transient hypofrontality (a03) | [M] | https://doi.org/10.1016/s1053-8100(02)00046-6 |
| Beaty, Benedek, Silvia, Schacter 2016, Trends Cogn Sci (a04) | [M] | https://pmc.ncbi.nlm.nih.gov/articles/PMC4724474/ |
| Beaty et al. 2015, Sci Rep (a05, a06, c26) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC4472024/ |
| Benedek et al. 2012 (a07, a08) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC3387381/ |
| Zabelina et al. 2018 ERP (a09) | [M] | https://doi.org/10.1016/j.neuropsychologia.2018.02.014 |
| Weinberger, Green, Chrysikou 2017 tDCS review (a10, a24) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC5432551/ |
| Rosen et al. 2016 jazz tDCS (a11, a12, a25, b03, b04) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC5110534/ |
| Khalil et al. 2020 IFG tDCS (a13) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC7321900/ |
| Khalil et al. 2023 mindset and inhibition (b12, b13, d08) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC10731982 |
| Zhang et al. 2016 lingual gyrus (a14, a15) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC5047031/ |
| Peeperkorn et al. 2024 temperature (a16, a17, c17) | [V] | https://arxiv.org/abs/2405.00492 |
| Bellemare-Pepin et al. 2024/2025 divergent creativity (a18, a19, c13-c15) | [V] | https://arxiv.org/pdf/2405.13012 |
| Schapiro et al. 2026 CreativityNeuro (a20, a21, c20-c22, d17) | [V] | https://arxiv.org/abs/2607.01433 |
| Mondal, Webb, Momennejad 2025 MAP planner (a22, a23, c25) | [V] | https://arxiv.org/abs/2310.00194 |
| Gong et al. 2023 WM meta-analysis (b05-b07) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC9861316 |
| Gerver et al. 2023 memory meta-analysis (b08, d03) | [V] | https://link.springer.com/article/10.3758/s13423-023-02303-4 |
| Chen et al. 2024 tDCS meta-analysis (b09, d04) | [M] | https://doi.org/10.1037/aca0000704 |
| Pena et al. 2022 tDCS vs tRNS (b10, b11) | [V] | https://www.frontiersin.org/articles/10.3389/fnhum.2022.997445/pdf |
| 2026 flanker and WCST study, Lancashire (b14, b15) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC13270686 |
| Zabelina et al. 2016 COMT x DAT (b16) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC4718590 |
| Lucchiari, Sala, Vanutelli 2018 (b17) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC6082949 |
| Chan, Lambon Ralph, Robinson 2026 ALE (b18) | [M] abstract | https://doi.org/10.1016/j.cortex.2026.06.022 |
| Barnett et al. 2025 flow review (b19) | [V] partial | https://pmc.ncbi.nlm.nih.gov/articles/PMC12827708 |
| Huang, Liu, Yang 2026 review (b20, b21) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC13608707 |
| Wenger et al. 2026 homogeneously creative (b22) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC13010328 |
| Horowitz-Kraus et al. 2026 children and ChatGPT (b23) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC13641069 |
| Ismayilzada et al. 2026 LLM-brain alignment (c01-c03) | [V] | https://arxiv.org/abs/2604.03480 |
| de Langis et al. 2025 Strong Memory, Weak Control (c04-c06) | [V] | https://arxiv.org/html/2504.02789v2 |
| Visual LLMs WCST 2025 (c07, c08) | [V] | https://arxiv.org/html/2505.22112v1 |
| Patel, Wang, Fan 2026 via press report (c09) | [V] press page; paper not opened | https://www.psypost.org/advanced-ai-models-suffer-a-near-total-collapse-on-classic-psychology-test-as-cognitive-demands-increase/ |
| Machine Psychophysics 2025 (c10) | [V] | https://ar5iv.labs.arxiv.org/html/2505.18969 |
| GPT-4o executive-function preprint (c11) | [M] | https://tyzhang98.github.io/zhang/files/Cognitive-Science.pdf |
| ExProf-Bench (c12) | [M] | https://gh.r-mj.com/gedp/ExProf-Bench-Results |
| Chen and Ding 2023 divergent semantic association (c16) | [M] | https://arxiv.org/abs/2310.11158v1 |
| Nath, Dayan, Stevenson 2024 creative process (c18, c19) | [V] | https://arxiv.org/html/2405.00899 |
| Olson et al. 2024 steering to evaluate creativity (c23) | [V] | https://arxiv.org/html/2412.06060v1 |
| Jiang et al. 2025 Artificial Hivemind (c24) | [V] abstract page | https://arxiv.org/abs/2510.22954 |
| Anderson, Verhoef, Zohrehvand 2026 Recipes for Creativity (d01) | [V] | https://arxiv.org/abs/2608.07243 |
| MUTATE and ReDNA 2026 (d02) | [V] | https://arxiv.org/abs/2605.28465 |
| Chan, Cho, Lambon Ralph, Robinson 2025 tDCS meta preprint (d05) | [V] | https://www.biorxiv.org/content/10.1101/2025.03.18.644047 |
| Chrysikou et al. 2021 Sci Rep (d06, d18) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC8065129 |
| Luyten and van der Schaar 2026 reasoning-creativity (d09) | [V] skimmed | https://arxiv.org/abs/2601.00747 |
| Olmo 3 diversity collapse 2026 (d10) | [V] | https://arxiv.org/abs/2604.16027 |
| LLMs lower uncertainty in creative writing 2026 (d11) | [V] | https://arxiv.org/abs/2602.16162 |
| Cognitive framework for idea diversity 2026 (d12) | [V] | https://arxiv.org/abs/2602.20408 |
| Wong et al. 2026 context injection, ICCC26 (d13) | [V] | https://computationalcreativity.net/iccc26/papers/ICCC26_paper_171.pdf |
| Does less hallucination mean less creativity 2025 (d14) | [M] abstract | https://arxiv.org/abs/2512.11509 |
| CreativityPrism 2025 (d15) | [M] abstract | https://arxiv.org/abs/2510.20091 |
| Executive-function vs creativity search (d16) | [M] | https://arxiv.org/abs/2504.02789 |

Note on opened flags: critique.md says top-10 numbers (Beaty 2015, Benedek 2012, Zhang 2016, Pena 2022, de Langis 2025, Ismayilzada 2026, the WCST-vision paper) were read by earlier agents and not re-opened in cross-check. Treat them as agent-read. Peeperkorn: 31 rated stories (5 per temperature), 36 raters; 100 stories per temperature were generated for the diversity analysis only. Rosen p = .043 is the omnibus model comparison; p = .002 is the fitted interaction term. Gerver 2023 (79 studies) is memory in general, not a pure WM-creativity paper.
