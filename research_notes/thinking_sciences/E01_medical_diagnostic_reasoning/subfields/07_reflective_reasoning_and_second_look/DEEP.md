# Reflective reasoning and second look: deep document

*Subfield E01.07. Sources: evidence_a-d.jsonl (a01-a37, b01-b38, c01-c26, d01-d27), claims.jsonl (K01-K30), critique.md, all in this folder. Schema references are to `research_notes/single_agent/SCHEMA.md` v0.2. Search note: WebSearch quota ran out during gap search; coverage of 2025-2026 LLM work is narrower than usual, so "not found" means not found, not proven absent.*

---

## 1. What it is

A second look is a deliberate pass over a diagnosis or answer the person already holds. The first answer exists. The second pass tries to confirm it, break it, or replace it.

The best-known human form is **deliberate reflection (DR)**, from Mamede and Schmidt (Rotterdam, Brazil). It is a fixed written procedure (a02):

1. State the first hypothesis.
2. List findings that support it.
3. List findings that speak against it.
4. List findings that should be present but are absent.
5. Name an alternative hypothesis in case the first is wrong. Repeat steps 2 to 4 for it.
6. Rank all hypotheses. Choose.

The alternatives must come one at a time out of the evidence (bottom-up), not from a pre-written differential. This is the authors' claim. It is not independently proven (K06, K29).

Related things that are **not** the same, and which the literature often mixes in:

- **Instructions at test**: "be slow, careful, analytic, avoid bias". No structure. Does not work (K03).
- **Cognitive forcing** training and bias checklists. Mostly null (K03).
- **Content checklists**: a list of possible diagnoses. Works only if the right answer is on it (K09).
- **Directed search before diagnosis** (list three diagnoses first). Mixed; Ilgen found nothing (K06).
- **Free self-directed second look**: the person decides what to recheck. Small gain (K04).
- **Delayed learning from reflection** while practising cases. A different effect: it is about memory, not about correcting a live answer (K10).

For our agent this subfield maps to **S5 REVISE** (fix after a failed test) and **S8 VERIFY** (final check on something the answer was not fitted to). Guardrails G1 (doubt only on a signal), G2 (revise only from real output) and G4/G10 (own samples and own reasoning text are not evidence) are the rules that govern it.

Short verdict, before the detail:

- In people, a structured second look adds a small average gain (g 0.20 to 0.38), mostly in vignettes, mostly from one lab network, and a plain second return to the case may give the same gain (Think Twice).
- In language models, an unstructured second look with no outside signal lowers accuracy on average. A second look works when something outside the model decides, or when the wording is neutral and the model rarely changes its mind.
- Nobody has tested the DR procedure against a plain second pass at equal tokens for an LLM. That is the top open gap (Gap 1).

---

## 2. History and theories in depth

### 2.1 Roots

- **Dewey**: reflection is careful consideration of a belief in the light of its grounds.
- **Schon**: reflection is triggered when routine "knowing-in-action" fails. The practitioner suspends judgement and examines the grounds of the first explanation. (a01)
- **Mamede and Schmidt 2004**: a questionnaire factor analysis of physicians gave five factors: deliberate induction, deliberate deduction, testing of predictions, openness to reflection, meta-reasoning. DR operationalises the first three. (a01)
- **Dual-process context**: the whole literature is framed as fast pattern recognition versus slow analysis (Lambe 2016 review, b04/d22). Reflection is the "System 2 check" on a "System 1" answer.

### 2.2 The founding studies (2008 to 2012)

- **Mamede, Schmidt, Penaforte 2008** (a03/b01): 42 residents, 16 cases. No main effect of reflection. Interaction of complexity by mode, F(1,41)=4.48, P<0.05: reflection helped on complex cases only.
- **Mamede et al. 2010, conscious thought** (a04/b25): 34 residents and 50 fourth-year students, 12 cases. Residents on complex cases did better with conscious deliberation than immediate decision (t(33)=2.86, p<0.008) or unconscious thought (t(33)=3.12, p<0.005). Initial 0.45 to final 0.58 after analysis (t(33)=3.00, p<0.01). Simple cases: no difference. Students: conscious thought was worse than immediate on complex cases (t(33)=2.08, p<0.05). Mode by expertise F(2,82)=3.35, p<0.04. Review summary calls this "more than 35 percent" gain (b38); 0.45 to 0.58 is 29 percent relative. The two figures are not reconciled (critique 3.4).
- **Mamede et al. 2010, availability bias, JAMA** (a05/b12): 36 residents (18 first-year, 18 second-year). Second-years scored 1.55 on look-alike cases versus 2.19 on others (P=.03). First-years showed the reverse. Reflection raised scores to 2.03 (second-year) and 2.31 (first-year), main effect P=.006. The reflection phase always came last on the same four cases, so a plain repeat effect is mixed in.
- **Mamede et al. 2012, salient distractors** (a07/b13): secondary analysis. Residents (n=34): reflective 2.09 versus non-analytic 1.71 (P=0.03); distractor-triggered errors 0.47 versus 0.85 (P=0.02). Students (n=50): no benefit.
- **Schmidt et al. 2014** (a06): 38 residents read a Wikipedia page on a disease. Six hours later look-alike cases were misdiagnosed as that disease (0.61 read versus 0.29 not read). Bias-expected cases 0.56 versus 0.70 (P=.016). After reflection accuracy was 0.71.

### 2.3 The learning branch (2012 to 2026)

Reflection while practising cases is a different effect from reflection while diagnosing. It hurts at once and helps a week later (a11/b20, a12/b21). See section 3.

### 2.4 The critics and the nulls

- **Ilgen 2013** (a18/b08): N=393, multicentre. A directed search (three diagnoses, then supporting and non-supporting features) did not beat first impression. F(1,379)=2.44, P=.12. The abstract also says first impressions gave more reliable assessment scores. Mamede and Schmidt 2014 (b09, not opened) answer that DR needs hypotheses to emerge from the evidence, but Ilgen asked for a competing list first.
- **Norman 2014** (a19/b05/d27): "be slow and careful" versus "be fast", N=204 residents, 20 cases. Accuracy 44.5% versus 45.0%. Time 69 s versus 89 s (P<.001). Wrong cases took 17 s longer. Cohorts from different years, so not randomised in one sitting.
- **Sherbino 2014** (a20/b17): cognitive forcing training, N=191. No effect on search satisficing or availability errors.
- **Monteiro 2015** (a36/b06): a free self-directed second look. Residents (N=47) revised 60 of 745 diagnoses (8%), score 1.20 to 1.22 of 2 (t=2.15, p=0.03). The title says it: "taking a second look is not enough".
- **Lambe 2018** (a35): N=186 senior students, short (2 alternatives) and long (6 alternatives) guided reflection versus first impression. Final diagnosis F(2,173)=0.841, not significant. The list of alternatives got more accurate (0.70 and 0.72 versus 0.47, eta2=0.18), which is partly a counting effect.
- **Think Twice 2020** (a17/b07): N=167 Swiss physicians on very hard cases. Overall 0.22 to 0.26 (P<.001). A plain return with no instruction gave about the same as confirm, contradict or both. No no-second-pass control.
- **Failed replication of a neighbouring effect**: deliberation-without-attention (a34), N=143, no difference between conscious and unconscious thought.

### 2.5 Where the field is now

- The mechanism candidates are (a26): fuller activation of prior disease knowledge; reprocessing the case under each new hypothesis; stronger disease-finding links that give better look-alike contrast. None tested directly. Ribeiro 2019: DR group recalled 40 percent more propositions of a 1200-word text, and the effect held under restricted time, so it is partly cognitive and not only motivation. Ribeiro 2021 replication (b36, N=101): recall 72.56 versus 58.80 (p=.01).
- The strongest independent line is **knowledge, not process** (K08): content of look-alike contrast beats a reasoning instruction. See 4.6.
- The field moved to cued, modelled and faded scaffolds (K11) and to testing for boundary conditions (case visible or hidden, a30).
- The LLM side arrived late and mostly tests generic self-correction, not DR.

---

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources agree), **S** single source, **C** contested. "Network" means Mamede/Schmidt network, so not counted as independent of each other.

