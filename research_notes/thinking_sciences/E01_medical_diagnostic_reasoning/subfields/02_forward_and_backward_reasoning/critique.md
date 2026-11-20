# Critique: E01.02 Forward and backward reasoning (cross-check)

## Re-checked numbers (sources re-opened 2026-11-19)
Confirmed: Coderre 2004 (expert group 5/80 hypothetico-deductive; judge agreement 0.84; expertise coefficient 2.69, CI 1.64-3.75; diarrhea/nausea -1.55); Bass 2013 (31.1 to 65.6, 40.0 to 70.0, 34.7% initial, 96% vs 4%, OR 5.69 and 0.57); Goh 2024 (76% v 74%, +2 points; LLM alone +16, CI 2-30, p=.03); Klutmann 2026 (OR 3.33, 2.67; 98.9% v 66.7%; FR>BR p=.006, p<.001); Kaemmer 2021 (0.75 v 0.49; DDXC+ 0.89); Singapore dental trial (3.86/1.99/1.24; d=0.714; 80 of 152); Dual-Inf (0.533 v 0.472; interpretation 0.446 v 0.334; rare 0.483 v 0.425); MSDiagnosis (final F1 34.32 v 32.04); Savage 2024 (all MedQA figures); MedEinst taxonomy 35/43/22 and Qwen3-32B 40.25/11.86/43.46.

## Corrections and caveats
1. Coderre 2.69 is a log-odds coefficient labelled "OR" in the table. The paper's own text calls it "approximately threefold higher odds", which does not match exp(2.69) = 14.7. Do not quote it as an odds ratio. The percentage counts (5/80 v 37/80) are safer.
2. Bass 2013: the abstract on the page gives p = 0.07 for the residents' OR 5.69, while the results say p < 0.01. Internal inconsistency in the source. The CI (1.59-20.33) excludes 1, so p<0.01 is more plausible.
3. Kaemmer 2021: evidence b11 omitted the final-diagnosis accuracy for the wrong-checklist arm: 0.43 v control 0.49 (p=0.602). "May have hurt" is not supported; it was a non-significant slightly lower result. The 0.66 figure is accuracy of the student's listed diagnoses, not final accuracy.
4. MedEinst base accuracies (c08, c25): the text says GPT-5 and Gemini-2.5-Pro have "the highest baseline accuracy (54.30% and 53.58%)", but the extracted Table 1 has these values on rows labelled Lingshu-7B and Llama3-Med42-8B, and GPT-5 40.51 in the extracted row. The table layout is garbled by pdftotext; this could not be resolved. Treat 54.30/53.58 as "per the paper's text", and trap rates (Gemini 60.90, Claude 42.98, GPT-5 51.87) as the safer figures. The claim "higher accuracy means more trap-prone" is therefore moderately uncertain.
5. a16/b09/c20 give the 1986 Patel and Groen DOI as cog1001_4 (a16, b09) and cog1002_4 (c20). Semantic Scholar confirms the title with cog1001_4 (632 citations). c20 has a wrong DOI.
6. c23 mixes relative gains (LAMBADA %) with absolute points; not comparable.

## Contradictions between sources
- Expert forward reasoning (Patel 1987) v expert backward use on hard cases (Coderre 2004; Klutmann 2026): consistent only if direction is read as difficulty-driven, not expertise-driven. That weakens "experts reason forward" as a trait.
- Forward-only reasoning is linked to accuracy in humans (a05, b03) but forward feature-first tools hurt novices (b07). Direction label and tool design are different things.
- LLM evidence: explicit backward checks help (c01, c06, c10), yet clinician-style prompts do nothing (c12). Reconciled as structure v persona, but no study compares them at equal tokens.
- Dual-Inf reduced missing content but raised factual errors (c03), so a net gain depends on the metric.

## Weak spots
- The founding 1986 Patel and Groen paper was never opened (publisher blocks; Cloudflare page again this session). Its exact N and counts are unverified. All "Patel-Groen" content comes from the 1987 and 1991 follow-ups, N = 4 to 6 per group, one or two cases.
- Direction coding is by hand-coded protocols; no inter-rater data for the 1987 paper.
- Dual-Inf and MSDiagnosis gains compare against SC-CoT or fewer-module variants, with no explicit token-matching; the backward module adds calls, so equal-token advantage is unproven. Dual-Inf CI (0.055-0.062) is implausibly tight (probably across-run, not across-case).
- Dual-Inf and MSDiagnosis use text notes and Chinese admission records; no real-time data gathering.
- Meta-analysis b18 and Goh 2024 are about human-AI use, not direction.
- Many opened=false lines (a13, a16-a19, b03, b06, b08-b10, b16, b22-b25, c20, c21) are snippets or titles only; claims leaning on them (K04, K07-K08) carry that risk. Snippet-only: Norman 2014 (b06) numbers, Coderre 2003.
- Search coverage was thin (APIs rate-limited); 1990s replications (Patel 1990, 1994; Rikers 1997) and any failed replication of the forward-expert claim were not retrieved.

