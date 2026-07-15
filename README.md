# Comparative Interpretability Analysis of Ensemble ML Models (SHAP vs LIME)

[![Status](https://img.shields.io/badge/Phase-0%20Foundation-blueviolet)]() [![Stack](https://img.shields.io/badge/Python-3.12-blue)]() [![License](https://img.shields.io/badge/License-Academic%20Use%20Only-lightgrey)]()

> **BSc CSE Thesis Project — Bangladesh**
> **Semester:** 6th · **Status:** Phase 0 — Foundation & Tooling (12 of 14 steps complete)

## Title

**Comparative Interpretability Analysis of Ensemble Machine Learning Models Using SHAP and LIME: A Multi-Disease Tabular Data Study**

## Abstract (TL;DR)

This thesis compares how two popular post-hoc explanation methods — **SHAP** (game-theoretic) and **LIME** (local surrogate) — agree, disagree, and behave when applied to ensemble classifiers (Random Forest, XGBoost, LightGBM, and a Stacking meta-learner) trained on three public binary-classification disease datasets. Comparison covers feature-ranking agreement (Spearman ρ, Kendall τ), fidelity, stability across runs, and runtime.

The contribution is **methodological**, not clinical: we treat the disease datasets as benchmarks for studying explainer behaviour on tabular data.

## Team

| Role | Name | ID |
|---|---|---|
| **Sole Executor** | MD. Marajul Haque | 23701070 |
| Co-Author (paper only) | Yeasmin Akter Shuchona | 22701052 |
| Co-Author (paper only) | Gian Juti Tripura | 22701073 |
| Co-Author (paper only) | Samira Oasela Antika | 22701043 |

## Research Goal

Compare SHAP and LIME explanations across ensemble ML models using public disease datasets as benchmarks — no medical claims are made.

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.12.3 |
| ML | scikit-learn 1.9, XGBoost 2.1, LightGBM 4.6 |
| Explainability | SHAP 0.52, LIME 0.2.0.1 |
| Statistics | SciPy, statsmodels |
| Compute (backup) | Google Colab, Kaggle Notebooks |
| Repo | Git + GitHub (private) |
| References | Zotero + Better BibTeX |
| Paper writing | Overleaf (LaTeX) |
| Backup | rclone → Google Drive (`gdrive-thesis`) |

## 📊 Datasets

| Dataset | Samples | Features | Type |
|---|---|---|---|
| PIMA Indians Diabetes | 768 | 8 numeric | Benchmark 1 |
| Heart Disease UCI | 303 | 13 numeric | Benchmark 2 |
| Chronic Kidney Disease | 400 | 24 mixed | Benchmark 3 |

All public, all binary classification, all small enough for an 8 GB laptop.

## 🗺️ Project Roadmap (11 Phases)

See [`THESIS_ROADMAP.md`](./THESIS_ROADMAP.md) for the complete plan. Phase documents live in `phase_XX_NAME.md` and are created on-demand.

| # | Phase | Status |
|---|---|---|
| 0 | Foundation & Tooling | 🟡 In progress (12/14 steps) |
| 1 | Topic & Scope Lock | ⏳ Pending |
| 2 | Literature Review | ⏳ Pending |
| 3 | Proposal | ⏳ Pending |
| 4 | EDA | ⏳ Pending |
| 5 | Preprocessing | ⏳ Pending |
| 6 | Models | ⏳ Pending |
| 7 | XAI (SHAP + LIME) | ⏳ Pending |
| 8 | Comparison | ⏳ Pending |
| 9 | Thesis Writing | ⏳ Pending |
| 10 | Paper Writing (IEEE Access) | ⏳ Pending |
| 11 | Revision & Defense | ⏳ Pending |

## 📂 Repository Structure

```
Thesis_V1/
├── AGENT.md                     # AI assistant context handoff
├── NOTES.md                     # private scratchpad (gitignored)
├── THESIS_ROADMAP.md            # 11-phase master plan
├── phase_00_FOUNDATION.md       # Phase 0 detailed guide
├── PHASE_CREATION_PLAN.md       # meta-plan for phase docs
├── notebooks/                   # exploratory + smoke-test scripts
├── results/                     # generated figures, tables, smoke-test outputs
├── src/                         # reusable code (preprocessing, models, XAI)
│   ├── requirements.txt
│   └── tests/                   # unit tests (planned)
├── 01_proposal/                 # Phase 3 deliverable folder
├── 02_literature/               # Phase 2 — papers + notes
│   ├── ZOTERO_SETUP.md
│   └── notes_per_paper/
├── 04_data/                     # Phase 4–5 — raw + processed datasets
├── 05_models/                   # Phase 6 — trained models + saved files
├── 06_xai_exploration/          # Phase 7 — experiment-specific XAI outputs
├── 07_xai_output/               # Phase 7 — final explanations
├── 08_comparison/               # Phase 8 — comparison results + figures
├── 09_thesis/                   # Phase 9 — thesis draft + figures
└── 10_paper/                    # Phase 10 — IEEE Access paper
```

## 🧪 Reproducing This Project

### Prerequisites
- Linux / macOS / WSL on Windows
- Python 3.10+ (project tested on 3.12.3)

### Setup

```bash
# 1. Clone the repo
git clone https://github.com/marajulcsecu/thesis-comparative-xai.git
cd thesis-comparative-xai

# 2. Create the virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r src/requirements.txt

# 4. Sanity-check the XAI tools (Phase 0 smoke tests)
python src/tests/test_shap_hello.py
python src/tests/test_lime_hello.py
```

Outputs land in `results/phase_00/`.

## 🔒 Privacy & Ethics

- **No patient data** is used — every dataset is a public benchmark.
- All clinical/medical interpretations are explicitly out of scope per advisor mandate ("we are CS students, not medical students").
- Dataset sources and licences are documented in `02_literature/` once Phase 2 is complete.

## 📜 License

Academic use only. Not for redistribution without author permission.

---

*Last updated: 2026-07-15 · Phase 0 in progress · Next: Step 0.13 README → Step 0.14 final verification → Phase 1*
