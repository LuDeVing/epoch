# Analogical prompting for LLMs: deep document

Scope: the prompt method in which a language model first writes related problems (with solutions) from its own memory, then solves the target. Founding paper: Yasunaga et al., arXiv 2310.01714 (ICLR 2024). Our schema slots: S3 (generate, variant) and O7 (map an analogue). Evidence ids (a01..d19) refer to evidence_a-d.jsonl in this folder. Claim ids (K01..K23) refer to claims.jsonl. Status tags: [E] established, [S] single-source, [C] contested.

Bottom line first. The founding gains are small (1 to 4 points on GSM8K and MATH with GPT-3.5), have no seeds or intervals, and were not reproduced by an independent group on the same model. Effects depend on the backbone: small gains on GPT-3.5 and GPT-4-turbo, losses on several open models, and no test at all on reasoning-trained models. The best-supported mechanism is a process effect (writing a related problem inside the same prompt), not the content of the recalled problems. Nobody has measured the method against plain CoT with self-consistency at equal tokens. That is the main gap.

## 1. What it is

The method (a01, c01). One prompt tells the model: recall K relevant and distinct problems, write each with its solution, then solve the new problem. No labels, no retrieval, no second call. The model replaces the human who would write few-shot demos, and replaces a retriever that would fetch similar problems.

Settings in the founding paper (a01):
- GSM8K: K=5. MATH and BIG-Bench Hard (BBH): K=3.
- Codeforces (level-A 2023 problems): K=3 plus a "knowledge" step (the model first writes a tutorial on core algorithms), then the exemplars, then the solution.
- Temperature 0 for math and BBH. Codeforces temperature 0.7 with 10 samples (Acc@1, Acc@10).
- The prompt asks the exemplars to be "distinct" (diverse). For text-davinci models the authors added an in-context demonstration of how to write exemplars. Other models got none (critique note 5). So the davinci rows and the GPT-3.5 row are not the same prompt.

Related ideas:
- Zero-shot CoT (Kojima 2022, a14): "think step by step". The main baseline.
- Few-shot CoT (Wei 2022, a15): hand-written demos. The other baseline.
- Auto-CoT (Zhang 2022, a16): model-written demos chosen by clustering.
- SG-ICL (Kim 2022, a17): model writes demos for classification, conditioned on the test input.
- Generated Knowledge (Liu 2022, a18) and Recitation (Sun 2023, a19): the model writes facts or passages first.
- Self-ICL (Chen 2023, a20): model writes pseudo-inputs, labels them, uses them as demos.
- Step-Back (Zheng 2023, a22): ask for the principle first, then solve.
- Thought Propagation (Yu 2023, a23): propose analogous problems, solve each separately, reuse their solutions. More calls.
- Self-Demos (Lin 2024, c25): write demos between the given ones and an out-of-distribution query.

Why it matters to us: it is the only prompt-level, no-training version of "recall a related problem" (S3 variant, operator O7). It is cheap to implement. The question is whether it pays for itself under guardrail G7 (win at equal tokens).

## 2. History and theories in depth

Human roots (a24, a25). Gick and Holyoak (1980) showed that people given Duncker's radiation problem rarely find the convergence solution alone. After reading a fortress story with the same structure, and after a hint to use it, many succeed. The lesson: unaided analogy rarely transfers. The source must be noticed and mapped. We did not verify their percentages (a25 not opened). Do not cite numbers from that line.

Theory behind it: structure mapping (Gentner) says match relations, not surface features. Yasunaga frame the method as the LLM playing the human who recalls past problems. Their ablation that "knowledge before exemplars" beats the reverse (a06, b07) fits the structure view: a principle steers recall toward the true method, not surface likeness.

LLM precursors, in order:
1. Kojima 2022 and Wei 2022: reasoning in text lifts accuracy on large models.
2. Min et al. 2022 (a21, b18): in classification demos, random labels cost only 0 to 5 points. Format and input distribution matter more than label correctness.
3. Kim 2022 SG-ICL (a17, b15, c10): one self-generated sample is worth about 0.6 gold samples. Conditioning generation on the test input helps relevance and lowers variance.
4. Zhang 2022 Auto-CoT (a16, b16, b17): similar retrieved demos made errors repeat (46.9% vs 25.8% still unresolved). Diverse cluster sampling fixed much of it. 1 to 2 wrong demos out of 8 did not hurt.
5. Wang 2023 (b19): invalid steps in CoT demos keep most of the gain (about 80 to 90% on older models). Relevance to the query and order of steps matter.
6. Chen 2023 Self-ICL (a20), Liu 2022 knowledge (a18).
7. Yasunaga 2023/2024 (a01-a08): the founding paper.

