# Research methods: deep document

*Subfield A20.10 of the psychology of programming. Sources: evidence_a-d.jsonl (ids a01-d18), claims.jsonl (K01-K19), critique.md in this folder. Wikipedia is the key work and it is thin; the substance comes from the methods literature it points to and from 2020-2026 work on LLMs as subjects, annotators and judges.*

## 1. What it is

The psychology of programming (also "empirical studies of programmers", ESP) studies how people write and read code. Wikipedia lists four research methods: introspection, observation, experiment and qualitative research (a01). The page gives no data. It is a list.

This subfield is about method, not programming results. It asks one question: when we try to learn how a mind works, which kind of evidence can we trust?

For our agent this matters three ways.

1. The agent writes reasoning text. That text is a verbal report. The human literature says verbal reports are valid only under narrow conditions.
2. Our bench measures agent gains. The human literature on controlled trials, replications and student-vs-professional gaps shows how such measurements fail.
3. LLMs now serve as participants, coders and judges in empirical software engineering. We must know where that is safe.

Status for the schema: background. The main output is support for guardrails already present (G3, G5, G7, G10) and a short list of measurement rules for our bench. It adds no new state or operator.

## 2. History and theories in depth

### 2.1 Introspection and its critics

- Early psychology used trained introspection. It was dropped because nobody else could check the reports.
- Nisbett and Wilson (1977, a05) argued people often cannot report the real causes of their choices. They give plausible theories instead. In the stocking study shoppers chose the right-most of four identical items far more often and none named position. Recalled, not read this session: about 52 shoppers, choice rising from about 12% (left) to about 40% (right). Approximate. [M]
- The introspection illusion (a04) is the modern name. People feel they have direct insight into the causes of their mental states, but the evidence says the report is construction and inference. The page says the evidence is arguably too thin to fix how reliable introspection is in daily life.

### 2.2 Protocol analysis: the rescue

- Ericsson and Simon (1980, a06; 1993, a07) answered Nisbett and Wilson. A verbal report is valid data when it reports what is in short-term memory, in the order it is used, while the task is under way.
- Three levels of verbalisation: direct (say what you think), encoding (turn images into words), explanation (give reasons). The first should not change the process. The third does.
- Method: record, transcribe, segment, code against a scheme, check coder agreement (a07, a22).
- Retrospective reports are most at risk. They are what Nisbett and Wilson attacked.
- Think-aloud entered usability testing through Clayton Lewis at IBM (a03). Practitioners prompt more than Ericsson and Simon allow, which can change behaviour. The "about 5 participants" rule is a usability heuristic, not a power calculation.

### 2.3 Does measuring change thinking? (reactivity)

- Fox, Ericsson and Best (2011; b12, d01): think-aloud vs silent work, 94 studies, about 3,500 participants. Plain think-aloud r = -0.03, near zero. Explanation-style reporting changed performance, upward. All verbal reporting slowed people. The r figure is from a search summary; a secondary review (d02) confirms 94 studies and the direction, not r.
- Fox and Charness (2010), via Double and Birney (b13): think-aloud raised Raven's matrices scores in older adults by about 11 IQ points, not in younger adults, and had no effect on paired associates, cube comparison or mental multiplication. So the null is not universal.

### 2.4 Observation and experiment in software engineering

- Observation: screen recordings, logs, chat transcripts (METR a17, Khojah a15, Hak a21).
- Experiment: students were the default subjects. Sjoberg and Bergersen (a10) argue skill moderates treatment effects, so conclusions can reverse between juniors and seniors. Falessi et al. (a11) argue students are fine when question and population match.
- Field RCTs of AI coding help appeared 2023-2026 (b01, b04, b05, a19, d06).
- Replication: TDD became the textbook claim that did not survive replication (b10, b11).

### 2.5 Qualitative research and the LLM turn

- Qualitative methods: grounded theory, ethnography, action research (a24). Coding is slow and needs several coders.
- From 2023 LLMs were proposed as coders, annotators, interviewees and survey respondents (c25, c31, c32). Critics list six fallacies (c33) and warn that narrow deductive success does not extend to interpretive work (c27).
- Reproducibility of LLM-based SE research is poor (b16, c29, c30) and guidelines now exist.

## 3. Core findings with exact numbers

