# Naturalistic decision making: deep document

*Subfield E13.06. Experts under pressure; recognition-primed decision (RPD). Written from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01 to d15) refer to those files. Claim ids (K01 to K19) refer to claims.jsonl. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested.*

Honesty note up front. Only two number groups were re-checked first-hand in the critique pass (Liu et al. on chain of thought; Kahneman and Klein 2009). The rest is carried from earlier agents. The founding 1986 study was never opened, so its counts are unverified. The only direct LLM test of RPD is one team, one domain, accuracy only.

## 1. What it is

Naturalistic decision making (NDM) studies how experienced people decide in real settings. The settings have time pressure, uncertainty, high stakes, shifting goals, and unclear information. Examples are fireground commanders, naval combat officers, nurses, military leaders, sport players, and police. The field began as a workshop in 1989 of about 30 researchers (a03, a09). Its book is Klein, Orasanu, Calderwood and Zsambok (1993). A technical group formed in 1995 and there were 12 NDM conferences by 2016 (a09).

NDM defines itself by setting, not by one mechanism. Lipshitz (1993) listed several field models: RPD, the cognitive continuum (Hammond), image theory (Beach), dominance search (Montgomery), and Rasmussen's skills-rules-knowledge and decision ladder (a03).

The core claim of the best-known model, RPD (Klein, Calderwood and Clinton-Cirocco 1986): experts rarely compare options. They recognise the situation as a type, bring one plausible action to mind, mentally simulate it, and act if it works. If the simulation shows flaws, they modify it. If it still fails, they take the next most plausible option (a01, a02). This is a serial generate-and-test loop with a recognition front end.

Why it matters for our agent: it is a theory of mode choice (when to act on a fast first candidate, when to deliberate) and of generate-test (one candidate at a time, simulate, move on only on failure). Both map to the S0 gate and the S3/S4 loop of SCHEMA.md.

## 2. History and theories in depth

**1986: the founding study.** Klein, Calderwood and Clinton-Cirocco studied fireground commanders (Human Factors Society proceedings 30(6), 576-580). The starting hypothesis was that commanders compare a pair of options. It was wrong. They usually generated one option and needed no more (a01). Secondary sources give 80 to 90 percent of decisions as RPD (a09, b20, d12). A search summary says 26 commanders, average 23 years of experience, 156 decision points (a27), but this was not opened. DTIC file ADA199492 was damaged and the citation page returned 403 (d12). Treat all counts as unverified. The design has no comparison group and uses retrospective interviews.

**1989 to 1993: the movement.** The Dayton workshop, then the book (a03, b22). The Vincennes incident (an AEGIS cruiser shot down an Iranian airliner) helped drive Navy interest (a09).

**Three RPD levels** (a24):
1. Simple match: the situation is familiar. Cues, goals, expectancies and action are all known.
2. Diagnosis: cues are unclear, or an expectancy is violated. The expert builds a story by simulation.
3. Evaluate an action: the expert simulates the action to see if it will work.
Recognition yields four by-products: expectancies, relevant cues, plausible goals, an action list.

**Other Klein tools.** Premortem (2007): imagine the plan has failed, write reasons for two minutes, take reasons round the table starting with the leader. It rests on prospective hindsight (Mitchell, Russo, Pennington 1989). No outcome data were given in the opened source (a08). Data-frame theory of sensemaking: a frame shapes which cues are seen; experts question, elaborate and reframe (c02, c14). Critical Decision Method: a structured interview used to elicit cues and decision points (a20 used it on coaches).

**2001: the rigour critique.** Lipshitz, Klein, Orasanu and Salas, "Taking stock of NDM", drew 16 commentaries. Lab researchers said NDM lacked controlled methods and tests of correctness. NDM authors answered "guilty as charged" on lack of correct answers and hypothesis tests, and argued control removes the object of study (a10, b21). Macrocognition split from microcognition around 2000 and NDM broadened to macrocognition about 2003 (a10).

**2009: the truce.** Kahneman and Klein, "Conditions for intuitive expertise: a failure to disagree". Both camps agree intuition is skilled only if (1) the environment has valid, learnable cues and (2) the person had enough practice with feedback. Confidence is not a reliable sign of accuracy (a04, b19). They map RPD onto dual process: automatic recall of candidates (System 1) plus deliberate simulation (System 2) that can override (a07). One review calls the dual-process labels the same ideas under new names (the "jangle fallacy", b27, abstract only).

**Competing tradition.** Meehl (1954): statistical rules beat clinicians in nearly all studies. Goldberg (1970): bootstrap models of 29 clinicians on 861 MMPI profiles (11 scales) were almost always more accurate than the clinicians. Karelaia and Hogarth (2008) meta-analysis ties this to inconsistency, which is noise (a06). Shanteau (1992) listed domains with real expertise (livestock judges, weather forecasters, test pilots, chess masters, physicists, grain inspectors) and without (stockbrokers, clinical psychologists, personnel selectors). Predictors: outcome predictability, experience, feedback quality, static versus dynamic stimuli (a05).

