# Early, attenuation and late selection: deep document

*Subfield A07.01. Written from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01 ... d18) point to those files. Claim ids are A07.01-K01 ... K23. Why it matters for our agent: mostly background. The one live link is distractor handling in context (guardrails, context hygiene, memory).*

**Reading warning.** None of the founding papers (Cherry 1953, Broadbent 1958, Moray 1959, Treisman 1960, Treisman and Geffen 1967, Deutsch and Deutsch 1963, Norman 1968, Corteen and Wood 1972, Holender 1986) was opened. Their numbers are second-hand, from Conway et al. 2001 and Macdonald and Lavie 2008, both opened. Where a number is second-hand it is marked so.

## 1. What it is

The question: when many inputs arrive at once and only one matters, where does the system stop processing the others?

- **Early selection** (Broadbent): a filter blocks unwanted input on physical features (voice, ear, colour) before meaning is extracted. Unattended input is never understood.
- **Attenuation** (Treisman): the filter turns unwanted input down, it does not cut it off. Items with a low threshold (own name, urgent words, words that fit the context) can still get through.
- **Late selection** (Deutsch and Deutsch, then Norman): all input is identified automatically. Selection comes after meaning, by importance (pertinence), at the response or memory stage.

The standard task is dichotic shadowing: play two speech streams, one per ear, and have the listener repeat one aloud. Then test what they know about the other stream. Variants: flanker letters (Eriksen), load tests (Lavie), inattentional blindness, own-name tests.

Why it is a useful lens for LLMs: a context window is a place where relevant and irrelevant text sit side by side. A transformer reads all of it (no early filter), then attention weights act as a soft, late selector. The human question "was the junk processed?" becomes "did the junk change the answer?" The LLM literature says yes, often (section 6).

Key point from a 2022 review (a19): Kahneman and Treisman (1984) called early and late selection paradigms in Kuhn's sense. Each camp used its own methods. Late-selection work used simple familiar stimuli and favoured efficiency of processing. So the dispute is partly a dispute about method.

## 2. History and theories in depth

**Cherry (1953), a01, not opened.** Shadowing one ear while the other plays. Listeners could report physical features of the ignored message (speaker sex, speech versus tone) but not its content. Physical changes were noticed. This gave the "cocktail party problem".

**Broadbent (1958), a02, not opened.** Filter model. Stimuli enter a sensory buffer in parallel. A single-channel filter, set by physical features, passes one channel to a limited-capacity system. The rest is lost or held briefly. Prediction: nothing about meaning in the unattended channel is perceived.

**Moray (1959), a03/b01, second-hand.** Own name in the ignored ear. About 33% of subjects reported it (Conway 2001). The same figure appears for responding to a command prefixed with the own name. A "4 of 12" count seen in one evidence line could not be confirmed (K21). First big problem for strict early filtering. Two thirds never noticed, so it is a leak, not a collapse of the filter.

**Gray and Wedderburn (1960), b15, not opened.** Split messages: people grouped by meaning across ears. Hard to explain with a purely physical filter.

**Treisman (1960), a04/b14, not opened.** Attenuation. When a sentence switched ears, shadowers followed meaning into the wrong ear for a word or two. Exact percentages not read (gap 4 stays open). Model: the filter applies gain, and each word has a threshold. Context and importance lower the threshold.

**Deutsch and Deutsch (1963), a05/b16, not opened.** Late selection. Everything is fully analysed. Poor memory for the ignored channel is a memory or response failure. Selection is by importance.

**Treisman and Geffen (1967), a07, not opened, direction only.** Online test of the memory objection. Targets in either ear were reported live. Few unattended targets were reported, most attended ones were. This favours early or attenuated selection. Exact percentages unread.

**Norman (1968), a06.** Pertinence model. All input activates stored items. Selection depends on sensory activation plus pertinence (current relevance). The most active representation wins.

**Eriksen and Eriksen (1974), a08.** Flanker task. A target letter is slower when flankers map to the opposite response. So irrelevant flankers get identified. Read as late selection.

**Corteen and Wood (1972), b17, and Holender (1986), b18.** Skin conductance to shock-paired words in the unattended ear (late-selection evidence) versus the critique that awareness of the stimuli was not properly checked.

**Lavie (1995), a10.** Perceptual load theory, a hybrid. Perception is automatic until capacity is full. Low load leaves spare capacity that spills to distractors (late-like). High load uses it all up (early-like). It was meant to settle the debate.