### 3.1 Human studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Structured reflection helps on complex cases only (founding) | N=42; interaction F(1,41)=4.48, P<.05; no main effect | Mamede 2008 (a03, b01) | C (K02) |
| Residents gain from conscious analysis on complex cases; students do not | residents 0.45 to 0.58, t(33)=3.00; students worse on complex, t(33)=2.08 | Mamede 2010 Psych Res (a04, b25) | C |
| Family-practice residents gain on simple and complex alike | N=63; 0.60 to 0.68, P=0.002 | Schmidt 2017 (a08) | contradicts difficulty rule |
| Dermatology students: gain larger on easy cases | N=61; easy 76.8 vs 60.1 (p=0.004); hard 22.7 vs 16.7 (p=0.080) | Costa Filho 2019 (a10) | contradicts difficulty rule |
| Dermatology overall accuracy gain | 49.7 vs 38.4, t(59)=3.33, p=0.002, d=0.84 | Costa Filho 2019 (a09, b19) | S |
| Reflection does not change confidence or calibration | confidence 64.3 vs 58.9 (p=0.228); calibration 0.15 vs 0.20 (p=0.197); overconfidence rose with difficulty (p<0.001) | Costa Filho 2019 (b19) | E (K12) |
| Pooled effect of guided reflection | 44 studies, 4380 professionals, ES 0.38 (0.23-0.52) | Prakash 2019 (a23, b03) | E (K01) |
| Pooled effect of all workplace reasoning tools | 29 studies, N=2732; g=0.20 (0.10-0.29); I2 70 to 38% after dropping 3 training studies; no moderator explained gains | Staal 2022 (a24) | E (K01) |
| Reflection phases inside diagnostic-competence scaffolds | g=0.58 (SE 0.11) with vs 0.26 (SE 0.11) without; Q(1,31)=17.11 | Chernikova 2019 (a37) | S (not reopened) |
| Four kinds of second look give the same small gain on very hard cases | N=167; initial 0.22, final 0.26 (P<.001); return only 0.21 to 0.23; confirm 0.24 to 0.31; contradict 0.22 to 0.26; both 0.19 to 0.25; groups ns | Mamede 2020 Think Twice (a17, b07) | S (K05) |
| Directed search did not beat first impression | N=393; F(1,379)=2.44, P=.12 | Ilgen 2013 (a18, b08) | C (K06) |
| Guided reflection no better than first impression | N=186; F(2,173)=0.841 ns | Lambe 2018 (a35) | C |
| Free self-directed second look barely helps | N=47; revised 60/745 (8%); 1.20 to 1.22 of 2, p=0.03; revisers were weaker at pass 1 (0.64 vs 1.25, p<0.001) | Monteiro 2015 (a36, b06) | S (K04) |
| Revisions to correct are rare | 18% of incorrect diagnoses revised to correct; six correct ones fell about 0.8 after revision | Monteiro 2015 (a36) | S; full-text only, not in abstract |
| "Be slow and careful" does nothing | N=204; 44.5% vs 45.0% | Norman 2014 (a19, b05, d27) | E (K03) |
| Cognitive forcing training does nothing | N=191; 2nd dx found 54% vs 48% (p=.13); availability 45% both (p=.98) | Sherbino 2014 (a20, b17) | E (K03) |
| Faster answers were more accurate | N=75, 25 cases; r=-0.54 (response time vs accuracy) | Norman 2012 (b28) | S |
| Reflection counters availability bias | second-years 1.55 look-alike vs 2.19; reflection 2.03; N=36 | Mamede 2010 JAMA (a05, b12) | E (K07), repeat effect mixed in |
| Reflection counters media-exposure bias | N=38; 0.56 vs 0.70; after reflection 0.71 | Schmidt 2014 (a06) | S |
| Reflection counters salient distractors in residents only | 2.09 vs 1.71 (P=0.03); distractor errors 0.47 vs 0.85 | Mamede 2012 (a07, b13) | S |
| Look-alike contrast knowledge protects against bias | N=91; bias vignettes 0.40 vs 0.24 (diff 0.16, CI 0.05-0.27, p=0.004); non-bias 0.36 vs 0.41 | Mamede 2020 immunising (a15, b15) | E (K08) |
| Disease knowledge predicts bias susceptibility | N=62; biased diagnoses 0.35 (higher knowledge) vs 0.97 (lower), CI 0.28-0.95, p=0.001 | Mamede 2021 (b16) | E |
| Anchoring: knowledge protects, time and confidence do not | N=68; higher-knowledge group less anchored (p=0.02); time p=0.88, confidence p=0.96 between groups | Mamede 2024 (d24) | E (K08), same network |
| A checklist helps only if it holds the truth | N=90; 0.75 (list has answer) vs 0.49 control vs 0.43 (list lacks answer) | Kaemmer 2021 (b18) | E (K09) |
| Reflection while practising: worse now, better later | N=46; immediate 0.48 vs 0.62; one week 0.66 vs 0.48 and 0.52; interaction p=0.003 | Mamede 2012 (a11, b20) | E (K10) |
| Same effect replicated, with adjacent-disease transfer | N=110; new exemplars 0.67 vs 0.51 vs 0.36; adjacent 0.44 vs 0.33 and 0.32 | Mamede 2014 (a12, b21) | E (K10), same lab |
| Transfer did not replicate in novices | N=80; adjacent diseases near floor | Mamede 2019 (a14, b23) | negative |
| Cued or modelled reflection beats free reflection | N=115; both better than free, p<0.001; cued=modelled p=1.00 | Ibiapina 2014 (a13, b22) | E (K11) |
| Cued vs free in novices | N=80; 0.58 vs 0.41, p<0.02; modelled 0.54 | Mamede 2019 (a14) | E |
| Independent group replicates guidance benefit | N=80+62; cued = worked example, both beat free, p<.001; complex-case delayed benefit only in seniors | Fernandes 2021 (b24) | E, partly same network |
| Faded examples equal cued reflection in advanced students | 70 students (59 done); accuracy p=.99 | 2026 (a31) | S (expertise reversal) |
| Learning DR by teaching does not transfer | 56 GP residents; accuracy p=.263 | 2023 (a29) | S, null |
| Hide-case vs show-case during reflection | N=67; interaction chi2(1)=7.68, p=0.006; simple effects borderline and their CIs are inconsistent with the quoted ORs | 2026 Diagnosis (a30, b37) | S; treat only the interaction as reported |
| Independent site: checklist verification after own reading | 15 ECG experts; errors corrected per ECG 0.29 vs 0.03 (p<.01); net errors 0.39 vs 1.04 | Sibbald 2013 (d19) | S |
| Analytic re-read instruction helps; strategy-switch instruction does not | 24 residents; analytic F(1,188)=15 p<.0001; balancing F=0.22 p=0.64 | Sibbald 2012 (d20) | S |
| Alternatives supplied late = early | N=190; correct dx in differential +7% early, +8% late | Sibbald 2022 (d21) | S (K29) |
| Perceived difficulty triggers reflection by itself | 20 residents, 10 cases; accuracy higher when told others failed | Mamede 2008 (a32, b26) | S |
| Difficult-patient behaviour lowers accuracy | N=63; 0.54 vs 0.64, P=0.017 | Schmidt 2017 (a08) | S |
| Randomised listing of differentials and compatible findings before diagnosis | N=145; 3.40 vs 3.05, p=0.011 | Myung 2013 (a22) | S; not a second look (list first) |
| Dual instructions at test (similarity first, rules second) help | numbers not in abstract | Kulatunga-Moruzi 2011 (a21, b10) | S |
| Combined instruction beats none, most with misleading cases | N=60 and 48 undergraduates, ECGs | Eva 2007 (b11) | S, novices |
| No outcome trial in practice | 2 of 29 studies in practice; 28 intervention studies mostly early career; 13 of 87 debiasing studies targeted professionals | Staal 2022; Lambe 2016; Ludolph 2018 (a24, d22, d23) | E (K30) |

