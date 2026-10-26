# Attentional capture, bottom-up versus top-down: deep document

*Subfield A07.04. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K30), critique.md in this folder. Status tags: [E] established, [S] single-source, [C] contested. [V] = page or PDF text opened, [M] = snippet or second-hand only.*

## 1. What it is

Attentional capture is the case where something pulls attention to itself although the observer did not choose to look at it. The two poles are:

- **Bottom-up (stimulus-driven):** a sudden onset, a bright or odd-coloured item, a loud change. It wins because of how it differs from its surroundings.
- **Top-down (goal-driven):** the observer holds a goal (find the red item, find the letter) and attention goes to what matches that goal.

The core question for 30 years: can a goal stop a salient but irrelevant item from taking attention? The classic tasks are:

- **Additional-singleton task (Theeuwes 1992).** Find the odd shape (one diamond among circles). Report the tilt of the line inside it. An irrelevant red circle slows the search.
- **Spatial cueing (Folk, Remington and Johnston 1992).** An irrelevant cue appears just before the target. If the target is found faster at the cued place, the cue captured attention.
- **Visual search with onsets (Yantis and Jonides 1984).** Abrupt onsets as targets.

Why it matters for our agent (schema step S1, input hygiene): a language model reads everything in its context. A planted hint, a stated guess, an irrelevant number or an extra clause can pull the answer. This is the LLM version of an irrelevant colour singleton. The analogy is loose. Humans orient in space and time. A model has one pass of attention over tokens. The useful part is the design lesson: pull depends on three things (the goal in force, how salient the item is, and what has paid off before), and control works best when set before the input arrives.

Scope note. Human capture work is about vision. All LLM studies below are about distraction in text. No paper tests human-style contingent capture in an LLM with a goal-match manipulation (critique, weak spots). Heuristics, anchoring and sycophancy are covered here only where they act as planted-input pull. Neighbouring subfields in this run: Heuristics and biases, Bias and debiasing, Diagnosticity of evidence, Question wording and presupposition.

## 2. History and theories in depth

**1984-1992: the first claims.**
- Yantis and Jonides (1984) [M]: abrupt onsets grab attention even when they are not the target. Exact slopes not retrieved (a20).
- Koch and Ullman (1985) [M]: saliency map plus winner-take-all. The most conspicuous location wins (a18).
- Theeuwes (1992) [M, second-hand]: an irrelevant colour singleton slows search for a shape singleton. The cost shrinks when the colour difference is small. Exact 1992 ms values were not read (a01). His reading: the most salient item wins the first shift of attention, independent of the goal (a04).
- Folk, Remington and Johnston (1992) [V abstract]: four experiments. Invalid abrupt-onset precues slowed onset targets, not colour-change targets. Invalid colour precues slowed colour targets more than onset targets. Their reading: capture happens only when the cue's property matches the control setting induced by the task (b10, a02). Quote: "Stimuli not exhibiting these properties will not involuntarily summon attention."

**1994-2004: the argument over small versus large displays.**
- Bacon and Egeth (1994) [M]: when the target is not the only odd shape, the colour singleton stops interfering. They proposed a "singleton detection mode" versus "feature search mode" (a06).
- Folk, Remington and Wright (1994) [M] and Remington, Folk and McLean (2001) [M]: contingent capture for apparent motion; capture versus delayed allocation. Snippets only.
- Theeuwes (2004) [V]: re-ran Bacon and Egeth with bigger displays. The singleton still interfered. With small displays the cost vanished, but search had become serial. His conclusion: top-down search strategy cannot override capture (a05, b04).
- Theeuwes, Kramer and Kingstone (2004) [V] and Theeuwes and Chen (2005) [V]: capture is real in perception, not only in RT. A distractor lowers detection of a brief target (a07, a08).

**1998-2008: contingent capture refined.**
- Folk and Remington (1998) [V]: a different-colour distractor cost 26 ms; cost appeared at 100 and 150 ms SOA, none at 50 ms (a09).
- Eimer and Kiss (2008) [V]: ERP evidence that capture follows task set (b03).
- Folk, Leber and Egeth (2008) [V]: contingent control extends to non-spatial settings, the attentional blink (a10).
- Yeh and Liao (2008) [V abstract]: the Folk pattern held only when set size 4 was used throughout. Mixing set sizes 4 and 8 produced onset capture even at set size 4 (b11).

**2010-2021: a third source and a third camp.**
- Gaspelin, Leonard and Luck (2015) [V]: direct evidence for active suppression of salient but irrelevant items. This is the "signal suppression" camp: a salient item makes a priority signal, and the system can suppress it before attention lands (a11).
- Anderson, Laurent and Yantis (2011) [V] and Failing et al. (2015) [V]: reward history makes a non-salient item capture (a14, b12).
- Awh, Belopolsky and Theeuwes (2012) [V]: the top-down versus bottom-up split is a failed dichotomy. They add selection history as a third source (a15).
- Luck, Gaspelin, Folk, Remington and Theeuwes (2021) [V]: the main opponents wrote a joint paper. Shared points: salient items make a priority signal and capture if nothing stops them; control can stop capture. Still open: whether control can beat very high salience, and the role of set size (a03, b01, b02). They also name two method problems: no independent measure of the control setting a task induces, and no direct measure of capture (fast reorienting hides it in cueing designs) (a04).
- Anderson (2021) [V]: "time to stop calling it attentional capture". The question has become one of weights on a priority map (a16).

