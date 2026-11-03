# A19.02 Dialectical reasoning: cross-check critique

## Numbers re-opened this session (full text in D:/research_scratch/A19.02/)
Confirmed against the source text:
1. Peng and Nisbett 1999: F(1,109)=12.45; F(1,64)=9.17; mother-daughter 72% vs 26%, chi2=13.61; school-fun chi2=8.50; M 2.22 vs 1.56, t=2.53; N 102 + 136, F(1,237)=7.90. All match a02-a06, b01-b04.
2. Jin et al. 2023 table: AHS 5.35/5.01 vs 4.87; DSS 4.59 and 3.97 (p=.344) vs 4.00; SCS-Ind 6.98/5.32 vs 4.73. Match a26, b18, c01, c02.
3. Sun and Wang 2025: p=.917 on expectation of change (a28 wrote p=.91, c05 wrote .917; .917 is right); mean origin effect 0.0897 vs -0.0437, p=.4826; knowledge vs reasoning d=0.097, p=.0248. Match.
4. Huang et al. 2024 Table 2: GPT-3.5 75.9 -> 95.5 and GPT-4 84.3 -> 97.5 on GSM8K with oracle labels; GPT-4 CommonSenseQA 89.7 -> 85.5.
5. Du et al.: arithmetic 67.0 / 72.1 / 69.0 / 81.8; GSM8K 77.0 / 75.0 / 81.0 / 85.0. Match c18.
6. Abbasloo 2026: GPT-5 pS 82.0, OC 81.4; GPT-5-nano pS 84.4, OC 15.5; GPT-5-chat -40.2. Match.
7. Many Labs 2: N=7,396, t=37.05, d=0.86; 125 samples, 15,305 participants. Match.
8. Atari et al.: r=-.70, 94,278 respondents, 65 nations, rho=-.72. Match.
9. Candussio: overall means 27.8/33.6/21.7/18.3/35.4; WikiHop vs CoT +11.6/+10.6/+15.6. Match.
10. SycEval 58.19/43.52/14.66/78.5; Kim and Khashabi 56.1% and 84.5%. Match.

## Corrections
- c20 says "With oracle labels GPT-4 GSM8K goes 95.5 to 97.5". Wrong. 95.5 is GPT-3.5 with oracle (from 75.9); GPT-4 goes 84.3 to 97.5. c25 is correct. Claims use c25.
- b11 says "14 (50%) at p<.0001". Many Labs 2 abstract: 15 of 28 (54%) significant, same direction (p<.05); the results text: 14 of 28 (50%) significant, same direction, 1 weakly consistent. Treat as 14-15 of 28; the "p<.0001" label in b11 could not be matched.
- a28 "p=.91" is p=.917.
- Sun and Wang report "3 of 8 models sensitive" in one analysis and "2/8" in another (different experiments); not a contradiction but easy to mix.

## Contradictions between sources
- Jin et al. (2023) say GPT models are more holistic than humans; Sun and Wang (2025) show cultural tendencies in LLMs collapse with larger item sets and temperature 0. Different models and item counts (4-21 vs 30-60), so the 2023 result should be treated as fragile.
- Hu et al. 2026 find reversed human patterns (Chinese model more individual and collective); Jin find models more holistic overall. No common effect.
- Mixed emotion: Williams and Aaker 2002 (Asian Americans less uncomfortable) vs Zheng et al. 2021 (no culture effect on mixed emotion; discomfort direction depends on valence).
- Debate: Du et al. report large debate gains; Huang et al. say gains largely match self-consistency at equal calls. Not settled for equal tokens.
- Antithesis prompting: Candussio shows big gains for small models, but with CoT some synthesis steps lowered accuracy; Abbasloo shows synthesis drops of 20-40 points on MMLU. Net effect depends on model and task.

## Weak spots
- No large replication of the 1999 contradiction studies was found; ML2 replicated a different effect (Norenzayan 2002). The 1999 N per cell is 32-136.
- Dialecticism subfacets barely correlate (r .06-.15), so "dialectical" is several constructs.
- Morio (2022) tolerance-for-contradiction scale had alpha .50 in Japan.
- The links to our agent (S7) are by analogy: no study tested "hold two rules until a counterexample decides" in an LLM.
- Antithesis/debate benchmarks use accuracy tasks with one right answer, not situations where both rules are partly true, which is what Peng and Nisbett's dialectical compromise is about.
- Self-correction needs an external signal (Huang): S7 must define what the counterexample is and who supplies it.
- Sycophancy shows models flip under casual challenge, so keeping two rules alive could collapse on pushback.

## Only seen in snippets or abstracts (not read as full text)
a15 (Ji, Nisbett, Su 2001), a16 (Choi and Nisbett 2000), a17 (Spencer-Rodgers 2004), a18, a23 (Ng thesis tables), b09 (Leu et al. 2010 Ns), b16 (Johnson-Laird and Lee 2006), b17 (Majima), b25 (priming studies), c04 (Lu, Song, Zhang 2025 details), the 2026 meta-analysis a22 beyond its abstract-level numbers. Numbers from the 2010 review (a10-a14, a19, a20) are second-hand citations.

