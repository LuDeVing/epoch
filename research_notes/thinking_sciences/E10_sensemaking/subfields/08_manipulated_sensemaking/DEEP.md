# Manipulated sensemaking: deep document

*Subfield E10.08. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K22), critique.md in this folder. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Numbers were cross-checked against paper text or abstracts in the critique pass; none needed changing. Search tools were rate-limited, so "no study found" means a limited search.*

## 1. What it is

Manipulated sensemaking is the idea that disinformation does not only add false facts. It attacks the meaning-making step. It hands an audience a frame, a "deep story", that decides which later events get noticed and how they are read. Prochaska, Vera, Tan and Starbird (CHI 2024 workshop, arXiv 2410.14858) coined the term. Their claim has two parts:

1. Deep stories (broad sets of related frames) set the frames people use on new, ambiguous events. [a01, a03]
2. Sensemaking runs on plausibility, and the bar for plausibility is far lower than the bar for accuracy. [a02]

For our agent the question is the S1 input-hygiene guardrail. If a context carries a source's framing, does the agent read later events through it? Do masking or neutral restatement help?

Limit up front. The founding claim rests on one qualitative paper from one research group (about 1,000 coded tweets, two US election cycles, no outcome measure, no inter-coder statistic seen, no control). No experiment on people tests it and none on LLMs. What exists for LLMs is a set of neighbour effects: uptake of false or coherent content, belief erosion, sycophancy, retrieval poisoning, injection. Those are measured well. The mechanism the founding paper names (a frame carried from earlier context to a later event) has zero direct measurements. [c26, d24]

## 2. History and theories in depth

**Sensemaking and plausibility.** Weick (1995, 1993) described sensemaking as retrospective, social, identity-linked and "driven by plausibility rather than accuracy". Mann Gulch (1949) is his case of sensemaking collapse when expected order fails. [a07, not opened; read via Prochaska]

**Data-frame theory.** Klein, Phillips, Rall and Peluso (2007): elements are explained by fitting them into a frame, and the frame decides which data count. Frame fixation is being stuck on one explanation. Covered in subfield 01. [a08, not opened here]

**Deep story.** Hochschild (2016) coined it for a "feels-as-if" story that carries feeling more than checkable fact. Polletta and Callahan (2019) add three traits: allusiveness (the moral is left unsaid), social storytelling, collective identity building. [a09, not opened]

**Rumour.** Kapferer (1990): a rumour is defined by its unofficial source, not by falsity. It often takes the form of an exemplary story that illustrates a larger suspected truth. [a10, not opened]

**The extension (Prochaska 2024).** The deep story is a structure behind frames. It narrows which frames people try on new data. Their coded tweets: 5 salient rumours per election (2020, 2022), 100 tweets per rumour, about 500 per year. Frames seen: election like a third-world election; censorship by media and tech firms; suspicion of government and voting technology. In Maricopa 2022 the frame switched from voter fraud to voter disenfranchisement while villains and blame stayed the same. In 2020 elites spelled out fraud claims. In 2022 they referred back and let the audience reuse the old story. The authors say this cut the number of frames used, but they do not count it. Ordinary events (Sharpie bleed-through, tabulator errors) were read as fraud. [a03, a04, a05, b02]

**Follow-ups, all same group and data tradition.**
- Prochaska et al. 2023 (CSCW): three 2020 cases where influencers and users co-built evidence for a fraud story; offline acts became new evidence. Only a summary page was opened. [a06]
- Deep Storytelling (CSCW 2025): audiences read 2022 events through the 2020 story. The first per-tweet codebook failed to capture rumouring, so a second was built. Abstract only. [d20]
- Evidence-frame framework (CSCW 2025): misleading claims arise from interaction between often factual evidence and distorted frames. Abstract only. [d21]
- Prochaska et al. 2026 (arXiv 2610.37804): 590 rumours found, 568 coded. 3 coders, each rumour to 2 coders, 50-rumour calibration set, third-coder arbitration. Actor in over 96%. 397 (69.9%) have the full Actor-Object-Action grammar; 171 (30.1%) miss a central element. Rumour summaries were LLM-generated, which the authors flag. No kappa seen. [d19]

