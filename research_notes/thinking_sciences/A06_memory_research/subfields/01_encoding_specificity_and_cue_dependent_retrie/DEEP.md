# Encoding specificity and cue-dependent retrieval: deep document

*Subfield A06.01. Built from evidence_a-d.jsonl (a01-a28, b01-b30, c01-c27, d01-d16), claims.jsonl (K01-K27) and critique.md in this folder. Evidence ids in brackets. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The encoding specificity principle (Tulving and Thomson, 1973) says a cue helps recall only if information about the cue was stored with the target at study. What is retrieved depends on the match between the trace and the retrieval cue, not on the cue's strength in the abstract.

The famous demonstration: a weak cue that was shown with the target at study beats a strong associate that was not shown. Example: study "train" with "black". At test, "black" cues "train" better than "engine" does, even though "engine" is the stronger link in everyday language [a03, b14].

Three related ideas sit under the same name:
1. **Cue match.** Retrieval is better when test conditions match study conditions (cues, context, processing).
2. **Environmental and state context.** Room, body state or scene is a cue like any other. This is the "diver" tradition.
3. **Cue diagnostic value (rival view).** A cue works because it points to few traces, not because it matches. Nairne (2002) and Goh and Lu (2012) [b17, b18, b22].

Why it matters for our agent: our memory holds one-line lessons by problem class (SCHEMA section 5). A lesson only helps if the key it is filed under shows up when the problem arrives. The agent writes notes now and reads them later with different words. This document is about that gap.

Scope: parallel subfields cover cue overload and interference, consolidation, model-based control, and self-consistency. This document touches them only where they change the cue story.

## 2. History and theories in depth

**1968: Tulving and Osler.** Weak cue words shown at study helped recall when reinstated at test and did nothing when absent. Not opened by us; known from the 1970 paper [a07, a01]. J Exp Psychol 77:593-601.

**1970: Thomson and Tulving.** Thomson says he ran the study to refute Tulving's claim that strong associates do not help unless encoded. The data supported Tulving instead [a06, d14]. Design: 24-word lists studied alone (O), with a weak cue (W) or with a strong cue (S); tested with no cue, weak cue or strong cue. Normative cue-target strength: 42% for strong, 1% for weak [a01]. The key cell, weak at study and strong (unseen) at test, gave a small gain (13.9 vs 10.7) but far below matched strong (20.2). Experiments II and III forced specific encoding and showed mismatch costs [a04, a05].

**1973: Tulving and Thomson.** The Psychological Review statement of the principle, plus the finding of "recognition failure of recallable words": a word can be recalled from a cue yet not recognised when shown alone. Not opened by us [a08, K16].

**1975: Godden and Baddeley.** Divers learned word lists on land or underwater and recalled 4 minutes later in the same or other place. Same place was better. The original interaction was F=22.0, which implies d of at least 2.7 for 16 divers. Not opened; described via Murre [b07, a11, d07].

**1975: Tulving and Wiseman.** The Tulving-Wiseman function relates recognition to recognition failure. Later challenged. Not opened [a09, b23].

**1977: Morris, Bransford and Franks.** Transfer-appropriate processing: match of processes, not only cues. Semantic encoding beat rhyme encoding on a standard test; the pattern reversed on a rhyme test. Not opened [a23].

**1981-2002: formal models.** SAM treats recall as sampling memory images by match to cues plus context [a21, not read]. MINERVA 2 stores one trace per experience; a cue activates all traces by similarity and the output is their summed content [a20]. The temporal context model has context drift and reinstatement as an asymmetric cue [a22].

**1985: field nulls.** Fernandez and Glenberg: eight experiments with room changes, mostly null [b11, via meta-analysis]. Saufley, Otaka and Bavaresco: 21 classroom comparisons across 7 courses, none reliable [a19, b10].

**2001: Smith and Vela meta-analysis.** 93 effect sizes, d=.28. Small and bound by conditions [a12, b01].

**2002: Nairne, "The myth of the encoding-retrieval match."** Cue diagnostic value, not raw match [b22]. **2002: Higham** shows part of the strong-cue failure is a report-criterion effect [a14, b15].

**2010-2014: video contexts.** Smith and Manzano: very large effects when each scene cues few words [a17, b12]. Smith and Handy: varied contexts plus retrieval practice make memory context-free [d06].

**2012: Poirier et al.** Memory as discrimination: shared cues slow retrieval; adding a second unique cue changes nothing [a15].

**2021: Murre** fails to replicate the diver study [a10, b08]. Shin et al.: VR worlds give a small effect [b19].

**2023-2026: neural networks.** Reversal curse (parametric cue direction) [c12-c14, d08]; Dinh et al. map attention keys to Tulving's cues [c01, c02]; agent memory papers invoke the principle (Stern and Nadel, Zhang et al., Guo et al.) [c03, c21, c06].

