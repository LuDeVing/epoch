# Critique and cross-check: A19.09 Critiques and universals

## Numbers re-opened this session (text read from source)
Confirmed against source text: Henrich 2010 (68% US, 96% Western, 12% of world, 73% first authors, 67% US samples undergrads, 4,000 times); Sun and Wang 2025 (language d=0.045, eta2=0.0002, p=.1501; model origin d=0.169, p=.0089; framing d=-2.095, eta2=0.5423); Jin 2023 (AHS 5.35 and 5.01 vs 4.87 N=702; DSS GPT-4 3.97 vs 4.0, p=.344; SCS-Ind 6.98); Hu 2026 (11.53 vs 8.10 d=1.01; horizon 533.47 vs 519.79 d=0.34; 5.30 vs 6.78 t=-7.74; HAP 113 vs 79 chi2=28.36; LAP 41 vs 2 chi2=40.91); Tao 2024 (2.42 to 1.57; 71.0/81.3/77.6/72.6%); Many Labs 2 abstract via Crossref (15305, 54%, d 0.60 vs 0.15, 32% reversed, Q in 39%); Blais 2008 (ages 24.4, 23.2); Caldara 2010 (F=2.18, p=.14); Talhelm 2018 (8,964 people, 256 stores; n=678 chair study); Atari 2023 abstract (r=-.70).

## Corrections
1. c01 is wrong on attribution. It lists GPT-4o as closest to New Zealand 0.98, Iceland 0.97, Australia 0.86. In Tao 2024 those are GPT-4. GPT-4o is closest to Finland 0.20, Andorra 0.21, Netherlands 0.45 (matches a17/b26). Jordan 4.10 is GPT-4o; GPT-4 is Jordan 4.19.
2. Hu 2026 reports 10.91 vs 10.07 in the discussion and 10.90 vs 10.06 in results. Same data, internal rounding. a16 and b21 are one source, not two.
3. a19 (author names unknown) and c11 are the same paper (Wang et al. 2024, arXiv 2310.12481). Count once.
4. a17, b26, c01-c03 are all Tao 2024; a18, c04, c05 all Cao 2023; a20, b27, c21 all AlKhamissi 2024; a21, b25, c18 all Atari 2023; a14, b18, b19 all Jin 2023. Independent-source counts in claims.jsonl reflect this.
5. Sun and Wang "model origin d=0.169" holds only for English prompts (Chinese vs English LLMs); eta2 for that is 0.0071.
6. Henrich-derived lines a02, a03, a04, a06, b02-b06 are secondary; originals (Segall, Witkin) were not opened.
7. b08-b10 claim to read Norenzayan 2002 but a08 says it was not opened. Conflict inside the evidence files; treat b08-b10 numbers (from a different session) as unverified here.
8. K03 evidence list originally cited Many Labs; removed.

## Contradictions between sources
- Original Nisbett-line findings (Peng and Nisbett 1999, Norenzayan 2002) vs Mercier 2015 and Hakim 2017 (little robust difference). Not resolved; replication abstracts only.
- Many Labs 2 moderation in 3/28 (Schimmelpfennig) reads as "mostly universal" but the same paper says power was 28% and samples culturally close; interested authors.
- AlKhamissi 2024 says prompt language matters for alignment; Sun and Wang and Hu 2026 find prompt language does not switch style. Likely differ in task (values vs reasoning).
- Jin 2023 finds LLMs holistic on scales; Hu 2026 finds the US model produced MORE holistic markers in images, opposite to human data.

## Weak spots
- Almost all effects rest on abstracts (b14, b15, b16, b17, a20, a21).
- Jin 2023 design: 10 runs, temperature 1, norms from different studies, agree-bias on self-report.
- Many LLM studies are preprints and several are by the Nisbett lineage (Hu).
- Survey alignment is not reasoning.

## Only seen in snippets or abstracts
a07, a09, a10, a21, c19, c20, a20, b14-b17, b25, Many Labs 2 (abstract only).

