# Critique: Consensus and premature agreement (A17.05)

## Corrections made (sources re-opened this session)
Re-opened as full PDF text: Kaesberg et al. 2502.19130, Choi et al. 2508.17536, Wynn et al. 2509.05396, Du et al. 2305.14325, Zhang et al. 2502.08788, Sharma et al. 2310.13548.

1. Choi et al. (Debate or Vote): confirmed single 0.7205, vote 0.7691, decentralized T=2 0.7377, T=5 0.7050, sparse 0.7330, centralized 0.6551. Table 2 gives vanilla 0.7332 (a different run than 0.7377), Conformist 0.7625, Follower 0.7629, oracle 0.8236 at T=2; at T=5 vanilla 0.7160, Conformist 0.7439, Follower 0.7527, oracle 0.8364. So a23 and b07 are both right but refer to different T. Do not quote one "oracle" number without T.
2. Wynn et al.: MMLU 40.0 to 28.0 (-12.0), CSQA 53.4 to 46.8, GSM8K 61.0 to 64.8 in the 1+1+1 mix; 2+1 mix CSQA 58.2 to 50.2, MMLU 51.8 to 43.6 confirmed. Note GSM8K went UP in the diverse mix (+3.8), so "weak agent always hurts" is wrong. Which agent is the "weaker" in the 2+1 label was not clear from the table text; claim K09 words it neutrally.
3. Du et al.: arithmetic 67.0/81.8, GSM8K 77.0/85.0, chess 91.4/122.9, biographies 66.0/73.8, MMLU 63.9/71.1 confirmed.
4. Zhang et al.: "about 15% of cases", Heter-SoM +6.4%, Heter-EoT +8.2%, up to +5.8% over CoT average confirmed.
5. Kaesberg et al.: a28 (MMLU +2.3, MMLU-Pro +4.9, MuSR voting +26.4, SQuAD +13.1) and c08 (13.2% reasoning, 2.8% knowledge) are not contradictory: the abstract numbers are pooled maxima, the others per dataset. 59% approval-voting failure, 1.42 vs 3.38 rounds confirmed.
6. Sharma et al.: the "up to 27%" is two different results. Main text: wrong user suggestion cuts accuracy up to 27% (LLaMA 2). Appendix: are-you-sure cuts accuracy up to 27% for Claude 1.3 on average. 98% admit-mistake for Claude 1.3 confirmed. a31 mixed these; claim K13 states both.
7. Asch replication: a07 says N=210, b24 says 210 recruited and 202 analysed. Use 202 for analysis. 33% vs 36.8% (t(16)=0.59, p=0.57) and 25% with incentive stand.
8. Not re-opened (APIs rate-limited or no abstract): Lu et al. 2012 meta-analysis (65 studies, 3,189 groups, "eight times"), Stasser & Titus 1985 (18% vs 83% from memory). Treat both as unverified numbers.

## Contradictions between sources
- Debate helps (Du 2023, Liang 2024) vs debate does not beat vote (Choi, Zhang, Smit). Main reason: Du compared to a weak baseline and majority of 3 at low N; later work uses matched compute and more benchmarks. Du's own majority-vote control did get 69.0 vs debate 81.8 on arithmetic, so not fully explained; model generation also differs (GPT-3.5 era vs 7-8B open models).
- Heterogeneous mixes help (Zhang) vs a weak member hurts (Wynn). Probably depends on whether the stronger model is the majority and on the debate protocol (SoM/EoT are conservative).
- Agreement prompts help (Smit: Multi-Persona +15 at 90% agreement) vs agreement is the core failure (Wynn, Yao, Zhu). The Smit gain is for a protocol that was over-disagreeing by default, so it is a calibration of disagreement, not evidence for conformity.
- Consensus helps knowledge tasks but hurts reasoning (Kaesberg) while Choi says Conformist updates help on average. Different measures; unresolved.