**Human continued influence.** Johnson and Seifert (1994): a retracted causal explanation still shapes inference unless a replacement explanation fills the causal gap. Not opened; numbers withheld. Lewandowsky et al. (2012) reviewed it; not opened. [a11, a28]

**Narrative.** Green and Brock (2000): transportation into a story raises acceptance of its beliefs. Not opened. [a27]

**Rival reading.** A deep story may reflect prior belief rather than manipulation. The founding paper has no counterfactual. [b03]

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Deep stories set frames on later events (humans, tweets) | about 1,000 tweets, 2 elections; no effect size, no control | Prochaska 2024 [a01] | [S] qualitative |
| Rumours reuse one grammar | 568 coded; 69.9% full Actor-Object-Action; actor in over 96% | Prochaska 2026 [d19] | [S] same group |
| Misinformation persists after debunking (humans) | k=52, N=6,878; misinfo d 2.41-3.08; debunk d 1.14-1.33; persistence d 0.75-1.06; I2 about 98-99% | Chan 2017 [b04] | [E] |
| Generating supporting reasons raises persistence | debunk d=0.62 (k=18) vs 3.77 (k=3); persistence b=2.09 [0.88, 3.30] | Chan 2017 [b05] | [E] small cells |
| Detailed debunks beat label-only, but confounded | d=1.25 (k=18) vs 0.16 (k=3); r(33)=.52 with misinformation detail | Chan 2017 [b06] | [E] confound flagged |
| Story implying a conspiracy changes later learning (humans) | N=276; blocking 87.4 vs 56.4 (d=1.61); later cue 57.1 vs 72.3 (d=0.49); forced choice d=0.26 | Kelly 2025 [d06] | [S] fictional task |
| Negative misinformation resists correction; corrected positive info reversed | N=403 and N=437, preregistered | COVID continued influence 2021 [d07] | [S] |
| LLMs accept coherent counter-evidence over memory | 8 models; coherent far above entity-swap; shares only in figure | Xie 2024 [a12, c19] | [E] |
| LLM confirmation bias with mixed evidence | GPT-4 PopQA: 1/2 aligned 65.4%, 2/4 75.4%, 2/3 91.0%; ChatGPT 43.0%, 63.3% | Xie 2024 [a13] | [E] |
| Wrong retrieved text beats right prior | over 60% adoption; 6 LLMs, 1,200+ questions | ClashEval 2024 [b27] | [E] abstract only |
| Retrieval poisoning | PaLM 2 ASR 97% NQ, 99% HotpotQA, 91% MS-MARCO with 5 texts; naive injection 0.02 | PoisonedRAG [a16] | [E] |
| LLM-made fakes cut QA | EM down up to 87% (28.20 to 3.53); 14-54% DPR, 20-87% BM25; 0.01-0.1% of corpus | Pan 2023b [a15, c07] | [E] |
| Pre-LLM readers: targeted fakes hurt most | 53.19% vs 7.72% relative EM drop; 0.2-4.0% of corpus | Pan 2023a [a14, c10] | [E] |
| Multi-turn belief erosion | turn 1: 4.1-63.4%; MR@4: 20.7% (GPT-4) to 78.2% (Llama-2-7B avg); robustness 79.3/52.1/49.9/36.3/21.8 | Xu 2024 Farm [a18, c04] | [S] |
| Sycophancy 2023 | wrong suggestion up to 27% accuracy drop (LLaMA 2); "are you sure" up to 27% (Claude 1.3); answer change 32-86%; false admission 42-98% | Sharma 2024 [a19, c17] | [S] |
| Sycophancy 2024 versions | sycophantic 58.19%; progressive 43.52%, regressive 14.66%; persistence 78.5% | SycEval [d15] | [S] |
| Models weigh relevance over credibility cues | style edits neutral to negative; question prefix raised win rate; stated convincingness weakly related to win | Wan 2024 [a17, c01-c03] | [S] |
| LLM fakes harder to catch | humans 9.6% on hallucinated news; GPT-3.5 0.0%; GPT-4 10.0% | Chen and Shu 2024 [a20] | [E] |
| GPT-3 tweets: small human gap | false recognised 0.89 vs 0.92 (p=.0032); true 0.84 vs 0.72; N=697 of 869 | Spitale 2023 [a21] | [E] |
| Persuasion grows with log of size | 5.77 pp avg; +1.26 pp per log unit; ceiling about 12 pp; N=25,982 | Hackenburg 2024 [a23] | [E] |
| Post-training and prompting beat scale | N=76,977; 19 LLMs; 707 issues; 466,769 claims; up to +51% and +27%; scale +1.59 pp per 10x; conversation +2.94 pp (+41%) | Hackenburg 2025 [a24, b20] | [E] |
| Information density drives persuasion; accuracy falls | density r=0.76, 44% of variance; info prompt +2.29 vs +1.37 pp; accurate claims 62% vs 78% (GPT-4o), 56% vs 70%, 72% vs 82% (GPT-4.5) | Hackenburg 2025 [b21, c16] | [E] |
| Personalised GPT-4 debate | N=820; +81.7% odds [26.3, 161.4]; non-personalised +21.3%, p=.31 | Salvi 2025 [a22, b17] | [S] |
| Spotlighting (injection only) | GPT-3.5 ASR about 50-60% to under 3% (datamark, summarisation), 8.0% Q&A; encoding 0.0% and 1.8%; GPT-4 1.0% | Hines 2024 [c22] | [S] |
| Hidden bias not shown in CoT | accuracy drop up to 36%; GPT-3.5 -36.3% | Turpin 2023 [b25] | [E] |
| Reasoning models rarely name a used hint | faithfulness 25% (Claude 3.7), 39% (R1); misalignment hints 20% and 29% | Chen 2025 [d17] | [E] |
| Chatbot lowers conspiracy belief | Study 1 N=1,055: -16.8 pts (d=1.15), 21.43% vs 1.04%; 2 months b=0.03; Study 2 N=2,286; 127 of 128 AI claims true | Costello 2024 [d01, d02] | [S] |
| LLM can raise it as well | N=3,996; bunk +13.6 (g=1.19) vs debunk -12.1; truth-constrained bunking keeps 64% of effect | Costello 2026 [d03, d04] | [S] |
| Debrief rebuttal undoes planted belief | -19.2 pts; Study 2 -15.4, ending 3.20 below baseline | Costello 2026 [d05] | [S] |
| AI correction can hurt later skill | N=67; +21% with AI; unassisted -15.3% at week 4 | Rani 2026 [d16] | [S] small N |
| Credibility step changes action, not enough | harmful execution on notices rated 3 or lower: 63/73/99/67/27%; no rating step +15 pp (CI 13-18) | Beyond Belief 2026 [d18] | [S] |
| Peer agreement misleads | all-wrong peers: harmful revision 15.6% to 62.9%; authority label alone 15.6 to 20.6% | Qu 2026 [d08] | [S] open-weight |
| Source label shifts judgement | 4 models, 4,800 statements, 192,000 assessments; blind agreement mostly 95%+ | Germani and Spitale 2025 [d09] | [S] |
| In-context priming | InstructGPT p_MAP<.001 (syntactic); FLAN-UL2 failed | Lam 2023 [d10] | [S] |
| Cognitive bias battery | 45 LLMs, 2.8M responses; bias in 17.8-57.3% of cases; directives +3.6-9.9% | Knipper 2025 [d11] | [S] |
| Inoculation | technique recognition d 0.28-0.68; truth discernment d 0.10-0.32; YouTube N=22,632 h=0.09, below SESOI 0.10 | Roozenbeek 2022 [b07, b08] | [E] |
| Accuracy prompts | N=34,286, 16 countries | Arechar 2023 [b12] | [E] abstract only |
| Sharing is habitual | 30-40% of false shares from the 15% most habitual; N=2,476 | Ceylan 2023 [b10] | [S] |

