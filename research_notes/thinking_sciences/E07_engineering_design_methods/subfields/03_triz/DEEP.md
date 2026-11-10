# TRIZ: deep document

*Subfield E07.03. Contradiction matrix, 40 principles, ideal final result. Built from evidence_a-d.jsonl (ids a01-a29, b01-b26, c01-c26, d01-d19), claims.jsonl (E07.03-K01 to K29) and critique.md in this folder. Status marks: [E] established, [S] single-source, [C] contested. [V] = page or PDF text opened, [M] = snippet, abstract or metadata only.*

**Bottom line.** TRIZ is a patent-derived catalogue of reframes. It is not a tested theory of thought. Human evidence is student studies from 2006 to 2024, mostly small, with the quantity gain not reproduced. LLM evidence (2024 to 2026) is case studies and benchmarks. No study compares a TRIZ-structured prompt with a plain prompt at equal tokens with blind ratings (K16). The one robust LLM result: models see *that* a trade-off exists, but cannot name the right pair. A code-held lookup table with the model only selecting beats free prompting.

---

## 1. What it is

TRIZ (Russian acronym, "theory of inventive problem solving") is a set of tools for technical invention. Three parts matter to us.

1. **Technical contradiction.** You improve one parameter and another gets worse (stronger but heavier). TRIZ says the best inventions remove the trade-off instead of compromising.
2. **Contradiction matrix and 40 inventive principles.** A table, usually described as 39 parameters by 39 parameters. Each cell lists the few principles (of 40) that past patents used for that trade-off. Examples: Segmentation (#1), Anti-weight (#8), Dynamics (#15), Composite materials (#40). In practice: name the improving parameter and the worsening parameter, look up the cell, read 3 to 4 principles, turn each into a concrete idea. The matrix size and the claim that the cells were derived by mining patents come from the standard literature. No opened source in our set confirms the counts (K01).
3. **Ideal final result (IFR).** State the ultimate solution: the desired function happens by itself, with no added system, cost or harm (a02 [V], Wikipedia only; no formula, no evidence).

Also in the family: physical contradictions (one property must be both X and not-X), ARIZ (a step-by-step algorithm), functional analysis, and five "levels of inventiveness". The first two parts above are what O4 and O8 would use.

Why it is in our study: the schema has operators that are typed reframes. O4 drops a constraint. O8 reframes the goal. TRIZ is the only large catalogue that tells you *which* reframe to try for *which* kind of stuck. The evidence that it works is weak and mostly human.

## 2. History and theories in depth

**Origins (a01, a03 [V], Wikipedia).** Genrich Altshuller (born 1926) was a patent-office clerk. TRIZ work began in 1946 in a Soviet Navy inventions office. He was arrested in 1950 and freed after Stalin's death (jailed 1950 to 1954 per a03). First paper 1956, "Psychology of inventive creativity", co-written with Shapiro. He founded an institute for inventive creativity in 1971 and died in 1998. The method came from screening patents to see which contradiction each invention resolved and how.

**The two insights (a04 [V], Trapp and Warschat 2024).** From manual patent analysis: (1) resolving a contradiction between system parameters often gives a highly innovative solution; (2) many high-grade innovations move an existing solution from another domain. The second point is the same idea as distant analogy (schema O7).

**What we could not verify (K01 [E]).** Patent counts, the five levels of inventiveness with their percentages, and how the matrix was derived. Wikipedia gives none of them. Treat the origin story as folklore with an anchor, not a measured base. The method was built by describing past successes. Nobody measured how many unsuccessful inventions also used the same principles. That is a selection problem the TRIZ literature does not address.

**Theory claims.** TRIZ rests on three assumptions: inventive problems share a small set of recurring patterns; the patterns are domain independent; a user pointed at the right pattern gets better ideas. Only the third can be tested, and only the human studies below test it.

**Critique in the literature.**
- Hard to use: students find the matrix tedious and confusing, with many tables, number lookups and too few examples. Teams drift from the principles without supervision (a27 [V]).
- Weak problem formulation. Mohammadi and Zeng (2025) note TRIZ is criticised for this (b26, abstract) and add an LLM question-asking step before the matrix.
- Gero, Jiang and Williams (2012) show the main cognitive effect may be the problem focus the method forces, not the principles (a23). See section 4.8.
- A general trade: stimulus-based methods give "more novel, fewer ideas" (a26, a22). Not special to TRIZ.

**TRIZ and creativity training.** Schema section 4b already lists "creativity training methods as prompts" as not to add, since the effect shrinks to d = 0.29 to 0.32 after publication-bias correction (F01). Nothing here overturns that. TRIZ is a typed form of such training, so it carries the same prior.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| TRIZ-taught first-year teams produced about twice as many feasible concepts (unrandomised, instructor present) | 8.94 vs 4.42 feasible concepts per team; 35 vs 16.3 unique solutions per section; 21 unique concepts only from TRIZ teams vs 8 only from non-TRIZ; 16 TRIZ teams (64 students) vs 24 teams (96 students) from 3 random non-TRIZ sections; fume-hood problem | Ogot and Okudan 2006 (a21, a27) [V] | [S] K02 |
| Controlled multi-site replication: quantity gain not reproduced; novelty up at 2 of 3 sites | Quantity p = 0.2879, 0.5409, 0.6291 (all n.s.). Novelty p = 0.0004, 0.0145, 0.5786. UTEP 21 control vs 9 TRIZ; UMD 20 vs 21. LED traffic-light task. No effect sizes; authors call some results a trend | Vargas-Hernandez, Schmidt, Okudan 2012 (a22, d08) [V]; 2013 J Mech Des (b01, d09) [M] | [S] K03 (same experiment family, one lab group) |
| TRIZ sessions shift effort from solutions to problem aspects | Problem-solution index 0.526 (SD 0.206) TRIZ vs 0.192 (SD 0.049) brainstorming; t = -4.892, p = 0.001. Second index 0.144 vs 0.230, p = 0.009. Gap not significant in second half. 22 seniors, 11 teams | Gero, Jiang, Williams 2012 (a23) [V] | [S] K04 |
| Matrix and principle methods beat no-method control; edge over SCAMPER small | Problem 1 means novelty/variety/quality (0 to 4): control 0.7/1.1/1.6; KJ 0.9/2.2/3.1; SCAMPER 1.8/2.5/3.3; MaTriz 2.3/3.1/3.5. Overall SCAMPER 89%, KJ 73%, control 54% of MaTriz score. 144 students, 72 pairs, 3 Chilean universities | Duran-Novoa and Torres-Benoni 2024 (a24, a25) [V] | [S] K05 |
| Relational reasoning moderates the novelty gain | Larger gain with higher relational-reasoning score; no N or coefficient obtained | Dumas and Schmidt 2015 (b21, d10) [M] | [S] K26 |
| Less abstract principle wording gives more ideas | 3 groups, 3 problems, 10 minutes; no counts obtained | Livotov et al. 2019 (b22, d11) [M] | [S] K27 |
| Patent-analogy stimuli raise novelty and cut idea count | 153 seniors, 95% mechanical | cited in a26, a29 [M] | [S] K23 |
| LLMs detect that a contradiction exists but not the right pair | Case detection F1 0.75 to 0.90; pair F1 0.29 to 0.45; patent pair Hit@3 0.13 to 0.28; best LoRA LLaMA3.1-8B detection 0.90; Gemini-2.5-Pro pair F1 0.36 zero-shot, 0.42 few-shot (text says 0.42 to 0.45; table garbled) | TRIZBench 2026 (a17, b11, c02, d04) [V] | [E] K06 |
| GPT-4 over-fires on contradiction finding | 100 patents with annotated contradictions: recall 0.71, precision 0.46, F1 0.56 (3.81 annotated, 2.69 found, 3.19 false positives per patent). 100 patents annotated with none: 86 flagged, 4.84 sentences per patent, 87 contradictions | Trapp and Warschat 2024 (a05, a06, b08) [V] | [S] K07 (label error possible) |
| Matrix lookup plus LLM rerank beats direct prompting | Hit@3 case/patent: Matrix 0.67/0.48; TF-IDF 0.69/0.56; Qwen3-8B zero-shot 0.39/0.27, few-shot 0.51/0.25; Gemini-2.5-Pro 0.45/0.31 zero-shot, 0.52/0.35 few-shot; Qwen3-8B Matrix-Rerank 0.71/0.59 | TRIZBench Table 3 (a18, b12, c03, d01) [V] | [S] K08 |
| Gold-pair numbers overstate the pipeline | Table 3 inputs include the gold improve/worsen pair. End-to-end Qwen3-8B zero-shot-rerank 0.59/0.46; LoRA-rerank 0.65/0.52. Above direct prompting, not above TF-IDF (0.69/0.56) | d01, d03 [V] | [S] K25 |
| No random baseline reported | Chance Hit@3 of 40: 7.5% (1 gold principle), 14.6% (2), 21.4% (3), 27.7% (4). Frequency-prior baseline never run | d02 (own calculation) | [S] K24 |
| Right label does not mean right reasoning | Evidence F1 rises with principle Hit@3 (figure only, no slope); one case right pair and Hit@3 = 1 with missing evidence; another evidence F1 = 1.0 with wrong pair | TRIZBench (a19, b13, c04, d05) [V] | [S] K09 |
| Humans show the same detect-versus-pair pattern | 5 cases, 6 participants at three TRIZ background levels | TRIZBench (b14) [V] | [S] |
| Benchmark scale and label quality | 1,354 cases from 590 sources; 1,679 contradictions; 2,630 solutions; only 491 contradictions (29.2%) carry parameters; 429 patents (257 with parameters, 304 with principles); 734 cases (54.2%) with principle labels; audit of 200 cases: 74.0% agreement before adjudication | TRIZBench (a16, b10, c01) [V] | data |
| Few-shot examples narrow output | GPT-4, 34 cases, recall/precision: basic 0.675/0.259; CoT 0.691/0.310; few-shot 0.245/0.333; CoT+few-shot 0.247/0.298. At least half of literature parameters found in 85.3% (basic), 88.2% (CoT) | TRIZ-GPT (a08, b05, c06) [V] | [S] K10 |
| Solution quality unchanged by prompt style | Cosine to published solution, 84 items: 0.829 (SD 0.031) basic; 0.823 CoT; 0.824 few-shot; 0.824 both; n.s. | TRIZ-GPT (a10, b06, c07) [V] | [S] K10 |
| Bigger model helps only under some prompts | 10 post-April-2023 cases (avg 5.5 pairs): GPT-4 vs GPT-3.5 recall 0.544 vs 0.400 (basic, CoT); few-shot 0.288 vs 0.304; CoT+few-shot 0.275 vs 0.383. GPT-3.5 dropped parameter numbers in 2 of 10 | TRIZ-GPT (a09, b07) [V] | [S] K12 |
| Contradiction choice unstable across samples | 100 runs per case, 10 textbook cases from 7 textbooks; entropy up to 6.64 bits; 7 of 10 matched or half-matched in top 3; 4 cases (5 to 8) had a dominant top answer; higher-frequency answers matched better | AutoTRIZ (a11, b03, b04, c10) [V] | [S] K11 |
| AutoTRIZ application case, no baseline | Volumetric energy density 206 vs 166 Wh/L (+24%); eTMS 21.66 vs 13.18 (+64%); grouping efficiency 43% vs 34% (+26%); expert-selected ideas, no plain-LLM arm | AutoTRIZ (a12, a13, c11) [V] | [S] K17 |
| Multi-agent TRIZ is costly and partial | 8 GPT-4o agents, 150,000 to 250,000 tokens and 60 to 80 graph node calls per run; 1 of 2 case solutions found; TRIZ specialist skipped its retrieval tool; 1 case, 2 runs | TRIZ Agents (a14, b16, c12, d15) [V] | [S] K18 |
| Typed principle vs vanilla in text-to-CAD, N = 1 | Baseline 16.93 kg, 0.627 MPa, 0.288 mm. Vanilla: mass -31.8%, stress +64.1%, deflection +99.4% (0.574 mm). Segmentation: -14.7% / -0.1% / +0.7%. Anti-weight -5.9% / +21.6% / +4.4%. Dynamics -4.0% / +33.2% / +16.3%. Composite -10.0% / +40.7% / +44.4%. One chair, one run per cell, not token-matched | Lee et al. 2026 (a20, b18, c16, d06) [V] | [S] K14 |
| TRIZ operators in an agent loop: small gains, cause unproven | F1 +2.88 (PowerDuck 0.9694 to 0.9982), +4.23 (CICIoT2023 0.8326 to 0.8749), +0.15 (CIC-DDoS2019 0.7470 to 0.7485). 45-activity campaign macro-F1 0.8325 to 0.8483 (+0.0158, 1.90% relative), 43 of 45 groups improved, failed own frozen gate (needs 3.2277%). Authors: no equal-budget unguided control | TRIZ-a (b17, c17, c18, d07) [V] | [S] K15 |
| TRIZ retrieval for parameter tagging | PaTRIZ about 3,000 instances, 3 seeds: BiLSTM-CRF 60.7, BERT-CRF 68.5, RoBERTa-CRF 71.7, GPT zero-shot 73.7, GPT+prompt 76.9, TRIZ-RAGNER 84.2 F1 (P 85.6, R 82.9). Ablations: no retrieval 78.1, no rerank 79.8, no structured prompt 76.6. Preprint shows signs of pasted text, no model names | TRIZ-RAGNER (a15, b15, c15, d17) [V] | [C] K13 |
| Blind run of all 40 principles | GPT-3.5, functional-analysis accuracy about 50%; many ideas, many do not resolve the contradiction | Mohammadi and Zeng 2025 (b26, c20) | [S] K21 |
| Humans with LLM help | Lower workload, better understanding of contradictions, quality not always better on complex tasks; three problems; no N | Cok et al. 2026 (b02) [M] | [S] K22 |
| Earlier rule/BERT pipeline | PaTRIZ stage 1 F1 0.37, stage 2 F1 0.65, end-to-end pair match about 0.33 | Trapp and Warschat 2024 (a07, c14) [V] | context |
| IFR alone as an LLM prompt | No study found (arXiv phrase search: 3 hits, all 2013-2014 non-LLM; Crossref scan of about 50 titles) | c22, d19 | [E] K20 (absence) |

## 4. Mechanisms and models

These are explained so an engineer can build them. Each is a design reading of TRIZ, not a measured mechanism.

**4.1 The typed reframe pipeline (the AutoTRIZ and TRIZBench pattern).**
1. Model reads the problem and writes one improving and one worsening parameter (from a fixed list of 39).
2. Code validates that both slots are filled and that the parameter ids exist.
3. Code looks up the matrix cell and returns 0 to 4 principle ids. The model never invents ids.
4. Model (optional) reranks the candidates. TRIZBench's best arm is exactly this: code supplies candidates, model selects.
5. Model writes one concrete idea per chosen principle.
6. Code runs the check (S4) on each idea. Novelty is judged by running (G8).
AutoTRIZ uses steps 1 to 5 with a deterministic lookup (b03, c09). Step 1 is the weak link (pair F1 0.29 to 0.45).

**4.2 Candidate set and variety control.** Contradiction choice varies run to run (entropy up to 6.64 bits). Use that as a feature. Sample the pair several times in separate contexts, count frequencies in code, and try the principles of the top 2 to 3 pairs in frequency order. The AutoTRIZ authors did not majority-vote, since different valid contradictions give different valid solutions (c10). Frequency orders trials. It is not proof (G4).

**4.3 Gating the trigger (G1).** Trapp's 86 of 100 false flags say a model finds a trade-off almost anywhere. A TRIZ-type reframe should fire only after a failing check or an impasse (S6). Further gate: the model must quote the span that states each side, and code confirms the span exists in the input (TRIZBench grounding, K09). A label with no supporting span is treated as unproven.

**4.4 Concrete principle cards.** Livotov (d11, abstract) found less abstract wording gives more ideas. Store each principle with a one-line concrete example in the code-held table. Prompt exemplars can backfire: few-shot narrowed GPT-4 output and cut recall from 0.675 to 0.245 (K10). So give a card, not a worked solution to copy.

**4.5 Physical-contradiction form (for O4).** TRIZ's second contradiction type: one element must have property X and not-X. The standard separations are in time, in space, on condition, and between whole and part. This maps to "drop a constraint": instead of dropping the condition, split it by time, place or part. No LLM study tests it. A possible typed O4 variant (design reading only).

**4.6 Ideal final result (for O8).** Prompt form: "State the answer in which the required function happens with no new part, no added cost and no harm. What in the current framing blocks that?" It reframes the goal by removing the means. Our only measured analogue is TRIZ-a's Ideality score used inside a search loop (K15, K20). Nothing measures it alone.

**4.7 Mutation operators (TRIZ-a).** Each principle becomes a typed code transformation. The agent must declare the contradiction and operator before seeing results, and a promotion gate decides acceptance. This is the closest published match to O4 and O8 in an agent loop. Gate tuning data: Campaign08 original gate promotion F1 0.508; a stricter variant had specificity 0.998 but recall 0.257 (F1 0.409); balanced V2 reached promotion F1 0.811 with recall 0.686 (c18). The gate matters as much as the operator.

**4.8 Why it might work (competing explanations).**
- *Content:* the principle supplies a useful transformation (the TRIZ claim).
- *Forced problem restatement:* naming two parameters makes the solver re-describe the problem. Gero 2012 shows problem focus up (0.526 vs 0.192). Restatement alone is a known gain elsewhere (schema S1; F03, F12).
- *Random stimulus:* any distant prompt breaks fixation. A second-hand note says randomly chosen design heuristics improved human outcomes (d18, K28). If so, the principle's identity matters little.
- *Taught-method effect:* student classes with an instructor present (Ogot) include coaching and time on task.
These cannot be told apart on current data. The arms in section 8 separate them.

## 5. What holds up

**Held up.**
- TRIZ users produce more novel and more varied ideas than ad hoc controls in several student studies (Hernandez 2012 at 2 of 3 sites; Duran-Novoa 2024; Ogot 2006 on unique concepts). Direction is consistent. Effect sizes are not reported, and sites vary (novelty p from 0.0004 to 0.5786).
- A structured method moves attention to the problem (Gero 2012, p = 0.001).
- For LLMs: detecting that a contradiction exists is easy; picking the right pair is hard. This appears across five model families in TRIZBench, in humans (b14), and in the older PaTRIZ baseline [E].
- For LLMs: code-held lookup plus model rerank beats free principle naming [S, one benchmark].
- Instability of contradiction choice across samples (AutoTRIZ) matches the general finding that same-model samples vary and are correlated (G4).

**Did not hold up or unresolved.**
- The quantity gain (Ogot: about 2x) did not replicate (quantity p 0.29 to 0.63; slightly lower). Designs differ (course sections vs controlled sessions), so not a clean refutation.
- The 2013 journal paper reports the same UTEP/UMD data as the 2012 paper (d09), so there is one experiment family, not two replications. No independent human replication since 2013 was found.
- Chulvi et al. 2013 found brainstorming better, but with one brainstorming team (a25, second hand).
- AutoTRIZ's central claim (LLM+TRIZ beats LLM alone) is not tested in its paper (K17). The only comparison is the remark that plain ChatGPT's TRIZ output "always included apparent errors" (a13).
- Text-to-CAD "TRIZ resolves strength-weight" overstates its own table: 1 of 4 principles kept stress flat; vanilla stress stayed under 2% of yield; the text's deflection claim (under 0.5 mm) is not met by vanilla (0.574 mm) (critique).
- TRIZ-a: gains cannot be credited to TRIZ (K15). The authors name the missing equal-budget unguided control themselves.
- TRIZ-RAGNER (+7.3 F1 points) is contested: signs of pasted text, no model names. Its ablations never swap TRIZ-typed knowledge for untyped knowledge (d17).
- IdeaForge's "convergence" is agreement across prompts of one 1.1B model (TinyLlama), not independent evidence (K19).

**Moderators.**
- Relational reasoning ability: higher raises the TRIZ novelty gain (abstract only).
- Supervision: unsupervised teams drift from the principles; guided practice fixed it (a27).
- Principle wording: concrete beats abstract (abstract only).
- Prompt style for LLMs: few-shot narrows output and cuts recall; CoT gives best recall; solution similarity unchanged.
- Model strength: GPT-4 over GPT-3.5 under basic and CoT, not few-shot.

**Interventions that worked (with limits).** Matrix lookup by code then model rerank (Hit@3 0.71/0.59 with gold pair; 0.59/0.46 end to end). LoRA tuning of an 8B model (detection F1 0.90 best; end-to-end Hit@3 0.65/0.52). Span grounding as a diagnostic for wrong labels. Retrieval of TRIZ definitions for tagging (contested). An LLM question step before TRIZ for functions and conflicts (abstract only).

**Did not work or no effect.** Few-shot for recall. Prompt strategy for solution similarity. Running all 40 principles blindly. Multi-agent role play (cost, partial recovery). Letting an agent choose whether to call its lookup tool (it skipped it).

**Unmeasured anywhere:** random-principle arm, restate-only arm, IFR-only arm, equal-token plain arm, blind raters (K16, K29).

## 6. Language models

**The evidence.** Seven LLM+TRIZ arXiv papers 2024 to 2026 (b25), TRIZBench (ACL Findings 2026), and Springer/Crossref items we could not open (c23 to c26, d12). Case counts: AutoTRIZ 10, TRIZ-GPT 47 (37 + 10), EBD-LLM 3, TRIZ Agents 1, Text-to-CAD 1, IdeaForge 5 use cases, Trapp 100 patents, TRIZBench 1,354 cases. None compares a TRIZ-structured prompt with a matched-token plain prompt using blind-rated outputs.

**How models behave.**
1. *Detect yes, pair no.* Detection F1 0.75 to 0.87 prompted, 0.90 best LoRA; pair F1 0.29 to 0.45; patent pair Hit@3 0.13 to 0.28. Humans show the same shape.
2. *Over-fire.* GPT-4 flagged 86 of 100 no-contradiction patents. TRIZBench told models to abstain when nothing could be grounded, yet detection stayed high. No false-positive rate is reported there.
3. *Unstable.* GPT-4 over 100 runs: entropy up to 6.64 bits; 7 of 10 cases matched or half-matched in the top 3. Frequency tracked textbook agreement.
4. *Principle choice.* Direct prompting Hit@3 0.25 to 0.52. Matrix lookup 0.67/0.48. TF-IDF 0.69/0.56. Matrix-Rerank Qwen3-8B 0.71/0.59 with the gold pair; end to end 0.59/0.46 zero-shot, 0.65/0.52 LoRA. Chance is 7.5% to 27.7%. Every number sits above chance, but a frequency-prior baseline was never run.
5. *Solutions.* Given a principle, GPT-4 writes solutions close to the published one (cosine 0.82 to 0.83, flat across prompts). Embedding similarity cannot rank quality. It rewards reproducing the textbook, and the cases may be in training data.
6. *Prompt effects.* Few-shot cut recall 0.69 to 0.25. CoT gave best recall. Model size helped only under basic and CoT.
7. *Type changes the answer.* In the one CAD case, a vanilla "lighter" prompt over-cut mass (-31.8%) and doubled deflection (+99.4%). Segmentation held stress (-0.1%) and deflection (+0.7%). The other three principles raised stress by 21.6% to 40.7%. N = 1, no repeats.
8. *Agent loops.* TRIZ operators with gates gave +0.15 to +4.23 F1 points over three tasks, unattributed. 45-activity campaign +1.90% against 3.2277% required.
9. *Cost.* A multi-agent TRIZ run used 150,000 to 250,000 tokens for one case.
10. *Baseline problem.* TRIZBench's LLM baselines also receive the gold pair (d01). Gold labels come from published TRIZ cases, which models may have seen.

**What changed behaviour, by how much.** Few-shot: -44 points recall (0.69 to 0.25). CoT: +0.016 recall (0.675 to 0.691). Code lookup instead of model naming: +0.15 to +0.30 Hit@3 on cases, +0.2 on patents. Rerank over lookup: +0.04 (cases), +0.11 (patents). LoRA over zero-shot end to end: +0.06. Model size: up to +0.14 recall, prompt dependent.

**IFR.** No study. It appears only as an Ideality score in TRIZ-a and as a prompt step inside pipelines (K20).

## 7. What our agent should take

Each item: schema part, status, claim and evidence ids.

### Add now (established)

Few items reach [E]. Both below confirm existing guardrails rather than add operators.

1. **Treat TRIZ claims as heuristics. Every TRIZ reframe must beat the plain model at equal tokens before it ships.** Part: G7. [E] K01, K16. Evidence a01, a03, a04, a28, b25.
2. **A model's "I see a trade-off" is not a trigger.** Reframe only after a failing check or impasse. The model detects trade-offs far better than it names them. Part: G1 (already present). [E] K06 for the detect-versus-pair gap (a17, b11, c02, b14, d04). The over-fire figure is [S] K07 (a05, a06).

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Typed reframe in O4: code lists 2 to 3 candidate principles from a table, model picks one and applies it | O4, G5 | [S] K08 | a18, b12, c03, d01, d03 |
| 2 | Restate-only arm vs typed-principle arm (content or restatement?) | S1, O4 | [S] K04, K28 | a23, d18 |
| 3 | Gate the trade-off trigger on a failing check plus a quoted span per side | G1, G2, O4 | [S] K07, K09 | a06, a19, d05 |
| 4 | Sample the pair several times in fresh contexts; order trials by frequency | S3, G4 | [S] K11 | a11, b04, c10 |
| 5 | Concrete one-line card per principle (not a worked solution) | O4, memory | [S] K27, K10 | d11, a08 |
| 6 | IFR prompt as the typed form of O8 vs plain "simplify" | O8 | [S] K20 (absence of evidence) | a02, c22, d19 |
| 7 | Physical-contradiction split (time, space, condition, part) as typed O4 variant | O4 | [D] no LLM test | design reading |
| 8 | Declare operator and contradiction before running; promotion gate on a held-out check | O4, O8, G3 | [S] K15 | b17, c17, c18, d07 |
| 9 | Record which principle solved which problem class | memory (S9) | [S] | b17 |
| 10 | Weak-model test: expect smaller gain with weaker analogy ability | O4, S0 | [S] K26 | d10 |
| 11 | Compute a principle-frequency top-3 baseline before crediting any selector | G7 | [S] K24 | d02 |
| 12 | No few-shot worked solutions inside principle prompts | O4 | [S] K10 | a08, a09 |
| 13 | Never run all 40 principles blindly: filter by table, score by code | O4, G12 | [S] K21 | c20 |
| 14 | Compulsory lookup in code, not a tool the agent may skip | G5 | [S] K18 | a14, d15 |

Notes. TRIZ-RAGNER (K13) and IdeaForge (K19) are not evidence. AutoTRIZ is a design to copy, not an effect to cite (K17). Per schema 4b, a TRIZ prompt is creativity training in the prompt, so start from the d = 0.29 to 0.32 prior and expect small gains.

## 8. Concrete tests on our bench

All arms at equal tokens, setup cost counted (G7), token counts reported per arm, at least 3 repeats (sample instability).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 typed vs free vs none (gap 1) | Open-mode design and NoveltyBench-style items; items with an explicit trade-off; checkable puzzles with a stuck first attempt | (a) plain; (b) free "reframe and retry"; (c) typed reframe, code-held candidates, model selects; (d) random principle; (e) restate-only | Correct rate where a check exists; distinct valid answers (code-clustered); blind-rated novelty on open items | Typed over plain by a small margin on trade-off items; typed vs restate-only within noise. Count down, variety up (K03, K23) |
| T2 content vs restatement (gap 2) | Same items | restate-only vs typed vs random principle | Same | If restate-only matches typed, drop the table and keep S1 |
| T3 end-to-end principle accuracy (gap 3) | 100+ TRIZBench cases | Model predicts pair, code looks up, model reranks; vs gold pair; vs TF-IDF; vs frequency prior | Hit@3 with the prior as floor | About 0.5 to 0.6, not above TF-IDF |
| T4 false-fire rate (gap 4) | 100 trade-off items vs 100 neutral items | Trigger on model claim vs trigger on failing check | False-trigger rate; wasted tokens | Check gating cuts false triggers sharply (Trapp 86%) |
| T5 pair sampling | TRIZBench cases | 1 sample vs 5 fresh samples ordered by frequency, equal total tokens | Principle Hit@3; answer correctness | Small gain if any |
| T6 IFR alone (gap 5) | Open and trade-off items | IFR prompt vs plain "simplify" vs none | Distinct valid answers; correctness | Unknown, small |
| T7 concrete cards (gap 6) | Same | Name only vs name plus one-line example | Idea count, distinct count | More ideas with cards (Livotov) |
| T8 span-citing (gap 10) | Non-patent items | Reframe with checked span vs without | Correctness; label vs span accuracy | Spans predict final correctness better than labels |
| T9 untyped-mutation ablation (gap 9) | TRIZ-a-style search loop | Typed operators vs untyped mutation vs random operator, equal budget | Held-out score | The decisive test the TRIZ-a authors say is missing |
| T10 weak vs strong model | Same items | Typed reframe on a small and a large model | Gain size | Small model gains less (K26) |

## 9. What does not transfer, and why

- **Student idea counts.** Humans were scored on number of concepts. Our agent wants correct answers or variety, not quantity.
- **The matrix itself.** It was derived from patents of physical devices. Reasoning, maths and code problems rarely map to "weight" or "reliability". The 39 parameters will not fit most schema tasks. Keep TRIZ's form (name a trade-off, look up typed moves) and build a table per problem class.
- **Instructor coaching.** Ogot's guided practice is not available. A code monitor stands in for it.
- **Teams.** Human studies used 2-person to 4-person teams. Our agent is single (G9).
- **Patent text as input.** TRIZBench cases are long technical texts with known labels. Our items are short puzzles.
- **Embedding similarity to a published solution.** Rewards copying and is flat across prompts. Not a usable metric.
- **Gold labels from published cases.** May sit in pretraining data and overstate generalisation.
- **Multi-agent TRIZ.** Costly (150,000 to 250,000 tokens) and against G9 and G11.
- **IFR as "means vanish".** Fine for design. It can hurt when the task demands a given mechanism (a proof step, a code spec). Needs a check that the IFR answer still meets the stated requirement.
- **TRIZ novelty claims.** Many rest on author or expert judgement. Our rule is that novelty is judged by running (G8).

## 10. Open questions

1. At equal tokens, does a typed TRIZ reframe beat free reframing and no reframe on correctness or blind-rated variety? (gap 1, K16)
2. Is the benefit principle content, restatement, or random stimulus? (gap 2, K28)
3. What is end-to-end principle accuracy against a frequency-prior baseline? (gap 3, K24)
4. What is the false-fire rate on neutral items, and does failing-check gating cut it? (gap 4)
5. Does an IFR prompt alone change quality or diversity? (gap 5)
6. Do relational reasoning and concrete examples moderate the effect, and by how much? (gap 6, abstracts only)
7. Do the 2025 to 2026 Springer IFIP chapters (ARIZ with LLMs, contradiction processing, cognitive skills) report controlled numbers? (gap 7, pages blocked)
8. Is the Hernandez novelty gain replicated by an independent lab? (gap 8, none since 2013)
9. Does the TRIZ-a gain survive an equal-budget untyped-mutation ablation? (gap 9)
10. Do span-citing reframes predict correct answers outside patents? (gap 10)
11. How much of TRIZBench is in model training data?
12. How do newer frontier models behave? Results here use GPT-4, GPT-3.5, GPT-4o, Qwen3-8B/32B, LLaMA3.1, Gemini-2.5-Pro and Claude Sonnet 4.5 (CAD only). Scaling is unmeasured.

Links to other subfields in this run (not covered here): Morphological analysis, Creative problem solving, Analogy and distant sources, Breakthrough innovation, Methodologies of discovery, Cognitive task analysis, Problem posing and conjecture, Reflection-in-action.

## 11. Sources

[V] opened, [M] snippet, abstract or metadata only. Ids refer to the evidence files.

- [V] Wikipedia, TRIZ. https://en.wikipedia.org/wiki/TRIZ (a01)
- [V] Wikipedia, Ideal final result. https://en.wikipedia.org/wiki/Ideal_final_result (a02)
- [V] Wikipedia, Genrich Altshuller. https://en.wikipedia.org/wiki/Genrich_Altshuller (a03)
- [V] Trapp and Warschat (2024) LLM-based Extraction of Contradictions from Patents. https://arxiv.org/abs/2403.14258 and https://arxiv.org/pdf/2403.14258 (a04 to a07, b08, b09, c13, c14)
- [V] Chen et al. (2024) TRIZ-GPT. https://arxiv.org/abs/2408.05897 , https://arxiv.org/html/2408.05897v1 (a08 to a10, b05 to b07, c05 to c08, d14)
- [V] Jiang, Li, Qian, Zhang, Luo (2025) AutoTRIZ. https://arxiv.org/abs/2403.13002 , https://arxiv.org/html/2403.13002v4 (a11 to a13, b03, b04, c09 to c11, d18)
- [V] Szczepanik and Chudziak (2025) TRIZ Agents. https://arxiv.org/abs/2506.18783 (a14, b16, c12, d15)
- [V] Xu, Wu, Zhao (2026) TRIZ-RAGNER. https://arxiv.org/abs/2602.23656 (a15, b15, c15, d17)
- [V] Wang and Uzzi (2026) TRIZBench, ACL Findings. https://aclanthology.org/2026.findings-acl.1798/ and https://aclanthology.org/2026.findings-acl.1798.pdf (a16 to a19, a28, b10 to b14, c01 to c04, c21, d01 to d05)
- [V] Lee et al. (2026) TRIZ-inspired text-to-CAD. https://arxiv.org/abs/2606.21378 (a20, b18, c16, d06)
- [V] Liu, Huang, Wang (2026) TRIZ-a. https://arxiv.org/abs/2610.04555 (b17, c17, c18, d07)
- [V] Bose (2026) IdeaForge. https://arxiv.org/abs/2605.13311 (b19, c19, d16)
- [V] Ogot and Okudan (2006) Integrating systematic creativity into first-year engineering design. https://www.ijee.ie/articles/Vol22-1/IJEE1618.pdf (a21, a27)
- [V] Vargas-Hernandez, Schmidt, Okudan (2012) ASEE paper. https://peer.asee.org/21369.pdf (a22, a26, d08)
- [V] Gero, Jiang, Williams (2012) Design cognition differences. https://collaborative.designsociety.org/download-publication/32457/Design+Cognition+Differences+When+Using+Structured+and+Unstructured+Concept+Generation+Creativity+Techniques (a23)
- [V] Duran-Novoa and Torres-Benoni (2024) JOTSE. https://jotse.org/index.php/jotse/article/download/2473/882 (a24, a25)
- [V abstract] Mohammadi and Zeng (2025) Enhancing TRIZ through environment-based design with an LLM. https://doi.org/10.1017/S0890060425000083 (b26, c20)
- [V abstract] Dumas and Schmidt (2015) Relational reasoning as predictor for engineering ideation success using TRIZ. https://doi.org/10.1080/09544828.2015.1020287 (b21, d10)
- [V abstract] Livotov, Chandra Sekaran, Masudah (2019) Lower abstraction level of TRIZ inventive principles. https://inria.hal.science/hal-02905548 (b22, d11)
- [V abstract] Hernandez, Schmidt, Okudan (2013) Systematic ideation effectiveness study of TRIZ. https://doi.org/10.1115/1.4024976 (b01, d09)
- [V abstract] Cok et al. (2026) Evaluating TRIZ with and without LLM support. https://www.citedrive.com/en/discovery/evaluating-triz-with-and-without-llm-support-an-experimental-study-on-engineering-problem-solving/ (b02)
- [V] arXiv TRIZ listing https://arxiv.org/search/?query=TRIZ (b25); IFR phrase search https://arxiv.org/search/?query=%22ideal+final+result%22&searchtype=all (c22); Crossref scan https://api.crossref.org/works?query.bibliographic=TRIZ+large+language+model (d19)
- [M] Ilevbare, Probert, Phaal (2013) A review of TRIZ. https://doi.org/10.1016/j.technovation.2012.11.003 (b20)
- [M] Chang, Chien, Yu, Chu, Chen (2016) Effect of TRIZ on the creativity of engineering students. https://doi.org/10.1016/j.tsc.2015.10.003 (b23, d13)
- [M] Hernandez et al. 2006 and 2012 DETC versions. https://doi.org/10.1115/detc2006-99483 (b24)
- [M] Springer IFIP TRIZ chapters. https://doi.org/10.1007/978-3-032-08847-5_12 , https://doi.org/10.1007/978-3-032-08847-5_22 , https://doi.org/10.1007/978-3-032-43196-7_9 (c23 to c25, d12)
- [M] Nuclear TRIZ GPT (2024). https://doi.org/10.13182/t130-45953 (c26)
- [M] 153-senior patent-analogy study, via the ASEE paper. https://peer.asee.org/21369.pdf (a29)
- [M] Yilmaz et al. on random design heuristics, second hand via AutoTRIZ (d18); Chulvi et al. 2013 and Duran-Novoa et al. 2019, second hand via a24 and a25.