**Rival theories to RPD.**
- Take-the-first (Johnson and Raab 2003): the first generated option tends to be best, and more options make the final choice worse (b10).
- Long-term working memory (Ericsson and Kintsch 1995): experts do not hold fewer options, they hold better organised, more task-relevant ones. Discriminating prediction: relevant options help, irrelevant options hurt (b28).
- Information processing and ecological dynamics accounts in sport (a21).

**Computational RPD.** Norling (BDI-RPD), Nowroozi (C-RPD in UML), Fan et al. (R-CAST), Hu (Bayesian-network pilot model), Sokolowski (military), and Danial et al. 2019 (Markov logic network plus ontology inside a BDI agent, trained on 17 participants) (a23, c12). Danial et al. say Klein's model is qualitative and does not specify how decisions or plans are made.

**Domain applications.** Surgery has four modes: intuitive, rule-based, option comparison, creative (a15). Clinical reasoning: typical cases get pattern recognition, atypical cases get extra cues and hypothesis testing, new cases get simulation (a22). Code review: 27 percent orientation questions then 73 percent analysis, read by the authors as RPD (a25, c24).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Commanders usually generate one option, not a pair | 80-90 percent RPD (secondary); 26 commanders, 156 decisions (unverified) | Klein et al. 1986 via a01, a09, a27, b20, d12 | [S] counts unverified |
| Naval AEGIS officers mostly recognitional | 95 percent recognitional, 4 percent option comparison (abstract record only) | Kaempf et al. 1996 (a26, not opened) | [S] |
| Sport experts: simple match share | 60-81 percent simple match, 13-28 percent diagnosis, 3-24 percent evaluate; first option preferred about 80 percent (uncited) | Macquet 2020 via b06, a19 | [S] second-hand |
| One goalkeeper (N=1) | 83 accounts: simple match 46 percent, simulation 34, diagnosis 20; rater agreement 85 percent / 95 percent | Le Menn 2019 (a18) | [S] |
| Intuition valid only with valid cues plus practice | Two conditions; 10,000 hours for chess (Chase and Simon) | Kahneman and Klein 2009 (a04, a11, b19) | [E] |
| Fractionated expertise | Predictors: predictability, experience, feedback, static stimuli | Shanteau 1992 via a05 | [S] list only |
| Models of judges beat judges | 29 clinicians, 861 profiles, 11 scales | Goldberg 1970, Karelaia and Hogarth 2008 (a06) | [S] |
| Take-the-first: first option better than later | 85 handball players, 31 trials | Johnson and Raab 2003 (b10) | [C] |
| Take-the-first replications mixed | Belling 2014: option count not significant; Laborde and Raab 2013: experts fewer options than near-experts, not than non-experts; Klein and Peio chess: not significant | b09, b11, b12 | [C] |
| Elite handball players choose best option more but are slower | Best choice 44.7 percent (72) elite vs 20.8 percent (32) amateur, chi2(1)=20.4; RT 1,920 vs 1,704 ms; n=22 per group | Embodied choice study (b13) | [S] |
| Referees: analytic slightly better than intuitive | 76.3 vs 74.7 percent, F(1,58)=5.29, p=.025; experts 83.5 vs 85.1 (ns); novices 69.0 vs 64.3; expertise 84.3 vs 66.6; n=60 | b14 | [S] |
| Unconscious thought no reliable benefit in medicine | d = 0.14 [-0.16, 0.43]; experts d = -0.14, novices d = 0.24 (opposite to theory) | b15 meta-analysis | [C] |
| Team-sport RPD studies fit RPD | 53 studies, 2,078 participants; only 4 tested RPD, 7-23 people each | a21, b07 | [S] weak test |
| Deliberation under pressure hurts athletes | Effect sizes not given | Raab and Laborde via b08 | [S] |
| Police stress and training | N=122; 27.9 percent made a lethal-force error; each training level +3 points (beta .461); each service year -0.39; higher sympathetic arousal lower score (B=-0.571); R2=.30 | Baldwin 2022 (a17) | [S] |
| Stress shifts decisions to habit | Directional only (Schwabe and Wolf 2009; Margittai 2015; Keinan 1987) | Yu 2016 (a16) | [S] model |
| ShadowBox, Marines | N=59 (feedback arm n=29); .59 vs .44, t(58)=2.45, d=.63 | Klein 2016 (a13) | [S] |
| ShadowBox, Army lieutenants (no control) | .48 to .58, d=.38; 20 of 30 improved, 10 got worse (mean -36 percent) | a14 | [S] |
| ShadowBox, fire officers | 86.9 vs 73.6 (N=15 controls), F=14.09 | Hintze 2008 (a12) | [S] |
| Video decision training, referees | 6 RCTs, N=163, g = 1.718 [1.058, 2.377], I2 69.6 percent | b16 | [S] likely inflated |
| Practitioners favour analysis | N=225 Norwegian military students: "generate several options and compare" M=1.88 (1 = agree); "rely on logic not intuition" M=3.00 | b18 | [S] attitude |
| RPD prompt raises LLM triage accuracy | Default 63.3, RPD 67.6, data-frame 66.7 percent; 13,500 answers; OR 2.26 and 2.05 | Kopka and Feufel 2026 (b01, c01) | [S] |
| Gain sits in under-called class | Self-care 13.4 to 29.8 (RPD), 24.6 (data-frame); non-emergency flat 82.5/82.0/82.8; emergency n=2 | c03, b03 | [S] |
| Gain is uneven by model | GPT-4.1 mini 49.8/60.7/62.4; GPT-4.1 64.4/72.7/72.4; GPT-4o 65.3/70.7/66.2; o3 70.7/75.1/76.2; GPT-5.2 Instant 57.8/56.4/55.3; GPT-5.2 Thinking 52.0/53.1/51.8 | c04 | [C] |
| RPD prompt helps and hurts cases | Up in 18 of 45 (median +18 pts), down in 13 (median -5); 12 of 13 drops non-emergency | c06 | [S] |
| RPD prompt less consistent | Modal share 76.9/66.9/71.1 percent; kappa .766/.717/.751 (ns); correct at least once 73.1/82.2/78.4 | c07 | [S] |
| Chain of thought hurts on implicit-pattern tasks | GPT-4o grammar 87.5 to 64.4 (-23.1, p<.0001); o1-preview 57.7 vs GPT-4o zero-shot 94.0 (cross-model); Claude 3 Opus 70.7 to 62.7; Claude 3.5 Sonnet 65.9 vs 67.7 (no drop) | Liu et al. 2025 (b04, c16) | [E] with d07 |
| CoT hurts face recognition | GPT-4o 64.0 to 51.2; Claude 3 Opus 44.0 to 29.6; Gemini 1.5 Pro 66.0 to 54.6; Sonnet 3.5 97.8 to 94.8; chance 20 percent | c17 | [S] |
| CoT slows learning rules with exceptions | GPT-4o 2.9 vs 12.5 rounds (+331 percent) | c18 | [S] |
| Longer reasoning hurts with distractors | Claude Opus 4 falls to about 80 percent on Python distractors; NoisyBench drops up to 80 percent | d07, d08 | [C] |
| Skipping thinking wins at low budget | AMC23 at 700 tokens: 51.3 vs 28.9; 3.3-3.7x fewer tokens on proofs | Ma 2025 (d01) | [S] |
| First round holds the answer | Over 92 percent of cases first round correct, under 60 percent of tokens; 48.6 percent token cut on MATH500 | Chen 2025 (d04) | [S] |
| Verifier makes many samples win | SWE-bench Lite 15.9 to 56 percent at 250 samples | Brown 2024 (d02) | [S] |
| Allocate compute by difficulty | About 4x saving vs best-of-N | Snell 2024 (d03) | [E] with d04, d09 |
| Token budget compresses reasoning | 83.75 to 81.03 percent, 461 to 149 tokens (67 percent fewer); 5-token budget 52.31 percent | Han 2025 (d09) | [S] |
| Always-on self-correction hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0 after 2 rounds | Huang 2024 (d06) | [S] older models |
| Always-on factored verification helps recall tasks | List precision 0.17 to 0.32 (factored), 0.36 (two-step) | CoVe (d11) | [S] |
| RPD agents beat human-only teams | API 5.725 vs 4.748 low switching; 3.863 vs 3.208; 2.833 vs 2.015; F=5.99, p=.025; 10 teams per arm | Fan et al. (c09, c10) | [S] |
| LLMs poor stand-ins for experts | 214 experts; about half of actions no significant difference; persona prompts no effect | Lamparth 2024 (c21, c22) | [S] |

