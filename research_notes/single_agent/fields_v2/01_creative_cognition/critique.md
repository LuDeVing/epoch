# Critique: Creative cognition

63 evidence lines, 25 claims: 6 established, 16 single-source, 3 contested.

## What is solid
- Humans fixate on examples and typical first ideas (design fixation, three sources).
- Group brainstorming loses to pooled solo work (three sources, one meta-analysis).
- LLM output is homogeneous across samples and models (four sources). This agrees with our NoveltyBench result.
- LLM judges are weak on contested taste (two independent sources).
- Creativity training works a little. The honest size after bias correction is about 0.3 SD, not 0.6.

## What is thin
- Much of the human side was read from snippets, not full texts: Ward 1994, Mullen 1991, Sio 2015, Chan and Schunn 2015, the 2019 analogy study, Scott et al. 2004.
- Many counts of "sources" collapse. Incubation has four lines but one meta-analysis. Doshi has four lines but one study. Si has two lines but one group.
- Several LLM findings are 2025 and 2026 preprints, read from abstracts. Diversity is often scored by an LLM judge, which the field itself says is unreliable here.
- Verbal overshadowing is from memory.
- Geneplore has no replication found and no LLM application found. It is a metaphor for generate-then-test, not tested evidence.

## What could be wrong
- Most human findings come from student lab tasks with one-shot ideas. They may not transfer to an LLM that can run 50 calls.
- Brainstorming loss is about humans waiting for a turn. An LLM has no turn-taking, so blocking may not apply. The transferable part is only "isolate samples, then pool".
- Diversity is not creativity. Higher spread can be higher noise. Verbalized sampling and personas raise spread; none of the evidence shows that the best output improved. Only Si 2025 checked execution, and it found a drop.
- Our own data says forced divergence hurts single-answer tasks. This field's evidence says nothing about when to switch it off. The agent needs a task-type gate, and no source here supplies one.

## What is missing that would change agent design
1. A task-type test: how to tell open-ended from single-answer. Not covered.
2. Selection after generation. Evidence says self-judging is weak, and quantity does not predict the chosen quality. Missing: any method that works (external verifier, execution, pairwise tournaments, diverse judge panels).
3. Whether divergence prompts help the best answer, not just the spread. Needs a quality-at-top-k measure.
4. Conceptual blending and constraint relaxation as concrete procedures (TRIZ, SCAMPER, "problem reformulation"). The round found no controlled evidence on them for LLMs.
5. Expert creativity studies (how working scientists and designers search), which would give procedures beyond lab tasks.
6. Whether independent resampling beats sequential "avoid previous ideas" prompting. Fixation evidence suggests independent, but the LLM evidence is one preprint.
7. Reasoning models and creativity: two benchmarks say no gain, but they are preprints with LLM judges.

## Claims to hold loosely
Verbalized sampling (single preprint), personas (contested), temperature (contested), far analogies (contested), anything from creative-b-18, b-19, b-21 (snippet, low credibility).

## Use order for the schema
Safe to act on: isolated generation then pooling, fresh context per idea, external or non-self filtering, a feasibility check on novel ideas, a gate that turns divergence off for single-answer tasks. Test in our harness before trusting: verbalized sampling, personas, near-versus-far mixing.
