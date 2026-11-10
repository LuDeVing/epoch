# Methodologies of discovery: deep document

Folder: D01.07. Evidence ids (a01-a25, b01-b26, c01-c26, d01-d20) point to the evidence_a-d.jsonl files. Claim ids (D01.07-K01 to K23) point to claims.jsonl. Corrections from critique.md are applied here.

## 1. What it is

This subfield asks one question: how do we choose which idea deserves work before we know if it is true? Philosophers of science call the pieces of the answer "methodologies of discovery". Four ideas matter.

- **Discoverability** (Nickles). A claim is supported if it could have been reached from known results by a reasoned route. This is "generative justification". It differs from "consequential justification", which checks novel predictions after the fact (a01, b14).
- **Preliminary appraisal and weak evaluation** (Schaffner). Before strong tests, we give reasons to take a hypothesis seriously enough to develop. Strong evaluation gives reasons to accept it as approximately true (a02, a08).
- **Pursuit** (Laudan). A third context beside discovery and justification: the decision to work on an idea at all (a04, a05).
- **Heuristic strategies and schema instantiation** (Darden). Mechanism discovery runs in phases: generate, appraise, revise. One strategy fills an abstract template. Protein synthesis started from "reactant1 + reactant2 = product" and was then specified (a03, b15).

Why it matters for our agent: the agent writes candidate ideas and has a fixed token budget. Two decisions follow. (1) The S0 gate: is this idea new, reachable, and worth a probe? (2) The pursuit decision: which of K candidates gets the next tokens? The philosophy gives the shape of these decisions. It gives no numbers. The numbers come from 2023-2026 LLM studies, almost all from one research circle (Si, Yang, Hashimoto, Wen). The only independent check is Beel et al. on the AI Scientist (b10).

Main honest finding: the philosophy has no direct empirical test (b14). The LLM evidence says model judgment of ideas is near chance, and only measured outcomes, retrieval of real papers, or outcome-trained predictors beat it.

## 2. History and theories in depth

All philosophy items below were read through the Stanford Encyclopedia (Schickore) entries, a secondary source. Nickles, Schaffner, Darden and Laudan were never opened (critique.md). Treat attribution details as reported, not checked.

**The split into contexts.** Reichenbach separated discovery from justification; Popper left conception of ideas outside logic. This became a demarcation rule: the generation of ideas is psychology, only testing is logic (a09). Reichenbach's own view was subtler. Kuhn treats discovery as an extended process that starts at an anomaly. Whewell describes a happy thought, colligation, then verification (a09).

**Hanson and retroduction.** Hanson's schema: a surprising phenomenon appears; it would not be surprising if a hypothesis of type H held; so there is reason to elaborate H. Kepler's Mars orbit is the example. Critics: Lugg (1985) finds the Kepler story historically inadequate. Harman (1965) says the schema is too permissive when many hypotheses explain the same data. Abduction also does not say how an idea is first conceived (a06). Status: endorsed but weak for ranking (K17).

**Laudan and the abandonment of the logic of discovery.** Laudan argued the shift from generativism to consequentialism in the 19th century drove the rejection of a logic of discovery. He conceded in 1983 that fallibilism does not rule one out. Critics say pursuit is not wholly outside discovery and justification (a05, snippet only, unverified). In his three-context view, pursuit is the decision to work on a theory. Many methodologists fold pursuit back into justification (a04).

**Nickles and generative justification.** Discovery methodology is reasoning to a claim, judged by whether it could have been found with the available information. The model case is Newton's deduction from the phenomena (a01). Nickles 2018 ("tools to theory") adds that heuristics can be ranked by reasons even without guarantees (a08).

**Schaffner and weak evaluation.** Discovery procedures already contain appraisal. Weak evaluation says "develop this". Strong evaluation says "accept this" (a02).

**Preliminary appraisal.** Field-specific criteria are applied before rigorous testing (a08). Seselja and Strasser proposed coherence-based indicators of pursuitworthiness: potential consistency, potential inferential density, potential explanatory power (b20, snippet only).

**Darden and schema instantiation.** Strategies for generating, evaluating and revising mechanism schemas: schema instantiation, modular subassembly, forward and backward chaining (a03, c22). SEP says they are sufficient, not necessary, and only weakly normative. Wimsatt (2007) warns heuristics bring systematic bias. Hey (2016) asks for principles to evaluate heuristics. Chow (2015) says "heuristic" has many meanings (b15). Bechtel and Richardson (1993), Arabatzis (2006, the two contexts are inextricable) and Nersessian (2008, reasoned routes via analogy, imagery, thought experiments) sit nearby (a10).

