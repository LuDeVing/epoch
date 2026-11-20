# B02.01 Valuation and common currency: critique (cross-check)

## Numbers re-opened this session (from saved full texts)
Confirmed against source text:
1. Bartra 2013: 206 studies; 12981-voxel positive cluster p=0.0002; decision-stage cluster 3304 voxels; decision>receipt 1580 voxels.
2. Clithero and Rangel 2014: 81 fMRI studies, 104 contrasts (a16 says 81 studies; b03 says "over 80" and 104 contrasts; both fit).
3. Kable and Glimcher 2007: median R2 0.95 (0.84-0.98); k from 0.0005 to 0.1189.
4. Padoa-Schioppa and Assad 2006: 931 cells; 505 (54%) varied with offer type; under 5% spatial/motor.
5. Botvinik-Nezer 2020: 108 individuals; hypothesis 5 at 84.3%; others 21.4% to 37.1%.
6. Chen et al. 2023: CCEI 0.998/0.997 etc. vs human 0.980/0.985/0.967 (0.963 food); 347 humans; Bronars 99.9%; framing CCEI 0.901 (34%), 0.884 (48%), 0.698 (88%), 0.894 (49%); invalid answers 4.7% (T=0.5), 9.8% (T=1).
7. Mazeika 2025: correlations 75.6%, -78.7%, 87.3%, -97.6%; 10 US lives to 1 Japanese life (GPT-4o).
8. Tarabeih 2026: pooled lambda 1.26, CI 1.06-1.46; 102 estimates, 11 studies, 32 models; human 1.96, 1.07, 1.31.
9. Goli and Singh 2023: 22% later-reward choice (GPT-3.5 headline).
10. Arithmetic-GPT: 69.3/63.2/64.0/96.1 (uniform) and 70.8/65.5/67.8/95.5 (ecological) both appear; a27 and b18 are two different training variants, not a conflict.

Not re-opened: Chib 2009 Z values (a07), Plassmann r=0.59 (a18), Padoa-Schioppa lines other than counts, Louie 2011 neuron counts, DeLLMa 40%, Schubert 0.93. These remain as the first-pass agent recorded them.

## Corrections and cautions
- a23 "correlation -97.6% between utility variance and scale" is a figure label (Figure 12) for variance across models, read from the PDF text. It is not a correlation with MMLU. Do not quote it as a scale effect on coherence without the figure.
- a01 gives "42.0% left striatum, 40.5% right, 23.5% vmPFC" as percent of studies with a focus within 10 mm. This is a density of reported foci, not an effect size.
- b12/c05/a23/b24 are four lines about one paper (Mazeika 2025). Counted as one independent source in claims.
- b13/c01/a25/c03 are one paper (Chen 2023). Same.
- Mazeika uses MMLU as the "scale" axis, so "scale" means capability, not parameter count alone.
- Tarabeih 2026 meta-analysis pools estimates that come from different elicitation methods (value curvature 1.01 vs 0.52 by method), so pooled values hide method effects.
- a21 and b07 are the same Hayden and Niv paper; counted once in the contested claim, but b08 and b23 are separate lines pointing to the debate.

## Contradictions between sources
- Common currency (Levy and Glimcher 2012; Bartra 2013) vs "no cardinal value by default" (Hayden and Niv 2021; Bennett 2021 cited only). The fMRI/neuron data cannot separate them because value correlates can arise from either. Status: contested.
- Chen 2023 says GPT is more rational than humans; the same paper shows collapse under reframing, and Binz and Schulz 2023 / Ross 2024 / Wang 2026 show human-unlike or unstable behaviour. These are compatible: high consistency within one frame, low across frames.
- LLM loss aversion: Jia 2024 reports loss aversion about 1.48 (ChatGPT lowest of three), Tarabeih pools to 1.26, Binz and Schulz found 3 of 6 biases. Range is wide; no single number is safe.
- Common-currency claim for fMRI is partly human-specific; the LLM literature tests only whether preferences are coherent, not whether any internal single-scale value variable is used. Mazeika probes are the only (partial) test.

## Weak spots
- The founding studies are small (Chib N=19 and 13; Kable N=10). Botvinik-Nezer shows large analysis variability.
- Almost no LLM study tests a vmPFC-like mechanism. The LLM work tests behavioural coherence (transitivity, GARP, expected utility), which is a weaker claim.
- Most LLM studies use GPT-3.5/GPT-4-era models. Reasoning models are rare (b17 only, plus 2026 papers).
- Montague, King-Casas and Cohen 2006 and Tom 2007 were seen as abstracts only (a19, a20). Sescousse 2013 (a17) not opened. b19-b23 were not opened.
- Sharot and Dolan 2011 (named key work) has no direct evidence line; only the Schubert 2024 LLM optimism-bias test (c22) touches it.
- Several 2026 LLM entries (b08, b15, a26, a29) are recent preprints without replication.

