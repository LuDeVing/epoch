# Motivation, mindset, classroom factors: deep document

*Subfield A05.10. Key works: Dweck. Sources: evidence_a-d.jsonl (ids a01-d18), claims.jsonl (K01-K25, prefix A05.10-), critique.md. Where ids are cited they are evidence ids in those files. "Opened" means the page or PDF text was read this series; snippet-only items are flagged.*

**Bottom line.** The human mindset literature gives a small, heterogeneous, contested average effect (about 0.05 to 0.11 SD) that depends on context. The LLM literature tests prompt wording (emotion, tips, threats, politeness, personas, trust framing), not mindset as the theory defines it. On current models, motivational wording gives no reliable gain. The thing that works in agents is a verifier-backed retry loop with a stored lesson (Reflexion), which is already in the schema (S5, S9, G2). Almost nothing in this subfield should be added to the schema now.

## 1. What it is

This subfield covers motivation, beliefs about ability ("mindset"), and classroom conditions that shape effort and learning. The anchor is Carol Dweck's work.

Core terms:
- **Implicit theory of intelligence.** A belief that ability is fixed (entity theory, "fixed mindset") or can be grown by effort and strategy (incremental theory, "growth mindset").
- **Goal orientation.** Learning goals (get better) versus performance goals (look good). Fixed beliefs push toward performance goals.
- **Helpless versus mastery response.** After failure, helpless students give up, blame ability, and avoid challenge. Mastery students try new strategies and persist.
- **Mindset intervention.** A short course (usually two online sessions of about 25 minutes) that teaches that the brain can change with effort, hard tasks, better strategies and help-seeking.
- **Mindset x context.** The claim that a belief helps only where the setting lets a student act on it (challenge-seeking peers, supportive teachers, flexible course tracks).
- **Related motivation work in this folder.** Self-determination theory (autonomy, competence, relatedness) and the over-justification effect (extrinsic rewards lower intrinsic interest). Self-efficacy (Bandura). These were not opened (a24, a25, a26) except through a meta-analysis (a18).

Why it is in our project. We build one language-model agent that thinks well through a scaffold, not training. The question is whether any motivational idea (belief framing, encouragement, praise, curiosity, trust) can be turned into a scaffold element that wins at equal tokens. The honest answer so far is: mostly no, for the reasons in sections 5, 6 and 9.

## 2. History and theories in depth

**Lineage (a07).** Learned helplessness (Seligman and Maier 1967) led to attribution theory, then to Elliott and Dweck (1988) on performance versus learning goals, then to Dweck and Leggett (1988) on entity versus incremental theories (a24, not opened). Dweck and Yeager (2019) describe mindset as a "meaning system": a belief ties together goals, attributions, effort beliefs and strategies.

**Founding correlational studies.**
- Robins and Pals (2002): 363 Berkeley students tracked over 3 years (a07).
- Blackwell, Trzesniewski and Dweck (2007), Study 1: 373 seventh graders over 2 years. Incremental belief predicted rising maths grades; entity belief predicted flat grades. Study 2: an intervention group (N=48) versus control (N=43) reversed the grade decline (d11, abstract only; slopes not read).
- Nationally representative US ninth graders, over 14,000: fixed mindset versus GPA r=-.22 (a07).

**Founding praise study (d09, read in full).** Mueller and Dweck (1998). Study 1, 123 children: after intelligence praise 67% chose performance goals; after effort praise 8%. After failure, score change was -0.92 (intelligence praise), +1.21 (effort praise), +0.13 (control). Study 3, N=88: 38% of intelligence-praised children misreported their score, versus 13% (effort) and 14% (control).

**Two eras (a07, a08).** Dweck and Yeager separate an "era of correlations and small experiments" from an "era of scaled interventions". They warn against "false growth mindset": praising effort alone, or posters with no change in practice.

**National Study of Learning Mindsets (NSLM, Yeager 2019, a01 to a04).** Pre-registered (osf.io/tn6g4), 65 US public schools, 12,490 ninth graders randomised individually. Two online sessions about 20 days apart. Control: lessons on brain function only.

**Context turn (a09).** Hecht, Yeager and Dweck (2021) argue a belief helps only if the setting affords acting on it. The Norway U-say RCT (about 49 of 50 high schools in two counties; a27, second-hand) changed maths course choices far more where tracks were flexible.

**Teacher turn (b04, b05).** Yeager 2022: the effect appeared in classes of growth-minded teachers.

**Critique and meta-analyses.** Burnette 2013 (a13) showed incremental beliefs relate to goals and strategies. Sisk 2018 (a12, b06-b08) found weak overall links. Macnamara and Burgoyne 2023 (a14) found near-zero intervention effects after bias correction. Yeager, Tipton and Burnette responded with a multilevel re-analysis (b10, b25). Both sides are invested; see section 5.

**Motivation neighbours.** Deci, Koestner and Ryan (1999, a18): tangible, expected rewards reduce later free-choice intrinsic motivation. Opower-style scale-up warnings (a16): average effects shrink when programmes go from pilots to millions.

## 3. Core findings with exact numbers

