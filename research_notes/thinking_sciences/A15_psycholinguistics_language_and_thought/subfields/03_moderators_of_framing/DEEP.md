# Moderators of framing: deep document

*Subfield A15.03. Scope: what removes, shrinks or enlarges a framing effect (credible information, load, time pressure, second language, expertise, individual differences) and what that means for one language-model agent run through a scaffold. Evidence ids (a01, b05, c10, d28 ...) point to evidence_a-d.jsonl; claim ids (A15.03-K01 ...) point to claims.jsonl. Cross-checks are from critique.md.*

## 1. What it is

A framing effect is a change in choice or judgment caused by how logically equivalent information is worded. The classic case is the Asian disease problem. "200 people will be saved" and "400 people will die" describe the same outcome. People choose differently anyway.

A moderator is anything that makes the effect larger, smaller or absent. This subfield asks four questions.

1. Does credible information remove the frame? (Druckman 2001.)
2. Do load and time pressure change it?
3. Is it weaker in a second language? (Keysar 2012.)
4. Do expertise and individual traits protect against it?

Why this matters for our agent. We build one LLM agent that thinks through a scaffold, not through training. If a framed prompt can swing the answer, the scaffold must clean the prompt or check against a second wording. The moderators tell us when a cleaned prompt is enough. They also tell us which human "fixes" (credible advice, slow thinking, a foreign language) have an LLM analogue and which do not.

Three kinds of "framing" appear in the literature. Keep them apart.

- **Equivalence framing.** Same facts, different wording (gain vs loss, "saved" vs "die"). This is the core of the human work.
- **Emphasis framing.** Different considerations are highlighted (free speech vs public safety). Druckman's source-credibility work and Chong and Druckman 2007 are mostly this.
- **Polarity or wording framing in LLM papers.** "Is it X?" vs "Is it not X?", "admit?" vs "reject?". Many LLM studies measure this and call it framing. It is a looser notion.

Short answer to the subfield question. In humans, a credible and relevant source, a tight time limit, a heavy memory load and (weakly, unreliably) a second language all move the effect. In LLMs, the best-supported lever is cleaning the input in code (rewrite the numbers into one canonical form). It is not telling the model to be careful, not adding a source label, not changing language, and not adding thinking tokens.

## 2. History and theories in depth

### 2.1 The founding effect

Tversky and Kahneman (1981), as restated in Druckman 2001 (a05, second-hand): in the Asian disease problem, 72% chose the sure program in the gain frame (N=152) and 22% in the loss frame (N=155). That is a shift of about 50 points. McNeil et al. (1982) found 44% preferring radiation under a "dying" frame and 18% under a "living" frame (26-point reversal). The original papers were not opened by us.

Size across the literature (a11, d19, Kuhberger 2023 review): the 1998 meta-analysis gave d = .31 (over 100 studies, over 200 effect sizes, about 30,000 people). A later publication-bias corrected update gave d = .52 and .56. Many Labs gave d = .60. A survey of over 100,000 people in 49 countries gave h = .612 (95% CI .568 to .656). Variants range from d = .16 to .91. Goal framing is near zero. Attribute framing has no comparable meta-analysis. About a quarter of people show no effect in the original design. Note from the cross-check: the corrected estimate (.52) is higher than the raw one (.31). The review explains it as "no publication bias in framing research", but this is argued, not tested.

### 2.2 Credible advice (Druckman 2001)

The claim: framing effects look large because lab participants decide alone. Give them advice from a source they find credible, and the effect shrinks or vanishes (a01). Two experiments with undergraduates.

- Experiment 1 (Asian disease with party endorsements), N = 464, six conditions, party identification measured about three weeks earlier. Credibility of sources pretested.
- Experiment 2 (McNeil lung cancer with specialist endorsements), N = 313, six conditions.

The mechanism is information, not suggestion. Advice tells people which option is better, so following it does not break invariance. This is the author's own point (a01).

A second Druckman paper (Journal of Politics 2001, a06, a07) shows that emphasis frames only work when the source is credible. Powell moved opinion on aid to the poor; Jerry Springer did not. The New York Times moved tolerance of a KKK rally; the National Enquirer did not. Belief-content measures did not change, so the frames changed which considerations were weighted, not what people believed (a07).

### 2.3 Frame strength and competition (Chong and Druckman 2007)

Frames work through accessibility (priming a consideration) and applicability (judged fit) (a10). Strong frames move opinion alone and win when two frames compete. Weak frames that invoke unavailable considerations do nothing. Repeating a weak frame never let it beat a strong opposing frame. Low-knowledge people were moved by weak frames in one-sided settings; knowledgeable people dismissed them. Competition between frames made everyone evaluate more carefully (a08, a09). Studies: N = 869 (urban growth), N = 1,277 (rally), 17 conditions.

### 2.4 Time pressure and load

Dual-system story: time pressure shuts down slow deliberation, so the fast emotional response (and thus the frame) dominates. Rival story from Roberts, Teoh and Hutcherson (2022; a13, b01, b02): under a one-second limit, people look first at the reward-coloured option and cut their search short. Less reading, not a separate fast mode, produces the larger effect. Eye tracking shows this account is sufficient, not that dual systems are wrong.

Working-memory load (Hinson et al. 2019; a15, d20): only a non-affective digit load enlarged framing. Positive or negative affective loads did not. Framing was large on trials where the participant got the knowledge probe wrong, small where they got it right. The authors read framing as non-engagement with the choice information.

### 2.5 Foreign-language effect

Keysar, Hayakawa and An (2012; a18, b05, d02): the Asian disease framing effect disappeared when the problem was read in a foreign language. The explanation: emotional distance and more deliberate processing. Costa et al. (2014) added a moral-dilemma version. Later work is mixed (section 5). The founding paper could not be opened (publisher blocked); numbers come second-hand from lecture slides (d02) and press summaries (d03).

### 2.6 Expertise and individual differences

Expertise: tennis players (2025; a16), 120 players per experiment (40 expert, 40 skilled, 40 novice). Novices stayed frame-susceptible even under time pressure. Experts followed the match situation. Only the abstract was read.

Individual differences: numeracy (Peters 2009; b20, abstract only), cognitive style (b09: moderated the effect in the larger online study but not the small one), age (unsettled: Strough 2011 says stable, a newer study cited via Wikipedia says more framing in older adults; b19, b18). Thinking-style scales give "no consistent picture" (a12).

### 2.7 Equivalence is itself a level question

Kuhberger 2023 (a12), following Sher and McKenzie: even logically equivalent frames carry information when a speaker chooses them. A listener may infer the speaker's reference point. So "remove the frame" has levels: surface words, then the information leaked by the speaker's choice of wording. Native vs foreign-language instruction is itself a (level 4) framing.

### 2.8 Why LLM work reuses this

LLM papers import the same set of ideas: source labels as credibility (Germani; Bajaj), reasoning budget as time (Kraishan), irrelevant context as load (not yet tested), prompt language as foreign language (BiasLab, Pantana), persona as expertise (d27, d15). The mapping is loose. Section 6 reports what was actually measured.

## 3. Core findings with exact numbers

Status key: established = two or more independent sources agree and numbers were opened; single-source = one study or no replication; contested = sources disagree.

