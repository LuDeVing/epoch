# Military planning and red teaming: subfields

This field covers how armed forces plan operations and test plans. It divides into planning doctrine (course-of-action development and analysis), wargaming, red teaming and alternative analysis, recognition-primed command decision research, and machine wargaming. The practices are widely taught. The opened sources agree that systematic evidence is missing. A War on the Rocks author who served on the CENTCOM Red Team calls for empirical assessment of which approaches work, which implies it does not exist. The Wikipedia pages on red teams and wargames give only anecdotes. I could not search for controlled studies in this second pass because the search budget ran out, so "no controlled study found" means "none in the opened sources", not "none exist".

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Course-of-action development and analysis | Several distinct plans, each tested against enemy moves | US Army doctrine, JP 5-0 (named in article) [V] | High | State (generate, test); selection |
| Wargaming | Tests a plan against adversary actions to expose weak execution; types by level (tactical, operational, strategic) and format | Kriegsspiel; US Naval War College 1894 [V] | High | State (test); operator (work backwards) |
| Red teaming as alternative analysis | Challenges the logic and assumptions of a plan; "internal audit of thinking" | UFMCS (2004); Army ADSO 2004; Ipcha Mistabra after 1973 [V] | Med | Guardrail design; verify |
| Technical and physical red teams | Cyber and physical break-in tests; blue, purple and white team roles | TSA test: weapons passed 67 of 70 times [V] | Low | Background only |
| Premortem and prospective hindsight | Assume failure, then explain it | Mitchell, Russo, Pennington 1989; Klein 2007 [V via Wikipedia]; page cites no outcome evidence | Med | Verify; impasse trigger |
| Recognition-primed decision making | Take first workable option, check by mental simulation; three variants; needs expertise | Klein, Sources of Power 1998 [V via Wikipedia] | High | Generate-test; keep-first mode |
| Automated wargaming | Simulated evaluation of plans | Cranfield and AIAA studies (search results only, [M]) | Med | Test by running |
| Red-team failure modes | Organisations use red teaming "for optics"; findings not taken up | Data & Society 2024, cited in War on the Rocks [V] | Low | Background only |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Course-of-action development and analysis | | not started |
| Wargaming | [`subfields/02_wargaming/DEEP.md`](subfields/02_wargaming/DEEP.md) | done, batch 5 (2026-10-27) |
| Red teaming as alternative analysis | | not started |
| Technical and physical red teams | | not started |
| Premortem and prospective hindsight | | not started |
| Recognition-primed decision making | | not started |
| Automated wargaming | | not started |
| Red-team failure modes | | not started |

## Dig into next

1. **Course-of-action analysis.** Questions: Does the doctrine rule "several distinct, feasible options tested against the opponent" match S3 history plus S4 testing? What criteria and weights are used, and does a coded scorecard beat a vote? Evidence needed: the doctrine manuals (not opened), and any study comparing single-option with multi-option planning (RPD suggests one workable option often suffices).
2. **Wargaming as test by simulation.** Questions: Can "action, reaction, counteraction" be a code-run test, with a second call as opponent and code scoring the result? Does same-model-on-both-sides break independence (G4)? Evidence needed: a small pilot; the Wikipedia page notes validation is hard because scenarios are hypothetical.
3. **Premortem.** Question: Does assuming failure find real faults, unlike the unstructured self-doubt SCHEMA 4b rejects? Evidence needed: Mitchell et al. 1989 [M], and a test where code, not the model, supplies the failure scenario.

## Does not transfer

Command hierarchies, staff politics, deterrence and cultural empathy training are about people and organisations. Red-team value rests on a different mind; one model on both sides is not independent. Doctrine is accepted by culture, not by outcome data. Prussia's 1870 victory is a correlation people credited to wargaming.

## Sources

[V] means opened this session with WebFetch. [M] means memory or search snippet only.

1. [V] War on the Rocks, who stress-tests US war plans: https://warontherocks.com/who-stress-tests-u-s-war-plans/
2. [V] Wikipedia, Red team: https://en.wikipedia.org/wiki/Red_team
3. [V] Wikipedia, Wargame: https://en.wikipedia.org/wiki/Wargame
4. [V] Wikipedia, Pre-mortem: https://en.wikipedia.org/wiki/Pre-mortem
5. [V] Wikipedia, Recognition primed decision (via NDM and RPD pages): https://en.wikipedia.org/wiki/Recognition_primed_decision
6. [M] Intelligent wargaming approach (Cranfield): https://dspace.lib.cranfield.ac.uk/handle/1826/19164
7. [M] Klein (1998), Sources of Power.

Opened sources: 5.
