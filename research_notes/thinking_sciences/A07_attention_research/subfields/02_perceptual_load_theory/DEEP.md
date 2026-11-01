# Perceptual load theory: deep document

*Subfield A07.02. Evidence: evidence_a-d.jsonl (a01-a34, b01-b25, c01-c25, d01-d28), claims.jsonl (K01-K37), critique.md. Evidence ids below are those files. Written 2026-11-01.*

## 1. What it is

Perceptual load theory (Lavie and Tsal 1994; Lavie 1995, 2005) is a theory of when irrelevant input gets processed. It is a human vision theory. It makes one central claim and two corollaries.

- Central claim: perception has limited capacity, but it runs automatically on everything within that capacity. A task with high perceptual load uses all of it. Nothing is left for distractors. A task with low load leaves spare capacity, and that capacity spills over onto irrelevant items (a01).
- Corollary 1: top-down settings (an instruction, an intention to ignore) say what is relevant, but only load prevents spillover. "Try harder to ignore" does not work in the theory. A harder task does (a01).
- Corollary 2: load of a different kind has the opposite effect. Working-memory or cognitive-control load removes the resources that keep distractors out, so distractor processing goes up (a02, a27, b09).

Standard evidence types: (1) response competition (a flanker letter that points to the wrong response slows people less at high load); (2) capture by salient irrelevant items; (3) inattentional blindness and deafness (people miss an unexpected object or tone when the main task is hard); (4) brain measures (V1 response, alpha power, mismatch negativity).

Why it is in this study: the schema's S1 (UNDERSTAND) has "input hygiene". The sub-field row asks whether irrelevant content intrudes more when the task is easy. If so, an easy-looking prompt full of side material would be the risky case.

Bottom line, up front:

- The human theory is contested. The classic flanker effect did not replicate in six online experiments (a25). The awareness findings are sturdier (K06).
- No study of language models has tested Lavie's manipulation, and none shows the shield. In every grid we found, distraction stays or grows as the task gets harder (K19, K32).
- LLM distraction by irrelevant context is large and well replicated. It depends on similarity to the task, position, and length. These facts are what the schema can use.

## 2. History and theories in depth

### 2.1 The early-versus-late selection debate

For decades the field argued about where selection happens. Early selection says unattended input is filtered before meaning is extracted. Late selection says all input is identified and selection acts on memory or response. Treisman and Geffen found 87% of attended target words detected versus 8% of unattended words, but late-selection results kept appearing (a02). Load theory (1994) was offered as a hybrid: selection is early when load is high and late when load is low. Benoni and Tsal (2013) disagree with the hybrid label. They read it as early selection with variable efficiency (a19).

### 2.2 Founding studies (second-hand only)

We could not open the founding papers. All of their numbers here are second-hand (critique.md section 3).

- Lavie and Tsal (1994): proposes that the locus of selection depends on the perceptual load of the relevant task (a03). Not opened.
- Lavie (1995): the response-competition paradigm. Distractor interference exists at low load and is removed at high load (a04). Not opened. The pattern is shown in the 2008 replication: 36 ms interference at low load versus -4 ms at high (a06).
- Lavie and Cox (1997): search task with a distractor. Per Benoni and Tsal, going from set size one to four raised RT but did not cut interference. Interference fell only at set size six (a05). Not opened. So load acts like a threshold.
- Lavie et al. (2004): the dissociation. Perceptual load lowers distractor processing. Working-memory load raises it. Reported effect sizes: six-digit versus one-digit memory load r=.604; articulatory suppression r=.514; dual versus single task r=.752 and r=.836 (b10). Second-hand, original not opened.
- Cartwright-Finch and Lavie (2007): inattentional blindness. A cross-judgement task with a surprise shape on the last trial. Second-hand figure: 10% aware at high load versus 55% at low (b15). Not opened. A later adaptation by the same group (Remington et al. 2014, adult Exp 3, 16 per cell) found 15/16 (94%) aware at low load versus 2/16 (13%) at high load, chi-square 21.20, p<.01 (d21). The 2008 review says awareness is typically 40-50% lower at high load (d22). The order of magnitude agrees.

### 2.3 Extensions (2007-2022)

- Invisible stimuli: V1 response to continuously suppressed images fell under high load (fMRI, N=7; a08).
- Load-induced blindness: high load lowers d', so it is sensitivity, not only response bias (a09).
- Inattentional deafness: a visual task makes people miss a clear tone. Capacity is shared across senses (a11, a12).
- Entirely irrelevant distractors: a cartoon character slowed search as much as an incongruent letter at low load (a06).
- Mind wandering: task-unrelated thoughts also fall at high load (a07, d20).
- Object recognition: unattended-object recognition drops under high load (a15).
- Attentional blink and dynamic blindness: 32% noticed a crossing cross at high load versus 71% at low (a14).
- Applied: eyewitness memory for peripheral objects 49.8% versus 9.4% (b17).
- Development and clinical: awareness grows with age (b23). ADHD shows a different profile (b24, a18).
- Semantic gating of unconscious processing (a28).

### 2.4 The critique (2010-2014)

Four lines of criticism.

1. Circularity. Load is never defined independently of its effect. High load is the condition in which interference falls. RT is a weak load check. Interference itself is sometimes used as the load check (a19, b06).
2. Dilution. Set size confounds load with crowding by neutral items. Low-load, high-dilution displays removed interference (Benoni and Tsal 2010; Tsal and Benoni 2010; Wilson et al. 2011; a21). With dilution controlled, high load gave more interference. Chen and Cave (2013) found dilution is conditional: it works only with broad focus, same-category neutrals, and an unknown target (a22, b13).
3. Alternatives. Salience beats load (Eltiti 2005). Similarity and distance matter (Paquet and Craig 1997). Same-object distractors interfere even at high load (Chen 2003; Cosman and Vecera 2012). Mixing load levels removes the effect (Theeuwes 2004; a20).
4. Display duration. Roper and Vecera (2013, N=24 per experiment) found a flanker effect at high load when the relevant display stays up until response. Typical load studies use 17-200 ms, mode 100 ms. The duration of the relevant array drives the leak, not that of the flanker (b03, b04).