## 4. Mechanisms and models

**RPD as a program an engineer could build.**

```
state = observe()
pattern = match(state, library)            # recognition
if pattern is None:                        # level 2: diagnose
    story = build_story(state)             # explain cues; look for expectancy violations
    pattern = match(story, library)
cands = pattern.actions                    # ordered by typicality
for a in cands:                            # serial, one at a time
    outcome = simulate(a, state, pattern.expectancies)   # level 3
    if outcome.ok: return a
    m = modify(a, outcome.flaws)
    if simulate(m, state).ok: return m
return fallback()                          # no option passes
monitor(expectancy)                        # violation -> back to diagnose
```

Key design points taken from the sources:
- Order matters. The first candidate is the most typical one for the matched pattern (a02).
- Expectancy monitoring triggers diagnosis. A violated expectancy is the signal to re-think (a24). This is a signal-triggered rethink, the same rule as G1.
- Recognition has four by-products: expectancies, cues, goals, actions (a24).
- Computational versions: R-CAST adds recognition cycle plus information exchange between agents about relevant cues (c09). Danial et al. learn the match with a Markov logic network from data (a23).

**Kopka and Feufel's prompt version** (c02): match the case to a typical known case, state the usual decision, simulate it, test whether it works, modify and retest if it fails, reassess if unfamiliar. Output format "Analysis ... || Answer ...". The default arm asked only "Answer: [category]" with no reasoning. So RPD versus default confounds the RPD content with having any reasoning text at all. No equal-length plain chain-of-thought arm exists.

