# A17.06 Conformity: cross-check critique

## Numbers re-opened (full text pulled this session) and result
1. Franzen and Mader 2023 (PLOS ONE): 33% error standard, 25% incentivised, 38% political conformity, N=210 recruited, 202 valid; Asch 1955 cited as 36.8% of 123. CONFIRMED.
2. Qu, Fu, Hu 2026 (2606.01637): harmful 15.6 to 62.9 (+47.3), beneficial 32.7 to 51.5 (+18.8), OR 28.5 vs 5.2, 56.8% collapse, authority 20.6/30.4. CONFIRMED.
3. Hussain and Nielbo 2026 (2608.11247): 23 models, 22.8/54.8/71.0 unanimous wrong; one peer 11.2 on MMLU; 83.6/89.4 match peers; R2 0.80-0.90; dissenter -7.5/-16.0; reasoning-first +7.2/+9.6; Reflection +7.9/-15.3. CONFIRMED. Note: numbers are macro-averages over models.
4. Weng et al. 2025 (2501.13381): Qwen2 IR 19.6 to 57.6; 405B IR 56.1; Llama3-70B 62.3 to 69.9, 69.9 to 32.6, 129 of 254 admit, reflection 22.8/35.2/68.5, persona 28.6 to 40.0 and 57.6 to 68.6. CONFIRMED. Not re-checked: the GPT-4o 17.3 to 37.9 line and the 6-to-5 non-monotone cases (a17 attributes it to Qwen2-72B 30.0 to 39.9, b17 to Llama3.1-405B 15.3 to 29.7; these are different models, so both may hold).
5. Zhu et al. 2024 (2410.12428): r=-0.777; TriviaQA 63.20/41.37/25.18/12.37/87.62. CONFIRMED.
6. Laban 2023: 46% flip, 17% drop, -8% GPT-4 to -34% Claude V2. CONFIRMED.
7. Sharma 2024: 98% wrongly admit (Claude 1.3), up to 27% accuracy drop, admission 42% to 98%. CONFIRMED. Note c17's line "'Are you sure?' cuts accuracy up to 27% (Claude 1.3)" is the paper's text; the 27% for a user-suggested wrong answer is LLaMA 2. Both appear; keep them separate.
8. Bose 2026 (2609.22090): 0/83.3/39.2 for gpt-oss-120B, Llama 70B 46.2 to 3.8, 96.7 to 85.8, 41,904 trials. CONFIRMED (Table 2/3).
9. Choi 2025: chi2 164.839 and 142.285, eta2p 0.068 and 0.1665, over 2,500 debates. CONFIRMED.
10. Cui and Du 2025: 100 to 26.67, 86.67 to 46.67, 93.33 vs 60.00. CONFIRMED.

## Corrections
- Asch's founding numbers: a01 (via Wikipedia) gives 50 experimental subjects and 35.7%; Franzen and Mader give 36.8% of 123 for Asch 1955. These are different reports (1951 vs 1955/56 pooled) and should not be mixed. Use 36.8% (N=123) as the headline; the 1951 figure is only secondary.
- Franzen and Mader's own text cites a meta-study of 44 strict replications with 25% average error rate. So "about a third" is the high end; the replication range is roughly 25 to 37%.
- Claim of "independent_sources" was lowered during triangulation where evidence lines were the same paper restated (e.g. a12/b13/c01 are all Zhu).
- b25/b26 and a22 etc. are arXiv ids dated mid-2026; they opened fine but are preprints.

## Contradictions between sources
- Model size: Weng (size raises independence, Qwen2 7B to 72B) vs Hussain (no size effect, 23 models). Likely pool and protocol differences.
- Instruction tuning: Zhu (less peer conformity) vs Wei, Perez, Sharma (more sycophancy toward a user).
- Tone: Zhu (confident and natural wording raises conformity) vs Hussain (certain wording lowers it, reasons raise it slightly).
- Gate by naming: Bose finds no conformity unless the paradigm is named (two of three families), while Zhu, Weng, Qu, Hussain find large conformity under plain prompts. Probable difference: Bose uses a conversational five-confederate script; the others use direct answer blocks.
- Human majority size: plateau at 3 vs linear to 7.
- Debate: Du 2023 gains vs Zhang 2025 and Wynn 2025 (no gain, more harm).
- Mori and Arai 2010 (not opened) says split majority is as strong as unanimous in humans; Zhu finds unanimity matters for LLMs.

## Weak spots
- Nearly all LLM work uses 7B to 70B open models and scripted peers. No result on frontier closed models except sycophancy studies on 2023 models (Claude 1.3, GPT-4).
- Peer-conformity (group) and sycophancy (single user) are different constructs but often blended.
- Most human numbers (Asch variations, Bond and Smith 1996, Sherif, Deutsch and Gerard) come from Wikipedia or study-guide summaries, never from the primary papers.
- Many LLM numbers are only in figures (Zhu, Zhang 2023, Bito, Wynn).
- Baron 1996, Mallinson and Hatemi, Fujita and Mori: second-hand only.