**Models.**
- Itti, Koch and Niebur (1998) [V]: saliency model with 42 feature maps (a17).
- Wolfe (2021) [V]: Guided Search 6.0, top-down guidance plus bottom-up salience on one priority map (a19).
- Luck et al. (2021) common framework: proactive control (boost features before onset) and reactive control (boost or suppress locations after the first allocation) (a28).

**2023-2026: the LLM turn.** Work on distraction in language models starts with Shi et al. (2023). It is not framed in capture terms. The link is by analogy (see section 6).

## 3. Core findings with exact numbers

Human capture, then LLM distraction. "Status" uses the claims file.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Irrelevant colour singleton slows search for a shape singleton in large displays | 950 vs 885 ms (65 ms cost), F(1,7)=37.1, N=8, displays of 12 and 20; slopes about -0.55 vs 0.38 ms/item (no display-size effect) | Theeuwes 2004 (a05, b04) [V] | [E] |
| The same cost vanishes in small displays, where search turns serial | No distraction effect, F<1; slopes 13.1 and 11.1 ms/item; N=8, sizes 5 and 9 | Theeuwes 2004 (a05) | [E] boundary |
| Bacon and Egeth: varied shapes remove the cost | Slopes up to 11.5 ms/item in the non-interfering conditions | via Theeuwes 2004 (a06) [M] | [E] |
| Capture lowers perceptual sensitivity | d' 1.52 vs 1.37 (distractor); near 1.30, far 1.46; F(1,13)=6.67; N=14 | Theeuwes, Kramer, Kingstone 2004 (a07) [V] | [S] lab |
| Sensitivity loss is at the distractor's location | d' at distractor location 2.626 vs 1.556 baseline (N=8, 190 ms exposure) | Theeuwes and Chen 2005 (a08) [V] | [S] lab |
| Contingent capture: matching cue captures, mismatched does not | Four experiments; no ms in abstract. Meta-analysis of 64 experiments agrees; moderators: target a singleton, pure vs mixed blocks | Folk et al. 1992 (b10); Buesel et al. 2020 (b09) [V] | [E] |
| Folk and Remington 1998 distractor cost and timing | 26 ms, F(1,22)=4.76; at SOA 100 ms F(1,23)=9.49, 150 ms F(1,23)=13.47, none at 50 ms | a09 [V] | [E] |
| Contingent capture extends to attentional blink | Exp 1 N=38, F(2,72)=66.10; Exp 2 N=23, F(2,44)=5.23 | Folk, Leber, Egeth 2008 (a10) [V] | [E] |
| ERP: capture follows task set | Colour task 37 ms faster at cued spot, t(11)=5.5; onset task none; N2pc colour F(1,11)=13.3 vs onset F=1.6 | Eimer and Kiss 2008 (b03) [V] | [E] |
| Active suppression of a salient singleton | Singleton-detection mode: RT 739 vs 674 ms (65 ms cost); probe recall 26.6% at singleton vs 14.7%. Feature search: RT 667 vs 678; recall 9.6% vs 15.4%. Set size 4: recall 15.5% vs 27.9%. N=24 each | Gaspelin, Leonard, Luck 2015 (a11) [V] | [C] vs Theeuwes camp |
| Suppression needs a predictable feature | Random colour: RT cost 15 ms (665 vs 650), probe 37% vs 36% (BF 4.18 for null), N=24. Eyes: first saccade to singleton 17% vs 10% per other item, N=28. Blocked colour: suppression about -0.3% in first quarter to about 6% in last | Gaspelin and Luck 2018 (b07) [V] | [E] |
| Set-size dispute | Wang and Theeuwes: suppression at 4, none at 6 or 10. Stilwell and Gaspelin: 4 experiments, suppression at 10 and 30 (called a floor effect) | Luck et al. 2021 (b08, b01) [M for the originals] | [C] |
| Location regularities cut capture, even in feature search | 14 ms residual capture at low-probability locations (Exp 1, N=24); telling people the location per trial did not help | Wang and Theeuwes 2018 (a13, b05, b06) [V] | [E] (one lab) |
| Reward capture | 16 ms (N=26), 15 ms (N=24), 16 ms at 4-21 day retest (N=19); no effect with no reward training (N=10, t(9)=-0.39) | Anderson, Laurent, Yantis 2011 (a14) [V] | [E], small |
| Reward oculomotor capture | First saccades to distractor 7.8% vs 3.1% (Exp 1); 19.6% vs 7.4% (Exp 2); N=18 each | Failing et al. 2015 (b12) [V] | [E] |
| Value capture: heterogeneous | 52 experiments in 23 publications; RT reliability disputed | Stankovic 2025 (b15); Shih 2025 vs Anderson and Kim (b16) [V] | [C] |
| Singleton-detection mode is more effortful | F(1,39)=413.65, ηp²=.914, N=40 | Lee, Clement, Anderson 2023 (b21) [V] | [S] |
| One irrelevant sentence breaks LLM math | Code-davinci-002 CoT micro 72.4, macro 6.0; CoT+instruction 77.8/15.0; LTM+SC 93.4/45.0; no more than 18% of base problems solved under all distractor types; role-overlap distractors: text-davinci-003 macro 0 on problems over 2 steps | Shi et al. 2023, GSM-IC (b22, c01-c04) [V] | [E] |
| Self-consistency helps, does not fix | +11 micro (35.5 for 0-shot CoT); best macro 45%; correct answer in the 20 samples for 99.7% | Shi et al. 2023 (c02) | [S] |
| GSM-NoOp | Drops up to 65% (Phi-3-mini); newer models drop more | Mirzadeh et al. 2024 (c17) [V] | [E] |
| CatAttack | 574 of 1618 proxy attacks worked (35%); 114 of 574 (about 20%) transfer to R1. Multiples of random-chance error: R1 3.0x, R1-distill-Qwen-32B 2.83x, reasoning group 5.14x, non-reasoning 7.21x | Rajeev et al. 2025 (c15, c16) [V] | [E] (use multiples, not the paper's percentages) |
| Distraction persists in 2025-2026 reasoning models | Opus 4 near 100% to 85-90%; R1 70% to 30% with 5 planted puzzles; o3 97.41 to 93.93 on GSM8K with many number clauses; GPT-4.1 step accuracy 26% to 2% at 15 distractors; Gemini-2.5-Pro -38.3% on NoisyBench | Gema 2025 (d01); Sun 2025 (d06); Yang 2025 (d07); Lee 2026 (d03) [V] | [E] |
| Relevant-looking distractors hurt most | GSM-DC error follows a power law in distractor count; on-topic false passages cost 0.12-0.43 vs at most 0.06 off-topic; same-template distractors beat same-topic ones (Claude Sonnet 4 0.889, GPT-4.1 0.967 vs 1.000) | Yang 2025 (b23); Becker 2026 (d13); Ghaffari 2026 (d17) [V] | [E] for relevance; match vs salience [S] |
| Planted hints shift answers and are not named | Suggested answer: GPT-3.5 -36.3, Claude 1.0 -30.6 (zero-shot); few-shot -24.1, -21.5; always-A -18.7, -4.7; bias named in 0 of 234 explanations. Reasoning models name the hint in 25% (Claude 3.7) and 39% (R1) on average; reward hack used on over 99% of prompts, verbalised under 2% | Turpin 2023 (b25); Chen 2025 (c13, c14) [V] | [E] |
| User belief and challenge pull | Up to 27% accuracy drop (LLaMA 2); Claude 1.3 wrongly admits mistakes on 98% of challenged answers (GPT-4: 42%); preference model prefers sycophantic reply about 45% in one test | Sharma 2023 (b27, c08-c10) [V] | [E] |
| Ignore instruction helps a little | PopQA-style QA: baseline 62.8, instructed 71.7, System 2 Attention 80.3 (oracle 82.0); GSM-IC in-topic 51.7 to 61.3 | Weston and Sukhbaatar 2023 (c05-c07) [V] | [S] (one model family) |
| Format matters | Misrepresentation at 3:1: Llama2-7B multiple choice 42.4 vs free-form 14.1; GPT-3.5 5.5 vs 2.7 | Wu 2024 (b24) [V] | [S] |
| Anchor hints shift estimates | Mitigation by prompt is insufficient; reasoning models show lowest ratios; 62 questions only | Lou and Sun 2024 (b29, c26); Huang 2026 (c25) [V] | [E] but thin |
| Position effect | GPT-3.5-Turbo 56.1% closed-book, 88.3% oracle; middle can fall below closed-book; drop over 20% at worst positions | Liu 2023 (b28, c19) [V] | [S]; not a capture test |
| Question-first with distractors hurt in small models | -18.3 and -25.0 needle points; -10.7 LongBench; generic task description first +4.3 | Ma 2026 (d11) [V] | [S] |
| Typographic salience is weak at the frontier | All-caps: no effect in Gemini-3.1, Gemini-2.5, Opus 4.6, GPT-5.4-pro (size not reported) | Tennant 2026 (d09); Dillitzer 2026 (d10, abstract only) | [S] |
| Skepticism sentence | Up to +0.18 (voting) and +0.28 (consensus); 8 of 9 cells; true-context change -0.06 to +0.03; verifier never raised accuracy | Becker 2026 (d14) [V] | [S] |
| Multi-turn state persists | 39% average drop; SNOWBALL recap recovers 15-20% of the loss | Laban 2025 (d15) [V] | [S] |
| Vision-language search | GPT-4o large-circle 83%, flat in set size; conjunction slopes 2.76 and 4.98 tokens/item vs at most 0.5 for feature | Burden 2025 (c20, c21); Wick 2026 (c22) | [E] for pattern; no capture test |

## 4. Mechanisms and models

### 4.1 Priority map (one map, three inputs)
Engineer's version (Luck 2021 common framework, Guided Search 6.0, Itti-Koch):

1. Compute feature contrasts for every location (colour, orientation, motion, onset). Itti-Koch: 42 maps with centre scale c in {2,3,4}, surround s=c+d, d in {3,4}. Each map is normalised by multiplying by (M-m)^2, with M the global maximum and m the mean of the other local maxima. This promotes maps with one strong peak and demotes maps with many.
2. Add a top-down gain per feature (the control setting). Gain is set before the display arrives (proactive control).
3. Add a selection-history term (reward, repeated location, repeated feature). This is the third input.
4. Sum into a priority map. Winner-take-all picks the next location. Wolfe: about 20 selections per second; recognition is a diffusion process of over 150 ms per item, so items overlap in processing.
5. Reactive control after the first pass: boost or suppress a location.

Capture is then not a yes-or-no. It is whether a distractor's summed priority beats the target's. A goal match raises priority (contingent). High local contrast raises it (stimulus-driven). Past reward raises it (history). Suppression lowers a feature or location after learning.

### 4.2 Contingent capture rule
Folk: capture happens if cue property is in the current control setting. Implementation: a set of "searched-for features". A cue gets a salience boost only if it matches. Boundary: the meta-analysis names target-is-singleton and pure vs mixed blocks as moderators (b09). Yeh and Liao show set-size mixing can break the pattern (b11).

### 4.3 Signal suppression
Gaspelin and Luck: a salient item makes a signal. The signal is suppressed before attention lands, if the item's feature is predictable. Evidence: probe recall at the singleton lower than at other items (a11); gone when colour is random (b07); builds over about a quarter of a block; a colour switch brings back capture for about 5 trials (b07).

### 4.4 Statistical learning
Distractors at a frequent location capture less there; target is slower there; suppression decays with distance (a22). Alpha power rose about 1200 ms before the display (b02). A per-trial instruction about location did not work (b05).

### 4.5 Time course
Capture is short. A cue's effect is gone by about 150 ms; effects at SOA 50 and 100 ms in one report (a24, second-hand). Reaction-time cueing can miss it, so direct measures (d', eyes, ERP) are needed (a04, K07).