Challenge phase:
- Qin et al. (2024, ACL 2025) "Relevant or Random" (a09-a13, c06-c08, d01-d05): relevance is not what matters in math. Accuracy of the examples is.
- Zhang 2026 (b09, b10, d08) and CodeSim (b11): third-party comparisons with analogical prompting below CoT.
- Luo et al. 2025 LBS3 (d09, d10): five models, eight tasks. Gain on GPT models, loss on open models.
- Michelman et al. 2025 (d15): Gemini 1.0, loss on some BBH tasks.
- Gwak et al. 2026 (c09, d06, d07): "Not the Example, but the Process". The gain exists only when recall and solve are in the same prompt.

Extension phase (2025 to 2026):
- Cognitive Tools (Ebouky 2025, b12-b14): "recall related" as one tool among four.
- Wang 2025 "From Harm to Help" (d12, d13): worked demos hurt reasoning-trained models. Turning them into insights first helps.
- Shen, Druckmann, Zou 2026 (b25, c23, d16): cross-domain relational analogy search for open research problems.
- Euclid geometry proofs (c24): analogous retrieved proofs plus a verifier.
- Lewis and Mitchell 2024 (b20, c17, d17), Lee et al. 2025 (b24, c21): why LLM analogy is brittle outside training patterns.

Competing explanations for any gain:
1. Relevance: the recalled problems carry the method (founding claim). Weakened by Qin.
2. Accuracy of recalled solutions (Qin: yes in math).
3. Extra generation: more tokens of reasoning before the answer.
4. Process: writing a related problem inside the same stream changes how the model attends and solves (Gwak).
5. Format priming: demos teach the output format (Min). This can explain gains on short-answer tasks and losses when the format breaks.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Self-generated exemplars beat 0-shot CoT and 5-shot CoT on math, GPT-3.5-turbo | GSM8K 75.0 (0-shot) / 75.8 (0-shot CoT) / 76.7 (5-shot CoT) / 77.8 (ours). MATH 33.0 / 33.9 / 34.9 / 37.3 | Yasunaga 2024 (a02, b01) | [S] single group, no seeds |
| Same on other models | text-davinci-003 GSM8K 14.8 / 50.3 / 54.0 / 61.0. PaLM 2 GSM8K 60.8 / 78.2 / 80.7 / 81.7; MATH 27.1 / 29.8 / 34.3 / 34.8 | Yasunaga (a02) | [S] |
| Competitive programming (Codeforces, 50 problems) | GPT-3.5-16k Acc@1/Acc@10: 0-shot 8/24, 0-shot CoT 9/27, 3-shot CoT 11/27, exemplars 13/25, knowledge+exemplars 15/29. GPT-4: 16/30, 16/29, 17/31, 17/32, 19/37 | Yasunaga (a03) | [S] 1 to 2 problem differences |
| BBH, five tasks, GPT-3.5 (0-shot / 0-shot CoT / 3-shot CoT / ours) | Word sorting 66.8/67.6/68.4/75.2; logical deduction 30.0/35.2/36.4/41.6; temporal sequences 40.4/44.8/58.0/57.6; colored objects 50.4/61.6/62.0/68.0; formal fallacies 53.6/55.6/55.6/58.8 | Yasunaga (a04, b04, c03) | [S] |
| Needs a strong model (GSM8K: 0-shot CoT / fixed 5-shot / retrieved / ours) | davinci-003 50/54/57/61; davinci-002 43/47/48 (ours 48); davinci-001 10/11/9 (ours 9); curie 2/3/2 | Yasunaga Table 4 (a05, b02, c04; corrected in critique) | [S] |
| Number of exemplars | K=1 76.1 / 34.8; K=3 77.5 / 37.3; K=5 77.8 / 37.1 (GSM8K / MATH) | Yasunaga (a05, b05) | [S] |
| Diversity instruction | GSM8K 77.8 vs 75.9 non-diverse; MATH 37.3 vs 35.2 | Yasunaga (a06) | [S] |
| Knowledge before exemplars beats after | Codeforces gain as above; order ablation | Yasunaga (a06, b07) | [S] |
| Self-consistency stacks on the method | 85.3 GSM8K / 46.0 MATH (a different arm, not token-matched) | Yasunaga (a06) | [S] |
| Manual error analysis | 100 cases (50 right, 50 wrong). Correct group: 6 irrelevant, 9 relevant but wrong, 35 relevant and correct. Wrong group: 10 irrelevant, 12 relevant but wrong, 28 relevant and correct yet unsolved (12 generalization gap, 8 over-reliance on one exemplar, 8 other) | Yasunaga (a07, b06, c05) | [S] authors only, no inter-rater check |
| Independent replication fails on math (GPT-3.5, 500 items per set, 3 seeds; GSM8K / MATH / mean) | Relevant 71.5 / 33.3 / 52.4; N/A 75.5 / 36.1 / 55.8; random-same 75.1 / 36.3 / 55.7; random-diff 76.3 / 34.1 / 55.2; random-bio 75.3 / 34.6 / 54.9 | Qin 2025 (a09, d02) | [C] relevant arm is below Yasunaga's own 0-shot (75.0), but Qin used own wording and did not re-run baselines |
| Same direction on four more models | GSM8K relevant vs fixed checked set ICL-math: Llama-2-70B 45.1 vs 55.5; Llama-3-8B 69.5 vs 75.8; Llama-3.1-8B 74.8 vs 80.2; Qwen2.5-14B 86.5 vs 91.1. Also CSQA 70.8 vs 74.6, MBPP 58.2 vs 62.0, GPQA 31.6 vs 35.8 | Qin (a13, d03, d04) | [S] one lab |
| BBH: original holds | Relevant 63.2 vs N/A 61.9 on five tasks | Qin (a10) | [S] |
| Example accuracy drives results | Hand-graded 50 MATH examples per arm: relevant 62% correct, N/A 72%, random-same 86%. Cosine similarity to query: relevant 0.54 GSM8K / 0.41 MATH, N/A 0.19 / 0.28 | Qin (a12, c07) | [S] |
| Fixing the answers helps | GSM8K relevant 71.2 to 75.2 with GPT-4 answers (random answers 70.0); MATH relevant 37.0 to 44.4; Llama-2-70B 56.2 to 60.8 | Qin (a12, d01) | [S] part of the lift is a stronger teacher |
| A fixed checked set beats per-query recall | ICL-math 75.7/36.8/56.3 and ICL-bio 77.9/34.9/56.4 vs relevant 52.4 mean (GPT-3.5). Llama-3.1-8B GSM8K: SC5 77.6, Auto-CoT 75.9, ICL-math 80.2 | Qin (a13, d05) | [S] authors' own methods |
| Process, not example (Integrated vs Decoupled) | Integrated about +4.7 over the other arms on average across 5 models (GPT-4o GSM8K 49.9 to 54.6, MATH 33.3 to 37.9). Decoupled (same example pasted in a new call) about zero-shot. Llama-3.3-70B 4-shot: Integrated 38.2 vs Decoupled 32.4. Llama-3.3-70B GSM8K cells 32.67 / 35.19 / 33.59 and MATH 25.26 / 28.34 / 26.69 (zero-shot, Integrated, Decoupled order). GPT-4.1 GSM8K 48.8 to 57.9 (+9.1) | Gwak 2026 (c09, d06, d07) | [S] one group, temperature 0, one run. Absolute GSM8K about 50, so the prompt format is probably restrictive |
| Third-party loss vs CoT | GPT-4o-mini average over 8 benchmarks AP 56.0 vs CoT 60.7 (MATH 65.4 vs 78.3). Near-identical deltas on two other backbones. CoT-SC about 6 points above AP | Zhang 2026 (b09, b10, d08) | [C] prompt not published; identical CoT averages (60.7 vs 60.4) hint at a shared harness |
| Model-dependence across 5 models, 8 tasks | Gain over ZS-CoT on GPT-3.5 and GPT-4-turbo (+3.1, +3.5 average). Loss on Qwen1.5-14B (-1.4), Qwen1.5-72B (-2.8), Llama3-70B (-2.5) | Luo 2025 (d09) | [E] agrees across Qin, Gwak, Luo |
| Loss tail on short-answer symbolic tasks | BBH colored objects: Qwen1.5-72B 50.8 vs ZS-CoT 78.8; Llama3-70B 69.6 vs 85.0. Temporal sequences 43.6 vs 51.6. Gemini 1.0 loses on Tracking Shuffled Objects | Luo (d10), Michelman (d15) | [S] may be answer-format failure |
| Self-ICL (related method) | 23 BBH-type tasks: direct 50.81 to 53.93 (+3.12); CoT 53.22 to 55.54 (+2.32); real 3-shot 55.49; 18-0-5 win-tie-lose vs direct. Temporal sequences 57.6 to 35.6 | Chen 2023 (a20) | [E] small, uneven |
| Reasoning-trained models: worked demos hurt | AIME'25: one R1-style demo -6 to -16 points; three demos up to -35. GPQA-Diamond -1 to -5 (1 shot), -4 to -8 (3 shots). Models 1.7B to 32B | Wang 2025 (d12) | [S] demos are R1 traces, not self-generated |
| Insight first, then solve, helps reasoning models | AIME'25 R1-Distill-7B 42.0/48.0/51.3 (direct/I2S/I2S+); 14B 50.0/54.0/60.0; Qwen3-1.7B 36.0/41.3/42.7. GPQA 14B 59.5/59.6/63.0. Majority@32 slightly above I2S+ on AIME'25 | Wang 2025 (d13) | [S] compute matched by calls, not tokens |
| Cognitive Tools: recall as one tool | Qwen2.5-32B 79.6 to 84.2; Llama3.3-70B 52.8 to 75.1 in an agent loop with other tools. Model rarely calls the tool itself | Ebouky 2025 (b12-b14) | [S] bundle effect |
| Thought Propagation (multi-call) | Shortest-path optimal rate baselines 0.33/0.26/0.22 to 0.65 on GPT-3.5. Tiny gain with GPT-4. Also wins creative writing | Yu 2024 (a23, b21, b22, c15) | [S] authors' own method |
| Step-back (sister method) | PaLM-2L Physics 66.4 to 73.2. GPT-4: CoT 82.9 vs step-back 84.5 | Zheng 2024 (a22, c13) | [S] gains shrink with a stronger model |
| Cross-domain analogy for open ideas | Solution Vendi diversity +90 to 173%. Binary novelty no-domain / cross-domain / AR: Claude 1.6/21.6/50.4%, GPT 8.8/27.2/58.8%, Gemini 8.6/37.9/68.8%. Humans pick AR as more novel 78% (kappa 0.445). AR uses 2 calls | Shen 2026 (d16) | [S] no same-type arm, no correctness |
| Analogous proofs plus verifier | Geometry proof success GPT-5 88 to 96 under a fixed verifier | Euclid study (c24) | [S] verifier gave most of the lift |
| Budget-aware view | At 10k tokens or 20 queries on GPT-3.5/4, CoT-SC is strongest or tied across GSM8K, MATH, TheoremQA, HotpotQA, CSQA | Wang 2024 (d14) | [S] AP not in the comparison |
| Relational transfer is brittle | Letter-string analogies with permuted alphabets: GPT-3/3.5/4 fall sharply, humans stay high. Models fail to carry relations in up to 38.4% of cases | Lewis and Mitchell 2024 (b20, c17, d17); Lee 2025 (b24, c21) | [E] zero-shot tests only |