**Lachter, Forster and Ruthruff (2004), b13, not opened.** Argued apparent late-selection effects come from attention briefly shifting to the unattended item. Early selection with leakage.

**Cohen, Dunbar and McClelland (1990), c24, not opened.** Neural-network model of Stroop: two pathways of unequal strength plus a control unit that boosts the task-relevant pathway. The oldest implementable model of "attention as gain".

**Where it stands now.** Single-theory answers have faded. Current work asks which conditions give leakage (own name, load, working memory, compression) and how big. Section 5 gives the numbers. The load theory that was meant to unify the camps is itself contested (K04, K22).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Own name noticed in unattended ear (minority) | Moray 33%; Wood and Cowan 34.6%; Roer and Cowan 29% (23 of 80); Naveh-Benjamin 2014 young adults 58% and 48% | a03, a13, b05 (Roer and Cowan opened; others second-hand) | Established (K01) |
| Working-memory span moderates name noticing | N=40 (20 per extreme quartile). High span 20%, low span 65%. Fisher p=.005. Shadowing errors 20.88 vs 10.00, t(32)=2.18, p=.04 | Conway et al. 2001, a12, d12 | Contested (K02) |
| Span link in preregistered replication | N=80. Bayes factors for name detection BF10 = 1.023, 0.582, 1.018 (inconclusive). Low-span still made more shadowing errors. Their low-span group had span 28.00 vs 8.22 in Conway | Roer and Cowan 2021, b05, b06 | Contested (K02) |
| Capture is brief | Errors rise at the name and next two words; none one word before or three words after | Roer and Cowan 2021, b07 | Established (K03) |
| Semantically unexpected words rarely capture | Of 80: 1 reported the unexpected word, 2 the expected word, 2 the yoked-control name; none changed shadowing | Roer and Cowan 2021, b05 (as corrected in critique) | Single-source |
| Own name slows visual categorisation | N=37 after exclusion, 22,033 trials; slowing over 100 ms; habituates across blocks | Li et al. 2024, a15, b08 | Established (K03) |
| Compression removes the name effect | Reported hearing own name: 24/24 at 57%, 20/24 at 38%, 4/23 at 25% (Exp 2). At 38% compression F(2,46)=5.11, p=.01, partial eta squared .182 | Li et al. 2024, a15, b08 | Single-source |
| Load-induced blindness | N=16. Detection of unexpected cross 37% (d' 1.31) at high load vs 90% (d' 3.68) at low; F(1,14)=11.90, p=.004. Search errors 11% vs 3%. Working-memory load did not change detection | Macdonald and Lavie 2008, a09 | Single-source (K05) |
| Load does NOT remove distraction | Incongruent minus congruent RT, low vs high load (ms): Exp1 111 vs 95; Exp2 79 vs 70; Exp3 123 vs 111; Exp4 31 vs 26; Exp5 23 vs 25; Exp6 13 vs 31. Exp1 N=39, Exp2 N=32 | Snowden and Gray 2025, a11, b09 | Contested (K04) |
| Individual variation in load effects | 8 experiments reanalysed per person; 7 observers x 5 sessions changed pattern across sessions; reversed effects seen | Marciano and Yeshurun 2017, b10 | Contested |
| Dilution can explain load effects | Set size cut distractor processing only with broad focus, same-category neutral items, weak preknowledge | Chen and Cave 2013, b11 | Established that dilution matters |
| Unattended syntax tracked in brain | MEG n=29 and n=23; 1 Hz peak p=0.045; left inferior frontal cluster p=0.0058 | Har-shai Yahav and Zion Golumbic 2021, a16 | Contested (K06) |
| No attention effect in brainstem | Wave V BF0+ moderate evidence against attention effect (3 to 10); latency BF01 about 4; CAP inconclusive | Brainstem study 2025, a17 | Contested (K06) |
| LLM distracted by one irrelevant sentence | GSM-IC. Of problems solved on the original, at most 18% solved under all distractors. Macro accuracy under 30% (code-davinci-002, text-davinci-003). code-davinci-002 CoT: micro 72.4, normalized 76.2, macro 6.0 | Shi et al. 2023, a20, b21 | Single-source (K07) |
| Role-overlap distractors worst | text-davinci-003 macro accuracy 0 on problems with more than 2 steps | Shi et al. 2023, b23 | Single-source |
| Sampling helps | 20-sample self-consistency: +11 points micro overall, +35.5 for 0-COT; right answer in samples 99.7% (CoT, LTM), 96.5% (0-COT); best macro 45% | Shi et al. 2023, a21 | Single-source (K08) |
| Instruction to ignore (older model) | code-davinci-002 CoT with instruction: micro 77.8, normalized 81.8, macro 15.0. LTM plus instruction: 80.6, 85.7, 25.0 | Shi et al. 2023, b21 | Single-source |
| System 2 Attention (rewrite filter) | LLaMA-2-70B-chat. Factual QA with opinions 62.8% to 80.3% (oracle 82.0). GSM-IC in-topic 51.7% to 61.3% (about +12 random, +10 in-topic). Objectivity +57.4% (abstract). 200 prompts for QA; 100 problems x 3 seeds for math | Weston and Sukhbaatar 2023, a22, b24 | Single-source (K09) |
| Keeping the original context hurts | S2A 80.3 vs S2A-KeepOrig 74.5 vs single-step 71.7 vs baseline+debias instruction 71.7 vs baseline 62.8 | Weston and Sukhbaatar 2023, a23, b25 | Single-source |
| Instruction alone: sycophancy remains | Instructed prompting: Suggest Correct 92% (above oracle), Suggest Incorrect 38% vs oracle 82% | Weston and Sukhbaatar 2023 | Single-source |
| Ignore line on a newer model | Llama-3.1-8B attack success 37.5% to 9.9% with "ignore" line | Rajeev et al. 2025, d03 | Contested vs S2A (K18) |
| Reasoning models still distracted | R1 combined attack success 4.50% vs 1.50% random; R1-distill-Qwen-32B 8.00%; 574 of 1,618 triggers broke V3 (35%), about 114 transferred to R1 (~20%); 225 problems x 6 runs; answers up to 3x longer | Rajeev et al. 2025 (CatAttack), d01, d02 | Single-source (K17) |
| Transfer of CatAttack multipliers | QwQ-32B 5.14x, Phi-4-reasoning 1.15x, Qwen3-30B-A3B 3.61x, Llama-3.1-8B 5.23x, Mistral-Small-24B 7.21x | d03 | Single-source |
| More distractors, lower step accuracy | Depth 5: Grok-3-Beta 43% (1 distractor) to 19% (15); GPT-4.1 26% to 2%. Error grows like m^delta, delta 0.11 (2 steps) to 0.49 (5 steps) | Yang et al. 2025, c11, d04 | Established (K13) |
| Process reward search helps out of domain | PRM-guided beam search +2.57 to +6.29 points | Yang et al. 2025, c12 | Single-source |
| Position effect (U shape) | GPT-3.5 drops more than 20 points mid-context; at 20 and 30 docs below closed-book 56.1%. Closed/oracle: GPT-3.5 56.1/88.3, Claude-1.3 48.3/76.1, LongChat-13B 35.0/83.4, MPT-30B 31.5/81.9 | Liu et al. 2023, a24, b26, c07 | Contested for new models (K11) |
| More documents barely help | Beyond 20 documents: +1.5% GPT-3.5, +1% Claude-1.3 | Liu et al. 2023, c08 | Established (K11) |
| Query before and after fixes key-value only | Key-value: GPT-3.5-16K perfect at 300 pairs vs worst case 45.6%. Multi-doc QA: small gain at start, small loss elsewhere | Liu et al. 2023, c09 | Single-source |
| Position bias shifts with fill | Middle dip strongest when inputs fill up to about half the window; end-bias beyond. Six models 8K to 128K; 4 synthetic sets of 100 items plus 1,500 RAG items | Veseli et al. 2025, d05 | Single-source |
| Reasoning inherits retrieval | P(right given retrieval wrong) 0.35 to 0.52 vs P(right given retrieval right) 0.72 to 0.82 across six models | Veseli et al. 2025, d06 | Single-source |
| Length alone hurts | Drops 13.9% to 85%. Llama3 VarSum 96.0 drops 59 at 7,500 essay tokens, 85 at 30,000; whitespace -48, masked -50 at 30,000. GPT-4o VarSum no drop | Du et al. 2025, d07 | Single-source (K19) |
| Recite-then-solve | Mistral-7B GSM8K with essay filler: 49.3 to 71.4 at 3,750 tokens; 35.5 to 66.7 at 26,250; gain up to +31.2. GPT-4o RULER: QA1 up to +2.6, QA2 up to +4.0 | Du et al. 2025, d08 | Single-source (K19) |
| Context rot, 18 current models | 194,480 calls; 8 lengths x 11 needle positions. Coherent haystacks more distracting than shuffled for all 18. No needle-position effect. Focused (~300 tokens) beat full (~113k) on LongMemEval for every model (306 prompts) | Chroma 2025, d10, d11 | Single-source, vendor report (K20) |
| Attention heads steer relevance | Top-20 heads, split-softmax 0.3: EM 59.4 to 67.1; random heads under 0.3 change | Zhu et al. 2025, b27 | Single-source |
| Attention noise cancelled | Differential Transformer: 30-point gap at N=6 needles, R=2 (4K) | Ye et al. 2025, c10 | Single-source |
| Selective Attention layer | Equals transformer with 2x heads. Memory 16x/25x/47x only with extra memory loss; 5x/7x/8x with standard loss (corrected) | Leviathan et al. 2025, a25 | Established as architecture result (K12) |
| Audio LLM cocktail party | Gemini-2.0-Flash single-stream 0.955 vs 0.242 cocktail party at 0 dB. Open models pick distractor stream on 21.5 to 41.0% of items at 0 dB, accuracy 0.016, ECE 0.73. Target-selection ratios 59.0 / 78.5 / 78.1 / 68.9% | MUSI, c15, c16, b28, b29 | Established (K14) |
| MUSI language cells | At +5 dB English target: English distractor 0.955, Spanish 0.320, Korean 0.442, Chinese 0.808. The English cell equals the single-stream score, which looks odd | MUSI Table 11, d16 | Unverified (possible slip) |
| Humans vs speech LLMs | 40 listeners (20 Hindi, 20 Kannada). Human attention gap about 32 (Hindi), 36 (Kannada), 12 (English L2), p<0.01. Closed models beat humans on the unattended speaker | c13, c14 | Single-source |
| Stroop in LLMs | Gemma-2-2B congruent 0.9644 vs incongruent 0.5676 delta probability (diff 0.3968, CI [0.3529, 0.4407], t(39)=18.28). 5 clauses vs 2: incongruent -0.3039 | Hu et al. 2026, c19, c20 | Single-source (K16) |
| Vision-language word-over-ink bias | CLIP: word accuracy 99.5%, ink 15.9% on 23,338 images. Qwen2-VL-7B ink accuracy on incongruent 31.1% with long ignore instruction | Teker et al. 2026, c21 | Single-source |
| VLM conflict | 4,410 tasks, 47 VLMs; all show congruency effects; large models below chance on high-conflict incongruent | Wang et al. 2026, c18 | Single-source |
| Chain-of-thought plus RL for target speaker | WER 4.84% (2-mix) and 12.23% (3-mix) after RL; CoT data cut WER by 21% and 16.2% | Zhang et al. 2026, c22 | Single-source |

