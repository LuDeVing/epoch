# D03.04 Non-monotonic and default logic: cross-check critique

Checker pass, 2026-10-26. Sources re-opened from arXiv PDF text (pdftotext) for the ten key numbers. Files: evidence_a/b/c.jsonl, claims.jsonl (K01-K19).

## Numbers re-checked

1. Kirkpatrick and Sterken 2025 (2508.13718), zero-shot table and CoT/few-shot deltas: CONFIRMED (Opus 96.51, 3.5 Sonnet 96.01, GPT-4 0613 93.52, CoT mean -11.14 SD 15.74, deltas -12.62, -18.77, -0.33, -41.52; few-shot +28.74, +25.08, -6.81).
2. DeReLab 2026 (2608.30413): gap 0.935, OR 891 [586, 1498]; 95.4 vs 20.3; 85.1 vs 14.9; Qwen3-32B thinking 0.008 vs 0.670 (0.816 reversed); order effect 0.970 to 0.264; overall 86.0, 83.7, 53.2. CONFIRMED. Note: the Qwen thinking gap 0.008 has Holm p=0.015, "significant but negligible".
3. Belief-R (2406.19764): Llama-3 70B DP 10.99/92.09/51.54, CoT 12.57/89.40/50.99; Mixtral 8x22B 35.38/36.57/35.98, CoT 27.28/34.93; 378 matched queries. CONFIRMED.
4. Huang et al. 2023 (2310.01798): GSM8K/CSQA/HotpotQA tables CONFIRMED; 74.7% keep-first-answer on GSM8K CONFIRMED. The oracle rows are mislabelled "Standard Prompting" by the PDF layout; values (84.3/89.7/29.0, 97.5/85.5/59.0) are the oracle rows.
5. Ishay and Lee 2026 (2604.27960): 59.0/52.9 to 90.5/81.0; average 51.3 to 78.0; 54.6 to 78.0 with revision; SMT 35.8/35.0; BoardgameQA 82.1 vs 60.1, plain 84.7. CONFIRMED.
6. DeFAb (2606.18557): table of six models and 1,054 failures (652/366/36) CONFIRMED. Table has Claude Sonnet 5.5 at 133 direct vs 336 structured: the gap is contract failures (203), not logic.
7. ArgGYM (2609.38409): 1,440 instances, 82.4 percent best, 12.4 to 29.0, 14.4 to 27.3, 28.4 to 39.2, 92.9 vs 71.8, 50.8 to 11.7 CONFIRMED. The paper is inconsistent on names: text says "Gemini 3.8 Flash" and "Qwen3.8-27B", table lists "Gemini 3.1 Pro Preview" and "Qwen3.5 27B". The 82.4 row could belong to either; treat the model identity as uncertain.
8. LogicBench (2404.15522): non-monotonic Avg row 57.78/43.74, 71.00/67.49, 67.78/69.71, 61.47/65.46, 74.43/84.75 CONFIRMED. Column order (model, then yes/no) is inferred from layout.
9. Leidinger 2024 (2406.06590): 650 generics, 260 pairs, p=0.01, >90% and >85% claims located. CONFIRMED in outline; per-model figures not individually re-read.
10. Byrne 1989 and Dieussaert 2000, read through Dietz Saldanha and Kakas (2002.10149) tables: Byrne 96/96/38 (MP), 92/96/33 (MT), Dieussaert 88/93/60 and MT 69/44. CONFIRMED, but still second-hand (original papers not opened).

## Corrections made

- b09: GPT-4 (0613) zero-shot was written as 96 percent and GPT-4 Turbo 93 percent. The paper's table gives 93.52 and 92.69. Patched in evidence_b.jsonl. (a21, b10, c29 already had the right values.)
- Nothing else needed numeric change.

## Contradictions and tensions

- CoT/thinking: hurts strong models in Kirkpatrick (-11.14), does nothing in Belief-R (about 1 point), removes bias in DeReLab's Qwen3-32B, helps in ArgGYM overall but hurts one strict-rule condition. Different tasks, models and vintages; no single rule (K05, contested).
- Format effect: 96 percent on generic one-step items vs 57 to 85 percent on LogicBench rule lists (K01). Likely a format and scoring difference (single-token yes/no vs yes/no with label split), not a true disagreement.
- BoardgameQA 2023 shows steady collapse with conflict; 2026 reasoning models reach 84.7 percent. The benchmark may now be saturated.
- Suppression effect size: 58-point drop in Byrne, 28 in Dieussaert, 60 percent in open answers. Direction agrees.
- a20 (25 of 32 cells correct, about 78 percent) comes from Tachmazidis et al.; b27 and c31 read the same paper as 8 theories x 4 variants with no aggregate. The 78 percent is a count the earlier agent made, not a figure the paper reports. Treat as soft.

## Weak spots

- Founding sources are thin. Reiter 1980 (c23) was not opened; McCarthy is opened, but Reiter, Moore and Lifschitz details come through SEP and Wikipedia (a14, a15, a16 are secondary). Complexity results (Sigma2P) are not tied to Gottlob 1992.
- Byrne 1989, Elio and Pelletier (b28, c22), Han et al. 2024 (c21), Shi/Wang (c25) were seen only second-hand (opened:false).
- Many 2026 preprints (DeReLab, DeFAb, ArgGYM, Ishay and Lee, Jhang) are single-lab, unreviewed and use model names I could not check elsewhere. DeFAb and DeReLab share a group (Sadhu, Marino): not independent.
- Ishay and Lee 2026 and Yang et al. 2023 share an author group.
- No study directly tests "doubt only on a signal" as a scaffold rule. K08 is inferred from the contrast between solver feedback and intrinsic self-correction.
- Nothing found tests Reiter-style default rules written into a prompt versus the same rules in plain language, at equal tokens.
- No test of the 2025-2026 Claude models on Belief-R or the Kirkpatrick set; the Claude numbers are Claude 3 / 3.5.

