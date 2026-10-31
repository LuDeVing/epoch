# Framing and reframing: deep document

*Subfield E05.04. Key works: Dorst 2015 (Frame Innovation), Schon 1983. Schema link: O8 (reframe the goal), with G1, G4, S1, S6. Evidence: evidence_a-d.jsonl (ids a01-d20), claims.jsonl (K01-K29), critique.md. Read before use: only K07, K21 and K22 reach "established". Every other claim rests on one source or is contested. The founding books were NOT opened, so no numbers from them are quoted.*

## 1. What it is

A frame is a way of seeing a problem. It says what counts as the problem, what counts as a solution, and which facts matter. Reframing means swapping that view for another one so that the problem itself changes.

Dorst gives the standard form of a frame: "If the problem of X is approached as if Y, then the direction of solutions could be Z" (a04, as restated by Shin 2025). The slow-elevator case shows it. The complaint is "elevators are too slow". Approached as a waiting-experience problem, the fix becomes a better waiting area, not a faster lift (a04).

Four things get called "reframing" in the literature. They are not the same, and the evidence differs for each:

1. **Goal reframing (Dorst sense).** The goal or the problem's nature changes. This is O8. Almost no LLM evidence tests it with a measured outcome other than Shin 2025.
2. **Representation change (insight sense).** The solver drops a default reading, as in matchstick arithmetic or lateral puzzles. Close to O6 and O4. Human studies plus BRAINTEASER-style LLM benchmarks.
3. **Abstraction or rephrase (prompt sense).** The model restates the question or asks for the principle first (step-back, Rephrase and Respond). Strictly this is O2 or S1, not O8. It has the largest benchmark numbers.
4. **Clinical reframing.** A negative thought is replaced by a more helpful one (Sharma 2023; Qi 2025). Different construct. It only shows how LLMs behave when asked to reframe.

The central finding for our agent: cheap, targeted rewrites help on benchmarks with a known answer. The one large controlled test with real designers on open problems found no gain from LLM help (K19, K01). The gap between those two result types is the main thing to resolve.

## 2. History and theories in depth

Entries a20-a31 were not opened. They are described from the secondary descriptions in opened papers (Shin 2025, Sood 2026, Wadinambiarachchi 2024, Spiridonov 2026) and from memory of the literature. Treat them as context, not as evidence.

**Rittel and Webber (1973), wicked problems [M].** Wicked problems have no definitive formulation. The way a problem is stated already shapes the solution. This is the root of the idea that problem-setting is work (a30).

**Lawson (1979) [M].** Scientists and architects on a block-arrangement task. Scientists tended to learn the hidden rule (problem-focused). Architects tended to try solutions and learn the problem from failed ones (solution-focused). Basis for "designers learn the problem by proposing solutions". Small samples, one lab task, confounded with training (a27).

**Schon (1979, 1983; with Rein 1994) [M].** Practice is a reflective conversation with the situation. The practitioner "sets" the problem by naming what to attend to. The situation "talks back". Surprise triggers reflection-in-action and a reframe. A frame is tested by moves, then the practitioner asks if the consequences are acceptable (a20). Generative metaphor: urban blight seen as a disease to cut out versus a natural community to keep. Same facts, opposite fixes (a21). Frame reflection: policy disputes persist because each side holds a different frame, so progress needs reflection on the frames, not argument inside one (a22). All are case-based essays with no controlled test.

**Kaplan and Simon (1990) [M].** Insight on the mutilated checkerboard needs search in the space of problem representations, not only the space of moves. Making the parity cue visible shortens solving (a28).

**Knoblich, Ohlsson, Haider, Rhenius (1999) [M].** Representational change theory. Matchstick arithmetic is hard for two reasons: tight constraints on what may change, and familiar chunks that must be broken. Turning XI = III + III into VI = III + III is harder than IV = III + III into VI = III + II (a29, as restated in a19). Sample sizes and solution rates not checked.

**Dorst and Cross (2001) [V, via a third-party copy].** Nine experienced industrial designers, 2.5 hours each, think-aloud, one brief (litter disposal on a Dutch train). Five design teachers rated the nine concepts on a 1-10 scale, inter-rater alpha 0.71. Creativity vs total judgement r = 0.32 (reported to rise to 0.8 without one design). The creative step was a "bridge" that fixes a problem and a solution together. Problem space and solution space co-evolve (b04, d18). No control group, so no causal claim that reframing causes creativity. Figures need a check against the journal PDF.

**Valkenburg and Dorst (1998), Paton and Dorst (2011) [M].** Applied Schon's moves (naming, framing, moving, reflecting) to coded recordings of student teams. Paton and Dorst: professional reframing happens in conversation with the client, through themes (a25, a26). Qualitative, small samples.

**Dorst (2011, 2015) [M].** The core of design is abduction. Given a desired value, the designer must find both a "what" and a "how". Frames bridge that gap (a23). The 2015 book gives a nine-step process: archaeology, paradox, context, field, themes, frame, futures, transformation, integration (c22). Shin 2025 implements it as: apparent problems, ineffective solutions, paradoxical problems, stakeholders (current, potential, their views), themes, frames, assessment (a04). No controlled study of the model's benefit has been opened (K20).

**Roozenburg (2002), Kolko (2010) [M].** Design reasoning as abduction and sensemaking (a31).

**Computational models [M].** Maher and Poon (1996) modelled co-evolution with a genetic-algorithm style search. Gero and Kannengiesser (2014) FBS ontology: the most radical reformulation changes the function space (c24). Not opened.

**Fixation, the opposite of reframing.** Jansson and Smith (1991): people shown an example made about as many designs as controls but copied more of its features (b07, second-hand). Sio, Kotovsky and Cagan (2015) is the standard meta-analysis. Only its existence was confirmed (b05). Youmans and Arciszewski (2014) split fixation into unconscious adherence, conscious blocks and intentional resistance, and into concept-based and knowledge-based types (b06, abstract only).

