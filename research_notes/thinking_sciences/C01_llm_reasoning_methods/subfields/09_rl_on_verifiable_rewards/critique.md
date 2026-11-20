# Critique, C01.09 RL on verifiable rewards

## Corrections made (sources re-opened as PDF text this session)
Re-checked against the PDFs: R1 (2501.12948), DeepSeekMath (2402.03300), DAPO (2503.14476), Yue et al. (2504.13837), one-shot RLVR (2504.20571), Spurious Rewards (2506.10947), Dr. GRPO (2503.20783), Wu et al. (2507.10532), Hochlehnert et al. (2504.07086).
- CONFIRMED: R1-Zero AIME 15.6 to 77.9, majority 86.7; R1 79.8; pass@64 90.0; GPT-4o 9.3 to 13.4; DeepSeekMath 82.9/88.2 and 46.8/51.7; DAPO ladder 30/36/38/41/42/50 and 47 for R1-Zero-32B; Yue 43.9 vs 42.6 and 26.1 to 42.5; one-shot 36.0 to 73.6, 17.6 to 35.7, 74.8/36.6; Spurious +29.1/+21.4, 65 to over 90% code, 60.9 vs 28.0; Dr. GRPO 43.3%, 27 h on 8 A100; Wu 54.60/65.80/39.20 and Llama 3.8/2.4; Hochlehnert 19.3 to 23.0.
- CORRECTED: c03 gives o1-1217 AIME 2024 as 78.1. The R1 paper table gives o1-1217 79.2 (as a10 and b03 say). 78.1 belongs to another column. Use 79.2.
- CORRECTED: c07 Table 1 numbers were flagged by its author as garbled; do not cite the Qwen2.5-Math-1.5B template averages.
- NUANCE: a24 and b11 mention OLMo2-SFT gains of +8.9/+5.5. The paper says OLMo2-7B-SFT degrades under standalone format or incorrect rewards and gains those amounts only under other reward types. Do not read it as spurious rewards working on OLMo.
- NUANCE: Spurious Rewards gives code-reasoning accuracy 60.9 vs 28.0 in the main text and about 64 vs 29 in an appendix line. Cite the main text.
- NOT RE-VERIFIED in PDF: Hochlehnert "5 to 15 points SD over 20 seeds" (the 3-point per-question and 30-seed advice were found); Chen et al. faithfulness numbers; ProRL, Gandhi, Kimi, SimpleRL-Zoo numbers.

## Contradictions
- Yue et al. (RL narrows coverage at large k) vs ProRL and SimpleRL-Zoo (boundary expands with long, diverse training or weak bases). Setups differ in base model, steps, KL control and k. Unresolved.
- Spurious Rewards (gains mostly elicitation) vs real-learning claims; Wu et al. attribute part of the effect to Qwen contamination.
- Math RL transfer (c22) vs Tulu 3 domain-specific gains (a07).
- Aha moment: R1 reports it as emergent from RL; Liu et al. and Gandhi et al. find it in base models.

## Weak spots
- Most gains are on Qwen2.5 models, which are contaminated and format-primed.
- Single-run AIME numbers have 5-15 point seed noise; many comparisons sit inside the noise.
- Items c07, b22, b15, b26, c20, c21 recorded no single headline number.
- c25 was not opened (duplicate of a03 and a04).
- Files a, b and c overlap on the same ten papers. Independent-source counts in claims.jsonl count papers, not labs, so "established" is mostly cross-paper agreement.
- Relevance to our agent is indirect: we do not train.

## Only seen in snippets
Only c25 is marked opened:false.

## GAPS
1. Does a prompt-only scaffold (verify, backtrack, subgoal operators) reproduce the RL-induced behaviours at equal tokens on a clean, uncontaminated benchmark?
2. Does a scaffold narrow pass@k at large k the way RLVR does, or keep coverage?
3. How much of the RLVR gain is format and elicitation, and can a format-only prompt capture it (one-shot RLVR, spurious rewards)?
4. Which prompt-time analogue of a verifiable reward (tests, symbolic check, executable code) gives the best gain per token on non-math tasks?
5. Does RLVR on code and tool-use agents (SWE tasks, agentic RL) transfer, with measured numbers beyond math?
6. How do long-CoT length and accuracy relate under equal budgets (overthinking, length-efficiency RL results)?
7. Do reward-hacking and unfaithful-CoT results imply the scaffold needs checks independent of the model's stated reasoning?
8. What are fresh-benchmark results (post-cutoff problems) for R1-style models vs the same models on AIME24?
9. What did 2026 work (rubric or non-verifiable rewards, test-time RL) show?

