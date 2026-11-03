# Dialectical reasoning: deep document

*Subfield A19.02, cross-cultural cognition. Written 2026-11-03 from evidence_a-d.jsonl (99 lines), claims.jsonl (K01-K27) and critique.md in this folder. Evidence ids (a01, b05, c14, d10 ...) point to those files. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Dialectical reasoning here means a way of handling two ideas that seem to conflict. Peng and Nisbett (1999) named it from Chinese folk thought. It has three parts:

- **Change.** Things keep changing. Expect reversals, not straight-line trends.
- **Contradiction.** Two opposed statements can both hold some truth. Do not rush to say one is false.
- **Holism.** Parts are linked, so a claim is judged in its context.

They set this against the "Aristotelian" rules of identity, non-contradiction and the excluded middle. When two claims clash there are four moves (a01):

1. Deny that there is a conflict.
2. Discount both claims.
3. Differentiate: pick one side and drop the other (the "logical" move they link to Americans).
4. Dialectical compromise: keep some truth in both (the move they link to Chinese).

The 2010 review recasts it as **naive dialecticism**: a set of lay beliefs about the world, not a general cognitive style (a09). The beliefs are domain specific and switched on by context.

Why it matters for us: schema state S7 (SELECT) says "if two rules still fit, run the one input where they differ". That is the engineering version of "keep two rules alive until a counterexample decides". This document asks what the human and AI literature says about when that is wise, and what it costs.

Honest summary up front. The human founding result is real in the original papers but small-sample and partly contested [C]. The LLM link is by analogy: no study has tested "hold two rules until a counterexample decides" in a scaffold on partly-true items. The best nearby evidence is about external checks, deferral and second views, not about culture.

## 2. History and theories in depth

**Roots.** Western dialectics (Hegel's thesis, antithesis, synthesis; Marx; Riegel; Basseches' 24 dialectical schemata) aims at a non-contradictory higher synthesis. Chinese dialectics (yin-yang, Bian Yi Lu, Mao Dun Lu, Zheng He Lu) tolerates the contradiction and aims at a middle way. Peng and Nisbett say their own decomposition into "principles" is analytic and does not fit the spirit of dialectics (a01). Critics (Ho 2000; Chan 2000, d18; Veraksa, Basseches and Brandao 2022, a25) say the Chinese compromise is mislabelled: dialectical thinking in Basseches' sense means finding hidden contradictions and moving to a more complex view, and naive dialecticism is closer to "dialogical relativism" with no method to settle the conflict. Chan and Ho also argue that dialectical thinking and formal logic are compatible and that it is not specifically Eastern or Western (d18, titles only).

**Founding paper (Peng and Nisbett 1999, a02-a08, b01-b04).** Five studies. Studies 1-2 on proverbs, study 3 on conflict resolution, study 4 on argument preference, study 5 on how two contradictory findings change plausibility. The authors state that neither style is better: it depends. Logic suits scientific exploration, dialectics suits life contradictions (a07). They flag the Needham paradox (did dialecticism cost China in reductive physics?) as speculation. They also admit effects are probably muted in general populations because all samples were students.

**Expectation of change.** Ji, Nisbett and Su (2001, a15, snippet only) and Ji et al. (2008): Chinese predict more reversals and cycles. Choi and Nisbett (2000, a16, snippet) on surprise and holistic theories. The 2010 review (a14) reports Chinese give higher odds that a couple breaks up or childhood enemies become lovers; Canadians follow price trends while Chinese sell on historical patterns; the pattern appears in children aged 11. No effect sizes in the review.

**Naive dialecticism and the Dialectical Self Scale (DSS).** Spencer-Rodgers, Williams and Peng (2010, a09-a14, a19, a20, b05, b06, b25) is the main decade review. Key moves: (a) lay beliefs not a style, (b) measured by the DSS, (c) primable in both Western and East Asian samples, (d) separate from collectivism. Mixed emotion (Williams and Aaker 2002): Asian Americans felt equally complex emotions at mixed ads but less discomfort (a20). Response-style work (Hamamura 2008): lower consistency across positive and negative items in East Asia was mediated by dialectical beliefs (a19).

**Late human work.** A mouse-tracking replication in Japan vs US (Morio et al. 2022, a21/b14). An fMRI study linking dACC activity to dialectical self-belief (Wang et al. 2016, b07). A cost study (Ng 2015 thesis, a23): East Asian Canadians more indecisive. A creativity study (Liu et al. 2015, b12). A first meta-analysis (Spencer-Rodgers et al. 2026, a22/d02): k = 139, N = 23,629, 28 countries; clusters by region; linked to Buddhism and rice farming; unrelated to collectivism or interdependent self-construal.

