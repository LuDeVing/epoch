# Critique: A05.07 Self-explanation (cross-check)

## Numbers re-opened and confirmed this session
Re-read from the source text (arXiv PDFs via pdftotext, OpenAlex abstract):
1. Bisra et al. 2018: g = .55, 69 effect sizes from 64 reports (OpenAlex dissertation abstract). Confirmed. Sub-values (g=.673, QB tests) not re-checked; they come from an opened read in the evidence files.
2. Gao et al. 2023 (arXiv 2309.12940) Table: MultiWOZ vanilla 35.93, CoT 27.64, self-explanation 44.44; STARv2 51.88 / 51.85 / 63.66. Confirmed. Prompt ablation 44.44 for "first analyze the dialogue utterance" also confirmed.
3. Huang et al. 2024 (2310.01798): GPT-3.5 GSM8K 75.9 / 75.1 / 74.7, CSQA 75.8 / 38.1 / 41.8, HotpotQA 26.0 / 25.0; GPT-4 GSM8K 95.5 / 91.5 / 89.0; 74.7% kept answer. Confirmed.
4. Chen et al. 2026 (2604.00142): +11.9, SE 5.8, t 2.06, p .030, CI [1.2, 22.6], d .44; problems 58.9 vs 16.9; kappa .78 with human consensus. Confirmed.
5. Zhao et al. 2024 (2311.06985): Self-Explain 56.6 / 59.6 / 59.7, human CoT 53.2 / 57.5 / 58.5, wrong-answer 56.0 / 59.4 / 59.1. Confirmed.
6. Chen et al. 2023 Self-Debug (2304.05128): Spider Codex 81.3 / 81.3 / 84.1; GPT-4 73.2 / 73.4 / 73.6. Confirmed.
7. Self-Debug TransCoder (c15): the pdftotext table layout shifts row labels by half a line. Reading rows as Baseline 80.4, Simple 89.3, UT 91.6, UT+Expl 92.5, UT+Trace 87.9, the evidence line c15 is CORRECT. Note the risk: the labels are not aligned in the text extraction.
8. ExPO (2507.02834): ExP-GRPO pass@4 96/91/86/76/23, GRPO-GT-CoT 95/89/83/65/12, GRPO 91/84/77/39, base pass@128 level 5 = 4%. Confirmed. Note: GRPO has no level-5 entry in the table.
9. Chi 1994 numbers (a03 to a06) were NOT re-opened: the journal PDF is paywalled (Semantic Scholar shows CLOSED). They remain from the first agent's opened read.
10. Chi 1989 numbers (a01, a02) remain second-hand.

No numeric corrections were needed. One small correction of interpretation: a22 says "Gain of about 12 points on STARv2": 63.66 - 51.88 = 11.78, fine.

## Contradictions between sources
- Chi 1989 explanation counts: 15.3 vs 2.8 (Chi 1994) against 15.5 vs 2.7 (VanLehn 1992). Not resolved; original is a scanned image.
- Bisra reports strong effects vs no-explanation controls (g=.67) but small ones against instructional explanation (g=.35); time-matched studies (McEldoon 2013, Scheitz 2025, Chen 2026) show nothing. The effect is therefore partly a time or processing effect.
- Chen 2026 shows better transfer explanation quality but equal post-test ANCOVA scores (menu -2.4, open +0.8, both ns).
- Self-explanation helps LLMs in Gao 2023 but intrinsic self-correction hurts in Huang 2024. The difference is that Gao asks for explanation before answering, Huang asks for revision after, with no signal.
- Zhao 2024: right-answer and wrong-answer explanations perform alike, which weakens any claim that explanation correctness drives the gain.

## Weak spots
- The founding study (N=8) is correlational and second-hand. The first experimental study (N=14 vs 10) has a time confound (about double the study time).
- Most LLM gains are single-benchmark, single-model-family, and from 2022 to 2023 models. Gains shrink with stronger models (Spider +2.8 Codex vs +0.4 GPT-4).
- The Chen 2026 and Lekshmi-Narayanan 2026 results use crowd or small samples (N=92; 8 students).
- No LLM study replicates the human mechanism (explain each worked-example step) at equal tokens.
- Region moderation (East Asia g=1.19, k=6) is probably an artifact of few studies.

## Only seen in snippets, or not read
- a15 Bichler 2026, a16 Scheitz 2025, a17 McGinn 2025, a28 Renkl 1997, a29 scoping reviews, b09 McEldoon 2013 (via Bisra), b10 to b12, c22 to c25: not opened as full text, so numbers there are weak.
- Lampinen 2022, Ye and Durrett 2022, Reflexion, STaR, Turpin, Lanham: opened by the evidence agents but not re-checked here.

