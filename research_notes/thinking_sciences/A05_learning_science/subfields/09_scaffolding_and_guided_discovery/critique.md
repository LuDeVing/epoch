# Critique: A05.09 Scaffolding and guided discovery (cross-check)

## Re-checked this session
Abstract text re-opened (arXiv abstract pages or Crossref) for:
- Zhou et al. (2023) least-to-most: SCAN at least 99% with 14 exemplars vs 16% chain-of-thought. Confirmed (a22, b16, c19).
- Zhang et al. (2025) Scaf-GRPO: AIME24 +44.3% relative over vanilla GRPO on Qwen2.5-Math-7B. Confirmed (c01).
- Bastani et al. (2025) PNAS: +48% (GPT Base) and +127% (GPT Tutor) in practice; -17% for GPT Base on the later unaided exam. Confirmed (a25, b10, c12).
- Wang et al. Tutor CoPilot: +4 pp mastery, +9 pp for lower-rated tutors, $20 per tutor per year. Confirmed.

## Corrections
1. Tutor CoPilot sample size. The current arXiv abstract says 900 tutors, 1,800 K-12 students and 550,000+ messages. b14, c14 and c-file text say "700+ tutors, 1,000+ students, 350,000 messages" (an earlier version). a29 says 900 tutors assigned, 783 analysed. Use: 900 tutors / 1,800 students / 550,000+ messages in the latest version; the headline +4 pp and +9 pp are the same in both versions.
2. b21 (Alfieri) was "from memory, unverified" with "164 studies". a15 and a17 (opened) give 108 + 56 = 164 studies, so b21 is consistent; prefer a15-a17 for all numbers.
3. GSM8K chain-of-thought baseline appears as 60.87 (a24) and 60.97 (b16, c19). Both are in the file for one paper; unresolved. Treat as about 61%.
4. Kestin N. N = 194 students in a crossover; group sizes 142 vs 174 appear because each student sits in both conditions (one per lesson), not because N differs. Do not read 142/174 as separate samples.
5. Klahr and Nigam 77% vs 23% (a04, b25) is unverified in both files (from memory/secondary). Treat as approximate.
6. Wood, Bruner, Ross 1976 numbers (30 children, ages 3-5) were not read in the paper itself (a01, b26 from secondary summaries).

## Contradictions between sources
- Fading: Belland 2017 (a20) finds no moderator difference; Kim 2018 (b02) finds fade-and-add best (g 0.59 vs 0.43/0.44, intervals overlap heavily); Belland 2015 (cited) finds unfaded better. Overall: contested.
- Self-selected fading (b03, g 0.52) vs performance-adapted (g 0.43) is within overlapping credible intervals; not a firm ranking.
- Restricting AI access: small guided-use study (b15/c16) positive for no-help quizzes; a larger preregistered study (c17, N=334) found no benefit from forced independent-first study and unrestricted access was slightly better. Different designs (rules on stepwise help vs read-first), so not a clean contradiction.
- Wood, Wood, Middleton contingency effect: failed to replicate (a03), but Belland-style meta-analyses still show scaffolding helps on average. The theory's core mechanism (contingency) has weak direct support; the average effect has strong support.
- "Discovery fails" (Alfieri d -0.38) vs "inquiry works" (Lazonder and Harmsen, d 0.50-0.71, b20 snippet only): reconciled by guidance, as both papers say.

## Weak spots
- Most human evidence is on children or university students in STEM; effects are on tests, not on open reasoning.
- Meta-analytic scaffolding effects have wide credible intervals (Kim 2018 g 0.385, CrI 0.022 to 0.802).
- LLM learning studies measure human learners, not the model. Only Zhou (least-to-most), Scaf-GRPO, QuestA and SEELE test scaffolding on the model itself, and the RL ones use hints at training time, not at inference.
- Zhou numbers are from code-davinci-002; no check that they hold on current models. GSM8K gain is tiny (1.5 points).
- Learner-side scaffolding studies (Kestin, LearnLM Eedi) are single-site, short-term, with human in the loop in some cases.
- Hint quality: a third of ChatGPT hints faulty (c18), so scaffold errors can mislead.
- Small studies: b15/c16 (37 analysed, not randomised), b12/c15 (33 dyads).

