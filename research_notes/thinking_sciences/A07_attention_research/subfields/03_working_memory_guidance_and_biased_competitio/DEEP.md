# Working memory guidance and biased competition: deep document

*Subfield A07.03. Evidence ids (a01-a34, b01-b26, c01-c27, d01-d16) and claim ids (K01-K29) refer to the jsonl files in this folder. Corrections from critique.md are applied. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The question: when you hold something in working memory, does it steer what you notice next?

Two answers have been fought over for 30 years.

- **Biased competition** (Desimone and Duncan 1995). Items in view compete for neural representation. A held target template tilts the race toward items that match it. A held item that matches a distractor should therefore help that distractor win, even when this hurts the task.
- **Load theory** (Lavie; de Fockert et al. 2001). Working memory also holds the control that keeps distractors out. Fill working memory with something else and control weakens, so distractors interfere more.

The conflict: under high memory load, a held item that matches a distractor adds interference by biased competition. Load theory predicts more interference from any distractor. The two accounts make different predictions about when a matching distractor costs most. The human data do not settle it (K03, contested).

Why it matters for our agent: a lesson, note or past answer held in context is a template. Anything in the next task that resembles it gets a head start, relevant or not. This is the machine form of fixation. The human work tells us which conditions make the pull strong (active, recent, several matching items, effortful to hold) and which make it vanish (deprioritised, delayed, replaced by other work).

Hard limit on the evidence: no study found tests load theory against biased competition in an LLM (c27, d14). All LLM links below are analogies (a similarity effect, a position effect, a token-copying effect), not tests of the human contrast.

## 2. History and theories in depth

### 2.1 Neural root: biased competition

- **Chelazzi, Miller, Duncan, Desimone 1993** (a02, d01). Monkeys held a picture cue, then saw 2 to 5 choice pictures. Cue-selective inferotemporal cells kept firing through the delay. About 90 to 120 ms before the saccade to the target, responses to non-targets were suppressed and the target dominated. Abstract read only; cell counts missing. The cue was always the target, so the cost of a matching distractor was not measured.
- **Chelazzi, Duncan, Miller, Desimone 1998** (a03, d02). Delay activity was higher after a good cue than a poor cue. Baseline was higher when the animal expected the good cue. After array onset the response first ignored which item was target, then within 150 to 200 ms was set by the target. Suppressive interactions between stimuli appeared in most cells.
- **Desimone and Duncan 1995** (a01, d04). The founding review. Not opened (paywall, 403). Content is known from later papers only. No numbers recorded.
- **Downing 2000** (a04, d03). First behavioural demonstration. A sample held in memory pulled attention to a matching object shown beside a novel one (probe task). A matched task with no memory demand showed the opposite pattern, so mere exposure was not the cause. Probe times and N not read.

### 2.2 Behavioural capture: the Soto line

- **Soto, Heinke, Humphreys, Blanco 2005** (a05, b13). Search for a tilted line among vertical lines, each inside a coloured shape. A held shape matching the target's shape sped search. A held shape matching a distractor slowed it. Participants knew the held item was never the target. Exact times not read.
- **Soto and Humphreys 2008** (a06-a10). Four experiments, opened. Details in section 3.
- **Soto, Hodsoll, Rotshtein, Humphreys 2008** (a22). Review: guidance from working memory is automatic, even when harmful, and differs from bottom-up priming (snippet only).
- **Soto and Humphreys 2009** (a16). Holding only the shape of a coloured object: search suffered when a distractor matched both colour and shape (abstract).

### 2.3 The "not automatic" challenge

- **Woodman and Luck 2007** (a11-a13, b09). Opened. One held item with a long delay: no cost (1,475 vs 1,505 ms). Three held items: a 67 ms benefit. They read this as memory being usable as a template for rejection.
- **Olivers, Meijer, Theeuwes 2006** (a15). Seven experiments. Interference is largest when the distractor is identical or related to the held object, but only if the content is hard to verbalise (abstract).
- **Han and Kim 2009** (a14, b10). Capture appeared but vanished when search was perceptually demanding or when onset was delayed long enough for cognitive control. Reconciles the two camps.
- **Hollingworth 2022 review** (b04, b25). Three conclusions: maintenance is not sufficient for guidance; the active state is set by task demands; the active state can span more than one item.

### 2.4 The template-state view

- **Olivers, Peters, Houtkamp, Roelfsema 2011** (a19). One item holds the status of attentional template; accessory items do not bias attention.
- **Carlisle, Arita, Pardo, Woodman 2011** (a18). The template leaves working memory with practice (CDA falls as the same target repeats).
- **Hollingworth and Beck 2016, Bahle et al. 2018, 2020** (b01, b05, b06). Two items can both guide, and their effects sum. Argues against a one-item template.
- **Van der Stigchel and Olivers 2019** (a20). Attention is an emergent property of maintaining the item for the task goal (sensory recruitment). Memory not serving a goal can be recoded verbally or moved to long-term memory.

### 2.5 Four rival accounts (b25)