## 4. Mechanisms and models

Prompt template (implementable). One call:
1. "Problem: {target}."
2. "Recall {K} relevant and distinct problems. For each, write the problem and its solution."
3. "Then solve the initial problem."
Optional first step for code and hard tasks: "First write a tutorial of the core ideas or algorithms." K=3 is the default (a05). K=1 is worse. Use temperature 0 for exact-answer tasks.

Four causal stories, with what each predicts and how it was tested.

A. Relevance transfer (founding story). The recalled problems share a method with the target. The model imitates the method. Predicts: relevant beats unrelated. Test: Qin d02. Result: relevant is worst on 5 of 5 models in math. Not supported there. It holds a little on BBH (63.2 vs 61.9).

B. Accuracy of recalled solutions. A wrong worked example leads the model astray. Relevant problems are harder and the model gets them wrong more often (62% correct vs 72% vs 86%). Predicts: verifying solutions repairs the loss. Test: Qin a12/d01. Replacing answers with GPT-4 answers lifts every arm by 2 to 7 points. Partly supported. A same-model check is untested.

C. Process effect. Writing a related problem and solving it inside the same stream makes the model reason differently. Predicts: the same problem pasted into a fresh prompt gives nothing. Test: Gwak d06/d07. Supported: Integrated about +4.7, Decoupled about 0. Attention analysis on Llama-3.1-8B: Integrated attends more to the self-written example. Single group.