**Computational discovery.** Simon, Langley and Bradshaw (1981): BACON searches a problem space for regularities and re-derives Kepler's third law. KEKADA simulates the Krebs cycle. Heuristics: means-ends analysis, start with the sub-problem with fewest unknowns (a07). Gillies (1996): a program cannot decide by itself which data are relevant or what form of law to seek. Re-discovery with a hand-picked representation is weak evidence. LLM-SR (2024) is the modern version (a23). Sibling folder 06 covers machine discovery more fully.

**Social epistemology of pursuit (model work).** Who works on which idea is studied in agent-based models. Kitcher's division of labor: credit seekers spread across problems better than pure truth seekers, who herd (Zollman 2018 argues credit is not needed) (b18). Weisberg and Muldoon (2009): mixed followers and mavericks beat either alone; this was criticised (Alexander, Himmelreich, Thompson 2015; Thoma 2015; Poyhonen 2017; Fernandez Pinto 2018) and partly restored in modified models (b17, b21, b22). Zollman effect (2007, 2010, after Bala and Goyal 1998): more communication can lower group accuracy, because misleading early evidence spreads and the group stops exploring (b16). Borg et al. (2017): in an argumentative model sharing does not hurt; heterogeneous no-sharing groups beat homogeneous ones (b19). No real-lab or LLM data confirm any of these (K13). Sibling subfield "Social epistemology" covers this; here only the pursuit link matters.

**Summary of the philosophy.** It gives a shape: a cheap "worth developing" tier and an expensive "accept" tier (K12); a reachability test (could the idea be derived from known premises?); strategies that are sufficient, not necessary; a warning that heuristics are biased. It gives no calibration.

## 3. Core findings with exact numbers

