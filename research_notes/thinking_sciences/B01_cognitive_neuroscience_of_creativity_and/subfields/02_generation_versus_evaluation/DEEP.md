# Generation versus evaluation: deep document

*Subfield B01.02, cognitive neuroscience of creativity and insight. Built from evidence_a-d.jsonl (a01-a27, b01-b29, c01-c27, d01-d24), claims.jsonl (K01-K29) and critique.md in this folder. No new search was done for this write-up. Evidence ids in brackets point to the jsonl lines. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested.*

## 1. What it is

The idea: producing ideas and judging ideas are different jobs. In people they lean on different brain configurations. The founding study is Ellamil, Dobson, Beeman and Christoff (2012). Art students designed book-cover illustrations in an fMRI scanner on a drawing tablet. They switched between a generation phase and an evaluation phase. Generation recruited medial temporal lobe regions. Evaluation recruited executive and default regions together, plus rostrolateral prefrontal cortex, insula and temporopolar cortex. Default and executive regions were positively coupled throughout. [a01, b01, c01, d19]

Why this matters for our agent: the schema keeps generation and judgement in separate calls (G5, G8, S3 versus S4/S7). The human literature is the motivation for that split. It is not a test of it. No study asks whether an LLM does better with a separate judge call than with one call that does both, at equal tokens (b29, critique gap 1). That is the central unknown of this subfield.

Three questions sit under the topic.

1. **Brain question.** Are there separate systems for generating and for evaluating? Partly. They are coupled, not isolated (K01, K02).
2. **Behaviour question.** Does mixing the two modes in time hurt output? Mixed. Early judging may drop promising ideas, but a short review mid-way helped in one EEG study (K19, K24).
3. **Engineering question.** In an LLM pipeline, how good is the judge, who should judge, and what should select? Prompt-only model judges of unexecuted ideas are near chance. Code checks, outcome-trained judges and real execution do better (K07, K08, K11, K22).

The real value of this subfield for the agent is on the third question. The brain data gives a design rationale. The LLM data gives the rules.

## 2. History and theories in depth

**Blind variation and selective retention (BVSR).** Campbell (1960); Simonton (1999 to 2012). Ideas come from blind variation and are then kept or dropped by selection. "Blind" means the creator has no inner certainty which variant leads to the goal. Sowden et al. note that BVSR assumes successive ideas are unrelated, which the serial-order data contradict (later ideas build on earlier ones). [a10] This is the oldest generate/select split. It is the direct ancestor of "sample many, pick one".

**Geneplore.** Finke, Ward and Smith (1992). A generate phase retrieves items, associates and builds "pre-inventive structures". An explore phase finds attributes of those structures and tests possible uses. The two phases cycle. [a09] Geneplore treats exploring as interpretation, not only accept/reject. For an agent, the explore phase is closer to S4 TEST plus S5 REVISE than to a final judge.

**Ideation-evaluation cycles.** Basadur (1982, 1995). Creative work has problem finding, problem solving and implementation. Ideation and evaluation alternate inside each stage in different ratios. Problem finding is mostly ideation. Implementation is mostly evaluation. [a11] This says the split is a ratio that moves, not a switch.

**Dual process links.** Sowden, Pringle and Gabora (2015) review how generate/evaluate maps onto Type 1 / Type 2 thinking. The mapping is loose. Generation is not simply "fast and intuitive" and evaluation is not simply "slow and analytic". [a08] This is a warning against turning the split into a "fast model call / slow model call" rule.

**Default network and self-generated thought.** Andrews-Hanna, Smallwood and Spreng (2014): the frontoparietal control network interacts with default and dorsal attention networks when a task needs maintenance and extended evaluation of internal information. [a25] This is the general account in which creative evaluation sits.

**The founding fMRI result (2012).** Ellamil et al. had N=15 (9 female, mean age 22.14, SD 2.25) according to a review table; the control was line tracing. In the generate stage people designed and sketched covers from descriptions of documentaries. In the evaluate stage they wrote or sketched evaluations of those covers. [d19] Full text was never opened by us. Thresholds and phase purity are unknown. Output differed by phase (sketching versus writing), so the contrast is confounded with motor and language demands. [critique §6, d19]

**Poetry study (2015).** Liu et al.: 30 recruited, 27 analysed (14 expert MFA poets, 13 novices). Poets improvised a poem, then revised it, in fixed order. Generation raised medial prefrontal cortex and lowered dorsolateral PFC, intraparietal sulcus and precuneus. Revision brought DLPFC and IPS back. Experts suspended control more strongly in generation. Same patterns against recitation and against random typing. [a03, a04]

**Cooperation account.** Beaty, Benedek, Silvia and Schacter (2016) argue default and executive networks, usually antagonistic, cooperate in creative thought. [a02, b03] Beaty et al. (2015) found default-salience coupling early in a trial and default-executive coupling later (N=28 plus a resting sample n=42). [a05, c02] Beaty et al. (2018) predicted creative ability from default, executive and salience connectivity together (abstract only). [a26, b14]

**Inverted U.** A 2025 study with N=2433 across 10 samples finds creative ability follows an inverted U with the balance of default-executive switching. The correlation between the two constructs ranged r=0.32, 0.33, 0.39 in three samples but 0.07 and 0.13 (CIs include 0) in two. [b15]

**Time course inside one idea.** Lloyd-Cox, Chen and Beaty (2022): classifier accuracy for creative versus non-creative trials followed a U over three phases of one idea, in both networks. Executive accuracy was higher early. [a12] Rominger et al. (2019, N=86 analysed): more original ideas showed a faster early rise in task-related alpha. Less original ideas rose more at later stages. [b07]

