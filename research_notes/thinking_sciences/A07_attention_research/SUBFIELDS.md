# Attention research: subfields

Attention research studies how limited processing is directed to some information and away from the rest. It divides into selection (early versus late, spatial and feature-based), capture (what pulls attention without intent), control (executive attention, switching, conflict), and capacity (divided attention, load, vigilance). The most useful link for an LLM is not the mechanism, which is biological, but behavioural findings: salient distractors capture, load changes how much distractors intrude, and a held goal biases what is noticed.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Early, attenuation and late selection | Where unattended input is filtered [V2] | Broadbent; Treisman; Deutsch and Deutsch; Cherry (cocktail party) | Low | background only |
| Perceptual load theory | High load uses up capacity and excludes distractors; low load lets them in; supported by response competition, capture and inattentional blindness studies [V1] | Lavie (1995, 2005) | Med | S1: irrelevant content intrudes more when the task is easy |
| Working memory guidance and biased competition | Held contents guide attention toward matching items even when it hurts; load theory and biased competition predict opposite outcomes when a held item matches a distractor under high load [V1] | Desimone and Duncan; Soto and Humphreys | Med | memory: held lessons bias what is noticed (fixation) |
| Attentional capture, bottom-up versus top-down | Exogenous, stimulus-driven orienting to sudden or bright change versus goal-driven attention [V2, V3] | Theeuwes; Folk et al. [M] | High | S1: planted hints and numbers pull answers |
| Three attention networks | Alerting, orienting, executive control; Attention Network Test [V3] | Posner and Petersen; Fan and Posner | Low | background only |
| Attentional control theory and executive functions | Inhibition, shifting, updating; Stroop and flanker tasks; anxiety impairs control [V3] | Eysenck and Derakshan; Miyake | Med | S6 switching costs, fresh contexts |
| Feature integration and visual search | Features in parallel, objects later; spotlight and zoom lens [V2] | Treisman and Gelade (1980) | Low | ARC grids only, by analogy |
| Divided and sustained attention | Dual-task costs; vigilance decrement [V2] | Kahneman (1973); Pashler [M] | Low | one task per call |
| Developmental and cultural attention | Neuroconstructivist accounts [V3] | Karmiloff-Smith; Scerif | Low | does not transfer |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Early, attenuation and late selection | | not started |
| Perceptual load theory | | not started |
| Working memory guidance and biased competition | | not started |
| Attentional capture, bottom-up versus top-down | [`subfields/04_attentional_capture_bottom_up_versus_top_dow/DEEP.md`](subfields/04_attentional_capture_bottom_up_versus_top_dow/DEEP.md) | done, batch 5 (2026-10-27) |
| Three attention networks | | not started |
| Attentional control theory and executive functions | | not started |
| Feature integration and visual search | | not started |
| Divided and sustained attention | | not started |
| Developmental and cultural attention | | not started |

## Dig into next

1. **Attentional capture by salient cues.** Questions: (a) Which kinds of salient but irrelevant material (a stated guess, a number, an authority statement, a long distractor paragraph) most reduce accuracy, by model size? (b) Does position in the prompt matter? (c) Does a marked block reduce it? Evidence: matched distractor ablations at equal tokens.
2. **Load theory versus working-memory guidance.** Questions: (a) Does more task difficulty reduce distractor impact, as perceptual load predicts, or raise it, as mnemonic load predicts, in an LLM? (b) Does what the prompt "holds" (examples, lessons) bias what is noticed, as biased competition predicts? Evidence: distractor by difficulty grid; lesson-matching-distractor condition.
3. **Executive control and switching.** Questions: (a) Is there a measurable cost when a subgoal changes representation mid-run? (b) Does a fresh context per subgoal beat carrying history? Evidence: fresh versus carried context ablation (links to S3).

## Does not transfer

Eye movements, neural networks (anterior cingulate, frontal areas), vigilance fatigue, arousal, anxiety effects on control and developmental work are about people. Load theory's capacity constructs are human; use only the behavioural prediction and test it directly.

## Sources

[V] = opened this session with WebFetch. [M] = memory or search snippet only.

1. [V] Competitive influences of perceptual load and working memory guidance (PMC4476695): https://pmc.ncbi.nlm.nih.gov/articles/PMC4476695/
2. [V] Attention, Wikipedia (first 100k characters): https://en.wikipedia.org/wiki/Attention
3. [V] Attentional control, Wikipedia: https://en.wikipedia.org/wiki/Attentional_control
4. [M] Roper and Vecera 2013; Minamoto et al. 2015; Frontiers 2021 load versus dwelling paper (urls appeared in search results, not opened)
5. [M] Desimone and Duncan (1995); Theeuwes (1992); Folk, Remington and Johnston (1992). No URLs. The Theeuwes search was blocked by the search budget.