Status: E established (2+ independent sources or replicated), S single-source, C contested. "Per review" and "per idea" are different levels of analysis.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Before running, blind experts rate LLM ideas more novel than expert ideas | Novelty 1-10 per review: human 4.84 (n=119), AI 5.64 (n=109), AI+rerank 5.81 (n=109). Per idea N=49: 4.86 / 5.62 / 5.78. 49 idea writers, 79 reviewers, 298 reviews, 7 topics. Feasibility per idea 6.53 / 6.30 / 6.41 (n.s.); excitement 4.56 / 5.18 (p=0.08) / 5.45 (p<0.01) | Si 2024 (a11, b01, b02, c01) | S |
| Experts barely agree on idea quality | Human split-half 56.1% balanced (50% chance); ICLR'24 reviews 71.9%; NeurIPS'21 66.0% balanced | Si 2024 (a12, b03) | S |
| LLM judges are near chance on ideas | Claude-3.5 pairwise 53.3%, Claude-3.5 direct 51.7%, GPT-4o direct 50.0%, GPT-4o pairwise 45.0%, AI Scientist reviewer 43.3% | Si 2024 (b03) | S |
| Rankers do better on finished papers, not on ideas | Claude-3.5 zero-shot 71.4%, GPT-4o 61.1%, Claude-3-Opus 63.5% on ICLR accepted-vs-rejected pairs (not on the expert ideas) | Si 2024 (a13, c03) | S |
| Executing ideas reverses the AI novelty advantage | N=43 projects (19 human, 24 AI), 58 reviewers. Score change: AI -1.049 novelty, -1.760 excitement, -1.879 effectiveness, -1.976 overall; human -0.010, +0.078, -0.052, -0.628. Difference p=0.025, 0.001, 0.003, 0.004 (FDR). Post-run AI excitement 3.90 vs human 4.48; effectiveness 4.13 vs 4.78 (flip not significant per idea). Execution overall 3.406 vs 3.968 (p=0.175) | Si 2025 (a14, b05, c04) | S |
| Gap not caused by executors editing ideas | Controlling for edits gave AI gaps -1.107, -1.843, -1.921, -2.009; still significant | Si 2025 App. F (c05) | S |
| Pre-run scores do not predict post-run scores | Pearson r, AI ideas: novelty -0.019, excitement -0.321, effectiveness 0.172, overall -0.092. Human: -0.084, 0.205, 0.022, 0.158. About 20 ideas per arm, no CIs | Si 2025 App. D (d01, a15) | S |
| After execution, overall score follows novelty and excitement | Overall vs novelty 0.616, excitement 0.771, soundness 0.635, effectiveness 0.654. Change in overall vs change in novelty 0.809, excitement 0.856, effectiveness 0.642 | Si 2025 (d02) | S |
| Overgeneration hits a diversity ceiling | 4000 seed ideas per topic, about 5% (about 200) non-duplicates at cosine 0.8 | Si 2024 (a13, b04, c02) | S |
| Off-the-shelf models are near chance at predicting which of two ideas works | GPT-4.1 zero-shot 51.9% on 1,585 test pairs; experts' majority of five 48.9% (25 experts, 45 pairs, 222 annotations) | Wen 2025 (b07, b08, c13) | E (with d03) |
| Outcome-trained predictors beat chance but drop out of distribution | Fine-tuned GPT-4.1 + full-paper retrieval 77% in-distribution (6,000 training pairs); 64.4% vs experts 48.9% on NLP subset; 63.6% on fresh unpublished ideas. Full-paper retrieval 38.8 to 53.0%. Fine-tuned GPT-3.5 only 45.0 to 53.7%. CoT gave no gain | Wen 2025 (b07, b09, b25, c13) | E |
| 2026 larger pair set | 11,488 pairs, 724 benchmarks, consistency-aware accuracy: GPT-5 zero-shot 57.65% (none), 59.61% (low), 61.10% (medium); off-the-shelf 8B about 30%; SFT 8B 77.10%; RLVR 71.35%; on Wen's set 67.49% vs 51.4%; cross-domain GPT-5 42.84-45.96%, best trained 45-49% | Mule 2026 (d03, d04, d05) | E (with Wen) |
| CoT can hurt on idea-outcome forecasting | Llama 3.1 8B 30.02% to 27.38% with CoT instruction; Qwen3 thinking about +5 | Mule 2026 (d05) | S |
| UCB-style pursuit with a computed score works on classification | HypoGeniC gain over few-shot: +31.7% shoe sales, +13.9% deceptive reviews, +3.3% headlines, +24.9% tweets; beats fine-tuning by 12.1% and 11.6% on two real sets; bank updating +0.7 / 5.8 / 8.1 / 7.0% | Zhou 2024 (a16, c06) | S |
| Adaptive allocation beats uniform when the score is informative | Up to +11.10 pts MATH-500, +10.82 AIME25, +11.23 LiveCodeBench at equal budget; avg budget 8: +7.41 (3.11x) and +9.97 (4.00x); Gemini-2.5-Flash-Lite +3.4 | Zuo and Zhu 2025 (d06, d07) | S (not on ideas) |
| Random or diversity-selected subset refinement beats refine-all | Strong non-duplicate yield MMR-k 23.70, random-k 22.18; MMR minus refine-all +1.90 CI [0.20, 3.60]; cost per strong idea 4492 vs 4859 tokens; raw generate+rerank gave 0 | Zhang 2026 (d08, d09) | S (proxy-judged) |
| Elo tournaments are the deployed pursuit selector | Co-scientist Elo rises with compute over 203 goals; 15-goal expert comparison rank 2.36, novelty 3.64, impact 3.09 of 5 (11 goals). Judge is model-made | Gottweis 2025 (a21, a24) | C |
| Tree search by scalar score gave one workshop paper | 3 papers, one scored 6.33 (6, 6, 7), top 45%; negative result; withdrawn | Yamada 2025 (b12, c12, d15) | S |
| Keyword novelty gates over-accept | All 10 generated + 2 seed ideas "novel"; 5 of 12 experiments (42%) failed; 4 of 7 manuscripts (57%) wrong numbers; median 5 citations, 5 of 34 from 2020+ | Beel 2025 (b10, c10) | E (with d10) |
| Novelty checkers that read reranked papers work much better | Accuracy 0.81, F1 0.79, kappa 0.59 (n=32); zero-shot 0.68; AI Scientist prompt 0.47, kappa 0.05; not-novel recall 89.66% full system vs 13.79% / 10.34% / 8.62% / 5.17% (RankGPT / embedding / snippet / keyword) | Shahid 2025 (d10, d11) | S (tiny n) |
| LLM novelty judging without search is near random | AUROC about 0.5 without search; with search 0.813 NeurIPS, 0.616 Nature Medicine, 0.597 mixed; RND 0.820 / 0.765 / 0.795 on a recency-and-citation proxy | RND 2025 (d12, d13) | S (proxy labels) |
| Screening funnels retrieve the right premises | MOOSE-Chem hit ratio at top 4%: 76.8% (150 papers), 83.7% (300), 88.9% (1000), 86.9% (3000); top 0.8%: 60.8-70.6%; top 0.016%: 46.7% / 52.0%; window 15 keep 3: 83.7% at 4%. (71.6% is the top-20% figure at window 60, not a 5% setting.) | Yang 2025 (a17, a18, c14) | E (with c16) |
| Retrieve-compare-revise raises novelty | Round 1 raised novelty for 54.4% / 55.6% / 47.8% / 46.7% of ideas by variant; round 2 57.8% | SciMON 2023 (c16) | S |
| Self-critique does not help; real feedback does | DiscoveryBench best about 25%, biology 0%, engineering 7%; Reflexion with oracle helps; POPPER: Self-Refine Type-I error 0.248, ReAct 0.145 at alpha 0.1; POPPER power 0.610 / 0.897 | Majumder 2024; Huang 2025 (a22, a25, c08, c09, c15) | E |
| Held-out fit with prior plus code-fitted constants | LLM-SR OOD NMSE about 0.0037 vs baselines above 1; no prior: 0.181 OOD | Shojaee 2024 (a23, c17) | S |
| LLM paper reviewers match humans only on finished papers | 65% vs 66% balanced accuracy; 70% vs 73% raw; F1 0.57 vs 0.49; AUC 0.65 both. GPT-4o with 5 reflections, 5 ensembled, 1-shot. Cheaper models reviewed substantially worse | Lu 2024 (a19, b11, c11) | E |
| Idea quality weakly tied to general reasoning scores | r=0.357 (CI 0.022-0.621) over 41 models; idea length vs quality r=0.089; LLM panel only | LiveIdeaBench (d14) | S |
| Isolation worst in LLM debate networks | GPT-3.5, 100 MATH questions, 3 runs: connected 67.7%, disconnected 63.9%, random 68.2%, scale-free 64.8% | Regan 2024 (d16) | S |
| Early outcome prediction cuts evaluation cost (not ideas) | 13-26% fewer steps; SWE-bench -26.0% steps for 1.1 pt resolve-rate shift at threshold 0.95; up to -44.1% input tokens | EarlyEval 2026 (d18) | S |
| Law-guided scaffold beats direct prompting (confounded) | 3 explananda, 5 proposals vs 1; max and mean significant; median p=0.0859 for LLM judges | DN-Hypo 2026 (d17) | S |

