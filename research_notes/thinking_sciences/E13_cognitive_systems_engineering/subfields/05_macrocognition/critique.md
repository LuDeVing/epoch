# E13.05 Macrocognition: cross-check critique

Checked 2026-11-10. Sources re-opened (full PMC or arXiv HTML text, searched for the exact numbers): Kopka and Feufel 2026 (PMC13061108), Vaccaro et al. 2024 (PMC11659167), Vidulich and Tsang 2026 (PMC13100097), Klein and Wright 2016 (PMC4731510), Norwegian survey 2026 (PMC13113691), Buchler et al. 2016 (PMC4916213), Porat et al. 2016 (PMC4878290), GraphRAG (arXiv 2404.16130), DecisionFlow (arXiv 2505.21397v2).

## Corrections and confirmations

Confirmed exactly:
1. Kopka and Feufel: 63.3 / 67.6 / 66.7%; OR 2.26 (z 8.69) and 2.05 (z 7.23); self-care 13.4 to 29.8 / 24.6%; 18 of 45 cases up (40%), 13 down (29%), median gain 18% (IQR 5-24), median loss 5%; 12/13 decreases nonemergency (92%); GPT-4.1 self-care 0% to 43.8% / 39.2%; GPT-5.2 Instant 57.8 to 56.4, GPT-5.2 Thinking 52.0 to 53.1.
2. Vaccaro: 106 studies, 370 effects, g -0.23 (CI -0.39 to -0.07), decision g -0.27 (CI -0.44 to -0.10, P=.002), creation g +0.19 (CI -0.09 to 0.48, P=.18), moderator F(1,104)=7.84, P=.006.
3. Vidulich and Tsang Study 1: t(19)=6.54 d=1.39; t(19)=4.23 d=0.96; about half a pawn.
4. Klein and Wright: "80-90%" and "10-20 years" quoted as written; replications named by the authors.
5. Norwegian survey: N=225, KMO .741, chi2(36)=282.86, 29.24% variance (factor 1 21.63%, factor 2 7.60%).
6. Buchler: 213 staff and 19168 correspondences; 3191 calls among 132 staff; 89 nodes (45 division, 23 UK brigade, 21 US brigade).
7. Porat: 13 min (SD 6) to under 5 min in 95% of cases; supervise up to 15, control 3.
8. GraphRAG: 72-83% / 72-80% comprehensiveness, 75-82% / 62-71% diversity; 125 questions per dataset; 47,075 claims, 31 per answer.
9. DecisionFlow: GPT-4o MTA 79.25, DeLLMa 70.70 (top-3 setting), table values match.

Corrections and flags:
- a25 / b24 say "88% of all errors were over-triage". I searched the Kopka text for "over-triage", "overtriage" and "88%": NOT FOUND. Treat that line as unverified. What the paper does say: 92% of accuracy decreases were in nonemergency cases, and the authors speculate the prompt helps the model "reconsider overly cautious recommendations".
- a24 says "one vendor's chat models". Correct: 10 OpenAI ChatGPT models (GPT-4o to GPT-5.2), default temperature 1, no seed, 10 repeats. A temperature-0 sensitivity check was run on the 2 best models only (not in our notes). Output length was not capped, so the prompt arms differ in tokens.
- a23 said "defence college". The paper says active-duty personnel of the Norwegian Armed Forces (2024-2025). Also factor loadings and alpha were not rechecked.
- c10 / c11: "prompt tokens about 7,900 vs 1,700" and "latency 28 s vs 2 s" were NOT found in the text I searched (the paper gives a runtime table by domain; format differs). Keep as unconfirmed. Direction (DecisionFlow uses larger budgets) is confirmed.
- Vaccaro "-0.23" is versus the BEST of human or AI alone, not versus the average of them. Egger test beta 1.96, P=.002 shows small-study asymmetry; authors did not correct. b22 reads more hopeful than the data.
- Buchler: b12 says SA from self-report survey (confirmed) and the survey covered core units only.

