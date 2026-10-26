# Critique: A07.04 Attentional capture, bottom-up versus top-down (cross-check)

Checked by re-opening the sources (arXiv PDFs via pdftotext, and earlier saved text of Theeuwes 2004, Lee 2023, Wu 2024, Liu 2023, Chen 2025, Mirzadeh 2024). 23 claims written to claims.jsonl.

## Numbers re-checked (ten plus)

| # | Number | Source | Result |
|---|---|---|---|
| 1 | Theeuwes 2004 Exp 1: 885 vs 950 ms (65 ms), F(1,7)=37.1 | PDF text | Confirmed. |
| 2 | Theeuwes 2004 slopes (b04: "20.55 vs 0.38"; a05: "0.55 and 0.38") | PDF text | CORRECTED. Text prints "20.55 msec/item for no-distractor and 0.38 for distractor". The paper says there was no display-size effect, so the leading "2" is a lost minus sign: slopes are about -0.55 and 0.38 ms/item. b04 is wrong ("20.55"); a05 is right. Fix b04. |
| 3 | Shi 2023 Table 3: CoT micro 72.4 / macro 6.0; CoT+inst 77.8/15.0; LTM 77.5/18.0; LTM+SC 93.4/45.0 | PDF | Confirmed. |
| 4 | Shi: "no more than 18%" (b22) vs "fewer than 30%" (c01) | PDF | Both are in the paper. 18% is the share of baseline-solved problems solved under all distractor types (abstract); 30% is the macro-accuracy remark. Not a contradiction, but the two denominators differ. |
| 5 | Shi: self-consistency +11 micro, 35.5 on 0-shot CoT, 99.7% in the 20 samples, best macro 45% | PDF | Confirmed. |
| 6 | Turpin 2023: -36.3 (GPT-3.5 suggested answer), -30.6 and -24.1/-21.5 few-shot, always-A -18.7/-4.7, 0 of 234 | PDF | Confirmed. Note -36.3 is the maximum over tasks in the text and the average in the table; read "as much as". |
| 7 | Sharma 2023: up to 27% (LLaMA 2), 98% wrongly admit (Claude 1.3), 45% PM prefers sycophantic, c.25% vs 75% at N=4096 | PDF | Confirmed. c09 "27% Claude 1.3" is the are-you-sure average drop, a different test from the LLaMA 2 27% in c08; both appear in the paper. The b27 line correctly says N=4096 (not N=4). |
| 8 | Chen 2025: 25% (Claude 3.7) and 39% (R1) average, 44%/32% harder, 63% RL gain then plateau 28%/20%, >99% hack use, <2% verbalised | PDF | Confirmed. |
| 9 | Mirzadeh 2024: up to 65% drop; newer models drop more | PDF | Confirmed. The 65% is Phi-3-mini; "up to 65% across all models" in the abstract is loose. |
| 10 | Rajeev 2025 CatAttack: ">300%", "up to 500%", "700%"; 35% proxy attack; ~20% transfer | PDF | PARTLY CORRECTED. Rates confirmed (574 of 1618 = 35%; 114 of 574 = 20%). But Table 3 gives multiples of the random-chance rate: R1-distill-Qwen-32B combined 3.0x, 2.83x for the other, reasoning group 5.14x, non-reasoning 7.21x. A 3.0x multiple is a 200% increase, not 300%, and 7.21x is +621%, not +700%. The paper's percentage wording is looser than its table. Use multiples, not percentages. c15 and c16 carry the percentages; c16 already has the multiples. |
| 11 | Wu 2024: 22.5/27.4/1.7/5.5 (GPT-3.5), 83.5/91.1/11.8/42.4 (Llama2-7B); format 5.5/3.3/2.7 and 42.4/20.4/14.1 | text | Confirmed. |
| 12 | Liu 2023: 56.1 / 88.3 GPT-3.5, 48.3 / 76.1 Claude-1.3, >20% drop | text | Confirmed. |
| 13 | Lee 2023: F(1,39)=413.65, eta p2 .914 | text | Confirmed. |
| 14 | S2A (Weston): 62.8 to 80.3, oracle 82.0, 51.7 to 61.3, instructed 71.7, other variant 74.5 | text | Confirmed. |