Status codes: E = established, S = single-source, C = contested (these match the claim statuses in claims.jsonl).

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| Mindset-achievement correlation is small and positive | Sisk meta-analysis 1: k=273, N=365,915, r about .10. Large proponent datasets: r=.24 to .34 with grades; PISA 2018 N=555,458 positive in 72 of 74 nations (single-item measure) | b06, a10, a13 | E (correlational) |
| Mindset correlates with goals and strategies | Burnette 2013: k=113, N=28,217. Learning goals r=.187; performance goals -.151; helpless strategies -.238; mastery strategies .227; negative emotion -.233; expectations .157 | a13 | E (possibly inflated by bias) |
| Student-level interventions: tiny average gain | Macnamara and Burgoyne: 63 studies, N=97,672, d=0.05 [0.02, 0.09]; 13 studies d=0.04; highest-quality 6 studies d=0.02. Tipton re-analysis: 0.09 SD overall (k=122), 0.15 at-risk, 0.05 after corrections (p=.004) | a14, b10, b25 | C |
| Sisk intervention meta-analysis | k=43, N=57,155; d=0.08 [-0.01, 0.17], not significant; larger for low-SES or at-risk | a12, b07 | E (abstract plus table) |
| NSLM main result, lower achievers | n=6,320: +0.10 GPA points [0.04, 0.16], p=.001, d=0.11. Higher achievers about 0 (interaction B=0.09 [0.01, 0.17], p=.034, N=12,490) | a01, b03 | S (proponent-run, one trial) |
| Belief changed more than grades | Fixed-mindset score -0.38 on a 1-6 scale, d=0.33 (n=5,650) versus d=0.11 on grades | a02 | E |
| Advanced maths course-taking (exploratory) | 33% to 36%, +3 pp [0.01, 0.04], n=6,690, 41 schools | a04 | S |
| School norm moderation | Lower achievers x challenge-seeking norm B=0.11 [0.01, 0.21], n=6,320, k=65. Top-quartile-norm schools: 0.18 GPA | a03, b03 | S |
| Teacher mindset moderation (NSLM) | 223 teachers, 9,167 records. Fixed-mindset teachers CATE -.02 [-.074, .038]; growth-mindset teachers .11 [.046, .167]; interaction b=0.09, p=.005. Student mindset shift d=0.37 regardless of teacher. Teacher-level effect r=.55 with teacher mindset | b04, b05 | S |
| Independent teacher-mindset data | Chile census: 292,960 students, 24,636 teachers; +0.02 SD, larger in low-income schools (0.053 SD difference). Teacher self-report ceiling 89% | d14 | S |
| A teacher-delivered trial found reverse direction | Larger gains for students of fixed-mindset teachers. No numbers read (403) | d17 | S (snippet only) |
| Heterogeneity is large | 95% prediction interval -0.22 to 0.40 (Tipton) or -0.08 to 0.35 (Burnette); tau2+omega2 = 0.16 | b10, b25 | E |
| Scale-up shrinks effects | Opower: 2% in 17 field experiments (~600,000 households) versus much smaller at ~8 million | a16 | E (analogy) |
| Error-monitoring mechanism failed | Moser 2011 replication N=89. Interaction wrong direction F(1,87)=4.19, p=.044 (uncorrected), F=2.51, p=.117 corrected. Mindset vs post-error accuracy r=.04 | a17 | S |
| Independent RCT null | EEF Changing Mindsets: 101 schools, 5,018 pupils. Maths -0.01 [-0.04, 0.01]; reading -0.00; grammar -0.00; 0 months' progress | d13 | E |
| Blackwell Study 1 not reproduced | Li and Bates 2020, n=832. Study 1 beta -0.02 [-0.16, 0.12]; Study 2 beta -0.05 [-0.14, 0.05]; earlier null studies N=222, 212; Chinese 5th-6th graders N=433; Czech applicants N=5,653 null | d12, a10 | E |
| Praise study replication partial | China, N=103: ability praise hurt (improvement -0.92 vs effort and -1.02 no praise; F(2,100)=7.17) but effort praise raised test anxiety versus no praise. Table inconsistencies noted | d10 | S |
| Extrinsic rewards lower intrinsic motivation | 128 studies. Free-choice d: engagement -0.40, completion -0.36, performance -0.28; positive feedback +0.33 | a18 | S (abstract only) |
| EmotionPrompt original claim | 6 models, 45 tasks, +8.00% relative on Instruction Induction, +115% on BIG-Bench; human study N=106, +10.9%. GPT-4 zero-shot average 78.96 vs 80.75 baseline | a20, c01, a21 | C |
| EmotionPrompt does not hold on 2026 models | 28,000 trials, 5 models, neutral 88.9%. Positive minus negative +0.04 pp [-0.34, +0.42]; both 1.3-1.4 pp below neutral, Holm p about .06; original claim rests on 13-20 items | d05 | E for "no gain", workshop abstract only |
| Six-benchmark emotion test | Small changes; GSM8K 92-95% band for most pairs; human and LLM prefixes alike | d04 | S |
| Negative emotion prompts also lift | +12.89% Instruction Induction, +46.25% BIG-Bench (same group) | b19, c04 | E that valence does not matter (with d05) |
| Tips and threats: no aggregate effect | GPQA N=4,950, MMLU-Pro N=2,500, 5 models incl. o4-mini, 25 trials per question. Per-question swings +36 and -35 pp. Only 5 GPQA and 10 MMLU-Pro comparisons differ, uncorrected | b22, d01 | E |
| Personas give no reliable gain | 162 roles, 4 families, 2,410 MMLU questions; automatic best-persona choice near random. Report 4: 6 models, no consistent expert gain, low-knowledge personas hurt | c06, d03 | E |
| Politeness depends on model | GPT-3.5 level 1: 51.93 vs 57-60; Llama2-70B 28.44 vs 49-55; GPT-4 stable 73.9-79.1; GPT-4o 50 questions x 5 tones: rude 84.8% vs polite 80.8% | a19, c05, b21 | C |
| Optimised wording matters but is model-specific | PaLM 2-L GSM8K: "Take a deep breath and work on this problem step-by-step" 80.2; "Let's think step by step" 71.8; no instruction 34.0 | a22, c07 | S |
| Trust framing in an agent | Claude Sonnet 4, 9 scenarios: 51 vs 32 hidden issues (+59%), d=2.28, p=.002. Study 2: +74% steps (p=.008), +25% hidden issues (p=.016); fear framing no gain (p>.3) | c09 | S |
| Intrinsic self-correction fails | GPT-4 GSM8K 95.5 to 89.0; GPT-3.5 CommonSenseQA 75.8 to 41.8; oracle labels 97.5 | c11 | E |
| Verbal lesson plus retry with signal works | Reflexion HumanEval 91 vs 80; ALFWorld 130 of 134; +22 pp over 12 trials | c10 | E (needs signal) |
| Step scaffold raises mean, lowers reliability | GPQA Diamond: non-reasoning RD 0.044-0.135, but all-25-correct RD down to -0.172; reasoning models about +0.03 or -0.033 | d02 | S |
| Positive thinking system message (older models) | 60 snippets, 3 models, GSM8K subsets of 10-100; not generalising; Llama2-70B best with none | d07 | S |
| LLM-rewritten supportive teacher language | 174 teachers, 1,006 raters; model beat expert by 8-10% perceived growth mindset, 23% more challenge-seeking choice | c08 | S (perceptions only) |
| Unguarded AI harms later learning | GPT Base students about -17% vs control after access removed (snippet). Structured tutor: 0.63 SD, N=194 | c20, b23 | E (Bastani snippet only) |
| Curiosity helps artificial agents (training time) | Voyager random curriculum -93% items; CDE +2.4 average (48.2 to 50.6) on Qwen3-4B-Base RLVR | c15, d15 | E for exploration design |
| Trait mindset of an LLM not measured | Negative search, about 25 candidates | c24 | S |