**Insight theory.** Representational change theory says solvers relax constraints and decompose chunks. Two opened human studies refine it: reassembling is the hard step (a19), and insight problems load working memory storage (a18).

## 3. Core findings with exact numbers

Status key: E = established (2+ independent sources), S = single source, C = contested, H = human-only, O = old models only. "(table read)" means the numbers came from text-extracted tables and need a check before quoting.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LLM help (GPT-4o, 3 modes incl. Dorst 9-step) gave no gain in novelty or usefulness of expert-rated problem frames | 456 recruited, 280 kept, 218 LLM users, about 62 manual, 4 arms, 3 design problems, 15 expert raters; Mann-Whitney and Kruskal-Wallis, no significant difference. Sized for medium effects only (220 and 280 needed at 95% power) | Shin 2025 (a01, b01, c01, d20) | S |
| The null rules out only effects above about 0.45 SD | SE of d = 0.144; detectable d = 0.40 at 80% power, 0.52 at 95%; TOST power 0.34 at +-0.3 SD, 0.74 at +-0.4, 0.93 at +-0.5. Group sizes inferred, no raw data | this agent's calculation (d19, K25) | S |
| Felt help is not real help | CSI direct 64.28 (SD 18.90), structured 64.85 (20.00), free-form 61.01 (17.19), all in the "good" band 50-90; 34% said LLM frames were not novel enough to build on; 93 of 218 reported trouble (31 not novel, 14 repetitive, 12 not useful) | Shin 2025 (a02, a03, b03, c03) | S |
| Rigid Dorst scaffold costs time, no quality gain | Minutes per 2 frames: manual 23.25 (SD 14.73), direct 21.82, structured 28.35 (SD 18.00), free-form 20.78. All but one structured user regenerated everything at least once; apparent-problem step regenerated by 39, stakeholder step by 25 | Shin 2025 (a03, c02) | S |
| Expertise moderates who benefits | Experts (3+ of 5 quiz items) vs novices on LLM frames: novelty +12.54% (p=0.01); free-form +20.84% (p=0.06, ns); agency +15.69% in structured arm (p=0.02); no usefulness gap. Post hoc split | Shin 2025 (a02, b02, c04) | C |
| Dorst-step prompt gave more "interesting" research answers | 29/189 vs 17/189 (direct) vs 17/189 (all content); top-3 slots 11 of 21 (52%) vs 7 (33%) vs 3 (14%); 7 students, no statistics; only steps 1-3 and 6 used | Sood 2026 (c05-c07) | S |
| Step-back (ask for principle first) lifts science QA | PaLM-2L physics 66.4 to 73.2, chem 70.9 to 81.8 (CoT 65.0, 75.3). GPT-4 physics 69.4 to 84.5 (CoT 82.9), chem 80.9 to 85.6 (CoT 85.3). Llama2-70B 51.9 to 64.8 and 55.7 to 66.7. TimeQA 41.5 to 66.0 (with RAG 68.7). StrategyQA 82.8 to 82.7 (no change alone) | Zheng 2023 (a05, a06, c08) | C |
| Step-back fixes and breaks | Physics: fixes 20.5% of baseline errors, introduces 11.9%; over 90% of its remaining errors are in the reasoning step. TimeQA+RAG fixes 39.9%, breaks 5.6%. StrategyQA fixes 15.4%, breaks 6.1% | Zheng 2023 (a07, c09) | S |
| Step-back below zero-shot CoT on a 2026 model | Qwen3.5-27B, 7-benchmark average: Step-Back 56.71, Re-Reading 58.36, zero-shot CoT 59.79, PromptWizard 67.99, spurious prompt 73.24 (table read) | Batorski 2026 (d11) | S |
| Model-written rephrase lifts GPT-4 on ambiguous tasks | Average 64.95 to 89.77 over 10 tasks. Day 54.29 to 93.33, Month 58.10 to 83.96, Year 57.14 to 89.52, last-letter-4 21.36 to 86.82, coin flip 74.55 to 99.09; CSQA 84.09 to 85.45 (ceiling). Weaker models gain little | Deng 2023 (a08, b09, b10, c10, c11) | S |
| Problem rewrite by the model before solving: small gain | text-davinci-003 CoT average 62.6 to 63.4-64.0 (+0.8 to +1.4); MultiArith CoT 90.8 to 88.5-90.2 (loss) | Zheng 2023 Self-Polish (b11) | S, O |
| Hand-reframed instructions help GPT-3 | 12 tasks; few-shot +12.5% (GPT-3 series), +6.7% (GPT-2 series); 12.5% is the average few-shot gain; separately ROUGE-L 44 to 58; corrects 24% of errors, causes 4%, retains 31% | Mishra 2022 (a09, b14, c12, c13) | S, O |
| Surface format alone moves accuracy hugely | Up to 76 points (LLaMA-2-13B); about 10 points on average across 50+ tasks; not removed by size, shots or instruction tuning | Sclar 2024 (b15) | S |
| Meaning-preserving rename costs little; setting change costs much | 1,051 Putnam problems, 5,255 variants, 18 models. Median drop about 2.1 points (surface) vs 10.3 (kernel/setting). o3 51.5 to 38.6; gemini-2.5-pro 78.4 to 63.5 | Hao 2026 (d12) | S |
| Rewrite to formal maths helps reasoning models on hard puzzles | 30 items: o3 56.7 to 73.3 (p=0.023), R1 50.0 to 63.3 (p=0.043). One offline o3 rewrite, not equal-token | Han 2025 (d13) | S |
| Content hint beats style rule on brainteasers | Math set, CoT / "Math prompt" / hint: o3 79.6/79.6/82.8; R1 66.8/70.2/72.4; Gemini-2.5-flash 66.0/65.2/69.2 | Han 2025 (d13) | S |
| Lateral puzzles are hard and fragile to rewording | BRAINTEASER 1,119 items (abstract: 1,100): ChatGPT 53% and 63% vs random 25%, human 92%; fails 45% and 61% of originals or variants it solves in the context-rewritten form | Jiang 2023 (a11, b17, c15) | S, O |
| Restart with compacted facts helps in puzzles | 5 puzzles, K=5 rounds, M=3 facts: wins 2/3 to 4/1; questions 28.6 to 22.6; K=10, M=6 worse (3/2). No statistics | Li 2025 (b16, c14, c27) | S |
| Repeating all known facts recovers part of the multi-turn loss | 200,000+ conversations, six tasks, about 15 models; average drop 39%; repeating facts (SNOWBALL) closes about 15-20% of the gap (GPT-4o, 4o-mini, four tasks) | Laban 2025 (d06) | S |
| Self-revision without feedback does not help | GPT-3.5 CSQA 75.8 to 38.1 to 41.8 (columns are 1, 3, 5 model calls); GSM8K 75.9 to 75.1 to 74.7. GPT-4 GSM8K 95.5 to 91.5 to 89.0. Oracle label GPT-3.5 GSM8K 84.3 | Huang 2024 (b18) | E |
| Finding the error is the bottleneck | GPT-4 mistake location 39.80 / 52.87 / 43.40 (three prompts, 2,186 traces). True location: +5 to +44 points; random location: 0 to -16 (column mapping unclear) | Tyen 2024 (d08); Kamoi 2024 survey (d09) | E |
| Reflection after the first answer is mostly confirmation | 8 reasoning models, 5 maths sets: over 90% of reflections confirm; corrective (wrong to right) mostly under 2%; reflection takes 16.8-47.8% of tokens for +1.4-3.5% accuracy | Kang 2025 (d01) | E |
| First step locks in the result | Wrong first step lowers average accuracy about 40% (43% on hard questions). DS-R1-Qwen-7B 94.8 vs 28.5; 1.5B 95.4 vs 64.4; 32B 100.0 vs 85.8 | Liao 2025 (d02) | E |
| Prompted anchors pull LLMs; simple fixes fail | 62 questions x 3 hints x 30 runs x 3 models; only 11 of 162 differences opposed the anchor. 22-61% of questions anchored across models; GPT-4o 27.3%, DeepSeek-R1 25.0%, Qwen3-235B thinking 22.0%, Qwen2.5-0.5B 60.5% | Lou 2024 (d03); Huang 2025 (d04) | E |
| Too many thought switches cost accuracy | Wrong answers use 225% more tokens and 418% more switches; penalty raised AIME24 pass@1 38.3 to 44.1 (QwQ-32B) | Wang 2025 (d07) | S |
| Agreement is not correctness | 94 eligible questions: 62 high accuracy, 21 answer-consistent but wrong; commitment prompt cut run variability 28% vs filler, no accuracy gain | Mehta 2026 (d05) | S |
| Strategy-level variety beats wording variety | 1 to 4 distinct approaches: best-of-N 63.8 to 65.6; OlympiadBench avg@3 67.56 (approach-seeking data) vs 55.51 (format-only). Self-Contrast +7.2% on maths vs -0.51% for plain self-reflection | Lee 2026 (d14); Zhang 2024 (d15) | C |
| Longer reasoning can hurt reframing-like tasks | Clinical: GPT-3.5 + DoT 0.956 vs CoT 0.395; o1 reframe ROUGE 0.126 vs GPT-3.5 0.287. GPT-5 high vs minimal effort: reading of "some" -20.6, "or" -18.8 points | Qi 2025 (b19, c19, c20); Kou 2026 (d17); Gema 2025 (d16) | C |
| Task-level method composition beats CoT cheaply | Self-Discover T4D 30 to 69 (PaLM-2L), 51 to 85 (GPT-4); BBH 67 vs 60 (PaLM-2L), 81 vs 75 (GPT-4); better on 21 of 25 tasks; 10-40x less compute than self-consistency. MATH gain only +1.5 to +3 | Zhou 2024 (b13, c17) | S |
| LLMs show a wording (framing) effect | GPT-4 admit rate 0.375 vs 0.780 by wording (gap -0.405). Counterfactual debiasing widened it to -0.570 (0.370 vs 0.940); self-help prompt narrowed it to -0.010. GPT-3.5 baseline has the opposite sign (+0.165) | Echterhoff 2024 (c18) | S |
| Generative AI images raise design fixation | N=60; fixation score GenAI +0.32 (89% CI 0.11-0.55, BF 124), image search +0.27 (BF 42.5) vs no support | Wadinambiarachchi 2024 (a14, b08) | S, H |
| AI-assisted ideation: clearer framing, less novelty | 32 students, within-subject: problem framing AI 4.64 vs human 2.94 (dz 2.48); innovation human 4.66 vs AI 3.40 (dz 2.69). "Framing" is a clarity rubric | PLOS ONE 2026 (b25) | S |
| Insight is abrupt; hints help | 61 people; 34% solved alone, +11% after hint; change point near 90% of solving time | Graf 2023 (a17, b21) | S, H |
| Reassembly is harder than decomposition | Chinese characters, 60 students: decomposition about 98.4% vs reorganisation about 62.2%; F(1,24)=205.23 on accuracy | Front. Psychol. 2017 (a19) | S, H |
| Physical-interaction boost of matchstick insight did not replicate | 3 experiments, n=54, 45, 45; movement interfered with constraint relaxation; only a VR condition showed an effect (about 92%, +6 points) | Spiridonov 2026 (b22) | S, H |
| Thinking in opposites raised spatial insight success | 3 studies by one group, higher success than controls in every arm; no pooled effect size; benefit in small groups | Bianchi and Branchini 2023 (b24) | S, H |
| Clinical reframes: empathy preferred | 2,067 users: empathic reframes preferred 39.7% vs 25.5% (p<1e-5); positive 29.6% vs 38.3%; 32 of 5,760 flagged (0.56%) | Sharma 2023 (a10, b20, c21) | S |
| Dorst-and-Cross base is qualitative | 9 designers, one brief, alpha 0.71, r = 0.32; no control | d18, b04 | S, H |

