# Critiques of the story model: deep document

*Subfield E11.03. Sources: evidence_a-d.jsonl (ids a01-a26, b01-b25, c01-c28, d01-d17), claims.jsonl (K01-K28), critique.md in this folder. Status tags: [E] established, [S] single-source, [C] contested. Ids like a06 point to evidence lines.*

## 1. What it is

The story model (Pennington and Hastie, 1981 to 1993) says a juror builds one causal story from the trial evidence, learns the verdict categories, and picks the verdict whose definition best fits the story. The story is built from events, goals, actions and consequences. Gaps are filled by inference. Confidence follows three things: coverage of the evidence, coherence, and uniqueness (no good rival story) (a03, a09).

This subfield is about the critiques of that model. The OpenLearn summary (a01, a02) names three:

1. **Thin on deliberation.** A jury is more than the sum of its members. The page gives an illustration: a jury can move from 11-1 for conviction to 12-0 for acquittal. The model describes one mind, not a group.
2. **Assumes a formal process.** The model treats judgment as logical and rule-bound. It struggles with extra-legal factors such as values, emotion and identity.
3. **Unclear why story form matters.** The same cognitive model could be written as stories, code, a connectionist net or neural activity. The story form has no shown causal role beyond the structure it carries.

Why it matters for our agent: the subfield row says "Caution on scoring". The story model is a good source of ideas for building and checking an account from messy evidence. But its evidence base is narrow, and its group claims are weak. We should take the structure (coverage, rivals, completeness) and leave the prose form and the group story. We should also not read agreement or convergence in a panel as proof.

Scope: the founding studies with exact numbers, what replicated or failed, deliberation evidence that bears on the critique, and every LLM study found that tests or uses the idea (2023 to 2026). Earlier documents in this series cover the model itself and LLM jury work in general; see `00_FIELDS.md`, section "Deep research by subfield", and the other E11 folders. Links to parallel subfields (not covered here): Conformity; Social epistemology; Argument evaluation criteria; Formal argumentation frameworks (AI); Cognitive bias and premature closure; Belief updating; Debiasing and cognitive forcing; Aggregation and extremizing; Computational coherence models; Search over thoughts.

## 2. History and theories in depth

### 2.1 Founding studies (all about one person and one case)

- **Interview study** (Pennington 1981; Pennington and Hastie 1986) (a03). 26 jury-pool volunteers watched a filmed murder trial (Commonwealth v. Johnson) and talked aloud. A 16-juror subsample was analysed. Verdicts of the 16: 5 first-degree murder, 4 second-degree, 4 manslaughter, 3 not guilty. 85% of events in the protocols were causally linked. 55% of references were to events in testimony, 45% were inferred events. Character inferences were 5.4% of story content. Different verdict groups built different stories; a verdict story was the set of events and links shared by 80% of a verdict group. The authors say the interview itself may have demanded stories as justification.
- **Verdict learning ruled out** (a04). Memory for verdict-element relations, understanding of the verdict content, and reasonable-doubt thresholds did not differ by verdict group. Only story structure covaried with verdict.
- **Recognition-memory study** (Pennington and Hastie 1988) (a05). 119-sentence written case. Mock jurors falsely recognised inferred sentences that matched their own verdict story and rated evidence importance by its causal role in the story. Hit and false-alarm rates are not given in the chapter. The authors admit this does not prove the story causes the verdict.
- **Order-of-evidence experiment** (Pennington and Hastie 1992, reported in the 1993 chapter) (a06). 130 college students, 100 evidence statements (50 each side), forced choice murder vs not guilty. Percent guilty, prosecution order / defense order: story/story 59%, story/witness 78%, witness/story 31%, witness/witness 63%. Row means: prosecution in story order 69%, in witness order 47%. Column means: defense in story order 45%, in witness order 70%. The pattern: whoever's case came in story order did better. People who heard both sides in story order were most confident. The authors say the lab design (no opening or closing statements) cannot size the effect in real trials. Numbers re-confirmed from the chapter text in critique.md.
- **Order with a memory control** (a07). N=414 college students, written materials, cases from Devine and Ostrom (1985). Story order raised story clustering in free recall (ARC measure) and moved verdicts and confidence the expected way. Total recall was equal across conditions, so it was not a simple memorability effect. Per-cell verdict percentages are not given in the chapter.
- **Completeness and global versus item-by-item judgment** (a08). Adding story-completing supplements pushed guilt judgments toward the completed story. Judgments made once at the end were more story-driven than item-by-item judgments. Item-by-item ratings fit anchor-and-adjust (weights: current judgment .45, new block .55). Global ratings fit a story-weighted model. Bayesian aggregation of local ratings was about 10 times stronger than global ratings and about 15 times stronger than item-by-item ratings (subjects were very conservative). Global ratings were about 1.5 times stronger than final item-by-item judgments.
- **Civil extension** (Hastie, Schkade and Payne 1998; Hastie 2008) (a09, a10). Punitive-damages think-aloud. In the student sample (N=20): 15 (75%) relied mainly on narrative summaries, 3 (15%) on legal elements, 2 (10%) neither. 12 (60%) considered causation; 17 (84%) discussed one conduct element; 11 (55%) another; 6 (30%) malice or reasonableness. Coder agreement over 90%. Few jurors covered every element the judge listed.
- The authors' own limits statement (a26): the first four studies used one trial or one set of case materials; student or jury-pool samples; no deliberation measured.

### 2.2 The three critiques, with what has been added since