### 2.5 Rival and bridging accounts

- Dilution (Tsal and Benoni): neutral items reduce distractor weight.
- Biased competition (Scalf et al. 2013): capacity is competition among stimuli. Fits both load and dilution, so it is hard to falsify (a23, b14).
- Saliency-map model (Neokleous et al. 2016): load patterns emerge from saliency, lateral competition and top-down bias, with no load variable (a24).
- Attentional engagement (Linnell and Caparos 2013): high load narrows attention only when cognitive resources are free. With one digit in memory, high load focused attention. With six digits it did not (b08).
- Active suppression plus target gain (Gutteling et al. 2022): high load raised alpha power on the distractor side and raised target excitability (a17).
- Contrast gain (Lavie et al. 2014): high load shifts the contrast response function right, like lowering contrast (a13).

### 2.6 Recent human evidence (2025-2026)

- Snowden et al. 2025 (same paper as Snowden and Gray): six online experiments, no load reduction of distraction (a25, b01). See section 5.
- Ertan et al. 2026: a reverse load effect for emotional-face distractors, 26.76 ms with 6 cues versus 11.55 ms with 2, N=60 (b21).
- 2026 awareness work: high perceptual load cut noticing only without an added cognitive load task (b19, abstract only).
- 2026 reliability work: group effect robust, test-retest reliability unclear (b20, d24, abstract only).

## 3. Core findings with exact numbers