## 4. Mechanisms and models

Each mechanism is written so it can be coded.

**4.1 Two-tier gate (Schaffner).**
- Tier 1 (weak): cheap. Input: idea text. Checks, done by code or a retrieval step: (a) known-solution check by reading retrieved papers, not keywords (K09, K20); (b) reachability: list the premises the idea cites, verify each exists in the problem statement or a retrieved source (Nickles, a01); (c) a probe: a small run on a held-out case, capped at a fixed fraction of the idea's budget.
- Tier 2 (strong): full check with held-out input, mutated input, or an independent verifier (G3, S8).
- Rule: an idea reaches tier 2 only if tier 1 produced a measured pass. Model opinion is never the gate (G8).
- No direct evidence the two tiers save budget (K12, K23). EarlyEval is the nearest analogue (d18).

**4.2 Pursuit as budget allocation (Laudan).**
- State: for each of K candidates, a list of measured scores (probe results) and tokens spent.
- Policies in the literature: uniform; random-k then refine; MMR-k (pick k candidates by relevance minus similarity to those already picked); successive halving (give each n tokens, drop the bottom half, double the rest); UCB (mean score plus an exploration bonus); Elo tournament (pairwise judge). HypoGeniC uses a UCB-style reward with a hypothesis bank and a bank of wrong examples (a16). Zuo and Zhu use elimination with an oracle score (d06).
- The score must come from code. If it is a model judge, the policy allocates budget by a near-chance signal (b03). Zhang 2026 (random-k strong, MMR best) fits this: when the signal is weak, spread and diversity beat chasing the score (d08).

**4.3 Diversity before selection.**
- Sampling more ideas from one model saturates (K05). Dedup by embedding (cosine 0.8 in Si 2024) in code, count distinct directions, and generate new ideas only with a changed prompt, schema or source (O6, O7), not more of the same prompt.

**4.4 Schema instantiation (Darden).**
- Keep a small library of abstract templates for the problem class, for example "A + B gives C", "invariant under X", "reduce to special case". Generation fills the template slots; code checks that every slot is filled with an object that exists in the input. Revision targets the slot that the failing output points to (G2).
- No controlled LLM test exists (K21). The one scaffolded study (d17) confounds scaffold with 5-vs-1 sampling.

**4.5 Surprise-triggered search (Hanson).**
- Open idea search only when a check fails or attempts disagree (G1). Not tested against a timer (K17).

**4.6 Outcome-trained predictor.**
- Log features of each idea (length, number of premises cited, operator used, probe score) and the executed outcome. After N >= 100, fit a logistic model. Wen and Mule show outcome prediction needs thousands of labelled pairs and degrades out of distribution (d04). Treat it as a long-run memory item, not a day-one gate.

**4.7 Sequential falsification.**
- POPPER pattern: turn a hypothesis into several measurable implications, test each, combine evidence with e-values, stop when the product crosses 1/alpha. It controls Type-I error where agent self-checks inflate it (c15).

