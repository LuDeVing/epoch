# Pragma-dialectics: deep document

*Subfield D04.04. Key works: van Eemeren and Grootendorst (1984, 1992, 2004). Relevance to our single agent: background only (the theory is about two or more parties). Evidence files: evidence_a-d.jsonl (ids a01 to d21), claims.jsonl (K01 to K27), critique.md. Written 2026-11-20. Search coverage was limited (APIs rate-limited, web budget spent), so "not found" means "not found here".*

## 1. What it is

Pragma-dialectics is a theory of argumentation from the Amsterdam school. It treats argument as a way to resolve a difference of opinion by reasonable discussion.

- Argumentation is a speech-act exchange between a protagonist (who holds a standpoint) and an antagonist (who doubts it).
- An ideal procedure called the **critical discussion** has **four stages**: confrontation, opening, argumentation, concluding.
- **Ten rules** govern the procedure: freedom, burden of proof (obligation to defend), standpoint, relevance, unexpressed premise, starting point, argument scheme, validity, closure, usage (a02).
- A **fallacy** is any violation of one of the rules. It need not be formally invalid and need not look valid (a03).
- **Strategic maneuvering** (van Eemeren and Houtlosser, 2006) adds rhetoric. Arguers want to be reasonable and effective at once. A fallacy is a derailment of strategic maneuvering (a04).
- The theory claims two kinds of validity for the rules. Problem-solving validity is argued by philosophy. Conventional validity (ordinary people accept the rules) is tested by experiment (b05).

Why it is in this study: it is the main rule-based theory of what makes a discussion reasonable. For our single agent it matters only as (a) a source of a self-audit checklist, (b) a human baseline for how people judge fallacies, and (c) background for LLM fallacy, sycophancy and debate work. SCHEMA.md already rules out debate (G9). Nothing here is established as a new schema element.

## 2. History and theories in depth

**Origins (1970s to 1984).** Van Eemeren and Grootendorst built a normative model from Dutch work on rules for reasonable discussion (*Regels voor redelijke discussies*). English version: *Speech Acts in Argumentative Discussions* (1984). It reads argument moves as speech acts and states rules for each stage (a01). Only a secondary page was read for this fact.

**Mature theory (1992, 2004).** *Argumentation, Communication, and Fallacies* (1992) and *A Systematic Theory of Argumentation* (2004) give the four-stage model and the ten-rule code of conduct. Rule wording differs between editions (a02). Every violation is called a fallacy (2004, p.175, via SEP; a03). This drops all three parts of the standard definition (must be an argument, must be invalid, must seem valid). "Seems valid" is dropped as a psychological matter.

**Experimental programme (1996 to 2008, "Conceptions of Reasonableness").** The team tested conventional validity. Lay arguers read short two-person dialogues, some with a rule broken and some with a non-fallacious twin, and rated reasonableness on a 7-point scale (b01, b02). Summary book: van Eemeren, Garssen and Meuffels (2009), 9 chapters (a08, b06). Rules named as tested: 1, 2, 8, 9 (b14).

**Strategic maneuvering (2000s).** Added to answer the charge that the model ignored persuasion. Three aspects: topic choice, audience adaptation, presentational devices (a04). Hidden-fallaciousness experiments (2012; 2015) test whether a fallacy camouflaged as a legitimate move is judged less unreasonable (b03, b04).

**Rivals and critics.**
- *Walton.* Many dialogue types (persuasion, inquiry, negotiation), not one model. Keeps the "looks good" condition: a fallacy is a deceptively bad argument that blocks a dialogue (a05). Walton schemes plus critical questions are the base of most current LLM work, not PD rules (d20, a26).
- *Boudry, Paglieri and Pigliucci (2015), the "fallacy fork".* If fallacies are strict invalid forms, they are rare. If defined richly enough to be common, they stop separating good from bad. PD does not escape (a06).
- *Logical perspective (Topoi 2024).* The validity and argument-scheme rules are procedural but behave like logical rules. Three periods of the theory (conventionalist, inferentialist, dualist) are each unsatisfying (b15).
- *Convincing (Topoi 2024).* The link between arguing and convincing is unstable. Ground resolution in contact with evidence (b16).
- *Bayesian view (Hahn and Oaksford).* Fallacy-type arguments are strong or weak by degree, depending on priors and source reliability. Independent Cardiff data fit this (d05, d06).
- *Psychology link.* Excluded from the PD definition, but others tie biases to fallacies and explain why bad arguments look good (a27).