D. Extra generation. More output tokens before the answer, like a longer CoT. Predicts: any plausible text (N/A, random) helps equally. Qin: N/A and random arms match or beat relevant. Consistent with D and with C.

Reconciling Qin and Gwak: both can hold if the gain is a process effect that is hurt by wrong content. The method then works as a warm-up whose benefit is capped by the accuracy of what it writes.

Failure mechanisms:
- Over-reliance on one exemplar (8 of 50 wrong cases) and generalization gap (12 of 50) (a07). The diversity instruction and K>=3 address the first.
- Error contagion from similar demos (Auto-CoT: 46.9% vs 25.8% unresolved) (a16, b16).
- Model too weak to write valid problems (davinci-001 loses) (a05).
- Answer-format failures on short-answer symbolic tasks (d10, d15). Cause unconfirmed.
- Brittle relational transfer under counterfactual changes (b20, b24).
- On reasoning-trained models, worked demos in context hurt (d12).

Variants worth implementing as options:
1. Recall a strategy, not a worked answer (I2S, d13): "name the key insights from similar problems, then solve." Gains reported on reasoning models.
2. Easy-to-hard proxies (LBS3, d11): ask for easy then hard related problems, solve easy first. Hard-only proxies beat easy-only in their runs.
3. Fixed verified bank (Qin ICL-math, c08): write a handful of problems once, check them, reuse for every query. No per-query recall cost.
4. Multi-call: solve each recalled problem separately, aggregate (Thought Propagation). More tokens.
5. Cross-domain relational search (Shen d16) for open tasks: extract the relational structure, generate analogies from other domains, search for solutions. 2 calls.

Cost model. Per query, output tokens grow by roughly K times (problem plus solution). Input exemplar tokens fall to zero versus few-shot CoT (a08, b08, K16). No paper reports a cost-matched comparison against CoT-SC. Qin Table 12 shows SC5 (77.6) above relevant recall (74.8) on Llama-3.1-8B, not token-matched (d05).

## 5. What holds up