**Evaluation is several operations.** ERP study of ads (N=31): novelty gave early N1-P2 effects, effort on novel content gave N200-500, usefulness gave a late positive component. [b09] fMRI (N=38 analysed of 40): default network encoded originality, executive network encoded adequacy, the reward system (vmPFC peak -8, 48, -10, t(37)=8.81) encoded subjective value of the idea. [b10] A 2023 fMRI study found right medial temporal lobe tracks novelty and left MTL tracks usefulness during evaluation. [b11]

**Phases share representations.** Matheson et al. (2023): information from generation is re-instated in later evaluation within and between executive and default regions. The phases share content. [d24]

**Behavioural side.** Jansson and Smith (1991): showing examples during generation reduces output. Nijstad et al. (2010): judging too early drops promising ideas. Both second-hand through Sowden et al. [a24] Hao et al. (2016) found that pausing to evaluate earlier ideas made later ideas more original than a distraction pause. [d20] Rietzschel, Nijstad and Stroebe (2010): people picking ideas favour feasible and desirable over original ones, so generating more ideas does not raise the quality of the ones picked. [d21]

**Newer meta-analyses.** Gonen-Yaacovi et al. (2013): 34 imaging studies, shared left caudal PFC, rostral PFC for combining remote information. [a07, b02] A 2020 ALE of divergent thinking (20 studies, 596 participants, 162 foci) found mostly semantic-network regions. [b13] He et al. (2025): 44 generation and 10 evaluation studies. Evaluation tied to insula, claustrum, inferior frontal and medial frontal regions. The medial temporal lobe finding of Ellamil was not reproduced. [d18, abstract level]

**Timeline summary.**

| Year | Event |
|---|---|
| 1960 | Campbell: blind variation, selective retention |
| 1991 | Jansson and Smith: example fixation |
| 1992 | Geneplore |
| 2010 | Nijstad and Rietzschel: premature evaluation and selection of feasible over original ideas |
| 2012 | Ellamil: fMRI split, N=15 |
| 2015 | Liu poets (N=27); Beaty default-executive coupling |
| 2016 | Beaty review (cooperation); Hao (reflection helps) |
| 2022-2025 | Time course, valuation system, inverted U (N=2433), ALE meta-analysis that does not reproduce MTL |
| 2023-2026 | LLM work: self-correction limits, judge bias, idea-judging near chance, execution gap |

## 3. Core findings with exact numbers

### 3a. Human brain and behaviour

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Generation recruits medial temporal lobe; evaluation recruits executive plus default, rostrolateral PFC, insula, temporopolar cortex; default-executive positive coupling throughout | N=15 (9 female), mean age 22.14; book-cover design versus evaluation versus tracing | Ellamil 2012 [a01, b01, c01, d19] | [E] as a pattern; abstract and review table only; MTL part [C] |
| Executive control down in generation, up in revision | 27 analysed (14 experts, 13 novices); 4 blocks of 60 s; generation versus recitation and versus typing gave the same pattern | Liu 2015 [a03, a04] | [E] with Ellamil, EEG |
| EEG design tasks: generation shows highest workload and lowest control | 42 participants in text (analysed N not checked) | 2021 EEG [b06] | [S] |
| Default and executive hubs co-activate during alternate uses; network efficiency rises with ability | N=28 plus n=42 resting; 12 s generation window | Beaty 2015 [a05, c02] | [E] |
| Inverted U of default-executive switching and creative ability | N=2433, 10 samples; r=0.32, 0.33, 0.39 in three, 0.07 and 0.13 in two; task-fMRI validation N=31 | 2025 [b15] | [E] but weak and site-dependent |
| Early ideas are recalled, later ones are new | N=35 (24 female); old ideas 6.69 s versus new 8.73 s, d=1.16; new rated more creative d=1.46; 85.37 ideas each, 48.34 old versus 37.02 new | Benedek 2014 [a06] | [E] with Heinonen [b12] and Rominger [b07] |
| ACC activity rises with serial order of idea | n=16 | Heinonen 2016 [b12] | [S] abstract |
| Novelty and usefulness are checked separately; valuation weights them | ERP N=31; fMRI N=38 of 40, vmPFC t(37)=8.81 | [b09, b10, b11] | [E] |
| Judging a novel use costs more semantic work | more upper-alpha, lower-alpha, larger N400; sample size not extracted | 2018 EEG [b08] | [S] |
| MTL is also active in evaluation (right = novelty, left = usefulness) | small sample, not extracted | 2023 [b11] | [C] against Ellamil |
| Meta-analysis does not list MTL among generation regions | 44 generation, 10 evaluation studies | He 2025 [d18] | [C], abstract only |
| Evaluation mid-generation raised later originality | EEG alternate uses; reflection versus distraction | Hao 2016 [d20] | [S], abstract only |
| People pick feasible over original ideas | abstract only, no N | Rietzschel 2010 [d21] | [S] |
| Early judging drops ideas; examples hurt output | no numbers, second-hand | Jansson and Smith 1991; Nijstad 2010 [a24] | [S], originals unopened |
| Generation phases are re-instated in evaluation | abstract level | Matheson 2023 [d24] | [S] |