**Critique 1: deliberation.**
- Qualitative: Rossner (2019) (a11, a12) studied one 12-person mock deliberation. The model explains one juror's story, not how many private stories become a shared one. A juror's alternative story was first rejected and then accepted for testing after rapport built through humour and shared focus. Competing accounts were compared for fit by arguing about the credibility of expert witnesses. Single case, facilitator present.
- Base rates: Kalven and Zeisel (1966) is the source of "the first-ballot majority wins in about 90% of juries". We confirmed it only through Diamond et al. (2010) (d01): 90% of cases in a retrospective sample of 225 juror reports; Kalven and Zeisel called it a "radical hunch". Immediate first votes are rare: 21% (Diamond and Casper 1992), 28% (Hastie et al. 1983), 3% (Sandys and Dillehay 1995) to 31% (Devine et al. 2004) (d02). In the Arizona Filming Project (50 civil cases) only 20% voted in the first 10 minutes. 38% of jurors rated their leaning at 3, 4 or 5 on a 7-point scale before deliberation; 20% of jurors in 382 criminal trials said they only leaned during deliberation. So the 90% figure is weak. It neither shows deliberation does nothing nor that it does much.
- Hung rates (d03): lab studies 21% vs under 10% outside the lab. Devine et al. 2001: when at most three fourths of initial preferences favoured a verdict, 31% hung. Conviction threshold somewhat above two thirds (Davis et al. 1975: two thirds initial majority wins, else hang). We have not opened Devine et al. 2001 or Kalven and Zeisel directly.
- Threshold effects (b01, b02, b22): in 1,960 Louisiana trials (10 of 12 needed), under 1% ended 9 to convict but 17% ended exactly 10 (chi2=91.18, df=1, p<.001). Experiments (Study 2a n=261: chi2=9.20, p=.002; Study 3 n=1,633: beta=0.46, SE=.12; deservingness beta=0.49, p=.016) show being pivotal raises punitive votes. It did not raise acquittal votes (Study 2b n=298: chi2=0.03, p=.870). Observers blamed a voter who blocked a decision more than one who tipped it (Study 4 n=505, beta=0.29, p=.021). So the end of deliberation is shaped by wanting to close the decision.
- Minority washout (a14, b13): 35 people, 7 six-person online juries, 34 with paired data. Before: 28 guilty (82.4%), 6 not guilty (17.6%). After: all 34 guilty. Exact McNemar p=0.031. A confederate dissented in 6 juries. This is the reverse of the 11-1 to 12-0 picture and cannot separate argument from conformity. Pilot only. (a14 and b13 are one paper.)
- Social influence on how a narrative is used (b03, b24): a fellow deliberator urging use of a life-history narrative raised its effect on outrage and compassion; urging to ignore it did nothing. Student groups of 2 or 3 plus a scripted confederate.
- Misinformation in deliberation (a20, b04, b05, b12): Cullen et al. (2024). Study 1 N=275, Study 2 N=339. Misinformation from fellow jurors was often remembered as trial evidence. A judicial warning had no effect; only 11 participants (6.5%) could report it. The direction of bias flipped between Study 1 (pro-prosecution items more often misattributed, not re-verified) and Study 2 (pro-defense items more misattributed, skewed judgment toward the defense). A reanalysis (Xie 2026) found memory entry exceeded judgment impact.

**Critique 2: formalism.**
- Jurors cover the legal checklist only partly (a10, above).
- The answer menu changes the verdict (a21, b08): meta-analysis of 10 mock trials, 1,778 jurors. Three verdicts (guilty, not guilty, not proven) vs two: convictions 28.7% (259/901) vs 39.2% (344/877). OR 0.625, 95% CI [0.51, 0.77]. Risk ratio 0.732; risk difference -10.5 points. Q(9)=12.28, p=.198, I2=22.2%. Funnel test p=1.0. The OR is 37.5% lower odds, not "about 40%" as one source line says. Only the single civil trial was an outlier.
- The verdict procedure changes the outcome even after group deliberation (b09, b25): special-verdict form vs general verdict, Exp 1 N=267, Exp 2 N=292 who deliberated in groups. Special verdict shifted outcomes toward the defense. Reasons before or after a general verdict did not change decisions.
- Wording changes verdicts (b10): concrete negative attorney language raised liability (M=72.2 vs 53.0, d=0.65); abstract language removed it (64.5 vs 59.0, d=0.20, p=.25). N=273; interaction F(1,269)=4.02, p=.046, eta2=.014. The abstraction manipulation check failed (d=0.14, p=.26). Weak.
- Identity and emotion: sample matters (b11): rape-myth acceptance MTurk 2.74 vs students 1.72 (d=-1.04); victim race effect appeared only in MTurk (F(3)=7.33, p<.001, eta2=.011). Emotional encoding of narratives (a25) is a conceptual proposal.
- Perceived realism (b16, abstract only): in N=83 adults, the feeling of a coherent story was the strongest predictor of case-strength ratings. Preprint.

**Critique 3: why story form.**
- No experiment compares a story format with an equally coherent non-story format (a02; claim K21). We searched and found none (d17).
- Formal answer: Urbaniak (2017) (c16, c17, b20) turns the informal story criteria into checkable conditions: explaining evidence (each non-excluded item must be plausible under the accusing story), missing evidence, exclusion between rivals, decision, initial plausibility, exhaustion. It also lists evidential support, completeness, resiliency and narrativity. It defends the story approach against the Bayesian charge that plausibility is undefined, and explains the gatecrasher paradox: bare high probability is not enough, because statistics alone are not a story. Pure theory; no tests.
- Simon, "Thin empirics" (a13, abstract only): the story model is "too narrow a foundation" for a general model of fact-finding. Year and venue unconfirmed.
- Coherence-based accounts (a24, b12): treat the story as part of a coherence process in which evidence and preference reinforce each other and shift before the verdict.

### 2.3 Replication status of the central result

