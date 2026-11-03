# Heuristics and biases: deep document

*Subfield E18.03. Anchoring and adjustment, availability, representativeness, framing. Key works: Tversky and Kahneman 1974, 1981, 1983. Schema link: S1 input hygiene (and guardrails G4, G5, G9, G10). Evidence ids (a01 to d19) refer to evidence_a-d.jsonl; claim ids (K01 to K34) to claims.jsonl in this folder. Cross-check notes are in critique.md.*

---

## 1. What it is

The heuristics-and-biases programme asks one question: when people judge under uncertainty, which short cuts do they use, and where do those short cuts fail in a predictable way? The founding paper names three short cuts (a01):

- **Representativeness.** Judge how likely A belongs to B by how much A resembles B.
- **Availability.** Judge how frequent or likely something is by how easily examples come to mind.
- **Anchoring and adjustment.** Start from a number, then adjust. The adjustment is too small.

**Framing** (gain versus loss wording of the same options) was added in 1981. It comes from prospect theory, not from the 1974 list, but it is the fourth topic here.

Underlying idea, later called attribute substitution (a19): a hard question is swapped for an easier, related one, without the person noticing. The method was to find cases where the short cut gives a systematic error and to use the error as a window onto the process (a09).

Why it matters for our agent. The schema (S1 UNDERSTAND) says that code moves suggestive material that is not part of the task (a stated guess, an appeal to authority, an irrelevant number) into a marked block. This subfield is the evidence base for that rule. Two questions:

1. Do language models show these biases, and how big are they?
2. What removes them at equal tokens? Schema section 4b already says bias checklists and "be careful" prompts do not work. This document checks whether that holds here and what does work.

Short answer, detailed below: numeric anchoring is real in models and survives prompt-level fixes. Removing the anchor from the input works better than asking the model to ignore it. Most other classic biases are item-dependent in current models, and model errors are often not the human error at all.

---

## 2. History and theories in depth

### 2.1 The 1974 paper (a01 to a09)

Tversky and Kahneman, Science 185:1124-1131. Research began in 1969; the paper was written during 1973 and had over 420 citations by 1983 (a09). It rests on thousands of subject hours (a09). The paper does not report group sizes for most items. Content, as printed:

**Representativeness (a02, a03, a04).**
- Engineer/lawyer problem. Base rates .7 and .3. With no personality sketch, people judged .7 and .3. With a worthless sketch of "Dick", they judged .5 in both base-rate conditions. A worthless description wiped out a base rate they had used one step before.
- Hospital problem. Large hospital 45 births a day, small 15. Which records more days with over 60 percent boys? Counts: larger 21, smaller 21, about the same 53 (about 95 subjects). Correct: the smaller one. This is insensitivity to sample size.
- Misconceptions of chance. A short random sequence is expected to "look random": H-T-H-T-T-H is judged more likely than H-H-H-T-T-T. Gambler's fallacy. No counts given.

**Availability (a05).**
- Committees from 10 people. Median estimate 70 for 2-member committees and 20 for 8-member committees. Truth is 45 for both. Small committees are easier to picture.
- Word frequency: people say more English words start with r or k than have it third; the reverse is true.
- Abstract words are judged more frequent than concrete words of equal frequency.

**Anchoring and adjustment (a06, a07, a08).**
- Wheel of fortune. A random number from a wheel moved estimates of the percent of African countries in the UN. Median 25 for anchor 10, median 45 for anchor 65. Pay for accuracy did not remove the effect.
- Incomplete computation. High school students had 5 seconds for 8x7x6x5x4x3x2x1 or the reverse order. Median 512 (ascending) versus 2,250 (descending). Truth 40,320. Both far too low, and the order sets the level.
- Conjunctive and disjunctive events (Bar-Hillel bets). A conjunctive event (p = .48) was preferred to a simple one (.50); a simple event was preferred to a disjunctive one (.52). Anchoring on one step's probability makes long plans look likelier and risks look smaller than they are.
- Confidence intervals too narrow: the true value fell outside the intervals about 30 percent of the time, where 2 percent is expected for a 98 percent interval (a08). A secondary source says 30 to 40 percent in much replicated work (a19).

The paper is a list of demonstrations. It has no formal model (a29, K26). For engineering this matters: there is no equation to implement, only a list of tests.

### 2.2 Framing and prospect theory (1981)

The Asian disease problem: equal outcomes get opposite choices depending on whether they are worded as lives saved or lives lost. Commonly quoted: 72 percent chose the sure option when worded as "saves 200 lives"; 78 percent chose the risky option when worded as deaths (a15, b27; Wikipedia only, second-hand). The primary text could not be fetched (critique gap 8). The Many Labs 2 framing item is T&K 1981 Study 10, not the Asian disease problem (d14).

### 2.3 Conjunction fallacy (1983)

Linda: described as bright, outspoken, concerned with social justice. Most chose "bank teller and active in the feminist movement" over "bank teller". About 85 percent in the original; 57 percent with the wording "whether or not" feminist; about 20 percent in a frequency format ("out of 100 people...") (a16, b22; Wikipedia only). The 85 percent is the original T&K figure, not a number from any LLM study's human sample (critique correction 1). The frequency account is contested (K05).

### 2.4 Rival accounts of anchoring (a10)

Three explanations, none decisive:
1. **Insufficient adjustment** (T&K). The person starts at the anchor and moves until the answer feels plausible, stopping too soon.
2. **Selective accessibility** (Strack and Mussweiler 1997). The anchor makes anchor-consistent facts easy to retrieve; this is semantic priming. Their Gandhi item (anchors 9 vs 140, mean guesses 50 vs 67) is cited second-hand (a10, b21).
3. **Attitude-change or scale-distortion accounts**: the anchor shifts how the response scale is read.

Clearly random anchors (die roll, random button) failed to replicate in several studies (a10); see section 5.

### 2.5 Rival views of heuristics (a19)

Heuristics as laziness (the original view); as natural assessments; as ecologically rational tools (Gigerenzer). Gigerenzer and Hertwig argued that Linda is ambiguous ("probable", "and" can be read in other ways) (a16). For our agent the rival views point to the same rule: change the input form and the error often changes.

---

## 3. Core findings with exact numbers

Status key: original = original demonstration; replicated = replicated at scale; shrunk = replicated but smaller; failed = failed to replicate; single = one source; second-hand = number known only through Wikipedia or a review.