### 3b. Language models

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Over-generate then rank gives ideas judged more novel than expert-human ideas | novelty 4.84 human, 5.64 AI, 5.81 AI plus human rerank; 49 ideas per condition; 119/109/109 reviews; 79 reviewers; overall 4.68 / 4.85 / 5.34 (rerank versus human p=0.04); feasibility 6.61 / 6.34 / 6.44 not significant | Si 2024 [a13, b16, c03] | [S] one group, NLP prompting topics |
| Prompt-only LLM judges rank ideas at or near chance | balanced accuracy 50.0 (GPT-4o direct), 45.0 (pairwise), 51.7 (Claude-3.5 direct), 53.3 (pairwise), 43.3 (AI Scientist reviewer); human 56.1; NeurIPS 66.0; ICLR 71.9 | Si 2024 [a15, b17, c04] | [E] with Wen and Mule |
| Same judges do better on a different object (past papers) | accept/reject on 1200 ICLR submissions: Claude-3.5 71.4%, Claude-3-Opus 63.5%, GPT-4o 61.1% | Si 2024 [a14] | [E] |
| Zero-shot frontier models stay near chance on pairs of ideas with known outcomes | GPT-4.1 51.9%; o1, o3 similar or slightly better; GPT-5 57.65 (default), 59.61 (low), 61.10 (medium thinking) | Wen 2025; Mule 2026 [d07, d08] | [E] |
| Judges trained on outcomes beat the human ceiling | fine-tuned GPT-4.1 plus retrieval 64.4% versus 48.9% for 25 experts (best annotator 60.0); 8B SFT 77.1% versus GPT-5 61.1%; 4B 59.2% versus expert majority 41.6% (chance 25) | [d07, d08, d09] | [E] |
| Frontier judges predict outcomes of concrete ML code changes above chance | R2: 0.49 (best), 0.41, 0.38, 0.18, 0.13; direction right 82, 78, 76, 72, 69%; 269 ideas analysed; no self-preference (+0.01, CI -0.06 to +0.08) | Bansal 2026 [d05, d06] | [S] |
| Ideas scored by reading lose value on execution | 43 executors, about 103 h each; AI drops: novelty -1.049, excitement -1.760, effectiveness -1.879 (effectiveness 6.00 to 4.13, N=24); human changes -0.010, +0.078, -0.052 (4.83 to 4.78, N=19); Spearman 0.077 and -0.148; flip not significant | Si 2025 [a17, b19, c06] | [S] one group |
| Gap may sit in the idea, not the execution, in economics | idea d=2.23, execution d=0.90; 953 papers (912 AI, 41 human); model judges only | Li 2026 [d10] | [S], not a replication |
| Single-model sampling is low-diversity | 200 non-duplicates of 4000 (cosine 0.8); most models give under 3 distinct responses in 10 queries; Claude-3.5 Sonnet 1.76, gpt-4o 2.88, Llama-3.1-405B 3.20, gemma-2-2b 5.66; cross-model similarity 71% to 82% | Si 2024; NoveltyBench; Hivemind [a16, a23, c20] | [E] |
| Showing earlier outputs raises diversity to about human-writer level | 100 prompts, 8 generations, three models; human baseline 8 authors, a lower bound | NoveltyBench [b28, c19, d22] | [S] |
| Without an outside signal, self-critique is flat or worse | GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1) to 41.8 (round 2); GSM8K 75.9 / 75.1 / 74.7; GPT-4 GSM8K 95.5 / 91.5 / 89.0; HotpotQA 26.0 to 25.0; with oracle 75.9 to 84.3, 75.8 to 89.7, GPT-4 95.5 to 97.5 | Huang 2024 [a18, b20, c08] | [E], 2023 models |
| Self-critique helps when the task has a checkable metric | Self-Refine about 20% absolute average on seven tasks; Game of 24 with LLM critic 5% to 3% | Madaan 2023; Stechly 2024 [a19, b27, c09] | [E] task-dependent |
| 2026 models gain when the check is explicit constraints | SAT: Mistral 34.62 to 64.96; Haiku 4.5 75.64 to 93.59; DeepSeek 78.63 to 92.74; Flash Lite 60.68 to 82.91; Gemini Pro 97.00 to 100 | Stav 2026 [d16] | [S] |
| Reasoning models gain only marginally from extra correction | text statement, no single number | CorrectBench [d17] | [S] |
| Blind spot to own errors in non-reasoning models | 64.5% average over 14 models; "Wait" cuts it 89.3%; 5,306 traces cut it 76.0%; reasoning models show little | Tsui 2026 [d15] | [S] |
| A sound verifier turns samples into accuracy | SWE-bench Lite 15.9% to 56% at 250 samples versus 43% prior best; Game of 24 5% standard, 36-38% with sound verifier, 42% at k=25 rejection; PRM 78.2 versus ORM 72.4 versus vote 69.6 (best-of-1860) | Brown 2024; Stechly 2024; Lightman 2023 [b24, c09, c18] | [E] |
| Splitting propose from evaluate with search | Game of 24: IO 7.3, CoT 4.0, CoT-SC 9.0, ToT b=1 45, b=5 74, best-of-100 CoT 49 | Yao 2023 [a20, b23] | [E] on checkable tasks |
| The generator is the bottleneck in a checkable puzzle | GPT-4 gen + GPT-3.5 eval 64%; GPT-3.5 gen + GPT-4 eval 31%; both GPT-4 74%; both GPT-3.5 19% | Yao 2023 appendix [c07] | [E] with Song |
| Generation and judging are partly independent skills | generator-validator consistency 76% GPT-4; Alpaca-30B 60% to 93-94% after consistency fine-tuning; generation +16%, validation +6.3% | Li 2023; Jiang 2024; West 2023 [c11, c12, a22] | [E] |
| Position and verbosity bias | Vicuna-13B vs ChatGPT win rate 51.3% to 23.8% on swap; 66 of 80 queries in favourable order; judge-human agreement above 80% | Wang 2023; Zheng 2023 [c16, b22] | [E] |
| Self-recognition and self-preference | GPT-4 self-recognition 73.5%; over 90% after 500-example fine-tune; preference rises linearly with recognition | Panickssery 2024 [a21] | [C] overall, see 5 |
| Authorship labels move scores, true source does not | label +0.43 (CI 0.39 to 0.47); originality +0.53; true source +0.02 (p=.689); 10 judges | Chae 2026 [d02, d03] | [S] |
| Length inflates automatic originality scores | 4,813 responses, 81 students plus ChatGPT-4o; 1.43-point drop when only the core idea was scored | Domanti 2026 [d04] | [S] |
| Critique-revise turns raise idea diversity then flatten | non-duplicate ratio 0.69 (none), 0.77, 0.80, 0.85, 0.86 for 0 to 4 turns; three critics 0.80 versus one 0.77 | Ueda 2025 [d13] | [S] |
| For a small model, selecting did nothing; revising helped | raw 5.34 versus rerank 5.29 (1 to 9, outside panel); refine all 7.01, random 40 of 50 6.91, diversity-aware 6.77 | Zhang 2026 [d12] | [S] |
| Selector matters more than generator diversity | diverse team + judge 0.810 versus 0.512 homogeneous; margin shrinks 53 to 67% with independent judges; Spearman 0.90 | Maryanskyy 2026 [d14] | [S] |
| Reviewer overall score tracks novelty and excitement, not feasibility | overall-novelty r=0.725; overall-excitement 0.854; overall-feasibility 0.097; novelty-feasibility -0.073 | Si 2024 [d23] | [S] |
| A trained critic finds more bugs than paid humans but invents some | model critiques preferred 63% | McAleese 2024 [c21] | [S] trained, not prompt-only |