**LLM phase.** 2023: Jin et al. gave ChatGPT the holism and dialectical scales (a26). 2025: Lu, Song and Zhang reported culture-like holism in generative AI (c04, snippet). Sun and Wang (2025) failed to replicate it with larger item sets (a28). 2026: Hu et al. found reversed human patterns (a27/b20). In parallel, the "Hegelian" prompting line (Abdali et al., c14) and the debate line (Du et al., c18) used dialectic as a method rather than as a cultural trait. We treat those as the practical parts of this subfield.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Proverb preference: culture x language x proverb type interaction | 70 white US undergrads, 41 Taiwanese students at Michigan; F(1,109)=12.45, p<.001; 4 coders, Kendall harmony .92; 8 dialectical and 5 non-dialectical proverbs | Peng and Nisbett 1999 (a02, b01) | [C] failed replication d01 |
| Proverb preference, Chinese vs US scientists | 32 Chinese, 34 US natural-science grad students; culture x type F(1,64)=9.17, p<.01; no difference for non-dialectical proverbs | a03 | [C] |
| Resolve mother-daughter conflict dialectically | US 26% vs Chinese 72%; chi2(1,64)=13.61, p<.001 | a04, b02 | [S] |
| Resolve school-vs-fun conflict dialectically | US 12%, Chinese about half; chi2(1,64)=8.50, p<.01 (gap comes from the US side) | a04 | [S] |
| Argument preference index (0-4), Galileo and first-cause topics | Chinese M=2.22 (SD 1.07), US M=1.56 (SD 1.05); t(1,65)=2.53, p<.05; n=32/34 | a05, b03 | [S] |
| Two contradictory findings: plausibility change | 102 Michigan, 136 Beijing undergrads; culture x condition F(1,237)=7.90, p<.01. US: plausible statement rated higher when contradicted, F(1,101)=5.10. Chinese: less plausible rated higher F(1,101)=6.90, more plausible rated lower | a06, b04 | [S] only study with Chinese in China |
| Failed replication of proverb part | Same Exp 2 stimuli plus a new set: no Chinese-US difference in preference for dialectical proverbs; Chinese rated all proverbs more familiar and (set 1) more poetic. N not read (abstract only) | Friedman, Chen and Vaid 2006 (d01) | failure |
| Expectation of change | Chinese give higher odds of reversals (breakup, enemies become lovers); effect also in age-11 children; no effect sizes in review | Ji et al. 2001/2008 via a14 | [S] second-hand |
| Priming raises forecast of change | Yin-yang prime moved Euro-Americans familiar with East Asia (Alter and Kwan 2009). Climate prime on Chinese: chi2(2)=4.99, p=.082, V=.207, stable 5.2% vs 0% (marginal) | a10, b13 | [C] |
| National difference in climate forecast | Study 1: chi2(2)=8.71, p=.013, V=.235; stable 23.2% vs 6.6%; increasing 64.6% vs 81.6% | Li et al. 2021 (b13) | [S] |
| Sub-facets barely correlate | Korea: r=.15 contradiction-change, r=.09 ns interdependence-holism, r=.13 attention-change; DSS vs interdependent self r=.08 (US), .06 (China) | a11, a12 | [E] |
| Dialecticism is not collectivism | Meta-analysis k=139, N=23,629, 28 countries: unrelated to collectivism, linked to Buddhism and rice farming, weak link to globalisation, no shift over two decades | a22, d02 | [E] (abstract only) |
| Mixed emotion, mouse tracking | Japan 59, US 68; duration F(1,125)=5.28, eta2=.041; fluctuation F(1,125)=5.59; alpha of contradiction scale .50 Japan, .75 US | Morio et al. 2022 (a21) | [S] |
| Mixed emotion not stable across designs | 160 US, 158 China: no culture effect on mixed-emotion indices, only on discomfort, direction by ad valence | Zheng et al. 2021 (b08) | [C] |
| dACC and dialectical self-belief | r=.71, p<.01, N=27 Chinese; three-way interaction F(1,23)=18.42 | Wang et al. 2016 (b07) | [S], likely inflated |
| Age | Older adults reason more multi-perspective: n=247 (t=10.26 vs young, 7.97 vs middle); n=200 (t=3.54, 3.05) | Grossmann et al. 2010 (b15) | [S] |
| Cost: indecisiveness | East Asian Canadians more indecisive; N=59, 511, 104; naive dialecticism mediates | Ng 2015 thesis (a23) | [S] |
| Cost: creativity | N=489 Chinese; negative DT-creativity link mostly in non-art majors (n=203, DT M=41.88) | Liu et al. 2015 (b12) | [C] |
| Replication context | Many Labs 2: Norenzayan 2002 intuitive-reasoning effect replicated (N=7,396, d=0.86); 125 samples, 15,305 participants; 14-15 of 28 effects replicated; 57% had d<.20 | b10, b11 | different effect, not support |
| GPT on Analysis-Holism Scale | GPT-3.5 5.35 (SD .11), GPT-4 5.01 (SD .10) vs human 4.87 (SD .49, N=702); 10 runs, temp 1 | Jin et al. 2023 (a26, c01) | [S] fragile |
| GPT on Dialectical Self Scale | GPT-3.5 4.59 vs human 4.00 (SD .54, N=158), p<.001; GPT-4 3.97 (p=.344, no difference); triad relational share .87 and .85 | a26, c02, c03 | [S] fragile |
| LLM cultural tendencies fail with more items | 8 models, 30-60 items vs 4-21 originally, temp 0. Expectation of change: language effect p=.917. Attribution: 62.5% of models insensitive, sensitive ones move <0.2 point; origin effect 0.0897 vs -0.0437, p=.4826. Syllogisms: p=1. Knowledge vs reasoning accuracy .401 vs .339, d=0.097, p=.0248 | Sun and Wang 2025 (a28, c05-c08) | [E] |
| Machine culture reversed | 8 tasks, 2x2 origin x language: Chinese model more collective (3.17 vs 2.81) and more individual (4.75 vs 4.67) attribution; US model more relational categorisation (8.10 vs 6.04, d=1.38) | Hu et al. 2026 (a27, b20) | [C] |
| Persona prompting moves values | Cultural distance GPT-4o 2.42 to 1.57, GPT-4-turbo 2.71 to 1.77, GPT-4 2.69 to 1.65, GPT-3.5-turbo 3.35 to 2.83; better for 71-81% of countries. WVS: r=-.70 with distance from US, 94,278 respondents, 65 nations | Atari 2023, Tao 2024 (c09-c11) | [E] |
| Thesis-antithesis-synthesis checks on 21 LLMs | GSM8K: O3 pT 97.1 / pS 93.6 / OC 95.5; GPT-5 pS 82.0 / OC 81.4; GPT-5-nano pS 84.4 / OC 15.5. MMLU: Llama-3.3-70B 85.1 to 58.3; GPT-4.1-mini pS 54.7; O1 91.1 to 90.3; GPT-5-chat loses over 40 points on GSM | Abbasloo 2026 (c12, c13) | [S] |
| Hegelian prompting loop | GSM-Symbolic GPT-4o .852 to .884 (+3.8%), GPT-4o-mini .709 to .770 (+8.6%), Qwen2.5-7B .587 to .623 (+6.1%); GSM-hard Qwen3-8B .585 to .658 | Abdali et al. (c14) | [S] |
| Antithesis pipeline, small models, oracle context | Mean gain thesis to synthesis: Phi-mini 27.8, Phi-medium 33.6, Gemma-2B 21.7, Gemma-9B 18.3, Llama-8B 35.4 points. Over CoT on WikiHop: +11.6, +10.6, +15.6, +3.8, +1.9 | Candussio 2026 (c16, c17) | [E] small models only |
| Debate beats single agent | 3 agents, 2 rounds: arithmetic 81.8 vs 67.0/69.0/72.1; GSM8K 85.0 vs 77.0; MMLU 71.1 vs 63.9; 20 GSM8K: Bard 11, ChatGPT 14, debate 17 | Du et al. (c18, c19) | [C] |
| Debate vs voting at equal calls | 36 configs, about 6 calls: debate beat CoT in about 15%. GPT-4o-mini GSM8K: CoT 93.60, SC 95.67, SoM debate 94.93; MMLU CoT 80.73, SC 82.13, SoM 74.73. Qwen2.5-7B average: single .7205, vote .7691, best debate .7377 | Zhang 2025, Choi 2025 (d04, d06) | [E] debate not better at equal cost |
| Mixed-model debate | Heter-SoM +6.4% vs same-model SoM, +5.8% vs CoT average; Heter-EoT +8.2% / +4.4%; some sets negative (MBPP -2.0 to -10.8) | d05 | [S] |
| Sycophancy | 58.19% of cases (43.52% to correct, 14.66% to wrong, persistence 78.5%). Full rebuttal persuasion 56.1%, casual "sure" 84.5%, "are you sure" 93.9% | SycEval, Kim and Khashabi (c22, c23) | [E] |
| Holding a stance | SYCON-Bench debate: o3-mini 4.97 of 5 turns, Qwen2.5-72B 4.90, DeepSeek-R1 4.85; Qwen2.5-7B 0.83, Llama-3.1-8B 2.44. Third-person prompt: up to 63.8% more turns held. Critic gate: Claude Sonnet 4 9.6% to 1.4% | d08, d09 | [S] |
| Self-correction without oracle | GPT-3.5 keeps first GSM8K answer 74.7%. With oracle: GPT-3.5 75.9 to 95.5, GPT-4 84.3 to 97.5. No oracle: GPT-4 CommonSenseQA 89.7 to 85.5 | Huang et al. 2024 (c20, c25, d17) | [E] |
| Real checker recovers part | CRITIC GSM8k ChatGPT: PoT 72.5, +CRITIC 78.2 (+5.7), oracle 83.9 (+11.4), no-tool +4.5; text-davinci-003 +1.1 with tool, no tool -1.8. TabMWP LLaMA-2-70B: 59.0 to 75.0 (+16), oracle 92.0 (+32.3) | Gou et al. 2024 (d11) | [E] |
| Hypothesis refinement with a symbolic checker | GPT-4 ACRE task accuracy: IO 28.0, SC 29.0, SR 32.0, refine T=1 N=5 48.0, T=3 N=5 59.0. Raw: 64.0, 65.0, 70.0, 82.5. MiniARC refine 18.7 vs IO 33.1 (loses). Model fails to apply its own rules | Qiu et al. 2024 (d14) | [S] closest to S7 |
| Early commitment | First answer attempt in first 20% of conversation: 30.9; in last 20%: 64.4. Average multi-turn drop 39%; reasoning models no better | Laban et al. 2025 (d10) | [S] |
| Self-contradiction detection | GPT-4 F1 52.2% vs humans 66.7%; finer error categories add 10-15 F1 | Liu et al. 2024 (b22) | [S] |
| Opposite-role critic | Role swap shifts blame in over 20% of cases (GPT-5.1 about 5%). FinQA-TAS: 4B ReTAS Acc 71.2, flip 12.4; QwQ-32B dual view 54.9 / 18.1; GLM-4.6 43.1 / 52.7 (dual view worse than single) | Li et al. 2026 (d15) | [S] |
| LLMs rarely flag input contradictions | All tested models incl. GPT-5.2 asserted a single answer in most cases; top models find about 60% of contradictory needles | Ostling and Kurfali 2026 (a29) | [S] |

