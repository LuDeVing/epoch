# Cognitive systems engineering: subfields

Cognitive systems engineering (CSE) was set up in the early 1980s by Hollnagel and Woods. Its unit of study is the joint cognitive system, people and tools working as one. Macrocognition is the companion programme: cognition adapting to complexity in real work, studied by task analysis, field methods and experiments, in the aim of understanding "work-as-done" rather than "work-as-prescribed". The field divides into anomaly response, coordination, cognitive artifacts, human error and safety, resilience engineering, and naturalistic decision making. Evidence is mostly case studies and incident analysis. The opened pages cite no quantitative outcome studies for resilience engineering.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Joint cognitive systems | People plus tools as one system | Hollnagel and Woods [V] | Med | Background; split of program and model roles |
| Anomaly response (dynamic fault management) | How operators handle faults in supervised processes under time pressure and uncertainty | Woods, Roth [V via Wikipedia] | High | Impasse detector; revise |
| Coordination and common ground | Shared understanding between agents, including software as team member | Klein, Woods, Bradshaw et al. [M] | Low | Background only |
| Cognitive artifacts | How tools and interfaces support or hinder thought | Hutchins, Norman [V names; works M] | Med | Interface between code and model |
| Macrocognition | Decision making, sensemaking, planning, coordination in real settings; mixed naturalistic and experimental methods | Klein et al.; editorial of a Frontiers topic [V] | Med | Background |
| Naturalistic decision making | Experts under pressure; RPD | Klein; first conference 1989 [V] | Med | Mode choice; generate-test |
| Human error and recovery | Why errors occur and how they are caught | Reason, Hollnagel CREAM [M] | High | Guardrail G2; revise |
| Resilience engineering | Four potentials: respond, monitor, learn, anticipate; Woods's failure patterns: decompensation, working at cross purposes, stuck in outdated behaviour | Hollnagel, Woods, Cook, Dekker; first symposium 2004 [V] | Med | Look back; impasse patterns |
| Work and domain analysis | Mapping goals, constraints, decisions of a job | Rasmussen, Vicente [M] | Med | S0 problem-class gate |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Joint cognitive systems | | not started |
| Anomaly response (dynamic fault management) | [`subfields/02_anomaly_response_dynamic_fault_management/DEEP.md`](subfields/02_anomaly_response_dynamic_fault_management/DEEP.md) | done, batch 5 (2026-10-27) |
| Coordination and common ground | | not started |
| Cognitive artifacts | | not started |
| Macrocognition | | not started |
| Naturalistic decision making | | not started |
| Human error and recovery | | not started |
| Resilience engineering | | not started |
| Work and domain analysis | | not started |

## Dig into next

1. **Anomaly response and failure patterns.** Questions: Do Woods's three failure patterns (decompensation, cross purposes, stuck in outdated behaviour) have counterparts in an LLM loop (budget spent without change, sub-attempts undoing each other, repeating a dead rule)? Can each be detected by code and mapped to an impasse operator? Evidence needed: Woods's papers (not opened), and a classification of our failed runs.
2. **Error detection and recovery.** Questions: Which cues let experts catch errors, and which are computable? Does recovery work better when the error is shown than when sought (G2)? Evidence needed: Reason and Woods studies; our logs of detected versus missed errors.
3. **Work analysis for S0.** Question: Can a short class analysis (goals, constraints, common traps) be built once and stored? Evidence needed: examples, then a test that a class record helps.

## Does not transfer

Much of CSE concerns teams, control rooms, interface design and trust in automation. Resilience engineering is about organisational safety. In the macrocognition editorial the results were about teams, for example that teams generally outperformed individuals, which does not carry to one agent. The framework names functions and does not give a procedure.

## Sources

[V] means opened this session with WebFetch. [M] means memory or search snippet only.

1. [V] Wikipedia, Cognitive systems engineering: https://en.wikipedia.org/wiki/Cognitive_systems_engineering
2. [V] Macrocognition editorial (PMC5398123): https://pmc.ncbi.nlm.nih.gov/articles/PMC5398123/
3. [V] Wikipedia, Resilience engineering: https://en.wikipedia.org/wiki/Resilience_engineering
4. [V] Wikipedia, Naturalistic decision-making: https://en.wikipedia.org/wiki/Naturalistic_decision-making
5. [M] Hollnagel and Woods (2005), Joint Cognitive Systems.
6. [M] Reason (1990), Human Error.

Opened sources: 4.