## Weak spots
- Founding human literature is thin: Janis, Stasser & Titus, Nemeth, Schulz-Hardt were only seen through Wikipedia or abstracts. Human numbers are the least verified part.
- Most LLM results use 7-9B open models, 2-5 agents, 2-5 rounds, and 100-sample cells (Wynn: 100 questions x 5 seeds), so confidence intervals are wide and several differences of 2-3 points are noise.
- 2026 preprints (c15 to c22) were read but not independently replicated; "Not Just RLHF" ranges (44 to 98%) are very wide. Anonymous or unreviewed.
- No study tests the exact thing our agent would do: one model, one scaffold, with an internal dissenting role at equal tokens. Panel studies use separate agents with shared context.
- MAST percentages came from garbled text; do not use.
- Human remedy evidence (devil's advocate, Hartwig 2007) is mixed: authentic dissent beats role-played dissent in humans (Nemeth), but LLM devil's advocate gave large gains in Zhu et al. (one source).

## Only seen in snippets or abstracts
Stasser & Titus 1985; Nemeth 1986; Schulz-Hardt 2006; Mullen 1994 groupthink meta-analysis; Lu 2012; Mojzisch & Schulz-Hardt 2010; Reimer 2010; Lorenz 2011; Estornell & Liu 2024; DEAR 2026 (c20, numbers not extracted).

## GAPS
1. At equal tokens, does a single agent that runs k independent samples and a dissent step beat k-sample majority vote? (Decides whether any internal-dissent operator is worth its cost.)
2. What is the flip rate of a correct answer under 1, 2, 3 wrong peers for frontier models (2025-2026), not 7-9B models, and does it fall with a structured judge versus a plain prompt?
3. Does a verifier-gated minority-overturn rule (Minority Sentinel type) hold up in a replication by a non-author team, and what is its net gain at equal tokens?
4. What are the verified numbers for Stasser & Titus 1985 and Lu et al. 2012 (hidden-profile effect sizes), so the human baseline can be cited exactly?
5. Does a hidden-profile benchmark for LLM panels (information split across agents, best option looks worse to each) exist, and what is the pooling failure rate? Only the Pescetelli 2022 human-bot study and a few synthetic tasks were found.
6. Does instructed disagreement level have an optimum that transfers across models and tasks (Liang: moderate; Smit: agreement helps), or does it need per-task tuning?
7. Is role-played dissent (devil's advocate) as effective as authentic dissent for LLMs? The human literature says no; Zhu et al. say yes for sycophancy rate but not for final accuracy.
8. Why do voting and consensus protocols split by task type (reasoning vs knowledge), and can the agent detect the type in time to choose?
9. Does independence before sharing (no peer answers shown until each agent has committed) account for most of the benefit? This is the human hidden-profile fix (Mojzisch & Schulz-Hardt) and is untested directly in LLMs.
10. How much of the 2026 "yield" (44 to 98%) is a training effect (RLHF) versus a prompt framing effect, and does it exist in the base-model setting at all?

## Gap search results (evidence_d.jsonl, d01-d18)
Note: arXiv, Semantic Scholar and OpenAlex APIs were rate-limited (HTTP 429) for most of this pass, so search relied on direct PDF downloads and 4 WebSearch calls.

1. Equal-token internal dissent vs k-sample vote: STILL OPEN. Nearest evidence: Prakash 2026 (d09, single agent beats a 62x-token deliberation system overall, loses only on hidden-profile tasks), Wunderlich 2026 (d10, debate 70.0 vs self-consistency 68.7 at comparable budget on MMLU-Pro), Bertalanic 2026 (d14, independent sampling keeps full effective N). No paper tests a single-agent dissent step against k-sample voting at equal tokens. Claim K31 states this.
2. Flip rate for frontier models and structured judge: PARTLY OPEN. Only open-weight models measured (Hussain d13: 22.8% MMLU, 54.8% GPQA, 71.0% SimpleQA for a unanimous wrong group over 23 models; Hu & Qu d12: 66.5% no-source). No closed frontier flip-rate table found; HiddenBench (d01) tests 15 frontier models but on pooling, not flips. Structured judge effect not found beyond the earlier Yao result.
3. Minority Sentinel replication: OPEN, and the earlier description was wrong. Full read (d11): it is a LightGBM classifier on debate logs, not a verifier gate; +1.71% net gain; LLM judge -1.37%; no non-author replication. K20 rewritten.
4. Stasser & Titus 1985 and Lu 2012: Lu 2012 abstract numbers confirmed at snippet level (65 studies, 101 effects, 3,189 groups, about eight times; d17, opened false). Stasser & Titus 18%/83% NOT recovered (d18); do not cite. Added a verified modern human anchor, Faulmueller 2010: 1/15 (7%) hidden-profile groups vs 100% full-information (d16).
5. LLM hidden-profile benchmark: CLOSED. HiddenBench (d01-d04, ICML 2026): 65 tasks, 15 LLMs, 30.1% vs 80.7%. Follow-ups: Consilience (d07), CrossProfile (d08), Mansuri (d05-d06).
6. Optimal disagreement level transfers? CLOSED (negative). Best dissent share differs by model (d03); moderate dissent is not universal; agreement is largely a prompt property (d05). Needs per-model calibration or a conditional trigger.
7. Role-played vs authentic dissent for LLMs: OPEN. No LLM study separates the two; claim K32 records mixed model-dependent results.
8. Why reasoning vs knowledge tasks split: OPEN. Mansuri (d05) offers a partial mechanism (benchmarks differ in how much grounds there are to disagree; relation unclear on MuSiQue) but no task-type detector was found.
9. Independence before sharing: PARTLY CLOSED. No direct LLM test of commit-before-sharing, but indirect support: private-vs-stated answers diverge and gain depends on stating dissent (d05, d06), a noise placebo matches self-correction (d14), and the human individual-preference effect (d16). Still worth a direct test.
10. RLHF vs prompt framing for the 2026 yield: PARTLY CLOSED. Hu & Qu (d12) show a speaker-free floor of 66.5% with a repeated wrong answer, so much is in-context repetition rather than social framing. Base vs instruct models not separated; still open for training effect.

Caveats on new evidence: all are 2026 preprints, mostly unreviewed; the arXiv ids carry far-future numbering and were opened as PDFs this session. Open-weight small models dominate. HiddenBench dissent table was read from extracted text, so row labels are reconstructed.
