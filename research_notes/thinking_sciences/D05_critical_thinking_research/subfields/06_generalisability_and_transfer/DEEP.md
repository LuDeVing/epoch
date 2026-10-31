# Generalisability and transfer: deep document

*Subfield D05.06. Question: does critical thinking carry across subjects? Key works: McPeck (1981), Ennis (1989). Why it matters: our agent's memory keeps lessons keyed to problem class, not shared across all. Evidence: evidence_a-d.jsonl, claims.jsonl (K01-K34), critique.md in this folder. Evidence ids are a01-a33, b01-b28, c01-c26, d01-d20.*

*Read this first: no paper tests the exact question for agents (class-keyed lessons versus one shared pool, at equal retrieved tokens). Everything below is indirect. Several "independent" sources are one paper counted in several evidence files; claims were recounted by paper (see critique.md).*

## 1. What it is

Transfer is when something learned in one setting helps in another. Generalisability is the same idea seen from the result side: does a skill, rule or lesson hold on items it was not built on?

Three layers matter for us.

1. **Philosophy of education.** Is critical thinking a general skill, or is it always thinking about some subject? McPeck (1981) said there are no general thinking skills. Ennis (1989) said there are, and that "field" is too vague a boundary to block them. [a01, a02, b01]
2. **Psychology of transfer.** How far does training on task A reach? Thorndike's common-elements theory says: as far as the two tasks share elements. Cognitive-training meta-analyses say far transfer is close to zero once controls are fair. [a04, a16, b02]
3. **Language models.** Do models carry a procedure to a new surface form, a new class, a longer case? And do stored lessons (memory, cheat sheets, workflows) carry from one class of task to another? [a21-a32, b08-b24, c04-c18, d01-d17]

