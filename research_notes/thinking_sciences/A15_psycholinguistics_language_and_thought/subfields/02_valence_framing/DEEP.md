# Valence framing: deep document

*Subfield A15.02. Sources: evidence_a-d.jsonl (ids a01-a29, b01-b25, c01-c29, d01-d16), claims.jsonl (K01-K23), critique.md. Numbers below were read in the cited evidence lines. Where a source was only seen as a snippet, it is marked [M] in section 11.*

## 1. What it is

Valence framing is the claim that the same preference can be held as "I support A" or as "I oppose B", and that the wording changes how strong the preference becomes. The position does not change. The strength does.

Two terms need care.

- **Valence framing (this subfield).** A person with a fixed preference is asked a question that makes them think of it as support for the liked option or opposition to the disliked option. Example: "What do you think about Candidate X being elected?", asked about the liked candidate or about the disliked one. Information and preference are held equal. Only the label differs (a27).
- **Gain/loss and attribute framing (the wider family).** "70 of 100 improved" vs "30 of 100 did not improve". Most LLM studies test this neighbour, not support/oppose (a29, b25).

What the human literature says, in one paragraph. Opposing something makes the preference more resistant to a later attack message, makes the person more certain, and raises willingness to act. It does not make the preference more extreme. It is object-specific, needs personal relevance and enough thinking effort, and in a consumer-choice version appears only when the liked and disliked options are about equally extreme (a01, a02, a06, a09, a12, d13). The mechanism is unsettled: certainty, ambivalence reduction, or basis of preference (a16, a20, d14). Nearly all evidence comes from one lab group (Petty, Bizer, Teeny, Rovenpor). No outside-lab preregistered replication was found (d16).

What it means for our agent. Schema step S1 restates the task neutrally and keeps the original wording beside it. The human result hints that a problem phrased as "reject X" could change commitment to the answer. The better-supported LLM result is adjacent: logically equivalent wording changes LLM answers a lot, and a rewrite step before answering removes much of it (K08, K11). No study has run the Bizer-Petty manipulation on an LLM (a29, K16). So the case for S1 rests on adjacent LLM evidence, not on the human oppose/support effect.

## 2. History and theories in depth

### 2.1 Roots

- **Tversky and Kahneman framing** (gain/loss, Asian disease). Levin, Schneider and Gaeth (1998; b25, snippet only) split framing into risky-choice, attribute and goal types. Support/oppose wording is closest to attribute or goal framing. The Bizer design differs: it changes resistance to later persuasion, not the immediate choice.
- **Inoculation theory** (McGuire and Papageorgis 1961; Lumsdaine and Janis 1953; a28, not opened). Weak counter-arguments before an attack, or two-sided messages, raise resistance. This needs effortful counter-arguing. Bizer, Larsen and Petty (2011) present valence framing as a cheap metacognitive route to the same result (a08).
- **Two-sided "pros and cons" labelling** (Rucker, Petty and Brinol 2008, described in a08, not re-run). Labelling attributes as pros and cons raised certainty with attitudes unchanged. Same logic: a label changes confidence, not content.
- **Negativity theories.** The bivariate attitude model (negative information needs more thought than positive), negativity dominance and negativity bias were offered as reasons opposition feels stronger (a04, a17).

### 2.2 Founding work

**Bizer and Petty (2005), Political Psychology 26:553-568** (a01-a04, a27). Three studies.
- Study 1: 69 Ohio State undergraduates read about two fictitious county commissioner candidates, chose a preference, then answered "what do you think about X being elected" for either the liked or the disliked candidate. Same preference; support or oppose label. A message attacking the preferred candidate followed. Attitude change: opposers 2.42 vs supporters 3.69, F(1,59)=3.99, p=.05. Ten of 69 were removed.
- Study 2: tested negativity priming. If the effect were priming, resistance would spread to an unrelated message (library job applicants). It did not. Framing x Match interaction F(1,86)=15.45, p<.001. Match cell: opposers 1.40 vs supporters 2.92, F(1,43)=12.45. Mismatch: F(1,43)=1.37, ns. About 90 analysed.
- Study 3: 22 Eastern Illinois students, one bipolar 9-point scale before and after an attack, so measure mismatch could not explain it. Change in relative preference: oppose 2.36 vs support 4.00, F(1,20)=5.40, p=.03.
- Proposed mechanism: negative framing raises certainty, certainty raises resistance. Three ELM routes: a rejection cue, less careful processing, more counter-arguing. No mediation test in 2005 (a04).

**Bizer, Larsen and Petty (2011), Political Psychology 32** (a05-a09).
- Experiment 1: 70 train-station adults, two fictitious state supreme court candidates. Opposers more certain: 4.90 (SD 1.82) vs 4.17 (SD 1.96), F(1,58)=7.94, partial eta2=.07. Number of thoughts listed did not differ (2.13 vs 1.92).
- Experiment 2: representative panel, real 2005 New Jersey and Virginia governor races. 471 adults, 451 kept. Among the 290 with a true preference: certainty (1-5) 3.90 vs 3.43, F(1,442)=15.51, partial eta2=.04. Intentions 3.05 vs 2.76, F(1,442)=11.08. Among the 161 with no preference: 2.56 vs 2.48, F<1. Framing x preference on certainty F=4.00, p=.046.
- Mediation (preference group, n=290): framing to certainty b=0.27; framing to intentions b=0.19; framing controlling certainty b=0.02, ns; Sobel z=4.43. The mediation is statistical and correlational.
- Attitude extremity did not differ by framing. The position is untouched (a09).