Status key: established = several independent sources agree; contested = sources disagree or design-dependent; single = one source.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Classic flanker load effect, long display, N=16 | Congruency effect 36 ms low load (t(15)=4.18, d=2.16), -4 ms high; load x congruency F(1,15)=5.19, p=.038 | Forster and Lavie 2008 (a06) | Established in originating lab; contested overall |
| Same, 100 ms display | 25 ms low vs -7 ms high | a06 | As above |
| Irrelevant cartoon distractor | Slowed search; NOT modulated by load (F<1) with long displays (Exp 1). Later 100 ms experiments: 60 and 25 ms at low load, 6 ms at high | a06 | Single lab |
| Failure to replicate, six online experiments | Exp 1 N=36: distraction 56 ms low vs 67 ms high; congruence 197 vs 202 ms; load x distractor p=.98. Exp 2 (200 ms): 58.5 vs 42.4 ms, p=.05. Exp 3 N=34: 2 vs 82 ms. Exp 4 N=24: 22 vs 19. Exp 5: 5 vs 21. Exp 6: -3 vs 41, p=.09. Interaction ns in Exps 1-5. Load main effect huge (Exp 1 F(1,35)=257) | Snowden 2025 (a25, b01) | Contested (one lab, online, interleaved) |
| Response-terminated display brings flanker effect back at high load | N=24; Exp 1 RT 554 vs 840 ms; neutral 684 vs incongruent 710 ms, F(1,23)=34.4, eta2p=.60 | Roper and Vecera 2013 (b03) | Single lab |
| Degraded visibility did not change interference | Interference at high load equal to low at 150 ms, larger at 100 ms (p<.02) | Yeshurun and Marciano 2013 (b05) | Single lab; Ns not extracted |
| Blocked versus intermixed load | Detection d' drop 1.8 blocked vs 0.3 intermixed (Exp 5, N=22) | Macdonald and Lavie 2008 (d22) | Single source; supports design dependence |
| Individual variability | RT pattern matched in 15/103 (15%) people; accuracy 13/103 (13%); new experiment N=20: group F(2,38)=20.23, eta2p=.52 but 7/20 match in RT; each of 7 people reversed in at least one of 5 sessions | Marciano and Yeshurun 2017 (b02) | Single source |
| Load-induced blindness (detection) | N=15: search RT 766 vs 593 ms; errors 11% vs 3%; d' lower at high load F(1,14)=15.44, p=.002; criterion beta 5.5 vs 9.0 | Macdonald and Lavie 2008 (a09) | Established direction |
| Inattentional deafness | Exp 1 N=56: tone heard 21/28 low vs 7/28 high, chi2=14.00. Exp 2 N=48: 21/24 vs 5/24, chi2=21.48. Deafness 79% at high load | Macdonald and Lavie 2011 (a11) | Established direction |
| Inattentional blindness (adaptation) | Adults 15/16 vs 2/16 aware, chi2=21.20 | Remington et al. 2014 (d21) | Established direction; 2007 numbers unverified |
| Meta-analyses of inattentional blindness | Blindness rises with perceptual load; cognitive-load account not clearly supported (abstract only) | 2022 review and three meta-analyses (b18) | Direction established; numbers not read |
| Cognitive load cancels the awareness effect | Five studies, about N=100 per condition: perceptual effect only without added cognitive task | 2026 JEP:HPP (b19) | Single, abstract only |
| Working-memory load raises distraction | 26 studies, 49 experiments: mean r=.202, t(48)=2.95, p<.005; 35 up, 14 down; high-capacity people r=.286. Compatibility effect 78 ms high WM load vs 46 low | de Fockert 2013 (a27, b09) | Established |
| Contrast gain mechanism | N=14: memory accuracy 95% vs 64% (d=1.91); contrast threshold 18% vs 27%, t(13)=2.64, p=.023, d=0.79; asymptote 80% vs 79% | Lavie et al. 2014 (a13) | Single, small N |
| Alpha suppression, MEG | N=30: load x salience F=12.9, p=.001, eta2p=.31; no salience effect at high load | Gutteling et al. 2022 (a17) | Single |
| Held memory cue | N=18: invalid-cue cost at low load F(1,17)=13.87, p<.01; high load F<1. P1 effect at both loads, N1 at low only | Tan et al. 2015 (a16, b11) | Single |
| Mind wandering | Probes with task-unrelated thought: 61.6% vs 48.9% (Exp 1a, N=10); 57.5% vs 44.0% (1b, N=14); Exp 4 N=20: 51.90% vs 41.25%, t(19)=3.43, d=1.57 | Forster and Lavie 2009 (a07, d20) | Single, small N |
| Unconscious semantic gating | n=20 per experiment; late trials 5.36% vs 0.62% slower | Hung et al. 2020 (a28) | Contested; small |
| Mismatch negativity, pooled | k=6, N=97: -0.46 uV [-0.72, -0.20]; power .15-.41 | Wiens et al. 2016 (a29) | Single; fragile |
| Eyewitness | N=111: peripheral objects 49.8% vs 9.4% (d=1.01); window witness ID 61.7% vs 20.3% | Murphy and Greene 2016 (b17) | Single |
| Age | N=188: awareness 7/40 (7-8y), 10/44, 20/40, 16/32, 27/32 (adults) | Remington et al. 2014 (b23) | Single |
| One irrelevant sentence in grade-school math (LLM) | code-davinci-002 CoT micro 72.4, macro 6.0; LTM 77.5/18.0; at most 18% of solved problems stay solved. text-davinci-003 CoT 68.4/9.0 | Shi et al. 2023 (a30, b25, c01) | Established (2022 models) |
| What distracts an LLM: similarity | In-topic micro 63.1 vs off-topic 80.7; role overlap 68.3 vs 76.6; macro 10.2 vs 33.0. Number in vs out of range 70.2 vs 74.6 | Shi 2023 (c02) | Established |
| Same-topic clause, 2024 models | GPT-4o 94.9 symbolic -> 63.1 NoOp; o1-mini 66.0; o1-preview 77.4; up to 65% drop (Phi-3-mini) | Mirzadeh et al. 2025 (d06) | Established |
| Adversarial in-topic context | GPT-4o 0.940 -> 0.390; Claude-3.5-sonnet 0.879 -> 0.495; seven-model mean 0.843 -> 0.323 | Wang et al. 2025 (d08) | Single (adversarial search overstates natural harm) |
| Related versus random documents (RAG) | One related distractor: up to -0.24 (-25%); more: over -0.38 (-67%). Random docs up to +0.07 (+35%), Llama2, 4 docs | Cuconasu et al. 2024 (c07) | Contested on later models |
| Position in context | GPT-3.5: closed-book 56.1, oracle 88.3; worst position fell below closed-book with 20-30 docs; over 20 points spread | Liu et al. 2023 (a31, c08) | Established |
| Length alone | GPT-4o 99.3 base, 69.7 at 32K; GPT-4o mini 84.8 to 13.7; 11 of 13 models under 50% of baseline at 32K. FLenQA 0.92 -> 0.68. Whitespace or masked padding: 13.9% to 85% drop | Modarressi 2025 (c09, c25); Levy 2024 (a33); Du 2025 (d14) | Established |
| Small gold passages missed | Gemini-2.0-Flash 48% small vs 73% large; small gold at start 94% vs 33% near end | Bianchi et al. 2025 (c10) | Single (11 models, 150K runs) |
| Distraction grows with reasoning depth | Grok-3-Beta error exponent 0.11 (2 steps) to 0.49 (5 steps); step accuracy 43% -> 19% (1 to 15 distractors); GPT-4.1 26% -> 2% | Yang et al. 2025 (c11) | Single grid, supported by d04 |
| CogniLoad (22 models) | 14,000 puzzles per open model; by d=5, 12 of 22 under 50%; gpt-5 1.00 -> 0.98 (N=20 to 50), 0.76 at N=250; distractor dip deepens with difficulty | Kaiser et al. 2025 (d04) | Single grid |
| Floor artefact in CatAttack | Error multiples by difficulty, R1: hard 1.80x, medium 3.03x, easy 5.33x; absolute rates only a few percent | Rajeev et al. 2025 (d05) | Explained as floor effect |
| Injected tasks | Claude-3.7-Sonnet MMLU-Redux 99.0 -> 87.2-89.9; injection position, drop: end 60.4%, middle 52.5%, start 48.7%; difficulty barely matters | Zhang et al. 2025 (d07) | Single |
| Medical distractors | Proprietary -3.7 to -3.8% vs open -10.6 to -10.9% | Vishwanath et al. 2025 (d25) | Single |
| Narrow instructions hide a co-present critical item | Text radiology: report 0.09 (gpt-4o-mini), 0.08 (gpt-4o), 0.48 (sonnet), 0.53 (haiku) vs about 1.00 open; strict 0.00 (N=64). Three flagships, 24 scenarios: GPT-5 0.00, Gemini 2.5 Pro 0.00-0.09 vs 1.00; Opus 4.8 0.83-0.96 | Shin 2026 (c14, d01) | Single-source preprint |
| Omission is a threshold | Report 1.00 at zero sub-questions, near zero at one; output length 189 vs 1,770 characters | Shin 2026 (c15, d02) | Single source |
| Monitors miss planted items in long context | Opus 4.6 obvious needle 99.7% at 100K vs 69% at 800K; subtle attacks missed 2x-30x more after 800K; padding both sides 5% (non-thinking) | Martin and Roger 2026 (d03) | Single; contested |
| Irrelevant context in a 2026 agent | gpt-5.4-mini: clean 8/10; irrelevant 299K chars 3/10 (Fisher p=0.0698); external checklist 10/10 vs generic self-check 5/10 (p=0.0325) | Xue 2026 (d15) | Single, 10 runs per cell |
| Interleaved vs appended filler | Gemini-2.0-Flash EM: control 0.85; 20% 0.82; 50% 0.78; 80% 0.72; long neutral control 0.82 (p=.45) | Adapala 2025 (d16) | Single |
| S2A (hard context rewrite) | LLaMA-2-70B: TriviaQA 62.8 -> 80.3 (oracle 82.0); keep-original 74.5; GSM-IC in-topic 51.7 -> 61.3 (oracle 69.7) | Weston and Sukhbaatar 2023 (c04, c05) | Single model; extra pass |
| Analyse-then-filter | GPT-3.5 COT 50.2% -> 74.9% | Jiang et al. 2025 (d09) | Single |
| Name-and-ignore (I3C) | GPT-3.5: +11.7 on GSM-IC2-1K; +11.1 on GSM-ICM-1K; average +6.9 | Wu et al. 2024 (d10) | Single |
| Generic ignore instruction | Shi: 72.4 -> 77.8 (COT); Weston: no consistent gain; Wang: -0.013 to +0.026 across seven models; CatAttack: 37.5% -> 9.9% (small model) | c03, c04, d08, d05 | Contested |
| Oracle distractor-aware truncation | BABILong Haiku +0.083 (p_adj=.003), Sonnet +0.104 (p_adj<.001); Opus +0.008, GPT-5.5 +0.017 at ceiling; naive 25% retention -0.138 to -0.613 | Arjmandi 2026 (d13) | Single; upper bound |