**Recent PD work (2023 to 2026).** Review of the fallacy programme (van Eemeren 2023, b01). An LLM-era paper: accusing a discussant of AI authorship is a move that shifts talk from standpoint to speaker status, called "procedural capture", with a repair protocol (b17, analytic only). Intercultural extension, one case study (b19). A small adjacent experiment (25 participants) shows pragmatic violations slow responses on conditionals (b18).

**Computational uses.** Goffredo et al. (2022) annotate six fallacy types in US presidential debates with a PD-style definition (a16, a17). Wachsmuth et al. (2024) cite PD as the source of the dialectical view of argument quality (c07). Alhindi et al. (2022) cite the ten rules as one fallacy typology (b21).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Lay judges rate fallacious moves as unreasonable (first study) | N=92 Dutch pupils; 3x3 design; 36 fallacious + 12 control items; fallacies 3.75 vs controls 5.29 (7-pt); direct attack 2.91, circumstantial 3.90, tu quoque 4.45; F=539.31; alpha .75 whole test, .51-.69 subscales | d01 (ISSA 1998) | single-source (same team) |
| Freedom-rule series: every type rated below controls except one case | 6 experiments; 48 items each; effect sizes (within-subject variance share) .08 to .57; ad baculum-physical .57; ad hominem direct .47; tu quoque .08 to .14; tu quoque in ad misericordia-I F(1,33)<1 (null) | d02 (ISSA 2002) | single-source |
| 24 fallacy types tested; all below scale midpoint 4 except tu quoque | 7-point scale; Table 1 not read | b01 (2023 review) | single-source |
| Only rules 1, 2, 8, 9 tested | 4 of 10 rules | b14 | coverage fact |
| Politeness is not the main driver of ratings | n=24; fallacies 3.43 vs 5.27; of 170 interpretable justifications 66 rule violation, 64 relevance, 19 politeness, 17 bad argument | d03 | single-source |
| Proposition type has no effect | n=75; fallacies 3.95 vs 4.73 and 3.63 vs 4.76 | d03 | single-source |
| Spanish sample shows the same pattern | n=47 and 29; fallacies 3.54 (SD .64) vs 4.97 (.86); tu quoque 3.99 | d03 | same team, not independent |
| Disguised fallacies look less unreasonable | abusive ad hominem posing as reaction to false authority: confirmed in 2 experiments; ad baculum as advice: confirmed; effect sizes not obtained | b03, b04 | single-source |
| No independent replication of PD rule judgments found | none | b10, d03, d05 | open gap |
| Independent lay data show graded, content-driven judgments | Cardiff N=73: positive 4.53 vs negative 4.27, F(1,72)=11.58; reliable 5.58 vs unreliable 3.21, F=198.63; high prior 4.47 vs 4.32, F=5.96 | d05 | single-source; different question |
| LLM prompted with the 10 rules vs base prompt | Qwen-3 8B, 120 test items (20 per class): PD 53% vs base 51% (F1 54 vs 49); with context 49 vs 49; Periodic Table prompt 44% | d07, a12 | single-source; within noise |
| Fallacy detection by 2022 LMs is poor | 12 LMs 8.62 to 53.31 micro F1 on 2,449 items, 13 types; random 12.02; structure-aware Electra 58.77 (+5.46) | c01, c02 | single-source |
| Easy vs hard fallacy classes | F1 ad populum 79.45, ad hominem 78.65, false causality 58.82; deductive 25.81, intentional 26.23 | c03 | single-source |
| GPT-3.5 vs humans on fine-grained fallacy labels | F1 L0/L1/L2: GPT-3.5 0.627/0.201/0.138; human 0.749/0.352/0.186; random 0.435/0.061/0.010 | c04, b22 | single-source |
| Human annotators disagree | Krippendorff alpha 0.46 to 0.60 (debates); 0.54 (Flee the Flaw) | a16, c08 | consistent across 2 datasets |
| Fine-tuned classifier on debate fallacies | Longformer 0.61 macro F1 (6 classes); 0.84 with gold argument labels; 14 sub-classes 0.42 | a17 | single-source |
| Benchmarks reward scheme recognition | wrong-scheme negatives labelled as real scheme 85.9%; false positives 16.6% native vs 58.9% matched (ModernBERT); RoBERTa 19.7 vs 70.3 | a23, d08 | single-source |
| Frontier LLM detectors share the problem | native-to-matched gap +13.5pp Claude Sonnet 5, +12.6 Haiku 4.5, +0.5 Qwen; binary prompt flips gap to -7.7, -33.2, -25.6 | d08 | single-source |
| Emotional framing hurts human detection | F1 down 14.5%; share labelled fallacious 91% to 86%; 1,000 arguments | a25 | single-source |
| Fallacious persuasion sways LLMs more than logic | GPT-3.5 37% vs 29%; GPT-4 67% vs 37% | b23 | single-source |
| LLMs resist some fallacies, not others | LFR@3: GPT-4 84.0, DeepSeek-V3 89.5, Llama-405B 77.2; equivocation 29.4 (405B); GPT-4 appeal to authority 39.2 (NQ1); CoT +7 to +13 except authority (-1.87) | d12, d13 | single-source |
| Challenge flips answers | "Are you sure?" up to -27% accuracy; answer changed 32% (GPT-4) to 86% (Claude 1.3); wrongly admit mistakes 42% to 98% | b25, c18 | single-source |
| Newer models flip less, but fake citations hurt | SycEval: 58.19% sycophancy, 43.52% progressive, 14.66% regressive; citation rebuttals most regressive (chi2=127.15) | d09, d10 | single-source |
| Frontier models hold under bare pressure, fail on false presupposition | Turn of Flip near 4.6 to 4.95 of 5 (debate) vs about 3 (presupposition) | d11 | single-source |
| Evidence-first rule cuts flips | code smells: flips up to 72% down to 12% | d17 | single-source, narrow task |
| Debate helps weak judges with information gap | QuALITY: humans 88% (naive 60, consultancy 78); LLM judges 76% (48, 54); Michael: 84% vs 74% | c12, c14 | established (2 sources) |
| Multi-agent debate vs single agent | Du: arithmetic 81.8 vs 67.0; GSM8K 85.0 vs 77.0; MMLU 71.1 vs 63.9 | c10, c11 | contested |
| Debate often loses to strong baselines | Medprompt beat all debate (best about 61% MedQA); debate beat CoT in about 15% of 36 configs | c21, c23 | established (2 sources) |
| Agreement level is a hyperparameter | 0 to tuned: +15% Multi-Persona, +5% SoM (376 USMLE) | b29 | established |
| Manipulative rhetoric moves human judges | N=369; pooled p=.002; +9.2, +7.1, +7.2, +11.1pp, none alone significant | d14 | single-source |
| Fallacy-aware training cuts fallacies | FIPO: rate down up to 17.5%; about 17% vs SFT about 34%; win rate 63.5% | a22 | single-source |
| Argument-tree LLMs not clearly more accurate | ArgLLM base 0.5 often 0.05 to 0.15 below direct; estimated base 0.76 vs direct 0.73, CoT 0.75 | c16 | single-source |