## 4. Mechanisms and models

Each mechanism is written so it can be coded. None of them is yet shown to help our agent.

**4.1 Frame as a template.** Store a frame as three slots: X (the problem as stated), Y (the lens), Z (the solution direction it implies). Shin 2025 used this template (a04). A reframe is a change in Y that changes Z. Code can check that the slots exist and that Z differs from the previous frame's Z.

**4.2 The nine-step process (Dorst).** Shin 2025 turned it into button-driven prompts: three destructuring steps (apparent problems, ineffective solutions, paradoxical problems), three stakeholder steps, then themes, frames, assessment. The interface reversed the order of the last two steps (a04). Result: the longest run time and no gain. Lesson: a full pipeline is not the unit to add. At most use one or two steps as a gated sub-step (K03).

**4.3 Step-back (abstraction).** Two calls. Call 1: "What are the principles or concepts behind this question?" Call 2: answer using the returned principles. The original used hand-written few-shot step-back exemplars per task (a05, c08). Treat as O2, not O8. Net effect = fixed errors minus broken errors (20.5% minus 11.9% on physics). Gate it and measure net.

**4.4 Rephrase and Respond.** One call: the model rewrites the question in its own words, then answers (one-step). Two-step version: a stronger model writes the rewrite, a weaker one answers (b10). Sits in S1. Gains concentrate on questions ambiguous as written, so part of the gain is repair of poor wording (a08).

