# Cross-check: Wason selection task and hypothesis testing

Checker re-opened the PDFs behind the main numbers (Wason 1960, Oaksford and Chater 1994 and 2003, Dasgupta 2022, Jhaveri 2026, Bertolazzi 2026, Banatt 2024, Abe 2026) and the Gale and Ball 2006 abstract. The Branchini 2025 paper (Springer) could not be fetched here, so its numbers were not re-checked.

## Numbers re-checked (confirmed unless noted)

1. Wason 1960: 6 of 29 correct with no wrong rule, 13 one wrong, 9 two or more, 45 minute cap. Confirmed. (The 1 who never announced is implied by 29 - 28; fine.)
2. Oaksford and Chater 1994: 845 subjects, card totals p 754, q 522, not-q 215, not-p 137, rho(16) = .92. Confirmed.
3. Oaksford and Chater 2003: G2(68) = 88.37, mean P(p) = .22 (SE .019), P(q) = .27, G2(12) = 16.07 and 13.68. Confirmed.
4. Dasgupta 2022: realistic advantage z > 2.2, p < .03 for four systems; z about 1.78, p about .08 for two; slowest 15% over 80 s; response time z = 4.44. Confirmed. Note: b15 and c11/c12 are the same paper (arXiv 2207.07051 and its journal version), so they are ONE source.
5. Jhaveri 2026: 6% to 78%; Gemini baseline 0.73; Llama-3.3-70B 0.212 to 0.375 with TiO; 42% to 56% in the abstract; 80 episodes per point. Confirmed.
6. Bertolazzi 2026: 75%, 68%, 41%, rho -0.779 (p = .003), rho -0.937, 59.2%, 18.0%. Confirmed.
7. Banatt WILT: 14/50 Claude 3.5 Sonnet, 28% best, o1-preview 12.1 guesses, 0.06 repeats, GPT-4o-mini 9.78 repeats. Confirmed.
8. Abe 2026: gpt-oss-120b 100.0 zero-shot (+30), qwen3-14b 97.5 (+45), gpt-oss-20b 67.5 and 91.2, gemma3-12b 58.8/78.7/43.8, llama-3.3-70b 62.5/78.7/83.8, CoT n/a for reasoning models. Confirmed. Correction: c14 lists qwen3-32b as 98.8 (+38.8) zero-shot; the PDF table row also shows 100.0 (+25) few-shot. Consistent.
9. Gale and Ball 2006: abstract says about 20% for the standard task and over 60% for dual goal. Now confirmed from the abstract (a26 can be marked opened). The 75% / 20% / 34% contrast figures (b24, b35) are still second-hand via Branchini.
10. Correction to c03 and A01.02-K11: the paper's text says Think-in-Opposites "improves task success in all" settings, but the table (Table 12) shows Qwen3-8B non-thinking at 0.062 baseline and 0.062 with TiO (no gain), and Dual-Goal lowers Qwen3-14B (0.225 to 0.125), Qwen3-32B (0.325 to 0.100) and slightly Llama (0.212 to 0.200). The text itself says non-thinking effects are "small improvement for TiO and small drop for Dual-Goal" with no significant I:C change. Treat "all 11" as "non-negative in all 11".
11. Correction to c03 evidence: a10 says Dual-Goal numbers for Qwen3-14B non-thinking "0.23 to 0.13": matches table (0.225 to 0.125).
12. Minor: Jhaveri cites WILT as "at best 26%" while WILT's own abstract says 28%. Use 28%.

## Contradictions between sources

- Content effect: Cosmides reports 70 to 80% on social contracts vs 20 to 25% controls. Fiddick's replication finds 45% vs 15% to 25%, with the deontic condition not above matched controls. Effect exists; size and cause differ.
- Is the information-gain model right? Oaksford and Chater fit 34 studies; Ragni et al. (228 experiments) say selections are dependent and nine theories including information gain fail to predict it. Both sides are the authors of their own models; Kellen and Klauer (not read) say Ragni's comparison is not identifiable.
- LLM social-rule advantage: Dasgupta finds human-like content effects; Seals and Shalin find the social-rule status effect not significant and LLMs far below humans (about 30% vs 70% on social rules). Different models and scoring (option likelihood vs forced two cards).
- Positive-test strategy as a "bias": Wason read it as a wish to verify; Klayman and Ha read it as a heuristic whose cost depends on base rates. LLM data (Bertolazzi, rho -0.78 with success) support "positive testing hurts when H is narrower than truth", but Bertolazzi also finds failed games drift into disjoint hypotheses, so confirmation is not the whole story.
- Matching bias vs confirmation bias in LLMs (Abe) is one study only.

## Weak spots

- Many "established" LLM results are correlations (I:C vs success, positive-test share vs success), not interventions. Only Jhaveri's TiO/Dual-Goal prompt runs and Branchini's human training are causal.
- Single-model-as-oracle designs (Bertolazzi, WordNet taxa) and small hidden-rule sets (WILT: 50 rules) limit generality. None tests a scaffold at equal tokens against a plain model; Jhaveri gives turn counts and tokens per turn but not matched-budget comparisons.
- Dependence/redundancy claims (A01.02-K05) rest on the proponents of the model theory. Treated as contested.
- Pooled effect sizes are almost absent. The meta-analyses give pattern frequencies, not effect sizes.
- The 2-4-6 task and selection task are one-shot or short; no evidence here about longer multi-hypothesis discovery with a code oracle like our harness.
- Several 2026 arXiv preprints are not peer reviewed (Jhaveri, Bertolazzi, Abe is EACL short paper).

## Seen only in snippets or second-hand (opened:false or approximate)

