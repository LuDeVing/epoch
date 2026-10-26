# Behavioural economics: subfields

Behavioural economics tests how real choices depart from the textbook rational agent. It divides into bounded rationality and satisficing, heuristics and biases, fast-and-frugal heuristics and ecological rationality, prospect theory, choice architecture and nudging, behavioural finance, behavioural game theory, and resource-rational models. The two heuristic programmes disagree: one counts departures from logic as errors, the other asks when simple rules win. Both bear on how much effort one agent should spend. The nudge evidence is contested, as set out below.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Bounded rationality and satisficing | Limits of time, information and mind; choose an option that meets a standard | Simon (Nobel 1978) [V via Wikipedia] | High | S0 gate; stopping rule G11, G12 |
| Ecological rationality, adaptive toolbox | Fast and frugal rules that work where optimising is infeasible; they exploit environment structure and can beat optimal procedures | Gigerenzer, Selten [V via Wikipedia] | High | Direct mode; S0 class record |
| Heuristics and biases | Anchoring and adjustment, availability, representativeness, framing | Kahneman, Tversky [V via Wikipedia] | Med | S1 input hygiene |
| Prospect theory | Loss aversion (median coefficient about 2.25), probability weighting; critics say loss aversion is less robust than claimed | Kahneman, Tversky; Gal [V via Wikipedia] | Low | Background only |
| Choice architecture and nudging | Defaults, ordering, framing change choices | Thaler, Sunstein [V via Wikipedia] | Med | Prompt layout |
| Nudge evidence | Mertens et al. 2022: over 200 studies, 450+ effects, 2.15 million people, d = 0.45 (95% CI 0.39 to 0.52), moderate publication bias; structure changes beat description changes; food up to 2.5 times larger. Maier et al. 2022 reanalysis: "No evidence for nudging after adjusting for publication bias." DellaVigna and Linos: nudge-unit trials on 23 million people show much weaker effects | Europe PMC records [V]; Wikipedia [V]; Maier abstract not read | Med | Guardrail G7 (measure before keeping) |
| Behavioural finance and game theory | Investor biases; fairness, reciprocity | Camerer, Rabin, Shleifer [V via Wikipedia] | Low | Background only |
| Debiasing | Training or tools that reduce bias | Larrick, Soll [M] | Med | Fits SCHEMA 4b: checklists fail |
| Resource-rational analysis | Optimal use of limited computation | Lieder and Griffiths 2020 [M] | High | S0 gate; meta-reasoning |
| Noise and judgement | Unwanted variance across judges | Kahneman, Sibony, Sunstein 2021 [M] | High | Code selects; G4 |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Bounded rationality and satisficing | | not started |
| Ecological rationality, adaptive toolbox | [`subfields/02_ecological_rationality_adaptive_toolbox/DEEP.md`](subfields/02_ecological_rationality_adaptive_toolbox/DEEP.md) | done, batch 5 (2026-10-27) |
| Heuristics and biases | | not started |
| Prospect theory | | not started |
| Choice architecture and nudging | | not started |
| Nudge evidence | | not started |
| Behavioural finance and game theory | | not started |
| Debiasing | | not started |
| Resource-rational analysis | | not started |
| Noise and judgement | | not started |

## Dig into next

1. **Ecological rationality.** Questions: Which environment features (few cues, redundancy, scarce data) make simple rules win? Can S0 choose direct, short or checked mode from class features? Evidence needed: Gigerenzer's comparisons with conditions (not opened beyond a summary), and our per-mode pass rates.
2. **Resource-rational analysis.** Questions: Is there a computable value-of-more-thinking rule that reproduces G11 and G12? Evidence needed: Lieder and Griffiths; our curves of plain versus extended thinking.
3. **Choice architecture on LLMs.** Questions: Which framing, order and default effects hit LLMs? Does S1 masking remove them? Given the nudge dispute, the human effect size is itself uncertain: report the Mertens estimate and the Maier correction together, and test directly. Evidence needed: LLM bias studies and a masking pilot.

## Does not transfer

Markets, consumer saving, public policy nudges, loss aversion and social preferences are about human motives and populations. Critics note reliance on WEIRD samples and no unified alternative theory. Human biases do not automatically appear in LLMs, and LLMs have their own. A Wall Street Journal claim that under half of nudge experiments kept their effect on long-term retest appears on a Wikipedia page and I did not verify it.

## Sources

[V] means opened this session with WebFetch. [M] means memory or search snippet only. The PNAS pages returned 403, so the Mertens figures come from the Europe PMC record, and Maier's from its title and from Wikipedia's description.

1. [V] Europe PMC record, Mertens et al., PMC8740589: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1073/pnas.2107346118&format=json&resultType=core
2. [V] Europe PMC record, Maier et al., PMC9351501 (no abstract returned): https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1073/pnas.2200300119&format=json&resultType=core
3. [V] Wikipedia, Nudge theory: https://en.wikipedia.org/wiki/Nudge_theory
4. [V] Wikipedia, Behavioral economics: https://en.wikipedia.org/wiki/Behavioral_economics
5. [V] Wikipedia, Bounded rationality: https://en.wikipedia.org/wiki/Bounded_rationality
6. [M] Simon (1955), A behavioral model of rational choice, QJE.
7. [M] Lieder and Griffiths (2020), Resource-rational analysis, BBS.

Opened sources: 5.