**Data-frame loop** (c14): three functions: extract evidence, retrieve hypotheses, score hypotheses in [0,1]. Stop when max score >= tau; otherwise add evidence or hypotheses. This is a threshold-based stopping rule that code can implement, with the score computed by code or by held-out checks, not by the model's feeling (G5).

**Premortem as an operator** (a08): "assume this plan failed; list reasons", two minutes, one round. Fits as an O-operator at S6 or after a failed check, not on a schedule (G1).

**Valid-cue gate** (a04): the recognition route is trusted only when the class has (a) valid cues and (b) fast feedback. For an agent, (b) becomes: the class has a cheap check or a track record of plain pass rate in S0 or S9 data.

**Difficulty routing** (d03, d14): estimate difficulty, then spend: easy gets sequential revision or one answer; hard gets parallel sampling or search. A difficulty estimate costs compute and shrinks the gain.

**Token budget as a dial** (d09): put the budget in the prompt, near the minimum needed. Budgets far too small raise cost (token elasticity).

## 5. What holds up

**Replicated or agreed across independent sources.**
- Intuition is reliable only in regular environments with practice and feedback. Kahneman and Klein (opposing camps) agree; Klein 2016 restates it; Shanteau's lists point the same way (a04, a05, a11). [E]
- Extra explicit reasoning can lower accuracy on implicit-pattern, visual-recognition and distractor tasks, in two independent paper families (Liu 2025; Gema 2025; NoisyBench) (K07). [E] But it is model-specific: Claude 3.5 Sonnet shows no drop, 3 of 6 human-failure archetypes did not transfer, and o3 resists distractors.
- Best compute use depends on difficulty (Snell, Chen, Han; K16). [E]
- Many samples win only with a verifier (Brown); without one, voting and reward models plateau (d02).

**Weak, mixed or failed.**
- The 80-90 percent RPD share: secondary only. The naval study says 95 percent. Sport studies say 60 to 81 percent simple match. The spread reflects domain and coding rules (critique). No independent re-coding by sceptics exists in the sources.
- Take-the-first: supported by Johnson and Raab, partly or not by Belling 2014, Laborde and Raab 2013, Klein and Peio (b09-b12). [C]
- Fast versus slow under time pressure: referee gap is 1.6 points; unconscious-thought meta-analysis is null with an expertise moderator opposite to theory (b14, b15). Elite handball players were slower on their best choices, not faster (b13). The simple "experts are fast and intuitive" story is not supported.
- Deliberation hurts athletes under pressure (b08), but if-then rule instruction helped transfer to complex tasks. So rule instruction is not worthless.
- Practitioners themselves believe in option comparison (b18), which shows NDM is not the folk view even in the military.
- NDM's field data are retrospective, mostly interview and think-aloud, with small N and no comparison group (a27, a21, b07). "RPD fit" is a loose test because the model has three levels and fits many outcomes.
- Preprint-to-paper shrinkage: Kopka and Feufel RPD 70.2 vs default 64.7 (preprint, snippet only) became 67.6 vs 63.3 (published). Use the published numbers.

**Moderators.**
- Expertise: experts equal under both styles, novices gain from analysis (b14).
- Time: Basevitch found intuition better when time was short and more options better when time was longer (a21).
- Model strength: the RPD prompt gain is larger for weak models in absolute terms and shows no gain for GPT-5.2 (c04, c05).
- Class base rate: gain concentrated in an under-called class; flat in the strong class (c03).

**Interventions that worked.** ShadowBox (d = .63, .38; 10 of 30 got worse), video training (g = 1.718, I2 69.6 percent, likely inflated, no active control) (a13, a14, b16). Training and service-year effects in police (a17). Outcome measures are agreement with experts or accuracy on similar clips, not field performance.

**Interventions that did not work or are unproven.** Premortem: no outcome data in sources (a08). Persona prompts for experts: no effect (c22). Mere prompting for noisy context: no fix (d08). Unconscious thought for clinicians: null (b15). Always-on self-correction without a signal: hurts older models (d06).

## 6. Language models