## 4. Mechanisms and models

Explained at the level an engineer can build or test them. The first four are human models. The last four are about LLMs.

### 4.1 Capacity-and-spillover (Lavie)

State: a perceptual budget C per moment. Task demand D comes from the relevant items. Leftover L = max(0, C - D). Distractors get processed in proportion to L. Implementation as a test: define D by an independent metric (items, operations, tokens), not by the result. Predicted curve: interference is flat while D is well below C, then drops to zero once D reaches C. Lavie and Cox suggests a threshold (set size 1-4 flat, 6 down; a05). Eayrs and Lavie (2021) tie the threshold to subitising capacity (d23). Warning: the budget is perceptual. Load of other kinds works differently (4.4).

### 4.2 Dilution

State: a distractor's weight falls with the number of other items competing. Neutral items share the pool. Implementation: weight_i = salience_i / (sum of salience over items + base). Conditions where it works: broad focus, same-category neutrals, unknown target (a22). It predicts the opposite sign from the load account when set size rises with an easy task.

### 4.3 Biased competition and saliency-map (Scalf; Neokleous)

State: every item has a saliency. Items inhibit each other (lateral competition). A top-down bias adds gain to target features. Output: the winning item gets processed. Load effects emerge because more target-like items raise the competition for the target, not because a budget runs out. A usable template for a code-checked distractor model (a24).

### 4.4 Cognitive-control load (de Fockert; Lavie 2004)

State: a control resource holds the task rule and rejects distractors. Filling it with memory items weakens rejection. Effect: distractor processing goes up. In an LLM agent this maps loosely to long task state held in context (lessons, instructions, intermediate results). The map is untested. Evidence: r=.20 meta-analysis (a27). Linnell and Caparos show the two load types interact: high perceptual load focuses attention only when cognitive resources are free (b08).

### 4.5 Softmax budget (LLM)

Attention weights sum to one. Each irrelevant token takes some mass. The Differential Transformer paper states this as "attention noise" and shows a 30-point gap on multi-needle retrieval at 4K (c17). It needs model internals. For a prompt-only agent the lesson is simple: fewer irrelevant tokens, positioned at the edges.

### 4.6 Capture as head shift (LLM)

Attention Tracker finds that injected instructions shift specific heads away from the original instruction (c16). AUROC up to 10.0% better than other detectors. Needs open weights. Not for API-only agents.

### 4.7 Similarity-gated intrusion (LLM, empirical)

In every LLM study with a similarity contrast, harm tracks closeness to the task: in-topic 63.1 vs off-topic 80.7 (c02); related docs -25% vs random +35% (c07); NoOp clause 63.1 vs 94.9 (d06). Implementation as a filter: score each context chunk by overlap with the task, and treat the highest-overlap chunks that do not carry the answer as the most dangerous, not the most useful. Note the tension: high overlap is what a retriever rewards.

### 4.8 Output-scope threshold (LLM, Shin)

A narrow task instruction restricts the output space. A co-present item that the task did not ask about is dropped, even though the same model reports it when asked openly (c14, c15). One narrow sub-question is enough to switch it on. The effect is on output scope, not on perception. The machine analogue of inattentional blindness is therefore an instruction effect. The code fix tested is a second, open-ended critic pass (restored 1.00 at the cost of one inference; d02).

## 5. What holds up

### 5.1 Replications and failures

- Classic flanker load effect: replicated in the originating lab (a06) but failed in six online experiments by another lab (a25). Mixed results also appear elsewhere: Yeshurun and Marciano did not find the basic effect in all four experiments (b05, b07). Status: contested.
- Boundary conditions found: display duration and whether the display ends at response (b03, b04); blocked versus interleaved load (d22, a26); previous-trial load (Eayrs et al. 2024: reduced distraction only when a high-load trial follows a high-load trial; a26); object grouping (a26); what is held in memory (b08); stimulus category and target predictability (a22).
- The strongest replication contradicts the "short display rescues it" story: Snowden Exp 2 at 200 ms still found no reduction (critique.md section 2).
- Founding-paper numbers remain unverified (K35).

### 5.2 Meta-analyses

- Working-memory load raises distraction: r=.202, 35 of 49 up (a27). Publication bias acknowledged. Established in direction, small in size.
- Mismatch negativity: k=6, N=97, -0.46 uV, power .15-.41. Fragile (a29).
- Inattentional blindness: the 2022 meta-analyses support the perceptual account (b18, abstract only).

### 5.3 Reliability

Few individuals show the pattern, and individuals flip across sessions (b02). A 2026 paper finds test-retest reliability unclear at practical trial counts (d24, abstract only). Weight the group-level literature as conditional, and expect single runs to be noisy. This matters for our bench: LLM runs of one prompt vary too. One task showed 73.9% versus 79.7% across identical runs (d28).

