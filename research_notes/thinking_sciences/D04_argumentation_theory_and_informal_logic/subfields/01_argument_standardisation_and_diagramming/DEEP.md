# Argument standardisation and diagramming: deep document

*Subfield D04.01. Written 2026-11-03 from evidence_a-d.jsonl (a01-a25, b01-b29, c01-c25, d01-d16), claims.jsonl (K01-K33) and critique.md in this folder. Evidence ids are in square brackets. [V] means the page or PDF text was opened; [M] means snippet or citation only.*

**Honest summary first.** Argument standardisation is a mature human craft with a thin LLM literature. The LLM studies measure extraction (F1, accuracy) or LLM-judged quality. No opened study shows that restating a claim with its grounds raises an agent's own downstream accuracy at equal tokens (K26). The best evidence says structure buys inspectability and faithfulness, not accuracy. Most key numbers come from 2026 preprints by single groups. Treat nearly everything for the schema as "test first".

---

## 1. What it is

Argument standardisation means rewriting a piece of natural reasoning into a clear form. The form lists:
- the **conclusion** (what is claimed);
- the **premises** (what is offered in support);
- the **hidden premises** (what must be true for the step to work, but is not said);
- the **support pattern**: **linked** (premises work only together), **convergent** (each supports alone), serial (a chain), or divergent (one premise, several conclusions).

Diagramming draws this form as a map: boxes for statements, arrows for support and attack. Related formats are the Toulmin layout (claim, grounds, warrant, backing, qualifier, rebuttal) and graph formats such as AIF.

The standard recipe [b29, V]: remove noise, restate questions as statements, clarify vague claims, recover unstated parts. The recovered premise should be the "logically minimum" one, the weakest bridge that makes the step valid. Indicator words ("therefore", "because") are neither necessary nor sufficient.

**Where it sits in our schema.** S1 UNDERSTAND (restate the task, say what makes an answer correct) and S2 REPRESENT (write candidate rules). The question for the agent is narrow: does "restate the claim with its grounds, and name what is assumed" help, and in which form?

**Three things people mean by "it works".** Keep them apart:
1. It can be done reliably (agreement between people, or between model and people).
2. The output is rated good (faithful, complete, inspectable).
3. Using it makes the final answer more often correct.

The literature mostly shows 1 and 2. Item 3 is the gap.

---

## 2. History and theories in depth

Founding works were not opened this session (a19-a25 are [M]). Descriptions come from how opened papers cite them. No numbers are given for them.

- **Toulmin (1958), The Uses of Argument [M, a20].** Layout: claim, grounds (data), warrant, backing, qualifier, rebuttal. The warrant licenses the step from grounds to claim and is usually implicit. This layout is used by Habernal et al. for the ARCT task [a09, V] and by Gupta et al. for LLM prompting [c05, V].
- **Beardsley, Thomas (1973) and the linked/convergent split [b28, V].** Thomas introduced "linked". Linked premises need each other; convergent premises support independently. Terminology and where the conclusion is placed in the diagram are disputed. Lawrence and Reed's survey [a05, V] adds divergent (one premise, several conclusions) and defines convergent as "removing one does not weaken the others".
- **Freeman (2011), Argument Structure [M, a21].** Shows the traditional linked definition is ambiguous in everyday text and lets a warrant be treated as a linked premise. Position taken from citations in Stab and Gurevych [a04] and Habernal [a09].
- **Yanal (1991), Conway (1991) [M via a04].** Yanal: linked versus convergent equals one argument versus several. Conway: linked can be omitted. Stab and Gurevych use these to justify not separating linked from convergent when identifying structure. Linking simply means grouping premises under one conclusion.
- **Johnson and Blair, Logical Self-Defense (1977/2006) [M, a22].** The informal-logic standard: a good argument has premises that are relevant, sufficient and acceptable (RSA). Nothing numeric was read. For us, RSA is a checklist for judging a restated argument, not an extraction method.
- **Peldszus and Stede (2013, 2016) [M, a23, a24].** Link diagramming schemes (Beardsley, Freeman, Toulmin) to mining tasks. They built the Microtext corpus: 112 short texts, 576 segments, with central claim, premises, support, rebuttal and undercut. Counts read through Feng and Hunter, not from the original.
- **Practitioner method [a06, a07, V].** Davies, van Gelder and Barnett teach two term-matching rules for hidden premises. Rabbit Rule: a term in the conclusion must appear in some premise. Holding Hands Rule: a leftover term in a premise must pair with a term in another premise. Linked test: ask whether the conclusion still follows if one premise is missing or false. If premise 3 supports the conclusion without 4, but 4 cannot without 3, then 4 depends on 3. Taught method; no accuracy data.
- **Argument mining (2010s on).** Stab and Gurevych (2017) built the persuasive-essay corpus and a joint parser [a01-a04, V]. Habernal and Gurevych applied Toulmin to web discourse [b06, V]. ARCT framed hidden-warrant recovery as a two-way choice [a09]. A 2025 survey of about 250 LLM argument-mining papers [b25, c23, V] says the field moved from trained classifiers to prompting, retrieval and reasoning approaches, and that implicit claims remain weak.
- **Training literature.** Argument-mapping courses (van Gelder, Twardy, Alvarez, Dwyer) claim large critical-thinking gains. Primaries other than Cullen et al. were not opened (section 5).

**Competing positions on linked versus convergent.** (a) It is a real logical difference and needs a label (Pirozelli pipeline [c01]). (b) It is ambiguous in practice and can be skipped [a04]. (c) It is just the question "one argument or several" (Yanal). No study tests which position helps a downstream task (K05).

