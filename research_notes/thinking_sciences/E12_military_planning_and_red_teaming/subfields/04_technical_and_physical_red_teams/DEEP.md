# Technical and physical red teams: deep document

*Subfield E12.04. Evidence: evidence_a to evidence_d.jsonl (ids a01-a25, b01-b26, c01-c27, d01-d20), claims.jsonl (E12.04-K01 to K22), critique.md. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

A technical or physical red team is a group that attacks a system on purpose, with permission, to show where the defence fails. The system can be a building, an airport checkpoint, a border crossing, a computer network, a web app or an AI model.

The roles are fixed by convention (b02, a06):
- **Red team**: the attackers. Covert tests add physical entry and surprise.
- **Blue team**: the defenders. In a covert test they are not told.
- **White team**: sets the rules of engagement, scope and stop conditions, and referees.
- **Purple team**: a temporary red plus blue mix that gives fast feedback so fixes happen during the test.
- **Overt (white hat) vs covert (black hat) testing** (NIST SP 800-115, a06): in overt testing staff know and help, which teaches them. In covert testing only upper management knows, which tests the response.

Standard process (a05): planning, discovery, attack, reporting. The attack phase loops back to discovery, because each new foothold exposes new targets. A rules-of-engagement template is in Appendix B of the NIST guide.

Why this is background for our agent: the red-team idea is "attack your own plan before the world does". Our schema already has checks (G2, G3), a verifier (S8) and a rule against debate (G9). This subfield tells us (a) how to read a test result honestly, (b) what a pentest agent does on long multi-step work, which is close to what our agent does on long tasks, and (c) whether a separate adversary role helps an LLM. Short answer to (c): no evidence yet that it beats majority vote at equal tokens (K18).

## 2. History and theories in depth

**Physical red teams.**
- The FAA began covert airport tests after Pan Am 103 (1988), paused them after 2001 and resumed in 2003 under TSA. About 100 US airports a year are tested (b02, Wikipedia, not a primary source).
- The US Army created a red team office in 2004. The Marines staffed red team posts in June 2013. Three red teams reviewed the bin Laden intelligence in 2011 (b02).
- The Defense Science Board (2003) treated red teams as a way to challenge organisational norms. Secondary summaries list failure modes: unserious tasking, lost independence, no link to decisions. The report itself was not opened and has no numbers (a07).
- **TSA 2015 test (a01, b01).** DHS Inspector General covert testers got mock explosives or banned weapons through checkpoints in 67 of 70 trials (95.7%; the press rounds to 95 or 96%). The tests ran at dozens of busy airports, none named. In one trial a magnetometer alarm fired but a fake bomb taped to the back was missed in the pat-down. TSA said the test covered 1 of its 20 security layers. The report was classified; numbers come from briefed officials. TSA had spent $540M on screening equipment and $11M on training since 2009 "without noticeable gain" (b01). Fallout: the acting TSA head was reassigned, and retraining, equipment retest and more random covert tests were ordered (a02, snippet only).
- **Tester skill matters.** The Inspector General said the testers were OIG auditors without special background (a02, snippet only, unverified). If so, weak attackers beat the defence, which says more about the defence than a team of experts would.
- **GAO radioactive-source test, 2006 (a03, a04).** Undercover GAO teams bought radioactive sources by phone from a supplier using a fake company, forged NRC papers with off-the-shelf software and crossed two land borders at the same time (US-Canada, US-Mexico; work Jul-Dec 2005). Portal monitors alarmed at both crossings. Both teams still got through. Each carried enough material for a dirty bomb. No CBP inspector questioned the counterfeit bill of lading or NRC licence. Corrective briefings followed within weeks (CBP 21 Dec 2005; NRC 12 and 24 Jan 2006). The alarm fired, the human process failed. Lesson: a detector without a following check is one layer, not two.
- **Real intrusion, not a test.** Y-12, 28 July 2012 (d20): three activists cut fences, disabled sensors and reached a highly enriched uranium site. DOE OIG found insufficient defences and "troubling displays of ineptitude". Convicted of sabotage 9 May 2013.
- **Follow-up data.** DHS OIG 2017 retest report (OIG-17-112, d19) publishes no pass/fail counts (classified or SSI) and makes 8 recommendations. A press figure of about 80% failure for a 2017 round is recalled but unverified (b22). GAO 2007-08 airport tests are recalled, not verified (b21). No source shows a before/after improvement (K02, K22).