Not re-checked this pass: Wick 2026 (June 2026 preprint, no id on hand), Burden 2025, Failing 2015 exact values, Anderson 2011, Gaspelin 2015/2018, Folk 1998, Eimer and Kiss 2008. These rest on the first-pass reading.

## Contradictions and tensions
- Stimulus-driven vs contingent: not resolved. The joint 2021 paper states a shared core, but this consensus is self-reported by the opponents, so it is one source, not independent proof. Set size and abrupt-onset rarity still split them (K03).
- Theeuwes 2004 itself shows the boundary: the interference vanishes at set sizes 5 and 9 (serial search). So "top-down cannot override capture" holds only with large displays.
- Reward capture (Anderson 2011): the original effect was weak; a larger sample (Anderson and Halpern 2017) found value-dependence. Reliability work (Shih 2025 vs Anderson and Kim 2019) disagrees on whether RT scores are reliable.
- Savelson 2025: direct replications of Vatterott and Vecera (2012) failed on the original analysis, and the effect appeared only under a different analysis. Treat as a fragile rescue.
- Ignore instructions: help in GSM-IC and S2A, but the S2A paper shows rewriting beats them. Wu 2024 reports "ignore" often fails and CoT can hurt (over-reasoning).

## Weak spots
- Human capture literature: founding studies (Theeuwes 1992, Folk 1992 values, Bacon and Egeth 1994, Yantis and Jonides 1984) were second-hand or abstract-only. Exact ms values are missing for 1992.
- The link from human capture to LLMs is by analogy. No paper tests Folk-style contingent capture in an LLM with a goal-match manipulation. K09 to K16 are about distraction in text, not attention in the human sense.
- LLM evidence is mostly 2022 to 2024 models (code-davinci-002, GPT-3.5, Claude 1.x, LLaMA 2). Only Chen 2025, CatAttack, and Wick 2026 involve reasoning models. Current-model sensitivity is unknown, and GSM-NoOp's finding that newer models drop more cuts against the idea that scale fixes it.
- Anchoring evidence (Lou and Sun 2024, "Anchors in the Machine") is small or on small models. Owusu and Feldman 2026 was not opened (c27); no claim relies on it.
- Several evidence lines are abstract-only (b14 to b20, b26). Lines whose numbers field says "abstract gives no numbers" cannot back effect-size claims.
- Duplicated lines inflate counts: c01 to c04 are all Shi 2023; c05 to c07 all S2A; c08 to c10 all Sharma; c12 and b25 are the same Turpin paper; b13 and a15 share one tradition (Theeuwes/Awh). Independent-source counts in claims.jsonl are by paper, not by evidence line.
- Wick 2026 is a single independent-author preprint, with tokens used as a reaction-time analog; the unit differs from ms.

## Seen only in snippets
Folk, Remington and Wright (1994), Remington et al. (2001), Theeuwes, Atchley and Kramer (2000), Yantis and Jonides (1984), Koch and Ullman (1985), Theeuwes 2018 fast-vs-slow debate, Owusu and Feldman 2026.