## 4. Mechanisms and models

This section says how each model could be coded.

### 4a. Two-mode loop (Geneplore / Ellamil style)

State: a pool P of candidate ideas, a mode m in {generate, evaluate}.

- generate(m): produce ideas with no critique language. In people this is the phase with relaxed prefrontal control. For an LLM that means: higher temperature, a fresh context, no examples of "good" answers, no mention of criteria beyond the task. Output goes to P.
- evaluate(m): a separate call with the goal restated and low temperature. It reads P and returns scores for named criteria. It does not write new ideas.
- Code sets the switch. A human-style loop lets the person switch when they feel like it. In Ellamil the switch was self-paced. Our agent should switch by a code trigger (count reached, plateau reached), not by the model.

### 4b. Coupling, not isolation

Because default and executive regions stay coupled, a hard wall between modes is a design choice (K02). Two engineering variants follow.

- **Hard split.** Generate N, then judge. Simple, matches G5.
- **Interleaved.** Generate k, short review of those k, generate N-k more, then judge (Hao 2016 style). Test K24 compares the two.

Implement both as one function with a parameter `review_at` (None or a count). The agent log records which one ran.

### 4c. Serial-order model

Early ideas are retrieved from memory. Later ones are new (Benedek 2014: 6.69 s vs 8.73 s, d=1.16; rated d=1.46). Engineering form: sample a long list in one context, or sample many isolated contexts. In one context, order matters and early items are the common ones. Code can drop the first k items and keep the rest (test K06). In isolated contexts (the schema's S3), each attempt starts from the "typical" answer. The history of directions tried (S3 open mode) is the equivalent of a "do not repeat" list.

### 4d. Evaluation as several scores

Evaluation splits into novelty detection, usefulness check, and valuation (K04). Engineering form: the judge call returns a vector, not a number: novelty, adequacy (or feasibility), maybe excitement. Code multiplies by weights and handles ties. Reason from data: reviewer overall score correlates 0.725 with novelty and 0.097 with feasibility; novelty and feasibility are uncorrelated at -0.073 [d23]. A blended score hides one axis.

### 4e. Selection stack, ordered by trust

1. Code check or small run (unit test, retrieval novelty against a corpus, a small experiment). Trusted.
2. Embedding dedup (cosine 0.8) to cut repeats. Cheap, label-free.
3. Judge trained on outcomes. Only if we have one.
4. Prompt-only judge. Use only to reject clear failures, never to rank (K22).

### 4f. Judge hygiene (all code)

- Run each pair in both orders and count disagreement (K12).
- Strip authorship cues and style hints; do not say "your earlier ideas" (K21).
- Length-normalise or score the core idea only (d04).
- Present candidates as another writer's work, not the judge's own, for non-reasoning models (d15, test K28).
- Give the judge call room and restate the goal (K18, single-source).

### 4g. Stop rules

Dedup-ratio gain per round under 0.01 (K25) is a label-free stop. A fixed cap of three revise rounds is the fallback (Ueda: ratio flattens after 3 to 4 turns). Song 2025 says self-improvement loops saturate within a few rounds with falling diversity [c10].

### 4h. Generation-verification gap

Song et al. define the gap as how much a model's own verifier improves its own generations. For good verification methods the relative gap rises with pretraining compute. Cross-verification gains grow with verifier strength and shrink with generator strength [c10]. In Game of 24 the generator was the bottleneck (64% vs 31%) [c07]. Engineering rule: measure the gap for each stage on our bench and give the larger model to the stage with the larger measured gain.

## 5. What holds up

### 5a. Holds up

- **Different modes exist, but are coupled.** Four independent sources: fMRI (Ellamil), poetry (Liu), EEG design (b06), connectivity (Beaty). Nobody finds clean isolation (K01, K02).
- **Control is lowered in generation, raised in revision.** Three sources (K03).
- **Evaluation has parts.** Three sources (K04).
- **Prompt-only LLM judges of unexecuted ideas are near chance.** Three independent sources: Si 2024 (43.3 to 53.3 against human 56.1), Wen 2025 (51.9), Mule 2026 (57.65 to 61.10) (K07).
- **Self-critique with no outside signal does not help reasoning.** Huang, Stechly, Olausson, CorrectBench, Tsui (K10).
- **External verifier turns samples into accuracy.** Five sources (K11).
- **Judge biases for position and verbosity.** Three sources (K12).
- **Single-model diversity is low.** Three sources (K16).
- **Generation and judging are partly separate skills in models.** Three sources (K14).

### 5b. Failed, contested or unreplicated

- **MTL for generation.** Ellamil places the medial temporal lobe in generation. The 2023 fMRI study finds it in evaluation. The 2025 ALE (44 + 10 studies) does not reproduce it. Do not encode brain regions in the schema (K05, [C]).
- **Ellamil is thin.** N=15, abstract plus review table only, phases confounded by output type, no pre-registered forced-phase replication found.
- **Self-preference in judges.** Panickssery: recognition drives preference. Zheng: smaller effect, data inconclusive. Chae 2026: once quality is controlled the coefficient is +0.003; a self-label alone adds +0.43. Bansal 2026: +0.01 for outcome prediction. Domanti 2026: part of the apparent preference is answer length. Mahbub and Feng 2025: swapping two words lowers harmful self-preference in QA by a few points, but rewriting the other answer in the judge's style raises it. Size depends on task. Labels and elaboration are the clearest drivers (K13, [C]).
- **Self-Refine versus Huang.** About 20% gain when a checkable metric exists; flat or negative without oracle labels. Task dependence, not contradiction (K10).
- **Ideation-execution gap.** One group, one field, N=43. The ranking flip was not significant. No regression-to-the-mean analysis. The economics study points the other way for the bottleneck but uses model judges only (K08).
- **Early-judging and example-fixation effects.** Second-hand. Hao 2016 cuts against a strict "never evaluate while generating" rule (K19, K24).
- **LLM judging reliability depends on the object.** Zheng: over 80% agreement with humans on chat answers. AI Scientist reviewer near human on papers. Si: 43.3% on ideas.

### 5c. Moderators

| Moderator | Direction | Evidence |
|---|---|---|
| Presence of a checkable metric | self-critique helps with it, hurts without | Self-Refine, Huang, Stav SAT |
| Model type | non-reasoning models have a 64.5% blind spot to own errors; reasoning models show little and gain marginally from more correction | d15, d17 |
| Object judged | answers and past papers: good; unexecuted ideas: near chance | Zheng, Si |
| Training on outcomes | lifts judges above human ceiling | d07-d09 |
| Task field | NLP prompting: gap in execution; economics: gap in idea | d10 |
| Order of presentation | verdicts flip on swap | c16 |
| Length | inflates originality scores | d04 |
| Label | +0.43 effect | d03 |
| Expertise (humans) | experts suspend control more strongly in generation | a04 |

### 5d. Interventions that worked

- Showing earlier outputs and asking for a different one (NoveltyBench, diversity to about human level) [S].
- Revising ideas rather than ranking them, for a small model (+1.5 on a 1 to 9 scale) [S].
- Generate-many with a sound verifier (SWE-bench Lite 15.9% to 56%) [E].
- Appending "Wait" for non-reasoning models (blind spot down 89.3%) [S].
- Critique-revise up to three turns for diversity (0.69 to 0.85) [S].
- Both-order judging in code [E].
- Outcome-trained judges [E].

### 5e. Interventions that did not work

- Intrinsic self-correction on reasoning for 2023 models (Huang).
- LLM critic on Game of 24 (5% to 3%).
- "Be creative" prompts and paraphrasing (NoveltyBench: marginal).
- Ranking raw ideas with a small model (5.34 vs 5.29).
- Rating each idea first or telling people to exclude ideas (Rietzschel: no help; abstract).
- Rewriting the rival answer in the judge's style (raises self-preference).
- Reasoning models plus more passes (marginal gains at higher time cost).

## 6. Language models

### 6a. Generation side

LLMs are good generators of ideas. Blind experts judged AI ideas more novel than expert-human ideas (5.64 vs 4.84, p<0.05; Si 2024). But the pool is narrow. 4000 samples held about 200 non-duplicates. NoveltyBench: under 3 distinct responses in 10 queries for most of 20 models; larger models often less diverse; Claude-3.5 Sonnet 1.76, gemma-2-2b 5.66. Different models answer alike (71% to 82%, Hivemind). So over-generation hits a ceiling set by duplication, not by quality.

What lifted diversity: show earlier outputs (about human-writer level, 8-author baseline); up to three critique-revise turns (0.69 to 0.85 non-duplicate ratio). What did not: "be creative" prompts, paraphrasing.

### 6b. Judge side

Prompt-only judges of ideas: balanced accuracy 43.3 to 53.3 (Si 2024), 51.9% zero-shot GPT-4.1 (Wen 2025), 57.65 to 61.10% GPT-5 (Mule 2026). Human reviewers: 56.1% in Si. So the best prompt-only frontier judge is about at the human ceiling on pairs but far from reliable. The change that moved it: training on outcomes (64.4% vs 48.9% for 25 experts; 77.1% for an 8B model vs 61.1% GPT-5). Giving a fast measurable target also moved it: frontier models reach R2 0.49 and 69 to 82% direction on ML code changes.

### 6c. Self-critique

2023 models: flat or worse without oracle (GPT-4 GSM8K 95.5 to 89.0). 2026 models: gains on explicit-constraint tasks (SAT 34.62 to 64.96 for Mistral Large; Gemini Pro 97.00 to 100) and marginal gains for reasoning models. Non-reasoning models have a 64.5% blind spot to errors in their own output. No matched-token test on open-ended ideas exists.

### 6d. Bias in judging

Position bias (51.3% to 23.8% on swap), verbosity, self-label (+0.43), length (1.43 points). Self-preference is task-dependent and may be near zero when quality is controlled.

### 6e. Execution and outcome

Reading-based expert scores of LLM ideas dropped 1.0 to 1.9 points after execution while human ideas barely moved (N=43, 103 hours each). The correlation between pre- and post-execution score is weak (Spearman 0.077 and -0.148). So a judge call that agrees with readers can still be wrong about outcomes.

### 6f. Selector versus generator

Strong evidence that the selector is the weak link on open ideas (d14: selection beat diversity) but that margin shrank 53 to 67% under independent judges. On checkable puzzles the generator was the bottleneck (64% vs 31%). Which stage is the bottleneck depends on whether a sound check exists.

### 6g. What is missing

No matched-token study of one-call versus two-call. No 2025 to 2026 frontier-model test of idea-judging with different-model judges. No larger human baseline for NoveltyBench. Per-idea outcome data from Si 2025 not located.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

Most of these are already in SCHEMA.md v0.2. They are listed so the evidence ids are on record, and so nothing here is re-proposed. The only items not already stated in the schema are marked NEW.

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | The generating model is not the final selector of ideas; prompt-only judges stay near chance. Judge only to reject clear failures. | G8 (already in) | [E] | K07, K22; a15, b17, d07, d08, d09 |
| A2 | Prefer a code check or small run to a judge call; never trust a judge on a task with no check unless it has beaten the human-agreement ceiling on held-out items. | G8, S4 (already in); add a ceiling gate NEW | [E] | K11, K07; b24, c09, c18 |
| A3 | No intrinsic self-critique without an outside signal; revise only from real output. | G2 (already in) | [E] | K10; a18, c09, d15, d16, d17 |
| A4 | Judge call hygiene in code: both orders, length-normalised, no authorship cue, no majority shown. | G5 (already in); both-order flip count as a logged metric NEW | [E] | K12; c16, b22 |
| A5 | Isolated contexts for generation, no critique language in the generation prompt. | S3 (already in) | [E] | K03, K16 |
| A6 | Measure distinct ideas by embedding in code (cosine 0.8) and stop sampling at a plateau. | G4, G12, S3 (already in for open mode); the plateau stop signal NEW | [E] | K16; a16, a23 |
| A7 | Give the stronger model to the stage with the larger measured gain; cap generate-judge loops. | G7, G12 | [E] | K15; c07, c10 |
| A8 | Do not put brain regions or "default/executive" labels into the schema. | none (add to 4b "not to add") NEW | [E] | K02, K05 |
| A9 | Report every selection gain against an outside rater, not against the selecting model. | G7, section 6 log | [S] but cheap and safe | K29; d14 |

### Test first (single-source, contested or untested)

| # | Item | Part | Status | Evidence | Test id |
|---|---|---|---|---|---|
| T1 | Separate generate call plus judge call versus one call that does both | G5, S3/S7 | [S], no direct study | K01, b29 | U1 |
| T2 | Review mid-generation (generate 5, review, generate 15) versus strict split | G5 | [S] | K24, d20 | U2 |
| T3 | Judge-picked versus random-picked versus diversity-picked before revision | G8, O1 | [S] | K26, d12 | U3 |
| T4 | Prior-ideas display in the generation call | S3, O1 | [S] | K17, d22 | U4 |
| T5 | Two-score judge with code weight versus one blended score | G8 | [S] | K27, d23 | U5 |
| T6 | Candidates shown as another writer's work | G5 | [S] | K28, d15 | U6 |
| T7 | Dedup-ratio stop rule versus fixed three rounds | S5/S6, O1 | [S] | K25, d13 | U7 |
| T8 | Drop the first k ideas by code | G12, S3 | [S] human-derived | K06, a06 | U8 |
| T9 | Different-model judge versus same-model judge | G5 | [C] | K13, d01-d06 | U9 |
| T10 | Numeric predicted-change judge checked against a small run | G8 | [S] | K23, d05 | U10 |
| T11 | Judge with long versus short reasoning allowance | G8 | [S] | K18, b08 | U11 |
| T12 | Judge pass repairs weak generation? Measure judge accuracy on own versus other output | G5/G8 | [E] that skills are separate; size on our bench unknown | K14 | U12 |
| T13 | Execution-grounded selection (check or run) versus judge | G8 | [S] | K08, a17 | U13 |

## 8. Concrete tests on our bench

All arms get the same token budget. Setup cost counts (G7). Outside rater means a held-out model panel plus, where we can, a human sample; the selecting model never rates its own picks.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| U1 split versus single call | NoveltyBench-style open prompts (100), plus our open-mode items | A: one call "give N ideas and pick the best". B: generate call (no judging language), then separate judge call with goal restated | distinct count (embedding, cosine 0.8) of picked ideas, held-out rater score of the pick, tokens | B higher on distinctness by a small amount; quality unclear. Confidence low. Null is a live outcome |
| U2 mid-review | open items, alternate-uses type | A: generate 20 then judge. B: generate 5, short review, generate 15, judge | distinct good ideas per 10k tokens | B slightly higher if Hao 2016 transfers |
| U3 pick before revise | research-idea items with execution check where possible | judge-picked, random-picked, diversity-picked 40 of 50, then same revise | outside-panel score after revision | random about equal to judge (d12); diversity picks cheaper |
| U4 prior ideas shown | NoveltyBench curated 100 prompts | A: plain resample. B: show earlier ideas by code and ask for different | distinct count out of 8; reward or rater quality | B up in distinctness, quality flat or lower |
| U5 two-score judge | ideas with held-out rater novelty and feasibility scores | A: single blended score. B: two scores, code weight | Spearman and pair agreement with held-out rater | B higher agreement on novelty; small |
| U6 other-writer framing | idea judging with known flaws | A: "your earlier ideas". B: "another writer's ideas" | flaw-detection rate and false-flag rate | gain for non-reasoning models only |
| U7 stop rule | critique-revise on ideas | A: stop when dedup gain under 0.01. B: fixed 3 rounds | distinct count per token | A same quality at fewer tokens |
| U8 drop first k | alternate-uses and open ideas | A: all N. B: drop first k=3 to 5, keep rest | mean outside-rater quality of kept pool | B higher quality, lower count |
| U9 judge identity | idea pairs with known outcomes | same-model, different-model, code-only | agreement with outcome or rater | small differences; if none, drop the concern |
| U10 numeric prediction | ML or code changes with fast score | judge predicts change; compare with small run | R2, direction right | R2 up to about 0.4 for frontier models |
| U11 judge budget | labelled set | short versus long reasoning | accuracy | flat for reasoning models; maybe up for non-reasoning |
| U12 own versus other | any generator | judge accuracy on own outputs versus other models' | accuracy gap | gap near zero or negative |
| U13 check versus judge | items where a cheap check exists | judge-picked versus check-picked | outcome after run | check-picked higher |

Run all with at least 3 seeds. Log mode, path, tokens per state, picked versus best available (SCHEMA section 6).

## 9. What does not transfer, and why

- **Brain region labels.** MTL, default, executive: they describe the human brain. The LLM has no regions. The MTL claim is contested even in humans.
- **Self-paced switching.** In Ellamil people chose when to switch. Our program decides by code. The human switch cost does not exist for an LLM call.
- **Working-memory limits.** The reason a person keeps modes apart is partly limited capacity. A new LLM call has an empty context and no fatigue.
- **Inverted U of default-executive switching.** It is a statistical property of individuals across a population (N=2433, weak and site-dependent). There is no per-call analogue.
- **Expertise effects.** Experts suspend control more strongly. We have no expert/novice model.
- **Drawing, poetry and alternate-uses tasks.** All human work used these. No study used the open problems, ARC-style items or code our agent faces.
- **Human premature evaluation.** In people, judging early costs attention and mood. A judge call has neither. The LLM analogue is context contamination (critique language steering the next sample), which is a different mechanism and untested.
- **Example fixation.** The human effect (Jansson and Smith) is second-hand and the replication record mixed.
- **Reward system / vmPFC valuation.** An LLM has no personal preferences. The analogue is a code-set weight.
- **Idea judging by reading versus by running.** A human judge may be calibrated by lived outcomes. A prompt-only LLM judge is not (K07).
- **Results from 2023 models.** Huang and Si used older models. 2026 results already differ (Stav, Tsui, CorrectBench).

## 10. Open questions

1. Does separate-call generate-then-judge beat single-call generate-and-judge at equal tokens on creative quality? No study found.
2. Which cheap code checks (retrieval novelty, dedup, unit test, small run) predict execution outcome? The per-idea Si 2025 data were not located.
3. Does the ideation-execution gap replicate outside NLP prompting, and how much is regression to the mean from selecting top-scored ideas?
4. Does a different-model judge reduce self-preference when judging ideas (not summaries or QA)?
5. What are the effect sizes for premature evaluation and example fixation, and do they replicate? Jansson and Smith 1991 and the Sio 2015 meta-analysis were paywalled.
6. Ellamil full text: thresholds, phase purity, any pre-registered forced-phase replication.
7. NoveltyBench regeneration against a larger human baseline, and quality (not just distinctness) of the added answers.
8. Do 2025 to 2026 reasoning models with extended thinking still show no gain from intrinsic critique on open-ended ideas, at matched tokens?
9. Does a two-score judge with a code weight agree better with held-out raters than a blended judge?
10. Is the selector or the generator the bottleneck on our own items? Both Yao and Maryanskyy give opposite answers in different settings.
11. How many critique-revise rounds pay before quality, not only diversity, falls?
12. Does mid-generation review help LLMs the way Hao 2016 reports for people?

## 11. Sources

[V] opened (page or full text read this session by a source agent or the cross-checker). [M] snippet or abstract only.

**Human neuroscience and behaviour**

- [M] Ellamil, Dobson, Beeman, Christoff (2012) Evaluative and generative modes of thought during the creative process. NeuroImage. https://europepmc.org/article/MED/21854855 ; https://doi.org/10.1016/j.neuroimage.2011.08.008 (abstract only; sample details via [V] Pidgeon table)
- [V] Pidgeon et al. (2016) Functional neuroimaging of visual creativity: systematic review and meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC5064346/
- [V] Liu, Erkkinen, Healey, et al. (2015) Brain activity and connectivity during poetry composition. https://europepmc.org/article/MED/26015271
- [V] Beaty, Benedek, Silvia, Schacter (2016) Creative cognition and brain network dynamics. https://europepmc.org/article/MED/26553223 (also [M] https://pubmed.ncbi.nlm.nih.gov/26553223/)
- [V] Beaty, Benedek, Kaufman, Silvia (2015) Default and executive network coupling supports creative idea production. https://europepmc.org/article/MED/26084037
- [M] Beaty et al. (2014) Creativity and the default network. https://pubmed.ncbi.nlm.nih.gov/25245940/
- [M] Beaty et al. (2018) Robust prediction of individual creative ability from brain functional connectivity. https://pubmed.ncbi.nlm.nih.gov/29339474/
- [M] Beaty et al. (2019) Network neuroscience of creative cognition. https://europepmc.org/article/MED/30906824
- [V] Benedek et al. (2014) To create or to recall? https://europepmc.org/article/MED/24269573
- [V] Gonen-Yaacovi et al. (2013) Rostral and caudal prefrontal contribution to creativity. https://europepmc.org/article/MED/23966927 ; https://pubmed.ncbi.nlm.nih.gov/23966927/
- [V] Sowden, Pringle, Gabora (2015) The shifting sands of creative thinking. https://www.tandfonline.com/doi/full/10.1080/13546783.2014.885464 (carries Finke/Ward/Smith 1992, Campbell 1960, Simonton, Basadur, Jansson and Smith 1991, Nijstad 2010 second-hand)
- [M] Lloyd-Cox, Chen, Beaty (2022) The time course of creativity. https://europepmc.org/article/MED/36240723
- [V] Andrews-Hanna, Smallwood, Spreng (2014) The default network and self-generated thought. https://europepmc.org/article/MED/24502540
- [V] Jia and Zeng (2021) EEG responses to generation, evolution and evaluation. https://pubmed.ncbi.nlm.nih.gov/33483583/
- [V] EEG network oscillations and cognitive workload in design ideation (2021). https://pubmed.ncbi.nlm.nih.gov/34930950/
- [V] Rominger et al. (2019) U-shaped alpha power. https://pubmed.ncbi.nlm.nih.gov/30756348/
- [V] Alpha bands when evaluating alternate object use (2018). https://pubmed.ncbi.nlm.nih.gov/30405471/
- [V] Neural model of creative evaluation in advertising, ERP (2020). https://pubmed.ncbi.nlm.nih.gov/33319861/
- [V] Reward system encodes subjective value of ideas (2025). https://pubmed.ncbi.nlm.nih.gov/39794481/
- [V] MTL lateralization in creativity evaluation (2023). https://pubmed.ncbi.nlm.nih.gov/35353185/
- [M] Heinonen et al. (2016) Default mode and executive networks and serial order. https://pubmed.ncbi.nlm.nih.gov/27627760/
- [V] ALE meta-analysis of divergent thinking fMRI (2020). https://pubmed.ncbi.nlm.nih.gov/32845058/
- [V] Dynamic switching between brain networks predicts creative ability (2025). https://pubmed.ncbi.nlm.nih.gov/39809882/
- [M] Meta-analysis of two creativity subsets in divergent thinking (2022). https://europepmc.org/article/MED/35906880
- [M] He et al. (2025) ALE meta-analysis of creative generation and evaluation. https://pubmed.ncbi.nlm.nih.gov/40614883/
- [M] Hao et al. (2016) Reflection enhances creativity. https://pubmed.ncbi.nlm.nih.gov/26808451/
- [M] Rietzschel, Nijstad, Stroebe (2010) Selection of creative ideas after individual idea generation. https://pubmed.ncbi.nlm.nih.gov/19267959/
- [M] Matheson et al. (2023) Representing creative thought, RSA. https://pubmed.ncbi.nlm.nih.gov/37268289/

**Language models and AI**

- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
- [V] Si, Hashimoto, Yang (2025) The ideation-execution gap. https://arxiv.org/abs/2506.20803
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601
- [V] Panickssery, Bowman, Feng (2024) LLM evaluators recognize and favor their own generations. https://arxiv.org/abs/2404.13076
- [V] West et al. (2023) The generative AI paradox. https://arxiv.org/abs/2311.00059
- [V] Zhang et al. (2025) NoveltyBench. https://arxiv.org/abs/2504.05228
- [V] Zheng et al. (2023) Judging LLM-as-a-judge. https://arxiv.org/abs/2306.05685
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787
- [V] Cobbe et al. (2021) Training verifiers. https://arxiv.org/abs/2110.14168
- [V] Lightman et al. (2023) Let's verify step by step. https://arxiv.org/abs/2305.20050
- [V] Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations. https://arxiv.org/abs/2402.08115
- [V] Song et al. (2025) Mind the gap. https://arxiv.org/abs/2412.02674
- [V] Li et al. (2023) Generator-validator consistency. https://arxiv.org/abs/2310.01846
- [V] Jiang et al. (2024) Self-[In]Correct. https://arxiv.org/abs/2404.04298
- [V] Wang et al. (2023) LLMs are not fair evaluators. https://arxiv.org/abs/2305.17926
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] McAleese et al. (2024) LLM critics help catch LLM bugs. https://arxiv.org/abs/2407.00215
- [V] Kumar et al. (2024) SCoRe. https://arxiv.org/abs/2409.12917
- [V] Olausson et al. (2024) Is self-repair a silver bullet? https://arxiv.org/abs/2306.09896
- [V] Lu et al. (2024) The AI Scientist. https://arxiv.org/abs/2408.06292
- [V] Li et al. (2024) Chain of Ideas. https://arxiv.org/abs/2410.13185
- [M] Weng et al. (2023) Self-verification. https://arxiv.org/abs/2212.09561
- [V] Mahbub and Feng (2025/2026) Mitigating self-preference by authorship obfuscation. https://arxiv.org/abs/2512.05379
- [V] Chae et al. (2026) Self- and other-labels induce bidirectional bias in LLM judges. https://arxiv.org/abs/2608.18091
- [V] Domanti et al. (2026) Effect of idea elaboration on automatic originality assessment. https://arxiv.org/abs/2604.20569
- [V] Bansal et al. (2026) Can LLMs predict outcomes of ML experiments? https://arxiv.org/abs/2610.22599
- [V] Wen et al. (2025) Predicting empirical AI research outcomes. https://arxiv.org/abs/2506.00794
- [V] Mule et al. (2026) Teaching LMs to forecast research success. https://arxiv.org/abs/2605.21491
- [M] Gong, Li, Zhou (2026) Scientific taste from institutional traces. https://arxiv.org/abs/2603.16659
- [V] Li (2026) The ideation bottleneck. https://arxiv.org/abs/2604.03338
- [V] Zhang (2026) Budgeted subset refinement. https://arxiv.org/abs/2607.14118
- [V] Ueda et al. (2025) Multi-agent LLM dialogues for research ideation. https://arxiv.org/abs/2507.08350
- [V] Maryanskyy, Budnikov, Kaliyev (2026) When agents disagree. https://arxiv.org/abs/2603.20324
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778
- [V] Stav et al. (2026) When does intrinsic self-correction help? https://arxiv.org/abs/2606.23196
- [V] Tie et al. (2025) CorrectBench. https://arxiv.org/abs/2510.16062

**Not opened, cited second-hand only:** Jansson and Smith (1991); Nijstad et al. (2010); Sio meta-analysis (2015); Finke, Ward, Smith (1992); Campbell (1960); Simonton; Basadur. Several LLM numbers (Li 2023, Jiang 2024, Wang 2023, McAleese, Kumar, Olausson, Lu 2024, Chain of Ideas, Cobbe, Lightman, Song) were read by source agents and not re-opened by the checker (critique §6).
