# Critique: A03.05 Debiasing by training (cross-check)

## Corrections made (sources re-opened this session)
1. Sellier et al. (2019), evidence b05: the file says "abstract states 29% less likely". The abstract (OpenAlex, DOI 10.1177/0956797619861429) says **19%** less likely. Raw rates 58.8% vs 72.2% give a 19% relative drop; the 29% is wrong (odds-ratio exp(b)=.549 is a 45% odds drop). A corrigendum (2020) exists and was not read. Claim K05 uses 19%.
2. Morewedge et al. (2015): abstract re-read. "Games >= -31.94%, videos >= -18.60% at once; games >= -23.57%, videos >= -19.20% later" are the minimum across the two experiments, not single numbers. Exp 1 game -46.25% (a01) is consistent. Confirmed: one-shot, medium to large effects, game bigger than video.
3. Chang et al. (2016): abstract confirms "less than one hour", 6 to 11% Brier gain. Confirmed. Note the training (CHAMPS KNOW) was a multi-part package, so which part worked is unknown.
4. SACD (Lyu et al. 2025): paper tables checked, FOMC Llama-3.1-8B vanilla 0.3805, SACD 0.1570; GPT-4o few-shot debiasing 0.7350, self-help 0.0625, SACD 0.0300. Confirmed.
5. Echterhoff et al. (2024): Table checked. GPT-4 baseline admit rate 0.375 vs 0.780 under the two frames, gap -0.405 (this is a gap in admission rates in points, not "40.5% more students"); awareness -0.470, self-help -0.010; Llama-2 "32.1% fewer females" confirmed. Wording in a13/c01 should say points.
6. Shepperd et al. (2018) d=1.19 vs 0.72 not re-opened. The 2014 poster by the same group (Mair, Shepperd, Jorgensen; N=118) reports a different effect size scale (0.3 to 0.14) so the two should not be mixed. c23 (not opened) is now seen at abstract level.
7. Huang et al. anchoring: abstract confirms "shallow-layer, cannot be eliminated by conventional strategies, reasoning offers some mitigation". The 34.7% to 24.7% figure was not re-checked.
8. CogBias abstract: activation steering gives 26-32% bias reduction; Qwen lost up to 19 pp on judgment benchmarks. Confirmed; evidence file said "about a third" (slightly high).
9. Aczel et al. (2015) abstract confirms N=154, 10 biases, 4 weeks, gains only on statistical tasks.
10. Hirt and Markman (1995) and Nisbett et al. (1987): abstracts now read (any plausible alternative debiases; brief rule training can enhance everyday reasoning). Still no numbers.

## Contradictions between sources
- Warnings and awareness: Morewedge 2015 and Aczel 2015 say awareness/knowledge does not debias; Mair/Shepperd workshop and Sumita 2024 (AwaRe on GPT-3.5) say awareness cuts bias somewhat. Resolved only partly: it depends on the bias and the model, and the effect is small next to practice with feedback.
- Self-reflection: Echterhoff (self-help works for strong models) vs Lou and Sun (reflection does nothing for GPT-4 anchoring) vs SACD (loop works). Likely the difference is bias type (anchoring is shallow) and one-pass vs iterative.
- Consider-the-opposite helps in Hirt and Markman and in the 2-4-6 LLM paper, but Schwarz et al. (2002, unopened) predicts backfire when generating many reasons feels hard.
- Game vs video: Exp 1 favours the game by a wide margin; Exp 2 shows game = video on two of three biases. The "feedback beats passive" story is strong only for some biases.

## Weak spots
- The central human result is one research team (Morewedge, Sellier). The analyst study (b12) is the only other group and is a 2025 listing; its journal and sample details were not re-checked.
- No LLM study imitates the human training (repeated own-error feedback). SACD is one group's work; its biased prompts are built by the authors and the bias score is their own metric.
- Many LLM numbers come from 7B to 70B models and 2024 model versions; frontier-model effects are smaller or absent (GPT-4 baseline already low in several tests).
- Overcorrection is under-measured: only CogBias and the "Rethinking prompt-based debiasing" paper report false alarms.

## Only seen in snippets or not opened
a07 and b25 (Nisbett/Fong originals), a08/b26 (Fischhoff 1982), a09 (Hirt numbers), a10 (Larrick numbers in a-file; b08 has them), a11 (Mellers 2014), b13 (Ludolph and Schulz 2018: snippet only, 68 articles), b28 (Sedlmeier and Gigerenzer 2001), b29, b30 (Schwarz 2002), c18, c22, c23. Claim K15 relies on a c15 paper whose identity was not re-confirmed.