## 4. Mechanisms and models

These are the mechanisms the theory proposes, written so they can be coded, plus what the data says about each.

**M1. Belief to goal to strategy to outcome chain (Dweck).**
```
belief(ability malleable?) -> goal(learning vs performance) -> reaction to failure(persist / withdraw)
   -> strategy(new strategy / repeat / avoid) -> practice volume -> outcome
```
Evidence: correlations in the chain are r about .15-.24 (a13). The first link changes strongly (d=0.33-0.37) but the last moves little (d=0.05-0.11). The chain is leaky. Engineer's reading: a prompt that changes stated belief is not a manipulation of behaviour. Measure behaviour (retries, revisions, checks passed).

**M2. Mindset x context (affordance model).**
```
effect = f(belief_change, affordance)
affordance = challenge-seeking norm + teacher practice + flexible track + chance to act
```
Evidence: NSLM norm moderation B=0.11 (b03); teacher CATE .11 vs -.02 (b04); Norway tracks (a27). The reverse teacher direction (d17, snippet) and the small Chile effect (d14) show this is not settled. Engineer's reading: a belief-style instruction should be tested with and without an environment that rewards revision (verifier feedback, retry allowed).

**M3. Targeted subgroup (low achiever or ego-threat).**
Effect concentrates where people are struggling (a01: 0.10 vs 0.01; a13: effects stronger under ego threat). Engineer's reading: any such prompt should be tested only on items the agent finds hard, and compared against the same items without the prompt.

**M4. Praise and attribution.**
Praise for ability links success to a fixed trait, raising performance-goal choice (67% vs 8%) and misreporting (38% vs 13%) in children (d09). Agent analog: none identified. A language model does not carry a self-concept across calls. The only transfer is a coding rule: feedback should name the process and the failing output, not the model's "ability" (this is already G2).

**M5. Over-justification and self-determination.**
Contingent tangible rewards lower later free-choice interest (d about -0.3 to -0.4); verbal positive feedback raises it (+0.33) (a18). Agent analog: a loop that optimises a bare score may stop doing what it is not rewarded for. The practical coding rule is to keep verbal critique tied to evidence and not to use bare score gating alone. Not tested on LLMs.

**M6. Error monitoring (Moser 2011).**
Proposed neural link between growth beliefs and attention to errors. Failed to replicate (a17, N=89, r=.04). Do not build on it.

**M7. Emotional stimulus as extra attention (EmotionPrompt).**
Claimed mechanism: emotional text raises salience or "motivation" in the model. Tested alternative: any added sentence perturbs the prompt (a prompt-sensitivity effect). The 2026 test (d05) finds positive equals negative, and both are slightly below neutral. So the supported reading is perturbation, not motivation. Engineer's reading: treat any extra sentence as a random prompt variable; the mean effect is zero and the per-item variance is large (item ICC 0.51; swings of +36/-35 pp per question in b22).

**M8. Verbal reinforcement with a signal (Reflexion).**
```
attempt -> external check (tests / env reward) -> write 1-line lesson -> store in memory -> next attempt reads lessons
```
Works only with a usable success signal (c10, c11, d08). The memory, not an attitude, does the work. This is the one "learning from mistakes" mechanism with agent evidence, and it is already S5 plus S9.

**M9. Trust versus fear framing (Wuji 2026).**
Treatment framed as safety and trust (a self-determination-theory idea) increased exploration depth in a coding agent; fear framing did nothing. Possible mechanism: the framing licenses extra checking. Alternative: the trust prompt simply contained extra task instructions (bundled treatment). Single author, one model, 9 scenarios (c09). Candidate test only.