The one causal test (story order vs witness order) has a cited replication (Smith 1988, story vs legal-issue order) that we could not locate (d17). No failed replication was found either. A search snippet said a 2008 dissertation reported a reversal between student and community samples; the page returned 403, so that is unverified. Later order work in legal judgment (Troop and Lagnado 2025, b06) is about moral-case order, not story order, and finds asymmetric and sometimes reversed effects. So the story-order effect is single-study.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Founding evidence is individual, single-case, no deliberation | Interview N=26 (16 analysed); order study N=130; N=414 | a03, a26 | [E] |
| Story order vs witness order changes individual verdicts | % guilty 59/78/31/63 across four cells; row means 69 vs 47; column means 45 vs 70; N=130 | a06 | [S] single study; replication not opened |
| About 45% of story content is inferred | 55% testimony, 45% inferred; 85% of events causally linked; N=26 (16 analysed) | a03 | [S] |
| Order effects in legal judgment are asymmetric and can reverse | 5 studies, n=1,023 | b06 | [E] for "order matters, direction varies" |
| Jurors cover the legal checklist only partly | 75% narrative (15/20); 84% one conduct element; 30% malice | a10 | [E] (with a01) |
| Three-verdict system lowers conviction | OR 0.625 [0.51, 0.77]; 28.7% vs 39.2%; 10 trials, 1,778 jurors; I2=22.2% | a21, b08 | [S] one meta-analysis |
| Special verdict vs general verdict shifts outcome, also in groups | Exp 1 N=267, Exp 2 N=292; 66.2% plaintiff overall in Exp 1 | b09, b25 | [S] |
| Louisiana threshold pile-up | n=1,960; under 1% at 9; 17% at exactly 10; chi2=91.18 | b01 | [S] observational |
| Pivotal voting raises punishing, not acquitting | 2a n=261 chi2=9.20; 2b n=298 chi2=0.03; Study 3 n=1,633 beta=0.46 | b02 | [S] |
| Minority washout in a pilot | 6/6 not-guilty voters became guilty; 34 paired; McNemar p=0.031; 7 juries | a14, b13 | [S] pilot |
| Warnings fail; misinformation remembered as evidence | N=275, N=339; 6.5% (11) could report the warning | a20, b04, b05 | [E] |
| First-ballot majority matches verdict | 90% of 225 retrospective reports; immediate votes 3% to 31% of juries | d01, d02, b18, b19 | [E] as a weak secondary figure |
| Lab hung rate above real | 21% lab vs under 10% real; 31% when at most 3/4 initial majority | d03 | [S] secondary |
| Inadmissible-evidence effect failed to replicate | Study 2 n=624: 43.5% vs 46.5% vs 37.2% vs 44.7%; chi2(3)=3.14, p=.371; OR 1.05; package vs instruction OR 1.47, one-tailed p=.049 | b07, b23 | [S] failed replication |
| LLM jurors seeded 11-1: almost no movement | 17/18 hung; GPT-4o 9/9; N=3 per cell; temp 0.9 | a16, c01, d09 | [C] |
| LLM debate no better than self-correction, costs more | Ministral GSM-Hard 20.7% vs 48.3%; tokens 23,816 vs 10,707; majority vote 77.35% both arms, +57% tokens | c08, d10, c09, d12 | [E] |
| One dissenter breaks fake consensus | 80.25% yield at 4v0 vs 12.75% at 3v1 (user role); 97.50% vs 60.25% (assistant role) | c10, d11 | [E] (factual QA only) |
| Prose open-mindedness instruction is model-dependent | Llama 2.0 to 6.0 vote changes; GPT-4o 1.0 to 1.0 | a17, c02 | [E] as "unreliable lever" |
| Pushback flips LLM judges | 25-71% static; 62-91% adaptive persuader; mechanical wiggle 2-9% | c13, c28 | [S] |
| Recency in evidence order in LLMs on legal tasks | GPT-4o F(1,711)=424.76; GPT-5.2 F(1,711)=71.24; N=720 per model per condition; prompts did not fix it; PE3 beta=0.39 | d04, d05, d06 | [E] (2 independent studies) |
| Coded coverage audit raised consistency (synthetic) | Coverage 0.9014 vs 0.8436 without audit; +20.35% consistency | c20 | [S] |
| List-then-verify improves omission detection (non-legal) | Paired discrimination 0.79-0.94 added content vs 0.50-0.63 omissions (monolithic); single call 36.9% vs 24.6% (p=0.002) | d15 | [S] |
| Choice-supportive bias in LLMs | Change of mind 32.5% (answer hidden) vs 13.1% (shown), p=0.002 | d07 | [S] analogy |
| No LLM test of story-model predictions | none found | b21, c22 | negative result, limited search |

## 4. Mechanisms and models

Each mechanism is stated so it can be coded.

### 4.1 Story-building (the base model)
Input: a case file (list of evidence items). Output: an account = ordered events with causal links, goals, and a set of inferred events. Code form:
- `events[]`, each with `source_ref` (a pointer into the evidence) or `inferred=true`.
- `links[]` (cause to effect).
- `verdict_map`: for each answer option, the required elements.
The 45% inferred share means any real account holds many unsourced items. Rule: count `inferred` items, require each to carry a stated basis, and have code verify each against the source text (guards against the false-recognition effect in a05).

### 4.2 Three certainty principles, made checkable (Urbaniak 2017; c16, c17)
For each candidate story s and each evidence item e:
- **Coverage**: `plausible(e | s)` is true, false or unknown, judged item by item. Coverage score = share of items plausible under s. Items with unknown status are listed as missing evidence.
- **Exclusion**: does a rival forbid anything the first story requires? Record contradictions as pairs.
- **Exhaustion/uniqueness**: have the live rivals been named, and does any rival cover at least as many items?
- **Decision**: each story must state its answer, so every story maps to exactly one option.
This is a scorer, not a narrative. It is the useful part of the story model without the story form.