**Adversarial note.** The test that founded the field was designed to disconfirm it. That favours the core weak-cue result. It is also a reason to distrust big naturalistic claims such as the diver study.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Weak cue shown at study helps; weak cue not shown at study does nothing or hurts | W-W 15.7 vs 10.7 uncued; O-W 11.1 vs 14.1; S-W 9.2 vs 12.2 (mean words, Exp I) | Thomson and Tulving 1970 [a03, b14] | [E] |
| Strong cue helps when study was compatible | S-S 20.2 vs 12.2; O-S 19.0 vs 14.1 | [a02] | [E] |
| Weak-to-strong switch gives a small gain only | W-S 13.9 vs W-O 10.7, far below S-S 20.2 | [a04] | [E] |
| Mixed-list mismatch (N=24) | weak-in weak-test .73; weak-in strong-test .33 (8 of 24); strong-in weak-test about .03 | [a05] | [E] |
| Forced training on matched weak cues | trained-weak groups 18.3 on lists 1-2; unexpected uncued test 7.1; strong-cue switch no gain. Untrained groups 11.0; strong-cue test 16.8/16.3 | [a04] | [E] (Exp II stats not extracted) |
| Strong-cue failure is partly report criterion | free report: weak .24/.29 vs none .08; strong not above none (F<1). Forced: strong .25/.27, weak .26/.31, none .08. Confidence weak 3.41, strong 1.84. N about 48 | Higham 2002 [a14, b15] | [E] |
| Warning that cues are associates removes strong-cue failure | 5.33 words (no warning) vs 5.40 (no cue) vs 10.07 (warned) | Santa and Lamwers 1974 via [b16] | [S] secondhand |
| Room context effect is small | d=.28 (CI +-.05, 93 effects, QT=242.47); reinstatement d=.23 (n=66); interference reduction d=.68 (n=10); multiple contexts d=.45 (n=7); QB=18.60 | Smith and Vela 2001 [a12, b01, b02] | [E] |
| Test type does not change it | free recall .29 (n=52), recognition .27 (n=28), cued .25 (n=3), QB=.21 ns | [b04] | [E] |
| Associative processing at study shrinks it | d=.13 (n=29) vs non-associative .33 (n=12) vs unsure .38 (n=42); chi2=6.67 | [b03] | [E] |
| Retention interval | <5 min .27; 5 min-1 h .22; 1 h-1 day .28; 1 day-1 week .63 (n=6, CI +-.21) | [a12] | [E] weak at long end |
| New experimenter at test | d=.62 (n=18) vs same experimenter .26 | [b05] | [S] |
| Diver study | original F=22.0, eta2 .647, d>=2.71, N=16, 4 days. Replication N=16: interaction F=1.999 p=.163; learning env F=16.2; recall env F=.601 p=.440; underwater-learned better on land p<.01 | Murre 2021 [a10, a11, b08, d07] | [C] |
| Classroom | 21 comparisons, 7 courses, none reliable; 253 and 250 students; 58.5 (n=125) vs 59.1 (n=97) | Saufley et al. 1985 [b10] | [E] null |
| Video context, cue overload | d=3.02 (1 word/scene), 2.18 (3), 1.00 (15); reinstatement F(1,318)=648.19, eta2=.67; interaction with load F=60.77, eta2=.28 | Smith and Manzano 2010 [a17, b12] | [E] |
| VR worlds | same .32 vs different .26 (N=64); beta=.349, p<.01; immediate test no effect | Shin et al. 2021 [b19, b20] | [S] |
| Diagnostic value beats match | Exp 1 (N=40): low overload .37 vs .24 (F=17.14); high overload .28 vs .28; interaction F=13.89. Exp 2 (N=42): .31 vs .20; .24 vs .23; F=5.23. Exp 3 (N=40): overload .31 vs .14 (F=90.24); weak studied .32 > strong new .25 > weak new .09 | Goh and Lu 2012 [b17, b18] | [E] |
| Shared cues slow retrieval | one unique+one shared slower than one unique, t(24)=2.77 p<.02; accuracy >90% everywhere | Poirier et al. 2012 [a15] | [S] |
| Retrieval practice in varied contexts frees memory | Exp 1 (N=45): constant .43 vs varied .61, d=.71; forgetting .50 vs .02. Exp 4 restudy (N=36): .51 vs .36 ns | Smith and Handy 2014 [d06] | [S] |
| Input task matters | recognition context effect only after short-term-memory input; about 50% more errors in different context (Exp 1) | Smith 1986 [d15] | [S] |
| Fan effect: humans vs retrievers | humans (N=112) 91.2/82.4/71.8% at fan 1/2/4, slope .41; DPR 94.1/76.3/58.2/44.7% at 1/2/4/8, slope .67; ColBERTv2 .53; HippoRAG .44 | Guo, Wu, Yiu 2026 [c06] | [S] |
| Scene trace in agent memory | 73.7% vs 53.5% (+20.2 pp, CI 12.1 to 29.3, n=99 pairs); McNemar 22 vs 2; single-session 75 vs 75; temporal 65 vs 25; update 80 vs 55; multi-session 50 vs 20 | Stern and Nadel 2026 [a24, c03, c04] | [S] |

## 4. Mechanisms and models

An engineer can treat each account as a different rule for scoring stored traces against a cue.

**4.1 Match model (Tulving, MINERVA 2).**
- Store: one trace per episode, a feature vector (item features plus context features present at study).
- Retrieve: build a probe vector from the cue. For each trace compute a similarity S. MINERVA 2 raises it to a power (activation A = S^3) so close matches dominate. Output = sum of traces weighted by A [a20].
- Prediction: a probe that shares more features with the trace gives higher activation. A cue not stored with the item shares no features and adds nothing.
- Analogue: embedding or keyword index over the note. The cue string at read time must overlap the text or tags written at write time.