**4.5 Compacted-facts restart.** After K=5 rounds, keep M=3 confirmed items, write them into the task text, and open a fresh chat (c27). Two parts work together. It drops the bad early context. It restates known facts, which large-scale data shows recovers part of the loss from early guessing (d06).

**4.6 Content-bearing reframe.** The reframe must supply a content change (a different representation or goal), not a style rule. A hint with the insight beat a "don't brute force" rule on checkable puzzles (d13). The formal-maths rewrite helped o3 and R1 on 30 items. Implementation: S6 asks the model for a changed statement of the goal, and code checks that it is not a paraphrase (for example, low overlap in the solution-direction slot Z).

**4.7 Strategy diversity.** Compare several self-made solving perspectives and review from where they disagree (Self-Contrast, d15). Candidate sets with distinct approaches help more than wording variants (d14). Implementation: S3 prompts for named, different strategies; code groups candidates by strategy label; disagreement between groups is a trigger candidate.

**4.8 Trigger logic.** Evidence points to: fire a reframe on a localised failure after sustained effort on one line. Do not fire on a generic re-check (d01), on run agreement (d05), or on the model's own doubt (d08, b18). Do not fire too often: switches cost accuracy (d07). This is the G1 and S6 interface. The cost of a false trigger in an O8 agent has not been measured.

**4.9 Anchoring control.** Prompted anchors pull models and "ignore the hint" does not remove the pull (d03, d04). Showing opposing anchors together helped in part. Implementation: fresh-context generation (already S3), and when frames must be compared, show them side by side instead of one after another.

**4.10 Noise control.** Surface changes move accuracy a lot (b15: up to 76 points on a small open model; d12: about 2 points median on Putnam variants for strong models). Unrelated prompts matched reframing prompts on one 2026 model (d11). Any claimed gain from reframe wording needs a paraphrase arm and a same-length unrelated-prompt arm.

## 5. What holds up

**Established (2+ independent sources).**
- Intrinsic self-revision without an outside signal does not help and can hurt (K07: Huang, Tyen, Kang, Kamoi). Scope: reasoning tasks without feedback.
- The first answer or first step dominates in reasoning models; late reflection adds little (K21: Liao, Kang).
- Prompted anchors pull LLMs, and ignore-the-hint or self-review do not fix it (K22: Lou, Huang).

**Replications and failures.**
- No replication of Shin 2025 exists. It is one study, a null. Its power covers medium effects only (d19).
- The physical-interaction insight boost failed conceptual replication (b22, three experiments, n=54, 45, 45). Human-only boundary.
- The chunk-level difficulty from Knoblich did not show up in new material; reassembly was the harder step (a19).
- Step-back has no independent replication in our evidence. On a 2026 model it fell below zero-shot CoT in one average (d11, table read).
- Echterhoff: a debiasing prompt widened the framing gap (-0.405 to -0.570). Do not assume prompts help.
- Sood 2026 (Dorst prompt wins, n=7) and Shin 2025 (no gain, N=280) point different ways. Sood used steps 1-3 and 6 and measured "interesting", not rated frame quality.

**Moderators.**
- Model capacity and task fit. Rephrase helped GPT-4 more than weaker models (b10). Qi found reasoning models gain nothing on clinical reframing, while a light task-fit prompt gave 0.956 (K11).
- Baseline level. Step-back gave no gain on StrategyQA (82.8 to 82.7). RaR gave +1.4 on CSQA (ceiling).
- Ambiguity of the question. RaR gains are largest where the question is poorly worded (a08).
- Reader expertise. Experts gained more novelty from LLM frames (+12.54%, contested).
- Task type. Cheap benchmark rewrites win; open design with human raters is null or mixed (K19).
- Reasoning length. Longer reasoning hurt on clinical reframing, distractor tasks and the reading of "some" and "or", but helps on hard maths. Task dependent (K11).

