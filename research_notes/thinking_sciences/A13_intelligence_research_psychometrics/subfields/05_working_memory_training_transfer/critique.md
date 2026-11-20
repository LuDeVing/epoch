# A13.05 Working memory training transfer: critique

## Corrections made (numbers re-opened this session)
Re-opened and confirmed against text in D:/research_scratch/A13.05: Jaeggi 2008 (trained d=0.65, t(33)=5.53; control d=0.25, t(34)=2.08; F(1,67)=5.27, p<.05, partial eta2=0.07), Hu and Lewis 2025 (retrieval 1/2/3-back: Llama 3.1 70B 1.00/0.99/0.93, Llama 3.1 8B 1.00/0.14/0.17, GPT-3.5 1.00/0.51/0.43), Huang et al. 2025 (GPT-4o 1.085, DeepSeek-R1 0.640, 173 failures), Soveri 2017 (n-back g=0.62, Gf g=0.16 [0.08,0.24], control analysis Gf g=0.11 p>.05, overall 0.11 [0.00,0.22] p=.048, age p=.794), Sprenger 2013 (253 participants, two experiments), Chooi and Thompson 2012 (text opened, setup consistent).

Corrections:
1. a14 said "284 effect-size values verified". Wrong. Soveri has 203 effect sizes from 33 RCTs (13 excluded as outliers). The 284 figure is raw means in an inter-rater agreement check on ten studies. Use 203 / 33 (b09 is right).
2. a01 gives "n=16, 22, 16, 15 per experiment". These are group totals (trained plus control) per dose level. Trained subgroups were n=7, 8, 11 (Redick, b03); 34 trained plus 35 controls. b01's N=70 does not match the paper's t(33) and t(34), which imply 69.
3. b11 attributes nonverbal g=0.15 (active) / 0.26 (passive) to Au 2015. In Soveri's text these are Melby-Lervag and Hulme 2013 (a11). Au 2015 is Gf g=0.24, later 0.13 (Au 2016).
4. Chooi and Thompson cell sizes ran from n=4 to 21, so the null is weaker than Redick's.

## Contradictions between sources
- Soveri: active vs passive control difference g=0.03 (p=.429). Sala and Gobet: passive 0.18 vs active 0.05. Melby-Lervag 2016: untreated 0.20 vs treated 0.05 (K05).
- Gong 2024: only GPT-4 above d'=1. Hu and Lewis: Llama 70B near ceiling, GPT-3.5 0.51/0.43; the failure is task understanding rather than capacity (K12).
- Au 2015 Gf g=0.24 vs Soveri 0.16 vs Sala and Gobet 0.11; spread follows control type and inclusion rules.
- Jaeggi 2010 BOMAT gain did not differ from control, while RAPM d=.98 (b03).

## Weak spots
- Not re-opened this session (earlier agents marked them opened): Melby-Lervag 2016 (b05 to b07; local text was a stub), Sala and Gobet 2017, Foroughi 2016, Gobet and Sala 2023, Redick 2013 power figures, Gong 2024 p-values.
- No numbers read: Harrison 2013 (b16), Shipstead 2012 (a10, b18), Simons 2016 (a17), Au 2015 (a13, b11). Abstract only: a06, a07.
- Snippet or abstract only: a12 (2019 reanalysis), a23, b24, c20, c21, c25; c23 and c24 are placeholders.
- LLM evidence is entirely probing, not training; a22 is a negative search, not proof of absence.
- RL-transfer studies (c13 to c17) connect only loosely to the human WM-training question.
- Several single-source LLM claims rest on one prompt set and one model family.