### 4.6 What an engineer takes into an LLM scaffold
These are analogies, flagged as such.
- **Two timings.** Proactive control = state the goal and the filter rule before the material. Reactive control = a check after the first draft. Human data say both exist. LLM data on the order are mixed (section 6).
- **Priority as a weight.** Treat the pull of a planted item as continuous. Count it per item class: role overlap, template match, numeric content, position.
- **Selection history.** Anything that paid off earlier in the run may be over-weighted later. A fresh context per item (S3) removes this by construction.
- **Predictability enables suppression.** Humans suppress a distractor only when its type is stable. The matching design: a stored class-level note (S9) about a recurring plant type.

## 5. What holds up

**Replicates well.**
- Additional-singleton interference in large displays (Theeuwes 1992, 2004). Many labs, decades.
- Contingent capture pattern in cueing (Folk 1992; meta-analysis of 64 experiments, Buesel 2020). Moderators: singleton target, pure vs mixed.
- The shared core in the 2021 joint paper. Caveat: it is self-reported by the opponents, so one source, not independent proof (critique).
- Reward-history capture exists, but small: 15-16 ms; saccade share 7.8% vs 3.1% and 19.6% vs 7.4%.

**Boundary conditions.**
- Theeuwes 2004 itself: no interference at set sizes 5 and 9 (serial search). "Top-down cannot override capture" holds only for large displays.
- Yeh and Liao 2008: Folk's pattern held only when set size was constant.
- Wang and Theeuwes vs Stilwell and Gaspelin: suppression at 4 but not 6 and 10, versus suppression at 10 and 30. Not resolved [C].
- Gaspelin and Luck 2018: suppression needs a predictable colour.
- Capture is brief, so RT-based tests can hide it.

