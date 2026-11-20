# Retrieval as consolidation: deep document

*Subfield A06.07. Written from evidence_a-d.jsonl (a01-a33, b01-b25, c01-c25, d01-d19), claims.jsonl (K01-K26) and critique.md in this folder. Evidence ids are cited in brackets. Status tags: [E] established, [S] single-source, [C] contested. Search was rate limited in the last pass, so every "no LLM study found" is a weak negative.*

## 1. What it is

The idea: remembering something is not only a read. It is also a write. When you retrieve a memory, you may strengthen it, link it to what you already know, and make it less dependent on the hippocampus. This is "retrieval as consolidation" (Antony, Ferreira, Norman and Wimber 2017) [a01, b12].

Three things are packed in this label. Keep them apart.

1. **The behavioural fact (very solid).** Testing yourself beats rereading on delayed tests. This is the testing effect. It is large, and it reverses on immediate tests [a07, a09, a10, a33].
2. **The mechanism claim (contested).** The testing effect happens because retrieval acts like a fast version of systems consolidation: hippocampus down, medial prefrontal cortex (mPFC) up, new item integrated into schema [a01, a04, a05].
3. **The schema claim (mixed).** Schema-consistent information integrates faster, so retrieval should help more for material that fits prior knowledge [a19, a21, b14, d03].

The subfield row in SUBFIELDS.md says "Retrieval can speed consolidation; schema-consistent info integrates faster [M, search snippet only]" and names a 2024 Chinese Advances in Psychological Science article. That article was not found or read [d15]. Everything here comes from English primary sources.

Why it matters for our agent is "background only". The agent is a prompt scaffold with no weight training. So the useful questions are narrow:

- Does making the agent answer from memory before it rereads its notes help later recall at equal tokens? (No LLM test exists. [K12, K25])
- Does writing questions about new material before storing it help? (Weight-training analogues say yes; prompt-level untested. [K13])
- Do consolidated notes lose information the agent needs later? (Yes, shown in 2026 papers. [K15])
- Does linking a new note into an existing structure help multi-hop recall? (Yes in engineering papers. [K17])

## 2. History and theories in depth

**1995: Complementary learning systems (CLS).** McClelland, McNaughton and O'Reilly: neocortex learns slowly and finds shared structure only if items are interleaved. The hippocampus learns new items fast without wrecking that structure. Reinstating new memories alongside old ones (replay, in sleep) integrates them over time [a17]. Original CLS says neocortical learning is slow.

**2006-2008: The behavioural founding studies.** Roediger and Karpicke 2006 showed the crossover: restudy wins at 5 minutes, testing wins at 2 days and 1 week [a07]. Karpicke and Roediger 2008 showed that retrieval itself is the driver. Dropping an item from further study did nothing; dropping it from further testing cut recall by more than half [a09]. Karpicke and Blunt 2011 showed retrieval beat concept mapping, the best "deeper processing" rival, including on inference questions [a10].

**2007: Schemas speed consolidation.** Tse et al. in rats: after a flavour-place schema was built over weeks, new one-trial pairs became hippocampus-independent fast [a19]. Tse 2011 tied this to prelimbic mPFC [a20]. Note the schema took weeks to build [d05, K24]. Lehmann 2009 found repeated reactivation could make rodent context memories hippocampus-independent without a long delay [a32].

**2007: Reconsolidation in humans.** Hupbach et al.: a reminder of List 1 before learning List 2 raised List-2 intrusions into List-1 recall two days later [b07]. This was read as "retrieval destabilises a memory so it can be updated". It is the opposite view to "retrieval strengthens". The two views make opposite predictions about what a reminder does [a28, a29].

**2007: A formal model of retrieval and competitors.** Norman, Newman and Detre: oscillating feedback inhibition strengthens weak parts of targets and weakens competitors [a16]. Hulbert and Norman 2015 extended it: when retrieval is interleaved with restudy, forgetting can flip into facilitation, with representational differentiation in hippocampus [a15].

**2010-2018: Rival accounts of the testing effect.** Pyc and Rawson: retrieval practice leads learners to build mediators (cue-to-target links) [a23]. Kornell, Bjork and Garcia's bifurcation model: retrieved items are simply pushed above a recall threshold [a03]. Rickard and Pan's dual-memory theory: separate memory traces form from study events and test events; with no free parameters it predicts test accuracy and effect size across 10 experiments [a24, a25]. None of these needs a consolidation step.

**2013-2014: Sleep and testing.** van Kesteren 2013: the schema-congruency advantage for item recognition appeared only after consolidation (20 h, 48 h), not at once [a21]. Baeuml, Holterman and Abel 2014: sleep helps restudied items but not retrieval-practised ones, shrinking the testing effect [a26, b25]. Antony 2017 read this as "retrieval already did the consolidation work". The original authors read it as bifurcation [a03].

**2016: CLS update.** Kumaran, Hassabis and McClelland: neocortical learning can be rapid when new information fits known structure, with goal-weighted replay. They explicitly link this to AI agent design [a18].