## GAPS
1. Does any LLM study train or fine-tune on n-back or span tasks and then test matrix or ARC-style reasoning with an equal-compute control? (Decides whether "no shortcut" holds for models.)
2. What exactly do Melby-Lervag 2016 and Sala and Gobet 2017 report (re-open full text), and is the active-control moderator real, given Soveri's null?
3. How large is the expectation effect in a prompt-only scaffold, measured against an equal-token placebo prompt (Foroughi's RAPM d=0.50 analogue)?
4. How much of the Gong vs Hu and Lewis disagreement is prompt wording? Run both prompts on one model at equal tokens.
5. Does an external scratchpad or memory buffer raise n-back and tracking accuracy more than the same tokens of free chain of thought?
6. Are there 2018 to 2026 large multi-site human RCTs of WM training that postdate Soveri 2017, and do they agree?
7. Who gains in humans (low ability, strategy users)? This bears on whether per-item scaffold choice matters.
8. Do human boundary conditions (dose, single vs dual n-back, age) have LLM analogues (context length, number of demos, model size)?
9. Does proactive interference (Wang and Sun 2025) respond to a structured memory reset across model sizes at equal tokens?
10. Do RL game-training gains (ViGaL, SPIRAL) survive format and pretraining controls, and why does ARC not benefit?


## Gap search results (run d, evidence_d.jsonl d01 to d21)
Closed or largely closed:
- Gap 2 (closed). Melby-Lervag 2016 and Sala and Gobet 2017 re-opened in full text (d01 to d03). Far transfer, treated controls: nonverbal g=0.05 [-0.02,0.13] vs untreated 0.20 [0.11,0.28], difference Q(1)=6.09, p=.01; verbal, decoding and arithmetic show no reliable gap. Sala and Gobet: passive 0.18 vs active 0.05, near transfer 0.44 to 0.46. The active-control moderator is real for nonverbal ability in two meta-analyses; Soveri's 0.03 difference (p=.429) stays unexplained, so K05 stays contested. Note: the printed CI [-0.09,0.26] around 0.18 in Sala and Gobet looks like a typo.
- Gap 6 (largely closed, thin search). No large multi-site RCT after 2017 reverses the null. Post-2017 evidence: Sala and Gobet 2020 (N=2,375 children, active-control far transfer g=0.001), Gobet and Sala 2022 (grand mean 0.12 naive, 0.00 active), Blacker 2017 (73 completers, BOMAT group x session p=.47), Pahor 2022 (460 people, replication-sample effect B=0.07, p=.50, passive control). A 2025 preregistered trial mentioned in search output was not identified. Caution: the Sala and Gobet papers share authors.
- Gap 3 (partly closed by analogue). Length-matched placebo prompts recovered +19.5 of +22.0 points on a 0.5B code model; frontier model at ceiling (d14, d15). Equal-token controls are not neutral: padding costs accuracy (0.92 to 0.68 at 3,000 tokens, d13) and filler tokens can add compute (d12). No direct measurement on our scaffold; that needs our own run.
- Gap 4 (document comparison only). Prompts, metrics and models differ between Gong and Hu and Lewis (d10). Not run on one model at equal tokens.
- Gap 7 (partial). Compensation correlation in Traut 2021 (82 coefficients, 25 papers, I2=91%), inconclusive; training moves efficiency, not capacity (von Bastian 2022).
- Gap 8 (partial, by analogy). Dose, age and training-type moderators in Melby-Lervag are mostly artefacts of small problematic studies; LLM analogues seen: model size (Wang and Sun, Hu and Lewis), demos (Hu and Lewis), starting strength (SPIRAL gains +10.5 vs +1.4). No study varies context length, demos and size together.
- Gap 9 (partial). Wang and Sun: forget prompts fail; mock-QA reset helps partly on four models; no size-tier analysis and no equal-token control.
- Gap 10 (partial). ViGaL random labels give no gain (49.4 vs 49.1) and SFT on the same data falls to 47.2; SPIRAL beats SFT (44.5 vs 39.7). Neither paper tests ARC, so why ARC does not benefit stays open.

Stayed open:
- Gap 1: no LLM study trains on n-back or span and then tests matrix or ARC reasoning (search thin: arXiv API empty, OpenAlex and Semantic Scholar rate-limited, 3 web searches).
- Gap 5: no head-to-head of external memory buffer vs free chain of thought at equal tokens; only Gong's written-after reasoning variant (no gain, capacity about 3).

Not tested because no model runs were made: gaps 3, 4, 5 and 9 need experiments of our own.