**Direct test of RPD as a prompt** (Kopka and Feufel 2026; b01-b03, c01-c07). 10 OpenAI models, 45 real triage vignettes, 3 prompts, 10 runs each = 13,500 answers.
- Overall: default 63.3 percent, RPD 67.6, data-frame 66.7. Mixed logit OR 2.26 and 2.05. Gain about 4 points.
- Where: self-care 13.4 to 29.8 percent. Non-emergency flat. Emergency had n=2, so no safety claim. Overtriage is 88 percent of errors. The default prompt was biased toward over-cautious answers, so the RPD gain looks like a shift in bias (critique). A balanced-set re-test is missing.
- By model: gains of +4.4 (o3) to +10.9 (GPT-4.1 mini) for RPD; GPT-5.2 Instant -1.4 and Thinking +1.1. Version is confounded with collection date (Feb 2026 vs May 2025).
- Case level: RPD helped 18 of 45, hurt 13.
- Consistency: modal share fell 76.9 to 66.9 percent. Correct-at-least-once rose to 82.2 percent, which is an oracle measure.
- Not controlled: tokens, and a plain chain-of-thought arm.

**Reasoning versus recognition** (Liu et al. 2025). Forced chain of thought hurts where verbal thinking hurts people: implicit statistical learning, face recognition, learning with exceptions. Numbers in section 3. Extras confirmed in the critique: bigram-instructed CoT reaches 68.43; a 3-node grammar shows no difference; temperature is robust; tree-of-thought 64.55 vs 62.52 CoT, still far below zero-shot. Note the "-36.3" is a cross-model comparison (o1-preview vs GPT-4o zero-shot), not a same-model drop.

**Overthinking and inverse scaling.**
- First round correct in over 92 percent of cases; o1-like models used 1,953 percent more tokens than conventional models on "2+3" (d04). Training on first-correct only: 1.1 solutions, 878.7 vs 1,051.3 tokens (d05).
- Distractors: Claude Opus 4 down to about 80 percent on Python distractors; o3 stable in the controlled setup; few-shot examples fixed spurious-feature failures (d07). NoisyBench: drops up to 80 percent, inverse scaling in noisy settings; prompting did not fix it; the fix was a training reward, so it does not transfer to a scaffold-only agent (d08).

**Compute allocation.**
- NoThinking at matched tokens: AMC23 51.3 vs 28.9 at 700 tokens; under about 3,000 tokens NoThinking wins at every k; Thinking wins pass@1 at about 3,500 tokens; on LiveCodeBench Thinking wins even at low budget (d01).
- Repeated sampling: coverage log-linear with a verifier (d02).
- Difficulty-matched allocation: about 4x (d03). TALE: 67 percent fewer tokens with under 3 percent loss (d09). s1 budget forcing: AIME24 50 to 57 percent (d10, fine-tuned, abstract and intro only).

**Self-checking.** Without an external signal, correction hurts older models (GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0). With oracle labels it looks good (97.5) (d06). Self-consistency with 6 responses 85.3 and 9 responses 88.2 on GSM8K beat multi-agent debate at the same response count. Chain-of-Verification, factored: precision 0.17 to 0.32 on list questions (d11, garbled table). Models are from 2023; current models may differ.

**Bias.** o1 shows no significant bias in 7 of 10 clinical vignettes; hindsight bias difference 52.2 points; Occam's razor reversed fully (b24). BiasMedQA: reasoning variants more accurate (OR 4.0, 3.6, 3.2) but not consistently less biased; debiasing instruction cut biased answers from 49.9 percent to 18.5 percent; few-shot to about 5 percent (b25). CRT: 5 percent GPT-3 davinci-003, 38 percent humans, 59 percent ChatGPT-3.5, 96 percent GPT-4; this says nothing about tasks where intuition is right (c19). GPT-3 matched humans on 12 of 12 vignettes but broke under rewording (c20).

**Expert stand-ins.** In a Taiwan-strait crisis game with 214 national-security experts, GPT-3.5, GPT-4 and GPT-4o differed from experts on about half of actions without significance, were more aggressive on some, and persona prompts ("strict pacifist" vs "aggressive sociopath") had no effect (c21, c22). Five models escalated unpredictably in an 8-nation simulation (c23).

**Classical NDM agents versus LLMs.** Alignment with a decision maker on health insurance: classical AI 0.892, GPT-5 0.895, GPT-4 0.892; differences are noise (c13). A single-pass multiple-choice "System 1" tool selector: 97.0 percent vs 95.2 percent for the best of 18 LLM-agent settings, 0 percent invented content vs 5.5 to 19.7 percent (c25). Reading this as recognition is our interpretation.

**Position papers, no data.** Data-frame dynamics (c14); collaborative sensemaking (c15, sycophancy as fatal to sensemaking). Practitioner premortem prompts exist with no measurement (c30). Searches found no LLM test of premortem, CDM, or RPD with commanders beyond Kopka and Feufel (c29, K13).