### 3.1 Human findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Wheel-of-fortune anchor on a country-percent estimate | median 25 (anchor 10) vs 45 (anchor 65) | T&K 1974 (a06) | original; random-wheel anchors contested (a10) |
| Incomplete computation anchor | median 512 vs 2,250, truth 40,320 | T&K 1974 (a07) | original |
| Relevant anchor on estimates (15 quantities, N=156) | Mississippi length: median 800 miles with no anchor, 300 with a 70-mile anchor, 1,500 with a 2,000-mile anchor | Jacowitz and Kahneman 1995 (a11) | original, second-hand |
| Many Labs 1 anchoring, four items, about 5,000 people | babies/day US: original 1k vs 40k, replication 3.2k vs 26.7k; Chicago: 600k vs 5.05m, replication 1.03m vs 3.00m; Everest: 8k vs 42.55k, replication 11.8k vs 34.5k; SF-NYC: 2.6k vs 4k miles, replication 2.85k vs 3.99k | Klein 2014 via review (a12) | replicated on all four; raw gaps smaller than original |
| Anchoring varies by country | N=6,344 in ten countries; r: NYC .26 [.22,.31], Chicago .48, Everest .61 [.56,.65], babies .57 [.52,.61]; I2 65 to 87 percent | Kakinohana 2023 (b05) | replicated, large heterogeneity |
| Large preregistered test of moderators | N=1,967, 8 questions; high anchors shift +0.57 item SD; debiasing reminder .613 to .499; cognitive load .513 to .597; subjective knowledge .641 (-1 SD), .555 (mean), .470 (+1 SD); incentive .550 vs none .560 | Schley and Weingarten 2026 (b06) | replicated; reminder helps a little, incentives do nothing |
| Anchor distance | effect rises steadily with anchor distance; decimals, page breaks, direction: little moderation | Schley and Weingarten 2026 (b07) | single design |
| Incidental anchor (phone named P97 vs P17) | original d=0.30, N=207 (58.1 vs 51.9 percent); replication d=0.04 [-0.01,0.09], N=6,826 (49.87 vs 48.98 percent); paper-and-pencil sites N=1,112 d=-0.01 | Many Labs 2 (a13, b02, d14) | failed |
| Anchoring as a trait | split-half reliability lowest of the tasks tested ("not reliable") | Rebholz 2026 (b08) | single |
| Scoring choice | a categorical "within 50 percent of anchor" rule finds no predictor effect where directional gaps show anchoring | Nawaz 2026 (d19) | single, abstract only |
| Expertise and anchors | expertise lowers anchoring; extreme anchors raise it; relevance made no difference | Mayer and Rebholz 2024 (d16) | single, abstract only |
| Gain/loss framing, T&K 1981 Study 10 item | original N=181: 68 vs 29 percent would travel, OR 4.96, d=1.08 [0.71,1.45]; replication N=7,228: 49 vs 32 percent, OR 2.06 [1.87,2.27], d=0.40 [0.35,0.45] | Many Labs 2 (a14, b03, d14) | shrunk (under half) |
| Framing with matched, complete options | N=1,697 (477 on completely described options): b=0.61 [0.29,0.93], OR 1.84, p<.001; significant in 7 of 9 matched comparisons, 3 of 4 domains | DeKay 2025 (b09) | shrunk, persists |
| Asian disease | 72 percent sure option (save frame); 78 percent risky option (loss frame) | T&K 1981 via Wikipedia (a15, b27) | second-hand |
| Children and framing | ages 10 to 12 show more framing than younger children | Wikipedia (b27) | second-hand |
| Base rate and worthless sketch | .7/.3 used with no sketch; .5 with worthless sketch | T&K 1974 (a02) | original |
| Hospital problem | 21 larger, 21 smaller, 53 about the same | T&K 1974 (a03) | original |
| Tom W. | over 95 percent said computer science was likelier than education or humanities despite lower base rate | K&T 1973 via Wikipedia (a17, b26) | second-hand |
| Cab problem | 85 percent Green, 15 percent Blue, witness 80 percent reliable: Bayes gives 41 percent (0.12 / 0.29); most people say over 50, often 80 | via Wikipedia (a17, b26) | second-hand |
| Linda conjunction | about 85 percent error; 57 percent with "whether or not"; about 20 percent in frequency format | T&K 1983, Gigerenzer 1991 via Wikipedia (a16, b22) | second-hand, contested |
| Frequency format for joint probabilities | Fiedler 1988: better Linda with a frequency question; Wedell and Moro 2007: none; advantage held for double tree diagrams but reversed for 2x2 tables | Stegmueller 2024 (d15) | mixed |
| Availability by ease of retrieval | recalling 12 vs 6 assertive acts gave lower self-rated assertiveness; lists of 19 famous women and 20 less famous men (and the reverse): famous names recalled more and that gender judged more frequent | Schwarz 1991, T&K 1973 via Wikipedia (a18, b25) | second-hand |
| Availability moderators | Vaughn 1999: effect only at semester start and for the hardest exam; Fox 2006: 2 vs 10 suggestions, the 10 suggestions worse | via Wikipedia (b25) | second-hand |
| Incentives and conjunction error | meta-analysis d=0.19, OR 1.40 for a correct answer when incentivised, N=3,276 | OSF 2022 (b23) | snippet only |
| Individual difference | bias tasks correlate only minimally with each other (Study 1 N=1,071; Study 2 N=480) | OSF 2026 (b24) | snippet only |
| Many Labs 2 overall | 28 findings, 125 samples, 15,305 people, 36 countries; 15 (54 percent) replicated at p<.05; 14 (50 percent) at p<.0001; median d 0.60 original vs 0.15 replication; 57 percent with d<.20; 7 (25 percent) larger than original; 9 went in the opposite direction; 11 of 28 (39 percent) heterogeneous | Klein 2018 (a13, b01, b04) | replication project |

