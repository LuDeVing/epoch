# E13.03 Coordination and common ground: cross-check and critique

Files checked: evidence_a.jsonl (33 lines), evidence_b.jsonl (26), evidence_c.jsonl (30). Claims: claims.jsonl (22 claims, K01-K22).
Many lines are duplicates of the same paper written by different agents (Shaikh 2024, Cemri 2025, Li 2023, Laban 2025, Kim 2026, Collaborative Gym, CollabLLM, FANToM, Ullman). Duplicates were counted as ONE independent source in claims.

## 1. Numbers re-opened this session (arXiv abstract or full PDF text)
1. Shaikh et al. 2024 (arXiv 2311.09144, PDF text): 77.5% fewer grounding acts, follow-ups -64.3%, acknowledgements -83.4%, clarification kappa 0 to -1.65, questions in 11.83% UltraChat, 13.77% preferred vs 18.35% dispreferred. CONFIRMED.
2. Laban et al. 2025 (2505.06120): 39% average drop, 200,000+ conversations, aptitude -15%, unreliability +112%. CONFIRMED.
3. Cemri et al. 2025 (2503.13657): 1,642 traces, kappa 0.88, failure rates 41% to 86.7%, category shares 41.8 / 36.9 / 21.3. CONFIRMED. a21 says 1,642 and b04/c18 say 1600+: both right (abstract rounds).
4. Cemri +9.4%: CORRECTION NEEDED. The paper itself is inconsistent. The introduction says the CEO-final-say workflow change gave +9.4%; the body and appendix say improved role specification alone gave +9.4% (ChatDev, GPT-4o). Evidence a22 and c19 state both as if the same figure and cause. Treat +9.4% as "ChatDev role/workflow fix, cause named two ways". The +15.6% on ProgramDev is from adding a verification step (confirmed). a22 wrongly ties +15.6% only to appendix H of the CEO change; it is the verification step.
5. Kim et al. 2026 (2512.08296): 260 configurations, 6 benchmarks, 5 architectures, +80.8% to -70.0%, cross-validated R2 0.373, best architecture predicted for 87% of held-out cases. CONFIRMED. The 17.2x vs 4.4x figure was not re-opened (abstract only says error propagation is worse without central verification).
6. Vaccaro et al. 2024 (abstract via OpenAlex): 106 studies, 370 effect sizes, g=-0.23, CI -0.39 to -0.07. CONFIRMED. Subgroup numbers (decision -0.27, creation +0.19) not re-opened here. Note: abstract itself lists publication bias as a limit.
7. Wu et al. 2025 CollabLLM (2502.00640 abstract): 18.5% task performance. CONFIRMED (46.3% and 13.3% are from the same abstract line, seen cut off; accepted).
8. Hu et al. 2020 Other-Play (PDF text): 15.75 (s.e.m. 1.23), 45% bombed out, vs 9.15 (1.18), 85%. CONFIRMED.
9. Ullman 2023 (2302.08399 text): 99% chocolate original, 95% and 98% in altered versions. CONFIRMED. Caveat: evidence b14 says a transparent bag keeps "95 to 98% chocolate"; the text shows 95 and 98 appear in two altered variants.
10. Kim et al. 2023 FANToM and Li et al. 2023 ToM probes: NOT re-opened (budget). Marked below as unchecked.

Note on c05: "12.3 rounds vs 28.3" has order uncertainty (flagged by its own author); b12/a20 give GPT-4 12.3 vs GPT-4+belief 11.0 and MAPPO 30.0. These disagree. Do not use 28.3 until checked.

## 2. Contradictions between sources
- c05 (12.3 vs 28.3 rounds) vs a20 (12.3 vs 11.0). Unresolved.
- a17/b01/c01 list the same Shaikh figures; c02 says human-human kappa 37.5 on a x100 scale, b02 says kappa "mostly below 0.3" and c02 "below 0.2 for most OpenAI variants". Different cut-offs, same finding.
- Keysar 2000: a13 reports 1.01 vs 0.65 fixations; b20 reports 23% hidden-object reaches. Different measures from Exp 1; not contradictory but both come from one study.
- Egocentric-bias claim is contested: Santiesteban 2015 finds accuracy equal for director vs camera (.79 vs .80), so the effect may not be perspective-taking at all. Samuel 2019 shows it flips after adopting another view.
- Debate fails (b18) vs blackboard design helps by 4.33% (c26) vs MAST says structure matters: not contradictory, but the benchmark sets differ and no equal-token comparison exists.

