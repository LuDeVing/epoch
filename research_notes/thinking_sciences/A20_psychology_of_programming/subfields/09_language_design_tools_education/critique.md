# Critique A20.09 Language design, tools, education

## Corrections made (sources re-opened this session)
Re-opened arXiv full texts and checked: Kazemitabaar 2023 (80.1 vs 44.4, d=1.67; doc use 22.1 vs 54.3, d=1.33; syntax errors 0.87 vs 1.67; retention d=0.28 p=.262, d=0.41 p=.092), Peng 2023 (71.17 vs 160.89 min, 55.8%, CI 21-89%), METR 2025 (16 devs, 246 tasks, +19%, 136/110 split, 44% Cursor experience), Leinonen 2023 (67-100% comprehensible, correct explanation 11-83%, fix correct 33%, improvement 54%), Denny 2023 Copilot (79/166 = 47.6%, 53 fixed by rewording, 60.9%), Berger 2019 (148 projects, 27,450 duplicates = 1.86%, FP 36%), Perry 2023 (67% vs 79%, p=0.017), Shen and Tamkin 2026 (N=52, d=0.738, p=0.01, 4.15 of 27 points, task time p=0.391). All confirmed except:
1. c15: "about 50% vs 65% per web summary" is NOT in the paper. The paper states a 17% score reduction (4.15 points of 27). Treat the 50/65 split as unverified. 65% is the high-pattern floor, not the control mean.
2. c15: the paper also reports pilot values (task faster d=1.11, p=0.03; quiz d=1.7, p=0.003). Do not mix with main study d=0.738.
3. a14 vs c01: both Leinonen rows agree; the 11% figure is for explanation correctness, not fix correctness (fix 17-56% by message, 33% overall).
4. Kazemitabaar d=0.28 appears for two different measures (direct hints, retention authoring). Keep them separate.
Not re-checked (snippet or secondary only): Pritchard 2015, Savelka 2023, Sarsa 2022, SWE-agent ablations, Liffiton, CodeAid, Lehmann 2025, Liang 2024.

## Contradictions
- Productivity: Peng +55.8% faster (new task, recruited freelancers) vs METR 19% slower (experts in own repos). Not truly contradictory: task type, expertise, tooling differ. METR forecast of 24% faster also shows self-report is unreliable.
- Kazemitabaar: large training gains, no immediate post-test gain, weak retention trend. Shen and Tamkin finds an actual skill loss. Designs differ (age, tasks, no-AI tests); direction is mixed.
- Roles of variables: authors report 99% coverage by ten roles, one count 84%; exam effects mostly null.

## Weak spots
- The classic core named in the brief (Shneiderman 1980, Weinberg 1971/1998, Sajaniemi 2008 review) was never opened (a09, a10, a12); no exact numbers from them.
- Language-design usability studies (Stefik and Siebert 2013, Hanenberg 2010 static typing, Uesbeck 2016, Pea 1986) were not opened (b20-b23, a27). No numbers.
- Evidence is mostly 2022-2024 Codex-era models; newer models untested.
- Most claims are single-source; small N (20 to 69) is common.
- No LLM study tests language design itself (syntax, types) on the model; only the SWE-agent interface.
- Agent relevance is mostly background, per the brief.

## GAPS
1. What do Stefik and Siebert 2013, Hanenberg 2010 and Uesbeck 2016 report (exact effect sizes), and did any replicate?
2. Does the Kazemitabaar null immediate transfer replicate with 2025-26 models and larger N?
3. Does the skill-loss effect (Shen and Tamkin) replicate, and does an explain-first scaffold remove it?
4. Do Weinberg 1971/1998 and Shneiderman 1980 contain empirical numbers (not essays) that can be cited?
5. Do newer LLMs (2025-26) still fail at compiler error message fixes (33% correct) or at conceptual prompt classes?
6. Was roles of variables replicated outside the Finnish group (Python study, Nikula 2007), with effect sizes?
7. How does language choice (typed vs untyped, syntax) change LLM code-generation accuracy, with measured results?
8. Does the METR slowdown persist in a 2026 follow-up with later tools?
9. Which interface features (SWE-agent ablations) matter most at equal tokens?
10. Do guardrail leaks (full solutions despite instruction) drop with 2025-26 models?

## Gap search results
Sources opened this session: type-constrained decoding (arXiv 2504.09246), MultiPL-E (2208.08227), Shen and Tamkin (2601.20245, full text), Lehmann et al. (2409.09047), SWE-agent (2405.15793 text), Prather Widening Gap (2405.17739), Kuittinen and Sajaniemi PPIG 2003, METR blog listing. arXiv, Semantic Scholar and OpenAlex APIs returned 429 and the web search budget was exhausted, so searching was limited to direct page fetches.

1. OPEN. Stefik and Siebert, Hanenberg, Uesbeck: paywalled (403 / closed access). No numbers (d14, d15).
2. PARTLY CLOSED. No 2025-26 replication of Kazemitabaar found. Lehmann 2025 (Study 3 N=69) agrees with a null overall effect on learning; it uses Python novices and 2024 models. Larger-N replication still missing (d08).
3. OPEN. No replication of the skill-loss effect. Lehmann found no overall effect, so K02 is now contested. An explain-first scaffold is supported only by post hoc clusters in Shen and Tamkin: Conceptual Inquiry 65% (n=7), Generation-Then-Comprehension 86% (n=2), Hybrid 68% (n=3) vs Delegation 39% (n=4) (d05-d07).
4. OPEN. Weinberg and Shneiderman not available; keep as background, no numbers (d16).
5. OPEN. No 2025-26 test of error message repair found; only small open models in d02 (Gemma 2B repaired 33.5% and 25.8% unaided).
6. OPEN. No outside replication of roles of variables; the 2003 experiment (about 80 students) shows mostly small, mixed effects (d12).
7. PARTLY CLOSED. Codex-era: static typing has no overall effect (p=0.34, p=0.23); type annotations matter in TypeScript (-2.5% when set to Any). Type-constrained decoding: compile errors -75.3% and -52.1%, correctness +3.5 to 5.5% relative. No 2025-26 frontier model data (d01-d04).
8. OPEN. No METR follow-up found on the blog listing (d13). Absence is not proof.
9. PARTLY CLOSED. SWE-agent Table 3 gives per-component numbers (edit action -7.7, linting -3.0, summarized search +6.0 over iterative, 100-line viewer best), but not at equal tokens (d10).
10. OPEN. No 2025-26 guardrail leak data found (d17).

Status changes: K02 single-source to contested; evidence added to K01, K03, K04, K09, K11; new claims K16 to K18.