**M10. Learnability and interestingness selectors (OMNI, Motif, Voyager).**
```
candidate tasks -> LLM scores learnability + interestingness -> pick next -> train / act
```
Helps in games and training (c12, c13, c15, d15). Not tested as an inference-time branch selector in a reasoning agent (d16 unopened).

## 5. What holds up

**Holds up (established).**
1. Small positive correlations between growth beliefs and achievement across large samples (r about .10 to .34, K01). Correlational.
2. The targeted belief changes strongly under the intervention (d=0.33-0.37) while outcomes barely move (K06).
3. Effects are heterogeneous, with prediction intervals that cross zero (K05).
4. Independent tests are null or weak: EEF RCT (zero months, d13), Li and Bates near-replications (d12), the Moser error-monitoring failure (a17), and partial support for praise (d10) (K07, K08).
5. Intrinsic LLM self-correction does not help; Reflexion needs a signal (K17).
6. Tips, threats, personas and emotion wording do not give a reliable gain on current models (K12, K14, K10, K11).

**Contested.**
- Average student effect. Sceptics: d=0.05, non-significant after bias correction, 0.02 in the highest-quality subset (a14). Proponents: 0.09 SD, 0.05 after corrections still p=.004 (b10). The Tipton group says the "highest-quality" subset came from miscoded studies and that the Egger test fired where no real publication bias exists, which weakens the sceptics' bias-correction line. Macnamara reports larger effects when authors had financial interests. Both teams are invested, and almost all evidence comes from these two teams.
- Emotional prompting: gains on older models, flat or negative on 2026 models.
- Politeness: rude hurts older models, but helps GPT-4o in one tiny study (50 questions).

**Moderators that reappear.**
- Achievement level: lower achievers gain (0.10 vs 0.01; at-risk 0.15 SD).
- Context: peer norms and teacher mindset (single dataset; reverse direction suggested elsewhere).
- Model strength: stronger models show less sensitivity to wording (GPT-4 stable under politeness; gain shrinks with model strength in EmotionPrompt, a20).
- Task type: effects largest on social tasks and some BIG-Bench Hard items (d04).

**Interventions that worked.**
- NSLM online course for lower achievers (+0.10 GPA, proponent-run).
- Structured AI tutoring (0.63 SD, N=194), but many features bundled, so mindset messaging is not isolated (b23, b24).
- Reflexion with a verifier.
- LLM-generated supportive teacher language (perceived quality only).

**Interventions that did not work.**
- Teacher-led programme at scale (EEF, 0 months).
- Intrinsic self-correction.
- Tips, threats, personas, politeness, emotion lines on current models.
- Fear framing in an agent.
- Unguarded AI help (worse after removal, c20 snippet).

**Weak spots.**
- Several human facts have only abstract-level support: Sisk numbers, Macnamara numbers (a14 opened as abstract), Blackwell Study 2 slopes, Deci meta-analysis details, Bastani 2025, Li and Bates 2019 JEP:General.
- Yeager 2019 figures come from one PMC page read three times (a01, b01, c16 are one source).
- c17 is mislabelled "Burnette et al. (2023)" but carries Macnamara and Burgoyne numbers; treat as the same source as a14 and b09. a15, b10, b25 are one commentary. c18 DOI is wrong; the Sisk paper is 10.1177/0956797617739704.

## 6. Language models

No study measured growth mindset as a stable trait of an LLM (c24). All LLM work here is prompt-wording tests, or training-time or human-side uses.

**Emotion and encouragement.**
- EmotionPrompt (c01, a20): 45 tasks, 6 models (Flan-T5-Large, Vicuna, Llama 2, BLOOM, ChatGPT, GPT-4). Relative gain 8.00% (Instruction Induction), 115% (BIG-Bench, low baselines). Relative gain shrinks with model strength: GPT-4 0.85, ChatGPT 4.32, Vicuna 9.58, Flan-T5 0.28 (as listed). GPT-4 zero-shot average was 78.96 versus 80.75 baseline. Human study N=106 raters (+10.9%), judging GPT-4 only.
- Negative prompts raised scores too: +12.89% and +46.25% (b19). The groups overlap.
- 2026 pre-specified test (d05): five frontier models, 28,000 trials, neutral 88.9%. Positive and negative are equal (+0.04 pp) and both 1.3-1.4 pp below neutral (Holm p about .06). The authors say the original claim rests on 13-20 items. This is a workshop abstract; models are unnamed.
- Zhao 2026 (d04): GSM8K, OpenBookQA, SocialIQA, MedQA-US, BoolQ, BIG-Bench Hard on Qwen3-14B, Llama-3.3-70B, DeepSeek-V3.2 and GPT-OSS. Small changes; stronger wording adds little. Largest on social tasks.
- Bernays 2026 (d06): with human participants using GPT-4, praise improved rated answers more than neutral; blaming did not. Subjective ratings on writing and ethics tasks; directions only.
- Anand blog (d18, snippet): fear and praise below normal wording on arithmetic; emotion hurt Gemini 2.5 reasoning models. Not peer reviewed.

**Tips and threats.** Prompting Science Reports 3 (b22, d01): five models, GPQA N=4,950, MMLU-Pro N=2,500; no aggregate effect; per-question swings +36 and -35 pp. Wording changes individual items but not the mean. Policy: only claim an effect if it beats a control on held-out items with per-item variance.