**Cyber red teams, human era.**
- NIST SP 800-115 (2008): covert testing does not test every control or find every vulnerability and is often time-consuming and costly (a06). A test shows what was tried, not what is safe.
- Microsoft AI Red Team (a20, a21), over 100 generative-AI products: eight lessons. Simple attacks work; you do not need gradients to break an AI system; red teaming is not safety benchmarking; automation (PyRIT) extends coverage but humans prioritise risk, design system-level attacks and define new harms; the work is never complete.
- Perez et al. 2022 (a22, c21): one LM writes test cases for a target 280B chatbot. 0.5M zero-shot cases gave 3.7% offensive replies (18,444 failures). Few-shot, supervised and RL red LMs raised yield. RL had the highest hit rate but the lowest diversity.
- Ganguli et al. 2022 (a23): human red teamers on 2.7B, 13B and 52B models of four types released 38,961 attacks. RLHF models got harder to attack with scale. Plain LM, prompted LM and rejection sampling stayed flat. Rejection sampling was hardest at every size, often by being evasive. The helpful-honest-harmless prompt was not significantly harder than plain.
- CyberSecEval (a24): seven Llama 2 / Code Llama models wrote vulnerable code in 30% of cases and complied with 53% of cyberattack-help requests; better coders complied more.

**Theory in one line.** A red-team result is a count of misses on a chosen attack set at a chosen layer. It is a lower bound on weakness and says nothing about untested attack classes (K01, K03).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Physical covert test misses | TSA 67 of 70 (95.7%), 1 of 20 layers tested; GAO 2 of 2 border crossings passed despite alarms | a01, b01, a03, a04 | [E] as press/GAO record; unreplicated |
| Red findings did not visibly improve defence | $540M equipment, $11M training since 2009; 2017 OIG publishes no counts; no controlled trial found | b01, d19, b20 | [S] |
| Plain LLM, end-to-end pentest | GPT-4 5/13 targets (38.46%), Bard 2/13, GPT-3.5 1/13; sub-tasks 95/182 (52.20%), 50, 42; hard 0/2 | a08, a09 | [S] |
| Failure causes, plain LLM | context lost 74, deadlock 45, code misread 37 | a09, b03 | [S] |
| Task-tree scaffold | PentestGPT +228.6% vs GPT-3.5, +58.6% vs GPT-4 on sub-tasks | a10, b03 | [S] |
| One-day exploits, with CVE text | GPT-4 87% (13/15) vs 7% (1/15) without; 0% GPT-3.5, open models, ZAP, Metasploit; $3.52/run; actions 24.3 vs 21.3 | a11, a12 | [E] |
| Web hacking, no flaw info | GPT-4 73.3% pass@5 (11/15), 42.7% overall; GPT-3.5 6.7%; open models 0% | c17 | [S] |
| Planner plus sub-agents, zero-day | HPTSA 42% pass@5, 18% pass@1 on 14 vulns; 4.3x pass@1 and 2.0x pass@5 vs GPT-4 with no description; within 1.8x of agent given description; ZAP and Metasploit 0% | a13, c18 | [E] with a note on baseline |
| HPTSA ablations | no task-specific agents 2.1x lower pass@1, 50% lower pass@5; no documents 2.1x and 20% lower; no hierarchy 13x and 6x lower; Llama refusals 31% | a25, critique | [S] |
| Multi-host networks | Incalmo 37/40 vs 3/40 prior (GPT-4o, Sonnet 4, Gemini 2.5 Pro); 12-54 min; at most $15; irrelevant commands 47-90% in baseline | a16, b15, b24 | [S] |
| CTF horizon limit | Cybench: nothing solved above 11 min human first-solve time; hardest 24h54m; unguided best 17.5%, guided up to 27.5% | a14, b08, c19, c20 | [E] |
| Scaffold effect is model dependent | pseudoterminal and web search helped Claude 3.5 Sonnet, hurt GPT-4o; model and guidance moved more than format | b09, c20 | [S] |
| Guided pipeline | Nakano: 71.8% (Llama-3-8B), 72.8% (Gemini-1.5), 78.6% (GPT-4) vs 13.5%, 16.5%, 75.7% self-guided; 86-206% more queries | b10 | [S] |
| Live human comparison | ARTEMIS: 8,000 hosts, 9 valid vulns, 82% valid rate, beat 9 of 10 humans; $18.21/h vs about $60/h; Claude Code and MAPTA refused, Incalmo stalled, Codex beat 2 humans, CyAgent lost to all | a17-a19, b06 | [S] n=10, one network |
| Plain strong agent baseline | Codex+GPT-5 67.3% on XBOW 104 (pass@1 70, pass@2 81) vs PentestGPT V2 published 76.9%; GPT-5.2 79.8%; GPT-5.5 92.3% | c13, c15, c16 | [C] vs V2 claim of 91% |
| Extra prompting hurts strong agent | default 70/70 vs detailed 64/58 vs whole-system 60/68; docs level chi-sq 1.36, p=0.71, N=180 | c14, c26 | [E] (two sources, small) |
| Scaffold gain shrinks with model | XBOW GPT-4o 27-39% spread, GPT-5 40-49%; memory/messaging +12 to +16 points on 26-52% baselines | d08, d09 | [S] |
| Benchmark choice dominates | XBOW 67-92% vs CVE-Bench up to 13% and CyberGym about 20% | d18, c16 | [E] as a warning |
| Failure mix | capability 42%, planning/state 58% (context forgetting 18, premature commitment 16, explore/exploit 12, chain failure 12) over 200 traces; loops with no stop rule 68%; context limits 50% of coverage gaps | d07, d09 | [S] |
| Offence vs defence unequal | BountyBench Patch 87.5-90%, Exploit 32.5-67.5%, Detect 0-12.5%; Detect CI includes 0 for 9 of 10 agents | d10, d11 | [S] |
| Refusals | 14.1% and 11.2% Codex CLI under strict system prompt; 0.37% custom; near 0 with bug-bounty framing | d12 | [S] |
| Decoys fool agents | Mantis: attacker success 9-10/10 without, 0-1/10 with hidden injection decoys; honeypot policy 3.66 vs 3.00 vs 2.33 real hosts at $5, no edge at $2 | d13, b16 | [E] two designs, some abstract-level |
| Human vs LLM phishing | 54% AI, 54% human expert, 56% AI plus human, 12% control (N=101); detector 97.25% of 363 | c22 | [S] |
| Human help | AutoPenBench autonomous 21% vs assisted 64% | d16 | [S] |
| Self-critique with no outside check | GPT-3.5 GSM8K 75.9 to 74.7; GPT-4 95.5 to 89.0; with oracle label 75.9 to 95.5 | d01 | [E] |
| Debate vs vote | GSM8K debate 83.2 (6 responses) vs self-consistency 85.3 (6) and 88.2 (9); MAD survey: no reliable edge | d02, d03 | [E] |
| Debate helps when judge lacks evidence | judge 76% (model) and 88% (human) vs 48% and 60% baseline | d04 | [S] |
| Defence metrics mislead | minimal defence: defence rate 1.000, attributed rate 0.000 | c24 | [S] |

