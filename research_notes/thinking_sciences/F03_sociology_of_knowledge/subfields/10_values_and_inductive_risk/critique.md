# Critique: F03.10 Values and inductive risk

## Numbers re-opened this session (PDF text, pdftotext)
Confirmed: Douglas dioxin counts (10 ng: 20/50 in 1978 vs 9/50 in 1990; 100 ng: 34/50 vs 18/50; $3 million for 200 rats); RiskEval Table 1 (HLE normalised utility gains, e.g. Llama-4-Maverick -0.688 to -0.004, DeepSeek-V3.2 -0.853 to -0.169, GPT-4.1-mini -0.537 to -0.087, GPT-5-nano +0.313); Kalai et al. (t=0.5/0.75/0.9, penalties 1/2/9; 20% singleton bound; WildBench as the one audited eval with minimal IDK credit); Mohri and Hashimoto (30 to 80, 78 to 93, 75 to 95; FActScore 25% to 80% keeping about half of sub-claims); BAS (ECE 49.0 to 84.2%; GPT-4o 11.7% / -5.06 on AIME); Act or Escalate (304 pairs, 201 = 66% overconfident; 64.7% to 87.1%, 62.0% to 78.8%); Yamin et al. (576 cases, 64 emergencies, AUROC 0.88-0.99, about 48% caught at about 10% false alarm).

## Corrections
1. c02 gives "normalized utility with own policy -0.295 to -0.862". Wrong: -0.295 is Qwen3-Next-Think WITH the enforced threshold. Model-own-policy values on HLE run about -0.517 (GPT-5-mini) to -0.862 (Qwen3-Next-Think) in the rows seen.
2. c06 says implicit threshold "53-54% to over 91%". The Act or Escalate text says "53% to over 100%" in one place and p>91% in another. Use "about 53% to 91-92%" with a flag.
3. c02 says consistency 0.119 to 0.492 averaged over penalties >=10. The Table 1 Pol. Con. column matches those endpoints (DeepSeek-V3.2-Think 0.119, Qwen3-Next-Think 0.492), but two Gemini rows are blank in the extracted table, so the true range may be wider.
4. Counting: b10/b11/b25 and c01-c05 are the SAME paper (RiskEval); b12 and c15/c16 are the same BAS paper; b09/b18/c17 are the same Kalai paper. In claims.jsonl independent_sources counts papers, not lines. This lowered several "established" labels to "single-source".

## Contradictions and tensions
- RiskEval says models ignore stated penalties at high stakes; Act or Escalate and Yamin say cost framing plus reasoning does help (GPT-5-mini +22.4 points; ratios 5/10 shift 30-50% of emergencies). Reconciliation: depends on model, reasoning level and penalty size (<=5 fine, >=10 breaks). Not a true conflict but unresolved for our agent.
- Yamin reports Claude Sonnet 5 and Fable 5 shift correctly across reasoning levels, yet recovered ratios differ from stated ones. Prompted ratio is not the same as realised threshold.
- Philosophy side: Dressel and Hatchwell resist the strong Rudner claim; the ML papers assume the decision-theoretic form without engaging this. Rudner's argument is conditional on acceptance being a binary act.

## Weak spots
- All LLM threshold evidence is 2026 preprints, mostly one study each, none replicated. Two (arXiv 2608.*, 2609.*) are very recent.
- Mostly verbalised confidence on QA benchmarks; little on open-ended scientific claims, which is Rudner's actual setting.
- No human behavioural data on threshold shifts (claim K19).
- "Value-laden" in the LLM papers means a stated numeric penalty, not contested social values. The sociology-of-knowledge content (whose values, legitimacy) has no LLM test.

## Seen only in snippets or not opened
a05, a12, a13, a14 (Hempel, Jeffrey, Levi, Henschen via secondary text); b08, b21, b22; c19, c20, c24, c28 (search summaries only; not used for numbers). c26 and c27 did not mention inductive risk.