---

## 3. Core findings with exact numbers

Status: **E** established (two or more independent sources), **S** single-source, **C** contested. "Independent" counts real papers, not evidence lines (critique.md section 1).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Humans agree on major claims and premises, less on plain claims | Fleiss kappa major claim .877 (97.9% agreement), claim .635 (88.9%), premise .833 (91.6%); unitized alpha .810 / .524 / .824; 80 essays, 3 annotators | Stab and Gurevych 2017 [a02, b01] | S |
| Corpus size | 402 essays, 6,089 components (751 major claims, 1,506 claims, 3,832 premises) | [a01] | S |
| Relation agreement is good in clean essays | support kappa .708, attack kappa .737; annotators marked only 0.9% of 4,922 possible pairs | [a02] | S |
| Machine near human on components, further on relations and stance | human F1 .868 / .854 / .844; ILP joint model .826 / .751 / .680 = 95.2% / 87.9% / 80.5% of human | [a03, b02] | S |
| Joint inference beats separate classifiers | claim F1 +.071, linked-pair F1 +.077; heuristic baseline .759 / .700 / .562 | [b03] | S |
| Unlinked premises are a large error source | 37.1% of premises unlinked in model selection data | [b05] | S |
| Agreement falls outside clean essays | Toulmin token-level alpha_U .48 on web discourse (340 docs); comments .59, forums .69, articles .22, blogs .24; by topic .68 to .08 | Habernal and Gurevych 2017 [b06, b07] | S |
| Attack harder than support, pre-LLM and LLM | attack stance F1 .413 in ILP; essays attack F1 52 vs support 94 (Llama-70B); CDCP Llama-13B attack F1 12 | [a03, a14, b15] | E |
| Gated second pass helps attack F1 | attack F1 .383 to .427 at confidence < 0.70 (14% of 2,407 pairs); full debate .378; only 42 attack test items | Baba and Chudziak 2026 [d06] | S |
| Humans recover hidden warrants about 80% of the time | ARCT 79.8% mean (SD .162, N=173); 90.9% with formal reasoning training; 30 of 173 scored 100%; education alone negligible; topic familiarity not significant | Habernal 2018 [a10, b08] | S |
| Early neural models were near chance | random .491, best .556 to .560 on 444 test items | [b09] | S |
| BERT's 77% on ARCT was a cue artefact | 77% peak; warrants alone 71%; "not" predicts label 61%; adversarial set 53% (mean and median 50%); 5 of 20 seeds failed | Niven and Kao 2019 [a11] | S (failed-replication-style result) |
| Single zero-shot LLM beats early models on ARCT | .7928 vs RoBERTa .7564 and LSTM .7050 | Ku et al. 2025 [b11] with [a10] | E |
| Two LLM agents with self-chosen stance beat one | .8694 (sequential), .8446 (simultaneous) vs .7928; assigned stance worse (275/77/35/57 contingency) | Ku et al. 2025 [b12, b13] | S |
| Writing intermediate premises helps entailment checks | ANLI .496 (none) to .716 (3 steps); ARCT .276 to .560; Microtext .426 (none), .512 (1), .555 (4 steps), drop at 5; 250 items per setting; Microtext chance .333 | Feng and Hunter 2026 [a16, a17, c20, c21, d10] | S |
| LLM-written warrants judged acceptable | gold 45.7%, GPT-4 61.7%, Llama-2-70B 26.3%; kappa .18 / .24 / .31 | Gupta et al. 2024 [c06] | S |
| Naming Toulmin triggers the layout | terms present: GPT-4 99-100%, GPT-3 94.6-95.4%, Falcon-40B 35-42.5%; C4 mentions Toulmin 3,401, Walton 975, Freeman 66 | [c05, c07] | S |
| Few-shot GPT-4 near trained models on component type | macro F1 .836 (5 nearest neighbours, 3-ensemble) vs Stab and Gurevych .826, Potash .849, Kuribayashi .856; fine-tuned GPT-3.5 above .857; structural features hurt in-context | Cabessa 2024 [a13] | E (with a12, b16) |
| Small open models unreliable | Llama-2-13B below random on most zero-shot tasks; fewer than 10 demos match PLMs trained on 500 samples | Chen et al. [a12, b16, b17, c10] | S |
| Relation classification is dataset-sensitive | Microtexts Llama-70B 96 vs RoBERTa 67; Nixon-Kennedy 64-68 vs 56-62; macro F1 Llama-70B 75, RoBERTa 68; 1.73 s vs 0.005 s | Gorur 2024 [a14, b14, b15, c11] | E |
| Prompt format moves scores as much as the task | GPT-4 AM 64.5 concrete vs 70.6 symbolic; with CoT format effect p ~ .77, without p < .05 | de Wynter and Yuan 2024 [c16, c17] | S |
| Paraphrase voting adds a few points | +2.4 to +4.5 UKP, +2.6 to +2.9 Args.me; GPT-5.2 78.0% UKP, 91.9% Args.me | Pietron / Gampel 2026 [a15, c12, c13] | S |
| LLM pipeline reconstructs textbook arguments | conclusion 92.50%; span P/R/F1 80.31 / 72.87 / 75.70; relation 80.57%; ratings 2.85 to 2.96 of 3 on 42 arguments (mean 332 chars) | Pirozelli 2026 [b19, c01-c03] | S |
| Same pipeline fails under strict span match on public corpora | AbstRCT span F1 59.65, link 20.82 vs 70.93 / 39.74; AAEC link 0.41 vs 55.72; gold components: AbstRCT link 51.51, AAEC 22.88 | [b21, c04] | S |
| Reconstruction as training data: mixed | ReClor 78.28 to 84.48; UKPConvArg2 92.45 to 92.49; WebisCMV20 55.45 to 53.30; about 41% of premises implicit; over 290 words or 9+ premises hurts | Ryu 2026 [b22-b24] | S |
| Fallacy reconstruction | GPT-4 P@1 57%, Arg@6 89.0%, Llama-2 59.7%; over-predicts False Equivalence | MISSCI [c08, c09] | S |
| Critical-question loop on MT-Bench | Llama 3.1-70B reasoning 8.05 / CoT 7.5 / CQoT 8.4; math 8.95 / 9.25 / 9.55; Nemotron-51B reasoning 6.75 / CoT 7.7 / CQoT 7.3; CQoT best in 18 of 20 | Castagna 2024 [c18, c19, d08] | S |
| Critical-question generation is hard | no model above 57% useful questions across 11 zero-shot LLMs | [d09] | S |
| Argument map shown to users helps on hard verbal items | over-trust b = -0.199, error correction b = +0.182, p = .002, N = 204; 5 of 180 rationales (2.8%) had structure faults; reversed on visual items | Wang 2026 [c22] | S |
| Toulmin-shaped training: inspectability yes, accuracy no | TrustScore 72.89 vs 60.86; accuracy 32.67 vs 32.14 (Llama-3.1-8B, MedCaseReasoning) | Zhan 2026 [d04] | S |
| Toulmin structure correlates with accuracy across models | r = .741, n = 273 pairs, 26,320 blocks, 7 models, 39 benchmarks; GSM8K 74.75 / 77.86 / 84.69 (1.5B, one run) | Kim and Yang 2026 [d03] | S |
| Extracted structure barely helps zero-shot LLMs | F1 .2525 to .2647 (Qwen3.6:27B); best neuro-symbolic F1 .57 vs random .5266; CIs about +-.05 | Bhargava 2026 [d05] | S |
| Verdicts computed from arguments do not beat direct prediction | Qwen3-8B, two claim-verification sets; exact values not extracted | Freedman 2026 [d11] | S |
| LLM reviewer is a poor sole gate | recall .96-1.00 on injected defects, objects to 9.8% of correct graphs, flips 6.2% on identical input, 2,758 ms vs 1 ms | Baba and Chudziak 2026 [d07] | S |
| Argument diagram training helps people | d = 0.71 [0.37, 1.04] LSAT (N=105 vs 56), essays d = 0.87 [0.26, 1.48] (15 vs 44); CCTST effects about 3x LSAT | Cullen 2018 [d01, d02] | C |
| Mapping course claims | about 0.8 SD (van Gelder), 0.70 SD (Alvarez thesis), 0.34 SD typical course; Dwyer 2012: 74 students, 8-week course | [a08, b26, b27] | C |