### 3.1 Human findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Asian disease frame effect (original) | Gain: 72% sure (N=152). Loss: 22% sure (N=155). About 50-point shift. | Tversky and Kahneman 1981 via a05 | Established |
| McNeil lung-cancer frame (original) | Radiation 44% (dying) vs 18% (living) | McNeil 1982 via a05 | Established |
| Risky-choice framing size | d=.31 (1998), .52 (bias-corrected), .60 (Many Labs); h=.612 [.568,.656], over 100,000, 49 countries; Asian-like studies 63% vs 41% sure | a11, d19 | Established |
| Credible advice cuts the effect, McNeil (Exp 2) | No advice: 44% (N=46) vs 13% (N=53), reversal 31% (z=3.45). Surgery endorsed: 22% vs 13%, reversal 9%. Radiation endorsed: 44% vs 38%, reversal 6%. | Druckman 2001 (a04) | Single-source |
| Credible advice, Democrats (Exp 1) | Neutral: 70% (N=30) vs 24% (N=34), reversal 46% (z=3.73). Democrat label: 77% vs 56%, reversal 21%. Republican label: 31% vs 16%, reversal 15%. | a02 | Single-source |
| Credible advice, Republicans | Neutral reversal 41% (65% N=20 vs 24% N=21). Republican endorsement: 4%. Democrat label: 5%. | a03 | Single-source |
| No credible source, no protection (Independents) | Neutral reversal 45% (z=2.94). With party labels 30% and 28%. | a03 | Single-source |
| The 46% to 21% drop for Democrats is weak | z=1.61, p=.054 one-tailed. "More than half" is a point estimate. | critique.md | Caveat |
| Source credibility gates emphasis frames | Powell: t(105)=2.21, p=.015; Springer: t(101)=.55, p=.29. NYT: t(34)=2.13, p=.02; Enquirer no difference. | a06, a07 | Single-source |
| Frame strength beats repetition | Weak frames moved only low-knowledge people; strong frames won under competition. N=869 and N=1,277. | Chong and Druckman 2007 (a08, a09) | Single-source |
| Trust-in-source moderates verbal-probability framing | Exp 1 (N=191): interaction F(1,190)=11.35, p=.001, eta2p=.06. Exp 2 (N=453): same pattern, not significant. Exp 3: unvaccinated did better with the negative frame from a trusted physician. | 2023 vaccine study (d18) | Contested |
| No direct replication of Druckman found | One search; absence is weak evidence | d31 | Gap |
| Time pressure enlarges framing (replication) | 1 s limit: gamble choice gain .34 vs loss .64, d=1.52. No limit: .52 vs .64, d=.75. Interaction F(1,44)=57.06. Gain frame d=1.32; loss frame d=.003. N=45 analysed (61 tested; eye tracking N=40). | Roberts 2022 (a13, b01) | Established (small N) |
| Time pressure, attention mechanism | First fixation on gamble: gain .42 (no limit) vs .32 (limit); loss .58 vs .60. F(1,39)=20.63. | b02 | Single-source |
| Time pressure, second lab | N=26 analysed. Risky choice, gain: .11 vs .36; loss: .85 vs .49. Interaction F(1,25)=309.50, partial eta2=.93. RT about 650-680 ms vs 2.0-2.5 s. Loss-frame change contradicts Roberts. | Gong 2026 (a14, b03) | Single-source |
| Time-pressure moderator overall | Review: thinking-style scales "no consistent picture"; Svenson and Benson 1993 and Szaszi 2022 report limited effects | a12, a14 | Contested |
| Non-affective working-memory load enlarges framing | N=80 (76 analysed). Load check F(2,54)=27.05. Accuracy .78 vs .99/.98. Framing difference .10, SEM .04, p=.016. | Hinson 2019 (a15, d20) | Single-source |
| Expertise reduces framing | 120 players per experiment (40/40/40). Effect sizes not extracted. | Tennis 2025 (a16) | Single-source |
| Foreign-language effect, original | Native: 77% sure in gain vs 47% in loss. Gone in L2 across 3 experiments, 3 L2s, 2 L1s. Exp 3: bets taken 71% Spanish vs 54% English, t(52)=-2.04, d=-.55. | Keysar 2012 via d02 (second-hand) | Contested |
| Foreign-language moral effect | 20% to 33% utilitarian, chi2(1,N=317)=6.9, p<.01 | Costa 2014 (b21) | Established (not framing) |
| Foreign language, framing nulls | Asian disease kept in 4 of 5 L2 groups (N=104 Exp 1; Exp 2 groups 77, 44, 21). N=475 and N=503: equal framing in both languages, effect only on footbridge. Gambling N=409: equal. | Dylman and Samuel 2026 (d01), d06, d07 | Contested |
| Foreign language, risk-taking | 4 experiments: 1 clear effect, 2 nulls, 1 general increase | Hayakawa 2019 (b06, d05) | Contested |
| Foreign language, deliberation | N>500: native, switching and L2 equal on CRT, ratio bias, probability matching, base rate | a21 | Single-source |
| Foreign-language sign flips | N=129 Hadza: non-native decreased risk preference; dilemmas still utilitarian | a20, b07 | Single-source |
| Framing measures converge poorly | N=159. Vignette vs gambling rs=.167 pooled (p=.040); loss domain rs=.056 | Zhen and Yu 2016 (b08) | Single-source |
| Experience does not remove framing | MTurk Asian disease: 32.3 points (standard) vs 36.4 (inexperienced); group x condition OR=-1.14, p=.80 | b10 | Single-source |
| Cognitive style moderates (sometimes) | Study 1 N=43; Study 2 N=262; risk style moderated both, cognitive style only in the larger one | b09 | Contested |
| Real-world frame choice moves behaviour | About 30% enrolled under "$5 a day" vs about 7% under "$150 a month" | Hershfield 2020 via Wikipedia (b18) | Single-source (secondary) |