**Personas.** Zheng 2024 (c06): 162 roles, 2,410 MMLU questions, no reliable effect, automatic best-persona choice near random. Report 4 (d03): six models including o3-mini and o4-mini; no consistent expert gain; layperson, child and toddler personas usually hurt.

**Politeness.** Yin 2024 (a19, c05): rudest prompts hurt GPT-3.5 (51.93 vs 57-60) and Llama2-70B (28.44 vs 49-55), not GPT-4. Dobariya and Kumar 2025 (b21): GPT-4o rude 84.8% vs polite 80.8%, 50 questions, single run each; a 4-point gap is about 2 questions.

**Wording found by search.** OPRO (a22, c07): "Take a deep breath..." 80.2 vs 71.8 vs 34.0 on GSM8K with PaLM 2-L, tuned on a training split. Model-specific. Battle and Gollapudi (d07): 60 positive-thinking snippets, three old models, GSM8K subsets of 10-100 items; helped inconsistently; Llama2-70B without CoT was best with no system message. 26 principles paper (a23, c22): principle 10 is a tip; set-level GPT-4 gains (+57.7% quality, +36.4% correctness) are not isolated to the tip.

**Reasoning scaffolds and reliability (d02).** A step-by-step prompt raised mean accuracy for non-reasoning models (RD 0.135 Gemini Flash 2.0, 0.117 Sonnet 3.5, 0.044 GPT-4o-mini p=.067) but lowered all-25-correct rate for some (RD -0.131, -0.172). For reasoning models the gain was about 0.03 (o3-mini 0.029, o4-mini 0.031) or negative (Flash 2.5 -0.033; all-correct -0.131). Time costs 20-80% more. A scaffold can raise mean and lower reliability.

**Self-correction (c11, c10, d08).** Without external feedback, GPT-4 GSM8K 95.5 to 89.0, GPT-3.5 CommonSenseQA 75.8 to 41.8. GPT-3.5 changed right to wrong more than wrong to right. Oracle labels: 97.5. Kamoi 2024 survey: positive results use oracle or unfair settings. Reflexion: HumanEval 91 vs 80, ALFWorld 130 of 134, but not WebShop.

**Trust framing in agents (c09).** Claude Sonnet 4; nine real debugging scenarios. Trust framing: 51 vs 32 hidden issues, 42 vs 23 steps, beyond-task action 100% vs 22%, self-corrections 6 vs 0, d=2.28, p=.002. Study 2 (5 runs x 3 conditions): +74% steps, +25% hidden issues; fear no gain. Single author, designed scenarios and treatment, no inter-rater check, bundled treatment.

**LLMs in education (human side).**
- Handa 2023 (c08): GPT-4 growth-mindset-supportive rewrites of 100 unsupportive teacher utterances (22.8% of relevant utterances were unsupportive). Beat expert rewrites by 8-10% on perceived growth mindset, 9-15% lower shame, 23% more challenge-seeking choice. Perceptions only.
- Kestin 2025 (b23): structured AI tutor beat in-class active learning, 0.63 SD, N=194, median 4.5 vs 3.5.
- Bastani 2025 (c20, snippet): unguarded GPT access, about -17% versus controls after removal.
- Pan 2026 (c19): 39 empirical studies on generative AI and student motivation, 34 of 39 in higher education, no effect sizes.
- Kim 2024 (c21, snippet): growth-mindset-style chatbot found more comfortable and engaging.

**Agent exploration.** OMNI (c12), Motif (c13, NetHack: reward-only agent scored higher than one trained on the game score), Du 2023 (c14), Voyager (c15: 3.3x items, 2.3x distance, random curriculum -93%), CDE (d15: +2.4 average, +3 on AIME). All exploration design or training; none an inference-time selector.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| N1 | **Do not add motivational wording** (emotion, tips, threats, politeness, persona, praise) as a schema element. Fix one neutral tone. Matches SCHEMA section 4b on personas | none (4b list) | [E] | b22, d01, d03, c06, d05, K10-K14 |
| N2 | **Revise only on a real signal.** Retry or "you can improve" prompts do not help without a verifier; keep Reflexion-style lessons tied to failing output | G1, G2, S5, S9 | [E] | c10, c11, d08, K17 |
| N3 | **Measure behaviour, not stated belief.** A prompt that changes self-description is not evidence of a change; score checks passed, retries, revisions | G7, G10 | [E] | a02, K06 |
| N4 | **Report per-item variance and the reliability metric** (all-trials-correct, not only mean) for any prompt change; a scaffold can lift the mean and lower reliability | G7, G12 | [E] for variance (b22, K05), [S] for the reliability pattern (d02) | b22, d02, K05, K23 |
| N5 | **Tune any wording per model on dev data**, never carry it across models | G7 | [E] practical rule, evidence [S] | a22, c07, d07, K15 |
| N6 | **Treat the mean effect prior as about 0.1 SD at best**, concentrated on hard items; expect no gain on easy items | G7, G12 | [E] for heterogeneity, [C] for size | b10, a14, a01, K02, K05 |

Most items here are "do not" rules. They add no new schema element; they add guard text to what the schema already says (G1, G2, G7).

