# A17.04 Social influence on crowds - cross-check critique

## Numbers re-opened this session (all against saved full texts in D:/research_scratch/A17.04/)
Confirmed as written:
1. Lorenz 2011: 144 students; arithmetic mean closer to truth than individuals in 21.3% of cases, 77.1% in log space; population-density arithmetic mean +1,337.2%; 13 of 864 runs in the top pay band every round (a01, a03, a05).
2. Bazazi 2019: diversity MPE 99.88% (individual pay) vs 73.35% (collective pay); group error MPE 99.57% vs 69.13% (a09, b01).
3. Becker 2017: 1,360 participants; SD -43% (13 trials, p<0.001); median error 0.76 to 0.67 SD (-12%); hub correlation rho=0.92, n=57 (a15, c04, c05).
4. Jayles 2017: median S=0.34; France data = 29 questions, 5,394 x 2 estimates; virtual experts 0/20/43/80% (b05, a11).
5. Mavrodiev 2013: slopes Q1 0.97, Q2 0.27, Q3 0.83, Q4 0.60 (a08).
6. Almaatouq 2022: 2,885 people, 99 groups, 54 tasks, 15,562 individual and 687 collective estimates (b08).
7. Schoenegger 2024: Brier 0.20 vs 0.19, t(60)=0.19, p=0.850; GPT-4 0.17 to 0.14, p=0.003 (a19, c19, c20).
8. Barrera-Lemarchand 2026: Wilcoxon z=3.58, d=0.24 (influence); deliberation d=3.25; 0.195 vs 0.164; 0.230 vs 0.159; clones z=1.22/0.51, d=0.087/0.144; mixed vs clones z=3.61, d=0.48; 167 of 168 groups converged (a20, a21).
9. Bertalanic 2026: Ministral GSM-Hard debate 20.7% vs self-correction 48.3% vs single shot 24.7%; modal adoption 85.5%; vulnerability 70.0%; oracle gap 32.3; 2.1-3.4x tokens (c09, c10).
10. Rajasekaran 2026: 22 points at n=1, 49 at n=10; 583 of 197,976 filler trials; per-model shifts +73 (gemini-3.8-flash) to +33 (claude-opus-5-5), sonnet-5-5 +39 (c11, c12).

## Corrections made
- Author order for Becker 2017: the paper is Becker, Brackbill, Centola. c04/c05 wrote Becker, Centola, Brackbill. Use the first.
- c03 (from memory, opened:false) says Lorenz used "12 estimation questions". The paper says 144 subjects answered six questions in runs of five. Six is correct; c03 should not be cited.
- a15/c04 are labelled "replication", but Becker 2017 is better read as a boundary-condition study (it replicates the diversity drop, not the "no accuracy gain"). a14 (Jayles 2021) is labelled replication but only partly tests Lorenz's contrast.
- Unverified-from-memory lines (b19-b26, c03) overlap with opened lines (Becker 2017/2019, Page); use the opened lines.
- Rajasekaran model names (gemini-3.8-flash, gpt-6-sol, etc.) match the paper's table; they are paper claims, not checked against any external model list.

## Duplicates (not independent)
a09/b01/c01 are the same paper (Bazazi); a19/b14/c19/c20 are the same paper (Schoenegger); a01-a05/b04/c03 the same paper (Lorenz); a15/b19/c04/c05 same (Becker); a22 is cited via other review text. Claims count independent sources by paper, not by line.

## Contradictions between sources
- Lorenz says no collective gain; Jayles 2017/2021, Becker 2017/2019 and Barrera-Lemarchand LLM Study 1 (d=0.24) all find some collective gain when influence is sequential, networked, or carries reliable information. The difference is the design: simultaneous round-wise mean feedback on hard right-skewed questions (Lorenz) vs sequential or network designs. Almaatouq 2022 offers a unifying account (shape of first estimates and centralisation) but is itself one reanalysis.
- Farrell 2011 vs Rauhut 2011: both are right at their level (individual vs group); the dispute is about which level matters for an outsider.
- Debate evidence conflicts by setting: Smit 2024 and Bertalanic 2026 find same-model debate no better than independent ensembling; Hegazy 2024 and Barrera-Lemarchand find mixed-model deliberation does better. Hegazy has no equal-token independent baseline in what was read.
- Barrera-Lemarchand: best single model deliberating with itself beat the mixed consensus (d=0.88), so "diversity helps" is relative to weaker copies; it does not show mixing beats the best model.
- Bazazi MPE values are posterior probabilities of direction, not effect sizes; the abstract-level phrasing "impairs" overstates what the magnitudes show.