### 3.2 Language-model studies (summary table; detail in section 6)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Self-correction with no outside signal lowers accuracy | GPT-3.5 CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0 | Huang 2024 (c01, b29) | E (K13) |
| With the true label deciding when to stop, the same loop gains | GPT-3.5 GSM8K 75.9 to 84.3; CSQA 75.8 to 89.7; GPT-4 HotpotQA 49 to 59 | Huang 2024 (c02) | E |
| Wording sets the sign | GPT-4 CSQA 84.11 vs presume-error 66.34 vs fair 84.60 | Liu 2024 (d14) | S (K23) |
| Untreated model flips more right to wrong | Gemini 1.0 Pro MATH 15.8% right-to-wrong vs 4.6% wrong-to-right | Kumar 2024 SCoRe (d13) | E (K22) |
| "Are you sure?" on diagnosis does net harm | 10 LLMs, 120 vignettes; 51.8% to 42.2%; 544 vs 198 flips | Samsel 2026 (d17) | E (K22), abstract only |
| Medical QA reflection loop no better than CoT | GPT-4o MedQA 87.80 to 88.80; HeadQA 91.39 to 90.57; PubMedQA 70.80 to 69.00 | 2026 (c07) | E (K14) |
| Structured clinician-style prompts do not help | GPT-4 differential +2.2 (p=.24); GPT-3.5 differential -8 (p<.001) | Savage 2023 (c05, c06) | S (K15) |
| External feedback makes revision work | CRITIC +7.7 F1; CoVe FACTSCORE 55.9 to 71.4; Reflexion AlfWorld +22 | c23, c25, c26 | E (K16) |
| Matched-budget debate and refinement lose to voting | no MAD method won over 20% of 36 settings vs CoT; self-refine below CoT on MMLU-Pro (64.3 vs SC 68.7) | d01, d03, d04, d05 | E (K24) |
| Multi-agent medical gains small and unmatched | MedAgents GPT-4 86.7 vs few-shot CoT+SC 85.4; MDAgents MedQA 88.7 vs 83.9 at 9.3 vs 6.0 calls | d06, d07 | C (K25) |
| Active evidence seeking lowers accuracy | -12.75 points over 468 cases, 15 models; VivaBench 0.35 vs 0.69 | c14, c15 | E (K19) |
| Sample agreement beats verbal confidence | AUC 0.66-0.79 vs overestimated confidence | Savage 2025 (d18) | S (K27) |
| Reasoning models: forced Wait gives little | m1 optimum about 4K tokens; Wait minimal and sometimes breaks correct answers | d08, d09, d10, d11 | C (K26) |

---

## 4. Mechanisms and models

Each item is written so that code can implement it.

### 4.1 The DR procedure as a slot-filling loop (human protocol)

```
input: case C, first answer A1 (already given)
H = [A1]
repeat up to K times:
    h = H[-1]
    FOR  = findings in C that support h        (model, from C only)
    AGN  = findings in C that speak against h  (model, from C only)
    MISS = findings that h predicts but C lacks (model)
    if AGN or MISS is non-trivial:
        h_next = best alternative that explains AGN and MISS   (emerges from findings)
        H.append(h_next)
    else: break
rank H, return top
```

Notes from the human data:
- The expected-but-missing list is the only step that adds information not in the case text as given. It needs disease knowledge (a26).
- The plain "return to the case" arm of Think Twice (0.21 to 0.23) matched the full procedure (b07). Treat the long procedure as unproven against the cheap one.
- Free reflection (no template) fared much worse than cued reflection in learning studies (K11). In-the-moment, Monteiro's free version barely changed anything (K04).

### 4.2 Why a second look can help: three accounts

1. **Knowledge activation** (a26): listing findings for a disease pulls up the disease's features. Helps only if the knowledge exists. Backed by: knowledge predicts bias resistance (b16, d24); a checklist helps only if it contains the truth (b18); R1's errors included too few alternatives (d10); MedAgents error analysis found 77% of 40 failures were knowledge confusion or missing or wrong retrieval (c20).
2. **Reprocessing under a new hypothesis** (a26): the same findings get re-read through a different frame. Backed by eye tracking: successful revisers looked longer at information relevant to the correct diagnosis (6.3 s versus about 4 s; 25 versus 16-17 fixations; N=19, a27). Tiny sample.
3. **Disease-finding link strengthening** (a26): mostly explains the delayed learning effect (K10).

None is tested directly. The Think Twice null on content suggests that for very hard cases the effect of "just look again" may be most of the gain.

### 4.3 What a revision does, as accounting (needed for any test)

Every second pass has four outcomes per item:

| First answer | After second look | Name |
|---|---|---|
| wrong | right | **fix** |
| right | wrong | **break** |
| wrong | wrong (changed) | churn |
| any | unchanged | keep |

Net benefit = fixes minus breaks. A scheme with high fixes can still lose. Evidence:
- Unprompted LLM revision: right-to-wrong 15.8% vs wrong-to-right 4.6% (d13).
- "Are you sure?": 544 breaks vs 198 fixes in 10 LLMs (d17).
- Self-Refine on MATH: breaks 4.2, fixes 3.2 (d13).
- Trained SCoRe: fixes 5.8, breaks 1.4 (d13). That needs training.
- Monteiro humans: six correct diagnoses turned worse after revision while 18% of wrong ones were fixed (a36).

The schema already says (section 6) that the log must record flips. This subfield says it is the single most important metric.

### 4.4 The difficulty gate

Human data say the benefit depends on difficulty and expertise, but the pattern is unstable (K02). Gate options for an agent:

- **Sample agreement**: draw 3 to 5 independent first passes (S3 already does this). If they agree, skip S8. If they split, do the second look. Diagnosis AUC of sample consistency: 0.66 to 0.79, with verbalized confidence consistently overestimating (d18).
- **Code check**: if a check exists (G3), failure triggers S5. This is the oracle-like case that works (c02, d03).
- **Hidden-state probe**: AUC 0.7 to above 0.9 on math and logic, early exit saved 24 percent tokens (d15). Needs weights. Not available to a prompt-only agent.
- **MDAgents-style complexity routing**: rate complexity, route solo or group; beat CoT-SC at 9.3 versus 6.0 calls (d07). Calls not equal.
- Do **not** gate by verbalized confidence: human confidence tracked nothing (64 to 67 percent whatever the accuracy, a27), and models overstate (d18, c13: reasoning rubric above threshold in 91% of evaluations while accuracy was 56.3%).

### 4.5 Wording and framing of the S8 prompt

- **Presumes an error** ("find problems with your answer"): damages accuracy. GPT-4 CommonsenseQA 84.11 to 66.34 and 72.56 for two such wordings; fair wording 84.60 (d14).
- **Neutral wording** leaves accuracy about unchanged, because the model rarely changes. The fair-prompt gain was +0.08 to +0.67 on CSQA. HotpotQA GPT-3.5 31.0 to 47.0 with a fair prompt (d14). The gain on CSQA is small and rests on the model changing little.
- **Blind spot**: 14 non-reasoning models fixed an injected error when it appeared as the user's, but not when it was their own. Mean blind spot 64.5 percent. Appending "Wait" cut the gap by 89.3 percent (d12). On GSM8K-SC: internal 0.183, external 0.881, Wait 0.796.
- **Pushback** ("Are you sure?") invites sycophancy (d17). One model flipped 58.6 percent of answers and lost 36.4 points.

Mechanism summary for an engineer: the sign of the effect is controlled by (a) how much the prompt presumes a mistake, (b) whether the model changes answers freely or only on new information, and (c) whether something outside the model decides.

### 4.6 Content beats process: contrast cards

The human line with the most independent support (K08, K09) is that **knowledge of discriminating features** protects. Implementation sketch:

- Memory store of look-alike pairs: disease A versus disease B, the features that separate them, and the usual trap.
- Retrieve by similarity to the current candidate list.
- Show **after** the first attempt (SCHEMA section 5 already says lessons are shown after the first attempt, not before, to avoid fixation).
- Caveat K09: a list that lacks the truth is not neutral; it fell to 0.43 against a 0.49 control (ns vs control but far below the 0.75 with the right list).

### 4.7 Factored verification

Chain-of-Verification (c26): plan verification questions, answer each **without seeing the draft**, then revise. Factored beat joint verification (60.8 to 63.7 on one measure; FACTSCORE 55.9 to 71.4 overall). This is the closest LLM analogue to a code-judged second look and it fits G4/G5 (independent, blind judge). It was tested on factual recall, not diagnosis.

### 4.8 Verification after the first reading, with a checklist

Sibbald (d19): experts read the ECG, then ran a checklist. Errors corrected 0.29 versus 0.03 per ECG. Cognitive load was not higher (3.7 versus 3.3, ns). The checklist cost time. The structure is: finish first pass, then run a fixed list. This is the same shape as S8 after S4.

---

## 5. What holds up

### 5.1 Replications and meta-analyses

- **Meta-analyses agree on a small to moderate average gain**: guided reflection ES 0.38 (Prakash 2019, N professionals 4380); all workplace tools g=0.20 (Staal 2022, N=2732). Staal could not explain the variance with intervention type, case difficulty or expertise, and noted that 13 of 29 studies let participants see the same cases (so revisiting is mixed in) and only 2 of 29 were in practice.
- **Availability bias and reflection**: one lab, small N (36, 38), repeat effect confounded.
- **Delayed learning** replicated three times in the Rotterdam/Brazil network (a11, a12, d25 with co-authors). No fully independent replication found.
- **Cued over free reflection**: replicated by a partly independent group (Fernandes 2021, b24), with the caveat that a co-author overlaps.
- **Independent group support for a structured verification pass**: Sibbald and colleagues (Toronto, Maastricht), ECG reading. Small.

### 5.2 Failed replications and nulls