**4.2 Diagnostic-value / discrimination model (Nairne; Goh and Lu; Poirier).**
- Score of a trace is the cue's match to it relative to its match to all other traces: P(target) = s(cue, target) / sum over j of s(cue, trace_j).
- A matching cue that also fits many other traces raises the denominator as fast as the numerator. No gain. A unique cue helps.
- Confirmed: match helped only at low overload (.37 vs .24) and not at high (.28 vs .28) [b17].
- Analogue: score keys by inverse frequency. "ARC" is a poor key; "symmetry about the vertical axis" is a good one. Count how many notes each key hits (fan) and downweight high-fan keys.

**4.3 SAM (search of associative memory).** Sample an image with probability proportional to the product of its strengths to all cues in the probe set, then try to recover it. Context is one more cue. Because strengths multiply, each added cue must be diagnostic [a21, secondhand].

**4.4 Temporal context model.** A context vector drifts with each item. Retrieving an item restores the context it was stored in, which then cues its neighbours, forward-biased [a22]. Analogue: store order and session id as keys. Stern and Nadel's gains were on temporal, update and multi-session questions [c04].

**4.5 Report criterion (Higham).** Retrieval has three stages: generate a candidate, monitor (confidence), report if confidence passes a threshold. Strong cues for unencoded items gave candidates with low confidence that did not pass a conservative criterion. Forced report removes the filter [a14, b15].
- Analogue: separate "retrieve" from "accept". Score retrieved notes for fit, then decide how many to show. Do not hide useful low-confidence items, and do not show distractors (section 6).

**4.6 Transformer attention as cue-based retrieval.** Query = retrieval context; key = trace index; value = content (Dinh et al.).
- Swapping V alone makes the model answer with the counterfactual (50% Olmo 2 to 90% Qwen 2.5). Swapping K alone leaves factual accuracy at about 30-40% without making it say the counterfactual. Swapping K and V gives 100% hallucination [c01, a26].
- Zeroing keyword keys cuts verbatim recall more than zeroing random tokens (except Llama 2) [c02].
- Reading: a missed lesson (wrong key) fails silently; a misleading lesson (wrong value) fails confidently. They need different checks. This is an analogy from one preprint on open models [K13, S].
- Induction heads behave like the CMR model: temporal contiguity, forward asymmetry [c10].
- Key-value theory: forgetting is often retrieval failure. Amplifying stored keys restored a forgotten task in a toy network (99% to 9% accuracy, then restored) [c11].

**4.7 Write-time versus read-time cue transformation.**
- Write-time: doc2query adds predicted questions to each document (Recall@1000 85.3 to 89.3) [b26]; A-MEM adds keywords, tags and context [c20]; contextual retrieval prepends about 100 tokens of document context (top-20 failure 5.7% to 3.7% / 2.9% / 1.9%) [d12]; LongMemEval key = value + fact [c08].
- Read-time: HyDE writes a hypothetical answer and searches with it (nDCG@10 61.3 vs BM25 50.6 and Contriever 44.5 on DL19) [b27, c18]; time-aware query expansion [c09].
- Both try to bring cue and trace into the same form. Neither has an extra-token control in agent memory.

**4.8 Parametric cue direction.** Facts learned as "A is B" are retrieved from A but not B (GPT-3: DescriptionToName 96.7% same vs 0.1% reverse; NameToDescription 50.0 vs 0.0). The same fact in context is reversible (3-shot GPT-3 96.67-100%) [c12, d08]. Varied wording and order in pretraining raised extraction from 9.7% to 96.6% on synthetic biographies [c14]. The lock is in weights, not in text we place in the prompt.

## 5. What holds up

**Holds up well**
- The core weak-cue pattern: replicated within Thomson and Tulving's own three experiments, by Goh and Lu Exp 3 (.32 vs .25 vs .09) and, in free report, by Higham (.24/.29 vs .08) [a03, b18, b15]. Three independent sources [K01, E].
- Context effects are real but small on average (d=.28), heterogeneous, and bound by conditions [K03, E].
- Cue overload is a strong moderator, from video contexts (d=3.02 to 1.00) and from diagnostic-value tests [K06, K07, E].

**Failed or weakened**
- The diver study did not replicate in the one close replication (F=1.999, p=.163, N=16). Caveats: 1.5 h instead of 4 days (possible proactive interference), filmed for TV, preregistration filed after data analysis (in-principle acceptance only) [a10, d07, K04, S]. The original d of at least 2.7 is implausible next to the typical d of about .25 [b09].
- Field studies: Saufley 21 null comparisons; Fernandez and Glenberg mostly null [b10, b11, K05].
- "Strong cues are useless without encoding" is an overstatement. With forced report strong cues beat no cue (.25-.27 vs .08) [b15]. The effect is partly a report criterion.
- Strict match as cause: at high overload, extra match gave nothing (.28 vs .28) [b17]. Nairne's reading is better supported here [K07].