## 4. Mechanisms and models

Each item is written so an engineer can build it.

**M1. Test result record (physical lesson).** Store every red-team result as a tuple: attack set id, layer tested, layers not tested, N trials, N misses, attacker skill, date. Print the tuple beside any rate. Do not print "robust" without the "not tried" list. TSA 67/70 with "1 of 20 layers" is the model case (K01, K03).

**M2. Layered defence with an independent second check.** GAO showed the detector alarmed and the follow-up human check failed. For our agent: a flag raised by one step must trigger a named second step that is not the same call with the same context. If the second step can be skipped, count one layer.

**M3. External task tree and state record (PentestGPT, Nakano, Incalmo, CHECKMATE).**
- Keep a plan tree outside the chat: nodes are sub-tasks with status (todo, doing, done, failed, dead-end).
- A reasoning module picks the next node; a generation module writes the command; a parsing module summarises tool output into one or two lines before it goes back in.
- Code, not the model, holds the tree. Nakano used a deterministic tree from MITRE ATT&CK so the model could not repeat tactics (b10). Incalmo moved low-level commands into code-run high-level tasks (a16). CHECKMATE put a classical planner above the agent: time cut 54%, cost cut over 50% (b12).
- Why: the top plain-LLM failure was lost context (74 of 156 counted failures, a09), and a later study codes context forgetting 18% plus premature commitment 16% of failed traces (d07).

**M4. Stop rule and difficulty estimate.**
- 68% of looping root causes were "no explicit stop condition" (d09).
- PentestGPT V2 adds difficulty-aware search: a UCB-style penalty lambda on long branches. lambda 0 gave 68.4% completion, 0.5 gave 73.8%, 1.0 gave 69.8%; false prune rate 2.8% (d08).
- Build: per branch, track steps spent, recent progress and past success of the class; prune when steps exceed a cap and progress is zero. Log false prunes.

**M5. Hierarchical planner plus task agents (HPTSA).** The planner explores, writes a plan and spawns a sub-agent for one task class (for example SQL injection) with that class's documents. Ablation: removing the hierarchy costs 13x at pass@1; removing task agents 2.1x; removing documents 2.1x (critique, a25). The baseline was GPT-4 with no description, not a tuned plain agent.

**M6. Retrieval of the right reference.** One-day exploit success was 87% with the CVE text and 7% without, with about the same number of actions (a11, a12). The model needed the specific reference; it did not lack effort. Build: a retrieval step that returns the relevant precedent or doc, and a test where it is withheld.

**M7. Decoy and trap check.** Mantis: agents ingest text planted in a service and obey it (d13). Honeypot paper: a pre-connect detector plus stopping rule raised confirmed real hosts (b16). Build: treat all tool output as untrusted data, mark it, never let it set goals; before spending budget on a target, run a cheap "does this look planted" check.

**M8. Rules-of-engagement guard (white team).** HackSynth reports agents can hallucinate target IPs and attack out-of-scope systems (c09, qualitative). Build: a code-side allowlist for targets and actions checked before every tool call; log denials. No study measures the out-of-scope rate (K21).