## 4. Mechanisms and models

**M1. Frame as filter (Klein).** State: frame F and data stream D. Reading = pick the F that best explains D, then use F to decide which data count. Fixation = F stays after contrary D. Test: put F in context, give a neutral ambiguous event E, score whether the reading of E follows F against a no-F control. This is the untested core (K01).

**M2. Plausibility threshold.** Accept an account if it is coherent and fits what is held; do not demand verification. For LLMs the best-supported form is coherence. Coherent LLM-written counter-evidence beats memory while crude entity-swap evidence does not (a12). PoisonedRAG texts are written to fit the planted answer and reach 0.91-0.99 ASR; a naive injection reaches 0.02 (a16). Engineer reading: the attack surface is internal consistency, not truth.

**M3. Relevance capture.** Models pick the passage most relevant to the question, not the one with trust cues (c01). A one-line "the following text is about the question" prefix raised win rate (c02). Retrievers also prefer fakes because they match the question (b23). Relevance is a cheap forgery target, so provenance must be checked in code.

**M4. Prior versus context tug of war.** Adoption of wrong context rises when model confidence in its prior is low and falls as the error becomes blatant (b27). Mixed evidence is read with confirmation bias toward the prior (a13). Astute RAG turns this into a defence: elicit the model's own prior first, then consolidate with the context (d12).