**Competing explanations**
- Match (Tulving) versus diagnostic value (Nairne). Both predict the weak-studied-cue win. They differ under overload [critique].
- Associative processing at study removes the room effect (d=.13), yet video work shows huge effects when each scene holds one target. Cue overload is the common variable [critique].
- Test type: Wikipedia says recall effects exceed recognition; the meta-analysis says .29 vs .27. Trust the meta-analysis [a28, b04].

**Moderators (human)**
- Overshadowing: strong item-to-item association at study leaves little role for context. Outshining: a good explicit cue at test makes context redundant. Mental reinstatement reduces the physical-context effect [a13, b05].
- Delay: 1 day to 1 week d=.63 (n=6, wide). VR effect absent at immediate test [a12, b19].
- Input processing: recognition context effects only after short-term-maintenance input [d15].
- Relevance: VR items judged relevant to the world gained more [b20].

**Interventions that worked (human)**
- Reinstate the cue. Mental reinstatement helps when the physical context changed (d=.27, .88) [b05].
- Varied contexts with retrieval practice: .61 vs .43 at 2 days (d=.71, N=45) [d06].
- Warn that cues are associates (5.33 to 10.07 words) [b16, secondhand].
- Forced report (strong cue .25/.27 vs none .08) [b15].

**Did not work**
- Varied contexts with restudy: .36 vs .51, ns (N=36) [d06].
- Classroom contexts [b10].
- Time spent in the study context did not predict the effect [b06].

**Agent-memory side (engineering results, not psychology)**
- Retrieval method moves accuracy 14-23 points; write strategy 3-8 (LoCoMo, GPT-5-mini, 1,540 questions) [d05, K23, S].
- Raw chunks beat LLM rewrites: 77.9/59.2/81.1 (cosine/BM25/hybrid) vs 72.2/49.4/77.3 for extracted facts vs 70.1/62.7/73.3 for summaries [d05].
- Expansion helps weak retrievers and hurts strong ones across 11 methods, 12 datasets, 24 models. All 28 hand-checked non-label failures were added irrelevant terms [d01, K22, E].
- Write-time enrichment is contested [K10, C]: gains in LongMemEval (+9.4% recall, +5.4% QA) and A-MEM (temporal F1 45.85 vs 25.52) against Weller and Yuan [c08, c20, d01, d05].
- Index-time prefix: failure 5.7% to 1.9% with embeddings, BM25 and reranking. Vendor report, no random-prefix control [d12].

## 6. Language models

**Direct Tulving tests on LLMs (weak)**
- Chauvet, Mistral-7B-instruct, 48-word list, 32 cues per run: immediate recognition 100% with copy cues and no false positives; delayed recall from the copy word: 0 words. Answers drift to pretrained associations [c15].
- Trace-valence replication: both targets recalled after associative encoding, LLM .53 vs human .32/.36. Associative cues beat rhyme cues far more than in humans. The "failed cue leaves trace unchanged" assumption is violated (discrepancy .08/.17 vs .06 human) [c16]. One author, one 7B model [K14, S].
- Huet et al. built a benchmark on encoding specificity with cues of time, space, entity and event. F1 falls for every model (GPT-4o, 4o-mini, Claude 3 Haiku, Claude 3.5 Sonnet, Llama 3.1 405B, o1-mini) once 2 or more events match a cue [c17].

**Parametric cue direction**
- GPT-3-175B: NameToDescription 50.0 same vs 0.0 reverse; DescriptionToName 96.7 vs 0.1. GPT-4 on real celebrities: 79% vs 33% [c12, c13]. In context: 100% with 3 shots [d08]. Long-context retrieved text: untested [K12].
- Varied wording and order of facts in pretraining: 9.7% to 96.6% QA [c14]. Prompt wording changes LAMA recall; mined and pooled prompts 31.1% to 39.6% (abstract only) [c24].

**Agent memory: adding a trace**
- Stern and Nadel (Claude Sonnet agent, GPT-4o judge, LongMemEval-S, 99 pairs): 73.7 vs 53.5 (+20.2 pp). Temporal +40, update +25, multi-session +30; single-session 75 vs 75. Session coverage 54.8% vs 57.4%. Tokens per query 3.3% lower. Earlier steps (coverage, format) moved only 40.4 to 53.5 [a24, a25, c05]. One run, no scene-at-retrieval ablation, conditions built in sequence [K09, S].

**Agent memory: widening cues**
- LongMemEval-M Recall@5: .582 (K=V), .530 (K=fact), .282 (keyphrase), .644 (V+fact). QA top-10 .670 vs .720 (GPT-4o). Fact-only or keyphrase-only keys were worse than raw text. Time-aware expansion +11.3% recall with GPT-4o expansion; with Llama 3.1 8B expansion no gain (.711 vs .721 baseline) [c08, c09].
- A-MEM: temporal F1 45.85 vs MemGPT 25.52 vs 18.41 baseline; 643 vs 16,910 prompt tokens. The ablation does not remove keywords alone [c20].
- MMS: removing two modules drops R@1/3/5 from 29.35/40.23/46.61 to 22.49/32.94/38.99; an added semantic-summary segment lowered recall [c21].
- HippoRAG R@5 72.9 vs ColBERTv2 65.6 vs BM25 58.4; better on multi-hop, worse on HotpotQA (77.7 vs 79.3) [b28].
- Generative agents: believability mu=29.89 full vs 21.21 without memory, planning and reflection. Relevance, recency and importance were never ablated separately [c19, K19].