**Interventions that worked (with caveats).**
Step-back on science QA; rephrase on ambiguous questions; hand-rewritten itemised instructions on GPT-3 (old model); restart with compacted facts (5 puzzles); a hint carrying the insight (d13); formal rewrite of puzzles (30 items); comparing self-made solving perspectives (Self-Contrast); thinking in opposites on spatial insight (one group).

**Interventions that did not work.**
- LLM help for human frame quality (Shin, three modes).
- The full nine-step scaffold (more time, no gain).
- "Ignore the hint", chain of thought and thoughts-of-principles against anchoring (d03).
- Reflecting after a first answer (d01).
- A commitment prompt for accuracy (d05).
- A "don't brute force" style rule (d13).
- Few-shot examples on o1-preview; voting gave the steady gain (d10, medical QA, no step-back arm).
- More thinking on clinical reframes and pragmatic readings (d16, d17, b19).

**Gaps in the foundations.** Schon, Dorst 2011/2015, Rittel, Lawson, Kaplan and Simon, Knoblich 1999, Paton and Dorst, Valkenburg and Dorst and the Sio 2015 meta-analysis were not opened. Dorst and Cross 2001 came via a third-party copy. No effect sizes are quoted from these.

## 6. Language models

**How they behave.**
- Models are weak on frame-breaking puzzles. BRAINTEASER (ChatGPT, 2023): 53% and 63% vs human 92%; scores fall when puzzles are reworded or moved to a new context, which points to memorised answers (a11, b17). CresOWLve (2026): up to 17% drop between factual and creative questions across frontier models, abstract only (a13). No 2025-26 reasoning-model result on BRAINTEASER was found.
- Models are sensitive to wording. Format alone moved accuracy up to 76 points on a small open model (b15). GPT-4 admit rates split 0.375 vs 0.780 by wording (c18).
- Models anchor. Prompt hints pull GPT-4, 4o and 3.5; reasoning models less but not zero (22-61% of questions anchored; d04). Fixes failed.
- Models lock in early. A wrong first step cuts accuracy about 40% (d02). Over 90% of later reflections confirm the first answer (d01). Stable runs can be stably wrong (21 of 94, d05). Multi-turn: 39% average loss, with models leaning on their own early guesses (d06).
- Models cannot find their own errors. GPT-4 locates the mistake 39.8 to 52.9% of the time (d08). With an outside signal, correction works (+5 to +44 points); with a wrong location it hurts.
- Reasoning models may switch lines of thought too often: 418% more switches in wrong answers (d07).

**What changed performance, and by how much.**
- Step-back: +6.8 to +15.1 points on physics across three models, +10.9 on PaLM chemistry, +24.5 on TimeQA; nothing on StrategyQA alone (a05, a06). Net of breakage: 20.5% fixed vs 11.9% broken.
- Rephrase: +24.8 points average for GPT-4 on a set built partly for ambiguity (64.95 to 89.77). Small for weaker models (a08, b10).
- Problem rewrite (Self-Polish): +0.8 to +1.4 on average, losses on some sets (b11).
- Formal rewrite: +16.6 points for o3, +13.3 for R1 on 30 items (d13).
- Content hint: +3.2 (o3), +5.6 (R1), +3.2 (Gemini) on the Math set; style rule near zero (d13).
- Task-level method choice: T4D +39 (PaLM-2L) and +34 (GPT-4) over direct; small on MATH (b13, c17).
- Strategy-level comparison: +7.2% on maths vs -0.51% for self-reflection (d15); approach-aware training 67.56 vs 55.51 (d14).
- Restart with compacted facts: 2/3 to 4/1 wins on 5 puzzles; fact repetition recovers 15-20% of a 39% multi-turn loss (c14, d06).
- LLM help for human designers: no measurable gain, N=280 (a01).
- Clinical: a light prompt method beat reasoning models by about 40 points on recognition (b19, c19).

**Age of the evidence.** Most numbers are from GPT-3, GPT-4, PaLM-2L and Llama-2 (2022-2023). Newer items: Han 2025 (o3, R1, Gemini 2.5), Hao 2026 (o3 and 17 others), Batorski 2026 (Qwen3.5-27B), Gema 2025, Kou 2026 (GPT-5), Qi 2025 (o1, o3-mini, R1). No paper tests step-back or RaR on a reasoning model at matched tokens. d10 shows prompt tricks add little on o1-preview. d12 sizes a paraphrase control at about 2 points.

**Pattern.** Cheap, targeted, benchmark-scored reframes help (K19). Open design with human raters is null or mixed. Our bench items (ARC, BRAINTEASER) are closer to the first type.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Fire O8 only on a failure signal that code can locate, never on a generic "re-check" or the model's own doubt. Matches G1 and G2 | G1, G2, S6 | [E] | K07; b18, d08, d09, d01, d07 |
| Choose the frame early: generate several candidate readings or first steps in fresh contexts before committing, rather than reframing late. Matches S3 | S3, S1 | [E] | K21; d02, d01 |
| When frames must be compared, show competing frames side by side. Do not rely on "ignore the earlier frame" or on chain of thought to remove anchoring. Matches G4 | G4, S3 | [E] | K22; d03, d04 |

These three are already consistent with SCHEMA.md (G1, G2, G4, S3, section 4b). They need no new element. They back the existing rules, and K21 adds the point that early frame choice beats late review.

