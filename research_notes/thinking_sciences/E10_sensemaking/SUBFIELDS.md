# Sensemaking: subfields

Sensemaking is the study of how people turn confusing or surprising situations into an account they can act on. It splits into a cognitive branch (Klein's data-frame theory, from naturalistic decision making), an organisational branch (Weick and followers), an applied branch (intelligence analysis, defence, patient safety) and a newer branch on manipulation of sensemaking. The cognitive branch fits a single agent best. The opened pages show that support for it is case-based: Weick's seven properties have no quantitative test on the page I read, and a reviewer cited in my searches (Pontis and Blandford, 2016) says the data-frame theory has not been tested across many tasks (snippet only, [M]).

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Data-frame theory | Sensemaking is "fitting data into a frame and fitting a frame around the data"; frames are stories, maps, scripts or plans | Klein, Moon, Hoffman 2006; Klein et al. 2007 [V] | High | State (understand, represent); impasse trigger |
| Frame activities (elaborate, question, compare, preserve, reframe, seek) | What people do with a frame when data do not fit | Klein et al. 2007 (list seen only in a search snippet, [M]) | High | Operator (reframe the goal); revise |
| Anomaly handling and fixation | When a frame is kept despite contrary data, and what breaks it; surprise as trigger | Klein cases [M]; Feltovich [M] | High | Guardrail G2; impasse detector |
| Weick's organisational sensemaking | Seven properties: identity, retrospect, enactment, social, ongoing, cues, plausibility; "plausibility over accuracy" | Weick 1995; Mann Gulch, Bhopal re-analyses [V] | Low | Background only |
| Reviews that map the field | About a dozen categories and related ideas such as sensegiving and sensebreaking; five ways sensemaking is studied (episodes, triggers, processes, outcomes, situational influences) | Maitlis and Christianson 2014; Sandberg and Tsoukas 2015 [V via Wikipedia] | Low | Background only |
| Sensemaking in defence and safety | Shared sensemaking in networked forces (a hypothesis, not tested on the page); detecting high-risk patient situations | Garstka and Alberts 2004; Battles et al. 2006 [V via Wikipedia] | Low | Background only |
| Analyst sensemaking | Foraging loop and sense loop | Pirolli and Card 2005 [M] | Med | State (represent); memory |
| Manipulated sensemaking | Disinformation builds "deep stories" that set the frames used on later events; people prefer plausible to accurate accounts | Prochaska et al. 2024 [V]; qualitative, human rumours only | Med | Guardrail (S1 input hygiene) |

## Dig into next

1. **Data-frame theory and frame activities.** Questions: Can the activities be written as program-checked moves around one stored frame (the current rule in plain words)? Which activity fires on a failed check, and none on a schedule (G1)? Does "preserve" (explaining anomalies away) predict our wrong answers? Evidence needed: the 2007 paper itself (I opened only a one-paragraph summary page), coded outcomes from Klein's cases, and our logs of runs where a rule fit the examples but failed a held-out one.
2. **Anomaly handling and fixation.** Questions: What computable signal marks an anomaly (failed unfitted check, disagreement)? Do experts tolerate a count of anomalies before reframing, and does a threshold beat judgement? Evidence needed: studies that timed reframing, then a replay on our logs.
3. **Manipulated sensemaking.** Question: Does the "deep story" effect, shown only in humans, appear in LLMs, and does S1 masking reduce it? Evidence needed: an equal-token test of masked versus unmasked prompts.

## Does not transfer

Weick's work concerns organisations: shared identity, talk, and stories told after a crisis. A single agent has none of these. The team and defence branches rest on people negotiating meaning. Klein's claim that experts reframe well comes from interviews, not controlled trials.

## Sources

[V] means the page was opened this session with WebFetch. [M] means memory or a search snippet only. The web-search budget ran out, so no extra searches were possible in the second pass.

1. [V] Gary Klein, Data-Frame page (thin; no activities listed): https://www.gary-klein.com/data-frame
2. [V] Wikipedia, Sensemaking: https://en.wikipedia.org/wiki/Sensemaking
3. [V] Prochaska et al., Misleading Ourselves (abstract page): https://arxiv.org/abs/2410.14858
4. [V] Wikipedia, Naturalistic decision-making: https://en.wikipedia.org/wiki/Naturalistic_decision-making
5. [M] Klein, Moon, Hoffman (2006), Making sense of sensemaking, IEEE Intelligent Systems.
6. [M] Klein, Phillips, Rall, Peluso (2007), A data-frame theory of sensemaking.
7. [M] Pirolli and Card (2005), The sensemaking process and leverage points for analyst technology.
8. [M] Pontis and Blandford (2016), as reported in a search snippet; not opened.

Opened sources: 4.