## 4. Mechanisms and models

Each model below is written so it can be coded.

**4.1 Broadbent filter (hard early gate).**
```
buffer   = parallel_encode(all_channels)      # physical features only
selected = channel whose feature == cue       # e.g. ear, voice
percept  = semantic_analyse(selected)         # limited capacity
others   = discard (or decay in buffer)
```
Predicts zero semantic leakage. Refuted as a strict rule by own-name breakthrough. But a hard early gate is exactly what the S2A rewrite does for LLMs (4.5).

**4.2 Treisman attenuation.**
```
gain[c] = 1.0 if attended else g              # 0 < g < 1
activation(w) = gain[c] * signal(w)
w is perceived if activation(w) > threshold[w]
threshold[w] = low for own name, urgent words, context-primed words
```
Free parameters: g and per-word threshold. Own name has a low threshold. Context lowers it for expected words. Roer and Cowan found expected-word capture rare (2 of 80), so the context part is weaker than the own-name part.

**4.3 Deutsch and Norman late selection with pertinence.**
```
for each input: activation = sensory_strength + pertinence(task_state)
winner = argmax(activation)                   # selection after identification
```
Everything is identified. Selection is a ranking at the end. This is the default picture of an LLM reading a full context: all tokens are encoded, attention decides. Soft attention is a late, graded version.