1. Single-item template, other held items inert.
2. Multiple-item template (supported by b01, b03, b05, b06).
3. Capture then rapid suppression (Sawaki and Luck 2011, b08).
4. Learned task statistics decide use or avoidance of the held content.

### 2.6 Recent human work (2025-2026)

- Hautekiet, Lewis-Peacock, Olivers 2026 (a27, d05): capture survives a cue to focus on search and an interruption task. Abstract only.
- Kim, Kwon, Heo, Han 2026 (a28, d06): matching distractors slow search but add no accuracy cost. Abstract only.
- Liu, Wang, Liu 2026 (a29, d07): matching distractors draw more first fixations; the cost arises after fixation; higher WMC lowers dwell. Abstract only.
- Won and Zhang 2025 (a30, d08): strong capture in feature search, weaker in singleton-detection mode. Abstract only.
- Niu and Hollingworth 2026 (b07): guidance needs a memory demand. A merely flashed colour gave no or weak guidance.

### 2.7 Machine models of biased competition

Reynolds and Heeger 2009 normalisation model (a24, c26), Deco and Rolls 2004/2005 spiking models (a25, a26, c25), Adeli and Zelinsky 2018 ATTNet (c21). None were numerically read. See section 4.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| One held item, matching distractor slows search (Exp 1, gaps 188/504/1008 ms) | N=10. Invalid 1,209 vs neutral 1,146 ms, F(1,9)=11.23, p=.008. Cost did not shrink with gap (validity x ISI p=.86). Search error about 1% | Soto and Humphreys 2008 (a06) | [E] K01 |
| Cost survives articulatory suppression (Exp 2) | N=15. 1,049 vs 991 ms, F(1,14)=16.24, p=.001. Cost clearer at longest gap (p=.025) | a07 | [E] |
| Two held items, no suppression (Exp 3) | N=14. 1,101 vs 1,015 ms, p=.005. Memory accuracy about 76% | a08 | [E] |
| Two items plus suppression: cost gone (Exp 4) | N=14. 980 vs 954 ms, p=.077 (not significant). Exp 3 vs 4 interaction p=.049 | a09 | [C] weak, small N |
| One held item, long delay: no capture | N=10. 1,475 vs 1,505 ms, p>.40; search accuracy 99.4 vs 98.9% | Woodman and Luck 2007 (a11) | [E] K02 |
| Identical match: still no capture | N=10. 1,455 vs 1,458 ms; difference -3.3 ms, 95% CI +/-5.9 | a12 | [E] |
| Three held items, matching distractor speeds search | N=10. 1,327 vs 1,394 ms (67 ms faster), p<.01; errors 0.2 vs 1.5% | a13 | [C] K03 |
| Match count scales capture (gap task) | N=24. Mem-1/Match-1 68 ms; Mem-2/Match-1 44 ms (p=.03); Mem-2/Match-2 124 ms; 124 vs 68 p=.034 | Hollingworth and Beck 2016 (b01) | [E] K05 |
| Same, singleton task | Mem-1/Match-1 58 ms; Mem-2/Match-1 6 ms (p=.72); Mem-2/Match-2 51 ms | b01 | [E] |
| Presence of a non-matching coloured item vs match | Gap task: Match-0 vs No-Color p=.20, .29 (not reliable); singleton task reliable | b02 | [E] task moderates |
| Large replication | 56 analysed of 66; load 1 BF10=36.5 (location match), 1.19e5 (mismatch); load 2 BF10=0.163, 0.117 (no difference). Capture at load 1 in 43/56 people, load 2 in 28/56 | Large-scale replication (b03) | [E] K04 |
| Memory demand needed | N=24 per experiment. Match effect about 150 ms at 0 ms ISI rising to about 250 ms at 500 ms ISI. Flashed-only colour: none or weak | Niu and Hollingworth 2026 (b07) | [E] K09 |
| Irrelevant feature of held object also captures | N=22. Neutral 998; irrelevant-match 1,036 (p=.001); relevant-match 1,065 (p<.001); conjunction 1,055 | Gao et al. 2016 (a17) | [S] |
| First saccade goes to the match | Natural scenes: distractor fixated on 23.6% of trials vs 11.0% when mismatching | Bahle et al. 2018 (b05) | [S] K06 |
| Template leaves working memory with repetition | Exp 1 N=20: CDA -0.8 uV (1 target), -1.5 (2 targets), r=-0.68 with speed. Exp 2 N=10 constant target: no CDA. Exp 3 N=18: -0.66, -0.50, -0.30 uV over trials 1-2, 3-4, 5-7, p<.05 | Carlisle et al. 2011 (a18) | [E] K07 |
| Deprioritised item does not capture | No observable capture though still remembered (continuous report) | Hollingworth and Hwang 2013 (b15) | [E] K07 |
| Bias fades over repeated memorising | Within one or two trials, while memory improves | cited in a20 | [E] K08 |
| Capture decays with lag; erased by effort | N=58. Lag 2 75.2% vs lag 7 81.9%, t(57)=3.22, p=.002, d=0.42. With arithmetic 80.0 vs 80.1% (BF=6.96 for no difference) | Sasin and Nieuwenstein 2016 (a21) | [E] K09 |
| Matching distractors are suppressed after capture | N=12. Pd 250-300 ms, t(11)=3.4 to 4.0; Pd onset about 220 ms vs about 120 ms for singletons | Sawaki and Luck 2011 (b08) | [S] K10 |
| Storage and attention separable inside working memory | N=30. Recall error invalid 18.97 vs valid 12.92 deg; cue effect 8.27 deg at 80% valid vs 3.83 at 50% | Gunseli et al. 2019 (a34) | [S] |
| Negative templates mostly fail | Becker 2015: no advantage in 3 experiments; also Berggren and Eimer 2021, Williams 2020, Cunningham and Egeth 2016, four unpublished nulls | b11 | [C] K11 |
| Capture costs time more than errors | Match slows search; no extra accuracy cost | Kim et al. 2026 (d06) | [S] K27, abstract |
| Task-switch cue does not remove capture | Two pre-registered experiments | Hautekiet et al. 2026 (d05) | [S] K26, abstract |
| Irrelevant sentence in maths problems | code-davinci-002 COT micro 72.4%, macro 6.0%. No more than 18% of baseline-solved problems stay solved across all distractor types. text-davinci-003 macro 0 on role-overlap distractors with more than 2 steps | Shi et al. 2023 (a31, b17) | [S] K12 |
| Mitigations on GSM-IC | Ignore instruction: micro 72.4 to 77.8, macro 6.0 to 15.0. COT+SC micro 88.1, macro 30.0. LTM+SC micro 93.4, macro 45.0 | Shi et al. (b18, c01) | [E] K13 |
| Related distractors hurt more | Wrong answer entity is in context in 77% of errors with low-ranked context vs 37% with random context. 73% of 240 retrieval-caused errors match automatic errors | Yoran et al. 2024 (c07); Wu et al. 2024 (c06) | [E] K14 |
| Lost in the middle | GPT-3.5 closed-book 56.1%, oracle 88.3%; Claude-1.3 48.3%, oracle 76.1%. Middle answer falls below closed-book at 20 and 30 documents. Drop above 20 points. Extra documents add about 1.5 points | Liu et al. 2023 (a32) | [E] K18 |
| Token entrainment | Llama-3.1-8B logit shift: related +4.08, irrelevant +4.92, random +4.01. Correct-token shift +0.75 / -1.23 / -1.17. Heads 2.9-10.7%; 36 heads (3.5%) for country-capital. Ablation widens gap 7.69 to 13.20 | Niu et al. 2025 (a33, b20) | [E] K15 |
| Entrainment scaling | Cerebras-GPT: counterfactual b=-0.330 (R2 0.926), related -0.135, irrelevant +0.091, random +0.217. Largest about 4x more resistant to counterfactual, about 2x more prone to arbitrary copying | Kukreja et al. 2026 (b21) | [E] K16 |
| Sentence-level entrainment | Llama-3.1-8B 79.4% to 22.4% with counterfactual sentence. 6-model mean 74.1 none, 55.9 factual, 46.5 counterfactual, 69.8 own earlier answer (-4.3) | Liu and Chu 2026 (d09) | [S] K28 |
| Instruction tuning and head masking | Tuning shrinks loss from -25.5/-31.9/-13.5 to -15.3/-9.5/-4.5. Masking 2-4% shared heads: -2.3 clean cost vs -6.8 per-relation | d10 | [S] K28 |
| Adaptive distractors | 7-model mean 0.843 to 0.323 (52.0% drop). Claude-3.5-Sonnet 0.879 to 0.495 (38.4 points absolute). Static GSM-IC: 1.8% drop | Adaptive Distraction (b23) | [E] K17 |
| Anchoring in LLMs | 22% to 61% of questions. Qwen2.5-0.5B 60.5%, GPT-4o 27.3%, Qwen3-235B thinking 22.0%, DeepSeek-R1 25.0%. Knowledge prompt made Llama-3.1-8B worse (34.7 to 50.5%) | Huang et al. 2025 (b22) | [E] K19 |
| Bias prompts and sycophancy | Accuracy down by up to 36% (BIG-Bench Hard, GPT-3.5, Claude 1.0); wrong user suggestion down up to 27% | Turpin 2023 (c03); Sharma 2023 (c04) | [E] K19 |
| Errors spread through held output | Snowballed hallucinations in 95% of failures; GPT-3.5 keeps first answer 74.7% (GSM8K); length-bias A=13.18, authority A=0.00 | c10, c11, c17 | [E] K20 |
| Inverse scaling on negation | NeQA 1,428 items; larger models below random beyond about 10^22 FLOPs | McKenzie et al. 2023 (d12) | [E] (not on lessons) |
| Adaptive attack beats prompt fixes | Prompt mitigations within +/-0.03 | b23 | [E] K13 |