Holds (three or more independent groups):
- The effect is small and depends on the backbone: gains on GPT-3.5 and GPT-4-turbo, losses on several open models (Qin, Gwak, Luo) [E] K19.
- Self-generated context gives modest, uneven gains with a real loss tail [E] K09 (Self-ICL, SG-ICL, generated knowledge, Analogical).
- Wrong demos are tolerated on label tasks, not in open-answer math [E] K11.
- Similar-looking demos can spread errors. Diverse ones are safer [E] K12.
- LLM relational transfer is brittle off distribution [E] K13.

Failed or contested:
- Founding gain on GPT-3.5 math: not reproduced by Qin. Their relevant arm is 3.5 to 4 points below Yasunaga's own 0-shot. But Qin used a different prompt and different subsets (500 items, 3 seeds). The gap is not isolated [C] K02.
- Third-party comparisons put AP below CoT (Zhang 2026, CodeSim). Cause unknown, no prompt published [C] K10.
- Qin's relevant arm replicated the direction on four more models and three more tasks, but it is one lab.
- Luo et al. (independent) find AP below ZS-CoT on three open models and above on GPT-3.5/4-turbo. A model-strength story is plausible but not proven.

Moderators found:
- Model strength to write valid problems (a05).
- Task type: BBH symbolic short answers lose most (d10). Math with open answers is sensitive to example accuracy (a12).
- K: K=1 worse, K=3 to 5 flat (a05).
- Diversity instruction: +1.9 GSM8K, +2.1 MATH (a06).
- Integrated vs separate call (d06).
- Backbone class: reasoning-trained models are hurt by worked demos (d12).

Interventions that worked:
- Verified or corrected recalled answers (a12, d01): +2 to +7 points.
- A fixed, checked set instead of per-query recall (a13): about +4 points over per-query relevant, lower cost.
- Knowledge-first for code (a03): +2 Acc@1 on 50 problems.
- Insight-first flow on reasoning models (d13): +4 to +10 on AIME'25 distilled models.
- Cross-domain recall for novelty (d16).

Did not work or not shown:
- Relevance as such (Qin).
- Decoupling recall from solving (Gwak).
- Retrieval of similar problems as a fix (Auto-CoT error contagion).
- Multi-call analogical methods on strong models (TP tiny on GPT-4, step-back +1.6 on GPT-4).

Methodological weak spots (critique): the founding paper has no seeds, one prompt, 2023 models. Codeforces is 50 problems. The manual error analysis has no inter-rater check. Most positive third-party evidence comes from authors of competing methods. Gwak's absolute GSM8K of about 50 suggests a restrictive format. Post-cutoff benchmarks are untested (K23).

## 6. Language models

How models behave:
- 2023 chat models (GPT-3.5, PaLM 2): small gains, +1 to +5 points on math (a02). Codeforces gains are 1 to 2 problems.
- Weak models (davinci-001, curie): negative or null. Fixed or retrieved labeled demos win (a05).
- Open instruction models (Llama-2/3/3.1, Qwen1.5/2.5): per-query relevant recall loses to N/A recall and fixed sets on all models Qin tried (by 2.5 to 6.3 points on GSM8K against N/A), and loses to ZS-CoT on three models in Luo (-1.4 to -2.8 average).
- Modern strong chat models (GPT-4o, GPT-4.1, Llama-3.3-70B): Gwak finds Integrated gains of +2 to +9 (GPT-4.1 GSM8K 48.8 to 57.9) from a low base. Zhang finds AP 4.7 points below CoT. Opposite signs, unresolved.
- Gemini 1.0 (Pro, Ultra): loses on Tracking Shuffled Objects and Colored Objects vs CoT (d15).
- Reasoning-trained models (R1 distills, Qwen3, o-series, Claude thinking): no test of self-generated recall exists. Worked demos in context cost 6 to 35 points on AIME'25. Converting demos to insights first recovers and exceeds direct accuracy (+4 to +10).

By how much, in one line: when it helps it adds about 1 to 5 points on math from a weak base. When it hurts it costs 1 to 3 points on average and up to 28 points on single tasks. Per-query relevance is not what drives it.

Loss tail by task: short-answer symbolic BBH tasks (colored objects, temporal sequences, tracking), and weaker open models. Unknown whether this is reasoning harm or answer-format failure (K20).

Self-consistency comparisons: Yasunaga's own SC add-on reaches 85.3 / 46.0, but that is a different arm. CoT-SC is above AP by about 6 points in Zhang and above relevant recall in Qin's Llama-3.1-8B row. The budget-aware study finds CoT-SC wins at equal tokens against other strategies (AP excluded).

Contamination: Yasunaga used 2023 level-A Codeforces. Recall of "related problems" from training data may partly be recall of the benchmark itself. No post-cutoff test found (d18, d19, K23).