### 3.2 LLM findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Models show a framing effect on classic items | GPT-3 showed framing, certainty effect, overweighting (3 of 6 biases) | Binz and Schulz 2023 (a24, b12) | Single-source |
| ChatGPT, attribute frame, deterministic | 5/7 in all 11 gain trials, 4/7 in all 11 loss trials; humans 5.2 vs 4.6, t(80)=3.86 | Suri 2023 (a23) | Single-source |
| Category change across 7 LLMs | 32.41% [30.48, 34.36] of 2,880 prompts (240 scenarios). GPT-4o-mini 63.33%; GPT-5 33.40%; Gemini 2.5 Pro 32.56%; GPT-4.1-mini 29.17%; Gemini 3 Flash 23.38%; Claude Sonnet 4.6 22.81%; Qwen3-VL-235B 21.58%. Direct reversal 0.63%; 98.1% of 2,153 changes involve "uncertain". Same-frame noise 7.12%; cross-frame 34.32%. | FrameBench (a28, d28) | Established |
| Framing risk shift by probability | .535 at 20% success, .287 (40%), .209 (60%), .109 (80%) | d28 | Single-source |
| Probability canonicalisation | 36.81% to 6.68% [5.12, 8.51] (paired drop 27.52 points). Frame-robust instruction 22.83%. Conversational 34.20%. Risk shift .363 to -.010 (canonical) and .154 (instruction). 32 scenarios, 3 models, 3 repeats. | FrameBench (a29, d28) | Single-source |
| Self-help rewriting | GPT-4 admissions gap -0.405 to -0.010. GPT-3.5 +0.165 to -0.080. Biased prompts left: 0%, 1.4%, 2.7%. | Echterhoff 2024 (a25, d11) | Single-source |
| Awareness prompt backfires on GPT-4 | Admit 0.360 vs reject 0.830, delta -0.470, worse than baseline -0.405 | d11 | Single-source |
| Generic warning, medical case | GPT-4 framing discrepancy 66% to 45%, p=.003; all ten biases down 6.9% on average; named the right bias in 5% | Wang and Redelmeier 2025 (d15) | Single-source |
| Generic debias prompt | Framing accuracy 35.6% to 41.4% (+5.8); Hyperbolic -13.4; Disposition -11.6; Mental accounting about -20; position independence +40.5%, judgment accuracy -4.4% | CogBias 2026 (c04, d24) | Single-source |
| DeFrame (show both framings) | Cuts disparity 92% and bias score 93% on BBQ, 8 small models; 4 calls per question | Lim 2026 (a31, d12) | Single-source |
| Judges flip with polarity | 14 judges, none robust. GPT-5-mini 5.69%, GPT-5 5.77%, LLaMA 3.2 1B 66.29% inconsistency | Hwang 2026 (c01) | Established |
| Judge lean is a family trait | LLaMA agrees, OpenAI rejects, Qwen mixed. Cell values garbled; example cells unverified | c02 | Single-source |
| Reasoning budget does not cut bias within a model | 30 vignettes, 6 biases, 7 models, ceilings 0/1,024/4,096/8,192, 12,350 calls; pooled delta +0.031, t(29)=1.45, p=.157 | Kraishan 2026 (c10) | Contested |
| Claude 4 with vs without thinking | Maritime +0.440 vs +0.404; Border +0.640 vs +0.562; Championship +1.800 vs +1.680; Business +0.080 vs -0.240 | Payne 2025 (d14) | Single-source |
| Visible thinking shrinks wording gap across models | Scenario B 81.1% (off) vs 25.4% (on); gap 75.7 vs 25.1 points; across 82 models, not within model | Wang and Zhang 2026 (d13) | Single-source |
| Reasoning-class models near frame-insensitive on lotteries | Correlation with expected-payoff maximiser 0.86-1 (reasoning) vs below 0.5 (conversational); 20 LLMs | Ge 2026 (d25) | Single-source |
| Direction can be reversed | Mean signed framing -0.28 to -0.87 across 7 models; anchoring +0.11 to +0.20. Career scenarios -0.37 to -0.60. | c11, a27 | Contested |
| Named vs blind task | gpt-oss-120B: .02 blind vs .62 named (canonical), .787 on invented scenarios named; persona low agreeableness -.319 | Bose 2026 (d27) | Single-source |
| Expert label as strong prior | Expert vs other-LLM beta=1.00 +/-0.06; switch odds 14.45x vs friend (CI 10.99-19.02); log-odds shift to a wrong prior at n=9: 7.97 expert, 3.70 LLM, 2.31 friend | Bajaj and Tiganj 2026 (d23) | Single-source |
| Models adopt supplied candidates | Adoption 93-100% after judging invalid; up to 99.4% held-out science; 12 LLMs, over 10 million trials | Kawada and Kellis 2026 (c19, d26) | Established |
| Tool evidence flips correct answers | External evidence helps weak beliefs, flips strong correct ones | Zhao 2025 (d30) | Established (with d26) |
| Sycophancy | Claude 1.3 wrongly admits mistakes 98% when challenged; weak wrong opinion cut accuracy up to 27% | Sharma 2024 (c17) | Established |
| Instruction register raises deference | Flagship scores +17 to +70 instructional vs near 0 to +28 conversational | Pander Score 2026 (c18) | Single-source |
| Source attribution shifts judges | 192,000 assessments; anti-Chinese bias Grok 2 -14.22%, o3-mini -2.64%; same Taiwan statement 50% blind, 0% misattributed | Germani 2025 (a32, b14) | Established |
| Bandwagon cue | 11 of 15 models heavily influenced; over 70% of evaluations followed the fake 85% statistic | Koo 2024 (c08) | Single-source |
| Authority-styled false context | Accuracy 71.1% to 38.0%; attack success 51.5%; authority-framed 69.5% | MedMisBench 2026 (d22; abstract) | Single-source |
| Verbal time pressure acts on LLMs | "High time pressure" cue: fewer tests (beta=-1.05), narrower differential; contraindication errors 8 of 56 runs in pressure + lean cell | Cureus 2026 (d16) | Single-source |
| Shorter reasoning raises inconsistency | No-Thinking and token budgets increased all three inconsistency kinds; numbers not extracted | Yang 2025 (d29) | Single-source |
| Position bias | First option 79.0%, 77.1%, 77.6% vs 36.8% chance on opinion items; order bias 30%, 56%, 66% | CogBias (c05, d24) | Single-source |
| Irrelevant leading context | Codex accuracy 32.9% to 2.4-10.6%; framing line copied in 62.2-92.7% | Jones and Steinhardt 2022 (a26) | Single-source |
| Formula in prompt fixes only the best model | GPT-4o deviation -0.05% to +0.11%; GPT-4 worse; LLaMA-8B no change | Liu 2025 newsvendor (c13) | Single-source |
| Price reframing cuts consistency | CCEI risk .901, time .884, social .698, food .894; 10,000 GPT tasks vs 347 humans | Chen 2023 (b13) | Single-source |
| Chat tuning raises bias | Certainty bias DaVinci 0.00 vs 0.67 (DaVinci-003); Mistral 0.03 vs 0.29 instruct | Itzhak 2024 (c15) | Single-source |
| Anchoring: instructions fail, opposing anchors help | Step-by-step, ignore, reflect did not remove the anchor; both-anchors strategy worked on straddling items | Lou and Sun 2024 (c06) | Single-source |
| Persona and affect | 67 cases, 4,020 prompts; shifts model-specific and away from consensus | Neurosurgical Review 2026 (d17) | Single-source |
| Multilingual framing item | Floor effect: GPT-3.5 and GPT-4 0% correct in all three languages | Pantana 2024 (d08) | Uninformative |

## 4. Mechanisms and models

This section is written so an engineer can turn each model into a switch or a test.

### 4.1 Information-use model (credible advice)

Human version. The decision maker has a weak prior on which option is better. The frame shifts the reference point. Advice from a credible source supplies the missing information, so the choice follows the advice and the frame drops out. The source must be believed to know and believed to share interests. Independents, who trust neither party, kept the effect (a03).

Implementation reading. In a prompt, "credible advice" means a verified signal: a computed expected value, a tool result, a test output. It does not mean a label. LLMs treat a label ("expert") as a strong prior whether or not it is right (d23). They also integrate candidates they have already judged invalid (d26). So the engineering rule is:

1. Put a code-computed fact beside the framed task. Example: "Expected deaths: A 400, B 400."
2. Never put an unverified source label or user belief in the prompt.
3. Keep the model's own unaided answer as a candidate and compare (tool evidence can flip correct strong-belief answers, d30).