**Time pressure for LLMs.** The analogy is weak. Token caps shorten output with small loss until a floor (d09). Longer reasoning hurts only in noisy or distractor tasks (d07, d08). No study shows human-style stress degradation of an LLM. Stress effects in humans (a16, a17) come from arousal and prefrontal control, which a model lacks.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Route to a direct, short mode only where the class has valid cues and a cheap check or a known plain pass rate; do not use the model's confidence as the validity signal | S0 gate, G10 | [E] | K02; a04, a05, a11, b19 |
| On pattern and recognition tasks (implicit rules, visual matching, exceptions) include a direct no-reasoning arm and do not default to step-by-step | G11, S0 | [E] | K07; b04, c16-c18, d07 |
| Spend by estimated difficulty and checkability: easy gets one short answer or one revision; hard gets parallel samples where a check exists | G12, S0 | [E] | K16; d01, d03, d04, d09, d14 |
| Keep rethinking, critique and premortem off by default; fire them only on a failed external check or an expectancy violation | G1 | [E] (already in SCHEMA) | K13, K18; d06 (indirect), a24 (expectancy trigger) |
| Cap reasoning length and filter distractors from input; use few-shot examples when a spurious feature is known | G11, S1 | [E] for the direction, [C] on size | K19; d07, d08, d09 |

These add no new element to SCHEMA.md. They confirm G1, G10, G11, G12 and S0.

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| RPD loop in S3/S4: one typical candidate first, simulate or check, next candidate only on failure, versus 4 parallel candidates | S3/S4 | [S] | K01, K08, K15; a02, b10, d04 |
| RPD-style prompt (match typical case, state usual decision, simulate, test) vs default and plain CoT at equal tokens on a balanced set | S2/S3 mode prompt | [S] | K04, K05, K06; b01-b03, c01-c07 |
| Number of candidates (1, 2, 4) and first-candidate quality | S3 | [C] | K08; b09-b12, d04 |
| Data-frame loop with a code-scored stopping threshold | S2/S7 | [S] | c14; no measurement |
| Premortem as O-operator on failed check, not always-on | S6 | [S] | a08, c30; K13 |
| Expert-ranked exemplar traces in few-shot memory | memory | [S] | K10; a13, a14, b16, d07 (few-shot fix) |
| Vote of 3 to 5 short samples vs one sample, code-selected | G5, S7 | [S] | K03; a06 |
| Verifier-driven generate-and-test only where a cheap checker exists; vote otherwise | O generate-test | [S] | K17; d02 |
| Difficulty router based on Liu archetypes (implicit pattern, visual) | S0 | [S] | d14; no router exists |
| Expectancy-violation trigger: store the expected check result for a candidate, rethink only when actual differs | S4/S6, G1 | [S] | a24; no LLM test |

## 8. Concrete tests on our bench

All arms get the same total token budget (output plus input), counted, with setup cost included (G7). Report absolute accuracy and the class mix.

| Test | Item type | Arms at equal tokens | Metric | Expected effect |
|---|---|---|---|---|
| T1 take-the-first | Checkable tasks (code with tests, small exact-answer puzzles) | (a) one candidate, test, fall to next on failure; (b) 4 parallel short candidates, code selects by check; (c) 4 candidates, vote | Pass rate; share of first-candidate failures that later candidates fix | RPD loop wins on easy items; parallel wins on hard; tie overall |
| T2 RPD prompt on balanced triage | Non-medical and medical triage sets with equal class counts | default, plain CoT of equal length, RPD prompt, data-frame prompt | Balanced accuracy; per-class recall; modal share | RPD +0 to 4 points over default; no gain over plain CoT at equal length |
| T3 direct vs deliberate on pattern items | Artificial grammar, face or shape matching from description, rules with exceptions | direct, short CoT, long CoT, S3 deliberation | Accuracy; rounds to learn | Direct wins on 2 of 3 types for models in the Liu pattern |
| T4 trigger vs always-on premortem | Checkable planning or code tasks | no premortem, always premortem, premortem on failed check or disagreement | Accuracy; tokens | On-signal >= always >= none, with always-on lowest on easy items |
| T5 candidate count | Open and closed tasks | 1, 2, 4 candidates | Quality of first vs best | First is at least as good on easy items |
| T6 expert-exemplar memory | Decision items with expert-ranked options | none, 3 ranked exemplars with reasons, 3 unranked exemplars | Match to expert ranking; accuracy | Ranked beats none by about 0.3 d; unranked no gain |
| T7 difficulty router | Mixed-difficulty set | always-deliberate, always-direct, difficulty-routed | Accuracy at equal total tokens | Routed beats both by 2 to 5 points |
| T8 token cap | Distractor-heavy and clean items | no cap, cap, cap with distractor filter | Accuracy by item type | Cap helps on distractors, costs under 3 points on clean |
| T9 expectancy trigger | Multi-step tool or code tasks | rethink on a schedule, rethink on expectancy violation, no rethink | Task success; tokens | Violation trigger best |
| T10 sample vote | Single-answer tasks, no checker | 1 long sample, 3 and 5 short samples with code vote | Accuracy | Vote of 3 to 5 beats one long sample |

## 9. What does not transfer, and why