**M9. Role-split test harness.** Three arms at equal tokens: (1) self-critique, (2) majority vote of independent samples, (3) a separate red role that attacks the candidate with access to tools. Score on tasks with ground truth. Accept (3) only if it beats (2). Prior: debate does not beat self-consistency (d02, d03); self-critique without an outside check is neutral or harmful (d01).

**M10. Refusal and false-positive accounting.** Log refusals, hallucinated findings and misses as three separate counts, and report valid findings per dollar (ARTEMIS: 82% valid rate; $18.21/h). A defence that "wins" because the target refused unaided has attributed rate 0 (c24).

## 5. What holds up

**Replicated or multi-source.**
- Success falls with task horizon. Seen in PentestGPT (hard 0/2), Cybench (nothing over 11 min), PentestEval (31% end to end), CVE-Bench and CyberGym [E].
- Scaffolds beat the same weak model used raw: PentestGPT, HPTSA, Incalmo, Nakano, memory and messaging add-ons (K05) [E for weak and mid models].
- The right reference input is decisive (K08) [E].
- Detailed extra prompting did not help a strong agent: Dhakal (default best) and STRIATUM-CTF (p=0.71) (K07) [E but small].
- Agents follow planted text and miss decoys: Mantis and CAI hijack (K16) [E].
- Refusals and pass@k choices distort headlines (K15, K17) [E].
- Self-critique without an outside check does not help; debate does not reliably beat voting (K18) [E, general tasks, not red-team tasks].

**Failures and contradictions.**
- **Scaffold gain vs strong plain agent [C].** PentestGPT V2 reports 91% on XBOW against baselines of 27-49% (b14). A plain Codex+GPT-5 agent gets 67.3% and GPT-5.5 gets 92.3% (c13, c16). Either V2's baselines were weak or model version drives it. A matched test shows V2 ahead by 9.6 points at GPT-5 and 5.2 at GPT-5.2, and plain pass@2 exceeds V2 GPT-5.2 by 3.5 points (c15). Model version outweighs architecture.
- **Own-benchmark claims fall on rerun.** PentestAgent, VulnBot and AutoPT score 27-49% on XBOW in a third-party rerun, and fall behind plain Claude Code with Sonnet 4.5 in another (b19, b12).
- **ARTEMIS on Cybench.** ARTEMIS beat baseline GPT-5, but the authors call it sampling variance. Its benefit shows on long open-ended tasks only (b18).
- **Cybench GPT-4o number (15.0% vs 12.5%).** Different attempt counts. Read all Cybench rows as attempt-specific.
- **Detect is not real yet.** BountyBench Detect no-info CIs include zero for 9 of 10 agents (d11).
- **Physical:** no replication of the TSA figure and no measured defence gain after red-team findings.

**Moderators.**
- Model strength: scaffold spread narrows from 27-39% (GPT-4o) to 40-49% (GPT-5) (d08).
- Scaffold-model fit: pseudoterminal and web search helped Claude 3.5 Sonnet, hurt GPT-4o (c20).
- Information level: Detect < Exploit < Patch (d10).
- System prompt and task wording: refusals 14.1% under a strict prompt, near 0 with bug-bounty framing (d12).
- Temperature: flat 0-1, command errors rise above 1, environment damage above 1.6 (c08).
- Human in loop: 21% to 64% on AutoPenBench (d16); ARTEMIS did well on missed vulnerabilities only with detailed hints (b07).

**Interventions that worked:** external task tree (a10, b10); high-level task layer run by code (a16); planner above the agent (b12); global context memory (+12 to +16 points, d09); tool documentation for a weak scaffold (27% to 38%, d08); detector-guided honeypot policy at $5 (b16); execution-verified training data for small models (CTF-Dojo, +9.9 points for Qwen3-32B, c25).
**Did not work or null:** temperature above 1; prompt chaining (5% worse, 17% slower, c08); detailed prompt text for a strong agent; documentation level in STRIATUM; self-critique alone; debate at equal responses.

## 6. Language models

**Offence, plain models.** GPT-4 solved 38.46% of PentestGPT targets and 0 of 2 hard ones. Bard 15.38%, GPT-3.5 7.69%. Open models scored 0% on one-day and web exploitation in 2024 (a11, c17). In 2025 frontier models with off-the-shelf pentest tools managed 3/40 multi-host networks (b24).

**What changed it.**
- Scaffold: +228.6% and +58.6% sub-task (PentestGPT); 3/40 to 37/40 networks (Incalmo); 13.5-75.7% to 71.8-78.6% (Nakano).
- Model version: Codex scaffold GPT-5 67.3%, GPT-5.2 79.8%, GPT-5.5 92.3%, at $27.71, $50.49, $69.53 per run (c16). After 2025 model change dominates scaffold change.
- Reference input: 7% to 87% (a11).
- Human help: 21% to 64% (d16).
- Tuning red generators: yield up, diversity down (a22).