## Seen only in snippets or second-hand

b01 (Byrne original), b28, b29, c21, c22, c23, c24, c25.

## GAPS

1. Does a "revise only when a defeater signal appears" rule beat "re-check always" at equal tokens on multi-turn default tasks (DeReLab, Belief-R style), and how many false revisions does it cause?
2. How do current Claude and GPT-5-class models score on Belief-R and the Kirkpatrick-Sterken set, with and without extended thinking? Existing numbers are 2023-2024 models.
3. Why does a model that labels an update "weakening" keep the old conclusion (know-but-do-not-output)? Does forcing the conclusion to be restated after the label fix it, and is it an order artefact?
4. Does giving defaults as explicit rules with a specificity ordering (Reiter-style, written in a prompt) beat plain-language generics, with no solver?
5. Does a small ASP/Prolog tool help once models are strong? ASP added nothing on BoardgameQA once plain reasoning reached 84.7 percent; where is the break-even and what does tool use cost in tokens?
6. When two defaults conflict and neither is more specific (Nixon diamond), what do LLMs do, and does a "skeptical: withhold" instruction help or just cause refusals?
7. Does the rule-memory update used by ExpeL (upvote on success, downvote on exception) work for exceptions to defaults, or does it just count frequency? Is there a test on exceptions learned from a single case?
8. What is the false-positive cost of defeasibility: if the agent treats every rule as defeasible, how often does it drop a correct conclusion on an irrelevant fact (Leidinger: irrelevant exemplars cut agreement below 50 percent)?
9. Human data: do experts or non-experts retract more like Byrne's suppression pattern or like a classical reasoner, and does the human size of effect (28 to 58 points) predict LLM error on the same items?
10. Can the original Reiter and Pelletier-Elio human default-inheritance results be opened and compared with LLM behaviour on the same puzzles?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d18; 16 opened, 2 snippet-only). Claims K20 to K25 added; K02, K03, K05, K12, K15, K16, K19 extended. Scratch work was under D:/research_scratch/D03.04 (PDFs read there).

Status per gap:

1. Gated revise vs re-check-always at equal tokens: STILL OPEN, but better bounded. No study ran the comparison. Indirect: unconditional "Are you sure?" cost 17 points on average (FlipFlop, d10); an exception-aware prompt on Opus 4.6 traded 3 fewer misses for 20 false positives (d02); with a clean irrelevant update strong models revise wrongly about 1 percent (DeReLab, d05), small ones 15 to 36 percent. DeFAb v2 plans the feedback-and-cost study but has not run it (d16).
2. Current Claude and GPT-5 on Belief-R and Kirkpatrick-Sterken: STILL OPEN for those two sets (nothing found). PARTIAL: Opus 4.6/4.7, Sonnet 4.6 and GPT-5.4 are at ceiling on single-level exceptions but fail nested chains in some cells, with March-to-April drift (d01, d03; vendor paper). DeReLab has GPT-5.1 and GPT-5-mini but no Claude (d04 to d06).
3. Why label without revising: MOSTLY CLOSED. It is partly a question-order effect. The entailment question first scaffolds the label; label first made the label and the conclusion worse (d04). Restate-after-label is untested and the nearest evidence argues against it. Only open Gemma and Qwen models were order-tested.
4. Explicit specificity rules vs plain generics: STILL OPEN. Explicit priority rules reach 63 to 86 percent on HOLMES law (d09) but there is no plain-language arm; the exception-aware prompt result (d02) is a warning.
5. ASP/Prolog tool break-even: PARTIAL. Models alone are weak at computing answer sets (ASPBench, d13) and a rule engine still beat Claude and GPT-5.4 on nested exceptions (d03, vendor). Plain reasoning models already match ASP on BoardgameQA (b15). Break-even is by task type (enumerating extensions or deep chains vs picking one winner). Token cost of a tool call: not measured anywhere I found; only GPT-5.4 at about $0.02 and 2 to 5 s per scenario (vendor claim).
6. Nixon diamond: STILL OPEN. Only an aggregate score exists (d14). No skeptical-withhold test. A search summary claim about abstention was wrong (d15); do not use.
7. ExpeL upvote/downvote for exceptions: CLOSED (negative). The update is a count (start 2, drop at 0), not an exception writer; no exception or single-case test exists (d12).
8. Cost of defeasibility: PARTIAL. Measured false revision is low for strong models on clean irrelevant updates (d05, d07) but irrelevant context still erodes multi-step reasoning (GSM-DC, d11) and the exception-aware prompt created 20 false positives (d02). Leidinger's below-50-percent agreement (c07) was on generics with irrelevant exemplars and has no 2026 retest.
9. Human effect size vs LLM error per item: STILL OPEN (d18). No large replication of Byrne found; no item-level link.
10. Reiter and Pelletier-Elio human data: STILL OPEN (d17). Repository pages returned 403 and the Synthese paper is paywalled; snippet only.

New cautions for the main synthesis:
- Several 2026 sources are vendor or single-group preprints (Aethis, DeReLab/DeFAb group, DeltaLogic workshop). Confidently Wrong withdrew one finding itself (GPT-5.4 low effort 7/11 became 11/11).
- DeFAb has a v2 (23 Oct 2026) whose abstract differs from the v1 numbers a search summary quoted (65 and 23.5 percent); K16 follows v2 and the earlier c09 line.
- Belief-R appendix row labels were partly lost in text extraction (d08); only printed rows are quoted.
- Reiter-style conclusions about "doubt only on a signal" remain inferred, not tested; K20 and K21 give the nearest direct numbers.