**Fan / cue overload**
- Dense retrieval loses accuracy faster than humans: 94.1 to 44.7% over fan 1 to 8, slope .67 vs human .41; HippoRAG .44. Humans recency-biased (ratio 1.43), DPR primacy-biased (0.52) [c06, c07]. Old retrievers; human sample at fan 1/2/4 only.

**Mismatched retrieval costs**
- Llama2-7b: gold only .5642; with 1/2/4 hard distractors .4068/.3815/.3626. Random unrelated passages next to the query raised accuracy up to +36% [d02, K20].
- Hard distractors cost 6-11 points, up to 70B [d03]. Hard distractors hurt more at prompt edges (36-44%) than in the middle (28-34%) [d04].
- Llama-2-13B: 73% of retrieval-caused errors copied an entity from the mismatched passage (77% with low-ranked context, 37% with random) [d09].
- Claude 3.5 Sonnet and Gemini 1.5 Pro: when all passages are wrong, plain RAG is more than 50 points below no-RAG; about 70% of retrieved passages lacked the answer [d11].
- Fixes tested: NLI filter (prevents the loss, discards useful passages) [d09]; Chain-of-Note +7.9 EM at 100% noise, +2.7 at 0% (fine-tuned 7B) [d10]; source-aware consolidation near no-RAG level [d11]. All cost some useful items [K26].

**Query rewriting**
- HyDE nDCG@10 61.3 vs 44.5 and 50.6. But gains concentrate where the generated text already holds entailed evidence: FEVER Recall@5 40.0 matched vs 23.4 unmatched vs 26.8 baseline (GPT-4o-mini) [b27, d13]. On private notes the model has not seen, the bet may fail [K25, S].

**Position**
- Mid-context answers: GPT-3.5 drops over 20% [c22] (2023 models). Reordering retrieved items by model preference equals random shuffle in real retrieval (Qwen 7B 71.73 vs 71.00) [d04, K27].

**Other**
- MemoryAgentBench: no method above 28% on multi-hop selective forgetting [c23].
- Long-context models show a human-like distance effect in order memory, using a time code in one attention head (abstract only) [b29].
- Human-inspired agent memory matched raw retrieval at 200K tokens: 70.1% vs 71.2% (abstract only) [b30].

**What changed it, by how much**
- Adding a scene trace at write time: +20 pp, but only on questions that need ordering or separation.
- Keeping raw text plus extra keys: +5 to +9% recall.
- Replacing text with LLM rewrites: -4 to -10 points.
- Removing mismatched passages: avoids 6-11 points (open models) and up to 50 points (all-wrong retrieval, frontier models).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory = SCHEMA section 5.

### Add now (established)

1. **Key lessons by what will be present at retrieval, not by what the author finds salient.** Part: memory. [E] K01, K07; a03, b14, b17, b18. A cue only helps if it was stored with the item. Key at least by problem class and by the surface form of the task as seen at S0/S1.
2. **Prefer unique keys over merely matching keys.** Part: memory. [E] K07; b17, b18, a15. Count how many lessons each key hits. Drop or downweight high-fan keys. Match without diagnostic value gave .28 vs .28 at high overload.
3. **Keep each key mapped to few lessons.** Part: memory. [E] K06; a17, b12, c17. Effects fell from d=3.02 to 1.00 as items per cue rose from 1 to 15. Cap fan per key.
4. **Keep the original wording of a lesson or problem as a key beside any rewrite.** Part: memory, S1. [E for the direction] K10, K22, K23; c08, d05, d01. Key = value + fact beat value-only (.644 vs .582). Fact-only and keyphrase-only keys lost (.530, .282). Fits SCHEMA S1 "keep the original wording beside it".
5. **Treat a retrieved lesson as possibly misleading; run a one-line fit check before use.** Part: O/memory. [E] K20, K26; d02, d03, d09, d10, d11. Hard distractors cost 6-11 points; 73% of retrieval-caused errors copied from the wrong passage. The check must cost less than it saves, and some useful lessons will be lost.
6. **Do not spend tokens on global context match or on re-ordering lessons.** Part: memory. [E] K03, K15, K27; a12, d04. Room-style match d=.28. Ordering by model preference equals random shuffle. Put the effort into filtering mismatches.
7. **Do not rely on the model to retrieve a fact by a different cue than the one it was written with; put the needed fact in context in the query direction.** Part: memory. [E] K12; c12, c14, d08. The lock is parametric; in-context reversal works.
8. **Show lessons after the first attempt (already in schema); a new reason: a lesson is a cue for the whole problem, and a wrong match primes a wrong entity.** Part: memory. [E] K20 for the harm.
9. **Test context match per item, not globally.** Part: memory. [E] K05. When the query already names the item, tags add nothing (outshining).

### Test first (single-source, contested, or no agent test yet)

