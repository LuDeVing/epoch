# Critique: A07.05 Three attention networks (cross-check)

## Corrections and confirmations (sources re-opened this session)
Confirmed against full text:
1. Fan, Wu, Fossella, Posner 2001 (a02): means 40/56/80 ms, RT 498; retest .36/.41/.81 (session means .53/.58/.90); MZ/DZ r .465/.375 for alerting. Confirmed.
2. Hedge et al. 2018 (b01/b02): Stroop RT cost ICC .60 and .66; flanker congruent .74, incongruent .66; go/no-go commission .76 both studies. Flanker RT cost ICC .40 (Study 1) confirmed; SEM 15 ms confirmed. CORRECTION/ADDITION: Study 2 flanker RT cost was .57, not .40; the evidence line gave only Study 1, so "flanker cost ICC .4" overstates the unreliability slightly when both studies are pooled. The table text extraction interleaves columns, so which row is flanker vs Stroop was cross-checked against the prose.
3. McConnell and Shore 2011 (b07): N=588, r .07/.01/-.04 confirmed.
4. de Langis 2025 (a18): Llama-3.1-8B incongruent .471 to .910; Qwen2-32B .638 to .985 confirmed in Table.
5. Patel, Wang, Fan (a16/b23): 91/57/22/15 and 76/24 confirmed in text.
6. Wang et al. 2025 VLM conflict (c01): 0.852 vs 0.567, diff 0.285 confirmed.
7. Hu 2026 (c09/c10): 0.9644 vs 0.5676, CI, 0.8829 and 0.7864 confirmed.
8. Teker 2026 (c06/c07): 97.8% (88/90 incongruent images, so "100 images" includes 10 congruent), 99.5% vs 15.9%, 31.1% vs 60.0% confirmed.
9. Zhao 2026 WCIT (c12): 6.3%, 38.4%, 21.6%, 51.9% [35.4, 66.8] confirmed.
Not re-opened: a05 Rueda 2004 table (the earlier reading was flagged garbled; treat the child/adult score numbers as unverified), a01 Fan 2002 (abstract only, paywalled), all a12-a15, a22, a24-a27, b20-b22, c25-c27.

Other corrections:
- a16 and b23 (PNAS Nexus 2026 and bioRxiv 2025) are the same study; counted as one source. a17 (PsyPost) is a press report; its 1% and 10% figures match the mixed-list condition, not the pure-incongruent one. Do not quote them as pure Stroop.
- a07 and a27: MacLeod 2010 values (.38/.55/.81) are second-hand. The local file macleod.txt is actually McConnell and Shore 2011, not MacLeod.
- b09 and b10 are the same paper; b01-b03, b13-b15, b17-b18, b23-b24 are repeated lines from single papers. Source count is lower than line count.
- a04 N=30, a05 and others: effect sizes are subtraction scores in ms, not standardized.

## Contradictions between sources
- Independence: Fan 2002 and McConnell 2011 find uncorrelated scores; Wang 2014 finds executive-orienting r=.44 with a new scoring method, and Wang 2015 finds A-O r=-.31. Scoring method drives the result.
- Interactions: present in adults (Fan 2009), absent in children (Rueda 2004). Inhibition of return usually vanishes in ANT.
- Alerting reliability: .35-.60 (literature) vs .684 (Wang 2015 mixed design). Design changes, not the construct, may explain it.
- LLM Stroop: GPT-4o collapse in pure lists (15% at 40) but Gemma-2-2B has 100% accuracy and only a probability cost (Hu 2026); text vs vision models differ in what "conflict" means.
- Flanker cost vs Stroop cost correlate weakly: tasks labelled "executive control" may not share a construct.

## Weak spots
- The agent relevance is background only. No study runs alerting and orienting on an LLM; "executive control" results are simply Stroop/flanker.
- Most LLM numbers are single studies with accuracy only, manual scoring, 30 trials per cell, and no confidence intervals (Patel).
- Prompt wording moves ink accuracy 24% to 97% (Teker), larger than most model differences. Many LLM "deficits" may be prompt artefacts.
- Gains from reasoning (de Langis) are not compared at equal tokens.
- Twin heritability rests on 52 pairs with wide intervals.
- ANT numbers are mostly young WEIRD samples; cross-cultural RT differences up to 110 ms (a11) mean absolute ms values do not transfer.

