# Critique and cross-check: Targeted memory reactivation (B04.04)

## Corrections made (sources re-opened this session)
Re-checked against full text or abstract: Hu 2020 (PMC7144680, full text), Sleep-time Compute (arXiv 2504.13171, abstract), Behrouz 2026 (arXiv 2606.03979, tables), Hoffman 2024 (PMC11868201), Wick and Rasch 2023 (PMC10547374), Henin 2019 (PMC6831893).

Confirmed exactly: overall g=0.29 [0.21,0.38], 91 experiments, 212 effect sizes, N=2004; stage table (SWS 0.27, N2 0.32, REM -0.06, wake 0.07, unspecified 0.26, Q(4)=10.744, p=.030); learning type (declarative 0.23, skill 0.44, conditioning -0.03 on 4 experiments N=91, others 0.38); outcomes (recall 0.24, recognition 0.18, performance 0.40, SCR -0.08, subjective 0.11); three-parameter model g=0.13 [0.06,0.21]; Rasch 2007 Exp 1 spatial g=0.69 [0.19,1.18], Exp 3 REM g=-0.05; sleep-time compute 5x, +13%, +18%; Sleep paper table (Qwen3-8B AIME-24 Sleep 79.2, GRPO 76.4, SFT 75.5, ARC-style 80% vs SEAL 72.5); Hoffman abstract (disrupted in Exp 1, unaffected in Exps 2-3); Wick and Rasch (no overall cued benefit, N=34); Henin (N=12 and N=19, no behavioural effect).

Corrections and refinements:
1. a06 says "published effects are larger than unpublished". Hu reports the difference is NOT significant (Q(1)=1.005, p=.316). Treat it as a trend only. Added trim-and-fill g=0.18 [0.06,0.30] (17 imputed effects), which a06 omitted.
2. a06 selection-model list: Hu gives 0.17 for severe two-tailed and 0.15 for moderate one-tailed; the 0.21 figure could not be matched to a labelled scenario. Do not quote a per-scenario mapping.
3. a02 "wake cues were mostly not EEG-checked" and "REM only 7 experiments": REM is 7 experiments (N=142), wake 18 experiments (N=366). Hu groups "unspecified" (k=6) as cueing not supervised by EEG. Wake and unspecified are separate rows.
4. a08 (Rudoy 2009): the primary paper gives t(11)=2.6, but Hu's table gives g=0.48 [-0.08,1.04], p=.095 for the same study. The meta-analytic conversion is more conservative. Quote both; do not call Rudoy "strong".
5. a16 (Henin 2019) is typed "replication", but it tests closed-loop acoustic stimulation (nonspecific), not item-cued TMR. It is a failed replication of the Ngo 2013 design, not of Rasch or Rudoy.
6. a22 omits OPSD (76.6) as the strongest baseline on Qwen3-8B AIME-24; the margin over the best baseline is 2.6 points, not 2.8 over GRPO. Single run per cell as far as the tables show; no variance reported in what we saw.
7. a24/c13/c14 describe one dataset (Shin et al. 2025, arXiv 2511.15013), counted as one independent source in the claims.
8. a22 and c07 are the same paper; counted once.

## Contradictions between sources
- Hu 2020 pooled effect is positive and reliable, yet the 2022-2026 single studies (Wick and Rasch, SleepStim, face-name, theta-tACS, once vs five-times, odor 2026) mostly find no overall cued benefit. Both can be true if the true effect is near 0.13-0.2 and most studies are underpowered (mean N=22). The meta-analysis needs updating.
- Hoffman 2024 says awake cueing is null or harmful; Hu's wake g=0.07 agrees on null but not on harm. Harm appeared in one experiment of three.
- N2 vs SWS: Hu pools N2 higher (0.32) than SWS (0.27) with a wide CI; Wick and Rasch and the 2024 Sci Rep study find no difference. Consistent: stage within NREM is not decisive.
- Fear: human pooled null vs mouse NREM cueing weakening fear (Purple 2017) vs positive odor-extinction (Hauner 2013). Sign differs by species and paradigm.
- Emotion: some studies say emotional items gain more, others find only RT effects, and a 2025 study finds REM cueing impairs them.

## Weak spots
- Most TMR studies have N between 12 and 40. Many positives come from within-subject designs with 25-50 items.
- The meta-analysis stops in 2019-2020; later nulls are not pooled.
- Only one LLM-side study (Sleep-time Compute) is plainly an "idle pre-computation" test; Behrouz 2026, Lee 2026 and SleepGate change weights or caches and are not scaffold methods. None is TMR. The mapping to TMR is by analogy.
- SleepGate and SCM use tiny models and 22 questions; results are likely to be fragile and single-lab.
- Sleep-time compute was measured on modified, stateful variants of GSM-Symbolic and AIME that the authors built; they are favourable to pre-computation, and the paper itself shows the baseline wins at high test-time budgets.

