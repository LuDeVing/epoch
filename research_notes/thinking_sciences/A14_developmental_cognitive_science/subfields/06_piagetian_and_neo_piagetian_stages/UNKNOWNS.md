# Piagetian and neo-Piagetian stages: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A14.06-U1 | Does feeding prerequisite sub-answers first beat plain CoT on a strong model? | A "prerequisites first" step inside O3 Decompose | O3 | K13, K23; single-source; small or 2022 models; d09, b04 | Items with 4+ dependent steps. Arm A plain CoT; arm B prerequisite chain; same total tokens. Metric: accuracy | B beats A by 3+ points on 5+ step items with no loss on short items, over 2 batches | High |
| A14.06-U2 | Does a code-held current-rule register fix rule-switching failures? | A rule register line in the state record | S5/S6 state line | K24; single-source; d13, a25; reasoning gave no WCST gain | WCST-style items with mid-item rule change. A plain; B register updated by code after each feedback; equal tokens. Metric: accuracy | B at least +10 points over A | High |
| A14.06-U3 | Is a one-line conflict check as good as long reasoning on interference items? | Conflict-check step for items with distractors or misleading cues | G11 / S2 | K17, K24; d13 (Llama-8B 0.471 to 0.910, thousands of tokens) | Flanker-like and misleading-cue items. A direct; B one-line check; C long reasoning. Metric: accuracy and tokens per correct | B within 3 points of C at under half the tokens | High |
| A14.06-U4 | Does assimilate-first memory help in our scaffold, and does accommodation add anything? | Assimilate-before-write rule for lessons and subgoal library | memory (S9) | K26 established for part ablations only; d04, d03, d01; small models; no accommodation ablation | Multi-session items. A always-write; B assimilate-first; C B plus accommodation on mismatch. Metric: F1 and tokens | B beats A by 5+ points; C counts only if it beats B by 3+ | High |
| A14.06-U5 | Does splitting high-arity steps into ternary then binary parts lift accuracy at fixed entity count? | Arity tag and segmentation rule in O3 | O3 / S2 | K07, K25; single-source (REL); operand complexity also matters; d11, d12 | Items with RC 3 to 9, fixed object count. A direct; B stepwise binary split; equal tokens. Metric: accuracy slope by RC | Slope flattens in B and B beats A by 5+ at RC 6+ | Med |
| A14.06-U6 | Is the answer bias toward "same / no change" present in our agent on state-judgment items? | Paired-item scoring rule in bench; evidence-first step if bias found | G3 / bench | K22; single-source; VLM only; d10 | Text items with change vs no-change answers, with and without evidence. Metric: share answering "no change" with no evidence | Blind rate above 60% and an evidence-first step cuts it 15+ points | Med |
| A14.06-U7 | Does naming the governing concept first help at equal tokens? | "Name the principle" line in S2 | S2 / O | K15; established but multimodal and prompt-confounded; b09, c09, c10 | Items with a named principle. A no hint; B concept stated first; same total tokens. Metric: accuracy | B at least +3 points on 2 batches | Med |
| A14.06-U8 | Does the scaffold hold up on perturbed social-reasoning items, where CoT stops helping? | Perturbed items as a standing bench class | G | K27; older open chat models only; d05 | Clean vs perturbed false-belief items. A plain; B CoT; C scaffold. Metric: accuracy gap clean minus perturbed | Scaffold gap under half the CoT gap (CoT clean gain 22.4 vs perturbed 3.9) | Med |
| A14.06-U9 | Does an external list lift n-back-like tracking beyond n=3? | Code-held scratch list for dependency tracking | memory | K18; single-source; a24, c16 | n-back and variable-tracking over long context. A in context; B external list. Metric: d' and accuracy by n | B at n>=3 above A by 10+ points | Med |
| A14.06-U10 | Does asking once instead of re-asking reduce answer flips for agents? | One-question rule in the clarify step | G1 / S1 | K02; human data only; a16, d14 | Items where the clarify step re-asks. A re-ask loop; B single ask. Metric: answer flips and accuracy | B has fewer flips with no accuracy loss | Low |
| A14.06-U11 | Do trivial-item probes predict failures on harder items within one model? | Simplest-item probe per class in S0 | S0 class record | K14; correlation across models only; b10 | Per class: 5 trivial items plus main items. Metric: within-model prediction | Probe failure predicts main failure (AUC 0.7+) | Low |
| A14.06-U12 | Does a stage-ordered scaffold of any kind pay for its setup cost? | Nothing new (this is the G7 check on U1) | G7 | critique gap 1; no equal-token test exists | Run U1 with setup tokens counted in arm B | Net accuracy gain after setup cost is positive | High |

## Open questions we cannot test on our bench yet
- LLM versus child on the same conservation or seriation task: needs child data collected with identical items. No such study exists.
- Perception versus response prior in VLMs: needs shuffled-image and matched-blank controls; our bench has no vision items.
- Original numbers for mountains (1956), Samuel and Bryant means, Pascual-Leone M tables: need primary papers or library access.
- Multi-lab object-permanence replication: needs a registered replication that does not exist.
- RL-trained reasoning models on perturbed false-belief items: needs access to those models and a perturbation set (d05 excluded them).
- The Nov 2025 Demetriou preprint on LLMs and developmental theory: page returned 403; reopen when available.
- Token cost of conflict-check reasoning: only "thousands" reported; we must measure it ourselves.

## Order to run
1. A14.06-U1 (with U12 setup-cost accounting): tests the central claim that prerequisite order helps at equal tokens; one batch, and decides whether stage ideas matter at all.
2. A14.06-U3: one-line conflict check against long reasoning; cheap, and the token saving matters for G11.
3. A14.06-U4: assimilate-first memory; strongest existing support (three systems) and a direct effect on section 5 memory.