## Seen only in snippets or secondhand
Fan 2002 (abstract), Posner and Petersen 1990, Corbetta and Shulman 2002, Dosenbach, Callejas 2004, Ishigami and Klein 2009/2010, MacLeod 2010, Johnson 2008, b21 (ADHD meta-analysis), b22 (bilingual meta-analysis), Cohen 1990, Botvinick 2001.

## GAPS
1. Does an explicit "ink only" verification pass beat plain prompting on Stroop/flanker lists at equal total tokens (de Langis and Patel never matched tokens)?
2. How much of the LLM Stroop collapse is prompt phrasing vs capacity? Teker shows a 24-97% range; no sweep exists for text LLMs.
3. Is there any LLM test of alerting (a warning cue speeding or helping response) or orienting (valid vs invalid cue)? Likely none; a cue-validity probe in prompts is untested.
4. Do reasoning models (o-series, extended thinking) close the long-list Stroop gap? Patel supplement had only n=5 per model.
5. Does S2A-style context rewriting keep its gain once rewrite tokens are counted, and on frontier models?
6. What are the exact Fan 2002 and Rueda 2004 condition RTs (full text unread)? Needed to verify the ANT basis numbers.
7. Do conflict-task scores in LLMs predict anything on real agent tasks (reasoning with distractors, long-context QA)? Reliability paradox suggests weak individual-difference prediction.
8. Is the cost-benefit trade (congruent margin up, incongruent down; Hu 2026) visible in black-box agents' confidence outputs?
9. Do ANT-R and later fMRI findings (Fan 2009/2005) change which network a "monitor" operator maps onto?
10. How many trials per condition are needed for a stable conflict score on an LLM (Kucina: about 420 for humans at r=.8)?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d18). Claims K01, K02, K04, K09, K11-K14, K16, K18 gained evidence ids; K20-K25 are new.

1. Ink-only verification pass vs plain prompting at equal tokens: STAYED OPEN. No study matches tokens. Closest: Shi 2023 (d08), where 20-sample self-consistency gave +11 points micro on GSM-IC but at 20x calls, and de Langis 2025 (d09) where reasoning closes the flanker gap at thousands of tokens.
2. Prompt phrasing vs capacity: PARTLY CLOSED. VLM sweep (Teker 2026, d12): ink accuracy 24-97% by wording; capacity side in small text LLMs (Hu 2026, d16): five vs two rule clauses cuts incongruent probability 0.30. Still no wording sweep for text LLMs.
3. LLM test of alerting or orienting: CLOSED as "none found" (d17, d18), limited search; arXiv API rate limited later in the session.
4. Reasoning models and long-list Stroop: PARTLY CLOSED. Flanker: reasoning closes the gap (0.638 to 0.985) at high cost (d09); mixed in semantic-deception arithmetic (d11: o1 94%, R1 40% at the hardest level). No long-list Stroop test of reasoning models found.
5. S2A with rewrite cost, frontier models: STAYED OPEN. S2A paper admits extra compute, gives no number, uses only LLaMA-2-70B (d06, d07). The instruction-only baseline did not help there but helped older models in Shi 2023.
6. Exact Fan 2002 and Rueda 2004 RTs: HALF CLOSED. Fan 2002 verified from full text (d01-d03): 47/51/84 ms, retest .52/.61/.77, cue x flanker interaction present. Rueda 2004 is closed access and could not be retrieved; its child numbers stay unverified (d04).
7. Conflict scores predicting agent tasks: STAYED OPEN, nothing found (d18).
8. Cost-benefit trade in black-box confidence outputs: STAYED OPEN. Only log-probability evidence: conflict adaptation in 12 of 13 VLMs (d14).
9. ANT-R and fMRI changing the mapping of a "monitor" operator: PARTLY CLOSED. Fan 2009 abstract only (d05): alerting can hurt executive control, validity modulates conflict resolution. Full text unread, no numbers. Interaction means a monitor operator should not be tied to one network.
10. Trials per condition for a stable LLM conflict score: STAYED OPEN, nothing found. Human figure (Kucina, about 420 for r=.8) remains the only anchor.

Corrections to earlier lines: Fan 2002 alerting retest is .52, not .36/.41 (those belong to Fan 2001, a02); the "(.81)" conflict retest in K04 also belongs to Fan 2001, Fan 2002 conflict retest is .77. Wang et al. 2025 "Increasing computation" means parameter count, not test-time compute.