---

## 4. Mechanisms and models

Written so an engineer could build each piece. The model fills slots. Code does the checks (schema section 1: the program decides, the model writes).

### 4.1 Data structure for a standardised argument
```
Argument = {
  conclusion: Statement,
  statements: [{id, text, source_span, kind: stated|implicit}],
  inferences: [{premises: [ids], conclusion: id, support: linked|convergent|serial,
                 hidden: [ids of implicit premises]}],
  attacks: [{from: id, to: id | inference_id, type: rebut|undercut}]
}
```
Rules the code can check without a model [d07]:
- every inference refers to existing ids (no dangling refs);
- no support cycles;
- every stated statement's source_span is a verbatim substring of the input;
- every stated statement is used or marked unused;
- the conclusion is not a premise of itself.

Why code: the LLM reviewer in d07 found injected defects at .96 to 1.00 recall but objected to 9.8% of correct graphs, flipped 6.2% of identical verdicts, and took 2,758 ms against 1 ms. Code checks are exact on structure. They say nothing about meaning.

### 4.2 Pipeline (components, then links, then types)
Pirozelli's ten-step pipeline is the clearest published recipe [c01]. Condensed:
1. Split text into candidate spans.
2. Pick the conclusion.
3. Link premises to conclusions (support, attack, undercut).
4. Group premises: linked or convergent.
5. Add implicit premises where a step needs a bridge.
6. Check completeness and faithfulness.

Measured weak points: span boundaries (the model merged sentences the gold diagram split) and strict-match link finding on public corpora. Stab and Gurevych show that doing components and links jointly beats separate classifiers (+.071 claim F1, +.077 pair F1) [b03]. For an LLM the analogue is to list components and links in one pass instead of separate calls. That analogue is untested (K03).

### 4.3 Hidden-premise generation with a bounded slot
Feng and Hunter ask for helpful and non-helpful chains of 1 to 3 statements, each under 10 words, no pronouns [a18]. The text is mapped to logic (AMR) and a SAT solver checks entailment. Gains rise with steps (section 3). Limits: two fixed candidate premises, entailment sets only, one engine [d10]. Implementation hint: cap steps at 3 or 4 and keep statements short so the checker can parse them.

Heuristics from teaching:
- **Weakest bridge rule** [b29]: add the logically minimum premise, not a strong one that makes the argument look better.
- **Rabbit and Holding Hands rules** [a06]: find missing premises by unmatched terms. Easy to code as a term-overlap check.
- **Drop-one test** [a07]: remove each premise; if the conclusion stops following, the premise is load-bearing. Linked premises fail together. When the model runs it, it is a judged step; the reliability of an LLM running it is not measured (gap 3).