### Test first (not established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | **Growth-style retry framing** ("ability is malleable, mistakes are informative") versus length-matched neutral at equal tokens; the decisive missing test | S5, S9 | [S]/open | d07, c24, K21 |
| T2 | **Encouragement x verifier 2x2** (verifier on/off, encouragement/neutral/none) | G2, S5 | [S] | c11, d08, K24 |
| T3 | **Trust versus fear framing** in a multi-step agent, replicated with 50+ scenarios, 3 models | G1, S6 | [S] | c09, K16 |
| T4 | **Curiosity or learning-progress branch selector** versus random at S6 | O/S6, M | [E] for training, untested for inference | c12, c15, d15, K20 |
| T5 | **Scaffold removal test** (Bastani-style): does a scaffold that raises in-loop score lower performance when removed or on the next problem class? | G7, S9 | [S] | c20, d02, K19, K23 |
| T6 | **Hard-items-only prompt use** (subgroup effect) | S0, G12 | [S] | a01, K03 |
| T7 | **Context moderation:** belief-style prompt with and without a revision-rewarding environment | S5 | [S]/[C] | b03, b04, d14, d17, K04 |
| T8 | **Verbal feedback framing**: verbal critique with evidence versus bare score in the loop (over-justification analog) | S5 | [S] | a18, K09 |

## 8. Concrete tests on our bench

All arms get the same token budget. Report the mean, the all-seeds-correct rate and per-item variance. Use at least 3 models (include one reasoning model) and at least 5 seeds. Items are drawn from the bench's reasoning and ARC-style items with a checker, split into dev (tune wording) and held-out (report).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 growth framing | Held-out checkable reasoning items (GPQA-style, BrainTeaser, ARC); retry after a failed first answer | (a) growth-mindset retry text; (b) neutral text of the same length; (c) no text | Accuracy after retry; all-seeds-correct rate | About 0 (prior from d05, d01, d07: no gain, maybe -1 pp). Add only if (a) beats (b) by 2 pp or more on a paired test |
| T2 verifier x encouragement | Same items; verifier = code check where available | verifier on/off x (encouragement / length-matched neutral / none) | Accuracy gain over single shot; revision right-to-wrong rate | Verifier on: gain whatever the text. Verifier off: flat or negative (c11). Interaction near 0 |
| T3 trust vs fear | Multi-step debugging items with planted hidden issues (50+) | trust-framed; fear-framed; length-matched neutral; none | Hidden issues found per scenario; steps; false-positive rate | Trust gains of +25% if c09 holds; likely smaller. Add only if trust beats neutral by 10% with CI above 0 on 3 models |
| T4 curiosity selector | Long-horizon tasks at S6 (branch choice) | LLM "learnability and interest" ranking; random; code-score (G5) ranking | Solved rate at fixed budget; distinct branches opened | Small gain over random; unlikely to beat code scoring. Add only if beats random by 5 pp and equals code score |
| T5 scaffold removal | Train-then-test: run the scaffolded agent on class A, then plain model on class B using lessons; compare to a never-scaffolded control | scaffold on during practice, off at test; never on; on at test | Plain-model accuracy on class B | Gain near 0. A drop of 3 pp or more signals dependency |
| T6 hard-items subset | Items bucketed by the plain model's pass rate (S0 stats) | prompt on hard bucket only; on all; none | Accuracy per bucket | Effect only on hard bucket if real; none on easy |
| T7 context | Same items with and without a revision-rewarding loop | belief-text x loop on/off | Accuracy | Text effect appears only in loop-on if mindset x context transfers; expect none |
| T8 critique framing | Revision loop on checkable items | verbal evidence-based critique; bare pass/fail score; verbal critique plus neutral praise | Final accuracy; revision quality | Verbal evidence critique beats bare score by a small margin (G2 already assumes this) |
| Control for all | Any extra sentence | positive, negative, length-matched neutral sentence on one model set | Accuracy | All equal (d05); this separates psychology from perturbation |

## 9. What does not transfer, and why

- **No trait.** A mindset is a stable belief a person carries across months. An LLM call has none; the belief must be restated in every context. Prompting "you have a growth mindset" is a role statement, which the persona results show is unreliable (K14).
- **No failure history.** The theory works through accumulated failures and the meaning students assign to them. Our agent has a fresh context per attempt (S3). The nearest analog is the stored lesson line (S9).
- **No affect, no anxiety, no ego threat.** Moderators (ego threat, test anxiety, shame) have no counterpart in a model. Praise and shame attribution (M4) therefore does not map.
- **No intrinsic motivation or reward value.** Over-justification (a18) needs a self-motivated organism. Analog only in loop design (K09).
- **Social setting.** Peer norms, teacher mindset and school track (M2) are social affordances, not prompt text.
- **Belief change versus behaviour.** Even in humans the belief moved at d=0.33 while grades moved d=0.11 (K06). In LLMs the stated belief is cheap to change and does not need to touch computation.
- **Small, heterogeneous effects.** A mean of about 0.05-0.11 SD would sit inside prompt noise (per-question swings of +36 and -35 pp in b22).
- **Gains shrink with model strength.** Stronger and reasoning models are less sensitive to wording (a19, a20, d01, d03).
- **Perception is not outcome.** The LLM-rewrite teacher study (c08) measures ratings, not learning.
- **Exploration and curiosity results are training-time.** They do not show a benefit at inference time (d15, d16).

## 10. Open questions