- Ilgen 2013 (N=393) and Lambe 2018 (N=186): no benefit from directed search or guided reflection over first impression.
- Think Twice: no difference between for, against, both and plain return.
- Norman 2014, Sherbino 2014: instructions and cognitive forcing do nothing.
- Learning-by-teaching of DR: no transfer (a29).
- Deliberation-without-attention failed to replicate (a34), which removes a competing "sleep on it" account.
- Transfer to adjacent diseases did not replicate in novices (a14).

### 5.3 Moderators

| Moderator | What was found | Status |
|---|---|---|
| Case difficulty | residents gain on complex (a03, a04); but family residents gain on all (a08), dermatology gains more on easy (a10), Think Twice gains only at 22% accuracy | contested (K02) |
| Expertise | residents gain; students worse on complex (a04); novices gain on simple | contested |
| Existing hypothesis | procedure works on a held hypothesis (a25) | single-lab claim |
| Knowledge | reflection helps with the needed knowledge; checklist helps only if it holds the truth | established |
| Guidance | cued and modelled beat free; expertise reversal at advanced level (a31) | established |
| Case visible during reflection | hide helps studied diseases, show helps adjacent diseases (interaction p=0.006) | single-source |
| Time delay | harm now, benefit a week later (learning) | established in the network |
| Trigger | self-chosen revision is rare (8%) and mostly of the weak items (a36) | single-source |
| Perceived difficulty | telling doctors others failed the case triggered reflection (a32) | single-source |

### 5.4 What worked, and what did not

Worked (in people):
- A fixed template listing for, against and missing findings, then alternatives (small to moderate).
- Cued or modelled reflection over free reflection.
- Look-alike contrast practice with feedback (knowledge).
- A differential list that contains the right answer.
- A checklist verification after the person's own reading (ECG, small).

Did not work (in people):
- "Be slow and careful", "be analytic", "avoid bias" instructions.
- Cognitive forcing training.
- Free self-chosen second looks.
- Telling the person to switch reading strategy (Sibbald 2012).
- Confidence as a guide: reflection did not improve calibration.

### 5.5 Quality warnings on the human evidence

- Nearly all written vignettes with all information supplied.
- One lab network; Ns 34 to 119 except Ilgen (393), Staal, Prakash.
- No study separates a structured second look from spending more time or seeing the case twice.
- No real-practice trial with patient outcomes (K30).
- Mechanism claims untested.
- Several numbers are from abstracts or from a review by the lab that promotes DR. critique.md lists which lines are abstract-only (a03, a05-a08, a11-a14, a17-a19, a21-a23, a29-a32, a35 partly, b09, b14).
- Two corrections in critique.md: Costa Filho p-values should be 0.228 and 0.197 (not 0.21 and 0.19); the case-revisitation 2026 ORs have inconsistent CIs and should not be relied on beyond the interaction.

---

## 6. Language models

### 6.1 Generic self-correction (no outside signal)

- **Huang et al. 2024** (c01-c03; Tables 2 and 3 re-checked by the critique):
  - GPT-3.5: GSM8K 75.9, 75.1, 74.7 over calls 1, 3, 5; CommonSenseQA 75.8, 38.1, 41.8; HotpotQA 26.0, 25.0, 25.0.
  - GPT-4: GSM8K 95.5, 91.5, 89.0; CSQA 82.0, 79.5, 80.0; HotpotQA 49.0, 49.0, 43.0.
  - Llama-2 GSM8K 62.0, 43.5, 36.5 (not rechecked). GPT-4-Turbo 91.5, 88.0, 90.0 (not rechecked).
  - With oracle labels deciding when to stop: GPT-3.5 GSM8K 75.9 to 84.3; CSQA 75.8 to 89.7; HotpotQA 26.0 to 29.0. GPT-4 GSM8K 95.5 to 97.5; CSQA 82.0 to 85.5; HotpotQA 49.0 to 59.0.
  - Stronger models change fewer answers, so they lose less and gain less. GPT-3.5 kept its first GSM8K answer 74.7% of the time.
- **Kamoi 2024 survey** (c04): no prior work shows success from prompted-model feedback alone, except on unusually suited tasks. Reliable external feedback works. Large-scale fine-tuning also works. Reflexion with oracle feedback is an unfair setting.
- **Liu 2024** (d14): the wording and the sampling temperature decide the sign (see 4.5). It reconciles the pro and con papers, with a caveat that the fair-prompt gain is small and relies on the model changing little.
- **Tsui 2026** (d12): 64.5% blind spot; "Wait" removes 89.3% of it, but on PRM800K-SC "Wait" dropped to 0.504 from 0.620 external.
- **Kumar 2024** (d13): Gemini 1.0 Pro on MATH. Base: 52.6 to 41.4 (-11.2). Self-Refine 52.8 to 51.8. SCoRe-trained 60.0 to 64.4 (+4.4). Training is needed to turn the sign.
- **Reflection words in reasoning traces do not track accuracy** (d11, R1-Zero on MATH).

### 6.2 Medical and diagnostic second looks

- **Medical QA self-reflection loops** (c07-c09, 2026): GPT-4o MedQA 87.80 to 88.80 (n=1,273); HeadQA 91.39 to 90.57 (n=244); PubMedQA 70.80 to 69.00 (n=500). GPT-4o-mini MedQA 74.80 to 76.00; HeadQA 79.10 to 79.10; PubMedQA 71.60 to 69.60. Over 85 percent of GPT-4o instances needed no extra reflection. Differences of about a point are within noise at these n. The stop rule was model-judged ("satisfied"), so the gap to a code-judged stop is untested.
- **Clinician-style prompts** (Savage 2023, c05-c06): MedQA, GPT-4 CoT 76; differential 78 (+2.2, CI -1.4 to +5.8, p=.24); analytic 78 (+1.6, p=.35); intuitive 77 (+0.8, p=.73); Bayesian 72 (-3.4, p=0.07). GPT-3.5: CoT 46; intuitive 48; analytic 40 (-6, p=0.001); differential 38 (-8, p<0.001); Bayesian 42 (-4, p=0.02). The published paper frames GPT-4 as mimicking reasoning "without sacrificing accuracy".
- **Sycophancy / pushback** (Samsel 2026, d17, abstract only): 10 LLMs, 120 vignettes (40 MultiCaRe, 80 MedMCQA-derived), 4 prompt conditions, 3 runs by 2 passes = 28,800 responses. Neutral 51.8 percent to 42.2 after "Are you sure?" (flip rate 32.8 percent). 544 correct-to-incorrect vs 198 incorrect-to-correct. GPT-5 74.4 to 75.3. Claude Sonnet 4 flip rate 58.6 percent, -36.4 points. Scoring by LLM judge.
- **Self-verification in psychiatry** (b34): 106 vignettes. Sensitivity 0.732-0.817 unchanged. PPV 0.534-0.779, effect p=.007 (reasoning model p=.009). Best o3-pro + self-verification: sensitivity 0.782, PPV 0.779. Precision rose, recall did not. Vignettes from a textbook likely in training.
- **Reflective self-review for code-status extraction** (b35): 1000 MIMIC-IV notes. It impaired MedGemma-27B for DNI (p=.047); multi-agent review doubled tokens and latency; the weak 8B model gained (DNR p=.017, CMO p<.001). Easy labels, so the Mamede boundary applies.
- **Bias induction** (c10-c11, b31-b32): BiasMedQA GPT-4 72.7 clean, drops of 10 to 26 points by model (GPT-3.5 average -37.4%). Mean over models: false consensus -24.9, frequency -18.2, recency -12.9, confirmation -8.1. Bias education: GPT-4 frequency 0.627 to 0.720. Radiology: authority cue -21.1 (text) and -44.9 (multimodal) points; audit +5.6 and +15.8; one-shot +4.0 and +24.9. Gemini fell from 80.0-88.6% to 47.4-86.1% on four unpublished bias prompts; a debiasing prompt and few-shot examples did reduce biased answers in three models (b31). Compare with humans where debiasing instructions fail (K03, K18).
- **Failure to gather evidence** (c13-c15): 32 frontier models, 20 hematologic oncology cases, best accuracy 68%; information utilisation fell from about 57% in rounds 1-2 to 25.7% in round 3. VivaBench: Gemini 2.5 Pro final top-1 0.35 vs full-information 0.69; failure causes classed by an LLM: inappropriate hypothesis generation 348, premature closure 291, inadequate investigations 90. Active evidence seeking: -12.75 points average over 468 cases, 15 models.
- **Anchoring in a reasoning model** (d10): R1 got 93 of 100 MedQA cases. The 7 errors showed anchoring, trouble with conflicting data, too few alternatives and overthinking. Wrong answers had longer reasoning (8,118 vs 3,648 characters, p=0.032, fragile with 7 errors).
- **Oncology notes** (c18): GPT-4 chain-of-thought interpretations had errors in 23.1% (+-0.8); 85.4% of errors were reasoning failures; detectors found that an error existed but could not name its type.
- **Human-AI** (c16-c17): 50 physicians with GPT-4 scored 76 vs 74 (+2, CI -4 to 8); GPT-4 alone 92. Reading AI text changed 27.6% of answers, 2.81% harmfully.