### 4.4 Toulmin naming as a template
Naming "Toulmin model" in the prompt makes models emit claim, grounds and warrant (GPT-4 99-100%) [c05]. The success metric counted words present, not correctness. Naming Toulmin beat naming Walton or Freeman in all four models, linked to pretraining frequency [c07]. Use the label as a cheap template, then check the parts.

### 4.5 Critical-question loop (CQoT)
Plan written as premises and conclusion; eight critical questions mapped to Toulmin parts; repeat until at least 7 of 8 are yes (up to 5 tries), then 5 of 8, maximum 10 tries; then answer [c18]. Ablation: plan-plus-answer keeps part of the gain (Llama-70B reasoning 8.05, 8.3, 8.4) [c19]. Caveats: different token caps (2000 vs 8192) [d08], LLM judge, and generating good critical questions is itself under 57% useful [d09].

### 4.6 Gated second pass for attack links
First pass labels each pair with a confidence. Only pairs under 0.70 (14%) get a second argue-both-sides pass. Attack F1 .383 to .427 at about 14% of calls; debating everything gave no net gain (249 fixed vs 236 broken) [d06]. A similar pattern (shrink the label space, debate uncertain cases only) won a shared task with 8B models [d12]. This fits G1 (act on a signal, not on a schedule). The signal there is the model's own confidence, which the schema treats as weak (G-table, F09). A code signal such as disagreement between two samples may be better. Untested.

### 4.7 Trace audit by Toulmin roles
TRACE labels each sentence of a chain of thought as claim, evidence, warrant, backing, qualifier, rebuttal or monitor, then scores flow [d03]. Labeller: DeBERTa-v3-base, human kappa .672 on 400 sentences, macro F1 .666. The score tracks accuracy across models (r = .741). As a GRPO reward it lifted GSM8K 77.86 to 84.69. Model size confounds the correlation; one run. It is not a test of restating the input.

### 4.8 Chunking long text
For long papers, sentence-level units anchored on named entities avoided long-range linking [d13]. Silver labels from an LLM ensemble beat the small gold set for fine-tuning. Ryu et al. found arguments over 290 words or 9+ premises degrade training [b24]. No direct length-cliff measure exists.

---

## 5. What holds up

### Replicated or multi-source
- **Attack is harder than support.** Seen in a classical ILP system, in three LLM relation-mining datasets, and in a debate study (K04). The most solid finding here.
- **Strong LLMs match or beat older trained models on component and relation tasks**, with large dataset spread (K09, K14, K16). Gorur's Microtext 96 vs Nixon-Kennedy 64-68 shows that tuning on one corpus misleads.
- **Format changes move scores.** de Wynter shows a 6-point gap from wording alone; Abkenar shows context-aware prompts help Llama2 (48 to 63%) but hurt Llama3 (86 to 61%) [c11, c16].
- **The standardisation recipe** (weakest bridge, restate, remove noise) is textbook and agreed (K25).

### Failures, cues and artefacts
- **Niven and Kao (2019)** broke the ARCT headline: BERT's 77% fell to 53% on the adversarial set (mean and median 50%; 5 of 20 seeds failed to train) [a11]. The word "not" alone gave 61%. Hidden-premise benchmarks can be gamed.
- **No opened source scores a current LLM on adversarial ARCT** (d15: 4 ARCT hits on arXiv). The 79.28% single-LLM figure may be cue-driven. It equals the human mean of 79.8%, which is suspicious rather than reassuring.
- **Structure did not buy accuracy.** Toulmin-form training: 32.67 vs 32.14 [d04]. Extracted structure for zero-shot LLMs: F1 +.012 [d05]. Argument-computed verdicts: not better than direct [d11]. Reconstruction as training data: +6.2 on ReClor, -2.2 on WebisCMV20 [b22].
- **Pirozelli's good numbers do not transfer.** 42 short textbook arguments: strong. Public corpora with exact span match: near zero (AAEC link F1 0.41). Even with gold components AAEC is 22.88 vs prior 55.72, so span finding is the main but not the only bottleneck [b21, c04].
- **Gupta's success metric is presence.** Gold warrants acceptable only 45.7%, kappa .18 to .31. Weak footing for "LLM warrants are better than gold".

### Moderators and boundary conditions
- **Genre.** Clean essays: kappa .63 to .88. Web discourse: alpha .48. Articles .22, blogs .24 [b06, b07].
- **Model size and mode.** Llama-2-13B below random; GPT-4 class fine [a12]. Reconstruction validity win rate: Sonnet 4.5 thinking 80.8 vs 40.8 for plain LLM prompting [b23].
- **Length.** More than 290 words or 9+ premises hurt [b24]. Short texts (332 chars) were Pirozelli's good case.
- **Step count.** 1 to 3 steps help on ANLI/ARCT; on Microtext 4 is the peak and 5 drops [a17]. No common optimum.
- **Fallacies and LLM-written text** are harmful as training material [b24]. Models over-predict False Equivalence [c09].
- **Stance assignment.** Self-chosen stance helps (.8694); assigned stance hurts [b12, b13]. Seen once.

### Interventions that worked (with caveats)
- Gated second pass for attack links (+.044 attack F1; 42 items; not significance-tested) [d06].
- Paraphrase voting (+2.4 to +4.5) [a15].
- Nearest-neighbour few-shot examples (.836) [a13].
- Hidden-premise steps up to 3-4 on entailment sets [a16].
- CQoT on MT-Bench (judge-scored, unequal token budgets) [c18].
- Showing a model-built map to a human on hard verbal items [c22].