## Only seen in snippets or not opened
b01, b02, b03, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26 (opened:false); c16, c17, c18, c19. Claims K04, K08, K10, K16, K17, K18 and K26 lean partly on these. Rasch 2007 primary text was never opened; its numbers come from Hu's table. a11 numbers not extracted. b13 participant count missing.

## GAPS (most decision-relevant first)
1. Does any experiment cue an LLM with an external token tied to a stored item and show item-specific recall gains at equal total tokens? (We found none; the design must be built.)
2. What is the effect of a replay pass done in a separate, isolated step versus the same re-presentation during active task work (the LLM analogue of NREM vs wake), measured at equal tokens?
3. Does replaying only low-confidence or failed items beat replaying all items in an agent loop (the weak-memory moderator)?
4. What is the cost to non-replayed neighbouring items (the interference prediction of Lu 2024 and feature-differentiation result of 2024), and does it appear in an LLM?
5. What is the updated pooled TMR effect after adding 2020-2026 studies, including nulls and preregistered multi-lab studies?
6. Does dose adapted to difficulty (Shin 2025) replicate outside one lab, and what is the equivalent compute-matched test?
7. For sleep-time compute, at what query predictability and test-time budget does the benefit vanish, and does that match the TMR weak-memory pattern?
8. Is the human conditioning null (4 experiments, N=91) real or just underpowered, and does the mouse NREM weakening replicate in humans?
9. Do the sleep-inspired weight-update methods (Sleep, SRC, WSCL) keep their gains against strong rehearsal baselines with reported variance?

## Gap search results (2026-11-19)
Method note: web search budget was exhausted, and the arXiv, OpenAlex and Semantic Scholar search APIs were rate-limited or empty. Evidence came from PubMed (title list plus NCBI efetch abstracts), the Semantic Scholar citation list of Sleep-time Compute, and full PDFs of IdleSpec, Auto-Dreamer, Studying Without a Syllabus, Zou 2026, ProAct and Librarian Agents. Evidence is in evidence_d.jsonl (d01-d26). Human papers are abstract-level only.

1. Cue-tied external token, item-specific recall at equal tokens: STILL OPEN. None of 49 citers of Sleep-time Compute tests it by title (d26). The design must be built.
2. Isolated replay vs in-task replay at equal tokens: STILL OPEN. Nearest: Zou 2026 shows a separate nightly rewrite gives 71 vs 0 multi-session recall versus no rewrite, but there is no in-task comparison (d22). Study-budget plateau (d20) is partial.
3. Replay only low-confidence items: PARTLY CLOSED on the human side, open for LLMs. Two 2026 studies find cue effects only for weakly encoded items (d06, d07), but difficult-to-learn words got no benefit (d05, N=22). Conclusion: replay needs a minimal trace; the very weakest items may not gain.
4. Cost to neighbours: PARTLY CLOSED on the human side. Stacked odour cues cancelled benefit (d07), cueing may spread across a context (d06), a competing positive memory weakened an aversive one (d03), and week-old memories resisted harm from disrupting cues (d10). No LLM test found.
5. Updated pooled TMR effect: STILL OPEN. PubMed shows no meta-analysis after Hu 2020 (d18). Title scan finds at least five 2024-2026 nulls or encoding-strength-only results against about six positives, mostly N 16-80 (K31).
6. Shin 2025 replication: STILL OPEN. Now published in NPJ Sci Learn (d14), but no independent replication found, and d05 gives a difficulty counter-result.
7. Sleep-time compute vs predictability and budget: PARTLY CLOSED. IdleSpec shows it falls to or below vanilla when observations are uncertain (Qwen3.5-4B 33.2 to 29.4, Gemini-2.5-Flash 50.5 to 50.1; row mapping from a garbled table) (d19). ProAct's gains come on predictable need chains (d23). More study budget did not reliably help (d20). Still missing: a single paper that sweeps predictability and budget together.
8. Conditioning null and mouse weakening: PARTLY CLOSED. Mouse sign depends on NREM substage: non-slow-wave cueing weakened, SWS cueing strengthened fear (d01). Human PTSD and interference studies are positive but small (d02, d03). The human conditioning pooled null is not re-tested.
9. Sleep, SRC, WSCL vs strong rehearsal baselines with variance: STILL OPEN. Behrouz 2026 shows no variance by text search (d25). Auto-Dreamer also reports point estimates only (d21).

Claims changed: K04, K10, K11, K14 (evidence added, text refined); K03, K12, K16, K17, K18, K20, K21, K02 (evidence added). New claims K27 to K32. No status was upgraded; K31 is marked contested.
