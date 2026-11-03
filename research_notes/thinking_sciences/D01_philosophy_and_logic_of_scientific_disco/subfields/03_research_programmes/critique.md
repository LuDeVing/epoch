# Critique: D01.03 Research programmes (cross-check)

## Sources re-opened this session (PDF text via pdftotext, numbers checked)
Huang et al. 2310.01798 (Tables 2, 3, debate vs self-consistency), Olausson et al. 2306.09896 (Table 1, human study size), Shinn et al. 2303.11366 (Table 1 and test-reliability table), Wang et al. 2501.18585 (225%, TIP table), Beel et al. 2502.14297 (edit sizes, 42%, 57%), Tsui 2507.02778 (64.5%, 89.3%, 76.0%, 5,306), Chen et al. 2412.21187 (48.6%), Kumar et al. 2409.12917 (15.6, 9.1), Yamada et al. 2504.08066 (3 of 43), Zhou et al. 2404.04326 (31.7, 13.9, 3.3, 24.9).

## Corrections made
1. b14 (Huang, oracle row) was wrong. Table 2 gives GPT-3.5 with oracle labels: GSM8K 75.9 -> 84.3, CommonSenseQA 75.8 -> 89.7, HotpotQA 26.0 -> 29.0. The line said GSM8K 75.9 -> 95.5 and HotpotQA 26.0 -> 49.0. Those are GPT-4 baseline numbers (95.5, 49.0). GPT-4 oracle (97.5, 85.5, 59.0) in c02 is right. Claim K07 carries the corrected values. The raw evidence files were left unedited; use K07 over b14.
2. b14 gives "GPT-4-Turbo GSM8K 91.5, 88.0, 90.0". Only 91.5 (standard) and 90.0 (5 calls) were seen in the text layer; the 88.0 was not confirmed.
3. SCoRe (b21): the 15.6 and 9.1 are absolute gains in the self-correction metric, on different models (Gemini 1.0 Pro for MATH, 1.5 Flash for HumanEval), not "over base Gemini models" on one model. Wording fixed in K08.
4. Confirmed with no change: Huang CSQA 75.8 -> 38.1 -> 41.8, GPT-4 GSM8K 95.5 -> 91.5 -> 89.0, HotpotQA 49 -> 49 -> 43; self-consistency 82.5/85.3/88.2 vs debate 83.2/83.0; Olausson 33.30/52.60 and 3.67/14.67 with 16 participants, 40 programs; Reflexion 0.80 -> 0.91, MBPP 0.80 -> 0.77, Rust 0.60 -> 0.68, TP/FN/FP/TN values; underthinking 225%, TIP 38.3 -> 44.1, R1 72.4 prompt vs 74.8 TIP; Beel edit sizes 529/118/83/66/21, 42%, 57%; Tsui numbers; Chen 48.6%; Yamada 3 of 43.

## Contradictions and tensions between sources
- Self-correction: Reflexion (b22) reports gains, Huang/Kamoi (b14, b18) report none without oracle. Resolved by signal reliability: Reflexion's own MBPP result (0.80 -> 0.77, false-positive rate 0.16) fits the Huang picture. Kamoi flags Reflexion as using environment signals.
- Overthinking (b24) says later rounds add little; underthinking (c14) says stopping or switching too early hurts. Both are true in different regimes; a stop rule can err in both directions. No source tests a rule that adapts.
- Lakatos "stagnant" (Branahl) vs Feyerabend's waiting objection: the stagnant label formalises patience that Feyerabend calls empty. Contested.
- Olausson: stronger-model feedback helps (b17), but that is cross-model, so it supports "diagnosis is the bottleneck", not self-repair.

## Weak spots
- No direct LLM test of Lakatos's criterion exists in the evidence (c25). All LLM evidence is indirect analogy. Source of c25 is a rate-limited search, so absence is not proven.
- Lakatos primary text (a01-a17) is solid, but everything after it is secondary (SEP, Wikipedia).
- Most LLM numbers are single-study, mostly GSM8K, CSQA, HotpotQA, HumanEval; older models (GPT-3.5, GPT-4). 2025-2026 reasoning-model replications of Huang are missing. HotpotQA test set is only 100 questions.
- The three "independent_sources" counts are my judgement of independence; several Lakatos reviews (SEP, Wikipedia) share one origin.
- Unverified this session: Park/Leahey/Funk 90% disruptiveness drop (c22, via Branahl), Denario passage (c23, summarising fetch), AI Scientist-v2 cap parameters in c19.

## Seen only in snippets or metadata
a28, a29, a30 (metadata only), b12 (Meehl 1990, secondary summary), b13 (EGU abstract), b23 (Self-Refine, no numbers), b25 and b26 (abstracts and intro only), c25.