1. **Write-time enrichment (keywords, likely questions) beyond the raw text.** Part: memory. [C] K10, K22; c08, c20, d01, d05, d12. Needs the extra-token control.
2. **Scene or context trace written with each lesson or fact.** Part: memory. [S] K09; a24. +20.2 pp in one run; needs a scene-at-retrieval ablation and another model.
3. **Query rewriting into the stored form (HyDE-style) versus storing 2-3 forms per note.** Part: O/memory. [S] K25 (K11 partly E); b27, d13. Works when the model already knows the text; unknown on private notes.
4. **Forced answer-then-score and the "cues are associates" warning for mismatched lessons.** Part: G/O. [S] K02, K26; b15, b16. No LLM test.
5. **Source-aware consolidation before using retrieved lessons.** Part: O/memory. [S] K21; d11. Claude and Gemini only; multi-call cost.
6. **Varied-use retrieval practice makes a lesson cue-independent.** Part: memory. [S] K17; d06. Human only, 2 days, N=45.
7. **Entity or graph index versus dense retrieval at high fan.** Part: memory. [S] K08; c06, b28. One preprint.
8. **Ablate relevance, recency and importance in retrieval scoring.** Part: memory. [S] K19; c19.
9. **Time-aware query expansion for temporal lessons.** Part: memory. [S] K11 part; c09. Needs a strong rewriter.

## 8. Concrete tests on our bench

All arms get equal total tokens (lesson text plus prompt plus attempts). Setup cost counts (G7). Items come from benchmarks the harness already runs (ARC, BRAINTEASER), with lessons written from earlier runs (S9).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Problems with a stored lesson from a sibling problem; query wording differs from lesson wording | (a) lesson with raw-wording key only; (b) raw + 3 LLM-written keywords/likely questions; (c) raw + 3 random same-length tokens; (d) raw + 3 wrong-lesson keywords | retrieval hit rate at k=1,3; final pass rate | b > a by 3-6 points on hit rate if form match matters; c about a; d < a. If b = c, the gain is tokens only |
| T2 | Problems needing ordering or separation of similar lessons (multi-attempt, updated rules) | fact-only lesson; lesson + scene (class, when, what failed); scene at write only; scene at write and in query | pass rate; McNemar on pairs | scene > fact-only on ordering/update items (+20 pp seen once; expect +5 to +10); no gain on single-lesson lookup |
| T3 | Fan sweep | 1, 2, 4, 8 lessons sharing one class key; dense vs entity/class index | top-1 accuracy of the right lesson | accuracy falls with fan; specific keys flatten the slope (human slope .41, dense .67) |
| T4 | Mismatch cost | right lesson alone; right + 2 hard distractors (similar surface, wrong rule); right + 2 random lessons; all-wrong lessons | pass rate; copied-wrong-rule rate | hard distractors -6 to -11 points; random about 0 or positive; all-wrong worst |
| T5 | Fit check | no check; one-line "does this lesson's condition hold here"; separate checker | pass rate, useful lessons kept, tokens | check recovers most of the hard-distractor loss and drops some useful lessons; accept if net pass rate rises at equal tokens |
| T6 | Query rewrite | raw query; HyDE-style rewrite into lesson format; store 2-3 forms per lesson; strong vs weak rewriter | hit rate, tokens | rewrite helps only with a strong rewriter; multi-form storage may cost fewer tokens per query |
| T7 | Free vs forced use | model decides whether to use a mismatched lesson; forced attempt with and without, scored by check; warning line "retrieved lessons are only associates" | pass rate, calibration | forced beats free on mismatched lessons if the check is reliable |
| T8 | Raw vs rewritten | lesson stored raw vs LLM-condensed | hit rate | raw >= condensed (LoCoMo 77.9 vs 72.2 and 70.1) |
| T9 | Placement | matched lesson at start, middle, end; mismatched lesson at the edge | pass rate | edge-placed distractors hurt most; placement matters less than match |
| T10 | Varied use | lesson retrieved and applied under 3 differently worded problems vs same wording 3 times vs re-read only | hit rate under a fresh wording | varied retrieval beats constant; re-read gives nothing (human d=.71) |
| T11 | Retrieval-term ablation | relevance only; recency only; relevance + recency; all three | hit rate under distractors | relevance carries most; recency helps temporal items |

## 9. What does not transfer, and why

- **Room and body-state context (diver, VR).** An agent has no room. The only analogue is session or prompt context. Global match gave d=.28 in humans and the strongest study failed to replicate [K03, K04].
- **Report criterion.** Humans withhold low-confidence answers. LLMs state answers with high confidence (SCHEMA 4b: verbal confidence is unreliable). Forced report may be less needed. The opposite risk, using a bad lesson with confidence, is bigger [b15, d09].
- **Recognition failure of recallable words.** Needs a recognition test separate from recall. An agent reads the whole note [K16].
- **Decay and interference over days.** A text store does not decay. Only retrieval failure is shared.
- **Chauvet's results.** One 7B model with the word list in the chat. "Delayed recall from the copy word was 0" says more about that model than about memory [c15].
- **Word-list effect sizes.** Lab lists at 3 s per item, undergraduates. Long agent notes differ [critique].
- **Attention-swap findings.** Memorised book text, open models, short counterfactual completions. Not a design guide [K13].
- **HyDE gains on public corpora.** They rely on the model already knowing the corpus [d13].
- **Position effects from 2023 models.** Newer models may differ [c22].

## 10. Open questions