### Test first (nothing below goes into SCHEMA.md until its test passes; see UNKNOWNS.md)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| O8 as a goal or strategy change (not a paraphrase) vs plain resampling at equal tokens | O8 | [S] | K01, K24, K29; a01, d13, d14, d15 |
| Same-length unrelated-prompt and paraphrase control arms for every reframe test | G7 | [S] | K08, K26, K27; b15, d12, d11 |
| Trigger for O8: localised failure after sustained effort on one line; cost of a false trigger | G1, S6 | [S] | K28, K23; d07, d08, d05 |
| Compacted-facts restart after K failed probes (K=5, M=3) | S6, O8 | [C] | K10; b16, c14, d06 |
| Step-back as a gated sub-step; score net fixed minus broken | O2, S1 | [C] | K05; a05, a07, d11 |
| Rephrase step only on ambiguous items; check no loss on clear ones | S1 | [S] | K06; a08, b10, b11 |
| Content-bearing reframe (new representation or goal) over style rule | O8, O6 | [S] | K29; d13 |
| Hide or show the model's own first frame to later frames | S3, G4 | [S] | K12 |
| Compare self-made strategies; disagreement as trigger candidate | S3, S6 | [C] | K24; d14, d15 |
| Pick-a-method step before solving | S0, O8 | [S] | K18; b13 |
| Reframe quality vs reasoning length (cap per mode) | G11 | [C] | K11; b19, d16, d17 |
| "Invert each assumption" sub-step | O4, O8 | [S] | K15; b24 |
| Two-wording consistency check as a trigger | S0, G1 | [S] | K16; c18 |
| Log self-rated confidence vs blind-rated quality for O8 outputs | memory/log | [S] | K02; a02 |
| Score clarity and novelty on separate rubrics in open mode | G8 | [C] | K19; b25 |

Do not take the full Dorst nine-step as a pipeline (K03, a03). Do not take expert-style reframe instructions as an add until tested (K04).

## 8. Concrete tests on our bench

All arms at equal tokens (count every call, including setup and the reframe step). Same items per arm. At least 3 seeds. Include a same-length unrelated-prompt arm in every test (d11).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Goal/strategy reframe vs resample | ARC training and eval items; BRAINTEASER (sentence and word) | (a) plain resample to budget; (b) one O8 step that states a changed goal or strategy, then solve; (c) paraphrase-only reframe; (d) same-length unrelated prompt | Pass rate; share of reframes passing a not-a-paraphrase check | (b) minus (a) small at best (0 to +3 points); (b) above (c) by 1 to 3 points if strategy change matters |
| T2 Noise control | Same items | Baseline vs meaning-preserving paraphrase vs unrelated prompt | Pass-rate spread | Paraphrase about 2 points (d12); any O8 gain below that is noise |
| T3 Trigger | ARC items with checks | O8 always; O8 never; O8 on generic doubt; O8 on localised failure after K steps on one line | Pass rate; tokens; false-trigger rate (fires on items already correct) | Localised trigger beats always and generic doubt; "always" lowers pass rate on easy items |
| T4 Compacted restart | BRAINTEASER; multi-turn ARC probe sequences | Continue chat vs restart with K=5, M=3 facts vs restart with all facts vs restart with no facts | Pass rate; questions used | Restart with facts above continue by a few points; restart with no facts isolates the effect of dropping context |
| T5 Step-back gate | Items with a known principle (science QA style); ARC | Plain; step-back always; step-back gated by class; spurious prompt | Net fixed minus broken; pass rate | Net near 0 on reasoning models; positive on knowledge-heavy items |
| T6 Rephrase on ambiguity | Mix of ambiguous and clear items | Plain vs RaR vs RaR gated by an ambiguity check | Pass rate by subset | Gain on ambiguous items only; loss or none on clear items |
| T7 Own-frame anchoring | Open and ARC items | Later attempts see first frame; see none; see two opposing frames | Feature overlap with first frame; pass rate; diversity of final answers | One shown frame raises copying; two opposing frames lower it |
| T8 Content vs style | BRAINTEASER, maths brainteasers | Hint-type reframe (new representation); style rule ("don't brute force"); plain | Pass rate | Content reframe above style rule by 2 to 5 points (d13) |
| T9 Strategy diversity | ARC; maths | N samples same prompt vs N paraphrased prompts vs N distinct named strategies | Best-of-N accuracy; strategy-label count | Distinct strategies beat paraphrase by 1 to 2 points (d14) |
| T10 Wording flip | Items in two wordings | Baseline vs O8; baseline vs consistency check | Answer flip rate between wordings; pass rate | O8 lowers flip rate; check it does not widen it (c18) |
| T11 Length | T1 items | O8 step capped at short, medium, long; total tokens equalised by adding resamples to the short arms | Pass rate of reframed attempt | Short at least equal to long (d16, d17, b19) |

## 9. What does not transfer, and why

- **Human design quality ratings (Shin).** Crowd designers, one-hour session, participants chose their best frame, expert raters. Our bench scores answers, not peer ratings of frames.
- **Insight physiology and manipulation studies.** Eye movements, change points, working-memory dual tasks, physical movement of sticks (a17, a18, b21, b22). Human-only.
- **Fixation by images (Wadinambiarachchi).** Midjourney images to student sketchers (N=60). Our agent has no sketching stage. Only the general principle (exposure to a candidate can anchor) carries over (K12).
- **Clinical reframing (Sharma, Qi).** Empathy and positivity preferences, ROUGE against one reference. Different goal. Only the finding that light task-fit prompting and shorter output matched or beat reasoning models carries over, as a caution (K11).
- **Dorst's multi-stakeholder process.** Needs stakeholders and a client. Our tasks have none to interview.
- **Old-model gains.** Mishra 2022 (GPT-3) and Self-Polish (text-davinci-003) may fade on instruction-tuned and reasoning models.
- **Prompted anchors from outside.** Lou and Huang test hints put in the prompt, not the model's own first frame (limit stated in d03).
- **First step as a calculation.** Liao's perturbed first step is a calculation, not a frame (d02). The lock-in claim may be stronger or weaker for real frames.
- **Writing-quality views of framing.** The PLOS ONE rubric scores clarity, not reframing (b25).
- **Benchmarks built for ambiguity.** Rephrase gains partly repair poor wording (a08).