1. Does any growth-style prompt beat a length-matched neutral at equal tokens on a reasoning benchmark across 3+ models and 5+ seeds? No study found (gap 1, T1).
2. Is the effect of an encouragement retry dependent on a verifier? No direct 2x2 (gap 2, T2).
3. Do tips, threats and personas hold on Claude thinking models? Report 3 and 4 had no Claude model (d01, d03).
4. Is the EmotionPrompt gain just any salient sentence? Partly closed by d05 but the workshop abstract does not name models or the benchmarks, and the neutral-length control is exploratory.
5. Can an independent group replicate Wuji's trust versus fear result with more than 9 scenarios (c09)?
6. Does a scaffold-removal harm exist for agents (gap 8)? Only a mean-versus-reliability pattern (d02).
7. Do curiosity or learning-progress signals work as branch selectors at inference time (d16 unopened)?
8. What are Blackwell Study 2 slopes and effect sizes (paywalled; d11 abstract only)? Li and Bates 2019 JEP:General, Yeager 2019 raw figures, Bastani 2025 and Kim 2024 numbers remain unread.
9. Does teacher-mindset moderation hold outside the Yeager dataset? Mixed: Chile (+0.02 SD) and a reverse-direction trial (snippet).
10. How large is the true average human effect? The sceptic and proponent estimates (0.05 versus 0.09, or 0.02 versus 0.05) cannot be settled by a third reader without new independent trials.

## 11. Sources

[V] opened (page or PDF text read); [M] snippet or abstract only, or from memory.

Human mindset and motivation
- [V] Yeager et al. (2019) national experiment, NSLM (a01, a02, a03, a04, b01-b03, c16): https://pmc.ncbi.nlm.nih.gov/articles/PMC6786290/
- [V] Dweck and Yeager (2019) Mindsets: a view from two eras (a07, a08): https://pmc.ncbi.nlm.nih.gov/articles/PMC6594552/
- [V] Hecht, Yeager and Dweck (2021) Beliefs, affordances, and adolescent development (a09, a27): https://pmc.ncbi.nlm.nih.gov/articles/PMC8903074/
- [V] Yeager, Dweck et al. (2021) What can be learned from growth mindset controversies? (a10, a11): https://pmc.ncbi.nlm.nih.gov/articles/PMC8299535/
- [V] Yeager et al. (2022) Teacher mindsets (b04, b05): https://pmc.ncbi.nlm.nih.gov/articles/PMC8985222/
- [V] Sisk et al. (2018) two meta-analyses, abstract and table (a12, b06-b08): https://pubmed.ncbi.nlm.nih.gov/29505339/ and https://englelab.gatech.edu/articles/2018/
- [V] Burnette et al. (2013) meta-analysis (a13): https://pubmed.ncbi.nlm.nih.gov/22866678/
- [V, abstract only] Macnamara and Burgoyne (2023) (a14): https://pubmed.ncbi.nlm.nih.gov/36326645/ ; [M] b09: https://doi.org/10.1037/bul0000352
- [V] Tipton et al. (2023) commentary, includes Burnette 2023 re-analysis (a15, b10, b11, b25): https://pmc.ncbi.nlm.nih.gov/articles/PMC10495100/
- [V] Bryan, Tipton and Yeager (2021) (a16): https://pmc.ncbi.nlm.nih.gov/articles/PMC8928154/
- [V] Moser 2011 replication (a17): https://pmc.ncbi.nlm.nih.gov/articles/PMC8318296/
- [V, abstract] Deci, Koestner and Ryan (1999) (a18): https://pubmed.ncbi.nlm.nih.gov/10589297/
- [V] Mueller and Dweck (1998) (d09): https://www.columbia.edu/cu/psychology/courses/3615/Readings/Mueller_Dweck.pdf ; [M] a06, b15
- [V, abstract] Blackwell, Trzesniewski and Dweck (2007) (d11): https://pubmed.ncbi.nlm.nih.gov/17328703/ ; [M] a05, b16, c23
- [V] Li and Bates (2020) (d12): https://www.gwern.net/doc/psychology/2020-li.pdf ; [M] Li and Bates 2019 (b12): https://osf.io/
- [V] Foliano et al. (2019) EEF Changing Mindsets (d13): https://discovery.ucl.ac.uk/id/eprint/10118795/11/ ; [M] b13
- [V] Zhao et al. (2018) China praise replication (d10): https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01883/full
- [V] Claro et al. (2021) Chile census (d14): https://www.edworkingpapers.com/sites/default/files/ai21-402.pdf
- [M] Teacher-delivered trial, Psychological Science (d17): https://www.psychologicalscience.org/journals/psychological-science/
- [M] Bahnik and Vranka (2017) (b14): https://doi.org/10.1016/j.paid.2017.03.040
- [M] Dweck and Leggett (1988) (a24): https://doi.org/10.1037/0033-295X.95.2.256 ; Ryan and Deci (2000) (a25): https://doi.org/10.1037/0003-066X.55.1.68 ; Bandura (1977) (a26): https://doi.org/10.1037/0033-295X.84.2.191

