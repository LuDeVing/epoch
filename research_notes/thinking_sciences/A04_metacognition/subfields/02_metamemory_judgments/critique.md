# Critique: A04.02 Metamemory judgments (cross-check)

## Numbers re-opened and checked (this session)
Confirmed against the source text:
- Xiong et al. (2024): GSM8K AUROC 54.8 (single) to 92.7 (5-sample consistency); GPT-4 mean AUROC 62.7; mean ECE above 0.377; 22.2% AUROC gain GPT-3 to GPT-4; GPT-4 ECE 0.064 at 93.6% accuracy.
- Tian et al. (2023) tables: gpt-3.5 TriviaQA label-prob ECE .140 / AUC .869; verbal top-2 .050 / .894; SciQ top-4 ECE .065 / AUC .763; TruthfulQA label AUC .418, verbal top-2 .485; GPT-4 label ECE .078 / .950, verbal top-1 .024 / .937, TruthfulQA .622.
- Steyvers et al. (2025): model AUC .751/.746/.781; human AUC .589/.602/.592.
- Yin et al. (2023): 1,032 unanswerable, 2,337 answerable, GPT-4 F1 75.47, human 84.93.
- Koriat (2026): FOK 91.2 vs 85.1 t(35)=8.91 (N=36); JOL 78.67 vs 62.99 t(23)=9.27 (N=24); children 73.22 vs 60.87 t(71)=8.24 (N=72 usable of 100); means 89.8 vs 74.7; slopes 3.48 (FOK) vs 6.06 (JOL); r values as logged.
- Huff & Ulakci (2025): human B=.167 [.018,.316]; GPT-4o B=.045 [-.159,.248]; all LLM CIs include zero.
- Tekin & Roediger (2021) Exp 1: N=164; recall .44/.45/.50/.52.
- Kapoor et al.: about 1,000 graded examples; user study N=181.
- Cheng et al.: Idk-SFT 74.75, prompting 66.93, 45.05% known.
- Binder et al.: self 49.6 / 48.5 vs cross plateau 36.2 / 35.2.
- Kadavath Table 1 gives AUROC/Brier per task (TriviaQA-only LAMBADA .864/.151, Python .928/.194; all-task .987/.042, .853/.108).

## Corrections
1. evidence a01 (Hart 1965) is marked opened:true but its URL is Wikipedia; Hart was never read. b27 correctly says no numbers. Treat as secondary; do not cite Hart numbers.
2. a08/b07: Rhodes and Tauber g values (.08 overall, .70 cue-target, .03 cue-only) come only from Tekin and Roediger's introduction, which describes them as recall outcomes. I recall the original meta-analysis reporting a large delayed-JOL advantage in metacognitive accuracy (about g=0.9), so these numbers may be mislabelled or may be a different outcome. Not resolved. Claim K09 marked contested. b26 "synthesis" row relies on this and should not be used as a number.
3. a24 vs c16 (Binder): the +17% headline is stated as GPT-4o as the strongest-model comparison in the intro; c16 says Llama-3-70B beats GPT-4o. The paper text also gives GPT-4o cross-predicting Llama at 31.8% and a 35.2% plateau. Use 48.5 vs 35.2 (plateau) and 49.6 vs 36.2, not the headline.
4. c27 (Didolkar): paper text says 3.5% over "Complex CoT" in one place and "Topic-Based" in another. Baseline unclear.
5. a05/b11/b12/c-rows: Koriat study-2 within-individual counts (52 positive, 5 negative) match items, not participants; the paper is ambiguous. Avoid quoting them.
6. Duplicates: Kadavath, Xiong, Tian, Steyvers, Kapoor, Lin, Yin each appear 3 or more times across a, b, c. These count as one independent source each; "independent_sources" in claims.jsonl counts papers, not rows.

## Contradictions between sources
- Tian (verbal ECE small, AUC .89 on TriviaQA) vs Xiong (verbal AUROC near chance on average): calibration (ECE) improves but discrimination (AUROC) stays weak, and TruthfulQA AUC is below .65. Different datasets and metrics; claim K17 contested.
- Delayed-JOL: gamma advantage (Kimball and Metcalfe: .76 vs .36) vs reactivity (Tekin and Roediger: effect absent in replication) vs text (Maki: no advantage). The advantage is real for word pairs, not general.
- Binder self-prediction vs Huff and Ulakci (LLM JOLs did not predict human item difficulty): different targets (own behaviour vs human memory), not a true conflict.

## Weak spots
- No FOK accuracy meta-analysis and no Hart-era replication (Gruneberg and Monks, Nelson and Narens 1980, Schacter) were found; the founding FOK evidence is thin. Search quota failed earlier.
- Ease-of-learning judgments (the S0 analogue) have almost no human evidence in the logs (Underwood 1966, Leonesio and Nelson 1990 absent).
- Illusion-of-competence literature (Koriat and Bjork 2005, foresight bias) and Dunning-Kruger style effects absent.
- Koriat's consensuality work is one lab; consensual strength is partly circular (majority size and judgment both depend on the same cue pool).
- LLM evidence is mostly 2022-2024 models; no 2025-2026 frontier reasoning-model calibration measured with AUROC. No equal-token tests of any gate.
- Most "opened" LLM claims were read from abstracts/introductions (Ji-An, Yamato, Lin tables garbled, Semantic Entropy AUROC from text).