### Interventions that did not work
- Explicit structural features in few-shot prompts (hurt) [a13].
- Debating every pair (net zero) [d06]; assigned-stance debate (worse than single) [b13].
- Self-rated certainty as a gate (unreliable) [a15]. Consistent with schema section 4b.
- CoT for argument classification: mixed [c13].
- Mine-then-generate pipeline lost to end-to-end on counter-speech [b18].
- Cross-skill fine-tuning transfers weakly [c15].

### Human training evidence
- Cullen 2018 (Princeton, quasi-experimental): d = 0.71 on LSAT, 0.87 on essays; control pretest 17.4 vs seminar 15.9; weekly feedback confounded with diagramming; essay sample 15 vs 44 [d01].
- Reported effect sizes vary (0.34, 0.70, 0.8). CCTST gains are about three times LSAT gains [d02]. Founder effects flagged by Twardy [a25, M]. Verdict: contested (K24).
- Humans with formal logic or argument training reached 90.9% on ARCT vs 79.8% overall; education alone did nothing [b08].

---

## 6. Language models

### 6.1 Extraction tasks
- **Component type** (major claim, claim, premise): GPT-4 5-NN ensemble macro F1 .836; major claim .914, claim .698, premise .897 [a13]. Claim stays weakest, the same weak point as human agreement (kappa .635). Fine-tuned GPT-3.5 reached above .857.
- **Support/attack relation:** large open models beat RoBERTa on average (75 vs 68), with huge dataset variance [b14, b15].
- **Stance classification:** GPT-5.2 78.0% UKP, 91.9% Args.me; voting +2.4 to +4.5 [a15].
- **Full graph pipelines:** good on textbook text, weak on strict public benchmarks [b19, b21].
- **Implicit premises:** about 41% of premises in the data are implicit; LLMs write fewer implicit premises than humans [b23].
- **Survey view:** implicit claims remain weak; focusing annotators on two labels raised agreement to kappa .81 [b25].

### 6.2 Hidden-premise choice and generation
- ARCT: single LLM .7928 vs trained RoBERTa .7564 [b11]. Cue contamination was not tested on LLMs.
- Debate with self-chosen stance reached .8694. G9 says debate does not beat voting at matched cost. The Ku paper has no token-matched baseline, so it does not overturn G9 (K10).
- Hidden-premise steps raise entailment accuracy up to 3 steps [a16], with a symbolic checker doing the judging. Part of the gain comes from the checker.
- GPT-4 warrants 61.7% acceptable vs Llama-2 26.3% [c06]. Writing the hidden premise helps GPT-4 on fallacy naming but not Llama-2 [c09].

### 6.3 What changed results, and by how much
| Lever | Effect | Source |
|---|---|---|
| Model size and family | Llama-2-13B below random; GPT-4 class beats trained models | [a12, a13] |
| Nearest-neighbour examples | F1 .836 (no matched fixed-demo arm extracted) | [a13] |
| Output format | up to 6 points (64.5 vs 70.6); binary matrix 9.88 F1 | [c16] |
| CoT | removes format sensitivity (p ~ .77 vs < .05) but outputs become alike | [c17] |
| Paraphrase vote (4 prompts) | +2.4 to +4.5 | [a15] |
| Theory name in prompt | 35% to 99% term presence, model-dependent | [c05] |
| Gated debate | +.044 attack F1 | [d06] |
| Reasoning mode (reconstruction quality) | Sonnet thinking 80.8 vs no-think 51.7 validity win rate | [b23] |
| Retrieved examples (shared task) | removing them cut F1 by 5.17 | [d12] |

### 6.4 Does standardising help the model's own reasoning?
This is the decisive question and it is open.
- Toulmin-form training: accuracy the same, trust score +12 [d04].
- Extracted structure given to LLMs: +.012 F1 [d05].
- Argument-first verdict: not better than direct [d11].
- Toulmin-structured traces correlate with accuracy across models [d03]; as a training reward it lifted GSM8K by 6.8 points in one 1.5B run. This concerns reasoning traces, not restating the input.
- Hidden-premise steps with a checker: gains on entailment sets [a16].
- CQoT: judge-scored gains with unequal tokens [c18, d08].
- Coherence filter: dropping forecasts whose reasoning conflicts with the forecast improves accuracy for people and LLMs [d16]. Numbers not read.

Lean: structure improves inspectability and faithfulness. Any accuracy gain is unproven and may come from extra compute.

### 6.5 Reliability of LLM checks
- LLM reviewer: 6.2% verdict flips on identical input [d07].
- Warrant-quality judges: kappa .18 to .31 [c06].
- LLM judges of moral reasoning agree 89.6% on a binary failure call [d14]. That measures judge agreement, not truth.
- Eleven LLMs produce under 57% useful critical questions [d09].

### 6.6 Human use of LLM-built maps
Wang et al. [c22]: maps built from rationales were structurally sound (5 of 180 faults) and reduced over-trust on hard verbal items. They reversed on visual items and had no effect on easy ones. The model did not use the map. Relevant only if our agent shows maps to a user.

---

## 7. What our agent should take

Format: item | schema part | status | evidence ids. The honest result is a short "Add now" list.

### Add now (established)