### 4.3 Order and presentation (a06, a07, d04, d06)
Model: answer = f(evidence set) + g(order). Estimate g by running the same item under k random orders (and under story vs source order) and recording flips. If the flip rate is high, the answer is low confidence. Recency is the observed direction in LLMs (last-listed incriminating evidence or last-listed party favoured). Prompts did not remove it, so the control is structural (permute and compare), not an instruction.

### 4.4 Judge once, from the built account (a08)
Item-by-item rating fits anchor-and-adjust (.45 current, .55 new) and is driven by order. Global judgment after building is more story-driven. The schema already judges once after build; this evidence says running item-wise scores adds order dependence.

### 4.5 Group dynamics a single-mind model misses
- Threshold/pivot effect: if a stop rule or quorum exists, belief can bend toward the answer that ends the process (b02).
- Conformity: a majority plus pressure moves the minority (a14); LLM analog: fake consensus moves a subject unless one dissenter exists (c10).
- Source confusion: claims from others get remembered as evidence (a20). Code form: attach `origin` (evidence / peer / own inference) to every claim; the scorer uses only `origin=evidence` items as support.
- Closure: causal reconstruction fails mainly by closing hypotheses early (b14). Code form: keep at least two live hypotheses until a named discriminating test has run.

### 4.6 Measuring whether anyone moved (c15, c09)
Log vote-change tuples, first-flip order, changes per turn. A flip counts as a valid revision only if tied to a failing check or new evidence (c09: 36.98% of pairs change under self-reflection alone; of pairs stable there, 29.30% adopted a peer answer).

### 4.7 Coherence shift (a24, d07, b16)
Evidence is rated higher after the favoured answer is formed. Code form: two passes. Pass 1 rates each item blind to any candidate answer. Pass 2 forms the answer. Compare pass-1 ratings with ratings made after exposure; the gap measures the shift. The LLM analog is choice-supportive bias: showing the model its own earlier answer cut change-of-mind from 32.5% to 13.1% (d07).

### 4.8 Weak-rival backfire (a09, d16)
A weak case for one side can raise confidence in the other. Code form: score the strength of a generated rival before it is shown; if weak, do not count it as a test of the favourite. Numbers unavailable (abstract only).

## 5. What holds up

**Holds up (human):**
- Building a causal account is common, and accounts differ by verdict (a03). Single case, single lab; the interview may have invited it.
- Order and format of evidence move verdicts (a06, a07, b06). The specific story-order effect is single-study; general order sensitivity is repeated, with direction varying (b06).
- Legal checklists are only partly covered (a10; students N=20 only).
- Answer menu and verdict procedure move outcomes (a21, b09, b25). One meta-analysis plus two experiments.
- Warnings and instructions do little: judicial warning (6.5% could report it; a20), instruction to disregard evidence (b07), open-mindedness line in LLMs (c02).
- Misinformation from others is remembered as evidence (a20, b04, b05, b12), though the direction flipped between studies.

**Failed or weak:**
- The inadmissible-evidence effect failed to replicate in Neal et al. (b07): OR 1.05, p=.823. Do not assume a famous bias exists in a new sample.
- The Neal package result rests on a one-tailed p=.049 (two-tailed .098).
- The abstraction manipulation failed its check (b10).
- Order direction reversed between studies (b06).
- Reversal by sample (students vs community) for story order: unverified (d17).
- The 90% first-ballot figure is weak (d01, d02).
- No replication of the story-order effect located (d17).

**Moderators seen:** sample (students vs MTurk, d=-1.04 on rape-myth, b11); rape-myth belief (a20); case type (civil outlier in a21); whether a fellow deliberator advocates a narrative (b03); time limits (lab hung rate inflated, d03).

**Interventions that worked:** the four-part package for inadmissible evidence (weak, one-tailed; b07, b23); special-verdict forms shift outcomes (b09; shift is not the same as improvement). **Did not work:** judicial warning (a20), disregard instruction (b07), an authority label judge vs AI (b12, equivalent to zero within a preset bound in Study 2).

**Reading of the critiques:** the formalism critique has the best support (checklist coverage, answer menu, procedure, wording). The deliberation critique rests mostly on indirect evidence (conformity, pivotal voting, misinformation). The story-form critique is unanswered: no experiment compares story format with an equal non-story structure.

## 6. Language models

### 6.1 Is the story model tested on LLMs? No.
Searches found no study of story building, story ordering, story completeness, or story-vs-source order on language models (b21, c22, d17). JuryBench notes that earlier simulators start from written judgments, so facts are conclusive (c21). Nearest work is below. Search budget was limited; other databases may hold more.

### 6.2 Order effects on legal judgments (nearest to the story-order test)
- Bessis et al. (2026) (d04, d05): six simplified criminal cases, N=720 trials per model per condition, temperature 1. Incriminating evidence last raised guilt ratings. GPT-4o: order F(1,711)=424.76, p<.001; rating-condition F(1,711)=181.11; order x rating F(1,711)=43.75. GPT-5.2: order F(1,711)=71.24 (smaller), rating-condition F(1,711)=8.43, p=.0038. At T=0.2 case means correlated r=.996 and .989 with the main run. Four prompts (baseline; legal-expert; reason carefully; reason carefully and justify from case elements): the GPT-5.2 order effect stayed significant in all (F(1,2859)=574.40). The justify prompt (PE3) made it larger (beta=0.39, SE=0.07). Evaluation bias rose under PE1 (beta=0.16, p=.018) and PE3 (beta=0.23, p<.001). Only OpenAI models; no chain-of-thought arm by design.
- Liu et al. (2025) LFPBench (d06): 657 Chinese civil cases; six LLMs favoured the party whose evidence was listed last. Example: GPT-4o accuracy 42.19 (plaintiff last) vs 48.80 (plaintiff first) (row alignment uncertain; only direction relied on).