- a19 Cheng and Holyoak 1985, a28 Evans and Lynch 1973, a29 Evans and Over 1996, a27 Ragni 2018 (only the 2020 reply was read), b33 Griggs and Cox 1982, b34 Cheng et al. 1986, b35 Gale and Ball 2009/2012 contrast figures, c17 Macmillan-Scott and Musolesi (press report; the 90% GPT-4 vs 0% GPT-3.5 figure is unverified).
- b25 Osman tutoring percentages were read from a garbled table.
- c04 Blicket correlations come from figure labels.
- Branchini 2025 numbers (b22, b23): not re-fetched by the checker.
- Duplicates: b15/c11/c12 (Dasgupta) and b21/c13 (Seals and Shalin) are single sources each; a15/a21 quote Stanovich and West and Sperber second-hand. Counts in claims.jsonl treat them as one.

## GAPS

1. Does forcing at least one hypothesis-failing test (an S4 rule enforced by code) raise success for our agent at equal tokens, for both thinking and non-thinking models? Jhaveri shows prompts help thinking models only; nobody tested code enforcement.
2. Is the TiO / contrast gain still there when the agent's token budget is matched (TiO changed tokens per turn, up to about 2x for some models)?
3. Does separating test proposal from rule inference (A01.02-K12) help on a single model, or is the WILT gain from using a stronger tester model? Needs an own-model-both-roles control.
4. Can expected information gain over an explicit hypothesis set be computed cheaply enough in code on our task classes, and how much of the +37 point 20 Questions gain survives when the hypothesis set is generated by the same model?
5. How often is a revised hypothesis only a rewording (Wason 1960 pattern) for current LLMs, and does a code check on prediction change (G2/S5) reduce it?
6. Do content/concrete re-expressions (O6) help LLMs on abstract rules, given the conflicting results on social-rule advantages (Dasgupta vs Seals and Shalin)?
7. Does longer chain of thought hurt or help falsification? Abe shows it hurt gemma3-12b and helped llama-3.3-70b; no controlled test on rule discovery.
8. What is the size of the human debiasing effect outside Italian student samples (Branchini N = 180), and has anyone replicated thinking-in-opposites or the original Rossi et al. 2001 finding?
9. Do the Ragni dependence results (selections are not independent) predict anything useful for sampling several independent attempts (G4)?
10. Which of the LLM results survive when the oracle is a programmatic rule and the task is not a number triple (e.g. grid transformation rules, ARC-like)?

## Gap search results

Evidence added: evidence_d.jsonl (d01 to d21; 15 opened, 6 snippet only). Claims: A01.02-K11, A01.02-K12, A01.02-K15, A01.02-K07, A01.02-K10, A01.02-K14 updated; A01.02-K20 to A01.02-K25 added.

Correction to A01.02-K11: Think-in-Opposites raised success significantly for non-thinking models too (+0.063, p = 0.0033); only the share of falsifying tests did not change for them. Dual-Goal hurt non-thinking models (-0.060). Branchini 2025 numbers are now confirmed from the paper (N = 180; 78.33, 38.33, 36.66 percent).

| Gap | Status | What was found |
|---|---|---|
| 1 Code-enforced falsifying test at equal tokens | OPEN | No study compares code-enforced and prompt-only falsification (d20). FalsifyBench and Jhaveri are correlational or prompt-based (d12, d01). Must be run in our harness. |
| 2 TiO gain at matched tokens | OPEN, partly informed | No matched-budget run. Thinking-model tokens per turn rose about 12 to 58 percent (d02). Success cells in the table text are garbled, so whether the gain survives at about +12 percent tokens is unconfirmed. |
| 3 Role split on one model | PARTLY CLOSED | WILT text says o1-mini did worse with its own tests than with another model's (d03); gain looks like a stronger-tester effect. The own-model number is only in a figure. A same-model split at matched tokens is untested. |
| 4 EIG over a self-generated hypothesis set | PARTLY CLOSED | With the same LLM generating hypotheses, EIG was no better than random on easy rules and failed on hard ones; it helped where falsification was needed (d05). The +37 point 20 Questions result is not decomposed. Use EIG as a tie-break, keep the set fresh. |
| 5 Rewording revisions | OPEN | Not measured for LLMs. Measurable pieces exist (d04, d12, d16). Refinement rarely fixes wrong ideas (4.3 percent, d13). Proposed code check: same predictions on held-out inputs means rejected. |
| 6 Concrete re-expression (O6) | OPEN | Only content-effect studies exist; no re-expression intervention (d19, d09). Dasgupta vs Seals and Shalin conflict not resolved. |
| 7 CoT length and falsification | OPEN, mixed evidence | CoT helped some models and hurt others on Wason (d09, gemma3-12b 58.8 to 43.8; llama-3.3-70b 62.5 to 83.8); hurt induction in other tasks (d10, d11). No rule-discovery test. See A01.02-K20. |
| 8 Human debiasing outside Italian students | OPEN | Numbers confirmed (d07) but no independent replication found. Country not stated in the paper. Rossi 2001 and Gale and Ball only second-hand (d08). |
| 9 Ragni dependence and G4 | OPEN, no transfer found | Result concerns one person's card choices, and is disputed (d18). No link to independent resampling. Measure sample correlation in our harness. |
| 10 Programmatic oracle, non-number task | PARTLY CLOSED | ARC-AGI-1 evidence (d14) and list-function induction (d13): hypothesis generation is the bottleneck; independent exploration plus re-exploration helped (not token-matched). No falsifying-probe test on ARC. See A01.02-K21, A01.02-K22. |

Still unverified after this search: Macmillan-Scott and Musolesi Wason figures (90 percent vs 0 percent; paper text has them only in a figure, d17), Rossi 2001 and Gale and Ball 2012 originals, Jin et al. numbers, the Jhaveri per-model token and success cells (garbled table).