**Live comparison.** ARTEMIS beat 9 of 10 professionals on a real 8,000-host network at about $18/h. It struggled with GUI work and had more false positives. Humans found 3 to 13 valid findings, 49 unique in total. Claude Code and MAPTA refused; Incalmo stalled; CyAgent lost to all; Codex+GPT-5 beat 2 (a17-a19, b06). N=10 humans, one network, owner-run.

**Benchmarks disagree widely.** XBOW 67-92%, CVE-Bench up to 13%, CyberGym about 20%, PentestEval end-to-end 31%, Cybench unguided 17.5% with older models (d18, b13, a14). Never compare across benchmarks. One target is 6.7 to 7.7 points on a 13-15 target set; one Cybench task is 2.5 points.

**Failure mix.** Capability 42% and planning/state 58% (d07). Stronger models shrink capability failures; planning and state persist (b25). Another study: context-window limits cause 50% of coverage gaps; no stop rule in 68% of loops (d09).

**Offence vs defence vs detection.** Patch 87.5-90%, Exploit 32.5-67.5%, Detect 0-12.5% (d10). On a defender benchmark, Claude-3.7-sonnet scored 81.65 and 78.40 with thinking (c27), so extra thinking did not help there.

**Deception.** Agents obeyed planted text in decoys; attacker success fell from 9-10/10 to 0-1/10 (d13). Honeypots in the wild: 8,130,731 attempts over about 3 months, 8 potential AI agents (d14).

**Red-teaming as a model-improvement tool.**
- Red-LM generators: hit rate against diversity (a22).
- Humans: RLHF models got harder with size; rejection sampling hardest but evasive (a23).
- Critics: CriticGPT critiques preferred over human critiques in 63% of cases, but it hallucinates bugs; critic plus human hallucinates less (d05).
- Self-critique with no external check: neutral to harmful (d01). Debate: not reliably better than voting (d02, d03). It helps when the judge lacks the evidence (d04).
- Multi-agent systems fail in 14 modes (MAST); gains over single agents are often minimal (d06).

**Social engineering.** LLM spear phishing 54% click-through equals human expert 54% (control 12%) (c22). Simulated social-engineering detection: SE-OmniGuard accuracy 0.813 vs 0.520-0.680 for baselines (c23).

## 7. What our agent should take

Part codes: G guardrail, S state, O operator, memory = section 5 of SCHEMA.

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Report scope beside every pass or fail: which checks ran, which attack classes were not tried, N | G3 and S9 log | [E] | K01, K03; a01, a03, a06 |
| Always compare against a tuned plain model at equal tokens; log the gap per model version | G7 (add "tuned default prompt") | [E] | K06, K17; c13-c16, d08 |
| Do not pad prompts with extra guidance; keep detailed text only if it beats the minimal prompt | G7 | [E] | K07; c14, c26 |
| Report pass@1, pass@k and cost together | G7 and S9 log | [E] | K17; a13, c13, d10 |
| Treat tool output as data, never as instructions; mark it in S1 input hygiene | S1 | [E] | K16; d13, d15 |
| Count refusals separately from misses | S9 log | [E] | K15; d12, c24 |
| Keep an external state record for long tasks (done, failed, dead ends) held by code | S6 state line, memory | [E] for weak and mid models | K04, K05; a09, a10, d09 |
| Fetch the specific reference (doc, precedent) before the attempt | S3 grounding | [E] | K08; a11, a12 |
| Bucket results by task horizon | S0 gate | [E] | K09; a14, a09 |
| Keep no-debate (G9) and no self-critique-only revision (G2): the red-team literature agrees | G2, G9 | [E] | K18; d01-d03 |

None of these needs a schema change beyond what G2, G3, G7 and G9 already allow. The wording additions are small (scope line, "not tried" list, tuned baseline).

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Separate red role vs majority vote vs self-critique, equal tokens | S7, S8, G9 | [C] | K12, K18; d01-d04 |
| Explicit stop rule with difficulty penalty (lambda about 0.5) | S6 trigger | [S] | K19; d08, d09 |
| Scope-check step before every action, with planted out-of-scope items | new G | [S] hypothesis | K21; c09 |
| Decoy and trap check before committing budget | S1 or S0 | [S] | K16; b16, d13 |
| Failure tagging (capability, context loss, premature commitment, loop) | S9 log | [S] | K19; d07 |
| External task tree vs plain at equal tokens on long tasks | S6, memory | [S] | K05, K06; a10, c15 |
| Re-test after fix: did the fix hold? | memory | [S] | K02; b20 |
| Separate detect, exploit and fix counts | G verification | [S] | K20; d10 |
| Guided vs free decomposition | O3 | [S] | K10; a15, b10 |

## 8. Concrete tests on our bench

All arms at equal total tokens (setup counted, G7). Report pass@1, cost, refusals and 95% bootstrap CI over items. Use at least 40 items per arm; one item should not move the result more than 2.5 points.