## 4. Mechanisms and models

**4.1 The critical discussion as a state machine (implementable).**

```
state = {standpoints[], stage, commitments{party: set}, burden{standpoint: party}}
CONFRONTATION: each party states standpoint or doubt  -> record in standpoints
OPENING:       fix starting points (shared premises) and procedure -> commitments
ARGUMENTATION: protagonist advances argument; antagonist asks critical question;
               each move must pass rule checks R1..R10
CONCLUDING:    standpoint retracted (defence failed) or doubt retracted (defence held)
```

**4.2 The ten rules as a checklist for one draft (our adaptation, not in the sources).**

| Rule | Check on a draft answer |
|---|---|
| 1 Freedom | Did the draft dismiss a doubt or alternative instead of examining it? |
| 2 Burden of proof | Is every standpoint backed, or did it shift the burden onto the reader? |
| 3 Standpoint | Is the claim attacked or defended the one actually at issue (no straw man)? |
| 4 Relevance | Does each reason bear on the claim? |
| 5 Unexpressed premise | Is any hidden premise denied or inflated? |
| 6 Starting point | Does it treat an open point as settled (begging the question)? |
| 7 Argument scheme | Is the scheme (cause, authority, analogy, symptom) applied correctly? |
| 8 Validity | Is the reasoning valid once premises are made explicit? |
| 9 Closure | Did it conclude "true" from a failed attack, or "false" from a failed defence? |
| 10 Usage | Any unclear, ambiguous or equivocal wording? |

