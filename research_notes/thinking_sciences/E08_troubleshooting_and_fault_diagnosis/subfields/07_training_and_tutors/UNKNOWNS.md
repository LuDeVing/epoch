# Training and tutors: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E08.07-U1 | Does a case bank beat the same tokens spent on self-consistency, for fault diagnosis? | A case bank, consulted after the first failed hypothesis | Memory, S6 | K08, K32; single-source (Memento, one lab); no equal-token diagnosis study (d18) | A plain scaffold; B plus 4 retrieved cases; C plain with self-consistency at B's token cost. Held-out diagnosis items, bank from a disjoint set. Accuracy, tokens | B beats both A and C by 3 or more points on 2 or more models, bank cost counted | High |
| E08.07-U2 | How much does a plausible wrong nearest case hurt on diagnosis items? | Verify-before-act step on retrieved cases | Guardrail (new G), S4 | K27, K28; single-source, web agents (d03, d06) | 30% of items get a planted wrong near case. Arms: bank, bank plus verify step, no bank. Accuracy on planted items | Verify arm loses under 5 points vs no bank while the plain bank loses 10 or more | High |
| E08.07-U3 | Does an abstain-on-poor-match rule keep the gain and remove the harm? | Abstain gate on case reuse | Memory, G | K30, K20; single-source, fine-tuning analogue only; relevance gating gave no gain in d03 | Bank with and without a structured match gate; items with matched and unmatched nearest cases. Accuracy by bucket | Gate keeps 80 percent or more of the matched-case gain and cuts unmatched harm by half | High |
| E08.07-U4 | Does storing distilled strategy lessons beat storing raw traces? | Lesson-style records instead of trace storage | Memory | K10, K33; single-source plus one independent (d13); web and embodied tasks | Raw trace vs distilled lesson with difference note, same bank size in tokens. Novel-fault accuracy | Distilled wins by 3 or more points on novel items | High |
| E08.07-U5 | Which index works: symptom, cause, device family or strategy? | The winning index key | Memory | K18, K33; single-source (OM-RAG, READ-Bench); no head-to-head | Four index keys over one bank, same items. Accuracy; share of queries served by the top-1 item | One key beats symptom-only by 4 or more points and top-1 share under 30 percent | Med |
| E08.07-U6 | Do failure cases with a diagnosis line help more than success-only cases in troubleshooting? | Admit failure lessons | Memory | K11; single-source (ReasoningBank +3.2); AWM lost with raw failures | Success-only vs success plus distilled failures vs raw failures. Accuracy | Distilled failures add 2 or more points and raw failures do not | Med |
| E08.07-U7 | Does a stated strategy hint (Hydrive) make the bank redundant? | A short strategy hint, with or without bank | Guardrail, S3 | K05; single-source, human only (a09, a10) | Hint only, hint plus bank, bank only | Hint alone within 2 points of hint plus bank means drop the bank for that class | Med |
| E08.07-U8 | Does memory multiply sampling at equal tokens? | Split budget between k samples and a bank | Operator, Memory | K12; single-source (ReasoningBank flat vs +5.4) | At fixed total tokens, k from 1 to 5 with and without bank | Bank arm gains 3 or more points more than no-bank at k >= 3 | Med |
| E08.07-U9 | Does a bank interact with the fixed scaffold (additive, redundant, conflicting)? | Bank wiring into the state graph | States, Memory | K36; single-source (PMCoder p=0.011); open models show structure is not always additive (d15) | 2x2: scaffold on/off by bank on/off, equal tokens | Interaction term is 0 or positive and both-on beats scaffold-only by 2 or more points | High |
| E08.07-U10 | How much does the gain fall for faults outside the banked device family? | A rule to widen or narrow retrieval by family | Memory | K02, K35; single-source plus supported similarity result (a03, d05, d07) | Hold out one whole family; compare in-family and out-of-family gain | Out-of-family gain is under half of in-family gain: restrict bank use to in-family matches | Med |
| E08.07-U11 | Can the bank be auto-built from the agent's own runs? | Self-built bank with strict admission | Memory | K37, K29; single-source (Agent KB), supported (d01) | Auto vs expert-written bank, strict gate. Accuracy; bank size | Auto within 3 points of expert bank, no cell worse than no bank | Med |
| E08.07-U12 | Does a source-tracing step before the verdict raise evidence-complete rate? | Evidence-before-verdict rule | Guardrail, S4 | K21; single-source (Cloud-OpsBench audit) | With and without a code-checked step "name the log or test that shows the cause" | Evidence-complete up 10 points with no accuracy loss | Med |
| E08.07-U13 | How many banked cases are needed, and what novel-to-repeat mix? | Bank size cap and seed set | Memory | K09, K35; single-source plus supported (K saturates near 4; bank saturates near 3k) | Bank sizes 0, 10, 50, 200, 1000 on a mixed set | Smallest size reaching 90 percent of the maximum gain | Low |
| E08.07-U14 | Is there a case-use audit signal (copying the case without evidence)? | A copy-only flag that triggers re-test | Guardrail | K22, K23; contested human tutor studies | Log answers whose cause appears only in the retrieved case. Compare accuracy of copy-only vs evidence-backed answers | Copy-only accuracy is 10 or more points lower | Low |

## Open questions we cannot test on our bench yet

- **Sherlock-style coached practice with fading hints.** We have no learner that changes between sessions except through the bank. What would unblock it: an offline loop that replays a graded fault set with hints and distils each solved path into the bank (that is U4 and U11 in one pipeline).
- **A diagnosis benchmark with real unseen causes.** About 25 percent of Microsoft incidents had unseen causes (c06). Our bench may not separate repeat from novel faults. Unblock: tag every item by whether its cause family is in the bank.
- **Third-party replication of Memento, ExpeL and AWM on diagnosis.** None exists. Unblock: run a cheap re-implementation of each on our items, which U1 partly does.
- **Human case-library numbers (N, effect sizes).** Only abstracts of Jonassen and Tawfik were read. Unblock: full texts of Hernandez-Serrano and Jonassen (2003), Tawfik (2017), Park et al. (2020).
- **Long-term retention.** Parker's six-month check was read at snippet level. A bank that is pruned may behave differently over months. Unblock: a multi-session drift run (U-series on 200 items, repeated).
- **Physical or noisy-sensor faults.** Shape similarity is a weak proxy for same-fault relevance (d14). Our bench is text. Unblock: a time-series fault set.

## Order to run

1. **E08.07-U1:** the equal-token bank vs self-consistency test. If the bank does not beat plain sampling at equal cost, every other memory question is moot.
2. **E08.07-U2:** the planted wrong-case harm test. It is cheap and measures the largest known risk (10 to 26 point losses) before we add any bank.
3. **E08.07-U9:** the scaffold-by-bank 2x2. It tells us where in the state graph the bank belongs, and whether it is redundant with guardrails and states.
