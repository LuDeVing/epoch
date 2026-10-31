# Critique: A14.01 Theory theory / child as scientist (cross-check)

## Re-checked against source text (this session, local text copies)
1. Benton & Rakison infant ANOVA: main test is F(3,54)=0.28, p=.84 (a11 correct). b05 cited F(3,51)=1.55, p=.21, but that is the sex x test-type interaction, not the main test. CORRECTION: use a11.
2. Weisberg, Choi & Sobel: N=242 (Exp 1), N=112 (Exp 2), younger groups chance p>.19, oldest binomial p=.007 (blicket) and p<.001 (butterfly). Confirmed.
3. Yiu et al.: imitation children 88.4% / adults 84.9%; innovation 85.2% / 95.7%; GPT-4 innovation 75.9%, imitation 83.3%. Confirmed.
4. Kosoy et al. 2022: 71% vs 32%, p=0.002; 17.7% and 17.5% tested empty machine. Confirmed. (Actions: a20 says about 12.4 both structures; b12 says 14.07 vs 10.58 by condition; not re-checked, likely different splits.)
5. Alderete et al.: pooled base 96/110 = 87.3%, and 12/110 = 10.9% exactly-N trap. Confirmed.
Not re-opened (network/PMC blocked, disk full on C): Gopnik 2017 age curve, Schulz 2007, Sobel 2007, Samiei 2026, Jhaveri 2026 Qwen figures, Bonawitz 2011. That is 5 of the intended 10 checks done as 5 source papers, not 10 separate numbers.

## Contradictions between sources
- Jhaveri et al.: Qwen3-8B success 0.21 to 0.36 (c13) vs 0.21 to 0.40 (b24) vs blicket 0.32 to 0.40 (b18). Probably different tasks (Wason vs blicket) and variants; unresolved, quote with the task named.
- Alderete: context graph raises post-switch reasoning accuracy (+20.6 pp) yet lowers pooled raw accuracy (77.3 vs 87.3%). Both are true; the headline depends on the subset.
- Sobel 2007 Exp 1: significant only one-tailed (p=.05); b07 and a09 agree.
- a04 (probability matching) and b04 (inside the 95% interval) both say the Bayesian reading is not distinguished from associative noise.

## Weak spots
- Most founding child numbers (Gopnik 2001, Sobel 2004, Denison 2010, Kushnir, Liu 2007) are second-hand via a review or McClelland & Thompson.
- Many child studies are small (n=14-25 per cell), deterministic, 2-3 variables.
- LLM studies: 2022-2023 models are obsolete; 2026 results are preprints (Samiei, Jhaveri, Alderete, Hieu); Alderete is a company lab and one model family.
- No study found testing a theory-theory-shaped REVISE loop at equal tokens against best-of-N.
- Only a snippet seen: Hieu RAUMA (c27, not opened).

## GAPS
1. Does a refine/REVISE loop beat best-of-N with equal tokens on blicket-type induction with current models (all cited gains are not token-matched)?
2. Is the 2026 AND-vs-OR gap in LLMs caused by hypothesis-space size (16-96 seeds) in non-text tasks and with reasoning models, or by prior bias?
3. Which exact intervention (counterexample prompt, graph state, monitor, final check) gives gains outside the lab that reported it; replications of Alderete and Jhaveri.
4. Original numbers for Gopnik 2001, Sobel 2004, Denison 2010 (read primary papers) and large-sample or multi-lab replications of child causal inference.
5. Do adults and LLMs retroactively revise (backward blocking) on re-scoring old evidence; why did Benton & Rakison find adults' B rating did not drop?
6. Does the child-better-than-adult result (Lucas 2014, Gopnik 2017) replicate with active exploration, per Samiei 2026 (peer-reviewed form)?
7. What is the error profile when an agent confirms rather than falsifies at S5, and does the incompatible-to-compatible test ratio predict success in non-thinking models?
8. Do effects hold with more than 4 uncertain causes and with probabilistic (noisy) rather than deterministic machines?
9. Does pedagogical framing (narrower search) have an analogue in directive system prompts for LLM agents?


## Gap search results (evidence_d.jsonl, d01-d18; claims K17-K21 added, K03/K12 now contested)