- **Human stress effects** (a16, a17). Arousal and prefrontal control have no counterpart in a model. Token pressure is a different mechanism (K11).
- **Felt familiarity.** RPD's "feels familiar" step has no meaning for a model; in the prompt it is a text instruction only (c02).
- **Ten to twenty years of practice** (a09). An agent has no personal practice; it has a training distribution and our memory library. The valid-cue condition has to be tested per class, not assumed.
- **Expert stand-ins.** LLM personas do not reproduce expert choices and ignore persona instructions (c21, c22).
- **Sport and fireground samples.** Mostly N=1 to 60, video-based, interview-based, sport-based (a18, a21). The 80-90 percent share is domain and coding dependent.
- **Always-deliberate versus always-intuitive framing.** Not supported even in humans (b14, b15). For the agent, the useful question is per-class mode choice.
- **R-CAST results** (c09-c11). Student teams, hand-built rules, 10 per arm, one research group; no replication with modern LLM agents.
- **Premortem and team debiasing.** Developed for human group dynamics (leader speaks last, anonymity). G9 already rejects multi-agent debate; one model's samples are not independent.
- **Training outcomes measured as agreement with experts** (ShadowBox). That is a closeness to experts score, not performance.
- **Sycophancy and long outputs.** Human NDM assumes the decision maker has its own view; LLMs conform to stated answers (G5), so a human-style "challenge the plan" step must be code-triggered.

## 10. Open questions