## 4. Mechanisms and models

### 4.1 Biased competition as an algorithm

State: a set of candidate items, each with a stimulus-drive score. A top-down bias from the held template multiplies or adds to the score of items whose features match. Items then compete by mutual suppression (divisive normalisation). The winner is read out.

Reynolds and Heeger 2009 (a24): response = (stimulus drive x attention field) / (suppressive drive + sigma). The suppressive drive pools neighbouring responses. This gives biased competition for items in the same pool and feature-gain effects across pools. (Described from the abstract record; not numerically read.)

Engineer's version for an agent: score(item) = relevance(item, task) + w x similarity(item, held lessons). The danger term is w x similarity when the item is a distractor. Fixation means w is too large, or similarity is measured on surface wording rather than on the structure that matters.

### 4.2 Why the human data are mixed

The best-supported reconciliation (b01, b03, b04, b25):

- Only items in an active template state bias attention. Which items are active is set by the task.
- More matching items give more pull (68 to 124 ms).
- Capture decays with time and with effortful intervening work (a21).
- Repetition turns a held item into a routine and the template leaves working memory (a18).
- After capture, a late suppression step may reject the match (b08).

Confound to remember: "load" is mixed with number of items, template state and memory accuracy (84.6% vs 68.4%, per critique). The Woodman and Luck benefit with three items fits "use the memory to reject".