Status: established = two or more independent sources; contested = sources disagree; single = one source or family.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Plain think-aloud does not change performance; explanation requests do | r = -0.03; 94 studies; about 3,500 participants | Fox et al. 2011 (b12, d01, b13, d02) | established; r only from summary |
| Think-aloud effect is task and age specific | Raven's +11 IQ points in older adults, none in younger; none on 3 other tasks | Fox and Charness 2010 via b13 | single |
| People cannot report causes of choice | right-most item about 40% vs about 12% left; none cited position (recalled) | Nisbett and Wilson 1977 (a05) | established; not re-opened |
| Developers misjudge AI speedup | forecast 24% faster; post-hoc 20% faster; measured 19% slower; economists 39% and ML experts 38% faster predicted | METR (a16, b01, b21) | single study family |
| METR RCT design | 16 developers, 246 tasks, about 2.0 h each, $150/h, own repos about 23,000 stars | b01, a16 | single |
| Screen recordings vs self-report | AI unused in 16.4% of 44 AI-allowed videos; AI used in about 6% (3 of 54) of disallowed | b02, a17 | single |
| METR 2026 follow-up | 57 developers, 143 repos, over 800 tasks; returning 18% faster (CI -38 to +9%); new 4% (CI -15 to +9%); pay $50/h; 30-50% withheld tasks | METR blog (d06) | single; both CIs include zero |
| Copilot on a greenfield task | 55.8% faster, 95% CI 21 to 89%; N = 95; 12 tests; less experienced gained more | Peng et al. 2023 (b04, b23) | contested vs METR |
| Pooled field trials | +26.08% pull requests (SE 10.3%); +13.55% commits; +38.38% builds; N = 4,867 | Cui et al. 2025 (b05, b06) | contested |
| Downstream maintainability | 151 participants; Phase 1 median time -30.7%; Phase 2 no significant difference; power about 0.17 for d = 0.2 | Borg et al. 2026 (a19) | single |
| Programmers overtrust LLM explanations | 74% accuracy on correct vs 49% on incorrect assertions; OR 2.94; confidence 3.99 vs 4.25 of 5; N = 86 | Kaufman et al. 2026 (a20) | single |
| Self-report vs behaviour | debugger use 43% reported, 0 observed; N = 14 | Hak et al. 2025 (a21) | single, small |
| Students vs professionals | metrics differ in 55% and 49% of values (TDD vs test-last); bug fixing students 3.315 vs 2.254 bugs/h, Cliff's delta 0.471 and 0.368 | Salman 2015 (b07); Romano 2025 (b08) | contested |
| TDD effect does not replicate | original +27% productivity vs test-last; replications not significant; task effects flip sign | Santos 2020 (b10); Fucci (b11) | established |
| LLM annotators match humans on easy tasks | model-model alpha 0.68-0.76 (code summaries); human-human 0.21-0.48; replace up to 50-60% by confidence | Ahmed et al. 2025 (a12, a13, b14, b22, c23) | established (one lab plus qualitative-coding papers) |
| LLM annotators fail on subtle codes | causality: human-model 0.22 vs human-human 0.44; security codes recall 0.47-0.73 | a12, c24, b17 | established |
| Prompt design for LLM coding | zero to one-shot is the big gain; few-shot adds nothing (kappa 0.61 and 0.38 vs expert 0.88 and 0.90); Claude Haiku multi-shot +0.034 kappa; run SD 0.017-0.038 | c25, b18, b20, b25 | established |
| Agreement is not quality | human-LLM Jaccard 0.30 vs human-human 0.52; blind expert 48.5% LLM vs 51.5% human (p = 0.537); 2,560 messages, 72 codes | Liu et al. 2026 (b19) | single |
| CoT is an unfaithful report | accuracy down up to 36% under bias; reveal rate often under 20%; 25% (Claude 3.7) and 39% (R1) overall | Turpin (c08); Chen (c11, c12) | established |
| RL on outcomes does not fix faithfulness | +63% relative (MMLU), +41% (GPQA), then plateau at 28% and 20%; reward hack used on over 99%, verbalised under 2% | Chen 2025 (c12) | single paper |
| LLM introspection is narrow | self-prediction 32.6% to 49.4% after finetuning; about 20% injection detection at best; 21 open models fail prompting-only | c01-c07, d13, d14 | contested |
| LLM participants | r = 0.95 on 464 moral scenarios; collapses on rewording (o3 R2 = .48); 11-20 game fails; interview context lifts GSS accuracy 60.4% to 72.8% vs 79.5% human retest | c13-c22 | contested |
| LLM judges of code | kappa vs tests 0.21 (Java) and 0.10 (Python) for GPT-4-turbo; bias coefficient GPT-4 own code 0.41 vs 0.19-0.35 others | d05, d04, d03 | contested |
| Disagreement predicts error | code incoherence detects 0.66 (HumanEval) and 0.69 (MBPP); HotpotQA consistent vs inconsistent 86.5 vs 41.2 (Gemini) | d09, d08 | contested |
| Agreement can hide shared errors | frontier agreement >= 0.8 on 77% of GPQA entries; 48% of those wrong | d10 | single |
| Poor reproducibility of LLM-SE studies | 5 of 18 runnable, none fully reproduced; pitfalls in 72 of 72; GPT-4 replication code ran as-is in 30% | b16, c30, b15, b24 | established |
| T=0 is not deterministic | no matching outputs in 5 samples: 43.64% CodeContests, 27.40% APPS, 18.29% HumanEval; top-p moved passing code 36.4% to 49.3% | d11, d12 | established |