Failure mode: the model has the information and ignores it (GPT-4 computes the right order quantity and adjusts it away, c13). Gate the final answer on the computed value in code.

### 4.2 Attention and search model (time pressure)

Human version (Roberts 2022). Under a tight limit, early fixation goes to the reward cue, search is cut short, and the gain-framed sure option wins more often. Prediction: the effect grows only where a salient cue dominates and search is truncated. Evidence: gain-frame d=1.32, loss-frame d=.003 (a13). A second lab disagrees on the loss frame (a14).

Implementation reading. For an LLM the analogue is what the model "reads" in a short budget. Candidate controls: (a) thinking-token cap, (b) short context, (c) option order. Pseudocode for a test: for budget in {0, 1k, 4k}: for pair in framed_pairs (order shuffled): record choice; compute gap = P(sure|gain) - P(sure|loss). The budget result so far is flat within a model (c10, d14) and mixed across models (d13).

### 4.3 Engagement model (working-memory load)

Human version (Hinson 2019). Framing is largest when the participant did not encode the choice information. Non-affective load lowers encoding. Implementation reading: irrelevant long context may bury the numbers. Prediction: the frame gap grows with distractor tokens placed before the task. Untested in LLMs (K06).

### 4.4 Language-distance and emotion model (foreign-language effect)

Human version: a foreign language adds emotional distance and fluency cost, so decisions are more deliberate (a18). Evidence against: deliberation tasks showed no benefit (a21); arousal did not predict the change (b04); only high-distance L2 groups looked protective, and that cell is 21 people (d01, d04). Implementation reading: an LLM has no verified analogue of emotional distance. A translated prompt may change tokenisation and training-data associations, not emotion. Treat as a low-priority test, not a mechanism.

### 4.5 Frame strength model (Chong and Druckman)

Effect size depends on availability, applicability and credibility, and is damped by competition and knowledge. Implementation reading. Showing both sides of a framed question is the competitive context, and it makes people evaluate more carefully (a09). DeFrame (show both framings, d12) and the both-anchors strategy (c06) are two LLM versions: the model sees the opposing frame, and the answer is compared across frames in code.

### 4.6 Script enactment (LLM-specific)

Bose (2026; d27) finds the framing effect appears when the prompt names the paradigm and is near zero when the same task is posed as routine work. A one-sentence persona flips the sign. Hypothesis: part of the "LLM framing" in the literature is the model playing a known experiment. Implementation: run every framing test blind (unnamed, routine wording) and named, and report both gaps. One model, one author; treat as a strong warning, not a law.

### 4.7 Canonicalisation (input hygiene)

The FrameBench mitigation (a29, d28). A code step finds each stated probability, writes both complementary forms in one standard layout ("20% chance of success, 80% chance of failure"), and passes only that to the model. Result: category change 36.81% to 6.68%, near the 7.12% same-frame noise floor. It beats a frame-robust instruction (22.83%) and a plain conversational prompt (34.20%). It works because the model no longer has to compute the complement itself, so the wording carries no extra information.

Limits: probability wording only; 32 held-out scenarios; 3 models; no token cost reported; consistency is not correctness.

### 4.8 Reframe-and-compare

Ask the same question in two framings (or two polarities), compare in code, and flag disagreement (c01, d12, d09). Disagreement is a free alarm. Cost: two or more calls. Not yet compared to canonicalisation at equal tokens (K23).

## 5. What holds up

### 5.1 Replications and meta-analyses

- Risky-choice framing is real and medium to large. Meta-analytic d about .3 to .6, and a 49-country sample gives h = .61 (a11, d19). Established.
- The time-pressure amplification replicated in a preregistered replication of Guo 2017 (a13) and in a second lab (a14). Both use about 26 to 45 analysed people. The loss-frame behaviour differs between the two. The mechanism (attention vs non-engagement) is not settled; Hinson supports non-engagement (d20). The Kuhberger review does not treat time pressure as a consistent moderator (a12).
- Foreign language: the moral-dilemma shift replicated (Costa, b21). Framing and risk-taking effects replicated poorly (section 5.2).

### 5.2 Failures and boundary conditions

- **Druckman 2001 has no direct replication.** One search found none (d31). The nearest independent test (d18) replicated the trust x framing interaction in Exp 1 only. All cells are small (N=14 to 55), samples are students, tests are one-tailed. The Democrats' drop from 46% to 21% has z=1.61, p=.054.
- **Not everyone follows advice.** At least 56% always chose surgery and at least 13% always radiation (a04).
- **No credible source, no protection.** Independents kept 28 to 30 of 45 points (a03).
- **Foreign-language effect.** Nulls: N=475 and N=503 (framing equal in both languages; effect only on footbridge, d06); Dylman and Samuel 2026 (4 of 5 L2 groups kept framing; d01); gambling N=409 (d07); N>500 on CRT, ratio bias (a21); the original lab's four experiments gave one clear effect (d05); Hadza sign reversal (a20). The sign depends on population and task. Mechanisms (emotion, deliberation) were not confirmed (b04).
- **Individual differences.** Convergence between two framing tasks is weak (rs = .167; .056 in the loss domain, b08), so a moderator found on one task may not transfer. Thinking-style scales give no consistent pattern (a12, b09).
- **Experience.** Familiarity with the problem does not remove the effect (b10). A model that has seen the Asian-disease text may still be framed; use novel scenarios.
- **Equivalence is not clean.** The speaker's choice of wording leaks information (a12). A "remove the frame" step has to remove that information too.

### 5.3 Interventions that worked and did not (humans)

Worked: credible, relevant advice (for audiences that trust the source); forced deliberation (Almashat 2008, via a12); experience instead of description for attribute framing (Poor and Isaac 2023, via a12); frame competition (a09); domain expertise (a16, abstract).

Did not work reliably: second language; thinking-style scales; naive familiarity.

### 5.4 Interventions that worked and did not (LLMs)

Worked, strongest evidence first:

1. Canonicalising numbers in code: 36.81% to 6.68% (single source, d28).
2. Rewriting the prompt neutrally (self-help): GPT-4 gap -0.405 to -0.010 (admissions only, d11).
3. Showing both framings (DeFrame): 92% disparity cut (small open models, fairness tasks, 4 calls, d12).
4. Showing opposing anchors: near the benchmark on straddling items (c06, anchoring).
5. Asking the model to restate the anchor: lower on all 5 items, p=.057 (c12; weak).
6. A reasoning-class model: near insensitive on lotteries (d25).

Did not work or backfired:

- Generic "be careful" prompts: +5.8 points for framing in CogBias, but -13.4 and about -20 on other biases (c04); worse than baseline on GPT-4 admissions (d11); framing 66% to 45% in one clinical case, with the right bias named 5% of the time (d15).
- Few-shot debiasing: pushed models to admit or reject nearly everyone (a25).
- Step-by-step, "ignore the hint", "reflect" for anchoring (c06).
- More thinking tokens within a model (c10, d14).
- A source label ("expert"): adds a large prior shift toward the label (d23).
- A persona: flips sign (d27); expert personas do not lift accuracy (d32, snippet only).
- Giving a formula: fixed GPT-4o, not GPT-4 or LLaMA-8B (c13).
- Generic fixes can hide the frame gap on average: measure the gap between frames (a31).