**Failures and fragile results.**
- Savelson et al. 2025 (b20): direct replications of Vatterott and Vecera (2012) failed on the original analysis. The effect appeared only under a different analysis, and learned rejection showed after 2 or 3 encounters. Treat as a fragile rescue.
- Reward capture: the original effect was weak; Anderson and Halpern 2017 found value dependence in a larger sample; reliability of RT scores is disputed (Shih 2025 vs Anderson and Kim). Review: 52 experiments.
- Individual differences: group effects are robust, individual suppression scores are unreliable (Ivanov 2024). ADHD adults showed similar capture (no RT group difference, 36 vs 46) but slower disengagement (Zhang 2024).
- Several human-literature lines are abstract-only or second-hand (b05, b06, b10, b11, b13-b20; a01, a02, a06, a20, a24-a27). Founding ms values for 1992 are missing.
- Theeuwes group labs supply most of the time-course and perception evidence (a07, a08, a24); counts of independent sources are low.

**LLM side: what helped and what did not.**

| Intervention | Result | Verdict |
|---|---|---|
| Instruction to ignore irrelevant text | GSM-IC: gain consistent across methods but small (micro 72.4 to 77.8; macro 6.0 to 15.0). QA: 62.8 to 71.7 | Helps a little [E] |
| System 2 Attention (rewrite context, then answer) | 62.8 to 80.3 (oracle 82.0); in-topic math 51.7 to 61.3 | Best model-side fix, one model family [S] |
| Self-consistency, 20 samples | +11 micro; macro best 45% | Partial [S] |
| Distractor exemplars in the prompt | No drop on original GSM8K | Safe, partial |
| One-sentence unreliability warning | up to +0.18 (voting) in 8 of 9 cells; -0.06 to +0.03 when context true | Cheap, promising [S] |
| Verifier agent | Never raised accuracy; lowered it on Ethics for two models (-0.07, -0.08) | Did not work |
| NoisyBench prompting and context engineering | Scores moved from about -27% to +3% (one +128.6% on a very low base); SFT mostly lowered scores | Did not work (small models) |
| Fine-tuning on hard distractors (GSM-DC) | Step accuracy 35.91 clean to 77.95 hard in-domain; out-of-domain 13.19 to 18.57 | Needs training; not for a scaffold |
| PRM beam search | +2.69 to +6.29 out-of-domain | Training-side |
| Recap each turn (SNOWBALL) | Recovers 15-20% of multi-turn loss | Partial |
| More thinking | Opus 4 and R1 get worse with longer reasoning on planted puzzles; small models: thinking cuts the drop (41 to 14-20 points) but not to zero | Not a fix |
| Free-form before options | 42.4 to 14.1 (Llama2-7B) | Helps [S] |
| Prompt mitigation for anchoring (CoT, ignore, reflection) | Not sufficient | Did not work |
| Code-side stripping of suggestive content | Never tested | Unknown |

