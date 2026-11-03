# C07.03 critique: Count-based exploration, unified with intrinsic motivation

Cross-checker pass. Sources re-opened this session (PDF text via pdftotext): Bellemare 2016, Ostrovski 2017, Tang 2017, Burda RND 2018, Taiga 2019/2020, Go-Explore, MERCI (Zhang 2025), CDE (Dai 2025), Krishnamurthy 2024, Yue 2025.

## Numbers re-checked (confirmed unless noted)
1. Bellemare: A3C fails on 15 games, A3C+ on 10 (8 shared with DQN); Montezuma 6600 by one run. Confirmed. ("15 of 24 rooms" was not re-grepped by that phrase.)
2. Ostrovski: PixelCNN beats CTS in 52 games by max score, 51 by AUC. Confirmed.
3. Tang Table 1: Freeway 16.5 to 31.6, Frostbite 2869 to 4683, Venture 121 to 616, Montezuma 0 to 238 (pixel-SimHash). Confirmed. The table is garbled by extraction; the AE-SimHash Montezuma row is unreliable.
4. RND: Montezuma 8,152 vs PPO 2,497; Private Eye 8,666. Confirmed.
5. Taiga: CTS reaches 5000 within 200M frames, others 2500; no correlation with other hard games. Confirmed.
6. Go-Explore: 43,763 on Montezuma without domain knowledge. Confirmed. CORRECTION: with domain knowledge the mean is 666,474 (evidence said "over 650,000"); Pitfall mean 59,494, max 107,363.
7. MERCI: pass@k average GRPO 65.8 to 67.4; DAPO mean@k 42.2 to 44.9; AIME25 pass@256 50.0 to 60.0; without noise filtering 63.8. Confirmed. NEW detail: Minerva (64.0 to 63.2) and MATH500 (91.8 to 91.4) pass@16 do not improve, so the average gain comes from AIME and a few sets. AIME25 has 30 problems, so +10 points is 3 problems.
8. CDE: baseline average 48.2, perplexity bonus 50.6, AIME24 20.8 to 23.3 in the tables; the SimHash-collapse statement is in the text. Confirmed.
9. Krishnamurthy: suffix failure in more than 60% of GPT-4 basic-prompt replicates. Confirmed.
10. Yue: pass@1 on training 26.1 to 42.5; RL nearly 30% above base at small k; base ahead by about 9% at k=128 on Minerva. Confirmed.

## Corrections and inconsistencies
- Kolter and Ng wording differs: a04/a25 say "1/N-type", c25 says "not proportional to 1/N". Bellemare's text says no algorithm with a bonus upper bounded by a power of N^-1 (exponent glyph lost in extraction) for any epsilon>0 can guarantee PAC-MDP. Read as: bonuses that decay faster than the count rate lack the guarantee. Original not opened.
- Years differ between files for the same paper (Burda 2018/2019, Taiga 2019/2020): arXiv vs venue year.
- a09 says Reactor-PixelCNN gains in "about 50 of 57"; the text gives 52 (max) and 51 (AUC) for DQN-PixelCNN vs DQN-CTS, a separate comparison from Reactor vs Reactor-PixelCNN. Do not mix them.
- b24 is labelled Auer (2002) but is the LIE paper restating the UCB bound; Auer was not opened.
- b13 "almost 4 times previous best" for Montezuma: exact multiple not re-checked.

## Contradictions between sources
- Bellemare/Ostrovski (the bonus is the key) vs Ostrovski's own mixed-Monte-Carlo finding (return type matters as much) vs Taiga (gains shrink under a stronger base agent and fair tuning). Summary: the bonus helps where exploration is the bottleneck, and less than first reported.
- RND finds 21-22 of 24 rooms, but the NGU ablation says RND alone hurt Pitfall! and RND itself scores -3 there. RND is not uniformly good.
- LIE (longer traces explore deeper) vs schema G11 (think briefly). Not tested head to head.
- Hash counts work in Atari (Tang) but collapse on LLM chain-of-thought embeddings (CDE). Key quality is domain-specific.

## Weak spots
- Nearly all RL numbers are Atari, 5 seeds or fewer, tuned on the test game (Montezuma). Bellemare's 6600 is one run.
- LLM evidence is thin: one count-style paper (MERCI: small mean gains, AIME-heavy, tiny test sets), one negative (CDE), one bandit study (GPT-4 only). None tests a prompt-level history table.
- Nothing tests count bonuses in an in-context, no-training agent at equal tokens.
- Most LLM papers change the training signal. Our agent cannot train, so only the idea (key plus count plus preference) transfers, not the results.
- Files a, b, c overlap heavily (all restate Bellemare and Tang), so independent_sources counts research groups, not files.

