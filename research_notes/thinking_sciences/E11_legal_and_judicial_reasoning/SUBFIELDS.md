# Legal and judicial reasoning: subfields

Legal reasoning is the study of how lawyers, judges and jurors reach decisions from contested facts and rules. It divides into the psychology of fact-finding (the story model), case-based and rule-based reasoning (law and artificial intelligence), legal theory of precedent and analogy, and empirical work on judges' biases and noise. For one agent the useful parts treat deciding as choosing the best explanation, and arguing as testing a claim against nearest cases. My second pass had trouble reaching sources: two PDFs were unreadable, one encyclopedia page was missing, and the search budget was gone. Rows on judicial bias therefore stay unverified.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Story model of juror decisions | Three stages: build a story from incomplete evidence, learn the verdict categories, fit the story to a category. Accepted stories have the most coverage of the evidence | Pennington and Hastie 1986, 1992 [V via OpenLearn] | High | Selection; state (represent) |
| Other acceptance principles | Coherence and uniqueness as further certainty principles | Pennington and Hastie [M]; only coverage confirmed in an opened page | Med | Selection by code |
| Critiques of the story model | Thin on deliberation (a jury can flip from 11-1 to 12-0); assumes a formal process; unclear why story form matters | OpenLearn page [V] | Med | Caution on scoring |
| Computational coherence models | Network models reaching human-like verdicts | Thagard's ECHO (search snippet only, [M]) | Med | Selection by code |
| Case-based reasoning in law | Cycle: retrieve similar cases, reuse, revise, retain; lawyers and judges reason from precedent; legal CBR is closer to rules plus judgement | General CBR [V]; HYPO and CATO by Ashley [M] | High | Operator (map an analogue); memory |
| Argumentation and defeasible rules | Rules with exceptions, burdens of proof, attack and defence | Prakken, Sartor, Toulmin [M] | Med | State (test) |
| Analogy and precedent in legal theory | What makes a past case "like" this one | Sunstein, Levi [M] | Med | Operator |
| Judicial bias and noise | Order, fatigue, anchoring, sentence variance | Danziger et al. 2011 (disputed); Kahneman, Sibony, Sunstein 2021 [M] | Med | Guardrail; background |
| Evidence and probability reasoning | Bayesian reading of evidence, prosecutor's fallacy | Fenton and Neil [M] | Med | Verify |

## Dig into next

1. **Story model and coverage selection.** Questions: Can candidate rules be scored in code on coverage (share of observations explained), then coherence and uniqueness? Does coverage as a tiebreaker beat a vote in S7? What do the critiques imply, namely that scoring should be on the whole story, not item by item? Evidence needed: the 1992 experiments (my attempt to read a Hastie and Pennington PDF failed), and a test in our logs.
2. **Case-based reasoning.** Questions: Does the retrieve, reuse, revise, retain cycle describe the subgoal library (memory) and S5? How does HYPO rank nearest cases and make counter-cases? Evidence needed: Ashley's work, and any measured benefit of retrieved cases for LLMs.
3. **Judicial noise.** Question: Which order effects replicate, and do they predict context-order effects in LLMs? Evidence needed: replications and critiques.

## Does not transfer

Jury deliberation, group pressure, persuasion, legitimacy and burden of proof are social and institutional. The story model describes what lay people do, not what is best. Precedent binds by authority, not by evidence. Judge fatigue findings concern bodies.

## Sources

[V] means opened this session with WebFetch. [M] means memory or search snippet only. No extra searches were possible (budget exhausted).

1. [V] OpenLearn, Jury decision making, what's the story: https://www.open.edu/openlearn/society-politics-law/law/jury-decision-making-whats-the-story
2. [V] Wikipedia, Case-based reasoning: https://en.wikipedia.org/wiki/Case-based_reasoning
3. [M] Hastie and Pennington, Colorado Law Review PDF (fetched, unreadable scan): https://lawreview.colorado.edu/wp-content/uploads/2026/02/Hastie-Pennington.pdf
4. [M] Pennington and Hastie (1992), Explaining the evidence, JPSP.
5. [M] Ashley (1990), Modeling Legal Argument (HYPO).
6. [M] Kahneman, Sibony, Sunstein (2021), Noise.

Opened sources: 2.