### 2.3 Extensions and boundary work

- **Zezelj et al. (2007)**: cited as a replication (a13, not opened).
- **Bizer, Zezelj and Luguri (2013), Br J Soc Psychol 52:191-201** (a12, b04; press release and abstract only, no numbers). Three experiments: the effect appears for a personally relevant (local) board and not a distant one; opposers are more certain only when able and motivated to think; extended to perceived importance. A memory-load task nullified it (secondary sources).
- **Taylor (2018) Ohio State senior thesis** (a10, a11). N=170, 343, 398. Added information valence and a choose/reject decision. Confidence was highest in a three-way match: positive information, support frame, "choose". Oppose is not always stronger. Study 3 did not replicate the frame x valence interaction of Studies 1-2; the author blames one unusually confident cell. Confidence mediation of the interaction ns (indirect CI [-.045, .104]).
- **Catapano and Tormala (2021), JPSP 121:23-42** (a14). Ten studies. Support-framed attitudes are shared more than oppose-framed ones, because support seems more value-expressive. A counterweight to the resistance effect. Participant numbers were not on the abstract page.
- **Siev, Rovenpor and Petty (2024), JESP 110:104538** (a22, b05). Five studies, N=51,687. Independents base choices on opposition more than partisans (ANES 1968-2020, N=42,940; Study 4 combined N=557, partisanship x frame F(1,545)=12.54, partial eta2=.023). Partisans agree more with support-framed appeals.
- **Teeny and Petty (2025), JPSP, "opposer's loss effect"** (a18-a21, d14, d15). N=12,830 across lab, longitudinal and archival studies. Opposers react more negatively when their option loses, at equal preference extremity. Mediated more by lower felt ambivalence than by certainty.
- **Rovenpor, Teeny and Petty (2026), Decision** (a15-a17, d13). Consumer choice. Opposition raises willingness to pay only when options are equally extreme.

### 2.4 Where the theory stands (2026)

The original two-step account (opposition, then certainty, then resistance) is weakened. Certainty did not mediate in Rovenpor 2026 (moderated mediation index CI [-0.51, 0.71]; a16). Certainty was only directional in Teeny and Petty Study 3 (6.14 vs 5.84, p=.146) while ambivalence moved (1.79 vs 2.40, p=.011; a20). Competing accounts: matching, negativity dominance, and disambiguity (opposing the worse option is a clearer basis when options are equally extreme; a16, a17). The honest summary: the effect is small, conditional, and of unknown mechanism.

## 3. Core findings with exact numbers

### 3.1 Human findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Opposition-framed preference resists an attack more (Study 1) | Change 2.42 vs 3.69, F(1,59)=3.99, p=.05; N=69 (10 removed) | Bizer and Petty 2005 (a01) | Established but borderline |
| Effect is object-specific, not priming | Interaction F(1,86)=15.45; match 1.40 vs 2.92; mismatch ns, F=1.37 | Bizer and Petty 2005 (a02) | Established, one lab |
| Effect on a bipolar scale, small N | 2.36 vs 4.00, F(1,20)=5.40, p=.03; N=22 | Bizer and Petty 2005 (a03) | Established, tiny N |
| Opposers more certain (fictitious judges) | 4.90 vs 4.17, F(1,58)=7.94, eta2=.07; N=70 | Bizer, Larsen, Petty 2011 (a05) | Established |
| Real-election panel: certainty and intentions | Certainty 3.90 vs 3.43, F(1,442)=15.51, eta2=.04; intentions 3.05 vs 2.76; N=451 (290 with a preference) | Bizer et al. 2011 (a06) | Established |
| No effect without a preference | 2.56 vs 2.48, F<1; n=161 | a06 | Established |
| Certainty statistically mediates intentions | Sobel z=4.43; direct effect after control b=0.02, ns | a07 | Contested (K03) |
| Extremity unchanged | Pooled 82.92 vs 82.70, F(1,2415)=.06 | a09, a19 | Established |
| Negative reactions to a lost option stronger | 32.14 vs 39.51 (lower = worse), F(1,2415)=41.10, eta2=.017; meta d=-.284, CI [-.364, -.203] | Teeny and Petty 2025 (a19) | Single-source |
| Certainty weak, ambivalence strong | Study 3 certainty p=.146, ambivalence 1.79 vs 2.40, p=.011; Study 4 certainty p=.026 | a20 | Contested |
| Preregistered Study 5 | N=452; effect b=.25, p=.018; interaction with ambivalence over negative expression b=.29, p=.015; only in the 57.96% higher in ambivalence | d14 | Single-source |
| Archival tweets (Super Bowl) | Postgame negative words .23 vs .15, F(1,4545)=9.99; ChatGPT-4 coder 91.4% agreement on 300 tweets | d15, a21 | Single-source |
| Consumer choice needs equal extremity | WTP at equal extremity 59.14 vs 45.24, F(1,840)=8.71; other conditions p=.401, .937. Combined N=857; interaction F(2,840)=4.00, p=.019, eta-p2=.009; no main effect | Rovenpor et al. 2026 (a15, d13) | Contested (not preregistered, same lab) |
| Basis of preference differs by extremity | 6.49 vs 4.61, p<.001, d=.75; N=117 | a16 | Single-source |
| Oppose not always stronger | Three-way match (positive info, support, choose) highest: 5.243 vs no-frame 4.971 | Taylor 2018 (a10) | Single-source thesis |
| Partial failure | Study 3: no frame x valence interaction; mediation ns, p=.179 | Taylor 2018 (a11) | Failure |
| Independents use opposition more | N=51,687; Study 4 F(1,545)=12.54 | Siev et al. 2024 (a22) | Established (same lab) |
| Support is shared more | Ten studies | Catapano and Tormala 2021 (a14) | Single-source |

