# Work and domain analysis: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E13.09-U1 | Does a five-level abstraction-hierarchy S0 (purpose, laws, functions, actions, forms, with why/how orphan check) beat plain or goals-only S0? | S0 template with five slots and orphan check | S0 | K01, K02; no direct test; nearest Step-Back and Self-Discover (d13, d14), older models | Plain vs goals-only vs five-level AH vs length-matched generic advice; mixed-class items, 3 seeds; pass rate by class | AH beats both goals-only and generic by 3+ points on pooled pass rate with non-overlapping seed ranges | High |
| E13.09-U2 | Is the gain of expert-decision scaffolds a content or a length effect? | Per-class expert decision lists in S0 | S0/O | K06, K21; Wang 2024, Kopka 2026 (single-source, no length control); padding hurts (d09) | Expert list vs same-length generic advice vs none; items with known expert decisions | Expert beats generic by 2+ points and beats none by 3+ | High |
| E13.09-U3 | How much does a wrong problem-class label cost, and how accurate is the agent's own label? | Label-accuracy guard with cheap exit; or drop labels if accuracy is low | S0/G1 | K07, K23; Wang random -97% (single-source); CLAMBER near chance (2023 models) | Gold vs self vs random vs no label; same items; pass rate and label accuracy | Self-label accuracy at least 75% and self beats no-label; otherwise do not add class labels | High |
| E13.09-U4 | Do independent S0 samples agree on which fact sits at which level? | Agreement check as an S0 quality gate (resample, compare) | S0/G4 | K14; no inter-rater figure for humans (d18); MAST kappa 0.88 as model | 5 S0 outputs per item; kappa of level assignments; correlate with solve rate | Kappa 0.6 or more and agreement predicts success by 5+ points; else S0 content is noise | Med |
| E13.09-U5 | Does a stable-or-open bit at S0 route better than fixed mode? | Routing bit | S0 | K15; WDA designed for stable systems (a07, a14); no LLM test | Route by bit vs fixed mode, items labelled stable/open | Routing gains 2+ points at equal tokens with bit accuracy 80%+ | Med |
| E13.09-U6 | Does a four-way order label (clear, complicated, complex, chaotic) help? | Four-class gate | S0 | K18; ACTIVE (b17), no data | Four-way label vs none vs binary stable/open | Beats binary by 2+ points; otherwise keep binary | Low |
| E13.09-U7 | Does a check loop on the S0 analysis (test the analysis against examples, revise) matter more than the analysis itself? | Verify-and-revise pass on S0 output | S0/S5/G3 | K04; Wright 2019 (14/14 vs 13/22, single-source, confounded) | S0 with vs without a check against held-out examples | Check arm beats no-check by 2+ points; token overhead under 20% | High |
| E13.09-U8 | Does a one-step abstraction before solving move errors out of S0 and into execution, and is the gain real at our scale? | One-line "principle or class" step at S0/S2 | S0/S2 | K22 (d13, d14); older models; over 90% of residual errors in reasoning | Plain vs abstraction step vs full AH; tag residual errors by stage | Abstraction step beats plain by 3+ points on 2 or more classes | High |
| E13.09-U9 | Do layered notes (purpose, workflow, unit) with contrast notes beat flat notes at equal injected lines? | Layered memory with contrast edges | memory | K10; STRATA single-source, Test-Normal mixed (c03-c06) | Flat vs 3-layer vs 3-layer with contrast; equal lines; later-split pass rate | Layered not worse than flat on all splits and better on 1 or more by 3+ points; never below no-memory | Med |
| E13.09-U10 | Does a program-or-model owner tag per function help the agent split work? | Owner tag in S0 plan | S0/section 1 | a07 (modelling only, no test) | With vs without owner tags on multi-step tasks; count of model-decided transitions | Fewer model-decided transitions and no loss in pass rate | Low |
| E13.09-U11 | Can the agent decide when to ask the human rather than act (desire vs capability)? | Ask-or-act gate | S0 | K13; WORKBank 47.5% mismatch (human-side only); CLAMBER weak detection | Act-always vs ask-at-ambiguity vs tag-based ask; tasks with missing information | Task success up with no more than 10% extra asks | Low |
| E13.09-U12 | Do S0 gains shrink on live or deployment-like tasks, as display gains (75% to 53%) and AI-tool forecasts (+24% vs -19%) did? | Expected-shrinkage factor in G7 reporting | G7 | K05, K25 (single-source, human or developer settings) | Run U1 winners on a held-out work-task set; compare gain size | Report only. If live gain is under half of benchmark gain, hold back the element | Med |
| E13.09-U13 | Are residual failures execution or problem-class misreading? | Failure tagging by MAST category and hierarchy level in logs | Logs/S6 | K24; MAST (d11) not keyed to levels; Step-Back over 90% in reasoning | Tag our failures by hand or by a judge checked on a sample | If over 50% of failures are misreading, strengthen S0; if under 20%, deprioritise S0 work | Med |
| E13.09-U14 | Decision-ladder shortcut: skip S1-S2 on a class with a high plain pass rate | Fast path rule | S0/G11 | a08, a04, K01; no LLM test | Shortcut vs always full S1-S2 at equal tokens | Same pass rate at 20%+ fewer tokens | Med |

## Open questions we cannot test on our bench yet
- DURESS II numbers (N, effect sizes, novel faults) and any replication. Publisher PDFs were blocked. Unblock by retrieving the 1995-1998 papers through a library.
- Chang Lee and Rondinelli 2026 (24.9% to 44.1% coverage). Paper not located again; unblock with the exact arXiv id and a re-run of their baseline.
- Pooled effect size for ecological interface design. No source found; needs a systematic search beyond the APIs used, or a new meta-analysis.
- Inter-rater agreement for human WDA. None found. Would need two analysts on one domain.
- Real-user outcomes of scaffolds (child or learner outcomes, live users). Our bench has no live users.
- Whether current frontier models label problem classes better than the 2023 models in CLAMBER. U3 answers this for our classes only.
- A work-task failure taxonomy keyed to work-domain levels. Needs a labelled failure set from TheAgentCompany or GDPval runs.
- Whether the Zhang 2024 AR-HUD result was "3 of 5" scenarios (text and listed numbers differ). One fact check in the paper.

## Order to run
1. E13.09-U1 (five-level AH vs goals-only vs generic advice): the only direct test of the subfield; its length-matched arm also answers U2.
2. E13.09-U3 (gold vs self vs random label): tells whether any S0 class label is safe; cheap, reuses the U1 items.
3. E13.09-U7 (check loop on the S0 output): cheapest add-on, and the best-supported human moderator (iterative evaluation) points here.
