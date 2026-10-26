# Intelligence analysis: subfields

Intelligence analysis is judgment from partial, conflicting evidence. Research splits into taught techniques (ACH, structured analytic techniques), tests of whether they work, studies of bias, probability language, and the forecasting tradition (see E03). Single answers with later checks are rare, but the controlled tests of ACH are useful because they show what fails. Opened results: with 50 intelligence analysts, ACH-trained analysts skipped steps, the bias evidence was mixed, and ACH may have increased inconsistency and error (Dhami, Belton, Mandel 2019). With 227 participants, ACH gave no coherence benefit over a control and was slightly less reliable (mean absolute deviation .22 against .18, d = 0.20, p = .051; Karvetski and Mandel 2020).

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Analysis of competing hypotheses (ACH) | Matrix of hypotheses against evidence | Heuer 1999; Dhami 2019; Karvetski and Mandel 2020 | Med | Evidence of no gain; supports "not to add" (schema 4b) |
| Diagnosticity of evidence | Which evidence separates hypotheses | Heuer, ch. 8 (not read) | High | S7 discriminating test |
| Structured analytic techniques (SATs) | Assumption checks, devil's advocacy, brainstorming | Heuer and Pherson; Coulthart | Low | Background; G9 |
| Systematic review of SAT evidence | Pooled findings from over 2,000 studies | Coulthart dissertation | Med | Reported: ACH, brainstorming, devil's advocacy have moderate to strong support; weighing evidence matters more than seeking disconfirming evidence; conflict improves quality |
| Layout and presentation | Rows against columns | Dhami et al. 2024 | Med | S4 presentation by code (abstract only) |
| Red teaming | Dedicated challenger | UK Red Team Handbook | Low | G9 warns against debate |
| Cognitive bias in analysis | Confirmation, anchoring | Heuer; Kahneman and Tversky | Low | Background |
| Probability language | Words of estimative probability | Kent 1964; Mandel | Low | Output format |
| Forecast accuracy of analysts | Measured accuracy and aggregation | Mandel and Barnes 2014 | High | Link to E03 |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Analysis of competing hypotheses (ACH) | | not started |
| Diagnosticity of evidence | [`subfields/02_diagnosticity_of_evidence/DEEP.md`](subfields/02_diagnosticity_of_evidence/DEEP.md) | done, batch 5 (2026-10-27) |
| Structured analytic techniques (SATs) | | not started |
| Systematic review of SAT evidence | | not started |
| Layout and presentation | | not started |
| Red teaming | | not started |
| Cognitive bias in analysis | | not started |
| Probability language | | not started |
| Forecast accuracy of analysts | | not started |

## Dig into next

**1. Diagnosticity.**
- Can code compute, for each pair of candidates, the input where they differ most, and does that beat the model's pick of test?
- Karvetski and Mandel measured pseudo-diagnostic weighting: non-diagnostic evidence had about 30 to 32 percent of the impact of fully diagnostic evidence. Do LLMs do the same?
- Evidence: Heuer ch. 8, a small LLM test on rule-discovery tasks.

**2. Why ACH fails, and the Coulthart contradiction.**
- Two controlled studies show no gain or harm; a review (abstract only) reports moderate to strong support. Which studies drive the review, and are they controlled?
- Is the cost extra judgment steps (noise, G1) or step order?
- Evidence: read Coulthart's full text, Dhami 2019 protocols.

**3. Weighing evidence against hunting for disconfirmation.**
- Coulthart's review says weighing matters more. Can the program weigh by computing, with the model only scoring each item once, blind?
- Evidence: Coulthart's 21-student experiment, an LLM test at equal tokens.

## Does not transfer

Secrecy, source handling, agency review, politics, and adversary deception are institutional or social. Many questions never resolve, so training effects are only measured in aggregate. Group red teams are about social dissent. Participants in the 227-person study were general-public graduates, not analysts.

## Sources

[V] = opened and read this session. [M] = search result only, or from memory. Two further searches were refused (search budget exhausted). Opened: 4.

1. Dhami et al. 2019, ACH with intelligence analysts (abstract page). https://strathprints.strath.ac.uk/69049/ [V]
2. Karvetski and Mandel 2020, JDM 15(6):939-958. https://dlab.sauder.ubc.ca/sjdm/journal/20/200430/jdm200430.html [V]
3. Coulthart, systematic review (abstract page). https://d-scholarship.pitt.edu/26055/ [V]
4. Heuer, Psychology of Intelligence Analysis, CIA page (preface only; ACH chapter in the linked PDF not read). https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/ [V]
5. Dhami et al. 2024, layout study. https://cognitiveresearchjournal.springeropen.com/counter/pdf/10.1186/s41235-024-00560-y.pdf [M] (redirect to login; not read)
6. Liverpool repository study on flexible technique. https://livrepository.liverpool.ac.uk/id/eprint/3107974 [M]
7. Mandel and Barnes 2014, PNAS. [M]