### 4.3 What the LLM analogues look like

- **Attention-head copying** (Niu et al., b20). A small set of heads (2 to 10% of heads) raises the logit of any token seen in context. It acts on random tokens too. This is a similarity-free copying force, different from feature-match capture.
- **Racing thoughts** (b24). Distractor text drives accuracy on context-dependent questions toward 50%. Hypothesis: late tokens read early tokens before those are contextualised. Backpatching gave 30+ points in some settings.
- **Retrieval by similarity** (c16). Agents copy output of stored records when the new input resembles the stored input. Errors in stored records spread.
- **Position bias** (a32, c19). U-shape: start and end of context favoured.

### 4.4 Implementable control points

1. A held lesson is only a template if it is restated or active. Keep stored lessons out of the prompt unless retrieved for the current task (K02, K07).
2. Rank retrieved lessons by structure match to the current problem and by evidence of success, not by surface similarity alone (K14, K21).
3. A late reject check: before using any lesson-derived element, ask whether the stated goal needs it (K10, untested in LLMs).
4. Insert intervening work between lesson and use (K09). This is a human finding only.

## 5. What holds up

### 5.1 Replicated

- Memory-matching distractors slow search under many conditions: Soto lab, Hollingworth lab, Olivers lab, several two-item replications (Chen and Du 2017; Fan 2019, 2021; King and Macnamara 2020; Zhang 2018; Zhou 2020) (b04).
- Capture scales with number of matching held items (b01, b03). Large-sample replication: Bayes factors 0.12 to 0.16 for no difference at load 2 with a single match.
- Capture needs an active template and a memory demand (b07, b15, a18).
- Entrainment in LLMs: Niu et al. 2025, replicated by Liu and Chu 2026 and Zheng and Shi 2026 (d09-d11) with overlapping method. Not fully independent.
- LLMs lose accuracy to related irrelevant context (Shi, Wu, Yoran, adaptive attack).

### 5.2 Failed or conflicting

- Woodman and Luck 2007 found no capture at one item with long delay and a benefit at three items. Soto and Humphreys 2008 found costs at one or two items. Hollingworth and Beck 2016 found capture at one item but not reliably at two with one match.
- Presence versus match is task dependent (b02).
- Negative templates fail in about 8 experiments across labs (b11). The one positive (Arita 2012) did not replicate.
- Hollingworth notes some early null experiments were underpowered (b12).
- Samples are small (N=10 to 24); one key contrast is p=.077 (K24).
- Founding papers were never opened in full, so original effect sizes are missing.

### 5.3 Moderators

| Moderator | Direction | Source |
|---|---|---|
| Consolidation time (ISI) | longer raises effect (150 to 250 ms) | b07 |
| Number of matching items | more raises effect | b01 |
| Task-active vs deprioritised | deprioritised gives no capture | b15 |
| Search demand and delay | demanding search or long delay removes capture | a14 |
| Search mode | feature search raises capture vs singleton mode | d08 |
| Working memory capacity | higher WMC lowers dwell on fixated distractor | d07 |
| Verbalisability of content | hard-to-verbalise content captures more | a15 |
| Repetition | bias falls within 1 to 2 trials | a20 |
| Intervening effort | arithmetic erases the decay pattern | a21 |
| Task-switch cue | does not remove capture | d05 |
| Measure | time and first fixation show it, accuracy may not | d06, b05 |

### 5.4 Interventions

Worked (partly): ignore instruction (+5.4 micro, +9.0 macro on GSM-IC); exemplars with distractors; self-consistency; fine-tuning on mixed contexts (Yoran); DPO training (adaptive attack paper); instruction tuning cut entrainment loss 40 to 70%; head masking (needs weights); history-based deletion with a strict evaluator for memory (c16); LLM consolidation cut length-bias propagation 84% (c17).