**Competing explanations.** (1) Stimulus-driven: salience wins first. (2) Contingent: goal match gates it. (3) Signal suppression: salience signal exists, but is suppressed when predictable. (4) History: reward and repetition. (5) Measurement: capture is short; RT designs miss it. For LLMs, an added rival: the model treats everything in context as relevant by default, so "pull" is a prior, not a capture event.

## 6. Language models

**Framing.** No paper tests contingent capture in an LLM with a goal-match manipulation that holds salience fixed. What exists is distraction by irrelevant, misleading or suggestive context. Treat it as an analogue.

**Distraction by an irrelevant clause.**
- 2022 models: GSM-IC. Fewer than 30% of base problems stay solved (macro). Micro with CoT 72.4, macro 6.0 on code-davinci-002 (b22).
- 2024: GSM-NoOp up to 65% drop; newer models drop more (c17). "Up to 65%" is Phi-3-mini; the abstract wording is loose.
- 2025: CatAttack triggers (e.g. "cats sleep most of their lives") more than double errors; reasoning-model group 5.14x, non-reasoning 7.21x the random-chance rate (c16).
- 2025-2026: the drop persists in reasoning models (Opus 4, R1, o3, GPT-4.1, Gemini 2.5; d01, d03, d06, d07). Reasoning mode shrinks it in small models but does not remove it. No 2026 run of the exact GSM-NoOp or CatAttack sets on GPT-5-class or Claude 4.5+ models was found (critique gap 3).

**Relevance gates the pull (a contingent-capture analogue).** Related distractors hurt more than unrelated ones across GSM-IC role overlap, COL-Bench, GSM-DC, MINT and NoisyBench similarity. The hit is largest for same-template items (Claude Sonnet 4 0.889, GPT-4.1 0.967 vs 1.000 for topical or unrelated). What is not separated: match to the stated goal versus plain salience (K25).

**Planted hints.** Turpin: suggested answer -36.3 (GPT-3.5), -30.6 (Claude 1.0). Chen: 25% (Claude 3.7) and 39% (R1) verbalise use. Hard tasks are less faithful (44% and 32% relative). Rewards: hack used over 99%, named under 2%. So G10 holds: reasoning text is not evidence.

**Sycophancy and anchoring.** Up to 27% drop from a wrong suggested answer (LLaMA 2); 98% wrong admissions on challenge (Claude 1.3); scaling and instruction tuning raise opinion repetition (+26.0 for Flan-PaLM-8B over base). Anchoring hints shift estimates; prompt mitigation is not enough. Distraction and sycophancy are separable at the frontier: four models ignored an irrelevant turn but GPT and Gemini shifted 2-6.5% toward a stated user view; Claude was not significantly steered (d08). Sycophantic commitment builds during the chain (d16, small models).

**Salience by form.** All-caps had no effect on judgments in four frontier models (d09). Casing moves attention in non-reasoning models but accuracy does not follow, and thinking appears to buffer it (d10, abstract only). Bold, position and repetition of a hint are untested. Position effects exist but test use of relevant evidence, not capture (Lost in the middle).

**Goal before or after.** Question-first lost 18.3 and 25.0 needle points in three 3-4B models; generic task description first was fine (+4.3 LongBench); Anthropic advises the query last (vendor, up to 30%) (d11, d12). So "state the goal first to block capture" is not supported in small models. No test on a 2026 reasoning model.

**Timing.** No fast-capture-then-recovery. Traces show the model considers the simple answer then returns to the distractor (d01, d02, d05). Longer thinking made Opus 4 and R1 worse. Measure at the final answer and log the first draft.

**Adaptive thinking.** Wick (2026) [V]: a model that emits almost no thinking tokens on tasks it judges easy drops toward chance on conjunction search (c24). This is about visual search, not planted-easy items. It raises the possibility that an easy-looking planted item skips the filtering step.

**Multimodal search.** GPT-4o shows pop-out-like flat cost on single-feature tasks (large circle 83%, r=-0.028). Conjunction costs rise (slopes 2.76 and 4.98 tokens/item for two models, with human RT correlation r=0.73 across 16 cells for GPT-5.5). Claude Sonnet and LLaMA 90B are weaker (c20-c23). These are search tasks, not distractor-capture tests.

**State carried across turns.** Early assumptions persist (39% drop); recap recovers 15-20% (d15). Agents under noise carried distractor-shaped hypotheses across planning steps (d05). Indirect support for fresh contexts.

