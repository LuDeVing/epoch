# Critique: A15.05 Thinking for speaking (cross-check)

## Verified this session (sources re-opened)
Re-opened: Papafragou, Hulbert & Trueswell 2008 (PMC2810627), Gennari et al. 2002, Montero-Melis 2021 (PMC8042225), Chen et al. 2026 (PMC13382187), Shi et al. 2022 (arXiv 2210.03057), Etxaniz et al. 2023 (2308.01223), Quiet-STaR (2403.09629), the Language of Thought diversity paper (arXiv 2601.11227), Language Matters (2505.17407), Under the Shadow of Babel text.

Confirmed exactly: 72/36% and 76/54% manner verbs (Papafragou); median onset 1267 ms; Language x Task F1(1,25)=4.95, eta2=.17; Spanish path-verb 0.80, manner 0.71 (Gennari); Swedish 97% S-framing vs Spanish 59% V (Montero-Melis); Goal 97.7% vs Source 87.5%, beta=-1.048 (Chen); PaLM 44.9% vs 47.9% (Shi, 3 points); LLaMA 30B 43.1 to 46.6 and XNLI 37.0 to 43.5, MGSM 15.5 to 16.3 (Etxaniz); Quiet-STaR GSM8K 5.9 to 10.9, CSQA 36.3 to 47.2; NoveltyBench 28.55/36.00/43.73 etc. and r=0.72-0.88; MATH-500 prefill table (Swahili 57.4 vs 25.9, Spanish 88.0 vs 72.5, Telugu 70.0 vs 46.2) and over 90% mismatch; BICAUSE 91.0/91.2/88.5/76.5.

## Corrections and caveats
1. a10 (Gennari 2002) said language differences did not show in non-verbal similarity. Incomplete. The paper reports no language effect in recognition memory, and none in similarity after non-linguistic encoding, but it DID find a language-specific similarity effect after verbal encoding (Language-as-Strategy reading). This is the closest match to thinking for speaking and is now claim K04 (contested).
2. a04 and a06: the paper's p-values look one-tailed. F1(1,16)=4.01 is printed p=.03, but two-tailed it is about .06; F1(1,25)=4.95 is printed p=.01 (two-tailed about .035). Effects are weaker than the printed p-values suggest. Eta2 values are as printed.
3. Apparent contradiction between a04 and b01 on item analyses is resolved. The first-second gaze interaction is significant by items (F2=10.14, p=.004), but the first-look interaction is only marginal by items (F2(1,11)=3.61, p=.08).
4. a21: in the DeepSeek row the "Mixed" column (52.07) is lower than "S-best" (52.42), so mixed thinking is not always the best setting.
5. Shi: the 3-point gap is a Native-CoT average of 4 vs 6 languages, not per language.
6. a23, b09, b10 and c12/c13 are one paper (same numbers; text 76.5 vs table 76.8). Counted as ONE source.
7. a03-a06 and b01-b03 are one paper; counted as one source unless another study agrees (a16/b15 do for the null).
8. Chen 2026 (a17, b07) is one paper, so K09 is single-source (the claim text in evidence says speaking reduces the Goal bias in gaze; the direction in b07 is that speaking raised attention to Source).

## Contradictions between sources
- Goller et al. 2017 (Korean/German, N=27) finds language-shaped similarity and gaze in a non-speaking task; Papafragou 2008 and Lee et al. 2026 find none. A possible reason is that explicit similarity ratings invite a verbal strategy.
- Wendler et al. 2024 (language-neutral concept in middle layers) vs Schut et al. 2025 (English-first route in open generation); different task designs (single token vs multi-token).
- BICAUSE: the easier language varies by model; large models close the gap.

## Weak spots
- Slobin 1996 and Berman & Slobin 1994 were never opened (PhilArchive 403). Founding claims rest on secondary description.
- The human evidence is a small set of English vs Greek/Spanish/Turkish/Korean/German studies; typical N is 17 to 47 per group. Heavy exclusions (about 15% in Papafragou; 27 of 128 in Chen eye analysis).
- No pooled effect size and no large preregistered replication of the 2008 gaze-timing result was found.
- No LLM paper tests the Slobin paradigm directly. The closest are the output-diversity paper (a21) and the English-latent-language logit-lens papers. The name-overlap papers (c19-c21) do not bear on the claim.
- Snippet only or second-hand: a24 (unverified arXiv id), c23 (CORE link not opened), a07 (abstract only), a10-a13, b04, b12, b13, b21-b24.
- Single-source LLM claims: K12, K13, K14, K15 each rest on one paper.