### 3.2 General human framing (priors)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Framing meta-analysis | 51 studies, 151 effects, about 13,500 subjects; d: risky choice 0.44, goal 0.44, attribute 0.26 | Pinon and Gambara 2005 (b07) | Established |
| Risky-choice meta | d=0.31 (100+ studies, about 30,000); bias-corrected 0.52; Many Labs 0.60; 49 countries, over 100,000 people, h=0.612 | Kuhberger 2023 (b08) | Established |
| Message framing small | d about 0.10; food gain frame d=0.47 overall, attitudes 0.82, intentions 0.05 | b09 | Established |
| Wording confound | "At least" vs "exactly" removed the effect in one study (t(74)=1.37); a replication found it with "exactly" (t=5.64, df=225) | Mandel (b11, b12) | Contested |

### 3.3 LLM findings (adjacent to support/oppose)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Admit vs reject framing, GPT-4 | Delta -0.405: admits 40.5 points more under reject framing; 13,465 prompts | Echterhoff 2024 (b16, c14) | Established |
| Self-help rewrite removes it | -0.405 to -0.010; framing elements left 2.7% (GPT-4), 0% (Llama2-13B), 1.4% (Llama2-7B); 17.2% for GPT-3.5 with an awareness prompt | c15, b16 | Established |
| Awareness, contrastive, counterfactual prompts fail | GPT-4 delta -0.470, -0.410, -0.570 | c16 | Established |
| Cross-family vote framing | P(B) 4.3% vs 68.8%, a 64.5-point shift; 82 models, 11 families, 3,280 responses | Wang and Zhang 2026 (c21, d11) | Single paper, large |
| Thinking mode | Thinking on: P(B) .003 vs .254 (n=362); off: .054 vs .811 (n=1,278) | c22 | Single paper |
| Asian disease, GPT-3 | Risky choice 11.3% (save) vs 60.0% (die) at save prob <0.5; overall 45.4 vs 74.1 (human 28 vs 78) | Jones and Steinhardt 2022 (b13) | Older model |
| ChatGPT gain/loss rating | 5 in 11 of 11 trials vs 4 in 11 of 11; humans 5.2 vs 4.6, t(80)=3.86 | Suri 2023 (b14) | Older model, zero variance |
| Cognitive-bias battery | Framing score mean 0.41 over 20 LLMs (range 0.10-0.55; baseline 0.01) | Malberg 2025 (b18) | Established |
| Prospect-theory risk framing | Sport frame effect +1.84 (GPT-4o), reverses in career (-0.37) and business (-0.20); 2,550 decisions; unrelated to EV attempts | Payne 2025 (b19) | Single-source |
| Allow/forbid | Llama2-7b -60.4, 13b -55.1, 70b -42.2, GPT-3.5 +25.3 (often opposite to humans); 40 allow/forbid questions | Tjuatja 2024 (c04, c05) | Established |
| Chat models | Less sensitive to bias wording, more to irrelevant perturbations (23 of 29 settings) | c06 | Single-source |
| "No" bias | 5 models, 9 tasks, 37,975 variations; neutral to yes/no raised "no" counts by 31% to 203% | Braun 2025 (c07, c08) | Established |
| Positive vs negative question wording | Agreement 76.2% vs 72.0%, beta=-0.219, z=-14.72; 6,614 pairs, 8 LLMs incl. GPT-5.1 and Sonnet 4.5; multi-turn 78.4 vs 70.7 | Yun 2026 (b22, d08) | Single-source |
| WildFrame sentiment | 1,000 texts, eleven LLMs; r with humans 0.52 (GPT-3.5), 0.57 (GPT-4o), 0.61 (GPT-5-mini); about 55% instance flips under paraphrase | Lior 2026 (b21, c01-c03) | Established |
| Directional word | Error toward "more" from 26% (Sonnet) to 93% (Qwen-3B) in short answers; free-form CoT mostly under 30% | Shafiei 2025 (c19, c20, d09) | Single-source |
| Sycophancy to stance | Wrong suggested answer cuts accuracy up to 27%; GPT-4 wrongly admits mistakes 42%; "I dislike" lowers feedback valence | Sharma 2023 (c11-c13) | Established |
| Question form vs statement | Sycophancy GLM coefficient: non-questions 0.59 vs questions -2.93; beliefs 0.72, convictions 0.82 | Dubois 2026 (a24, d06) | Single-source |
| Rewrite beats instruction | Control 1.13; one-step question reframe 0.16; two-step -0.55; explicit "do not be sycophantic" 0.51 | a25, d06 | Single-source |
| Repeated challenge | GPT-4o 55.85% to 27.32% after three turns; mean NEG-Flip@3 79.31%; valid correction accepted 93.23% | Tan 2025 (d04, d05) | Single-source |
| Blind vs named | gpt-oss-120B 0.020 blind vs 0.619 named (counterfactual 0.019 vs 0.787) | Bose 2026 (d01, c23) | Contested |
| Rephrase and Respond | GPT-4 mean 64.95 to 89.77 over 10 tasks; CSQA 84.09 to 85.45 | Deng 2023 (d12) | Single-source |