Search conditions: the web-search tool, OpenAlex and Semantic Scholar were out of quota. Work was done with arXiv listing pages, Europe PMC, Crossref and direct PDF reads (stored on D:, deleted afterwards). Coverage is thinner than intended. Paywalled originals (Gopnik 2001, Sobel 2004) could not be opened.

### Contradiction resolved
- Jhaveri Qwen3-8B figures: 0.21 to 0.36 is the Wason task; 0.32 to 0.40 is the blicket test (thinking mode). The earlier "0.21 to 0.40" mixed the two (d07). Qwen3-32B: Wason 0.41 to 0.61, blicket 0.57 to 0.86. Non-thinking Qwen3-8B blicket 0.11 to 0.19.

### Gap by gap
1. REVISE vs best-of-N at equal tokens on blicket tasks: OPEN. No such study exists. Nearest evidence says self-inspecting loops lose to repeated sampling at equal cost on math with 1.5B-7B models (d10: 0 of 36 comparisons better, 10 worse) and that orchestration gains are at most 4.6 points at 2-4x tokens (d11). Qiu 2024 has no equal-token comparison; its refinement gain used a symbolic checker (d15). K12 moved to contested; K17 added.
2. AND/OR gap: hypothesis-space size or prior bias: PARTLY ANSWERED, cause still open. Reasoning models (gpt-5, deepseek-reasoner) are near-perfect on OR and much better on AND than older models, still below top humans (d02). Higher reasoning effort in o3-mini/o4-mini made 8-object AND exploration worse (d03). The seeding fix changes hypothesis count and prior flatness together, so the two causes are not separated. Non-text tasks: nothing new found.
3. Outside replication of Alderete and Jhaveri: OPEN, with one partial result. None for Alderete (one model family, hand-written monitors; d09). For Jhaveri, FALSIFYBENCH (another lab) finds the same negative-testing-to-success link as a correlation (rho = -0.779, 12 models, 1,200 games; d08), not as a prompt intervention. The blicket-LLM papers share authors (d18). K18 (correlation) is established; K21 records the missing replications.
4. Original numbers (Gopnik 2001, Sobel 2004, Denison 2010): OPEN. Paywalled; the best open review has no N or statistics for them, and its Denison 80/20 chip figure is a hypothetical, not data (d16). Verified instead from open text: Gopnik 2017 age curve (d04) and Bonawitz 2011 (d05). Beckers 2009 reports no backward blocking at age 3 (abstract only, d12). No large-sample or multi-lab replication of child causal inference found.
5. Backward blocking in adults and LLMs: OPEN for LLMs (no study found, d17). Adults: found in an incidental reaction-time task (d13), not in Benton and Rakison's rating task. ACRE shows backward-blocking queries are hardest for pre-LLM models (d14). K03 moved to contested.
6. Child-better-than-adult under active exploration: PARTLY CLOSED. Samiei 2026 is now accepted at CogSci 2026 (d01) but is adults only; the child arm does not exist. Gopnik 2017 numbers verified (d04).
7. I:C ratio in non-thinking models and the confirm-vs-falsify error profile: PARTLY ANSWERED. In Jhaveri the I:C vs success correlation holds in both thinking and non-thinking models, but TiO changes behaviour mainly in thinking models; going from non-thinking to thinking raises success without a consistent I:C rise (d07). In FALSIFYBENCH lost games carry more confirmation bias than won games for the same model (20% vs 50% for GPT-5.2-Chat; d08). Still no S5-specific error profile.
8. More than 4 causes and noisy machines: PARTLY ANSWERED for noise, OPEN for causes. With activation probability 0.70 all agents sit at 73-77% and the scaffold adds nothing (d09; K19). Nothing found beyond 8 objects (GX-Chen) or on the Weisberg cliff at 4 causes in LLMs.
9. Pedagogical framing in LLM agents: OPEN. No LLM study found (d17). Bonawitz 2011 numbers verified (d05). A 2026 adult study finds that handing over a heuristic keeps search broader than handing over a solution (abstract only, d06).

### Net effect on the schema
- Keep: log tests outside the current hypothesis at S5 (K18). Give the agent a mechanical hypothesis-vs-data check (d15, d09).
- Do not assume: that a REVISE loop beats N independent tries (K17), that scaffold gains survive noise (K19), or that backward blocking happens by itself (K03).
- Test model matters: counterexample prompts and loop gains differ between thinking and non-thinking models and between backbones (d07, d11).