## 3. Weak spots
- Founding human studies are thin: Clark and Wilkes-Gibbs 1986, Brennan and Clark 1996, Krauss and Weinheimer 1964, Horton and Keysar 1996 were NOT opened (a14, a16, a32, a33). Cohen 1984 is second-hand through Clark and Brennan. No exact human numbers for the tangram or conceptual-pact result.
- Klein et al. 2004 ten challenges: only titles read.
- Most LLM evidence is single-source per finding (K04-K14, K19-K21). Status "single-source" is honest.
- Shaikh 2024 used GPT-3.5 and older open models; results for 2025-2026 frontier models and reasoning models are unknown.
- Meta-analysis b06 mixes tasks and AI types; "AI" in 2020-2023 studies is mostly not LLM.
- DeChurch 2010 (b23) was seen only through a search summary.
- Nothing here tests software-as-teammate via the Klein/Woods/Bradshaw requirements (predictability, directability) with measured results; the 2004 and 2005 papers are conceptual.
- Mesmer-Magnus 2017 and DeChurch 2010 are human-team results; transfer to a single LLM is by analogy only.
- Zero direct test of a grounding or clarification step inside a scaffold at equal tokens. Everything pointing to our schema is inference.

## 4. Only seen in snippets or abstracts
a14, a16, a32, a33 (not opened); b23; c29 (first page only); c12 and c16 (garbled tables, column mapping unverified); c23 (column order inferred); b19/c17 numbers absent.

## GAPS
1. Does an ambiguity-gated clarify step (ask only when slots are missing) beat both never-ask and always-ask at equal tokens on underspecified single-agent tasks? (Shaikh shows always-ask overshoots; Laban shows never-ask loses 39%.)
2. Do 2025-2026 reasoning models and frontier chat models still show the 77.5% grounding gap, and does thinking before replying change it?
3. Does an explicit "what the other party believes" slot improve a single agent, or only multi-agent games (Li 2023 evidence is from a 3-agent bomb game)? Is the Li et al. round count 28.3 or 11.0 for the no-belief case?
4. Does a recap or snowball restatement in the scaffold recover the sharded-conversation loss at equal tokens (Laban recap 66.5 vs full 86.8 for GPT-4o-mini)?
5. What are the exact human numbers for conceptual pacts and reference shortening (Clark and Wilkes-Gibbs 1986; Brennan and Clark 1996) and their replication record?
6. Is there any measured test of the Klein et al. Basic Compact requirements (predictability, directability) on LLM teammates, in human-AI studies of 2023-2026?
7. Is the Cemri +9.4% due to role specification or CEO final say, and did anyone replicate MAST interventions on other frameworks?
8. Does preference tuning's grounding drop (DPO R about -0.79) show in current RLHF models, and can a prompt repair timing (not only frequency)?
9. Does the Santiesteban spatial-coding account hold for LLM referential tasks, i.e. do LLMs show egocentric reference errors or something else?
10. How does the 17.2x vs 4.4x error amplification (Kim 2026) behave for a single agent with an internal verifier?

## Gap search results (evidence_d.jsonl, d01-d19; claims updated, K23-K28 added)
Web search was out of budget, so work used arXiv PDFs, Semantic Scholar citation lists and the Stanford copies of the two Clark papers.

1. CLOSED in part (K23, K24). Gated clarification: Edwards and Schuster 2026 (N=500) gives never-ask 54.8, forced-ask 70.4, one agent self-checking 61.2, separate intent checker 69.4, full spec 70.8. Gate beats never-ask and ties forced-ask. Not at equal tokens, so the equal-token part stays OPEN. Ambig-SWE: detection is the bottleneck (best 84-89%, some at chance).
2. CLOSED for 2024-25 models (K04, K07). Rifts (2025): GPT-4o, o3-mini, Claude 3.5 all at or below chance on grounding initiative. Laban: o3 and R1 degrade like others. 2026 frontier models and thinking-before-replying beyond o3-mini, o3, R1 remain OPEN.
3. PARTLY CLOSED. 28.3 vs 12.3 in Li 2023 cannot be tied to belief vs no belief (table labels lost, prose inconsistent); do not use it. Belief slot helps single agents too: Grounding Layer (Sensitivity 0.06 to 0.56). The round-count effect stays OPEN.
4. PARTLY CLOSED. Recap recovers about 52% of lost points (GPT-4o), snowball about 18%; both need extra tokens, no equal-token test. Equal-token test OPEN.
5. CLOSED for human numbers (K25): 41 to 8 words per figure; 48% vs 18% same vs new partner. Replication record OPEN (Metzing and Brennan 2003 not opened). LLM side: no pact formation (d12, d13).
6. OPEN. No measured test of predictability or directability on LLM teammates; only descriptive taxonomies (K27).
7. PARTLY CLOSED. The +9.4% cause was already ambiguous in the paper. No replication of the ChatDev fix found among the citers checked (a handful of 89+ titles read). A later paper: forcing submission raised recovery 0.198 to 0.613, so role effects may be a gate effect.
8. PARTLY CLOSED. Rifts shows timing can be repaired by a forecaster-gated prompt (about 24 to 54.48). The DPO drop in current 2026 RLHF models remains OPEN.
9. OPEN. No LLM test of the spatial-coding account. PARLEY says agents show excessive compliance rather than egocentric bias.
10. OPEN. Kim 2026 never ran a single agent with an internal verifier; the amplification coefficient is not significant after controls (p=0.658).

Unchecked: d09 not opened; d12, d13, d14, d17, d18 are abstract-level only. Table 1 of Li 2023 not rendered.