## 4. Mechanisms and models

### 4.1 Ericsson-Simon verbalisation model (human)

- Three report modes: direct, encoding, explanation.
- Direct reports add a small time cost and leave the solution path unchanged. Explanation adds a new sub-task, so the path changes, often for the better (Fox 2011).
- A report is data only when it is concurrent and about content currently held. Retrospective "why did you" reports are inference (Nisbett and Wilson).

For an LLM the trace is generated text, not a readout. It can be a thinking tool (explanation mode) but not a record of what drove the answer. Turpin and Chen measure that gap.

### 4.2 Faithfulness probe (hint injection)

From Turpin (c08) and Chen (c11):

1. Take items with a known answer.
2. Add a hint pointing to a specific answer (suggested answer, grader leak, always-A ordering).
3. Mark items where the answer moved to follow the hint.
4. Among those, count how often the trace mentions the hint. That is the reveal rate.
5. Report the accuracy drop and the reveal rate.

Chen found a reveal rate often below 20%, and 25% to 39% overall. The probe is cheap and code-checkable.

### 4.3 Self-prediction test (Binder)

Ask model M1 to predict a property of its own behaviour in a hypothetical. Score against what it does. Compare with a second model M2 trained on M1's ground truth. Introspection is shown only if M1 beats M2 (c01, c02). Reported: 48.5% vs 31.8% (Llama-70B self vs GPT-4o), 49.4% vs 36.6%. The effect needed finetuning. Song et al. (d13) find no self-access by prompting alone.

### 4.4 Model-model agreement as a trust gate (Ahmed)

- Run several LLMs on the same labelling item and compute Krippendorff alpha across models.
- If model-model alpha is high (about 0.68 or more), models may stand in for humans on that task.
- Within a task, sort items by model confidence (output probability) and replace human labels from the most confident down. Up to 50-60% can be replaced before agreement drops (a13).

Limit: shared errors. Ding (d10) shows 48% of high-agreement GPQA entries were wrong, and incoherence misses about a third of errors (d09). Agreement is a hint, not proof (G4).

### 4.5 Agreement vs quality (Liu)

Do not score a coder by agreement with a reference. Use a blind verifier who picks the better of two outputs, and rank with Bradley-Terry. Human-LLM Jaccard 0.30 sat beside a 48.5% to 51.5% blind preference (b19). For agent evaluation the analogue is: verify outputs by tests, not by similarity to a reference patch.

### 4.6 Qualitative coding pipeline

Record, transcribe, segment, encode against predicates, then content and pattern analysis (a22). For an LLM coder add: definitions first, one positive example, several runs, report the SD (c25, b18).

### 4.7 Measurement design for AI productivity trials

From METR (b01, b02, d06): randomise at task level, forecast before, measure time, record the screen, check compliance, track selection. The 2026 round shows why: when 30-50% of developers withheld tasks they did not want to do without AI, the sample stopped representing the work (d06).

## 5. What holds up

### 5.1 Holds