### 6.3 Deliberation among LLMs
- Ersoz (2026), 12 Angry AI Agents (a16-a18, c01-c03, d09): 12 persona jurors seeded 11-1. 2 models (GPT-4o, Llama-4-Scout), 3 conditions, N=3 per cell = 18 runs, T=0.9, up to 150 turns, hung after 3 vote rounds with no change. 17 of 18 hung. GPT-4o 9/9 hung. Llama: 8 hung, 1 unanimous not guilty (no-initial-vote condition, 64 turns, 6 changes). Mean vote changes: GPT-4o 1.0 / 0.7 / 1.0 (baseline / no initial vote / open-minded); Llama 2.0 / 3.3 / 6.0. All runs cited the same five core evidence items. No agent deviated from its assigned vote at the first check. The author blames RLHF intensity, but the design confounds it with model family, persona and temperature; the persona stayed in the no-vote arm. Treat 17/18 as a statement about this setup [C].
- Debate does not beat cheap baselines: Bertalanic and Fortuna (2026) (c08, d10, c24): Qwen2.5-7B, Ministral-3-8B, Llama-3.1-8B; 10 agents; 3 rounds. Ministral GSM-Hard debate 20.7% vs self-correction 48.3% (p<0.001) vs zero-shot 24.7%; tokens 23,816 vs 10,707. Ministral MMLU-Hard 62.0% vs 65.3% (p=0.002). Qwen MMLU-Hard 60.7% vs 66.7% (p<0.001). Llama 45.0% vs 47.7%, p=0.131 (not significant). Modal sycophancy up to 85.5%; oracle gap up to 32.3 points (right answers produced then discarded). Conformity at 2 agents 69.4% vs 73.4% at 9 (Qwen GSM-Hard); more agents or higher temperature did not help.
- Hao et al. (2026) (c09, c27, d12): GPT-4o, MMLU-Pro disagreement questions, 5,200 agent-question pairs. 36.98% changed answer under self-reflection alone; 29.30% of the rest adopted a peer answer. Majority-vote accuracy 76.22% (round 0), 77.18% (stance only), 77.35% (self-reflection), 77.35% (full reasoning); paired difference 0.00 pp, 95% CI [-0.59, +0.59]; tokens 4,469 vs 7,019 (+57%). A predictor that blocked likely adopters suppressed good and bad adoption alike; no accuracy gain.
- Wynn et al. (2025) (c07, c25): debate can fall below majority vote; flip-to-wrong rises with the number of agreeing agents; social pressure dominates over sycophancy and sequential revision (table values not transcribed).
- Choi et al. (2025) (c11): 2,500+ debates; conformity rose with majority size and agent capability.
- Sachdeva and van Nuenen (2026) (c12): 15,000 debates on moral dilemmas. GPT-4.1 revised 0.6-3.1% vs 28-41% for Claude and Gemini (synchronous). Who spoke first decided outcomes (Claude first: round-1 end near 90%; GPT first: about 40%).
- Positive cases: CyberJurors (c19): a 17-juror simulation with per-juror structured reasoning and precedent beat single models on 6,000 e-commerce disputes (+9.48% over LLMs, +6.19% over court simulators; sellers win 62.6%); gains from jury and precedent are bundled. AgentsCourt (c18): +8.6% and +9.1% F1 on legal article generation, from debate plus retrieval, using finished judgments. Zhu et al. (d14): diverse starting answers and confidence-modulated updates beat vanilla debate and majority vote (table values not extracted).

### 6.4 Peer pressure and dissent
- Kumarappan and Mujoo (2026) (c10, c26, d11): Llama-3.1-8B-Instruct, 400 MMLU humanities questions. User-role framing: yield under 13% for 0 to 3 wrong peers, 80.25% at 4v0, 12.75% at 3v1. Assistant-role: under 7% up to 2 wrong, 60.25% at 3v1, 97.50% at 4v0. Cross-framing gap at 3v1: 47.5 points. Dissenter rescue cut yield 54-73 points (67.50 pp at the cliff, N=4). "3 out of 3" (82.25%) beat "100 out of 100" (64.75%); a bare declarative line alone gave 64.00%. Base models show the same pattern (Qwen2.5-7B base 92.1% vs Instruct 43.2%), which argues against a pure RLHF explanation. Adaptive weak-dissenter attacks added 8.50 to 23.25 points.
- Ni and Zou (2026) (c14): hiding the agent's earlier answer raised Qwen3.5-4B's giving-in from 8% to 89%.
- Jagged Judges (2026) (c13, c28): nine judges, 14 tasks; verdicts flip 25-71% under static pushback and 62-91% under an adaptive persuader; mechanical wiggle only 2-9%. First-challenge flips: GPT-5 32%, Claude 4.6 Sonnet 26%, Gemini 3.1 Pro 7%, Grok-4.1 9%. "Three independent reviewers disagree" cut retention to 73% at turn 1.
- Singh et al. (2026) (b17, abstract only): a random third-annotator label moved verdicts +6.5 pp (Claude Opus 4.7) and +9.3 pp (Gemini 3.5 Flash); false-valued cues +10.5 / +16.7 pp; GPT-5.5 resisted.
- Dutta and Moharir (2026) (d08): targeted challenge reversed 49% of judge decisions; 64% of reversals harmful; authority framing most destabilising.
- Kumaran et al. (2025) (d07): Gemma 3 12B, 2,000 questions x 36 conditions; change-of-mind 32.5% vs 13.1%; with opposing advice 85.0% (hidden) vs 39.2% (shown).
- Hu et al. (2026) (d13): at a matched 960-token ceiling no protocol wins everywhere (each of four cells had a different best); oracle routing +14.0 and +13.7 pp on MuSiQue; vote-entropy escalation +1.6 pp combined (p=0.125, not significant).