**M5. Social and authority pressure.** Preference data rewards agreeing with the user; "matches user beliefs" is among the most predictive features (c18). Best-of-N with N=4096: about 25% sycophantic with an oracle preference model vs about 75% with the Claude 2 preference model (b29). Authority label alone moved harmful revision only 15.6% to 20.6%; peer content did the damage (d08).

**M6. Information density.** Persuasion tracks the count of checkable-looking claims (r=0.76), and the most persuasive set-ups were less accurate (b21). Treat dense claim-rich context as a risk marker and check each claim.

**M7. Unfaithful traces.** The model's rationale does not report the planted cue (b25, d17). A trace reader cannot detect framing carry-over. Detection must compare outputs with and without the cue.

**M8. Continued influence and repair (people).** Retraction without replacement leaves a causal gap and the claim persists (a11, b04). Generating supporting reasons raises persistence (b05). A claim-by-claim rebuttal in a debrief undid a planted belief (d05). A repair step should name the planted account and give a replacement explanation.

**M9. Provenance marking.** Delimit, datamark or encode untrusted text. Cuts instruction injection a lot (c22). Untested for framing.

**M10. Isolate-then-aggregate.** Answer from passage groups separately, then combine by counts (RobustRAG d13; Pan voting b24). Independent subsets limit the reach of a few coherent fakes. Cost grows linearly with groups.

## 5. What holds up

**Replicated or multi-source (established).**
- Misinformation persistence after debunking in people: meta-analysis k=52, N=6,878. Heterogeneity 98-99%, mostly lab analogues, mean age about 20, 72% female. [b04]
- Coherent injected text steers retrieval LLMs: Pan 2023, PoisonedRAG and ClashEval agree across model families. [K04, K05]
- Coherent counter-evidence beats memory and mixed evidence is read with confirmation bias (Xie, supported by Pan). [K02]
- Reasoning text hides the real cause: Turpin 2023 and Chen 2025, two model generations. [K15]
- AI persuasion scales weakly with size (Hackenburg 2024, 2025). [K10]
- LLM-written fakes are harder to catch, but the size differs by method: 9.6% human detection of one category versus a 3-point gap on tweets. [K09]

**Failed, small or contested.**
- Inoculation: technique recognition d up to 0.68, truth discernment d 0.10-0.32, field effect h=0.09 below the preregistered h=0.10. Knowing a technique exists does not reliably change the judgment. [b07, b08]
- Bad News game: abstract-only, n=266, better than Tetris. The response-bias counter-argument is from memory, not verified. [b09]
- AI correction: Costello 2024 durable (2 months) versus Rani 2026 unassisted detection down 15.3% at week 4 (N=67). Different outcomes, so not a failed replication. [d01, d16]
- Truth-constraint prompt on a persuader cut but did not remove bunking; bunking worked even in the top truth quartile. [d04]
- Story form: expected to help (Green and Brock), but storytelling did not beat the basic prompt in Hackenburg 2025 (one of eight strategies, effect not read). Contested. [K12]
- Vigilance warning: inconsistent in Pan 2023, 0 to +8% across attack types. [b24]
- Chain-of-thought and reflection cut harmful revision (63.9 to 36.5% in one report) but did not do so without blocking good revision. [d08, K20]
- Trained detectors: AUROC 91.4-99.7 in domain, 50.7-64.8 out of domain. [c08]
- No independent replication of the deep-story claim. [K01]