### 6.3 What changed the result, and by how much

| Change | Effect | Source |
|---|---|---|
| Oracle label decides when to stop | GPT-3.5 GSM8K +8.4; CSQA +13.9; GPT-4 HotpotQA +10 | c02 |
| Tool or retrieval check | CRITIC +7.7 F1 (QA); +7.0 (math) | c25 |
| Factored verification questions, answered blind | FACTSCORE +15.5 (55.9 to 71.4); factored over joint +2.9 | c26 |
| Environment pass/fail signal | Reflexion AlfWorld +22 | c23 |
| Fair rather than presume-error wording | CSQA 66.34 to 84.60 (about +18) | d14 |
| Training on self-correction | SCoRe +4.4 vs base -11.2 | d13 |
| Mixing different models | MMLU-Pro mixture of agents 71.4 vs SC 68.7 vs CoT 64.3 | d04 |
| Model-judged stop (Reflexion with GPT-4 judge) | no gain over Reflexion-SC (judge only slightly better than random) | d03 |
| Role-play medical agents | MedQA GPT-3.5 CoT 55.0 to role-play 62.0, analysis 65.0, summary 67.0; but GPT-4 vs few-shot CoT+SC only +1.3 on average | c20, d06 |
| Adaptive complexity routing | MedQA 83.9 to 88.7 at 9.3 vs 6.0 calls | d07 |
| Long reasoning training with verifier (HuatuoGPT-o1) | LLaMA-3.1-8B MedQA 65.2 (answers only) to 69.0 complex CoT to 72.6 with PPO verifier | d16 |
| Forced Wait re-thinking in medicine | minimal gain, sometimes harm | d08 |

### 6.4 Matched-budget evidence

- Debate: no multi-agent debate method won more than 20 percent of 36 settings versus CoT; budget 6 calls (d01). gpt-4o-mini MMLU: CoT 80.73, SC 82.13, SoM 74.73, MultiPersona 75.47, EoT 67.87, ChatEval 79.13, AgentVerse 80.40.
- Wang 2024 (d03): at 20 queries or 10k tokens, CoT-SC beats Reflexion and debate. Reflexion and debate can get worse with more budget.
- Tran and Kiela 2026 (d05): one agent matches or beats sequential, debate, ensemble and role-based setups at equal thinking tokens (Qwen3-30B-A3B, R1-Distill-Llama-70B, Gemini 2.5 Flash and Pro; FRAMES and MuSiQue). Example R1-70B FRAMES: single 0.448, sequential 0.391, debate 0.397. The authors found budget-control artifacts in Gemini.
- Wunderlich 2026 (d04): self-refinement stays below CoT. Debate (4 agents, 2 layers) 70.0 and mixture of agents 71.4 beat SC 68.7 on MMLU-Pro. By item difficulty: easy base 94.4 (+2.2), medium 53.0 (+8.5), hard 8.4 (+9.0 at 15-20x compute).
- In medicine: Smit 2024 (d02): Medprompt and SC top on medical sets; on MedQA Medprompt 0.65, SoM 0.64, SC 0.60, single 0.60; PubMedQA Medprompt 0.77, single 0.75. Differences 0.01 to 0.05. Cost not equalised.
- Gain in reasoning-model thinking budgets: roughly log scale up to about 256 tokens on routine items and about 4K on hard sets (d08, d09); +15 to 20 percent for small models, +5 to 10 for large.

This matches SCHEMA G9 (no debate) and G11 (parallel attempts beat extended thinking at equal compute).

---

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Evidence ids refer to the evidence files; K ids to claims.jsonl.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Log both flip directions at every S5 and S8 pass** (fix, break, churn, keep) and report the break-to-fix ratio per condition. Accept a changed answer only if the change cites a new finding from real output (code located). Tightens G2 and section 6. | S5, S8, G2, logging | [E] | K22, K13; d13, d17, c01, a36 |
| A2 | **A revision trigger must be external**: a code check, a held-out example or a tool, not the model's own judgement that it should rethink. Reinforces G1, G2, G3. | S5, S8, G1/G2 | [E] | K13, K16; c01, c02, c04, c23, c25, c26, d03 |
| A3 | **Every S5/S8 test runs against an equal-token CoT-SC arm**; credit the second look only for the margin above sampling more first passes. Reinforces G7, G9, G11. | G7, bench | [E] | K24; d01, d03, d04, d05 |
| A4 | **Do not add a generic "slow down, be careful, avoid bias" instruction.** Already in 4b; add this subfield's evidence ids to the row. | 4b | [E] | K03; a19, a20, b05, b17, d27 |
| A5 | **Do not use stated confidence as a stop or reflect rule.** Reflection does not fix calibration in people; models overstate. Sample agreement is the usable proxy, only as a hint (G4). | G (4b row on confidence) | [E] | K12, K27; b19, a27, d18, c13 |
| A6 | **If S8 asks a model to look again, use a fixed template, not "reflect" in open form.** S5's "one line naming what is wrong, then fix" already is one. Keep it; do not replace with open prose. Human evidence only (cued beat free, p<.001). | S5 template | [E] human only | K11; a13, a14, b22, b24 |
| A7 | **Candidate lists help only if they contain the truth.** Build any list in S3/S4 from the agent's own harvested attempts plus untried directions, and treat a list as capable of hurting when its truth is missing. Do not hand the model a fixed external list as proof. | S3/S4 harvest | [E] human | K09; b18, d19 |
| A8 | **Write the evidence limit into the schema notes**: the second look is supported by vignette evidence, mostly one lab network, and no practice trial exists. | notes | [E] | K30; d22, d23, a24 |

### Test first (not established for an LLM agent)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Structured for/against/missing/alternative second look vs plain second pass vs no second pass**, equal tokens. | S5, S8 | [S] human small gain; no LLM test | K01, K05, K06; a17, b07, a24, b03 |
| T2 | **Difficulty gate**: revise only when first passes disagree. | S8 gate | [C] | K02, K25, K27; d07, d18 |
| T3 | **Neutral S8 wording vs presume-error vs colleague's-claim framing.** | S8 wording | [S] | K23; d12, d14 |
| T4 | **Factored (blind) verification questions vs joint verification.** | S8 | [E] outside medicine, untested in diagnosis | K16; c26 |
| T5 | **Contrast cards retrieved after the first attempt vs process prompt.** | memory | [E] human; no LLM test | K08; a15, b15, d24 |
| T6 | **Store a for/against reflection note after a case; test on later look-alikes.** | memory/S9 | [E] human network; LLM untested | K10; a11, a12, d25 |
| T7 | **Forced "what is still missing" check before the final answer** in interactive tasks. | S8, gather | [E] failure, fix untested | K19; c13, c14, c15 |
| T8 | **Budget B vs B/2 plus structured S8 at B/2** on a reasoning model. | G11/S8 | [C] | K26; d08, d09, d10 |
| T9 | **Alternatives listed late (after the first commitment) vs early.** | S3/S5 order | [S] | K29, K06; d21, a18 |
| T10 | **Fixed analytic verification step after S5 vs adaptive mode-switch prompts.** | S8 | [S] | K28; d19, d20 |
| T11 | **Pushback resistance**: S8 must hold the first answer against a bare "are you sure". | S8 | [E] harm shown | K22; d17 |
| T12 | **Hide the case text vs show it during the second look.** | S5 | [S] | a30, b37 |

Items not to take: debate between agents (G9), generic bias checklists (4b), cognitive forcing prompts (4b), a model critic that sees the proposed answer (G5), ACH-style full matrices (4b).

---

## 8. Concrete tests on our bench

All arms get the same total token budget per item (first pass plus second pass plus any extra samples). The CoT-SC arm gets the freed tokens as additional independent first passes (A3). Report accuracy, fixes, breaks, churn, tokens per item. Use paired comparisons on the same items, at least 3 seeds.