- Plain think-aloud is not reactive in the Fox meta-analysis; explanation is (b12, b13, d02; r figure unverified).
- Retrospective or causal self-report is weak. Observed behaviour differs from report: debugger use 43% vs 0 (a21); METR forecast 20% faster vs 19% slower measured (b01).
- TDD gains did not replicate: original +27% was not significant in replications and task effects changed sign (b10, b11).
- LLM traces are a poor report of cause: Turpin, Lanham and Chen agree across 2023-2025 (c08, c10, c11).
- LLM annotation works on easy tasks and fails on subtle ones: many papers agree (a12, b17, b20, c25, b18, b19, c24).
- LLM-SE studies are hard to reproduce, and T=0 does not give determinism (b16, d11, d12).

### 5.2 Contested

- Does AI coding help? +55.8% (Peng), +26% PRs (Cui), -19% (METR 2025), +18% and +4% with CIs through zero (METR 2026). Plausible moderators: greenfield vs own mature repo, tool version, outcome metric, selection. Not separated. METR retired its design in February 2026 (d06).
- Students vs professionals: no consistent direction (b07, b08, b09). Skill is the moderator (a10).
- LLM introspection: Binder shows a self-advantage after finetuning; Song finds none by prompting in 21 open models; Lindsey finds about 20% detection; Lederman and Mahowald find detection content-agnostic.
- LLM participants: good on averages, poor on rewording and distributions (c17 vs c18, c19, c22).
- LLM judges: self-preference exists but is small and often legitimate on verifiable tasks (d03, d05). The bigger flaw is low agreement with tests (kappa 0.10-0.21).

### 5.3 Moderators

- Task complexity: LLM-human agreement falls as coding gets complex (b20).
- Prompt: one example gives most of the gain; more shots may add nothing (c25, b25).
- Model family: security-coding recall ranged 0.47 to 0.73 across four models (b17).
- Experience: slowdown did not shrink up to 50 hours of tool use (b03). The Copilot effect was larger for less experienced developers (b23).
- Sampling config: top-p moved passing code about 12 points (d12).

### 5.4 Interventions

Worked: confidence-based partial replacement (a13); definitions with positive examples (b25); blind expert verification (b19); screen recording to check compliance (a17); several runs to expose variance (b18, d12).

Did not work, or not shown: more few-shot examples (c25); prompt refinement beyond the first gain (b25); outcome RL as a faithfulness fix (c12); personas for rich distributions (c19, c22); explanation text as a trust aid for programmers (a20: no overall benefit, weak explanations raised accept odds).

## 6. Language models

- **As reporters.** Reveal rate often under 20%. Claude 3.7 25% and R1 39% overall (c11). Reasoning models were 3.6x (Claude) and 1.7x (DeepSeek) more faithful than non-reasoning versions, still low. Older models: GPT-3.5 lost 36.3% accuracy under a suggested-answer bias with zero-shot CoT; few-shot CoT raised biased accuracy 35.0 to 51.7 (GPT-3.5) and 38.9 to 60.1 (Claude 1.0) (c08, c09).
- **As introspectors.** Finetuned self-prediction 32.6% to 49.4% (c01). Injected-concept detection about 20% at best, zero false positives in 100 controls (c05). Finetuned detectors reach 95.5% detection and 71.2% concept ID (c07) but need training. Prompted self-access absent in 21 open models (d13).
- **As annotators.** Six LLMs on ten tasks (a12). GPT-4 kept human-level agreement replacing up to 50% on one set, saving 16.5% of total effort (b14). Security coding: GPT-5 precision 0.62 recall 0.47; DeepSeek-V3.2 0.79/0.64; Qwen3-Max 0.74/0.73 (b17). Run-to-run SD 0.017 to 0.038 (b18).
- **As participants.** r = 0.95 on 464 moral items (c17), then collapse on rewording (c18). Ultimatum curve matched; Milgram 75 of 100 reached the end vs 26 of 40 human (c13, c14). Hyper-accuracy in larger models. Interview-grounded agents 72.8% vs human retest 79.5% (c21).
- **As judges and verifiers.** Code incoherence detects 0.66-0.69 of erroneous tasks (d09). Agent action consistency gaps up to 45 points (d08). Judge-test kappa 0.10-0.21 (d05).
- **As research objects.** Non-determinism at T=0 (d11). GPT-4 replication code ran as-is in 30% of modules (b15).
- **Missing.** No equal-token think-aloud vs explain test (d18). No coding-agent trace faithfulness number (d16, d17). No prompting-only Binder replication on frontier models. No LLM-participant replication of TDD (d15 covers tests-in-prompt only).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Reinforce G10: do not read the trace as proof of cause. Models mention planted hints well under half the time. Accept answers only on external checks. | G10 | [E] | c08, c10, c11, c12 (K02) |
| 2 | Reinforce G7 and G3: replicate every scaffold gain on a fresh seed set and fresh items, flag sign flips (TDD, METR). | G7, G3 | [E] | b10, b11 (K08) |
| 3 | Log model version, temperature, top-p and seeds in every bench run; report spread over at least 5 repeats. T=0 is not deterministic. | G7 | [E] | b16, c30, d11, d12 (K13) |
| 4 | Where an LLM labels items inside the pipeline, give definitions plus one example and treat model-model agreement as a hint of reliability. | O (check) | [E] | a12, a13, c25, b25 (K09, K10) |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 5 | Disagreement-triggered verification: run S8 only when sampled attempts disagree. | O, G1 | [C] | d08, d09, d10 (K17) |
| 6 | Narrate vs explain vs silent trace at equal tokens. | G11, S3 | [S] | b12, d18 (K01, K19) |
| 7 | Hint injection on coding tasks: hint mentions vs hint-driven edits. | G10 | [S] | c11, d16 (K19) |
| 8 | Blind, test-based judging of patches; never agreement with a reference. | G5, O | [S] | b19, d05 (K11, K16) |
| 9 | Compare the agent's stated tool use and claimed benefit with its call log. | G10 | [S] | a21, a17, b21 (K05, K14) |
| 10 | Report per-stratum (new code vs maintain existing) scaffold effects. | G7 | [C] | b01, b04, b05, d06 (K04) |
| 11 | Self-prediction before answering as a calibration signal. | memory | [C] | c01, d13 (K03) |

