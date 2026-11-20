# Critique and cross-check: Testing effect (A05.03)

## Numbers re-checked this session
1. Roediger and Karpicke 2006 (a01, b11): abstract confirmed the pattern (restudy better at 5 min, testing better at 2 days and 1 week, students more confident after restudy). Exact percentages and d values agree between two separate extractions (a01, b11). Not re-opened a third time.
2. Rowland 2014 (b01-b03): abstract confirmed the direction (recall tests beat recognition; weak support for semantic elaboration; bifurcation model viable). g=0.50, I2=84%, feedback 0.73 vs 0.39 were not re-opened; a15 repeats g=0.50 from a different source, so only the headline agrees.
3. Yang et al. 2021 (b05): abstract confirmed 222 studies, 48,478 students, g=0.499. The "bias-corrected about 0.43" in b05 stays unverified.
4. Pan and Rickard 2018 (b08): abstract confirmed 192 effect sizes, 122 experiments, N=10,382, d=0.40 [0.31, 0.50]. The abstract says moderator effect sizes were minimally affected by bias correction but intercept predictions were substantially reduced. b08 states this correctly.
5. Smith and Karpicke 2014 (a26, b15): abstract confirmed N=372 and four experiments. CORRECTION by nuance: the pooled d=0.07 hides Exp 4, where raising initial short-answer success gave short-answer and hybrid an advantage over MC. Claim K10 is marked contested for this reason.
6. Jiang et al. 2024 PIT (b29, c09): arXiv text confirmed 17.8% (it is points, 48.1 vs 30.3 EM) and 45.4/62.7 for PIT. CORRECTION: continued pretraining is 27.2 in the paper text but 27.6 in the table rows (c09 says 27.6); the paper is internally inconsistent.
7. Kestin et al. 2025 (c16): paper confirmed N=194 of 233, medians 4.5 (N=142) vs 3.5 (N=174), pre-test median 2.75, 49 min median. CORRECTION: c16 says "about 0.73 (quantile)"; the paper gives a range of 0.73 to 1.3 SD for quantile regression, with 0.63 from linear regression. The design is a crossover, so N=142 and 174 are group-period counts.
8. Adesope 2017 (b06): only abstract opened; confirms practice tests beat restudy and all other conditions. The g=0.61/0.70 figures stay unverified (secondary summary).
9. Yang et al. 2023 anxiety (b27): title confirmed; g=-0.52 not re-opened (a16 and b27 agree).
10. Mulligan 2026 (b24): not re-opened; abstract-level only.
Only 1-5 and 6-7 were fully or partly re-opened; items 2, 8, 9, 10 are unconfirmed beyond the headline.

## Contradictions and tensions
- Short-answer vs multiple choice: the old claim (short-answer is better) is not supported by Smith and Karpicke 2014; Rowland's recall-vs-recognition gap is confounded with feedback use (44% vs 11%). The two do not conflict once retrieval success is considered.
- Effect size ladders: d=4.03 (Karpicke and Roediger 2008, no-overlap scores, unmatched trial counts) vs g=0.50 (Rowland) vs g=0.40 for transfer. Lab single-experiment effects are far larger than meta-analytic averages.
- Test vs no-test controls (Pan and Sana 2021, d=1.02) give larger numbers than test vs restudy (g=0.50). Do not mix them.
- Mediator evidence: Rowland's trend fits elaboration, but Lehman and Karpicke 2016 found no mediator activation increase. Unresolved.

## Weak spots
- Most of the foundational work comes from one lab (Roediger, Karpicke). Independent-source counts are low for many claims; I lowered several that the evidence authors marked as two sources but that were one paper or one lab.
- Many a-file lines were read through Karpicke's 2025 chapter, not the original papers (a14-a22, a27, a30).
- Zero primary LLM study of the testing effect. All "LLM" lines are either quiz generation for human students (c01-c08) or LLM training or memory work used as analogy (b29, b30, c09-c11, c17). The LLM-quiz studies are small, non-randomised or measure item quality, not learning.
- Replication evidence is thin: b25 (failed negative-testing-effect replications) and b26 (Prolific nulls) are not direct replications of the core effect. No large preregistered replication of Roediger and Karpicke 2006 was found.

## Only seen in snippets or abstracts
b05 (abstract), b06, b07, b24, b25, b29, b30 (abstract), a14, a15, a16 (via chapter), c06, c18-c25 (not opened).