## GAPS
1. What patch-count or no-progress threshold at S6 gives the best accuracy at equal tokens (1, 2, 3 failed patches), and does it differ for exact-answer vs open problems?
2. Does a "predicts a held-out case" test on each patch (an operational Lakatos excess-content test) separate good patches from degenerating ones better than a plain round cap?
3. Does the Huang no-oracle result still hold for 2025-2026 reasoning models (o-series, R1, Claude thinking) at equal tokens? No replication was found.
4. How reliable must a check be before revision pays? Reflexion shows FP 0.01 helps and FP 0.16 hurts; where is the break-even, and can S0 measure it cheaply?
5. Can shrinking patch size or semantic similarity of successive patches (Beel's 529 -> 21) predict failure in our own transcripts?
6. Is there any published LLM study that labels agent traces as progressive or degenerating in Lakatos's sense (core, belt, novel prediction)? A targeted search of 2025-2026 was not completed.
7. How should "stagnant" (no check available, Branahl) be handled: accept best attempt, or spend budget elsewhere (G12)?
8. How do we stop the agent from abandoning too early (underthinking, 225% token gap) while also stopping endless patching? Does one adaptive rule beat both a fixed cap and a fixed floor?
9. Does keeping the "core" explicitly fixed (task restatement, S1) reduce drift under repeated patches, compared with letting the model rewrite the whole attempt each round?
10. Meehl 1990 (track record before shielding the core): read the primary text and extract any numeric guidance.


## Gap search results (2026-11-03)
Evidence in evidence_d.jsonl (d01-d16). Claims K24-K30 added; K08, K11, K13, K15, K20, K23 updated (K15 now established). Sources opened as PDF text this session: Zhang 2412.14959, Stroebl 2411.17501, Snell 2408.03314, Self-Debug 2304.05128, CRITIC 2305.11738, S* 2502.14382, MAST 2503.13657, Laban 2505.06120, 2509.09677, Liu 2503.20783, s1 2501.19393, Ghosal 2506.04210, Zhang 2504.05419, Denario 2510.26887. Tools limits: arXiv/Semantic Scholar/OpenAlex search were rate-limited; one WebSearch worked, then the budget was gone. Papers were fetched by known ID, so coverage reflects what I already knew, not a systematic search.

1. Patch-count threshold: PARTLY CLOSED. With a real check, 2-3 rounds capture most gain (d06, d07, d08; K25). No study compares caps of 1, 2, 3 at equal tokens, and none splits exact vs open problems. Snell (d05) says difficulty should change the patch-vs-restart choice. Run our own test.
2. Held-out prediction test per patch: STAYS OPEN. Only indirect: model-generated tests added no gain over public tests in S* (d08; K26). The test needs an external verifier.
3. Huang result for 2025-2026 reasoning models: PARTLY CLOSED. o1-preview and o1-mini still lose accuracy without an oracle (d02), smaller drop for o1-preview (4.2 points) than 4o (20.4). R1 and V3 rows could not be read reliably. No equal-token test. Claude thinking not tested.
4. Check reliability break-even: PARTLY CLOSED. Stroebl (d04; K24) gives the cost-benefit form and optimal K about 5 at ratio 4. No universal false-positive threshold, and Reflexion's 0.01 vs 0.16 remains the only revision-loop pair. Cheap measurement in S0 is a design idea, untested.
5. Shrinking patch size predicts failure: STAYS OPEN. No transcript analysis done. MAST (d09) gives a base rate for step repetition (15.7%) but not for edit size.
6. LLM study labelling traces progressive/degenerating: STAYS OPEN. Search found only Denario's philosophical passage (d01) and no labelling study (d16). Not proof of absence.
7. Handling stagnant (no check): STAYS OPEN. No new evidence. Current rule (accept best attempt, spend budget elsewhere) is a design choice. Stroebl's zero-optimal-K case at high false-positive cost supports not looping when no check exists.
8. Adaptive rule vs fixed cap and floor: PARTLY CLOSED. Both errors are measured (d09, d13, d14; K29), and difficulty matters (d05, d13). No head-to-head of an adaptive rule. Probe-based exit (d15) shows a calibrated signal can cut 24% tokens but needs model internals.
9. Fixed core reduces drift: PARTLY CLOSED, contested (K28). Indirect support: models lean on earlier wrong attempts (d10, d11) and re-appending the question helped (d03). Last-attempt-only context was mixed (d08). No direct core-fixed vs rewrite experiment.
10. Meehl 1990 primary text: STAYS OPEN. meehl.umn.edu returned HTTP 403. K23 stays single-source.

Remaining weak points: all new numbers are single-study per claim except the 2-3 round pattern (three code/math studies, all with external feedback); the Dark Side table lost some row labels in text extraction; s1 and Ghosal are math with 30-problem or distilled-model limits.