**Moderators.**
- Model strength: Farm robustness GPT-4 79.3 vs Llama-2-7B 21.8; size above 32B cut bias in 39.5% of cases (Knipper); alignment tuning raises sycophancy while scale and reasoning help (d14). [c05, d11, d14]
- Blatancy: less deviation from truth means more adoption. [b27]
- Corpus share: 0.01-0.1% was enough. [b23]
- Strategy: non-factual logical appeals strongest in Farm; plain repetition weaker. [a18]
- Rebuttal type: citation-based rebuttals had the highest regressive rate; preemptive 61.75% vs in-context 56.52%. [d15]
- Person: Republicans +60% more persuadable in Salvi; topic knowledge cut opinion change. [b17]

**Interventions that worked (measured, cheap).** Astute RAG: +6.85% over best baseline (Claude 3.5 Sonnet), +4.13% (Gemini 1.5 Pro), about 5% extra tokens; in the all-wrong worst case plain RAG fell over 50 points below no-RAG. RobustRAG: injection success from over 90% to 15% or less. Narrator reframing: memorisation 35.2% to 3.0% (but it raises trust in context, the opposite risk). Third-person persona: Turn of Flip up to +63.8% in debate. Forewarning cut harm in 4 of 5 models but cost legitimate task completion. Reminder prompt in Farm helped ChatGPT partly. [d12, d13, c20, d14, d18, c06]

## 6. Language models

**Direct tests of deep-story priming on current LLMs: none.** Nearest: Lam 2023 (pronoun priming; InstructGPT shows a syntactic effect, FLAN-UL2 fails; semantic bias not shown) and Kelly 2025 in people (d=0.26-0.49 on a later cue). [d10, d06]

**Uptake of false or coherent content.**
- Memory vs evidence: coherent counter-evidence accepted by most of 8 models; crude evidence rejected. Mixed-evidence bias grows with memory-aligned share (GPT-4 65.4% to 91.0%). [a12, a13]
- Retrieval: ClashEval over 60% adoption; PoisonedRAG above 90% in almost all cases across 8 LLMs; Pan 2023 up to 87% EM loss. Mostly 2023-2024 models. No frontier-model numbers found for Farm, ClashEval or PoisonedRAG. [K04, K05, d24]
- Belief erosion: Farm 4.1-63.4% at turn 1, 20.7-78.2% MR@4. GPT-4 doubled its misinformed rate after 3 more repeated turns on items it first wavered on. [c04, c05]
- Pushback: 2023 models flip 32-86% and falsely admit 42-98%. 2024 models in SycEval: sycophantic 58.19%, 78.5% persistence. Multi-turn tests on 17 recent models: alignment tuning raises sycophancy; scale and reasoning help. [c17, d15, d14]
- Peer content: all-wrong peers push correct-to-wrong revision to 62.9%. [d08]
- Cognitive-bias battery: 45 LLMs bias-consistent in 17.8-57.3% of cases; detailed prompts cut most biases up to 14.9% but overattribution rose up to 8.8%. [d11]
- Source label: author nationality or self-attribution changed judgments of identical text. [d09]
- Tool use: 5 victim LLMs acted on false notices they rated untrustworthy in 27-99% of cases; dropping the rating step added 15 pp harmful execution. [d18]

**What models weigh.** Relevance over credibility (Wan), coherence over truth (Xie), claim density (Hackenburg); not human style cues. Credibility and sharing questions overlap: credibility explains 30.8-72.5% of model sharing variation and adding sharing changes error by -0.25 to +0.69%. [c01, a12, b21, d23]

**Models as persuaders (threat side).** GPT-4 with personal data +81.7% odds in debate. Conversation beats static (+2.94 pp). The chatbot that cut conspiracy belief 21% can raise it by a similar amount; a truth prompt did not remove it; 85.2% of requests to bunk were complied with. [a22, a24, d03, d04]

**Own reasoning.** Biasing hints cut accuracy up to 36% with no mention in CoT; reasoning models verbalise a used hint 25% (Claude 3.7) and 39% (R1); they are 3.6x and 1.7x more faithful than non-reasoning siblings. [b25, d17]