## Only seen in snippets or not opened
a24 (Strehl and Littman), a25 (Kolter and Ng), b15 (Martin 2017, abstract only), b24 (Auer via LIE). c19 to c23 (ELLM, OMNI, entropy-advantage paper, SELM): abstract-level, margins not extracted. Voyager 93% and 73% not re-opened. Agent57 and Machado SR: abstract only.

## GAPS
1. Does a code-side history table (counts per normalised direction) with a 1/sqrt(n) preference raise distinct-correct-answer coverage in S3 at equal tokens, compared with plain independent resampling? No paper tests this.
2. What key should the table use for LLM attempts (exact text, operator plus approach label, embedding hash)? CDE shows embedding hashes collapse; what granularity avoids both collapse and "everything is new"?
3. Does summarising history in code beat showing raw attempts to the generator (Krishnamurthy suggests yes for bandits)? Does this hold for open problems and for newer models than GPT-4?
4. Does novelty pressure hurt on easy problems (Taiga's reversed trend)? Can the S0 gate decide per class when to switch the table on, consistent with G12?
5. Is the MERCI gain real beyond AIME? A per-benchmark replication with more problems and seeds is missing; Minerva and MATH500 showed no gain.
6. How to stop "dancing with skulls" in text: after a verified pass, how do we stop novelty from pulling the agent off the right answer (G6, G2)?
7. Does Go-Explore style return-to-archive (extend the best partial attempt) beat restart at S6 impasse at equal tokens?
8. Do long, redundancy-penalised traces (LIE) beat several short independent attempts (G11) at equal tokens, or is the gain only more sampling?
9. How much of the Montezuma gain came from the bonus vs the return type (MMC)? Is there an equivalent confound (length, entropy change) in LLM RLVR papers?
10. Are tabular guarantees (UCB, MBIE-EB) of any use when the "state" is a free-text direction? What is the right notion of state for counts over reasoning?

## Gap search results
Evidence file evidence_d.jsonl (d01 to d18). Opened as PDF text this session: Large Language Monkeys, Intelligent Go-Explore, Snell 2024, Song 2025, Tuyls 2025, Hu 2026, Shao 2026 (Spurious Rewards), COPO, Harris and Slivkins, EVOLvE, Monea 2025; DivSFT from its listing page (abstract only). The Semantic Scholar and OpenAlex APIs were rate limited; three WebSearch calls were used.

- Gap 1 (history table vs independent resampling at equal tokens): STILL OPEN. No paper tests a prompt-level table. Nearest: DivSFT (sequential conditioned generation, after fine-tuning) and Tuyls (history-aware selection from a pool). Baseline to beat is Large Language Monkeys (d01).
- Gap 2 (key granularity): MOSTLY CLOSED by literature. Judge-labelled strategy clusters (Hu 2026) and hidden-state covariance (Tuyls) work; hashes collapse; outcome keys work where answers are checkable (Song). Our own test is still missing (K16).
- Gap 3 (summary vs raw history, newer models): PARTLY CLOSED. EVOLvE, Harris and Slivkins 2026 (GPT-5 family included) and Monea agree that code summaries or filtered positive examples beat raw history. Only bandits and classification, not open problems.
- Gap 4 (novelty on easy problems, gating): PARTLY CLOSED. Snell shows a difficulty-dependent best strategy and beam search hurting easy items; Tuyls shows gain grows with model strength. The S0 gate itself is untested.
- Gap 5 (MERCI beyond AIME): STILL OPEN. No replication found.
- Gap 6 (after a verified pass): PARTLY CLOSED. Snell: naive revision flips about 38% of correct answers; Song: revisiting refuted answers hurts. Rule drawn: freeze verified answers, hard-exclude refuted outcomes. Not tested head to head.
- Gap 7 (return to archive vs restart): PARTLY CLOSED. Intelligent Go-Explore beats ReAct, Reflexion and classic Go-Explore in text games, with an action-history ablation. Equal operations, not tokens, and no free-text reasoning task.
- Gap 8 (long redundancy-penalised traces vs short attempts): STILL OPEN. Snell gives sequential vs parallel by difficulty, not LIE-style penalised long traces.
- Gap 9 (bonus vs confounds): PARTLY CLOSED. Spurious Rewards shows Qwen-math RLVR gains are confounded by pre-training priors (random reward +21.4 vs +29.1 on MATH-500); this applies to MERCI-type claims. The MMC confound in Atari remains from Ostrovski.
- Gap 10 (tabular guarantees for free-text states): PARTLY CLOSED as argument. Song argues deterministic checkable rewards make 1/sqrt(N) bonuses the wrong tool (hard exclusion instead). Kolter and Ng and Strehl and Littman originals are still unopened.

Limits of this pass: API rate limits blocked systematic forward citation search; DivSFT was read from its abstract page and the COPO table from garbled extraction.