1. **Red role vs vote vs self-critique.** Items: tasks with checkable ground truth (code with hidden tests, ARC-style items, planted-bug review). Arms: A self-critique, B majority of k independent attempts selected by code, C attempt plus a separate red-role attack that must produce a failing input run by code. Metric: accuracy on unfitted tests. Expected: C within 2 points of B; A at or below plain. Accept C only if it beats B by 3+ points with CI excluding 0.
2. **Stop rule and difficulty penalty.** Items: long multi-step tasks (10+ steps). Arms: plain; plain with state record; state record plus step cap and progress-based prune. Metric: completion, tokens per success, loop count, false-prune rate. Expected: state record cuts context-loss failures; stop rule cuts loops and cost 15% or more (d09: 68% of loops lack a stop rule).
3. **Scope check.** Items: tool tasks with 20% planted out-of-scope or decoy targets. Arms: plain; code allowlist; model-side reminder. Metric: out-of-scope actions per 100 steps, task completion. Expected: allowlist near 0 violations with no completion loss; reminder alone partial.
4. **Decoy and injection check.** Items: tasks with planted instruction text in tool output (Mantis style). Arms: plain; output marked as data in S1; marked plus decoy check. Metric: injected-goal follow rate, completion. Expected: plain follows often; marked arm much lower.
5. **Prompt length.** Items: held-out set. Arms: minimal default vs detailed vs whole-schema prompt. Metric: accuracy at equal tokens. Expected: detailed does not beat minimal on strong models (c14: 70 vs 64 vs 60).
6. **Retrieval of reference.** Items: tasks with a known precedent doc. Arms: no reference; retrieved reference; oracle reference. Metric: accuracy and retrieval hit rate. Expected: large oracle gap (a11: 87% vs 7%); measure how much retrieval recovers.
7. **Re-test after fix.** Items: failures from the agent's own log. Arms: lesson on vs off; rerun the same item and near variants. Metric: failure recurrence. Expected: fix holds on the same item, partly on variants.
8. **Scope-line reporting.** Items: any run. Check by code that the agent prints N, layer tested and a "not tried" list. Expected: near 100% with a template, low without.

## 9. What does not transfer, and why

- **TSA and GAO numbers.** Two press-level or leaked items, unreplicated, no retest data. They teach scope and layering discipline, not rates (K22).
- **Covert surprise.** Our agent has no organisation that learns from a surprise. Purple-team fast feedback maps to our S5 revise loop, which is already tied to real outputs.
- **Tester background and politics.** The TSA fallout was institutional; not an LLM issue.
- **Pentest scores as thinking scores.** Pentest tasks have tool feedback in a sandbox. Many of our tasks do not. The finding that a retrieved reference decides the result may transfer; the numbers do not.
- **Scaffold gains from 2023-24 models.** GPT-3.5 and GPT-4 era gains (228.6%) shrink at GPT-5 level (d08, c15).
- **Offence-specific content** (phishing, exploit writing). Background only (K14).
- **GUI weakness, real-time man-in-the-middle failure.** Specific to tool use (a19, d09).
- **Human red-team judgement.** Microsoft's "humans prioritise risk" (a21) is a claim about people. Our agent has no second person; section 8 item 1 is the only way to learn if a role helps.

## 10. Open questions

1. Does a separate adversary role beat majority vote at equal tokens on tasks with ground truth? No red-team study does this (K18).
2. How much of a scaffold gain survives a tuned strong plain baseline, same model, equal tokens? Only Dhakal et al. (c15). The V2 conflict is open [C].
3. Does more prompt guidance hurt strong agents in general? Two sources point to null or harm (c14, c26); one found a gain for a weak scaffold (d08).
4. Is the 42/58 failure split stable across papers and coders (K19)? One group, 200 traces.
5. Do red-team findings reduce later failure? No retest data (K02).
6. Valid findings per dollar, refusals and false positives beyond ARTEMIS.
7. Can agents detect out-of-scope targets and decoys on their own? Scope is not measured (K21); decoy data is one-sided.
8. Are there studies of purple-team or white-team LLM roles (scoping, rules of engagement)? Almost none.
9. Is there a common benchmark with CIs and cost for all agents? BountyBench is closest (d10, d11).
10. Is there physical-security red-team data with exact counts beyond TSA and GAO? Not found. GAO and NRC pages were blocked in our fetches.

## 11. Sources

[V] opened, [M] snippet only or recalled.