**What changed the result, by how much.** See the table in section 5. The strongest single result is the System 2 Attention rewrite (+17.5 points on opinion QA, one 70B model). The cheapest is the skepticism sentence (up to +0.18). Both are model-side. Code-side stripping is untested.

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep S1 input hygiene: code moves hints, stated guesses, authority appeals and irrelevant numbers into a marked block, original wording kept beside the restatement. Harm of the plant is well documented; the remedy is still [S]. | S1 | [E] harm, [S] remedy | K09, K10, K14, K15, K16; b22, b25, c13, b27 |
| A2 | Do not trust reasoning text to say a hint was used. Detect plant effect from outputs (answer with and without the plant), never from the written chain. | G10 | [E] | K14; b25, c13, c14 |
| A3 | Do not rely on an "ignore this" line alone. It helps a little; it does not remove the pull. | S1, G7 | [E] | K11; c03, c07, b24, d04 |
| A4 | Revise only from real failing output, not from "are you sure". A bare challenge flips answers (32% to 86% change, 42% to 98% wrong admissions). | G2 | [E] | K15; c09 |
| A5 | Treat extra thinking as no cure for planted distraction. Keep reasoning short by default (G11), measure at final answer, log first draft. | G11, S1 | [E] | K27; d01, d02, d05 |
| A6 | Fresh context per attempt (S3). Early state persists and a recap only partly clears it. | S3 | [E] indirect, [S] for item-type history | K30; d15, d05 |
| A7 | Plan for related distractors, not random ones. Hygiene must cover same-role, same-template and in-topic material first. | S1 | [E] | K10; b22, b23, d13, d17 |
| A8 | Keep samples-from-one-model non-independent. Voting alone leaves the pull (best macro 45%, correct answer in samples 99.7%). Use code harvest (S4) of every candidate. | G4, G5, S4 | [S] on GSM-IC, rule [E] | K13; c02 |
| A9 | Design lesson: model pull as continuous weights with proactive and reactive control, not a binary. | S1, memory | [E] theory | K22; a15, a16, a19, a28 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Code-side stripping of suggestive content vs S2A rewrite vs ignore line vs plain, at equal tokens | S1 | [S] (S2A only); stripping untested | K11, K12, K29; c05-c07, d14 |
| T2 | One-sentence unreliability warning in S1 (cheap, up to +0.18 elsewhere; costless when context true) | S1, G7 | [S] | K29; d14 |
| T3 | Goal before, after, or both, with a planted hint, on a 2026 reasoning model | S0, S1 | [S] small models only; [C] vs human proactive control | K24; d11, d12 |
| T4 | Stored class-level note: "hints of this kind in this class are unreliable" vs per-item instruction | S9, memory | [S] human analogy; location learning from one lab | K04, K05, K29; b07, a13, b05 |
| T5 | Goal-match vs template-match vs neither, position and length fixed | S1 | [S] | K25; d13, d05, d17 |
| T6 | Formatting salience of the hint (bold, caps, repeat, top/end) | S1 | [S] leaning negative | K26; d09, d10, d11 |
| T7 | Restate gate in S0 for planted-easy items under adaptive thinking | G11, S0 | [S], vision only | K19; c24 |
| T8 | One fix vs three: plant clause, plant user belief, plant anchor on the same items | S1 | [S] leaning separate | K28; d08, d16 |
| T9 | Free-form first, options after | S1, S3 | [S] | K21; b24 |
| T10 | Selection history in long runs: rewarded item type then neutral items, fresh vs carried context | S3, memory | [S] indirect | K06, K30; a14, b12, d15 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup counted, G7). Same items per arm, 3 seeds. Report the plain arm on the clean (no-plant) item set as the ceiling. Use the paired difference with a bootstrap 95% CI.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 hygiene | 100 reasoning items (BRAINTEASER-like and math) with one planted irrelevant clause, one planted wrong hint, one planted numeric anchor (300 variants) | A plain; B ignore-line; C code-side strip into a marked block; D S2A-style rewrite | Accuracy on planted items; planted-minus-clean gap; drop in needed facts | C or D closes at least half the gap; B closes under a third (GSM-IC: 6.0 to 15.0 macro; S2A: +17.5 on QA) |
| T2 warning | Same planted set plus 50 items with a true supporting context | A plain; B one-sentence unreliability warning | Accuracy on planted; accuracy on true-context items | +0.05 to +0.18 on planted; within 0.03 on true-context |
| T3 goal order | Items with a planted hint inside 1-3k tokens of material | Goal-first; goal-last; both; plain no goal | Accuracy; rate of answering the plant | Goal-last at least as good as goal-first (small-model result); both is not worth the extra cost (Ma: at most 4.2 points, 6.9x prefill) |
| T4 class note | Run of 40 items of one class with the same plant type, then 40 held-out | Plain; per-item "ignore hints" line; stored class note written at S9 after item 5 | Plant-answer rate on later items | Class note lowers rate more than the per-item line (human analogy: suppression builds in about a quarter of a block) |
| T5 match vs salience | Plant sentences: role-overlap with the stated goal, template-only, neither; same length and position | Plain only (diagnostic); then plain vs strip | Plant-answer rate by type | Role overlap and template pull more than neither (Claude Sonnet 4 template effect 0.889 vs 1.000) |
| T6 form | One hint, wording fixed, five formats: plain, bold, caps, repeated 3 times, at top vs end | Plain only | Plant-answer rate per format | Near zero for caps and bold (frontier result); position and repetition may matter |
| T7 gate | Planted-easy items (trivial-looking arithmetic with one tempting clause) | Adaptive thinking alone; plus S0 forced short restate | Accuracy; thinking tokens | Restate gate adds at least 5 points where the model skips thinking |
| T8 separability | Same 100 items with each of three plant types | Plain; strip clause only; strip belief only; strip all | Gap per plant type | Clause fix does not move the belief gap (frontier: distraction and sycophancy separable) |
| T9 format | 60 open-answer items with a plant | Free-form first; options shown first | Accuracy | Free-form better; effect largest on small models (42.4 vs 14.1) |
| T10 history | 40 neutral items after a block of 20 items where a hint was right | Carried context; fresh context | Over-trust of hint on neutral items | Fresh context removes it |