**2017: The founding proposal.** Antony, Ferreira, Norman and Wimber, a four-page TICS Forum piece with no data [a01, a02]. Claims:
- Retrieval pattern-completes the memory and co-activates linked neocortical knowledge.
- Strong co-activation of related memories gives integration. Moderate co-activation of competitors gives weakening and push-apart (Norman's non-monotonic plasticity).
- Predictions: vmPFC up and hippocampus down for retrieved vs restudied items; testing benefit smaller for novel material without schemas; more insight and inference after retrieval; reduced context dependence.
- Behavioural parallels to sleep: testing effects grow with delay; both retrieval and sleep protect from retroactive interference; restudied items gain more from sleep than retrieved ones [a03].

**2018-2019: The first direct test.** Ferreira, Charest and Wimber. mPFC rose within the first session as predicted. The hippocampus did not fall within a session; it fell only across two days [a05, a06]. Published as NeuroImage 2019 [d01]. Himmer et al. 2019 found a within-session fall in hippocampus and mPFC with seven learn-recall rounds, but with no restudy control [a04].

**2021-2026: Boundary and failure work.** Gupta, Pan and Rickard: testing benefit independent of prior study amount [b16]. Ferreira and Wimber 2023: meaningless squiggles show no testing benefit [b14]. Gupta et al. 2026: testing benefit 26% smaller for highly related pairs [d03]. Two 2026 online experiments found no testing effect [d06, d07]. A 2026 EEG study found retrieval, not sleep, merged similar-object representations [b18].

**2023-2026: The LLM side.** Not a test of the human theory. Two lines grew on their own: (a) weight-training with questions and self-generated study material [c01-c09]; (b) agent memory stores with write-time linking, reflection and rewriting [c10-c18]. 2026 papers then found that rewriting memories loses aspect, hedges and dates [b20, b21, b23].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Testing effect crossover, prose, free recall | 5 min: restudy 81% vs test 75% (d=0.52). 2 d: test 68% vs 54% (d=0.95). 1 wk: test 56% vs 42% (d=0.83). Interaction F(2,117)=32.10, partial eta2=.35 | Roediger and Karpicke 2006 Exp 1 [a07] | [E] |
| Restudy feels better than testing | Confidence SSSS vs SSST t(118)=2.95, d=0.54; vs STTT t(118)=3.35, d=0.61. Ratings 4.8, 4.2, 4.0 of 7 | RK 2006 Exp 2 [a08] | [E] |
| Retrieval, not study, drives long-term gain | 1 wk recall: repeated-test conditions about 80%; dropped from testing 36% and 33%. Combined d=4.03. 40 Swahili pairs | Karpicke and Roediger 2008 [a09] | [E] |
| Retrieval beats concept mapping | Exp 1: 0.67 vs 0.45, d=1.50, F(1,38)=21.63. Exp 2: d=1.07 and 1.01. Holds on inference questions | Karpicke and Blunt 2011 [a10] | [E] |
| Retrieval engages hippocampus and mPFC | N=22; 192 word pairs; 1 d later test 0.63 vs restudy 0.51, t(21)=9.25 | Wing et al. 2013 [a11] | [E] |
| Posterior vs anterior hippocampus split | N=50; 0.53 vs 0.36, d=1.22; ROI x retrievals F(5,225)=3.96. Anterior only after 4-6 retrievals | Wiklund-Hornqvist 2021 [a12] | [S] |
| Within-session hippocampal fall | N=31; 28 words, 7 rounds; hippocampus beta=-0.864, R2=.748; three-way F(1,29)=6.68, P=0.015. No restudy control | Himmer 2019 [a04] | [S] |
| mPFC rises with retrieval; hippocampus does not fall within session | N=22; mPFC retrieval slope t(19)=3.66, restudy t(19)=-0.65, difference t(19)=2.60. Hippocampus within-session difference t(19)=-1.69, p=.107. Fall only across 2 days | Ferreira et al. 2018/2019 [a05, d01] | [C] |
| Schema advantage needs a consolidation delay | N=69 (23 per group). Item d': delay x congruency F(2,66)=5.04. 20 h t(22)=2.12; 48 h t(22)=2.55; 0 h n.s. Associative memory advantage present at 0 h, shrinks | van Kesteren 2013 [a21] | [E] |
| Schema makes rat consolidation fast | Schema built over weeks, then one-trial pairs hippocampus-independent. Numbers not read | Tse 2007 [a19, d05] | [S] |
| Retrieval updates memory, fewer old intrusions | Exp 2 N=46: new recall t(45)=3.93, d=0.57; intrusions t(45)=2.75, d=0.36; old A-B unchanged (55.9%, p=.19). Exp 1 N=19, d=1.30 and 1.04 | Ye et al. 2020 [a13, b13] | [S] |
| Retrieval suppresses cortical competitor patterns | N=24; competitor intrusions 9.2% vs unrelated 2.3% (t23=6.53); intrusions fell over 4 repetitions F(1,23)=55.4 | Wimber 2015 [a14] | [C] (Ye 2020 saw no suppression of old memory) |
| Testing effect needs meaning | Squiggles: no benefit (Exp 1A, 1B; 24 vs 24). Objects: restudy better at once, retrieval better after 1 wk | Ferreira and Wimber 2023 [b14] | [S] |
| Prior study depth does not change testing gain | Exp 1 N=95; Exp 2 N=129; Exp 3 N=51; BF01=4.52 for null interaction | Gupta, Pan, Rickard 2021 [b16] | [S] |
| Relatedness shrinks testing gain | N=231, 24 h delay: gain about 26% smaller for high relatedness. Rowland 2014 as quoted: g=0.66 related vs 0.67 unrelated (between-study) | Gupta et al. 2026 [d03] | [C] |
| Sleep shrinks testing effect at 12 h (no feedback) | Exp 1a: sleep vs wake restudy 70.6 vs 48.8 (d=0.78); retrieval+feedback 65.1 vs 45.8; retrieval no feedback 54.6 vs 51.2 (t<1). F(1,70)=29.81 | Abel et al. 2019 [b01] | [E] |
| Sleep effect vanishes at 24 h, 7 d, and with feedback | Exp 2a N=160, 7 d recall 33.8% restudy vs 37.5% retrieval; Exp 2b N=128 | Abel et al. 2019 [b03, a27] | [E] |
| Reconsolidation intrusion effect replicates at 3 days | N=132 planned; reminder>no-reminder t(42)=3.34, d=1.01, BF10=39.3. 2-day null also replicated | Parks et al. 2022 [b06] | [C] |
| Reconsolidation meta-analysis | Mean d=1.03 over eight intrusion effect sizes | Scully et al. 2017 [b08] | [C] |
| Reconsolidation failed replications | Motor sequence: 4 direct (n=64) and 3 conceptual (n=48), no effect. Recognition: 3 experiments, N=40 each, BF about 4-14 for null. Reminder test strengthened and immunised | Hardwicke 2016; Levy 2018; Potts and Shanks 2012 [a29, b10, a28] | [E] that it is unreliable |
| Retrieval training merges similar-object EEG patterns | N=30, within-subject, 4 interventions; only retrieval merged | 2026 EEG study [b18] | [S] |
| Testing effect failed online | Exp 1 N=67 (39.6% completion): F(1,66)=0 for condition. Exp 2 N=129 (30.3% completion): 7.44 vs 6.51 of 19, U=1773, p=0.17, r=0.14 | Prolific studies 2026 [d06, d07] | [S] |
| LLM-written quizzes raise student quiz scores | 0.89 (n=31) vs 0.73 (n=27); U=703, r=0.586. Non-randomised | An et al. 2025 [b19] | [S] |

## 4. Mechanisms and models

### 4.1 Integrate vs differentiate by co-activation (Antony 2017, Norman 2007) [a02, a16]

Core rule, engineer-ready:
- A retrieval cue activates a target memory and, because retrieval is imprecise, also activates neighbours.
- Let `a` be the activation of a neighbour while the target is being retrieved.
- High `a` (strong): strengthen the link between target and neighbour. Result: integration, shared representation.
- Medium `a` (moderate): weaken the neighbour's own unit. Result: push-apart, competitor forgetting.
- Low `a`: nothing.

Predictions: close pairmates are helped, far unrelated ones hurt (retrieval-induced forgetting). Interleaved restudy can turn forgetting into facilitation [a15].

### 4.2 CLS with sleep rules (Liu, Ranganath, O'Reilly 2024) [b04, b05]

A neural-network model with a fast hippocampal and a slow cortical system. Retrieval practice always helps temporally close untested pairmates and hurts far ones. Sleep flips only the far, unrelated case: model 3-way interaction F(1,38)=20.21, np2=.35; sleep facilitation t(19)=4.25, d=0.95; wake impairment t(19)=3.13, d=0.70. Rival rules fail (sleep as extra retrieval gives impairment). Numbers are from the model, 20 simulated subjects per cell. One group, one dataset.

### 4.3 Bifurcation model (rival) [a03]

Each item has a strength. Retrieval pushes strong-enough items far above threshold and leaves weak ones. Restudy gives a uniform small boost. After sleep, restudied items near threshold cross it; retrieved items were already above. No consolidation step is needed to explain "sleep helps restudy more".

### 4.4 Dual-memory model (rival) [a24, a25, b16]

Two independent trace types: one formed by study events, one by test events. Final recall succeeds if either trace is retrievable. Effect size follows from the accuracy of the test event and trace decay. Parameter-free predictions across 10 experiments, and distributions across 509 subjects at 1-7 days. It predicts that the testing gain does not depend on prior study amount (confirmed, b16) and fits relatedness effects [d03]. It has no hippocampal transfer parameter.

### 4.5 Mediator effectiveness [a23]

During tested practice the learner invents cue-to-target mediators. These are more retrievable at final test. Implementable: when answering from memory, record the cue path used.

### 4.6 LLM analogue: pre-instruction-tuning (PIT) [c01, c02]

Recipe: fine-tune on question-answer pairs first, then on documents. The model learns what kind of access will be needed, so it encodes facts in a retrievable way. Llama-2 7B on Wiki2023-film QA exact match: no training 9.5; continued pretraining 27.6; plus instruction tuning 30.3; PIT 48.1. 70B: 17.2, 41.7, 46.4, PIT 62.7. Gains: +17.8 (7B), +16.3 (70B) [critique correction]. QA after documents did not work. The "perplexity curse": document perplexity near 1 does not give retrieval; closed-book 9.5 EM vs open-book 72.2 EM (7B). Storage is not access.

### 4.7 LLM analogue: self-generated study material [c05, c08]

Active Reading: the model writes questions, timelines and paraphrases for a document, then trains on them. SEAL: the model writes "self-edits" (implications, restatements), fine-tunes on them, and RL rewards edits that raise later QA. Both mirror elaborative retrieval-style study, with the cost of weight updates.

### 4.8 Offline consolidation: sleep-time compute [c07, c25]

Loop for a stored context `C`: before any query, the model anticipates questions on `C`, precomputes inferences, stores the result `C'`. At query time it answers from `C + C'` with a small budget. About 5x less test-time compute at equal accuracy. Works only when queries are predictable from context. Authors say changing context between rounds is not handled.

### 4.9 Write-time linking: HippoRAG, A-MEM [c10, c17]

On write: an LLM extracts noun-phrase nodes and links them into a graph (HippoRAG), or finds similar notes, links them, and may rewrite old notes (A-MEM). On read: Personalized PageRank (HippoRAG) or neighbour traversal. This is the engineering analogue of schema integration.

### 4.10 Strength-on-recall: MemoryBank [c13]

Each memory has strength S. Retention R = exp(-t/S). On recall: S += 1, t = 0. Direct implementation of "retrieval strengthens". Never ablated.

### 4.11 Rewriting drift [d08, b20, b21]

If consolidation means training a generator on its own recalls, recalls drift toward the category mean over rounds, like Bartlett distortion in humans (Mistral 7B, cosine distance to category mean, 100 recalls per topic, epoch 5, temperature 0.5). In agent memory stores the same pressure shows up as aspect flattening ("is working" becomes "works"), hedge-to-fact conversion, and dropped dates.

## 5. What holds up

**Established.**
- The testing effect on delayed tests, d about 0.8 to 1.2 at 2 days to 1 week with free recall, word pairs and science text [a07, a09, a10, a11, a12]. Five or more independent sources. Retrieval beats concept mapping, so it is not just "more elaboration" [a10].
- The crossover: restudy wins immediately [a07, b14]. Learners misjudge this and prefer restudy [a08].
- Retrieval engages hippocampus and mPFC and this predicts later memory [a11, a12, a05].
- Schema-congruent items gain after a delay [a21].
- Sleep modulates the testing effect only narrowly: 12 h, no feedback [b01-b03, a27].

**Contested or weakened.**
- Fast consolidation neural signature. Within-session hippocampal fall: Himmer yes, Ferreira no. Across days: yes. Tasks differ [K03].
- Competitor suppression: Wimber 2015 yes, Ye 2020 no (only intrusions reduced) [K08].
- Schema moderation: relatedness effect 26% smaller in N=231; Rowland g 0.66 vs 0.67; Carpenter 2009 Exp 1 smaller, Exp 2 none; Walsh and Rissman 2023 no significant difference as described [d03, d04]. Prior study depth: no effect [b16]. Meaning needed: squiggles fail [b14]. Net: no clear evidence that schema-richer material gains more.
- Reconsolidation: Hupbach replicates at 3 days (d=1.01) and meta-analyses at d=1.03, yet motor-sequence and recognition versions fail, and a reminder test can protect memory [K09]. Intrusion may be explained by context or retroactive interference [b08].
- Rival theories fit without any consolidation step [K10]. A gain in the testing effect is not evidence of consolidation.

**Failures and moderators.**
- Online Prolific studies found no effect (N=67 and N=129; completion 39.6% and 30.3%). Direction was positive in the second (r=0.14). Treat as noisy, not as a refutation [d06, d07].
- At low initial accuracy retrieval is harder: in Ye 2020 updating retrieval began near chance while restudy was 99.0% correct [a13].
- Initial-test format: recall tests beat recognition tests in Rowland 2014 [a22].
- Material: no benefit for meaningless stimuli [b14].
- Sleep and feedback: with corrective feedback sleep helps retrieved items too [a27].

**Interventions that worked.** Retrieval with feedback; spaced repeated retrieval to criterion [a09]; question-first training for LLM weights [c01]; self-generated study content [c05, c08]; write-time linking [c10, c17]; reflection notes [c14, c15].

**Interventions that did not.** Reading the document alone for weights (SEAL passage-only 33.5 vs 32.7 base) [c08]; QA training after documents [c01]; reminder-based updating as a general tool [a29, b10]; unverified-tag labelling on memory notes (ignored by models) [b21].

## 6. Language models

**No direct test.** About 20 queries across arXiv, Europe PMC and others found no LLM study of retrieval-before-reread, retrieval-induced forgetting, reconsolidation or question-first self-study without weight updates [b24, c21, d11, d12, d14, d19]. This is a weak negative: the search tools returned HTTP 429 on most calls. The one retrieval-practice hit used an LLM to make memory cues for human learners [d18].

**Weight-training analogues (change the model, not a prompt).**
- PIT: 7B 30.3 to 48.1 EM (+17.8), 70B 46.4 to 62.7 (+16.3). Training QA before documents works; after, it did not [c01].
- Allen-Zhu and Li: models memorise but fail to extract without augmentation. Held-out QA 0 to 9.7% without it, 96.6% with rewording plus shuffling. Mixed training out-of-distribution 86.6% (bioS single) and 77.7% (bioR single). Real-world-like case 10.0 to 76.3% [c03, c04]. Small models from scratch, synthetic.
- Active Reading (Llama 3.1 8B, SimpleWikiQA graded by GPT-4o): base 7.42; repeat 15.92; paraphrase 25.74; synthetic QA 47.87; Active Reading 63.33 task-agnostic, 66.25 task-specific; gold context in prompt 65.85. FinanceBench: 26% (+160%). At scale, WikiExpert-8B on 1T tokens: SimpleQA 23.5 vs Llama 8B 7.3 and Llama 405B 17.1; NQ 29.0 to 31.2, TriviaQA 64.3 to 68.5 [c05, c06].
- SEAL (Qwen2.5-7B, SQuAD no context): base 32.7; passage 33.5; own implications 39.7; GPT-4.1 data 46.3; SEAL after RL 47.0; 58.2 for 200-passage continued pretraining; ARC few-shot 72.5% vs 20% [c08]. The paper admits catastrophic forgetting over sequential edits.
- Two-speed memory (fast adapters, slow replay) at 1,000 episodes is a 2026 preprint, abstract only [d09].
- Larimar: external episodic memory beside a frozen LLM, one-shot edits 8-10x faster; framing only [c19].

**Offline compute.** Sleep-time compute: about 5x less test-time compute at equal accuracy on Stateful GSM-Symbolic and AIME; more offline compute gives up to +13% and +18%; 2.5x lower cost per query when amortised. Needs predictable queries [c07, c25].

**Agent memory systems (authors' own baselines, mostly LLM judges).**
- Generative Agents TrueSkill: full 29.89; no reflection 26.88; no reflection or planning 25.64; crowdworker 22.95; none 21.21 [c14].
- Reflexion: HumanEval pass@1 91% vs 80%; ALFWorld 130 of 134, +22% absolute; HotPotQA reflection +8% [c15, c23].
- Voyager skill library: 3.3x more unique items, up to 15.3x faster milestones [c16].
- A-MEM (GPT-4o-mini F1 on LoCoMo): Multi-Hop 9.65 (no linking, no evolution), 21.35 (links only), 27.02 (full); Temporal 24.55, 31.24, 45.85; Single Hop 13.28, 39.17, 44.65; Adversarial 15.32, 44.16, 50.03. About 1,200 tokens per memory operation vs 16,900 [c17, c22].
- HippoRAG: R@2 and R@5 average 53.9/65.6 (ColBERTv2) to 57.2/72.6; 2Wiki R@2 71.5, R@5 89.5; QA F1 35.5 to 42.5, with IRCoT 51.7; 10-30x cheaper than IRCoT [c10-c12].
- Mem0: 26% relative LLM-judge gain over OpenAI memory; over 90% token saving vs full context [c18].
- MemoryBank rule S+=1 on recall: never ablated [c13].

**What goes wrong when memory is rewritten (2026).**
- Aspect flattening: writers turned progressive into simple present in 210 of 381 pairs, never the reverse, across 11 models and in mem0, Graphiti and Letta. A reader (GLM-5.2) acted without asking on 64% of "works" notes vs 40% of "is working" notes; effect varies by reader [b20].
- Hedge-to-fact: a hedged remark becomes a flat dated fact that agents obey on all five models. Passive "unverified" tags were ignored; do-not-trust instructions worked [b21].
- Date loss: gist compression on LoCoMo (1,501 questions per condition). Salience-weighted gist with temporal anchors protected: 0.468 accuracy, +0.298 over truncation, +0.231 over sliding window. Temporal category full gist 0.156; protecting anchors +0.314 [0.254, 0.375], n=315 [b23].
- Drift toward prior: a Mistral 7B model of consolidation-by-rewriting pulled recalled stories toward category mean, like human Bartlett distortion [d08].
- Stale values: a learned forget-and-merge gate on a 793K-parameter transformer recovered newest-value retrieval: 99.0-99.5% at 2-5 prior updates, 97.0% at 10; best baseline 18.0% at 2 and 10.0% at 5; fell to 16.5% at 30. Synthetic only [b22].
- A-MEM's rewriting of old notes: drift not measured [c17, d17].

**Education use.** LLM-written multiple-choice retrieval quizzes: 0.89 vs 0.73 next-week quiz, non-randomised, different weeks [b19].

## 7. What our agent should take

Schema parts: G guardrails, S states, O operators, memory (SCHEMA.md section 5). The schema's S1 already says "keep the original wording beside" the restatement; the evidence below supports that rule and extends it to memory notes.

### Add now (established)

1. **Keep source wording and dates beside any consolidated note.** Part: memory + G (S1 original wording). [E] K15. Evidence b20, b21, b23, c17, d08. Rule: every stored note carries the original sentence, its date, and any hedge words verbatim. Never store only a gist. Cost is a few tokens per note. The fix itself is untested (K25), so measure it (test T5).
2. **Do not let a summary overwrite the raw record.** Part: memory. [E] K15, K23 (drift). Append-only raw layer plus derived layer; derived notes are replaceable.
3. **Write-time linking of a new note to related existing notes.** Part: memory. [E] K17. Evidence c10-c12, c17, c22. Gain is on multi-hop questions. Authors' own baselines, so size is uncertain.
4. **Store a lesson only after a verified outcome (success or located failure).** Part: S9 / memory. [E] K16. Evidence c14-c16, c23. Already matches S9.
5. **Mark superseded entries as superseded rather than leaving both live.** Part: memory + G (stale value). [S] K20, evidence b22 (synthetic). Low-risk hygiene, not a proven gain at prompt level.
6. **Read any "retrieval improved recall" result as unexplained by consolidation.** Part: G7 reading rule. [E] K10. Evidence a22-a25, b16. Rival theories fit; a gain does not prove mechanism.

### Test first

1. **Retrieve-before-reread** (answer from memory, then check against notes) vs plain reread, delayed fact test. Part: memory/O. Human effect [E] K01; LLM transfer unknown K12. Evidence a07, a09, a10, d11. This is the direct test.
2. **Question-first self-study** (agent writes questions on new notes before storing). Part: memory. [S] K13, weight-training analogue only. Evidence c01, c05, c08, d12.
3. **Offline digest of stored notes** (sleep-time compute at prompt level). Part: memory/O. [S] K14. Evidence c07, c25.
4. **Strength-on-recall rule** (retention extends when a note is used). Part: memory. [S] K18. Evidence c13.
5. **Retrieval-induced forgetting in agent stores** (does retrieving A hurt B?). Part: memory/G. [S] K07, K25. Evidence a14, b04, d14.
6. **Update test A-B then A-C**, retrieving the new vs rereading the new, counting old-answer intrusions. Part: O (update conflicting memory). [C] K08. Evidence a13, b13.
7. **Linked vs isolated storage of new facts after a long gap.** Part: memory. [E] in humans K04, [C] for moderation K05, K22. Evidence a21, b14, d03.
8. **Reminder-before-new-info raises intrusions in a prompted agent.** [C] K09. Do not build on it; test only to know the hazard. Evidence b06, b08, a29, b10.

## 8. Concrete tests on our bench

All arms at equal total tokens (reading plus generation). Scores by code, not by a model judge (G8). At least 3 seeds, paired differences, setup tokens counted (G7).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Delayed fact recall: 40 new facts in a session, queried after 20+ intervening turns (or a context reset with notes only) | A: reread notes twice. B: answer from memory, then read notes once with feedback | Exact-match accuracy at delay; also at immediate query to see the crossover | Human d about 0.8; LLM unknown. Expect B lower or equal immediately, higher at delay only if the agent actually loses context. Success if B beats A by 5+ points |
| T2 | Same facts: feedback vs no feedback after the retrieval attempt | B with feedback vs B without | Accuracy; error persistence | Feedback should help (a27, b01). Checks that the attempt, not only re-exposure, matters |
| T3 | 30 documents, later QA | A: store notes. B: agent writes 5 questions per doc, answers them, stores Q+A with notes | QA accuracy at delay | PIT-like gain; prompt-level size unknown. Add if +5 points |
| T4 | Multi-hop questions over stored facts | A: append-only. B: link-on-write | Multi-hop EM/F1; tokens per write | A-MEM-style gain (Multi-Hop 21.35 to 27.02); smaller on single hop |
| T5 | User statements with hedges, aspect ("I am working on X"), dates; later decisions | A: gist note only. B: gist plus verbatim sentence and date | Rate of wrong-confidence actions; temporal accuracy | Fewer hedge-to-fact and tense errors. Measure token cost |
| T6 | Related fact pairs (A, B): retrieve A repeatedly, then query B | Retrieve A vs reread A vs control | B accuracy relative to control | Tests retrieval-induced forgetting in context or note store. Sign unknown |
| T7 | A-B then A-C updating, queries on A | Retrieve new C vs reread C vs reminder of B first | New accuracy; old-answer intrusion rate | Human: fewer intrusions with retrieval (d=0.36). Reminder arm tests the hazard |
| T8 | Notes with predictable vs unpredictable follow-up queries | Raw notes vs notes plus offline digest at fixed query-time budget | Accuracy; query-time tokens | About 5x compute gain only when predictable; none when not |
| T9 | Facts used 0, 1, 3, 6 times over a long run | Flat store vs strength-on-recall ranking | Recall of heavily used vs unused facts; stale-fact rate | Unknown; MemoryBank never ablated |
| T10 | Meaningful domain facts vs random IDs | T1 on each | Interaction of arm x meaning | Humans: no benefit for meaningless stimuli. Same in LLM would mean retrieve-first only suits structured content |

## 9. What does not transfer, and why

- **Hippocampus and mPFC signatures.** The agent has no such regions. K02 and K03 are not testable.
- **Sleep.** No biological sleep. Closest analogue is an offline digest pass [c07]. The sleep x retrieval interaction [K06] has no counterpart.
- **Reconsolidation.** A prompt does not destabilise a stored trace. Contested in humans anyway [K09].
- **Weight-level results.** PIT, Active Reading, SEAL, Larimar and the two-speed adapters change weights. Our scaffold does not train. Transfer to prompt-level study steps is untested [c01-c08, d09].
- **Forgetting as the default state.** Humans forget between sessions; a context window or note store does not decay unless we make it. The crossover (restudy wins early) may not appear if nothing is forgotten. Retrieval practice may only pay when the agent must work from memory or from a truncated context.
- **Effort and desirable difficulty.** Human retrieval gains are tied to effort (recall beats recognition [a22]). An LLM generating an answer is not effortful in the same way.
- **Student calibration.** Students misjudge restudy as better [a08]. An LLM has no such feeling; its verbal confidence is a different problem.
- **Authors' own baselines in agent-memory papers** limit how much their sizes can be trusted [critique].
- **Consolidation as a theory.** Rival accounts fit all the behavioural data [K10]. The agent should use the practice, not the mechanism story.

## 10. Open questions

1. Does retrieve-before-reread beat reread at equal tokens for an LLM agent? (Gap 1, open.)
2. Does question-first self-study help without weight updates? (Gap 2, open.)
3. Does keeping verbatim wording beside the note remove aspect and hedge errors, and at what cost? (Gap 3, open.)
4. Does retrieval-induced forgetting appear in LLM agents? (Gap 4, open.)
5. Exact Rowland 2014 overall g, and the effect on schema-poor material. (Partly closed: g 0.66 vs 0.67 quoted; N=231 study shows 26% smaller for related pairs.)
6. Tse 2007 numbers (days to schema, retention). Not read [d05].
7. Does link-on-write cause drift or overwriting of true detail? Not measured [c17, d17].
8. What does sleep-time compute gain when stored context changes between rounds? [c25, d16]
9. Does the 2024 Chinese review add schema-consistency data? Not found [d15].
10. Why did Himmer 2019 see a within-session hippocampal fall and Ferreira not? Task difference or noise.
11. Are the 2026 online null results about attrition and engagement, or about the effect? [d06, d07]
12. Did the anterior-posterior hippocampus split replicate? Single study [a12].

## 11. Sources

[V] = opened and read. [M] = abstract or snippet only. Evidence ids in brackets.

Founding and theory
- [V] Antony, Ferreira, Norman, Wimber 2017, Retrieval as a fast route to memory consolidation. https://pmc.ncbi.nlm.nih.gov/articles/PMC5912918/ [a01-a03, b12]
- [M] McClelland, McNaughton, O'Reilly 1995. https://pubmed.ncbi.nlm.nih.gov/7624455/ [a17]
- [M] Kumaran, Hassabis, McClelland 2016. https://pubmed.ncbi.nlm.nih.gov/27315762/ [a18]
- [M] Norman, Newman, Detre 2007. https://pubmed.ncbi.nlm.nih.gov/17907868/ [a16]
- [M] Hulbert and Norman 2015. https://pubmed.ncbi.nlm.nih.gov/25477369/ [a15]

Testing effect, behavioural
- [V] Roediger and Karpicke 2006. https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf [a07, a08]
- [V] Karpicke and Roediger 2008. https://learninglab.psych.purdue.edu/downloads/2008/2008_Karpicke_Roediger_Science.pdf [a09]
- [V] Karpicke and Blunt 2011. https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Blunt_Science.pdf [a10]
- [M] Roediger and Butler 2011. https://pubmed.ncbi.nlm.nih.gov/20951630/ [a33]
- [M] Rowland 2014 meta-analysis. https://pubmed.ncbi.nlm.nih.gov/25150680/ and https://doi.org/10.1037/a0037559 [a22, b17, d02]
- [M] Pyc and Rawson 2010. https://pubmed.ncbi.nlm.nih.gov/20947756/ [a23]
- [M] Rickard and Pan 2018. https://pubmed.ncbi.nlm.nih.gov/28585057/ [a24]
- [M] Rickard 2020. https://pubmed.ncbi.nlm.nih.gov/32409922/ [a25]
- [V] Gupta, Pan, Rickard 2021. https://rickardlab.ucsd.edu/pdf/Gupta-Pan-Rickard-2021.pdf [b16]
- [V] Gupta, Pan, Rickard 2026 (also quotes Carpenter 2009 and Walsh and Rissman 2023 second-hand). https://doi.org/10.1038/s41539-026-00416-8 [d03, d04]
- [V] Prolific testing-effect failures 2026. https://doi.org/10.3389/fpsyg.2026.1727423 [d06, d07]

Neural
- [V] Wing, Marsh, Cabeza 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3932674/ [a11]
- [V] Wiklund-Hornqvist et al. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC7821628/ [a12]
- [V] Himmer et al. 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6482015/ [a04]
- [V] Ferreira, Charest, Wimber 2018 preprint. https://www.biorxiv.org/content/10.1101/458687v1 [a05, a06]
- [M] Ferreira, Charest, Wimber 2019 NeuroImage. https://doi.org/10.1016/j.neuroimage.2019.07.009 [d01]
- [V] Ye et al. 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7272192/ [a13, b13]
- [V] Wimber et al. 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4394359/ [a14]
- [V] 2026 EEG retrieval vs sleep study. https://pmc.ncbi.nlm.nih.gov/articles/PMC13430988/ [b18]
- [M] 2026 Current Biology mPFC relational map. https://doi.org/10.1016/j.cub.2026.05.068 [d10]

Schema
- [V] van Kesteren et al. 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3567062/ [a21]
- [M] Tse et al. 2007. https://pubmed.ncbi.nlm.nih.gov/17412951/ and https://doi.org/10.1126/science.1135935 [a19, d05]
- [M] Tse et al. 2011. https://pubmed.ncbi.nlm.nih.gov/21737703/ [a20]
- [M] Sharon, Moscovitch, Gilboa 2011. https://pubmed.ncbi.nlm.nih.gov/21199935/ [a31]
- [M] Lehmann et al. 2009. https://pubmed.ncbi.nlm.nih.gov/19553378/ [a32]
- [V] Ferreira and Wimber 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10519161/ [b14]
- [M] Ashton, Staresina, Cairney 2022 (abstract and design). https://pmc.ncbi.nlm.nih.gov/articles/PMC9231735/ [b15]

Sleep
- [V] Abel et al. 2019 and Baeuml et al. 2014. https://baeuml.app.uni-regensburg.de/paper/papers_open/JEPLMC_sleep.pdf [b01-b03, b25]
- [M] Baeuml, Holterman, Abel 2014. https://pubmed.ncbi.nlm.nih.gov/24933697/ [a26]
- [M] Baeuml and colleagues 2019. https://pubmed.ncbi.nlm.nih.gov/29698042/ [a27]
- [V] Liu, Ranganath, O'Reilly 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11543715 [b04, b05]

Reconsolidation
- [V] Parks et al. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9012516/ [b06, b07]
- [M] Scully, Napper, Hupbach 2017. https://europepmc.org/search?query=%22Does%20reactivation%20trigger%20episodic%20memory%20change%22 [b08]
- [M] Hardwicke, Taqi, Shanks 2016. https://pubmed.ncbi.nlm.nih.gov/27114514/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC4868433/ [a29, b09]
- [V] Levy et al. 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC5906735/ [b10]
- [V] Craig, Dewar et al. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC7812862/ [b11]
- [M] Potts and Shanks 2012. https://pubmed.ncbi.nlm.nih.gov/22686838/ [a28]
- [M] Retrieval-context replication 2019. https://pubmed.ncbi.nlm.nih.gov/30084743/ [a30]

LLM and agents
- [V] Jiang et al. 2024 PIT. https://arxiv.org/abs/2402.12847 [c01, c02]
- [V] Allen-Zhu and Li 2023. https://arxiv.org/abs/2309.14316 [c03, c04]
- [V] Lin et al. 2025 Active Reading. https://arxiv.org/abs/2508.09494 [c05, c06]
- [V] Lin et al. 2025 Sleep-time compute. https://arxiv.org/abs/2504.13171 [c07, c25]
- [V] Zweiger et al. 2025 SEAL. https://arxiv.org/abs/2506.10943 [c08, c09]
- [V] Gutierrez et al. 2024 HippoRAG. https://arxiv.org/abs/2405.14831 [c10-c12]
- [V] Zhong et al. 2023 MemoryBank. https://arxiv.org/abs/2305.10250 [c13]
- [V] Park et al. 2023 Generative Agents. https://arxiv.org/abs/2304.03442 [c14, c24]
- [V] Shinn et al. 2023 Reflexion. https://arxiv.org/abs/2303.11366 [c15, c23]
- [V] Wang et al. 2023 Voyager. https://arxiv.org/abs/2305.16291 [c16]
- [V] Xu et al. 2025 A-MEM. https://arxiv.org/abs/2502.12110 [c17, c22]
- [V] Chhikara et al. 2025 Mem0. https://arxiv.org/abs/2504.19413 [c18]
- [V] Das et al. 2024 Larimar (framing only). https://arxiv.org/abs/2403.11901 [c19]
- [M] Packer et al. 2023 MemGPT (keyword scan). https://arxiv.org/abs/2310.08560 [c20]
- [V] An et al. 2025 LLM retrieval quizzes. https://arxiv.org/abs/2507.05629 [b19]
- [V] Panthi et al. 2026 memory flattening. https://arxiv.org/abs/2609.36457 [b20]
- [V] Kwon 2026 manufactured confidence. https://arxiv.org/abs/2606.29279 [b21]
- [V] Xie 2026 SleepGate. https://arxiv.org/abs/2603.14517 [b22]
- [V] Kyrkewood 2026 gist compression. https://arxiv.org/abs/2608.11775 [b23]
- [V] 2026 compressive retrieval-augmented consolidation model (Mistral 7B). https://doi.org/10.1038/s41467-026-74357-6 [d08]
- [M] 2026 complementary learning system for continual episodic memory in LLMs. https://doi.org/10.64898/2026.08.24.746712 [d09]
- [M] SmartPhone keyword mnemonic 2023 (listing only). https://arxiv.org/abs/2305.10436 [d18]
- Search logs, no source: [b24, c21, d11-d17, d19]. The Chinese Advances in Psychological Science 2024 article was not found [d15].
