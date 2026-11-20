# Critique: B02.02 Reward prediction error learning

## Corrections and re-verification (this session, from PDFs or PMC text)
Confirmed against source text, no change needed:
1. Daw 2011: median model-free weight 61%, lambda median 0.57, sign tests P<.005 / P<.05 (PMC3077926).
2. Dabney 2020: split-half R=0.58, p=1.8e-5; 13/40 above and 10/40 below baseline at 5 uL (PMC7476215).
3. Demircan 2024: best TD latent block 34 r=0.58; SR max r=0.62 vs transition matrix 0.49; TD error r=0.60; lesion 24.3% to 18.9% (arXiv 2410.01280).
4. Schubert 2024: regret 0.09 to 0.05, t(199)=3.1, p=.002; alpha+ 0.87, alpha- 0.10, t(49)=20.1; posterior probability 0.93 (arXiv 2402.03969).
5. Monea 2025: Qwen2.5-7B 6.2% to 72.2%; Llama 28.6 to 74.4, Qwen 29.2 to 68.4 gains (arXiv 2410.05362).
6. Song 2026: Game of 24 table CoT 6, Long-CoT 47, Reflexion 44, Best-of-N 49, Self-Refine 47, ICRL 90/84 (arXiv 2506.06303 v6, ICLR 2026 version).
7. Kim 2020: spiking fit, RPE weight alpha=0.91 +/- 0.20, n=78 neurons (PMC7736562). This is stronger than the calcium-only numbers in a20; add it as support for the TD-with-ramps account.
Correction of wording: a20 and a21 describe Kim 2020 and Jeong 2022 as separate accounts; both only fit the TD family if state space or value ramps are allowed, so "contested" in claim K05 is right and "classic TD fails" would be too strong.
Not re-opened: Sharpe 2017/2020, Maes 2020 p-values, Sadacca 2016, Taira 2024, Hayes 2024, test-retest ICC (b10), D-MEM. These keep their original read status.

## Contradictions between sources
- Sharpe 2020 (stimulation does not act as a model-free error, F(1,14)=0.004 on conditioned reinforcement) vs Maes 2020 (silencing impairs second-order conditioning, z=1.9, p=0.03, r=0.34). Different manipulations (sufficiency vs necessity); one lab family; effects modest.
- Dabney 2020 (diverse reversal points) vs Eshel 2016 (common response function). Dabney reanalysed related data; dopamine heterogeneity may depend on projection target (Avvisati 2024).
- Krishnamurthy 2024 (LLMs fail to explore) vs Zhang 2025 (reasoning LLMs show directed exploration): different tasks and models, no common metric.
- D-MEM: big token saving but single-hop F1 halves; the headline "F1 up" hides this.

## Weak spots
- Counts of "sources" overstate independence: a24, b11, b12, b14, c06, a25 are all the same Demircan paper. K06 is therefore single-source.
- Most neuroscience samples are small (N=17 humans; 5 mice for Dabney; n=7 to 8 mice for Jeong; 8 rats per Sharpe group).
- The LLM RL results mix reward-from-environment and self-judged reward (Game of 24 reward is the model's own 0-3 judgment).
- LLM "TD" evidence is correlational (SAE feature vs a fitted Q-learner).
- Learning rates (alpha+/alpha-) are fitted descriptions, and human test-retest reliability of such parameters is poor (b10).
- Relevance to our scaffold is indirect: learning is outside the loop (no weight updates). Only in-context reward feedback, exploration and memory gating are usable.

## Seen only in snippets or abstracts (opened:false)
a01-a05, a11, a23 (abstracts); b18-b23, c19-c22, c24, c25 (snippets); Schultz 1997 original data (never opened). Founding numbers for the 1990s monkey recordings are therefore not verified.

## GAPS
1. Does a reward-annotated multi-attempt loop (ICRL-style) beat best-of-N at matched total tokens when the reward is external and verifiable, not self-judged? (Song 2026 uses self-judged reward on Game of 24.)
2. Do failed attempts with negative reward help or hurt in context? Monea says negative rewards are learned weakly; Reflexion-style loops assume they help.
3. Can LLM asymmetric updating (alpha+ >> alpha-) be corrected by a prompt or scaffold rule, and does correcting it reduce regret? Which models and temperatures?
4. Is the Demircan TD latent replicated in other open models and tasks, and does steering it change behaviour (causal, not lesion only)?
5. Is there any measured gain from summary statistics or algorithm-guided prompts (EVOLvE, Krishnamurthy) in non-bandit scaffolds such as multi-step reasoning?
6. What are the exact original numbers of Schultz, Dayan, Montague 1997 and Bayer and Glimcher 2005 (neuron counts, monkeys, effect sizes)? Not opened.
7. Gershman 2024 "Explaining dopamine through prediction errors and beyond" and Gershman and Uchida 2019: what do they list as the main failures of RPE theory? Not opened.
8. Does surprise- or prediction-error-gated memory (D-MEM, ReSuME, PreCoMem) hold up against write-all at equal tokens on multi-session tasks, and does it lose single-hop recall systematically?
9. Dopamine pharmacology in humans (Deserno 2021, levodopa studies): sample sizes and effect sizes for credit assignment; is there a replication?
10. Do reasoning-trained LLMs show more model-based behaviour in the two-step task than base models at equal tokens (CogBench suggests CoT raises it)?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d20). claims.jsonl now has K18 to K26 added; K10 moved to contested, K11 to established.