### 5.5 Cross-check corrections adopted

- Roberts 2022: 61 tested, 45 analysed in behaviour (df=44), 40 in eye tracking. The "N=40" in a13 is the eye-tracking sample.
- Echterhoff 40.5: percentage points (0.780 minus 0.375, Table 3), not a relative figure (d10 resolved the earlier doubt).
- Hwang 2026 example cells (80.08% LLaMA 3.1 70B) are from a garbled row; use only the headline numbers 5.69%, 5.77%, 66.29%.
- FrameBench 36.81% to 6.68% is the 3-model, 32-scenario test, not all 240; the appendix per-model table is garbled.
- Foreign-language per-cell numbers for Keysar 2012 are second-hand.

## 6. Language models

### 6.1 Do LLMs show framing?

Yes, but it depends on wording, scenario, model class and even whether the task is named.

- Older base and chat models: GPT-3 shows the classic frame (a24). ChatGPT shows a deterministic one-point shift on an attribute-frame rating (a23).
- Current models on advice vignettes (FrameBench, a28): the recommendation category changes in 32.41% of triplets, from 21.58% (Qwen3-VL-235B) to 63.33% (GPT-4o-mini). Almost all changes are into or out of "uncertain" (98.1%); direct yes/no reversals are 0.63%. Same-frame repeats disagree 7.12%, so the framing effect is about five times the noise.
- Magnitude depends on the probability: risk shift .535 at 20% success, .109 at 80% (d28).
- Other wording frames: yes/no polarity flips every one of 14 judges (c01); admit vs reject framing moves GPT-4 by 40.5 points (d10); an instrumental vs cooperative wording gives 4.3% vs 68.8% option B across 82 models (a30).
- Direction is not always the human one. All seven models in Kraishan leaned against the human framing pattern (c11). Career scenarios reverse (a27). GPT-3.5 and GPT-4 have opposite signs on admissions (d10). Always measure the signed gap.

### 6.2 Model class and training

- Instruction tuning and RLHF increase bias on the certainty effect (c15). Chat tuning appears to cause omission and wording bias (b11).
- Reasoning-class models are near insensitive on stake-free lotteries (d25, correlation 0.86 to 1 with an expected-payoff maximiser) but are still framed in vignettes (a27, c10). The authors tie it to maths-reasoning training.
- Size helps but does not remove: disparity is generally smaller in larger models (d12); small models can be at random level (c01).

### 6.3 Moderator by moderator

| Human moderator | LLM analogue | What was measured | Result |
|---|---|---|---|
| Credible advice | Source label / verified signal | Expert label: beta=1.00; 14.45x switch odds (d23). Candidate adoption 93-100% (d26). Authority-styled false context: 71.1% to 38.0% accuracy (d22). | A label is a prior, not evidence. Verified signals help weak states and can harm strong ones (d26, d30). No LLM test of "credible correct advice removes the framing gap" exists. |
| Source credibility gates a frame | Attribution to a nationality or LLM | Four LLMs, 192,000 assessments; anti-Chinese bias up to -14.22% (b14) | Models respond to claimed source. Hide authorship from judges. |
| Time pressure | Thinking budget | Flat within model (c10, d14); gap 75.7 to 25.1 across 82 models, thinking on vs off (d13); shorter reasoning raises inconsistency (d29); verbal "high time pressure" narrows search (d16) | Contested. No matched-budget frame-gap test. |
| Working-memory load | Distractor context | Irrelevant leading line 32.9% to 2.4-10.6% in code (a26); no frame-gap test with distractors | Open. |
| Foreign language | Prompt language | Only a floor-effect item (d08) and a polarity benchmark without per-language gaps (d09); human effect unreliable | Open and low priority. |
| Expertise | Persona / domain context | One-sentence persona flips the sign (-.319, d27); expert personas do not lift accuracy (d32, snippet) | Persona is not a debiaser. |
| Frame competition | Show both frames | DeFrame 92% disparity cut (d12); both anchors (c06) | Works, at higher cost. |
| Warning / awareness | "Be careful about bias" | +5.8 / -13.4 (c04); GPT-4 worse than baseline (d11); 66% to 45% in one case (d15) | Unreliable. |

### 6.4 What changed the gap, and by how much (ranked)

1. Canonicalise probabilities in code: 36.81% to 6.68% (single source).
2. Neutral rewrite by the model: -0.405 to -0.010 for GPT-4, admissions only.
3. Show both framings: 92% disparity cut, four calls.
4. Model class: reasoning-class near zero on lotteries.
5. Name the task or not: .62 vs .02 for gpt-oss-120B (a measurement hazard, not a fix).
6. Generic warning: at most a few points, sometimes negative.
7. More thinking tokens: no measurable change within a model.

### 6.5 Measurement hazards

- **Naming inflates.** Named framing .62, blind .02 (d27).
- **Order mimics frame.** First-option choice is 77 to 79% on opinion items vs 36.8% chance (c05). The CogBias authors measure it as a separate family, so it is not the frame gap (d24). Still, randomise option order.
- **Floor and ceiling.** Llama-2 7B and 13B reject almost everything (d10); Pantana's framing item is at floor (d08); GPT-4o is at ceiling in 5 of 6 vignettes in an omission study (b11).
- **Template effect.** Most human studies copy one template; DeKay 2022 varied domain, magnitude, 13 probabilities, format, order and layout and still found about 26 points (d19). LLM tests should vary these facets.
- **Justifications mislead.** Models give opposite verdicts and then write reasoning that justifies each (c03). Never test frame-freeness by reading the explanation.
- **Run-to-run noise.** Same-frame repeats disagree 7.12% (d28). Use repeats.
- **Preprints.** Many 2026 items are preprints with author-built tasks (CogBias, Kraishan with 5 items per bias, FrameBench with its own templates).

## 7. What our agent should take

Status codes: [E] established, [S] single-source, [C] contested. Schema parts refer to SCHEMA.md: G1-G12 guardrails, S0-S9 states, O1-O8 operators, memory.

### Add now (established)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| N1 | A bare framed prompt is a valid stress test. Use Asian-disease and McNeil pairs, with shuffled option order, to measure our model's signed gain-loss gap. This is a measurement, not a feature. | G7 | [E] | K01; a05, a11, d19 |
| N2 | Do not add generic "avoid bias" or "be careful" lines to the schema. They help framing a few points at most and backfire on other biases. A line stays only if it wins at equal tokens on the task. | G7, G11 | [E] | K11; c04, d11, d15, a25 |
| N3 | Any yes/no check (verify, critique, judge) is asked in both polarities and compared in code. Disagreement is an alarm, not an answer. | G5, S8 | [E] | K14; c01, c03, d09, a31 |
| N4 | The judge sees no authorship, source label, user belief or popularity claim. Strip these in S1. | G4, G5, S1 | [E] | K14, K15; b14, a32, c08, c17, d23 |
| N5 | Do not show the verifier a user's stated belief or a prior answer; verify in fresh context. | G2, G9, S3 | [E] | K15; c17, c19, c18, d26 |
| N6 | A supplied hint or candidate is not weighed by credibility. Keep the model's own unaided answer as a candidate. Gate the final answer on a code check, not on a model's judgement of the hint. | G2, G10 | [E] | K16; c19, d26, d30, c13 |
| N7 | Do not rely on written reasoning to show an answer is frame-free. Flip the frame and compare outputs instead. | G10 | [E] | c03 |
| N8 | Report the frame gap signed and per task type, never pooled. Use the 7.12% same-frame noise floor as a reference and run repeats. | G7 | [E] | K13, K18; d28, b08 |