## GAPS (most decision-relevant first)
1. Does an S7 step that keeps two candidate rules alive until a counterexample appears beat plain CoT and self-consistency at equal tokens on our agent, on items where the answer is one of the two rules? Nobody has tested this exact design.
2. What counts as the counterexample in S7 (tool run, retrieved fact, test case) and how much of Huang's oracle gain (84.3 to 97.5 on GSM8K) can a realistic checker recover?
3. Does the antithesis gain (Candussio, Abdali) hold for strong models at equal token budget? Gains were largest for small models and shrank over CoT.
4. How often does a model drop the held-open second rule under casual pushback (sycophancy 58%), and does an S7 guardrail reduce flips to wrong answers?
5. Is there a replication of Peng and Nisbett 1999 with N>=300 per culture and non-student samples, and what is the effect on the contradiction-plausibility task (F(1,237)=7.90)?
6. Which dialectical subfacet (expectation of change vs tolerance of contradiction) maps to which agent operator, given weak correlations between them?
7. Do Jin's 2023 LLM holism results survive a 30-60 item, two-language rerun with current models (Sun and Wang tested other tasks, not the Dialectical Self Scale)?
8. Does tolerance of contradiction hurt on single-answer tasks (creativity result in non-art majors, N=489; synthesis drops on MMLU)? When should S7 commit to one rule?
9. For debate versus self-consistency at equal tokens, does the benefit survive on tasks with partly true competing rules?

## Gap search results (evidence_d.jsonl d01-d19; claims K21-K27 added)
1. S7 vs CoT and self-consistency at equal tokens on two-rule items: STILL OPEN. Nearest test is Qiu et al. 2024 (d14): GPT-4 ACRE task accuracy 28.0 IO, 29.0 SC, 59.0 with candidate rules filtered by a symbolic checker. No test of the partly-true case.
2. What counts as the counterexample: PARTLY CLOSED. A tool run or test case works. CRITIC (d11): +5.7 of +11.4 oracle points on GSM8k (ChatGPT), +16 of +32.3 on TabMWP (70B). Without the tool, +4.5 or even -1.8. Kamoi survey (d12): no robust self-correction without reliable external feedback. Realistic checker = roughly a third to a half of the oracle gain.
3. Antithesis gain for strong models at equal tokens: CLOSED NEGATIVE (not shown). Candussio used only small open models (d16); debate papers show no gain for GPT-4o-mini or Claude-3.5-haiku over CoT (d04).
4. Dropping the second rule under pushback: PARTLY CLOSED. SYCON-Bench (d08): o3-mini holds 4.97 of 5 turns, Qwen2.5-7B 0.83; third-person prompt up to +63.8% turns held. Critic gate cut Claude Sonnet 4 sycophancy 9.6% to 1.4% (d09, single author). Whether the held stance was correct is not measured.
5. Replication of Peng and Nisbett 1999 with N>=300: STILL OPEN, and a failed replication was found. Friedman, Chen and Vaid 2006 (d01) found no culture difference in dialectical proverb preference; poeticality and familiarity differed. K01 now "contested". N unknown (abstract only). No replication of the contradiction-plausibility task (F(1,237)=7.90) found.
6. Which subfacet maps to which operator: PARTLY CLOSED by argument, not data. The 2026 meta-analysis (d02) ties country means to both tolerance of contradiction and expectation of change and finds no link to collectivism. Working mapping: tolerance of contradiction = S7 hold-two-rules; expectation of change = revisit a committed rule when new evidence arrives (d10 shows early commitment halves scores). Subfacet-to-operator testing has not been done.
7. Jin et al. 2023 rerun with 30-60 items: STILL OPEN. Two web searches and a PubMed search found none; arXiv API was down for later queries (d19).
8. Does tolerance hurt on single-answer tasks / when to commit: PARTLY CLOSED. Early commitment hurts when evidence is still arriving (d10: 30.9 vs 64.4). Debate and synthesis lose to voting or CoT on single-answer sets (d03, d04, d06). Rule: stay open only while a checker can still produce a deciding case; otherwise commit by vote.
9. Debate vs self-consistency at equal budget on partly-true tasks: PARTLY CLOSED. Single-answer tasks: debate loses to SC (d04: wins in about 15% of 36 configs; d06 vote 0.7691 vs debate 0.7377 on Qwen2.5-7B). Partly-true tasks: no study found.

Net change: S7 should use a different-source second rule plus an external counterexample, defer commitment, and add a neutral-reviewer wording for pushback. The human effect (K01) is weaker than the first pass assumed.
Not opened in full text: d01, d02, d18 (abstract or PubMed record only), d07 (abstract and intro).
