# Three attention networks: deep document

*Subfield A07.05. Evidence ids (a01-d18) are in evidence_a-d.jsonl; claims K01-K25 are in claims.jsonl; the cross-check is in critique.md. Relevance to our agent is background only: no study runs alerting or orienting on an LLM, and the "executive" results are Stroop and flanker.*

## 1. What it is

Posner and Petersen (1990) proposed that human attention is three separate brain systems, each with its own job, anatomy and chemical:

- **Alerting.** Reaching and holding a ready state. Norepinephrine from the locus coeruleus, right hemisphere for tonic alertness. A warning signal speeds the response (phasic alerting). Guanfacine and clonidine can block warning-signal effects (a03).
- **Orienting.** Selecting information from many inputs. Parietal lobes, frontal eye fields (dorsal system, goal-directed), temporo-parietal junction (ventral system, reorienting to surprises). Acetylcholine affects orienting, not alerting (a03, a14).
- **Executive control.** Resolving conflict between responses, monitoring errors, holding the task set. Anterior cingulate, anterior insula, lateral prefrontal cortex. Later split by Dosenbach into a cingulo-opercular network (sustained set) and a frontoparietal network (transient adjustments) (a09, a15).

Fan, McCandliss, Sommer, Raz and Posner (2002) built the **Attention Network Test (ANT)** to measure all three in one 30-minute session. It joins a cueing task (Posner 1980) with the Eriksen flanker task (1974). A central arrow points left or right; the person presses the matching key. Flanking arrows are congruent, incongruent or neutral. Before the target comes one of four cues: none, centre, double (both locations), spatial (the target location).

Scores are subtractions of mean RT:

- Alerting = no cue minus double cue.
- Orienting = centre cue minus spatial cue.
- Conflict (executive) = incongruent minus congruent.

The claim to test was that the three scores are efficient and independent. The field found this is only partly true (section 5).

Why this matters for us: our agent is a scaffold around a language model. The three networks are a taxonomy of what a thinking system needs: a readiness signal, a selection step, a conflict check. The honest finding is that the literature gives analogies, not tested mechanisms. No LLM has been run on the real ANT. The only LLM work is on the conflict half (Stroop, flanker, distractor text).

## 2. History and theories in depth

**1974: Eriksen and Eriksen flanker task.** Respond to a central letter and ignore flankers. Incongruent flankers slow responses and cut accuracy. Human accuracy 93-96%, RT 300-500 ms, as cited in a12. Source not opened.

**1980: Posner cueing.** A cue at the target location speeds the response; an invalid cue slows it. This is the orienting effect.

**1990: Posner and Petersen review.** Three networks. Cited nearly 3,500 times by 2012 (a03). The ACC top-down role rested on "rather slim evidence" in 1990 (a03). Known to us only through the 2012 restatement.

**1990: Cohen, Dunbar, McClelland.** A connectionist account of Stroop: attention modulates pathways; reading wins because it is more practised (c26, not opened). **2001: Botvinick et al.** Conflict monitoring: a monitor detects response conflict and raises control, giving conflict adaptation (c27, not opened). Both are the models behind the later LLM papers.