### 5.4 What holds up best, ranked

1. Inattentional blindness and deafness rise with high load. Consistent across tone, shape and applied tasks; the adaptation gave 15/16 vs 2/16. Mostly one lab, but meta-analyses agree on direction.
2. Working-memory load raises distraction (opposite sign).
3. Neural and mind-wandering effects: small samples, fragile.
4. Flanker response competition: design-dependent, failed once in a strong test.

### 5.5 Interventions for LLMs: what worked and what did not

Worked:
- Hard rewrite of context to relevant text, then answer from the rewrite only: S2A 62.8 -> 80.3 (c04). Keeping the original beside it lost part of the gain (74.5; c05).
- Analyse-then-filter (50.2 -> 74.9; d09) and named-condition ignore (I3C, +11.7; d10), both on GPT-3.5.
- Self-consistency: COT micro 88.1, LTM 93.4; the right answer is present in 20 samples for 99.7% of problems. Best macro still 45% (a30, c03). Needs a code selector (G4/G5).
- Oracle distractor-aware truncation +0.083 and +0.104 on small current models (d13).
- A detailed external checklist 10/10 vs a generic self-check 5/10 (d15).
- Listing suspicious items first, and short reminders (under 3% extra tokens), for obvious planted needles (d03).
- Chain-of-thought gave the largest robustness gain under prompt overload in 20+ LLMs (d27).
- Recite the evidence first: up to +31.2% on GSM8K for Llama (d14).

Did not work:
- A generic ignore instruction on in-topic or adversarial context: lowered accuracy in one case (d09), changed seven models by -0.013 to +0.026 (d08), gave no consistent gain on LLaMA-2-70B (c04).
- Few-shot examples showing the clause is irrelevant did not repair NoOp (d06).
- RAG and medical fine-tuning did not fix MedDistractQA (d25).
- More thinking does not fix the omission: GPT-5 stayed at 0.00 (d01). Reasoning models are still hurt by CatAttack (R1 4.50% vs 1.50% random; d05).
- Fine-tuning (Yoran et al.) works but is outside our scaffold (c06).

Open: S2A and Thread of Thought were not rerun on 2026 models. At equal total tokens a hard-filter win on distracted prompts is not shown (K21).

## 6. Language models

### 6.1 Is there a load shield in LLMs?

No study applies Lavie's manipulation to an LLM (c24, a34, K29). An arXiv search for "perceptual load" with language model returned zero results on 2026-11-01. We opened the two unverified candidates (2603.00270 and 2601.11585): neither is a load study (d18, d19). The closest controlled grids use working-memory-type load.

Every grid points the same way. Harder main tasks do not protect. They expose.

- GSM-IC: harm grows with steps for COT and PROGRAM, largest at 4+ steps (a30).
- GSM-DC: exponent 0.11 at 2 steps to 0.49 at 5 steps (c11).
- CogniLoad, 22 models including gpt-5, o3, gemini-2.5-pro: the distractor dip deepens as intrinsic difficulty rises; length is the dominant stressor (d04).
- Distractor injection: harm barely depends on distractor difficulty; position and instruction-likeness matter (d07).
- MedDistractQA: capability, not task hardness, predicts robustness (d25).
- The only counter-pattern is CatAttack, where relative harm is larger on easy problems (5.33x vs 1.80x). The authors say this reflects near-zero baselines (d05).

### 6.2 Which distractors hurt

Similarity to the task, not volume (c02, c07, d06). Adversarial, semantically coherent context cuts strong models 38-52 points (d08). Random unrelated documents helped Llama2 (c07), but that did not hold on later models. A 299K-character irrelevant context cut a gpt-5.4-mini agent from 8/10 to 3/10 (d15). Interleaved irrelevant tokens hurt Gemini 2.0 Flash (0.85 -> 0.72 at 80%), while appended neutral filler did not (0.82, p=.45; d16). So where filler sits matters.

### 6.3 Position and length

The U-shape was confirmed on 2023 models (a31) and is still present on Opus 4.6, GPT 5.4 and Gemini 3.1: worst in the middle (d03). Length alone hurts with perfect retrieval (d14). Effective context is far below advertised: GPT-4o claimed 128K, effective 8K (c25). Short critical passages are most at risk (c10).

### 6.4 The machine analogue of inattentional blindness

Shin (2026): see 4.8 and the table. Opus 4.8 is robust (0.83-0.96). GPT-5 and Gemini 2.5 Pro are not. Model family predicted the gap better than scale. Weaknesses: single author, 24 scenarios per model on the flagship test (not 64+), LLM judges (kappa 0.97), disclosed duplicated items. The effect is large (1.00 vs 0.00), so small flaws are unlikely to erase it, but the threshold claim needs a second lab. A related, non-LLM-judged analogue exists in very long transcripts (d03).

### 6.5 Load-like manipulations that changed behaviour

- Explicit dual-task (arithmetic interleaved with a sentence): GPT-4o, o3-mini and o4-mini shifted toward plausibility-based answers, as humans do (d17).
- Noise symbols in n-back lowered ChatGPT's working-memory capacity (about 3 without noise); CoT helped on spatial tasks (c12, c21).
- Overloaded logical thinking jailbroke Llama 2 and ChatGPT; numbers not read (c18).
- Scaffold text itself is load: Llama 3.3 70B collapsed to 0% true recall with prompts above 2KB (d28).

### 6.6 What changed the outcome and by how much

