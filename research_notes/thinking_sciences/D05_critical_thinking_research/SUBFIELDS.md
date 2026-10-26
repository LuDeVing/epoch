# Critical-thinking research: subfields

This field asks what critical thinking is, how to measure it and how to teach it. It mixes philosophy (definitions, ideals), educational psychology (tests, interventions) and cognitive science (reasoning, bias). The Stanford entry (Hitchcock) covers history, definition, process, dispositions, abilities, knowledge, methods and controversies. The main results: it is partly teachable (a meta-analysis by Abrami and colleagues, 2015, found dialogue, anchored instruction and mentoring each help), but transfer across domains is weakly supported and depends on subject knowledge.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Definitions and ideals | What counts as critical thinking | Dewey (1910); Ennis; Facione, Delphi Report (1990) | Low | Background only |
| Process models | Stages of thinking critically | Hitchcock (SEP) | Med | State graph comparison (S1 to S9) |
| Skills versus dispositions | Abilities (inference, argument analysis) and habits (open-mindedness, willingness to self-correct) | Ennis; Facione; Halpern | Med | Dispositions map to guardrails (e.g. doubt on signal) |
| Assessment and tests | Standardised tests of skills | Watson-Glaser; Cornell tests; CCTST | Med | Benchmarks for the S0 gate and our logs |
| Instruction effectiveness | Which teaching methods work | Abrami et al. (2015) meta-analysis | Med | Evidence on what raises performance: dialogue, worked examples |
| Generalisability and transfer | Does it carry across subjects | McPeck; Ennis | High | Memory: lessons keyed to class, not shared across all |
| Bias and debiasing | Whether training cuts biases | Kahneman and Tversky tradition; Willingham | High | Confirms 4b: debiasing instructions fail |
| Argument mapping training | Diagram arguments to improve reasoning | van Gelder; Harrell | Med | Represent (S2), scoped to a task class |
| Informal reasoning research | How people reason with everyday arguments | Kuhn (Deanna); Stanovich | Low | Background only |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Definitions and ideals | | not started |
| Process models | | not started |
| Skills versus dispositions | | not started |
| Assessment and tests | | not started |
| Instruction effectiveness | | not started |
| Generalisability and transfer | | not started |
| Bias and debiasing | [`subfields/07_bias_and_debiasing/DEEP.md`](subfields/07_bias_and_debiasing/DEEP.md) | done, batch 5 (2026-10-27) |
| Argument mapping training | | not started |
| Informal reasoning research | | not started |

## Dig into next

**1. Generalisability and transfer.** Questions: (a) What does the evidence say about which skills transfer and which are domain-bound? (b) Does it support keying lessons and operator records by problem class? Evidence: transfer studies, effect sizes with follow-up.

**2. Bias and debiasing results.** Questions: (a) Which interventions measurably reduce error (as opposed to instructions)? (b) Do any involve structure that code could enforce (forced alternatives, consider-the-opposite)? Evidence: controlled studies with effect sizes, and checks for publication bias.

**3. Argument mapping and instruction meta-analyses.** Question: which of the effective components (dialogue, worked examples, mentoring) have an agent analogue (multiple isolated attempts, retrieved solved examples, lessons)? Evidence: the component tables in the meta-analyses.

## Purely conceptual

Definitions, the value of critical thinking, worries about bias in critical thinking theory (cultural and gender critiques) and the ideal of the "critical thinker" give no runnable procedure. Dispositions such as courage cannot be implemented in a program except as rules.

## Sources

1. https://plato.stanford.edu/entries/critical-thinking/ [V]
2. Abrami et al. (2015), meta-analysis in *Review of Educational Research* (cited by [1]) [V via 1]
3. Facione (1990), *Critical Thinking: A Statement of Expert Consensus* (California Academic Press) [M]
4. https://philpapers.org/sep/critical-thinking/ [M] (seen in a search listing only)
5. Ennis (1962), "A concept of critical thinking," *Harvard Educational Review* [M]