**4.4 Lavie load.** `distractor_processing = max(0, capacity - task_demand)`. High task demand leaves zero spare capacity. Evidence now says this is too simple: distraction was similar at both loads in six experiments (Snowden and Gray), and load effects reverse with layout (Wang and Chen 2026, d15). Dilution is the rival: extra neutral items weaken the distractor signal.

**4.5 System 2 Attention (S2A), a hard early filter for LLMs.**
```
cleaned = LLM("Rewrite the context keeping only what is relevant to the question. Drop opinions and unrelated text.", context, question)
answer  = LLM(cleaned_only, question)         # original context NOT shown
```
Two calls. Showing the original next to the cleaned text lost part of the gain (80.3 to 74.5).

**4.6 Recite-then-solve.**
```
evidence = LLM("Copy out the passages needed to answer", long_context, question)
answer   = LLM(evidence, question)
```
Turns a long task into a short one.

**4.7 Soft attention inside the network.** Selective Attention (a token can reduce attention to tokens no longer needed; reduce only), Differential Transformer (subtract two softmax maps to cancel common-mode noise), head-focus scaling (raise the split-softmax exponent on 20 heads). These need weight access. Not a scaffold lever.

**4.8 Conflict model (Cohen, Dunbar and McClelland).** Two pathways; the stronger wins unless a control signal boosts the task pathway. LLM analogue: in-weight default versus in-context rule (Hu et al. 2026). Fine-tuning the default stronger hurt incongruent trials; adding rule clauses hurt middle clauses.