### Test first (not yet established; see UNKNOWNS.md)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Deterministic input rewrite (canonical numbers, neutral wording) before the model sees the task. Strongest single lever found (36.81% to 6.68%). Needs an equal-token test against a warning and a reframe-and-compare arm, on ARC and BrainTeaser wording. | S1 (input hygiene) | [S] | K10, K23; a29, d28, d11, d21 |
| T2 | A code-verified, correct signal beside the task (computed expected value, tool output) as the LLM version of "credible advice". Do not use a label. | G10, S1 | [S] | K02, K16, K19; a01-a04, d23, d26, d30 |
| T3 | Reframe-and-compare: run the second framing, let code compare, escalate only on disagreement (consistent with G1: doubt on a signal). | S1, S8, G1 | [S] | K09, K14; d12, c01, d09 |
| T4 | Thinking-budget floor for framed items (0 / 1k / 4k), as the time-pressure analogue. Prior evidence points to no gain. | G11, G12 | [C] | K12; c10, d13, d14, d29 |
| T5 | Test frame gaps blind (unnamed) and named, with the persona line off; do not trust a gap measured on a named paradigm. | G4, G7 | [S] | K20; d27 |
| T6 | A distractor-context load test: does long irrelevant context before the task widen the gap? If yes, keep S1 outputs short. | G11 | [S] | K06; a15, d20, a26 |
| T7 | Restating the question in neutral words before answering (cheap one-line step). | S1 | [S] | c12, K10 |
| T8 | A model-class check: if our base model is reasoning-class, the frame gap on numeric items may already be near zero. | G7 | [S] | K22; d25 |
| T9 | Prompt language (second language). Expect a small, model-specific effect. Low priority. | none | [C] | K08; d01, d05-d08 |
| T10 | Expertise: a domain checklist (state of the situation) as the analogue of expert reading. A persona line is not allowed (G4). | S0, S2 | [S] | K07; a16, d27, d32 |
| T11 | Opposing evidence (the "both anchors" idea) for numeric anchors. | O8, S1 | [S] | c06, a09 |

## 8. Concrete tests on our bench

All tests use both arms at equal total tokens (including setup, rewrite and extra calls, per G7). Repeats: at least 3 per item, temperature fixed, option order randomised and logged. Report the signed gap with 95% CI, the same-frame noise floor, and accuracy.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | 60 sure-vs-risky pairs (Asian disease family; vary domain, magnitude, probabilities, format; DeKay style) plus 30 BrainTeaser items with complementary-fact wording (e.g. "30% fail" vs "70% pass") | (a) plain, (b) code canonicaliser, (c) warning line, (d) reframe-and-compare (two framings, code compares) | Category change rate; signed gap in points; accuracy | Canonicaliser drops change rate from about 35% to under 10% if FrameBench holds; warning a few points; reframe-compare similar to canonicaliser at 2x tokens |
| B2 | Same 60 pairs | (a) none, (b) verified-correct signal (computed expected value), (c) unverified "expert" label with a random answer, (d) verified signal plus the model's own answer kept as candidate | Gap; adoption of correct vs wrong hint; accuracy | Verified signal shrinks the gap; expert label raises adoption of a wrong hint (d23: switch odds 14x) |
| B3 | Same items | Thinking budget 0 / 1k / 4k, total tokens matched by fewer repeats at higher budget | Gap | No change (Kraishan, Payne); a drop would contradict c10 |
| B4 | Same items, blind vs named | (a) task posed as routine work, (b) named as a decision-bias experiment, each with and without a persona line | Gap per cell | Named larger than blind (d27) |
| B5 | Same items with 0 / 2k / 8k tokens of irrelevant context before the task | Context length sweep at equal total output tokens | Gap; accuracy | Gap grows if the load analogue holds (K06); not predicted by LLM evidence |
| B6 | 100 yes/no judge items (truthfulness, grammar) | (a) single polarity, (b) both polarities, code compares and flags | Inconsistency rate; accuracy on flagged vs unflagged | Disagreement flags the items with higher error |
| B7 | Same 60 pairs in English vs a second language (one close, one distant) | Matched wording, back-translation checked | Gap | Small, model-specific; null most likely (d06, d07) |
| B8 | ARC and BrainTeaser items with neutral vs loaded phrasing ("fails", "never", "trap") | (a) plain, (b) code-stripped loaded words | Accuracy; answer change | Small gain if loaded words matter (c14, a26) |
| B9 | Judge items with source labels ("expert", "student", "AI") | (a) hidden authorship, (b) labelled | Agreement shift | Labelled shifts agreement (b14, d23) |
| B10 | Any option-choice step in our loop | Original order vs shuffled order with majority over orders | Order effect and frame effect reported separately | Order bias is large on opinion items; separate it (d24) |

## 9. What does not transfer, and why

- **Emotion and emotional distance.** The foreign-language and affect accounts need an affective system. The LLM has no verified one. Even in humans the arousal measures did not predict the change (b04).
- **Real time pressure.** A one-second limit shuts down reading. An LLM has no clock; a token cap changes length, and a verbal "hurry" line changes behaviour (d16). These are different manipulations.
- **Credibility as a social judgment.** Humans decide whether a source shares their interests. An LLM treats "human expert" as a prior (d23). Do not copy Druckman's design by adding a label.
- **Stakes and incentives.** Human framing tests used hypothetical or small stakes; no LLM test used real stakes.
- **The 25% who show no effect.** Human variation comes from individuals. An LLM gives one model's deterministic lean (a23); variation comes from sampling temperature and the prompt, not from traits.
- **Individual-difference scales.** Numeracy, need for cognition and faith in intuition have no LLM counterpart; thinking-style results are inconsistent even in humans (a12).
- **Memory capacity.** Working-memory load assumes limited capacity. Context length in an LLM does not limit encoding in the same way; it may bury information, which is a different risk (d20 note).
- **Domain expertise as knowledge.** Tennis players use a model of the match. A persona line gives the LLM no model; it gives a script (d27, d32).
- **Debiasing by awareness.** Humans can be warned and sometimes correct. LLM warnings were shallow: models named the correct bias 5% of the time (d15).
- **Equivalence of the stimulus.** Many LLM "framing" tests are polarity or wording tests, where the two prompts are not logically identical (the authors argue equivalence; Wang and Zhang acknowledge wording also changes the social role, a30). Do not treat them as gain-loss framing.

## 10. Open questions