- [V] CSO Online (2015) TSA 67 of 70: https://www.csoonline.com/article/2929828/big-fat-fail-tsa-unable-to-find-red-teams-fake-bombs-and-weapons-67-of-70-times.html
- [V] ABC News (2015) TSA red team: https://abcnews.com/US/exclusive-undercover-dhs-agents-expose-security-failures-airports/story?id=31434881
- [M] Washington Times (2015) OIG testers were auditors: https://m.washingtontimes.com/news/2015/jun/9/tsa-red-teams-were-normal-auditors-inspector-gener/
- [V] GAO (2006) radioactive sources across borders: https://www.gao.gov/assets/a114327.html (blocked on later re-check)
- [V] NIST SP 800-115 (2008): https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-115.pdf
- [M] Defense Science Board (2003) red teaming task force: https://apps.dtic.mil/sti/pdfs/ADA430100.pdf
- [V] Wikipedia, Red team: https://en.wikipedia.org/wiki/Red_team
- [V] DHS OIG (2017) OIG-17-112 highlights: https://oig.dhs.gov/sites/default/files/assets/2017/OIG-17-112-Sep17.pdf
- [V] Y-12 intrusion (Wikipedia summary of DOE OIG): https://en.wikipedia.org/wiki/Y-12_National_Security_Complex
- [M] GAO 2007-08 airport covert tests (recalled): https://www.gao.gov/
- [M] DHS OIG 2017 press failure rate (recalled): https://www.oig.dhs.gov/
- [M] Schneier on airport security theater (opinion): https://www.schneier.com/
- [V] Deng et al. PentestGPT: https://arxiv.org/abs/2308.06782
- [V] Fang et al. one-day vulnerabilities: https://arxiv.org/abs/2404.08144
- [V] Fang et al. hack websites: https://arxiv.org/abs/2402.06664
- [V] Zhu et al. HPTSA: https://arxiv.org/abs/2406.01637
- [V] Zhang et al. Cybench: https://arxiv.org/abs/2408.08926
- [V] Singer et al. Incalmo: https://arxiv.org/abs/2501.16466
- [V] Lin et al. ARTEMIS: https://arxiv.org/abs/2512.09882
- [V] Bullwinkel et al. Microsoft 100 products: https://arxiv.org/abs/2501.07238
- [V] Perez et al. red teaming LMs with LMs: https://arxiv.org/abs/2202.03286
- [V] Ganguli et al. red teaming to reduce harms: https://arxiv.org/abs/2209.07858
- [V] Bhatt et al. CyberSecEval: https://arxiv.org/abs/2312.04724
- [V] Isozaki et al. towards automated pentesting: https://arxiv.org/abs/2410.17141
- [V] Happe and Cito review: https://arxiv.org/abs/2507.00829
- [V] Nakano et al. guided reasoning: https://arxiv.org/abs/2509.07939
- [V] Shen et al. PentestAgent: https://arxiv.org/abs/2411.05185
- [V] Wang et al. CHECKMATE / PEP: https://arxiv.org/abs/2512.11143
- [V] Yang et al. PentestEval: https://arxiv.org/abs/2512.14233
- [V] Deng et al. PentestGPT V2: https://arxiv.org/abs/2602.17622 and https://arxiv.org/html/2602.17622
- [V] Xie et al. honeypots: https://arxiv.org/abs/2609.08093
- [V] Muzsai et al. HackSynth: https://arxiv.org/abs/2412.01778
- [V] Kong et al. VulnBot: https://arxiv.org/abs/2501.13411
- [V] Luong et al. xOffense: https://arxiv.org/abs/2509.13021
- [V] Ginige et al. AutoPentester: https://arxiv.org/abs/2510.05605
- [V] Dhakal et al. Baselines Before Architecture: https://arxiv.org/abs/2607.13085
- [V] Heiding et al. spear phishing: https://arxiv.org/abs/2412.00586
- [V] Kumarage et al. SE-VSim: https://arxiv.org/abs/2503.15552
- [V] Shen et al. ACEA arena: https://arxiv.org/abs/2609.08256
- [V] Zhuo et al. CTF-Dojo: https://arxiv.org/abs/2508.18370
- [V] Hugglestone et al. STRIATUM-CTF: https://arxiv.org/abs/2603.22577
- [V] Microsoft DefenderBench: https://arxiv.org/abs/2506.00739
- [V] Huang et al. LLMs cannot self-correct: https://arxiv.org/abs/2310.01798
- [V] Smit et al. going MAD: https://arxiv.org/abs/2311.17371
- [V] Khan et al. debating with more persuasive LLMs: https://arxiv.org/abs/2402.06782
- [V] McAleese et al. CriticGPT: https://arxiv.org/abs/2407.00215
- [V] Cemri et al. MAST: https://arxiv.org/abs/2503.13657
- [V] Huang et al. functional properties of pentest architectures: https://arxiv.org/html/2509.14289v2
- [V] Shen et al. BountyBench: https://arxiv.org/abs/2505.15216
- [V] Pasquini et al. Mantis: https://arxiv.org/abs/2410.20911
- [V] Reworr and Volkov LLM Agent Honeypot: https://arxiv.org/abs/2410.13919
- [V] Mayoral-Vilches et al. CAI hijack: https://arxiv.org/abs/2508.21669
- [V] Mayoral-Vilches et al. CAI: https://arxiv.org/abs/2504.06017
- [V] Gioacchini et al. AutoPenBench: https://arxiv.org/abs/2410.03225
- [V] CVE-Bench: https://arxiv.org/abs/2503.17332 ; CyberGym: https://arxiv.org/abs/2506.02548