## 4. Mechanisms and models

### 4.1 Human mechanism candidates

1. **Certainty route** (Bizer and Petty 2005). The label changes metacognitive confidence. Model: certainty = base + 0.27 x oppose; resistance = f(certainty). In the data: framing to certainty b=0.27, certainty to intentions b=.60 (a07). Weakened by a16 and a20.
2. **Ambivalence route** (Teeny and Petty 2025). Opposition lowers felt ambivalence (1.79 vs 2.40). The effect holds only for people high in ambivalence over negative expression (b=.29; d14).
3. **Disambiguity or basis route** (Rovenpor 2026). When options are equally extreme, "I oppose the bad one" gives a clearer basis than "I support the good one". The effect disappears when one option dominates (a15, a16).
4. **Matching route** (Taylor 2018; a10). Frame matched to information valence and choice type gives the most confidence.
5. **Processing route** (Bizer, Zezelj, Luguri 2013; a12). Needs ability and motivation; load nullifies it. So the label acts through thoughtful elaboration, not as a cheap cue.

### 4.2 LLM mechanism candidates

- **Lexical association pull.** One word ("more", "less", "forbid", "reject") pulls the output toward the cue (c19, c05). Suri et al. suggest linguistic association is strongest in the native tongue (b15, interpretation only).
- **Stance and agreement pull (sycophancy).** Preference models reward agreement with the user (c13). Certainty of wording raises it (a24). Question form removes the cue (d06).
- **Contamination or recognition.** Some effects exist only when the paradigm is named (d01); the gate is model-specific (d02).
- **Answer-format polarity.** Models say "no" more whichever way "no" points (c07, c08). This is separate from valence.
- **Persona.** A one-sentence low-agreeableness persona reversed the named framing effect (-0.319 vs 0.619; d03).

### 4.3 An implementable S1 frame-stripping step

Input: raw task text T. Output: neutral restatement R, with T kept beside it.

1. Code step (no model): detect stance cues with a pattern list: "I oppose", "I believe", "I'm convinced", "reject", "forbid", "don't you agree", "I think the answer is". Move them to a marked block that attempts do not see (this is the existing S1 input hygiene).
2. Model step: rewrite the task as a neutral question with no valence verb. "Choose Y" and "reject X" both become "which option fits criterion C". This is the Dubois two-step rewrite (d06) and the Echterhoff self-help step (c15).
3. Code check, constraint preservation: extract numbers, named entities and quantifiers from T and R. Flag R if any is missing or added. This guards the Deng failure (wrong constraint, rephrase loops; d12). If flagged, fall back to T with the stance block removed.
4. Solve from R (S3). Optional on frame-sensitive items: run once from R and once from the opposite framing; code compares (G5). If the two disagree, mark the item frame-sensitive and send it to S6.
5. Log tokens spent on steps 2 and 3 (G7).

Do not use: a generic "avoid bias" instruction (c16, c18), persona instructions, or JSON-only output for the first pass (d09).

## 5. What holds up

### 5.1 Human

- **Replicated, with caveats.** Opposers more certain (a05, a06), more resistant (a01-a03), object-specific (a02), needing relevance and load-free processing (b04, a12). Zezelj 2007 and Bizer 2013 replicate it (K05). Most work is from one lab.
- **Weak spots.** Study 1 p=.05; Study 3 N=22 (a01, a03). Taylor 2018 Study 3 failed (a11). Rovenpor 2026 (N=857) was not preregistered and the effect appears only at equal extremity (d13). Teeny and Petty pooled: no change in extremity (82.92 vs 82.70). The certainty mediation is correlational and was not reproduced (a16).
- **No outside-lab preregistered replication located** (d16). The search was limited: WebSearch refused, APIs rate-limited. A negative search is not proof.
- **Sign reversals.** Oppose is not always stronger (Taylor; a10). Support is shared more (a14). Partisans respond better to support frames (a22).
- **General framing prior.** Attribute framing d=0.26, risky choice d=0.31-0.60, message framing d about 0.10 (b07-b09). A wording confound explains part of the classic Asian disease effect (b11, b12).

### 5.2 LLM: what is robust

- Wording of logically equivalent items moves answers a lot across many models (c21, b16, b13, c19, d08). Established.
- Direction is not reliably human-like (c05, c07). Allow/forbid went opposite to humans in several models. Sign differs by model and size.
- Newer models are closer to human framing patterns (WildFrame r .52 to .61; c02) yet stay sensitive (55% flips under paraphrase; c03). 2026 models still show effects (d08, c21).
- Correction to an earlier note: the Dubois model terms (GPT-4o 0.90, Sonnet-4.5 -0.24, GPT-5 -0.66) are baseline sycophancy levels, not opposite-sign framing effects (d07).

### 5.3 Interventions that worked