| Change | Effect |
|---|---|
| Hard S2A rewrite | +17.5 points (TriviaQA); +9.6 (in-topic GSM-IC) |
| Keep original too | gives back 5.8 of the 17.5 points |
| Self-consistency, 20 samples | micro +15.7 (COT) |
| Ignore line (Shi) | +5.4 micro |
| Analyse-then-filter | +24.7 (GPT-3.5 COT) |
| I3C | +11.7 |
| Oracle truncation | +0.083 to +0.104 (small models); about 0 at ceiling |
| Open instruction vs narrow | 0.00-0.53 -> about 1.00 report rate (Shin) |
| External checklist vs self-check | 10/10 vs 5/10 |
| Reminders | under 3% extra tokens; helps obvious needles only |
| Model strength | proprietary lose 3.7% vs open 10.6% |

None of the mitigation gains was measured at equal total tokens on a current frontier model, except Focused CoT (cost, not distraction; d11).

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Treat extra context as a cost, not a neutral extra.** One irrelevant sentence sharply lowers accuracy; length alone hurts; effective context is far below the limit. Keep the working context short and drop what is not needed. S1 / G11. [E] K16, K20. a30, c01, a31, a33, c09, c25, d14.
2. **Extend S1 input hygiene to task-like clutter, not only suggestive cues.** The dangerous class is material that resembles the task (same topic, same names, a related non-answer). Code should flag and move or drop it. S1. [E] K17. c02, c07, d06, d08. The current S1 text covers stated guesses, authorities and irrelevant numbers. The new part is similarity-ranked clutter. Number size alone mattered little (70.2 vs 74.6; c02).
3. **Do not assume a hard task is protected from distractors.** Report absolute accuracy loss by difficulty tier. Never write a rule like "relax hygiene on hard items". S1 / S0. [E] K19, K32. c11, d04, d07, d25.
4. **Put the key item at the start or end; keep side content out of the middle.** S1 / G11. [E] K20. a31, d03. Put the question last and keep injected material away from the end (d07: end injection hurts most).
5. **Measure with many items and report flip rates.** Single-run effects are noisy in humans (b02) and in models (d28: 73.9% vs 79.7% on identical runs). G7. [E] K05 (human single source), d28.

### Test first

1. **Open-scope field in the output schema** (also a one-line appended open sentence): "anything unrequested but critical". S1 / G1. [S] K24, K25. c14, c15, d01, d02. Free if it works.
2. **Hard context rewrite** (restate relevant facts, solve from the rewrite, drop the raw context) against plain at equal total tokens. S1. [E] for accuracy on 2023 models, unproven at equal tokens (K21). c04, c05, c19, d11, d13.
3. **Ignore instruction**, split by off-topic versus in-topic distractors, on current models. S1. [C] K22. c03, d05, d08, d09, d10.
4. **Easy-versus-hard planted-distractor grid** with absolute-loss reporting. S1 / S0. [E] that no shield appears elsewhere; the test checks whether our own tasks differ. K19, K29, K32.
5. **Appended versus interleaved filler.** G11 / S1. [C] K18. c07, d14, d15, d16.
6. **List-suspicious-items-first and short periodic reminders.** S1 / G5. [C] K30, K31. d03.
7. **Code-held detailed checklist vs generic self-check.** G5. [C] K31. d15.
8. **Named-candidate filter (I3C style) and entailment gate.** S1 / G5. [S] c06, d10.
9. **Side-task load.** Add a side task in the scaffold; check if plausible-but-wrong answers rise. S1. [S] K36. d17.
10. **Blocked versus mixed difficulty in the context block.** S1. [C] K03. d22, a26.
11. **Held-in-mind items (long task state) versus intrusion.** S1 / M. [E] human direction (K08); the LLM mapping is untested. a27, b09.
12. **Isolate or repeat short critical items.** S1. [S] c10.
13. **Memory lessons as a distractor class.** Lessons that resemble the problem may be the most dangerous distractor. M. [S] by analogy (c02). The schema already shows lessons after the first attempt; test against a no-lesson arm at equal tokens.

## 8. Concrete tests on our bench

All arms at equal total tokens (count extra passes, G7). Code-score answers. Report macro accuracy (same item under all variants) and flip rate per item. At least 65 items per cell.

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Planted critical side-fact in a narrow task (a code bug with an unrelated security flaw; a math word problem with a planted data error) | Narrow / narrow + one open line / narrow + output field "other critical" / open | Report rate of planted item (code string-match); main-task accuracy | Narrow: low report. Open line or field: close to open at near-zero tokens. Add if report rises by 0.3+ with no accuracy loss |
| T2 | Grade-school math and our reasoning items, one planted sentence of 3 types: off-topic, in-topic, role-name overlap | Plain / ignore line / S2A-style rewrite / code filter + plain | Micro and macro accuracy | In-topic hurts most (about 17 points in Shi). Rewrite wins only if it beats plain at equal tokens |
| T3 | Same items at 3 difficulty tiers (steps 2, 4, 6) with and without a planted sentence | Plain | Absolute accuracy loss per tier | Loss stays or grows with tier (expected from c11, d04). A shrinking loss would be the first Lavie signal |
| T4 | Same items, filler 20/50/80% of context | Appended neutral / interleaved irrelevant / none, equal length | Accuracy | Interleaved hurts; appended near neutral on strong models (d16) |
| T5 | Multi-fact tasks with the key fact at start/middle/end of a 4K and a 32K prompt | Plain / reminder every N steps / list-first | Recall of key fact | Middle worst; reminders help obvious needles |
| T6 | Code review with a planted flaw | Generic self-check / code-held detailed checklist | Pass rate | Checklist better (10/10 vs 5/10, d15) |
| T7 | Items with an interleaved arithmetic side task | Single / dual | Share of plausible-but-wrong answers | Rises under dual task (d17) |
| T8 | Same items, difficulty blocked vs mixed in the prompt | Blocked / mixed | Distractor cost | Mixed reduces the cost in humans; direction in LLMs unknown |
| T9 | Items with a lesson shown before vs after first attempt, topic-matched vs unmatched | 4 arms | Accuracy | Matched lessons shown first may harm (fixation plus similarity) |

## 9. What does not transfer, and why