### 3.2 Language-model findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ChatGPT (GPT-3.5) anchoring, estimate task | low anchor 20.83 (SE 3.38) vs humans 22.50; high anchor 105.97 (SE 9.08) vs humans 80.50; t(58)=8.78 (ChatGPT), 5.55 (humans); n=30 per cell. GPT-4: 22.0 vs 94.33 (5 trials) | Suri 2023 (a21, b15, c09) | single paper, re-checked |
| GPT-3.5, 4, 4o pulled by numeric hints | 62 questions, 3 hint types; 12 expert-anchor questions no exceptions; 42-question set: 11 exceptions of 162 values, 9 from GPT-3.5; time-period questions 7 of 42 but 6 of 11 exceptions | Lou and Sun 2024 (a24, b17, c04, c06, d17) | single paper |
| Anchoring across 20 models | mean bias score 0.39 (model range -0.05 to 0.67); random model 0.00 | Malberg 2025 (c12, c13) | single benchmark |
| Anchored share of questions, 11 models | 22 to 61 percent; Llama-3.1-8B 34.7, Qwen2.5-7B 40.0, GPT-4o 27.3, DeepSeek-R1 25.0, Qwen3-235B thinking 22.0 | Huang 2026 (c24) | contested by d01, d05 |
| Only anchoring points the human way in 2025 models | 7 models, 6 biases, 30 vignettes (5 per bias), 10 samples per cell: anchoring +0.163 [+0.111,+0.215], d=+1.89, p_Holm=.037 (range +0.11 Qwen3 thinking to +0.20 Claude instruct); framing -0.336, d=-2.35; availability absent | Kraishan 2026 (d03) | single paper |
| Thinking on vs off, matched weights | pooled reasoning minus sibling +0.031 (p=.157); no negative slope over realised 0 to 2,800 tokens; 12,350 calls | Kraishan 2026 (d01, d02) | single paper |
| Thinking mode raises credible-anchor adoption | 6 of 7 models; 3 flipped sign by source credibility (5 sources, fortune teller to chief judge) | Yao 2026 (d05) | abstract only |
| Restate-every-number line | signed score change -0.015 [-0.026,-0.004]; 5 of 5 items fall; item t(4)=-2.65, p=.057; sign test p=.063 | Kraishan 2026 (d04) | tentative |
| Code models copy irrelevant context | Codex accuracy 32.9 to 2.4 percent, CodeGen 25.6 to 1.5, with an irrelevant function plus "raise NotImplemented"; that framing line output 91.7 and 79.3 percent of the time. Averaged over five framing lines: Codex accuracy 2.4 to 10.6 percent, line copied 81 percent vs 4.5 baseline; CodeGen 70.7 vs 0.0 | Jones and Steinhardt 2022 (a22, b10, c10) | single paper, re-checked |
| Code-anchor | Codex writes anchor line "return tmp" in 26 to 46 percent of solutions, CodeGen 13 to 79; GPT-3 estimate shifts toward the anchor 28.6 percent (p=20) and 42.9 (p=50), away 10.7, no change 10.7 to 14.3, gibberish 50.0 and 32.1 | same (b11, c11) | single |
| No anchoring in a code-length task | GPT-3, 4 experiments, 838 items: small vs large anchor means 41.5 vs 41.28 (p=.51); 41.08 vs 39.90 (p=.006); 45.78 vs 42.04 (p<.001); 48.86 vs 46.31 (p<.001) | Shaki 2023 (a25, c18) | contested |
| Asian disease in GPT-3 | 704 prompts; save frame 45 percent risky (humans 28); die frame 74 percent (humans 78); at save probability 1/3: 11.3 percent (save) vs 60.0 percent (die); boundary at high save probability | Jones and Steinhardt (b12) | single |
| Framing in admissions | GPT-4 admit rate 0.375 vs 0.780 (-0.405: 40.5 percent more admitted under reject wording); GPT-3.5 +0.165; Llama-2 7B 32.1 percent fewer females rated good at math; 13,465 prompts | Echterhoff 2024 (a23, b16, c07) | single paper, re-checked |
| ChatGPT framing and Linda | drug rated 5 vs 4 in all 11 trials each (humans 5.2 vs 4.6, t(80)=3.86); artist-who-likes-to-read prompt: ChatGPT chose the conjunction 18 of 20, humans 10 of 20 | Suri (a21, b15) | single |
| GPT-3 on vignettes | 12 of 12 standard vignettes correct or human-like; Linda fallacy yes; cab roughly correct; hospital "about equal"; black-cab variant answered 20 percent; CRT 1-3 intuitive wrong; three of six prospect-theory biases | Binz and Schulz 2023 (a20, b13, c17) | single |
| Fresh Linda/Bill vignettes | 1,024 items; mean accuracy Bill 0.53, Linda 0.46; humans Bill 0.83, Linda 0.56; joint-probability sum humans 0.34 vs davinci-003 0.96; large option-order effects | Yax 2024 (c16) | single |
| Seven models on classic tasks | correct with correct reasoning: GPT-4 69.2, Claude 2 55.0, Bard 35.8, GPT-3.5 29.2, Llama-2 70b 15.0, 13b 5.0, 7b 2.5 percent; human-like biased: GPT-3.5 21.7 (50.8 counting human-like correct); total human-like GPT-4 73.3; Llama-2 70b refused 41.7; Llama-2 7B incorrect 77.5 | Macmillan-Scott 2024 (a27, b19, c14) | single paper, re-checked |
| CRT | davinci-003 5 percent correct, 80 intuitive; ChatGPT-3.5 59 / 15; GPT-4 95 to 96 / 0; 500 humans 38 / 55; semantic illusions: davinci-003 fell for 72 percent | Hagendorff 2023 (a28, b14, c01) | single paper, re-checked |
| CoT and few-shot on davinci-003 | CRT correct 5 to 28 percent, intuitive 80 to 29; semantic illusions correct 18 to 54 percent (over 64 with 10+ examples); CRT type-1 accuracy 0 to about 78 percent after 30 examples | same (c02) | single |
| Instruction tuning raises bias | certainty effect up to 0.67 (text-davinci-003); belief-invalid up to 0.65; some base models near 0 (0.00 belief-valid DaVinci) | Itzhak 2024 (a26, b18, c19) | single |
| Vulnerability triage | 8 LLMs: mean susceptibility framing 33.2, anchoring 23.5, halo 18.4 percent; "ignore metadata" prompts left combined attack success at 83 to 88 percent on four open models | Shahriar 2026 (d06) | single |
| Software-engineering dilemmas | median bias sensitivity: base 12.9, CoT 16.1, implication prompting 13.3, impersonated self-debiasing 10.2, bias warning 10.3, both 8.3 percent; anchoring only 5.9 percent at baseline, hindsight 35.3 | Sovrano 2026 (c26) | single |

### 3.3 Judge and agent findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Order swap flips verdicts | 80 questions; conflict rate GPT-4 46.3 and 5.0 percent (two comparisons), ChatGPT 82.5 and 52.5; Vicuna-13B beats ChatGPT on 66 of 80 by order alone | Wang 2023 (d11) | single |
| Position consistency | Claude-v1 23.8, GPT-3.5 46.2, GPT-4 65.0 percent; biased toward first 75.0, 50.0, 30.0; repetitive-list attack fails GPT-4 8.7 percent, Claude and GPT-3.5 91.3 | Zheng 2023 (d12) | single |
| Judge biases | 16 models, about 40 percent of comparisons biased; over 70 percent follow a fake majority cue; most large models prefer their own output in over 50 percent of anonymised comparisons | Koo 2023 (b20, c20, c21) | single, partly snippet |
| Position robustness | robustness rate under 0.5 with 3 to 4 candidates for most judges; Claude-3.5 most robust | Ye 2024 (d13) | single |
| Layer location | anchoring acts in early layers; Anti-DP 24.7 vs 34.7 percent baseline is the only mild gain | Huang 2026 (c24, c25) | single |
| Cloned agents add anchors | one-sentence anchor to sellers: market efficiency 96 to 15 percent; a one-line debiasing instruction reversed it | Hantel 2026 (d10) | abstract only |
| Small agents negotiating | randomised starting anchor saves up to 25 percent energy vs fixed anchor (1B model, 200 trials per strategy) | Chergui 2026 (d07) | single |
| Long-horizon agents | Qwen3-235B Hit@5 0.526 with insight memory vs 0.601 without | Shen 2026 RealICU (d08) | single |
| Self-anchoring over turns | Claude confidence drift -0.032 (t(14)=-2.43, p=.029, d=-0.63; open-ended domain -0.094); GPT-5.2 +0.007 (p=.181); Gemini +0.001; N=15 per cell | Harshavardhan 2026 (d09) | single |

---

## 4. Mechanisms and models

There is no formal model of the three heuristics (a29, K26). What follows are working models an engineer can turn into tests or code.

### 4.1 Anchoring in a person

