# Structured analytic techniques (SATs): deep document

*Subfield: assumption checks, devil's advocacy, brainstorming, and the competing-hypotheses family, as taught to intelligence analysts (Heuer, Pherson, Coulthart) and as now tested on humans and language models. Evidence ids (a01-a31, b01-b26, c01-c22, d01-d16) refer to evidence_a-d.jsonl in this folder. Claim ids (E02.03-K01 to K26) refer to claims.jsonl. Wording follows the opened pages; items marked "not opened" were seen only as abstracts or second-hand.*

## 1. What it is

A structured analytic technique (SAT) is a taught, step-by-step routine that makes an analyst externalise thinking that would otherwise stay in the head. The aim is to counter known weaknesses of unaided judgment: locking onto one favoured explanation, failing to list the full set of rivals, looking for confirming evidence, and holding unexamined assumptions.

The family covers three groups of techniques.

- **Hypothesis techniques.** Analysis of Competing Hypotheses (ACH) is the flagship. The analyst lists all plausible hypotheses, lists evidence, rates each item as consistent or inconsistent with each hypothesis, and ranks hypotheses by how little evidence contradicts them (a02).
- **Challenge techniques.** Key assumptions check, devil's advocacy, team A/team B, premortem, "what if" analysis, red team. They try to break the leading view (a03, a04).
- **Imagination techniques.** Brainstorming, scenario development, alternative futures. They widen the idea set before any evaluation (a04).

Why it matters for our agent: the schema is a scaffold that makes one model think better without training. Every SAT is a candidate scaffold step, "list rivals", "check assumptions", "attack the leader", "brainstorm before judging". The question is whether any of them pay for themselves at equal tokens (guardrail G7). Our schema already says: no full ACH matrix and no debate (section 4b, G9). This document tests whether the new evidence supports that, and what narrower pieces might survive.