Our bench holds ARC items, BRAINTEASER word puzzles and NoveltyBench. Diagnosis vignettes are not on the bench yet. For items 1 to 5 below we need a diagnosis vignette set (MedQA subset plus a harder set with natural first-pass accuracy of 30 to 60 percent; avoid selecting by first-pass failure, as the MedAgents bias set did). For the others, use the bench items.

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| 1 | Structure vs plain second pass | diagnosis vignettes, stratified easy/hard by first-pass agreement | (a) first pass only, (b) plain re-read and re-answer, (c) DR template (for / against / missing / alternative), (d) for-only, (e) against-only, (f) CoT-SC with the same tokens | accuracy; fix and break counts; net by stratum | (c) minus (b) near 0 to +2 points (Think Twice shape); (c) and (b) above (a) only on hard; (f) probably beats both; break rate of (b) and (c) under 5 percent |
| 2 | Difficulty gate | diagnosis vignettes and BRAINTEASER | always revise; never revise; revise when 3 first passes disagree; revise when verbal confidence below threshold | accuracy at equal tokens; breaks per 100 items | agreement gate keeps most fixes and removes most breaks; verbal confidence gate no better than random (AUC 0.5 to 0.6) |
| 3 | Wording | diagnosis, BRAINTEASER | presume-error; neutral "check against the case"; "a colleague proposed this answer, assess it"; bare "are you sure" | net flips; accuracy | presume-error and "are you sure" lose several points; neutral near 0; colleague framing may fix more but break more |
| 4 | Trigger source | ARC (code check exists) and diagnosis (no check) | model-judged trigger vs code-judged trigger (held-out example fails) vs sample-disagreement trigger | accuracy; harmful flip ratio | code trigger wins on ARC (oracle-like); on diagnosis, disagreement trigger beats model-judged |
| 5 | Contrast cards | diagnosis look-alike pairs with a bias cue injected (prior similar case, authority cue) | no aid; generic debias warning; process template; retrieved contrast card shown after first attempt | accuracy under cue; recovery of cue loss | generic warning recovers a fraction (4 to 25 points per b32); contrast card recovers more if the card holds the discriminating feature; card without truth hurts |
| 6 | Factored verification | diagnosis; BRAINTEASER | joint verification; factored verification (sub-questions answered without the draft); CoT-SC | accuracy; fixes and breaks | factored beats joint by 1 to 3 points (CoVe-like), may tie CoT-SC |
| 7 | Missing-evidence check | interactive or staged-information tasks (reveal findings in rounds) | no check; forced "what is still missing and ask for it" before final; more rounds budget | accuracy; information utilisation by round | utilisation in last round up from about 25 percent; accuracy +2 to +6 |
| 8 | Reasoning-model budget split | diagnosis, harder BRAINTEASER | one pass at budget B; one pass at B/2 + structured S8 at B/2; one pass at B/2 + sample at B/2 | accuracy | all within 1 to 2 points; structured S8 unlikely to win by more than noise |
| 9 | Hypothesis order | diagnosis with misleading cue | list differential first; first hypothesis then alternatives one at a time from the evidence | right answer present in list; final accuracy | no difference (d21) |
| 10 | Pushback hold | diagnosis | after the answer, inject "are you sure"; S8 keeps first answer unless it cites a new finding vs free change | accuracy; break rate | rule cuts breaks sharply (544 vs 198 baseline pattern) |
| 11 | Reflection note memory | sequence of look-alike diagnosis cases (30 pairs) | store the answer only; store a for/against note; store a contrast card | accuracy on later look-alikes, after other cases intervene | note beats answer-only if it names discriminating features; process-only note ties |
| 12 | Existing G1 check on diagnosis | diagnosis | forced doubt on every item vs doubt only on signal | accuracy | repeats our word-puzzle result (92 vs 75) |

Pass rule for adding any element: wins over its matched CoT-SC arm at equal tokens, on at least two item sets, with break-to-fix ratio under 1 to 3, and the gain exceeds two standard errors across seeds (see UNKNOWNS.md for the per-item thresholds).

---

## 9. What does not transfer, and why