1. **Weakest-bridge rule for any hidden premise the agent writes.** When S1/S2 states an assumption, it must be the minimum premise that makes the step valid. The agent must not strengthen it. | S1/S2 | **[E]** (textbook recipe from two sources; no accuracy data, so it is a hygiene rule, not a performance claim) | K25; b29, a06.
2. **Never trust a one-corpus or one-format result for argument tasks.** Any bench item that depends on component or relation extraction is run on at least two item sources and reported separately. | G7 bench hygiene | **[E]** | K16, K17; a14, b15, c16.
3. **Attack is the weak link.** If the agent restates an argument, code checks that at least one counter-consideration was listed; do not assume a support-only restatement is complete. | S2 note; supports G2 | **[E]** that attack is harder; the remedy is untested | K04; a03, a14, b15, d06.
4. **If the restate step shows demonstrations, prefer retrieved similar ones over fixed ones.** | S1 | **[E]** (two papers) | K14; a13, a12, b16. Marginal for us; settle on the bench.
5. **Do not add debate or an argument-based gate on top of G9.** Reconfirms G9 and section 4b; no new element. | G9 | **[E]** | K10, K22; b13, d08.

### Test first (single-source or contested)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Restate-claim-with-grounds step before solving (the core S1/S2 question) | S1/S2 | **[C]** (no accuracy evidence either way) | K26, K29, K28; d03, d04, d05, d11 |
| Hidden-premise generation capped at 3 to 4 short statements, checked by code | S2 / O1 | **[S]** | K11; a16, a17, d10 |
| Code checks on the restatement (verbatim spans, no orphan premise, no cycle) before any model review | S2 guardrail | **[S]** | K30; d07 |
| Gated second pass for counter-argument, fired only on low agreement | S6 / O (critic) | **[S]** | K31, K04; d06, d12 |
| Drop-one-premise test, code-run on the agent's own statements | S2 / O1 | **[S]** (human-taught, no accuracy data) | K06; a07 |
| Linked/convergent label | S2 | **[C]** | K05; a04, c03, d05 |
| Toulmin-labelled template ("claim, grounds, warrant") vs plain restatement | S1/S2 | **[S]** | K13; c05, c07 |
| Chunked restatement for inputs over about 290 words or 9 premises | S1 | **[S]** | K20, K32; b24, d13 |
| Paraphrase vote on the restatement | O (self-consistency) | **[S]** | K18; a15 |
| Self-chosen stance two-pass vs single pass at equal tokens | O | **[S]**, conflicts with G9 | K10; b12 |
| Critical-question loop vs token-matched CoT and sample-and-vote | S2 / O | **[S]** | K22; c18, d08, d09 |
| Trace audit by Toulmin role (within one model, fixed length) | G10 support | **[S]** | K28; d03 |
| Format invariance of the restatement (prose, JSON, indexed list) | G | **[S]** | K17; c16, c17 |

---

## 8. Concrete tests on our bench