**2001: Fan, Wu, Fossella, Posner twin study (a02).** 26 MZ and 26 DZ pairs (104 people). Mean alerting 40 ms (SD 16), orienting 56 (SD 17), conflict 80 (SD 34), RT 498 (SD 67). Retest .36, .41, .81 for one session; .53, .58, .90 for the two-session mean. Twin r for alerting .465 (MZ) vs .375 (DZ); orienting .099 vs .395. Conflict looked heritable, but the DZ value was suspiciously low, which inflates the estimate (the authors' own flag).

**2002: Fan et al., the ANT (a01, d01-d03).** N=40 adults, mean age 30.1. Mean RT (ms) by cue (none / centre / double / spatial): congruent 530/490/479/446; incongruent 605/585/574/515; neutral 529/483/472/442. Scores: alerting 47 ms (SD 18), orienting 51 (SD 21), conflict 84 (SD 25). Retest .52, .61, .77; raw RT .87. No pair of scores correlated significantly. ANOVA: cue F(3,117)=291.99, flanker F(2,78)=438.86, interaction F(6,234)=17.43, all p<.001. So an interaction was there from the start. Eye movements 3-5% of trials. A pilot with 7-year-olds is mentioned without numbers.

**2004: Rueda et al. child ANT (a05, a21).** Fish instead of arrows. Conflict improves from age 6 to 7, then stays flat. Child Exp 3: cue F(3,129)=20.65, flanker F(2,86)=65.3, cue x flanker F(6,258)=1.03, not significant. Child RTs no cue 875/966 ms (congruent/incongruent); spatial cue 789/925 ms. The paper is closed access; the score tables were not read cleanly (d04). Treat child score values as unverified.

**2004: Callejas, Lupianez, Tudela (a24).** Double-modality ANT; significant interactions for all pairs. Known only from a table in Wang 2014. The main early challenge to independence.

**2006-2008: Dosenbach dual control networks (a15), Corbetta and Shulman dorsal/ventral orienting (a14).** Both refine the anatomy. Petersen and Posner (2012) concede about five control networks in total, range three to seven.

**2009: ANT-R (a04, a23, d05).** N=30, mean age 25.4. Adds 75% valid spatial cues, cue-target intervals of 0, 400, 800 ms and location conflict. Overall RT 604 ms (SD 59), accuracy 94%. Alerting 29 ms (SD 24). Validity effect 95 ms (SD 32). Flanker conflict 137 ms (SD 43). Alerting x flanker -13 ms (t(29) = -2.07). Conflict 171 ms after an invalid cue vs 111 ms after a valid one (validity x flanker 60 ms). At the 400 ms interval, incongruent minus congruent was 687 vs 559 ms with no cue and 664 vs 524 ms with a double cue: alerting speeds responses but raises conflict. Invalid-cue cost at 0 ms interval -60 ms. Moving and engaging 41 ms, disengaging 54 ms. Lesson: the networks interact.

**2011-2015: Psychometric turn.** McConnell and Shore (2011), Ishigami and Klein (2011), Habekost et al. (2014), Wang et al. (2014, 2015) show that the subtraction scores mix conditions and that two of three have poor reliability.

**2012: Petersen and Posner "20 years after" (a03).** The authors' own update. Same three networks, more anatomy, more neurochemistry.

**2018: Hedge, Powell, Sumner "reliability paradox" (b01-b03).** Robust group effects give unreliable individual differences. Hits flanker and Stroop costs directly.

**2020-2024: Revisions and population work.** ANTI and ANTI-Vea (auditory warning, vigilance; a10, b16, b17). ANT database (a11). Lifespan graphical meta-analysis (b13). Calibration to fix the paradox (Kucina 2023, b04).

**2025-2026: LLMs.** Patel, Wang, Fan (Stroop in GPT-4o and Claude), de Langis et al. (flanker in open models), VLM conflict papers, mechanism papers on text conflict. Details in section 6. The Patel paper is by ANT authors and maps transformer self-attention to orienting, with no alerting or executive component (b24, d17).

## 3. Core findings with exact numbers

Status: **E** established (two or more independent sources), **S** single source, **C** contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ANT adult scores, original sample | Alerting 47 ms, orienting 51, conflict 84; N=40 | Fan 2002 (a01, d01) | E |
| Twin sample means | Alerting 40, orienting 56, conflict 80 ms; N=104 | Fan 2001 (a02) | S |
| Retest reliability, Fan 2002 | .52 / .61 / .77 (alerting / orienting / conflict) | d02 | E |
| Retest reliability, Fan 2001 | .36 / .41 / .81 single session; .53 / .58 / .90 two-session mean | a02 | E |
| Split-half across 15 studies | .38 vigilance, .55 orienting, .81 executive (second-hand) | MacLeod 2010 via a07 | S |
| Network scores nearly uncorrelated | N=588: r .07 (A-O), .01 (A-E), -.04 (O-E) | McConnell and Shore 2011 (b07) | E |
| Scoring method changes correlations | Old: A-E -.13, A-O .03, E-O .14. New: .30, -.01, .44 (p=.007); N=36 | Wang 2014 (a06) | S |
| Mixed design lifts reliability | Split-half alerting .684, orienting .588, executive .616; N=44; A-O r=-.31 not surviving Bonferroni | Wang 2015 (b11) | S |
| Networks interact | Cue x flanker F(6,234)=17.43; about half of 14 ANT studies show strong interactions | a01, a20, a04 | E |
| Alerting can hurt conflict control | 400 ms interval: 687 vs 559 ms (no cue), 664 vs 524 ms (double cue) | Fan 2009 (a23) | S |
| Validity shapes conflict | 171 ms after invalid cue vs 111 ms after valid; N=30 | Fan 2009 (a04) | S |
| Executive score varies by cue type | Trimmed RT flanker effect differs by cue, t>4.3, p<.001 | McConnell and Shore (b08) | E |
| Reliability paradox, flanker | RT cost ICC .40 (Study 1), .57 (Study 2); congruent .74, incongruent .66; SEM 15 ms | Hedge 2018 (b01, b02, critique) | E |
| Reliability paradox, Stroop | RT cost ICC .60 / .66; go/no-go commission .76 | Hedge 2018 | E |
| Tasks do not share a construct | Flanker cost vs Stroop cost r=.14, disattenuated .25; N=100 | Hedge 2018 (b02) | E |
| Trials for stable conflict score | About 420 for r=.8 at trait precision .13 | Kucina 2023 (b04) | S |
| Repeated sessions raise reliability | N=10 older adults, 10 sessions; reliable in RT only with more than 9 sessions | Ishigami and Klein 2011 (b05) | S |
| Executive vs TVA tests | Only executive retest matched TVA; N=68, 3 sessions; literature retest alerting/orienting .35-.60, executive .65-.80 | Habekost 2014 (b09) | S |
| ADHD effect small | 491 ADHD vs 402 controls: alerting +13 ms (5-22), executive +13 (3-22), orienting +2 (-5 to 10) | ANT database (a11) | S |
| ADHD meta-analysis | 7 studies, N=3,826; alerting g=0.235 (0.021-0.449); RT g=0.433 | b21, snippet only | S |
| Cross-cultural RT gap | China vs Europe mean RT 110 ms (43-177), 27 studies | a11 | S |
| Chronic exercise and conflict | Active 31 vs passive 33: group x condition F(1,60)=5.29, p=.025, partial eta2 .081 | Perez 2014 (a08) | S |
| Vigilance and executive decrement | N=617; interference grows with time on task, partial eta2 .02 (RT) | Luna 2022 (b17) | S |
| Heritability | Only conflict clearly heritable; 52 pairs; wide intervals | a02 | S |
| Child ANT | No cue x flanker interaction, F(6,258)=1.03 | Rueda 2004 (a21) | S |
| Lifespan | Alerting adult-like by about 12; adult executive RT cost rises with age while error cost trends the other way; 36 publications | Klein 2024 (b13, b14) | S |
| LLM Stroop collapse with list length | GPT-4o incongruent 91% (5 words), 57% (10), 22% (20), 15% (40). Claude 3.5 Sonnet 76% (20), 24% (40). Congruent about 99% at 20 | Patel 2026 (a16, b23) | S |
| LLM flanker | Open 7B-72B models 40-60% incongruent vs human 93-96% | de Langis 2025 (a18) | S |
| Reasoning closes flanker gap | Llama-3.1-8B .471 to .910; Qwen2-32B .638 to .985 | a18, d09 | S |
| VLM conflict | 47 VLMs, 4,410 tasks: 0.852 congruent vs 0.567 incongruent (diff 0.285); squared 0.634 vs 0.297 | Wang 2025 (c01) | S |
| VLM prompt wording | Ink accuracy 24% to 97% by wording; "ignore the word" prompt 31.1% vs short prompt 60.0% (Qwen2-VL-7B) | Teker 2026 (c07, d12) | S |
| CLIP word dominance | Word 97.8% vs ink about 20%; 23,338 images: 99.5% vs 15.9% | c06 | S |
| Conflict adaptation in VLMs | 12 of 13 open VLMs show it | Hu 2025 (c04, d14) | S |
| Text LLM conflict | Gemma-2-2B correct-answer probability 0.9644 vs 0.5676; ablation 0.8829 vs 0.0962 | Hu 2026 (c09, c10) | S |
| Distractor text hurts LLMs | Under 30% of problems solved consistently (GSM-IC) | Shi 2023 (c15) | E |
| Self-consistency vs distractors | 20 samples: +11 points micro; best macro 45% | Shi 2023 (c16) | S |
| System 2 Attention | Factuality 62.8% to 80.3% (LLaMA-2-70B); GSM-IC +12 and +10 points | Weston 2023 (c17, d06) | S |
| Position effects | Mid-context accuracy drops over 20 points | Liu 2023 (c19) | E |
| Inhibition-gated deliberation | 8.2% routed lifts 47.90% to 48.92% vs random 46.76% | He 2026 (c21) | S |
| Semantic deception | Level 4b: GPT-4o 40%, o1 94%, V3 88%, R1 40% | De Leeuw 2026 (d11) | S |
| A-not-B errors in ICL | Drops up to 83.3% (Qwen1.5-7b, 25 shots) | Han 2024 (c20) | S |

All ANT numbers are subtraction scores in milliseconds, not standardised effect sizes, and come from mostly young, Western samples.

## 4. Mechanisms and models

Written so an engineer could build the probes or the controls.

**4.1 The ANT as a program.** Per trial: fixation 400-1600 ms random; cue 100 ms; 400 ms gap; target and flankers up to 1700 ms; total trial about 3800 ms (a08). Conditions 4 cues x 3 flankers. Scores by cell-mean subtraction. To handle the mixed-measure problem, compute the executive score within each cue type and look at it separately (b08). Non-orthogonal scoring (Wang 2014, 2015) uses cell differences that are not collapsed across cue types.

**4.2 Why subtraction scores are weak.** Reliability = between-person variance / total variance (Hedge, b03). Experimental tasks are built to shrink between-person variance. A difference of two correlated RTs removes the shared variance and leaves noise. Rule for an engineer: a "conflict cost" compared across models is noisy; a paired comparison inside one model over many items is not. Plan for about 420 trials per condition for stable person-level scores in humans at r=.8 (b04). The LLM figure is unknown.

**4.3 Cost-benefit competition model (Cohen 1990; Hu 2026).** Two pathways run in parallel. A strong default (reading the word; the same-colour completion) competes with a weaker task-defined pathway (name the ink; follow the in-context rule). Control adds gain to the task pathway. In an LLM: probability of the correct answer comes from a softmax over default and rule logits. Hu 2026 measured this on Gemma-2-2B: default same-colour next-token probability 0.5074 vs 0.0822 for the runner-up. Making the default stronger (fine-tuning) lifted congruent margin 0.9644 to 0.9846 and cut incongruent: a trade. Five rule clauses instead of two cut incongruent probability by 0.3039 with little change on congruent.

**4.4 Two attention pathways in a text LLM (c10).** Short-range attention to the surface cue serves congruent trials. Long-range attention to the rule prefix serves incongruent trials. Ablating attention to the satisfied consequent changed incongruent probability by 0.8829 vs 0.0962 congruent. A conflict-modulated supernode sits in layers 24-25 of InternVL 3.5 4B; ablating it raises Stroop errors while congruent trials barely change (c05). Needs open weights.

**4.5 Feature competition in VLMs (Teker 2026).** In CLIP, word identity lies along stronger, more separable embedding directions than ink colour. Steering along word directions succeeded in 100% of cases, along colour directions in 36.67% (d13). Prompt wording selects which direction is read.

**4.6 Conflict monitoring and adaptation (Botvinick 2001).** A monitor measures co-activation of competing responses and raises control on the next trial. Test: accuracy on an incongruent trial after an incongruent trial (II) beats that after a congruent trial (CI). Hu 2025 used 30 CC, 120 CI, 120 IC and 360 II sequences per layout and scored log probability of the correct colour token. Patel found no trial-to-trial adaptation in GPT-4o and Claude (a16 summary).

**4.7 System 2 Attention (Weston and Sukhbaatar 2023, c17).** Two calls. Call 1: rewrite the context, keeping only relevant material and the question. Call 2: answer from the rewrite only. The cost is one extra generation of roughly context length; the paper gives no number (d07). Keeping the original context beside the rewrite was worse (74.5% vs 80.3%).

**4.8 Inhibition-gated slow reasoning (He and Feng 2026, c21).** Draft a fast answer. A controller reads confidence, logit margin, parseability and generation cost and decides whether to suppress the draft and think slowly. Routed 8.20%; gain 1.02 points; random routing at the same budget was 1.14 points below the start.

**4.9 Cue-validity probe (not built; proposed in K25).** A hint is right with probability 0.8 and wrong with 0.2. Alerting analogue: a "hard item next" prefix. Orienting analogue: a valid or invalid pointer to where the answer lies in context. Score accuracy and tokens with and without the cue, and the invalid-cue cost (human analogue: 95 ms in ANT-R).

## 5. What holds up

**Holds up**
- The three scores are nearly uncorrelated in large samples: N=588, r .07/.01/-.04 (K01, E). This is a statement about averaged scores.
- The executive score is the reliable one (.77-.81 retest; .81 split-half). Alerting and orienting are .36-.61 (K04, E).
- Interactions exist: cue x flanker F(6,234)=17.43 in the original paper; about half of 14 ANT studies show strong ones; they depend on cue-target interval, modality and inhibition of return (K02, E).
- Group effects are robust but individual differences are not (reliability paradox; K05, E).

**Failed or weakened**
- Full independence. The subtraction score mixes conditions: executive scores differ across the four cue types, t>3.3 after Bonferroni (K03, E). With non-orthogonal scoring, alerting-executive r=.30 and orienting-executive r=.44 appear (Wang 2014; N=36, small).
- Child independence is a developmental fact, not a law: adults show the cue x flanker interaction, children do not (F=1.03; K09, S).
- Heritability: 52 pairs, wide intervals; DZ conflict value suspiciously low (K07, S).
- Executive control as one construct: flanker cost vs Stroop cost r=.14, disattenuated .25 (K06, E).
- Inhibition of return usually vanishes in ANT, so "orienting" is mostly the benefit of valid cueing (a20).
- Alerting reliability .684 in a mixed design vs .14-.38 in older work suggests design, not the construct, drives the poor values (critique). A-O r=-.31 did not survive Bonferroni.

**Moderators**
- Cue-target interval (alerting peaks near 400 ms, lasts no longer than 900 ms).
- Signal modality (visual vs auditory warning; auditory isolates phasic alerting, ANTI).
- Age: alerting near adult level by 12; executive improves through childhood; adult RT cost rises with age while error cost trends the other way (b13, b14).
- Culture: China vs Europe RT gap of 110 ms (43-177), so absolute milliseconds do not transfer.
- ADHD: alerting +13 ms (5-22), executive +13 (3-22), orienting about 0; the meta-analysis of 7 studies finds alerting g=0.235 but not executive.
- Time on task: executive control declines with the vigilance decrement, N=617, small effects.

**Interventions**
- Worked: repeated measurement (reliability rises with sessions, b05); task calibration with a second response to the distractor (reliable person-level estimates in under 100 trials; b04); mixed design (b11).
- Mixed: chronic exercise reduced conflict in active adults (partial eta2 .081, N=64); orienting differed but likely from a ceiling effect; acute exercise cut alerting but not other scores (a22, second-hand).
- Not established: working memory capacity does not predict other executive tasks in LLMs (a18). No LLM-side training intervention was tested on the ANT.

## 6. Language models

**What was tested.** Only the executive half. No LLM run of the full ANT, of alerting (warning cue) or of orienting (valid vs invalid cue) was found (K18, K25). Searches were limited and arXiv API rate limiting cut the last ones.

**Text LLMs, flanker (de Langis 2025, a18).** Open Gemma-2, Llama-3.1, Qwen2 at 7B-72B. Incongruent accuracy 40-60% vs human 93-96%. They beat humans on working-memory span (tested at 15 and 50 digits against human 5-7) but not on control. Working-memory capacity did not predict other tasks. With reasoning: Llama-3.1-8B incongruent .471 to .910 (congruent .944 to .977); Qwen2-32B .638 to .985 (congruent .917 to .994). Chains were hundreds to thousands of tokens, equal on congruent and incongruent trials (d09). Reasoning did not help much on WCST or spans; chains often hit the 30,000 token cap (d10). The gain was not compared with a matched-token baseline.

**Frontier LLMs, Stroop (Patel, Wang, Fan 2026, a16, b23).** GPT-4o and Claude 3.5 Sonnet saw word lists as images. 30 trials per list length (1, 5, 10, 20, 40), accuracy only, manual scoring. Incongruent colour naming: GPT-4o 91%, 57%, 22%, 15% at 5, 10, 20, 40 words; Claude 76% at 20 and 24% at 40. Congruent about 99% at 20; 89% (GPT-4o) and 92% (Claude) at 40. Mixed lists: GPT-4o 100% at 1, 99% at 5, 72% at 10, 52% at 20. Word reading stayed near perfect, so it is not a vision failure. No adaptation. The supplement (GPT-5, Claude Opus 4.1, Gemini 2.5 Pro) used n=5 per model, too few to claim anything. The PsyPost press piece quotes 1% and 10% figures; those match mixed-list incongruent trials, not pure lists, and should not be cited as pure Stroop (a17). The authors argue that code or chain-of-thought workarounds do not count as executive control.

**VLMs.** 47 VLMs across 4,410 tasks (Wang 2025): 0.852 congruent vs 0.567 incongruent. Easy designs: Stroop-colour 0.968 vs 0.931 (p=0.153), flanker-letter 0.873 vs 0.860 (ns), word overlay 0.977 vs 0.813 (p=5e-13). Squared designs: Stroop 0.591 vs 0.366; word overlay 0.719 vs 0.265. Larger models fall below chance on the hardest incongruent trials; small models sit at chance. "Increasing computation" in the title means parameter count, not test-time tokens (critique). Teker 2026: CLIP word 97.8% vs ink about 20%; SigLIP-2 100% vs 5-6%; 23,338 images 99.5% vs 15.9%. Prompt wording moved ink accuracy 24% to 97%; "ignore the written word" was worse (31.1%) than a short prompt (60.0%). Contrast and font size also moved results (word match 87.8% high contrast vs 67.8% low). Zhao 2026 (embedded Stroop, 16 MLLMs): exact colour accuracy 6.3%, coarse 38.4%, hallucination rate 21.6%; conditional rate 51.9% [35.4, 66.8]; GPT-4o 47.0, GPT-5.2 25.0, Gemini-3-Flash 14.0, Qwen3-VL-Plus 53.0. An adversarial-aware prompt cut it by up to 91% (best case). Hu 2025: 12 of 13 VLMs show conflict adaptation.

**Text mechanism (Hu 2026).** Six of seven models show strong congruency effects. Gemma-2-2B accuracy is 100%, so the cost sits in probability (0.9644 vs 0.5676, CI [0.3529, 0.4407]). Wang 2026 (lexical override): interference is positive in all 11 open settings; slope 0.086 (p<1e-9).

**Distractors.** GSM-IC: fewer than 30% solved consistently (code-davinci-002, text-davinci-003). Self-consistency with 20 samples: +11 points micro; best macro 45%. An ignore instruction helped older models. S2A on LLaMA-2-70B: factuality 62.8% to 80.3%, GSM-IC +12 and +10; instructed prompting gave no consistent gain (54.7 vs 56.3 and 54.7 vs 51.7). Lost in the middle: mid-position accuracy can fall over 20 points; in 20- and 30-document settings it falls below closed-book for GPT-3.5-Turbo (closed-book 56.1%, oracle 88.3%).

**Other control tests.** A-not-B in in-context learning: drops up to 83.3%; larger models average an 8.7% drop at 25 shots vs 20.8% for smaller (c20). IDPR: 1.02 point gain from gating at 8.2% routing (c21). Semantic deception: R1 fell from 96% (level 1) to 40% (4b) while o1 held 94%; R1 answered the sentence instead of the calculation 10% of the time (d11). GPT-3 on cognitive-psychology tasks: 6 of 12 vignettes correct, all CRT items intuitive-wrong (c23).

**What changed it, by how much.**
1. Reasoning tokens: flanker gap closed (incongruent accuracy +0.44 and +0.35 in the two cited models), at hundreds to thousands of tokens per item.
2. Prompt wording: up to 73 points swing (24% to 97%) on a VLM.
3. Model size: helps, but large models can go below chance on the hardest trials.
4. Rewrite-then-answer (S2A): +10 to +12 points on GSM-IC, +17.5 on factuality; extra generation uncounted.
5. Instruction to ignore: no consistent effect; sometimes harmful.
6. Self-consistency: +11 points micro at 20x calls.

**Limits.** Most numbers are single studies, accuracy only, 30 trials per cell, no confidence intervals (Patel). Prompt wording effects may exceed model differences, so many "deficits" may be wording artefacts. Reasoning gains were not tested at equal tokens.

## 7. What our agent should take

Relevance is background only. Nothing from this subfield is established as a scaffold element. Each item gives schema part, status and evidence ids.

### Add now (established)

None of these changes the schema's states. They are design notes for measurement and restate guardrails we already hold.

1. **Measure with many trials and paired comparisons, never between-model difference scores.** Part: G7 (pay for itself; bench design). [E] K04, K05. Evidence a02, b01, b02, b04, b09, d02.
2. **Test a scaffold on several conflict tasks, not one.** Flanker cost and Stroop cost share little (r=.14). Part: G7, bench design. [E] K06. Evidence b02.
3. **Report results over prompt permutations, never one prompt.** Part: G7, supports S1's existing line that wording moves accuracy. [E] K19 for the principle; the size of the effect on text LLMs is [S]. Evidence c07, d12, c23.
4. **Distractors hurt, and the instruction "ignore it" is not a fix.** Part: S1 input hygiene (already in the schema; this supports its existing harm claim). [E] K15. Evidence c15, c16, c19, c24, d08. The remedy (a filter or rewrite step) stays [S].
5. **Alerting, orienting and conflict are separate; a "monitor" operator should not be tied to one network.** Part: none (design note). [E] K01-K03. Evidence a01, b07, a04, d05.

### Test first (not established)

6. **Filter-then-answer (S2A rewrite) at equal total tokens on a current model.** Part: S1 input hygiene / filter. [S] K16, K22. Evidence c17, d06, d07, d08. +10 to +12 points on an old 70B model; rewrite cost never counted; instruction baseline inconsistent.
7. **A separate "target only" verify pass vs plain prompting on long distractor lists.** Part: S8 VERIFY, G3. [S] K10. Evidence a16, b23. Collapse 91% to 15% with length seen in two frontier models only.
8. **Short reasoning step vs reasoning-token budget on conflict items.** Part: G11, G12. [S] K11, K20. Evidence a18, d09, d10, d11. Gain comes at high cost; the R1 vs o1 split shows it is not uniform.
9. **Prompt-phrasing sweep on one text Stroop list; report the range.** Part: G7 measurement; S1. [S] K13, K24. Evidence c07, d12, d16.
10. **Keep rule lists short.** Part: S1 / S2. [S] K24. Evidence d16. Five clauses vs two cut incongruent probability by 0.3039 in a 2B model.
11. **Cue-validity probe (valid vs invalid hint, 80/20).** Part: S0 / S1. [S] K25 is a negative search result; no LLM evidence. Evidence d17, d18.
12. **Confidence-gated slow path.** Part: G1, G12. [S] K17. Evidence c21. About +1 point; likely not worth the complexity. Verbal confidence is already in section 4b.
13. **Raise checking after a conflict vs a fixed schedule.** Part: G1. [S] K21. Evidence d14, c04. G1 already says doubt on signal; the test is whether "attempts disagree" works as the conflict monitor.

## 8. Concrete tests on our bench

All arms at equal total tokens (prompt plus all generated). Report the mean over 10 prompt phrasings with the range.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Text Stroop lists of 5, 10, 20, 40 items; 30+ trials per cell | plain; "target only" verify pass; short reasoning step | Incongruent accuracy, tokens | Verify beats plain at 20-40 items; long reasoning wins on accuracy but loses at equal tokens |
| T2 | GSM-IC style math with one irrelevant sentence, plus long-context QA | plain; "ignore irrelevant" instruction; filter-then-answer (rewrite counted); 3-5 sample vote | Accuracy, macro and micro | Filter beats plain by 3-8 points at equal tokens; instruction about equal to plain |
| T3 | One text Stroop item, 10 phrasings | wording variants | Accuracy range | Range over 20 points; any scaffold gain below the range is not trustworthy |
| T4 | Items with a hint right 80% and wrong 20% | no hint; hint; hint plus check-the-hint pass | Accuracy on valid and invalid items; invalid-cue cost | Shows how far the model follows a cue; check step cuts the cost |
| T5 | Flanker-style text items (distractor characters around target), 30 permutations | plain; 1-line reasoning; long reasoning | Incongruent accuracy per 1,000 tokens | Short reasoning gives most of the gain |
| T6 | Rule lists of 2 vs 5 clauses with a conflicting default | plain; rule restated last | Incongruent accuracy | 5 clauses hurt incongruent only; restating helps |
| T7 | Sequential conflict items (II vs CI order) | fixed check schedule; conflict-triggered checks | Accuracy on II vs CI; tokens | Tests whether a monitor gives adaptation at no extra cost |
| T8 | A-not-B: few-shot all "A", then a switch | plain; separate "does the pattern still hold" check | Accuracy after switch | Larger models drop less; check tests use of a G1 signal |

## 9. What does not transfer, and why

- **Millisecond RTs.** An LLM has no human-style reaction time. Only accuracy, probability and tokens exist. Absolute ANT values (47/51/84 ms) have no counterpart.
- **Alerting and tonic arousal.** Norepinephrine-based readiness has no analogue in a stateless forward pass. A warm-up prefix is a prompt, not an arousal state, and no test shows it helps.
- **Orienting as spatial selection.** The nearest analogue is position in context (lost in the middle). That is a retrieval effect, not a cue-driven shift.
- **Brain anatomy and drugs.** Locus coeruleus, ACC, guanfacine, clonidine and exercise findings are human-only.
- **Development, ADHD, heritability, culture.** Not applicable to a scaffold.
- **Subtraction scores.** Weak even in humans; do not build an "attention score" for an agent from them.
- **"Deficient executive control" in LLMs.** The Stroop authors say chain-of-thought is a workaround, not executive control. For our agent the workaround is the point, so the human claim does not set our design.
- **Conflict adaptation.** Seen in 12 of 13 VLMs on log probability; absent in frontier-model accuracy. Not a settled property.
- **Mixed-list percentages.** PsyPost's 1% and 10% belong to mixed lists.

## 10. Open questions

- Does an explicit verify pass beat plain prompting on long distractor lists at equal tokens? No study matches tokens.
- How much of the LLM Stroop collapse is wording vs capacity? No wording sweep for text LLMs exists.
- Can alerting (warning cue) or orienting (valid vs invalid cue) be measured on an LLM at all? None found.
- Do reasoning models close the long-list Stroop gap? The Patel supplement used n=5 per model; no larger test found.
- Does S2A keep its gain once rewrite tokens are counted, and on frontier models?
- What are the exact Rueda 2004 child scores? Closed access, unread.
- Do LLM conflict scores predict agent task accuracy? Nothing found.
- Is the cost-benefit trade (congruent margin up, incongruent down) visible in black-box confidence outputs?
- Does the ANT-R full text change where a "monitor" operator belongs? Only the abstract was read.
- How many trials give a stable LLM conflict score? The human anchor is about 420 for r=.8.
- Does a "hard item ahead" prompt, the alerting analogue, make models more distractible, as alerting did at the 400 ms interval in humans?

## 11. Sources

[V] opened and read this session; [M] snippet, abstract or second-hand only.

- [V] Fan et al. (2002) ANT. https://doi.org/10.1162/089892902317361886 (full text via https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.474.442)
- [V] Fan, Wu, Fossella, Posner (2001) heritability. https://bmcneurosci.biomedcentral.com/articles/10.1186/1471-2202-2-14
- [V] Petersen and Posner (2012). https://pmc.ncbi.nlm.nih.gov/articles/PMC3413263/
- [V] Fan et al. (2009) ANT-R. https://pmc.ncbi.nlm.nih.gov/articles/PMC2674119/ ; [M] abstract https://pubmed.ncbi.nlm.nih.gov/19269079
- [M] Rueda et al. (2004). https://doi.org/10.1016/j.neuropsychologia.2003.12.012 (child numbers via restatements; closed access)
- [V] Wang et al. (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC3940671/
- [V] Wang et al. (2015) mixed design. https://pmc.ncbi.nlm.nih.gov/articles/PMC4440527
- [V] Dalhousie battery paper quoting MacLeod 2010 (2016). https://www.frontiersin.org/articles/10.3389/fpsyg.2016.00823/full
- [M] MacLeod et al. (2010). https://doi.org/10.1037/a0019803
- [V] Perez et al. (2014) exercise. https://doi.org/10.1371/journal.pone.0101478
- [V] Posner (2012) attention and consciousness. https://doi.org/10.3389/fpsyg.2012.00064
- [V] ANTI platform page. https://www.ugr.es/~anti/Presentation.html
- [V] ANT database and ADHD (2020). https://www.frontiersin.org/articles/10.3389/fpsyg.2020.00388/full
- [M] Eriksen and Eriksen (1974), Posner and Petersen (1990), Corbetta and Shulman (2002), Dosenbach (2006-2008), Callejas (2004), Ishigami and Klein (2009, 2010), Johnson (2008), Huertas, Hillman, Boucard: known only through the papers above.
- [V] Hedge, Powell, Sumner (2018). https://link.springer.com/content/pdf/10.3758/s13428-017-0935-1.pdf
- [V] Kucina et al. (2023). https://www.nature.com/articles/s41467-023-37777-2
- [V] Ishigami and Klein (2011). https://www.frontiersin.org/articles/10.3389/fnagi.2011.00017/pdf
- [V] McConnell and Shore (2011). https://link.springer.com/content/pdf/10.3758/s13414-010-0085-3.pdf
- [V] Habekost, Petersen, Vangkilde (2014). https://link.springer.com/content/pdf/10.3758/s13428-013-0341-2.pdf
- [V] Klein, Good, Christie (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC10889552/
- [V] Luna et al. (2023) ANTI-Vea platform. https://pmc.ncbi.nlm.nih.gov/articles/PMC10532513/
- [V] Luna et al. (2022) vigilance and executive decrement. https://pmc.ncbi.nlm.nih.gov/articles/PMC9568446/
- [V] Adolescent ANTI-V (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8073862/
- [M] ADHD meta-analysis (2023). https://doi.org/10.3389/fnins.2023.1246490
- [M] Bilingual ANT meta-analysis (2020). https://doi.org/10.1007/s41809-020-00068-z
- [V] Patel, Wang, Fan (2026) PNAS Nexus. https://academic.oup.com/pnasnexus/article/doi/10.1093/pnasnexus/pgag149/8698838 and https://doi.org/10.1093/pnasnexus/pgag002 ; preprint https://www.biorxiv.org/content/10.1101/2025.01.22.634394 (same study)
- [V] PsyPost (2026). https://www.psypost.org/advanced-ai-models-suffer-a-near-total-collapse-on-classic-psychology-test-as-cognitive-demands-increase/
- [V] de Langis et al. (2025). https://arxiv.org/abs/2504.02789
- [V] Wang et al. (2025/2026) VLM conflict. https://arxiv.org/abs/2505.18969
- [V] Hu (2025) conflict adaptation in VLMs. https://arxiv.org/abs/2510.24804
- [V] Teker et al. (2026) feature competition. https://arxiv.org/abs/2610.12650
- [V] Hu et al. (2026) verbal conflict task. https://arxiv.org/abs/2608.11510
- [V] Zhao et al. (2026) WCIT. https://arxiv.org/abs/2511.13400
- [V] Wang (2026) lexical override. https://arxiv.org/abs/2606.07555
- [V] Shi et al. (2023) GSM-IC. https://arxiv.org/abs/2302.00093
- [V] Weston and Sukhbaatar (2023) S2A. https://arxiv.org/abs/2311.11829
- [V] Liu et al. (2023) Lost in the middle. https://arxiv.org/abs/2307.03172
- [V] Han et al. (2024) A-not-B. https://arxiv.org/abs/2409.15454
- [V] He and Feng (2026) IDPR. https://arxiv.org/abs/2606.06745
- [V] Bandara et al. (2026) governance model (framing only). https://arxiv.org/abs/2604.25684
- [V] Binz and Schulz (2023). https://arxiv.org/abs/2206.14576
- [V] Ortu et al. (2025/2026). https://arxiv.org/abs/2507.13868
- [V] De Leeuw et al. (2026) semantic deception. https://arxiv.org/abs/2512.20812
- [M] Cohen, Dunbar, McClelland (1990). https://doi.org/10.1037/0033-295X.97.3.332
- [M] Botvinick et al. (2001). https://doi.org/10.1037/0033-295X.108.3.624
- [M] Search record for LLM cueing/ANT (negative). https://export.arxiv.org/api/query

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 13 established claims: 9 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A07.05-K03** (reworded: the sources support less). McConnell & Shore verify that executive scores differ across cue types (t>3.3) but they and Fan 2002 still find between-network scores uncorrelated; sources show interactions and mixing, not that independence is an artefact (Wang 2014 and 2015 are one lab). Corrected claim: The subtraction score is a mixed measure: executive (flanker) scores differ across the four cue types (McConnell & Shore 2011), and cue x flanker interactions mean the three networks are not fully separable, which calls the independence claim into question even though between-network score correlations stay near zero.
- **A07.05-K06** (reworded: the sources support less). Hedge reports flanker-Stroop RT cost rho=.14 (disattenuated .25, N~100) but says low reliability attenuates correlations and only that some relations are 'not consistent with a single underlying construct'; it does not conclude executive conflict is not one construct. Corrected claim: Flanker and Stroop RT costs correlate weakly across tasks (rho=.14, disattenuated .25; Hedge et al. 2018), which is partly due to low reliability of RT-cost scores and is not evidence by itself that executive conflict is not a single construct.
- **A07.05-K08** (reworded: the sources support less). ADHD-minus-control 13/13/2 ms verified, and Klein 2024 says alerting reaches near-adult level by age 12 and executive scores keep improving in childhood; but orienting 'mature by 10-12' is not supported (Rueda 2004: orienting unchanged age 6-9, conflict stable after age 7; Klein: orienting depends on cue informativeness; adolescent study: all networks keep developing to 19). Corrected claim: Development: alerting reaches near-adult level by about age 12 (Klein 2024) and keeps changing past age 10 (Rueda 2004); orienting trajectories depend on cue informativeness and are unclear; executive conflict scores improve with age in childhood per the lifespan meta-analysis (Rueda 2004 found them stable after age 7), and all three networks still develop through adolescence. In children, ADHD minus control differences are small: alerting 13 ms, executive 13 ms, orienting about 0 (2 ms, CrI -5 to 10).
- **A07.05-K16** (now contested: a source does not say this). 62.8->80.3 factuality and GSM-IC +12/+10 verified in Weston & Sukhbaatar, but the closing clause is backwards: instructed prompting gave no consistent gain over baseline (GSM-IC 54.7 vs 56.3 and 54.7 vs 51.7; factuality 71.7%), so S2A beat instructed prompting clearly (68.3/61.3 vs 54.7; 80.3 vs 71.7); Shi et al. found the ignore-instruction helped other models (code-davinci-002).