## GAPS (most decision-relevant first)
1. At equal token budget, does an explicit "expected findings if diagnosis d were true" backward check beat self-consistency on a held-out differential diagnosis benchmark, and does it raise factual errors?
2. Does direction instruction (forward-first v hypothesis-first) interact with case difficulty or model strength in LLMs, as Bass 2013 found with human expertise?
3. What do the original Patel and Groen (1986) data show (N, counts of forward v backward in accurate v inaccurate diagnosers), and did anyone fail to replicate it (Patel 1990, 1994, Rikers 1997)?
4. Is the MedEinst "stronger prior, higher trap rate" pattern real once the garbled Table 1 is read properly, and does a shadow-evidence penalty alone (without critic and memory) reduce trap rate?
5. Does the Dual-Inf gain hold with a non-GPT model and under matched compute, and are its factual-error increases from the backward module?
6. Do reasoning models (o1/o3, R1, Claude thinking) already show mixed forward and backward traces, and does the share shift with difficulty as in Klutmann 2026?
7. Does a generic reflect prompt harm or help LLMs relative to a content-bearing check (parallel to Norman 2014 and Kaemmer 2021)?
8. Does a candidate list that lacks the truth hurt an LLM (anchoring on supplied differentials), as Kaemmer's checklist-without-truth arm hints for humans?
9. Does multiple-choice option-first reasoning (backward from options) lower LLM accuracy against blind-first generation?

## Gap search results (2026-11-19, gap searcher)
Search was limited: the shared WebSearch budget ran out after one query, and the arXiv, Semantic Scholar and OpenAlex search endpoints returned rate limits or empty replies. Sources were opened by direct fetch (arXiv PDFs, ACL Anthology, Crossref, Europe PMC). New evidence is in evidence_d.jsonl (d01-d18).

1. Equal-token backward check v self-consistency, and factual errors: STAYED OPEN. Dual-Inf (d11, d12) reports no token or call accounting. Its factual-error rise (8.2 to 17 per 100) is measured against SC-CoT on 100 notes, not against its own ablations, so the backward module is not shown to cause it.
2. Direction instruction x difficulty or model strength: PARTLY ANSWERED, by analogy only. Thinking budget changes the harm from a misleading hypothesis in GPT-5 (10.4 to 1.7-4.4 points) and Qwen3 (11.7 to 3.9) but not in Claude Sonnet 4.5 or Gemini-3-Pro (d06). No direction-instruction study found.
3. Patel and Groen 1986 data and replications: PARTLY CLOSED. Abstract read (d01): seven cardiologists, one endocarditis case; accurate diagnosers pure forward, inaccurate mixed forward and backward. Per-group counts still unseen. Groen and Patel 1985 (d02) and a 2023 review (d03) say hypothetico-deductive use does not explain the novice-expert shift. No direct failed replication, and no Patel 1990, Patel 1994 or Rikers 1997 numbers, were retrieved. Knowledge-structure accounts (d04) are the rival explanation.
4. MedEinst table and shadow penalty: FIRST HALF CLOSED, SECOND OPEN. The paper contradicts itself: text gives 54.30 and 53.58 to GPT-5 and Gemini-2.5-Pro, while Table 1 rows give them to Baichuan-M2-32B and Lingshu-32B (trap 66.10 and 54.20). Table A2 confirms Qwen3-32B = 40.25 / 11.86 / 43.46. Trap rates above 50% hold for both groups, but the "higher accuracy, higher trap" ranking is weak (d08). No shadow-only ablation; the causal-graph module bundles forward, backward and shadow parts (d09). Added: an explicit warning prompt raised trap rate 43.46 to 60.50 (d10).
5. Dual-Inf with non-GPT models and matched compute: HALF CLOSED. Gain held on GPT-4o, Llama3-70B, BioLlama3-70B (+0.059, +0.048, +0.049, p<0.001) (d11). Matched compute not tested.
6. Reasoning models' forward/backward trace mix: STAYED OPEN. MedR-Bench (d16) measures accuracy, factuality and completeness but does not code direction.
7. Generic reflect v content-bearing check in LLMs: CLOSED in direction. Generic self-review hurt (d13), a generic warning backfired (d10), a reliability cue helped (d07).
8. Candidate list lacking the truth: MOSTLY CLOSED for supplied misleading differentials: 14 of 21 models lost accuracy, mean -5.4 points, GPT-4o -29.8 (d05). It is a clinician differential with rationale, not a bare list, so a pure list-without-truth test is still missing.
9. Option-first v blind-first in LLMs: STAYED OPEN. Only indirect evidence: option-ID bias survives debiasing instructions (d14); open-style scores about 25% below MCQ (d15).

Corrections to earlier lines: c08/c25 baseline-accuracy attribution is unresolved (paper inconsistent), not a pdftotext artefact alone. K18 now rests on an abstract (N=7, one case), not on nothing.