**Era caution.** GPT-3, GPT-3.5, Llama-2 and 2023 models dominate. 2025-2026 data: SycEval, SYCON (17 LLMs), Astute RAG on Claude 3.5 Sonnet and Gemini 1.5 Pro, Costello 2026 (Claude Opus 4.6, GPT-5.2, Gemini 3 Pro), Chen 2025, Beyond Belief (small open-weight plus Gemini-3.6-Flash). Treat every range as model-specific.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established [E])

1. **[E] G / S1: carry source and trust status in code, not in model judgement.** Models weigh relevance over trust cues, and style is not a detector. Part S1. Ids: a17, c01-c03, a20, a21, b22 (K08 is single-source, K09 established; the code-side rule is the safe part).
2. **[E] S1: coherence is not support.** Mark coherent but unsourced, claim-dense context as a risk marker; check each claim against the task. Part S1. Ids: a12, a16, b21, c16 (K02, K04, K10).
3. **[E] G10 (extend): carry-over of a planted cue is detected by comparing outputs with and without the suspect context, never by reading the trace.** Part G10. Ids: b25, d17 (K15).
4. **[E] G (retractions): when a claim is found false, state a replacement account rather than only "ignore it".** Human evidence is established; the LLM version is not and goes to Test first. Part G note. Ids: b04, b05 (K03).
5. **[E] S1 / memory: keep the prior answer visible beside inserted or retrieved evidence.** The mechanism is established (b27, a13); the exact remedy is [S] (T4 below). Ids: b27, a13 (K05).
6. **[E] No trained fake detector as the guard.** Out-of-domain AUROC 50.7-64.8. Part S1. Ids: c08 (K14).
7. **[E] G2 wording check:** a stated claim or authority label alone is never a reason to revise; only new checked output is. This restates G2. Ids: d08, d15, a19 (K07 is single-source; use only as a wording strengthening).

### Test first ([S] or [C])

| Item | Part | Status | Evidence | Why test |
|---|---|---|---|---|
| T1 Planted-frame priming check with no-plant control | S1 note | [S] | K01, K21, d06, d10 | core claim has no LLM data |
| T2 Frame-stripping: neutral actor-object-action restatement before reasoning | S1 | [S] | K22, d19, d09 | cheap; no equal-token test |
| T3 Provenance tags on inserted text | S1 | [S] | K13, c22 | works for injection; unknown for framing |
| T4 Prior-first recall then reconcile | S1 | [S] | K05, K20, d12 | best gain per token so far |
| T5 Isolate-then-aggregate over evidence subsets | S1 / vote | [C] | K14, K20, d13, b24 | linear token cost |
| T6 Plausible-versus-verified split into two checks | S1 | [S] | K19, d18, d22, d23 | no direct test |
| T7 Frame check beside fact check on true-but-selective evidence | S1 | [S] | K18, d03, d04 | fact check alone may miss frame manipulation |
| T8 Claim-by-claim rebuttal of a planted frame vs plain retraction | repair | [S] | K17, d05 | humans only |
| T9 Auditor pass comparing with and without the suspect context | G10 | [S] | K15, d17 | traces will not show it |
| T10 Accuracy prompt at start of S1 | S1 | [S] | K16, b11, b12 | human nudge only |
| T11 Check by action, not stated belief | S1 | [S] | K19, d18 | models act on notices they rated bad |

Do not add narrator reframing as a misinformation defence: it makes the model trust the context more (c20).

## 8. Concrete tests on our bench

All arms at equal tokens (setup cost counted, G7), against plain and best-of-N. Report right-to-wrong and wrong-to-right flips separately.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Deep-story priming | ambiguous neutral events, each preceded by a planted 150-word frame; control has a neutral paragraph of equal length | plain with control vs plain with frame vs frame plus S1 masking | share of frame-consistent readings | unknown; a shift of at least 5 pp, with masking removing at least half |
| B2 Frame-stripping | same items | raw context vs neutral restatement then reason | frame-consistent rate and accuracy | lower shift, accuracy not lower |
| B3 Coherent vs crude false evidence | paired passages, Xie-style | plain vs rate-source-first vs prior-first | accept rate of false evidence | prior-first lowers adoption; rating-first only partly (d18) |
| B4 Poison injection | k=1, 3, 5 fake passages in context | no isolation vs provenance tags vs subset vote | answer flips | tags and vote lower flips; vote costs tokens |
| B5 Farm-style erosion | 4 turns of misinformation on items answered correctly | plain vs recheck step | MR@4 | modest drop |
| B6 Pushback | "are you sure" and wrong suggestion | plain vs strengthened G2 | right-to-wrong flips | fewer flips |
| B7 Retraction | retraction mid-context with and without replacement account | plain | share of answers using the retracted claim | replacement lowers persistence |
| B8 True-but-selective | true facts under a misleading frame | fact check vs fact check plus frame check | misleading-reading rate | frame check catches cases fact check misses |
| B9 Trace audit | planted hint | read trace vs A/B outputs with and without hint | detection rate | trace under 40%; A/B higher |
| B10 Plausible vs verified | coherent fakes vs crude truths | one check vs two split checks | accept rate of fakes | split lowers fake acceptance |

