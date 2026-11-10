# E04.06 Cognitive task analysis: cross-check critique

## Numbers re-opened this session (10)
1. Bridge (arXiv 2310.10648v3), Table 1: confirmed. GPT-4 none 0.51, expert 0.83, self 0.84, random 0.26; Llama-2 none 0.53, expert 0.49, self 0.70, random 0.35; GPT-3.5 none 0.28, expert 0.45, self 0.16, random 0.17; expert-written 1.02. Entropy 6.00 vs 3.37 confirmed.
2. Bridge random-decision loss: abstract says -97%, intro says -67%. Both are in the PDF text. Computed from Table 1 (0.26 vs 0.83) the drop is about -69%. CORRECTION: use "about two thirds worse than expert decisions (table-derived); abstract says 97%". a19 quotes -67%; b16 and c01 quote -97%. Neither is wrong as a quote; the paper is inconsistent.
3. Bridge "+76% prefer, +80% useful" for GPT-4: confirmed in text. Note 0.95 vs 0.54 on the table gives +76%.
4. Tutor CoPilot (2410.03017v3): b17 (900 tutors, 1,800 students, 550,000 messages) is from an older abstract. CORRECTION: current version says 900 tutors randomised (450/450), 783 analysed (388 treatment), 1,013 students, 4,136 sessions, 350,000+ messages; +4 pp, +9 pp for lower-rated tutors, $20 per tutor, test-score estimate 0.024 SD. c04 is right; use c04 numbers.
5. Tofel-Grehl and Feldon g = 0.871: confirmed from Crossref abstract. CORRECTION: b23 gave the wrong DOI (…490166); the right one is 10.1177/1555343412474821 (a11). Journal year 2013, issue 3.
6. Edwards 2021 meta-analysis: confirmed 2205 records, 12 studies, 327 participants (162 trainees, 139 students), knowledge SMD 1.36 (0.67-2.05), technical 2.06 (1.17-2.96) for trainees. Authors themselves call these large effects without discussing inflation; the inflation caveat is ours.
7. Sullivan 2014: confirmed 71% (10/14), 51% (14/27), 73% (3.6/5), 13% how-to, 44% (20/46) to 66% (31/46). Note "3.6 of 5" is a fractional average over 3 experts.
8. Clark 2012: confirmed "nearly 70% of necessary decision steps" omitted. Abstract text read; the 4/5/1 split from b07 matches the earlier read.
9. Velmahos 2004: confirmed checklist 12.6 vs 7.5 (P<0.001) and MCQ P=0.03. Remaining values consistent with the earlier read.
10. Klein and Borders 2016: confirmed Marines N=59, .59 vs .44, d=.63, 86.9 vs 73.6. Printed group sizes (29 feedback + 31 control = 60) do not sum to N=59, and 20 improved + 8 worse = 28 of 29. Authors' own inconsistency. Mansoori 2025: confirmed 11 of 23 (48%), 9 of 11 (82%) guideline-concordant, Fleiss kappa 0.64.

## Contradictions between sources
- Bridge -67% vs -97% (above).
- a09/b07 say 1 CTA participant; a09 says authors "unverified". Authors are Clark, Pugh, Yates, Inaba, Green, Sullivan (b07), so a09's doubt is resolved. Same lab as Sullivan 2014 and Velmahos 2004, so these are not independent.
- c15 says hand-crafted insights lost to LLM insights in ExpeL; c14 shows insights beat retrieval on HotpotQA but not on ALFWorld. Task-dependent, not contradictory.
- c11 (reasoning-mode templates hurt GPT-3.5, flat for GPT-4) vs Bridge (decision scaffold helps GPT-4): difference is that Bridge decisions are domain-specific content from CTA, while Savage templates are generic reasoning styles.
- c12 (personas do nothing) vs c13 (ExpertPrompting helps by GPT-4 judge): different outcome measures, so contested.

## Weak spots
- Founding paper (Klein, Calderwood, MacGregor 1989), Hoffman 1998, Hoffman 1995, Cooke 1994, Nisbett and Wilson, Ericsson and Simon: never opened. All claims about the CDM structure come from later sources.
- Almost all surgical evidence is abstract-only, from small trials by overlapping groups (Clark lab). Counted as one source for K01.
- Whole LLM-side CTA evidence (K04-K07) is one research group (Wang, Demszky). No independent replication of Bridge was found.
- Bridge's expert arm uses gold labels on the test items, so it is an upper bound; raters judged 40 pairs per model.
- 80-90% RPD share (a03) is the model author's own coding.
- No study compares CTA content to a plain-structure control with equal time (b04 says the field cannot separate content from multimedia structure).
- Search coverage was partial: Semantic Scholar, OpenAlex and arXiv API returned 429; 2025-2026 LLM-CTA work may exist.