Sketch (a10):
1. Anchor `A` is shown, often through a comparison ("more or less than A?").
2. The person starts at `A` and moves toward their own belief `B` until the value feels plausible. Stopping point `E = A + k(B - A)` with `k < 1`. A larger `|A - B|` gives a bigger absolute pull, which fits "the effect rises with anchor distance" (b07).
3. In parallel the comparison primes anchor-consistent facts (selective accessibility). This is why the anchor can work even when it is not used as a start.

Moderators measured in humans: more knowledge, less pull (b06: .641 to .470; d16 expertise). More extreme anchors, more pull (d16); farther anchors, more pull (b07). Relevance is unsettled: b07 says anchors pull harder when they apply to the target, d16 found no relevance effect. Cognitive load raises it (.513 to .597). A debiasing reminder lowers it a little (.613 to .499).

### 4.2 Anchoring in a model

Working hypothesis from the data: for a language model the anchor is text in the context. Text near a question raises the probability of numerically close tokens. Evidence:
- Models are pulled by hints that look like facts, expert opinions or irrelevant numbers (b17).
- Pre-answer anchors resist prompt and decoding changes; the effect appears in early layers (c24, c25).
- Code models copy anchor lines wholesale (a22, b11). This is the extreme case.
- Source credibility matters: thinking-mode models adopt an authority-tagged anchor more (d05).

Engineer's version: treat the anchor as a shift in the output distribution, larger with salience of the number and closeness to the answer scale. The fix with the best evidence is not to argue the shift away at output time (K12, K25) but to keep the number out of the context when it is not part of the task (K14, K30).

### 4.3 Framing

Prospect-theory form: outcomes are coded as gains or losses against a reference point; the value function is concave for gains and convex for losses, so people take risks to avoid sure losses and avoid risk to keep sure gains. Part of the observed effect is wording mismatch: when options are written out completely and symmetrically the effect drops but stays (DeKay OR 1.84, b09).

For a model: framing words (admit/reject, saved/die) are features that flip the answer. Echterhoff measured a 0.405 swing in GPT-4 (a23). But seven 2025 models leaned against the human direction on five items, mean -0.336 (d03). The sign depends on item and scoring, so tests must use paired wordings and require invariance, not just look for the human pattern.

### 4.4 Representativeness and base rates

Bayes form: `posterior odds = prior odds x likelihood ratio`. People over-weight the likelihood side (the sketch) and drop the prior. Implementation: ask for the base rate (reference class) as an explicit first line before reading case details; compute the posterior in code from stated numbers. Cab check: `0.15*0.8 / (0.15*0.8 + 0.85*0.2) = 0.12/0.29 = 41%` (a17).

Sample-size insensitivity: the variance of a proportion falls as `1/n`. The agent can be made to name `n` and state that small samples vary more.

### 4.5 Availability

Two parts (a18): the count of instances recalled, and the ease of retrieval. Ease works as a cue: recalling 12 examples is hard, so the person concludes the trait is weaker (Schwarz). Moderators: uncertainty and relevance of the felt ease (b25).

Model analogue: models retrieve by frequency in training text, so "availability" in a model is mostly the training frequency of examples. Only Malberg tests it (0.11, weak across 20 models) and Kraishan found it absent in seven 2025 models (d03).

### 4.6 Self-debiasing by rewriting (the best-supported fix)

Procedure from Echterhoff and Lyu (c08, c22):
1. Give the model the prompt.
2. Ask it to point to biased elements (framing words, stated guesses, irrelevant numbers).
3. Ask it to rewrite the prompt without them.
4. Repeat until none are flagged (SACD) or stop after one pass (self-help).
5. Answer from the rewritten prompt only.

Results: leftover biased elements 0 to 2.7 percent for framing (a23, c08). FOMC bias score for llama3.1-8b: vanilla 0.3805, CoT 0.3425, Reflexion 0.3830, debate 0.5020, self-help 0.2100, SACD 0.1570 (c22). Cost is extra calls, so the equal-token comparison still has to be run.

### 4.7 Judge order bias

A pairwise judge reads position as evidence. Fix in code: randomise order; for close calls, swap and require agreement (d11, d12, d13). Swapping doubles calls.

---

## 5. What holds up

### 5.1 In humans

**Holds (replicated at scale):**
- Relevant numeric anchoring: all four Many Labs 1 items replicated with smaller raw gaps (a12); cross-culture r from .26 to .61 (b05); +0.57 item SD in N=1,967 (b06). It holds as a group effect and is a poor individual measure (b08).
- Gain/loss framing: replicated at under half the original size, d 1.08 to 0.40 (d14, a14). It persists with matched options, OR 1.84 (b09).
- Base-rate neglect with a worthless sketch, sample-size insensitivity, committee estimates (a02, a03, a05): original findings; large new replications were not opened this run.

**Fails or shrinks:**
- Incidental anchors: d=0.30 (N=207) became d=0.04 (N=6,826) (a13, b02).
- Random-number anchors (die roll, random button) failed in several studies (a10, second-hand).
- Many Labs 2 as a whole: 54 percent replicated; median d fell from 0.60 to 0.15 (b01). Lab effect sizes are upper bounds (K03).
- Linda frequency format: contested; Fiedler yes, Wedell and Moro no; natural-frequency advantage not found for joint probabilities (d15).
- Anchoring as a trait: poor reliability (b08). Bias tasks correlate minimally with each other (b24, snippet).

**Moderators measured:**
- Cultural values: Harmony negative, Mastery positive, Intellectual Autonomy and Egalitarianism negative (b05).
- Knowledge lowers the effect (b06, d16). Load raises it (b06). Anchor distance raises it (b07). Extremity raises it (d16).
- Incentives: nothing for anchoring (b06: .550 vs .560); d=0.19 for the conjunction fallacy (b23, snippet).
- Cognitive ability and reflection predict fewer errors (b22).

**Interventions in humans:** a debiasing reminder gave a small gain (.613 to .499). Payoffs did not remove the wheel-of-fortune effect (a06). Frequency format: mixed.

### 5.2 In language models

**Did not work (K12):**
- CoT, "principles of thought", "ignore the anchor", reflection: anchor gaps stayed highly significant in GPT-4 and GPT-4o (b17).
- Knowledge enhancement raised anchoring from 34.7 to 50.5 percent in Llama-3.1-8B (c25).
- "Ignore metadata" instructions left combined attack success at 83 to 88 percent (d06).
- CoT gave no significant per-bias gain in software dilemmas (median 12.9 to 16.1 percent, c26).
- Thinking on versus off: no reliable gain (+0.031, p=.157) and no dose-response over realised tokens (d01, d02). Thinking raised credible-anchor adoption in 6 of 7 models (d05, abstract only).
- Few-shot, Reflexion and debate raised bias by feeding it back (K15; c22, c23).
- Model-level fixes on Llama-3.1-8B: adversarial finetuning 34.7 to 33.3; DoLa 37.5 to 38.5; self-improving 38.4; question-aware 36.8; only Anti-DP gave 24.7 (c25).