1. Does a scene written with the note, but absent at retrieval, still help at equal tokens (the missing ablation of Stern and Nadel)? Closest: index-time prefixes (5.7% to 1.9% failure), no random-prefix control [d12].
2. Is the benefit of write-time enrichment form match or just extra tokens? No study separates matched from same-length random keys at write time. Weller: expansion hurts strong retrievers [d01].
3. Cost of a mismatched strong cue for a frontier model in a Thomson-Tulving design. Closest: 6-11 points (up to 70B) and over 50 points in the all-wrong case (Claude 3.5 Sonnet) [d03, d11].
4. Fan limit before accuracy falls, entity/graph vs dense, at equal context (one preprint) [c06].
5. Forced answer-then-score and the associates warning for LLM agents [K26].
6. Query rewriting versus multi-form storage on private notes [K25].
7. Does varied use make notes cue-independent for an agent? Human: yes with retrieval practice only [d06].
8. Exact founding numbers: Tulving and Osler 1968, Tulving and Thomson 1973, Godden and Baddeley 1975 are unopened.
9. Does the reversal curse appear for retrieved text in long contexts and for 2025-26 models? [K12]
10. Matched lesson in the middle versus mismatched at the edge: not run [d04].
11. Is the diver effect real at all? One failed close replication, no second [K04].
12. Do models show Higham-type report effects? Nobody has asked.

## 11. Sources

[V] = opened (full text read in this series); [M] = snippet, abstract or secondhand only.

**Human memory**
- [V] Thomson and Tulving (1970), Associative encoding and retrieval: weak and strong cues. https://doi.org/10.1037/h0028569 ; copy https://support.pstnet.com/hc/en-us/article_attachments/360082711074 [a01-a05, b14]
- [V] Thomson (1984), Citation Classic commentary. https://garfield.library.upenn.edu/classics1984/A1984TB51800001.pdf [a06, d14]
- [M] Tulving and Osler (1968), Effectiveness of retrieval cues in memory for words. https://deepdyve.com/lp/american-psychological-association/effectivene [a07]
- [M] Tulving and Thomson (1973), Psychological Review 80:352-373. https://link.springer.com/article/10.3758/BF03198232 (listing page only) [a08]
- [M] Tulving and Wiseman (1975). https://doi.org/10.3758/bf03333153 [b23]
- [V] Wikipedia, Recognition failure of recallable words. https://en.wikipedia.org/wiki/Recognition_failure_of_recallable_words [a09]
- [M] Godden and Baddeley (1975). https://doi.org/10.1111/j.2044-8295.1975.tb01468.x [b07]
- [V] Murre (2021), Godden and Baddeley replication. https://pmc.ncbi.nlm.nih.gov/articles/PMC8568063/ ; https://doi.org/10.1098/rsos.200724 [a10, a11, b08, b09, d07]
- [V] Smith and Vela (2001), meta-analysis. https://doi.org/10.3758/BF03196157 ; https://link.springer.com/content/pdf/10.3758/BF03196157.pdf [a12, a13, b01-b06]
- [V] Higham (2002). https://link.springer.com/content/pdf/10.3758/BF03195266.pdf [a14, b15]
- [V via Higham] Santa and Lamwers (1974) [b16]
- [V] Poirier et al. (2012), Memory as discrimination. https://openaccess.city.ac.uk/id/eprint/2519/1/poirier_et_al_Memory_as [a15]
- [V] Goh and Lu (2012). https://link.springer.com/content/pdf/10.3758/s13421-011-0133-9.pdf [b17, b18]
- [M] Nairne (2002). https://doi.org/10.1080/09658210143000353 [b22]
- [V] Smith, Handy, Angello and Manzano (2014). http://dx.doi.org/10.1080/09658211.2013.800553 [a16]
- [V] Smith and Manzano (2010). https://link.springer.com/content/pdf/10.3758/BRM.42.1.292.pdf [a17, b12, b13]
- [V] Smith and Handy (2014). http://dx.doi.org/10.1037/xlm0000019 [a18, d06]
- [V] Saufley, Otaka and Bavaresco (1985). https://link.springer.com/content/pdf/10.3758/BF03198323.pdf [a19, b10]
- [M] Fernandez and Glenberg (1985). https://doi.org/10.3758/bf03202501 [b11]
- [V] Smith (1986). https://link.springer.com/content/pdf/10.3758/BF03202513.pdf [d15]
- [V] Shin et al. (2021), VR. https://doi.org/10.3758/s13423-020-01835-3 [b19, b20]
- [M] Eich et al. (1980-95). https://doi.org/10.1037/0096-3445.109.4.408 [b21]
- [M] Morris, Bransford and Franks (1977). https://www.redalyc.org/pdf/2070/207021439002.pdf [a23]
- [V] Wikipedia, Context-dependent memory. https://en.wikipedia.org/wiki/Context-dependent_memory [a28]

**Models of memory**
- [V] Hintzman (1986), MINERVA 2. https://miashs-www.u-ga.fr/prevert/MasterIC2A/SpecialiteSC/FichiersPDF [a20]
- [M] Raaijmakers and Shiffrin (1981), SAM. https://raaijmakers.edu.fmg.uva.nl/PDFs/Raaijmakers%20and%20Shiffrin%2 [a21]
- [V] Howard and Kahana (2002). https://people.bu.edu/marc777/docs/HowardKahana02-JMP.pdf [a22]
- [V] Gershman, Fiete, Irie (2025). https://arxiv.org/abs/2501.02950 [c11]
- [V] Li Ji-An et al. (2024). https://arxiv.org/abs/2405.14992 [c10]