Analogy ability itself (not the prompt). Webb, Holyoak and Lu (a24, c16): zero-shot GPT-3 (text-davinci-003) matched or beat undergraduates on text matrices (N=40), letter strings (N=57) and verbal analogies (N=57), and was worse on story analogies (N=54). On the radiation problem it needed the right source story, failed with two distractors, and succeeded when told to consider previous stories. Lewis and Mitchell (b20, c17, d17): permuted alphabets make GPT models fall while humans stay high. AnaloBench (c20): finding the right analogue in a large pool is the hard part. Scale did not fix it. Lee 2025 (c21): the relation is encoded in middle layers but often not applied to the new entity.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence | What to do |
|---|---|---|---|---|
| Treat self-generated recall as a modest, task-dependent aid with a loss tail. Never run it by default | S3 / G7 / G1 | [E] | K09, K19; a20, d09, d10 | Gate O7 per backbone and task class with a 20-item pilot, recall vs plain. Log the class delta in S9. Off until the pilot wins. |
| Verify recalled worked solutions before use on open-answer tasks | G2 / G3 / S4 | [E] (that wrong answers hurt) | K11; a12, d01, b19 | If a recalled solution is used as a demo, code checks it (re-solve, or run it). Drop disagreements. |
| Prefer diverse recalled items over near copies. Avoid error contagion from one near neighbour | S3 / O7 | [E] | K12; a16, b16, a06 | Recall prompt asks for distinct problems. K=3 default. |
| Do not expect unaided analogy to transfer under counterfactual or altered rules | O7 / G3 | [E] | K13; b20, c17, b24 | Test the mapping in code on the unfitted part. Do not trust a recalled analogy that was not tested on the target. |
| Count recall tokens as output cost | G7 | [E] (principle) | K16 | Every O7 or S3-recall arm is compared at equal total tokens. |

Not added to the schema: nothing here justifies running recall on every item. Section 4b of the schema already lists unstructured self-reflection as a non-add. The same logic applies to ungated recall. O7 stays impasse-only (G1).

### Test first

| Item | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|
| Recall-then-solve vs plain CoT vs CoT-SC at equal tokens on our backbone | S3, O7 | [C] | K01, K02, K10, K16 | No paper has this comparison. Decides whether recall stays. |
| Relevant vs unrelated vs no recall (same wording) | S3, O7 | [C] | K02, K03 | Separates relevance from extra generation. |
| Integrated (one stream) vs Decoupled when recall is an S3 state | S3 | [S] | K08 | Decides how S3 is built. Default to one stream meanwhile (cheap). |
| Same-model verification of recalled problems, and its cost | G3, O7 | [S] | K03 | Does it recover the accuracy loss? At what tokens? |
| Fixed verified bank vs per-query recall | S3, memory | [S] | K21; a13, d05 | A bank belongs in memory. Cheaper if it wins. |
| Strategy-only recall vs worked-example recall on a reasoning backbone | S3, O7 | [S] | K17, K18 | Reasoning backbones may be harmed by worked demos. |
| Counterfactual and post-cutoff variants | O7, G3 | [S] | K13, K23 | Does recalled analogy mislead? |
| Cross-domain vs same-type recall on open tasks, blind judged | O7 open mode, G8 | [S] | K14, K22 | Novelty must be judged by running or blind humans, not by the model. |
| Per-task gating from the loss tail | S0 | [S] | K20 | Predict harm from task features. |

## 8. Concrete tests on our bench

All arms get the same total token budget (input plus output, recall tokens counted). 3 seeds. Report the paired difference with a 95% interval. At least 500 items for main tests, 20 for pilots. Bench: the HTSA harness (ARC items, BrainTeaser, math sets).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | GSM8K and MATH subsets, plus a post-cutoff math set; our backbone | (a) plain short CoT; (b) CoT-SC at the token budget of (c); (c) one-prompt recall K=3 then solve | Accuracy; accuracy per 1000 tokens | (c) at or below (b) by 1 to 5 points (Zhang, Qin Table 12). (c) above (a) by 0 to 3 on GPT-class, negative on open models. |
| T2 | Same items | (a) relevant recall; (b) unrelated recall (Qin N/A); (c) no recall, same wording otherwise | Accuracy; recalled-solution accuracy graded by a checker | (b) >= (a) on math by 2 to 4 points as in Qin. If (a) >= (b), the relevance story survives. |
| T3 | Same items | (a) Integrated (one stream); (b) Decoupled (recall in call 1, solve in call 2 with the problem pasted); (c) zero-shot | Accuracy | (a) beats (c) by about 3 to 5. (b) about equals (c) (Gwak). |
| T4 | Same items | (a) unchecked recall; (b) recall plus same-model re-solve, drop disagreements; (c) fixed verified bank | Accuracy; extra tokens | (b) +2 to +6 over (a) (Qin with GPT-4 answers). (c) >= (b) at lower cost. |
| T5 | ARC-style items with a check, impasse only | (a) S6 with O1-O6 only; (b) S6 with O7 worked recall added; (c) S6 with O7 as strategy-insight recall | Solve rate on items that reached S6 | O7 adds little (0 to 2 points). Insight recall is best on reasoning backbones. |
| T6 | Reasoning-trained backbone; AIME-like and GPQA-like items | (a) direct; (b) worked-recall then solve; (c) insight-first then solve; (d) CoT-SC | Accuracy | (b) below (a) by 5 or more points (Wang 2025). (c) above (a) by 3 to 8. (d) about equals (c). |
| T7 | Counterfactual variants of our tasks (changed symbols or rules), plus the originals | (a) plain; (b) recall then solve | Accuracy drop from original to counterfactual | Recall widens the drop (recalled analogies from training data mislead). |
| T8 | Open idea tasks (BrainTeaser-style or idea generation) | (a) same-type recall; (b) cross-domain recall; (c) no recall | Blind-judged novelty and usefulness (human or run-based); count of distinct ideas | (b) above (c) on novelty by 20+ points (Shen). (b) vs (a) unknown. |
| T9 | BBH-style short-answer symbolic tasks | (a) plain; (b) recall; (c) recall graded with a lenient answer extractor | Accuracy; format-error rate | Part of (b)'s loss disappears in (c) if the loss is format failure. |
| T10 | Pilot gate | 20 items per class, recall vs plain | Per-class delta | Used by S0 to set the mode per class. |