## 5. What holds up

**Replicated or multi-source.**
- Models and humans are poor at ranking ideas before outcomes. Si 2024 (human 56.1%, best LLM 53.3%), Wen 2025 (GPT-4.1 51.9%, experts 48.9%) and Mule 2026 (GPT-5 57.7-61.1% consistency-aware) agree. Tasks and metrics differ, so this is a pattern, not a numeric replication.
- Outcome-trained predictors beat chance: Wen 77% and Mule 77.1%, both trained on published pairs. Both fall out of distribution (63.6%; 45-49% cross-domain).
- Keyword novelty gates fail: Beel (all 10 ideas novel) and Shahid (AI Scientist prompt 0.47, kappa 0.05) agree.
- Self-critique without outside signal gives no gain: DiscoveryBench and POPPER agree. See also guardrail G2.

**Single-source and fragile.**
- The ideation-execution gap. N=43, one field, one generator, 2025 models. The post-run flip is not significant per idea (a14). The accepted ICLR 2026 version is the only record; no replication outside NLP found (d19).
- Zero correlation between ideation and execution scores. Each r rests on about 20 ideas, no CIs (d01).
- Diversity ceiling of about 5% (one generator, one embedding model, threshold chosen by hand).
- HypoGeniC UCB gains: classification sets where a score exists.

**Failures and weak evidence.**
- Zollman-type harm from sharing did not appear in LLM networks; isolation was worst (d16). Early-only isolation untested.
- Chain-of-thought did not help the forecaster (b25, d05).
- Elo rise with compute (co-scientist) may reflect judge preference (a24).
- The DN-Hypo scaffold win is best-of-5 vs 1 (d17).
- No test of the Nickles, Schaffner, Darden or Laudan frameworks themselves (b14, K12).

**Moderators.**
- Finished paper versus early idea: judges do ok on papers (65-71%) and fail on ideas (43-53%).
- In-distribution versus new domain or new time (d04, b09).
- Search access: reasoning-model novelty judgment about 0.5 AUROC without search, 0.6-0.8 with search, domain-dependent (d13).
- Judge model size: cheaper reviewers were substantially worse (c11).
- Verifiable versus open-ended: bandit allocation gains need a scoring oracle (d06).

**Interventions that worked.** Full-paper retrieval (38.8 to 53.0%, c13); reranked retrieval for novelty (89.66% vs 5-14%, d11); UCB with held-out score (K06); screening funnel with small window (K10); sequential falsification (c15); random-k or MMR-k subset refinement (proxy only, d08).

**Interventions that did not.** Few-shot and CoT for LLM rankers (c03); CoT sampling for the forecaster (b25); ReAct and self-critic planning in DiscoveryBench (c09); model self-scores that feed no step (K14); more sampling from one model (K05).

## 6. Language models

**Behaviour on idea appraisal.** Zero-shot, current models rate their own ideas well and cannot tell good from bad. Before execution, AI ideas beat human ideas on novelty (+0.80 on a 10-point scale per review, a11). After 100+ hours of execution the AI-idea scores fell about 1.0 to 2.0 points while human ones stayed flat (c04). Ideation-to-execution correlation is about zero for AI ideas (d01). Treat a model's novelty or promise rating as inflated.

**Zero-shot forecasting of idea outcomes.** GPT-4.1 51.9%, o1 and o3 near chance (b07, c13). Mule 2026: GPT-5 57.65 / 59.61 / 61.10% at none/low/medium reasoning, consistency-aware (a pair counts only if right under both orderings, d05). More thinking helps GPT-5 a few points with diminishing returns. A CoT instruction lowered Llama 3.1 8B from 30.02% to 27.38%.

**What raises accuracy, by how much.**
- Outcome fine-tuning on 6,000 pairs: to 77% in-distribution (Wen); on 11,488-pair benchmark data 77.10% for SFT 8B vs GPT-5 61.10% (Mule).
- Full-paper retrieval: 38.8 to 53.0%.
- Out of distribution: 63.6% on fresh ideas; cross-domain 45-49%.
- Reward hacking was seen in RL (the model stopped writing reasoning, d05).

**Novelty checks.** Keyword and snippet retrieval recover 5.17-8.62% of not-novel cases; a reranked, facet-based system 89.66% (o3-mini judge, 58 ideas, d11). Expert-labelled test n=32: 0.81 accuracy, gpt-4o, 2024 (d10). The AI Scientist's own novelty prompt: 0.47 accuracy, kappa 0.05. No 2026 reasoning-model test found.

**Idea generation.** Overgeneration plateaus (5% unique of 4000). LiveIdeaBench: idea score vs reasoning score r=0.357, CI 0.022-0.621; a 32B model ranked 8 of 41 (d14). All scoring there is by a model panel.