Headline for the reader. The human evidence that SATs raise accuracy is thin and mostly null. The LLM evidence that the nearest analogues (self-check, debate, devil's advocate prompts) help is mostly null or negative at equal compute. The best-supported gains come from steps that SATs do not emphasise: independent re-asking, forcing probabilities to sum to one, and averaging many judges.

## 2. History and theories in depth

### 2.1 Heuer and the cognitive-limits argument (1999)

Heuer's *Psychology of Intelligence Analysis* (CIA) is the founding text (a01 to a05). His argument rests on psychology of the 1970s and 80s, not on a test of his own technique.

- Three weaknesses of unaided analysis: selective perception, an incomplete hypothesis set, and a focus on confirming evidence (a01).
- Working memory cannot hold several hypotheses and their evidence at once. Heuer: "Retaining multiple hypotheses in working memory ... is beyond the mental capabilities of most people." (a01)
- The remedy is ACH, eight steps. Step 1 is group brainstorming of hypotheses. Evidence goes in a hypotheses-by-evidence matrix. The work centres on diagnosticity: an item that fits all hypotheses tells you nothing. The analyst tries to disprove rather than confirm, and ranks hypotheses by least inconsistent evidence (a02).
- Heuer claimed ACH "increases the odds of getting the right answer" and leaves an audit trail. He did not report an experiment, and per Mandel and Tetlock he declined to test ACH under experimental control and relied on common sense (a02, b09).
- Support cited: Stech's review found that of the intelligence successes with documented method, only three accounts (WWII propaganda, U-boat, Luftwaffe) gave method detail, and all pitted competing hypotheses against evidence (a01). That is three cases, selected by documentation.
- On devil's advocacy Heuer is cautious. He describes an assigned minority view, "think like the adversary", calls its history in the IC controversial, and says competition of views is healthy but all-out political battle is not (a03).
- On brainstorming he gives the standard rule: defer criticism until after idea generation (a04).
- On assumptions: do sensitivity analysis on linchpin assumptions. Ask what would make each assumption out of date and try to disprove it. If you cannot think of anything that would change your mind, your mind-set may be entrenched (a04).
- Imaginability: analysing an unlikely scenario in detail makes it feel more likely. Heuer says ACH tends to give alternatives more weight than conventional analysis (a05).
- Anchoring numbers he cites: anchor 10 percent gave a mean estimate of 25 percent; anchor 65 percent gave 45 percent. 98 percent confidence ranges missed the true value 40 to 50 percent of the time (a05). These come from Tversky and Kahneman era work, not SAT tests.

### 2.2 Institutionalisation

The US Intelligence Reform and Terrorism Prevention Act of 2004 mandated the use of SATs in the IC (b09). Pherson and Heuer's *Structured Analytic Techniques for Intelligence Analysis* then catalogued dozens of techniques; Coulthart is the main academic voice who has argued SATs need empirical testing. Mandel and Tetlock (2018) argue SATs spread through institutional endorsement, not through tests (d05, b09).

### 2.3 The audit: RAND 2016

Artner, Girven and Bruce (RAND RR-1408) asked whether the IC measures SAT value (a06, a07, a08).

- No IC element routinely measures whether SATs improve analysis.
- A review of finished products: of the CIA assessments sampled, 23 showed no sign of SAT use and 6 made explicit, extensive use. NIC sample: 14 products, 10 with no explicit SAT, 2 centred on SATs, 2 with SATs in a box or appendix. A random 20 DIA and CIA documents: 8 showed use of at least one SAT.
- Old experiments: a 2000 Joint Military Intelligence College study (Folker) found structured hypothesis testing markedly improved accuracy in one of two experiments and had little effect in the other. A 2004 Mitre experiment found ACH reduced confirmation bias only for people without an intelligence background.
- Academic caution: devil's advocacy does not necessarily lead to real re-examination of assumptions and can raise confidence in the preferred hypothesis (Nemeth et al. 2001). Tetlock (2005) ran two experiments where scenario development lowered forecast accuracy.
- Limits: tiny, non-random, qualitative; SAT use inferred from text; no accuracy measure. The authors call the conclusions preliminary. Folker and Mitre primaries could not be opened.

### 2.4 The experimental turn (2008-2026)

- Lehner, Adelman, Cheikes and Brown (2008): ACH reduced confirmation bias in non-professionals, not demonstrably in about 12 analysts (a10, d03). Not opened as a primary.
- Mandel, Karvetski and Dhami (2018): the main ACH test on 50 UK analysts (d04, d02). See section 3.
- Karvetski and Mandel (2020): 227 participants, ACH no gain in coherence, slightly less reliable (a17, d03).
- Maegherman et al. (2020): 191 law students, no effect of ACH training on guilt ratings (a14).
- Wilcox and Mandel (2024): critical review of the 6 experiments; no benefit, possible harm; discourages mandating ACH (a16, d01).
- Dhami et al. (2024): task layout matters, and Dutch military analysts show little confirmation bias to begin with (a11, a12).
- Otzipka and Volbert (2026): ACH did not reduce adversarial allegiance among mock expert witnesses (a15, b07).
- 2025 content analysis of 138 experimental reports: SATs track process norms, not accuracy (a18, b13, b14).

### 2.5 Theories of why a technique might or might not help

1. **Working-memory support.** Externalising the matrix frees memory. Counter: 80 percent of untrained analysts rebuilt an ACH-style matrix on their own (a13), so the externalisation is not what training adds.
2. **Disconfirmation focus.** Seeking inconsistency beats seeking confirmation. Counter: most analysts and students already chose balanced or disconfirming questions (a12, a14); the premise that analysts are biased may be overstated.
3. **Dissent stimulates divergent thought.** Nemeth et al. 2001: an authentic minority produced more and better solutions than a role-played devil's advocate, which tended to bolster the original view (a09, d15). So the form of dissent matters.
4. **Technique adds noise.** Free choice of SATs and subjective consistency ratings add inter-analyst variance (b12, d05). ACH cell ratings are even less constrained than Admiralty-code source ratings.
5. **One-directional warnings flip the bias.** Warnings against overconfidence may produce underconfidence (b11).

## 3. Core findings with exact numbers

Status key: established = replicated or consistent across several independent sources; single = one source; contested = sources disagree; not opened = abstract or second-hand only.

### 3.1 Humans

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ACH training does not improve analyst probability accuracy | N=50 UK analysts (25 ACH, 25 control), 4 hypotheses, 12 cues. MAE ACH 0.26 vs control 0.21 (diff 0.04, d=0.43, p=.14). Pooled raw MAE 0.23; random-guess "chimp" 0.33 | Mandel, Karvetski, Dhami 2018 (d04, d02) | Established (3 small nulls) |
| ACH raises perceived usefulness, not accuracy | Usefulness-tracking correlation r .68 vs .17 (d=1.59) in one reading; in the ACH group usefulness tracking was uncorrelated with accuracy, in control it was correlated | d04, d02 | Single-source |
| Forcing probabilities to sum to 1 cuts error | Coherentized MAE 0.15, 35 percent lower (d=0.96). Effect d=1.37 in ACH arm vs 0.69 in control. After coherentizing the tradecraft effect was 0.01 | d04 | Single-source, large effect |
| Averaging analysts cuts error further | Aggregating all 50 after coherentizing: MAE 0.09, 61 percent below raw 0.23 | d04 | Single-source (consistent with wisdom-of-crowds literature) |
| 80 percent of untrained analysts build an ACH-style matrix anyway | Control group of the 50-analyst trial; ACH-trained group did not use ACH as designed and was less internally consistent | Dhami et al. 2019 via a13, b05 | Single-source, second-hand |
| ACH-trained analysts more susceptible to unpacking effects | Significant (no figures in review) | Mandel et al. 2018 via b10 | Single-source |
| ACH had no coherence benefit with uncertain evidence | N=227, six cases, two hypotheses; mean absolute deviation .22 (ACH) vs .18 (control), d=0.20, p=.051; pseudo-diagnostic weighting | Karvetski and Mandel 2020 (a17, d03, SUBFIELDS) | Single (abstract and review table) |
| ACH did not change law students' guilt ratings | N=191; no group difference before or after; about one third of ACH group used the matrix; helpfulness 57 of 100 | Maegherman et al. 2020 via a14 | Single, second-hand |
| ACH did not reduce adversarial allegiance | N=159; ACH effect F(1,153)=1.79, p=.183, partial eta2=.012. Retaining-party effect F(2,153)=3.12, p=.047, partial eta2=.039. Defence vs accessory prosecution -.19, 95% CI [-.37, -.00], p=.047 | Otzipka and Volbert 2026 (b07, b08) | Single |
| Pooled verdict on ACH | 244 Scholar hits, 7 papers, 6 experiments, no pooled effect size. Accuracy no difference (studies 2, 4, 5). Confirmation bias better only in Lehner 2008 (non-analysts). Diagnosticity better in 2 of 3, worse in 2 (4, 5). Reliability worse (5). Base-rate use worse (3) | Wilcox and Mandel 2024 (d01, d03) | Established (a tally, not a meta-analysis) |
| Layout of evidence changes confirmation bias | N=161. Balanced choice: rows layout 60.8 percent (31/51), ACH-style columns 38.2 percent (21/55), paragraph 32.7 percent (18/55); chi2(2)=9.43, p=.009, phi=.24. Confirming-only 56.5 percent overall. Choose confirming Hypothesis A: rows 39.2, columns 61.8, text 67.3 percent | Dhami et al. 2024 (a11, b01) | Single |
| Layout did not change credibility sensitivity | 77 percent columns, 78 rows, 75 text | a11, b02 | Single |
| Analysts are mostly not confirmation-biased on this task | N=62 Dutch analysts: 66.1 percent balanced, 14.5 percent inconsistent-only, 19.4 percent confirming-only. Balanced users 98 percent credibility-sensitive vs 72.7 percent confirming-only, 33.3 percent inconsistent-only | a12, b03 | Single |
| CRT and coherence did not separate good from poor evaluators | Per-condition correlations of CRT with deviation from additivity; none predicted performance | b04 | Single |
| Authentic dissent beats role-played devil's advocate | Quantity and quality of solutions; means not obtained | Nemeth, Brown, Rogers 2001 (a09, d15) | Single, abstract only |
| SATs track process norms not accuracy | 138 experimental reports; weak correlation with accuracy; standard probability ranges and timelines predicted norm adherence | 2025 content analysis (a18, b13, b14) | Single, abstract/preprint |
| SAT use is rare and unmeasured in practice | CIA sample 23 none / 6 extensive; NIC 10 of 14 none; multitopic 8 of 20 used at least one | RAND 2016 (a06) | Established but tiny samples |
| Analysts report deliberate strategies often | N=113; deliberate beat intuitive at 3 of 6 workflow stages, equal at the rest; not linked to training | Dhami and Careless 2019 via a19 | Single, self-report |

### 3.2 Language models (nearest analogues, since no direct SAT test exists)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Self-check without feedback lowers accuracy | GPT-3.5 CommonSenseQA 75.8 to 38.1 after one round, 41.8 after two. GSM8K 75.9, 75.1, 74.7. GPT-4 GSM8K 95.5, 91.5, 89.0; CSQA 82.0 to 80.0; HotpotQA 49.0 to 43.0. With oracle labels GSM8K rose 75.9 to 84.3 (GPT-4: 97.5) | Huang et al. 2024 (c01, a23, b21) | Established |
| Wrong flips outnumber fixes | Gemini 1.0 Pro, MATH: first try 52.6, second 41.4 (-11.2); correct-to-incorrect 15.8 percent vs incorrect-to-correct 4.6 percent. Self-Refine 52.8 to 51.8. RL-trained SCoRe 60.0 to 64.4 (c->i 1.4, i->c 5.8) | Kumar et al. 2024 (d08) | Single (consistent with Huang) |
| Self-correction blind spot | 64.5 percent avg over 14 open non-reasoning models; Claude 3.5 Haiku 52.5, Sonnet 4 41.4; non-math domains 62.8. SCLI5: own error 0.499, user-attributed error 0.910, with "Wait" 0.957. GSM8K-SC 0.183 / 0.881 / 0.796. DeepSeek-V3 0.567 to 0.902 with Wait vs R1 0.908. Reasoning models show a small or negative blind spot | Tsui 2025 (d07) | Single (injected errors) |
| Debate beats single answer (original) | Du et al., GPT-3.5, 3 agents x 2 rounds. Arithmetic: single 67.0, reflection 72.1, majority 69.0, debate 81.8. GSM8K 77.0, 75.0, 81.0, 85.0. Chess 91.4, 102.1, 102.2, 122.9. Biographies 66.0, 68.3, 73.8. MMLU 63.9, 57.7, 71.1 (reflection) | Du et al. 2023 (a22, b15, b16, c06) | Established as reported; see next row |
| Debate does not beat self-consistency at equal calls | GSM8K: standard 76.7; SC 3 responses 82.5; debate (6 responses) 83.2 vs SC6 85.3; debate (9) 83.0 vs SC9 88.2 | Huang et al. 2024 section 4 (a24, critique item 2) | Established |
| Debate protocols no better than Medprompt or SC | MedQA: Medprompt 0.65, Society of Mind 0.64, Ens. Refinement 0.64, ChatEval 0.60, SC 0.60, single 0.60, Multi-Persona 0.58. PubMedQA: Medprompt 0.77, single 0.75, Multi-Persona 0.70 | Smit et al. 2024 (a25, b17, c04) | Established |
| Disagreement level is a hidden knob | Tuning agreement via prompt: Multi-Persona +15, Society of Minds +5 on a 376-question USMLE subset; at 90 percent agreement Multi-Persona went from worst to best on MedQA. More disagreement helped on counter-intuitive arithmetic, more agreement helped on MedQA and PubMedQA | Smit et al. (b18, c04); Liang et al. (a21) | Established |
| Divergent-thinking debate on counter-intuitive arithmetic | GPT-3.5 26.0, CoT 28.0, SC 29.5, self-reflect 27.5, MAD 37.0; GPT-4 51.0. Diversity MAD 49.7 vs self-reflect 19.3; bias 24.8 vs 29.0. "Disagree on everything" (0.988) was not best | Liang et al. 2023 (a20, a21, c03) | Single dataset (200 items) |
| Debate rarely beats CoT across 36 configs | 5 methods x 9 benchmarks x 4 models; significant wins over CoT in about 15 percent of configs; Multi-Persona none; Claude-3.5-haiku MMLU AgentVerse +0.85, others at least -3.60. Heter-SoM +6.4 over SoM average, +5.8 over CoT average; Heter-EoT +8.2 | Zhang et al. 2025 (b19, b20) | Established (null); heterogeneity gain single |
| Mixing models can hurt | Self-MoA +6.6 over mixed MoA on AlpacaEval 2.0, +3.8 average over MMLU, CRUX, MATH. LC win rate: mixed 2-layer MoA 59.1; Self-MoA + WizardLM 65.7; single 53.1 | Li et al. 2025 (d10) | Contested vs Zhang |
| Peer debate among small models lowers accuracy | GPT-4o-mini, Llama-3.1-8B, Mistral-7B; 100 items per set, 5 seeds, 3 rounds. CSQA debate always hurt. Correct-to-incorrect flips exceed fixes. Correctness payoff prompt did not reduce flips | Wynn et al. 2025 (d06) | Single |
| Single strong prompt equals best discussion | Qualitative; discussion helps mainly without demonstrations | Wang et al. 2024 (c05) | Single, no numbers recorded |
| Sycophancy under challenge | "Are you sure?" lowers accuracy up to 27 percent (Claude 1.3); first-answer change 32 percent (GPT-4) to 86 percent (Claude 1.3); wrongly admit mistakes 42 to 98 percent; suggested wrong answer up to -27 percent (LLaMA 2) | Sharma et al. 2024 (a27, c10) | Established (2023 models) |
| Stated reasoning omits real cause | Biasing features cut accuracy up to 36 percent on 13 BIG-Bench Hard tasks; CoT gains in unbiased context 57.1 to 59.6 (GPT-3.5), 59.2 to 65.3 (Claude 1.0) | Turpin et al. 2023 (a28, c11) | Established |
| Independent factored checks beat joint review | Wikidata list precision 0.17 to 0.36 (two-step), 0.32 factored; Wiki-Category 0.39 to 0.48 factored; FactScore 63.7 factored to 71.4 factor+revise (Llama 65B) | Dhuliawala et al. 2023 (d11) | Established as closest analogue of an assumption check |
| Debate with a stronger debater raises judge truthfulness | QuALITY: non-expert LLM judges 76 vs 48 percent naive; humans 88 vs 60 percent. Debaters hold the passage; judges do not | Khan et al. 2024 (a26, c07) | Single, information asymmetry |
| Debate evaluators give small gain | FairEval ChatGPT single 58.7 vs multi 62.5; GPT-4 60.0 vs 63.8 (column order unverified); human agreement 68.8 | ChatEval (a30) | Single, unverified labels |
| Persona prompt can truncate runs | Fixed-persona variant ended early: Codenames 37/50 with system message vs 4/50 without; trivia 18/100 and 16/100 vs 0/100 and 1/100; benefit only in GPT-4 | Solo Performance Prompting (c09) | Single |
| Diverse-model consensus | ReConcile up to +11.4 over baselines; +3.4 over GPT-4 on StrategyQA; +8 on MATH | Chen et al. 2023 (c08) | Single, abstract only |

### 3.3 Brainstorming, devil's advocate and forecasting with LLMs

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LLM brainstormed ideas rated more novel than human experts' | N=79 reviewers, 49 ideas per condition. Idea-level novelty human 4.86, AI 5.62 (p=0.03), AI + human rerank 5.78 (p<0.01). Review-level 4.84 / 5.64 / 5.81 (N=109 reviews). Feasibility slightly lower for AI | Si et al. 2024 (a29, b23) | Single-source |
| LLM brainstorm duplicates | Of 4000 seed ideas per topic, about 200 (5 percent) non-duplicate at cosine 0.8; duplicates grow per batch; LLM rankers near chance; experts guessed AI vs human at 50 percent | Si et al. (a29, b24) | Single |
| ChatGPT raises group-level homogeneity | 36 participants; group similarity M=.24 vs .28 (t(32)=2.154, p=.038, d=.47); categories 8.58 vs 6.77 (d=.54); no difference in unique ideas | Anderson et al. 2024 (c14) | Single |
| Cross-model sameness | 26K queries, 31,250 annotations; cross-model similarity 71 to 82 percent; within-model similarity exceeds 0.8 in 79 percent of cases | Artificial Hivemind (c15) | Established (3 sources agree on direction) |
| Clinical devil's-advocate agent team | 16 cases x 5 repeats x 3 frameworks = 240 responses. Initial diagnosis 0/80 correct; best framework top-2 differential 76 percent (61/80); OR 3.49 vs human evaluators, P=.002 | GPT-4 multi-agent clinical (b25) | Single, curated bias cases |
| Anticipatory reflection ("devil's advocate") agent | WebArena 23.5 percent vs LATS 22.7 and Plan+Reflexion 19.8; +3.5 over prior zero-shot; 45 percent fewer plan revisions | Wang et al. 2024 (c17) | Single, small margins |
| Pro/con scratchpad for forecasting | Best prompt: rephrase, list reasons for no and yes with strength, aggregate. System Brier .179 vs crowd .149; GPT-4 base .208; accuracy 71.5 vs 77.0 percent; random .25 | Halawi et al. 2024 (c12) | Single |
| LLM crowd equals human crowd | 12 LLMs, 31 questions, 1007 forecasts; Brier 0.20 (SD .12) vs 0.19 (SD .19); t(60)=0.19, p=.850; yes-bias and overconfidence | Schoenegger et al. 2024 (c13) | Single |
| Machine red teaming at scale | 0.5M zero-shot cases, 3.7 percent offensive (18,444 failures); few-shot and RL variants raise rate | Perez et al. 2022 (c16, a31) | Single, safety domain |
| Models read probability words like humans (mostly) | 7 of 10 models human-like; mapping shifts with truth of statement, more than humans; 19 words, 123 respondents for the human consensus | Belem et al. 2024 (d14); Sileo and Moens 2023 (d13) | Single |

## 4. Mechanisms and models

Each mechanism is written so an engineer can implement it or a test.

### 4.1 Why ACH-style matrices may not add accuracy

- **Diagnosticity needs a probability, not a tick.** ACH asks for consistent/inconsistent cells. People then count ticks, which gives pseudo-diagnostic weighting (a17). In code: a likelihood ratio per evidence item per hypothesis pair would be needed. The tally of cells loses that.
- **Cell ratings are noisy.** Consistency ratings vary widely between analysts (d05, b12). An LLM making the cell ratings adds sampling noise. Averaging many samples reduces it (d04, 61 percent error cut by averaging).
- **Incoherence.** Probabilities over mutually exclusive hypotheses do not sum to 1 (unpacking effect). Fix in code: divide by the sum. Cut MAE by 35 percent in humans (d04). This is the one robust, cheap technique found, and it is a G5 operation, not an SAT.

### 4.2 Self-check and assumption-check failure model

Three measured parts:

1. **No signal.** The model cannot judge whether its own reasoning is right (b22). With oracle labels the same loop gains (GSM8K 75.9 to 84.3), so the gain is the label.
2. **Asymmetric flipping.** Rate of correct-to-incorrect 15.8 percent vs incorrect-to-correct 4.6 percent on MATH (d08). Any check step is judged by this ratio. If the base answer is right most of the time, a check that flips at a fixed rate is net-negative.
3. **Blind spot, and its cure.** Models fix an error labelled as the user's far better than their own (0.910 vs 0.499 in SCLI5). A one-word "Wait" lifts non-reasoning models to near reasoning-model level (0.957). Reasoning models already do it inside the trace (d07).

Implication: an assumption check should be a separate, fresh pass that gets the assumption as external text and asks "is this true", ideally verified by a tool or retrieval. It should not be "re-read your answer".

### 4.3 Factored verification (the best-supported analogue of a key assumptions check)

Chain-of-Verification (d11): draft, list verification questions, answer each question in a fresh context that does not see the draft, then revise. The "factored" variant avoids copying the draft's errors. Precision on list questions 0.17 to 0.32 factored; FactScore 63.7 to 71.4 with factor plus revise. Mapping to SAT: the key assumptions check becomes "extract the assumptions the answer depends on; query each one blind". Test arm in section 8.

### 4.4 Debate as ensemble, not critique

Huang et al. read debate as "consistency, not critique" (a24). At equal responses, SC beats debate at 6 and 9 responses. Zhang et al. find debate wins over CoT in about 15 percent of 36 configs (b19). Wynn et al. find flips from correct to incorrect exceed fixes, rising with the number of dissenting peers (d06). So the mechanism of any debate gain is more samples plus voting, and the mechanism of debate loss is sycophancy to peers (a27: 32 to 86 percent first-answer change under challenge).

Moderators found:
- Disagreement intensity (a21, b18): too much forced disagreement hurts; best level is task-dependent.
- Heterogeneity (b20 vs d10): conflicting.
- Information asymmetry (a26): debate helps a weak judge when the debaters see evidence the judge cannot.
- Prompt strength (c05): strong single prompt with demonstrations closes the gap.

### 4.5 Why dissent type matters (authentic vs assigned)

Nemeth et al. (d15): an authentic minority gave better solutions than all three kinds of assigned devil's advocate. Mechanism proposed in the literature: assigned dissent is recognised as role play and triggers bolstering of the starting view; authentic dissent prompts re-appraisal. Translating to an LLM: a rival that argues its own best-supported conclusion from the evidence is "authentic"; a critic assigned to attack the leader is "assigned". Not tested on LLMs (K25).

### 4.6 Brainstorming and homogeneity

LLM brainstorming gives novelty by rating but saturates: about 5 percent of 4000 ideas are non-duplicate (b24). Across models, similarity is 71 to 82 percent (c15). Mechanism: all instruction-tuned models share modes. Implementation: embed each rival, drop near-duplicates (cosine 0.8 was Si's threshold), count unique yield per token. G8 already says the generating model is not the selector of ideas.

### 4.7 Wording of probabilities

Models map words like "probably" to numbers mostly like humans, but the mapping moves with whether the statement is true (d14). Standardised probability ranges predicted norm adherence among human reports (b13). Implementation: ask for numbers, or give a fixed word-to-range table, and compare Brier. Not tested.

## 5. What holds up

### 5.1 Replications and failures

- **ACH accuracy gain: failed to replicate in humans.** Folker 2000 (one of two experiments gained, one near zero), Mitre 2004 (non-professionals only), Mandel 2018 (N=50, null), Karvetski and Mandel 2020 (N=227, null or slightly worse), Maegherman 2020 (N=191, null), Otzipka 2026 (N=159, null). Wilcox and Mandel 2024 tally: never improved accuracy. Weakness: there is no pooled effect size, studies are small, students dominate, training time is short, and control participants often used falsification themselves (a15 limits, a13).
- **Debate gain: replicated against single sample, failed against equal compute.** Du et al. gains are real versus one sample (81.8 vs 67.0). Huang et al. find SC beats debate at equal responses (88.2 vs 83.0 at 9). Smit and Zhang find no reliable debate win (about 15 percent of 36 configs).
- **Self-correction: replicated failure.** Huang, Kamoi (survey: no prompted-LLM feedback success outside special tasks), Kumar, Tsui.
- **Sycophancy under challenge: replicated** (Sharma; Wynn).
- **Self-MoA vs heterogeneity: failed to agree** (d10 vs b20). Possible reconciliation: different tasks (open-ended AlpacaEval vs reasoning benchmarks).

### 5.2 Moderators

- Task structure: layout of evidence changed balanced choice from 32.7 to 60.8 percent (a11).
- Background: ACH helped non-analysts but not analysts (Lehner; Mitre).
- Disagreement intensity: task-dependent (a21, b18).
- Model type: reasoning models show little self-correction blind spot; non-reasoning Claude Sonnet 4 shows 41.4 percent (d07).
- Feedback: external or oracle feedback is what makes correction work (b21, c02).
- Information asymmetry: debate helps when the debaters see more than the judge (a26).
- Adversarial allegiance: retaining party shifted evidence weighting, ACH did not (b08).

### 5.3 What worked

- Coherentizing probabilities (35 percent MAE cut) and averaging analysts (61 percent total cut) in analysts (d04).
- Factored verification questions (d11).
- Reframing the check as an outside voice or adding "Wait" in non-reasoning models (d07).
- RL-trained self-correction (SCoRe +4.4 net, c->i 1.4 percent) but needs training (d08).
- Row layout of hypotheses and evidence in humans (a11).
- Dedup and rerank on LLM brainstorming (a29).
- Tuning the debate agreement level per task (b18), but this is a tuned null versus an untuned one.

### 5.4 What did not work

- ACH matrix training: accuracy, coherence, bias, adversarial allegiance (sections 3.1).
- Untuned debate; same-model debate; role-played Multi-Persona (about 7 percent below Medprompt, c04).
- A correctness payoff in the debate prompt (d06).
- Bias warnings as one-directional correctives (b11).
- Scenario development in two Tetlock experiments lowered accuracy (a08, second-hand).
- Self-review without a signal (section 3.2).

## 6. Language models

### 6.1 Direct tests of SATs on LLMs

None found with measured results. A search of arXiv, OpenAlex and Semantic Scholar plus WebSearch (rate-limited late in the run) found no study testing an LLM on ACH, a key assumptions check or a premortem as named techniques (c22, d16, K17). AI devil's-advocate systems for groups report design or group-decision outcomes only (c18 design, c19 not opened). So the following is evidence from analogues.

### 6.2 How models behave on analogue tasks

1. **Self-check.** Prompted self-check lowers accuracy on 2023-era models (Huang: GPT-3.5 CSQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0). The wrong-flip rate is 15.8 percent against 4.6 percent fixed (Gemini 1.0 Pro, MATH). Newer non-reasoning models still show a 41.4 to 64.5 percent blind spot (Sonnet 4, 14-model mean); reasoning models do not (d07). Nobody has replicated Huang's tables on o-series or Claude 4+ (critique gap 6).
2. **Challenge and devil's advocate.** Models yield to challenge: 32 to 86 percent change their first answer (Sharma). Group debate of small models lowers accuracy across 3 rounds (Wynn). So a devil's advocate prompt can cause wrong flips; a guard is needed.
3. **Debate.** Versus a single sample it helps (+14.8 points on arithmetic for Du). Versus self-consistency at the same number of responses it does not (88.2 vs 83.0). Over 36 configs only about 15 percent show significant wins over CoT.
4. **What changed the result.**
   - Making the check external or "Wait" framed: SCLI5 0.499 to 0.910 or 0.957; GSM8K-SC 0.183 to 0.881 or 0.796.
   - Tuning disagreement: +15 (Multi-Persona) and +5 (Society of Minds) on a 376-question set.
   - Heterogeneous models: Heter-SoM +6.4 over SoM average, but Self-MoA finds same-model resampling better.
   - Information asymmetry: judge accuracy 76 vs 48 percent.
   - Factored verification: precision 0.17 to 0.32.
   - RL on own traces: MATH 60.0 to 64.4.
5. **Brainstorming.** LLM ideas are rated more novel (5.62 vs 4.86) but are 95 percent duplicates at scale. Ranking by LLM is near chance (b24).
6. **Forecasting.** An LLM crowd of 12 models equals a human crowd (Brier 0.20 vs 0.19). A single retrieval system reached .179 vs .149. A pro/con scratchpad is in the best-performing prompt but the study does not isolate its effect (c12).
7. **Faithfulness.** Written reasoning omits biasing cues (up to 36 percent accuracy loss). An assumptions list written by the model is not proof that those assumptions drove the answer (Turpin).
8. **Probability words.** 7 of 10 models map words like humans; the mapping shifts with truth value (d14).

### 6.3 Caveat on age and scale

Most of the 2023-24 results use GPT-3.5 or comparable models, on arithmetic and QA, not analytic tasks. Only Tsui (2025) and Wynn (2025) cover newer models, and neither tests frontier reasoning models on debate. All numbers should be treated as a prior to be remeasured on our bench.

## 7. What our agent should take

Schema parts: G = guardrails G1-G12, S = states S0-S9, O = operators O1-O8, memory = section 5. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Do not add a full ACH matrix; already in 4b. New human evidence confirms (N=50, 227, 191, 159; Wilcox and Mandel tally) | 4b / G7 | [E] | a13, a14, a15, a16, a17, d01, d02, d03, d04 (K09, K12, K23) |
| Keep G9 (no debate). New evidence: SC beats debate at 6 and 9 equal responses (88.2 vs 83.0); about 15 percent of 36 configs win over CoT; debate among small models lowers accuracy | G9 | [E] | a24, a25, b17, b19, d06 (K03) |
| Keep "no unstructured self-review". Add the number: prompted self-check flips 15.8 percent right to wrong vs 4.6 percent fixed; any check step must beat this ratio | 4b, G2 | [E] | b21, c01, d08 (K01) |
| Log wrong flips and fixes for every doubt step (already in section 6 of schema) and add a hold rule: an answer is overturned only by new evidence or a failed check, not by a counter-argument | G1, G2 | [E] | a27, c10, d06 (K06) |
| Do not treat the model's written assumption list or reasoning as proof of what drove the answer; decide from outputs | G10 | [E] | a28, c11 (K07) |
| Forcing probabilities over exclusive hypotheses to sum to 1 in code; average several independent samples | G5, G4 | [E] for coherentizing as already in G5; averaging effect [S] in humans | d04 (K22), c13 |
| Brainstormed candidates are deduplicated in code and picked by running, not by the generating model; expect heavy duplication across samples and models | G8, S4 | [E] | a29, b24, c14, c15 (K14) |
| A fixed devil's advocate strength is risky; no schedule, trigger only on a signal | G1 | [E] | a21, b18, c04 (K04) |

### Test first (not established)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Fresh-context, per-assumption check ("is this assumption true?") with tool or retrieval where possible, instead of joint review | S7 / O-check | [S] | d11, d07, d09 (K24) |
| "Wait" or external-voice frame on a non-reasoning model's check pass | G2 | [S] | d07 |
| Rival-hypothesis step as a short list (2 to 4 rivals) with probabilities that sum to 1, versus plain CoT and versus self-consistency at equal tokens; no matrix | S1/S2, O2 | [S], direct LLM test missing (gap 1) | d04, c12, b25 (K16, K17) |
| Authentic-rival arm (rival argues own best conclusion) vs assigned critic arm | O-rival | [S] | d15, a09 (K25) |
| Pre-action failure imagination (premortem style) for agent tasks | S6 | [S] | c17 (K19) |
| Embedding-based dedup of rivals and mixed-model vs same-model sets | O-diverge | [C] | d10, b20, c15 |
| Fixed probability-range table in outputs, measured by Brier | G calibration | [S] | b13, d14 (K11, K26) |
| Layout of rival evidence (rows of hypotheses vs paragraph) in the prompt | S2 | [S] | a11, b01 (K08) |
| Independent judge that sees both sides, not the debater | G8 | [S] | a26 (K15) |

## 8. Concrete tests on our bench

All arms use equal total tokens, counted including setup, and all rival-based arms are compared against plain majority vote over the same number of samples (G7). Report wrong flips (correct to incorrect) and fixes separately. Report 95 percent intervals, at least 100 items per arm.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Rival list vs plain vs SC | Diagnostic or multiple-hypothesis items with a keyed answer (our BrainTeaser-type and diagnostic-style items; forecasting items with resolved outcomes) | (a) plain CoT, (b) majority vote of N samples, (c) 3-rival list with probabilities normalised in code, one pass, (d) rival list plus N/3 samples averaged | Accuracy; Brier on probabilities | (c) no better than (a); (d) about equal to (b). Expect null, based on ACH nulls and debate at equal compute |
| T2 Factored assumption check vs joint review | Items where the first answer rests on 2 to 4 stated assumptions, some false (inject false premise) | (a) no check, (b) joint "review your answer", (c) extract assumptions then query each in fresh context, (d) (c) with "Wait" or external-voice frame | Accuracy; wrong-flip rate; fix rate; flip ratio vs 15.8/4.6 | (b) negative; (c) small positive on false-premise items; flip ratio better than 1 only in (c) or (d) |
| T3 Authentic rival vs assigned critic | Items with an intuitive but wrong answer (counter-intuitive arithmetic, trick questions) and items where the intuitive answer is right | (a) plain, (b) critic assigned to attack leader, (c) rival argues its own best answer, (d) majority vote | Accuracy on both item types; wrong flips | (b) flips right answers; (c) smaller harm; both below (d) at equal tokens |
| T4 Debate strength sweep | Two task types: counter-intuitive and plain factual | Adversary strength low, moderate, high; plus SC | Accuracy by task type | Optimum differs by task; at best equal to SC |
| T5 Hold rule | Correct-answer items challenged with "Are you sure?" or a rival argument | (a) free revision, (b) revise only with new evidence from a tool or a failed check | Flip rate on correct answers; fix rate on wrong answers | (b) lowers wrong flips with small loss of fixes |
| T6 Brainstorm yield | Open candidate-generation items (idea tasks, hypothesis lists) | (a) N samples same model, (b) N samples with persona prompts, (c) mixed prompts and temperatures, each followed by embedding dedup at cosine 0.8 | Unique-after-dedup yield per 1000 tokens; best-candidate quality by execution or keyed set | Yield low (about 5 percent in Si); personas add little real diversity |
| T7 Pre-action failure imagination | Multi-step agent tasks with a pass/fail checker | (a) act, (b) imagine failure modes then act, (c) act then reflect after failure | Success rate at equal steps; plan revisions | (b) at best small gain (Wang: 23.5 vs 22.7) |
| T8 Probability range table | Forecasting or calibration items | (a) free words, (b) numeric probabilities, (c) fixed word-to-range table | Brier; coherence | (b) and (c) similar; table cheap |
| T9 Rival layout | Rival-evidence items | Rows of hypotheses vs matrix vs paragraph | Share of balanced evidence use; accuracy | Layout shifts balanced use in the model as in humans; accuracy effect unknown |
| T10 Same-model vs mixed rivals | Items with several rival slots | Same-model resamples vs mixed models, same tokens | Accuracy; rival embedding distance | Same-model wins on accuracy (Self-MoA), mixed wins on diversity |

## 9. What does not transfer, and why

- **Group process.** Most SATs assume a team that argues. Our agent is one model; its "voices" are not independent (G4; cross-model similarity 71 to 82 percent, within-model above 0.8 in 79 percent of cases). Team A/B and red teams lose their independence.
- **Role-play dissent.** The human result is that role-played devil's advocate bolsters the starting view. An LLM playing devil's advocate is also sycophantic to the leader, so it may bolster or flip arbitrarily.
- **Training and buy-in.** ACH's human costs (training time, whether analysts used the matrix) do not exist for a model that follows instructions, but neither do its benefits from motivation or audit trails.
- **Audit trail and communication.** SATs are partly justified by transparency for consumers. A model's reasoning text is not a faithful record (Turpin), so the audit value is weaker.
- **Organisational outcomes.** Process-norm adherence (138-report study) is not accuracy and is irrelevant to our bench.
- **Student and analyst samples.** The human nulls come from small samples with short training; they show that ACH does not help in those conditions, not that matrices never help. LLM context, memory and speed differ.
- **Idea novelty ratings.** Si et al. rated research ideas in NLP; our bench uses keyed or executable answers (G8), so a novelty rating does not transfer.
- **Heuer's premise of bias.** Dutch analysts mostly did not show confirmation bias (66.1 percent balanced). LLMs show different biases: sycophancy, acquiescence, anchoring on the prompt, and the blind spot for own errors. The remedies should target those, not human confirmation bias.

## 10. Open questions

1. Does an explicit rival-set step (2 to 4 rivals, probabilities normalised in code) beat plain CoT and self-consistency at equal tokens? No direct study (gap 1).
2. Does a key assumptions check or premortem reduce errors in an LLM agent, and how often does it cause wrong flips? Closest numbers are for generic self-check.
3. What exactly do the 6 ACH experiments show? The Wilcox and Mandel review is a tally; no pooled effect size exists, and the primaries (Folker 2000, Lehner 2008, Mitre 2004) were not opened.
4. Nemeth et al. 2001: exact means and effect sizes for authentic dissent vs devil's advocate; and whether an LLM "authentic dissent" prompt beats an assigned critic.
5. Can LLM rival hypotheses be made diverse enough? What is the unique-yield per token of rival lists, and does a mixed-model set help (Zhang vs Li disagree)?
6. Do stronger reasoning models (o-series, Claude 4+) still lose accuracy under challenge? Huang and Sharma have not been replicated on them.
7. Do SATs improve calibration (Brier), not only accuracy, in humans? Mandel 2018 measured MAE; the 2025 content analysis found weak links to accuracy.
8. Does a standardised probability-range table improve LLM calibration at no token cost?
9. Does debate or a devil's advocate help when information is asymmetric (Khan: 76 vs 48 percent), and can we create that asymmetry in a single-agent scaffold by hiding the leader's reasoning from the critic?
10. How large is the layout effect in LLMs (rows vs columns vs text), given it was 60.8 vs 32.7 percent in humans?

Links to subfields run in parallel in this batch (not covered here): Assumption testing; Debiasing; Argumentation and defeasible rules; Retrieval and ensembles for LLM forecasts; Verbal confidence; Heuristics and biases; Evidence and probability reasoning; Technical and physical red teams; Dual-process and three-process accounts; Imprecise credences; Automated discovery; Deliberate practice (analysis tradecraft).

## 11. Sources

[V] = opened and read this session (or in an earlier run of this batch, recorded opened:true); [M] = snippet, abstract only or second-hand.

- [V] Heuer (1999), Psychology of Intelligence Analysis, CIA CSI. https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf (a01-a05)
- [V] Artner, Girven, Bruce (2016), RAND RR-1408. https://www.rand.org/content/dam/rand/pubs/research_reports/RR1400/RR1408/RAND_RR1408.pdf (a06-a08; c20 listing https://doi.org/10.7249/rr1408 [M])
- [M] Nemeth, Brown, Rogers (2001), Devil's advocate versus authentic dissent, Eur J Soc Psych. https://doi.org/10.1002/ejsp.58 (a09, d15; abstract only)
- [M] Lehner, Adelman, Cheikes, Brown (2008), Confirmation bias in complex analyses. https://doi.org/10.1109/TSMCA.2008.918634 (a10; via the Wilcox and Mandel table)
- [V] Dhami, Belton, De Werd, Hadzhieva, Wicke (2024), Effects of task structure and confirmation bias in alternative hypotheses evaluation. https://pmc.ncbi.nlm.nih.gov/articles/PMC11169332/ (a11-a14, a19, b01-b06; the critique notes the 2024 numbers were carried over from the first run)
- [V] Otzipka and Volbert (2026), ACH and expert witness testimony. https://pmc.ncbi.nlm.nih.gov/articles/PMC13094959/ and https://doi.org/10.1371/journal.pone.0346891 (a15, b07, b08)
- [V] Wilcox and Mandel (2024), Critical review of ACH. https://doi.org/10.31234/osf.io/an32t (a16, d01-d03; full PDF read in gap search)
- [M] Karvetski and Mandel (2020) / Mandel et al. (2020), Coherence of probability judgments from uncertain evidence: does ACH help? https://doi.org/10.31234/osf.io/7xg8j (a17; abstract plus review table)
- [M] Content analysis of 138 reports (2025), The relationship between SATs and intelligence analysis quality. https://osf.io/preprints/psyarxiv/7p9v4 and https://doi.org/10.31234/osf.io/7p9v4_v1 (a18, b13, b14 read as [V] on the preprint page; c21 [M])
- [V] Mandel, Karvetski, Dhami (2018), Boosting intelligence analysts' judgment accuracy. https://doi.org/10.1017/S1930297500006628 (d04)
- [V] Mandel and Tetlock (2018), Correcting judgment correctives in national security intelligence. https://pmc.ncbi.nlm.nih.gov/articles/PMC6309046/ (b09-b12, d05)
- [V] Liang et al. (2023), Encouraging divergent thinking in LLMs through multi-agent debate. https://arxiv.org/abs/2305.19118 (a20, a21, c03)
- [V] Du et al. (2023), Improving factuality and reasoning through multiagent debate. https://arxiv.org/abs/2305.14325 (a22, b15, b16, c06)
- [V] Huang et al. (2024), Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (a23, a24, b21, b22, c01)
- [V] Smit et al. (2024), Should we be going MAD? https://arxiv.org/abs/2311.17371 (a25, b17, b18, c04)
- [V] Khan et al. (2024), Debating with more persuasive LLMs leads to more truthful answers. https://arxiv.org/abs/2402.06782 (a26, c07; abstract and intro)
- [V] Sharma et al. (2024), Towards understanding sycophancy in language models. https://arxiv.org/abs/2310.13548 (a27, c10)
- [V] Turpin et al. (2023), Language models don't always say what they think. https://arxiv.org/abs/2305.04388 (a28, c11)
- [V] Si, Yang, Hashimoto (2024), Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109 (a29, b23, b24)
- [V] Chan et al. (2023), ChatEval. https://arxiv.org/abs/2308.07201 (a30; table column order unverified)
- [V] Perez et al. (2022), Red teaming language models with language models. https://arxiv.org/abs/2202.03286 (a31, c16; abstract and intro)
- [V] Zhang et al. (2025), Stop overvaluing multi-agent debate. https://arxiv.org/abs/2502.08788 (b19, b20)
- [V] Mitigating cognitive biases in clinical decision-making through multi-agent LLM conversations. https://pmc.ncbi.nlm.nih.gov/articles/PMC11615553/ (b25)
- [V] Lee et al. (2025), Amplifying minority voices: AI-mediated devil's advocate system. https://arxiv.org/abs/2502.06251 (b26, c18; design only)
- [V] Kamoi et al. (2024), When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 (c02, d09; abstract level)
- [V] Wang et al. (2024), Rethinking the bounds of LLM reasoning: are multi-agent discussions the key? https://arxiv.org/abs/2402.18272 (c05; no per-task numbers recorded)
- [M] Chen et al. (2023), ReConcile. https://arxiv.org/abs/2309.13007 (c08; abstract)
- [V] Wang et al. (2024), Solo Performance Prompting. https://arxiv.org/abs/2307.05300 (c09)
- [V] Halawi et al. (2024), Approaching human-level forecasting with language models. https://arxiv.org/abs/2402.18563 (c12)
- [V] Schoenegger et al. (2024), Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379 (c13)
- [V] Anderson, Shah, Kreminski (2024), Homogenization effects of LLMs on human creative ideation. https://arxiv.org/abs/2402.01536 (c14)
- [V] Jiang et al. (2025), Artificial Hivemind. https://arxiv.org/abs/2510.22954 (c15)
- [V] Wang et al. (2024), Devil's advocate: anticipatory reflection for LLM agents. https://arxiv.org/abs/2405.16334 (c17)
- [M] Chiang et al. (2024), Enhancing AI-assisted group decision making through LLM-powered devil's advocate. https://doi.org/10.1145/3640543.3645199 (c19; PDF not fetched)
- [V] Wynn, Satija, Hadfield (2025), Talk isn't always cheap. https://arxiv.org/abs/2509.05396 (d06; Table 1 and figures not readable in text)
- [V] Tsui (2025), Self-Correction Bench. https://arxiv.org/abs/2507.02778 (d07)
- [V] Kumar et al. (2024), SCoRe. https://arxiv.org/abs/2409.12917 (d08)
- [V] Li, Lin, Xia, Jin (2025), Rethinking mixture-of-agents (Self-MoA). https://arxiv.org/abs/2502.00674 (d10)
- [V] Dhuliawala et al. (2023), Chain-of-Verification. https://arxiv.org/abs/2309.11495 (d11)
- [M] Wang et al. (2022), Self-consistency improves chain of thought reasoning. https://arxiv.org/abs/2203.11171 (d12; numbers not extracted)
- [V] Sileo and Moens (2023), Probing neural language models for words of estimative probability. https://arxiv.org/abs/2211.03358 (d13; setup only, result numbers not extracted)
- [V] Belem et al. (2024), Perceptions of linguistic uncertainty by language models and humans. https://arxiv.org/abs/2407.15814 (d14; exact drop figures not extracted)
- [M] Search logs for this subfield (c22, d16): no direct LLM study of ACH, key assumptions check or premortem found.