## 9. What does not transfer, and why

- Gains measured on 2023 GPT-3.5 and PaLM 2 do not carry to current strong or reasoning-trained models. Gains shrink as the base gets stronger (step-back and TP on GPT-4), and worked demos hurt reasoning models.
- Codeforces numbers (50 problems, 1 to 2 problem differences) are not evidence for our bench.
- Human analogy findings (Gick and Holyoak) concern noticing a source from a different domain. The LLM method recalls same-type textbook problems, closer to schema retrieval than to distant analogy. O7's "distant analogue" role is only weakly served by this method.
- Self-generated examples cannot carry knowledge the model lacks. The model's own memory is the only source, so it repeats its own blind spots and may recall benchmark items.
- Multi-call methods (Thought Propagation) gain through more calls. Under G7 and G9 (extra sampling is not independent), their gain cannot be credited to analogy without a token-matched control.
- Cross-domain novelty gains (Shen) are scored by LLM judges, checked against humans at kappa 0.445. Our G8 says model judges are near chance for novelty. These gains do not transfer without running or blind-human checks.
- Cognitive Tools gains (Qwen2.5-32B 79.6 to 84.2; Llama3.3-70B 52.8 to 75.1) come from a four-tool bundle in an agent loop. They cannot be credited to recall alone.
- The Euclid proof gains (GPT-5 88 to 96) come mostly from a formal verifier. They support G2 and G3, not analogy.

## 10. Open questions

1. Does recall-then-solve beat plain CoT and CoT-SC at equal tokens on a modern chat model? (K16; no data.)
2. Is the gain from relevance, accuracy, extra generation, or process? A clean four-arm test with one wording is missing.
3. Does Gwak's Integrated vs Decoupled result replicate outside one group, and with S3 as a separate state?
4. Does same-model verification of recalled problems recover Qin's accuracy loss, and at what token cost?
5. Why do Zhang 2026 and CodeSim find AP below CoT? Need the exact prompts. Re-run with Yasunaga's published prompt.
6. What happens on reasoning-trained models with self-generated (not R1-written) recall?
7. Counterfactual or novel-rule variants: does recall mislead?
8. Distant vs same-type recall: does cross-domain beat same-type on correctness, not only novelty?
9. Which task features predict the loss tail (format-bound short answers, weak backbones)?
10. Post-cutoff benchmarks: are the gains partly benchmark recall?
11. Does a strong model need K recalled problems, or is one targeted insight enough?

## 11. Sources

[V] = opened this session (page or PDF text read). [M] = snippet or abstract level only.