**Agent systems.** AI Scientist under $15 per paper, review $0.25-0.50 (c11). Independent test: 5 of 12 experiments failed (b10). AI Scientist-v2: tree search, 1 of 3 papers accepted at workshop level (b12). Co-scientist: Elo rises across 203 goals with compute (a24). AI-Researcher: 93.8% implementation completeness, self-reported, measures running code not correctness (c19). Chain of Ideas: +56 Elo over the next best in human evaluation, authors' own arena (b13).

**Allocation.** Gains from adaptive allocation shrink with strong models: +11 points with 8B-class models, +3.4 with Gemini-2.5-Flash-Lite (d06, d07).

**Open for 2026 models.** No test of 2025-2026 reasoning models on the ideation-execution gap; none on Darden-style schema generation; none on two-tier gating.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Never let the generating model pick the final idea; select by a measured score in code.** G8 / G5. [E]. Evidence b03, c03, b07, d03, d01 (K03).
2. **Novelty or known-solution check must read retrieved text, not keyword hits.** S0 gate. [E]. Evidence b10, c10, d10, d11, d13 (K09). Report false-novel rate; require reranked retrieved passages in the prompt.
3. **Revise from real output; self-critique alone is not used.** G2. [E]. Evidence a22, a25, c09, c15 (K08). Already in the schema; this confirms it.
4. **Cheap staged screening for premise retrieval (funnel with small windows).** S0. [E]. Evidence a17, a18, c14, c16 (K10). Use for choosing which retrieved facts or sources to read.
5. **Do not use an LLM judge tuned on finished work to rank early ideas.** G8. [E]. Evidence a19, b11, c11, b03 (K15). Judge reliability is task-specific.
6. **Drop any self-score that no transition reads.** G7. [S] (one reading of Beel), but removal is costless. Evidence b24, c23 (K14). Hygiene, not a performance claim.

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Probe-based pursuit: run a cheap held-out probe per idea, allocate by probe score (successive halving or UCB) vs uniform | S0 / pursuit | [S] | K06, K19, d06, d08, a16 |
| Two-tier weak/strong gate vs single full check | S0 / S3 | [S] | K12, K23, d15, d18 |
| Diversity before selection: embedding dedup and schema-seeded generation vs more samples | G4 / S3 | [S] | K05, b04 |
| Schema-instantiation templates in generation (Darden) | S3 with O1-O8 | [S] | K21, d17 |
| Reachability / generative-justification check (Nickles): every cited premise must exist | S0 | [S] | a01, K12 |
| Surprise-triggered idea search vs timer | G1 | [S] | K17 (a06) |
| Logistic outcome predictor over own logged runs | memory | [E] that predictors work with thousands of pairs; [S] at our scale | K04, d03, d04 |
| Isolated early answers then merge, vs shared early answers | G4 | [C] | K13, d16 |
| Sequential falsification wrapper | G3 / S8 | [S] | c15 |
| Random-k cheap refinement baseline | S0 | [S] | d08, d09 |

## 8. Concrete tests on our bench

All arms at equal total tokens, setup included (G7). Use items with a checkable answer (K16).

1. **Probe vs opinion selection.** Items: 50 problems where the agent produces 8 candidate ideas or routes each. Arms: (A) model picks best by its own score; (B) random pick; (C) cheap probe on a held-out case, pick best; (D) successive halving by probe. Metric: executed pass rate of the chosen idea; Spearman of pre-run score vs final outcome. Expected: A about equals B (correlation near zero, d01); C and D beat A. Size unknown.
2. **Allocation rule.** 20 candidates per item, 30 items. Arms: uniform; random-k; MMR-k; successive halving; UCB, all scored by an executed check. Metric: solved items per 100k tokens, cost per strong idea. Expected: halving and UCB beat uniform when the probe is informative; random-k close behind when it is weak (d08).
3. **Two-tier gate.** Same ideas with and without a stage-1 probe, equal total tokens. Metric: tokens wasted on ideas that later fail, plus final accuracy. Expected: saves budget at under 1-2 points accuracy loss (EarlyEval analogue: 26% fewer steps for 1.1 points).
4. **Novelty gate.** 30 hand-labelled known-vs-novel items. Arms: keyword hit; model opinion; read reranked retrieved text. Metric: false-novel rate and accuracy. Expected: keyword and opinion false-novel rate high; retrieval arm near 0.8 accuracy (d10).
5. **Overgeneration vs structured diversity.** 20 samples with the same prompt vs 20 with seeded templates or operators, deduped by embedding at cosine 0.8. Metric: distinct directions; pass@k. Expected: plain sampling gives few distinct directions (about 5% in Si); structured arm gives more.
6. **Schema instantiation.** Template-filled generation vs best-of-N plain generation at equal tokens, scored by executed probes. Metric: pass rate. Expected: unknown (K21: no test exists). Success needs the template arm to beat best-of-N, not best-of-1.
7. **Surprise trigger.** Idea search on check failure or attempt disagreement vs a fixed timer. Metric: tokens to correct answer. Expected: trigger saves tokens.
8. **Isolation.** K branches with isolated vs shared early answers; metric distinct final answers and accuracy. Expected: Regan-type result, isolation not better.
9. **Self-score ablation.** Remove every score that drives no branch. Metric: accuracy. Expected: no change.
10. **Logged predictor.** After 100+ runs, fit logistic regression on idea features. Metric: held-out AUC. Expected: modest; do not gate on it before AUC exceeds 0.65 on held-out items.