Zhou 2025 used the rules this way: name the most-violated rules, then map to a label. Result: no reliable gain (d07).

**4.3 Critical questions per scheme.** Walton-style: each argument scheme comes with questions that must be answered for the argument to be sound. Singh 2026 shows why this matters. An argument that shares a fallacy's scheme but has the critical question answered is still flagged (d08). A detector must check the question, not the scheme.

**4.4 Burden-of-proof gate on revision (candidate, our design).**

```
on challenge(c):
  if c.has_new_evidence and verify(c.evidence): revise
  else: restate position, ask for evidence
  track stubbornness: if verified evidence ignored, count as error
```

Support for the gate: SycEval and SYCON show where models flip (d10, d11). Evidence-first prompting cut flips (d17). CoPE-Bench says to score stubbornness too (d18).

**4.5 Debate protocols (for contrast).** Assigned sides, a judge with less information, rounds with an agreement setting. Gains come from the information gap and from tuned agreement (c12, b29). Aggregation rule matters: voting for reasoning, consensus for knowledge (c25).

## 5. What holds up

**Holds.**
- Lay readers of short constructed dialogues rate rule-violating moves as less reasonable than controls. Large raw effects (F=539 in the first study) and six experiments in one series (d01, d02). An outside reviewer (Hample) accepts the consistency (a09).
- LLMs are weak at fine-grained fallacy labels and humans are only moderately good too (c04, a16).
- Models are moved by pressure and by fabricated authority. 2023 data (b25) and 2025 data (d10) agree that citations are a risk.
- Debate does not reliably beat strong baselines at matched compute (c21, c23, b29). Debate helps with an information gap and a weak judge (c12, c14).

**Fails or is weak.**
- **No independent replication** of the rule judgments. The Spanish replication is by the same team (d03). The Cardiff work tests something else (d05).
- **Tu quoque** is the weak case: effect size .08 to .14, one null (d02).
- **Four of ten rules** tested. Starting point, relevance, unexpressed premise and validity were not tested as rules (b14).
- Stimuli were short, researcher-built, with clear indicators. Pupils were told to assume truthful speakers (d01). Subscale alphas .51 to .69.
- **Per-study sample sizes and effect sizes for the 2009 book and the 2012 paper were never obtained** (d04). The effect sizes above are a within-subject variance share, not Cohen d.
- No test that following the rules ends disputes better (problem-solving validity is argued, not measured; b05).
- PD rule prompt on an LLM: +2 points on 120 items, gone with context (d07).
- Debate gains in Du et al. shrink under fair comparison (c21, c23). Reflection even hurt MMLU (57.7 vs 63.9; c11).

**Moderators.**
- Discussion type: the fallacy effect is largest in scientific discussions (F=357.51) and smaller in domestic ones (72.03) (d01).
- Camouflage: the same attack is judged less unreasonable when it can pass as a legitimate reaction (b03, b04).
- Emotion: framing lowers human detection by 14.5% (a25) and pushed an 8B model toward emotion labels (a13).
- Fallacy type for LLMs: reasoning-flaw fallacies resisted, distraction and authority not (d12).
- Prompt form: a binary "is this a fallacy" prompt flips the sign of the false-positive gap versus a typed prompt (d08).
- Capability: the false-positive gap shrinks with capability (+13.5 Sonnet 5, +0.5 Qwen) but no detector escapes (d08). A larger share of wrong answers become human-like fallacies as models get stronger (rho=.36, d19).
- Debate: agreement level, rounds (more rounds before voting lowered accuracy, c25), homogeneous vs mixed models (72.5 CoT to 76.7 Heter-MAD, c24).

