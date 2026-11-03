# Cross-check: E12.03 Red teaming as alternative analysis

## Numbers re-opened this session (arXiv PDF text, 10 checked)
1. Huang 2024 (2310.01798) GPT-3.5: GSM8K 75.9 -> 75.1 (3 calls) -> 74.7 (5); CSQA 75.8 -> 38.1 -> 41.8; HotpotQA 26.0 -> 25.0. GPT-4 GSM8K 91.5 -> 89.0; CSQA 79.5 -> 80.0; HotpotQA 49.0 -> 43.0. Oracle GPT-4: 97.5 / 85.5 / 59.0. CONFIRMED. Note: a14 calls 38.1 "round 1"; the table counts calls (3 and 5), not rounds. Also 74.7% unchanged answers on GSM8K confirmed.
2. Tyen 2024 (2311.08516): 2186 traces, GPT-4 52.87 overall, multistep arithmetic backtracking +43.92 (true location) / -6.67 on correct traces, +20.39 random location. CONFIRMED. The random-location baseline also gains, so part of the gain is plain resampling (not stated in a16/b17).
3. Du 2023 (2305.14325): arithmetic 67.0 / 72.1 / 81.8, GSM8K 77.0 / 75.0 / 85.0, chess 91.4 / 102.1 / 122.9, MMLU 71.1 to 74.2 with mixed agents. CONFIRMED.
4. Liang 2023 (2305.19118): 26.0, 29.5, 27.5, MAD 37.0. CONFIRMED.
5. Sharma 2024 (2310.13548): "Claude 1.3 wrongly admits mistakes on 98% of questions"; admit range 42% (GPT-4) to 98%. CORRECTION: the 27 percent drop under "Are you sure?" is Claude 1.3; the 27 percent drop under a user-suggested wrong answer is LLaMA 2. Evidence a24 only reports the second; b10 blends them. Fixed in claim K08.
6. Khan 2024 (2402.06782): 76 / 88 vs 48 / 60. CONFIRMED.
7. Wang 2024 anticipatory reflection (2405.16334): 23.5 / 22.7 / 19.8, 45 percent fewer plan revisions, +3.5 points. CONFIRMED. The 3.5 is described as percent in the text, and may be points; treat as small.
8. Perez 2022 (2202.03286): 3.7 percent, 18,444, over 40 percent, "invisible". CONFIRMED (the 78 percent figure was not re-grepped).
9. Smit 2024 (2311.17371): 376 USMLE questions and the 90 percent agreement setting present. Exact +15 percent not re-located; kept as reported.
10. Zhang 2025 (2502.08788): Society of Mind below CoT on all nine sets (GPT-4o-mini); ChatEval/AgentVerse above on one of nine; Claude-3.5-haiku MMLU +0.85 / at least -3.60; about 15 percent of cases. CONFIRMED.

## Contradictions between sources
- Debate: Du and Liang report gains; Huang (full GSM8K), Smit, Wang, Zhang report none against equal-compute baselines. Counted as contested (K06), not refuted: the baselines differ and Du used its own setup.
- Self-critique: Huang/Kamoi say it fails; Bohnet 2025 (b15) shows 49.8 -> 89.3 on Blocksworld without a verifier. Plausible reconciliation: structured, rule-checkable tasks versus open reasoning. Not tested.
- Smit (b06) says Multi-Persona was worse on medical sets but best with 90 percent agreement; c07 says it was 7 percent below Medprompt. Same paper, different settings; the moderator is agreement level.
- Nemeth: a10 (from memory) and b26 (secondary source) agree in direction, but neither read the paper.
- Team B: Garthoff vs Pipes disagree on whether core intent was right.

## Weak spots
- The military core (UFMCS handbook, ADSO, DSB 2003, Ipcha Mistabra) was never opened. a27 and a28 are unopened; Ipcha Mistabra is linked to 1973 only via a Wikipedia page that, for Agranat, does not mention it.
- Classic human-effect evidence (Schwenk 1990 meta-analysis, Schweiger 1986, Nemeth 2001, Mitchell 1989, Lord 1984, Herzog and Hertwig 2009) was NOT read; a08-a11 and b25-b29 are from memory or snippets. Do not cite effect sizes from them.
- Several "established" claims rest on one family of LLMs (GPT-3.5/4, early Claude); newer reasoning models may self-verify better.
- Tyen: random-location gain shows resampling confound.
- Lee 2025 "Amplifying Minority Voices" (c21) seen only in a snippet.
- Counts of "independent sources" for K01 treat Huang, Kamoi, and Zhang as independent; Kamoi partly summarises Huang.
- Wynn 2025 deltas were read only from figures.