## Seen only in snippets or abstracts
a01-a10 (Wikipedia), b04-b08 (secondary pages), b11 (abstract), b12 (abstract), a11 (abstract), a21/b31 (results skimmed).

## GAPS
1. Does conformity to a stated wrong answer occur in frontier reasoning models (GPT-5-class, Claude-class, o-series) at the rate seen in 7-70B models, and does thinking budget change it? (Most decision-relevant for G5.)
2. What is the net effect on accuracy, at equal tokens, of a "solve before reading peers or the user's claim" rule versus read-first, on a mixed block of right and wrong claims?
3. Does the resistance-receptivity frontier (Hussain) hold for a scaffolded agent with evidence checking (tools, derivation), or can verification move off the frontier?
4. Which cheap signal best predicts which of the agent's answers will flip (self-consistency, logprob, verbalised confidence), and is it usable to gate when to check a claim?
5. How do the primary Asch (1951, 1955, 1956) numbers read: exact error by condition, N, and the dissenter and group-size results (replace the Wikipedia-based lines)?
6. What do Bond and Smith 1996 report (effect sizes, 133 studies), and how large is the cultural moderator and the US decline?
7. Do the "Are you sure?" flip and peer-majority flip share a mechanism, so a single guard covers both (user pushback in a long single-agent chat versus injected peers)?
8. Does a persuasive but wrong tool or retrieved-document output behave as a conforming source (MAD-Spear style) at the same rate as a peer, and does labelling its provenance reduce acceptance?
9. Can Bose's naming-gate result be reproduced on other families, and does it imply conformity in deployed use is mainly cue-triggered rather than general?
10. Is there evidence that conformity helps (Toyokawa-style) in repeated agent loops with noisy feedback, so a blanket anti-conformity rule would cost accuracy?

## Gap search results (evidence_d.jsonl d01-d23; claims K31-K42 added)

Closed or mostly closed:
- Gap 5 (Asch primary): CLOSED for the 1956 monograph. N=123, 12 critical trials, mean 36.8%, control 37 with under 1% error, 24% never erred, 27% erred 8-12 times, written answers 12.5% (N=14). The monograph has NO partner, dissenter or group-size result, so K02 and K03 stay second-hand (d04). The 35.7% of 50 figure is not in it.
- Gap 8 (wrong tool output / document): MOSTLY CLOSED. Frontier agents defer to one answer-like false document on 72.6-98.1% of clean-correct tasks (DRNoise); tool-role content is accepted more than peer or user content in Llama-3.1-8B (98.0% vs 75.75% vs 44.0%). Provenance labels help little (5.4% vs 1.7%; audit report 82.7% = trade review 84.0%; forum post 54.3%).
- Gap 10 (does conformity help): ANSWERED for humans only (Toyokawa and Gaissmaier 2022, 585 people). No LLM study found. Scope any anti-conformity rule to factual/derivable claims.

Partly closed:
- Gap 1 (frontier models): PARTLY. Newer open/Chinese models resist bare wrong answers better than GPT-4o (DeepSeek-V4-Flash 20% vs 64%) but still follow a plausible wrong rationale (37%-54%). Claude 4.5 Haiku, Kimi K2.5 and Qwen3-80B-Thinking at a 10K budget resist an incorrect user opinion hint more than other hint types. No study of GPT-5/o-series/large Claude under a unanimous wrong group, and no thinking-budget sweep, was found. Still open.
- Gap 3 (verification off the frontier): PARTLY. Generic verify instruction 12 to 28 of 100; attack-aware instruction 64-67 (GPT-5.4, DRNoise). Verification can move off the frontier only if it names the failure.
- Gap 4 (cheap signal): PARTLY. Round-0 features give AUC 0.80 for who adopts, 0.66 for who is harmed; gating gave no accuracy gain. No clean logprob vs self-consistency vs verbalised comparison.
- Gap 7 (shared mechanism): PARTLY. R^2=0.31 across 15 models between user-pressure and consensus-pressure yield; base models flip as much as Instruct; a correct dissenter cuts yield 54-73 pp. Shared in part, not shown to be one mechanism.

Still open:
- Gap 2 (solve-first vs read-first at equal tokens): only indirect evidence (10x solo budget beats debate in 7-8B models). No direct test.
- Gap 6 (Bond and Smith): abstract and paper not reachable. 133 studies, 24,617 participants, 17 countries and d 0.55 to 1.40 come from a blog only. Do not quote.
- Gap 9 (Bose reproduction): no independent replication found; Bito et al. found model-specific cue effects (gpt-5.1 ignored a named ballot but responded to evaluation), a different paradigm. preprints.org 202608.0971 returned 403 and was not read.

Search notes: arXiv search API, OpenAlex and Semantic Scholar were rate-limited, so 6 WebSearch calls plus direct arXiv PDF reads were used. Downloaded PDFs under D:/research_scratch/A17.06/ should be deleted.