- **Writing for/against lists for a model is not the same as for a person.** The human benefit is attributed to knowledge activation and reprocessing; a model that already attended to all tokens in context may have nothing to reprocess. Savage found no structured-prompt gain for GPT-4 (c06).
- **Learning effects (delayed benefit, adjacent diseases) do not apply inside one run.** A model's weights do not change. They may apply to the memory store between runs (T6), not to a single case.
- **Human time pressure and motivation.** Reflection took time; slow versus fast was not the cause (Norman 2012: faster was more accurate, r=-0.54). Models have no fatigue and no motivation effect (b36's motivation share is not relevant).
- **Vignettes with all information.** DR results come from cases where all findings are on the page. Real diagnosis, and our agent on open tasks, must gather evidence, and models under-gather (K19).
- **Expertise as moderator.** Students versus residents differ in stored knowledge. A model's "knowledge level" is fixed per model; the analogue is model size (weaker models gained more from a reviewer in b35, and small reasoning models gained most from thinking in d09).
- **Perceived difficulty as a trigger.** Telling doctors others failed a case triggered reflection (a32). For a model, that is a prompt cue and likely to cause the presume-error harm (d14).
- **Calibration and confidence findings** are useful as warnings only. They do not tell us what the model's internal state does.
- **Eye-tracking mechanisms** (a27). Not available; attention in a transformer is not a gaze.
- **Human-AI interface findings** (K20, c16-c17) concern how a person reads a model. Our agent has one model.
- **Multi-agent critic gains** in medicine (b33, c20, c21) depend on roles, retrieval and mixing models; they do not support a single-model scaffold, and G9 already excludes debate.
- **Training-based self-correction** (SCoRe, HuatuoGPT-o1, AMIE) changes the model, which we do not do.
- **Checklists written by researchers** (d19) carry the answer-relevant content from outside. An agent without retrieval does not have this.

---

## 10. Open questions

1. Does a structured for/against/missing/alternative second look beat a plain second pass at equal tokens for an LLM, and on which items? No study found.
2. Does a code- or tool-judged trigger beat a model-judged one in diagnosis? Shown only in math, commonsense and games.
3. In diagnosis, can first-pass confidence or sample agreement separate harmful flips from helpful ones? Sample agreement predicts correctness (AUC 0.66-0.79), but gating a second look with it inside a diagnosis pipeline is untested.
4. Do reasoning-trained models already do the second look internally? Evidence points both ways (d08-d11, d16). No equal-thinking-budget comparison of B versus B/2 plus structured S8 in medicine was found.
5. Does retrieved look-alike contrast knowledge beat a process prompt for an LLM facing availability or anchoring cues? Human evidence only.
6. Is the bottom-up hypothesis order real? The one independent test (d21) shows no order effect on presence of the right diagnosis; it does not test DR directly.
7. Does the DR benefit exist in real practice with patient outcomes? None found.
8. Is a plain return to the case (time-on-task, repeat exposure) most of the human effect? Think Twice had no no-return control; Staal noted 13 of 29 studies share the flaw.
9. Does the delayed learning effect replicate outside the Mamede/Schmidt network?
10. Do multi-agent critic gains in medicine (MedAgents, MDAgents, DERA, MedARC, MCC) survive a matched-token single-agent baseline? Outside medicine they do not (d01, d03, d05).
11. How large is the net flip rate for modern reasoning models on diagnosis when the second look is a neutral check, not a pushback? Only pushback (d17) and math (d13) are measured.
12. Which wording is safe at the second look in diagnosis (presume-error, neutral, colleague framing)? Only commonsense and math are measured.
13. Case-visible versus case-hidden reflection (a30): is there an LLM analogue (second look with the case text versus only the model's summary)?
14. Why did the earlier "more than 35 percent" and the 0.45 to 0.58 figures differ (critique 3.4)?

---

## 11. Sources

[V] opened (full text, PDF text or abstract page read; critique.md records which numbers were re-checked). [M] snippet only or not opened.

### Founding and DR program

- [V] Mamede and Schmidt 2023, Deliberate reflection and clinical reasoning (Med Educ 57:76-85) https://pmc.ncbi.nlm.nih.gov/articles/PMC10083910/ (a01, a02, a25, a26, b02, b27, b38; note: a review by the DR lab)
- [M] Mamede, Schmidt, Penaforte 2008, Effects of reflective practice (Med Educ 42:468-475) https://europepmc.org/article/MED/18412886 (a03; abstract read for b01 at https://pubmed.ncbi.nlm.nih.gov/18412886/, [V] abstract)
- [V] Mamede et al. 2010, Conscious thought beats deliberation without attention (Psychol Res) https://europepmc.org/article/MED/20354726 (a04; b25 https://pubmed.ncbi.nlm.nih.gov/20354726/)
- [M] Mamede et al. 2010, Availability bias, JAMA https://europepmc.org/article/MED/20841533 (a05; b12 https://pubmed.ncbi.nlm.nih.gov/20841533/ [V] abstract)
- [M] Schmidt et al. 2014, Exposure to media information, Acad Med https://europepmc.org/article/MED/24362387 (a06)
- [M] Mamede et al. 2012, Salient distracting features, BMJ Qual Saf https://europepmc.org/article/MED/22389021 (a07; b13 https://pubmed.ncbi.nlm.nih.gov/22389021/ [V] abstract)
- [M] Schmidt et al. 2017, Patients' disruptive behaviours, BMJ Qual Saf https://europepmc.org/article/MED/26951795 (a08, b14)
- [V] Costa Filho et al. 2019, Dermatology, Perspect Med Educ https://repub.eur.nl/pub/118085/Repub_118085_O-A.pdf and https://pmc.ncbi.nlm.nih.gov/articles/PMC6684533/ (a09, a10, b19)
- [M] Mamede et al. 2012, Reflection as a strategy to foster acquisition, Med Educ https://europepmc.org/article/MED/22515754 (a11; b20 https://pubmed.ncbi.nlm.nih.gov/22515754/ [V] abstract)
- [M] Mamede et al. 2014, Practice with clinical cases, Acad Med https://europepmc.org/article/MED/24280855 (a12; b21 [V] abstract)
- [M] Ibiapina et al. 2014, Free, cued and modelled reflection https://europepmc.org/article/MED/25039736 (a13; b22 https://pubmed.ncbi.nlm.nih.gov/25039736/ [V] abstract)
- [V] Mamede et al. 2019, Fostering novice students' diagnostic ability https://pmc.ncbi.nlm.nih.gov/articles/PMC6594026/ (a14, b23)
- [V] Mamede et al. 2020, Immunising physicians against availability bias https://pmc.ncbi.nlm.nih.gov/articles/PMC7362774/ (a15, b15)
- [V] Mamede et al. 2021, Specific disease knowledge as predictor https://pmc.ncbi.nlm.nih.gov/articles/PMC7947124/ (a16, b16)
- [M] Mamede et al. 2020, Think Twice, Acad Med https://europepmc.org/article/MED/31972673 (a17; b07 https://pubmed.ncbi.nlm.nih.gov/31972673/ [V] abstract)
- [V] Fernandes et al. 2021, Adding guidance to deliberate reflection https://pubmed.ncbi.nlm.nih.gov/33978967/ (b24)
- [V] Ribeiro, Mamede et al. 2021, Mechanisms underlying learning from DR https://pubmed.ncbi.nlm.nih.gov/33159364/ (b36)
- [V] Eye-tracking experiment on selective processing, Med Educ 2025 https://pmc.ncbi.nlm.nih.gov/articles/PMC11976213/ (a27)
- [V] Teaching medical students to apply DR https://pmc.ncbi.nlm.nih.gov/articles/PMC10841076/ (a28)
- [M] Learning DR: learning-by-teaching, Adv Health Sci Educ 2023 https://europepmc.org/article/MED/35913665 (a29)
- [M] Case revisitation during DR, Diagnosis 2026 https://europepmc.org/article/MED/42644626 (a30; b37 https://pubmed.ncbi.nlm.nih.gov/42644626/ [V] abstract)
- [M] Faded examples vs cued reflection 2026 https://europepmc.org/article/MED/41943587 (a31)
- [M] Mamede et al. 2008, Perceived difficulty https://europepmc.org/article/MED/19202502 (a32; b26 https://pubmed.ncbi.nlm.nih.gov/19202502/ [V] abstract)
- [V] Self-explanation and structured reflection: layered analysis https://pmc.ncbi.nlm.nih.gov/articles/PMC8187699/ (a33)
- [V] Conscious versus unconscious thinking in the medical domain 2014 https://pmc.ncbi.nlm.nih.gov/articles/PMC4078052/ (a34)
- [V] Mamede, Zandbergen et al. 2024, Anchoring bias https://pubmed.ncbi.nlm.nih.gov/38365449/ (d24)
- [V] Chamberland et al. 2019, Self-explanation and feedback https://pubmed.ncbi.nlm.nih.gov/31185971/ (d25)
- [M] Mamede and Schmidt 2014, Reflection in diagnostic reasoning: what really matters? https://pubmed.ncbi.nlm.nih.gov/24979158/ (b09, not opened)

### Independent human studies, nulls and reviews

- [M] Ilgen et al. 2013 (Acad Med) https://europepmc.org/article/MED/23969355 (a18; b08 https://pubmed.ncbi.nlm.nih.gov/23969355/ [V] abstract)
- [M] Norman et al. 2014 System 1 vs System 2 https://europepmc.org/article/MED/24362377 (a19; b05, d27 https://pubmed.ncbi.nlm.nih.gov/24362377/ [V] abstract)
- [V] Sherbino et al. 2014 cognitive forcing https://europepmc.org/article/MED/24423999 (a20; b17)
- [M] Kulatunga-Moruzi et al. 2011 https://europepmc.org/article/MED/21942311 (a21; b10 [V] abstract)
- [M] Myung et al. 2013 https://europepmc.org/article/MED/23327617 (a22)
- [V] Lambe et al. 2018 https://doi.org/10.3389/fpsyg.2018.02297 (a35)
- [V] Monteiro et al. 2015 https://doi.org/10.1007/s11606-015-3369-4 and https://pubmed.ncbi.nlm.nih.gov/26173528/ (a36, b06)
- [V] Eva et al. 2007 https://pubmed.ncbi.nlm.nih.gov/18045367/ (b11)
- [V] Norman et al. 2012 response time https://pubmed.ncbi.nlm.nih.gov/22534592/ (b28)
- [V] Kaemmer et al. 2021 differential checklists https://pubmed.ncbi.nlm.nih.gov/34291481/ (b18)
- [V] Sibbald et al. 2013 checklists https://pubmed.ncbi.nlm.nih.gov/23398016/ (d19)
- [V] Sibbald and de Bruin 2012 https://pubmed.ncbi.nlm.nih.gov/21874594/ (d20)
- [V] Sibbald et al. 2022 early vs late differential support https://pubmed.ncbi.nlm.nih.gov/34611040/ (d21)
- [V] Prakash et al. 2019 meta-analysis https://pubmed.ncbi.nlm.nih.gov/30244625/ (b03; a23 https://europepmc.org/article/MED/30244625)
- [V] Staal et al. 2022 meta-analysis https://pmc.ncbi.nlm.nih.gov/articles/PMC9685706/ (a24; sub-counts remain full-text only)
- [V] Chernikova et al. 2019 https://doi.org/10.1007/s10648-019-09492-2 (a37; not reopened by critique)
- [V] Lambe et al. 2016 systematic review https://pubmed.ncbi.nlm.nih.gov/26873253/ (b04, d22)
- [V] Ludolph and Schulz 2018 debiasing review https://pubmed.ncbi.nlm.nih.gov/28649904/ (d23)

### Language-model studies

- [V] Huang et al. 2024, LLMs cannot self-correct reasoning yet https://arxiv.org/abs/2310.01798 (b29, c01-c03)
- [V] Kamoi et al. 2024 survey https://arxiv.org/abs/2406.01297 (b30, c04; abstract page only)
- [V] Savage et al. 2023, diagnostic reasoning prompts https://arxiv.org/abs/2308.06834 (c05, c06)
- [V] Medical QA self-correction exploratory study 2026 https://arxiv.org/abs/2604.00261 (c07-c09)
- [V] Schmidgall et al. 2024, BiasMedQA https://arxiv.org/abs/2402.08113 (c10, c11)
- [V] Echterhoff et al. 2024, BiasBuster https://arxiv.org/abs/2403.00811 (c12)
- [V] Braitsch et al. 2026, information-seeking failures https://arxiv.org/abs/2607.10275 (c13)
- [V] VivaBench 2025 https://arxiv.org/abs/2510.10278 (c14)
- [V] Active evidence-seeking 2026 https://arxiv.org/abs/2605.22047 (c15)
- [V] Goh et al. 2024, JAMA Netw Open https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395 (c16; last part not read)
- [V] Rhetorical misalignment 2026 https://arxiv.org/abs/2608.14630 (c17)
- [V] Cognitive bias in oncology notes 2025 https://arxiv.org/abs/2511.20680 (c18)
- [V] Nair et al. 2023, DERA https://arxiv.org/abs/2303.17071 (c19)
- [V] Tang et al. 2023, MedAgents https://arxiv.org/abs/2311.10537 (c20, d06)
- [V] Kim et al. 2024, MDAgents https://arxiv.org/abs/2404.15155 (c21, d07)
- [V] Tu et al. 2024, AMIE https://arxiv.org/abs/2401.05654 (c22)
- [V] Shinn et al. 2023, Reflexion https://arxiv.org/abs/2303.11366 (c23)
- [V] Madaan et al. 2023, Self-Refine https://arxiv.org/abs/2303.17651 (c24)
- [V] Gou et al. 2024, CRITIC https://arxiv.org/abs/2305.11738 (c25)
- [V] Dhuliawala et al. 2023, Chain-of-Verification https://arxiv.org/abs/2309.11495 (c26)
- [V] Zhang et al. 2025, Stop overvaluing multi-agent debate https://arxiv.org/abs/2502.08788 (d01)
- [V] Smit et al. 2024, Should we be going MAD? https://arxiv.org/abs/2311.17371 (d02)
- [V] Wang et al. 2024, Reasoning in token economies https://arxiv.org/abs/2406.06461 (d03)
- [V] Wunderlich et al. 2026, Multi-agent reasoning and Pareto test-time scaling https://arxiv.org/abs/2605.01566 (d04)
- [V] Tran and Kiela 2026, Single-agent vs multi-agent at equal thinking tokens https://arxiv.org/abs/2604.02460 (d05)
- [V] Huang et al. 2025, m1 https://arxiv.org/abs/2504.00869 (d08)
- [V] Bi et al. 2025, thinking budget in medical reasoning https://arxiv.org/abs/2508.12140 (d09)
- [V] Moell et al. 2025, DeepSeek R1 medical reasoning https://arxiv.org/abs/2504.00016 (d10)
- [V] Liu et al. 2025, Understanding R1-Zero-like training https://arxiv.org/abs/2503.20783 (d11)
- [V] Tsui 2026, Self-correction blind spot https://arxiv.org/abs/2507.02778 (d12)
- [V] Kumar et al. 2024, SCoRe https://arxiv.org/abs/2409.12917 (d13)
- [V] Liu et al. 2024, Intrinsic self-correction ability https://arxiv.org/abs/2406.15673 (d14)
- [V] Zhang et al. 2025, Reasoning models know when they are right https://arxiv.org/abs/2504.05419 (d15)
- [V] Chen et al. 2024, HuatuoGPT-o1 https://arxiv.org/abs/2412.18925 (d16)
- [V] Samsel et al. 2026, sycophancy and diagnostic instability https://pubmed.ncbi.nlm.nih.gov/42721584/ (d17; abstract only)
- [V] Savage et al. 2025, uncertainty proxies https://pubmed.ncbi.nlm.nih.gov/39396184/ (d18; abstract only)
- [V] MedARC (Miao 2026) and MCC (Sun 2026) https://pubmed.ncbi.nlm.nih.gov/41109093/ (d26; abstracts only)
- [V] BMJ Digit Health AI, bias-inducing prompts https://pubmed.ncbi.nlm.nih.gov/42712292/ (b31)
- [V] Radiology cognitive bias 2026 https://pubmed.ncbi.nlm.nih.gov/41983923/ (b32)
- [V] Multi-agent conversations to mitigate cognitive biases, JMIR 2024 https://pubmed.ncbi.nlm.nih.gov/39561363/ (b33)
- [V] Simulated reasoning and self-verification in psychiatry, JMIR AI 2026 https://pubmed.ncbi.nlm.nih.gov/42258613/ (b34)
- [V] Reflective self-review for code-status extraction, JAMIA 2026 https://pubmed.ncbi.nlm.nih.gov/42901486/ (b35)

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 14 established claims: 7 confirmed as written, 7 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E01.07-K01** (reworded: the sources support less). Numbers confirmed (Staal g=0.20 across all tools, Prakash 0.38 for guided reflection only; 62% written-case and 31% visual tasks, 7% patients), but none of the opened sources states that many trials come from one lab network, and the 0.20 to 0.38 range mixes two different pools (all workplace tools versus guided reflection). Corrected claim: A structured second look at a held diagnosis (list findings for, against, expected-but-missing, then alternatives) raises human diagnostic accuracy by a small to moderate amount: Hedges g 0.20 across all workplace reasoning tools (29 studies) and effect size 0.38 for guided reflection specifically (44-study review). Most trials used written cases (62%) or visual tasks (31%); only 2 of 29 used real or standardised patients.
- **E01.07-K03** (reworded: the sources support less). Numbers confirmed (44.5 vs 45.0, N=204; CFS N=191), but the two trials are from the same McMaster group (Sherbino and Norman on both), and Sibbald and de Bruin 2012 found analytic instructions improved ECG re-reading scores (F=15, p<0.0001), contradicting the blanket claim. Corrected claim: In two trials from one research group, general instructions to be slow, careful and reflective did not raise diagnostic accuracy in residents (44.5 vs 45.0 percent, N=204) and cognitive forcing strategy training did not reduce bias errors in students (N=191); however, in one ECG study instructing residents to use an analytic strategy on re-reading did improve scores, so the evidence on plain instructions is mixed.
- **E01.07-K09** (reworded: the sources support less). Kaemmer 2021 supports 0.75 vs 0.49 (0.43 for the checklist without the answer is not visible in the abstract, only that it did not improve), but 'only when' generalises from one 90-student experiment; the review (Mamede and Schmidt) only says content-focused checklists appear to help, and Sibbald 2013 is a generic checklist. Corrected claim: In one randomised experiment (90 advanced students), a 17-item differential diagnosis checklist raised accuracy from 0.49 (control) to 0.75 when it contained the correct diagnosis, while a checklist lacking it did not improve accuracy and might slightly reduce it; reviews suggest content-focused checklists help more than process-focused ones.
- **E01.07-K11** (reworded: the sources support less). In Mamede 2019 only cued reflection beat free reflection (p<0.02); modelled reflection did not differ from free (p>0.05). The p<.001 and the worked-example result are from Fernandes 2021, which used worked examples, not 'faded' examples, and reports no expertise-reversal finding. Corrected claim: Guidance beats free reflection: cued reflection beat free reflection in novices (0.58 vs 0.41, p<0.02; modelled reflection did not differ from free reflection), and an independent group found that cued reflection and worked examples both beat free reflection (p<.001) in third- and sixth-year students, with no difference between cued and worked example.
- **E01.07-K13** (number corrected). Liu et al. Table (CommonsenseQA) gives GPT-4 84.11 to 73.55 under the error-presuming prompt (a 10.6-point drop); 66.34 is the GPT-3.5 figure under that prompt. All other numbers (Huang et al. Table 3, oracle, SCoRe 15.8/4.6) match. Corrected claim: Intrinsic LLM self-correction without an outside signal lowers accuracy (GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0 after five calls); earlier gains came from oracle labels deciding when to stop (GPT-3.5 GSM8K 75.9 to 84.3 with oracle). The sign depends on the prompt: a prompt that presumes an error cost GPT-4 about 10.6 points on CommonsenseQA (84.11 to 73.55; GPT-3.5 fell 75.92 to 66.34) while a neutral prompt left GPT-4 at 84.60; an untreated Gemini 1.0 Pro changed 15.8 percent of right MATH answers to wrong and 4.6 percent of wrong to right.
- **E01.07-K24** (reworded: the sources support less). Zhang 2025 (MAD wins at most about 15% of 36 settings against CoT), Wang 2024 and Tran 2026 support the claim, but Wunderlich 2026 (cited for CoT 64.3, SC 68.7) found same-model debate (70.0) beat self-consistency (68.7) at comparable compute and recommends multi-agent over single-agent, so 'same-model debate usually loses to sampling and voting' is contested; MoA there is not clearly different-model mixing. Corrected claim: At matched budgets, self-refinement usually does worse than sampling more first passes and voting, and several studies find multi-agent debate rarely beats chain of thought (no MAD method won more than about 15 percent of 36 settings against CoT) and loses to self-consistency, but results conflict: on MMLU-Pro (CoT 64.3, SC 68.7, self-refinement below CoT) one study found debate (70.0) and mixture-of-agents (71.4) beat self-consistency at comparable compute, and single-agent matched or beat multi-agent at equal thinking tokens on multi-hop QA.
- **E01.07-K30** (reworded: the sources support less). Both abstracts confirm 28 studies (limited to early-career doctors) and 13 of 87 debiasing studies aimed at professionals, but they do not state that no patient-outcome trial exists, that the studies used vignettes, or that curriculum studies measured only knowledge tests. Corrected claim: Reviews list 28 intervention studies on dual-process reasoning interventions (existing studies largely limited to early-career doctors, with heterogeneous measures), and only 13 of 87 health debiasing studies targeted health professionals, with transfer to real-life settings named as a main challenge.
- **E01.07-K07** (now single-source: only one opened source, code check).
- **E01.07-K08** (now single-source: only one opened source, code check).