- **The load manipulation itself.** Perceptual load is about visual operations on a brief display. A model reads text in parallel with no eye movement. Our text analogue (task difficulty) is working-memory-type load, whose human prediction has the opposite sign.
- **The brain evidence (alpha, V1, MMN, TMS).** No LLM counterpart without model internals (K09, K10, K26).
- **Mind wandering.** A prompted agent has no free-running thought. A long free-running loop might drift, but nothing supports that yet (K12).
- **Individual differences by age or ADHD.** Maybe an analogue in model size or family. Shin found family predicted the gap better than scale (K13, c15).
- **Display duration.** An LLM sees the full prompt at once. No analogue (b03).
- **Dilution as a shield.** In humans, neutral filler can reduce interference. In LLMs, interleaved filler hurt and long irrelevant context hurt a 2026 agent (d16, d15). Appended neutral filler was harmless once (d16). Do not use filler as protection.
- **Inattentional-blindness numbers as a size guide.** The LLM omission effect is an output-scope effect (instruction narrowing), not perceptual. Use it as a design warning, not a quantitative expectation.
- **Architecture fixes.** Differential Transformer, attention sinks and head-based detectors need model access (K26).
- **Fine-tuning fixes** (Yoran; DPO in Wang): not in our scaffold.
- **Old-model numbers.** Most mitigation numbers use 2022-2024 models. Shin and the 2026 context-rot papers are the only current-model sources.

## 10. Open questions

1. Does any current model show a Lavie-style shield on a text analogue (planted off-topic item, harder main task, equal tokens, code-scored)? So far no.
2. What is Shin's threshold in detail, and does a free appended open line remove it? Untested.
3. Is the human load literature narrower than assumed (blocked designs only), or is the Snowden null a measurement issue? Reliability is unresolved (K34, K05).
4. Does a model-run context filter get close to oracle filtering (K33)?
5. Do S2A and Thread of Thought win on 2026 models at equal total tokens?
6. Do the position and length results hold with scaffolded multi-step reasoning?
7. Which models are family-robust (Opus 4.8) and why?
8. Are the founding-paper numbers (10% vs 55% aware) as reported? The paywalled originals were not opened.
9. Do perceptual-type and cognitive-type load interact in LLMs the way they do in people (K07)?
10. How big is the harm of lessons or examples that resemble the problem when shown before the first attempt?

## 11. Sources

[V] opened (full text or PDF text this session). [M] snippet or abstract only. Evidence ids in brackets.

Human theory and replication
- [M] Lavie and Tsal (1994), no URL (a03).
- [M] Lavie (1995), no URL (a04).
- [M] Lavie and Cox (1997), no URL (a05).
- [M] Lavie (2005) TICS review, https://doi.org/10.1016/j.tics.2004.12.004 (c23).
- [V] Lavie, Beck, Konstantinou (2014), https://pmc.ncbi.nlm.nih.gov/articles/PMC3965161/ (a01, a02, a13, a14).
- [V] Forster and Lavie (2008), https://pmc.ncbi.nlm.nih.gov/articles/PMC2672049/ (a06).
- [V] Forster and Lavie (2009), https://pmc.ncbi.nlm.nih.gov/articles/PMC2706319/ (a07, d20).
- [V] Bahrami, Lavie, Rees (2007), https://pmc.ncbi.nlm.nih.gov/articles/PMC1885953/ (a08).
- [V] Macdonald and Lavie (2008), https://pmc.ncbi.nlm.nih.gov/articles/PMC2672054/ (a09, d22).
- [M] Cartwright-Finch and Lavie (2007), https://doi.org/10.1016/j.cognition.2006.01.002 (a10, b15).
- [V] Macdonald and Lavie (2011), https://pmc.ncbi.nlm.nih.gov/articles/PMC3152714/ (a11).
- [V] Raveh and Lavie (2015), https://pmc.ncbi.nlm.nih.gov/articles/PMC4677383/ (a12).
- [V] Lavie, Lin, Zokaei, Thoma (2009), https://pmc.ncbi.nlm.nih.gov/articles/PMC2759815/ (a15).
- [V] Tan et al. (2015), https://pmc.ncbi.nlm.nih.gov/articles/PMC4476695/ (a16, b11).
- [V] Gutteling et al. (2022), https://pmc.ncbi.nlm.nih.gov/articles/PMC7615060/ (a17).
- [V] Remington, Swettenham, Lavie (2012), https://pmc.ncbi.nlm.nih.gov/articles/PMC3357114/ (a18).
- [V] Benoni and Tsal (2013), https://pmc.ncbi.nlm.nih.gov/articles/PMC3741554/ (a19-a21, b06).
- [V] Chen and Cave (2013), https://pmc.ncbi.nlm.nih.gov/articles/PMC3675768/ (a22, b13).
- [V] Scalf et al. (2013), https://pmc.ncbi.nlm.nih.gov/articles/PMC3650668/ (a23, b14).
- [V] Neokleous et al. (2016), https://pmc.ncbi.nlm.nih.gov/articles/PMC4726798/ (a24).
- [V] Snowden et al. (2025) = Snowden and Gray (2025), https://pmc.ncbi.nlm.nih.gov/articles/PMC12605277/ (a25, a26, b01, d23).
- [V] de Fockert (2013), https://pmc.ncbi.nlm.nih.gov/articles/PMC3659333/ (a27, b09, b10).
- [V] Hung, Wu, Shimojo (2020), https://pmc.ncbi.nlm.nih.gov/articles/PMC7190740/ (a28).
- [V] Wiens et al. (2016), https://pmc.ncbi.nlm.nih.gov/articles/PMC4704804/ (a29).
- [V] Marciano and Yeshurun (2017), https://pmc.ncbi.nlm.nih.gov/articles/PMC5391011/ (b02; details beyond Snowden Exp 1-2 and this paper were not re-checked by the cross-checker).
- [V] Roper and Vecera (2013), https://pmc.ncbi.nlm.nih.gov/articles/PMC3872048/ (b03, b04).
- [V] Yeshurun and Marciano (2013), https://pmc.ncbi.nlm.nih.gov/articles/PMC3665929/ (b05).
- [V] Makovski, Hommel, Humphreys (2014), https://pmc.ncbi.nlm.nih.gov/articles/PMC3960578/ (b07).
- [V] Linnell and Caparos (2013), https://pmc.ncbi.nlm.nih.gov/articles/PMC3731537/ (b08).
- [V] Commentary (2025) on load and dilution, https://pmc.ncbi.nlm.nih.gov/articles/PMC13271119/ (b12).
- [M] Murphy, Groeger, Greene (2016), https://doi.org/10.3758/s13423-015-0982-5 (b16).
- [V] Murphy and Greene (2016), https://pmc.ncbi.nlm.nih.gov/articles/PMC5003837/ (b17).
- [M] 2022 review and three meta-analyses, https://doi.org/10.1177/17470218211064903 (b18).
- [M] 2026 JEP:HPP, https://doi.org/10.1037/xhp0001452 (b19).
- [M] 2026 Psychological Research reliability, https://doi.org/10.1007/s00426-026-02361-y (b20, d24; abstract read in full via Europe PMC).
- [V] Ertan, Baran, Cicek (2026), https://pmc.ncbi.nlm.nih.gov/articles/PMC13634949/ (b21).
- [V] Registered report (2026), https://pmc.ncbi.nlm.nih.gov/articles/PMC13719732/ (b22; Stage 1 only).
- [V] Remington, Cartwright-Finch, Lavie (2014), https://pmc.ncbi.nlm.nih.gov/articles/PMC4005968/ (b23, d21).
- [V] ADHD study (2023), https://pmc.ncbi.nlm.nih.gov/articles/PMC10727773/ (b24; abstract level).