## 4. Mechanisms and models

This section turns the findings into pieces an engineer can build. Items marked "analogy" are our extrapolation, not a tested design.

### 4.1 The four responses as a decision menu (a01)

Given two rules R1 and R2 that both fit the examples seen so far:

- **Deny**: assume the data is wrong. Costly; only if a check shows the example is noisy.
- **Discount both**: drop both and search again. This is what S5/S6 already do.
- **Differentiate**: pick one. This is the default, the cheap path, and the right one when a vote or a check is decisive.
- **Compromise**: keep both, each with a stated domain where it holds. Right when both are partly true (a rule that works in one region of the input space and not another).

Study 5 showed that Americans polarised (the more plausible side got stronger when contradicted) and Chinese moved toward the middle (a06). In agent terms: the scaffold should not let the contradiction itself raise confidence in the favoured rule. That is checkable in code (log confidence before and after the conflicting evidence).

### 4.2 Two-rules-alive loop (analogy to S7; closest tested form is d14)

```
rules = propose N candidate rules (N = 2..5), from DIFFERENT sources if possible
for each rule: record scope (inputs it claims to cover)
while budget remains and len(rules) > 1:
    case = find_discriminating_input(rules)   # code, not the model: an input where outputs differ
    if no case: break                         # equivalent on all reachable inputs -> commit by vote
    truth = run_external_check(case)          # tool run, test, retrieved fact, held-out example
    rules = [r for r in rules if r.predict(case) == truth]   # kill only on a failed case
    if len(rules) == 0: restore rules, widen scope, go to S5/S6
commit: shortest / most general surviving rule (S7 order)
```