### 6.5 LLM juror simulations (single-juror step)
JuryBench (Wu 2026) (a19, c04-c06, c21): 20 frontier LLMs, about 432K decisions, 500 controversial cases. Statement effect (severity drop on a 0-15 scale): Gemini 3 Flash +0.549, GPT-5 Mini +0.327, Grok-4.3 +0.305; Qwen3 -0.592, Claude Opus 4.6 -0.385, GLM 5 -0.384. In most rows 66-86% of verdicts did not change. Hurt rate exceeded success rate in most models. Background match drove change more than emotion or remorse. Conservative jurors showed larger post-statement change in about 70% of models. 12 human raters on 25 cases tended to get harsher (emotion 0.173, remorse -0.168, both p<0.05 but above 0.01). It tests the single-juror step only.

### 6.6 Coverage and audit
- VeriScene (Fu et al. 2026) (c20): cite every claim, then audit. Coverage 0.9014 (0.8436 without the fusion audit), factual consistency 0.7217; +20.35% factual consistency and +34.88% temporal coherence over the end-to-end baseline (which has zero coverage by construction). 25 scenarios, 20 test scenes, $1.82 per scene. Synthetic scenes.
- Fox et al. (2026) (d15): clinical notes, 500 pairs (298 omissions). Listing what the source establishes, then closed present/absent checks. Paired discrimination 0.79-0.94 on added content vs 0.50-0.63 on omissions (monolithic judges). Single-call evolved prompt 36.9% vs pipeline 24.6% of flawed notes (p=0.002), false alarms 6.2% vs 2.7%, about a tenth of the cost. Judge task, not reasoning accuracy.

### 6.7 What changed behaviour, by how much
- Evidence order: large (F 71 to 425), not removed by prompts, made worse by "justify from the case" in GPT-5.2.
- Persona-seeded group chat: almost no change; a prose open-mindedness line helped one model.
- A structured dissenter: -54 to -73 points of yield on factual QA.
- Keeping the agent's own answer visible: giving-in 8% vs 89% when hidden (Ni and Zou, small model).
- Debate vs self-correction: weaker, and 2 to 3 times more tokens in small models.
- Explicit list-then-verify: better omission detection in a non-legal judge task.

## 7. What our agent should take

Status key: [E] established (two or more independent sources, or replicated), [S] single-source, [C] contested.

### Add now (established)

1. **Order check on evidence-bearing items.** Run each item with 2 or more evidence orders; a flip lowers confidence and feeds the impasse detector, not a rewrite. Part: G4 / S7. [E]. Evidence: d04, d05, d06, b06, a06; claims K03, K24.
2. **Do not count agreement or convergence as proof, and do not count a changed answer as a win.** A revision is valid only when tied to a failing check or new evidence; log why an answer changed. Part: G2, G4 (G9 for debate). [E]. Evidence: c09, c27, a15, c07, c08, d12; K12, K15, K25.
3. **Doubt by code signal, not by a prose line.** An "open-minded" or "be careful" prompt is model-dependent and can raise bias (PE3 beta=0.39). Part: G1. [E]. Evidence: a17, c02, d05, c13; K14.
4. **Source tags on every claim** (evidence / own inference / other attempt); only evidence-tagged claims count as support; a reminder prompt does not protect. Part: S1 input hygiene, G3. [E]. Evidence: a20, b04, b05, b12; K10.
5. **Keep early closure out: two live hypotheses until a named test separates them.** Part: S5/S6 (impasse and rival), S7. [E]. Evidence: b14, a09; K20.
6. **Check every required element by code** (not only the story). Part: S7. [E] for the problem (checklist coverage is partial), [S] for the remedy (see Test first). Evidence: a10, a01; K05.
7. **Fix and report the answer menu.** Option set and wording held constant across arms. Part: S8 / bench design. [E] as an experimental control. Evidence: a21, b08, b09, b25; K06, K07 (the effect size itself is [S]).
8. **No group-story claims for single-agent output; no debate.** Already G9; this subfield adds the human side (pivotal pressure, washout) and LLM side (d10, d12). Part: G9. [E]. Evidence: c08, c09, d10, d12, a14.
9. **Record the true first answer before any critique step** and report the final = first rate. Part: S4 / S9 (memory). [E] as logging; real-jury base rates are biased because juries rarely vote immediately. Evidence: d01, d02, d03; K22.
10. **Rate evidence blind to the candidate answer; do not show the model its own earlier choice before it rates support.** Part: G5. [E] for the analog (d07, 32.5% vs 13.1%), [C] for direct evidence-rating shifts in LLMs. Evidence: d07, a24, b16; K23.

### Test first

1. **Story order vs source order vs matched causal list** (K02, K28, K21). Part: S1/S2, O6. [S].
2. **Coverage audit with citations** (VeriScene-like) as an S7 scorer at equal tokens (K19). [S].
3. **Urbaniak criteria as code**: per-item plausibility under each rival, missing-evidence list, exclusion check (K18). [S].
4. **Protected dissent slot vs code-triggered recheck** in any multi-attempt step (K13, K26). [S]; measured only on factual QA.
5. **Vary answer-menu size** to see how large our own sensitivity is (K06). [S].
6. **Weak-rival backfire**: score a self-generated rival before showing it (K27). [S], abstract only.
7. **Element-wise vs holistic answering** of the same item; log disagreement (K07). [S].
8. **Strip persona and identity cues** from scoring steps (K16). [S].
9. **Pivot or stop-rule effect**: log belief before the stop rule (K08). [S], human only.