## 10. Open questions

1. Does an LLM-driven goal reframe beat no reframe on tasks with a checkable answer at equal tokens, with current models? Only Han 2025 is close, and it was not equal-token (d13).
2. Do step-back and RaR gains survive on 2025-26 reasoning models, with matched tokens and a paraphrase control?
3. What should trigger a reframe, and what does a false trigger cost? Direction known (localised failure, sustained effort); cost unmeasured.
4. Is Shin's null a real zero? Raw ratings would be needed for a TOST. From group sizes, effects above about 0.45 SD are excluded, small ones are not (K25).
5. Does the model anchor on its own first frame, and does hiding it help? Prompted anchors are shown (K22); own-frame is not.
6. What do the unopened foundations report in numbers (Dorst and Cross full text, Sio 2015, Knoblich 1999)?
7. Does compacted-facts restart hold on more than five puzzles, on BRAINTEASER, with current models?
8. Does a clearer frame trade off against novelty in LLM-assisted work? Can the schema score both?
9. Does the length effect (more tokens hurt reframe generation) generalise beyond clinical and language tasks? It is task dependent (K11).
10. Which reframing type adds value: abstraction, rephrase, inversion, or goal change? No isolated ablation exists.
11. Does the expertise effect (+12.54% novelty for expert users) have an analogue in the quality of the instruction we give the agent?
12. Is disagreement between self-made frames a useful trigger signal (d15)?

## 11. Sources

[V] = opened and read this session (full text or substantial text). [M] = not opened, abstract or snippet only, or described second-hand.