## Duplicates (not independent)

Many evidence lines repeat the same paper: a02 = b01; a18/a19 = b14/b15; a24-a28 = b23/b24 = c01 (c01 is a search summary of the same Kopka paper); a09 = b09 = b13 (editorial vs Porat); a25/a26 = b24; b25 = c23. In claims.jsonl I count papers, not lines. c01 should be dropped as a source.

## Contradictions between sources

- RPD "explains 80-90%" (founders) versus chess blunders rising under time pressure (Vidulich and Tsang): not a direct clash, since RPD includes simulation, but the applied emphasis on fast intuition is weakened.
- Kopka: overall gain, but the prompt lowered accuracy in 29% of vignettes and did not help the two newest GPT-5.2 models (57.8 to 56.4; 52.0 to 53.1). The "reasoning vs nonreasoning" labels in the table look inconsistent with model names (GPT-5.2 Thinking labelled "Reasoning" in one column order); I did not resolve this.
- Cue-utilisation: strong latency effect in the rail study (eta2 .267) but no accuracy effect and a non-significant multivariate workload effect in the control-room study.
- LLM heuristics: c02 says LLMs resemble human bias; c05 shows they are more extreme and learn differently. "Human-like" is not one finding.

## Weak spots

- No study tests macrocognition as a scaffold for an agent against a token-matched control. Kopka comes closest, and it has no length control.
- The founding RPD figure rests on retrospective interviews coded by the authors; original paper (a29) and its replications were never opened by us.
- Plausibility-transition model: single coder, 23 of 73 cases, no predictions tested.
- GraphRAG and DecisionFlow are not NDM studies; they are sensemaking or decision pipelines that I linked to macrocognition by analogy.
- Human-AI team results (Vaccaro, SOC study) are about people, not a single agent.

## Only seen in snippets or abstracts

a13 (Laurent and Bianchi, body not read), a17 (Klein, Moon, Hoffman 2006), a29, a30, a31, a32, b17 (abstract), b27 (title only), c01 (search summary), c12, c17, c18, c19, c20, c21, c22, c25 (abstracts only), Kopka appendix tables S1, S2, S4. I did not re-open Brouwers 2016, Collins 2016, the ICU CTA study, Horowitz and Plonsky, Suri, Nguyen, Lim, Singh, Mainali or Kostka numbers; they are carried over as recorded.

## GAPS (most decision-relevant first)

