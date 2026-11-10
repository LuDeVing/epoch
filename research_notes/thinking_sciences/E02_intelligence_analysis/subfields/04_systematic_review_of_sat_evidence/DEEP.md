# Systematic review of SAT evidence: deep document

*Subfield E02.04. Written 2026-11-10 from evidence_a-d.jsonl, claims.jsonl (K01-K34) and critique.md in this folder. Ids like a09 or d08 are evidence lines; K-ids are claims. Numbers marked "corrected" were re-opened in the critique pass. Nothing here is added to SCHEMA.md until the tests in UNKNOWNS.md pass.*

## 1. What it is

Structured analytic techniques (SATs) are named procedures that intelligence analysts are told to follow: Analysis of Competing Hypotheses (ACH), brainstorming, devil's advocacy, key assumptions check, red team, Team A/Team B, alternative futures, pre-mortem and others. The CIA Tradecraft Primer lists 12. They spread by endorsement (Heuer, Pherson), not by trial (b15).

This subfield asks one question: what does the pooled evidence say about whether they work? Its anchor is Coulthart's Pitt dissertation (2015; journal version 2017, IJIC). The abstract says a systematic review of a random sample of more than 2,000 studies found moderate to strong support for ACH, brainstorming and devil's advocacy. It reports three findings (a01, d01):

1. Face-to-face collaboration lowers creativity.
2. Weighing evidence matters more than seeking disconfirming evidence.
3. Conflict tends to improve analysis quality.

A 21-student experiment (graduate intelligence-studies students) "confirmed" the first two. A survey of 80 analysts at one agency found 1 in 3 never used SATs. Training (p=0.001, V=0.41) and perceived value (p=.049, V=0.23) predicted use. Time pressure did not (p=0.74) (a02, d01).