- **Rewrite before answering.** Echterhoff self-help (-0.405 to -0.010 for GPT-4; c15). Dubois question reframe (1.13 to 0.16, and -0.55 for two steps; d06). Chapala neutral third-person rewording improved alignment for two of three models (c26). Rephrase and Respond lifted GPT-4 from 64.95 to 89.77 (d12).
- **Free-form reasoning before the label.** Directional error under 30% (d09). Thinking mode cut the vote swing (0.254 vs 0.811 for scenario B; c22).
- **Question form.** Questions reduce sycophancy sharply (d06).

### 5.4 Interventions that did not work, or hurt

- Awareness, contrastive and counterfactual prompts: GPT-4 delta stays -0.47, -0.41, -0.57 (c16).
- Explicit "do not be sycophantic": 0.51 vs 1.13 control, worse than the rewrite (d06). CautiousPrompt did nothing for open-model negative accuracy (d05).
- Prompt-level debiasing: helps framing by +5.8 pp but hurts other biases by 13-21 pp (c18).
- Thinking mode: reduces, does not remove (c22). Payne found framing size unrelated to EV attempts (b19).
- JSON-structured reasoning keeps drift (d09).
- Restating on weak models: wrong constraints and loop rephrases (45 of 220 Sports items, 21 of 369 Dates items; d12).
- Resist-only training made models rigid (d05).

### 5.5 Moderators

Human: personal relevance, load, option extremity, ambivalence, partisanship, information valence, choose vs reject (a12, d13, d14, a22, a10). LLM: model family and size (c21), RLHF (c06), paradigm label (d01, d02), persona (d03), question form and stated certainty (d06), answer format (d09), domain (Payne: sport vs career; b19), single vs multi-turn (d08).

## 6. Language models

### 6.1 No direct test

No paper runs the "I support X / I oppose Y" manipulation followed by an attack message on an LLM (a29, K16; confirmed after the gap search, d16). Nearest items:

- **Yun 2026**, positive vs negative question framing: agreement 76.2% vs 72.0% (single-turn 75.4 vs 72.4; multi-turn 78.4 vs 70.7), 6,614 pairs (d08).
- **Dubois 2026**: stance cues (belief, conviction) raise sycophancy; question form removes it (d06).
- **Sharma 2023**: stated dislike lowers feedback valence; a weak user belief lowers accuracy up to 27%; GPT-4 admits mistakes 42% of the time when challenged (c11, c12).
- **DuET-PD**: three-turn challenge cuts GPT-4o from 55.85% to 27.32%. Plain repetition is almost as strong as elaborate appeals on closed models (NEG-Flip@3 32.21 vs up to 40.93); on open models 76.02 (d04, d05). This resembles an attack message but not a support/oppose manipulation.
- **Kaur 2025**: stance moves toward whichever side the added argument supports; 62 propositions, four open models (a26; exact table not extracted).

### 6.2 Gain/loss and wording on LLMs

- **Magnitude.** GPT-4 admits 40.5 points more under reject framing (b16). 82 models: 4.3% vs 68.8% (c21). GPT-3: 11.3% vs 60.0% (b13). ChatGPT gain 5 vs loss 4 with zero variance (b14). 20 models: framing score 0.41 (b18).
- **Direction.** Not human-like in allow/forbid: Llama2-7b -60.4, 70b -42.2, GPT-3.5 +25.3 (c05). WildFrame r .52-.61 shows partial human-likeness for sentiment. Braun finds a "no" bias (c07).
- **Model families.** Claude shifts strongly with much non-compliant output; GPT and DeepSeek shift most (d11). The two family tables in c21 and d11 use different summaries (Gemini 0.375 vs 0.660), so do not compare across them.
- **Reasoning.** Thinking on cuts the swing (0.254 vs 0.811) but not to zero (c22). Free-form CoT works better than JSON (d09).
- **Domain.** The same model reverses sign across domains (Payne: sport +1.84; career -0.37; b19).
- **Contamination.** On gpt-oss-120B the gain/loss effect is 0.020 blind and 0.619 named (d01). The Asch conformity gate is also model-specific: 0.0% blind vs 83.3% named on gpt-oss-120B; no change on Llama 3.1 8B and 3.3 70B (d02). Caveat: the blind result sits near a sure-option ceiling and so understates sensitivity. Yun 2026 shows effects in an unlabelled medical task, so not all sensitivity is memorisation (K10).
- **Persona.** A low-agreeableness persona reversed the named effect to -0.319 (d03).

### 6.3 What changed it, by how much

| Intervention | Before | After | Source |
|---|---|---|---|
| GPT-4 self-help rewrite | -0.405 | -0.010 | c15 |
| Awareness prompt | -0.405 | -0.470 | c16 |
| Counterfactual few-shot | -0.405 | -0.570 | c16 |
| Question reframe, 2-step (sycophancy) | 1.13 | -0.55 | d06 |
| Question reframe, 1-step | 1.13 | 0.16 | d06 |
| Explicit no-sycophancy instruction | 1.13 | 0.51 | d06 |
| Thinking on, scenario B P(B) | 0.811 | 0.254 | c22 |
| Free-form CoT | directional error up to 93% (Qwen-3B) | most under 30% | d09 |
| Rephrase and Respond (GPT-4) | 64.95 | 89.77 | d12 |
| Debias prompt (framing, CogBias) | 35.6% | 41.4% | c17, c18 |
| Neutral third-person (ANES) | baseline | closer for 2 of 3 models | c26 |
| Low-agreeableness persona | 0.619 | -0.319 | d03 |