## Only seen in snippets or from memory
a01, a02 (1976 paper), a12 (Hmelo-Silver 2007), b20 (Lazonder and Harmsen), b21-b28 (written from memory), c23, c24 as separate entries. Claims resting only on these are flagged single-source.

## GAPS
1. Does decompose-then-solve (least-to-most) still beat plain chain-of-thought on current reasoning models at equal tokens, and on which task types beyond length generalisation?
2. Is contingent (adaptive) support better than fixed support for an LLM agent at equal tokens, given the failed 285-child replication of the original contingency result?
3. Does fading or withdrawing scaffolds across a stream of items help a model (or its memory) later, and is "fade only after success" better than a fixed schedule?
4. What is the best hint level for inference-time scaffolding (knowledge, plan, solution), and does a 50%-success dosage rule carry over from RL training to prompting?
5. Does scaffold benefit reverse for strong models (expertise reversal)? Measure scaffold on/off across model sizes and reasoning-mode models.
6. How should the agent verify its own hints and plans, given a third of LLM-written hints are wrong and majority voting fixes most of it? What is the token cost?
7. Does an answer-withholding rule (hint before answer, no copying) improve later unaided performance for an agent using carried memory, as in the Bastani crutch effect?
8. Is code-enforced step sequencing (Kestin) better than prompt-only sequencing for the schema's state machine, and at what token cost?
9. When should the agent stop probing and tell (escape rule), given the frustration cost of withholding answers?
10. Do the exact 1976 and Klahr and Nigam numbers and the Smit Bayes factors hold when read in the full text (not yet opened)?

## Gap search results (evidence_d.jsonl, d01-d16)
Limits: the shared search budget ran out after 5 searches, and arXiv, Semantic Scholar and OpenAlex rate-limited many calls, so coverage is thinner than planned.

1. Decompose-then-solve on current models: OPEN. No current-model test of least-to-most was found. Full text of Zhou (d01) fixed the numbers: GSM8K 62.39 vs 60.87 (the 60.97 in the prose is a typo in the paper), CoT better on 2-step problems (76.68 vs 74.53), least-to-most better only at 5+ steps (45.23 vs 39.07), DROP +7.7 and +13.9 points. Indirect: generic CoT adds little on reasoning models (d02, d05), though d04 disagrees.
2. Contingent vs fixed support for an LLM: PARTLY CLOSED for experience, OPEN for learning. One within-subject study (d09, N=131 adults) favours a contingent tutor on frustration and answer give-away; it has no delayed unaided test and no equal-token control.
3. Fading across an item stream: OPEN. No study found (d09, d10 log fading but test no outcome). Fade-after-success vs fixed is untested for models.
4. Best hint level: PARTLY CLOSED. Inference-time prefix hints rise broadly with length, 80.6% of GSM8K items need none (d07); next-step hints help small models (d08). The 50% rule is a training-time result (d16) and is not shown for prompting. Knowledge vs plan vs solution level is still not compared head to head.
5. Expertise reversal for strong models: CONTESTED. Generic CoT/exemplars give ~0 on reasoning-mode or strong models (d02, d03, d05) but help distilled reasoning models in 72% of cases (d04) and hints lift them (d08). Depends on task difficulty and model size; needs our own on/off test.
6. Verifying own hints: PARTLY CLOSED. Self-review without an outside signal does not help and often hurts (d06); vote over fresh samples beats debate at equal responses (88.2 vs 83.0 at 9). Cost is N times tokens; no hint-specific cost number found.
7. Answer withholding and later unaided performance: OPEN for agents. Human result re-read (d12): guardrails remove the -17% harm but add no unaided gain. No agent-with-memory test.
8. Code-enforced vs prompt sequencing: OPEN. Kestin full text (d11) states the prompt-only failure as an observation; no ablation, no token cost.
9. Escape rule: OPEN. No measured test; d09 is the nearest.
10. Exact numbers: NOT CLOSED. Wood-Bruner-Ross 1976, Klahr and Nigam 77/23 and Smit Bayes factors could not be opened (d13-d15). Flags in the earlier corrections stay.

Other corrections: GSM8K baseline is 60.87 (table). Kestin effect: 0.63 SD from regression, 0.73 to 1.3 SD from quantile regression; median AI time 49 min. Bastani GPT Base answered correctly only 51% of the time. Claims K12, K14, K15 reworded; K23-K28 added (K27, K28 status open).