## GAPS
1. Is there any direct test of retrieval practice (self-quizzing) inside an LLM agent loop, after context truncation or between sessions, with token cost matched against re-reading? Search agent-memory and "self-testing" literature under other names.
2. Does a pre-registered, multi-site replication of Roediger and Karpicke 2006 exist, and how large is the effect there (Many Labs style or Registered Replication Report)?
3. What is the exact Rowland 2014 and Adesope 2017 headline effects, and how do they change after publication-bias correction? Open the full papers.
4. How strongly does initial retrieval success (the 75% threshold in Rowland) moderate the effect, and does the same hold for LLM self-checks where success rate can be measured directly?
5. Does feedback (checking against a source) account for most of the benefit, as Rowland's delayed-feedback g=1.38 (k=6) suggests, and is that cell too small to trust?
6. Do the LLM training results (PIT, Self-Tuning) reproduce on newer models, and is "question exposure before documents" a real analogue of testing, or only of format matching?
7. Is there a large randomised study showing that LLM-generated retrieval quizzes improve human learning outcomes (not item quality) vs instructor quizzes at equal exposure?
8. For agents without forgetting, does retrieval-style rehearsal change anything besides compressing a long context (for example, forcing reconstruction that exposes gaps)? Test with a gap-detection metric rather than recall.
9. What is the exact bifurcation model prediction (Kornell, Bjork and Garcia 2011) for items that fail retrieval, and does it map to agent errors that stay uncorrected without feedback?
10. Do Yang 2021's moderators (test format consistency, number of repeats, feedback) interact, so that the best-practice recipe differs from single-moderator findings?

## Gap search results (evidence_d.jsonl d01-d22; claims K27-K35 added)
Search note: WebSearch gave 3 usable calls; OpenAlex, Semantic Scholar and arXiv APIs were rate-limited or unreachable, so the OSF API, arXiv listing pages and direct PDFs were used. Rowland 2014 and Adesope 2017 full texts could not be fetched.

1. Agent-loop self-testing: STAYS OPEN. No direct test found. Nearest: Task2Quiz (d01, quiz as measurement only), ARISE (d03, learn from failures, +10.0 self / +10.9 teacher on SOP-Bench), migration-agent audit (d04, leakage warning). Cao et al. 2025 (d14) does not test the testing effect. Claim K31.
2. Multi-site replication of Roediger and Karpicke 2006: STAYS OPEN (none found). Only small pre-registered studies (d16 N=111/117 positive; d17 N=122 weak-to-absent on events). Claim K35.
3. Rowland and Adesope exact headline and bias correction: STAYS OPEN for those two papers (d22, unopened). PARTLY CLOSED by analogy: Boustani and Shanks re-analysis (d07) and Pan and Rickard (d08) show large shrinkage under correction. K05 downgraded to contested; K27 added.
4. Initial success threshold: PARTLY CLOSED. Pan and Rickard (d09) show initial accuracy is a significant moderator for transfer (PEESE +0.50); Karpicke chapter (d11) shows success decides short-answer vs MC. The 75% cut-off itself was not verified. LLM difficulty labels do not predict real difficulty (d06, rho 0.06). K28, K29.
5. Feedback as main ingredient: PARTLY CLOSED. d11 and d19 (practice with feedback only matched full instruction, preprint) support it; the Rowland g=1.38 delayed-feedback cell (k=6) was not re-opened and stays too small to trust.
6. PIT and Self-Tuning on newer models: PARTLY CLOSED. PIT order ablation re-read (d12: 38.2 vs 27.2 EM, QA before vs after doc); Self-Tuning (d13) covers Llama2-7B, Qwen2-7B, Mistral-7B. No 2025-2026 frontier replication found. Question exposure is format matching more than testing.
7. Large randomised LLM-quiz study on human learning: STAYS OPEN. Best found is An et al. 2025 (d05, quasi-experimental, ~60 students, no instructor arm); An and Wang 2026 (d06) is item validity, not learning.
8. Gap-detection rehearsal for agents: STAYS OPEN. Task2Quiz (d01) supplies a quiz metric but no rehearsal arm. Memory systems did not beat in-context.
9. Bifurcation model: PARTLY CLOSED via Karpicke 2025 (d10). Original paper not opened. Maps to uncorrected failures without feedback. K30.
10. Moderator interactions in Yang 2021: STAYS OPEN for Yang itself (not opened). Pan and Rickard (d08, d09) show stacking for transfer; best recipe differs from single-moderator findings. K28.
Corrections: Pan and Rickard N is 10,396 in the abstract text (b08 said 10,382).