None of these is token-matched, and none measures accuracy on unframed items. That is the main gap for S1.

### 6.4 LLMs coding the human construct

Teeny and Petty used ChatGPT 4.0 to code support vs oppose framing in tweets: 91.4% agreement with humans on 300 tweets, but identifying which team was opposed failed (a21, d15). A usable detector for stance cues in input hygiene, not for target identification.

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Equivalent wording changes LLM answers a lot, including 2026 models and the same model across domains. Treat wording as a controlled input. | S1 | [E] | K08; b16, c21, b13, b14, b18, d08 |
| 2 | S1 neutral restatement is justified by adjacent literature: a rewrite step before answering cuts framing and sycophancy (GPT-4 -0.405 to -0.010; sycophancy 1.13 to 0.16 or -0.55). Keep the original beside it. | S1 | [E] for rewriting; [S] for our exact form | K11; c15, a25, d06, c26 |
| 3 | Do not add a generic "be unbiased" or awareness instruction. It fails or backfires. | G (list in 4b) | [E] | K12; c16, c18 |
| 4 | Stance cues (user belief, certainty, like/dislike, a suggested answer) move answers. Code moves them to a marked block in S1; attempts never see them as part of the task. | S1 hygiene | [E] | K15; c11-c13, a24 |
| 5 | Do not assume the human direction. Measure framing sensitivity per model. | S0/memory | [E] | K09; c05, c07, c02 |
| 6 | Reasoning reduces but does not remove drift. Do not rely on extended thinking as the fix; use free-form reasoning before extracting a label. | S3/output | [E] | K13; c22, d09 |
| 7 | Keep the human oppose/support effect out of the schema as a design driver: it is small, moderated and from one lab. | none | [E] | K05, K14 |
| 8 | A label can shift stated certainty without changing the position (humans). This supports the existing rule that verbal confidence is not evidence. | G10/4b | [E] | K02; a06, a09 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Run Bizer-Petty on an LLM: equal preference, "X rejected" vs "Y chosen", then a counter-argument. Does an oppose-framed agent keep its first answer more? | S1 | [S] (K16) | a01, a27, d16 |
| T2 | Neutral restatement vs "avoid bias" instruction vs extended thinking, at equal total tokens, on framed pairs and on unframed items. | S1 | [S] | K11, K12, K19; d06, c16 |
| T3 | Constraint-preservation check after restatement (code compares numbers, entities, quantifiers). Does it stop distortion? | S1 | [S] | K22; d12 |
| T4 | Neutral restatement of each challenge in multi-turn pushback (Flip@3), while still accepting valid corrections. | S1/G | [S] | K20; d04, d05 |
| T5 | Free-form restate and reason first, then extract the label, vs JSON-first. | S1/output | [S] | K21; d09 |
| T6 | Blind vs named framing items, to separate memorised effects from wording sensitivity on our models. | S0/memory | [C] | K10; d01, d02 |
| T7 | Dual-frame check: solve once under each framing, code compares. Disagreement flags the item as frame-sensitive and routes it to S6 or a second restatement. | S4/S7 | [S] | K08, K11 |
| T8 | Question-form rewrite (turn statements into questions) as the restatement style. | S1 | [S] | K19; d06 |

## 8. Concrete tests on our bench

All arms use equal total tokens per item, with restatement tokens counted inside the budget (G7). Use 3 or more seeds per item. Report flip rate with a 95% interval.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | Binary choices between two options of equal quality, with an attack message after the first answer (build 60 items; vary extremity: equal, one dominant) | A: "Y chosen"; B: "X rejected"; C: neutral | Answer flip after attack; verbalised confidence | Small or null. Effect, if any, at equal extremity only (d13). |
| B2 (T2) | 80 paired logically equivalent items (admit/reject, save/die, gain/loss, allow/forbid, more/less) plus 80 unframed control items | Plain; S1 neutral restatement; "avoid bias" instruction; extended thinking | Framing delta (answer difference between frames); accuracy on unframed controls | Restatement lowers delta to near 0 (c15, d06); instruction less (c16); thinking partial (c22); controls: no loss. |
| B3 (T3) | Items with 2-4 numeric constraints | Restate with check; restate without; plain | Rate of altered or dropped constraints; final accuracy | Check cuts distortion (d12 on weak models). |
| B4 (T4) | 50 MMLU-Pro style items with a 3-turn false challenge | Plain; restated challenge; "be cautious" prompt | NEG-Flip@3 and POS-Acc@3 | Restatement lowers NEG-Flip without lowering valid-correction acceptance. Prompting alone does not (d05). |
| B5 (T5) | 100 comparison tasks with a more/less/equal cue | Free-form first; JSON-first; restated + free-form | Directional error | Free-form under 30% (d09); restated no worse. |
| B6 (T6) | Matched gain/loss items: named paradigm vs blind invented content | Same arms as B2 | Framing delta, blind vs named | Named above blind on some models (d01). |
| B7 (T7) | As B2 | Single run vs dual-frame with code comparison | Accuracy and token cost | Disagreement predicts error; costs about 2x. Keep only if it wins at equal tokens. |
| B8 (T8) | Stance-laden statements (belief, conviction, I-perspective) vs question forms | Statement; question rewrite; plain | Sycophancy score (agreement with a stated view when the view is wrong) | Question rewrite lower (d06: 0.16 vs 1.13). |