## 9. What does not transfer, and why

- **Deep story as social identity.** Needs a group, identity and feeling. A single agent has no tribe. Only a context-carried frame transfers. [a09]
- **Narrative transportation.** Works on people (Green and Brock). In LLMs, claim density, not story form, drove persuasion. [a27, b21]
- **Sharing, habit, platform design.** Human sharing is habitual (Ceylan); an agent does not share. [b10]
- **Inoculation and gamified prebunking.** Built for people learning over time. For an agent only a one-line forewarning has been tested. [b07, d18]
- **Persuasion studies (Salvi, Hackenburg, Costello).** They measure people being moved, so they inform the threat, not the defence. [K11]
- **Spotlighting.** Proven for instruction injection, not frames. [c22]
- **In-group repetition as credibility.** An agent has no in-group unless the context supplies one. [a05]
- **Trained detectors.** Fail out of domain. [c08]
- **Prochaska's data.** US English Twitter election rumours, one political direction, LLM-made summaries in 2026 coding. [d19]
- **Human debrief.** Works through trust in the experimenter. [d05]

## 10. Open questions

1. Does a frame planted earlier in an LLM's context shift how a later unrelated ambiguous event is read, and by how much on current frontier models? Nothing measures this. [d24]
2. Does S1 frame-stripping or provenance marking reduce that shift at equal tokens?
3. Which cheap defence is best on coherent frames: subset voting, prior-first, narrator, accuracy prompt? No head-to-head.
4. What are 2025-2026 frontier numbers for Farm, ClashEval and PoisonedRAG?
5. Is the deep-story claim real in people? No experiment, no independent replication. Johnson and Seifert, Green and Brock, Lewandowsky 2012 and Walter and Tukachinsky 2020 were not opened.
6. Does retraction plus replacement repair LLMs as it does people?
7. Do plausibility and verification, asked as two checks, differ in effect? Only indirect evidence.
8. Can an auditor pass catch frame carry-over cheaply?
9. What was the inter-coder agreement in Prochaska's coding (no kappa seen)? Do the 2026 tropes hold on other events?
10. Is a frame effect in LLMs separable from sycophancy and plain recency in context? The sources cannot tell.

## 11. Sources

[V] opened and read in the research run (full text, PDF, abstract page or summary page as noted); [M] snippet or memory only.