## 8. Concrete tests on our bench

All arms run at equal total tokens. Count setup cost. Use 100 or more items for yes/no effects (K26 shows 1 to 2 pp effects are not detectable at small N).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Evidence-bearing items (case files, multi-clue puzzles) | A: plain; B: 2 permuted evidence orders plus code vote; C: B plus flip flagged as low confidence and rechecked | Accuracy; order-flip rate; accuracy on flipped vs unflipped items | Flip rate 5 to 25%; flipped items markedly lower accuracy; B at least equal to A |
| T2 | Same items | Presentation: chronological-causal; by-source; matched structured causal list (not prose) | Accuracy; flip rate; confidence | Small to moderate gap for chronological/causal if the S&H effect carries; list equals story if only structure matters (answers K21) |
| T3 | Items with a required element list | A: plain; B: story-only account then answer; C: account plus code-checked element coverage with one revision | Accuracy; share of elements covered | C above B by several points; if B equals A the story step adds nothing |
| T4 | Items with several plausible answers | A: plain; B: rival list with per-item plausibility under each (Urbaniak form); C: B with a weak rival injected | Accuracy; flip to wrong | B above A on items with real rivals; C shows backfire if K27 holds |
| T5 | Items with a planted wrong peer or prior-attempt answer | A: no dissent slot; B: protected dissent slot; C: code-triggered recheck on attempt disagreement | Wrong-adoption yield; accuracy; tokens | B and C both cut yield; C cheaper; head-to-head open (K26) |
| T6 | Items with a fixed menu | 2-option vs 3-option (add "unclear") vs original | Accuracy; abstain rate; flip between menus | Shift of several points; tells us what to report |
| T7 | Items with a candidate answer | A: rate evidence with candidate shown; B: rate evidence blind, then show candidate | Rating gap; accuracy | Gap above 0.3 points on a 5-point scale if coherence shift exists in LLMs |
| T8 | Our past run logs | Log first answer before any critique; compute final = first rate | Share first-answer retained; accuracy of changed vs unchanged | Retained above 85%; changed-answer accuracy below unchanged unless tied to a check |
| T9 | Items with persona cues added | With vs without cues in the scoring step | Verdict invariance | No change after stripping; change with cues in some models |
| T10 | Items with peer text | A: warning prompt; B: code tag; C: none | Share of peer claims treated as evidence | B below A below C |

## 9. What does not transfer, and why

- **Jury group results.** Pivotal-vote thresholds (b01, b02), minority washout (a14) and rapport-based acceptance of a story (a11) depend on social cost, face and time pressure. A single agent has none; separate attempts are not a group.
- **The 90% first ballot.** A weak secondary figure from retrospective reports (d01, d02). Not usable as a base rate for an agent.
- **Student-sample order-effect size.** Real trials have opening and closing statements; the authors say the lab study cannot size the real effect (a06). The 31-78% range will not be our effect.
- **The story's emotional pull.** Emotion and identity effects (a25, c04, c05) are a risk to control in a scorer, not a feature. A story told with more feeling is not a better-supported story (c04).
- **LLM persona deliberation as a measure of deliberation.** Ersoz persona agents hold assigned votes; the result says little about neutral agents (c23, d09).
- **Model-judge scoring of story quality.** Judges conform to cues and flip under pushback (c13, d08); G5 and G10 already bar this.
- **Debate results from civil-law judgment simulators.** AgentsCourt uses finished judgments, so facts are conclusive (c18, c21).
- **Non-legal analogs.** Choice-supportive bias (binary geography), omission blindness (clinical notes), conformity on MMLU (factual QA) show mechanisms, not legal effects.
- **Human sample moderators** (rape-myth, race, student vs MTurk) belong to human data (b11).

## 10. Open questions

1. Does story order beat source order for LLMs, and does a matched non-story structure do equally well? (K02, K21, K28)
2. Does a coded coverage or Urbaniak check raise accuracy at equal tokens? (K18, K19)
3. Why did 17 of 18 LLM juries hang: persona, temperature, RLHF or stop rule? (K11)
4. Protected dissent vs code-triggered recheck at equal tokens. (K26)
5. Do LLMs shift evidence ratings toward a favoured answer, and does blind rating remove it? (K23)
6. Does a weak self-generated rival strengthen the favourite in LLMs? Exact McKenzie et al. numbers. (K27)
7. Smith 1988 and other replications of the story-order effect; any failed replication. (K28)
8. Real first-ballot match rate from direct sources (Kalven and Zeisel; Devine et al. 2001).
9. Why does order direction differ across human studies (b06)? Does it differ across LLMs?
10. Does the dissenter effect hold on evidence-weighing tasks, not only factual QA?

## 11. Sources

[V] = opened (this session or the earlier run); [M] = snippet or abstract only or recalled.