## GAPS (most decision-relevant first)
1. At equal tokens, does one-line per-step explanation (S5) beat spending the same tokens on extra samples or a second attempt, on a current-generation model?
2. Does the gain depend on the model's strength, so that it vanishes above some capability level? Needs a ladder of models on the same task.
3. Is the useful content "name what is wrong" (error-naming) or any explanation? Zhao 2024 suggests right/wrong explanation barely matter; test a wrong-but-plausible explanation arm.
4. Does an external check (test, verifier, different model) after the explanation turn the effect from null to positive, as Self-Debug and Huang 2024 hint?
5. What are the exact Chi 1989 and Chi 1994 numbers and conditions from the primary texts (replace second-hand figures)?
6. What are the effect sizes and controls in McEldoon 2013, Matthews and Rittle-Johnson 2009, and Schworm and Renkl 2006 (time-matched and on-demand comparisons)?
7. How does explanation quality get scored reliably for an LLM agent without self-grading bias (kappa .32 to .78 in the tutor studies)?
8. Does free-text explanation beat menu-based selection for an agent (Chen 2026: +11.9 vs +4.7) outside calculus?
9. Does explanation help at the step level on long multi-step tasks, or only on short transfer items (Bisra: transfer g=.53, problem solving g=.45)?
10. Are there any 2024 to 2026 studies that apply the Chi mechanism to LLM-as-learner (few-shot with worked examples) directly? Four searches found none.

## Gap search results
Search tools: the WebSearch budget was spent by other agents, and the Semantic Scholar, OpenAlex and arXiv search APIs were rate-limited. Work was done through Europe PMC and direct arXiv PDFs (opened with pdftotext). Evidence is in evidence_d.jsonl (d01 to d19).

- Gap 1 (equal tokens, S5 vs extra samples): PARTLY CLOSED. Snell 2024 shows the answer depends on difficulty: sequential revision wins on easy items, parallel or verifier search on hard ones. Sprague 2025 says a compute-matched comparison for CoT is missing. No direct test of per-step one-line explanation at equal tokens exists. Stays open as an experiment.
- Gap 2 (model strength ladder): PARTLY CLOSED. Difficulty relative to the model controls the effect (Snell), and Sprague tested 14 models, gains concentrate in math, symbolic, logic. No clean ladder for self-explanation itself.
- Gap 3 (error-naming vs any explanation): PARTLY CLOSED. Wang 2023: invalid reasoning keeps 81 percent of CoT, irrelevance destroys it. Tyen 2024 and Madaan 2023: locating the error and specific feedback matter in the revise step. So the split is generation (relevance and order matter) vs revision (specific error location matters). No wrong-but-plausible arm run on a current model.
- Gap 4 (external check): CLOSED in direction. Kamoi 2024 survey, Tyen 2024, Madaan 2023: self-correction helps with reliable external feedback or a sufficiently accurate error-finder (about 65 percent), not otherwise.
- Gap 5 (Chi 1989 and 1994 primary numbers): OPEN. Wiley 403, ASU login redirect. Numbers remain second-hand.
- Gap 6 (McEldoon, Matthews, Schworm): PARTLY CLOSED. Abstracts of McEldoon 2013 (N=69, modest benefit over time-matched practice) and Matthews and Rittle-Johnson 2009 (n=48, no prompt effect after conceptual instruction) read. Effect sizes and Schworm and Renkl 2006 not obtained.
- Gap 7 (scoring explanations without self-grading bias): PARTLY CLOSED. Panickssery 2024 and Zheng 2023 give the bias and the mitigation (other model, order randomisation). No calibration against kappa .32 to .78 in tutor studies.
- Gap 8 (free text vs menu outside calculus): OPEN. No new source reached.
- Gap 9 (step level on long tasks): PARTLY CLOSED. Lightman 2023 (78.2 vs 72.4 vs 69.6) and Sprague 2025 support step-level checking on formal multi-step tasks; ProcessBench 2024 (opened abstract: o1-mini 87.9 vs GPT-4o 61.9 average F1 in figure) shows strong models find the earliest error step far better than weak ones.
- Gap 10 (Chi mechanism on LLM-as-learner): OPEN. Not searched again; budget gone.

Claims changed: K15 raised to supported; K05, K11, K13, K14, K21 got extra evidence; K22 to K27 added.