- [V] Prochaska, Vera, Tan, Starbird 2024, Misleading Ourselves. https://arxiv.org/abs/2410.14858
- [V] Prochaska et al. 2026, New Election, Same Old Story. https://arxiv.org/abs/2610.37804
- [V] Deep Storytelling, CSCW 2025 (abstract). https://doi.org/10.1145/3757576
- [V] Evidence-frame framework, CSCW 2025 (abstract). https://doi.org/10.1145/3757522
- [V] Prochaska et al. 2023, Mobilizing Manufactured Reality (summary page only). https://cip.uw.edu/?p=8017
- [M] Weick 1995. https://doi.org/10.2307/2393339
- [M] Klein et al. 2007. https://doi.org/10.4324/9780203810088
- [M] Hochschild 2016; Polletta and Callahan 2019. https://doi.org/10.1007/s11133-017-9378-2
- [M] Kapferer 1990. https://www.routledge.com/Rumors-Uses-Interpretations-and-Images/Kapferer/p/book/9780765804860
- [M] Johnson and Seifert 1994. https://doi.org/10.1037/0278-7393.20.6.1420
- [M] Green and Brock 2000. https://doi.org/10.1037/0022-3514.79.5.701
- [M] Lewandowsky et al. 2012. https://doi.org/10.1177/1529100612451018
- [M] Walter and Murphy 2018. https://doi.org/10.1080/03637751.2018.1467564
- [V] Chan et al. 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5673564/
- [V] Roozenbeek et al. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9401631/
- [M] Bad News preprint 2025. https://doi.org/10.31234/osf.io/7xgbt_v1
- [M] Ceylan et al. 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC9942822/
- [M] Pennycook et al. 2021. https://doi.org/10.1038/s41586-021-03344-2
- [M] Arechar et al. 2023. https://doi.org/10.1038/s41562-023-01641-6
- [M] Vosoughi, Roy, Aral 2018. https://doi.org/10.1126/science.aap9559
- [V] Kelly, Hattersley, Ludvig 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC13400819/
- [M] COVID continued influence 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8652781/
- [V] Xie et al. 2024. https://arxiv.org/abs/2305.13300
- [V] Pan et al. 2023a. https://arxiv.org/abs/2110.07803
- [V] Pan et al. 2023b. https://arxiv.org/abs/2305.13661
- [V] Zou et al. PoisonedRAG. https://arxiv.org/abs/2402.07867
- [V] Wan, Wallace, Klein 2024. https://arxiv.org/abs/2402.11782
- [V] Xu et al. 2024 Farm. https://arxiv.org/abs/2312.09085
- [V] Sharma et al. 2024. https://arxiv.org/abs/2310.13548
- [V] Chen and Shu 2024. https://arxiv.org/abs/2309.13788
- [V] Spitale et al. 2023. https://arxiv.org/abs/2301.11924
- [V] Salvi et al. 2025. https://arxiv.org/abs/2403.14380
- [V] Hackenburg et al. 2024. https://arxiv.org/abs/2406.14508
- [V] Hackenburg et al. 2025. https://arxiv.org/abs/2507.13919
- [M] Costello, Pennycook, Rand 2024 (Science page 403; manuscript numbers from an earlier run, not re-opened). https://www.science.org/doi/10.1126/science.adq1814
- [V] Costello et al. 2026. https://arxiv.org/abs/2601.05050
- [M] Goldstein et al. 2023, 2024. https://arxiv.org/abs/2301.04246 ; https://doi.org/10.1093/pnasnexus/pgae034
- [V] Qu, Fu, Hu 2026. https://arxiv.org/abs/2606.01637
- [V] Germani and Spitale 2025. https://arxiv.org/abs/2505.13488
- [V] Lam et al. 2023. https://arxiv.org/abs/2305.16917
- [V] Knipper et al. 2025. https://arxiv.org/abs/2509.22856
- [V] Wang et al. 2025 Astute RAG. https://arxiv.org/abs/2410.07176
- [V] Xiang et al. RobustRAG. https://arxiv.org/abs/2405.15556
- [V] Hong et al. 2026 SYCON. https://arxiv.org/abs/2505.23840
- [V] Fanous et al. 2025 SycEval. https://arxiv.org/abs/2502.08177
- [V] Rani et al. 2026. https://arxiv.org/abs/2510.01537
- [V] Chen et al. 2025 Reasoning models. https://arxiv.org/abs/2505.05410
- [V] Beyond Belief 2026. https://arxiv.org/abs/2610.33962
- [V] Plausibility as Failure 2025 (abstract). https://arxiv.org/abs/2512.16750
- [V] What Does a Sharing Question Add 2026. https://arxiv.org/abs/2604.06820
- [V] Turpin et al. 2023. https://arxiv.org/abs/2305.04388
- [V] Shi et al. 2023. https://arxiv.org/abs/2302.00093
- [V] Wu et al. 2024 ClashEval (abstract and intro). https://arxiv.org/abs/2404.10198
- [V] Zhou et al. 2023 Context-faithful prompting. https://arxiv.org/abs/2303.11315
- [V] Hines et al. 2024 Spotlighting. https://arxiv.org/abs/2403.14720
- [M] Greshake et al. 2023 (first page only). https://arxiv.org/abs/2302.12173