SEP splits "subject-specificity" three ways. Only the third raises a testable transfer problem. [a02]
- Conceptual: thinking abilities are logically tied to a subject (McPeck's strong thesis).
- Epistemological: norms of good thinking differ by field.
- Empirical: a good thinker in one field is not automatically good in another.

For an agent the empirical version is the one to measure: a lesson learned on class A, used on class B, at what gain or loss?

Common ground of both sides: good thinking about a topic needs background knowledge of it. [a03, K06, established]

## 2. History and theories in depth

**Formal discipline (to 1900s).** Idea: hard subjects (Latin, geometry) train the mind for everything. Thorndike tested it with school tests in autumn and spring. Students in the supposedly mind-training courses did not gain more. Methods were criticised later (Rosenblatt 1967), and this is second-hand. [a05]

**Common elements (Thorndike and Woodworth 1901).** Subjects trained to estimate areas with error feedback. Gains did not spread evenly to other shapes; some people showed no spread. The authors concluded practice spreads only where identical elements are shared. A habit (such as discounting your own error) can itself be a shared element. Table values were lost in the copy read; subject count not recorded. [a04, b05]
Prediction: near transfer common, far transfer rare. Sala and Gobet use it as the baseline account. [a17]

**Chunking and template theory (Chase and Simon 1973; Gobet and Simon 1996).** Expertise rests on tens of thousands of domain chunks. So little carries across domains. General ability (IQ, working memory) predicts success but training it does not carry over. Chess players beat non-players by about 0.5 SD on cognitive tests, which is a correlation (self-selection), not a training effect. [a17]
The agent analogue: per-class memory is the chunk store.

**Analogical transfer (Gick and Holyoak 1980, 1983).** Duncker's tumour-ray problem. People who read the fortress story (same solution) still mostly failed to use it. A hint that the story might help raised solving to "nearly 100 per cent" (summary wording). Using the analogy was easy; noticing to use it was the failure. This is a retrieval-cue problem, not a skill problem. Exact human numbers are second-hand: Experiment 2 had 29% (8/28) spontaneous vs 50% (14/28) with hint. The often-quoted "20-30% vs 90%" is unverified and probably mixes studies. [a06, d16, b25, K05]

**Encapsulated principles (Jepson, Krantz and Nisbett 1983).** People know that 20 dice throws beat two. They do not use sample size when judging a person from two tests. The rule stays tied to the setting where it was learned. Second-hand, no percentages. [a07]

**What helps transfer in humans (second-hand, no effect sizes unless stated).**
- Compare two solved cases that differ in surface (Loewenstein, Thompson and Gentner 1999). Business students who did this used the shared solution more on a novel problem two weeks later. [a08]
- Label each step with the goal it serves (Catrambone 1995, 1998). Handles changed problems better than lock-step procedure. [a09]
- A taught step sequence plus 8 hours of simulator practice with expert feedback transferred to new naval problems (Helsdingen 2010). Near to mid transfer. [a11]
- Halpern (1998) proposed dispositions, skills, structure training and monitoring; transfer needs cues to structure. Not opened. [b27]
- School add-on thinking programmes (about 5 hours a week for one or two years) seldom test real transfer: puzzle training is measured by puzzles. Where transfer was tested, results were absent or modest and faded. [a12]

**The McPeck-Ennis debate.** McPeck: no general skills; teach thinking inside subjects. He exempted one general item: the disposition to suspend judgment. Critics (Paul 1985, Siegel 1985): writing and speaking are general abilities that are always about some subject. Counter-example to McPeck: spotting a confusion of necessary and sufficient conditions. Ennis: "field" is vague; inter-field principles exist (for example hypothetico-deductive reasoning). SEP: evidence that cross-domain instruction aids transfer is scanty. [a01, a02, b01]

**Computational accounts (2026).** Gabriel and Mushtaq contrast two models. Pattern recognition with state-action associations allows limited transfer to tasks with different actions. Heuristic search with a learned state-value estimate can reuse learning across tasks. Their data favoured limited transfer. [a19, a20]

**Training-distribution view for models.** Error grows with the gap between training and test distribution (Zhao et al. Theorem 3.1). [a24] Procedural knowledge in pretraining: reasoning questions of one task share influential documents holding procedures (formulae, code), so a procedure per class is the natural unit. [a29]

## 3. Core findings with exact numbers

Status key: established = two or more independent sources; single = one paper; contested = sources disagree or a correction is pending. Human or LLM noted by context.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Far transfer of trained skills is about zero with active controls (humans) | 14 meta-analyses, 332 samples, 1,555 effects, 21,968 people. Uncorrected far-transfer g 0.04-0.19, grand mean 0.12. Corrected, active controls only: -0.03 to 0.02, grand mean 0.00 | Gobet and Sala 2023 [b02, b03] | Established (authors take one side; a 48-researcher paper disagrees, not opened) |
| Passive controls inflate transfer | Music: g 0.25 (k=64, passive) vs 0.03 (k=54, active). WM training: 0.18 (passive, k=34) vs 0.05 (active, k=40). Overall g: chess 0.34, music 0.16, WM 0.12 | Sala and Gobet 2017 [a16, b04] | Established |
| Near transfer holds | WM training to other memory tasks g 0.44 (active), 0.46 (passive) | Sala and Gobet 2017 | Established |
| Transfer is one-way | Updating to span g 0.176 (p<.001); span to updating 0.048 (p=.453). 55 studies, 208 effects, N=3,492 | Fu et al. 2026 [a18, b06] | Single |
| No reuse of a reusable heuristic on a new problem set | 73 completed, 56 analysed (17 excluded). 4 days of training; no reliable gain on untrained set beyond direct practice | Gabriel and Mushtaq 2026 [a19] | Single (low power for a null) |
| Generic CT instruction: small effect, stable across level, subject, duration | g 0.30 over 341 effects. Content-specific CT outcome 0.57 (97); disposition 0.23 (25); subject facts 0.33 (140) | Abrami 2015 [a13, d18] | Contested. The 0.57 is an outcome-type split, not content-specific teaching |
| Mixed teaching best, not significantly | Mixed +0.38; infusion +0.29; general +0.26; immersion +0.23. Combined three approaches 0.57 (19 studies). Problem solving 0.35 (31); role-play 0.61 (5); teacher questions 0.38 (19); whole-class discussion 0.42 (16); small group 0.41 (14) | Abrami 2015 via summaries [a14, d19] | Single; primary paper blocked (403) |
| Stage 1 of the same meta-analysis | 117 studies, 20,698 participants, 161 effects, g+ 0.341 (snippet only) | Abrami 2008 [a15] | Single, not opened |
| Inquiry learning: huge but unreliable | g 1.336, CI [1.061, 1.611], I2 92.09%, Egger p<.001. Subject domain not a moderator (Qm 1.43, p=.698); control group Qm 5.21, p=.022. 57 studies | Harapan 2026 [b07] | Do not use the number |
| Programming transfers only where concepts overlap | Average g .47 (source text); smaller with active control; no literacy benefit | Scherer 2018 via Willingham [a10] | Single; source detail unverified |
| Humans rarely use a studied analogy unprompted | 29% (8/28) vs 50% (14/28) with hint, Exp 2 (second-hand) | Gick and Holyoak 1983 via [d16] | Established in direction; exact numbers second-hand |
| GPT-4 matching-task version of Gick-Holyoak | 60 trials (15 per cell). No hint: 1/15 analogy use (radiation problem), correct-source precision and recall 0.00. With hint: recall 1.00, precision 0.52 (TP 15, FN 0, FP 14, TN 1), accuracy 0.53 | arXiv 2505.00603 [d15] | Single |
| GPT-3 far story analogy not significant | Humans N=54; near p=0.0039; far p=0.065; humans beat GPT-3 OR 0.37, p=0.0003; 15 of 54 humans always chose the analogous story | Webb, Holyoak and Lu 2023 [a21] | Single (GPT-3 only; GPT-4 preliminary) |
| Counterfactual variants cut accuracy | GPT-4 2-digit addition: 100.0% base-10 vs 23.4% base-9 (no CoT); 98.2% vs 38.6% (0-shot CoT). GPT-3.5: 100.0% vs 6.6%. GPT-3.5 drawing programs 99% to 62/71/75% (flip, 90, 180 rotation). Base-9 comprehension check 90.0% | Wu et al. 2024 [a23, b08, b09] | Single paper in three files |
| Rare variants fail more | Word reversal GPT-4 97% (high-probability output) vs 53% (low). rot-13 21% vs 11%. Shift cipher 51% vs 13%. rot-13 over 100x more common online than rot-12 | McCoy et al. 2024 [b12, c09] | Established (with Wu) |
| Irrelevant clause: large drops | GSM-NoOp up to -65.7 (Phi-3-mini), o1-preview -17.5, o1-mini -29.1, Gemma-7b-it about -20.6, Mistral-7b-v0.3 -24.0. Gemma2-9B best-to-worst set gap over 12 points; GSM8K on the right tail for 21 of 25 models | Mirzadeh et al. 2025 [b10, c05, c06] | Established with Shi |
| GSM-IC distractors | Fewer than 30% of base problems solved consistently (macro). code-davinci-002 micro/macro: CoT 72.4/6.0; +instruction 77.8/15.0; LTM 77.5/18.0; LTM+instruction 80.6/25.0; CoT+SC 88.1/30.0; LTM+SC 93.4/45.0; Program 54.4/5.0; 0-CoT 29.0/1.0 | Shi et al. 2023 [c07, d03] | Single |
| Premise order | R-GSM: GPT-4-turbo 94.1 to 85.0; PaLM 2-L 86.4 to 79.5; Gemini 1.0 Pro 80.5 to 69.1; GPT-3.5 67.3 to 51.8. Deduction: up to 20-30+ points lost; some models from over 65% to below 25%. Zero-shot, greedy; no scaffold arm | Chen et al. 2024 [c08, d05] | Single |
| CoT help is class-bound | Avg gain: symbolic 14.2, maths 12.3, logical 6.9 points. Top three categories 56.9 vs 45.5; others 56.8 vs 56.1. Gains up to 66.9 (GSM8K), 41.6 (MATH). 100+ papers, 20 datasets, 14 models | Sprague et al. 2025 [a26] | Single |
| CoT out of distribution (trained from scratch) | Exact match 100% in distribution; 0.01% new composition (Qwen3-14B); 8.52% (LLaMA3-8B); 0% partial or full OOD. SFT recovery plateaus once edit distance reaches 3 | Zhao et al. 2025/26 [a24, b14, c10] | Established (with Dziri); small synthetic setting |
| Compositional depth | 3x3-digit multiplication: ChatGPT 55%, GPT-4 59% | Dziri et al. 2023 [a27, b11] | Established with Zhao |
| Compositionality gap | About 40% of 2-hop questions with both sub-answers known are wrong. davinci-002 2Wiki EM: direct 25.4, CoT 29.8, self-ask 30.0, self-ask+search 40.1; Musique 5.6/12.6/13.8/15.2 | Press et al. 2022 [d17] | Single, old model |
| Puzzle collapse | Hanoi N=5 near perfect; River Crossing N=3 fails (valid only to about move 4); Hanoi N=10 first error about move 100. Three regimes | Shojaee et al. 2025 [a28, b13] | Contested |
| Rebuttal of collapse | Hanoi failures match token caps; River Crossing N>=6 (capacity 3) unsolvable. Function output under 5,000 tokens. With Python: Hanoi 5/5 at N=11 and 13 (direct 0/5); DeepSeek-R1 about 80% on River Crossing and Blocks World; Checker Jumping 0 for N>=3. 5 runs per cell | Lawsen 2025; Song et al. 2025 [d01, d02] | Contested; preliminary |
| Giving the algorithm | Did not fix collapse (Shojaee). Step-explicit demos cut error about 10x on long parity, 9x addition, 5x multiplication, 2x subtraction (Zhou) | [b13, b16] | Contested |
| Self-correction without outside signal | GPT-3.5 CommonSenseQA 75.8 to 38.1 after one round; GPT-4 GSM8K 95.5, 91.5, 89.0 over rounds. Oracle labels: GSM8K 97.5; HotpotQA 29.0 to 59.0 (100 items) | Huang et al. 2024 [b15] | Single (matches SCHEMA 4b) |
| RL on maths transfers, SFT does not | Qwen3-14B-Base, maths-only data. Non-reasoning avg: base 45.7, SFT-think 21.1, SFT-no-think 29.0, RL 53.2 (RL minus best SFT +24.0). Other-reasoning avg: base 30.2, SFT-think 45.3, SFT-no-think 45.2, RL 60.0. Maths avg: base 27.7, SFT-think 49.8, RL 53.8. IFEval 69.2 to 42.3 (SFT-think) vs 70.0 (RL). RL vs SFT: +17.1 LiveCodeBench2, +1.8 GPQA | Huan et al. 2025 [a25, b17, c01, c02] | Contested. One model family. Correction: 55.9 is the base GPQA score, row uncertain |
| SFT memorises, RL generalises | GeneralPoints rule variant +3.5 (11.5 to 15.0); V-IRL language variant +11.0 (80.8 to 91.8); visual OOD +17.6 (23.6 to 41.2) | Chu et al. 2025 [b18] | Single |
| Logic-RL | 7B on 5K logic puzzles: AIME +125% relative, AMC +38% relative | Xie et al. 2025 [b19] | Single, low base |
| Maths-only costs breadth | Qwen2.5-7B-Base: MMLU-Pro 58.9% full data vs base 47.7%. Maths-only +1 on maths (49.1 vs 48.5) but about 2 points lower on MMLU-Pro, GPQA, SuperGPQA | Ma et al. 2025 [c11] | Contested vs Huan |
| Curated memory lifts repeated-structure tasks | Dynamic Cheatsheet, Claude 3.5 Sonnet: AIME 2024 23.3 to 50.0 (DC-Cu); AIME 2025 6.7 to 36.7; GPQA-Diamond 59.6 to 68.7 (DC-RS); AIME 2020-24 6.7 to 40.6; equation balancing 44.8 to 98-100; GPT-4o Game of 24 10% to about 99%. Full-history 26.7 on AIME 2024 | Suzgun et al. 2025 [b22, c12] | Single |
| Workflow memory across gaps (step success, GPT-4) | Cross-task 36.2 / 45.1 offline / 43.6 online; cross-website 30.1 / 33.7 / 33.9; cross-domain 18.6 / 32.6 / 35.5. Relative gain 24.6% Mind2Web overall, 51.1% WebArena. Whole-task SR cross-domain 1.0 / 0.7 / 1.7 | Wang et al. 2024 [a31, b20, c14] | Single; near-zero whole-task success |
| Memory gain vs distance | ReasoningBank (flash) step SR no memory 40.3/31.7/31.9; AWM 41.0/31.7/30.1; RB 44.9/33.9/36.6 (gain +4.6/+2.2/+4.7). Pro: 44.4/34.8/35.0; AWM 44.4/34.8/34.4; RB 45.6/36.9/38.1 (gain +1.2/+2.1/+3.1). Whole-task SR 1.0 to 1.6 (flash cross-domain) | Ouyang et al. 2026 [d13, d14, c13] | Contested |
| Insight transfer | FEVER success: Act 58, ReAct 63, ExpeL transfer no demos 65, ExpeL transfer 70 | Zhao et al. 2024 [a32, b21] | Single; both tasks use Wikipedia lookup |
| Add-all memory hurts | RegAgent 67.53 fixed vs 55.48 add-all vs 70.95 strict. EHRAgent 16.75 / 13.05 / 38.50. AgentDriver 40.11 / 32.32 / 51.00. CIC-IoT 71.50 / 59.90 / 85.40. Add-all hurt in 4 of 4 | Xiong et al. 2025 [d10] | Established with DC full-history; strict filter used ground truth |
| Self-composed structures | BBH +11% (GPT-4), +7% (PaLM-2); T4D +39% / +29%; 10-40x less compute than self-consistency | Zhou et al. 2024 [b24] | Single |
| Thought templates | +11% Game of 24, +20% Geometric Shapes, +51% Checkmate-in-One, about 12% of multi-query cost | Yang et al. 2024 [c16] | Single |
| Self-generated analogies beat CoT | Beats 0-shot and 3-shot CoT on GSM8K, MATH, Codeforces, BIG-Bench. MATH row read 8%/24% Acc@1/Acc@10 (0-shot) vs 11%/27% (3-shot CoT) | Yasunaga et al. 2024 [c15] | Single, table values not fully recorded |
| Skill library carries to a new world | Voyager: ReAct and Reflexion made no meaningful progress on unseen tasks in a fresh world; Voyager did. GPT-4 5.7x more unique items than GPT-3.5 | Wang et al. 2023 [c18] | Single |
| Skills graph | Skill-it +35.8 points over random on LEGO continual pretraining; stratified sampling only 0.007 loss gain | Chen et al. 2023 [c17] | Single, model-level |
| Cognitive behaviours predict RL gains | Countdown: Qwen-2.5-3B about 60% vs Llama-3.2-3B about 30% under identical RL; priming Llama with verification, backtracking, subgoals, backward chaining closed the gap, even with incorrect solutions | Gandhi et al. 2025 [a30] | Single; 3B, one game |

## 4. Mechanisms and models

Written so an engineer can build from them.

**M1. Common elements as a feature match.** Describe every problem by features: surface (words, entities, units) and structure (operation type, constraint type, goal type, tool). Transfer from lesson L (learned on class A) to item x is predicted by overlap of structural features, not surface. Implement: each lesson stores a feature set from the class record; retrieval score = structural overlap, with surface overlap only as a tie-break. [a04, a17, b05, a33]

**M2. Retrieval cue failure (Gick and Holyoak).** The lesson is available, but nothing fires it. In GPT-4, an explicit hint gave recall 1.00 but precision 0.5: with a cue the model over-applies. [d15] Implement two parts: (a) code retrieves candidates by structure and presents them; (b) code then asks "does the source's key relation hold in the target?" and verifies by running the mapped solution. Do not rely on the model to notice. A cue raises reuse but also false matches, so the pair needs a verifier (SCHEMA O7 already requires a code-checked mapping). [a06, a22, d15]

**M3. Generalisation gap bound (Zhao).** Test error rises with distance between training and test distributions along three axes: task (including composition), length, format. Implement a distance score for each new item against the class record: task mismatch, size mismatch, format mismatch. Large distance means: do not trust a stored lesson; fall back to the plain path, code execution or search. SFT recovery was local: plateau once edit distance reached 3. [a24, b14, c10]

**M4. Frequency effect (McCoy, Wu).** Accuracy follows how common the task form, input and output are in pretraining, even when the abstract procedure is the same. Implement: tag each class with a familiarity bucket (common, rare, counterfactual). For rare and counterfactual buckets, route execution to code and keep the model to filling slots. Comprehension is often intact (base-9 check 90.0%), so the failure is in execution under a changed mapping. [b09, b12, c09, c25]

**M5. Class-conditioned operator choice.** CoT pays in maths and symbolic classes (+12.3 to +14.2) and not elsewhere (56.8 vs 56.1). Implement: per class, store the pass rate by mode (direct, short, CoT, checked); S0 picks the cheapest mode that passes; an unknown class defaults to short. [a26]

**M6. Memory write, read, prune (curation).** From Dynamic Cheatsheet, AWM, ReasoningBank, Xiong:
- Write: store a lesson only if a verifier passed (strict filter beat add-all by 15.5 to 25.5 points across Xiong's four agents) and keep it as principle plus steps plus goal per step. [d10, a09]
- Read: retrieve by similarity, show after the first attempt (SCHEMA memory rule). Agents copy the nearest stored record (experience-following), so errors spread. [d10]
- Prune: delete a record when later retrievals of it go with low-quality outcomes (history-based), and cap size. Needs a reliable judge; a weak judge can hurt. [d11]

**M7. Direction of transfer.** Log each cross-class reuse as an ordered pair (source class, target class). Updating-to-span transferred (0.176); span-to-updating did not (0.048). Treat lesson reuse as directional until shown otherwise. [a18, b06]

**M8. Principle plus varied cases.** Humans transfer best from an abstract principle stated explicitly plus several concrete cases that differ in surface (Abrami's best cells; Loewenstein et al.). Implement: when a lesson is stored, merge it with an earlier lesson from another class if both share the structure; keep a one-line principle and two examples. A lesson becomes trusted after it helps on two different problems (already in SCHEMA section 5). [a08, a14]

**M9. Control design for transfer claims.** Gobet and Sala show most apparent far transfer is a passive-control artefact. For prompts the analogue is a bare-prompt comparison. Use three arms of equal length: (1) valid scaffold, (2) invalid-but-relevant scaffold, (3) off-topic filler. Invalid-but-relevant keeps 80-90% of the gain (CoT 43.9 vs invalid reasoning 39.8 vs no coherence 25.2 vs no relevance 9.6), so arm (2) is not a placebo; arm (3) is. A generic instruction of the same form ("Solve grade school math problems.") did not help; only the one naming the failure did. [d04, d07, d08, K28]

## 5. What holds up

**Agreement across papers**
- Far transfer is near zero with active controls: two meta-analytic papers from one group (Sala and Gobet 2017; Gobet and Sala 2023) agree. Both read the same literature and the critique did not re-open them. The opposing view (a 48-researcher paper) was not opened. [K02, K03]
- Irrelevant content hurts: Shi (2023) and Mirzadeh (2025) agree across two years and model families. o1-class models also dropped (o1-preview -17.5, o1-mini -29.1). [K09]
- Rare or counterfactual forms hurt: Wu and McCoy agree. [K08]
- CoT out-of-distribution failure: Zhao (controlled small models) and Dziri (3x3 multiplication 55-59%) agree on direction. [K11]
- Add-all memory hurts: Xiong (4 of 4 agents) and Dynamic Cheatsheet (full-history 26.7 vs 50.0) agree. [K19]

**Corrections made in this run (do not repeat the old claims)**
- Abrami 0.57 is not content-specific teaching. It is the effect on content-specific CT measures (97 effects). Explicit vs infused and STEM vs non-STEM did not differ. K01 is contested and cannot justify class-keyed memory. [d18]
- Zhao 0.01% composition is Qwen3-14B; LLaMA3-8B is 8.52%. [critique]
- 55.9 in Huan's table is the base GPQA score, not SFT-think. [critique]
- 6.7 to 40.6 (DC-RS) is AIME 2020-24; the AIME 2025 figure is 6.7 to 36.7 (DC-Cu). Different sets. GPT-4o AIME 2025 fell 20.0 to 6.7 under full history in one run: a harm case. [critique]
- 24.6% in AWM is the overall Mind2Web relative gain, not cross-task only. [critique]
- Gick-Holyoak "20-30% vs 90%" is unverified. [K05]
- Premise-order cost was overstated for maths: 9-15 points on R-GSM; 20-40+ on deduction. [K10]
- Memory gain does not shrink steadily with distance on web tasks (ReasoningBank); AWM falls below no-memory cross-domain. [K17]

**Failed or weak replications and null results**
- Gabriel and Mushtaq: no transfer to an untrained problem set although a reusable heuristic existed. 56 analysed; a null with low power. [a19]
- GPT-3 far analogy p=0.065 (not significant). [a21]
- Self-correction without feedback hurts (GPT-3.5 CommonSenseQA, -37.7 points). [b15]
- AWM cross-domain below no-memory in ReasoningBank's setup (30.1 vs 31.9 on flash; 34.4 vs 35.0 on pro). [d13, d14]
- Reasoning models (R1, o1) gained little from Dynamic Cheatsheet; small models (GPT-4o-mini) gain little; poor retrieval confused GPT-4o on GPQA-Diamond. [d12]
- Filler tokens help only small models trained for them. [d09]

**Moderators**
- Control-group type is the only real moderator in cognitive training (tau squared 0.000-0.012 with active controls). [b03]
- Distance on three axes: task, length, format (Zhao). [a24]
- Familiarity of the form (Embers, Wu). [c25]
- Shared tools and structure (ExpeL HotpotQA to FEVER: both Wikipedia lookup). [a32]
- Presence of a retrieval cue (Gick-Holyoak). [d15, d16]
- Training route for models: RL vs SFT. [c02, b18]
- Training dose, age and stimulus type for WM transfer: larger at low doses, in non-adults, with verbal stimuli. [a18]
- Direction (updating to span, not reverse). [a18]

**Interventions that worked**
- Naming the failure in an instruction (ignore irrelevant text) plus distractor exemplars; no harm on clean problems (CoT 59.3 vs 60.3). [d04, c07]
- Least-to-most: about double the macro accuracy of CoT with code-davinci-002 (18.0 vs 6.0). [c07, d03]
- Voting on top: CoT+SC macro 30.0, LTM+SC 45.0. Still leaves over half the base problems unsolved consistently. [d03]
- Compositional prompt (iterative subgoal plus verify): +3.4 over LTM on GSM8K, +4.7 on GSM-Plus (GPT-3.5-Turbo). [d06]
- Self-ask with search: 2Wiki EM 25.4 to 40.1. [d17]
- Python tool: Hanoi to N=13 for reasoning models. [d02]
- Strict admission filter and history-based deletion for memory. [d10, d11]
- Compare-cases and goal-labelled steps for people. [a08, a09]

**Interventions that did not work**
- Add-all memory and full-history context. [d10, c12]
- Eight same-question shots did not repair NoOp. [c06]
- Counterfactual demonstrations in context did not close the gap. [b09]
- Giving the solution algorithm to reasoning models on puzzles did not stop collapse (but see Zhou's step-explicit demos on arithmetic). [b13, b16]
- Unstructured self-reflection, bias checklists (SCHEMA 4b). [b15]
- A generic same-form instruction. [d04]

**The RL-versus-SFT dispute (K14, K15)**
Huan and Chu say RL transfers and SFT memorises. General-Reasoner says maths-only training costs about 2 points on other benchmarks relative to broad data (and at 14B the full-data model won on every metric). Both can hold: RL beats SFT, yet breadth beats maths-only. This concerns model training, not scaffolds. It informs model choice only.

## 6. Language models

**How models behave on transfer tasks**
- They carry a procedure only partly. Failure grows with new surface values (GSM-Symbolic), irrelevant content (NoOp, GSM-IC), premise order, task unfamiliarity (counterfactual, rare), composition and depth, and length or format shift. [c23]
- Understanding survives; execution fails. Base-9 comprehension check 90.0% while base-9 addition is 23.4% (no CoT). [b09]
- Memorisation is not the whole story for GSM-Symbolic: GPT-4o and Llama3-8B showed negligible drop on name and number changes, but 21 of 25 models had GSM8K on the right tail. [b10, c05]
- Analogy: GPT-3 near analogy fine, far analogy not significant. With a supplied analogue it used it (qualitative, one problem). GPT-4 without a hint almost never picked the correct source (precision and recall 0.00); with a hint it recalled all but half the claims were false positives. [a21, a22, d15]
- Reasoning models: puzzle collapse is partly an evaluation artefact (token caps, unsolvable instances), and tools fix part of it. Skill in one puzzle does not predict a sibling: Hanoi N=5 near perfect, River Crossing N=3 failing. [a28, d01, d02]
- CoT is class-bound: big in maths and symbolic, near zero elsewhere. [a26]
- Pretraining: reasoning rests on shared procedural documents per task. [a29]

**What changed performance and by how much**
- Targeted instruction plus voting: macro accuracy 6.0 to 45.0 (LTM+SC) on distractor items; still short of full rescue. [d03]
- Test-time memory: AIME 2024 23.3 to 50.0; AIME 2025 6.7 to 36.7; GPQA-D 59.6 to 68.7. Web agents: step success +9 to +17 points cross-domain (AWM, GPT-4), whole-task success still 1-5%. [c12, c14]
- Memory curation: +15.5 to +25.5 points vs add-all (strict filter minus add-all across Xiong's agents). [d10]
- Tool use: Hanoi N=11 and 13 from 0/5 to 5/5. [d02]
- Training route: RL +24.0 vs SFT on the non-reasoning average. [c02]
- Decomposition plus search: 2Wiki EM +14.7 (25.4 to 40.1) on an old model. [d17]
- Self-generated analogies, thought templates and self-composed structures beat plain CoT or multi-query prompting; the last two at lower cost. [c15, c16, b24]

**Not known for current frontier models.** Whether composition failure (0.01%) persists with tools; whether scaffolds help on counterfactual and NoOp items (no scaffold arm found for Wu or NoOp with frontier models); whether keyed memory beats shared memory. All memory studies compare memory against none. [K31, K32, critique gaps 1, 3, 9]

**Measurement caveats.** Task-level success in web-memory studies is 1-5%; step-level gains hide near-zero whole-task success. Several tables were extracted from PDFs with garbled columns (d06, d07, d11, Bamboogle in d17).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = SCHEMA section 5. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Always include an equal-length placebo arm when testing any scaffold; vary relevance, not correctness.** G7 (equal-token testing). [E] K02, K03, K28. Ev: a16, b02, b04, d04, d07, d08.
2. **Test every lesson on held-out items and on a different class or surface before trusting it.** Memory (the "trusted after two different problems" rule: the two must differ in class or surface). [E] K02, K06. Ev: a12, b03, a33.
3. **Admit a lesson to memory only after a verifier passes; prune lessons whose retrievals lead to failures; never add-all.** Memory (write and prune). [E] K19. Ev: d10, d11, c12. Note: the strict filter in Xiong used ground truth; in production the verifier is our code check or a held-out check.
4. **Store the conditions under which a lesson was learned (class, familiarity bucket, tool, size range).** Memory. [E] K08, K11. Ev: a23, b08, b12, c09, a24.
5. **Route rare, counterfactual and deep cases to code or search, not recall.** S0 gate / tools. [E] K08, K11. Ev: b09, b12, a27, d02. Comprehension is intact; execution is the failure.
6. **Filter irrelevant clauses at input and test with NoOp-style items.** S1 input hygiene (already present). [E] K09. Ev: b10, c05, c06, c07. Naming the failure in the instruction helps; a generic one does not (d04, single-source).
7. **Do not rely on the model to notice a stored analogue; retrieve it in code and require a checked mapping.** O7, memory. [E] K05. Ev: a06, a22, d15, d16.
8. **Keep G2 (no revision from opinion alone).** [E] already in schema. Ev: b15.
9. **Do not cite the Abrami 0.57, inquiry g=1.336, or the 20-30% vs 90% analogy figure as evidence.** Documentation. [E] K01, K24, K05.

### Test first

1. **Class-keyed lessons vs one shared pool at equal retrieved tokens.** Memory. [S] K31, K01, K25, K16. No direct test exists (critique gap 1). Ev: d12, a31, b20, d13.
2. **Retrieval by structural features vs by topic or surface similarity.** Memory / S0. [S] K05. Ev: a04, a08, d15.
3. **Class gate for CoT: use the scaffold only where it pays.** S0 / mode choice. [S] K12. Ev: a26.
4. **Distance guard: skip a stored lesson when the item is far from the class record.** S0 / memory. [S] K11, K17. Ev: a24, b14, d13, d14.
5. **Hint-style cue to reuse a stored lesson, then verify the mapping.** O7. [S] K05. Ev: d15, a06.
6. **Lesson as principle plus two cross-surface examples vs one-line rule.** Memory. [S] Ev: a08, a14, a09.
7. **Goal-labelled steps in stored operators.** Memory. [S] Ev: a09, b16.
8. **Scaffold on perturbed variants (NoOp, premise-order shuffle, counterfactual).** G3 / S1. [S] K07, K10, K26. Ev: d03, d05, d06.
9. **Explicit decomposition into known sub-steps on a current model with tools.** O3. [S] K32. Ev: d17, d02.
10. **Self-composed structure per task vs fixed scaffold.** Mode choice. [S] K21. Ev: b24, c16.
11. **Pruning rule for memory.** Memory. [S] K30. Ev: d11.
12. **Direction log for cross-class reuse.** Memory. [S] K04. Ev: a18, b06.
13. **Python as an operator before declaring a complexity limit.** Tools. [C] K33, K23. Ev: d02, d01.

Note: nothing here justifies a new operator. The evidence supports memory and S0 changes and test design.

## 8. Concrete tests on our bench

Common rules: both arms at equal tokens (setup cost counted, G7). Use the three-arm control wherever the claim is "scaffold helps". Hold out by class. At least two seeds; report confidence intervals. Add only on a pass; thresholds are in UNKNOWNS.md.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Items from 4-6 problem classes, lessons mined from a train split | (a) lessons keyed by class, top-k within class; (b) one shared pool, same top-k and token budget; (c) no memory | Accuracy on held-out items per class and pooled | Keyed beats shared by a few points on structurally distinct classes; equal on similar classes. Unknown: this is the McPeck test |
| T2 | Same set, ordered by distance: same class, sibling class, other domain | Memory vs no memory at each distance | Gain curve per distance | Gain shrinks with distance on reasoning (unlike web). Possibly flat. The curve is the output |
| T3 | Items with a solved source in memory, surface changed | (a) topic-similarity retrieval; (b) structural-feature retrieval; (c) no source | Correct-source retrieval rate; accuracy; false-match rate | (b) beats (a) on surface-shifted items; false matches near 0.5 without a verifier |
| T4 | NoOp-style and premise-shuffled items | (a) plain; (b) scaffold; (c) length-matched generic instruction; (d) invalid-but-relevant scaffold; (e) off-topic filler | Accuracy; macro accuracy over variants | (b) > (c) = (e); (d) keeps most of (b); drop shrinks but not to zero |
| T5 | Counterfactual variants (base-9, altered mapping) | (a) plain; (b) scaffold with conditions stated; (c) code-executed slot filling | Accuracy base vs counterfactual; gap | (c) closes most of the gap; (b) partial |
| T6 | Items from classes with and without CoT benefit | (a) always-on scaffold; (b) class-gated; (c) plain | Accuracy per class; tokens | (b) matches (a) on maths and wins on tokens elsewhere |
| T7 | Streams of tasks with repeated structure | (a) add-all; (b) verifier-gated; (c) gated plus history-based pruning | Accuracy over stream; memory size | (b) > (a); (c) >= (b) only if the judge is reliable |
| T8 | Items far from every class record | (a) always use top lesson; (b) distance guard falls back to plain | Accuracy on far items; harm rate (lesson makes it worse) | (b) lowers harm rate; no loss on near items |
| T9 | Compositions of known steps unseen in lessons | (a) direct; (b) explicit decomposition; (c) decomposition plus tools | Exact match | (b) and (c) beat (a); (c) best |
| T10 | Lessons moved A to B and B to A | Direction log vs symmetric reuse | Gain per direction | Asymmetric gains in some pairs |

## 9. What does not transfer, and why

- **Human far-transfer nulls.** Gobet and Sala's null concerns training of general abilities (working memory, music, chess), not prompts. A prompt scaffold is not practice. We borrow only the control lesson. [b02]
- **Training-route results (RL vs SFT, Logic-RL, General-Reasoner).** They change weights. Our agent does not train. They inform model choice. [K14, K15]
- **Web-agent memory numbers.** Step-level gains with whole-task success of 1-5%. Do not extrapolate to reasoning items. [d13, d14]
- **Education effect sizes.** Mostly near-transfer outcomes tied to taught content; inflated and heterogeneous (I2 92%). [b07, a13]
- **Synthetic trained-from-scratch CoT collapse (62K-3B models).** Direction informs us; the 0.01% figure does not apply to frontier models. [a24]
- **GPT-3 and davinci results.** Old models (Webb 2023, Press 2022, Shi 2023); current models may differ. [K22, K26, K32]
- **Puzzle collapse claims.** Contested; token caps and impossible instances. [d01]
- **The human cause of the analogy failure.** Humans fail to notice (memory search); a model fails because the prompt has no retrieval step. The fix (cue) looks the same but the cause differs. [a33]
- **Priming with cognitive behaviours (Gandhi).** One game, 3B models. [a30]

## 10. Open questions

1. Does class-keyed memory beat a shared pool at equal tokens on reasoning items? No paper tests it.
2. What does the distance-decay curve of memory gain look like on reasoning tasks (same class, sibling, other domain)?
3. Do scaffolds help on counterfactual and NoOp items with frontier models? No scaffold arm found for Wu or NoOp.
4. Which active-control prompt removes the expectation effect for a scaffold test? A three-arm design is proposed; never applied to a scaffold-transfer claim.
5. Does composition failure persist for frontier reasoning models with tools, and does decomposition rescue it?
6. Are the Illusion of Thinking collapses real? Rebuttals are preliminary (5 trials per cell, no counts). Puzzle-design critiques about output limits were not searched.
7. Does Abrami's moderator picture survive control-type and quality modelling? Primary paper was blocked (403).
8. What is the true human Gick-Holyoak spontaneous rate? Only second-hand.
9. Do reasoning models (R1, o1 class) benefit from curated memory? Early evidence says minimal or inconsistent.
10. Is lesson transfer directional (easy to hard, hard to easy)?
11. What pruning rule is safe when the judge is weak?
12. Search coverage: the WebSearch quota ran out after four queries and the APIs returned 429. Gaps that need unknown papers (reasoning-task distance curves, frontier composition) are under-searched, not proven empty.

## 11. Sources

[V] = opened and read (full text, PDF or page text this session). [M] = snippet only or not opened. Several [V] education items were read through a secondary summary; marked.

**Philosophy and education**
- [V] Hitchcock, Stanford Encyclopedia of Philosophy, Critical Thinking (McPeck 1981, Ennis 1989, Abrami 2015): https://plato.stanford.edu/entries/critical-thinking/ [a01-a03, b01]
- [V] SEP methods supplement (Abrami four approaches): https://plato.stanford.edu/entries/critical-thinking/methods.html [d19]
- [V, second-hand] Willingham (2019) How to teach critical thinking, NSW Education (reports Thorndike 1923, Gick and Holyoak, Jepson et al., Loewenstein et al., Catrambone, Scherer 2018, Helsdingen 2010, Ritchhart and Perkins): https://education.nsw.gov.au/content/dam/main-education/teaching-and-learning/education-for-a-changing-world/media/documents/How-to-teach-critical-thinking-Willingham.pdf [a05-a12]
- [V] Thorndike and Woodworth (1901): https://psychclassics.yorku.ca/Thorndike/Transfer/transfer1.htm (table values lost) [a04]
- [V, summary only] Abrami et al. (2015), Clearing House Unterricht summary: https://www.clearinghouse.edu.tum.de/wp-content/uploads/2023/12/CHU_KR18_ENG_Abrami_2015.pdf [a13, a14, d18]
- [M] Abrami et al. (2015) primary, Rev Educ Res (HTTP 403): https://journals.sagepub.com/doi/pdf/10.3102/0034654314551063 [d20, b26]
- [M] Abrami et al. (2008) Stage 1: https://journals.sagepub.com/doi/10.3102/0034654308326084 [a15]
- [M] Halpern (1998): https://doi.org/10.1037/0003-066X.53.4.449 [b27]
- [M] Willingham (2007) American Educator: https://www.aft.org/ae/summer2007/willingham [b28]
- [M] Gick and Holyoak (1980, 1983), recalled only [b25]; Experiment 2 numbers come second-hand via [V] arXiv 2505.00603 [d16]
- [V] Harapan et al. (2026) inquiry meta-analysis: https://europepmc.org/article/PMC/PMC13562932 [b07]

**Cognitive training and transfer**
- [V] Sala and Gobet (2017): https://pmc.ncbi.nlm.nih.gov/articles/PMC5724589/ [a16, a17, b04, b05]
- [V] Gobet and Sala (2023): https://europepmc.org/article/PMC/PMC9903001 [b02, b03]
- [V] Fu et al. (2026) WM transfer asymmetry: https://pmc.ncbi.nlm.nih.gov/articles/PMC13553679/ [a18, b06]
- [V] Gabriel and Mushtaq (2026): https://pmc.ncbi.nlm.nih.gov/articles/PMC13056334/ [a19, a20]

**Language models: transfer and robustness**
- [V] Webb, Holyoak and Lu (2023): https://arxiv.org/abs/2212.09196 [a21, a22]
- [V] Wu et al. (2024) Reasoning or Reciting: https://arxiv.org/abs/2307.02477 [a23, b08, b09, c04]
- [V] Mirzadeh et al. (2025) GSM-Symbolic: https://arxiv.org/abs/2410.05229 [b10, c05, c06]
- [V] Shi et al. (2023) GSM-IC: https://arxiv.org/abs/2302.00093 [c07, d03, d04]
- [V] Chen et al. (2024) Premise Order: https://arxiv.org/abs/2402.08939 [c08, d05]
- [V] Li et al. (2024) GSM-Plus: https://arxiv.org/abs/2402.19255 [d06]
- [V] McCoy et al. (2024) Embers of Autoregression: https://arxiv.org/abs/2309.13638 [b12, c09]
- [V] Zhao et al. (2025/26) CoT mirage: https://arxiv.org/abs/2508.01191 [a24, b14, c10]
- [V] Dziri et al. (2023) Faith and Fate: https://arxiv.org/abs/2305.18654 [a27, b11]
- [V] Press et al. (2022) Compositionality gap: https://arxiv.org/abs/2210.03350 [d17]
- [V] Shojaee et al. (2025) Illusion of Thinking: https://arxiv.org/abs/2506.06941 [a28, b13]
- [V] Lawsen (2025): https://arxiv.org/abs/2506.09250 [d01]
- [V] Song, Yue and Zhang (2025): https://arxiv.org/abs/2507.17699 [d02]
- [V] Sprague et al. (2025) To CoT or not: https://arxiv.org/abs/2409.12183 [a26]
- [V] Huang et al. (2024) Self-correction: https://arxiv.org/abs/2310.01798 [b15]
- [V] Zhou et al. (2022) Algorithmic reasoning: https://arxiv.org/abs/2211.09066 [b16]
- [V] Ruis et al. (2025) Procedural knowledge: https://arxiv.org/abs/2411.12580 [a29]
- [V] Gandhi et al. (2025): https://arxiv.org/abs/2503.01307 [a30]
- [V] arXiv 2505.00603 (2025) analogical reasoning for strategic decisions: https://arxiv.org/abs/2505.00603 [d15, d16]
- [V] Wang et al. (2023) Towards understanding CoT prompting: https://arxiv.org/abs/2212.10001 [d07]
- [V, abstract and figure labels only] Min et al. (2022): https://arxiv.org/abs/2202.12837 [d08]
- [V] Pfau, Merrill and Bowman (2024): https://arxiv.org/abs/2404.15758 [d09]

**Training and transfer in models**
- [V] Huan et al. (2025): https://arxiv.org/abs/2507.00432 [a25, b17, c01-c03]
- [V] Chu et al. (2025): https://arxiv.org/abs/2501.17161 [b18]
- [V] Xie et al. (2025) Logic-RL: https://arxiv.org/abs/2502.14768 [b19]
- [V] Ma et al. (2025) General-Reasoner: https://arxiv.org/abs/2505.14652 [c11]
- [V] Chen et al. (2023) Skill-it: https://arxiv.org/abs/2307.14430 [c17]

**Memory, scaffolds, agents**
- [V] Wang et al. (2024/25) Agent Workflow Memory: https://arxiv.org/abs/2409.07429 [a31, b20, c14]
- [V] Zhao et al. (2024) ExpeL: https://arxiv.org/abs/2308.10144 [a32, b21]
- [V] Suzgun et al. (2025) Dynamic Cheatsheet: https://arxiv.org/abs/2504.07952 [b22, c12, d12]
- [V] Ouyang et al. (2026) ReasoningBank: https://arxiv.org/abs/2509.25140 [b23, c13, d13, d14]
- [V] Zhou et al. (2024) Self-Discover: https://arxiv.org/abs/2402.03620 [b24]
- [V] Xiong et al. (2025) memory management, experience-following: https://arxiv.org/abs/2505.16067 [d10, d11]
- [V] Yasunaga et al. (2024) Analogical prompting: https://arxiv.org/abs/2310.01714 [c15]
- [V] Yang et al. (2024) Buffer of Thoughts: https://arxiv.org/abs/2406.04271 [c16]
- [V] Wang et al. (2023) Voyager: https://arxiv.org/abs/2305.16291 [c18]
- [M] Tang et al. (2025) AgentKB: https://arxiv.org/abs/2507.06229 [c19]
- [M] Wang et al. (2024) Can in-context learning generalize out of distribution: https://arxiv.org/abs/2410.09695 [c21]
- [M] Mind2Web (Deng et al.) and WebArena (Zhou et al.) benchmarks; split definitions taken from the agent papers [c22]

**Not re-opened in the critique pass:** Sala and Gobet, Gobet and Sala, Abrami, Sprague, Dziri, Shojaee, Webb et al., McCoy, Chu, ExpeL. Treat as seen once.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 8 established claims: 4 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D05.06-K02** (now single-source: the sources are not independent). Numbers match (music 0.03 active vs 0.25 passive; WM 0.05 vs 0.18; second-order grand mean 0.00 with active controls), but both sources are by the same lab (Sala and Gobet), the 2023 paper re-using their 2019 meta-analytic data; the 332 samples is the whole dataset while the 0.00 grand mean rests on the 142 active-control samples.
- **D05.06-K03** (reworded: the sources support less). Sala and Gobet show effects shrink with active controls in music, WM and chess training, not that 'every' far-transfer effect is partly artefact; chess had only one active-control study and the authors' conclusion is contested; the prompt-control step is a design inference, not a finding. Corrected claim: In cognitive-training meta-analyses (Sala and Gobet), far-transfer effects shrink toward zero when active rather than passive controls are used, which points to passive-control or expectation artefacts in those literatures; by analogy, a scaffold test should include an equal-length placebo prompt.
- **D05.06-K08** (reworded: the sources support less). Embers numbers are right but they show sensitivity to the probability of the output or input text (GPT-4 word reversal 97% vs 53%, rot-13 21% vs 11%), not pretraining frequency of the task form; the only distinct listed source is this one paper (c25 is blank). Corrected claim: LLM accuracy on deterministic tasks depends on how probable the text is (Embers of Autoregression, GPT-4): word reversal 97% when the answer is a high-probability sentence vs 53% when low-probability; rot-13 21% for high-probability input vs 11% for low-probability input. The same paper also reports task-frequency effects (common vs rare variants of a task).
- **D05.06-K28** (reworded: the sources support less). Wang et al. (text-davinci-002, Table 2): invalid reasoning keeps 39.5/48.5 GSM8K answer accuracy (about 81%), but 9.6 vs 43.9 is intermediate-step recall, not task accuracy (answer accuracy 11.0 vs 48.5); incoherent-only prompts keep about half (23.1 vs 48.5), and Bamboogle drops far less; single model setting. Min et al. (random labels) does not bear on scaffold relevance. Corrected claim: In Wang et al. (InstructGPT, GSM8K), CoT demonstrations with invalid reasoning keep about 80-90% of CoT performance (answer accuracy 39.5 vs 48.5), while relevance-free rationales fall to 11.0 answer accuracy (intermediate-step recall 9.6 vs 43.9); incoherent-only rationales keep about half (23.1). Hence a control prompt should vary relevance and coherence separately from correctness.
- **D05.06-K06** (now single-source: only one opened source, code check).