1. Does an RPD-style or data-frame prompt beat a length-matched plain "think carefully" prompt at equal total tokens, on a non-medical benchmark and with a seeded, temperature-controlled run?
2. In Kopka, is the gain a threshold shift (more self-care answers, fewer over-cautious ones) rather than better reasoning? What is the gain on a metric that ignores class prior, such as balanced accuracy, and with temperature 0?
3. Do the 2025-2026 reasoning models (GPT-5.2, Claude, Gemini) already do the RPD steps internally, so the prompt adds nothing? Kopka's GPT-5.2 results hint at yes.
4. What do the original 1986 fireground data and the cited replications (Schmitt and Klein 1999, Keren 2013, Skriver 1998) actually report: N, coder agreement, share of RPD decisions?
5. Is there any controlled study of an anomaly-tracking or reframe step (the data-frame model's core) on LLMs, measuring how often the model abandons a wrong frame?
6. Does "pre-decision pattern retrieval from a case memory" (cue utilisation, RPD) cut tokens or errors in agents with a case library, and does the effect depend on experience size?
7. How large are human-AI team losses on decision tasks once publication bias is corrected, and does the loss apply to an agent's own self-critique step?
8. Which LLM-agent papers from 2024-2026 use "situation awareness", "sensemaking" or "naturalistic decision making" in their loops with a measured result (the arXiv title search missed them; try full-text and Semantic Scholar once the rate limit lifts)?
9. Do GraphRAG-style concept graphs help on reasoning tasks (not summaries), measured by answer correctness rather than LLM-judged comprehensiveness?
10. Are the DecisionFlow cost numbers (tokens and latency versus CoT) as reported, and does the gain survive a token-matched CoT with self-consistency?

## Gap search results (2026-11-10)

Evidence in evidence_d.jsonl (d01-d18); claims.jsonl updated (K01, K02, K03, K04, K05, K07, K11, K12, K17 changed; K19-K22 added). Web search budget ran out, so I used direct page fetches of PMC and arXiv. OpenAlex and Semantic Scholar were rate limited.

Corrections to the cross-check above:
- The "88% over-triage" line IS in Kopka and Feufel, worded "higher-than-necessary urgency (accounting for 88% of all errors, CI 87-88.9)". The cross-checker's keyword search missed it. a25/b24 stand.
- The temperature-0 check was on GPT-4.1 mini and GPT-5.2 Instant (largest and smallest prompt gain), not the 2 best models.
- The table's model-type label follows each row; GPT-5.2 Thinking is "Reasoning". The text says reasoning models gained more (OR 2.15) but the table shows larger raw gains for non-reasoning models. Still unresolved.
- DecisionFlow cost numbers are confirmed: MTA prompt tokens 7938.6 vs 319.10, latency 27.67 vs 2.21; DeLLMa 7892.68 vs 1673.32.
- Vaccaro main text says no publication bias was found; the Egger value was not located in the main text.

Gap status:
1. OPEN. No token-matched RPD or data-frame control exists. Kopka had no max_tokens and no length control.
2. CLOSED (for this paper). Nonemergency accuracy flat (82.5/82.0/82.8%); all gain from self-care (13.4 to 29.8/24.6%); 88% of errors over-urgent. Class-balanced mean still gains about +4.6 / +3.5 (my arithmetic). Temperature-0 appendix tables not read.
3. PARTLY CLOSED. GPT-5.2 (Instant and Thinking) gained nothing; gains were largest on weaker models. No Claude or Gemini data.
4. PARTLY OPEN. The cited "replications" are a magazine article (Schmitt and Klein 1999), a PhD thesis (Skriver 1998) and a VR stress and time-to-decision paper (Keren 2013, by title). 1986 paper not accessible; N and coder agreement still unknown.
5. OPEN. No planted-anomaly reframe test on LLMs found. Nearest: Laban et al. 2025 (39% multi-turn drop, models do not recover from early wrong turns; restating all information recovers 15-20% of the gap).
6. PARTLY CLOSED. Agent Workflow Memory: WebArena 35.5% vs 23.5%, fewer steps, gain within tens of examples and flat near 40. No test of token saving or library-size dependence in the RPD sense.
7. PARTLY CLOSED. Main text claims no publication bias; any bias would favour gains. Still no study of an agent's own self-critique step. Huang et al. 2023 (abstract only) says intrinsic self-correction does not help reasoning.
8. CLOSED (negative). Searches found no 2024-2026 agent paper using RPD or data-frame steps with measured results besides Kopka. "Situation awareness" appears as monitoring: SAUP (AUROC 0.771 vs 0.702, error detection only) and Collaborative Gym (SA failures in 40% of real trajectories). Search tooling was patchy, so absence is weak evidence.
9. CLOSED. On correctness, graph retrieval gain is small: MultiHop-RAG 70.27 vs 67.02; at matched tokens 71.17 vs 71.01; textbook set 69.3-73.6 vs 70.68 no retrieval; much higher cost.
10. PARTLY CLOSED. Costs confirmed. DecisionFlow beats 3-vote self-consistency (79.25 vs 69.25, GPT-4o) but with about 25 times the prompt tokens of CoT on MTA; no matched-compute comparison.

Not opened this round: Klein 1986, Schmitt and Klein 1999, Skriver thesis, Kopka appendix, Huang 2023 body, DeepSeek R1 medical paper body, last 12,500 characters of DecisionFlow, rest of Laban and Co-Gym.