**Worked:**
- Self-rewrite of the prompt (self-help, SACD): see 4.6.
- Showing both a low and a high anchor: removed the pull only on 8 questions where the hints straddled the benchmark (b17, c05).
- Eliciting best practices first and injecting them: about 51 percent mean cut in bias sensitivity, up to 73 percent (c26, K16). Anchoring baseline was only 5.9 percent, so this is not an anchoring result.
- Restating every number: pooled change -0.015, 5 of 5 items down, p=.057 (d04). Suggestive only.
- CoT and few-shot for CRT in older models (davinci-003 5 to 28 percent; 0 to about 78 with 30 examples) (c02).
- Swapping or randomising order in judges (d11, d12, d13).
- A one-line debiasing instruction in the multi-agent market (d10, abstract only).
- Randomising the opening anchor in a negotiation agent: up to 25 percent energy saved (d07).

**Disagreements between sources (critique.md):**
1. Shaki says GPT-3 shows no anchoring, though two of four experiments had small significant gaps. Suri, Lou and Sun, Huang and Malberg find clear anchoring in chat models. Likely cause: task type (code-completion length vs numeric Q&A) and model.
2. Huang: reasoning models least anchored (DeepSeek-R1 25.0, Qwen3 thinking 22.0). Kraishan: no reasoning advantage in matched pairs. Yao: thinking amplifies. Unresolved; K11 is contested.
3. Lou and Sun: stronger GPT versions are more consistently anchored.
4. Instruction tuning raises bias (Itzhak) yet ChatGPT-class models avoid CRT traps (Hagendorff). Different bias families.
5. Self-rewrite works but "ignore the anchor" does not. The first removes the anchor from the input; the second asks the model to resist it while it stays in view.

**Weak spots in the whole base:**
- Many 1974-era follow-up numbers come from Wikipedia only.
- Most LLM studies use GPT-3, GPT-3.5, Llama-2, early GPT-4. Only Huang, Malberg, Kraishan, Yao and Harshavardhan involve 2025 to 2026 models.
- Small N: Suri 30 per cell; GPT-4 5 trials. Few studies report variance over repeats.
- Contamination: Linda, CRT and the Asian disease are in the training data. Only Yax built fresh vignettes.
- Bias scores in Malberg and Kraishan are the authors' own, not human d.
- Several evidence lines are the same paper read more than once (critique correction 5). Independent source counts are by paper.

---

## 6. Language models

### 6.1 Overall picture

1. **Numeric anchoring is the most reliable human-direction bias in models.** GPT-3.5: 20.83 vs 105.97 (humans 22.50 vs 80.50) (a21). GPT-4: 22.0 vs 94.33 over 5 trials. 20-model mean bias score 0.39 (c12). In seven 2025 models it was the only bias pointing the human way: +0.163, d=1.89 (d03).
2. **Framing is strong but its sign is unstable.** GPT-4 admission swing 0.405 (a23); GPT-3 mirrors Asian disease (b12); mean score 0.41 across 20 models (c12); yet seven 2025 models leaned against the human direction on five items, -0.336 (d03).
3. **Availability is weak or absent**: 0.11 across 20 models (c12); absent in seven 2025 models (d03).
4. **Errors are mostly not human errors.** GPT-4 was correct with correct reasoning 69.2 percent of the time; only 21.7 percent of GPT-3.5 answers were the human-like bias; answers varied across repeats; Bard reasoned correctly and then named the wrong card (a27, c15). Item rewrites break models: standard vignettes 12 of 12 fine, adversarial rewrites produce non-human errors (c17); fresh Linda/Bill near chance, 0.46 to 0.53 (c16).
5. **Scale and training move different biases in different ways.** CRT: davinci-003 5 percent correct (80 intuitive), ChatGPT-3.5 59, GPT-4 96 (a28). Instruction tuning raised decoy, certainty and belief bias (a26). Intuitive errors grew with size in the GPT-3 family, then vanished in ChatGPT and GPT-4 (b14).

### 6.2 What changed the bias, by how much

| Lever | Effect | Source |
|---|---|---|
| Chain of thought, CRT, davinci-003 | correct 5 to 28 percent; intuitive 80 to 29 | c02 |
| 30 few-shot examples, CRT type-1 | accuracy 0 to about 78 percent | c02 |
| Chain of thought, anchoring, GPT-4/4o | no removal | b17 |
| "Ignore the anchor", principles, reflection | no removal | b17 |
| Knowledge enhancement | anchoring 34.7 to 50.5 percent (worse) | c25 |
| Anti-DP decoding | 34.7 to 24.7 percent | c25 |
| Self-help rewrite, framing | 0 to 2.7 percent of biased elements left | c08 |
| SACD loop, FOMC, llama3.1-8b | bias score 0.3805 to 0.1570 | c22 |
| Multi-agent debate | 0.3805 to 0.5020 (worse); gpt-3.5 0.5155 | c22, c23 |
| Reflexion | 0.3830 (no change); PubMedQA llama3.1-70b 0.5585 | c22, c23 |
| Counterfactual few-shot | GPT-4 framing gap -0.405 to -0.570 (worse) | a23 |
| Best-practices-first | median sensitivity cut about 51 percent (up to 73) | c26 |
| Bias warning plus impersonated self-debiasing | median 12.9 to 8.3 percent | c26 |
| Restate each number | -0.015 signed score, p=.057 | d04 |
| Thinking on vs off | +0.031, p=.157, no gain | d01 |
| Both anchors shown | works only when hints straddle the benchmark | c05 |
| Order swap in judges | conflict rates 5 to 82.5 percent show the problem; swap/average fixes at 2x cost | d11 |

### 6.3 Agents and long contexts

- Early interpretations persist and model-written insight memory hurts: Hit@5 0.526 with insight memory vs 0.601 without (d08).
- Self-anchoring over five turns changes confidence in a model-specific way (Claude -0.032, p=.029; others none; N=15 per cell) (d09). Weak evidence.
- Cloned agents compound a shared anchor instead of cancelling it (96 to 15 percent efficiency) (d10).
- Code models copy irrelevant earlier context: Codex 32.9 to 2.4 percent (a22).
- Context around identical code flips verdicts: susceptibility framing 33.2, anchoring 23.5, halo 18.4 percent (d06).

### 6.4 Judges

Judges inherit order, verbosity, bandwagon and self-preference biases (d11 to d13, b20, c20, c21). Self-preference evidence is weaker than order evidence (Zheng: too few data). Nobody has tested a model judging its own output with random order at equal tokens.

### 6.5 Limits for our agent

Our agent's model is probably newer than most tested ones. Only Kraishan, Yao, Harshavardhan, Huang and Malberg (2025 to 2026) touch such models. They agree that numeric anchoring remains. They disagree on whether reasoning mode helps.