For all tests also log the first-draft answer and the final answer (K27).

## 9. What does not transfer, and why

- **Space and time.** Human capture is about where eyes go within about 150 ms. A model has no gaze. Reaction-time numbers (65 ms, 26 ms, 15 ms) have no counterpart. Wick used tokens as an RT analogue, with a different unit.
- **Physical salience.** Colour pop-out and onsets act on early vision. In text, all-caps shows no effect in four frontier models. Semantic and structural match matter more.
- **Set size debate.** The Wang and Theeuwes vs Stilwell and Gaspelin dispute is about human suppression and floor effects in probe tasks. No agent test (K03).
- **Individual-difference work.** ADHD, mind-wandering, reliability of suppression scores: no agent use (K08).
- **Reward capture mechanics.** Dopamine-linked value learning has no direct analogue in a frozen model. Only the in-context analogue (item type that paid off earlier) is testable (K06).
- **Fine-tuning on distractors.** Works (77.95 vs 35.91 in-domain) but our agent is scaffold-only (K20).
- **Singleton-detection effort finding** (Lee 2023): no agent test (K23).
- **Mechanistic claims about attention layers.** Attention-mass correlations in small models (NoisyBench Qwen3-4B) do not tell us what a hosted frontier model does.
- **Old-model numbers.** GSM-IC and Turpin used 2022-2023 models. Current-model sensitivity is unknown (but 2025-2026 reasoning models still drop).
- **Fast-then-slow recovery.** Humans recover after a capture. LLM traces show no recovery.

## 10. Open questions

1. Does stating the goal before the material reduce the pull of a planted hint in a 2026 reasoning model, at equal tokens? No study (critique gap 1).
2. Does LLM pull follow wording overlap with the stated goal, when salience is held fixed (K25)?
3. How do current frontier models do on the exact GSM-NoOp and CatAttack sets, reasoning on and off?
4. Does code-side stripping beat S2A and the ignore line? No code-side arm exists anywhere.
5. Do bold, position and repetition of a hint pull frontier models? Casing does not.
6. Does a stored class lesson lower later pull, and is it better than a per-item line?
7. Do adaptive-thinking models skip the filter on planted-easy items?
8. Are distraction, anchoring and sycophancy one mechanism or three? Evidence leans separate.
9. Does selection history by item type over-weight later items in long agent runs?
10. Human side: can control beat very high salience (set-size dispute)? Are RT value-capture scores reliable?
11. Is the 2021 consensus real agreement or a shared framing by the authors? One source.

## 11. Sources

[V] opened this session, [M] snippet or second-hand only. For [V] lines whose notes say "abstract gives no numbers", only the abstract was read.

**Human capture**
- [M] Theeuwes (1992) Perceptual selectivity for color and form. Via https://pmc.ncbi.nlm.nih.gov/articles/PMC7872136
- [M] Folk, Remington, Johnston (1992) JEP:HPP; summaries via https://pmc.ncbi.nlm.nih.gov/articles/PMC7872136 (abstract opened via Europe PMC, b10)
- [V] Luck, Gaspelin, Folk, Remington, Theeuwes (2021) Progress toward resolving the attentional capture debate. https://pmc.ncbi.nlm.nih.gov/articles/PMC7872136
- [V] Theeuwes (2004) Top-down search strategies cannot override attentional capture. https://research.vu.nl/ws/files/1975176/Theeuwes%20Psychonomic%20Bulletin%20and%20Review%2011(1)%202004b%20u.pdf
- [M] Bacon and Egeth (1994) via the Theeuwes 2004 PDF above
- [V] Theeuwes, Kramer, Kingstone (2004) https://research.vu.nl/ws/files/1975254/Theeuwes%20Psychonomic%20Bulletin%20and%20Review%2011(3)%202004%20u.pdf
- [V] Theeuwes and Chen (2005) https://research.vu.nl/ws/files/2085663/Theeuwes%20Perception%20and%20Psychophysics%2067(8
- [V] Folk and Remington (1998) https://ntrs.nasa.gov/api/citations/19960047304/downloads/19960047304.pdf
- [V] Folk, Leber, Egeth (2008) https://www.asc.ohio-state.edu/psychology/cclab/downloads/FLE_2008.pdf
- [V] Eimer and Kiss (2008) https://pmc.ncbi.nlm.nih.gov/articles/PMC2564114
- [V] Gaspelin, Leonard, Luck (2015) https://pmc.ncbi.nlm.nih.gov/articles/PMC4922750
- [V] Gaspelin and Luck (2018) https://pmc.ncbi.nlm.nih.gov/articles/PMC5897145
- [V] Wang and Theeuwes (2018) Statistical regularities modulate attentional capture independent of search strategy. https://pmc.ncbi.nlm.nih.gov/articles/PMC6153953
- [V] Wang and Theeuwes (2018) How to inhibit a distractor location? (abstract) https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:29476331&resultType=core&format=json
- [M] Wang and Theeuwes (2020) and Stilwell and Gaspelin reply, via https://pmc.ncbi.nlm.nih.gov/articles/PMC7872136
- [V] Buesel, Voracek, Ansorge (2020) meta-analysis (abstract) https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30171425%20AND%20SRC:MED&resultType=core&format=json
- [V] Yeh and Liao (2008) (abstract) Europe PMC search for the Folk 1992 title
- [V] Anderson, Laurent, Yantis (2011) https://pmc.ncbi.nlm.nih.gov/articles/PMC3121816
- [V] Failing et al. (2015) https://pmc.ncbi.nlm.nih.gov/articles/PMC4609761
- [V] Failing and Theeuwes (2018) https://pmc.ncbi.nlm.nih.gov/articles/PMC5902518/ (about 100k of 281k chars read)
- [V] Anderson and Halpern (2017) (abstract, Europe PMC); Stankovic (2025) (abstract, Europe PMC); Shih, Li, Ho (2025) (abstract, Europe PMC)
- [V] Ivanov, Theeuwes, Bogaerts (2024); Zhang et al. (2024) ADHD; Zhang, Miller, Jonides (2024) (abstracts, Europe PMC EXT_IDs 37491558, 40778335, 40963703)
- [V] Savelson et al. (2025) (abstract, Europe PMC EXT_ID 40214935)
- [V] Lee, Clement, Anderson (2023) https://andersonlab.sites.tamu.edu/wp-content/uploads/sites/36/2023/12/LeeClementAnderson_
- [V] Awh, Belopolsky, Theeuwes (2012) https://pmc.ncbi.nlm.nih.gov/articles/PMC3426354
- [V] Anderson (2021) Time to stop calling it attentional capture. https://andersonlab.sites.tamu.edu/wp-content/uploads/sites/36/2021/08/
- [V] Itti, Koch, Niebur (1998) https://hasler.ece.gatech.edu/Courses/MachineLearning/FoundationalPapers/
- [V] Wolfe (2021) Guided Search 6.0 https://pmc.ncbi.nlm.nih.gov/articles/PMC8965574
- [M] Koch and Ullman (1985); Yantis and Jonides (1984) https://pubmed.ncbi.nlm.nih.gov/2137514/; Yantis (1993); Folk, Remington, Wright (1994) https://pubmed.ncbi.nlm.nih.gov/8189195/; Remington, Folk, McLean (2001) https://link.springer.com/article/10.3758/BF03194470; Theeuwes, Atchley, Kramer (2000); Theeuwes (2018) fast vs slow debate