**Language models and agents**
- [V] Dinh et al. (2026). https://arxiv.org/abs/2601.20282 [a26, a27, b24, b25, c01, c02]
- [V] Stern and Nadel (2026). https://arxiv.org/abs/2604.12948 [a24, a25, c03-c05]
- [V] Guo, Wu, Yiu (2026). https://arxiv.org/abs/2606.28327 [c06, c07]
- [V] Wu et al. (2025), LongMemEval. https://arxiv.org/abs/2410.10813 [c08, c09]
- [V] Berglund et al. (2024), Reversal Curse. https://arxiv.org/abs/2309.12288 [c12, c13, d08]
- [V] Allen-Zhu and Li (2023). https://arxiv.org/abs/2309.14316 [c14]
- [V] Chauvet (2024), Memory GAPS. https://arxiv.org/abs/2402.16505 [c15]
- [V] Chauvet (2024), Memory Traces. https://arxiv.org/abs/2404.08543 [c16]
- [V] Huet et al. (2025). https://arxiv.org/abs/2501.13121 [c17]
- [V] Gao et al. (2023), HyDE. https://arxiv.org/abs/2212.10496 [b27, c18]
- [V] Park et al. (2023), Generative Agents. https://arxiv.org/abs/2304.03442 [c19]
- [V] Xu et al. (2025), A-MEM. https://arxiv.org/abs/2502.12110 [c20]
- [V] Zhang et al. (2026), Multi-Memory Segment. https://arxiv.org/abs/2508.15294 [c21]
- [V] Liu et al. (2024), Lost in the Middle. https://arxiv.org/abs/2307.03172 [c22]
- [V] Hu et al. (2025), MemoryAgentBench. https://arxiv.org/abs/2507.05257 [c23]
- [M] Jiang et al. (2020). https://arxiv.org/abs/1911.12543 [c24]
- [M] Eldan and Russinovich (2023). https://arxiv.org/abs/2310.02238 [c25]
- [M] Ryu and Lewis; Timkey and Linzen; Yoshida et al., cited in Dinh [c26]
- [M] MemoCue / CDMem. https://arxiv.org/abs/2507.23633 [c27]
- [V] Nogueira et al. (2019), doc2query. https://arxiv.org/abs/1904.08375 [b26]
- [V] Gutierrez et al. (2024), HippoRAG. https://arxiv.org/abs/2405.14831 [b28]
- [M] Temporal Context Reinstatement in long-context LMs. https://arxiv.org/abs/2607.22575 [b29]
- [M] Human-Inspired Memory Architecture for LLM Agents. https://arxiv.org/abs/2605.08538 [b30]
- [V] Weller et al. (2024). https://arxiv.org/abs/2309.08541 [d01]
- [V] Cuconasu et al. (2024). https://arxiv.org/abs/2401.14887 [d02]
- [V] Amiraz et al. (2025). https://arxiv.org/abs/2505.06914 [d03]
- [V] Cuconasu et al. (2025). https://arxiv.org/abs/2505.15561 [d04]
- [V] Yuan, Su, Yao (2026). https://arxiv.org/abs/2603.02473 [d05]
- [V] Yoran et al. (2024). https://arxiv.org/abs/2310.01558 [d09]
- [V] Yu et al. (2024), Chain-of-Note. https://arxiv.org/abs/2311.09210 [d10]
- [V] Wang et al. (2025), Astute RAG. https://arxiv.org/abs/2410.07176 [d11]
- [V] Anthropic (2024), Contextual Retrieval (vendor post, read via a summarising fetch tool). https://www.anthropic.com/news/contextual-retrieval [d12]
- [V] Yoon et al. (2025). https://arxiv.org/abs/2504.14175 [d13]
- [M] Hutter et al. and related position-effect snippets. https://arxiv.org/abs/2512.14313 [d16]

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 10 established claims: 9 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A06.01-K20** (number corrected). Cuconasu (0.5642 to 0.4068/0.3815/0.3626, +0.08 / +36% from random docs) and Amiraz (6 to 11 points, persists for Llama-3.3-70B, range is across LLMs not 70B alone) match, but Yoran et al. say retrieval caused the error in 73% of 240 manually annotated failures, and separately that in 77% of NQ errors with low-ranked context the wrong entity appeared in the retrieved text; the claim merges these into '73% of retrieval-caused errors copied an entity ... (77%)'. Corrected claim: Retrieved passages that are semantically close to the question but lack the answer cost an LLM reader more than unrelated ones: Llama2-7b 0.5642 gold-only to 0.4068/0.3815/0.3626 with 1/2/4 ADORE distractors, while random passages placed next to the query raised accuracy by up to 0.08 (+36%); hard distractors cost 6 to 11 accuracy points depending on the LLM, and the cost persists for Llama-3.3-70B; in Llama-2-13B, manual review of 240 failures found retrieval caused the error in 73% (65-85% by setting), and with low-ranked context the wrong answer entity appeared in the retrieved text in 77% of NQ errors (37% with random context).
- **A06.01-K01** (now single-source: only one opened source, code check).
- **A06.01-K06** (now single-source: only one opened source, code check).