Design points, each with evidence:

- **Kill only on a failed case, never on model opinion.** Qiu et al. (d14) keep N candidate rules and let a symbolic interpreter filter them. GPT-4 ACRE task accuracy goes 28.0 (IO), 29.0 (SC), 59.0 (refine). The model's own critique gives 32.0.
- **The counterexample must be external.** Pure self-critique does not help (c20, c25: GPT-3.5 keeps first answer 74.7%; GPT-4 CommonSenseQA 89.7 to 85.5). A tool-based check recovers about half of the oracle gain (d11: 5.7 of 11.4; 16 of 32.3). A survey finds no robust self-correction without reliable external feedback (d12).
- **The second rule should have a different source** (another model, retrieved text, a tool-derived rule). Same-model second views add little beyond voting (d03, d04, d06); different models help +5.8 to +8.2% (d05). Forcing the same model to play opponent is weak (d15: dual view worse than single for GLM-4.6).
- **Defer commitment while a deciding case can still arrive.** First answers made early in staged evidence average 30.9 vs 64.4 when made late (d10). This is the expectation-of-change half of dialecticism: a committed rule stays revisable.
- **Commit when no checker can produce a deciding case.** Otherwise the loop spends tokens for nothing and may lose accuracy (synthesis drops on MMLU, c13; debate loses to SC, d04, d06).

### 4.3 Thesis-antithesis-synthesis as a prompt (c14, c15, c16)

Three calls. State a view (thesis). List its defects and the phenomena it cannot explain (antithesis). Write a third view that explains how the two agree and oppose (synthesis). Measured gain: strong on small models with oracle context (+18 to +35 points), small on strong or saturated models (+3.8% GPT-4o), sometimes negative with CoT (c17: the synthesis step can pull a correct CoT answer off track). It needs two extra calls. No equal-token comparison exists (d16). For our agent it is a candidate for open mode or S6 only.

### 4.4 Measuring whether a model really holds the opposition (c12, c13)

SIEV (Abbasloo) gives three numbers per model: pT (thesis accuracy), pS (accuracy after synthesis), OC (opposition coverage, in percent). A high pS with a low OC means the model replays the thesis and ignores the antithesis (GPT-5-nano pS 84.4, OC 15.5). We can log the same three numbers for any S7 variant to see whether the hold-two step is real or decorative.

### 4.5 Pushback guard (d08, d09, c22, c23)

If a held-open second rule collapses when the user says "are you sure", the loop is worthless. Guards with measured effect:

- Third-person framing ("a reviewer says X; assess whether X is right"): up to 63.8% more turns held (d08).
- A gating plus critic-rewrite layer: Claude Sonnet 4 sycophancy 9.6% to 1.4% on 437 adversarial TruthfulQA scenarios (d09, single author, preprint).
- Code rule: a stance may change only when a new external fact or failed case is attached, never on assertion alone. This matches G2.

Caveat: no study measures whether the held stance was correct.

### 4.6 Two subfacets, kept separate (a11, a12)

Human subfacets correlate only r = .06-.15, so measure them separately in the agent:

- **Tolerance of contradiction** maps to S7 hold-two-rules (working mapping, argument not data).
- **Expectation of change** maps to revisiting a committed rule when new evidence arrives (d10 argument, not data).

## 5. What holds up

**Replications and failures (human).**

- *Founding studies.* No direct large replication of the 1999 contradiction tasks was found (d19). One partial replication failed: Friedman, Chen and Vaid (2006) reused the Experiment 2 proverbs and found no Chinese-US difference in preference for dialectical proverbs (d01). Many Labs 2 replicated a different effect from the same school (Norenzayan 2002, d=0.86, N=7,396), but only 14-15 of 28 effects overall (b10, b11). That is not support for the dialectical studies.
- *Sample weakness.* Cells of 32 to 136 students; some Chinese samples lived in the US; only two conflict scenarios; in the school-vs-fun scenario about half the Chinese answered dialectically and the gap came from the US side (a04, K02). The authors say effects are probably muted in general populations (a07).
- *Mixed emotion.* Williams and Aaker (2002) vs Zheng et al. (2021, 160 US and 158 China) disagree; Morio's contradiction scale had alpha .50 in Japan (a21, b08).
- *Construct validity.* Sub-facets barely correlate (r .06-.15). Critics say the compromise is not dialectical in Basseches' sense (a25, d18).
- *What survives.* The DSS meta-analysis (k=139, N=23,629, 28 countries, d02) finds regional clustering and independence from collectivism. It uses country means of a self-report scale, and measurement invariance was not shown. Abstract only.