1. What are the exact 1986 counts and coding rules behind 80-90 percent RPD, and do later coded studies agree? (needs the original proceedings)
2. Is the Kopka gain real accuracy or a bias shift toward self-care calls? A balanced set is needed.
3. Does an RPD-style prompt beat plain CoT and best-of-N at equal tokens on non-medical tasks?
4. Is the first candidate better than later ones for LLM generation on hard items (Chen's data are easy math)?
5. Do premortem, CDM or data-frame prompts help if triggered only on a failed check?
6. Which task features predict that direct mode beats deliberate mode, and can a cheap router detect them from the item alone?
7. Do expert-ranked exemplars improve agent decisions at equal context length?
8. Do R-CAST-style agents replicate with LLM agents in multi-task switching?
9. How well can LLMs stand in for experts beyond one crisis scenario?
10. Is there any analogue of time pressure for an LLM that degrades decisions the way stress degrades humans?
11. Does the GPT-5.2 null reflect model change, date drift, or ceiling? (c04 notes confounding)
12. Why did 10 of 30 Army lieutenants get worse after ShadowBox (a14), and does an agent have an analogue?

## 11. Sources

[V] opened this session or by earlier agent; [M] snippet or abstract record only.

- [V] Kahneman and Klein 2009, Conditions for intuitive expertise. https://www.hansfagt.dk/Kahneman_and_Klein(2009).pdf (a01-a08)
- [M] Same paper, PubMed abstract. https://pubmed.ncbi.nlm.nih.gov/19739881/ (b19)
- [V] Klein and Wright 2016, Macrocognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC4731510/ (a09, a10)
- [V] Klein et al. 2016, Can we trust best practices? https://www.gary-klein.com/_files/ugd/2360d8_6a4be03988d44f1e88d21d177756402b.pdf (a11)
- [V] Klein et al. 2016, ShadowBox evaluation. https://www.gary-klein.com/_files/ugd/2360d8_32306473d35f4022ac49e0456830f8dc.pdf (a12-a14)
- [V] Flin et al. 2007, surgeons. https://pmc.ncbi.nlm.nih.gov/articles/PMC2464983/ (a15)
- [V] Yu 2016, SIDI model. https://pmc.ncbi.nlm.nih.gov/articles/PMC5146206/ (a16)
- [V] Baldwin et al. 2022, A reasonable officer. https://pmc.ncbi.nlm.nih.gov/articles/PMC8803048/ (a17)
- [V] Le Menn et al. 2019, handball goalkeeper. https://pmc.ncbi.nlm.nih.gov/articles/PMC6942481 (a18)
- [V] Bossard et al. 2022, NDM in sport (cites Macquet 2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC9252097/ (a19, b06)
- [V] Collins et al. 2016, coaches. https://pmc.ncbi.nlm.nih.gov/articles/PMC4830814/ (a20)
- [V] Systematic review of team-sport decision making 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8156213/ (a21, b07, b08)
- [V] Shin 2019, clinical reasoning. https://pmc.ncbi.nlm.nih.gov/articles/PMC6900348/ (a22)
- [V] Danial et al. 2019, RPD for artificial agents. https://link.springer.com/content/pdf/10.1186/s13673-019-0197-2.pdf (a23, a24)
- [V] Heander et al. 2025, code review. https://arxiv.org/abs/2507.09637 (a25, c24)
- [M] Kaempf et al. 1996, naval command and control. https://data.zhenzhi.com/details/1/866709503 (a26)
- [M] Klein, Calderwood and Clinton-Cirocco 1986. https://apps.dtic.mil/sti/pdfs/ADA199492.pdf (a27; file damaged)
- [M] Johnson and Raab 2003. https://ideas.repec.org/a/eee/jobhdp/v91y2003i2p215-229.html (a28)
- [V] Kopka and Feufel 2026, JMIR Biomed Eng. https://pmc.ncbi.nlm.nih.gov/articles/PMC13061108/ (b01-b03, c01-c07; doi 10.2196/88053 not re-opened in critique, single source)
- [M] Kopka and Feufel preprint. https://preprints.jmir.org/preprint/88053 (c08)
- [V] Liu et al. 2025, Mind your step by step. https://arxiv.org/abs/2410.21333 (b04, b05, c16-c18; re-checked in critique)
- [V] Belling, Suss and Ward 2014. https://gala.gre.ac.uk/id/eprint/12003/ (b09-b12, b28; Johnson and Raab, Raab and Johnson, Klein and Peio read through it)
- [V] Embodied choice in handball 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9207261/ (b13)
- [V] Referee yellow card decisions 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11322511/ (b14)
- [V] Unconscious thought meta-analysis 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4436803/ (b15)
- [V] Video training for referees meta-analysis 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12239248/ (b16)
- [V] ShadowBox in medicine 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13595719/ (b17; abstract and opening only)
- [V] Norwegian military survey 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13113691/ (b18)
- [M] Frontiers 2016 perspective (1986 study, Lipshitz 2001). https://www.frontiersin.org/articles/10.3389/fpsyg.2016.00054/full (b20, b21, d12; page read, secondary)
- [V] Wikipedia, NDM and RPD. https://en.wikipedia.org/wiki/Naturalistic_decision-making ; https://en.wikipedia.org/wiki/Recognition-primed_decision (b22, b23, d13)
- [V] o1 bias vignette study 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12372181/ (b24)
- [V] BiasMedQA 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13528315/ (b25)
- [V] VR-DMX 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC12783459/ (b26)
- [V] Old wine in a new bottle 2026 (abstract and intro). https://pmc.ncbi.nlm.nih.gov/articles/PMC13600057/ (b27)
- [V] Fan et al. R-CAST 2009. https://agentlab.ist.psu.edu/lab/publications/Fan_SMC2009.pdf (c09, c10)
- [V] Fan et al. 2005. https://cs.huji.ac.il/course/2005/aisemin/articles2006/docs/pa7e4_945.pdf (c11)
- [M] Norling et al. via patent. https://patents.google.com/patent/US8442839 (c12)
- [V] Mainali et al. 2025. https://arxiv.org/abs/2510.06093 (c13)
- [V] Zheng et al. 2025. https://arxiv.org/abs/2504.15894 (c14)
- [V] Jain and Khurana 2025. https://arxiv.org/abs/2512.07801 (c15)
- [V] Hagendorff et al. 2023. https://arxiv.org/abs/2212.05206 (c19)
- [V] Binz and Schulz 2023. https://arxiv.org/abs/2206.14576 (c20)
- [V] Lamparth et al. 2024. https://arxiv.org/abs/2403.03407 (c21, c22)
- [V] Rivera et al. 2024. https://arxiv.org/abs/2401.03408 (c23)
- [V] Tzanis and Klontzas 2025. https://arxiv.org/abs/2611.21053 (c25)
- [V] Binz et al. 2025, Centaur (abstract). https://arxiv.org/abs/2410.20268 (c26)
- [V] Albert and Billinger 2024 (abstract). https://arxiv.org/abs/2410.06932 (c27)
- [M] Frontiers in AI 2025, JDM for LLM evaluation. https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1592399/full (c28)
- [V] arXiv negative search. https://arxiv.org/search/?query=%22recognition-primed%22&searchtype=all (c29)
- [M] Practitioner premortem prompt page. https://www.tomsguide.com/ai/i-use-the-pre-mortem-prompt-before-every-big-decision-its-stopped-me-making-3-huge-mistakes (c30)
- [V] Ma et al. 2025, Reasoning models effective without thinking. https://arxiv.org/abs/2504.09858 (d01)
- [V] Brown et al. 2024, Large Language Monkeys. https://arxiv.org/abs/2407.21787 (d02)
- [V] Snell et al. 2024. https://arxiv.org/abs/2408.03314 (d03, d14)
- [V] Chen et al. 2025, overthinking. https://arxiv.org/abs/2412.21187 (d04, d05; table text garbled)
- [V] Huang et al. 2024, self-correction. https://arxiv.org/abs/2310.01798 (d06)
- [V] Gema et al. 2025, inverse scaling. https://arxiv.org/abs/2507.14417 (d07)
- [V] Lee et al. 2026, NoisyBench. https://arxiv.org/abs/2601.07226 (d08)
- [V] Han et al. 2025, TALE. https://arxiv.org/abs/2412.18547 (d09)
- [V] Muennighoff et al. 2025, s1 (abstract and intro). https://arxiv.org/abs/2501.19393 (d10)
- [V] Dhuliawala et al. 2023, Chain-of-Verification. https://arxiv.org/abs/2309.11495 (d11; table text garbled)
- [M] Gap search log. https://arxiv.org/ (d15; absence of search, not absence of evidence)