## GAPS
1. Does a code-enforced cost threshold beat model self-applied thresholds on our agent at equal tokens, across penalty 1 to 100 (RiskEval replication)?
2. Where does our agent's own policy consistency collapse (which penalty), and does the schema's reasoning stage move that point?
3. Does verbalised confidence from our agent carry enough signal to threshold at all (AUROC vs ECE), and does isotonic recalibration on its own runs hold across domains?
4. Does a mirror test (raise FN cost, then FP cost) pass for our agent, and how does it vary with phrasing?
5. How many calibration items does a conformal claim filter need for our agent before coverage variance (sd 0.09 seen at small n) is acceptable?
6. Do humans (scientists, analysts) shift acceptance thresholds with stated error cost? Any behavioural study, to set a human baseline.
7. Can inductive-risk disclosure (naming which error was traded and who bears it) improve user decisions, tested with blind raters?
8. Does the effect of cost framing plus reasoning replicate for Claude-family models, and does it survive when evidence is open-ended claims rather than multiple-choice QA?
9. How should thresholds be chosen when losses are unknown or contested (Manski minimax regret vs maximin) and can an LLM apply it reliably?
10. Does test-time compute raise accuracy at a high threshold enough to pay for itself in abstentions, at equal total tokens?

## Gap search results
Evidence in evidence_d.jsonl (d01-d16). Search tools were rate-limited (WebSearch budget gone; arXiv, Semantic Scholar and OpenAlex returned 429 for most calls), so coverage is thinner than planned.

Closed (answered from literature or maths):
- Gap 5 (calibration size): closed on the maths. Coverage follows Beta(n+1-l, l). For a 90% target sd is 0.063 at n=20, 0.030 at n=100, 0.021 at n=200, 0.009 at n=1000. A 99% target is vacuous below n=99. The earlier sd 0.09 matches n of about 10. Cascade work used 1,275-1,500 calibration items per dataset (d01-d03, d12). Not measured on our agent.
- Gap 9 (unknown or contested losses), theory side only: Manski gives explicit maximin and minimax-regret rules (d10). Whether an LLM applies them reliably is still untested, so partly open.

Partly answered:
- Gap 3 (does verbalised confidence carry signal): mixed. Claude Sonnet gave AUROC 0.937 on easy TriviaQA (99 items) but phrasing flips 4-9% of decisions at 0.8 (d08). Small Qwen models showed near-zero agreement across formats (d04). ECE misleads; resolution matters (d05). A constant-confidence setting gave AUROC 0.500 and all-defer at break-even (d07). Own-agent AUROC still unmeasured.
- Gap 4 (mirror test): no mirror test on Claude found. Negation-coherence evidence (d09) gives a cheap label-free precondition.
- Gap 6 (human baseline): one behavioural null found: offence seriousness did not shift BRD interpretation or verdict, N=118 (d14). Abstract only. No study of scientists found.
- Gap 7 (disclosure): human survey shows value disclosure never raised trust (d15). Error-trade disclosure with blind raters not found.
- Gap 8 (Claude family, open-ended claims): only a Sonnet row on easy QA (d08) and a Haiku row on ticket routing (d07). Open-ended claims untested.
- Gap 10 (test-time compute at a threshold): replay of 19,200 traces shows compute converts some abstentions to answers, but no penalty-weighted, equal-token test (d13).

Still open (need runs on our agent): gap 1 (code gate vs self-applied threshold at equal tokens, penalty 1-100), gap 2 (penalty where policy consistency collapses, and the schema's reasoning stage). d11 adds that a pending state moves along the threshold frontier rather than beating it.

Not opened: Simon and Mahan 1971 and the earlier acquittal-bias studies (JSTOR/Taylor and Francis blocked); Pauker and Kassirer full text (403). New claims K21-K26 added; K13, K15, K19, K20 updated.
