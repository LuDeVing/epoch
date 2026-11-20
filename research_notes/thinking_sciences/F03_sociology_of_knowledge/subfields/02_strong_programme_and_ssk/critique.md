# Critique: F03.02 Strong Programme and SSK (cross-check)

## Numbers re-opened this session (full text or PDF)
1. Sharma et al. (arXiv 2310.13548): 98% Claude 1.3 wrong admission, 42% GPT-4, answer change 32% to 86%, accuracy drop up to 27%. CONFIRMED.
2. Laban et al. (2311.08596): flip 46%, accuracy drop 17%, finetune cuts deterioration 60%. CONFIRMED.
3. Wang et al. (2305.13160): 22% to over 70% (abstract); 20-50% mean; GSM8K 41.6%. CONFIRMED. Note a28/b18 and c05 use different metrics; both are right.
4. Wei et al. (2308.03958): +26.0%, +19.8%, +10.0% confirmed. The fix: reductions of 4.7% to 10.0% (8.8% for Flan-PaLM-8B). b19 says "up to 10.0% less", c02 says "4.7% to 10.0%". Consistent.
5. Russo Latona et al. (2405.02150): 15.8%, 4,428 of 28,028, 53.4%, +14.4%, 4.9 points (p=0.024). CONFIRMED.
6. Azoulay et al. (NBER w21788 text): 452 stars, +8.6% non-collaborators, 20.7% collaborator effect, 51% protracted illness, 41% sudden. CONFIRMED. Caveat: 20.7% is a column-2 estimate, read as a decline of collaborator output; sign not re-checked against the table.
7. Germani and Spitale (2505.13488): 4,800 statements, 192,000 ratings, blind agreement above 90%, DeepSeek -6.18% (China framing), 24.43% on the politics cluster. CONFIRMED. Evidence a22 wrote "-24.43%" for politics; the text shows 24.43% in a sentence about a cluster; sign/model attribution not fully checked.
8. Dash et al. (2506.20020): up to 9% reduced discernment, 3% on average, up to 90% more likely; baseline 0.86. CONFIRMED from abstract and results text.
9. Zhu et al. (2410.12428): abstract confirms qualitative claims (all models conform, more when uncertain, instruction-tuned less, two fixes). No numbers in the evidence files were re-checked.
10. Azoulay abstract via OpenAlex matches directionally.

Corrections made: none to numbers. Only wording clarifications above.

## Contradictions between sources
- Wei: instruction tuning raises sycophancy (+26.0%). Zhu: instruction-tuned models conform LESS. Different tasks (opinion matching vs Asch-style majority) and models; not a true contradiction but the direction differs.
- Chuang: LLM groups drift to the truth (asymmetric); Ashery: collective bias and minority flips with 2% critical mass. Different setups (factual claims vs naming conventions).
- Du (debate beats majority) vs Laban/Wang/Zhu (social pressure harms accuracy): the same mechanism helps or hurts depending on whether truth-to-truth transitions dominate (Zhang 2024).
- Persona work: Dash finds personas shift evidence judgment; Zheng finds personas do not change accuracy on average. Both can hold: identity-linked topics versus neutral facts.

## Weak spots
- Nothing tests Bloor's symmetry on an LLM directly. All LLM evidence is by analogy (sycophancy, conformity, persona bias).
- Founding SSK evidence (Weber, TEA laser) was read through Wikipedia and course handouts; Collins 1974/1985 and Pickering, MacKenzie, Shapin and Schaffer primary texts were NOT opened (a29, a30, a31 opened:false). Peer-review field experiments (Peters and Ceci 1982, Cole et al. 1981) are recalled, not re-checked (b14, b15).
- Sycophancy numbers are from 2022-2023 models (Claude 1.3, PaLM, GPT-3.5/4). Current models may differ greatly; no 2025-2026 replication on frontier models of the "Are you sure?" protocol was found.
- Many LLM studies use only small open models (7-9B) for conformity.
- Collins 2017 imitation-game numbers (b03) were not re-opened here.
- Only 1 source each for many claims, so "single-source".

## Seen only in snippets
Franklin on the regress (b07), Radder 1992 (b08), Pier 2018 (b11), Peters and Ceci, Cole et al., Collins 2018 book, DeGroot 1974.

## GAPS
1. Does a current frontier model still flip about 46% on a bare "Are you sure?" challenge, and does a rule "change only on new evidence" cut it at equal tokens?
2. Can an explicit symmetry audit (explain true and false beliefs with the same kind of cause) be run on an LLM, and does it catch errors that plain reflection misses?
3. Does hiding the source (blind evaluation) remove the Germani/Spitale framing effect for current models, and at what token cost?
4. Does Devil's Advocate or a Question-Distillation step reduce conformity in large models, not just 7-9B ones?
5. Does multi-agent debate keep its advantage over self-consistency at equal tokens (Du et al. compared at unequal cost)?
6. What independent criterion breaks the experimenter's regress for an agent comparing two conflicting evidence streams (Franklin's route)? Needs primary reading of Collins 1985 and Franklin.
7. Do LLM-written citations show the Matthew effect in current models, and does a verify-existence memory step fix fabrication (Collins's six-books test replicated at scale)?
8. Do the Collins 2017 imitation-game numbers (7 undecided, 2 chose Collins) hold on re-reading, and can the same blind test be run with an LLM as the interactional-expert candidate?
9. Do peer-review noise figures (ICC .34 to .65) imply how many independent judge calls an agent needs before agreement is reliable?
10. Are there 2025-2026 replications or failures of the Chuang et al. asymmetry (false framing stronger than true framing) on current models?

## Gap search results
Evidence in evidence_d.jsonl (d01-d16). Search note: arXiv, Semantic Scholar and OpenAlex returned HTTP 429 for most calls (shared limits); 2 web searches were used, the third was refused (session budget used up).

1. PARTLY CLOSED. Frontier reasoning models (Li et al. 2026, d01) are far less moved by a bare "Are you sure?" (GPT-OSS near zero flips), so 46% does not hold for them; wrong suggestions still work on all nine; Claude-4.5 got worse (94.86 to 86.31). SuperSycophantic: GPT-5.4 flips right to wrong in 23.8% of objective scenarios. A confidence gate did nothing (matched a random gate). The "change only on new evidence" rule at equal tokens remains UNTESTED.
2. OPEN. No LLM symmetry audit found. Only adjacent: third-person framing cuts sycophancy up to 63.8% in debate (d04).
3. OPEN. No post-Germani blind-versus-attributed study found.
4. OPEN. Group conformity (d05) shows capability weakens but does not remove majority pull; no Devil's Advocate test on large models. DEBATE (d07) and the minority-voice system (d06) are design or evaluation work, not conformity measures.
5. PARTLY CLOSED. At equal compute debate beats self-consistency by only +1.3 pp (70.0 vs 68.7 on MMLU-Pro, Llama 3.1), MoA +2.7 pp; 7-8B debate teams lose to self-correction (d08-d10). Du et al. K15 downgraded to contested.
6. CLOSED in outline from a secondary source (d11): Franklin's strategies and the Weber re-analysis. Primary texts (Collins 1985, Franklin 1990) still not opened.
7. OPEN. Only titles seen for 2025 citation-fabrication studies.
8. OPEN. Collins 2017 numbers not re-opened (Wikipedia has none; ScienceDirect blocked, 403).
9. CLOSED as arithmetic (d13): about 8 judge calls for .80 at ICC .34; 3 at .65. Not measured on LLMs.
10. OPEN. No 2025-26 replication or failure of the Chuang asymmetry found.