Why it matters for our agent: the headline is a vote count over mostly non-intelligence studies (group decision making, creativity labs). The claims map to scaffold ideas: a hypothesis matrix (ACH), independent idea generation (brainstorming), assigned dissent (devil's advocacy), evidence weighing, and conflict. The direct evidence on each is far weaker than the headline. The founding review was only read through its abstract; the PDF is behind a bot wall.

Scope. We cover (a) the Coulthart review and its critics, (b) the controlled ACH experiments (Wilcox and Mandel 2023 review), (c) the conflict and dissent meta-analyses, (d) every LLM or AI study found that tests or uses ACH, debate, devil's advocacy, pre-mortem or evidence weighing, 2020-2026. We do not repeat the debiasing, calibration or sycophancy literature in other folders; see section 9 and the parallel subfields (Calibration and overconfidence, Debiasing and cognitive forcing, Peer review and replication, Social epistemology, Conformity, Aggregation and extremizing).

## 2. History and theories in depth

**Origin (1970s-1999).** Heuer's work at the CIA argued that analysts confirm their first hypothesis. ACH was his fix: list all hypotheses, list evidence, mark each item consistent, inconsistent or neutral per hypothesis, then prefer the hypothesis with the least inconsistent evidence. The key rule: evidence consistent with many hypotheses is not diagnostic. Heuer never ran experiments on ACH (b15).

**Early tests (2000-2008).** Folker (2000) ran two controlled experiments: structured hypothesis testing improved accuracy markedly in one, little in the other (b14). A Mitre experiment (Lehner, Adelman, Cheikes and Brown 2008; USS Iowa case) found ACH cut confirmation bias only among people without intelligence experience. The ACH cell had 5 experienced analysts, the control 7 (a08, b13). Tetlock (2005) found scenario development lowered forecast accuracy in two experiments. Heuer and Pherson dispute this, because scenarios outline futures and do not predict (b14). RAND (Artner, Girven, Bruce 2016) concluded SATs have little formal evaluation and the cited tests are dated, mixed and not IC-like (b14). A RAND review, cited by Martin, found only 22 of 63 unclassified reports (about 35%) used SATs, and agencies did not track whether they helped (a06).

**The Coulthart review (2015, 2017).** Second-hand (b02, from Martin 2025): of the 12 Primer SATs only 6 had any empirical test: Devil's Advocacy, ACH, Brainstorming, Alternative Futures Analysis, Red Teaming, Team A/Team B. The share of supporting studies ran from 0 to 100% by technique. Only the first three had credibility above "low". The grades are Coulthart's own. Mandel, Karvetski and Dhami (2018) quote him saying ACH was "effective and had a highly credible evidence base" (2017, p.377) and call that unwarranted (d02). Per-technique study counts and effect sizes remain unread (K01).

**Judgment science turns on SATs (2015-2023).** Mandel (2015) showed brief natural-frequency instruction improved the coherence of 43 analysts' Bayesian judgments (b19). Chang, Berdini, Mandel and Tetlock (2018) argued SATs should be redesigned around judgment-science evidence (a20, snippet only). Mandel and Tetlock (2018) argued judgment correctives can add noise and called for tournaments and trials (b15). Mandel, Karvetski and Dhami (2018) ran the first randomised ACH trial, with 50 UK analysts (a09). Karvetski, Mandel and colleagues ran three lay-panel studies (a11, a12, b06, b07). Wilcox and Mandel (2023) reviewed every ACH-vs-no-SAT-control experiment they found and advised against mandating ACH (a07, b03). Caveat: the same group wrote two of the six included experiments and the review itself (b03, b15).

**Process versus outcome (2016-2026).** Marcoci et al. (2019) showed tradecraft-standard scoring is unreliable for a single rater (b16). Martin (2025) found technique use tracks process quality, not accuracy (a04, a05, b17). Dhami et al. (2024) showed a feature of ACH, the hypotheses-in-rows layout, reduced confirmation bias while the standard columns layout did not (b08). Otzipka and Volbert (2026) found ACH did not reduce allegiance bias in expert-witness credibility judgments (preregistered; b12).

**Conflict and dissent theory (1990-2012).** Schwenk (1990) meta-analysed devil's advocacy and dialectical inquiry in lab decision tasks. Recollection: both beat consensus (a18, unverified). De Dreu and Weingart (2003) found task conflict correlated negatively with team performance (a16). De Wit, Greer and Jehn (2012; 116 studies, 8,880 groups) did not replicate the strong negative task-conflict effect and found benefits only under moderators (a17). So "conflict improves quality" is a moderated, contested claim, not a general one.

**Brainstorming theory (1991).** Mullen, Johnson and Salas (1991) found interacting groups generate fewer ideas than the same number of people working alone. Standard causes: production blocking, evaluation apprehension, free riding (a19, unverified). This is the human basis for "independent first, merge later."

**LLM era (2023-2026).** Debate between LLM agents is the machine analogue of devil's advocacy and conflict. Du et al. (2023) reported large gains (a21). Later equal-compute work mostly could not confirm them (a23, a24, a25, a28). Few studies use ACH directly: AgentCDM (b27), PRISM (d06), a threat-actor paper (c05), a mixed-initiative tool (c08), and a 12-skill SAT pipeline (a30). LEAP (d08) is not ACH, but it tests the design idea ACH lacks: per-item rating with code-side weighing.

**Competing explanations of why SATs fail in experiments.**
- Premise failure: confirmation bias is rarer than assumed. 66.1% of 62 Dutch military analysts were balanced (b08). Law students showed little bias in either arm (a14).
- Protocol failure: people do not follow the steps. Only 38% of ACH law students used the matrix (a14, b10). Most ACH-trained analysts broke ACH rules. 80% of controls built a matrix unprompted (a10, b09).
- Design failure: ACH scoring (count inconsistencies, ignore consistency) breaks Bayesian norms, gives no rule for weighing, and does not handle correlated cues (a07, b07, b12).
- Power failure: samples range from 12 to 227 (a15). Small samples miss real effects and inflate others.

## 3. Core findings with exact numbers

Status: established = two or more independent sources; single-source = one team or paper; contested = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Coulthart review rates ACH, brainstorming, devil's advocacy moderate to strong | random sample of over 2,000 studies; 21-student experiment; per-technique counts unread | a01, b01, d01 | single-source; vote count; abstract only |
| Only half of SATs have any test | 6 of 12 tested; 3 of 6 above "low" credibility; support share 0 to 100% | b02, a03, b14 | established (2 sources), second-hand |
| ACH as a whole: no gain in judgment quality vs a no-SAT control | 244 records, 7 papers, 6 experiments; accuracy null in 3 of 3 that measured it; confirmation-bias reduced in 1 of 4 (novices only) | a07, b03, b04 | established; narrative vote count; reviewers wrote 2 of the 6 |
| ACH trial, 50 UK analysts: accuracy | MAE control .21 vs ACH .26, p=.14, d=0.43 (corrected from 0.45), favouring control | a09, b05 | single-source (same trial in a09, a10, b05, b09) |
| ACH improves cue-usefulness judgments | usefulness tracks probability gain r=.68 ACH vs .17 control, d=1.59, p<.001 | a09 | single-source |
| Post-hoc code fixes beat ACH | coherentising .23 to .15 (35% cut); averaging all 50 analysts .09 (61% cut) | a09, b05 | established with b07 |
| Lay panel, ACH vs Bayes-style elicitation (N=147) | no unaggregated accuracy difference; ACH less coherent; aggregation gave "just over 1 SD" error cut | b07, a11 | single-source preprint |
| Largest ACH vs control test (N=227, gang graffiti) | unreliability MAD .22 [.19,.24] vs .18 [.16,.20], d=.20, p=.051; other contrast t(218)=1.14, p=.25, d=.15; pseudo-diagnosticity | b06, a12 | established with b07 (double counting) |
| Double counting of correlated cues | rose when the correlation was made salient | b07, a11 | established |
| ACH training, small samples | Whitesmith N=39 null (8 of 39 showed bias); Maegherman N=191, 38% used the matrix, no difference in guilt ratings; Lehner 5 vs 7, novice-only effect | a13, b11, a14, b10, a08 | established (null, underpowered) |
| ACH and expert-witness allegiance | N=159 (ACH 86, control 73); method F(1,153)=.21 p=.649; interaction F(2,153)=1.12 p=.328 | b12 | single-source; preregistered; 78 failed knowledge checks |
| Matrix layout changes confirmation bias | chose confirming hypothesis: rows 39.2% (20), columns 61.8% (34), text 67.3% (37); N=161; chi2(2)=9.43, p=.009, phi=.24 | b08 | single-source |
| Confirmation bias is rare in experts | 62 analysts: 19.4% confirmation, 14.5% inconsistent, 66.1% balanced; 83.3% sensitive to credibility | b08 | established with a14, b11 |
| Process quality tracks technique count; accuracy does not clearly | count vs QoR r=.46; vs accuracy r=.23, p=.15; QoR vs accuracy partial r(77)=.25, p=.028; ACH vs accuracy r=-.08; Timeline best r=.28; N=138 reports, about 80 scored | a04, a05, b17 | single-source (one preprint), observational |
| Tradecraft-score reliability | single-rater ICC .366; 2 raters .498; 3 raters .608; 15 raters .897 | b16 | single-source |
| Natural-frequency instruction | 43 analysts; over 4/5 answered all 8 problems additively after, over half before | b19 | single-source, no control |
| Bayesian-network group method | Glass delta 1.4-2.2 vs unaided; N=256 (25 teams of 6-9 vs 58 individuals) | b18 | established with b19 and b07 (Bayes-structured methods win) |
| Task conflict meta-analyses | 2003: negative; 2012: 116 studies, 8,880 groups, strong negative not replicated; positive only under moderators | a16, a17 | contested |
| Assigned dissent vs consensus (Schwenk 1990) | no numbers read | a18 | single-source; unverified |
| Brainstorming groups lose ideas (Mullen 1991) | no numbers read | a19 | single-source; unverified |
| Debate beats single answer (original) | ChatGPT, 3 agents, 2 rounds. Arithmetic 81.8 vs single 67.0, majority 69.0, reflection 72.1. GSM8K 85.0 vs 77.0. MMLU 71.1 vs 63.9 (reflection 57.7). Biographies 73.8 vs 66.0. Chess validity 45.2 vs 29.3 | a21, b20, c13 | single-source; unequal compute; old model |
| Debate does not beat self-consistency at equal compute | GSM8K 6 responses: debate 83.2 vs SC 85.3 (corrected). MedQA Medprompt .65, SoM .64, SC .60, single .60, Multi-Persona .58. 36 configs: AgentVerse beat CoT in about 15% | a23, a24, a28, b21, b22, d03, d13 | contested (next row) |
| Debate slightly beats SC at equal compute (2026) | MMLU-Pro CoT 64.3; SC 68.7 (10 samples); debate 70.0 (4 agents); MoA 71.4; debate +1.3, MoA +2.7 over SC | d11 | single-source; contradicts the row above |
| Debate vs independent-first majority, small models | accuracy fell after debate in most mixed groups; e.g. MMLU one-of-each 40.0 to 28.0; CSQA 53.4 to 46.8; GSM8K 61.0 to 64.8 | d03 | single-source (Wynn 2025) |
| Debate flips correct answers to wrong | correct-to-incorrect exceeds incorrect-to-correct; highest when the agent is alone; "be correct" prompt did not cut flips | a27, b23, c15, d04, d05 | established (4 sources) |
| Sycophancy under pressure | "Are you sure?": Claude 1.3 wrongly admits a mistake 98%, GPT-4 42%; wrong user hint cuts accuracy up to 27% (LLaMA 2); argumentative thread: 13 assistants, median 50% to 79% | b25, c21, d17 | established; old models; b25 figures unverified |
| Self-correction without oracle lowers accuracy | GPT-3.5 CSQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 91.5 to 89.0; oracle labels GPT-3.5 GSM8K 84.3, CSQA 89.7, HotpotQA 29.0 (corrected) | a24, c16 | single-source (one team); old models |
| Dissent strength has a task-dependent optimum | counterintuitive arithmetic MAD 37.0 vs 26.0 base, SC 29.5; MedQA liked 90% agreement, CIAR liked disagreement; forced-disagreement MAD weakest in Wang 2024 | a22, c14, c19, a25 | contested |
| Role- or model-diverse panels beat identical ones | ChatEval same-role panel 53.8 acc, kappa .25; Heter-MAD +5.8% / +4.4% over CoT average; DynaDebate AIME24 35.56 to 28.89 without diverse start, MATH500 only -1.44 | a29, a28, d13 | established (3 sources) |
| Zero-shot ACH-style decider prompt (AgentCDM) | all-average single 66.0; voting 79.9-80.6; ACH decider (Qwen-7B-Instruct) 82.2; R1 87.6; trained 88.4; scaffold-only ablation 68.1/49.4/84.0 vs vanilla 72.6/52.5/89.0 | b27, c01-c04, c24 | single-source; trained 7B model; table alignment partly uncertain |
| ACH inside a structured pipeline (PRISM, MuSR, 10 models) | Direct 58.1; CoT 57.2; SC 63.2; PRISM 71.3. Filter-only 63.8; profiling +6.7; ACH matrix +0.8 | d06, d07 | single-source; tokens not matched; LLM judge |
| Code-aggregated evidence rating (LEAP) | FutureX .6512 to .7284; Brier .2689 to .2057; ECE .1840 to .0876; token-matched control .6736 / .2497 / .1471 | d08 | single-source; forecasting, not ACH |
| Dependency clustering by code | without it FX .7089 (-1.9), ECE .0876 to .1578; source-key grouping keeps 4.37 of 5.12 items | d09 | single-source |
| Models verify then still adopt invalid candidates | 93-100% adoption with propositional constraints; exact repeats discounted; distinct second message sub-additive; over 10 million trials, 12 models | d10 | single-source (one team) |
| 12-skill SAT pipeline on 15 LLMs (HypoEval) | 988 cases; arena rating change +88 (kimi-k2.5) to -60 (claude-opus-4.6); Spearman with baseline strength -0.10 | a30 | single-source; model-dependent |
| Extra structure pays on hard items | MMLU-Pro bins by solve rate: easy +2.2, medium +8.5, hard +9.0 at 15-20x compute | d12 | single-source |
| Pre-action devil's advocate in an agent loop | WebArena 23.5 vs LATS 22.7; plan revisions down 45% | c20 | single-source; under 1 point |
| Pre-mortem prompt (safety, not accuracy) | harm 3.22 to 2.62 (safety prompt) to 2.19 (InvThink prompt-only) | d14 | single-source; LLM judge |
| LLM bias-mitigation prompts | awareness prompts small gains; few-shot sometimes broke the model; self-rewrite best for high-capacity models; GPT-4 admitted 40.5% more students under reject framing | b26, c17, c18 | single-source |

## 4. Mechanisms and models

Each mechanism is written so an engineer could implement it.

**M1. Per-item rating, code-side combination (the missing piece in ACH).** ACH's weakness is that humans do the weighing and break it (double counting, ignoring base rates, pseudo-diagnosticity). The design with measured support:
1. Fix the hypothesis list H1..Hn (the model proposes; code freezes it).
2. For each evidence item e_j, call the model once in isolation: "How likely is this item under H_i?" Return a number per hypothesis. The model never sees the other items or the running total.
3. Code applies a prior (base rate), multiplies likelihood ratios in log space, and normalises so probabilities sum to 1.
4. Code groups items with the same source key and keeps one (dependency clustering).
5. Code caps confidence unless a rare, discriminating item supports it (Evron: cap 0.4 unless rarity >= 0.5; c06).

LEAP (d08, d09) is this design on forecasting: FX .6736 to .7284 against a token-matched baseline, ECE .1471 to .0876. Dropping the prior put it below the plain baseline. Dropping dependency clustering cost 1.9 points and raised ECE to .1578. Human analogue: coherentising and averaging cut error 35% and 61% (a09).

**M2. Diagnosticity-first scoring.** Core ACH insight: an item that fits all hypotheses should move nothing. Implement: for each item compute the spread of its likelihoods across hypotheses; items with spread below a threshold get weight zero. GroundWork hides "neutral" items for the same reason (c08). In humans, ACH raised usefulness ratings (r .68 vs .17) but not accuracy, because the weighing stayed human (a09).

**M3. Independent first, merge in code.** From brainstorming (Mullen) and the debate failures (Wynn): generate k hypothesis lists or answers in separate contexts, then merge, dedupe and vote in code. This is the baseline debate fails to beat on small models (d03). DynaDebate adds distinct assigned solution paths before any exchange. Removing the diverse start costs 6.7 points on AIME24 (35.56 to 28.89) and 6.7 on AIME25 (27.78 to 21.11), but only 1.4 on MATH500 (d13).

**M4. Blind critic.** Conformity (b23, d04, d17) means a critic that sees the proposed answer tends to agree. Implement: the critic sees the task and evidence only, produces its own answer or list of objections, and code compares. Not tested as such (GAP 4). Sycophancy rises 2-3x in argumentative threads (d17). A "maximise correctness" instruction did not help (d05).

**M5. Triggered, not always-on, structure.** Extra structure pays most on hard items (d12). Cheap trigger: draw k independent short samples; if agreement is below a threshold or the margin between the top two answers is small, run the matrix or critic step. DynaDebate calls a verifier only on disagreement (d13). No test compares triggered to always-on.

**M6. Layout of the hypothesis state.** Humans: hypotheses in rows 39.2% confirming vs columns 61.8% vs text 67.3% (b08). Implement: present candidates as a table with hypotheses as rows, rather than prose; permute order across independent samples. For LLMs only option-position bias is known (gold in slot D costs gpt-3.5 6.3 points, d16).

**M7. Natural-frequency format.** "Out of 100 cases like this, how many..." improved analysts' Bayesian coherence (b19). Cheap to try as the prompt format for the per-item rating in M1.

**M8. Compression failure (candidate compression).** When a pipeline squeezes rich intermediate analysis into a short final list, the right answer is lost (a30). Implement: code keeps the whole candidate list with its scores to the end. The final step ranks; it does not rewrite.

## 5. What holds up

**Holds up (established).**
- ACH as a whole gives little or no accuracy gain over no SAT in human experiments (K03: accuracy null in 3 of 3; bias reduction in 1 of 4; N from 12 to 227).
- Post-hoc code processing beats the technique (K05): coherentising 35%, averaging 61% (a09); about 1 SD in a lay panel (b07).
- ACH users double count correlated cues and show pseudo-diagnosticity (K06).
- Humans do not follow the protocol (K07: 38% compliance; 80% of controls build a matrix unprompted).
- Confirmation bias is less common than the premise assumes (K09).
- Only 6 of 12 SATs have any tests (K02).
- LLM agents conform in debate and give in under challenge (K18, K33).
- Diverse panels beat same-role panels (K23).
- Structured Bayesian methods beat unaided people (K27).
- No controlled LLM test of pre-mortem, key assumptions check, red team or weighing vs seeking evidence on analyst tasks exists (K28).

**Failed replications and failures to confirm.**
- Task conflict: the 2003 strong negative effect was not replicated in 2012 (a16, a17).
- Debate's lead over self-consistency (Du 2023) was not confirmed at equal compute (Smit, Huang, Zhang, Wang). One 2026 study puts it +1.3 ahead (d11). The sign depends on setup.
- ACH diagnosticity: 1 positive study (2 reports of one dataset) vs 2 negative (b04).
- Lehner 2008 novice effect was not seen in experts; sample 5 vs 7.
- A zero-shot ACH scaffold alone hurt in AgentCDM (MMLU-Pro 49.4 vs 52.5 vanilla). Big gains needed RL training (b27).
- The 12-skill SAT pipeline gave no uniform gain, from +88 to -60 (a30).

**Moderators.**
- Expertise: ACH helped novices only (Lehner).
- Task type: debate helps counterintuitive items, hurts routine ones (K17; c14, a22).
- Difficulty: gains concentrate on hard items (d12).
- Agent quality: more agents help GPT-4, hurt weak 7B models (c04).
- Model strength: SAT pipeline benefit is unrelated to baseline strength (rho -0.10, a30).
- Prompt demonstration: discussion helps only when the single-agent prompt has no demonstration (a25, b22).
- Task conflict helps for top management teams, low relationship conflict, financial outcomes (a17).
- Layout: rows vs columns (b08).
- Compliance: 38% in law students (b10).

**Interventions that worked.** Code coherentising and averaging; natural-frequency instruction; Bayesian-network structure with Delphi exchange; usefulness ratings after ACH training; LEAP per-item rating plus code prior; source-key dedupe; diverse starts in debate on hard sets; evidence filtering and per-suspect profiling (PRISM: direct 58.1 to 63.8 with filter, +6.7 with profiling; the ACH matrix added +0.8).

**Interventions that did not.** ACH on probability accuracy or coherence; generic debate at equal compute; unstructured self-critique; "be correct" or "be careful" prompts; few-shot debiasing; same-persona panels; a rigid scaffold without training.

**Weak points in the evidence base (from critique.md).** The founding claim was never read beyond its abstract. Most analyst ACH tests have N under 60; the large ones used lay people. The Mandel and Karvetski group ran much of the ACH work and the review. Dhami 2019 and Mandel 2018 are one dataset. Martin's lines are one preprint. Schwenk, Mullen, De Dreu, De Wit and Sharma numbers are not re-verified. The AgentCDM table extract was misaligned: an early line gave "informed dictatorial 82.9", but 82.9 is Homogeneous ACH, and the 1.9-point zero-shot margin is the authors' own statement.

## 6. Language models

**There is almost no direct LLM test of SATs.** An arXiv search for "structured analytic techniques" with "language model" returned zero hits. "Analysis of competing hypotheses" returned four (b30, c26). The sats4llms wiki lists seven hypotheses and states they are untested (b29). A practitioner note (b28) says ACH works only as separate sequential calls and single-prompt ACH fails (anecdote, no control).

**ACH-like scaffolds on LLMs.**
- AgentCDM (b27, c01-c04): a decider agent with a four-part ACH-style protocol over other agents' answers, on MMLU, MMLU-Pro, ARC-Challenge. All-average: single agent 66.0, best voting 80.6, ACH-protocol decider with untrained Qwen-7B 82.2, with R1-distilled 87.6, trained AgentCDM 88.4. Prompt-only gain over voting is small (about +1.6; authors state 1.9 over informed dictatorial). Ablation MMLU/MMLU-Pro/ARC: full 78.5/65.2/96.0; vanilla prompt 72.6/52.5/89.0; scaffold-only 68.1/49.4/84.0. So a scaffold alone lowers results (MMLU-Pro -3.1, ARC -5.0 vs vanilla). Heterogeneous pool, MMLU-Pro: AgentCDM 67.9 vs 55.9. Mistral-7B worsened as agents increased. A decider trained on hard MMLU-Pro transferred (80.84 MMLU, 94.0 ARC); one trained on easy ARC transferred poorly.
- PRISM (d06, d07): four-agent investigation pipeline on MuSR murder mysteries (250 items, 2 suspects, 10 models). Direct 58.1, CoT 57.2, persona 58.2, SC (5) 63.2, PRISM 71.3 (+13.2; range +6.0 Ministral-8B to +22.0 GPT-5.2; GPT-5.2 58.0 to 80.0). Ablation: evidence filter alone 63.8; profiling +6.7; ACH matrix +0.8. Tokens not matched; judge is an LLM; no significance test.
- HypoEval (a30): 12 SAT skills, 988 cases, 15 models. Effect +88 to -60 arena points. Failure mode: candidate compression.
- Adversary Brains (c05-c07): ACH scaled to thousands of machine-checkable hypotheses with code rules (cap 0.4 unless rarity >= 0.5; contradiction lowers standing, absence does not; derived conclusions never re-enter as evidence). Synthetic only; no detection rate; design rules not measured.
- GroundWork (c08, c09): ACH-style stance matrix with LLM stance labels; 4 experts; no accuracy measure. Experts preferred a persistent editable state over chat.
- CLEO (c10, c11): a minimal 3k-line harness on a fixed open model nearly matched a 512k-line one (83.8% vs 85.0%) on 240 held-out analyst questions with misleading evidence. No SAT tested.
- ARBITRA (c12, c25): role experts plus argumentation-graph verification for ATT&CK extraction. F1 .649, 15.5 above the best baseline; precision loss under adversarial perturbation about half the baselines'. Cyber labels, fine-tuned.

**Debate and dissent.**
- Du 2023 (a21): large gains, unequal compute, small samples. Smit (a23, b21, c14): no protocol beat simple baselines overall. Agreement level must be tuned (+15% for Multi-Persona and +5% Society of Mind on a 376-question USMLE subset). Huang (a24): at 6 responses debate 83.2 vs SC 85.3. Wang (a25, b22): a single agent with one demonstration matches the best discussion. Zhang (a28): 36 configurations; MAD seldom beats CoT or SC; Heter-MAD helps. Wynn (a27, d03): debate below independent-first majority in most mixed groups; flips most when alone. Wunderlich 2026 (d11, d12): debate +1.3 over SC at comparable budget, MoA +2.7; gains concentrate on hard items. DynaDebate (d13): generic MAD often no better than CoT; diverse start helps on hard sets. Khan (a26): debate raised weak-judge accuracy 48% to 76% (LLM judges) and 60% to 88% (humans), but only with an information asymmetry and a hidden ground truth.
- Liang (a22, c19, b24): degeneration of thought; MAD 37.0 vs 26.0 on counterintuitive arithmetic. The dataset was built by the authors; judge choice matters.

**Conformity and sycophancy.** Claude 1.3 admitted a mistake on 98% of "Are you sure?" challenges, GPT-4 on 42% (b25; old models). An argumentative thread raised sycophancy from a median 50% to 79% across 13 assistants (d17). Instructions to be correct did not stop flips (d05). Kawada and Kellis (d10): models integrate candidates they have verified as invalid 93-100% of the time. Agreement of two distinct messages is sub-additive. Exact repeats are discounted.

**Bias and debiasing.** BiasBuster (b26, c17, c18): awareness prompts give small gains; few-shot debiasing sometimes drove admission rates to 0 or 1; self-rewrite of the prompt worked best for GPT-4. Jhang (c22): a stated direct update moved probabilities 18-28 points per new item; source-report wording lowered it by 2-5 points; five weighted estimates cut movement 43% and 68% in two small models.

**Pre-mortem and devil's advocate.** Anticipatory reflection before each action (c20): WebArena 23.5 vs 22.7, plan revisions -45%, no intervals. Pre-mortem prompt for safety (d14): harm 3.22 to 2.19 (LLM judge). A position paper (d15) with no data.

**What changed model behaviour, by how much.**

| Change | Effect |
|---|---|
| Per-item rating plus code Bayes update with prior (LEAP) | FX .6736 to .7284 vs token-matched; ECE .1471 to .0876 |
| Remove the prior | worse than the plain baseline |
| Remove dependency clustering | -1.9 points; ECE to .1578 |
| Evidence filter + profiling (PRISM) | 58.1 to 70.5 (63.8 + 6.7); ACH matrix +0.8 |
| Independent samples, vote (SC) | MuSR 58.1 to 63.2; MMLU-Pro 64.3 to 68.7 |
| Debate over SC | -2.1 to +1.3 depending on study |
| Blind first answers, then exchange | fewer flips (direction only; no number) |
| Scaffold alone, small model | -3 to -5 points |
| Diverse initial paths | +6.7 on AIME24; +1.4 on MATH500 |
| Structure triggered on hard items | +8.5 to +9.0 vs +2.2 on easy |

**Generality caveat.** Most LLM debate evidence is from GPT-3.5, 7-8B and 70B open models, on multiple-choice benchmarks. Only Zhong 2026 (a30), Lee 2026 (d06; GPT-5.2) and LEAP (d08) use 2026 models. None has a frontier no-structure ceiling check on hard analyst tasks. Newer models are tuned against the 2023 sycophancy figures.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Do not add ACH as a default step or a scoring rule.** Human accuracy null in 3 of 3 studies; ACH scoring breaks Bayesian norms. SCHEMA 4b already says this; keep it and cite the extra sources. Part: 4b. [E] (a07, b03, b04, a09, b06, b07, b12, K03)
2. **Code does the combining of any evidence.** If evidence from several items is combined, code does weights, normalisation and averaging; the model rates single items. Part: G5 (already there). Extra support: coherentising -35%, averaging -61% in analysts. [E] (a09, b07, K05)
3. **Handle correlated or duplicate evidence in code.** Tag items with a source key; keep one per group. Part: G5 / S4. [E] for the human failure (a11, a12, b06, b07, K06). The size of the fix is [S] (d09: -1.9 points without it), so add it as a rule but measure it.
4. **Enforce steps in code, not in text.** Humans skip steps (38% compliance); LLMs conform and ignore instructions. Part: G1/G5 (already there). [E] (a10, a14, b09, b10, K07)
5. **No default dissent, and no in-thread critic that sees the proposed answer.** Conformity flips right to wrong; "be correct" prompts do not fix it. Part: G4, G5, G9 (already there). [E] (a27, b23, d04, d05, d17, b25, K18, K33)
6. **Diverse independent samples beat same-role panels.** Part: G4, S3 (fresh context, already there). [E] (a29, a28, d13, K23)
7. **Measure by outcome, not by process-looking output.** Technique count tracks quality scores, not accuracy; one rater is unreliable (ICC .366). Part: G7. [S] per line (a05, b16, K10, K11), but it follows from K02 and G10; use as a rule.
8. **Do not trigger doubt on a schedule: confirmation bias is rarer than assumed.** Part: G1 (already there). [E] (b08, a14, b11, K09)

### Test first

1. **Code-weighted matrix vs plain judge vs prompt-only ACH, at equal tokens.** Part: new operator near S7 (hypothesis comparison); G5. [S] (d08, d09, d06, d07, K29, K32). Closest evidence: LEAP (no ACH arm) and PRISM (+0.8 for ACH).
2. **Trigger on disagreement, not always-on.** Part: G1, S0/S6 trigger. [S] (d12, d13, K31).
3. **Blind critic whose output code applies.** Part: S7/G5. [S] (K18, K33; no direct test of this design).
4. **Source-key dedupe with paraphrase duplicates.** Part: G5. [S] (d09, d10, K30).
5. **Independent lists merged in code vs one shared-context list (brainstorming transfer).** Part: S3 open mode. [S] (a19 unverified, a31, d13, K14, K22).
6. **Natural-frequency format for per-item ratings.** Part: G5 / matrix prompt. [S] (b19, K27).
7. **Hypothesis layout rows vs columns; permute order across samples.** Part: S2 display. [S] (b08, d16, K08, K34).
8. **Pre-action devil's advocate at S8 on high-stakes steps.** Part: S8 / O8. [S] (c20, d14, K24).
9. **Keep the wide candidate list to the end (no compression).** Part: S7. [S] (a30, K21).
10. **Weighing evidence vs seeking disconfirmation.** Part: S7 counterexample search (already [E] for the preference for confirming tests). [C] (a01 only; K28). No LLM test exists.

## 8. Concrete tests on our bench

All arms at equal total tokens (count setup, all calls and merge text). Items need known answers. Report accuracy with a 95% interval; log flips (right to wrong, wrong to right), tokens per state and trigger rate. Use at least 100 items per arm per type; with fewer, read results as direction only.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Hypothesis-choice items with 4+ hypotheses and 8-12 evidence items, known answer (MuSR-style, planted correlated and misleading items) | (a) plain judge, (b) prompt-only ACH in sequential calls, (c) code-weighted matrix with per-item ratings and prior, (d) plain SC at the same tokens | accuracy, Brier, ECE | (c) beats (a) by 2-7 points and ECE falls (LEAP .1471 to .0876); (b) within +-1 of (a) |
| T2 | Same items with duplicated and correlated evidence (exact repeat, paraphrase, shared source) | code-side source-key dedupe vs none vs LLM-side "ignore duplicates" | accuracy on duplicate items; ECE; double-counting index (posterior shift per duplicate) | dedupe +1 to +2 points, ECE -.05 on duplicate items (d09); paraphrases less |
| T3 | Hard counterintuitive items and routine items | single answer; k independent samples + vote; shared-thread debate; blind critic + code rule; assigned dissent that sees no answer | accuracy by difficulty bin; right-to-wrong flip rate | debate no better than vote; blind critic helps hard items only; fewer flips for blind |
| T4 | Mixed items | always-on matrix/critic vs triggered on low agreement among 3 samples vs plain | accuracy; tokens; trigger rate | triggered matches always-on at 30-60% of the tokens; gain on hard bin about +8 |
| T5 | Open hypothesis-generation items with an enumerable valid set | one shared-context list vs k independent lists merged in code vs stratified sampling | distinct valid hypotheses; coverage of the true set | independent merge raises coverage; shared list collapses to few modes (a31) |
| T6 | Hypothesis-choice items with a confirming hypothesis planted first | rows vs columns vs prose layout; fixed vs permuted order across samples | rate of choosing the planted hypothesis | permuting order cuts position bias (gold in D cost gpt-3.5 6.3 points); layout effect unknown |
| T7 | Items with misleading evidence | (a) code-weighted matrix, (b) matrix + forced disconfirmation search, (c) plain judge | accuracy; calibration | (a) matches (b); forced search adds nothing or hurts (our G1 data: 92% vs 75%) |
| T8 | Multi-step investigation tasks | with and without a pre-action "what could go wrong" check, fired only before irreversible steps | success rate; revisions per task | small (c20: +0.8 point); probably below noise; run only if cheap |
| T9 | Tasks with a long evidence pool | full candidate list kept to the end vs compressed to a short list after analysis | recall of the correct answer in the final output | compression loses answers (a30) |
| T10 | Items with a stated wrong hint or "Are you sure?" challenge | current model, in-thread vs blind critic | flip rate | in-thread flips high on old models; check whether current models still do it |

## 9. What does not transfer, and why

- **Confirmation-bias remedies.** The ACH premise is a human bias (anchoring on a favourite hypothesis, seeking confirming tests). It is rare in experts (66.1% balanced). LLMs have their own failures: conformity, option-position bias, fixation, mode collapse, verbosity. A fix designed for the human bias does not target these.
- **The matrix as a thinking tool.** For humans the matrix is a memory aid and a layout. An LLM already has the evidence in context; a prose matrix adds tokens, and prompt-only ACH gave about +2 points or less (b27, d07). Its value is only as a data structure that code can score.
- **Brainstorming group loss.** Production blocking and evaluation apprehension do not exist for independent LLM samples. What transfers is the structure: independence, then merging. LLM samples are correlated (G4), so the human gain from nominal groups will be smaller.
- **Devil's advocate as a social role.** A human advocate has an incentive and independent knowledge. An LLM advocate has the same weights and conforms to what it is shown. Assigned dissent may only add noise unless the critic is blind.
- **Conflict improves quality.** The human mechanism is shared information and accountability, mixed with relationship harm. None of that exists in a single-agent loop. Even in humans the claim is moderated (a17).
- **Training analysts.** Compliance, training and experience effects (38% compliance, novice-only effects) do not apply to a model that follows a fixed script. The LLM analogue of training is RL on the structure, which we do not do.
- **Vote-count reviews.** Counting studies that support a technique says nothing about effect size on our tasks. The Coulthart review is not usable as a size prior.
- **Process scoring.** Tradecraft standards (ICD 203) reward looking rigorous. LLMs write rigorous-looking text cheaply (G10). Never score the scaffold on it.
- **Older-model debate and sycophancy numbers.** GPT-3.5-era figures may not hold on current models (b25 note), though 2025-2026 studies point the same way.

## 10. Open questions

1. What per-technique counts and effect sizes does Coulthart (2017) report, and how many studies are intelligence-like? (PDF behind a bot wall.)
2. Are the Schwenk 1990 and Mullen 1991 effect sizes as remembered? Do they replicate for LLM "teams"? No LLM brainstorming-teams study was found.
3. Does a code-scored hypothesis matrix beat both a plain judge and prompt-only ACH at equal tokens on items with known answers? Two of the three arms exist, in separate studies; none has all.
4. Does a critic that sees no proposed answer beat self-consistency at equal tokens on current frontier models, and for which item types?
5. What signal best predicts when structure helps (disagreement, margin, tie)? Triggered vs always-on has no direct test.
6. Does weighing evidence beat seeking disconfirming evidence for an LLM? No test.
7. How do current LLMs handle paraphrased duplicates and partly correlated items? Does code-side dependence fix them when the same model writes the dependency key?
8. Do pre-mortem, key assumptions check and red team improve accuracy on analyst-style tasks (not safety, not web navigation)?
9. What are the exact flip rates in Wynn 2025, and do independent-first sampling or model mixing reduce them?
10. Does hypothesis layout (rows vs columns) change LLM anchoring?
11. Can the 12-skill SAT pipeline effect be predicted? It was unrelated to baseline strength (rho -0.10, a30).
12. Why is the 2026 equal-compute debate result (+1.3) opposite to the 2024-2025 results? Model size, task, or how compute is counted?
13. Does ACH work better in humans when a code-side Bayesian step scores the matrix? Karvetski 2020 (b07) tested factorised Bayes elicitation against ACH and found neither fixed correlated evidence.

## 11. Sources

[V] = opened and read this run. [M] = snippet, abstract only, or second-hand. Some [V] items were read in part only (see limits in the evidence files).

- [V] Coulthart (2015) dissertation abstract, Univ. of Pittsburgh. https://d-scholarship.pitt.edu/26055/ (full text blocked; abstract also at https://core.ac.uk/works/19937451) (a01, a02, b01, d01)
- [M] Coulthart (2017) IJIC systematic review of the 12 Primer SATs, via Martin 2025 (a03, b02)
- [V] Martin (2025) SAT use and analysis quality, PsyArXiv. https://osf.io/preprints/psyarxiv/7p9v4_v1 (a04, a05, a06, b17)
- [V] Wilcox and Mandel (2023) Critical review of ACH. https://osf.io/preprints/psyarxiv/an32t_v1 (a07, a08, a10-a15, b03, b04, b05, b09, b11)
- [V] Mandel, Karvetski, Dhami (2018) Boosting intelligence analysts' judgment accuracy, JDM 13(6). https://jbaron.org/journal/18/18803/jdm18803.html (a09, d02)
- [V] Karvetski and Mandel (2020) Coherence of probability judgments. https://osf.io/preprints/psyarxiv/7xg8j_v1 (b06)
- [V] Karvetski, Mandel, Irwin (2020) From structured analysis to statistical aggregation. https://osf.io/preprints/psyarxiv/fb9ej_v1 (b07)
- [V] Dhami et al. (2024) task structure and confirmation bias. https://pmc.ncbi.nlm.nih.gov/articles/PMC11169332/ (b08)
- [M] Dhami, Belton, Mandel (2019) ACH in intelligence analysis, ACP, via secondary (a10, b09)
- [M] Maegherman et al. (2021) ACH in legal decision-making, via secondary (a14, b10)
- [M] Whitesmith (2020) ACH and bias, via secondary (a13, b11)
- [M] Lehner et al. (2008) Confirmation bias in complex analyses, via secondary. https://www.rand.org/pubs/research_reports/RR1408.html (a08, b13)
- [V] Otzipka and Volbert (2026) ACH and expert witnesses, PLoS One. https://pmc.ncbi.nlm.nih.gov/articles/PMC13094959/ (b12)
- [V] Artner, Girven, Bruce (2016) RAND RR-1408. https://www.rand.org/pubs/research_reports/RR1408.html (b14; the PDF returned 403, so a06 is second-hand)
- [V] Mandel and Tetlock (2018) Correcting judgment correctives. https://pmc.ncbi.nlm.nih.gov/articles/PMC6309046/ (b15)
- [V] Marcoci et al. (2019) Better Together. https://www.frontiersin.org/articles/10.3389/fpsyg.2018.02634/full (b16)
- [V] Korb et al. (2020) BARD. https://pmc.ncbi.nlm.nih.gov/articles/PMC7314942/ (b18)
- [V] Mandel (2015) Information structuring. https://pmc.ncbi.nlm.nih.gov/articles/PMC4389401/ (b19)
- [M] Chang, Berdini, Mandel, Tetlock (2018) Restructuring SATs. https://doi.org/10.1080/02684527.2017.1400230 (a20)
- [M] De Dreu and Weingart (2003). https://pubmed.ncbi.nlm.nih.gov/12940412/ (a16)
- [M] De Wit, Greer, Jehn (2012). https://pubmed.ncbi.nlm.nih.gov/21842974/ (a17)
- [M] Schwenk (1990). https://doi.org/10.1016/0749-5978(90)90051-A (a18, unverified)
- [M] Mullen, Johnson, Salas (1991). https://doi.org/10.1207/s15324834basp1201_1 (a19, unverified)
- [V] Du et al. (2023) Multiagent debate. https://arxiv.org/abs/2305.14325 (a21, b20, c13)
- [V] Liang et al. (2023/2024) Divergent thinking via MAD. https://arxiv.org/abs/2305.19118 (a22, b24, c19)
- [V] Smit et al. (2024) Should we be going MAD. https://arxiv.org/abs/2311.17371 (a23, b21, c14)
- [V] Huang et al. (2024) LLMs cannot self-correct yet. https://arxiv.org/abs/2310.01798 (a24, c16)
- [V] Wang et al. (2024) Are multi-agent discussions the key? https://arxiv.org/abs/2402.18272 (a25, b22)
- [V] Khan et al. (2024) Debating with more persuasive LLMs. https://arxiv.org/abs/2402.06782 (a26)
- [V] Wynn, Satija, Hadfield (2025) Talk isn't always cheap. https://arxiv.org/abs/2509.05396 (a27, b23, c15, d03, d04, d05)
- [V] Zhang et al. (2025) Stop overvaluing MAD. https://arxiv.org/abs/2502.08788 (a28)
- [V] Chan et al. (2023) ChatEval. https://arxiv.org/abs/2308.07201 (a29)
- [V] Zhong et al. (2026) HypoEval. https://arxiv.org/abs/2607.15766 (a30)
- [V] Chen et al. (2025) HypoSpace. https://arxiv.org/abs/2510.15614 (a31; abstract and intro only)
- [V] Sharma et al. (2024) Sycophancy. https://arxiv.org/abs/2310.13548 (b25, c21; the 98%/42%/27% figures were not re-verified)
- [V] Echterhoff et al. (2024) BiasBuster. https://arxiv.org/abs/2403.00811 (b26, c17, c18)
- [V] Zhao et al. (2025) AgentCDM. https://arxiv.org/abs/2508.11995 (b27, c01-c04, c24)
- [V] Evron (2026) Adversary Brains. https://arxiv.org/abs/2610.35624 (c05-c07)
- [V] Vink et al. (2026) GroundWork. https://arxiv.org/abs/2611.09840 (c08, c09)
- [V] Gefen et al. (2026) CLEO. https://arxiv.org/abs/2611.03434 (c10, c11)
- [V] Jin and Shin (2026) ARBITRA. https://arxiv.org/abs/2610.39433 (c12, c25)
- [V] Wang et al. (2024) Devil's advocate anticipatory reflection. https://arxiv.org/abs/2405.16334 (c20)
- [V] Jhang (2026) Hearsay or fact. https://arxiv.org/abs/2610.27745 (c22, c23)
- [V] Lee, Kang, Shin (2026) PRISM. https://aclanthology.org/2026.acl-long.1056.pdf (d06, d07)
- [V] Chen et al. (2026) LEAP. https://arxiv.org/pdf/2609.01337 (d08, d09)
- [V] Kawada and Kellis (2026) Evidence integration in LLMs. https://arxiv.org/pdf/2609.04290 (d10)
- [V] Wunderlich et al. (2026) Pareto-optimal test-time scaling. https://arxiv.org/pdf/2605.01566 (d11, d12)
- [V] Li et al. (2026) DynaDebate. https://arxiv.org/abs/2601.05746 (d13)
- [V] Kim et al. (2025) InvThink. https://arxiv.org/abs/2510.01569 (d14)
- [V] Suh et al. (2025) Don't just translate, agitate. https://arxiv.org/abs/2504.12424 (d15; position paper)
- [V] Zheng et al. (2024) LLMs are not robust multiple choice selectors. https://arxiv.org/abs/2309.03882 (d16)
- [V] Nogueira et al. (2026) Opinion bias and sycophancy via persuasion. https://arxiv.org/abs/2604.21564 (d17)
- [M] Roberts (2025) LLM SATs FTW, via wiki summary. https://mattdot.github.io/sats4llms/sources/roberts-llm-sats-ftw-2025 (b28)
- [V] sats4llms wiki (2026). https://mattdot.github.io/sats4llms/ (b29)
- [M] arXiv searches for ACH and SATs (b30, c26). https://arxiv.org/search/?query=%22analysis+of+competing+hypotheses%22&searchtype=all