## Weak spots
- Almost all LLM studies are 2026 preprints, small open models (7-8B) or one task. Several have no peer review.
- Rajasekaran and Pokharel measure shifts toward supplied words or opinions, not accuracy loss on a task with ground truth.
- c15/c16 (Liu) use Qwen2.5 and Llama only, same authors for replication.
- Jayles/Lorenz tasks are numeric estimation; transfer to reasoning chains or code is untested.
- Bazazi: one lab, one spatial task, mean shown once.

## Only seen in snippets or abstracts
a18 (Proc R Soc B 2020, abstract only), a24 (DEAR, abstract and intro), a26 (Galton and other older work, not opened), c24 (abstract claim of 7x cost reduction), c25 (share of gap closed not extracted), a22 exact accuracies (in figures), b19-b26 (memory only).

## GAPS (most decision-relevant first)
1. At equal tokens, does a single model's N independent samples pooled by median beat the same N samples allowed one round of seeing each other's answers (same model, numeric and reasoning tasks)? No study found does this directly for frontier models.
2. Does the conformity seen in Asch-type and herd tests (Rajasekaran, Herd Behavior) translate into accuracy loss when the peer answers are the model's own earlier attempts rather than other agents?
3. Does scoring each attempt on the collective outcome (the Bazazi collective-pay idea) reduce copying in LLM agents? No LLM test of incentive structure was found.
4. Can heavy-tailedness of first-round attempts (Almaatouq R) be used as a gate for allowing or blocking peer exposure, and does it hold for LLM answer distributions?
5. Which peer-information format (mean, full list, verdict only, reasoning) minimises herding in current frontier models; Jayles 2021 tested this in humans only.
6. Does a verifier-gated acceptance rule (only accept a revision that passes an external check) restore the gains seen with planted correct sources (Jayles 2017) in LLM groups?
7. Is there a failed or null replication of Lorenz 2011 in a larger or non-student sample? None was found; the claim rests on one study and its reanalyses.
8. Does mixing model families help beyond the best single model once equal tokens and the best-model baseline are controlled (Barrera-Lemarchand d=0.88 for best single)?
9. How much do effects depend on sampling temperature and prompt diversity (persona prompts barely moved conformity; do temperature or retrieval diversity)?


## Gap search results

Evidence is in `evidence_d.jsonl` (d01-d21; 19 opened full text, d20 and d21 abstract only). Claims K24-K32 added; K01, K08, K13, K14, K20 updated in `claims.jsonl` (now 32 claims: 12 established, 14 single-source, 6 contested). Web search quota was exhausted, so the search used arXiv PDFs, Europe PMC and Crossref. PDFs deleted.

### Gap 1: independent samples pooled vs one round of exchange (same model) - CLOSED for open and older models, OPEN for frontier models
Four matched-budget tests all favour independent sampling plus vote.
- Huang 2024 (GPT-3.5, GSM8K): at 9 responses vote 88.2 vs debate 83.0 (d01).
- Choi 2025 (5 agents, 7 tasks): Qwen2.5-7B vote 0.7691 vs debate 0.7377; Llama3.1-8B 0.7242 vs 0.6929 (d03). Debate is a martingale; mean agent accuracy stays flat across rounds.
- Zhang 2025 (4 models, 9 benchmarks): debate beat CoT in about 15% of 36 cells; self-consistency won where it applied (d05).
- Wynn 2025: majority of first answers vs majority after debate fell for Llama (MMLU 61.6 to 57.8) and Mistral (33.6 to 24.4) and was flat for GPT-4o-mini (81.4 to 82.2) (d07).
None used a current frontier or reasoning model on numeric estimation. Token cost, not call count, was matched only loosely.

### Gap 2: does conformity cost accuracy when the peers are the model's own earlier attempts? - PARTLY CLOSED
Off-the-shelf models lose accuracy when they re-read their own answer without outside facts (GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0, d02) and favour their own output when judging it (d15). A model trained to revise turns about 38% of correct answers wrong unless a verifier or vote picks the answer (d14). Still open: a clean test where the peers are verbatim copies of the same model's own earlier samples in a current frontier model, versus other-agent peers. Own-attempt revision is not the same as consensus pressure, and Snell found sequential beat parallel narrowly when trained for it.

