# Critique: A15.10 Pragmatics and shallow comprehension (cross-check)

## Numbers re-opened (this session, full text)
1. Christianson et al. 2001 (ch.txt): 47.4% vs 32.1% (Exp 1a), 55.6% vs 9.4% (question type), 62.0% vs 39.1% (RAT verbs). CONFIRMED.
2. Ruis et al. 2023 (arXiv 2210.14986): human mean 86.2%, best 89.8% (Table: 89.8; text also says 92%). GPT-4 CoT 86.5 +/- 1.0. Particularised 71.97 / 81.63 / human 83.18; generalised 86.23 / 88.66. 0.04% per billion. CONFIRMED.
3. Ruis Table 3 (0-shot, 5-shot, 5-shot CoT): davinci-001 72.3/74.5/67.3; davinci-003 71.2/79.7/83.6; ChatGPT 72.1/73.9/77.2; GPT-4 81.8/82.0/86.5; Cohere-52b 60.2/75.4/75.3. CONFIRMED.
4. Amouyal et al. 2025 (arXiv 2502.09307): humans 95.4% simple (92.4-98.7), 37.0% GP; o1-preview 78%; CoT "did not lead to a significant change" (footnote 2). CONFIRMED.
5. Cai et al. 2024 (arXiv 2303.08014): ChatGPT strong imposter 0.14 (z=12.55), weak 0.17; 0.17 vs 0.13 strong-vs-weak p=.036; inference yes rates 0.95/0.49/0.23; DO 0.92 vs PO 0.56. CONFIRMED.
6. Hagendorff et al. (arXiv 2212.05206): 72% intuitive, 18% correct for davinci-003; 74% and 88% correct for ChatGPT-3.5 and 4; warning suffix 18% to 54%; 10+ examples to over 64%; humans 64% vs 52%. CONFIRMED.
7. Liu et al. 2023 AmbiEnt (arXiv 2304.14399): 35.2% ambiguous, 89.7% crowd agreement, 96.7% plausible, GPT-4 EDIT-F1 18.0 / 32.0 / 63.0, 76%, 43.6%, recall 88.8% / precision 12.4%. CONFIRMED.
8. Speckmann and Unkelbach 2021 (PMC7751745): 52.3%, 73.2%, 914 participants. CONFIRMED.
9. Dygert et al. 2026 (J Intelligence): 9% and 5% extra variance. CONFIRMED (N about 100; small).
10. Bott et al. 2022: opened PMC8970470; the 200 ms figure was not re-located by text search, so it stays as in b18 (unconfirmed).

## Corrections made
- a15 says "text-davinci-003 60.2% at k=0 to 75.4%". Wrong model. 60.2 to 75.4 is Cohere-command-52B; davinci-003 is 71.2 to 79.7 (c02/c03 correct).
- a15 gives "best human 92%"; c01 gives 89.8%. Both appear in the paper (92% best rater in the text, 89.8% in the table/CoT text). Quote both.
- b14 says "one example-IT model 74.5 to 67.3". It is text-davinci-001, and the drop is from the 5-shot value.
- b17 describes 26.5% as "a high-knowledge subset". The source puts it in Study 2 (true/false judgment format). The 52.3% is Study 1.
- b04 gives ChatGPT strong imposter 0.13; a21 gives 0.14. Both are in the paper (0.14 in the baseline contrast, 0.13 in the weak-vs-strong contrast text). Use 0.14 for the baseline contrast.
- a15 "GPT-4 82.3% +/- 1.4": table value 82.31 is a mean across prompts at one k; Table 3 gives 82.0 at 5-shot. Treat 82.0 to 82.3 as one number.
- Hagendorff title in b01/b02 is the PNAS title; arXiv title is "Thinking Fast and Slow in Large Language Models". Same study.

## Contradictions between sources
- Cai (ChatGPT detects slightly more weak than strong impostors) vs a "human-like" reading: the gap vanishes after removing exemplar items, so it is not solid.
- Hagendorff says strong models solve illusions without CoT; Ruis says CoT helps GPT-4 on implicature. Different tasks. Not a contradiction, but it means CoT value is task-specific.
- Amouyal (CoT no change) vs b10 (thinking helps, but half as much on GP). Those are different model sets (non-reasoning with CoT prompt vs reasoning models).
- Zhang et al. (LMs over-fall for NPI illusion, not for depth-charge) vs Paape (c26, unread: transformers look more literal). Both agree LMs differ from humans on semantic illusions.
- Chromy, Qian, Nakamura and Arai disagree on mechanism (a11); only seen via Frances 2024.

## Weak spots
- Almost all LLM results use 2022-2023 models. Only Amouyal 2025 (o1-preview, GPT-5) and Qiu 2025 look at current models. No Moses or implicature number for current frontier models with a scaffold.
- Founding items (Erickson and Mattson 1981, Ferreira 2003, Reder and Kusbit 1991, Hannon and Daneman 2001, Swets 2008, Slattery 2013) were not opened; all second-hand.
- Human data in Amouyal: 400 ms per word presentation, 5 s question limit, which inflates errors relative to untimed reading. LLMs saw the whole sentence. The comparison is not like for like.
- Dentella et al. (a20) authors are sceptics and the benchmark is unvalidated; do not rely on it.
- Dygert (b20) is a small correlational study.
- Hu et al. human data (374 participants) cited as "in prep" in the paper.
- No study tests a scaffold (not a prompt tweak) on these traps at equal tokens. The only direct intervention results are Hagendorff (one-line warning) and Ruis (CoT).