## Only seen in snippets or abstracts
a04, a05, a06, a07, a08, a09, a10, a11, a13, b05, b06, b07, b11, b12, b13, b14, c13, c20, b22-b25.

## GAPS
1. Does an LLM-run Critical Decision Method sweep on an agent's own failed traces produce lessons that, at equal tokens, beat plain-structure lessons and no lesson? No published test exists.
2. Is the Bridge result (decision model beats none for strong models only) replicated by anyone outside the original group, and in a domain other than tutoring?
3. Does lesson content help beyond structure? A same-length, same-format control with non-expert content has not been run in any CTA study.
4. How accurately can a modern LLM turn CDM transcripts into cue-action protocols versus human analysts (inter-analyst ceiling)?
5. What model strength threshold gates benefit from expert-cue lessons? Bridge shows GPT-4 gains, Llama-2 and GPT-3.5 do not; the surgery data shows only trainees gain. Where does it flip for current models?
6. Do failure-derived lessons (CDM-style, hard non-routine incidents) beat success-derived lessons at equal count, across model sizes? ReasoningBank suggests yes on one benchmark.
7. How many cases per task type saturate a lesson set (ICU study: 7-10 interviews)? Does the saturation point transfer to agent traces?
8. What are the real effect sizes after correcting small-study bias in the surgical meta-analyses (funnel plots, trim-and-fill, larger RCTs)?
9. Does retrospective self-explanation by an LLM about its own past action match the true cause (counterfactual cue removal), given Nisbett and Wilson?
10. Have the founding papers (Klein 1989, Hoffman 1998) reported reliability numbers for CDM probes that we can use as targets?


## Gap search results
Evidence is in evidence_d.jsonl (d01-d16). Searches: 8 WebSearch calls; arXiv, Semantic Scholar and OpenAlex APIs were rate limited, so forward-citation lists could not be pulled.

1. LLM CDM sweep on own failed traces vs plain-structure vs none: STAYS OPEN. No published test. Indirect: Wray 2024 (d06) and Data Therapist (d07) show LLM analysts and interviewers work in small pilots.
2. Bridge replication outside the group: STAYS OPEN (not found, d15). Tutor CoPilot remains the same group.
3. Content beyond structure: STAYS OPEN as a direct test. Indirect evidence is mixed: Zhao 2026 (d03) finds corrupt, irrelevant or filler condensed lessons often match real ones; SkillsBench (d04) finds curated skills beat self-written by 25 to 33 pp but lists length-matched random-text controls as future work. ReasoningBank random labels still beat no memory (d02). Add a length-matched irrelevant arm to any test.
4. LLM vs human analyst accuracy: PARTLY CLOSED for applying a codebook (d08: GPT-4 kappa 0.97/0.75/0.56 vs human 0.97/0.83/0.63; d09: blind expert preference 51.5% human vs 48.5% LLM). Open for building cue-action protocols from CDM transcripts.
5. Model strength threshold: PARTLY CLOSED, contested. SkillsBench (d05) shows a small model with skills beating stronger no-skill baselines, against the Bridge pattern. Likely depends on task type (procedural with verifier vs open judgement).
6. Failure vs success lessons: PARTLY CLOSED. ReasoningBank (d01) +3.2 pp from adding failures, AWM -2.2 pp; no equal-count failure-only arm.
7. Saturation: PARTLY CLOSED for curated lessons (d05: 2-3 skills +19.0 pp, 4+ +10.1; compact beats comprehensive, +0.7 for comprehensive). Interview-count saturation on agent traces is still open.
8. Corrected surgical effect sizes: STAYS OPEN (d13). Meta-analysis had no funnel plot, 4 studies per outcome, I2 60-87%, risk of bias some concern. MERSQI mean 13.6.
9. Self-explanation vs true cause: CLOSED as a warning (d10-d12). Models omit the cue that changed the answer: up to -36% accuracy with unmentioned bias; reasoning models verbalise hints 25% (Claude 3.7 Sonnet) to 39% (R1); larger models less faithful in one study. Counterfactual cue removal is required. No study tests CDM-style retrospection by an agent itself.
10. Founding-paper reliability numbers: STAYS OPEN (d14). Only the Hoffman 1998 abstract was reachable; no coefficient. Klein 1989 not reached.

New claims added: K20 to K24. Changed: K03 to contested, K11 to established; K12, K13, K15, K16, K17 extended with gap-search evidence.