Language models
- [V] Shi et al. (2023), https://arxiv.org/abs/2302.00093 (a30, b25, c01-c03).
- [V] Liu et al. (2023), https://arxiv.org/abs/2307.03172 (a31, c08).
- [V] Yoran et al. (2023/24), https://arxiv.org/abs/2310.01558 (a32, c06).
- [V] Levy, Jacoby, Goldberg (2024), https://arxiv.org/abs/2402.14848 (a33).
- [V] Weston and Sukhbaatar (2023), https://arxiv.org/abs/2311.11829 (c04, c05).
- [V] Cuconasu et al. (2024), https://arxiv.org/abs/2401.14887 (c07).
- [V] Modarressi et al. (2025), https://arxiv.org/abs/2502.05167 (c09, c25).
- [V] Bianchi et al. (2025), https://arxiv.org/abs/2505.18148 (c10).
- [V] Yang et al. (2025), https://arxiv.org/abs/2505.18761 (c11, c22).
- [V] Gong et al. (2023), https://arxiv.org/abs/2305.03731 (c12, c21).
- [V] Zhou et al. (2023), https://arxiv.org/abs/2311.08734 (c13).
- [V] Shin (2026), https://arxiv.org/abs/2606.26529 (c14, c15, d01, d02). Single-author preprint.
- [V] Hung et al. (2024) Attention Tracker, https://arxiv.org/abs/2411.00348 (c16).
- [V] Ye et al. (2025) Differential Transformer, https://arxiv.org/abs/2410.05258 (c17).
- [V] Xu et al. (2024) Cognitive Overload jailbreak, https://arxiv.org/abs/2311.09827 (c18; numbers not read).
- [V] Struppek et al. (2025) Focused CoT, https://arxiv.org/abs/2511.22176 (c19, d11).
- [V] Xiao et al. (2024) Attention sinks, https://arxiv.org/abs/2309.17453 (c20; only skimmed).
- [V] Martin and Roger (2026), https://arxiv.org/abs/2605.12366 (d03).
- [V] Kaiser et al. (2025) CogniLoad, https://arxiv.org/abs/2509.18458 (d04).
- [V] Rajeev et al. (2025) CatAttack, https://arxiv.org/abs/2503.01781 (d05).
- [V] Mirzadeh et al. (2025) GSM-Symbolic, https://arxiv.org/abs/2410.05229 (d06).
- [V] Zhang et al. (2025) Distractor injection, https://arxiv.org/abs/2510.16259 (d07).
- [V] Wang et al. (2025) Adaptive Distraction, https://arxiv.org/abs/2502.01609 (d08).
- [V] Jiang et al. (2025) GSMIR/ATF, https://arxiv.org/abs/2408.10615 (d09).
- [V] Wu, Shen, Jiang (2024) I3C, https://arxiv.org/abs/2403.12744 (d10).
- [V] Xia et al. (2026), https://arxiv.org/abs/2606.29718 (d12).
- [V] Arjmandi (2026), https://arxiv.org/abs/2608.03297 (d13).
- [V] Du et al. (2025), https://arxiv.org/abs/2510.05381 (d14).
- [V] Xue (2026), https://arxiv.org/abs/2607.17937 (d15).
- [V] Adapala (2025) ICE, https://arxiv.org/abs/2509.19517 (d16).
- [V] Emura and Sugawara (2026), https://arxiv.org/abs/2604.26351 (d17).
- [V] Chattaraj and Raj (2026), https://arxiv.org/abs/2603.00270 (d18).
- [V] Kim (2026), https://arxiv.org/abs/2601.11585 (d19).
- [V] Vishwanath et al. (2025) MedDistractQA, https://arxiv.org/abs/2504.01201 (d25).
- [V] Wang (2026), https://arxiv.org/abs/2605.06672 (d26; adjacent: option-position bias, not context position).
- [V] Dettki, Wu, Rehder (2026), https://arxiv.org/abs/2602.02983 (d27).
- [V] Canizares (2026), https://arxiv.org/abs/2604.18897 (d28).
