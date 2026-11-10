# Critique: E12.05 premortem and prospective hindsight

## Corrections and confirmations (re-opened this session)
- Huang 2024 (arXiv 2310.01798): PDF table text shows 75.9/75.1/74.7 (GSM8K, GPT-3.5), 75.8 -> 38.1 -> 41.8 (CommonsenseQA), GPT-4 GSM8K 95.5 -> 91.5. CONFIRMED. The 89.0 round-2 value was not seen in the garbled table text; unconfirmed.
- Tyen 2024 (arXiv 2311.08516): 52.87 overall for GPT-4 confirmed in the text and table. Abstract confirms 5 tasks and the correct-when-told finding. The +18 to +44 figures were not re-opened.
- Who&When (arXiv 2505.00212): 127 systems, 53.5% agent, 14.2% step confirmed from the abstract.
- MAST (arXiv 2503.13657): 150 traces, kappa 0.88, 14 modes, 3 groups, 1600+ traces confirmed. The 0.77 LLM kappa and 41-86.7% rates are not in the abstract; unconfirmed.
- Renze and Guven (arXiv 2405.06682): nine LLMs, eight types, p < 0.001 confirmed from abstract. Per-type accuracies not re-opened.
- Mitchell 1989: Crossref confirms the record only. The +30% was NOT confirmed from the primary paper. Treat as second-hand.
- Veinott 2010 (N=178, ~2x confidence drop), Gallop 2016 (N=101) and Peabody: not re-opened; secondary pages only.
- Correction to a12/b25/c23: an LLM-vs-human premortem paper exists: Veinott and Lehman (2024), "Adaptive Planning: Comparing Human and AI Responses in Premortem Planning", HCI International 2024 Late Breaking Papers (DOI 10.1007/978-3-031-76827-9_15), found via Crossref. No abstract available, so results unknown. The earlier "no study found" statements are wrong.
- a03/b05 and a04/b06 are the same source (one review page) and are counted once in the claims. a01 is abstract only. c17 and b23 are the same paper under different author attributions (not checked).

## Contradictions
- Self-Refine (+20% average) vs Huang/Kamoi (no gain or loss): partly task type (style vs verifiable reasoning) and oracle leakage.
- Reflexion and Renze gains vs intrinsic self-correction loss: the gains rely on being told the first answer failed, a signal a premortem does not give.
- b12 poster: backward failure framing changed confidence in Exp 1 but not in Exp 2.

## Weak spots
- Core premortem evidence is small, mostly students, no effect sizes, nothing on plan outcomes.
- The 30% claim is propagated through citations without primary check.
- No LLM premortem study was actually read.
- Self-correction results are on GPT-3.5/4-era models; reasoning models may differ.

## Seen only in snippets
Veinott 2010 detail, Gallop 2016, Peabody (abstract), b12 poster; a10 and a11 from memory only.

## GAPS
1. What does Veinott and Lehman (2024) find when LLMs do a premortem, and did the LLM causes match human ones?
2. Does a failure-frame prompt beat a plain "list risks" or Retry prompt on current reasoning models at equal tokens, scored by confirmed flaws?
3. What is the true Mitchell 1989 effect: N, test, and was reason quality measured?
4. Do premortem causes verified by code or tools improve the final answer versus unverified ones?
5. Does a premortem shift LLM confidence (P(True)) and in which direction does accuracy move?
6. Is the effect due to certainty of failure, to safe dissent, or to extra generation (promortem controls)?
7. What are the numbers in Hill 2012 and Park, Lu, Hedgcock 2017 (forward vs backward planning)?
8. How diverse are repeated premortem samples from one LLM, and does sampling several scenarios beat one?
9. Did Roose, Lehman, Veinott 2023 (game teams) and Zhang 2024 show any premortem benefit?
10. Does the premortem help only on complex, unfamiliar plans (Peabody Exp 3) and waste tokens on easy ones?

## Gap search results

Evidence in evidence_d.jsonl (d01-d19). Claims K01, K02, K05-K08, K19, K21 edited; K22-K29 added.

| Gap | Status | What was found |
|---|---|---|
| 1 Veinott and Lehman 2024 | Open | Abstract read: qualitative comparison of student vs ChatGPT-4 failure reasons. No results on any open page; Springer is behind a login wall (d01, d02). |
| 2 Failure frame vs plain risk list at equal tokens | Open, one partial lead | No reasoning-model test found. InvThink (safety task) beat a plain safety instruction at similar tokens: harmfulness 2.19 vs 2.62 vs 3.22 zero-shot (d10). |
| 3 True Mitchell 1989 effect | Partly closed | Abstract read: Exp 1 found time direction had little effect; outcome certainty drove longer, more episodic explanations. No +30% in the abstract; N and tests still unread (d03). K01 now contested. |
| 4 Verified vs unverified causes | Open, indirect | Audited-gate paper: self-labelled "verified" gave no benefit, harness-audited gave +0.114 [0.019, 0.208], n=55 (d17). Not a premortem test. |
| 5 Confidence (P(True)) shift | Open | No study found (d18). |
| 6 Certainty vs safe dissent vs extra generation | Open, leaning null | InvThink forward-vs-inverse SFT control was a null (d11, low power). Hill 2012 shows unpacking any scenario set inflates probability, a rival mechanism (d05). A human study shows what-if prompts feel helpful but do not measure better (d15). |
| 7 Hill 2012 and Park 2017 | Hill closed, Park half open | Hill 2012 is NOT a premortem study (support-theory unpacking, N=32, F(1,28)=4.753, p=.038, 11 of 32 showed the effect) (d04, d05). Park abstract read: backward planning wins, mostly on complex goals; no numbers; a corrigendum exists (d06). |
| 8 Diversity of repeated samples | Open | No study found (d18). |
| 9 Roose 2023 and Zhang 2024 | Closed (no benefit shown) | Roose: 10 teams, n=68, 17.8 reasons and 16.7 mitigations per team, few revised plans, no control (d07). Zhang 2023: N=622, future perspective and wise reasoning in conflicts, not a premortem (d08). |
| 10 Only complex unfamiliar plans | Partly closed | Peabody abstract: Exp 2 (N=72) similar counts vs worst-case; Exp 3 (N=82, complex unfamiliar) more reasons. Thesis dated 2017, not 2022 (d09). Counts only; no token-cost data. |

Corrections to earlier notes:
- b08 and others cite Hill 2012 for reduced overconfidence; the paper did not test a premortem.
- Peabody date is 2017 per the repository page.
- New LLM items: InvThink (arXiv 2510.01569) and AUGUR (preprint, +5.01/+4.28/+5.66 over GRPO) are trained methods, not prompt-only scaffolds. arXiv 2610.02740 "Prospective Hindsight" is a name collision (RL), not a premortem.

Still blocked: Springer full text, Peabody PDF (bot check), Sage and preprints.org (403), arXiv API (429). Gaps 1, 2, 4, 5, 6, 8 need our own equal-token experiments.