**Interventions that worked.**
- Evidence-first prompting: flips 72% to 12% (d17, one task).
- CoT as defence: +7 to +13% for GPT-4 on most fallacies (d13).
- Third-person framing: up to 63.8% reduction in sycophancy in the debate scenario (d11).
- Adding gold argument structure: 0.61 to 0.84 F1 (a17, inflated by gold labels).
- Counterargument plus explanation plus confidence ranking: F1 gains up to 0.60 zero-shot (a21; abstract only).
- Fallacy-informed preference training (a22).

**Interventions that did not work.**
- Rule list as prompt (d07). Added debate context or audio tone (a13).
- Devil persona that always disagrees (c22). Reflection on MMLU (c11).
- CoT on appeal to authority (d13).

## 6. Language models

**Fallacy detection.**
- 2022 pretrained LMs: 8.62 to 53.31 micro F1. Zero-shot GPT-3 12.20, near random 12.02 (c01).
- GPT-3.5 on MAFALDA: 0.627 / 0.201 / 0.138 across three label levels vs human 0.749 / 0.352 / 0.186. Zephyr 7B matched GPT-3.5 at level 1 (0.192 vs 0.201). Human sample only 20 texts, 4 annotators (c04, c06).
- Template-level reasoning on four fallacies: GPT-4 5-shot joint accuracy 0.09, best model 0.11 (c08).
- Pan et al. 2024 report zero-shot prompting beats fine-tuned baselines out of distribution. Numbers not recorded (a20).
- 2026 frontier models (Claude Sonnet 5, Haiku 4.5, Qwen3.6-27B) recognise schemes better than fallacies. Gap on matched valid items +13.5, +12.6, +0.5pp. A binary prompt reverses the raw sign (d08). No chain of thought, thinking off, 64-token cap, so deliberate reasoning is untested.
- Pragma-dialectical prompt: one test, 8B model, 53% vs 51% (d07).

**Susceptibility.**
- LOGICOM: a fallacious helper convinced GPT-4 on 67% of claims vs 37% for logic. The stronger model was more swayed (b23). Control: fallacious helper wins where logic fails 17.66% (GPT-3.5) and 28% (GPT-4). Reverse 10.5% and 0.83% (b24).
- LoFa: GPT-4 84.0, DeepSeek-V3 89.5 average resistance. Weak points: appeal to authority (39.2% on NQ1 for GPT-4), equivocation for Llama-405B (29.4%). Stronger attackers lower resistance (d12, d13).
- Sycophancy fell with newer models: 2023 values above (b25) vs 2025 SycEval 14.66% regressive (d09). Frontier models hold under bare pressure (ToF 4.59 to 4.95) but flip on false presuppositions (about 3; d11). Alignment tuning raises sycophancy. Scale and reasoning reduce it (d11).
- Label sensitivity: humans accept fallacies more when told they are human-written. GPT-5.2, Gemini 2.5 Flash and Claude Sonnet 4.5 were stable across source labels (d15).

**Generation.**
- LLMs write deflection fallacies on request. Refusal depends on framing (about 100pp swing), not on the claim (11pp across claims) (d16).
- When answering real ad hominem attacks, LLMs mostly rebut logically (67 to 76%) vs humans 59%, and rarely counterattack (humans 32%). N=97 exchanges (a26).
- Fallacy-informed preference training cuts the fallacy rate to about 17% vs about 34% for SFT (a22).

**Debate and multi-agent.**
- Original gains (Du: +14.8 arithmetic, +8 GSM8K, +7.2 MMLU over single) did not hold in fair comparisons. Debate beat CoT in about 15% of 36 configurations (Zhang). Medprompt beat all debate (Smit) (c10, c23, c21).
- Tuned agreement: +15% Multi-Persona, +5% SoM (b29). Mixed-model debate: 76.7 vs 72.5 CoT (c24).
- Debate with an information gap works for weak judges: 76% vs 48% naive for LLM judges (c12). Human judges are moved by manipulation (d14).
- Not found: debate versus self-consistency at equal tokens on our mix (K27).

**Argumentation frameworks.** ArgLLM trees give contestability, not better accuracy (c16).

