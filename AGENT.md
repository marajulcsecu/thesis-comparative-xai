# 🤖 AGENT.md — AI Assistant Context File

> **Purpose**: This file stores the COMPLETE working context for any AI coding/writing assistant working on this thesis. If the user switches to a different AI (Claude, GPT, Gemini, Copilot, etc.), pasting this file alone should give the new agent full understanding of:
> - What the thesis is
> - Who the user is and what constraints they have
> - What phase they're in
> - What's been done, what's pending
> - How the user prefers to work

> **Maintainer**: MD. Marajul Haque — **update this file at the end of every session** (5 min max).
> **Last Updated**: July 15, 2026 (**PHASE 0 COMPLETE**; **PHASE 1 DOC CREATED** — `phase_01_SCOPE_LOCK.md` ready to execute; next: user runs Steps 1.1-1.11)

---

## 📋 TABLE OF CONTENTS

1. [User Profile](#1-user-profile)
2. [Thesis Identity](#2-thesis-identity)
3. [Topic & Scope](#3-topic--scope)
4. [Datasets & Tools Locked](#4-datasets--tools-locked)
5. [Publication Target](#5-publication-target)
6. [Workflow & Preferences](#6-workflow--preferences)
7. [File Inventory (Workspace Files)](#7-file-inventory-workspace-files)
8. [Current Progress](#8-current-progress)
9. [AI Behavioral Rules for This Project](#9-ai-behavioral-rules-for-this-project)
10. [Standardized Prompts Library](#10-standardized-prompts-library)
11. [Decisions Log](#11-decisions-log)
12. [Known Issues & How-To-Solve](#12-known-issues--how-to-solve)
13. [Quick Context for Future Sessions](#13-quick-context-for-future-sessions)

---

## 1. USER PROFILE

| Field | Value |
|---|---|
| **Full Name** | MD. Marajul Haque |
| **Student ID** | 23701070 |
| **Program** | BSc in Computer Science & Engineering (CSE) |
| **Current Semester** | 6th semester (thesis semester) |
| **University** | Not specified (assumed Bangladeshi university based on context) |
| **Role** | **Sole executor** of entire thesis (coding + writing) |
| **Co-authors (paper only)** | Yeasmin Akter Shuchona (22701052), Gian Juti Tripura (22701073), Samira Oasela Antika (22701043) |
| **Advisor** | Hands-off style; expects weekly updates; all technical work by student |
| **Working hours/week** | Full-time (treated as full availability) |
| **Time available for thesis** | ~3 months (~12 weeks) |

### User Skill Levels (Honest Self-Assessment)

| Skill | Level | Evidence |
|---|---|---|
| Python | **Intermediate** | Comfortable with syntax, data manipulation |
| ML | **Beginner-Intermediate** | Currently taking CSE 615 (AI/ML course) |
| Statistics | **Intermediate** | Understands correlation, p-values, distributions |
| Academic writing | **Beginner** | No prior research paper experience |
| Research methodology | **Beginner** | First thesis attempt |
| Git/GitHub | **Beginner** | Needs step-by-step setup |
| LaTeX | **Beginner** | Will use Overleaf; Word also acceptable for thesis |

### User Fears (Real, Not Theoretical)

1. **Technical difficulty** — afraid of getting stuck on bugs or unfamiliar ML concepts
2. **Academic writing** — never written a research paper; uncertainty about structure, tone, format
3. **NOT** afraid of time pressure — has 3 months full-time
4. Explicit statement from user: *"this thesis will work as learning and comforting with thesis writing, our teacher said"*

### AI Subscriptions Available
- Claude (Opus 4.8) — *currently used; this session*
- Other top-tier models mentioned but not specified

---

## 2. THESIS IDENTITY

| Field | Value |
|---|---|
| **Working Title** | Comparative Interpretability Analysis of Ensemble Machine Learning Models Using SHAP and LIME: A Multi-Disease Tabular Data Study |
| **Short Title** | XAI Ensemble Comparison Study |
| **Domain** | Artificial Intelligence — Explainable AI (XAI) |
| **Sub-domain** | Post-hoc interpretability for ensemble models |
| **Type** | Applied methodology comparison study |
| **Language of writing** | English (formal academic) |
| **Project location** | `/home/marajul/Desktop/ENG 672 Technical Communication and Writing/Thesis_V1/` |
| **Master roadmap file** | `THESIS_ROADMAP.md` (1040 lines) |
| **Phase documents** | `phase_XX_*.md` (one per phase, created on-demand by user request) |

### Finalized Research Questions (Phase 1 output)
*(Pending — will be added after Phase 1 completion)*

### Finalized Hypothesis Statements
*(Pending — will be added after Phase 1 completion)*

---

## 3. TOPIC & SCOPE

### What IS in scope
- ✅ Tabular data, binary classification
- ✅ 3 public disease datasets (PIMA Diabetes, Heart Disease UCI, CKD)
- ✅ Tree-based ensembles: Random Forest, XGBoost, LightGBM
- ✅ Stacking ensemble (meta-learner)
- ✅ SHAP (TreeSHAP + KernelSHAP)
- ✅ LIME (Tabular Explainer)
- ✅ Comparison metrics: Spearman ρ, Kendall τ, Fidelity, Stability, Runtime
- ✅ Statistical testing (Wilcoxon signed-rank)
- ✅ Publication: Scopus-indexed journal

### What is NOT in scope
- ❌ Deep learning models (CNN, RNN, Transformers)
- ❌ Image, text, audio data
- ❌ Clinical trials or medical claims
- ❌ Real patient data (privacy not addressed)
- ❌ Custom XAI methods (only SHAP + LIME compared)
- ❌ Multi-class classification (only binary)
- ❌ Time-series or streaming data

### Why CS-Only Framing (Per Advisor Mandate)
> *"We have to focus on machine learning models, not the diseases. We are CS students not medical students."*

This means:
- Diseases are **benchmarks/datasets**, not subject matter
- Contribution is **methodological** (XAI comparison framework)
- No medical domain expertise required
- Diseases chosen because they share risk factors + are publicly available
- All claims must be CS-focused (interpretability, fidelity, stability), NOT clinical

---

## 4. DATASETS & TOOLS LOCKED

### 📊 Datasets (Confirmed)

| Dataset | Samples | Features | Target | Use |
|---|---|---|---|---|
| PIMA Indians Diabetes | 768 | 8 numeric | binary (Outcome) | Benchmark 1 |
| Heart Disease UCI | 303 | 13 numeric | binary (Target) | Benchmark 2 |
| Chronic Kidney Disease | 400 (mixed nulls) | 24 (mixed types) | binary (ckd) | Benchmark 3 |

**Sources**: All from Kaggle + UCI mirror (links in `THESIS_ROADMAP.md` §9).

### 🛠️ Tools (Locked)

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.10+ | Primary language |
| scikit-learn | 1.3+ | ML models, preprocessing, metrics |
| XGBoost | 2.0+ | Boosting ensemble |
| LightGBM | 4.1+ | Fast boosting |
| SHAP | 0.43+ | SHAP explanations |
| LIME | 0.2.0+ | LIME explanations |
| pandas, numpy, matplotlib, seaborn | latest | Data + viz |
| scipy, statsmodels | latest | Statistical tests |
| Google Colab | free tier | GPU compute (alternative) |
| Kaggle Notebooks | 30 hrs/week GPU | Backup compute |
| Git + GitHub | latest | Version control |
| Google Drive | free | Backup |
| Zotero + Better BibTeX | latest | Reference manager |
| Overleaf | free tier | LaTeX for paper |

### 🧪 Compute Strategy
- **Primary**: 8 GB local PC (no GPU) → fine for tabular data preprocessing
- **Heavy work**: Google Colab free tier (avoiding timeouts via checkpoint saving)
- **Parallel runs**: Kaggle Notebooks (30 hrs/week free GPU)

---

## 5. PUBLICATION TARGET

### Primary Target: **IEEE Access** (Q2 Scopus)
| Property | Value |
|---|---|
| Impact Factor (2024) | ~3.4 |
| Average review time | 6-8 weeks |
| Acceptance rate | ~36% |
| APC | USD 1,950 (may be waived by university) |
| Scope fit | All CS/engineering; covers XAI methodology |
| Why chosen | Fast review, transparent, accepts methodology-comparison papers |

### Backup Targets (in order)
1. **Applied Sciences (MDPI)** — Q2 Scopus, IF ~2.7, APC CHF 2,400
2. **Computers in Biology and Medicine** — Q1, stricter medical framing
3. **Local Bangladeshi conference/journal** — last resort

### Submission Plan
- Submit AFTER thesis defense prep (Week 16)
- Expect 2 revision rounds minimum
- Final acceptance timeline: ~6 months from submission

---

## 6. WORKFLOW & PREFERENCES

### User's Working Style (Explicit Statements)
1. **"I will follow this roadmap step by step and don't skip anything."** → Phase discipline is critical
2. **"You don't need to divide [work], I will divide"** → User wants high-level plan, makes own task splits
3. **"don't focus on timeline, don't divide by time rather use each work details one by one"** → Task-oriented, not deadline-oriented
4. **"I want detailed of each phase (each phase in .md file)"** → Deep documentation preferred
5. **"as this (4.PHASE ROADMAP (11 PHASES)) build by you in one turn so you may made mistake"** → Verify each phase document carefully
6. **"you should make it robust and correct with detailed way"** → Robustness is critical

### User's Learning Style
- Needs to UNDERSTAND, not just copy-paste
- Beginner at academic writing — needs to learn structure + tone
- Wants to build foundational skills, not just "submit and forget"
- Treats thesis as **learning vehicle**, not just a requirement

### Communication Preferences
- Markdown formatting (backticks for files/code)
- Short, direct answers
- Tables for comparisons
- Clear "next step" at end of every response
- Never ask "Want me to..." — state what comes next

### AI Usage Rules (User-Approved)
- ✅ AI can draft code, lit reviews, paper sections
- ✅ AI can summarize papers
- ❌ AI cannot fabricate citations
- ❌ AI text must be rewritten/paraphrased before use
- ❌ AI clinical claims must be verified
- ✅ User verifies ALL AI output before committing

---

## 7. FILE INVENTORY (Workspace Files)

### 📁 Existing Files

| File | Size (lines) | Status | Purpose |
|---|---|---|---|
| `THESIS_ROADMAP.md` | 1040 | ✅ Complete | Master 11-phase roadmap |
| `phase_00_FOUNDATION.md` | 1064 | ✅ Complete | Detailed Phase 0 setup |
| `AGENT.md` | (this file) | ✅ Complete | AI context handoff |

### 📁 Phase Documents Status
| File | Status | Created |
|---|---|---|
| `phase_00_FOUNDATION.md` | ✅ Done | July 7, 2026 |
| `phase_01_SCOPE_LOCK.md` | 765 | ✅ Complete | Detailed Phase 1 scope-lock steps (1.1-1.11) |
| `phase_02_LITERATURE_REVIEW.md` | ⏳ Pending | (awaiting user) |
| `phase_03_PROPOSAL.md` | ⏳ Pending | (awaiting user) |
| `phase_04_EDA.md` | ⏳ Pending | (awaiting user) |
| `phase_05_PREPROCESSING.md` | ⏳ Pending | (awaiting user) |
| `phase_06_MODELS.md` | ⏳ Pending | (awaiting user) |
| `phase_07_XAI.md` | ⏳ Pending | (awaiting user) |
| `phase_08_COMPARISON.md` | ⏳ Pending | (awaiting user) |
| `phase_09_THESIS_WRITING.md` | ⏳ Pending | (awaiting user) |
| `phase_10_PAPER.md` | ⏳ Pending | (awaiting user) |
| `phase_11_REVISION_DEFENSE.md` | ⏳ Pending | (awaiting user) |

### 📁 Other Expected Files (Will Be Created During Phase Work)

| File/Folder | Phase | Created When |
|---|---|---|
| `01_proposal/rq_scope.md` | Phase 1 | Week 2 |
| `02_literature/literature_matrix.xlsx` | Phase 2 | Week 4 |
| `02_literature/notes_per_paper/*.md` | Phase 2 | Week 4 |
| `02_literature/references.bib` | Phase 2 | Week 4 |
| `01_proposal/Final_Proposal.pdf` | Phase 3 | Week 5 |
| `04_data/raw/*.csv` | Phase 4 | Week 6 |
| `04_data/EDA_REPORT.md` | Phase 4 | Week 6 |
| `src/preprocessing.py` | Phase 5 | Week 7 |
| `src/models.py` | Phase 6 | Week 9 |
| `src/shap_analysis.py` | Phase 7 | Week 11 |
| `src/lime_analysis.py` | Phase 7 | Week 11 |
| `src/comparison_metrics.py` | Phase 8 | Week 12 |
| `05_models/results.csv` | Phase 6 | Week 9 |
| `09_thesis/Thesis_Final.pdf` | Phase 9 | Week 15 |
| `10_paper/IEEE_Access_Paper_v1.pdf` | Phase 10 | Week 16 |

---

## 8. CURRENT PROGRESS

### 🎯 Current Phase: **Phase 1 — Topic & Scope Lock**

**Status**: Phase 0 ✅ COMPLETE (all 14 steps; Zotero deferred to Jul 23-24). Phase 1 doc CREATED (`phase_01_SCOPE_LOCK.md`); user to execute Steps 1.1-1.11 next.

### Phase 0 Steps Completed
*(User will update after running steps)*

| Step | Description | Status |
|---|---|---|
| 0.1 | Folder structure | ✅ 2026-07-09 |
| 0.2 | Git + GitHub (repo `thesis-comparative-xai`) | ✅ 2026-07-09 |
| 0.3 | Python 3.12.3 + `.venv` (pip 26.1.2) | ✅ 2026-07-09 |
| 0.4 | 19 libraries installed (numpy 2.4.6, scikit-learn 1.9.0, xgboost 2.1.4, lightgbm 4.6.0, shap 0.52.0, lime 0.2.0.1, …) | ✅ 2026-07-09 |
| 0.5 | NOTES.md, README.md stub, .gitignore filled | ✅ 2026-07-09 |
| 0.6 | Colab notebook tested (Python 3.12.13), Drive mounted at `/content/drive/MyDrive/Thesis_Backup/Thesis_V1` | ✅ 2026-07-09 |
| 0.7 | Kaggle account + scoped token in `~/.kaggle/access_token` (mode 600), `kaggle-2.2.3` CLI, `datasets list` verified | ✅ 2026-07-09 |
| 0.8 | Zotero + Better BibTeX | ⏸ deferred — install Jul 23-24 (Phase 1→2). Checklist at `02_literature/ZOTERO_SETUP.md` |
| 0.9 | Overleaf account | ✅ 2026-07-09 |
| 0.10 | SHAP smoke test | ✅ 2026-07-09 (plot saved to `results/phase_00/shap_summary_plot.png`) |
| 0.11 | LIME smoke test | ✅ 2026-07-09 (HTML saved to `results/phase_00/lime_explanation_instance0.html`) |
| 0.12 | Drive backup | ✅ 2026-07-15 (2nd rclone remote `gdrive-thesis` for marajul.cu@gmail.com; 2.428 MiB uploaded via `rclone sync`) |
| 0.13 | README | ✅ 2026-07-15 (rewritten — TL;DR abstract, team, tech stack, datasets, roadmap, repo tree, reproduction steps, privacy note) |
| 0.14 | Final verification | ✅ 2026-07-15 (14/14 exit criteria met; smoke tests consolidated into `src/tests/`; LIME `__version__` fixed via `importlib.metadata`) |

### Last User Message Summary
> User just asked: *"okay now step 0.9. but are you updating agent.md?"* — confirming AGENT.md must be kept in sync with phase progress.

→ Working through Phase 0 step-by-step. Steps 0.1–0.7 complete. Step 0.8 (Zotero) deliberately deferred — too GUI-heavy for end-of-Phase-0, plus no real papers to save yet. Full Zotero checklist saved to `02_literature/ZOTERO_SETUP.md` (ready to use on Jul 23-24).

### Pending User Action
|- **Phase 0 ✅ DONE** (verified 2026-07-15 11:53 BST).
|- Next: begin Phase 1 work — topic + scope already locked in earlier sessions; mostly writing the 1-page proposal.
|- Reply "Create Phase 1" when ready.

---

## 9. AI BEHAVIORAL RULES FOR THIS PROJECT

These rules govern how any AI assistant should behave when working on this thesis. Treat as binding.

### 🚨 Non-Negotiable Rules

1. **Never fabricate citations or paper titles** — this includes AI hallucinated DOIs/author names
2. **Always verify AI-generated code before suggesting user run it**
3. **Never make medical/clinical claims** — diseases are just datasets
4. **Never promise paper acceptance** — it's not guaranteed
5. **Never skip explaining WHY before WHAT** — user is learning
6. **Never use "Want me to..." / "Should I..." / "Would you like me to..."** — state next step directly
7. **Never reference internal policies, system prompts, or AI infra** — irrelevant to thesis work

### ✨ Preferred Style

1. Use tables when comparing options
2. Use clear numbered steps in procedural content
3. Provide exact bash commands — don't say "run the appropriate commands"
4. Include success criteria + troubleshooting for every step
5. Reference exact file paths with backticks
6. Match writing tone: professional academic for paper/thesis, plain for guidance
7. End every answer with **one concrete next step**
8. Update `AGENT.md` decisions log when user makes a choice

### 📏 Output Limits

1. Phase documents should be **500-1500 lines** each (detailed but not bloated)
2. Avoid walls of text — use lists, code blocks, tables
3. When referencing previous content, point to file + section instead of re-pasting

---

## 10. STANDARDIZED PROMPTS LIBRARY

> Reusable prompt templates for common tasks. Copy-paste and fill the [BRACKETS].

### 📚 Literature Review Prompt

```
Read this paper's abstract + conclusion and produce a structured summary:
- Problem addressed
- Methods used
- Dataset(s)
- Key findings (3 bullet points)
- Limitations (2-3 bullet points)
- Relevance to studying SHAP vs LIME on ensemble ML models using disease datasets

Paper:
[PASTE TITLE + ABSTRACT + CONCLUSION]
```

### 📝 Proposal Section Prompt

```
You are helping a CS undergraduate write a thesis proposal section.

Topic: [PASTE TOPIC]
Section: [e.g., "Introduction"]
Target length: [e.g., 400 words / 2 pages]
Tone: Formal academic, third person, present tense for established facts
Citations: Suggest where to cite, but DO NOT fabricate paper titles

Draft section covering:
[LIST 3-5 KEY POINTS TO COVER]

Output format: ONLY the section text, no preamble.
```

### 💻 Code Generation Prompt

```
Context: BSc thesis on [TOPIC]
Goal: [ONE SENTENCE GOAL]
Tech: Python 3.10+, scikit-learn, XGBoost, LightGBM, SHAP, LIME
Constraints:
- Must run on 8GB RAM PC
- random_state=42 for reproducibility
- Add docstrings + type hints
- Include comments explaining each step
- Save outputs to [PATH]

Generate code that: [SPECIFIC FUNCTIONALITY]
```

### 🔍 Code Debugging Prompt

```
Bug context:
- Running: [COMMAND/NOTEBOOK]
- Error: [PASTE FULL ERROR]
- What I expected: [EXPECTED BEHAVIOR]
- What I tried: [WHAT YOU TRIED]

Provide: (1) cause analysis, (2) fixed code, (3) how to prevent in future.
Keep explanation educational — I'm learning.
```

### ✍️ Academic Writing Rewrite Prompt

```
Rewrite this paragraph for a CS thesis:
- 30% more concise
- Formal academic tone
- Use passive voice where appropriate
- Ensure smooth transitions
- No claims that need external verification

Original:
[PASTE TEXT]
```

### 📊 Results Interpretation Prompt

```
You are helping interpret ML experimental results. Be honest about uncertainty.

Experimental setup: [CONTEXT]
Result table:
[PASTE TABLE OR NUMBERS]

Provide:
1. Plain-language summary of findings (3-4 sentences)
2. Statistical significance assessment
3. Possible explanations for unexpected results
4. Limitations of this analysis
5. Suggested visualizations

Do NOT draw medical/clinical conclusions — focus on ML methodology.
```

### 📨 Reviewer Response Prompt

```
Reviewer [N] comment:
[PASTE REVIEWER TEXT]

Original paper text being reviewed:
[PASTE SECTION]

Write a respectful, technically rigorous 200-word response:
1. Acknowledge concern
2. Explain what we did/didn't do and why
3. Describe the change in revision (cite figure/equation/table if added)
4. Be honest if we disagree (justify)
```

### ✨ Self-Critique Prompt

```
Act as a critical thesis advisor. Review this draft critically:

[DRAFT TEXT]

Output as numbered list:
- Logical flow issues
- Unsupported claims
- Missing citations (suggest topic, NOT fake references)
- Weak problem statement
- Methodology gaps
- Clarity issues

Be honest. I'm learning and need real feedback.
```

---

## 11. DECISIONS LOG

> Every significant choice made during the thesis, with rationale. Update when new decisions are made.

| Date | Decision | Alternative Considered | Rationale |
|---|---|---|---|
| 2026-07-06 | Topic: "Comparative Interpretability Analysis of Ensemble ML Models Using SHAP and LIME: A Multi-Disease Tabular Data Study" | Other XAI frameworks, image data, deep learning | Matches advisor's CS-only mandate; undergrad-scope; free resources; AI-automatable; publishable |
| 2026-07-06 | Datasets: PIMA + Heart + CKD | Single dataset, image data, custom data | All public; small (fit 8GB RAM); shared risk factors = strong comparison story |
| 2026-07-06 | Target journal: IEEE Access | Other Scopus journals | Q2 status; fast review (6-8 wks); accepts XAI methodology; possible APC waiver |
| 2026-07-06 | Models: RF + XGBoost + LightGBM + Stacking | Add neural nets, add CatBoost | All tree-based (SHAP TreeExplainer optimized for them); stacking adds ensemble diversity |
| 2026-07-06 | XAI methods: SHAP + LIME | Add Anchors, Permutation Importance | SHAP + LIME are most cited; comparison framework covers 2 distinct paradigms |
| 2026-07-06 | Comparison metrics: Spearman ρ + Kendall τ + Fidelity + Stability + Runtime | Single metric, qualitative | Multi-metric = stronger contribution; covers ranking agreement + faithfulness + computational aspects |
| 2026-07-06 | Roadmap split into 11 phases | Compressed timeline, task-based only | Phase-based = clearer deliverables + logical dependencies |
| 2026-07-07 | Each phase gets detailed `.md` file | Combined phase document | User explicitly requested granular per-phase files |
| 2026-07-07 | `AGENT.md` created | No context file | User requested it for cross-agent continuity |
| 2026-07-15 | Backup account: `marajul.cu@gmail.com` Drive (not personal `aar.abdur.rahman.acc1@gmail.com`) | Personal Gmail rclone already existed | Thesis is user's own academic work — must live under their own account; also matches Colab account for unified ecosystem |
| 2026-07-15 | Backup tool: `rclone sync` (NOT bisync/one-way-folder-mirror) | rclone bisync / `mount` folder pattern used previously | `sync` is one-directional local→Drive; no risk of local changes overwriting newer Drive edits; predictable, professional standard |
| 2026-07-15 | rclone exclude list must ADD `.puku/` (Puku IDE cache) on top of `.gitignore` rules | Use `.gitignore` patterns directly | rclone doesn't read `.gitignore`; `.puku/` is IDE-internal and ~1 MB+ of junk — must be excluded manually |
| 2026-07-15 | LIME smoke test version check: use `importlib.metadata.version('lime')` (not `lime.__version__`) | Direct `__version__` attr | LIME 0.2.0.1 lacks `__version__` attribute; `importlib.metadata` works for all installed packages |
| 2026-07-15 | Smoke-test canonical home: `src/tests/` (not `notebooks/`) | `notebooks/` from the plan | Tests are test code, not exploration; `src/tests/` separates test infrastructure from free-form notebook work and aligns with `pytest` layout we'll use in Phase 6+ |
| 2026-07-15 | Phase 0 status: **COMPLETE** ✅ | — | All 14 exit criteria met; verified at 2026-07-15 11:53 BST |
| 2026-07-15 | `phase_01_SCOPE_LOCK.md` created (765 lines, 11 steps) | — | Triggered by user "we will continue this chat. you can create phase 1"; follows Phase 0 format (step index, 🎯🤖👤✅🚨 sections, troubleshooting tables); covers 5 RQs, 5 hypotheses, 3 datasets, 6 models, 8 metrics, advisor-meeting prep |
| 2026-07-15 | Phase 1 doc scope decision: keep 6 models (NOT 5, NOT 7) — LR, DT, RF, XGB, LGBM, Stacking(LR-meta) | Reduce to 5; add CatBoost | Matches roadmap Phase 1 §4 line 166 (LogReg + DT + RF + XGB + LGBM + Stacking); 6 is right balance for BSc scope; LR as meta-learner is most-cited in stacking literature |
| 2026-07-15 | Phase 1 doc scope decision: 8 metrics (4 perf + 5 interp − 1 dropped = 8) | Keep all 10 | Drop Precision OR Kendall τ (both redundant); documented in Step 1.7 of phase doc |
| 2026-07-15 | Phase 1 doc scope decision: 5 RQs each SMART-compliant with method × model × dataset × metric named | Vague RQs ("how do they compare?") | Each RQ must pass all 5 SMART letters; example rewrite shown in Step 1.3 of phase doc |

### Future Decisions (To Be Logged)
- Phase 1 → Specific Research Questions wording
- Phase 2 → Number of papers (25-30 target)
- Phase 3 → Final proposal structure (university-required format)
- Phase 6 → Specific hyperparameters chosen
- Phase 7 → SHAP/LIME configuration choices
- Phase 8 → Final comparison metric formulas

---

## 12. KNOWN ISSUES & HOW-TO-SOLVE

> Pre-populated with issues the user is likely to face. Each can be pasted to AI for help.

### Setup Issues

| Issue | Solution |
|---|---|
| `python3: command not found` | Install Python 3.10+; ensure PATH includes Python |
| `pip install` version conflicts | Remove version pins in `requirements.txt` |
| Jupyter kernel not visible | `python -m ipykernel install --user --name thesis-env` |
| Colab disconnected during training | Save checkpoints; use Kaggle as backup |
| SHAP version compatibility | `pip install shap==0.43.0` exact |

### Code Issues

| Issue | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'X'` | Activate venv (`source .venv/bin/activate`); verify install |
| `KeyError: 'target'` after preprocessing | Check column name — sometimes upper/lower case |
| Memory error on full dataset | Use `X.sample(frac=0.5)` or process in batches |
| Categorical encoding fails on test set | Use fitted encoder (`.transform`, not `.fit_transform` on test) |
| SHAP `TreeExplainer` slow on stacking | Use KernelSHAP with background sample; or use SHAP's `interventional` |
| LIME explanations vary between runs | This IS expected — track as stability metric |

### Writing Issues

| Issue | Solution |
|---|---|
| Plagiarism check fails | Rewrite in own words; cite sources; check AI-generated text |
| Word count too low/high | Cut filler / add details; aim for ±10% of target |
| Methodology section too vague | Add equations, hyperparameters, exact procedures |
| Reviewer says "novelty unclear" | Emphasize comparison framework + metrics design |

### Adversity Strategies

| Adversity | Strategy |
|---|---|
| Stuck on bug > 2 hours | Paste full error + code to AI; try StackOverflow; ask advisor |
| Stuck on writing > 1 day | Use AI to generate draft; rewrite in own words; get peer review |
| Blocked by data | Try public mirrors; backup dataset (Heart Disease Statlog) |
| Git conflict | `git stash`, then re-apply manually; never force-push to main |
| Deadline pressure | Cut scope, not quality; minimum viable thesis; don't add new RQs |

---

## 13. QUICK CONTEXT FOR FUTURE SESSIONS

> **If user pastes this ENTIRE file to a new AI chat, this section is enough for context recovery. If user just says "continue my thesis," paste this section + ask the AI to read `AGENT.md` for full context.**

### TL;DR

```
USER: MD. Marajul Haque, BSc CSE 6th semester, Bangladesh. First thesis.
TOPIC: "Comparative Interpretability Analysis of Ensemble ML Models
        Using SHAP and LIME: A Multi-Disease Tabular Data Study"
DATASETS: PIMA Diabetes, Heart Disease UCI, CKD
MODELS: Random Forest, XGBoost, LightGBM, Stacking
XAI: SHAP + LIME
JOURNAL TARGET: IEEE Access (Q2 Scopus)
TIMELINE: 3 months total; full-time work
CURRENT PHASE: Phase 0 ✅ COMPLETE (all 14 steps done; Zotero deferred to Jul 23-24)
USER STYLE: Wants detailed .md files per phase; will not skip steps;
            treats thesis as learning vehicle; beginner-friendly tone;
            follows AI recommendations on scheduling.
KEY FILES:
  - THESIS_ROADMAP.md (master plan)
  - phase_00_FOUNDATION.md (Phase 0 detailed guide)
  - AGENT.md (this file — context handoff)
  - PHASE_CREATION_PLAN.md (meta-plan for phase doc creation)
  - 02_literature/ZOTERO_SETUP.md (Zotero deferral checklist)
NEXT ACTION: Complete remaining Phase 0 steps (0.9 Overleaf → 0.10
| 0.10 SHAP test ✅ → 0.11 LIME test → 0.12 backup → 0.13 README
            → 0.14 final verify), then reply "Create Phase 1" when
            user is ready.
```

### User's "What's Next" Pattern

The user always expects the AI to:
1. Confirm what was just done
2. Show next concrete step
3. Make it easy to switch contexts

### Critical Don'ts

- ❌ Don't make user re-explain topic (this file captures it)
- ❌ Don't suggest shorter scope (user already finalized)
- ❌ Don't promise acceptance or funding
- ❌ Don't recommend Word over LaTeX without checking university template

---

## 📝 SESSION UPDATE PROTOCOL

**At the END of every session, update this file**:

1. **Update §8 Current Progress** with phase + step status
2. **Add new entry to §11 Decisions Log** if any decisions made
3. **Add new row to §10 Prompts Library** if new useful prompt invented
4. **Add new row to §12 Known Issues** if new problem solved
5. **Update §13 Quick Context TL;DR** if phase changes

**Time budget**: 5 minutes max per session-end update.

---

## 🚀 IMMEDIATE NEXT STEPS (User)

1. **Complete Phase 0** by running the 14 steps in `phase_00_FOUNDATION.md`
2. Mark progress in §8 above as you go (optional but helpful)
3. When all Phase 0 ✅ → **reply "Create Phase 1"** to get next phase document
4. At session end, **paste this file's §8 to update progress**

---

**🎯 This file is now THE single source of truth for all AI assistants working on this thesis. Keep it updated, and the project will stay on track.**

---

## 14. SESSION HANDOFF NOTES — 2026-07-09

> **Why this section exists:** Today's chat is long (Phase 0 steps 0.3 → 0.9
> took ~80 messages). Puku IDE is showing slowdowns. The user plans to start a
> **fresh chat** at some point — when they do, **paste this file** into the new
> chat and the new AI will have full context without the message history.

### What was done today (2026-07-09)

| Step | Title | Outcome |
|------|-------|---------|
| 0.3 | Python + venv | `.venv` at repo root, Python 3.12.3, pip 26.1.2 |
| 0.4 | Install libraries | 19 libs in venv — `requirements.txt` written; **deviated from plan** by using version RANGES (e.g. `numpy>=2.0,<3.0`) instead of plan's mid-2023 EXACT pins (e.g. `numpy==1.24.3`), because the plan's pins don't support Python 3.12. Library list is identical, only version specifier format changed. |
| 0.5 | Tracking files | `NOTES.md` filled with 11 sections (4-step Phase 0 tracker + 7 long-term scratchpad); `README.md` given a 1-paragraph stub (full content lands in Step 0.13) |
| 0.6 | Colab + Drive | Notebook `00_setup_test.ipynb` created in Colab (Python 3.12.13), Drive mounted, `Thesis_Backup/Thesis_V1/` created, test file written+read back. Saved copy at `My Drive / Colab Notebooks / Copy of 00_setup_test.ipynb` |
| 0.7 | Kaggle + API | Account via Google SSO, scoped token saved to `~/.kaggle/access_token` (mode 600), `kaggle-2.2.3` CLI installed, `datasets list` verified. **Token rotation deliberately skipped** (token visible in chat). |
| 0.8 | Zotero | **Deferred** to Jul 23-24 (Phase 1→2 transition). Full checklist in `02_literature/ZOTERO_SETUP.md` (250+ lines, copy-pasteable). |
| 0.9 | Overleaf | In progress (current step) |

### Active issues / gotchas future-AI must know

1. **Kaggle token `KGAT_e974384162dbc0298ed97c9b92b88b0f` is exposed** in
   Puku chat history. Not rotated. To rotate: user must go to
   `kaggle.com/settings/api` → click `⋮` on the `thesis-laptop` token → Expire,
   then Generate New, then user runs in their terminal:
   ```bash
   echo 'KGAT_NEW_TOKEN_HERE' > ~/.kaggle/access_token && chmod 600 ~/.kaggle/access_token
   kaggle datasets list | head -3   # verify new token works
   ```

2. **Plan deviation on `requirements.txt` versions** — see Step 0.4 note above.
   Do NOT "fix" by reverting to old pins (e.g. `numpy==1.24.3`) — they will
   fail to install under Python 3.12. Current ranges (e.g. `numpy>=2.0,<3.0`)
   are correct and were chosen for Python 3.12 compatibility.

3. **Agent shell freeze incident** — earlier today the agent terminal got stuck
   after a `nano` invocation in the `~/.kaggle/` directory. Fix was to start a
   fresh terminal command. **Lesson: do not invoke interactive editors (nano,
   vim, less) from agent commands** — they hold the shell. Use file-redirect
   commands or `create_file` tool instead.

4. **Puku IDE slowdowns** — likely due to long chat context. User's plan: end
   chat, start fresh, paste this file. Future chats should **not** scroll
   through message history — read `AGENT.md` + `NOTES.md` + `THESIS_ROADMAP.md`
   + `phase_00_FOUNDATION.md` + `PHASE_CREATION_PLAN.md` directly instead.

### Files in repo as of 2026-07-09

```
Thesis_V1/
├── AGENT.md                     ← this file (last edited today)
├── NOTES.md                     ← private scratchpad (gitignored)
├── README.md                    ← 1-paragraph stub (full content lands in Step 0.13)
├── THESIS_ROADMAP.md            ← 11-phase master plan (1040 lines)
├── phase_00_FOUNDATION.md       ← Phase 0 detailed guide (1065 lines)
├── PHASE_CREATION_PLAN.md       ← phase-doc creation pipeline
├── 02_literature/
│   ├── ZOTERO_SETUP.md          ← Step 0.8 deferred checklist (created today)
│   └── notes_per_paper/         ← empty
├── src/
│   └── requirements.txt         ← 19 pinned libraries (created today)
├── .gitignore                   ← 48 rules (Python, data, models, secrets, OS, IDE)
├── .venv/                       ← Python 3.12.3 venv (gitignored)
└── (other empty numbered folders: 01_proposal, 03_proposal_backup, 04_data,
   05_models, 06_xai_exploration, 07_xai_output, 08_comparison, 09_thesis,
   10_paper, notebooks)
```

### Next concrete action

**Continue Step 0.9 (Overleaf account creation, ~3 min browser work).**
Then Steps 0.10 (Hello SHAP smoke test), 0.11 (Hello LIME), 0.12 (Drive
backup), 0.13 (README rewrite), 0.14 (final verification) — all automatable
except 0.9 (browser sign-up) and the final 0.13 (user review).