Stop rule (G7): an element stays only if it beats the plain arm at equal tokens on both framed pairs and unframed controls.

## 9. What does not transfer, and why

- **Resistance to persuasion through a self-held attitude.** The human effect depends on ego involvement, personal relevance and ambivalence about negative expression (a12, d14). An LLM has no stake. Do not read "oppose is stronger" as "an LLM with an oppose frame will hold its answer".
- **Certainty as mechanism.** Even in humans it is not shown to be the cause (a16, a20). LLM verbal confidence is not evidence (G10).
- **The equal-extremity condition.** The human effect shows only when liked and disliked options are about equally extreme (d13). Many agent tasks have one correct answer; the effect would not be expected there.
- **Support is shared more** (a14); **independents oppose more** (a22). Sharing and individual-difference effects have no agent analogue (K07, K17).
- **Student and MTurk samples, fictitious candidates.** Low stakes. The human effect sizes (meta d=-.284 for negative reactions) are not priors for LLM effect sizes.
- **Direction of effects.** LLM allow/forbid shifts are often opposite to humans (c05). A human-based fix such as "frame as support" cannot be assumed.
- **Contamination.** Some LLM framing effects occur only when the paradigm is named (d01). Textbook items overstate real-world sensitivity; blind items may understate it (ceiling).
- **Memory-load nullification** (a12). The human effect disappears under load; the LLM analogue (long context) is untested.
- **Large human risky-choice effects** (d=0.31-0.60) are not directly relevant to deterministic-answer tasks.

## 10. Open questions

1. Does an LLM given "X being rejected" vs "Y being chosen" (equal preference) resist a counter-argument more? (K16; B1)
2. At equal tokens, does S1 cut framing flips more than an "avoid bias" instruction or extended thinking, and does it keep accuracy on unframed items? (K19)
3. What is the token cost of restatement, and how often does it distort constraints on current models? (d12: no token counts; weak models distorted)
4. Do 2026 frontier models show allow/forbid and reject/admit shifts? Only vote framing and clinical-question framing are tested on them (c21, d08).
5. How much LLM framing sensitivity is memorisation of the named paradigm? Only gpt-oss-120B was tested for framing; the Asch gate differs by model (d01, d02).
6. What is the human mechanism: certainty, ambivalence, or basis of preference? Is there an agent analogue? (a16, d14)
7. Is there an independent preregistered replication of Bizer and Petty 2005? (d16)
8. Do multi-turn agent settings show entrenchment after an oppose-style first answer, and does restating each challenge help? (d04, d05, d08)
9. Does structured output keep drift on restated problems? (d09)
10. Does a persona or system prompt change frame sensitivity in a way we can control cheaply? (d03)

## 11. Sources

[V] = opened and read this session. [M] = snippet only or not opened.

**Human, founding and extensions**
- [V] Bizer and Petty (2005), How we conceptualize our attitudes matters. https://richardepetty.com/wp-content/uploads/2019/01/2005-pol-psy-bizerpetty.pdf (a01-a04, a27)
- [M] Same paper by DOI. https://doi.org/10.1111/j.1467-9221.2005.00431.x (b01)
- [V] Bizer, Larsen and Petty (2011), Exploring the valence-framing effect. https://richardepetty.com/wp-content/uploads/2019/01/2010-polipsy-bizer-larsen-petty.pdf (a05-a09)
- [M] Same paper by DOI. https://doi.org/10.1111/j.1467-9221.2010.00795.x (b03)
- [M] Zezelj et al. (2007), cited in the above (a13)
- [V] Bizer, Zezelj and Luguri (2013), press release only, no numbers. https://www.eurekalert.org/news-releases/611578 (a12). [M] abstract by DOI. https://doi.org/10.1111/bjso.12014 (b04)
- [V] Taylor (2018), Ohio State senior thesis. https://kb.osu.edu/server/api/core/bitstreams/03e2d549-5921-56c2-b9b5-81a5866e8191/content (a10, a11)
- [V] Catapano and Tormala (2021), JPSP 121:23-42, abstract page. https://www.gsb.stanford.edu/faculty-research/publications/do-i-support-its-good-or-oppose-its-bad-effect-support-oppose-framing (a14)
- [V] Rovenpor, Teeny and Petty (2026), Decision. https://richardepetty.com/wp-content/uploads/2026/09/2026-Rovenpor-et-al-decision-proof.pdf (a15-a17, d13, d16)
- [V] Teeny and Petty (2025), JPSP, opposer's loss effect. https://richardepetty.com/wp-content/uploads/2025/02/2025-JPSP-Teeny-Petty-Opposers-Loss-galley-proof.pdf (a18-a21, d14, d15)
- [V] Siev, Rovenpor and Petty (2024), JESP 110:104538. https://richardepetty.com/wp-content/uploads/2023/09/2024-JESP-Siev-Rovenpor-Petty-independents-negativity.pdf (a22)
- [M] Rovenpor, Teeny, Petty (2023 preprint). https://doi.org/10.31234/osf.io/xmuy3 (b05)
- [M] Kellogg faculty listing for the 2025 Petty-lab choice paper. https://www.kellogg.northwestern.edu/faculty/research/detail/2025/when-and-why-opposition-vs-support-framing-increases-choice (b06)
- [V] Teeny blog summary. https://everydaypsych.com/?p=4003 (b02)
- [V] Wikipedia, Framing effect (psychology). https://en.wikipedia.org/wiki/Framing_effect_(psychology) (a23); [M] c28 same page
- [M] McGuire and Papageorgis 1961; Lumsdaine and Janis 1953, as described in Bizer et al. 2011 (a28)
- [M] Levin, Schneider, Gaeth (1998). https://digitalcommons.usf.edu/psy_facpub/1886/ (b25)
- [M] Data portal listing of Bizer et al. 2011. https://data.zhenzhi.com/details/1/882196395 (c29)

