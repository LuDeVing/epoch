# Critique: E13.06 Naturalistic decision making

## Corrections and re-checks (this session)
Re-opened and confirmed against full text:
- Liu et al. (arXiv 2410.21333): 87.5 vs 64.4 (GPT-4o grammar, p<0.0001); 94.00 zero-shot vs 57.7 o1-preview (the -36.3 is a cross-model comparison, not a same-model CoT drop); face recognition 64.0 to 51.2 and 44.0 to 29.6; rounds 2.9 vs 12.5 (+331%); ToT 64.55 vs 62.52. All confirmed. Extra: bigram-instructed CoT reaches 68.43; 3-node grammar shows no difference; temperature robust.
- Kahneman and Klein (2009): 30 researchers in 1989; Goldberg 29 clinicians, 861 patients, 11 scales; 10,000 hours for chess masters (Chase and Simon). Confirmed. Line a06 says "judges"; they were clinicians.
- b05 wording "-1.8 pt drop" is a gain of 1.8 points (65.9 to 67.7).
- b04 (2024) and c16-c18 (2025) are the same paper (arXiv 2024, later venue version): one source, not two.

Could NOT re-open: Kopka and Feufel (2026, JMIR, doi 10.2196/88053). The doi redirects to biomedeng.jmir.org but page text came back empty. Its numbers (63.3 / 67.6 / 66.7; OR 2.26) rest on earlier agents' reads (b01-b03, c01-c07), which are the same paper, not independent. Treated as single-source.
Not re-checked: ShadowBox d values, referee meta g = 1.718, unconscious-thought meta-analysis, R-CAST numbers, Belling 2014 details. Only 2 of the 10 target numbers groups were confirmed first-hand (Liu, Kahneman and Klein); the rest are carried from earlier agents.

## Contradictions
- Kopka preprint (RPD 70.2, default 64.7, self-care 18.5 to 37.6) vs published (67.6, 63.3, 13.4 to 29.8). Use published.
- RPD share: 80-90 percent (a09, b06 via Macquet), 95 percent recognitional (naval, a26), Macquet range 60-81 percent simple match. Differences are domain and coding. Original 1986 counts unverified.
- Take-the-first: Johnson and Raab 2003 supports; Belling 2014, Klein and Peio, Laborde and Raab 2013 null or partial.
- RPD prompt: "reasoning models gain more" (OR 2.15) vs smaller absolute gains for o3 (+4.4) and a loss for GPT-5.2 Instant.
- Fast vs slow under time pressure: tiny referee effect, null meta-analysis, expertise moderator opposite to theory.

## Weak spots
- The only direct LLM test of NDM is one team, one domain (triage vignettes), accuracy only. RPD gains came from more self-care calls; overtriage is 88 percent of errors, so it may be a shift in bias. Tokens not matched.
- Founding 1986 study never opened in full; 80-90 percent is a repeated secondary number.
- Most human evidence is sport, small N, video simulation.
- R-CAST agent work is 2005-2009 on student teams.
- Snippet or Wikipedia level only: a26-a28, b10-b12, b19-b23, c08, c12, c28, c30.

## GAPS
1. Does an RPD-style prompt (one candidate, simulate, test) beat default and best-of-N at equal tokens on non-medical tasks with checkable answers?
2. Is the Kopka gain real accuracy or a shift in answer distribution (more self-care calls), checked on a balanced dataset?
3. Which task features predict when a direct pattern mode beats deliberate reasoning for LLMs (Liu archetypes), and can a cheap router detect them?
4. Does first-candidate quality beat later candidates for LLM generation (take-the-first test)?
5. Do premortem, Critical Decision Method or data-frame prompts help LLMs when triggered only on a failed check (G1) versus always on?
6. What are the exact 1986 counts and coding rules behind 80-90 percent RPD, and do later coded studies agree?
7. Do expert-ranked exemplars (ShadowBox style) improve agent decisions at equal context length?
8. Are RPD-agent results (R-CAST) replicated with modern LLM agents in multi-task switching?
9. How well do LLMs stand in for expert decision makers across crisis tasks beyond one scenario?
10. Do time-pressure analogues (token caps) degrade LLM decisions the way stress degrades human experts?

## Gap search results (2026-11-19)
Tools were limited: arXiv API, OpenAlex and Semantic Scholar returned rate-limit errors, and the WebSearch budget ran out after one call. I read full PDF text of 10 papers (evidence_d.jsonl d01-d11), found via direct arXiv PDF links. Gap-by-gap:

1. Gap 1 (RPD prompt vs best-of-N at equal tokens, non-medical): PARTLY CLOSED indirectly. NoThinking vs Thinking at matched tokens (d01), repeated sampling (d02) and difficulty-matched allocation (d03) give measured results, but none uses an RPD-style prompt. Direct test still open.
2. Gap 2 (Kopka gain vs answer-distribution shift): OPEN. No search possible; no balanced-dataset re-test found.
3. Gap 3 (task features for pattern vs deliberate mode, cheap router): PARTLY CLOSED. Difficulty-based routing is supported by Snell, Chen and Han (d03, d04, d09, d14), about 4x, 48.6 percent and 67 percent savings. No router on Liu's implicit-pattern archetypes found.
4. Gap 4 (first candidate beats later ones): MOSTLY CLOSED for reasoning models on math: first round correct in over 92 percent of cases (d04). It shows later rounds add little, not that the first is best; harder sets not checked.
5. Gap 5 (premortem / CDM / data-frame, triggered vs always): OPEN. Indirect only: always-on self-correction hurts (d06), always-on verification helps fact precision (d11). No trigger comparison.
6. Gap 6 (1986 counts and coding): OPEN. DTIC PDF damaged, citation page 403; Frontiers and Wikipedia give only the 80-90 percent (d12, d13). Needs the original proceedings.
7. Gap 7 (ShadowBox-style exemplars at equal context): OPEN. Only weak adjacent support: few-shot examples fixed the spurious-feature failure (d07).
8. Gap 8 (R-CAST replication with modern agents): OPEN, not searchable.
9. Gap 9 (LLMs as expert stand-ins across tasks): OPEN, not searchable.
10. Gap 10 (token caps vs stress): PARTLY CLOSED. Caps shorten output with small loss until a floor (TALE d09); longer reasoning hurts only on noisy or distractor tasks (d07, d08). No human-stress-style degradation; the analogy is weak.

Caveats: d05 and d11 table numbers come from a garbled text extract; d10 used only the abstract and introduction. Re-run gaps 2, 5, 6-9 when search quota returns.