## Seen only in snippets or abstracts
a19, a20, a17, b19, b20, b21, b22, b23, c30 (abstract only). Their claims are not used as sole support for any claim.

## GAPS
1. Does an LLM scaffold that elicits explicit pairwise utilities then ranks beat plain CoT at equal tokens on open-ended option choice (not only DeLLMa-style tasks)? Only one paper tests this.
2. How large is the framing-induced CCEI drop for current reasoning models (2025-2026), and does a "re-ask under reframing and require agreement" step repair it at equal tokens?
3. Do Mazeika-style utility fits and linear probes replicate on models other than those tested, and do probe-read utilities predict behaviour on novel items (causal test, not only correlation)?
4. Is LLM value context-dependent (divisive normalisation, decoy or range effects) as in monkey LIP and human choice? No LLM study found on this.
5. Do LLMs show a stable shared scale across goods (money vs food vs time vs social) in the Chib/Levy-Glimcher sense, i.e. equal-value cross-domain exchange rates that predict choice?
6. Sharot and Dolan 2011 and Montague 2006 were not opened: what are the exact effect sizes, and does the optimism bias in LLM learning (Schubert 2024, one model) replicate in other models and after RLHF vs base?
7. What does the 2026 "value as common currency" defence (b08) predict that Hayden and Niv's alternative does not, in a testable behavioural form?
8. Do stated-vs-revealed preference gaps (b15, b16) shrink when the agent is forced to output a numeric score and then choose, versus choosing directly?
9. How stable are loss-aversion estimates across elicitation methods in current LLMs (lambda 1.26 pooled vs 1.07-1.96 human), and does a scaffold change them more than a prompt does?
10. Do hidden exchange rates (Mazeika lives-by-country) persist in agents with a scaffold and tools, or does an audit step remove them?

## Gap search results
Search budget: WebSearch ran out early (3 usable calls); arXiv, Semantic Scholar and OpenAlex APIs were rate-limited (429), so work used direct PDF/HTML fetches, Europe PMC and arxiv.org pages. Evidence is in evidence_d.jsonl (d01 to d20).

Closed or partly closed:
- Gap 6 (Sharot and Dolan 2011 numbers): CLOSED for the human side. N=19, update 11.2 vs 7.7, t(18)=4.4, 15 of 19 people, slopes 0.72 vs 0.33 (d01). The effect is disputed (Shah 2016, abstract only, d03) and defended by the original lab (d02), so it is contested. Montague, King-Casas and Cohen 2006 is a review with no effect sizes (d04, abstract only). The LLM half (replication of Schubert 2024 on other models, base vs RLHF) stays OPEN: the paper used Claude v1.3 only (d13).
- Gap 4 (context dependence in LLMs): PARTLY CLOSED. Decoy effects exist and grow with instruction tuning and RLHF (d05), survive a warning (d06), and are larger in gpt-4o than in humans on credibility ratings (d07). No divisive-normalisation test. Xie 2025 seen as a snippet only (d19).
- Gap 2 (framing drop for reasoning models): PARTLY CLOSED. Plain-format CCEI is 0.95-1.00 (d08), format changes hurt Llama and Qwen but not GPT or DeepSeek (d09). No 2025-26 reasoning-model reframing test and no "re-ask and agree" test found. OPEN.
- Gap 1 (scaffold vs CoT at equal tokens): PARTLY CLOSED. DeLLMa is not equal-token: 5181 tokens vs 1946 CoT (d15), and beat o1-preview 73.3% vs 33.3% and 64.2% vs 35.0% (d16). Open-ended option choice not tested. OPEN.
- Gap 3 (probe replication, causal test): OPEN. Probes tested on three Llama models only; no steering test (d11).
- Gap 9 (loss-aversion stability): PARTLY CLOSED. 28 estimates over 19 models, range 0.49 to 2.72, prediction interval 0.20 to 2.31, model family 27% of variance (d18). Correction to the earlier cross-check: the 102-estimate/32-model figure is not the loss-aversion pool. No scaffold-vs-prompt contrast. OPEN.
- Gap 8 (numeric score first vs direct choice): OPEN. Stated-vs-revealed papers use forced binary choices (d17); Yamin 2026 (d20) elicits probability then choice but only abstract and intro were read.
- Gap 10 (exchange rates under scaffolds): OPEN. Fine-tuning moved a model toward assembly preferences, 73.2% to 90.6% (d12), but no scaffold or audit test.
- Gap 5 (stable cross-domain exchange rates, Chib style): OPEN. Nothing new found.
- Gap 7 (what the 2026 common-currency defence predicts that Hayden and Niv do not): OPEN. Not searched, budget.
- Coherence is model-specific: Seror 2025 finds 2 of 39 models pass at 1%, 7 at 5%, 9 at 10% (d10). This weakens a simple "LLMs are rational" reading of Chen 2023.
- Not opened: d03, d04, d19 are abstract or snippet only; do not use them as sole support. Several pages were read via fetch summaries or garbled PDF tables (noted in limits).