## Seen only in snippets or unread
a25 and b11 (Li et al. 2024: b11 opened but small), c25 Cong and Rayz (empty download), c26 Paape, c27 NLPSI debate, c28 Stanford report, b22 to b28 background items.

## GAPS (most decision-relevant first)
1. Does a premise-check or "what is being asked and what does it presuppose" step reduce Moses-type and false-presupposition errors in current frontier models, and by how much at equal tokens (Hagendorff showed 18% to 54% on davinci-003 only)?
2. What is the current false-premise and Moses-illusion flag rate for 2025-2026 frontier models, and is it still below human or above?
3. Does an explicit "list who did what to whom" or paraphrase-first step fix garden-path and passive misreadings in reasoning models, given that thinking tokens help GP items only half as much (Amouyal 2025b)?
4. Do models that ask a clarifying question when intent is ambiguous beat always-assume at equal tokens (INTENT-SIM, EIG results are on older models), and what is the error cost of asking too often?
5. What are the actual rates in Ferreira 2003 and Erickson and Mattson 1981 (passives, Moses), and do the 52% Moses rates replicate across languages and samples (Speckmann gives 52.3%, Reder and Kusbit 32-35%)?
6. For current models, are the context-heavy (particularised) implicature gaps closed, and does CoT still help only there (Ruis found the gain concentrated on particularised items)?
7. Does telling the agent what kind of check will follow (shallow vs deep question) change its depth of reading (Swets 2008 in humans), and can a scaffold exploit this without gaming?
8. Does a prompt-side fix that marks load-bearing words (change-detection findings, Sanford) improve detail retention in long prompts?
9. Are model errors on pragmatic traps stable across re-asking (Dentella reported instability), and does self-consistency voting reduce them at equal tokens?
10. Which model-side failures are about missing a signal (noisy-channel misrepair, Qian and Levy 2026) vs over-literal reading, and can a "check for likely speaker error" step help or hurt?

## Gap search results (evidence_d.jsonl, d01 to d16; claims K30 to K37 added)

Web search budget ran out after 3 calls, and arXiv, Semantic Scholar and OpenAlex APIs were rate-limited. Sources were opened by direct PDF download and read in full text where noted.

### Closed or mostly closed
- Gap 2 (current flag rates): closed for factual false premises. Reasoning models fail to challenge 26-42% of false presuppositions (d01, Dec 2025 models); no frontier model above 43% correction on hidden patient-question premises (d02); multi-hop hidden premises: best 0.46 (d05); GPT-4o rejects 84% in political questions (d06). No LLM study of the classic Moses word swap was found, so the "below human" comparison on Moses items stays unmeasured; the old ChatGPT-3.5/4 numbers (K07, K09) are the latest.
- Gap 4 (ask vs assume): mostly closed on the direction. Models default to assuming (at most about 5% clarifying questions, d07). In agent tasks asking recovers a lot (Opus-4.5 47% to 78%, d08) but GPT-5.2 over-clarifies (38% of trials with questions) and Gemini under-clarifies (31%). Not equal-token; cost is gain per question.
- Gap 5 (rates): partly closed, with a correction. The 52.3% Moses rate is Erickson and Mattson (as reported by Speckmann and Unkelbach); Speckmann's own rates are 49% and 52.6%; Reder and Kusbit's literal condition gives 32-35% (d14). K05 was reworded. Primary text for Erickson and Mattson 1981 and Ferreira 2003 (passives) was still not obtained, so the passive rates stay open.
- Gap 6 (implicature): closed in direction. Context-heavy items are not solved in 2026 (GPT-4o 76% vs humans 89%, d10). Scaffold prompts help small models only. Graded, context-light pragmatics are near human (d11). Whether CoT mainly helps particularised items in current reasoning models was not tested directly.

### Partly answered
- Gap 1 (premise check): the only intervention data on frontier models is Cancer-Myth: detection up (to 80%) but 41% false alarms on clean questions and about 10% loss elsewhere (d03). AbstentionBench shows an abstain-list system prompt works without a precision loss (d04). No equal-token test of a "what does this presuppose" step exists. Claim K31 is marked contested.
- Gap 9 (stability): older-model instability is documented (d12, sceptic authors), but no self-consistency test on pragmatic traps was found.

### Still open (no source found)
- Gap 3: paraphrase-first or role-listing for garden paths in reasoning models. Only the 0.17 vs 0.35 thinking gain (d13) exists.
- Gap 7: telling the agent the check type (Swets 2008) in LLMs.
- Gap 8: marking load-bearing words (Sanford) in prompts.
- Gap 10: "check for likely speaker error" (Qian and Levy 2026) against literal reading. The closest finding is that models over-commit to strong readings (d10), which suggests a check for over-reading may help small models, but this is not a noisy-channel test.

### Caveats
- Cancer-Myth Table 1 rows were scrambled in text extraction; model assignment inferred from position.
- Reasoning-model results (d01, d04) rest on open mid-size models plus GPT-5 Mini and Gemini 2.5; no 2026 top-tier model was included.
- Evidence files a, b and c were not edited.