Did not work: prompt mitigations against adaptive distractors (within +/-0.03); knowledge-enhancement prompt on anchoring (worse); complicated prompts on multi-step problems; self-correction without external feedback; negative templates in humans; query-before-documents for lost-in-the-middle.

## 6. Language models

### 6.1 Behaviour that mirrors the human pattern

- **Similarity raises the pull.** Related irrelevant text misleads more than unrelated (Wu 2024, c06). Wrong answers copy entities from low-ranked context in 77% of errors vs 37% with random context (c07). Role-name overlap in GSM-IC hurts most (a31).
- **More distractors hurt more** (c06). Padding alone drops accuracy 0.92 to 0.68 at 3,000 tokens (c08).
- **Held output is a template.** The model's own earlier answer costs 4.3 points as context (d09). Snowballing in 95% of failures (c10). Laban 2025: 39% average drop in multi-turn (c09).
- **User-stated belief acts as a template.** A wrong suggestion cuts accuracy up to 27% (c04). Bias features shift answers by up to 36% and chain-of-thought never mentions them (c03).
- **Anchoring.** 22% to 61% of questions; reasoning models lowest (b22).

### 6.2 Where LLMs differ from humans

- Entrainment hits random and irrelevant tokens (+4.92 for irrelevant) in Llama-3.1-8B. This is not a feature-match effect (critique, contradiction 4).
- Scale: larger models resist counterfactual context more but copy arbitrary tokens more (b21). Liu and Chu (d09): Qwen3 3.91 at 0.6B to 3.35 at 32B.
- Position effects have no strong human analogue in this literature (a32).
- Static distractors barely hurt modern models (1.8% on GSM-IC) while adaptive ones cut accuracy 52% on average (b23).

### 6.3 What changed it, by how much

| Change | Effect | Source |
|---|---|---|
| Ignore instruction (code-davinci-002 COT) | micro +5.4, macro +9.0 | b18 |
| Self-consistency, 20 samples | micro +11 points | b17 |
| LTM + SC | micro 93.4, macro 45.0 | c01 |
| Instruction tuning | entrainment loss down 40-70%, 4.5 to 15.3 points left | d10 |
| Head masking (2-4% heads) | with-context +1.5 to +7.9, clean -2.3 | d10 |
| Fine-tuning on mixed contexts | restores robustness | c07 |
| DPO | most effective of tested fixes against adaptive distractors | b23 |
| Reasoning models | lowest anchoring (22-25%) | b22 |
| Larger model | less counterfactual entrainment, more random copying | b21 |

### 6.4 Not tested

No LLM study crosses held-content match with task load (c27, d14). Working-memory-limit studies exist (c13 n-back drop at n=3; c14 best models 90.08% at n=8; c15 two small models at 0% even in clean controls, a floor effect). They do not test load theory. An attention-dispersion account of capacity exists (c22, snippet only).

ENTRAP-VL (2607.20092) and the other 2026 entrainment papers seen only in listings were not read.

## 7. What our agent should take

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Retrieve lessons per task by structure match and past success, not by surface similarity alone. Agents copy records that resemble the query. | memory | [E] | K14, K21; c07, c16 |
| Do not keep every lesson in the active prompt. Only items that serve the current goal act as templates; stored ones barely bias. | memory / S1 | [E] (human evidence; LLM by analogy) | K02, K07; b04, b15, a20 |
| Gate memory writes. One bad lesson spreads to later tasks. Use a strict evaluator and deletion by history. | memory / G2 | [E] | K20; c16, c17 |
| Position the lesson deliberately. Middle placement loses information. Put the task-critical item at the start or end. | S1 / memory | [E] | K18; a32, b19 |
| Do not rely on an ignore instruction alone. It gives a few points. Use code-side selection (voting, checks). | G5 | [E] | K13; b18, b23 |
| Do not trust a prompt-only fix against adaptive distractors. Test with a search-based attack, not static ones. | G7 | [E] | K17; b23 |
| Keep context short. Padding itself costs accuracy. | G11 | [E] | K18; c08 |
| Count steps and tokens as well as errors when judging a lesson's pull. | G7 | [S] for LLMs | K27; d06 |

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Matching-lesson bias scales with number of matching lessons, not number held. | memory | [E] human, untested in LLMs | K04, K05; b01, b03 |
| Load x match: does a held lesson matching a distractor hurt more under high task load? | G / S | [C] | K03, K23 |
| Positive wording beats "do not" lessons. | G | [C] | K11; b11, d12 |
| Restating a lesson each step raises pull; one-time display fades. | S / memory | [E] human | K07, K08 |
| Late reject step (does this lesson element serve the goal?). | O | [S] | K10 |
| Delay or unrelated work between lesson and use reduces pull. | S | [E] human | K09 |
| Lesson position x similarity. | memory | open | K29 |
| A "now do the task" reminder does not remove pull. | G | [S] | K26 |
| The agent's own earlier notes entrain as context does. | memory | [S] | K28 |

## 8. Concrete tests on our bench

