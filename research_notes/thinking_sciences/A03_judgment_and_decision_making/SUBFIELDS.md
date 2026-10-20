# Judgment and decision making: subfields

Judgment and decision making (JDM) studies how people estimate, predict and choose under uncertainty. It divides into judgment (probability, frequency, prediction) and choice (risky, riskless, over time), and by stance: the heuristics-and-biases view (errors from shortcuts), the fast-and-frugal view (simple rules can win in the right environment), and normative models (Bayes, expected utility). Much of it concerns preferences and motives, but the judgment side has clear lessons about anchoring, wording and how to reduce errors.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Heuristics and biases | Whether intuitive judgments deviate from logic or probability, explained by heuristics: availability, representativeness, anchoring and adjustment. Findings: Linda problem, base-rate neglect, sample-size insensitivity [V1] | Tversky and Kahneman (1974, Science); attribute substitution (Kahneman and Frederick) | High | S1 input hygiene: anchors, stated guesses |
| Fast and frugal heuristics, ecological rationality | The "adaptive toolbox": take-the-best, recognition heuristic, fast-and-frugal trees; "less is more" [V1] | Gigerenzer, Goldstein, Brighton; Simon (satisficing, elimination by aspects) | Med | S0 gate; simple modes where the class allows |
| Prospect theory and risky choice | Reference points, loss aversion, probability weighting, editing and evaluation phases; critics say it describes choices, not process [V3] | Kahneman and Tversky (1979); cumulative prospect theory | Low | background only |
| Framing and preference construction | Wording changes choices ("25% fat" versus "75% lean") [V2] | Tversky and Kahneman (1981); Slovic; Payne, Bettman, Johnson [M] | High | S1: neutral restatement; paraphrase stability |
| Debiasing by training | Game-based training with feedback cut six biases over 30% at once and over 20% after three months; statistical-reasoning teaching; consider-the-alternative; perspective-taking [V2] | Morewedge et al. (2015); Nisbett et al. (1987); Hirt and Markman (1995); Fischhoff (1982) | Med | guardrails; shows feedback plus practice, not warnings, worked |
| Debiasing by structure: incentives, nudges, reference class forecasting | Incentives raise effort; nudges change defaults and framing; the outside view counters optimism [V2] | Thaler and Sunstein; Kahneman; Lerner and Tetlock (accountability) | Med | S0 gate/S7 selection: use base rates (outside view) from the class record |
| Calibration and overconfidence | Confidence versus accuracy [M] | Lichtenstein, Fischhoff; Koriat | Med | consistency not stated certainty |
| Expert judgment and forecasting | Statistical versus clinical prediction [M] | Meehl; Dawes; Tetlock | High | S7: model scores features, code combines |
| Dual-process accounts of judgment | System 1 and System 2 | Kahneman (2011) | Low | contested; see A01 |
| Intertemporal and social choice | Delay discounting, fairness [M] | Loewenstein; Fehr | Low | does not transfer |

## Dig into next

1. **Heuristics and biases: anchoring and input cues.** Questions: (a) How much does a stated wrong guess or irrelevant number move our model's answers, by class and size? (b) Does S1's marked block restore accuracy? (c) Does placing the hint after the first attempt help? Evidence: matched items with and without planted cues at equal tokens.
2. **Debiasing by training with feedback (Morewedge et al.).** Questions: (a) What exactly was in the game training (definitions, feedback, practice) and is the LLM analogue a stored lesson plus worked feedback? (b) Which biases fell most? (c) Does it transfer across bias types? Evidence: the 2015 paper's design and effect sizes, then a lesson-library test.
3. **Reference class forecasting and the outside view.** Questions: (a) Can the class record in code supply a base rate that overrides a case-specific estimate? (b) When does that beat the plain model's estimate? Evidence: Kahneman and Lovallo; our per-class pass rates.

## Does not transfer

Loss aversion, risk attitudes, time preference, regret, social preferences, incentives and nudges for human effort are about human values and motivation. Debiasing by awareness or checklists failed in people and sits on our "do not add" list. Stated confidence is a person-calibration topic.

## Sources

[V] = opened this session with WebFetch. [M] = memory or search snippet only.

1. [V] Heuristics in judgment and decision-making, Wikipedia (first 100k characters): https://en.wikipedia.org/wiki/Heuristics_in_judgment_and_decision-making
2. [V] Debiasing, Wikipedia: https://en.wikipedia.org/wiki/Debiasing
3. [V] Prospect theory, Wikipedia: https://en.wikipedia.org/wiki/Prospect_theory
4. [M] Heuristics: the good, the bad, and the biased: https://oro.open.ac.uk/66825 (403 on fetch)
5. [M] Review of cognitive biases in rule-based ML: https://arxiv.org/pdf/1804.02969 (PDF unreadable)
6. [M] Tversky and Kahneman (1974); Gigerenzer, Todd and ABC Group (1999); Meehl (1954); Tetlock (2005). No URLs.