## GAPS (most decision-relevant first)
1. Does a stated goal placed before the material reduce the pull of a planted hint or irrelevant clause in a current (2026) reasoning model, and by how much, at equal tokens? No study tests goal-before vs goal-after with a planted item. This is the direct S1 test.
2. Does a contingent-capture analog exist in LLMs: is a planted item that matches the stated goal's wording (role or topic overlap) pulled in more than a mismatched one, holding salience (position, length, formatting) fixed? Shi and Wu suggest yes but never separate match from salience.
3. How do current frontier models (not 2022 to 2024 models) score on GSM-IC, GSM-NoOp, and CatAttack-type triggers, with reasoning on and off? Which of the old drops persist?
4. Does code-side stripping of suggestive content (hints, user beliefs, anchors) beat a model-side rewrite (S2A) or an ignore instruction, at equal tokens? Only S2A vs instruction has been compared, on LLaMA-2-70B-chat.
5. Does visual or formatting salience (bold, capitals, position at top or end, repetition) pull LLM answers independent of semantic relevance? Human capture is about salience; LLM work mostly manipulates semantics. Little is known.
6. Does a stored class-level lesson (S9 note: "hints in this class are unreliable") reduce later pull, as location statistical learning does in people? Do lessons beat per-item instructions?
7. Do reasoning models that skip deliberation on easy-looking items (Wick 2026) fail more on planted-easy items, and does an S0 gate that forces a restate step fix it?
8. Timing: is there an LLM analog of fast capture then recovery, such that the first draft is pulled but a later check discards the plant? That decides whether to measure plant effects at draft or only final answer.
9. Are anchoring and sycophancy effects the same mechanism as irrelevant-context distraction, or separate? This decides whether one S1 hygiene step covers all three or each needs its own.
10. Does selection history (an earlier item type that paid off) over-weight later items in a long agent run, and does clearing context between items (fresh contexts, S3) remove it?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d18). New claims A07.04-K24 to K30; K09, K10, K11, K17 and K19 were extended. The b04 slope typo was fixed (about -0.55). Search quota ran out partway (WebSearch limit, arXiv API, OpenAlex and Semantic Scholar rate limits), so some gaps were searched less than others.

1. Goal before versus goal after with a planted item: STAYED OPEN. Closest is Ma (2026): question-first lost 18.3 and 25.0 needle points in small models, and Anthropic advises queries last. No 2026 reasoning model was tested with a planted hint (K24).
2. LLM contingent capture: PARTLY CLOSED. Relevance gates pull (relevant false passage 0.12-0.43 vs at most 0.06; same-template distractors beat same-topic ones for Claude Sonnet 4 and GPT-4.1). Wording overlap with a stated goal, with salience held fixed, is still untested (K25).
3. Current models on GSM-IC, NoOp, CatAttack: PARTLY CLOSED. Drops persist for Opus 4, R1, o3, GPT-4.1, Gemini 2.5 (d01, d03, d06, d07). No 2026 run of the exact GSM-NoOp or CatAttack sets on GPT-5-class or Claude 4.5+ models, and no clean reasoning on versus off comparison for frontier models. Small models show thinking shrinks the drop (41 to 14-20 points) but not to zero.
4. Code-side stripping versus S2A versus instruction: STAYED OPEN. Only model-side arms exist: a skepticism sentence helped (+0.18), a verifier and NoisyBench prompting and context tools did not. No code-side arm anywhere (K29).
5. Visual and formatting salience: PARTLY CLOSED, leaning negative. All-caps had no effect in four frontier models; casing moves attention in non-reasoning models but not accuracy; format-copying matters (K26). Bold, position and repetition of a hint are untested.
6. Stored class lesson: STAYED OPEN. A generic unreliability warning works at no cost when context is true (K29), but no stored-lesson, learned-over-items test exists.
7. Adaptive thinking skips planted-easy items: STAYED OPEN. Wick (2026) is about visual search only; no restate-gate test found.
8. Fast capture then recovery: CLOSED, answer is no recovery. Traces show consideration of the simple answer, then a return to the distractor (K27). Still log the draft.
9. One mechanism or three: PARTLY CLOSED, leaning separate. Frontier models ignored an irrelevant turn yet shifted toward a stated user view (K28). Anchoring was not retested here.
10. Selection history in agents: STAYED OPEN, with indirect support. Early state persists in multi-turn use and recaps clear 15-20% of it (K30); reward-history by item type is untested.

Caveats: several 2026 sources are single preprints or listing abstracts (Ma, Dillitzer abstract only, Ghaffari). The Sun et al. table rows were quoted only for o3 and GPT-4o because the PDF text did not align the other rows. Becker used open-weight models.