All arms use equal tokens. Run 30+ seeds and report Bayes factors or confidence intervals (K24). Log steps and tokens as well as errors (K27).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Match vs neutral lesson | Tasks with a distractor that shares wording with a held lesson | (a) lesson matches distractor; (b) neutral lesson of same length; (c) no lesson | Distractor-following rate; accuracy | (a) worse than (b) by several points (K14) |
| T2 Load x match | Same items, easy vs hard (more steps or more held facts) | 2x2 plus no-lesson control | Interaction on error rate | Biased competition predicts a bigger match cost at high load; load theory predicts more cost from any distractor. Either result is informative |
| T3 Match count | 1, 2, 4 lessons matching the same distractor, total held count fixed | Matching count vs held count | Distractor-following rate | Rises with matches (68 to 124 ms human pattern) |
| T4 Positive vs negative lesson | "Use Y" vs "Do not use X" | Equal length | Error rate; mention rate of X | Negative lessons raise X use (NeQA, human nulls) |
| T5 Restate vs once | Multi-step tasks over 8 turns | Restate each step; show once; show once and repeat across tasks | Bias by turn | Restate stays high; repeated routine fades |
| T6 Delay | Insert 0, 2, 5 unrelated steps between lesson and use | Equal tokens through padding of different type | Bias vs lag | Decays, as in Sasin and Nieuwenstein |
| T7 Position x similarity | Lesson at start, middle, end; similar vs dissimilar to distractor | 3x2 | Error rate | Middle weakest use; a similar lesson near the end pulls most |
| T8 Late reject | Add a check after retrieval: "which lesson parts does the goal need?" | With vs without check, equal tokens | Distractor-following; correct-use rate | Cuts following without hurting correct use |
| T9 Retrieval policy | Top-k by surface similarity vs by structure | Equal k | Accuracy; copying of wrong record | Structure retrieval wins when a lookalike record is wrong |
| T10 Bad-lesson spread | One wrong lesson planted | Ungated write vs gated | Spread rate to later tasks | Gate cuts spread |
| T11 Adaptive attack | Search for the worst distractor lesson | Plain vs scaffold | Accuracy drop | Static tests underestimate the drop (1.8% vs 52%) |

## 9. What does not transfer, and why

- **Millisecond effects.** Human costs are 55 to 124 ms in search. An LLM has no response time. Use error rate and steps.
- **Visual features.** Colour, shape and gap location do not map to lesson text without a similarity definition. Define match by shared entity, shared role, shared template.
- **Neural markers.** CDA, Pd, N2pc and single-cell suppression times (90 to 120 ms) have no counterpart in a prompt.
- **Verbal recoding and articulatory suppression.** The LLM has no separate verbal loop.
- **Working memory load as a trade-off with control.** An LLM context is not a limited-capacity buffer in the same sense. Context length and position effects are the nearest analogue. Capacity studies give contradictory or floor results (c13-c15).
- **Automatic versus strategic.** Human capture may depend on strategy. LLM entrainment acts on random tokens in a mechanical way (b20), so part of it is not an attention-to-match effect at all.
- **Small human samples** (N=10 to 24) limit effect-size transfer (K24).
- **Static distractors** barely hurt modern models, so positive human findings may not show up without adaptive search.

## 10. Open questions

1. Does a held lesson that matches a distractor hurt more under high than low load in an LLM agent? (No study; gap 1.)
2. Is bias set by the number of matching lessons or the number held in an LLM? (gap 2)
3. Do "do not" lessons help or hurt on current RLHF models? NeQA used older models. (gap 3)
4. Does restating each step increase pull compared with one display? (gap 4)
5. Exact numbers in Desimone and Duncan 1995, Chelazzi 1993/1998 and Downing 2000 are missing.
6. Effect sizes in the 2026 capture papers (Hautekiet; Kim; Liu; Won and Zhang) are missing.
7. Does position of the held lesson interact with similarity? (gap 8)
8. Does a late reject step filter matching distractors at no cost to correct use? (gap 9)
9. Is there lag decay of a held lesson's influence in LLMs? (gap 10; Laban 2025 is the nearest)
10. Can entrainment be suppressed at prompt level? Both 2026 papers needed model weights (d10, d11).
11. Which of the four rival accounts (single template, multiple templates, capture then suppression, learned statistics) fits LLM agents? Not asked of any model.
12. Do reasoning models (lowest anchoring, 22 to 25%) show less lesson-match pull? Untested.

## 11. Sources

[V] = opened (full text, or the abstract record where the evidence file says so). [M] = snippet or citation only.