## 9. What does not transfer, and why

- **Expert idea judging in NLP is peer review of research ideas.** Our items have a checkable answer. Si's execution costs 100+ hours; our probe costs seconds. The ideation-execution gap may be smaller or larger on bench items. Treat the direction as transferable, the size not.
- **Outcome-trained predictors (Wen, Mule)** learn which published AI-research ideas won. They need thousands of pairs from one domain and fail cross-domain (45-49%). Our bench cannot supply that at start.
- **Co-scientist and AI Scientist-v2 evidence** is system-level with 3 papers or a model-made Elo judge. It shows deployment, not benefit of the tournament.
- **MOOSE-Chem retrieval** measures recovery of known inspiration papers from a chemistry corpus with possible training leakage (a17). Our items have no corpus.
- **Philosophical reconstructions** (Kepler, Krebs, protein synthesis) are rational reconstructions of successes. Case selection bias (b15), and no failures counted.
- **Social epistemology models** assume agents with beliefs and a network; LLM samples from one model are not independent agents (G4).
- **POPPER and DiscoveryBench** use data-driven hypotheses about real datasets; our tasks do not.
- **HypoGeniC gains** are on classification where a held-out accuracy exists; ideas without a score do not get this loop.
- **LiveIdeaBench and Chain of Ideas** are scored by LLM panels or arenas, which share the bias in b03.
- **Hanson abduction** justifies searching a class; it is not a ranking rule (Harman).

## 10. Open questions

1. Does a cheap executed probe predict final outcome better than a model's pre-run score, at equal tokens, for LLM-generated ideas? No paper tests a probe-based pursuit rule head to head.
2. Does the ideation-execution gap replicate outside NLP, with 2026 reasoning models, with larger N? Only the original was found (d19).
3. Do frontier 2026 models beat chance on idea-pair forecasting with retrieval and outcome priors? GPT-5 gets 57.7-61.1% without them (d03).
4. Is there any controlled LLM test of Darden-style schema instantiation or Nickles-style generative justification at equal tokens? Not found.
5. Which allocation rule (UCB, successive halving, Elo) best splits a token budget over noisy-scored ideas? Only proxy evidence (d08).
6. Does early isolation help in LLM ensembles (Zollman-style)? Regan tested sharing from round 1 only.
7. How accurate are 2026 reasoning-model novelty checks that read retrieved text, on a larger expert-labelled set than n=32?
8. Does a two-tier gate save budget in any agent system? AI Scientist-v2 has stages with no ablation.
9. Do LiveIdeaBench findings hold when ideas are executed?
10. Do Nickles, Schaffner, Darden and Laudan say what the SEP summaries say? Primary texts were not read; details in section 2 could change.

## 11. Sources

[V] opened and read this session (including critique re-checks); [M] snippet only or not opened.