- [V] Shin, Polyanskaya, Lucero, Oulasvirta (2025), No Evidence for LLMs Being Useful in Problem Reframing. https://arxiv.org/abs/2503.01631 (a01-a04, b01-b03, c01-c04, d19, d20)
- [V] Zheng et al. (2023/2024), Take a Step Back. https://arxiv.org/abs/2310.06117 (a05-a07, b12, c08, c09)
- [V] Deng, Zhang, Chen, Gu (2023/2024), Rephrase and Respond. https://arxiv.org/abs/2311.04205 (a08, b09, b10, c10, c11)
- [V] Mishra et al. (2022), Reframing Instructional Prompts to GPT-k's Language. https://arxiv.org/abs/2109.07830 (a09, b14, c12, c13)
- [V] Sharma et al. (2023), Cognitive Reframing of Negative Thoughts. https://arxiv.org/abs/2305.02466 (a10, b20, c21)
- [V] Jiang et al. (2023), BRAINTEASER. https://arxiv.org/abs/2310.05057 (a11, b17, c15, c16)
- [V] Weak-eval-Strong, situation puzzles (NeurIPS 2024). https://arxiv.org/abs/2410.06733 (a12)
- [M] Sotnikova et al. (2026), CresOWLve (abstract, setup and limits only). https://arxiv.org/abs/2604.03374 (a13)
- [V] Wadinambiarachchi et al. (2024), Effects of Generative AI on Design Fixation. https://arxiv.org/abs/2403.11164 (a14, b08)
- [V] Carichon et al. (2026), IDEAFix. https://arxiv.org/abs/2606.00875 (a15; figures read from chart)
- [V] Wang et al. (2026), NexusAI. https://arxiv.org/abs/2604.10575 (a16)
- [V] Insight problem solving with GAMs and change point analysis (J. Intelligence 2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10219327/ (a17, b21)
- [V] Korovkin et al. (2018), working memory and representational change. https://pmc.ncbi.nlm.nih.gov/articles/PMC6174229/ (a18)
- [V] Chunk decomposition and reorganisation with Chinese characters (Front. Psychol. 2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC5694466/ (a19)
- [M] Schon (1983), The Reflective Practitioner. Book, no URL. (a20, c23)
- [M] Schon (1979), Generative metaphor. Chapter, no URL. (a21)
- [M] Schon and Rein (1994), Frame Reflection. Book, no URL. (a22)
- [M] Dorst (2011), The core of design thinking, Design Studies 32(6). Not located open. (a23)
- [M] Dorst (2015), Frame Innovation, MIT Press. https://mitpress.mit.edu/9780262029877/frame-innovation/ (a24, c22)
- [M] Paton and Dorst (2011), Briefing and reframing. Not located open. (a25)
- [M] Valkenburg and Dorst (1998), The reflective practice of design teams. Not located open. (a26)
- [M] Lawson (1979), block-arrangement study. Not located. (a27)
- [M] Kaplan and Simon (1990), In search of insight. Not opened. (a28)
- [M] Knoblich, Ohlsson, Haider, Rhenius (1999). Not opened; described in a19 and b23. (a29, b23)
- [M] Rittel and Webber (1973). Not opened. (a30)
- [M] Roozenburg (2002); Kolko (2010). Not opened. (a31)
- [M] Dorst and Cross (2001), abstract page. https://research.tue.nl/en/publications/creativity-in-the-design-process-co-evolution-of-problem-solution/ (b04)
- [V] Dorst and Cross (2001), via third-party copy; figures need a journal check. https://www.slideshare.net/slideshow/dorst-kees-and-cross-nigel-2001-creativity-in-the-design-process-co-evolution-of-problemsolution/30190014 (d18)
- [M] Sio, Kotovsky, Cagan (2015), meta-analysis of examples and fixation. https://doi.org/10.1016/j.destud.2015.04.004 (b05; bibliographic data only)
- [M] Youmans and Arciszewski (2014), Design fixation. https://www.cambridge.org/core/journals/ai-edam/article/design-fixation-classifications-and-modern-methods-of-prevention/A4F74AE59E42615EC7FDF1DAD3553FFC (b06; abstract only)
- [M] Jansson and Smith (1991), as summarised by Wadinambiarachchi 2024. https://arxiv.org/abs/2403.11164 (b07)
- [V] Zheng et al., Self-Polish. https://arxiv.org/abs/2305.14497 (b11)
- [V] Zhou et al. (2024), Self-Discover. https://arxiv.org/abs/2402.03620 (b13, c17)
- [V] Sclar et al. (2024), spurious features in prompt design. https://arxiv.org/abs/2310.11324 (b15)
- [V] Li et al. (2025), Situation puzzles and external reformulation. https://arxiv.org/abs/2503.18394 (b16, c14, c27)
- [V] Huang et al. (2024), LLMs Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (b18)
- [V] Qi, Lee, Breazeal, Park (2025), reasoning and cognitive reframing. https://arxiv.org/abs/2504.00163 (b19, c19, c20)
- [V] Spiridonov et al. (2026), matchstick interactivity replication. https://pmc.ncbi.nlm.nih.gov/articles/PMC12862482/ (b22)
- [M] Weller et al. (2011), interactivity in matchstick algebra; as described in b22. https://pmc.ncbi.nlm.nih.gov/articles/PMC12862482/ (b23)
- [V] Bianchi and Branchini (2023), thinking in opposites. https://pmc.ncbi.nlm.nih.gov/articles/PMC10219495/ (b24)
- [V] PLOS ONE (2026), Generative AI as a cognitive support tool in early-stage design ideation. https://pmc.ncbi.nlm.nih.gov/articles/PMC13585246/ (b25)
- [V] Sood, Wan, Paris, Grace (2026), Valuable LLM answers for research problem reframing. https://computationalcreativity.net/iccc26/papers/ICCC26_paper_78.pdf (c05-c07)
- [V] Echterhoff et al. (2024), Cognitive Bias in Decision-Making with LLMs. https://arxiv.org/abs/2403.00811 (c18)
- [M] Maher and Poon (1996); Gero and Kannengiesser (2014). No URL. Described in Sood 2026. (c24)
- [V] HTSA SCHEMA.md, O8 row. C:/Users/User/Desktop/AGI/research_notes/single_agent/SCHEMA.md (c25)
- [V] Kang et al. (2025), First Try Matters. https://arxiv.org/abs/2510.08308 (d01)
- [V] Liao et al. (2025), Lost at the Beginning of Reasoning. https://arxiv.org/abs/2506.22058 (d02)
- [V] Lou and Sun (2024), Anchoring Bias in LLMs. https://arxiv.org/abs/2412.06593 (d03)
- [V] Huang et al. (2025/2026), Anchoring Effect of LLM with synthetic data. https://arxiv.org/abs/2505.15392 (d04)
- [V] Mehta and Datta (2026), When Agents Commit Too Soon. https://arxiv.org/abs/2606.22936 (d05)
- [V] Laban et al. (2025), LLMs Get Lost In Multi-Turn Conversation. https://arxiv.org/abs/2505.06120 (d06)
- [V] Wang et al. (2025), Underthinking of o1-like LLMs. https://arxiv.org/abs/2501.18585 (d07)
- [V] Tyen et al. (2024), LLMs cannot find reasoning errors but can correct them. https://arxiv.org/abs/2311.08516 (d08)
- [V] Kamoi et al. (2024), When Can LLMs Actually Correct Their Own Mistakes. https://arxiv.org/abs/2406.01297 (d09; abstract and introduction only)
- [V] Nori, Usuyama, Horvitz (2024), From Medprompt to o1. https://arxiv.org/abs/2411.03590 (d10)
- [V] Batorski et al. (2026), Spurious Prompts. https://arxiv.org/abs/2605.29678 (d11; table read)
- [V] Hao, Wan, Zhai (2026), Robustness of LLMs in mathematical reasoning. https://arxiv.org/abs/2508.08833 (d12)
- [V] Han et al. (2025), Creativity or Brute Force? https://arxiv.org/abs/2505.10844 (d13)
- [V] Lee et al. (2026), Are We Measuring Strategy or Phrasing? https://arxiv.org/abs/2606.29985 (d14)
- [V] Zhang et al. (2024), Self-Contrast. https://arxiv.org/abs/2401.02009 (d15)
- [V] Gema et al. (2025), Inverse Scaling in Test-Time Compute. https://arxiv.org/abs/2507.14417 (d16)
- [V] Kou et al. (2026), Entertain, then Cancel. https://arxiv.org/abs/2610.21204 (d17)
- [V] This agent's equivalence-bound calculation on Shin 2025 (d19). Method note only.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 3 established claims: 2 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E05.04-K21** (reworded: the sources support less). Liao et al.: average final accuracy falls 40% (43% on hard questions) when the first step is wrong; Table 1 shows DS-R1-Qwen-7B 94.8 vs 28.5. Kang et al.: reflections after first answer use 16.8% to 47.8% of tokens for only +1.4% to +3.5% accuracy. All on math/science reasoning benchmarks; neither paper tests 'frame choice', so 'frame choice early matters more than review late' is an extrapolation. Minor: tokens range is 16.8-47.8%, not 17-48 exactly (rounding). Corrected claim: In long-CoT reasoning models on math and science benchmarks, the first answer or first step dominates the result: final accuracy falls about 40% on average when the first reasoning step is wrong (DS-R1-Qwen-7B 94.8 vs 28.5 in a perturbation test), and reflection after the first answer adds only 1.4-3.5% accuracy while using 16.8-47.8% of tokens (Liao et al.; Kang et al.).