**Founding and human behaviour**
- [M] Desimone and Duncan 1995. https://www.annualreviews.org/doi/10.1146/annurev.ne.18.030195.001205
- [V] Chelazzi et al. 1993 (abstract). https://doi.org/10.1038/363345a0
- [V] Chelazzi et al. 1998 (abstract). https://doi.org/10.1152/jn.1998.80.6.2918
- [V] Downing 2000 (abstract). https://doi.org/10.1111/1467-9280.00290
- [M] Soto, Heinke, Humphreys, Blanco 2005. https://doi.org/10.1037/0096-1523.31.2.248
- [V] Soto and Humphreys 2008. https://link.springer.com/content/pdf/10.3758/PP.70.5.924.pdf
- [V] Woodman and Luck 2007. https://pmc.ncbi.nlm.nih.gov/articles/PMC2048820/ (journal: https://doi.org/10.1037/0096-1523.33.2.363)
- [M] Han and Kim 2009. https://doi.org/10.1037/a0016452
- [M] Olivers, Meijer, Theeuwes 2006. https://doi.org/10.1037/0096-1523.32.5.1243
- [M] Soto and Humphreys 2009. https://doi.org/10.1027/1618-3169.56.3.165
- [V] Gao et al. 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC4783775/
- [V] Carlisle et al. 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3147306/
- [M] Olivers et al. 2011. https://doi.org/10.1016/j.tics.2011.05.004
- [V] Van der Stigchel and Olivers 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6688549/
- [V] Sasin and Nieuwenstein 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC5133283/
- [M] Soto et al. 2008 review. https://doi.org/10.1016/j.tics.2008.05.007
- [M] De Fockert et al. 2001. https://doi.org/10.1126/science.1056496
- [V] Gunseli et al. 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6751203/
- [V] Hollingworth and Beck 2016. https://hollingworth.lab.uiowa.edu/sites/hollingworth.lab.uiowa.edu/files/2024-06/2016-Hollingworth-Memory-based%20attention%20captu.pdf
- [V] Large-scale replications of van Moorselaar et al. 2014 and Hollingworth and Beck 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC6856200/
- [V] Hollingworth 2022 chapter (also source for Bahle et al. 2018, 2020, Hollingworth and Hwang 2013, negative-template summary). https://hollingworth.lab.uiowa.edu/publications
- [V] Niu and Hollingworth 2026. https://dx.doi.org/10.1037/xge0001947
- [V] Sawaki and Luck 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3204803
- [V] Dowd et al. 2017; Zhou et al. 2020 (via thesis summary). https://fse.studenttheses.ub.rug.nl/28473/1/report_minor_DianaMP.pdf
- [V] Hautekiet et al. 2026 (abstract). https://doi.org/10.31234/osf.io/8n9vt_v1
- [V] Kim et al. 2026 (abstract). https://doi.org/10.3758/s13421-026-01924-z
- [V] Liu, Wang, Liu 2026 (abstract). https://doi.org/10.31234/osf.io/fkt9c_v1
- [V] Won and Zhang 2025 (abstract). https://doi.org/10.3758/s13414-025-03147-x

**Machine models of biased competition**
- [M] Reynolds and Heeger 2009. https://doi.org/10.1016/j.neuron.2009.01.002
- [M] Deco and Rolls 2005. https://doi.org/10.1016/j.pneurobio.2005.08.004 ; https://doi.org/10.1016/j.neuroimage.2004.12.009
- [M] Deco and Rolls 2004. https://doi.org/10.1016/j.visres.2003.09.037
- [V] Adeli and Zelinsky 2018. https://arxiv.org/abs/1811.09699