**Moderators and boundary conditions.**

- Domain: Chinese participants judged national groups as consistent and homogeneous, not contradictory (a13). Tolerance is not universal.
- Task: dialectical thinking correlated with lower creative personality in non-art majors (b12); naive dialecticism mediated higher indecisiveness (a23).
- Age: older adults reason more multi-perspective despite lower fluid intelligence (b15). Age is a rival to culture.
- Familiarity: yin-yang priming worked for Westerners familiar with East Asian culture (a10).
- Priming evidence is thin: the climate prime was marginal (p=.082, b13); other priming effect sizes were not recovered (b25).

**LLM cultural tendency claims.** Jin et al. (2023) found GPT more holistic than humans on the AHS and equal on the DSS for GPT-4. Sun and Wang (2025) show tendencies shrink or vanish with 30-60 items, temperature 0 and eight models (language effect on expectation of change p=.917). Hu et al. (2026) found reversed human patterns. Persona prompting does move value answers (Atari, Tao), but values are not reasoning style. Verdict: **do not assume a model has, or can be given, a dialectical style by nationality or prompt language.** Nobody reran Jin's scales with 30-60 items (d19), so that result stays fragile.

**Interventions that worked.**

- External-check refinement: GPT-4 ACRE 28.0 to 59.0 (d14). Tool critique: +5.7 on GSM8k, +16 on TabMWP-70B (d11). Execution feedback: up to +12% (d13).
- Mixed-model debate: +5.8 to +8.2% (d05).
- Antithesis steps on small models: +18 to +35 points on oracle-RAG multi-hop QA (c16).
- Votes with diverse starts and calibrated confidence beat plain voting (d03: Qwen GSM8K 0.932 vs 0.908).
- Neutral third-person reviewer wording against flips (d08).

**Interventions that did not work.**

- Pure self-critique (c20, c25, d12).
- Same-model debate versus voting at equal calls (d03, d04, d06). Choi et al.'s theory says debate preserves expected correctness (a martingale), so debate alone cannot raise it.
- Synthesis for strong models on single-answer sets: MMLU drops (Llama-3.3-70B 85.1 to 58.3, GPT-4.1-mini 54.7; c13).
- An opposite-role critic alone (d15).
- Antithesis on top of CoT (c17). No frontier-model or equal-token test exists (d16).
- Reasoning models do not fix early commitment (d10).

## 6. Language models

**Do LLMs show dialectical style?** Early: yes. GPT-3.5 and GPT-4 scored above human norms on analytic-holistic (5.35, 5.01 vs 4.87), and GPT-4 equalled the DSS norm (3.97 vs 4.00, p=.344; a26). Later: no. A replication with 8 models and many more items found no prompt-language or model-origin effect (a28, c05-c08). A third study found reversed patterns (a27). The result depends on item count, temperature and model. These are not stable traits.

**Do LLMs tolerate or flag contradictions?** Mostly not. In a five-language conflicting-needles benchmark, all tested models including GPT-5.2 asserted a single answer in most cases (a29). GPT-4 detects self-contradictions in reasoning chains at F1 52.2% against 66.7% for humans (b22).

**Do LLMs integrate opposition when asked?** It differs by model (c12, c13). Strong reasoning models integrate (O3: pT 97.1, pS 93.6, OC 95.5). Others replay the thesis (GPT-5-nano OC 15.5). Many lose accuracy when asked to synthesise (MMLU Llama-3.3-70B -26.8, GPT-4.1-mini -30.2, GPT-5-chat over 40 points on GSM).

**Do dialectical prompts help?** On small open models with oracle context, yes, a lot (Candussio +18 to +35 mean; +1.9 to +15.6 over CoT on WikiHop). On GSM-Symbolic: GPT-4o +3.8%, GPT-4o-mini +8.6%. Not shown for strong models at equal tokens (d16). With CoT, synthesis sometimes hurts (c17).

**Do second views help?** Debate gains (Du et al.: 81.8 vs 67.0 arithmetic; GSM8K 85.0 vs 77.0) largely vanish against self-consistency at equal calls (Huang; Zhang: debate beat CoT in about 15% of 36 configs; Choi: Qwen2.5-7B vote .7691 vs debate .7377). Source diversity helps (+5.8 to +8.2% mixing models).

**Do they hold a position under pushback?** Depends on size. SYCON-Bench: o3-mini 4.97 of 5 turns, Qwen2.5-7B 0.83. SycEval: 58.19% sycophancy, 14.66% regressive. Casual challenges persuade more than reasoned rebuttals (93.9% "are you sure" vs 56.1% full rebuttal; c22). Third-person wording gave up to 63.8% more turns held.

**Does external feedback matter?** It is the whole story. Oracle: GPT-4 GSM8K 84.3 to 97.5. Real tool: roughly half of that. No tool: flat or negative. A symbolic checker with N candidate rules: ACRE 28.0 to 59.0 for GPT-4, but MiniARC raw accuracy fell (refinement 18.7 vs IO 33.1, d14).