## 5. What holds up

**Holds up well.**
- Own-name breakthrough in about 30% of shadowers, across 1959, 1995 and 2021 (K01). Three sources, the last preregistered.
- The capture is short and local (K03).
- Time-compressed names go unnoticed (24/24, 20/24, 4/23 report it), and slowing exceeds 100 ms at N=37.
- Distractor cost rises with more distractors in LLMs, and with length alone (K13, K19).

**Failed or contested.**
- Span link (Conway 20% vs 65%, N=40) did not replicate cleanly: Bayes factors 0.58 to 1.02 at N=80. The replication's low-span group (mean 28.00) was far higher than Conway's (8.22), so it was not like for like. No larger clean replication exists (K02).
- Perceptual load: six experiments failed to find the signature effect (Snowden and Gray 2025). Marciano and Yeshurun found few individuals who follow the theory. Dilution explains many results. 2026 papers show reversals with layout. No independent replication of the 2025 failure yet (K22).
- Semantic capture by unexpected words: not found (Roer and Cowan).
- Neural tracking of unattended syntax: small N, p near .045, against a brainstem null (K06).
- Position effects in LLMs: strong in 2023 models, fading beyond half the window (Veseli), absent in Chroma's 18 models (K11).

**Moderators that matter.**
- Human: own-name relevance, speech rate (compression), habituation across blocks, working-memory span (disputed), load (disputed), layout.
- LLM: distractor type (role overlap and same topic worst), distractor count, length, question-distractor similarity (needle-question similarity 0.445 to 0.775; lower similarity degrades faster), model size (larger resolves conflict better), model strength (GPT-4o barely hurt by length on VarSum, a 7B hurt a lot).

**Interventions that worked.**
- Rewrite-and-discard filter (S2A): +17.5 points on factual QA, +10 to +12 on GSM-IC (one model).
- Recite-then-solve: up to +31.2 for a 7B model, up to +4.0 for GPT-4o.
- Self-consistency: +11 points micro, +35.5 on 0-COT (older models).
- Focused versus full prompt: better for all 18 models on LongMemEval.
- Ignore line: Llama-3.1-8B attack success 37.5% to 9.9%.
- Distractor-containing exemplars (Shi). Training on strong distractors and PRM-guided search (Yang): +2.57 to +6.29 out of domain.

**Interventions that did not work, or worked little.**
- Ignore line on GSM-IC with LLaMA-2-70B: no consistent gain (Weston).
- Keeping the original context visible next to the cleaned one: worse.
- Query before and after the documents on multi-doc QA: no real fix.
- Separating audio sources first: did not fix wrong-stream answers (MUSI).
- More retrieved documents past 20: about +1%.
- Telling a VLM to ignore the written word: ink accuracy only 31.1% (Qwen2-VL-7B).

## 6. Language models

**No direct test of the classic theories.** A full-text grep of Shi, Weston, Liu and Leviathan found zero hits for Treisman, Broadbent, cocktail, attenuation (K15). Links here are analogies.