## Seen only in snippets
Nelson and Dunlosky (1991), Weaver and Kelemen (1997), Spellman et al. (2008), b08-b10. Hart (1965) not seen at all. Rhodes and Tauber (2011) seen only as a quote.

## GAPS
1. Does a cheap pre-attempt gate (P(IK)-style or ease rating) beat a short unaided draft attempt (delayed-JOL analogue) at predicting failure, at equal tokens, for current frontier models?
2. What do Rhodes and Tauber (2011) actually report: which outcome do g=.08/.70/.03 describe, and what is the delayed-JOL accuracy effect size?
3. What is the accuracy of human feeling-of-knowing (Hart, Nelson and Narens 1980, Gruneberg and Monks) in meta-analysis, and how large is the cue-familiarity effect (Reder and Ritter, Metcalfe)?
4. Do ease-of-learning judgments (before study) predict anything in humans (Underwood 1966, Leonesio and Nelson 1990), and does an LLM easy/hard rating from the prompt alone predict failure beyond surface cues like length?
5. How large is the illusion of competence from fluency (Koriat and Bjork 2005, Kornell) and does the same fluency effect inflate LLM self-ratings (e.g., polished prompts)?
6. Do 2025-2026 reasoning models (long chain of thought) have better verbalised-confidence AUROC than the 62.7 reported for GPT-4, and does thinking longer improve or hurt calibration?
7. Does adding a self-rating step change task accuracy for LLMs (reactivity analogue), and in which direction for related vs unrelated material?
8. How well does a small probe or calibration layer trained on about 1,000 of the agent's own graded runs transfer across task classes (S0 for new classes)?
9. Is a separate small judge model's estimate of the main model's uncertainty (Kapoor) as good as self-estimate at equal cost, given Binder's privileged-access result?
10. Do metamemory judgments on long text and multi-step tasks (Maki 1998: no delayed advantage) have an LLM analogue, i.e. does the gate fail on long multi-step problems?

## Gap search results
Tools: WebSearch quota was used up; the Semantic Scholar, OpenAlex and arXiv search APIs returned 429. Sources were reached by known arXiv ids, PubMed/Europe PMC abstracts and PMC full text. Evidence is in evidence_d.jsonl (d01-d20); new claims K30-K42; K09 now established. Most human items are abstract only.

1. Pre-attempt gate vs short draft at equal tokens: STILL OPEN. No head-to-head found. Indirect support for draft-first: probes at question end are weaker than at the answer token (AUC .72-.80 vs .83-.95, d15); reasoning-model confidence improves along the chain of thought (d11). Support for a pre-attempt gate: AdaptThink -53% length, +2.4% accuracy on a 1.5B model (d20).
2. Rhodes and Tauber: CLOSED for the main numbers. Delayed JOL accuracy g = 0.93 (4,554 participants, 112 effects); memory g = 0.08 (3,807, 98 effects) (d01). So .08 is the memory effect. The .70 and .03 values are not in the abstract and stay unverified (probably subgroups); full text paywalled.
3. Human FOK accuracy and cue familiarity: MOSTLY OPEN. Hart (1965), Nelson and Narens (1980), Gruneberg and Monks, Reder and Ritter were not retrieved. Only an aging meta-analysis (age effects g = .53 episodic, -.10 semantic, d10), Koriat 1993 (d06) and Schwartz and Metcalfe 1992 cue familiarity (d07, no effect sizes). Do not quote a human FOK gamma.
4. Ease-of-learning: PARTLY CLOSED. Human EOL was the least accurate judgment (Leonesio and Nelson 1990, d02); base-rate item difficulty beat own FOK (d03). Underwood 1966 not found. LLM side: difficulty is decodable from hidden states (rho about .88 for human labels, d18), but no test of a prompted easy/hard rating against length and surface cues.
5. Fluency illusion: PARTLY OPEN. Human direction confirmed (Koriat and Bjork 2005 d05; Kornell et al. 2011 d08) but no effect sizes obtained. No LLM study found on fluency inflating self-ratings.
6. 2025-2026 reasoning-model calibration: CONTESTED. Yoon (better in 33 of 36 settings, d11) vs Mei (overconfident, above 85% on wrong answers, deeper reasoning worse, d12). No frontier-model AUROC beating 62.7 was confirmed.
7. Reactivity of self-rating for LLMs: OPEN. Nothing found.
8. Probe transfer with about 1,000 graded runs: CLOSED as partial. Ranking transfers within a family (math to math AUC .76-.83), fails across skills (d14, d15, d16); calibration degrades under shift (d13, d14). Thresholds need resetting per class.
9. Separate judge vs self: PARTLY CLOSED. Kapoor: Mistral features beat LLaMA's own on LLaMA (d13); Kadavath: no self-advantage on model A data (d16); Binder: self-advantage 48.5 vs 31.8 but modest and absent for some properties (d17). Equal-cost comparison with a small judge was not found.
10. Long-text failure analogue: PARTLY CLOSED, indirect. Binder: models failed to beat baselines for long responses (d17). No direct gate-by-length test.

Caveats: Yoon table cells and Kadavath Table 1 columns are garbled by PDF extraction; Kapoor, Orgad, Binder were read only to about 100,000 characters.