1. At equal tokens, does a deterministic input rewrite beat a warning and a reframe-and-compare step on our tasks, and what does setup cost? (K23.)
2. Does the canonicalisation result hold on non-medical, non-probability tasks such as ARC and BrainTeaser wording, and on larger models? (K10.)
3. Is there any independent human replication of Druckman 2001, and does an LLM treat a credible-source label as evidence or as deference? (d31; d23 says deference.)
4. Does a checkable signal (computed expected value) beat a label as a frame-remover for LLMs, and does it harm strong models? (d26, d30; computed EV not tested.)
5. What is the human time-pressure mechanism (attention vs non-engagement), and does a matched-budget test change the LLM gap? (Hinson vs Roberts; c10, d13, d29.)
6. How big is the gap in real two-option gain-loss pairs with stakes, against the 7.12% noise floor? (d25 has stake-free lotteries; no stakes study.)
7. Does prompt language change the LLM gap? (Only floor-effect data, d08.)
8. How much of reported LLM framing is script enactment rather than frame? (d27, one model.)
9. Does an expert persona or domain context reduce LLM framing, or is G4 the end of it? (d27 flips the sign; d32 snippet only.)
10. Is the reverse (against-human) direction a product of alignment training, and does it persist in post-2025 reasoning models? (c11, a27, d25.)
11. Does the 6.68% canonicalisation hold when the vignette is not about probabilities (attribute, goal, emphasis)? (d21 says it was not tested.)
12. Does a long irrelevant context widen the frame gap (load analogue)? (d20 note: untested.)

## 11. Sources

[V] = opened and read (in this series of evidence files). [M] = snippet, abstract or listing only.

### Human founding and moderator studies