---

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, M memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Keep suggestive numbers out of the working context.** In S1 code moves any number or guess that is not part of the task (a stated estimate, an expert's figure, a prior verdict) into a marked block. Numeric hints pull model estimates, and the pull survives CoT, "ignore the anchor" and reflection. Keep the original wording beside the restatement, as S1 already does. | S1, G-input | [E] on the harm and the failure of prompt-level defences; [S] on the remedy itself | K10, K12, K25; a21, b17, c05, c25 |
| A2 | **Do not add "ignore the anchor" or "be careful" prompts as a fix.** Already in 4b; this subfield adds LLM numbers. Knowledge-enhancement prompts made anchoring worse (34.7 to 50.5 percent). | 4b | [E] | K12; b17, c25, d06 |
| A3 | **Paired-wording invariance as a bench test, not a runtime step.** For decisions, run gain/loss rewrites of the same options to find where the agent flips. | S1, bench | [E] that framing moves models | K17; a23, b12, c12 |
| A4 | **No critique or debate step that sees a copy of the proposer's framing.** Debate raised bias (0.50 vs 0.38); cloned agents amplified an anchor. Matches G9. | G9, G-no-echo | [E] | K15; c22, c23, d10 |
| A5 | **Randomise candidate order in any model-based comparison; never show authorship or a majority cue.** Order swaps flipped 5 to 82.5 percent of verdicts; over 70 percent followed a fake majority cue. Matches G5. | G5 | [E] | K24; d11, d12, d13, b20, c20 |
| A6 | **Do not let stored model-written conclusions replace raw evidence.** Insight memory cost 7.5 points of Hit@5. Schema section 5 already shows lessons only after the first attempt. | M | [E] | K31; d08, d09 |
| A7 | **Measure with repeats and a pre-set scoring rule.** Anchoring is a noisy individual measure and the scoring rule changes the verdict. At least 10 repeats; directional low-vs-high gap. | G7, bench | [S] (single studies on noise and scoring) | K09, K34; b08, d19 |
| A8 | **Use fresh paraphrased items and shuffled option order in all bias tests.** Standard vignettes score 12 of 12; rewrites break models. | bench | [E] | K21; c16, c17 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | **S1 rewrite step (self-help / SACD style) at equal tokens** versus plain, CoT and "ignore anchor". Best-supported fix in LLM studies, never tested head to head on a 2025 reasoning model. | S1 | [E] on older models; [S] on current | K14; a23, c08, c22 |
| T2 | **Generate-then-compare**: the agent writes its own estimate before seeing the hint. No LLM study. | S1/S3 | none for models | critique gap 4 |
| T3 | **Counter-anchor**: opposing anchors in a marked block. Works only when hints straddle the truth. | O8-like reframe | [S] | K13; b17, c05 |
| T4 | **Best-practices-first** injection. About 51 percent cut in sensitivity; anchoring baseline already low. | S1/M | [S] | K16; c26 |
| T5 | **Strip source labels from numbers before any thinking step.** Thinking can amplify authority-tagged anchors. | S1, G-source | [S] abstract only | K28; d05 |
| T6 | **Restate every number** line. p=.057. | S1 | [S] | d04 |
| T7 | **Base-rate line first**, posterior computed in code, for Bayes-type items. | S1, G-prior | [E] in humans; untested in models | K06 |
| T8 | **Relevance filter on irrelevant context** (code models, long contexts, vulnerability triage). | S1, G-context | [S] | K18, K30 |
| T9 | **Thinking on/off at matched weights** for our own model, signed scores, 10 repeats. | G11 | [C] | K11, K27 |
| T10 | **Order-randomised self-verification at S8**, judged by a different model than the generator. | G5, S8 | [E] on order, untested on self-verification | K24 |
| T11 | **Ease-of-retrieval probe** (6 vs 12 examples before a frequency judgement). | S1/M | [E] in humans, no LLM study | K07 |

Not to add: any bias checklist, any "think slowly" line, any extremizing, any use of the model's confidence to stop (all in 4b).

---

## 8. Concrete tests on our bench

All arms get equal total tokens, counted including setup (G7). Items are fresh paraphrases with option order shuffled, at least 10 repeats per cell, scoring rule fixed before the run (directional low-vs-high gap in item SD units for anchoring; paired-wording flip rate for framing).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Anchor rewrite | 30 numeric estimate questions (distance, count, year) with low hint, high hint, none | plain; CoT; "ignore the hint"; code move-to-marked-block; model rewrite | high-minus-low estimate gap in item SDs | code and model rewrite shrink the gap by half or more; CoT and "ignore" under 15 percent (from b17, c05, c08) |
| B2 Generate-then-compare | same questions | own estimate first, then hint; plain | same gap | smaller gap; no prior LLM data |
| B3 Thinking on/off | same questions plus framing pairs | thinking off vs on, same weights, same total token ceiling | signed bias score; dose-response over realised tokens | about zero difference (d01); possible increase for authority-tagged hints (d05) |
| B4 Source credibility | hints labelled "random number", "intern", "chief judge" | label kept; label stripped | share of answers within 10 percent of the hint | stripped label removes the credibility sign flip |
| B5 Framing invariance | 20 decisions, each in gain and loss wording, options fully written | plain; rewrite to neutral frame; both frames shown | share of items whose choice flips | rewrite drops flips toward 0; baseline for current models unknown |
| B6 Base-rate line | 20 Bayes items (cab, medical test, Tom W. style) | plain; base-rate line first with code posterior; CoT | absolute error to the Bayes answer | base-rate line cuts error; human gap is 41 vs about 80 percent on the cab item |
| B7 Irrelevant context | 40 tasks with a prepended irrelevant function or paragraph | no filter; code relevance filter; model summary | accuracy | filter recovers most of the drop (Codex 32.9 to 2.4 percent in the original) |
| B8 Judge order | answer pairs with a known winner | fixed order; random order; swap-and-agree on close calls only | accuracy; position consistency | random order removes systematic bias at no cost; swap-and-agree adds accuracy on close calls at 2x tokens on those items |
| B9 Self-anchoring | 5-turn tasks where turn 1 states a guess | raw evidence only; earlier conclusions visible | confidence drift; final accuracy | visible conclusions lower accuracy (d08: 0.601 vs 0.526) |
| B10 Ease of retrieval | frequency judgements after listing 6 vs 12 examples | list 6; list 12 | judged frequency | possible reversal; no LLM data |
| B11 Critique echo | proposer with framed prompt, then critic | critic sees proposer prompt; critic sees neutral restatement | bias score after critique | neutral restatement avoids the rise (0.38 to 0.50 in c22) |

---

## 9. What does not transfer, and why

- **Human mechanism claims.** Insufficient adjustment, selective accessibility and the prospect-theory value curve describe people. For a model there is no start-and-adjust process we can read. Use the human literature for what to test, not for how the model works.
- **Human effect sizes.** Many Labs 2 cut the median d from 0.60 to 0.15. Do not set any correction strength from original lab effects (K03). Calibrate on the agent.
- **The incidental-anchor null.** It failed in humans (d=0.04, N=6,826). In models, irrelevant hints still pull in some studies (Lou and Sun test an irrelevant-hint type; code models copy irrelevant lines). Do not rely on the human null.
- **Linda and CRT numbers.** These items are heavily in training data. Model scores on them measure memory of the answer as well as bias. Only fresh items count.
- **Individual-difference findings.** Reflection and ability predict fewer errors in people. Models have no stable trait; use repeats instead.
- **Incentives.** Payoffs did nothing for anchoring in humans (b06). The model has no stake. Token budget is the only analogue and it has not helped (d01).
- **Frequency format and ambiguity.** The Linda wording debate is about English pragmatics in people. For a model it is a prompt-form effect worth testing, but it is contested in humans.
- **Availability.** Humans retrieve from a life of events; models retrieve from training frequency. The 6-vs-12 ease effect has no obvious model analogue (the model feels no effort).
- **Framing sign.** The human direction is not the direction in current models (d03). A scheme that tries to "undo the human bias" could push the wrong way. Test invariance, not direction.
- **Debiasing by awareness.** In people a reminder helps a little (.613 to .499). In models bias warnings help partly in one study (12.9 to 10.3 percent median) but schema 4b excludes checklists by default.

---

## 10. Open questions

1. Does an S1 input rewrite beat CoT and "ignore the anchor" at equal tokens on a 2025 reasoning model? No head-to-head study exists (critique gap 1).
2. Is the reasoning-mode effect on bias due to tokens or to training? Kraishan toggled thinking at matched weights for Claude and GPT-5.1; DeepSeek and Qwen are not separated (d01, d02). Yao finds amplification; Huang finds reduction.
3. How large are the effects on frontier models with fresh items and 10 or more repeats? Kraishan used 10 samples but only 5 items per bias from the public benchmark.
4. Does generate-then-compare cut anchoring in models?
5. How do irrelevant earlier numbers in long, multi-turn contexts affect bias? RealICU and Harshavardhan are indirect.
6. Which critique designs avoid copying the biased frame?
7. Are base-rate and sample-size errors present in current models on rewritten items? Two representativeness papers (d18) could not be opened.
8. Primary reads of T&K 1981 and 1983 and Gigerenzer 1991 are missing for Linda, Tom W. and Asian disease.
9. Do the human moderators (expertise, extremity, distance, relevance) predict model anchoring? Humans disagree on relevance (b07 vs d16).
10. Does a model judging its own output still favour itself when order is random?
11. Why is anchoring near zero in a code-length task (Shaki) while numeric Q&A anchors? Task type or model?
12. Do bias scores correlate across biases in models? If not (as in humans, b24), one overall "bias score" is the wrong summary.

---

## 11. Sources

[V] = full page or PDF text opened by the evidence agents. [M] = snippet or abstract only. Where a [V] source was read from an abstract only, this is stated.

**Founding and human literature**
- [V] Tversky and Kahneman (1974) Judgment under uncertainty. https://web.archive.org/web/2020/https://www2.psych.ubc.ca/~schaller/Psyc590Readings/TverskyKahneman1974.pdf (a01 to a08)
- [V] Tversky and Kahneman (1983) citation-classic note. https://garfield.library.upenn.edu/classics1983/A1983QG78800001.pdf (a09)
- [V] Klein et al. (2018) Many Labs 2. https://journals.sagepub.com/doi/pdf/10.1177/2515245918810225 ; https://osf.io/preprints/psyarxiv/9654g/ ; https://doi.org/10.1177/2515245918810225 (a13, a14, b01 to b04, d14)
- [V, second-hand] Klein et al. (2014) Many Labs 1 anchoring items and Jacowitz and Kahneman (1995), as tabulated in a LessWrong review. https://www.lesswrong.com/posts/eXwpbnSeRHTahvJAx (a11, a12)
- [V] Kakinohana, Pilati and Klein (2023) Does anchoring vary across cultures? https://osf.io/preprints/psyarxiv/xm94b/ (b05)
- [V] Schley and Weingarten (2026) Metastudy on anchoring moderators. https://osf.io/preprints/psyarxiv/tyq7f/ (b06, b07)
- [V] Rebholz et al. (2026) Reliability of anchoring. https://osf.io/preprints/psyarxiv/5u8br/ (b08)
- [V] DeKay (2025) Risky-choice framing with matched options. https://osf.io/preprints/psyarxiv/nfwp3/ (b09)
- [M] Mayer and Rebholz (2024) Navigating anchor relevance. https://doi.org/10.31234/osf.io/69jwr (d16, abstract only)
- [M] Nawaz (2026) Reframing anchoring bias measurement. https://doi.org/10.31234/osf.io/b9vyz_v1 (d19, abstract only)
- [V] Stegmueller, Binder and Krauss (2024) Natural frequency effect. https://doi.org/10.3389/fpsyg.2024.1296359 (d15)
- [M] Incentivization meta-analysis (OSF, 2022). https://osf.io/preprints/psyarxiv/f6h2c/ (b23)
- [M] Dispositional intuitive vs deliberative thinking (OSF, 2026). https://osf.io/preprints/psyarxiv/v4uwg/ (b24)
- [M] Ryu, Kim and Kim (2024) Representativeness heuristics in LLMs. https://doi.org/10.1109/access.2024.3474677 (d18, not opened)
- [V, secondary] Wikipedia: Anchoring effect; Anchoring (cognitive bias); Framing effect (psychology); Conjunction fallacy; Representativeness heuristic; Availability heuristic; Heuristic (psychology). https://en.wikipedia.org/wiki/Anchoring_effect ; https://en.wikipedia.org/wiki/Anchoring_(cognitive_bias) ; https://en.wikipedia.org/wiki/Framing_effect_(psychology) ; https://en.wikipedia.org/wiki/Conjunction_fallacy ; https://en.wikipedia.org/wiki/Representativeness_heuristic ; https://en.wikipedia.org/wiki/Availability_heuristic ; https://en.wikipedia.org/wiki/Heuristic_(psychology) (a10, a15 to a19, a29, b21, b22, b25 to b27)

**Language-model studies**
- [V] Jones and Steinhardt (2022) Capturing failures of LLMs via human cognitive biases. https://arxiv.org/abs/2202.12299 (a22, b10 to b12, c10, c11)
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (a20, b13, c17)
- [V] Hagendorff, Fabi and Kosinski (2023) Thinking fast and slow in LLMs. https://arxiv.org/abs/2212.05206 (a28, b14, c01 to c03)
- [V] Suri et al. (2023) Do LLMs show decision heuristics similar to humans? https://arxiv.org/abs/2305.04400 (a21, b15, c09)
- [V] Shaki, Kraus and Wooldridge (2023) Cognitive effects in LLMs. https://arxiv.org/abs/2308.14337 (a25, c18)
- [V] Itzhak et al. (2024) Instructed to bias. https://arxiv.org/abs/2308.00225 (a26, b18, c19)
- [V] Yax, Anllo and Palminteri (2024) Studying and improving reasoning in humans and machines. https://arxiv.org/abs/2309.12485 (c16)
- [V] Macmillan-Scott and Musolesi (2024) (Ir)rationality and cognitive biases in LLMs. https://arxiv.org/abs/2402.09193 (a27, b19, c14, c15)
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811 (a23, b16, c07, c08)
- [V] Lou and Sun (2024) Anchoring bias in LLMs. https://arxiv.org/abs/2412.06593 (a24, b17, c04 to c06, d17)
- [V] Malberg et al. (2025) Comprehensive evaluation of cognitive biases in LLMs. https://arxiv.org/abs/2410.15413 (c12, c13)
- [V] Lyu et al. (2025) Self-adaptive cognitive debiasing. https://arxiv.org/abs/2504.04141 (c22, c23)
- [V] Huang et al. (2026) Understanding the anchoring effect of LLMs. https://arxiv.org/abs/2505.15392 (c24, c25)
- [V] Sovrano, Dominici and Bacchelli (2026) Mitigating prompt-induced cognitive biases. https://arxiv.org/abs/2604.16756 (c26)
- [V] Kraishan (2026) The long road to the same answer. https://arxiv.org/abs/2610.10049 (d01 to d04)
- [M] Yao (2026) When the thinking mode strengthens the anchor. https://doi.org/10.2139/ssrn.6975478 (d05, abstract only)
- [V] Shahriar et al. (2026) Words speak louder than code. https://arxiv.org/abs/2606.30587 (d06)
- [V] Chergui et al. (2026) Mitigating anchoring bias in LLM-based agents. https://arxiv.org/abs/2606.18272 (d07)
- [V] Shen et al. (2026) RealICU. https://arxiv.org/abs/2605.13542 (d08)
- [V] Harshavardhan (2026) Self-anchoring calibration drift. https://aclanthology.org/2026.gem-main.4/ (d09)
- [M] Hantel (2026) Small bias, large failure. https://doi.org/10.2139/ssrn.7095458 (d10, abstract only)

**LLM judges**
- [M] Koo et al. (2023) Benchmarking cognitive biases in LLMs as evaluators. https://arxiv.org/abs/2309.17012 (b20, c20, c21)
- [V] Wang et al. (2023) LLMs are not fair evaluators. https://arxiv.org/abs/2305.17926 (d11)
- [V] Zheng et al. (2023) Judging LLM-as-a-judge. https://arxiv.org/abs/2306.05685 (d12)
- [V] Ye et al. (2024) Justice or prejudice? https://arxiv.org/abs/2410.02736 (d13)

**Not obtained.** Primary T&K 1981 and 1983 papers and Gigerenzer 1991 could not be fetched. Linda, Tom W., cab and Asian disease numbers are second-hand.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 13 established claims: 7 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E18.03-K02** (reworded: the sources support less). Numbers verify (Many Labs 2: d=0.30 N=207 vs d=0.04 [-0.01,0.09] N=6,826), but they come from one incidental-anchor paradigm (Critcher and Gilovich 2008 phone-name study), so 'incidental anchors do not replicate' is wider than the evidence; Schley and Weingarten support relevance and distance as moderators for explicit anchors only. Corrected claim: In Many Labs 2 the incidental-anchor effect of Critcher and Gilovich 2008 (phone name P97 vs P17) did not replicate (d=0.04, 95% CI [-0.01, 0.09], N=6,826 vs original d=0.30, N=207); Wikipedia reports random-anchor studies (die roll, random button) also failed to replicate, and in Schley and Weingarten's explicit-anchor study (N=1,967) the effect was larger when the anchor applied to the target judgment and was farther from the centre of unanchored beliefs.
- **E18.03-K04** (reworded: the sources support less). Numbers verify (ML2 jacket/calculator OR 4.96 to 2.06, d 1.08 to 0.40; DeKay OR 1.84), but the ML2 item is Tversky and Kahneman 1981 Study 10 (cheap vs costly item, mental accounting), not a gain/loss risky-choice problem, so it is not evidence about risky-choice framing weakening; the claim's own caveat contradicts using it as the headline. Corrected claim: Risky-choice (gain/loss) framing persists: DeKay (2025, N=1,697) found a framing effect for completely described, matched options (OR=1.84, 95% CI for b [0.29, 0.93]) and in seven of nine matched comparisons, while part of the classic effect depends on mismatched option wording. Separately, Many Labs 2 replicated the Tversky and Kahneman 1981 Study 10 cheap/costly-item framing at roughly half the original size (OR 4.96 to 2.06; d 1.08 to 0.40), which is a different framing task, not a risky-choice problem.
- **E18.03-K06** (now single-source: the sources are not independent). Numbers verified in Tversky and Kahneman 1974 (no description: base rates used; worthless description: .5; hospital 21/21/53 = 95 students), but both listed primary entries are the same 1974 paper and Wikipedia just relays it; 'small-sample insensitivity is common' rests on one student question.
- **E18.03-K07** (reworded: the sources support less). T&K 1974 supports the committee-estimate availability bias, but the ease-of-retrieval and moderator findings (Schwarz 1991, Vaughn 1999) were only read second-hand via Wikipedia, and the Schwarz result is that recalling 12 assertive examples gave lower assertiveness self-ratings than recalling 6 (and the reverse for unassertive recall), not that 12 examples generally lower self-ratings. Corrected claim: Availability judgments depend on ease of retrieval, not only the number of examples recalled: in Schwarz and colleagues' study (as reported on Wikipedia, primary not read) participants who recalled 12 assertive behaviours, a hard task, rated themselves less assertive than those who recalled 6; Vaughn (1999), as reported there, found the effect of listed-example count only when uncertainty was high (start of semester, hardest exam); Tversky and Kahneman (1974) showed availability-type biases in committee-count estimates (median 70 for 2-member vs 20 for 8-member committees; correct answer 45).
- **E18.03-K12** (reworded: the sources support less). Lou and Sun, Huang (Llama-3.1-8B 34.7 to 50.5), Sovrano (CoT 16.1 vs 12.9 baseline) and Kraishan (p=.057) check out, but in Shahriar et al. the 83-88% combined attack success is the weak defense; the strong ignore-context defense cut it to 88.45 (LLaMA 4), 69.23 (LLaMA 3), 49.32 (DeepSeek) and 67.80 (Qwen). Corrected claim: Simple prompt fixes do not remove LLM anchoring: CoT, 'ignore the anchor', principles and reflection leave significant anchor effects (Lou and Sun); knowledge enhancement raised Llama-3.1-8B's anchoring ratio from 34.7 to 50.5 percent (Huang); CoT was worse than baseline overall on PROBE-SWE bias sensitivity (16.1 vs 12.9 percent, Sovrano); in code review, a weak ignore-context prompt left combined attack success at 83 to 88 percent on four open models while a stronger one lowered it to 49 to 88 percent (Shahriar); a verbalise-the-anchor line lowered anchoring on 5 of 5 items but only at p=.057 (Kraishan).
- **E18.03-K17** (now contested: a source does not say this). The Jones & Steinhardt 2022 paper (arXiv 2202.12299) is about Codex and GPT-3 anchoring/framing of code and estimates and contains no Asian disease experiment, 704 prompts, 74% die-frame figure or save-probability boundary; the other numbers (GPT-4 40.5%, Malberg framing 0.41, Kraishan -0.336 on five items, seven models) check out.