**Text distraction.**
- 2023 models: one irrelevant sentence cuts GSM8K-style accuracy hard (macro under 30%; for code-davinci-002 CoT, micro 72.4 vs macro 6.0). Role-overlap distractors drove macro accuracy to 0 on problems of 3 or more steps.
- 2025 non-reasoning models: with 15 distractors, step accuracy at depth 5 fell to 19% (Grok-3-Beta) and 2% (GPT-4.1).
- 2025 reasoning models: smaller in absolute terms but real. R1 attack success 4.50% vs 1.50%. Slowdown to 1.5x the token budget: o1 26.4%, o3-mini 16.8%, R1 28.0%, R1-distill 42.2%. The triggers were adversarially searched, so these are not natural rates. Phi-4-reasoning was nearly immune (1.15x). GSM-DC tested no reasoning model.
- Long context: length alone costs 13.9% to 85% in 2025 work, even with whitespace. Strong models (GPT-4o on VarSum) barely moved.

**What changed it, by how much.**

| Lever | Gain | Model | Caveat |
|---|---|---|---|
| S2A rewrite | 62.8 to 80.3 | LLaMA-2-70B-chat | one paper, GPT-4 graded |
| Recite first | up to +31.2 (7B), +4.0 (GPT-4o) | Mistral-7B, GPT-4o | gain shrinks with stronger model |
| 20-sample vote | +11 micro, +35.5 on 0-COT | davinci family | not retested on current models |
| Ignore line | 37.5% to 9.9% attack success | Llama-3.1-8B | contrast with Weston |
| Focused vs full | significant for all 18 | 2025 frontier | vendor report |
| PRM beam search | +2.57 to +6.29 | GSM-DC models | out of domain only |

**Position.** The U shape is real in 2023 models. In 2025 models it depends on fill level (Veseli) or is absent (Chroma). Reasoning inherits retrieval: P(right | retrieval wrong) is 0.35 to 0.52, versus 0.72 to 0.82 when retrieval is right.

**Audio and vision.** Audio LLMs fail cocktail-party selection (Gemini-2.0-Flash 0.955 to 0.242; open models choose the distractor stream on 21.5 to 41.0%). Closed models beat humans on the unattended speaker, which is also a failure to ignore. Source separation first did not fix it. CoT plus GRPO fine-tuning cut word error rate to 4.84% (2-mix) and 12.23% (3-mix). Stroop-type conflict shows in LLMs and VLMs (Gemma-2-2B 0.9644 vs 0.5676; CLIP ink 15.9%).

**Mechanism work.** A few heads control weight on relevant context (top-20 heads, EM 59.4 to 67.1). Selective Attention and Differential Transformer change the architecture. All need training or weight access.

**Honest limits.** Most text results are 2023 vintage or single-paper. No equal-token comparison of S2A against best-of-N exists (K23). No test with a self-relevant token (own task name) exists.

## 7. What our agent should take

Schema parts: G guardrails, S states, O operators, memory (SCHEMA section 5). Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Context hygiene is a cost, not free [E] (G7 note, memory).** More irrelevant text lowers accuracy in every study, and length alone does too. Admit an item to context only if it earns its place. Evidence: K13 (c11, d04), K19 (d07), Liu c08 (past 20 documents adds about 1%). G7 already demands equal-token payback; this makes the rule concrete for context.
2. **Never rely on a plain "ignore" line as the only distractor defence [E that results are mixed; size S] (G).** Weston: no gain. Rajeev: 37.5% to 9.9%. Treat it as a cheap arm, not as proof of safety. Evidence a23, c06, d03.
3. **Do not build on perceptual load or working-memory span [E that they are contested] (none).** Evidence K02, K04, K22.

### Test first (single-source or contested)