- [V] Si, Yang, Hashimoto (2024) Can LLMs Generate Novel Research Ideas? https://arxiv.org/abs/2409.04109 (a11-a13, b01-b04, b26, c01-c03, c25, c26)
- [V] Si, Hashimoto, Yang (2025) The Ideation-Execution Gap. https://arxiv.org/abs/2506.20803 (a14, a15, b05, b06, b23, c04, c05, d01, d02, d20)
- [M] Si et al. (2026) ICLR 2026 poster record. https://www.iclr.cc/virtual/2026/poster/10010564 (d19)
- [V] Wen, Si, Yueh-Han, He, Feng (2025) Predicting Empirical AI Research Outcomes with Language Models. https://arxiv.org/abs/2506.00794 (b07-b09, b25, c13)
- [V] Mule, Garikaparthi, Patwardhan (2026) Teaching Language Models to Forecast Research Success. https://arxiv.org/abs/2605.21491 (d03-d05)
- [V] Zhou, Liu, Srivastava, Mei, Tan (2024) HypoGeniC. https://arxiv.org/abs/2404.04326 (a16, c06, c07)
- [M] Zhou et al. (2024) LLMs are zero-shot hypothesis proposers. https://arxiv.org/abs/2311.05965 (c20)
- [V] Yang et al. (2025) MOOSE-Chem. https://arxiv.org/abs/2410.07076 (a17, a18, c14)
- [V] Lu et al. (2024) The AI Scientist. https://arxiv.org/abs/2408.06292 (a19, a20, b11, b24, c11, c23)
- [V] Beel, Kan, Baumgart (2025) Evaluating Sakana's AI Scientist. https://arxiv.org/abs/2502.14297 (b10, c10)
- [V] Yamada et al. (2025) The AI Scientist-v2. https://arxiv.org/abs/2504.08066 (b12, c12, d15)
- [V] Gottweis et al. (2025) Towards an AI co-scientist. https://arxiv.org/abs/2502.18864 (a21, a24)
- [V] Majumder et al. (2024) DiscoveryBench. https://arxiv.org/abs/2407.01725 (a22, a25, c08, c09)
- [V] Shojaee et al. (2024/2025) LLM-SR. https://arxiv.org/abs/2404.18400 (a23, c17)
- [V] Li et al. (2024) Chain of Ideas. https://arxiv.org/abs/2410.13185 (b13)
- [V] Wang et al. (2023) SciMON. https://arxiv.org/abs/2305.14259 (c16)
- [V] Huang, Leskovec et al. (2025) POPPER. https://arxiv.org/abs/2502.09858 (c15; table cells unverified)
- [V] Ruan et al. LiveIdeaBench. https://arxiv.org/abs/2412.17596 (c18, d14; abstract and grep level for c18)
- [V] Tang, Zhang et al. (2025) AI-Researcher. https://arxiv.org/abs/2505.18705 (c19; grep level)
- [V] Zuo, Zhu (2025) Strategic Scaling of Test-Time Compute: A Bandit Learning Approach. https://arxiv.org/abs/2506.12721 (d06, d07)
- [V] Zhang (2026) Budgeted Subset Refinement for Execution-Aware LLM Research Ideation. https://arxiv.org/abs/2607.14118 (d08, d09)
- [V] Shahid et al. (2025) Literature-Grounded Novelty Assessment of Scientific Ideas. https://arxiv.org/abs/2506.22026 (d10, d11)
- [V] Relative Neighbor Density (2025) Enabling AI Scientists to Recognize Innovation. https://arxiv.org/abs/2503.01508 (d12, d13)
- [V] Regan, Gournail, Oka (2024) Problem-Solving in Language Model Networks. https://arxiv.org/abs/2406.12374 (d16)
- [V] Lin et al. (2026) DN-Hypo-Pipeline. https://arxiv.org/abs/2606.08532 (d17)
- [V] Shi et al. (2026) EarlyEval. https://arxiv.org/abs/2609.02783 (d18)
- [V] Stanford Encyclopedia of Philosophy, Scientific Discovery (Schickore). https://plato.stanford.edu/entries/scientific-discovery/ (a01-a04, a06-a09, b14, b15)
- [V] SEP, Scientific Method. https://plato.stanford.edu/entries/scientific-method/ (a10)
- [V] SEP, Social Epistemology. https://plato.stanford.edu/entries/epistemology-social/ (b16-b18)
- [V] Borg, Frey, Seselja, Strasser (2017) An argumentative agent-based model of scientific inquiry. https://arxiv.org/html/1612.04432 (b19)
- [M] Laudan (1980/1981) Why was the logic of discovery abandoned? https://www.humanindex.unam.mx/humanindex/fichas_pdf/Capitulo6848%20Laudan%20Why%20Was%20the%20Logic%20of%20Disc.pdf (a05)
- [M] Seselja and Strasser (2014) Epistemic justification in the context of pursuit. https://core.ac.uk/download/55722691.pdf (b20)
- [M] Alexander, Himmelreich, Thompson (2015) Epistemic landscapes, optimal search, and the division of cognitive labor. https://philarchive.org/archive/ALEELO (b21)
- [M] Weisberg and Muldoon (2009) Epistemic landscapes and the division of cognitive labor. https://repository.upenn.edu/philosophy_papers/7 (b22)
- [M] Langley, Simon, Bradshaw, Zytkow (1987) Scientific Discovery. https://mitpress.mit.edu/9780262620529/scientific-discovery/ (c21)
- [M] Darden (2006) Reasoning in Biological Discoveries; Schaffner (1993) Discovery and Explanation in Biology and Medicine. https://www.cambridge.org/core/books/reasoning-in-biological-discoveries/ (c22)