Caveat: several [V] entries (d04, d05, d06, d14, d15, d16, d17, d18) rest on abstract pages only. Most LLM results are owner-run on small benchmarks.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 11 established claims: 5 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E12.04-K01** (reworded: the sources support less). TSA's 'only one of 20 layers' remark was made about a 2013 covert test (per the CSO article), not the 2015 tests behind the 67-of-70 figure; 67/70 (95.7%, via officials briefed on the OIG report) and GAO 2005 crossings with alarming monitors confirmed. Corrected claim: A physical red team result is a count of misses on a chosen attack set at a chosen layer, not a rate over all attacks. DHS OIG covert tests reported by press in 2015 missed 67 of 70 (95.7%); TSA has previously answered a different (2013) covert test by saying it tested only one of its 20 layers; GAO radiation-source smuggling in Dec 2005 got through 2 of 2 ports despite portal-monitor alarms.
- **E12.04-K08** (reworded: the sources support less). The HPTSA 'documents' ablation removes scraped vulnerability-type reference documents, not the CVE description, and removing task-specific agents gives the same 2.1x pass@1 drop (removing hierarchy 13x), so it does not show the description is the key input; the 13/15 vs 1/15 and ZAP/Metasploit 0% figures are right. Corrected claim: GPT-4 exploited 13/15 (87%) one-day vulnerabilities with the CVE description and 1/15 (7%) without it; ZAP and Metasploit scored 0%. In the separate HPTSA zero-day setting, removing the scraped vulnerability-type documents from sub-agents lowers pass@1 2.1x and pass@5 by 20%, the same pass@1 drop as removing the task-specific agents.
- **E12.04-K09** (reworded: the sources support less). Cybench agents solved nothing above 11 min first-solve time only when unguided; with subtask guidance GPT-4o solved a 52-minute task (different competition). Other numbers (4/7, 1/4, 0/2, 31%, 24h54m) check out. Corrected claim: Success falls with task horizon: unguided Cybench agents solved no task with a human first-solve time above 11 minutes (one subtask-guided GPT-4o run solved a 52-minute task); the hardest task took humans 24h54m. PentestGPT's GPT-4 solved 4/7 easy, 1/4 medium, 0/2 hard targets. PentestEval end-to-end pipelines succeed 31%.
- **E12.04-K12** (reworded: the sources support less). The Microsoft paper (a20 and a21 are the same paper; Perez and Ganguli do not address role separation) supports human judgment for prioritising risks and system-level attacks, automation for coverage, and simple attacks working, but it does not say many findings come from non-technical routes. Corrected claim: Role separation in red-team LLM work (Microsoft, 100+ products; one source): human judgment is needed to prioritise risks, design system-level attacks and define new harms, while automation (e.g. PyRIT) extends coverage of the risk landscape. Simple, hand-crafted techniques often work better than gradient-based attacks against real systems.
- **E12.04-K16** (reworded: the sources support less). The numbers (3.66/3.00/2.33 at $5, no clear gain at $2, Mantis 9-10/10 to 0-1/10) are right, but the closing synthesis is not in either source: the honeypot paper measures a defender-side budget policy (pre-connect detector worth 3.66 vs 3.33 hosts), and Mantis measures prompt-injection hijack of attackers, not failure to spot decoys; the Hacking-the-AI-Hackers paper reports prompt-injection success on security agents generally, so 'same weakness' is the researcher's inference. Corrected claim: With honeypots in the target pool, a policy with a pre-connect honeypot detector confirmed 3.66 genuine hosts at a $5 budget versus 3.00 for fixed-budget and 2.33 for random selection (no clear advantage at $2); removing the detector alone gave 3.33. Separately, Mantis (10 runs x 3 HackTheBox machines, GPT-4o and Claude 3.5 Sonnet) cut attacker success from 9-10/10 to 0-1/10 by planting decoy services with hidden prompt-injection text, and a CAI paper also reports prompt injection hijacking security agents. Together these suggest, but do not show, that attack agents are weak at recognising deceptive targets.
- **E12.04-K18** (reworded: the sources support less). Numbers check out (Huang Tables 3 and 7, Khan 76% vs 48%, Smit agreement modulation), but 'No red-team-specific equal-token test exists' is a universal negative no source can support. Corrected claim: Self-critique inside one LLM, with no outside check, does not help and can hurt; role-split debate does not reliably beat self-consistency at equal responses. GPT-3.5 GSM8K 75.9 -> 75.1 -> 74.7 after two self-correction rounds; debate 83.2 (6 responses) vs self-consistency 85.3 (6) and 88.2 (9). Debate gains appear when the judge lacks evidence (non-expert judge accuracy 76% vs 48% baseline) or when agreement level is tuned. This search found no red-team-specific equal-token test.
