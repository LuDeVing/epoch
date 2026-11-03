# Critique: Bayesian models of cognition (C03.01)

## Numbers re-opened this session (10)
1. Qiu et al. Fig 2 (arXiv 2503.17523): Bayesian Assistant 58% after round 1, 81% final; random 37%; Gemma 2 9B 37%, Llama 3 70B 45%, Gemini 1.5 Pro 51%. CONFIRMED. New nuance (appendix): when simulated users are filtered to human-like preferences, Gemma Original reaches about 60%, not 37%. The LLM deficit depends on how typical the preference is.
2. Qiu: Bayesian-tuned agreement with the Assistant "around 80%". CONFIRMED (text). The 75-76% accuracy figures stay figure-read only.
3. Xie et al. (2111.02080): 81% to 85% from 12 to 16 layers at validation loss 1.33. CONFIRMED (table row 81.2 +/- 7.1).
4. McCoy & Griffiths (2305.14701): perplexity 19.67 vs 19.75 (p<1e-20), 19.69 earlier Transformer, 24.4 5-gram. CONFIRMED.
5. McCoy et al. Embers (2309.13638): cipher 51% vs 13%; reversal 97% vs 53%. CONFIRMED.
6. MMToM-QA (2401.08743): BIP-ALM GPT-J 75.3, LLaMA 2 76.7, GPT-4V 44.0, human 93.0 multimodal; human text 82.5. CONFIRMED.
7. Ellis (2306.02797): R2=0.95 appears for the number game; logical concepts R2=.81 with 100 proposals per batch. CONFIRMED.
8. Griffiths & Tenenbaum 2006: groups 208 and 142; pharaoh follow-up 35 students, median 30 years, b=17.9 vs true about 9.34; exponent 2.43. CONFIRMED.
9. G&T 2006 domain count. CORRECTED: evidence b01 says "5 of 8 analysable domains" and a01 says "5 empirical-prior domains". The paper states no such count. Marriage was dropped (52% answered "forever"). Eight domains were analysed; six use empirical priors without tuning (grosses, poems, lifespans, run times, House terms, cakes), pharaohs needed a subjective scale parameter, waiting times used a fitted prior. Claim K01 uses the safer wording.
10. Falck et al. (2406.00793): the martingale framing and model list are CONFIRMED; per-model closeness to Bayes (Mistral-7B, GPT-3-170B closest; GPT-4 the Bernoulli exception) comes from figure text and was not re-derived. Evidence a11 and c13 differ on which model is the exception in the Gaussian task (a11: clear deviations generally; c13: all except GPT-3.5). Unresolved.

## Contradictions between sources
- Rich prior vs 2-sample memory: Mozer et al. 2008 (Min2 fits group medians; humans more variable than k>1 models) versus Lewandowsky et al. 2009 (iterated-learning chains converge to real priors). Vul et al. 2014 partly reconcile: each person acts on one sample from a rich posterior. Contested.
- Binz & Schulz: a15 says GPT-3 treated the base rate as irrelevant "like people"; b19 and c19 say it answered the cab problem near-correctly (20%). Read: no base-rate neglect. Disregard the a15 wording.
- ICL Bayesian or not: Xie (theory, synthetic) versus Falck (martingale violations in real LLMs). Compatible only if "approximately Bayesian" is allowed.
- Qiu: prompt fixes fail, yet AdaptFuse (training-free) works by moving the posterior into code. Consistent: the failure is carrying the arithmetic in text, not the model's likelihood judgments.

## Weak spots
- Most strong LLM results come from one research family (Griffiths, Tenenbaum, Ellis, Andreas labs); independence is lower than the counts suggest.
- Qiu et al. is one task family (flights, hotels, shopping) with simulated users. Many LLM claims are single-source.
- Zhu & Griffiths priors are compared with humans by eye, no fit statistic.
- Xie et al. results are on small synthetic models.
- Critiques (Jones & Love, Marcus & Davis, Tauber, Sanborn & Chater, "myth of the Bayesian brain") are abstract-level; only Bowers & Davis has text-level detail (c18). Perceptual cue-combination replications and suboptimality reviews were not opened.
- Xu & Tenenbaum 2007 numbers are second-hand.
- Batista & Griffiths (c07), Liu et al. (c20), Piriyakulkij (c22) and AdaptFuse (c06) were not independently re-opened (Semantic Scholar rate-limited; arXiv search returned empty).