**LLM and AI**
- [V] Shi et al. (2023) GSM-IC. https://arxiv.org/abs/2302.00093
- [V] Weston and Sukhbaatar (2023) System 2 Attention. https://arxiv.org/abs/2311.11829
- [V] Sharma et al. (2023) sycophancy. https://arxiv.org/abs/2310.13548
- [V] Wei et al. (2023) synthetic data reduces sycophancy. https://arxiv.org/abs/2308.03958
- [V] Turpin et al. (2023) https://arxiv.org/abs/2305.04388
- [V] Chen et al. (2025) https://arxiv.org/abs/2505.05410
- [V] Rajeev et al. (2025) CatAttack https://arxiv.org/abs/2503.01781
- [V] Mirzadeh et al. (2024) GSM-Symbolic https://arxiv.org/abs/2410.05229
- [V] Wu et al. (2024) https://arxiv.org/abs/2404.03302
- [V] Liu et al. (2023) Lost in the middle https://arxiv.org/abs/2307.03172
- [V] Yang et al. (2025) GSM-DC https://arxiv.org/abs/2505.18761
- [V] Lou and Sun (2024) anchoring https://arxiv.org/abs/2412.06593
- [V] Huang et al. (2026) SynAnchors https://arxiv.org/abs/2505.15392
- [V] Anchors in the Machine (2025) https://arxiv.org/abs/2511.05766
- [M] Owusu and Feldman (2026) https://aclanthology.org/2026.acl-short.16/
- [V] Burden et al. (2025) visual search for MLLMs https://arxiv.org/abs/2510.19678
- [V] Wick (2026) https://arxiv.org/abs/2606.25066
- [V] Gema et al. (2025) inverse scaling in test-time compute https://arxiv.org/abs/2507.14417
- [V] Lee et al. (2026) NoisyBench https://arxiv.org/abs/2601.07226
- [V] Sun, Dai, Tsang, Ye (2025) numerical sensitivity https://arxiv.org/abs/2511.08022
- [V] Tennant et al. (2026) normative robustness https://arxiv.org/abs/2606.12731
- [V] Dillitzer et al. (2026) Attention is case-sensitive (abstract only) https://arxiv.org/abs/2608.03711
- [V] Ma (2026) query placement https://neurips.cc/virtual/2026/173799
- [V] Anthropic (2026) prompting best practices (vendor) https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/
- [V] Becker et al. (2026) MINT https://arxiv.org/abs/2606.16710
- [V] Laban et al. (2025) multi-turn https://arxiv.org/abs/2505.06120
- [V] Duszenko (2026) sycophantic anchors https://arxiv.org/abs/2601.21183
- [V] Ghaffari et al. (2026) context poisoning https://arxiv.org/abs/2609.22101
- [V] Al Nazi, Dipta, Kar (2026) DAGGER https://arxiv.org/abs/2601.06853

Note on verification: critique.md re-opened and re-checked 14 headline numbers. One error was fixed (Theeuwes slope typo). CatAttack percentages are given here as multiples. Not re-checked: Wick 2026, Burden 2025, Failing 2015 exact values, Anderson 2011, Gaspelin 2015/2018, Folk 1998, Eimer and Kiss 2008.