- [V] Yasunaga et al. (2024) Large Language Models as Analogical Reasoners. https://arxiv.org/abs/2310.01714 (a01-a08, b01-b08, c01-c05)
- [V] Qin et al. (2025) Relevant or Random: Can LLMs Truly Perform Analogical Reasoning? https://arxiv.org/abs/2404.12728 and https://arxiv.org/pdf/2404.12728 (a09-a13, c06-c08, d01-d05)
- [V] Gwak et al. (2026) Not the Example, but the Process. https://arxiv.org/abs/2602.15863 (c09, d06, d07)
- [V] Zhang et al. (2026) Learning Global Hypothesis Space (GHS-TDA). https://arxiv.org/abs/2602.09794 (b09, b10, d08)
- [V] Luo et al. (2025) Let's Be Self-generated via Step by Step (LBS3), Findings of ACL. https://aclanthology.org/2025.findings-acl.795.pdf (d09-d11)
- [V] Michelman et al. (2025) Enhancing Reasoning with Collaboration and Memory. https://arxiv.org/pdf/2503.05944 (d15)
- [V] Wang et al. (2025) From Harm to Help: reasoning in-context demos for reasoning LMs. https://arxiv.org/pdf/2509.23196 (d12, d13)
- [V] Wang et al. (2024) Reasoning in Token Economies: budget-aware evaluation. https://arxiv.org/pdf/2406.06461 (d14)
- [V] Islam et al. (2025) CodeSim. https://arxiv.org/abs/2502.05664 (b11; table extraction garbled, block-to-model mapping uncertain)
- [V] Ebouky, Bartezzaghi, Rigotti (2025) Eliciting Reasoning in Language Models with Cognitive Tools. https://arxiv.org/abs/2506.12115 (b12-b14)
- [V] Kojima et al. (2022) Large Language Models are Zero-Shot Reasoners. https://arxiv.org/abs/2205.11916 (a14, c12)
- [V] Wei et al. (2022) Chain-of-Thought Prompting. https://arxiv.org/abs/2201.11903 (a15)
- [V] Zhang et al. (2022) Automatic Chain of Thought Prompting. https://arxiv.org/abs/2210.03493 (a16, b16, b17, c11)
- [V] Kim et al. (2022) Self-Generated In-Context Learning. https://arxiv.org/abs/2206.08082 (a17, b15, c10)
- [V] Liu et al. (2022) Generated Knowledge Prompting. https://arxiv.org/abs/2110.08387 (a18)
- [V] Sun et al. (2023) Recitation-Augmented Language Models. https://arxiv.org/abs/2210.01296 (a19)
- [V] Chen et al. (2023) Self-ICL. https://arxiv.org/abs/2305.15035 (a20, c14)
- [V] Min et al. (2022) Rethinking the Role of Demonstrations. https://arxiv.org/abs/2202.12837 (a21, b18)
- [V] Zheng et al. (2023) Take a Step Back. https://arxiv.org/abs/2310.06117 (a22, b23, c13)
- [V] Yu, He and Ying (2024) Thought Propagation. https://arxiv.org/abs/2310.03965 (a23, b21, b22, c15)
- [V] Wang et al. (2023) Towards Understanding Chain-of-Thought Prompting. https://arxiv.org/abs/2212.10001 (b19)
- [V] Webb, Holyoak and Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196 (a24, c16; not re-opened in the final pass)
- [V] Lewis and Mitchell (2024) Using Counterfactual Tasks to Evaluate the Generality of Analogical Reasoning. https://arxiv.org/abs/2402.08955 (b20, c17, d17)
- [V] Hu et al. (2023) In-Context Analogical Reasoning with Pre-Trained Language Models. https://arxiv.org/abs/2305.17626 (c18; not re-opened)
- [V] Choi et al. (2024) AnaloBench. https://arxiv.org/abs/2402.12370 (c20; not re-opened)
- [V] Shen, Druckmann and Zou (2026) Unlocking LLM Creativity in Science through Analogical Reasoning. https://arxiv.org/abs/2605.11258 (b25, c23, d16)
- [V] Lin et al. (2024) Self-Demos. https://arxiv.org/abs/2404.00884 (c25)
- [V] OpenAlex citation scan of works citing Yasunaga. https://api.openalex.org/works?filter=cites:W4387355871 (d18)
- [M] Gick and Holyoak (1980) Analogical problem solving, Cognitive Psychology 12:306-355. https://doi.org/10.1016/0010-0285(80)90013-4 (a25; numbers not verified)
- [M] Lee et al. (2025) The Curious Case of Analogies. https://arxiv.org/abs/2511.20344 (b24, c21; abstract and intro)
- [M] Euclid-geometry study, Reliable Proof Generation with LLMs via Analogical Reasoning. https://arxiv.org/abs/2505.14479 (c24)
- [M] Jiayang et al. (2023) AnalogyKB. https://arxiv.org/abs/2305.05994 (c19)
- [M] Jiang and Merlo (2026) Analogical Structure, Minimal Contextual Cues and Contrastive Distractors. https://arxiv.org/abs/2511.10441 (c22)
- [M] Singhal and Singhal (2025) Analogy-Driven Financial Chain-of-Thought. https://arxiv.org/abs/2509.12611 (c26)
- [M] Chen et al. (2025) DeFine. https://arxiv.org/abs/2410.01772 (c27)
- [M] Which Prompting Technique Should I Use? (2025). https://arxiv.org/abs/2506.05614 (b26; its "analogical" prompting is a different method)
- [M] Yang et al. (2026) Batch-of-Thought and other citing papers. https://arxiv.org/abs/2601.02950 (b27)
- [M] LiveCodeBench Pro and The SWE-Bench Illusion (contamination background). https://arxiv.org/html/2506.12286v4 (d19)

Related subfields run in parallel (links only, not covered here): Analogy and distant sources; Tree of Thoughts; Search over thoughts; Comparison and relational language; Vector-space relational similarity; Productive failure; Calibration and overconfidence; Scaffolding and guided discovery; Compression at inference time.