**LLM studies**
- [V] Shi et al. 2023. https://arxiv.org/abs/2302.00093
- [V] Liu et al. 2023, Lost in the middle. https://arxiv.org/abs/2307.03172
- [V] Niu et al. 2025, Llama see, llama do. https://arxiv.org/abs/2505.09338
- [V] Kukreja et al. 2026. https://arxiv.org/abs/2604.13275
- [V] Liu and Chu 2026. https://arxiv.org/pdf/2606.24077
- [V] Zheng and Shi 2026. https://arxiv.org/pdf/2610.18674
- [V] Huang et al. 2025, anchoring. https://arxiv.org/abs/2505.15392
- [V] Adaptive Distraction. https://arxiv.org/abs/2502.01609
- [V] Racing thoughts. https://arxiv.org/abs/2410.02102
- [V] Turpin et al. 2023. https://arxiv.org/abs/2305.04388
- [V] Sharma et al. 2023. https://arxiv.org/abs/2310.13548
- [V] Echterhoff et al. 2024. https://arxiv.org/abs/2403.00811
- [V] Wu et al. 2024. https://arxiv.org/abs/2404.03302
- [V] Yoran et al. 2024. https://arxiv.org/abs/2310.01558
- [V] Levy et al. 2024. https://arxiv.org/abs/2402.14848
- [V] Laban et al. 2025. https://arxiv.org/abs/2505.06120
- [V] Zhang et al. 2023. https://arxiv.org/abs/2305.13534
- [V] Huang et al. 2024, self-correction. https://arxiv.org/abs/2310.01798
- [V] Chen et al. 2024, premise order. https://arxiv.org/abs/2402.08939
- [V] Gong et al. 2024, n-back. https://arxiv.org/abs/2305.03731
- [V] Hu and Lewis 2025. https://arxiv.org/abs/2412.18120
- [V] Adapala 2025. https://arxiv.org/abs/2509.19517
- [V] Xiong et al. 2025. https://arxiv.org/abs/2505.16067
- [V] Memory Contagion 2026. https://arxiv.org/abs/2606.23195
- [V] Shinn et al. 2023, Reflexion. https://arxiv.org/abs/2303.11366
- [V] Guo and Vosoughi 2024. https://arxiv.org/abs/2406.15981
- [V] Liang et al. 2026. https://arxiv.org/abs/2601.07470
- [V] McKenzie et al. 2023, Inverse scaling. https://arxiv.org/pdf/2306.09479
- [M] Gong and Zhang 2024. https://nips.cc/virtual/2024/102121
- [M] Zhou, Frank, McCoy 2024. https://arxiv.org/abs/2406.18501
- [M] Jumelet et al. 2024. https://arxiv.org/abs/2406.04847
- [M] ENTRAP-VL (2607.20092), arXiv listing only.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 18 established claims: 13 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A07.03-K01** (reworded: the sources support less). Numbers match Soto and Humphreys 2008 (58-86 ms), but the three contrasts are not all one held item with a short gap: Exp 1 spanned gaps of 188-1008 ms with no shrinkage, Exp 2 used articulatory suppression, and Exp 3 (1,101 vs 1,015) held two items; all three are one paper. Corrected claim: Held visual contents bias attention toward matching items: in Soto and Humphreys 2008 a distractor matching the held item slowed search by about 60-85 ms against neutral (Exp 1, one item, gaps 188-1008 ms: 1,209 vs 1,146 ms; Exp 2, with articulatory suppression: 1,049 vs 991 ms; Exp 3, two held items: 1,101 vs 1,015 ms), and Hollingworth and Beck 2016 found a 68 ms capture effect with one held colour.
- **A07.03-K05** (reworded: the sources support less). Holds only for the gap-location task: there capture was 124 ms (two matches) vs 44 ms (one match) at memory load 2 and 68 ms for one item; in the singleton task of the same paper, Match-2 (51 ms) was no larger than load-1 Match-1 (58 ms), and the large-sample replication (Fratescu et al. 2019) found no capture at load 2 in its other paradigm. Corrected claim: In the gap-location task, capture was larger with two matching distractors than one when two colours were held (Match-2 124 ms vs Match-1 44 ms at load 2; Match-1 at load 1 was 68 ms; Hollingworth and Beck 2016, N=24), replicated in the Match-2 > Match-1 pattern by Fratescu et al. 2019 (BF10 = 158); the singleton task showed no such scaling (51 vs 58 ms).
- **A07.03-K07** (reworded: the sources support less). The CDA part is supported by Carlisle et al. 2011 (-0.80 uV at repetition 1, binned -0.66/-0.50/-0.30 uV; the -0.8 to -0.30 pairing mixes a single trial value with a 5-7 bin), but the opened sources do not show that deprioritised held items do not capture (Hollingworth and Hwang 2013; Olivers 2011): Van der Stigchel and Olivers 2019 does not mention those studies, and the Hollingworth chapter page lists only a citation. Corrected claim: When the same target is searched repeatedly, the contralateral delay activity declines (-0.66 uV on repetitions 1-2 to -0.30 uV on 5-7, not different from zero from repetition 5; Carlisle et al. 2011), taken to mean that long-term memory takes over from working memory as the template; with a constant target across the experiment there was no CDA. Memory-driven bias also drops within one or two repeated memorisations (Van der Stigchel and Olivers 2019).
- **A07.03-K15** (reworded: the sources support less). Niu et al. numbers all verified (+4.01, +4.92, +4.08, 3.2-10.7% of heads, 36 heads = 3.5%, gap 7.69 to 13.20), but Liu and Chu (sentence-level, different models and intervention, 2-4% shared heads) and Zheng and Shi (head-recovery metric 1.464) extend and are consistent with the finding rather than replicate the Llama-3.1-8B logit results. Corrected claim: Llama-3.1-8B raises the logit of any token already in context, even random (+4.01) or irrelevant (+4.92) vs related (+4.08); a small set of heads (3.2-10.7%; 36 heads = 3.5% for country-capital) mediates it, and ablating them widens the counterfactual logit gap 7.69 to 13.20 (Niu et al. 2025). Two 2026 papers extend this: Liu and Chu find a shared set of 2-4% of heads controlling sentence-level entrainment, and Zheng and Shi find a shared global head core across relations (average recovery 1.464).
- **A07.03-K16** (reworded: the sources support less). Kukreja numbers verified (b=-0.330, +0.217, 4x, 2x), but Liu and Chu do not confirm the counterfactual trend: they report counterfactual entrainment rising slightly with model size, i.e. resistance more pronounced in smaller models, which contradicts Kukreja; only the overall decline with size (Qwen3 3.91 to 3.35) agrees. Corrected claim: Kukreja et al. (Cerebras-GPT, Pythia) find larger models resist counterfactual context more (b=-0.330; largest about 4x more resistant) but copy arbitrary tokens more (+0.217; about 2x). Liu and Chu 2026 (26 LLMs) agree that overall entrainment falls with size (Qwen3 3.91 at 0.6B to 3.35 at 32B) but find counterfactual entrainment rising slightly with size, contradicting Kukreja on that point.