### Gap 3: collective-outcome scoring and copying in LLM agents - MOSTLY OPEN
Only two related tests. A payment-for-correctness prompt did not reduce correct-to-incorrect flips (Wynn, d08). A collective verifier reward changed revision behaviour in small models, but only when trained with RL (MAPoRL, d16). No test of Bazazi-style pay by the group result on a frozen model. Practical reading: incentives in words do nothing; only the selection rule (what is kept) can act.

### Gap 4: heavy-tail gate (Almaatouq R) for LLM answer distributions - OPEN
Nothing found on tail shape of LLM sampled numeric answers or on gating exposure by it. Europe PMC search returned nothing relevant. Needs a direct measurement: kurtosis of log answers across N samples, then compare exposure vs no exposure by tail class.

### Gap 5: which peer-information format minimises herding - PARTLY CLOSED (open models only)
Candidate-only exchange after independent drafts: StrategyQA 65.7% vs baseline 58.3%; reasoning exchange 51.9% (d10). Visible self-reported confidence had no significant effect (coefficient 0.025, SE 0.015, d09). Prompted agreement level swings results by up to 15% and its best value flips between tasks (d13). Anti-conformity prompt plus trajectory scoring improved on Society of Minds in one round (d19) but was never compared with voting. No test of mean vs full list vs verdict only on frontier models; the human result (Jayles 2021) has no LLM counterpart.

### Gap 6: verifier-gated acceptance restoring gains - PARTLY CLOSED
An oracle that locks correct answers adds about 9 points to debate (d04); oracle labels lift GPT-3.5 GSM8K 75.9 to 84.3 while label-free self-correction gives 74.7 (d02). Real verifiers: a learned process reward model on a trained reviser (d14), and external feedback with accurate assessment reducing self-bias (d15). No test with an exact external check (run code, unit test) on multi-attempt groups. K20 stays contested.

### Gap 7: failed or null replication of Lorenz 2011 - STILL OPEN
No direct replication in a larger or non-student sample was found. Closest: Da & Huang 2020 randomised field experiments on Estimize (individual forecasts better, consensus worse with more public information; abstract only, d20), and Mercier & Claidiere 2022 (N=1,958, free discussion did not hurt, boundary condition not a replication, abstract only, d21). K01 stays contested. Full-text read of Da & Huang is the next step.

### Gap 8: mixing families vs best single model - CLOSED against mixing (aggregation); OPEN for debate with frontier models
Self-MoA (best model sampled many times) beat mixed MoA by 6.6 points on AlpacaEval 2.0 and 3.8 on average (d12). Heter-MAD's gain was measured against the two-model average; my arithmetic on their Table 3 gives GPT-4o-mini CoT alone 77.0 vs Heter-SoM 76.7 (d06, not reported by the authors). With Barrera-Lemarchand d=0.88 this is K29, established. Mixing helps only in some task-specific cases (+0.17 and +0.35 points).

### Gap 9: temperature and prompt diversity - PARTLY CLOSED
Single-attempt accuracy is flat from T=0 to 1.0 (p=0.403, d17); self-consistency is robust across T=0.3-0.7 (d18). Persona prompts moved accuracy by 1.9 points (45 configs) and 3.1 points (81 configs) (d11). Not tested anywhere found: whether temperature changes how much peer exposure helps or harms. Self-MoA's regression (diversity coefficient 2.6-4.7 per unit Vendi score, d12) mixes temperature with model mix.

### Corrections and cautions from this pass
- d06 contains one number I computed, not the authors (flagged in the line).
- Wynn Table 1 row-to-model mapping was inferred from the single-agent rows because model symbols were lost in text extraction.
- Choi (d03) Table 1 vs Table 2 vanilla values differ slightly (0.7377 vs 0.7332 at T=2), both recorded as printed.

### Still open after this pass
Gaps 3 (frozen-model incentive), 4 (heavy-tail gate) and 7 (replication) are essentially untouched; gaps 1, 2, 5, 6, 9 have open-model evidence but need a frontier-model test. Most useful next step: a single experiment with N attempts, arms (a) independent plus median, (b) peer exposure in three formats, (c) exposure accepted only through an exact check, at equal tokens and two temperatures, logging log-variance and tail shape.
