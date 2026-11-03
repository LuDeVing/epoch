# Systematic design: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E07.01-U1 | Does a staged clarify-abstract-function-principle-evaluate prompt beat a plain prompt on a frontier model? | A staged open-mode flow (S1, S2, S3) | S1, S2, S3 | K19, d11: no study exists; human evidence weak (K01) | Plain vs generic extra steps vs staged-in-order vs staged-shuffled; open design briefs with 8-12 requirements; requirement coverage, distinct concepts, pass^3 | Staged beats plain AND generic-extra by 10 or more coverage points, 3 seeds | High |
| E07.01-U2 | Does a code-owned requirements ledger (fixed IDs, unmet-ID list after each stage) fix requirement loss? | Ledger in S1 plus check at every stage end | S1, G4 | K25 conjecture; K11 (coverage at most 20%, partly bookkeeping, d01, d16) | Staged flow with vs without ledger; same briefs; blind per-ID semantic coverage | Coverage +15 points or more, no drop in quality score | High |
| E07.01-U3 | Does a stage-end check (go on / repeat / go back), computed by code, beat stages without checks? | Gates at the end of S1-S3 | S4, G2 | K13 single-source (+15.6% verification topology, b20); K20 (VDI 2222 had gates, 2221 lost them) | Staged without gates vs with code gates; code tasks with unit tests and constraint tasks; held-out pass rate | +8 points or more at equal tokens | High |
| E07.01-U4 | Is a fixed S1-S9 order worse than a check-chosen subset and order? | Flexible order rule in S0 | S0, G7 | K02 established for humans (a09, a11); K23 single-source for LLMs (d06, once per task) | Fixed vs check-chosen vs plain; mixed easy and hard items; accuracy and tokens | Flexible matches fixed accuracy with 20% fewer tokens, or beats it | High |
| E07.01-U5 | Does a solution-neutral abstraction step widen the set of solution principles found? | Abstraction sub-step in S1, S3 sees only the abstract | S1, S3 | K05 single-source (Roth worked example, no trial, a14); LLM fixation shown (d08, d09) | Generate from literal vs abstract task; open design items; code-clustered distinct principles, share of typical answer | +1 distinct principle per item, no loss on checker score | Med |
| E07.01-U6 | Does a typed function-structure graph with code validation improve later concepts? | Graph check in S2 | S2 | K10 (human study, a22), K14 (LLM graphs error-free only 16%, b16) | Free-text decomposition vs validated graph with repair loop; design briefs; checker score of final concept | +5 points checker score, graph error rate under 10% | Med |
| E07.01-U7 | Does a morphological table (sub-function x principle, code combines) beat a free list of concepts? | Morphological table in open mode | S2, S3 | K07 single-source (n=7 per group, confounded order, b04); c23 author metric | Free 5 concepts vs table; open design; distinct concepts, best-of checker score | +30% distinct concepts and no loss on best score | Med |
| E07.01-U8 | Is the scaffold gain bigger for weaker models and for novel items? | Gate rule: route by model strength and novelty | S0 | K03 established for humans; K22 mixed for LLMs (d04, d05, d14, d15); K04 single-source | Scaffold vs plain on one weak and one strong model; items tagged novel or routine; gain per cell, token ratio | Gain differs by 8 points or more between cells, in a stable direction | Med |
| E07.01-U9 | Does a persistence rule (keep a rejected concept alive until a check fails twice) stop early abandonment? | Rule in S5/S6 | G6, S5 | K17 single-source, one hackathon run (b14); K26 (d08, d09), no frontier replication | Drop-on-first-fail vs two-fail rule; tasks with a transient hitch; final success, abandonment rate | +10 points on hitch tasks, no loss elsewhere | Med |
| E07.01-U10 | Should early structure sketches be allowed inside the clarify and function stages? | Provisional-structure note in S1/S2, kept out of S3 | S1 | K08 human-only (b03); anchoring risk (d09) | Blocked vs sketch-allowed (and hidden from S3); open design; distinct concepts, anchoring share | More distinct concepts and anchoring share not higher | Low |
| E07.01-U11 | Does repeat-run agreement (entropy) flag wrong S2 decisions? | Entropy as a hint for impasse trigger | G5, S6 | K16 single-source (7 of 10 TRIZ cases, a26); G4 says agreement is only a hint | Run S2 decision 5 times; correlate entropy with later failure; AUROC | AUROC above .65 on at least two item types | Low |
| E07.01-U12 | Can per-stage token caps keep the staged flow inside the plain arm's budget without losing the gain? | Stage budget table | G7 | K09 human-only (b08); K24 (35-600% extra time, d04, d07) | Staged at caps of 10%, 20%, 40% of budget vs plain; coverage per token | A cap exists where staged still beats plain by 5 points | Med |
| E07.01-U13 | Does a stage-specific lesson memory (which stage was decisive per problem class) help later items? | Class record field "decisive stage" | memory | No direct evidence; indirect only (K03) | Run with vs without the record over 3 passes on the same classes; accuracy and tokens | +5 points on repeat classes, no harm on new classes | Low |

## Open questions we cannot test on our bench yet

- Original effect sizes from Fricke (1993/1999), Ehrlenspiel and Dylla, Bender (2004), Rueckert (1997). Only Motte's summary was read. Unblock: obtain the German originals or Motte's source tables.
- Whether the 2019 VDI 2221-1 restored decision checks. Unblock: read the guideline text.
- A benchmark of novel versus variant design items for LLMs. Unblock: tag our open items by novelty with an outside rater.
- Real mechanical embodiment stages (layouts, prototypes, physics). Our bench has no physical build or solver; the Massoudi and Fuge ladder (levels 2-7) is also unmeasured. Unblock: a pint/sympy unit check at least.
- Frontier replication of Egea's hackathon (single run, human hands). Unblock: a simulated build loop with a hitch.
- Long-run effect on human users (time pressure, motivation, d=.59) has no counterpart in a model; skip.
- Cash et al. (2023) chain-of-evidence counts (abstract page only). Unblock: full text.

## Order to run

1. E07.01-U1 (staged vs plain vs generic-extra vs shuffled): it decides whether any stage list is worth keeping and separates order from content.
2. E07.01-U2 (requirements ledger): cheap code, directly attacks the largest measured LLM failure (requirement loss, at most 20% coverage).
3. E07.01-U3 (code-computed stage-end gates): the best-supported single fix (verification), and cheap to build on top of U1.