## Seen only in snippets or from memory (opened:false)
a18-a23 (Ernst & Banks, Jones & Love, Bowers & Davis, Tenenbaum 2011, Kemp & Tenenbaum 2008, Chater 2006); b07-b12; the 2026 "Heuristic-Anchored Bayesian Sampler" and 2025 "myth of the Bayesian brain" abstracts.

## GAPS
1. Does a code-held posterior (LLM supplies likelihoods) beat chain of thought and self-consistency at equal tokens on tasks beyond the flight/hotel family, e.g. diagnosis or rule discovery? (AdaptFuse is one preprint.)
2. How many independent samples per item pay off at equal tokens for LLMs (Vul et al. one-sample result transferred to an agent)? Are LLM samples correlated enough (G4) to break the analogy?
3. Can an agent's own prior be audited cheaply before it answers (iterated-ICL elicitation), and does correcting it help on tasks with low-probability correct answers (Embers)?
4. Reference-class estimation: does naming the reference distribution first improve current-model predictions in the Griffiths-Tenenbaum paradigm? No direct study found.
5. Has any pre-registered Bayesian vs rival-model comparison, with priors fixed in advance, been run on LLM behaviour (2023-2026)?
6. Does martingale-violating (order-sensitive) behaviour persist in current frontier reasoning models, and do reasoning traces reduce it?
7. Do priors learned on earlier problems (overhypotheses, memory) transfer to later problems for an LLM agent, and by how much?
8. How does belief-updating accuracy vary with prior-typicality of the case (Qiu appendix), and does a step that flags atypical cases help?
9. Sycophancy as confirming evidence: does a disconfirmation-seeking probe step reproduce the discovery gain with agent-generated tests rather than human participants?
10. Is expected-information-gain question selection (LIPS, OPEN) better than simple diverse question sampling at equal tokens?

## Gap search results (gap searcher, 2026-11-03)
Search budget: WebSearch was exhausted by the shared session budget; arXiv API, OpenAlex and Semantic Scholar were rate limited. Work was done by opening arXiv PDFs directly (18 evidence lines in evidence_d.jsonl, all opened). Claims K09, K10, K11, K12, K13, K15, K19, K21 updated; K23-K26 added.

1. Code-held posterior vs CoT / self-consistency beyond flights: STAYS OPEN. AdaptFuse v2 (2604.03925, Oct 2026) still tests only flights, hotels, web shopping, admits the comparison is not equal-information and has no symbolic-only baseline; margin over Bayesian Teaching shrinks 2.8 to 0.6 points without its EMA step (d09, d10). UoT (d05) is a related method on diagnosis and 20Q, partial support at equal tokens.
2. Samples per item and correlation (G4): CLOSED, against the analogy. LLM errors are highly correlated (60% agreement when both wrong, 71 models, d12); voting plateaus while coverage keeps rising (d11); vote can decline on hard queries (d13); self-consistency saturates quickly (d14). The Vul one-sample result does not transfer. Open detail: correlation among samples of the same model was not measured directly.
3. Auditing own prior and correcting it: HALF CLOSED. Verbalised priors can be elicited (d15) but are unvalidated and no correction experiment exists. o1 still shows probability sensitivity (d18).
4. Reference-class estimation in the Griffiths-Tenenbaum paradigm: STAYS OPEN. No direct study found (search tools were limited).
5. Pre-registered Bayesian vs rival comparison on LLM behaviour: STAYS OPEN. Nothing found.
6. Martingale violations in reasoning models: CLOSED. Persist in 51 of 54 CoT setups; only DeepSeek R1 clearly lower; debate helps (d01, d02). Caveat: LLM-judge probabilities, 2025 models.
7. Transfer of priors/overhypotheses: STAYS OPEN. Only skill transfer by fine-tuning (d17).
8. Typicality: HALF CLOSED. Measured (37% vs about 60%, d16); no flagging step tested.
9. Disconfirmation-seeking probe with agent-generated tests: CLOSED positively for one task family. 42% to 56% mean, Blicket 0.57 to 0.86 (d03, d04). Single source.
10. EIG question choice vs diverse sampling at equal tokens: PARTLY CLOSED. EIG search beats CoT-SC at equal tokens (d05) but diversity constraints alone gave 39.4% to 80.0% (d08); no matched-token head-to-head exists (d07 has none either).

Note: AdaptFuse 76.2% in claim K09 is the original configuration; its table in the text extract was partly garbled, only the Gemma column was checked against prose.