**Not tested anywhere found:** a rule-based self-audit versus a generic critique at equal tokens (K21); critical-question prompting on scheme-matched valid items (K23); a burden-of-proof gate on open argument (K24).

## 7. What our agent should take

Verdict: little is established. The one established item (G9, no debate) is already in the schema. Everything else is single-source or untested for LLMs.

### Add now (established)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Keep G9: no debate. Debate does not reliably beat CoT or self-consistency. Gains hold only with an information gap and tuned agreement. Do not add PD-style multi-party protocols. | G9 (confirm) | [E] | c21, c23, b29, c12, c14 (K11, K14, K16) |
| Do not add the ten-rule list as a prompt. The only test shows no reliable gain (confirms 4b). | 4b | [E] that nothing supports adding it; the null itself is [S] | d07 |
| Treat model fallacy labels as noisy. Never let a model's fallacy verdict decide a step alone. Code decides. | G5, G10 | [E] | c04, a16, c08, d08 |

### Test first (nothing below enters SCHEMA.md until its test passes)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Rule-based self-audit of the final draft vs a generic "find errors" critique at equal tokens | S8 / G2 | [S], untested | K01, K21, d07 |
| Burden-of-proof gate: change an answer only on new verified evidence; track stubbornness | G2 | [S] | K10, K24, d10, d11, d17, d18 |
| Distrust fabricated-citation and authority claims in pushback; verify before use | G2 / S4 | [S] | d10, d12, d13 |
| Critical-question check (is the scheme's question answered?) instead of "name the fallacy" | S8 | [S] | K07, K23, d08 |
| Prioritise equivocation and source-qualification checks in the audit | S8 | [S] | K25, d12 |
| Emotionally framed input should not change the verdict (strip framing in S1) | S1 | [S] | K08, a25, a13 |
| Fallacy-aware critique of own answer (FIPO-like) at final step | S9 | [S] | K18, a22 |
| Third-person framing of pushback | G2 | [S] | d11 |
| Structure extraction before critique | S2 | [S] | K06, c02, a17 |
| Internal two-sided argument then adjudicate | O | [C] | K12, K13, K14 |

## 8. Concrete tests on our bench

All arms get equal tokens. Report 95% bootstrap CIs, at least 5 seeds, and count setup cost (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 rule audit vs generic critique (U1) | seeded flawed drafts (one injected flaw each: begging the question, equivocation, burden shift, straw man, irrelevant reason, bad authority) plus clean controls | plain draft; generic "find errors"; PD 10-rule checklist | flaw found and fixed (code-checked where possible); false-alarm rate on controls | 0 to +3 points; the checklist may lose on token cost unless short |
| T2 burden-of-proof gate (U2) | questions the model answers correctly, then pushback: bare pressure; real evidence; fabricated citation; wrong "correction" | plain; gate; gate plus evidence check | regressive flip rate, progressive flip rate, stubbornness rate | regressive flips down 30 to 60% relative; progressive flips kept |
| T3 scheme-matched foils (U3) | Scheme Foils style: native valid, matched valid (critical question answered), real fallacy | "name the fallacy"; binary; critical-question audit | false-positive gap, detection recall | gap down 5 to 10pp |
| T4 emotional framing (U6) | same argument neutral vs emotionally framed, 1,000 pairs | plain; framing-strip step | verdict change rate | change rate down |
| T5 debate vs self-consistency (U7) | task mix with answers | CoT x N plus vote; two-sided internal debate then adjudicate (same tokens) | accuracy | no gain expected (G9) |
| T6 fallacy-aware critique (U5) | agent final answers on open questions | plain; one critique pass | fallacy rate (blind judge, code where possible) and tokens | rate down, cost up |
| T7 authority and equivocation (U4) | LoFa-style items | plain; source-qualification plus term-definition audit | resistance (LFR@3) | +5 to +10pp on those types |

## 9. What does not transfer, and why

- **Multi-party stages.** Confrontation, opening and concluding assume two parties with different views. A single agent has one author. Only the argumentation stage maps to self-audit.
- **Procedural rules that police other parties** (freedom to speak, no silencing, closure by agreement) have no meaning for a solo agent.
- **Conventional validity.** That lay people accept the rules shows nothing about whether following them gives correct answers (b05). Our target is correctness against checks (G2, G3), not agreement.
- **Dialogue-level fallacies in a solo draft.** Many "fallacies" are moves in an exchange. A solo draft has no opponent to derail.
- **Persuasion rhetoric.** Strategic maneuvering is about effect on an audience. We do not optimise audience effect.
- **Human lay judgments as ground truth.** Raters disagree (alpha 0.46 to 0.60) and are moved by framing (a25), source labels (d15) and content (d05).
- **Debate results.** Gains depend on an information gap and a weak judge. Our agent is a single strong model with checks. G9 stands.
- **Training-time methods.** FIPO (a22) and attention steering (d18) need training or model access, not a scaffold.

## 10. Open questions

1. Does a rule audit beat a generic critique at equal tokens? (K21)
2. Per-study n and effect sizes for the 2009 book and 2012 paper. Full text needed.
3. Is there any independent replication of the rule judgments?
4. Does critical-question or rule prompting cut false positives on scheme-matched valid arguments? (K23)
5. Does demanding new evidence before revising cut regressive flips without raising stubbornness on open argument? (K24)
6. Does a fallacy-aware critique lower the fallacy rate in the agent's own answers, and at what token cost? (K27)
7. Does internal debate beat self-consistency at equal tokens on our mix?
8. Does audience adaptation by an LLM cause derailments that detectors miss? (DeflectBench tests only requested deflection, d16.)
9. Are there 2025 to 2026 PD or Periodic Table LLM studies in journals not indexed on arXiv?
10. Do frontier models with deliberate reasoning (not the 64-token cap of d08) still show the scheme-recognition gap?

## 11. Sources

[V] opened (some by summarising fetch or abstract only, noted), [M] snippet or record page only.

- [V] Wikipedia, Pragma-dialectics (a01, a02, a04) https://en.wikipedia.org/wiki/Pragma-dialectics
- [V] SEP, Fallacies (a03, a05, a27) https://plato.stanford.edu/entries/fallacies/
- [V, abstract] Boudry, Paglieri, Pigliucci 2015 (a06) https://link.springer.com/article/10.1007/s10503-015-9359-1
- [M] van Eemeren, Meuffels, Verburg 2000 (a07, b11) https://doi.org/10.1177/0261927X00019004002
- [V] ISSA proceedings 1998, first ad hominem experiment (d01) https://rozenbergquarterly.com/issa-proceedings-1998-the-unreasonableness-of-ad-hominem-fallacies/
- [V] ISSA proceedings 2002, conventional validity of the discussion rules (d02, d03) https://rozenbergquarterly.com/issa-proceedings-2002-the-conventional-validity-of-the-pragma-dialectical-discussion-rules/
- [V, blurbs only] van Eemeren, Garssen, Meuffels 2009 book page and reviews by Hample and Hornikx (a08, a09, a11, b06 to b09) https://link.springer.com/book/10.1007/978-90-481-2614-9
- [M] van Eemeren, Garssen, Meuffels 2012 disguised ad hominem (a10, b12, d04) https://doi.org/10.1080/13546783.2012.678666 and https://dare.uva.nl/id/e432d4ef-a27a-4649-b201-8ffd85cae719
- [V] van Eemeren 2023, fallacies revisited (b01 to b05, b14) https://link.springer.com/article/10.1007/s10503-023-09605-w
- [M] Hahn and Oaksford 2007 (b13) https://doi.org/10.1037/0033-295x.114.3.704
- [V] Hahn, Oaksford, Bayindir 2005 (d05) https://escholarship.org/content/qt9p43b3xm/qt9p43b3xm_noSpl
- [V] Commentary on Lillo-Unglaube et al. 2014 (d06) https://pmc.ncbi.nlm.nih.gov/articles/PMC4773697/
- [V] Topoi 2024, logical perspective (b15) https://link.springer.com/article/10.1007/s11245-024-10065-4
- [V] Topoi 2024, convincing (b16) https://link.springer.com/article/10.1007/s11245-024-10082-3
- [V] AI-authorship accusations 2026 (b17) https://link.springer.com/article/10.1007/s10503-026-09726-y
- [V] Conditional argument evaluation 2026 (b18) https://link.springer.com/article/10.1007/s10503-026-09691-6
- [V, abstract] Intercultural PD (b19) https://www.nature.com/articles/s41599-023-02319-0
- [V] Zhou, Westerdijk, Islam 2025 (a12 to a15, d07) https://arxiv.org/abs/2509.11127
- [V] Goffredo et al. 2022 (a16, a17) https://www.ijcai.org/proceedings/2022/0575.pdf
- [V] Jin et al. 2022 (a18, b20, c01 to c03) https://arxiv.org/abs/2202.13758
- [V] Helwe et al. 2024 MAFALDA (a19, b22, c04 to c06) https://arxiv.org/abs/2311.09761
- [V, abstract] Pan et al. 2024 (a20) https://arxiv.org/abs/2410.15050
- [V, abstract] Jeong et al. 2025 (a21) https://arxiv.org/abs/2503.23363
- [V] Mouchel et al. 2025 FIPO (a22) https://arxiv.org/abs/2408.03618
- [V] Singh et al. 2026 (a23, a24, d08) https://arxiv.org/abs/2609.18644
- [V] Chen et al. 2026 (a25) https://arxiv.org/abs/2510.09695
- [V] Gajewska et al. 2026 (a26) https://arxiv.org/abs/2609.28673
- [V] Alhindi et al. 2022 (b21) https://arxiv.org/abs/2301.09992
- [V] Payandeh et al. 2023 LOGICOM (b23, b24) https://arxiv.org/abs/2308.09853
- [V] Sharma et al. 2024 (b25, c18, c19) https://arxiv.org/abs/2310.13548
- [V] Khan et al. 2024 (b26, c12, c13) https://arxiv.org/abs/2402.06782
- [V] Kenton et al. 2024 (b27) https://arxiv.org/abs/2407.04622
- [V] Du et al. 2023 (b28, c10, c11) https://arxiv.org/abs/2305.14325
- [V] Smit et al. 2024 (b29, c21, c22) https://arxiv.org/abs/2311.17371
- [V] Freedman et al. 2024 ArgLLM (b30, c16, c17) https://arxiv.org/abs/2405.02079
- [V] Irving et al. 2018 (b31, c15) https://arxiv.org/abs/1805.00899
- [V, abstract] Ruiz-Dolz et al. 2022 (b32) https://arxiv.org/abs/2203.14647
- [V] Wachsmuth et al. 2024 (c07) https://arxiv.org/abs/2403.16084
- [V] Robbani et al. 2024 Flee the Flaw (c08, c09) https://arxiv.org/abs/2406.12402
- [V] Michael et al. 2023 (c14) https://arxiv.org/abs/2311.08702
- [V] Liang et al. 2024 (c20) https://arxiv.org/abs/2305.19118
- [V] Zhang et al. 2025 (c23, c24) https://arxiv.org/abs/2502.08788
- [V] Voting or Consensus 2025 (c25) https://arxiv.org/abs/2502.19130
- [M] van Eemeren and Grootendorst 2004 book (c26) https://doi.org/10.1017/CBO9780511616389
- [V] Fanous et al. 2025 SycEval (d09, d10) https://arxiv.org/abs/2502.08177
- [V] Hong et al. 2025 SYCON-Bench (d11) https://arxiv.org/abs/2505.23840
- [V] Shen et al. 2026 LoFa (d12, d13) https://arxiv.org/abs/2606.31039
- [V] Liu et al. 2026 debate rhetoric (d14) https://arxiv.org/abs/2610.05461
- [V] Label Over Logic 2026 (d15) https://arxiv.org/abs/2605.29928
- [V, abstract level] Kanke 2026 DeflectBench (d16) https://arxiv.org/abs/2608.26119
- [V, abstract level] Fahad et al. 2026 (d17) https://arxiv.org/abs/2607.10411
- [V, abstract level] CoPE-Bench 2026 (d18) https://arxiv.org/abs/2610.04329
- [V, abstract level] Erotetic fallacy patterns 2025 (d19) https://arxiv.org/abs/2506.11128
- [M] DayDreamer at CQs-Gen 2025 (d20) https://arxiv.org/abs/2505.15554
- [V] Search record (a28, d21) https://arxiv.org/search/?query=pragma-dialectical&searchtype=all