## GAPS
1. Does forcing different reasoning languages for different branches raise candidate diversity at equal total tokens in a scaffold (replicating a21 beyond Qwen3, with correctness measured, not only diversity)?
2. Is there a large (over 100 per group) or preregistered replication of Papafragou 2008 gaze timing, in English-Greek, English-Spanish or English-Turkish?
3. What does Slobin 1996 claim and test at page level, and what did Berman & Slobin 1994 frog-story numbers show for manner and path by language and age?
4. Do vision-language models, given the same motion clips and prompts in several languages, show manner and path verb rates that differ by language as speakers do? (None found.)
5. Does a describe-first step in an agent shift later judgments toward description-language categories (the Gennari-type strategy effect), and does it help or hurt accuracy at equal tokens?
6. Why do Wendler et al. and Schut et al. disagree about the language of latent concepts, and does the answer change with reasoning-model training?
7. How large is the penalty for reasoning in the input language across more tasks and current frontier models than MATH-500/MMMLU (Language Matters)?
8. Do the aspect-language results (von Stutterheim, Flecken, Bylund & Athanasopoulos) hold in numbers when opened, and do bilingual switching effects replicate?
9. Does the Goal bias (K09) appear in LLM-written plans and descriptions, and can a checklist reduce it?


## Gap search results
Evidence in evidence_d.jsonl (d01-d19). Claims K03, K06, K07, K10, K11, K17 updated; K19-K24 added. Limits: the WebSearch budget ran out after one call, and the arXiv, Semantic Scholar and OpenAlex APIs were rate-limited (HTTP 429), so searching used arXiv listing pages, Europe PMC and direct fetches.

1. Language-diverse branches at equal tokens (partly closed). Best evidence is UL-XCoT (d13, 2604.20090): voting over several reasoning languages beat a monolingual control with the same pruning on PolyMath (Low 83.8 vs 65.5, Medium 31.1 vs 26.3, High 13.6 vs 12.3, Top 10.6 vs 9.4; 7B distilled model) at over 50% fewer tokens than prior sampling baselines. polyGRPO (d12) shows a non-English response language beating English for some questions on Qwen2.5-7B. Still open: strictly equal total tokens, frontier models, and a scaffold that pairs correctness with the diversity measure of a21. Claim K19, single-source.
2. Large or preregistered replication of Papafragou 2008 (stays open). None found. Nearest are Fu et al. 2023 (51-55 per group, flash suppression and sentence-video verification, d01/d02) and Soroli 2024 (20 per language, d03). Soroli found a language effect in non-verbal categorisation (French 78% path-congruent vs English 59%), which weakens K03 "established"; K03 is now contested. Claim K24.
3. Slobin 1996 and Berman & Slobin 1994 at page level (stays open). Publisher pages were blocked and APIs rate-limited. Only the second-hand description opened (d06, d07): Slobin's evidence is translations, narrations and mental imagery, all linguistic. No frog-story manner/path figures obtained. Claim K23.
4. VLMs on motion clips in several languages (stays open). Still none found (d19).
5. Describe-first in an agent (partly closed, indirectly). Liu et al. 2024 (d15) show verbal CoT lowers accuracy on face recognition after description (GPT-4o 64.0 to 51.2) and artificial grammar (GPT-4o 87.5 to 64.4). Not a Gennari design; no equal-token test of describe-first before category judgements. Claim K21.
6. Wendler vs Schut (mostly closed). The second paper itself names single-token versus multi-token generation as the difference, and English-centrism varies by model (Aya least, Gemma most). Reasoning-trained models were not tested in either paper, so the training question stays open; M-Thinker (d11) shows consistency can be trained. Claim K22.
7. Penalty for thinking in the input language (mostly closed). XReasoning (d09): matching 46% to 98% with a prompt hack, mean accuracy 26% to 17%, AIME 25.5 to 17.0 and GPQA 40.3 to 33.4 for Distill-R1-32B; Zhao et al. (d10) agree. Three independent groups now back K10. Still open: current frontier models and non-math tasks.
8. Aspect-language results in numbers (stays open). Only second-hand through Fu et al. (d04, d05): aspect effects vanished under verbal interference. Original numbers not opened. Bilingual switching not re-tested. A future-tense study (d18) reversed the expected sign, a caution for grammar-to-cognition claims.
9. Goal bias in LLM plans (stays open). No study found (d19).

Closed or mostly closed: 6, 7. Partly closed: 1, 5. Open: 2, 3, 4, 8, 9.