## GAPS
1. Does any LLM study measure Nisbett-style reasoning tasks (triads, change blindness, contradiction) against same-study human data, with at least 100 runs per cell?
2. What are the exact N, effect sizes and original-authors' replies in the Mercier 2015 and Hakim 2017 failed replications of Peng and Nisbett and of visual-cognition effects?
3. Which Many Labs 2 effect size did the Norenzayan 2002 item show per site, and was its moderation by WEIRDness robust under continuous cultural distance?
4. Does framing/prompt variance (eta2=0.54 in Sun and Wang) also swamp reasoning performance on standard benchmarks at equal tokens, and by how much?
5. Does persona or language prompting change reasoning accuracy (not values) on logic, math or ARC tasks?
6. What do Atari 2023's per-task numbers show, and does the WEIRD correlation hold for reasoning tasks versus value items?
7. Is the Chinese-model (ERNIE, DeepSeek, Qwen) vs US-model difference in reasoning style explained by RLHF "service persona" or by data? Any ablation?
8. Are there independent replications of the rice-wheat theory (Talhelm 2014) with causal designs?
9. How do belief bias and content effects (Lampinen 2024) differ across non-Western human samples, and in LLMs at equal tokens?
10. What is the original Norenzayan 2002 sample size for Study 1 and its Korean-vs-American effect sizes (not read here)?

## Gap search results
Sources opened this session: Talhelm 2024 (Nature Comms, full text), Many Labs 2 preprint full text (Norenzayan item), Atari 2023 full text, Sclar 2024, Zheng 2024, Kong 2024, Shi 2023, Lampinen 2024 methods, Hu 2026, Sabir 2025, Tao 2024 (RLHF passage). Evidence in evidence_d.jsonl (d01-d16). Search limits: WebSearch budget gone, OpenAlex and arXiv APIs rate-limited, SSRN and SAGE blocked. One Unpaywall call used a placeholder address (no real address sent).

1. Nisbett-style LLM task with 100+ runs: CLOSED in part. Atari 2023 ran the triad task 1,100 times (20 triads) against 31 human populations on the same platform; GPT closest to Netherlands, Finland, Sweden, Ireland. Holism score only in a figure. Change blindness and contradiction tasks: none found. K19 rewritten.
2. Mercier 2015 and Hakim 2017 numbers: OPEN. Only abstracts. Mercier: Chinese vs French, no difference. Correction: authors are Mercier, Zhang, Qu, Lu, Van der Henst.
3. Many Labs 2 Norenzayan item: CLOSED for the item, OPEN for continuous distance. It is Study 2; replication N=7,396, instruction effect d=0.86 (original EA d=0.00, East Asian d=0.67). WEIRD advantage appeared under "belong to" (65.2 vs 59.8%) and reversed under "similar to" (42.8 vs 48.4%). Moderation by WEIRD was binary only. The earlier K02 numbers (67%) are replaced by the source values 69% and 70%.
4. Framing variance on standard benchmarks: CLOSED in part. Sclar 2024: median spread 7.5 points, up to 76 (LLaMA-2-13B); GPT-3.5 up to 56. Not chain-of-thought tasks, no equal-token control.
5. Persona or language prompts on reasoning accuracy: CLOSED in part. Personas: no gain on 2,410 MMLU questions (Zheng); role-play helps only as chain-of-thought trigger (Kong, AQuA 53.5 to 63.8%). Language: MGSM 3-point gap. No ARC test found; cultural personas not tested.
6. Atari per-task numbers: OPEN for numbers (figures only). WEIRD correlation does hold on a reasoning-style task (triad) as well as on values.
7. RLHF vs data ablation: OPEN. No ablation in Hu 2026, Tao 2024 or Sabir 2025; hypotheses only.
8. Rice-wheat causal replication: CLOSED in part. Talhelm 2024 quasi-random farms: holistic B=0.28, p=.025, r=.15; two farms, same lab; no independent replication.
9. Belief bias across non-Western humans: OPEN. Lampinen human data are UK only (625 plus 360); no equal-token control.
10. Norenzayan 2002: Study 2 N=157 (52 EA, 52 Asian American, 53 East Asian). Study 1 N: OPEN.