## GAPS (most decision-relevant first)
1. Does feedback on the agent's own earlier errors inside a run (error log with immediate correction, repeated item sets) lower bias at equal tokens versus a one-shot warning? No LLM study tests this directly.
2. Does SACD-style detect-analyse-rewrite beat a single self-help rewrite at equal total tokens, and does it still help on frontier reasoning models?
3. Which part of the debiasing packages (CHAMPS KNOW, the Morewedge game) carries the effect: naming the bias, direction of effect, practice, or feedback? Ablations are missing in people and LLMs.
4. Does the training effect transfer across bias families in LLMs (train on confirmation, test on anchoring)? Humans show transfer only inside a bias type or statistical-rule family.
5. What is the false-alarm cost (flagging unbiased content, over-hedging, lost accuracy) of each debiasing prompt, especially for judgment biases?
6. Do consider-the-alternative prompts backfire when the agent generates many alternatives (Schwarz ease-of-retrieval, plausibility moderator in Hirt and Markman)? Find the optimal number.
7. How long do effects last in a multi-step agent run (decay over steps) compared with the human 2 to 3 month retention (d 1.1)?
8. Independent replications of Morewedge 2015 and Sellier 2019 outside the Morewedge group, and the Sellier corrigendum content.
9. Does the order and kind of bias cue in the prompt (bandwagon-style, authority) get ignored after RL-style training only, or also after in-context practice?

## Gap search results (evidence_d.jsonl, d01-d19; claims K22-K27 added, K05/K06/K11/K16 changed)
Search note: WebSearch, OpenAlex, Semantic Scholar and arXiv search were all rate-limited or exhausted; work used Crossref, PubMed, the Conversation page and papers already saved in D:/research_scratch/A03.05.

1. Feedback on own errors inside a run: STAYED OPEN. No LLM study found. Adjacent only: static few-shot debiasing examples made gpt-4o much worse (0.7350 vs 0.3650 vanilla, d08); Reflexion helped there (0.2450).
2. SACD vs single self-help rewrite: PARTLY CLOSED. Ablation (d06) shows the detect and analysis steps each matter (FOMC 0.1175 vs 0.3490 for self-help). Still open: equal-token comparison and reasoning/frontier models (gpt-4o was the top model; DeepSeek-R1 appears only in PROBE-SWE, d09, with a different method). Iteration 1 can be worse than vanilla (d07).
3. Active ingredient of the human packages: STAYED OPEN, but sharpened. Game vs video differs in practice, coaching and interactivity, not just feedback; the authors say so (d05, d03). Game variants (hints, scores, first round only) did not differ.
4. Transfer across bias families in LLMs: PARTLY CLOSED. Weight-trained: content cues transfer, structural cue (position) does not (d14); social-stereotype dimensions transfer (d16); steering transfers across families but random directions also work (d15). In-context practice transfer for judgment biases: not tested.
5. False-alarm cost: PARTLY CLOSED. SACD false flags 12/3/6 per 500, wrong type 49/108/73 (d07); BBQ prompts over-flag and hide behind "Unknown" (d17); prompt mitigation cut Qwen3-4B clean accuracy 66.2% to 40.9% (d14); judgment bias prompt effect -4.4% (d15).
6. Backfire with many alternatives: HUMAN SIDE CLOSED, LLM SIDE OPEN. 10 alternatives raised hindsight bias, 2 did not (d11, d12). Hirt and Markman plausibility moderator not re-opened. No LLM test of list length; Failing-to-Falsify (d10) tests one opposite per turn and helps only thinking models.
7. Decay over steps: STAYED OPEN. Only human retention data (d02, d05) and a hint that an AI-labelled prior anchors recent models more (d19).
8. Independent replication and corrigendum: PARTLY CLOSED. Corrigendum exists (Psychol Sci 2020;31(6):762, PubMed); published abstract says 19% while the accepted manuscript and the authors' Conversation piece say 29%, so the correction is very likely 29% to 19% (corrigendum text not read, so this is inference). No independent replication found; the 2025 analysts study has no control group and shares authors, so K06 was downgraded to single-source (d04).
9. Cue order/kind and in-context practice: STAYED OPEN. Only RL-trained results (d14); no in-context-practice arm.

Corrections to earlier files: K06 was called a replication and is not independent; K16's LLM paper is arXiv 2604.02485 (identity confirmed); K05 effect confirmed as 19%.