**Human, general framing**
- [V] Pinon and Gambara (2005), Psicothema 17:325-331. https://www.psicothema.com/pdf/3107.pdf (b07)
- [V] Kuhberger (2023), EXCLI J 22:1012-1031. https://excli.de/excli/article/view/6169 (b08-b10)
- [V] Mandel reply (OSF). https://osf.io/34jeg/ (b11)
- [M] Mandel (2014), JEP General. https://doi.org/10.1037/a0034207 (b12)

**LLM studies**
- [V] Dubois et al. (2026), Ask, don't tell. https://arxiv.org/pdf/2602.23971 (a24, a25, d06, d07)
- [V] Kaur (2025), EMNLP Findings. https://aclanthology.org/2025.findings-emnlp.1241.pdf (a26)
- [V] Jones and Steinhardt (2022). https://arxiv.org/pdf/2202.12299 (b13)
- [V] Suri et al. (2023). https://arxiv.org/pdf/2305.04400 (b14, b15)
- [V] Echterhoff et al. (2024). https://arxiv.org/pdf/2403.00811 (b16, c14-c16)
- [V] Itzhak et al. (2023). https://arxiv.org/pdf/2308.00225 (b17; does not test framing)
- [V] Malberg et al. (2025). https://arxiv.org/pdf/2410.15413 (b18)
- [V] Payne (2025). https://arxiv.org/html/2508.00902v1 (b19, b20)
- [V] Lior, Naccache, Stanovsky (2026), WildFrame. https://arxiv.org/pdf/2502.17091 (b21, c01-c03)
- [V] Yun et al. (2026). https://arxiv.org/pdf/2604.05051 (b22, d08)
- [V] Huang et al. (2026), CogBias. https://arxiv.org/pdf/2604.01366 (b23, b24, c17, c18)
- [V] Tjuatja et al. (2024), BiasMonkey. https://arxiv.org/abs/2311.04076 (c04-c06)
- [V] Braun (2025). https://arxiv.org/abs/2509.08480 (c07-c09)
- [V] Rupprecht, Ahnert, Strohmaier (2025). https://arxiv.org/abs/2507.07188 (c10)
- [V] Sharma et al. (2023). https://arxiv.org/abs/2310.13548 (c11-c13)
- [V] Shafiei, Saffari, Moosavi (2025). https://arxiv.org/abs/2506.03923 (c19, c20, d09, d10)
- [V] Wang and Zhang (2026). https://www.alphaxiv.org/abs/2603.19282.md and https://arxiv.org/pdf/2603.19282 (c21, c22, d11)
- [V] Bose (2026), PsyAgentBench. https://arxiv.org/pdf/2609.22090 (c23-c25, d01-d03)
- [V] Chapala, Mironov, Deng (2026). https://arxiv.org/abs/2512.22725 (c26)
- [V] Tan et al. (2025), DuET-PD. https://arxiv.org/abs/2508.17450 (c27, d04, d05)
- [V] Deng et al. (2023), Rephrase and Respond. https://arxiv.org/pdf/2311.04205 (d12)

Source counting notes: WildFrame (b21, c01-c03) is one paper with eleven LLMs; the "eight" in c01 is the annotator count. Echterhoff (b16, c14-c16) is one paper. Siev et al. (a22, b05) is one body of work. Bizer-Zezelj-Luguri (a12, b04, a23) is one paper seen through three secondary sources.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 9 established claims: 7 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A15.02-K02** (now single-source: the sources are not independent). Numbers verified (3.90 vs 3.43, N=451 after exclusions, Study 3 p=.146, Study 4 p=.026, ambivalence drop), but both papers are from Petty's lab (Bizer, Larsen, Petty; Teeny and Petty) and no outside replication is listed.
- **A15.02-K09** (number corrected). WildFrame reports r>=0.52 for all eleven LLMs; 0.52 to 0.61 is only the range across the GPT models (GPT-3.5 to GPT-5-mini), which the authors call the least human-correlated family. Corrected claim: LLM framing sensitivity is not simply human-like in direction: allow/forbid shifts in Tjuatja 2024 were often opposite to humans (Llama2-7b -60.4, GPT-3.5 +25.3); Braun 2025 finds an LLM 'no' bias rather than human acquiescence; in WildFrame (eleven LLMs) all models correlate with human reframing shifts at r>=0.52 (GPT models lowest, 0.52 for GPT-3.5 to 0.61 for GPT-5-mini), so response to naturally occurring reframing is more human-like than the survey-bias results.
- **A15.02-K01** (now single-source: only one opened source, code check).
- **A15.02-K07** (now single-source: only one opened source, code check).