LLM and AI
- [V] Li et al. (2023) EmotionPrompt (a20, a21, b17, b18, c01, c02): https://arxiv.org/abs/2307.11760
- [V] Wang et al. (2023/2024) EmotionAttack (c03): https://arxiv.org/abs/2312.11111
- [V] Wang (2024) NegativePrompt (b19, c04): https://arxiv.org/abs/2405.02814
- [V] Yin et al. (2024) politeness (a19, b20, c05): https://arxiv.org/abs/2402.14531
- [V] Dobariya and Kumar (2025) (b21): https://arxiv.org/abs/2510.04950
- [V] Meincke et al. (2025) Prompting Science Report 3 (b22, d01): https://arxiv.org/abs/2508.00614
- [V] Meincke et al. (2025) Prompting Science Report 2 (d02): https://arxiv.org/abs/2506.07142
- [V] Basil et al. (2025) Prompting Science Report 4 (d03): https://arxiv.org/abs/2512.05858
- [V] Zhao et al. (2026) emotional framing (d04): https://arxiv.org/abs/2604.02236
- [V, abstract page] Joshi et al. (2026) Sticks and Stones (d05): https://icml.cc/virtual/2026/79999
- [V] Bernays et al. (2026) (d06): https://arxiv.org/abs/2601.05104
- [V] Battle and Gollapudi (2024) (d07): https://arxiv.org/abs/2402.10949
- [V] Kamoi et al. (2024) (d08): https://arxiv.org/abs/2406.01297
- [V] Zheng et al. (2024) personas (c06): https://arxiv.org/abs/2311.10054
- [V] Yang et al. (2023) OPRO (a22, c07): https://arxiv.org/abs/2309.03409
- [V] Bsharat et al. (2023) 26 principles (a23, c22): https://arxiv.org/abs/2312.16171
- [V] Wuji (2026) Trust over fear (c09): https://arxiv.org/abs/2603.14373
- [V] Shinn et al. (2023) Reflexion (c10): https://arxiv.org/abs/2303.11366
- [V] Huang et al. (2024) self-correction (c11): https://arxiv.org/abs/2310.01798
- [V] Zhang et al. (2023) OMNI (c12): https://arxiv.org/abs/2306.01711
- [V] Klissarov et al. (2023) Motif (c13): https://arxiv.org/abs/2310.00166
- [V] Du et al. (2023) ELLM (c14): https://arxiv.org/abs/2302.06692
- [V] Wang et al. (2023) Voyager (c15): https://arxiv.org/abs/2305.16291
- [V] Dai et al. (2025) CDE (d15): https://arxiv.org/abs/2509.09675
- [M] Search summary on curiosity selectors (d16): https://arxiv.org/pdf/2504.03380
- [V] Handa et al. (2023) Mistakes Help Us Grow (c08, c24): https://arxiv.org/abs/2310.10637
- [V] Kestin et al. (2025) AI tutoring RCT (b23, b24): https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/
- [V] Pan, Abuhassna and Jiang (2026) (c19): https://pmc.ncbi.nlm.nih.gov/articles/PMC13751964/
- [M] Bastani et al. (2025) (c20): https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Generat
- [M] Kim et al. (2024) (c21): https://www.media.mit.edu/publications/exploring-llm-based-chatbot-for-language-
- [M] Anand (2026) blog (d18): https://www.s-anand.net/blog/emotion-prompts-dont-help-reasoning-does/
- [M] Burnette 2023 (c17, mislabelled; same as a14): https://www.ebi.ac.uk/europepmc/webservices/rest/search
- [M] Sisk 2018 mis-DOI'd entry (c18): correct DOI 10.1177/0956797617739704

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 9 established claims: 5 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A05.10-K01** (number corrected). Sisk (k=273, r=.10) and PISA 72 of 74 match, but in Yeager et al. only r=.24 (three studies, N=23,446) is with grades; r=.27-.28 (California CORE) and .34 (Chile) are with test scores, so 'r .24-.34 with grades' is mislabelled; PISA is also test scores. Corrected claim: Mindset-achievement correlations are small but positive and recur across large samples (r about .10 in the Sisk meta-analysis of 273 effects; r=.24 with high-school grades in three large studies, N=23,446, and r=.27 to .34 with test scores in California CORE and Chile datasets reported by proponents; PISA 2018 test scores positive in 72 of 74 nations). Correlational, so causation is not shown.
- **A05.10-K05** (now single-source: the sources are not independent). Numbers match (prediction intervals -0.22 to 0.40 and -0.08 to 0.35; Opower 17 experiments, 600,000 then 8 million households), but both intervals come from the single Tipton et al. 2023 paper (listed four times; Burnette's interval is quoted inside it), and the second source, Bryan, Tipton and Yeager 2021, is by overlapping authors from the same heterogeneity-advocacy group.
- **A05.10-K06** (now single-source: the sources are not independent). d=0.33 and d=0.37 are both manipulation checks in the same National Study of Learning Mindsets by the same lab (not two experiments); also d=0.33 is small-to-moderate rather than 'strong', and the 'weak coupling' reading is an inference (grades rose 0.10 points for lower achievers, 0.11 SD in growth-mindset teachers' classes).
- **A05.10-K11** (reworded: the sources support less). NegativePrompt numbers (12.89%, 46.25%, 45 tasks, 5 models) and the +0.04 pp [-0.34, +0.42] result match, but the same 2026 poster found both emotional framings 1.3-1.4 pp below neutral (Holm p about .06), which cuts against 'any salient addition lifts scores', and 'valence does not matter on current models' generalises one unreviewed workshop poster on five unnamed models and four reasoning benchmarks. Corrected claim: Negative-emotion prompts also raised scores in NegativePrompt (+12.89% relative on Instruction Induction, +46.25% on BIG-Bench; older models), which hints that the lift may come from any salient addition rather than psychology-specific content (inference, not tested). A 2026 workshop poster (five unnamed frontier models, four reasoning benchmarks, 28,000 trials) found positive minus negative framing +0.04 pp (CI -0.34 to +0.42) and both framings slightly below neutral (-1.3 to -1.4 pp, not significant after Holm correction), so valence made no detectable difference there and the lift does not carry over to those models.
- **A05.10-K12** (now single-source: only one opened source, code check).
- **A05.10-K19** (now single-source: only one opened source, code check).