All tests: both arms at equal tokens (charge the restate step's tokens to its arm). At least 3 seeds. Pre-register the threshold before running.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Reasoning items with a check (math word problems, ARC-style, multi-step QA with distractors) | A plain short reasoning; B restate as claim + grounds + stated assumptions, then solve; C same tokens spent on a second independent attempt and a code vote | exact-match accuracy; paired difference vs C | 0 to +2 points over C; likely none (K26). Larger on items with planted irrelevant material |
| T2 | Items with a suggestive cue (stated guess, authority appeal), from S1 input hygiene | A hygiene only; B hygiene + premise/conclusion split marking which sentences are grounds | accuracy; rate of anchoring on the cue | small gain on small models; none on strong ones |
| T3 | Adversarial ARCT (claim negated, warrants swapped) and original ARCT | single zero-shot run, our model | accuracy on each; gap | original about .79 (Ku); adversarial lower if cue use exists. A gap over 10 points means do not use ARCT as evidence |
| T4 | Hidden-premise step count on three task types (entailment, math, planning/code) | 0, 1, 2, 3, 4, 5 steps at matched tokens | accuracy by step count | peak at 3 to 4 on entailment (Feng and Hunter); flat or negative on math and code |
| T5 | Argument items with 9+ premises or over 290 words | whole restatement vs chunked | premise recall (code-matched spans); answer accuracy | chunking helps above the threshold; no difference below |
| T6 | Corpora with gold links (UKP essays, Microtexts, a held-out set of our own) | one pass listing components + links + stance; separate calls; plus gated attack pass | attack recall and F1 (report n attack items); false-attack rate; calls used | gated pass +0.03 to +0.05 attack F1 for about 15% more calls (d06); needs far more than 42 attack items for significance |
| T7 | Restatements with a deliberate defect (orphan premise, cycle, non-verbatim quote, swapped premise) | code check only; LLM review only; both | defect recall; false-reject rate on correct restatements; latency | code exact on structure, zero on semantic defects; LLM high recall with about 10% false rejects (d07) |
| T8 | Toulmin template vs plain | "According to the Toulmin model" vs "state the claim and why" | part correctness by two judges (report kappa) and final accuracy | parts present 95%+ for a strong model; correctness gain unknown |
| T9 | Output format variance | prose, JSON, indexed list restatement | std of accuracy over formats | with CoT under 1 point; without, up to 6 points (c16) |
| T10 | Drop-one-premise test | code-run (premise removal then re-solve) vs LLM-judged "does it still follow" | agreement with human linked/convergent labels; effect of the label on accuracy | label changes answers rarely; mostly a diagram feature |
| T11 | Critical-question loop | CQoT vs plain CoT vs sample-and-vote at equal tokens; use items with exact answers | accuracy, no LLM judge | gain shrinks or vanishes when tokens are matched |
| T12 | Trace audit | label our own steps by Toulmin role; correlate structure score with correctness within one model at fixed length | within-model AUC | weak; if AUC under .6, drop |

---

## 9. What does not transfer, and why

- **Human argument-mapping gains** (d = 0.71, 0.8 SD). People learn skills over 8 to 12 weeks with feedback. An LLM at inference time does not learn. Not testable on the agent (K24, K27).
- **BERT-era results** (ARCT 77%, ILP parsers). Models are old and cues explained the score [a11]. Useful only as warnings.
- **Small-model results** (Llama-2-13B below random). Our agent uses a strong model.
- **Corpus-specific F1 targets** (UKP essays, AbstRCT). Our agent does not output a gold-span graph for scoring. Exact span match is a benchmark artefact.
- **Textbook reconstruction scores** (Pirozelli ratings 2.85 to 2.96). Plausibility ratings by two annotators on 42 short items; not accuracy.
- **Argument maps shown to humans** [c22]. The agent does not read its own picture.
- **Persuasion prediction and moral-dilemma probes** [d05, d14]. Different target, noisy labels.
- **Debate with self-chosen stance** [b12]. G9 rules out debate at matched cost, and the paper has no matched control.
- **Training-time Toulmin rewards** [d03, d04]. We do not train.
- **Walton critical-question lists** for open arguments [d09]. Under 57% useful; costs tokens for little.
- **Theory-name prompting success rates** [c05]. Presence, not correctness; tied to pretraining frequency, which may differ for our model.

---

## 10. Open questions

1. Does restating a claim with its grounds improve downstream accuracy at equal tokens against plain CoT and sample-and-vote? (The central gap, K26.)
2. Do hidden-premise steps help on math, planning and code, and is the 3 to 4 peak stable across engines and authors? (K11, d10)
3. Does the linked/convergent label change any downstream answer, or only the diagram? Is an LLM-run drop-one test reliable?
4. How do current LLMs score on adversarial ARCT, and how much of 79% is cue use? (d15)
5. How much of CQoT's gain survives a token-matched baseline and a non-LLM judge? (d08)
6. Why is attack recall low, and does a dedicated counter-argument pass raise it without false attacks? Needs a false-attack rate and more than 42 attack items. (d06)
7. Is the gold-span vs full-pipeline gap an annotation-definition artefact or true model error, and does it matter for free-form agent text with no gold spans? (b21)
8. What do the primary mapping studies (Twardy 2004, Alvarez 2007, van Gelder 2015) say, and what is the replication record outside Melbourne? (K24)
9. Is there a length cliff (over 290 words, 9+ premises), and does chunking restore performance? (b24, d13)
10. Do Toulmin-name prompts still give correct (not only present) parts with current models, and is Toulmin still better than Walton? (c05)
11. Is the TRACE correlation (r = .741) real within one model once size and length are fixed? (d03)
12. Founding theory (Toulmin, Freeman, Johnson and Blair) was not opened here. Claims about their positions rest on citations.

**Links to other subfields run in parallel (not covered here):** Chain-of-thought prompting; Worked examples; Self-explanation; Fallacy theory; Dialectical reasoning; Theories of mental representation; Analysis of competing hypotheses; Coherence norms and Dutch book arguments; Consensus and premature agreement; Logic and philosophy of analogical arguments; Surface-cue heuristics; Confidence and metacognition.

---

## 11. Sources

[V] opened (page or PDF text read); [M] snippet or citation only.

**Theory and surveys**
- [M] Toulmin (1958) The Uses of Argument. Book, not opened. [a20]
- [M] Freeman (2011) Argument Structure: Representation and Theory. Not opened. [a21]
- [M] Johnson and Blair (1977/2006) Logical Self-Defense. Not opened. [a22]
- [M] Peldszus and Stede (2013) From argument diagrams to argumentation mining in texts. https://www.igi-global.com/article/from-argument-diagrams-to-argumentation-mining-in-texts/87173 [a23]
- [M] Peldszus and Stede (2016) An annotated corpus of argumentative microtexts. Counts via Feng and Hunter. [a24]
- [M] Sviridova, Cabrio, Villata (2025) Mining implicit arguments for reasoning: a survey. [a19]
- [V] Lawrence and Reed (2019) Argument Mining: A Survey. https://aclanthology.org/J19-4006.pdf [a05]
- [V] Stanford Encyclopedia of Philosophy, Informal Logic. https://plato.stanford.edu/entries/logic-informal/ [b29]
- [V] Wikipedia, Argument map. https://en.wikipedia.org/wiki/Argument_map [b27, b28]
- [V] Li et al. (2025) Large Language Models in Argument Mining: A Survey. https://arxiv.org/abs/2506.16383 [b25, c23]

**Humans, corpora and training**
- [V] Stab and Gurevych (2017) Parsing argumentation structures in persuasive essays. https://arxiv.org/abs/1604.07370 [a01-a04, b01-b05]
- [V] Habernal and Gurevych (2017) Argumentation mining in user-generated web discourse. https://arxiv.org/abs/1601.02403 [b06, b07]
- [V] Habernal et al. (2018) The Argument Reasoning Comprehension Task. https://arxiv.org/abs/1708.01425 [a09, a10, b08-b10]
- [V] Niven and Kao (2019) Probing neural network comprehension of natural language arguments. https://arxiv.org/pdf/1907.07355 [a11]
- [V] Davies, van Gelder and Barnett, computer-assisted argument mapping (Melbourne). https://minerva-access.unimelb.edu.au/server/api/core/bitstreams/f891a7a2-1bfb-5ba6-8800-b55b89108af5/content [a06-a08]
- [M] Twardy (2004) Argument maps improve critical thinking. https://web-archive.southampton.ac.uk/cogprints.org/3008/ (HTTP 403) [a25]
- [V] Dwyer, Hogan, Stewart (2012) Argument mapping and critical thinking in e-learning. https://eprints.teachingandlearning.ie/id/eprint/4011/ [b26]
- [V] Cullen, Fan, van der Brugge, Elga (2018) Improving analytical reasoning and argument understanding. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6279835/ [d01, d02]
- [M] Alvarez (2007) thesis, via Wikipedia only. [b27]

**LLM studies**
- [V] Chen, Cheng, Luu, Bing (2023/2024) Exploring the potential of LLMs in computational argumentation. https://arxiv.org/abs/2311.09022 [a12, b16-b18, c10]
- [V] Cabessa, Hernault, Mushtaq (2024) In-context learning and fine-tuning GPT for argument mining. https://arxiv.org/abs/2406.06699 [a13]
- [V] Gorur, Rago, Toni (2024) Can LLMs perform relation-based argument mining? https://arxiv.org/abs/2402.11243 [a14, b14, b15]
- [V] Abkenar et al. (2024) Assessing open-source LLMs on argumentative unit and relation classification. https://arxiv.org/abs/2411.05639 [c11]
- [V] de Wynter and Yuan (2024) I'd like to have an argument, please. https://arxiv.org/abs/2309.16938 [c16, c17]
- [V] Gupta, Zuckerman, O'Connor (2024) Harnessing Toulmin's theory for zero-shot argument explication. https://aclanthology.org/2024.acl-long.552.pdf [c05-c07]
- [V] Glockner, Hou, Nakov, Gurevych (2024) MISSCI. https://arxiv.org/abs/2406.03181 [c08, c09]
- [V] Castagna, Sassoon, Parsons (2024) Critical-Questions-of-Thought. https://arxiv.org/abs/2412.15177 [c18, c19, d08]
- [V] Calvo Figueras and Agerri (2025) Benchmarking critical questions generation. https://arxiv.org/abs/2505.11341 [d09]
- [V] Gorur, Rago, Toni (2025) Argumentatively coherent judgmental forecasting. https://arxiv.org/abs/2507.23163 (numbers not read) [d16]
- [V] Ku et al. (2025) Multi-agent LLM debate unveils the premise left unsaid. https://aclanthology.org/2025.argmining-1.6 [b11-b13]
- [V] Feng and Hunter (2026) Making implicit premises explicit in logical understanding. https://arxiv.org/abs/2603.06114 [a16, a18, c20, d10]
- [V] Feng and Hunter (2026) Identifying implicit premises for logical reconstruction of argument graphs. https://arxiv.org/abs/2608.18821 [a17, c21]
- [V] Pietron / Gampel et al. (2026) A comprehensive study of LLM-based argument classification. https://arxiv.org/abs/2603.19253 (one paper, two author lists) [a15, c12, c13]
- [V] Pirozelli et al. (2026) An LLM-based system for argument mining. https://arxiv.org/abs/2605.13793 [b19-b21, c01-c04]
- [V] Ryu et al. (2026) Argument reconstruction as supervision for critical thinking. https://arxiv.org/abs/2603.17432 [b22-b24]
- [V] Ajjour et al. (2026) ArgBench. https://arxiv.org/abs/2604.17366 [c14, c15]
- [V] Wang et al. (2026) Graphionale. https://arxiv.org/abs/2608.27932 [c22]
- [V] Bhatia and Parent (2026) Guided sensemaking. https://arxiv.org/abs/2606.02260 [c24]
- [V] Mori et al. (2026) WarrantScore. https://arxiv.org/abs/2601.17377 [c25]
- [V] Kim and Yang (2026) TRACE. https://arxiv.org/abs/2605.29656 [d03]
- [V] Zhan et al. (2026) From answers to arguments (Toulmin-guided curriculum). https://arxiv.org/abs/2604.11137 [d04]
- [V] Bhargava, Tonelli et al. (2026) Have you been convinced? https://arxiv.org/abs/2610.15091 [d05]
- [V] Baba and Chudziak (2026) From argument components to graphs. https://arxiv.org/abs/2606.16047 [d06]
- [V] Baba and Chudziak (2026) On the LLM verification for argument graph generation. https://arxiv.org/abs/2610.27361 [d07]
- [V] Freedman et al. (2026) Neurosymbolic learning for inference-time argumentation. https://arxiv.org/abs/2605.20098 [d11]
- [V] Tran et al. (2026) LLM-INSTRUCT at UZH shared task. https://arxiv.org/abs/2607.20430 [d12]
- [V] Verma et al. (2026) Full-text scholarly argument mining. https://arxiv.org/abs/2610.40196 [d13]
- [V] Henselmans, Prinzhorn, Libert (2026) Measuring AI accountability through argumentation. https://arxiv.org/abs/2609.05088 [d14]
- [V] Search record (3 Nov 2026): arXiv listing for ARCT and Toulmin. https://arxiv.org/search/?query=%22argument+reasoning+comprehension%22&searchtype=all [d15]

*Caveats on sources.* a15 and c12 are one paper under two author lists. b19-b21 and c01-c04 are one Pirozelli paper. a16/c20 and a17/c21 are two Feng and Hunter papers. a12/b16/c10 are one Chen et al. paper. Pirozelli's Table 1 human ratings are column-shifted in the PDF text, so running-text values were used. Sources marked [V] in the evidence files but not re-opened this session (critique.md section 4) are taken as recorded.