## GAPS
1. Does a challenger from a different model family, given equal tokens, beat a same-model challenger and plain majority vote on our own tasks?
2. Does a code- or retrieval-located flaw plus fix (Tyen-style) beat model-located self-critique at equal tokens, once the random-location resampling control is included?
3. Do reasoning-trained models (2025-2026) still lose accuracy under intrinsic self-critique, or has Huang 2024 been overturned for them?
4. What are the real numbers in Schwenk 1990 (number of studies, pooled effects) and Nemeth 2001, and do any LLM studies replicate "authentic dissent beats assigned dissent"?
5. What does the UFMCS Red Team Handbook actually list as tools, and which have any measured effect (Ipcha Mistabra outcomes, ADSO assessments)?
6. Does a pre-mortem or anticipatory-reflection step improve planning accuracy beyond resampling, and when should a gate trigger it?
7. Does challenge wording ("are you sure?" vs a neutral evidence request) change flip rates enough to design the challenge slot around it?
8. Does the Bohnet 2025 structured-planning gain (no verifier) hold on tasks beyond Blocksworld and Logistics, and what separates those from Huang's open tasks?
9. What is the optimal disagreement intensity for a challenger by task type (Smit moderator), and can it be set from a cheap signal?
10. Are there LLM-based tests of Team A/Team B versus a single devil's advocate on forecasting tasks (e.g. against Good Judgment style questions)?

## Gap search results (evidence_d.jsonl, d01-d17)
Searches: the WebSearch budget was exhausted when this step began, so discovery used arXiv's own listing pages; PDFs were read with pdftotext. Semantic Scholar and OpenAlex returned HTTP 429.

1. CLOSED for small open models, OPEN for frontier. Ferreira 2026 (d03): mixed-model debate loses to a vote over its own roster by 1.04 pp [-1.61,-0.52] at equal generations; cross-family helps as extra votes, not as debaters. Ringelmann (d04): heterogeneous teams lower the correlation ceiling (c 0.85 to 0.54). Not tested: a frontier different-family challenger on our own tasks.
2. PARTLY CLOSED. Hu 2026 (d06): test-located checks give +8.14 pp (public tests) and +2.70 pp (generated tests) with near-zero harm vs LLM selector 4.69% harm. No new paper redoes Tyen's located-flaw fix against self-critique at equal tokens; the Tyen random-location control (+20.39) stays the only one.
3. CLOSED, claim revised. Tsui 2026 (d01): reasoning models show a small or negative self-correction blind spot; non-reasoning models 64.5%. Stav 2026 (d05): 2025-26 models gain on verifiable tasks (SAT 65.66% of errors removed) and still lose on low-verifiability ones (C2W up to 13.25%). K01 moved from established to contested.
4. OPEN. Schwenk 1990 and Nemeth 2001 returned HTTP 403 (d15, d16). No LLM test of authentic vs assigned dissent found; nearest proxies d03, d13.
5. OPEN. Seven handbook URLs failed (d17). No new outcome data on Ipcha Mistabra or ADSO.
6. PARTLY CLOSED. InvThink (d12) shows a failure-first step beats safety prompts at matched budget, for harm only. Planning-accuracy gain beyond resampling remains untested.
7. CLOSED. Yang 2026 (d07): plain repetition 15.0% adoption, fallacy 12.9%, emotion 13.2%; task verifiability explains R2 0.485 vs pressure tactic 0.009; 84.0% of concessions follow the first push; max reasoning takes adoption on deep puzzles to 0%. Huang 2026 (d08): wording class does change which model flips, so tests need matched no-challenge controls. Not isolated: neutral evidence request vs Are-you-sure as separate arms.
8. PARTLY CLOSED. Stav 2026 (d05) extends beyond Blocksworld: gains track verifiability (Spearman 0.65) and reasoning load (0.54). Bohnet-style no-verifier gains were not re-tested.
9. OPEN. Choi 2025 (d02) shows debate is a martingale unless biased toward correction (vanilla 0.7332 vs oracle 0.8236 at T=2). No cheap signal for setting intensity was found.
10. OPEN. No LLM Team A/Team B vs devil's advocate forecasting study found by arXiv listing queries.

Caveat: all new evidence is 2025-26 preprints, several by single authors, on small open models; none peer-reviewed as far as seen. Numbers for d08, d09, d11 are from abstracts only.