- [V] Druckman (2001) Using credible advice to overcome framing effects, JLEO 17(1):62-82. https://faculty.wcas.northwestern.edu/jnd260/pub/Druckman%20JLawEconOrg%202001.pdf (a01-a05)
- [M] Druckman (2001) JLEO abstract page. https://academic.oup.com/jleo/article/17/1/62/2537131 (b17)
- [V] Druckman (2001) On the limits of framing effects: who can frame? J. Politics 63(4). https://faculty.wcas.northwestern.edu/jnd260/pub/Druckman%20JOP%202001.pdf (a06, a07)
- [V] Chong and Druckman (2007) Framing public opinion in competitive democracies, APSR 101(4). https://faculty.wcas.northwestern.edu/jnd260/pub/Chong%20Druckman%20APSR%202007.pdf (a08, a09)
- [V] Chong and Druckman (2007) Framing theory, Annu. Rev. Polit. Sci. 10:103-126. https://faculty.wcas.northwestern.edu/jnd260/pub/Chong%20Druckman%20Annual%20Review%202007.pdf (a10)
- [V] Kuhberger (2023) A systematic review of risky-choice framing effects, EXCLI J 22:1012-1031. https://pmc.ncbi.nlm.nih.gov/articles/PMC10620856/ (a11, a12, d19)
- [V] Roberts, Teoh and Hutcherson (2022) Time to pay attention? Psych Sci 33. https://pmc.ncbi.nlm.nih.gov/articles/PMC8985223/ (a13, b01, b02)
- [V] Gong, Wang, Ma and Lv (2026) How time pressure amplifies framing effects, Behav. Sci. 16(4):548. https://pmc.ncbi.nlm.nih.gov/articles/PMC13113354/ (a14, b03)
- [V] Hinson et al. (2019) Working memory loads and frame-induced bias, PLOS ONE. https://pmc.ncbi.nlm.nih.gov/articles/PMC6438504/ (a15, d20)
- [V] Tennis players study (2025) Frontiers in Psychology. https://pmc.ncbi.nlm.nih.gov/articles/PMC12624778/ (a16; abstract level)
- [V] Diaz-Lago et al. (2018) Thinking in a foreign language reduces the causality bias. https://pmc.ncbi.nlm.nih.gov/articles/PMC6295649/ (a17)
- [M] Keysar, Hayakawa and An (2012) The foreign-language effect, Psych Sci 23:661-668. https://doi.org/10.1177/0956797611432178 (a18, b05)
- [V] Keysar et al. 2012 as quoted in MIT 9.59J lecture 12 slides (second-hand). https://ocw.mit.edu/courses/9-59j-lab-in-psycholinguistics-spring-2017/6526aafa6c124f893a8b0795bba9a58d_MIT9_59jS17_lec12.pdf (d02)
- [V] BPS Research Digest summary of Keysar 2012. https://bps.org.uk/2012/06/we-think-more-rationally-in-foreign (d03)
- [V] Costa et al. (2014) Your morals depend on language, PLOS ONE. https://pmc.ncbi.nlm.nih.gov/articles/PMC3997430/ (a19, b21)
- [V] Stibbard-Hawkes et al. (2024) Foreign-language effects, Tanzanian Hadza, PNAS Nexus. https://pmc.ncbi.nlm.nih.gov/articles/PMC11194998/ (a20, b07)
- [V] Deliberate reasoning is not affected by language (2019) PLOS ONE. https://pmc.ncbi.nlm.nih.gov/articles/PMC6355010/ (a21)
- [V] Review (2023) Why should we study the foreign language effect, J. Intelligence 11(6):103. https://pmc.ncbi.nlm.nih.gov/articles/PMC10299445/ (a22, b04)
- [M] Hayakawa et al. (2019) Reliability of the foreign language effect on risk-taking, QJEP. https://doi.org/10.1177/1747021817742242 (b06, d05)
- [V] Dylman and Samuel (2026) L1-L2 similarity and the foreign language effect, Language and Cognition 18:e27. https://www.cambridge.org/core/product/2A01C2A415C8A104990A3F429F0FEDCB/core-reader (d01)
- [V] Wooster thesis (2015) foreign language and loss aversion (not peer reviewed). https://openworks.wooster.edu/independentstudy/6642 (d04)
- [M] Cognition and Emotion (2021) The affect of negativity. https://pubmed.ncbi.nlm.nih.gov/33622178/ (d06)
- [M] Foreign Language does not Affect Gambling-Related Judgments (2020). https://pubmed.ncbi.nlm.nih.gov/32060773/ (d07)
- [V] Zhen and Yu (2016) All framing effects are not created equal. https://www.nature.com/articles/srep30071 (b08)
- [V] Individual differences in the Unusual Disease paradigm (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10086346/ (b09)
- [V] Robinson et al. (2019) Tapped out or barely tapped? MTurk. https://pmc.ncbi.nlm.nih.gov/articles/PMC6913990/ (b10)
- [V] Trust in the source and verbal-probability framing of vaccine side effects (2023), Med. Decis. Making. https://pmc.ncbi.nlm.nih.gov/articles/PMC10625727/ (d18)
- [V] Wikipedia, Framing effect (psychology), moderators section (secondary). https://en.wikipedia.org/wiki/Framing_effect_(psychology) (b18)
- [M] Strough, Karns and Schlosnagle (2011) Decision-making across the life span. https://doi.org/10.1111/j.1749-6632.2011.06208.x (b19)
- [M] Peters et al. (2009) Numeracy and medical decisions. https://doi.org/10.1037/a0017327 (b20)
- [M] Search for independent replication of Druckman 2001. https://ideas.repec.org/a/oup/jleorg/v17y2001i1p62-82.html (d31)

### LLM and AI studies

- [V] Suri et al. (2023) Do LLMs show decision heuristics similar to humans? https://arxiv.org/pdf/2305.04400 (a23)
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3, PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC9963545/ (a24, b12)
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/pdf/2403.00811 (a25, d10, d11)
- [V] Jones and Steinhardt (2022) Capturing failures of LLMs via human cognitive biases. https://arxiv.org/pdf/2202.12299 (a26)
- [V] Payne (2025) AI decision under risk: prospect theory in LLMs. https://arxiv.org/pdf/2508.00902 (a27, d14)
- [V] Zhang et al. (2026) FrameBench-HPS. https://arxiv.org/pdf/2610.29294 (a28, a29, d21, d28)
- [V] Wang and Zhang (2026) Framing effects in independent-agent LLMs. https://arxiv.org/pdf/2603.19282 (a30, d13)
- [V] Lim, Kim and Whang (2026) DeFrame. https://arxiv.org/pdf/2602.04306 (a31, d12)
- [V] Germani and Spitale (2025) Source framing triggers systematic evaluation bias. https://arxiv.org/pdf/2505.13488 and https://pmc.ncbi.nlm.nih.gov/articles/PMC13142764/ (a32, b14)
- [V] Cheung, Maier and Lieder (2025) LLMs show amplified cognitive biases in moral decision-making, PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC12207438/ (b11)
- [V] Chen et al. (2023) The emergence of economic rationality of GPT, PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC10740389/ (b13)
- [V] Susceptibility of LLMs to user-driven factors in medical queries (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13156382/ (b15)
- [V] Take caution in using LLMs as human surrogates, PNAS (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12184514/ (b16)
- [V] Cross-linguistic patterns of cognitive biases in LLMs (2026), Front. AI. https://pmc.ncbi.nlm.nih.gov/articles/PMC13318900/ (b22; mostly abstract and intro)
- [V] Hwang et al. (2026) When wording steers the evaluation. https://arxiv.org/pdf/2601.13537 (c01-c03)
- [V] Huang et al. (2026) CogBias. https://arxiv.org/pdf/2604.01366 (c04, c05, d24)
- [V] Lou and Sun (2024) Anchoring bias in LLMs. https://arxiv.org/pdf/2412.06593 (c06, c07)
- [V] Koo et al. (2024) CoBBLeR. https://aclanthology.org/2024.findings-acl.29.pdf (c08, c09)
- [V] Kraishan (2026) The long road to the same answer. https://arxiv.org/pdf/2610.10049 (c10-c12)
- [V] Liu, Chen and Zhong (2025) Large language newsvendor. https://arxiv.org/pdf/2512.12552 (c13, c14)
- [V] Itzhak et al. (2024) Instructed to bias, TACL. https://arxiv.org/pdf/2308.00225 (c15)
- [V] Hagendorff et al. (2023) Thinking fast and slow in LLMs (abstract and opening only). https://arxiv.org/pdf/2212.05206 (c16)
- [V] Sharma et al. (2024) Towards understanding sycophancy. https://arxiv.org/pdf/2310.13548 (c17)
- [V] Botas et al. (2026) Pander Score. https://arxiv.org/pdf/2606.07897 (c18)
- [V] Kawada and Kellis (2026) Evidence integration in LLMs. https://arxiv.org/pdf/2609.04290 (c19, d26)
- [V] Lampinen et al. (2024) Language models show human-like content effects (abstract and intro only). https://arxiv.org/pdf/2207.07051 (c20)
- [M] Macmillan-Scott and Musolesi (2024) (Ir)rationality in LLMs. https://doi.org/10.1098/rsos.240255 (c21)
- [M] Nguyen (2024) Anchoring in LLMs. https://doi.org/10.1016/j.jbef.2024.100971 (c22)
- [M] Liu et al. (2026) When algorithms meet ethics. https://doi.org/10.70175/algorithmicsocietyl.2026.1.1.3 (c23)
- [V] Pantana et al. (2024) Cognitive biases in ChatGPT 3.5 and 4. https://aclanthology.org/2024.amta-research.21.pdf (d08)
- [M] BiasLab (2026) multilingual dual-framing framework (abstract). https://pubmed.ncbi.nlm.nih.gov/42434887/ (d09)
- [V] Wang and Redelmeier (2025) Forewarning AI about cognitive biases, Med. Decis. Making. https://pmc.ncbi.nlm.nih.gov/articles/PMC12413502/ (d15)
- [V] Persona prompts for simulated clinical reasoning (2026), Cureus. https://pmc.ncbi.nlm.nih.gov/articles/PMC13107492/ (d16)
- [V] Patient persona and affective framing in ChatGPT, Gemini and Claude (2026), Neurosurg. Rev. https://pmc.ncbi.nlm.nih.gov/articles/PMC13433641/ (d17)
- [M] MedMisBench (2026) preprint (abstract). https://doi.org/10.64898/2026.05.25.727671 (d22)
- [V] Bajaj and Tiganj (2026) Who do LLMs trust? https://arxiv.org/pdf/2602.13568 (d23)
- [V] Ge, Zhang and Vorobeychik (2026) Mind the (DH) gap! https://arxiv.org/pdf/2602.15173 (d25)
- [V] Bose (2026) Recognition, simulation, and refusal (PsyAgentBench). https://arxiv.org/pdf/2609.22090 (d27)
- [M] Yang et al. (2025) Is long-to-short a free lunch? (abstract and method). https://arxiv.org/pdf/2506.19492 (d29)
- [M] Zhao et al. (2025) When tools hurt LLM reasoning (abstract and intro). https://arxiv.org/pdf/2508.15754 (d30)
- [M] Wharton Prompting Science, expert personas (summary page, snippet). https://knowledge.wharton.upenn.edu/article/why-you-shouldnt-ask-chatbots-to-act-like-an-expert/ (d32)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 7 established claims: 5 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A15.03-K11** (number corrected). CogBias Table 13 (clean text extraction) gives Framing Effect 17.7% -> 24.3% (+6.6); 35.6% -> 41.4% (+5.8) is Risk Compensation; Hyperbolic Discounting is -21.0 and -13.4 is Halo Effect (the researcher read a garbled table). Echterhoff self-help 0/1.4/2.7% and few-shot failure verified. Corrected claim: Naive debiasing instructions are unreliable: a be-careful prompt helps framing only a little (CogBias, averaged over 3 models: framing-effect accuracy 17.7% to 24.3%, +6.6 points) and backfires on other biases (hyperbolic discounting -21.0 points, disposition effect -19.6, halo effect -13.4); few-shot debiasing can push models to admit-all or reject-all; self-help rewriting leaves 0-2.7% framing-biased prompts (Echterhoff et al.).
- **A15.03-K14** (reworded: the sources support less). Hwang numbers (5.69% GPT-5-mini, 66.29% LLaMA 3.2 1B, 14 judges) verified; but Germani and Spitale find the agreement drop for attribution to Chinese authors specifically, not 'a nationality' in general. Corrected claim: Wording and source cues shift LLM judgments beyond the content: 14 LLM judges vary from 5.69% (GPT-5-mini) to 66.29% (LLaMA 3.2 1B) inconsistency across logically equivalent framings of the same query, and attributing statements to Chinese authors lowered agreement across four LLMs (most for Deepseek Reasoner).