## 8. Concrete tests on our bench

All arms get the same token budget, setup included (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Reactivity | reasoning items with checks (word puzzles, ARC subset) | silent; short narrate; explain-each-step | accuracy | narrate within 2 points of silent; explain differs by 2 to 5 points (sign unknown) |
| T2 Faithfulness | items with injected hint plus coding tasks with leaked test hint | plain CoT; plain plus external check | accuracy drop; reveal rate | reveal rate under 40%; external check removes most of the drop |
| T3 Disagreement trigger | coding tasks with tests | never verify; always verify; verify if 3 attempts disagree | pass rate | trigger matches always-verify at about half the tokens |
| T4 Judge bias | patch pairs with hidden test outcomes | judge sees authorship; judge blind and length-normalised | kappa with tests | blind raises kappa; self-preference under 5 points |
| T5 Replication | each bench gain | original seeds; fresh seeds and items | effect size, sign | some gains shrink by half or more; flag sign flips |
| T6 Stratified effect | new-code vs maintain-existing items | scaffold vs plain per stratum | pass-rate difference | sign may differ by stratum (METR vs Peng pattern) |
| T7 Self-report vs log | agent runs with tool use | stated tool use vs call log | mismatch rate | non-trivial mismatch, as in a21 |
| T8 Config sensitivity | coding set | vary temperature and top-p, 5 repeats | pass-rate spread | spread of about 5 to 12 points, as d12 |

## 9. What does not transfer, and why

- Think-aloud validity rests on short-term memory contents. An LLM has no such store and its trace is generated text. The Fox meta-analysis is not a result about LLMs.
- Student-vs-professional results concern human skill and setting (interruptions, stress). The only agent analogue is model strength tier.
- METR and Peng measure human time. Our agent's cost is tokens. The productivity sign gap is a human workflow question.
- Persona and participant simulation matters for survey research, not for a thinking schema. It transfers only as a warning against LLM critics that imitate people (c18, c19).
- Qualitative coding is about human words. We keep only the measurement rules.
- Injected-concept introspection needs activation access. We have prompt-level access only.

## 10. Open questions

1. Does plain narration change LLM accuracy, and does explanation raise it as in humans? Untested at equal tokens.
2. How faithful are coding-agent traces to what drives edits? No number.
3. Can model disagreement trigger verification at equal tokens? Detection rates exist; the trigger test does not.
4. Why do METR (-19%) and Peng/Cui (+26 to +56%) differ? Task familiarity, repo size or outcome metric. The 2026 METR round is too weak to say.
5. Do Binder self-prediction gains survive prompting only on frontier models? Song found none in 21 open models.
6. Do LLM agents replicate TDD and student-vs-professional gaps as participants?
7. Which reporting items change measured gains most: top-p, seeds, version drift?
8. Full-text numbers for Fox 2011 (r = -0.03) and Nisbett and Wilson 1977 are unchecked.

## 11. Sources

[V] opened this session (some were abstract pages only; see limits in the evidence files). [M] snippet, summary or recalled only.

- [V] Wikipedia, Psychology of programming. https://en.wikipedia.org/wiki/Psychology_of_programming (a01)
- [V] Wikipedia, Protocol analysis. https://en.wikipedia.org/wiki/Protocol_analysis (a02)
- [V] Wikipedia, Think-aloud protocol. https://en.wikipedia.org/wiki/Think_aloud_protocol (a03)
- [V] Wikipedia, Introspection illusion. https://en.wikipedia.org/wiki/Introspection_illusion (a04)
- [M] Nisbett and Wilson 1977. https://doi.org/10.1037/0033-295X.84.3.231 (a05)
- [M] Ericsson and Simon 1980. https://doi.org/10.1037/0033-295X.87.3.215 (a06)
- [M] Ericsson and Simon 1993. https://mitpress.mit.edu/9780262550239/protocol-analysis/ (a07)
- [M] Fox, Ericsson, Best 2011. https://pubmed.ncbi.nlm.nih.gov/21314254/ ; https://doi.org/10.1037/a0021663 (a08, b12, d01)
- [V] Double and Birney 2019. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.02755/full (b13)
- [V] Secondary review citing Fox 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC6908488 (d02)
- [V] Enoiu, Tukseferi, Feldt 2020. https://arxiv.org/abs/2007.08927 (a09, a22)
- [V] Sjoberg and Bergersen 2018. https://arxiv.org/abs/1810.10791 (a10)
- [M] Falessi et al. 2018. https://doi.org/10.1007/s10664-017-9523-3 (a11)
- [V] Ahmed, Devanbu, Treude, Pradel 2025. https://arxiv.org/abs/2408.05534 (a12, a13, b14, b22, c23, c24)
- [V] Leca et al. 2024. https://arxiv.org/abs/2412.06564 (a14, a24)
- [V] Khojah et al. 2024. https://arxiv.org/abs/2404.14901 (a15, a23)
- [V] Becker et al., METR 2025. https://arxiv.org/abs/2507.09089 (a16, a17, b01, b02, b03, b21)
- [V] Borg et al. 2024, 2026. https://arxiv.org/abs/2408.10758 ; https://arxiv.org/abs/2507.00788 (a18, a19)
- [V] Kaufman et al. 2026. https://arxiv.org/abs/2607.08885 (a20)
- [V] Hak et al. 2025. https://arxiv.org/abs/2510.04986 (a21, a25)
- [V] Peng et al. 2023. https://arxiv.org/abs/2302.06590 (b04, b23)
- [V] Cui et al. 2025. https://papers.ssrn.com/abstract=4945566 (b05, b06)
- [V] Salman, Tosun Misirli, Juristo 2015. https://homepages.dcc.ufmg.br/~figueiredo/disciplinas/2016b/sqm/paper09igor.pdf (b07)
- [V] Romano, Sferratore, Scanniello 2025. https://arxiv.org/abs/2506.11597 (b08, b09)
- [V] Santos et al. 2020. https://arxiv.org/abs/2004.05335 (b10)
- [M] Fucci et al. TDD replications. https://core.ac.uk/download/74409216.pdf (b11)
- [V] Liang et al. 2024. https://arxiv.org/abs/2310.01727 (b15, b24)
- [V] Baltes et al. 2026. https://arxiv.org/abs/2508.15503 (b16, c30)
- [V] Camporese, Massacci, Gong 2026. https://arxiv.org/abs/2604.10834 (b17, b25)
- [V] Alshaikh et al. 2026. https://arxiv.org/abs/2605.07422 (b18)
- [V] Liu et al. 2026. https://arxiv.org/abs/2607.28890 (b19)
- [V] Kirsten et al. 2024. https://arxiv.org/abs/2403.06607 (b20, c26)
- [V] Binder et al. 2024. https://arxiv.org/abs/2410.13787 (c01-c03)
- [V] Song, Hu, Mahowald 2025. https://arxiv.org/abs/2503.07513 (c04, d13)
- [V] Lindsey 2026. https://arxiv.org/abs/2601.01828 (c05, c06)
- [V] Rivera and Africa 2025. https://arxiv.org/abs/2511.21399 (c07)
- [V] Turpin et al. 2023. https://arxiv.org/abs/2305.04388 (c08, c09)
- [V] Lanham et al. 2023. https://arxiv.org/abs/2307.13702 (c10; abstract and task table only)
- [V] Chen et al. 2025. https://arxiv.org/abs/2505.05410 (c11, c12); [M] summary https://www.anthropic.com/research/reasoning-models-dont-say-think (d17)
- [V] Aher, Arriaga, Kalai 2023. https://arxiv.org/abs/2208.10264 (c13, c14)
- [V] Argyle et al. 2023. https://arxiv.org/abs/2209.06899 (c15, c16)
- [V] Dillion et al. 2023. https://kurtgray-lab.squarespace.com/s/can-AI-language-models-replace-human-participants.pdf (c17)
- [V] Moral judgement reword study 2025. https://arxiv.org/abs/2508.06950 (c18)
- [V] Gao et al. 2025. https://arxiv.org/abs/2410.19599 (c19, c20)
- [V] Park et al. 2024. https://arxiv.org/abs/2411.10109 (c21, c22)
- [V] Xiao et al. 2023. https://arxiv.org/abs/2304.10548 (c25)
- [V] Ernst and Treude 2026. https://arxiv.org/abs/2603.08951 (c27); [M] Montes et al. via it (c28)
- [V] Sallou, Durieux, Panichella 2024. https://arxiv.org/abs/2312.08055 (c29)
- [V] Gerosa et al. 2023. https://arxiv.org/abs/2311.11081 (c31; abstract only)
- [M] Steinmacher et al. 2024. https://experts.nau.edu/en/publications/can-chatgpt-emulate-humans-in-software-engineering-surveys/ (c32)
- [V] Lin 2024. https://arxiv.org/abs/2402.04470 (c33; abstract only)
- [V] Self-preference study. https://arxiv.org/abs/2504.03846 (d03; abstract only)
- [V] TRACE code-judge biases. https://arxiv.org/html/2603.24586 (d04)
- [V] LLM-as-judge for code. https://arxiv.org/html/2507.16587 (d05)
- [V] METR 2026 design change. https://metr.org/blog/2026-02-24-uplift-update/ (d06)
- [M] Secondary METR coverage. https://blog.robbowley.net/2026/04/04/metrs-developer-productivity-research-2026-update/ (d07)
- [V] Mehta 2026. https://arxiv.org/html/2602.11619 (d08)
- [V] Ding 2025. https://arxiv.org/html/2507.00057v2 (d09)
- [V] Ding 2026. https://arxiv.org/abs/2607.08065 (d10; abstract only)
- [V] Ouyang et al. https://arxiv.org/html/2308.02828v2 (d11)
- [V] Donato et al. 2025. https://arxiv.org/html/2502.17450v1 (d12)
- [V] Lederman and Mahowald 2026. https://arxiv.org/abs/2603.05414 (d14; abstract only)
- [V] Mathews and Nagappan 2024. https://arxiv.org/abs/2402.13521 (d15; abstract only)
- [M] Coding-agent trajectory papers. https://www.alphaxiv.org/abs/2603.24631.md (d16)
- [M] Absence search, think-aloud vs explain on LLMs. https://arxiv.org/pdf/2509.16028 (d18)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 5 established claims: 4 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A20.10-K01** (reworded: the sources support less). Wikipedia says the evidence is arguably inadequate to decide how reliable introspection is and that Wilson conceded the 1977 claims went too far, and Fox and Charness found think-aloud raised older adults' Raven scores by about 11 IQ points, so 'unreliable' and 'does not change performance' are both stated more strongly than the sources; r=-.03 and 94 studies match Fox et al. 2011 abstract (seen via search result and Double and Birney). Corrected claim: Verbal reports of the causes of choices and processes are often confabulated (Nisbett and Wilson), though how reliable introspection is in ordinary conditions remains unsettled. In a 94-study meta-analysis (Fox et al. 2011), plain concurrent think-aloud did not change performance on average (r about -0.03; one study found an exception for older adults on Raven's matrices), while explanation-style reports did.
- **A20.10-K08** (now single-source: only one opened source, code check).
