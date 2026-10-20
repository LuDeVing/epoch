# Troubleshooting and fault diagnosis: subfields

This field studies how technicians and engineers find the fault in a system that fails: electronics, machines, software, plants. It divides into cognitive models of troubleshooting, expert-novice studies, search strategies (half-split, cost-weighted tests), model-based diagnosis in AI, training systems, and industrial fault detection. The task has one answer (the faulty part) and a real check (repair works). Honest status: I did not open a primary study of half-split or hypothesis-limit strategy. The Jonassen review failed to load and two PDFs were unreadable or a login page. What I did open is a 2026 NSF-funded interview and think-aloud study, and an LLM circuit-debugging study.

Opened facts. The ASEE paper (Sabuncu et al.) summarises troubleshooting as a search from symptoms through components, where hypotheses about causes are generated and tested until the root cause is found, alternating divergent and convergent work, seldom linear, with the same structure in maintenance, circuit and software debugging, and clinical diagnosis. It interviewed 18 engineers with over 10 years of experience, coded think-aloud protocols (two cases compared: an expert sought system understanding first, a PhD student only as needed for root-cause search), and proposes five "manifolds" (system dynamics, epistemic, normative, divergence, situational). Preliminary only, no statistics. The circuit-debugging study (Hu and Ash, 2026) found LLMs gave sensible suggestions but struggled with images and sounded overconfident.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Cognitive models of troubleshooting | Problem description, causes, test, validate | Jonassen and Hung 2006; Schaafstal 1993 | High | Maps to S1 to S4 (opened source supports the cycle) |
| Expert-novice differences | Experience and schemas | Gott; Rasmussen | High | Memory; S0 |
| Hypothesis limits | Few hypotheses held, overconfidence | Gettys; Mehle (from memory); 1980 dissertation in a search snippet | High | S3 many independent attempts; code holds list (not verified by me) |
| Search strategies | Half-split, symptom matching | Rasmussen and Jensen 1974 | High | S7 discriminating test (not opened) |
| Surface-cue heuristics | Fast symptom matching and its failures | Rasmussen skill-rule-knowledge | Med | Input hygiene S1 |
| Model-based diagnosis | Reason from a system model | Reiter 1987; de Kleer and Williams 1987 | High | Code-run reasoner |
| Training and tutors | Simulators, case libraries | Jonassen; Lesgold | Med | Case library as memory |
| Complexity of expert troubleshooting | Interview models | Sabuncu et al. (ASEE) | Med | Operators, triggers |
| LLM help in hardware debugging | Chat with LLMs | Hu and Ash 2026 | Med | Overconfidence matches G10 |
| Industrial fault detection | Statistical detection | Isermann | Low | Background |

## Dig into next

**1. Search strategy: half-split and cost-weighted tests.**
- Which ordering lowers expected number of checks, and do people follow it?
- Can code keep the candidate list and choose the next test that splits it, with the model only writing the test?
- Evidence needed: Rasmussen and Jensen protocols, de Kleer and Williams, an LLM test with known faults. None opened yet.

**2. Hypothesis limits.**
- Is a few hypotheses per problem true of experts, and do LLMs narrow to one cause?
- Evidence: link to the E09 hypothesis study (about two hypotheses per defect), Mehle.

**3. Experts' system-model first versus root-cause-first.**
- The two ASEE cases differ in whether they model the system before searching; which suits which problem class?
- Evidence: larger think-aloud sets than two cases.

## Does not transfer

Hands-on skills, dials, safety procedures, parts access and plant downtime are physical. Manuals differ by trade. Hardware faults are noisy and intermittent. Studies are small and mostly interviews. The ASEE paper's "stakeholder" and "normative" manifolds are organisational.

## Sources

[V] = opened and read this session. [M] = search result only, or from memory. Two further searches were refused (budget exhausted). Opened: 2.

1. Sabuncu et al., BSCER capacity building for a troubleshooting learning environment (ASEE, PDF text read). https://peer.asee.org/bscer-capacity-building-for-developing-a-troubleshooting-learning-environment.pdf [V]
2. Hu and Ash 2026, Chat Debugging (arXiv abstract). https://arxiv.org/abs/2608.02955 [V]
3. Jonassen and Hung 2006, Learning to troubleshoot (redirect, not opened). https://dx.doi.org/10.1007/s10648-006-9001-8 [M]
4. Journal of Agricultural Education link (opened, was a login page). https://jae-online.org/index.php/jae/article/download/786/631/1077 [M]
5. Reiter 1987; de Kleer and Williams 1987, Artificial Intelligence. [M]
6. Rasmussen and Jensen 1974, Ergonomics. [M]