4. **Rewrite-and-discard filter before solving [S] (O, S0 gate).** Evidence a22, a23, b24, b25. Must beat plain and best-of-N at equal tokens. Hold the original out of view.
5. **Recite-then-solve for long inputs [S] (memory read).** Evidence d07, d08. Gain may vanish for strong models (+4.0 for GPT-4o).
6. **Focused retrieval over full history [S] (memory).** Evidence d10, d11 (vendor report).
7. **Sample-and-vote against distractors [S] (O, G4 caution).** Evidence a21. G4 says samples from one model are correlated; the +11 is from older models.
8. **Key evidence first or last, truncate the middle [C] (memory).** Evidence a24, d05, d10.
9. **Salient self-relevant irrelevant token capture [S, human analogue only] (G).** Evidence a15, b05, d01, d02. No LLM test with a self-relevant token exists.
10. **Log distractor-count slope [S] (G7 logging).** Evidence c11, d04.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, with the rewrite pass counted. Report accuracy, tokens, and a 95% interval over at least 3 seeds.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | GSM-IC-style math with 1 added irrelevant sentence (random, in-topic, role-overlap) | plain / plain + ignore line / S2A rewrite / best-of-N sized to match tokens | macro and micro accuracy | Rewrite beats plain by 5 to 10 points on in-topic; vs best-of-N unknown (K23) |
| T2 | Same items, our reasoning-capable model | plain thinking vs thinking with filter pass | accuracy and thinking tokens | Smaller gap than 2023 models; distractor raises token use |
| T3 | Long-context QA, 1 key fact among 20 distractor documents | full / recite-then-solve / top-k truncation / key fact first | accuracy | Recite helps a weaker model by 10+ points, a strong model little |
| T4 | Memory recall over a long run history | full history vs focused slice | accuracy, tokens | Focused wins (K20) |
| T5 | Distractor count sweep (1, 5, 15) on multi-step items | plain vs filter | slope of accuracy on count | Filter flattens the slope |
| T6 | Insert the agent's own task name or a self-referential line into irrelevant text | with vs without insertion | accuracy, answer length | Small cost at most; short and local |
| T7 | Position sweep (start, middle, end) at 25% and 90% context fill | plain | accuracy by position | Middle dip at lower fill only |
| T8 | Same-topic vs off-topic distractor | plain vs filter | accuracy gap | Same-topic worse; filter helps more there |
| T9 | Clean items the plain model already solves | plain vs filter | accuracy | Filter must not cost accuracy when no distractor is present (G7) |

## 9. What does not transfer, and why

- **Ears and physical channels.** Text has no physical channel to filter on. The Broadbent filter has no direct counterpart; the cue is content.
- **Capacity and load.** Human limited capacity is a bottleneck. An LLM reads all tokens in parallel. Load theory has no clean mapping and is contested in humans anyway.
- **Working-memory span.** A human individual difference, and itself contested.
- **Own-name breakthrough as a mechanism.** The LLM analogue (a salient irrelevant token) is only an analogy. No LLM paper tests it.
- **Neural evidence.** Small samples, no scaffold relevance.
- **Architecture fixes** (Selective Attention, Differential Transformer, head scaling) need training or weight access, outside a scaffold.
- **Audio results (MUSI, cocktail-party LLMs).** A text agent has no audio streams.
- **2023 model numbers.** Pre-reasoning models. Do not carry sizes forward.
- **Vocabulary overlap.** Human attention rests on a bounded physical filter; LLM "attention" is a soft weight over every token. The words match, the machinery does not.

## 10. Open questions

1. Treisman 1960 and Treisman and Geffen 1967 percentages (originals unread). Moray "4 of 12" unverified.
2. Does S2A beat best-of-N at equal tokens with a current reasoning model? (K23)
3. Does a self-relevant irrelevant token capture reasoning, as own name does?
4. Does the first/last position effect hold in 2025 to 2026 long-context models, and does equal-token truncation beat full context?
5. Does Snowden and Gray's load-independence replicate independently? The 2026 load papers were read as abstracts only.
6. Does the span link replicate with a larger sample and a like-for-like quartile contrast?
7. The MUSI same-language cell (0.955 at +5 dB, equal to single-stream) may be a table slip. Mixed-language text agents untested.
8. Is the ignore line effective on current models, given Weston (no gain) vs Rajeev (37.5% to 9.9%)?
9. Does a recite step still help strong models (GPT-4o gain only +4.0)?
10. Do CatAttack rates hold for natural, unsearched distractors?

## 11. Sources

[V] opened this session, [M] snippet or second-hand only.

