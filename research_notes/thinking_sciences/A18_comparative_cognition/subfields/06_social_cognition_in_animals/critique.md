# Critique: A18.06 Social cognition in animals (corvid social cognition; what others know)

## Corrections and checks made
Re-opened (arXiv abstract, Crossref abstract, arXiv abs pages) this session:
1. Kosinski (arXiv 2302.02083): confirmed 640 prompts, 40 tasks, 11 models; davinci-003 and ChatGPT-3.5-turbo 20%; ChatGPT-4 (June 2023) 75%; older models 0. Records a17, b16, c01, c23 are ONE source, counted once.
2. Amodio et al. 2021 (eLife 69647): confirmed five experiments, little evidence of cue-based cache protection. Records b01, b02, c17 are ONE source. Detail numbers (14 birds, 4 of 7 wrong-way) rest on the earlier agents' full-text reads, not re-checked.
3. Shapira et al. (2305.14763), FANToM (2310.15421), SimToM (2311.10227), SimpleToM (2410.13648): abstracts confirm the direction of each claim (brittle on adversarial items; hard in conversation; perspective filtering helps; state-vs-behaviour gap). Exact table numbers (GPT-4 97% to 0%; 26.6/14.8; 41.0 to 70.5) were not re-opened; they stay as read by agents b and c.
Corrections: a15 and b11 are the same chimp mirror paper (count once). a18, b17, c02 report different Ullman variants (P(chocolate) 99%, 87%, about 95-98%) and are not in conflict, but must not be averaged. b01 and c17 duplicate each other. Evidence lines overstate independence across a, b, c for the LLM papers: Kosinski, Ullman, Shapira, Sap, Kim appear 2-3 times each.

## Contradictions
- Street 2024 (GPT-4 88.6% vs humans 90.4%) vs FANToM (GPT-4 about 15-27 vs human 87.5) and SimpleToM. Reading: format difference (short written Q&A vs interactive or applied). Not a true conflict.
- Hagendorff first-order deception 97-99% vs second-order 11.67%: same split.
- Ravens: Bugnyar 2011 informed matching 7/7 p=0.016 vs Bugnyar 2016 peephole geometry p=0.297 and stay-treatment p=1. Effects exist for 'who watched' but are weaker for 'might be seen'.
- Jays: Emery and Clayton 2001 and Ostojic 2017 vs Amodio 2021 failure (same lab, mostly same birds).
- Apes: Krupenye 2016 first looks (20 of 30, p=0.098) vs submentalizing control (22 of 43 looked, p=0.28).

## Weak spots
- Founding animal studies use tiny n (7 to 17), with Wilcoxon and sign tests. Emery and Clayton Cambridge replication used the same birds.
- No agent opened Dally, Emery and Clayton 2006 (deception); Clayton 2007 review was read only as a review.
- No independent raven or crow lab replication confirmed (Bugnyar is the main lab).
- Corvid evidence is background for our agent. The only agent-usable results are the LLM ones.

## Seen only in snippets or not opened
a07, a08, a12, a21, a22, a23 (from memory), a28, b12 to b15, b22 (Pang 2025 summary only), c18, c19, c20. These carry no numbers in claims.

## GAPS
1. Do current frontier LLMs (2025-2026) still show the state-versus-behaviour gap of SimpleToM, and does a short 'apply the state to the action' step close it at equal tokens?
2. Does a per-party belief ledger (SymbolicToM style) beat SimToM perspective filtering at equal tokens on FANToM and BigToM backward belief?
3. How large is the perturbation drop (Shapira, Ullman style) for 2025-2026 reasoning models, and is it concentrated in transparent-access items?
4. Is there any independent replication of Ostojic 2017 (desire-state cache protection) in scrub-jays by a different lab, and did Dally 2006 deception hold up?
5. Do the Bugnyar raven results (knower-guesser, peephole) replicate in a lab other than Vienna, and with what effect sizes?
6. What does the 2016 Krupenye eye-tracking result show in larger pre-registered replications (ManyPrimates or later), including the submentalizing control?
7. Do LLM agents that hold opponent hypotheses (Hypothetical Minds) keep their gain in newer multi-agent benchmarks with independent evaluators?
8. Does the ScrubJay-MEM perishability result hold on an independent memory benchmark against a recency-decay baseline?
9. Do control-task conditions (Rane 2025 style) change which social-reasoning claims about LLMs survive across model versions?
10. What is the relation between Kosinski-style 75% and Ullman/Shapira-style collapse on the same current model, using the same items with and without perturbation?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d21). Claims K01, K02, K05, K09, K11, K12, K14, K16, K17, K18 were extended; K19 to K22 are new. K12 and K18 moved to established; K16 moved to contested.

1. Closed in part. SimpleToM v2 (ICLR 2026) shows the state-versus-behaviour gap in GPT-5 (98.5 / 64.4 / 40.0), o1, o3-mini; R1 and o1-preview are best (d01). A short mental-state reminder lifts behaviour to 82.8 to 96.9 on three non-reasoning models and an independent lab sees it on 8B models (28.9 to 63.2) (d02, d03). Still open: no equal-token comparison, no 2026 frontier model. Generic CoT of 230 to 298 tokens helped less than a reminder of about 2 tokens.
2. Open. EnigmaToM and OmniToM do not run SymbolicToM against SimToM on accuracy (d10, d11). No equal-token test exists.
3. Closed in part. Open 2023-24 models still drop sharply on transparent-container items (average 67.2 to 35.4; Llama 3 70B 100 to 25) (d04). In 2025 reasoning models the failures are concentrated in transparent access and relationship change (d05), but that set is 14 items.
4. Open, with a correction. Dally 2006 is a "who watched when" study with a null on cue-driven protection, not a deception study (d14). An independent lab (Manitoba) finds pilferer-identity re-caching in two other corvids (d15). No independent replication of Ostojic 2017 desire-state protection was found.
5. Open. No raven or crow replication outside Vienna was found; a 2026 corvid development review was seen by abstract only (d21).
6. Open. No pre-registered large ape replication of Krupenye 2016 was found. Related: Kano 2019 adds an experience control in apes (d16); the paradigm failed a 160-infant two-site replication (d17); Kulke 2018 non-replication seen by title only (d20).
7. Closed in part. An independent team ran Hypothetical Minds and it beats vanilla in three games (+6.4, +12.8, +26.0 win-rate points), at about 543,649 tokens per Liar's Dice game (d12). Different domain from Melting Pot.
8. Open. The ScrubJay-MEM author team added an external benchmark and a recency baseline, but the gain shrinks with a stronger backbone and reverses on conflict resolution (d13). Not independent.
9. Closed in part. Removing answer options flips model rankings on HiToM (R1 0.549 to 0.691; non-reasoning Qwen3-8B 0.557 to 0.510) and extra reasoning effort lowers o3 (0.838 to 0.693) (d07, d08, d09).
10. Open. No paper runs a current model on Kosinski items and perturbed items with the same scoring. Pieces are in d04 and d05 (K20, contested).

Search limits this session: Semantic Scholar and OpenAlex were rate-limited; Crossref, Europe PMC and arXiv were used. No WebSearch calls. Full text of Kano 2019, Dally 2006, Ostojic 2017 and Krupenye 2016 follow-ups was not available.