1. CLOSED in part. External verifiable reward: Kwon 2026 (d01-d02) shows the gain over a no-context baseline comes mostly from showing earlier attempts; flipped, random or removed rewards keep most of it. Reward-sensitive improvement is 3.3 to 4.4% of cells. No matched-token comparison with best-of-N was found for an external verifier. TR-ICRL (d04) beats best-of-16 at a stated fixed budget, but its reward is a majority-vote pseudo-label. Still open: reward loop vs best-of-N at equal tokens with a hard verifier.
2. CLOSED. Raw failed attempts are replayed more, not avoided (0.7% to 3.1%; true low reward label 2.5%, d03). Reflexion shows failures help when verbalised and gated by a reliable test (0.60 to 0.68; no test signal 0.52, d06). So Monea and Reflexion do not conflict: raw negatives in context are weak, reflections work.
3. OPEN with one lever. No prompt that corrects alpha+ > alpha- was found. Schubert (d07-d08) shows the asymmetry is limited to free choices, reverses for counterfactual outcomes, and disappears with another agent's forced choices (regret 0.07 to 0.02, t(143)=2.5). One model (Claude v1.3, temperature 0); no newer-model replication found.
4. OPEN. No replication of the Demircan SAE TD latent and no steering study were found. Zou 2026 (d09-d10) is convergent but a different method: probe neurons in Qwen and Llama; ablation of 1% value neurons cuts MATH500 75.2% to 37.0%, and a TD-neuron process reward gives 72.3% avg vs 66.1% random at K=4. The authors call the causal evidence preliminary.
5. OPEN. EVOLvE (d11) confirms externally computed statistics help strong models in bandits (Gemini Pro contextual 7.1 to 64.3) and hurt the smallest (Gemma-2B 7.6 to 4.9). No test in multi-step reasoning scaffolds found.
6. CLOSED in part. Bayer and Glimcher 2005 opened (d14): 2 monkeys, 81 recorded, 50 analysed, 44 of 50 modulated at p<0.01, mean R-squared 0.29, positive-only coding. Schultz 1997 is a synthesis paper with no new neuron counts (d16, abstract only); Mirenowicz and Schultz 1994 (d15, abstract only): two monkeys, three quarters of neurons responded to unpredicted liquid. Full-text Schultz 1993 / 1994 counts are still unread.
7. CLOSED in part. Gershman and Uchida 2019 read (d18): backward blocking, uncertainty. Gershman 2024 (d17): abstract and figure titles only (paywall); its three challenges are ramping, sensory and motor responses, and action selection. Body text not read.
8. OPEN in part. D-MEM (d12) halves single-hop F1 (44.7 to 21.6) while cutting tokens 80%; PreCoMem (d13) leads LoCoMo overall (73.57) and keeps single-hop at 81.41, so the loss is not systematic across gated designs. Neither has a write-all baseline at equal tokens in the main table. ReSuME was not found.
9. CLOSED in part. Deserno 2021 (d19): N=62, 150 mg levodopa, within-subject; effect on MB guidance of MF credit assignment; model-agnostic tests partly null; no replication found. Other levodopa studies not opened.
10. OPEN. No reasoning-model vs base-model two-step comparison found; NeuroCogMap (d20) does not make it. CogBench CoT result (K15) stays the only data point.

Net: the main new finding is K18/K19. It changes how the scaffold should use outcome feedback: do not rely on a reward label, summarise failures in words, and keep the verifier external. The earlier note that "ICRL beats best-of-N" (Song 2026, self-judged reward) should be read with K18 beside it.