**When to commit.** Early commitment under piecemeal evidence roughly halves scores (30.9 vs 64.4, d10).

## 7. What our agent should take

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | A second rule or view must be checked by something outside the model: a tool run, a test case, a retrieved fact, a held-out example. Self-critique alone is not a counterexample. (Confirms G2/G3; S7's counterexample must be code-run.) | G2, G3, S7 | [E] | c20, c25, d11, d12, d13, d17 |
| A2 | Do not use same-model debate or persona voters as the "second view". It adds little beyond voting at equal cost. (Confirms G4/G9.) | G4, G9 | [E] | d03, d04, d06, c20, d07 |
| A3 | Do not assume a model's culture, origin or prompt language gives a thinking style. Do not use a persona to produce "dialectical" behaviour. | none (4b candidate) | [E] | a28, c05-c08, a27, b20, c09-c11 |
| A4 | Pushback rule: a stance may change only when a new external fact or failed case is attached, not on assertion. Log every flip and whether it went right to wrong. | G2, G10, S7 | [E] for the risk | c22, c23 (risk); d08, d09 (fixes are single-source) |
| A5 | A real checker recovers only part of an oracle gain (about a third to a half). Set budgets and expectations on that and report the fraction recovered. | S4, S7, S8 | [E] | d11, d12, d17 |
| A6 | Log pT, pS and OC whenever a second-view step is used, so we can see if it is real. | logging (section 6 of SCHEMA) | [S] as a metric idea | c12, c13 |

A1-A5 add no new element; they confirm and tighten existing guardrails. That is the honest result of this subfield. Everything specific to "hold two rules" is still a test.

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | S7 holds 2 to 3 candidate rules from different sources and kills one only on a failed discriminating case (code-chosen input, tool run). Commits by vote when no case exists. | S7 | [S] | d14, d11, d05 |
| T2 | Defer the first firm answer on staged-evidence items until a deciding observation arrives (expectation of change as "revisit"). | S7, S0 | [S] | d10 |
| T3 | Neutral third-person reviewer wording on any pushback turn. | G2, S7 | [S] | d08, d09 |
| T4 | Thesis-antithesis-synthesis step in open mode or at S6 only; never in direct mode. | S6, O8, S3 open | [C] | c14, c16, c17, c13 |
| T5 | Perspective-swap consistency check instead of a bare opposite-role critic. | S7 | [S] | d15 |
| T6 | Contradiction-category checklist to detect conflicting rules. | S7, S8 | [S] | b22 |
| T7 | Mixed-source second rule (different model or retrieved analogue) at S3 for O7 in impasses. | S3, O7 | [S] | d05, d03 |
| T8 | Separate "tolerance" (hold) and "change" (revisit) as two knobs and measure each alone. | S7 | [S] argument only | a11, a12, d02 |

## 8. Concrete tests on our bench

All arms at equal total tokens, including setup and extra calls (G7). Report accuracy with a paired test over items and the flip table (right to wrong, wrong to right).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 two-rule items | ARC-style or puzzle items with exactly 2 candidate rules fitting all shown examples, one correct, plus a held-out discriminating input | (a) plain CoT, (b) self-consistency, (c) S7 hold-two with code-run discriminating case, (d) S7 hold-two with model-judged discrimination | Held-out accuracy; tokens per solved item | (c) beats (a),(b) clearly, as in d14 (28.0/29.0 vs 59.0); (d) near (a) |
| B2 partly-true items | Items where each rule is right in a subregion (answer is a conditional rule) | B1 arms plus (e) forced pick-one | Accuracy in both subregions; share of correct conditional answers | (c) beats (e); no prior data, effect unknown |
| B3 single-answer control | One right answer, no ambiguity | plain vs S7 hold-two | Accuracy, tokens | Equal or tiny cost; if it loses, S0 must not route these items to S7 (d03, d04, c13) |
| B4 staged evidence | Items revealed in 3-5 pieces | (a) answer at first piece, (b) answer after all pieces, (c) provisional answer revised at each piece, (d) S7 defer | Final accuracy vs time of first answer | Defer beats early commit (d10: 30.9 vs 64.4) |
| B5 pushback | Same items, then 1-3 turns of "are you sure", false rebuttal, correct rebuttal | with/without neutral-reviewer wording; with/without "new fact required" code rule | Flip rate right to wrong; flip rate wrong to right | Fewer wrong flips without losing right flips (d08 up to 63.8% more turns held; c23 14.66% regressive baseline) |
| B6 second-view source | As B1 | second rule from (a) same model, (b) different model, (c) retrieved or tool-derived, (d) none | Accuracy | (b),(c) beat (a) (d05 +5.8 to +8.2%); (a) about equal to (d) |
| B7 checker quality | Code-checkable items | oracle counterexample, tool counterexample, none | Fraction of oracle gain recovered | About a third to a half (d11) |
| B8 synthesis step | Single-answer and open items | CoT vs CoT + antithesis + synthesis (equal tokens via fewer samples) | Accuracy; pT, pS, OC | Small gain on weak configs, neutral or negative on strong (c13, c17) |
| B9 DSS probe | 30-60 items per scale, 2 prompt languages, temp 0 and 1, 5+ runs | model with and without S7 text | Score and variance | No stable language effect (a28); check S7 does not randomly change answers |
| B10 contradiction flagging | Documents with embedded contradictory facts | plain vs "list conflicting statements first" step | Share of contradictions flagged | Low baseline (a29: about 60% at best); step may add 10-15 F1 (b22) |

## 9. What does not transfer, and why

- **Culture itself.** The agent has no East Asian upbringing. A nationality or language prompt moved value answers (Atari, Tao) but not reasoning style (Sun and Wang p=.917 on expectation of change). Do not build a "Chinese-style mode".
- **The size of the 1999 effect.** Small student samples, two scenarios, one failed proverb replication. Do not use F(1,109)=12.45 or 72% vs 26% to set any threshold (K02, K27).
- **Scale self-reports.** A model has no beliefs to report. DSS scores for GPT depend on version, temperature and item count (a26 vs a28).
- **Mixed emotion, dACC, age, indecisiveness, creativity.** Human facts about emotion, brain and personality. They say nothing about a scaffold. The cost findings (indecisiveness, creativity) are a design warning: tolerating contradiction has a price when a decision is needed.
- **Dialectical compromise for single-answer problems.** When there is one right answer, "both are partly true" is wrong. Debate and synthesis often lose to voting (d03, d04, c13).
- **Hegelian synthesis as a higher truth.** Western dialectics aims at a non-contradictory synthesis. Our counterexample step aims at elimination or conditional scope. These differ, and critics say Peng and Nisbett's compromise is not the Western method either (a25).
- **Debate between agents.** G9 stays. The positive Du et al. results do not survive equal-call controls.
- **Collectivism and interdependence.** Unrelated to dialecticism (d02), so ignore them here.

## 10. Open questions

1. Does S7 hold-two-until-counterexample beat plain CoT and self-consistency at equal tokens on two-rule items? Nobody has tested the exact design (K20). Nearest: d14.
2. What exactly is the counterexample, who generates the discriminating input, and how much of the oracle gain is recovered in practice (d11: about half)?
3. Does the antithesis gain hold for strong models at equal tokens (d16: no test)?
4. Does a held-open rule survive casual pushback, and is the held stance more often correct (d08, d09 do not measure correctness)?
5. Is there an N>=300 per culture, non-student replication of the 1999 contradiction-plausibility task (d19: none found)?
6. Does Jin et al.'s LLM result survive 30-60 items, two languages and current models (d19: none found)?
7. Which subfacet (hold vs revisit) helps where, given weak human correlations (r .06-.15)?
8. When to commit: is "a checker can still produce a deciding case" a good enough rule (K21, K22)?
9. Does debate beat self-consistency on tasks with partly true rules at equal tokens (no study)?
10. Does the 2026 meta-analysis hold at measurement level (invariance)? Only abstract-level numbers were read.

## 11. Sources

Marks: [V] opened and read this session (full text, or enough body text to take the numbers), [M] snippet, abstract or record only.

- [V] Peng and Nisbett (1999) Culture, dialectics, and reasoning about contradiction. https://public.websites.umich.edu/~nisbett/cultdialectics.pdf ; https://doi.org/10.1037/0003-066X.54.9.741 (a01-a08, b01-b04)
- [V] Spencer-Rodgers, Williams and Peng (2010) Cultural differences in expectations of change and tolerance for contradiction. https://culcog.studentorg.berkeley.edu/Publications/2010PSPR_dt.pdf (a09-a14, a19, a20, b05, b06, b25). The studies it cites (Ji et al., Choi et al., Hamamura et al., Williams and Aaker, Alter and Kwan) are second-hand.
- [M] Ji, Nisbett and Su (2001) Culture, change, and prediction. https://pubmed.ncbi.nlm.nih.gov/11760130/ (a15)
- [M] Choi and Nisbett (2000) Cultural psychology of surprise. https://pubmed.ncbi.nlm.nih.gov/11138759/ (a16)
- [M] Spencer-Rodgers, Peng, Wang and Hou (2004) Dialectical self-esteem. https://pubmed.ncbi.nlm.nih.gov/15448306/ (a17)
- [M] Spencer-Rodgers, Boucher, Mori, Wang and Peng (2009) The dialectical self-concept. https://pubmed.ncbi.nlm.nih.gov/19106076/ (a18)
- [V] Morio, Yeung, Peng and Yamaguchi (2022) Of mice and culture. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.917649/pdf (a21, b14)
- [M] Spencer-Rodgers et al. (2026) The Dialectical Self around the world: a meta-analysis. https://pubmed.ncbi.nlm.nih.gov/41578120/ (a22, d02; abstract/PubMed record only per critique.md)
- [V] Ng (2015) Cultural differences in indecisiveness, PhD thesis, York University. https://yorkspace.library.yorku.ca/xmlui/bitstream/10315/30698/2/Ng_Andy_H_2015_PhD.pdf (a23; critique says only the abstract and part of the tables)
- [V] De Vaus, Hornsey, Kuppens and Bastian (in press) East-West divide in affective disorders. https://lirias.kuleuven.be/retrieve/557b77fe-bae3-46d1-bf19-da66bec1f22d (a24)
- [V] Veraksa, Basseches and Brandao (2022) Dialectical thinking. https://www.frontiersin.org/articles/10.3389/fpsyg.2022.710815/pdf (a25)
- [V] Jin, Zhang, Shu and Cui (2023) The cultural psychology of LLMs: is ChatGPT a holistic or analytic thinker? https://arxiv.org/abs/2308.14242 (a26, a30, b18, b23, c01-c03)
- [V] Hu et al. (2026) Machine culture as an emergent phenomenon in LLMs. https://arxiv.org/abs/2601.17096 (a27, b20)
- [V] Sun and Wang (2025) The fragility of cultural tendencies in LLMs. https://arxiv.org/abs/2510.05869 (a28, b19, b24, c05-c08, c24)
- [M] Lu, Song and Zhang (2025) Cultural tendencies in generative AI, Nature Human Behaviour. https://arxiv.org/html/2510.05869v1 (c04; details via Sun and Wang)
- [V] Ostling and Kurfali (2026) Language bias under conflicting information. https://arxiv.org/abs/2604.07123 (a29)
- [V] Wang et al. (2016) dACC and dialectical self. https://doi.org/10.3389/fpsyg.2016.00152 (b07)
- [V] Zheng, Yu, Li, Fang and Peng (2021) Cultural differences in mixed emotions. https://doi.org/10.3389/fpsyg.2020.538793 (b08)
- [M] Leu, Mesquita, Ellsworth et al. (2010) Situational differences in dialectical emotions. https://repository.eduhk.hk/en/publications/situational-differences-in-dialectical-emotion (b09)
- [V] Many Labs 2 (Klein et al. 2018). https://osf.io/8cd4r/ (b10, b11)
- [V] Liu, Wang and Yang (2015) More dialectical thinking, less creativity? https://doi.org/10.1371/journal.pone.0122926 (b12)
- [V] Li et al. (2021) Dialectical versus linear thinking and anticipation of climate. https://doi.org/10.3389/fpsyg.2020.623591 (b13)
- [V] Grossmann, Na, Varnum, Park, Kitayama and Nisbett (2010) Reasoning about social conflicts improves into old age. https://doi.org/10.1073/pnas.1001715107 (b15)
- [M] Johnson-Laird and Lee (2006) Are there cross-cultural differences in reasoning? https://www.jimdavies.org/summaries/JohnsonlairdLee2006.html (b16)
- [M] Majima, epistemically suspect beliefs (abstract only). https://journalpub.escholarship.org/cognitivesciencesociety/article/27565/galley/17201/dow (b17)
- [V] Abbasloo (2026) Evaluating LLM reasoning beyond correctness and CoT (SIEV). https://arxiv.org/abs/2510.18134 (b21, c12, c13)
- [V] Liu et al. (2024) Self-contradictory reasoning evaluation. https://arxiv.org/abs/2311.09603 (b22)
- [V] Atari, Xue, Park, Blasi and Henrich (2023) Which Humans? https://osf.io/5b26t (c09, c10)
- [V] Tao, Viberg, Baker and Kizilcec (2024) Cultural bias and cultural alignment of LLMs. https://arxiv.org/abs/2311.14096 (c11)
- [V] Abdali et al. (2025, v7 2026) Self-reflecting LLMs: a Hegelian dialectical approach. https://arxiv.org/abs/2501.14917 (c14, c15)
- [V] Candussio (2026) A dialectic pipeline for improving LLM robustness, MSc thesis. https://arxiv.org/abs/2601.20659 (c16, c17, d16)
- [V] Du, Li, Torralba, Tenenbaum and Mordatch (2023/2024) Improving factuality and reasoning through multiagent debate. https://arxiv.org/abs/2305.14325 (c18, c19)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (c20, c25, d17)
- [V] Liang et al. (2023/2024) Encouraging divergent thinking in LLMs through multi-agent debate. https://arxiv.org/abs/2305.19118 (c21)
- [V] Kim and Khashabi (2025) Challenging the evaluator: LLM sycophancy under user rebuttal. https://arxiv.org/abs/2509.16533 (c22)
- [V] SycEval authors (2025) SycEval. https://arxiv.org/abs/2502.08177 (c23)
- [M] Friedman, Chen and Vaid (2006) Proverb preferences across cultures. https://pubmed.ncbi.nlm.nih.gov/16893007/ (d01; abstract/record only per critique.md)
- [V] Zhu et al. (2026) Demystifying multi-agent debate. https://arxiv.org/abs/2601.19921 (d03)
- [V] Zhang et al. (2025) Stop overvaluing multi-agent debate. https://arxiv.org/abs/2502.08788 (d04, d05)
- [V] Choi, Zhu and Li (2025) Debate or vote. https://arxiv.org/abs/2508.17536 (d06)
- [V] Wu, Li and Li (2025) Can LLM agents really debate? https://arxiv.org/abs/2511.07784 (d07; abstract and intro only)
- [V] Hong et al. (2025, v4 2026) Measuring sycophancy (SYCON-Bench). https://arxiv.org/abs/2505.23840 (d08)
- [V] Shah (2026) The Silicon Mirror. https://arxiv.org/abs/2604.00478 (d09)
- [V] Laban, Hayashi, Zhou and Neville (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120 (d10)
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 (d11)
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 (d12)
- [V] Chen, Lin, Scharli and Zhou (2024) Self-Debug. https://arxiv.org/abs/2304.05128 (d13)
- [V] Qiu et al. (2024) Phenomenal yet puzzling: hypothesis refinement with LLMs. https://arxiv.org/abs/2310.08559 (d14)
- [V] Li et al. (2026) Taming actor-observer asymmetry. https://arxiv.org/abs/2604.19548 (d15)
- [M] Chan (2000) and Ho (2000) comments on Peng and Nisbett. https://pubmed.ncbi.nlm.nih.gov/11036714/ (d18, records only)
- Search log for gaps 5 and 7, null result (d19).