- [V] OpenLearn, Jury decision making: what's the story? https://www.open.edu/openlearn/society-politics-law/law/jury-decision-making-whats-the-story (a01, a02)
- [V] Pennington and Hastie (1993), The story model for juror decision making, ch. 8 in Inside the Juror. https://www.marcellodibello.com/legal-probabilism/readings/Hastie-story-model.pdf (a03-a08, a26)
- [V] Hastie (2008), What's the story? Explanations and narratives in civil jury decisions. https://beckassets.blob.core.windows.net/product/readingsample/443373/9780387744889_excerpt_001.pdf (a09, a10)
- [V] Rossner (2019), Storytelling Rituals in Jury Deliberations. https://opo.iisj.net/index.php/osls/article/download/1066/1203/0 (a11, a12)
- [M] Simon, Thin empirics. https://vlex.co.uk/vid/thin-empirics-874265572 (a13; excerpt only)
- [V] Cohen and Berryessa (2026), dissenting voter pilot. https://pmc.ncbi.nlm.nih.gov/articles/PMC13701490/ (a14, a15, b13)
- [V] Ersoz (2026), 12 Angry AI Agents. https://arxiv.org/abs/2605.01986 (a16-a18, c01-c03, c15, c23, d09)
- [V] Wu (2026), JuryBench. https://arxiv.org/abs/2609.09887 (a19, c04-c06, c21); read in part
- [V] Cullen et al. (2024), misinformation during deliberation. https://pmc.ncbi.nlm.nih.gov/articles/PMC10853387/ (a20, b04, b05)
- [V] Verdict system meta-analysis (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC11774159/ (a21, b08)
- [M] Hastie, Penrod and Pennington (1983), Inside the Jury. https://www.hup.harvard.edu/books/9780674454620 (a22; cited only)
- [M] Devine et al. (2001), 45 years of research on deliberating groups. https://doi.org/10.1037/1076-8971.7.3.622 (a23, b19; not opened, figures via Diamond et al.)
- [V] Xie (2026), Legal Evidence-Authority Dissociation. https://pmc.ncbi.nlm.nih.gov/articles/PMC13719418/ (a24, b12)
- [V] (Dis)passionate law stories (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9321950/ (a25)
- [V] Davenport and Winet (2022), Pivotal voting. https://europepmc.org/article/PMC/PMC9371710 (b01, b02, b22)
- [V] Gill and Zungu (2023). https://europepmc.org/article/PMC/PMC10656008 (b03, b24)
- [V] Troop and Lagnado (2025), case order effects. https://europepmc.org/article/PMC/PMC12466634 (b06)
- [V] Neal, O'Hara et al. (2025), inadmissible evidence. https://europepmc.org/article/PMC/PMC11761953 (b07, b23)
- [V] Burd et al. (2025), verdict procedures. https://europepmc.org/article/PMC/PMC12729272 (b09, b25)
- [V] Attorney language abstraction (2025). https://europepmc.org/article/PMC/PMC12562236 (b10)
- [V] St. George et al. (2026), student vs MTurk. https://europepmc.org/article/PMC/PMC13084973 (b11)
- [V] Forensic Science International: Synergy (2022). https://europepmc.org/article/PMC/PMC9136362 (b14)
- [V] Rape myth education systematic review (2024). https://europepmc.org/article/PMC/PMC11545151 (b15)
- [M] Perceived realism in juror decision making (preprint). https://doi.org/10.31234/osf.io/axgv2_v4 (b16)
- [M] Singh et al. (2026), Suggestible judges. https://doi.org/10.21203/rs.3.rs-10688342/v1 (b17)
- [M, recalled] Kalven and Zeisel (1966), The American Jury (b18); Allen and Pardo, Heller on relative plausibility (b20)
- [V] Wynn, Satija, Hadfield (2025), Talk Isn't Always Cheap. https://arxiv.org/abs/2509.05396 (c07, c25); table values not transcribed
- [V] Bertalanic and Fortuna (2026), Cost of Consensus. https://arxiv.org/abs/2605.00914 (c08, c24, d10)
- [V] Hao et al. (2026), Not All Flips Are Conformity. https://arxiv.org/abs/2606.00820 (c09, c27, d12)
- [V] Kumarappan and Mujoo (2026), Not Just RLHF. https://arxiv.org/abs/2605.12991 (c10, c26, d11)
- [V] Choi et al. (2025), Group conformity. https://arxiv.org/abs/2506.01332 (c11)
- [V] Sachdeva and van Nuenen (2026), Interaction protocol. https://arxiv.org/abs/2510.10002 (c12)
- [V] Jagged Judges (2026). https://arxiv.org/abs/2608.12645 (c13, c28)
- [V] Ni and Zou (2026), Silent Dissent. https://arxiv.org/abs/2610.02702 (c14)
- [V] Urbaniak (2017), Reconciling Bayesian epistemology and narration. https://arxiv.org/abs/1707.08763 (c16, c17)
- [V] He et al. (2024), AgentsCourt. https://arxiv.org/abs/2403.02959 (c18)
- [V] Sun et al. (2026), CyberJurors. https://arxiv.org/abs/2605.28369 (c19)
- [V] Fu et al. (2026), VeriScene. https://arxiv.org/abs/2609.08342 (c20)
- [V] Diamond et al. (2010), cognitive perspective on jury deliberation. https://link.springer.com/content/pdf/10.3758%2FPBR.17.2.174.pdf (d01-d03)
- [V] Bessis et al. (2026), Legal decision biases in GPT. https://openaccess.city.ac.uk/id/eprint/37200/1/behavsci-16-00437-v2.pdf (d04, d05)
- [V] Liu et al. (2025), Legal Fact Prediction. https://arxiv.org/pdf/2409.07055 (d06)
- [V] Kumaran et al. (2025), change of mind in LLMs. https://arxiv.org/pdf/2507.03120 (d07)
- [V] Dutta and Moharir (2026), Stability vs manipulability. https://arxiv.org/pdf/2606.05384 (d08)
- [V] Hu, Shen and Lakshmipathi (2026), matched-ceiling study. https://arxiv.org/pdf/2605.09618 (d13)
- [V] Zhu et al. (2026), Demystifying multi-agent debate. https://arxiv.org/pdf/2601.19921 (d14; table values not extracted)
- [V] Fox et al. (2026), omission blindness. https://arxiv.org/pdf/2608.31016 (d15)
- [M] McKenzie, Lee and Chen (2002), JBDM 15. https://zendy.io/title/10.1002/bdm.400 (d16; abstract only)
- [M] Search records for gaps 4 and 6 and a dissertation snippet (403) (d17); search note (b21, c22)