- [M] Cherry (1953). https://doi.org/10.1121/1.1907229
- [M] Broadbent (1958) Perception and Communication. https://doi.org/10.1016/C2013-0-08000-3
- [M] Moray (1959). https://doi.org/10.1080/17470215908416289
- [M] Treisman (1960). https://doi.org/10.1080/17470216008416732
- [M] Gray and Wedderburn (1960). https://doi.org/10.1080/17470216008416728
- [M] Deutsch and Deutsch (1963). https://doi.org/10.1037/h0039515
- [M] Treisman and Geffen (1967). https://doi.org/10.1080/14640746708400062
- [M] Norman (1968). https://doi.org/10.1037/h0026118
- [M] Corteen and Wood (1972). https://doi.org/10.1037/h0033154
- [M] Eriksen and Eriksen (1974). https://doi.org/10.3758/BF03203267
- [M] Holender (1986). https://doi.org/10.1017/S0140525X00021269
- [M] Cohen, Dunbar and McClelland (1990). https://doi.org/10.1037/0033-295X.97.3.332
- [M] Lavie (1995). https://doi.org/10.1037/0096-1523.21.3.451
- [M] Wood and Cowan (1995). https://doi.org/10.1037/0278-7393.21.1.255
- [M] Lachter, Forster, Ruthruff (2004). https://doi.org/10.1037/0033-295X.111.4.880
- [M] Tsal and Benoni (2010), via Snowden and Gray 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12605277/
- [M] Mesgarani and Chang (2012). https://doi.org/10.1038/nature11020
- [M] Luo and Mesgarani (2019) Conv-TasNet. https://arxiv.org/abs/1809.07454
- [M] Kamradt (2023) Needle in a Haystack. https://github.com/gkamradt/LLMTest_NeedleInAHaystack
- [V] Conway, Cowan, Bunting (2001). https://memory.psych.missouri.edu/assets/doc/articles/2001/conway-et-al-pbr-2001.pdf
- [V] Macdonald and Lavie (2008). https://pmc.ncbi.nlm.nih.gov/articles/PMC2672054/
- [V] Chen and Cave (2013). https://pmc.ncbi.nlm.nih.gov/articles/PMC3675768/
- [V] Marciano and Yeshurun (2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC5391011/
- [V] Roer and Cowan (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8908911/
- [V] Har-shai Yahav and Zion Golumbic (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8163500/
- [V] Attention-Setting and Human Mental Function (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9224755/
- [V] Li et al. (2024) own name and compression. https://pmc.ncbi.nlm.nih.gov/articles/PMC11089017/
- [V] Brainstem study (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12500158/
- [V] Snowden and Gray (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12605277/
- [V] Shi et al. (2023). https://arxiv.org/abs/2302.00093
- [V] Weston and Sukhbaatar (2023). https://arxiv.org/abs/2311.11829
- [V] Liu et al. (2023). https://arxiv.org/abs/2307.03172
- [V] Hsieh et al. (2024), abstract only. https://arxiv.org/abs/2406.16008
- [V] Meng et al. (2024). https://arxiv.org/abs/2409.08596
- [V] Leviathan et al. (2025). https://arxiv.org/abs/2410.02703
- [V] Ye et al. (2025) Differential Transformer. https://arxiv.org/abs/2410.05258
- [V] Zhu et al. (2025). https://arxiv.org/abs/2503.23306
- [V] Rajeev et al. (2025) CatAttack. https://arxiv.org/abs/2503.01781
- [V] Yang et al. (2025) GSM-DC. https://arxiv.org/abs/2505.18761
- [V] Veseli et al. (2025). https://arxiv.org/abs/2508.07479
- [V] Du et al. (2025). https://arxiv.org/abs/2510.05381
- [V] Chroma (2025) Context Rot. https://www.trychroma.com/research/context-rot
- [V] Benchmarking humans and machines (2025). https://arxiv.org/abs/2509.17965
- [V] Zhang et al. (2026) Thinking in Cocktail Party. https://arxiv.org/abs/2509.15612
- [V] Wang et al. (2026) VLM conflicts. https://arxiv.org/abs/2505.18969
- [V] Koo (2026) MUSI. https://arxiv.org/abs/2605.17225
- [V] Hu et al. (2026) conflict in LLMs. https://arxiv.org/abs/2608.11510
- [V] Teker et al. (2026). https://arxiv.org/abs/2610.12650
- [V] Nguyen et al. (2026) CHiME-9. https://arxiv.org/abs/2608.08510
- [V] Seeligmuller, Wolfe, Roer (2026), abstract only. https://doi.org/10.3758/s13414-026-03360-2
- [V] Wang and Chen (2026), abstract only. https://doi.org/10.1111/nyas.70346

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 5 established claims: 5 confirmed as written, 0 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