## Gap search results
Sources opened as PDF text this session: d01-d20 (evidence_d.jsonl). Search limits: the WebSearch budget was exhausted, and the arXiv, Semantic Scholar and OpenAlex search endpoints returned 429 rate limits, so papers were fetched by known arXiv id only. Papers from 2026 that I could not look up by search are therefore missing.

- Gap 1 (scaffold vs RL-induced behaviours at equal tokens, clean benchmark): PARTLY CLOSED. d01 (power sampling, 8.84x tokens, recovers most of GRPO on MATH500), d02 (steering recovers 76% of RL gap), d16 (NoThinking plus verifier beats Thinking at equal tokens). No study tests a prompt-only verify/backtrack scaffold on post-cutoff problems. OPEN for that exact test.
- Gap 2 (pass@k narrowing): CLOSED in direction, OPEN in magnitude. d19 (more questions lose than gain a verified success), d18 (negative correlation with base pass@128, expansion on weak-base tasks), d20 (pass@k reward keeps coverage), d01 (sampler keeps pass@k). No scaffold-level pass@k curve was found.
- Gap 3 (format and elicitation): PARTLY CLOSED. d03 (format compliance 12.2% to 95.6%; MATH strict vs lenient 63.2/70.9/73.7), d01 (low temperature alone 49.6 to 69.0), d09 (majority-vote reward). No clean split of gain into format vs reasoning for one model.
- Gap 4 (best prompt-time verifier analogue per token): PARTLY CLOSED. d17 (verifier gates the gain: oracle 95.5 vs intrinsic 74.7 on GSM8K), d16 (task verifier best-of-N), d04 (test verifier), d11 (instance-specific rubrics beat generic). No head-to-head per-token table across tests, symbolic checks and rubrics. OPEN.
- Gap 5 (code and agent RL transfer): PARTLY CLOSED. d03, d05, d04 give numbers on SWE-bench Verified (41.0, 60.4, 32.0 with verifier). Gains are mixed with SFT and scaffold choices. No pure agentic-RL ablation found. OPEN for tool-use agents beyond SWE.
- Gap 6 (length vs accuracy at equal budget): CLOSED. d12, d13, d14, d15: single-chain accuracy rises then falls; parallel samples keep gaining; first round is right in over 92% of cases.
- Gap 7 (reward hacking, unfaithful CoT): CLOSED. d06 (25% and 39% faithfulness, hacks verbalised under 2%), d07 (CoT monitor 95% vs 60% recall, obfuscation under strong optimisation). Conclusion: scaffold checks must be independent of the stated reasoning.
- Gap 8 (fresh-benchmark results): PARTLY CLOSED. d08 shows AIME 2024 contamination (10-20 points) and gives post-cutoff results for current models (GPT-5 91.3 on AIME/HMMT 2025). No paired R1-Zero-style RL vs base comparison on post-cutoff problems. OPEN for that pair.
- Gap 9 (2026 work: rubrics, non-verifiable, test-time RL): PARTLY CLOSED. d09 (TTRL), d10 (Intuitor, ICLR 2026), d11 (rubrics as rewards), d02 and d19 (2026 revisions). The coverage of 2026 first-appearance papers is thin because searching was blocked. OPEN.

Corrections: K16 upgraded to established (two papers, full text); K13 gains d08; new claims K19-K26. The 'not re-verified' flag for Chen et al. faithfulness numbers is cleared; ProRL headline numbers (14.7/13.9/54.8/25.1/18.1) are now confirmed in text. Hochlehnert seed SD, Gandhi, Kimi and SimpleRL-Zoo numbers remain not re-verified.
Extraction caveats: tables in d01 (Phi-3.5 rows), d09, d10, d14 and d20 came out garbled in pdftotext; only unambiguous numbers were used.
