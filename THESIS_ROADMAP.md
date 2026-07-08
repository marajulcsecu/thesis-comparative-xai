# 🗺️ THESIS MASTER ROADMAP
## **Comparative Interpretability Analysis of Ensemble Machine Learning Models Using SHAP and LIME: A Multi-Disease Tabular Data Study**

> **Author**: MD. Marajul Haque (ID: 23701070) — *Sole Executor*
> **Co-Authors (paper only)**: Yeasmin Akter Shuchona (22701052), Gian Juti Tripura (22701073), Samira Oasela Antika (22701043)
> **Status**: Phase 0 — Foundation Setup
> **Last Updated**: July 6, 2026

---

## 📑 TABLE OF CONTENTS

1. [Project Context & Decision Log](#1-project-context--decision-log)
2. [Recommended Datasets](#2-recommended-datasets)
3. [Recommended Journal Target](#3-recommended-journal-target)
4. [Phase Roadmap (11 Phases)](#4-phase-roadmap-11-phases)
5. [Weekly Milestone Checklist (12 Weeks)](#5-weekly-milestone-checklist-12-weeks)
6. [Folder Structure](#6-folder-structure)
7. [Tools, Libraries & Stack](#7-tools-libraries--stack)
8. [AI Usage Guide Per Step](#8-ai-usage-guide-per-step)
9. [Resources & Direct Links](#9-resources--direct-links)
10. [Key Deliverables Tracker](#10-key-deliverables-tracker)
11. [Risk Register & Mitigation](#11-risk-register--mitigation)
12. [Glossary of Terms](#12-glossary-of-terms)

---

## 1. PROJECT CONTEXT & DECISION LOG

| Field | Value |
|---|---|
| **Thesis Title** | Comparative Interpretability Analysis of Ensemble Machine Learning Models Using SHAP and LIME: A Multi-Disease Tabular Data Study |
| **Short Title** | XAI Ensemble Comparison Study |
| **Domain** | Artificial Intelligence / Machine Learning — Explainable AI (XAI) |
| **Problem Statement** | Ensemble ML models achieve state-of-the-art accuracy on tabular healthcare data but are black boxes. Existing XAI tools (SHAP, LIME) are studied in isolation; a *systematic, quantitative comparison* on ensemble architectures is missing. |
| **Contribution** | A reproducible comparative framework that quantifies SHAP vs. LIME behavior across multiple ensemble strategies using public disease datasets as benchmarks. |
| **Scope IN** | Tabular data, binary classification, public datasets, tree-based ensembles, SHAP + LIME |
| **Scope OUT** | Deep learning models, image/NLP data, clinical trials, medical claims, real patient data |
| **Solo Executor** | MD. Marajul Haque — all coding, writing, experiments |
| **Co-Authors** | Co-author credit only; need to be informed and approve final draft |
| **Advisor** | Weekly meetings; advisor reviews progress, guides, signs off |
| **Compute** | Local PC (8 GB RAM, no GPU) + **Google Colab free tier** (heavy training) + **Kaggle Notebooks** (parallel runs) |
| **Skill Snapshot** | Intermediate Python, ML course (CSE 615), statistics ✅; academic writing ❌ |

### Decision Log (running record)
| Date | Decision | Reason |
|---|---|---|
| 2026-07-06 | Topic finalized | Advisor-aligned, undergrad-scope, publishable |
| 2026-07-06 | Datasets: PIMA, Heart Disease UCI, CKD | Shared risk factors → strong unified comparison story |
| 2026-07-06 | Target journal: *IEEE Access* (Q2 Scopus) | Fast review (~6-8 wks), accepts XAI methodology, no submission fee for some Bangladeshi universities; backup: *Applied Sciences (MDPI)* |

---

## 2. RECOMMENDED DATASETS

### ✅ Primary Dataset 1: PIMA Indians Diabetes Dataset
| Property | Value |
|---|---|
| **Source** | UCI ML Repository / Kaggle |
| **Samples** | 768 |
| **Features** | 8 (Pregnancies, Glucose, BP, SkinThickness, Insulin, BMI, DPF, Age) |
| **Target** | Outcome (0/1 diabetic) |
| **Why** | Highly cited baseline; clean for teaching; well-known features |
| **Kaggle link** | `https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database` |
| **UCI link** | `https://archive.ics.uci.edu/ml/datasets/diabetes` |

### ✅ Primary Dataset 2: Heart Disease UCI Dataset
| Property | Value |
|---|---|
| **Source** | UCI / Kaggle (`heart.csv` by ronit) |
| **Samples** | 303 |
| **Features** | 13 (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal) |
| **Target** | Target (0/1) |
| **Why** | Classic benchmark; 13 features give SHAP plenty to explain |
| **Kaggle link** | `https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset` |
| **UCI link** | `https://archive.ics.uci.edu/ml/datasets/heart+disease` |

### ✅ Primary Dataset 3: Chronic Kidney Disease (CKD) Dataset
| Property | Value |
|---|---|
| **Source** | UCI / Kaggle |
| **Samples** | 400 (158 complete records + 242 with missing values) |
| **Features** | 24 (mixed numeric + categorical) |
| **Target** | Classification (ckd/notckd) |
| **Why** | Tests categorical handling + missing-value strategy |
| **Kaggle link** | `https://www.kaggle.com/datasets/mansoordaku/ckdisease` |
| **UCI link** | `https://archive.ics.uci.edu/ml/datasets/chronic_kidney_disease` |

### ⚖️ Why these 3 datasets work for CS thesis
1. **Similar feature types** (numeric + binary outcome) → unified pipeline
2. **Shared risk factors** (Glucose, BP, Age, BMI-like features) → consistent comparison narrative
3. **All public, all free, all small** → fits 8 GB RAM after preprocessing
4. **Dataset size variance** (303 → 768) → tests method robustness

---

## 3. RECOMMENDED JOURNAL TARGET

### 🎯 Primary: **IEEE Access** (Q2 Scopus)
| Detail | Value |
|---|---|
| **Impact Factor** | ~3.4 (2024) |
| **Review Time** | 6-8 weeks average |
| **Acceptance Rate** | ~36% |
| **Scope** | All CS/engineering; covers XAI in healthcare |
| **APC** | USD 1,950 — *check if your university has a waiver agreement* |
| **Submission URL** | `https://ieeeaccess.ieee.org/submit-a-manuscript/` |
| **Why pick** | Fast, transparent review, broad scope, accepts methodology-focused papers |

### 🥈 Backup 1: **Applied Sciences (MDPI)**
- Q2 Scopus, IF ~2.7
- APC: CHF 2,400
- Faster acceptance, scope covers AI in healthcare

### 🥉 Backup 2: **Computers in Biology and Medicine** (Q1)
- Higher prestige but stricter medical framing
- *Use as backup if your department insists on Q1*

### ⚙️ Pre-submission checklist
- [ ] Confirm journal template from author guidelines
- [ ] Check APC funding (dept / supervisor / grant)
- [ ] Verify journal accepts methodological CS comparison papers (read 2 recent issues)

---

## 4. PHASE ROADMAP (11 PHASES)

> **🚨 Important Rule**: Do NOT move to the next phase until current phase deliverable is **complete + reviewed by you + at advisor's meeting**. Skipping phases = guaranteed rework later.

---

### **PHASE 0: Foundation & Tooling** ⏱️ Week 1

**Why this phase**: Set up workspace BEFORE any work — otherwise you'll lose hours finding files later.

**Tasks**:
1. Create folder structure (see Section 6)
2. Install Python 3.10+ locally + create virtual environment
3. Create Google Colab account + link Google Drive
4. Create Kaggle account + generate API token
5. Install Git + create GitHub private repo
6. Create Zotero/Mendeley account + import BibTeX style file
7. Setup Notion OR Excel sheet for tracking (literature matrix, weekly progress)
8. Install Overleaf account (LaTeX)
9. Create `NOTES.md` for daily observations & AI prompts that worked

**Deliverable**: Empty folder structure + accessible accounts + working notebook

**Exit Criteria**: Run a "Hello SHAP" Colab notebook successfully

---

### **PHASE 1: Topic Finalization & Scope Lock** ⏱️ Week 1-2

**Why**: Lock the scope NOW or it will drift.

**Tasks**:
1. Write 3-5 **Research Questions** (RQs):
   - **RQ1**: How consistent are SHAP and LIME feature rankings when applied to ensemble models trained on the same dataset?
   - **RQ2**: Does explanation stability (across similar patients) differ between SHAP and LIME?
   - **RQ3**: How does explanation fidelity (model-faithfulness) compare between SHAP and LIME on tree-based ensembles?
   - **RQ4**: What is the computational trade-off between SHAP and LIME explanations across ensemble architectures?
   - **RQ5**: Do SHAP and LIME identifications of "important features" agree with established medical risk factors in the literature?
2. Lock **Hypothesis statements** (e.g., H1: SHAP feature rankings have higher Spearman correlation with permutation importance than LIME)
3. Define **datasets** (Phase 2 list above)
4. Define **models** (Logistic Regression baseline, Decision Tree, Random Forest, XGBoost, LightGBM, Stacking Ensemble)
5. Define **metrics**:
   - Performance: Accuracy, Precision, Recall, F1, AUC-ROC
   - Interpretability: Spearman ρ, Kendall τ, Fidelity, Stability index, Runtime (sec/explanation)
6. Finalize with advisor (Week 2 meeting)

**Deliverable**: `01_proposal/rq_scope.md` document

**Exit Criteria**: Advisor approves RQs, scope, datasets, models, metrics

---

### **PHASE 2: Literature Review** ⏱️ Week 2-4 (longest research-only phase)

**Why**: A thesis WITHOUT a thorough lit review gets rejected instantly. You need **25-30 papers**.

**Tasks**:
1. Search Google Scholar, IEEE Xplore, Springer, Elsevier, ArXiv using:
   - ("ensemble learning" OR "XGBoost" OR "stacking") AND ("SHAP" OR "LIME") AND ("disease" OR "medical" OR "healthcare")
2. Filter: 2020-2026 papers, Q1/Q2 journals, citation count > 5
3. Read in this order:
   - **Round 1** — Abstract + conclusion only (~50 papers)
   - **Round 2** — Full skim of top 30
   - **Round 3** — Deep read of top 15-20
4. Build **literature matrix** (Excel/Notion table):
   - Paper | Year | Method | Dataset | Key finding | Limitation | Relevance to our RQ
5. Identify **research gap** — what is NOT done in existing work?
   - Expected gap: "No systematic quantitative comparison of SHAP vs LIME across multiple ensemble architectures on multi-disease tabular datasets"
6. Categorize papers into:
   - Ensemble methods (10 papers)
   - XAI methods (10 papers)
   - XAI in healthcare (10 papers)
   - SHAP vs LIME comparisons (5-8 papers)
7. Take notes in Zotero + `NOTES.md`

**Deliverable**:
- `02_literature/literature_matrix.xlsx`
- `02_literature/notes_per_paper/` (one `.md` per paper — use AI to summarize)
- Annotated bibliography (Zotero export `.bib`)

**Exit Criteria**: 25+ papers summarized, gap statement written, references imported

---

### **PHASE 3: Proposal Writing & Defense** ⏱️ Week 3-5

**Why**: Proposal is the contract between you and advisor. Changes after approval are hard.

**Tasks**:
1. Standard proposal structure (12-15 pages):
   - **Chapter 1**: Introduction (1.5-2 pages) — problem, motivation, contribution
   - **Chapter 2**: Literature Review (3-4 pages) — organized by themes
   - **Chapter 3**: Research Gap & Objectives
   - **Chapter 4**: Proposed Methodology (3-4 pages) — datasets, models, XAI framework, comparison metrics
   - **Chapter 5**: Expected Outcomes
   - **Chapter 6**: Timeline (Gantt chart)
   - References (BibTeX generated from Zotero)
2. Write using AI assistance (see Section 8)
3. **Self-edit** before showing advisor — AI cannot replace your judgment
4. Run **plagiarism check** (Turnitin/iThenticate — check university access)
5. Internal review (self + AI critique)
6. Advisor review (Week 4 meeting)
7. Revise based on feedback
8. **Proposal Defense** (~Week 5)

**Deliverable**: `03_proposal/Final_Proposal.pdf`

**Exit Criteria**: Proposal defended and approved with grade/feedback

---

### **PHASE 4: Data Acquisition & EDA** ⏱️ Week 5-6

**Why**: Garbage in = garbage out. EDA reveals hidden issues (missing values, class imbalance, outliers).

**Tasks**:
1. Download all 3 datasets from Kaggle (use Kaggle API token)
2. Save raw data to `04_data/raw/`
3. Write `01_eda.ipynb`:
   - Shape, dtype, head, describe
   - Missing value heatmap
   - Class balance bar chart
   - Histograms for numeric features
   - Correlation matrix heatmap
   - Outlier detection (boxplots, IQR method)
   - Pairplot of top correlated features
4. Save EDA plots to `04_data/eda_figures/`
5. Document insights in `04_data/EDA_REPORT.md`

**Deliverable**:
- `04_data/raw/{diabetes,heart,kidney}.csv`
- `04_data/eda_figures/*.png`
- `04_data/EDA_REPORT.md`

**Exit Criteria**: All 3 datasets understood; preprocessing plan written

---

### **PHASE 5: Data Preprocessing Pipeline** ⏱️ Week 6-7

**Why**: Unified preprocessing function ensures fair comparison across datasets.

**Tasks**:
1. Write `src/preprocessing.py`:
   - Missing value imputation (median for numeric, mode for categorical)
   - Outlier handling (clip at 1.5*IQR or keep + tree model absorbs it)
   - Categorical encoding (One-Hot or Label Encoding)
   - Numerical scaling (StandardScaler / MinMaxScaler — compare effect)
   - Train/test split (stratified, 80/20)
   - Save processed data to `04_data/processed/`
2. Write `02_preprocessing.ipynb` applying to all 3 datasets
3. Verify pipeline reproducibility (seed = 42 everywhere)

**Deliverable**:
- `src/preprocessing.py`
- `04_data/processed/{diabetes,heart,kidney}_train.csv` and `_test.csv`

**Exit Criteria**: All datasets processed identically, split, saved

---

### **PHASE 6: Model Development** ⏱️ Week 7-9

**Why**: This is your ENGINEERING phase. Models must be optimized BEFORE XAI is applied.

**Tasks**:
1. Train baselines first (sanity check):
   - Logistic Regression
   - Decision Tree
2. Train ensembles:
   - Random Forest (`n_estimators=200`, depth tuned)
   - XGBoost (use `XGBClassifier`)
   - LightGBM
3. Build Stacking Ensemble:
   - Base learners: RF + XGBoost + LightGBM
   - Meta-learner: Logistic Regression
4. Hyperparameter tuning with `GridSearchCV` (use small grid first, expand if time)
5. Log all results to `05_models/results.csv`
6. Generate comparison table (accuracy/precision/recall/F1/AUC)
7. Save best models as `.pkl` files in `05_models/saved_models/`

**Deliverable**:
- `src/models.py` (training + evaluation functions)
- `05_models/results.csv`
- `05_models/saved_models/*.pkl`
- `05_models/comparison_table.png`

**Exit Criteria**: Stacking ensemble beats individual ensembles; results documented

---

### **PHASE 7: XAI Implementation (SHAP + LIME)** ⏱️ Week 9-11

**Why**: This is your CORE NOVELTY. XAI must work correctly and produce publication-quality visualizations.

**Tasks**:
1. Write `src/shap_analysis.py`:
   - Use `shap.TreeExplainer` for tree models, `KernelExplainer` for stacking
   - Generate: summary plot, bar plot, force plot (single instance), dependence plot
2. Write `src/lime_analysis.py`:
   - Use `lime.lime_tabular.LimeTabularExplainer`
   - Generate: explanation plot for sample instances, feature importance plot
3. Write `06_xai_exploration.ipynb`:
   - Run SHAP and LIME on all 3 models × 3 datasets
   - Save visualizations
4. Generate 2-3 representative case studies (one easy patient, one borderline, one misclassified)

**Deliverable**:
- `src/shap_analysis.py`
- `src/lime_analysis.py`
- `07_xai_output/{dataset}_{model}_shap.png`, `..._lime.png`

**Exit Criteria**: Both SHAP and LIME produce clean visualizations for all models

---

### **PHASE 8: Comparative Analysis (NOVELTY)** ⏱️ Week 10-12

**Why**: This phase produces your **research contribution**. The comparison metrics must be novel.

**Tasks**:
1. Design 5 comparison metrics:
   - **Metric 1**: Spearman rank correlation between SHAP & LIME feature rankings (per model)
   - **Metric 2**: Kendall τ coefficient (alternative rank metric)
   - **Metric 3**: Fidelity — does removing top-k SHAP/LIME features drop accuracy proportionally?
   - **Metric 4**: Stability — variance of explanations across 5 random samples of similar patients
   - **Metric 5**: Computational cost — avg time per explanation (sec)
   - **Metric 6 (bonus)**: Agreement rate — % of features in top-5 of BOTH methods
2. Write `src/comparison_metrics.py` implementing all
3. Write `08_comparison_analysis.ipynb`:
   - Run all metrics on each (model × dataset) pair
   - Generate comparison tables
   - Generate heatmaps
   - Run statistical tests (Wilcoxon signed-rank for paired comparison)
4. Save result tables to `08_comparison/results/`

**Deliverable**:
- `src/comparison_metrics.py`
- `08_comparison/results/comparison_table.csv`
- `08_comparison/figures/*.png`

**Exit Criteria**: All metrics computed; significance tested; figures publication-ready

---

### **PHASE 9: Thesis Document Writing** ⏱️ Week 11-14 (parallel with Phase 10)

**Why**: Most students write the thesis in last week — DON'T. Write incrementally.

**Tasks**:
1. Use university template (get from dept)
2. Chapter-by-chapter writing:
   - **Ch 1 Intro** (3-4 pages)
   - **Ch 2 Lit Review** (8-10 pages — expand proposal version)
   - **Ch 3 Methodology** (10-12 pages — detailed, with code snippets as figures)
   - **Ch 4 Results** (12-15 pages — tables, figures, statistical analysis)
   - **Ch 5 Discussion** (5-6 pages — interpret results, address RQs)
   - **Ch 6 Conclusion & Future Work** (2-3 pages)
   - **Abstract** (250-300 words) — write LAST
3. Figures: use Matplotlib/Seaborn, consistent style
4. References: BibTeX from Zotero (final pass)
5. Appendices: code, full result tables
6. **Run plagiarism check** (target < 15% similarity)
7. **Self-edit** then advisor review (Week 12 + 14)

**Deliverable**: `09_thesis/Thesis_v1.docx` → `Thesis_Final.pdf`

**Exit Criteria**: Advisor approves final draft; plagiarism check clean

---

### **PHASE 10: Journal Paper Writing & Submission** ⏱️ Week 12-16

**Why**: University mandates publication. Thesis content adapts to journal format.

**Tasks**:
1. Choose journal (see Section 3 — IEEE Access recommended)
2. Get journal template (`.docx` or LaTeX)
3. Map thesis → paper:
   - Thesis 30+ pages → paper 12-15 pages
   - Keep Methodology + Results + Discussion
   - Compress Lit Review to 2-3 pages
   - Tighten Abstract, add Keywords
4. Write sections (AI-assisted, then edit):
   - Introduction (1.5 pages, sharp problem statement)
   - Related Work (2 pages)
   - Methodology (3 pages)
   - Results (3 pages)
   - Discussion + Conclusion (1.5 pages)
   - References (25-30 papers from thesis)
5. Cover letter to editor
6. Submit via journal portal (ScholarOne / Editorial Manager)
7. Track status weekly

**Deliverable**:
- `10_paper/IEEE_Access_Paper_v1.pdf`
- `10_paper/cover_letter.pdf`
- Submission acknowledgement email screenshot

**Exit Criteria**: Paper submitted with confirmation ID

---

### **PHASE 11: Revisions, Defense & Final Submission** ⏱️ Week 14-18+

**Why**: First submission usually gets "minor revision" or "major revision". Plan for 2 revision rounds.

**Tasks**:
1. If accepted: 🎉 celebrate, camera-ready prep
2. If revisions requested:
   - Read reviewer comments carefully
   - Write `response_to_reviewers.pdf` (point-by-point reply)
   - Re-run experiments if needed
   - Submit revised version + response letter (deadline: usually 30-60 days)
3. **Thesis defense preparation**:
   - Prepare 15-20 slide presentation
   - Practice 2-3 times (record yourself)
   - Prepare answers to expected questions
   - Have backup slides (Q&A appendix)
4. **Defense** (~Week 16)
5. **Final thesis submission** (bound copies if required)
6. **Post-defense corrections** if required
7. Update CV with publication

**Deliverable**:
- Thesis defended ✅
- Paper accepted ✅
- Publication ready ✅

---

## 5. WEEKLY MILESTONE CHECKLIST (12 WEEKS)

> Even though phases are non-linear, here is a **week-by-week task view** for accountability.

### Week 1 — Foundation
- [ ] Workspace folders created
- [ ] Python 3.10 installed + virtual env
- [ ] Google Colab working
- [ ] GitHub repo initialized
- [ ] Zotero library created
- [ ] 5 seed papers downloaded from Google Scholar

### Week 2 — Scope Lock
- [ ] 5 Research Questions written
- [ ] 3 datasets confirmed + downloaded
- [ ] Model list locked
- [ ] Metric list locked
- [ ] Advisor meeting Week 2 — scope approved

### Week 3 — Lit Review (start)
- [ ] 15 papers read (skimming)
- [ ] Literature matrix started
- [ ] Search strings logged
- [ ] Research gap statement drafted

### Week 4 — Lit Review (deep) + Proposal Draft
- [ ] 25 papers fully noted
- [ ] Lit review chapter drafted (5 pages)
- [ ] Proposal Method chapter drafted (3 pages)
- [ ] Advisor meeting — draft review

### Week 5 — Proposal Defense
- [ ] Proposal polished
- [ ] Plagiarism check < 15%
- [ ] Defense slides prepared (10 slides)
- [ ] **Proposal defense** ✅

### Week 6 — EDA
- [ ] All 3 datasets downloaded
- [ ] EDA notebook complete
- [ ] EDA report written
- [ ] Preprocessing plan finalized

### Week 7 — Preprocessing + Baseline Models
- [ ] `preprocessing.py` complete
- [ ] All datasets processed + split
- [ ] Logistic Regression baseline trained
- [ ] Decision Tree baseline trained

### Week 8 — Ensemble Models
- [ ] Random Forest trained + tuned
- [ ] XGBoost trained + tuned
- [ ] LightGBM trained + tuned
- [ ] Results table filled

### Week 9 — Stacking + XAI Start
- [ ] Stacking ensemble built
- [ ] Stacking beats individual models (validate)
- [ ] SHAP analysis working on diabetes dataset

### Week 10 — XAI Continuation
- [ ] SHAP complete on all 3 datasets
- [ ] LIME complete on all 3 datasets
- [ ] Visualizations saved

### Week 11 — Comparison Metrics
- [ ] All 5 metrics implemented
- [ ] Comparison tables generated
- [ ] Statistical tests run

### Week 12 — Thesis Writing Sprint
- [ ] Chapter 1-3 written
- [ ] Advisor meeting — interim review
- [ ] Chapter 4 drafted

### Week 13-14 — Thesis Completion
- [ ] Chapter 5-6 written
- [ ] Abstract written
- [ ] References finalized
- [ ] Plagiarism check

### Week 15 — Defense Prep + Paper
- [ ] Defense slides ready
- [ ] Journal paper draft started
- [ ] Advisor final review

### Week 16 — Defense + Submission
- [ ] **Thesis defense**
- [ ] Paper submitted to journal

### Week 16+ — Revisions
- [ ] Address reviewer comments
- [ ] Revise and resubmit
- [ ] Final thesis binding

---

## 6. FOLDER STRUCTURE

Create this EXACT structure in your workspace NOW:

```
Thesis_V1/
├── 01_proposal/
│   ├── rq_scope.md
│   ├── Final_Proposal.pdf
│   └── proposal_slides.pptx
├── 02_literature/
│   ├── literature_matrix.xlsx
│   ├── notes_per_paper/
│   │   ├── paper_01.md
│   │   ├── paper_02.md
│   │   └── ...
│   └── references.bib
├── 03_proposal/  (overlap with 01 — keep separate for clarity)
│   └── ...
├── 04_data/
│   ├── raw/
│   │   ├── diabetes.csv
│   │   ├── heart.csv
│   │   └── kidney.csv
│   ├── processed/
│   │   ├── diabetes_train.csv
│   │   ├── diabetes_test.csv
│   │   └── ...
│   ├── eda_figures/
│   └── EDA_REPORT.md
├── 05_models/
│   ├── results.csv
│   ├── comparison_table.png
│   └── saved_models/
│       ├── random_forest.pkl
│       ├── xgboost.pkl
│       ├── lightgbm.pkl
│       └── stacking.pkl
├── 06_xai_exploration/
│   ├── shap_outputs/
│   │   ├── diabetes_xgb_shap.png
│   │   └── ...
│   └── lime_outputs/
├── 07_xai_output/
│   └── (organized by dataset + model)
├── 08_comparison/
│   ├── results/
│   │   ├── comparison_table.csv
│   │   ├── spearman_results.csv
│   │   └── ...
│   └── figures/
│       ├── heatmap_rank_correlation.png
│       └── ...
├── src/
│   ├── preprocessing.py
│   ├── models.py
│   ├── shap_analysis.py
│   ├── lime_analysis.py
│   └── comparison_metrics.py
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_baseline_models.ipynb
│   ├── 04_ensemble_models.ipynb
│   ├── 05_stacking.ipynb
│   ├── 06_xai_exploration.ipynb
│   └── 08_comparison_analysis.ipynb
├── 09_thesis/
│   ├── Thesis_v1.docx
│   ├── Thesis_v2.docx
│   ├── Thesis_Final.pdf
│   └── figures/
├── 10_paper/
│   ├── IEEE_Access_Paper_v1.pdf
│   ├── response_to_reviewers.pdf
│   └── cover_letter.pdf
├── NOTES.md   ← YOUR PRIVATE THINKING + AI PROMPTS THAT WORKED
├── .gitignore
├── README.md
└── THESIS_ROADMAP.md  ← this file
```

**Setup command (Linux/Windows bash)**:
```bash
mkdir -p 01_proposal 02_literature/notes_per_paper 03_proposal 04_data/{raw,processed,eda_figures} 05_models/saved_models 06_xai_exploration/{shap_outputs,lime_outputs} 07_xai_output 08_comparison/{results,figures} src notebooks 09_thesis/figures 10_paper
touch NOTES.md README.md .gitignore
```

---

## 7. TOOLS, LIBRARIES & STACK

### 🖥️ Hardware
| Resource | Specs |
|---|---|
| Local PC | 8 GB RAM, no GPU |
| Google Colab | Free tier — T4 GPU (sufficient for tabular) |
| Kaggle | 30 hrs/week free GPU |

### 🐍 Python Environment
| Tool | Version | Use |
|---|---|---|
| Python | 3.10+ | Language |
| Anaconda | Latest | Package manager (easier than pip for beginners) |
| Jupyter Notebook | Latest | Interactive dev |
| VSCode | Latest | Code editing |

### 📦 Python Libraries (install everything in Week 1)
```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost lightgbm shap lime optuna joblib scipy statsmodels
```
| Library | Purpose |
|---|---|
| numpy, pandas | Data manipulation |
| matplotlib, seaborn | Visualization |
| scikit-learn | ML models, preprocessing, metrics |
| xgboost | Gradient boosting |
| lightgbm | Fast gradient boosting |
| shap | SHAP explanations |
| lime | LIME explanations |
| optuna | Hyperparameter tuning (optional, GridSearchCV also fine) |
| joblib | Save/load models |
| scipy, statsmodels | Statistical tests (Wilcoxon, Spearman) |

### 📚 Writing & Management
| Tool | Purpose |
|---|---|
| **Overleaf** | LaTeX (paper writing) |
| **Zotero + BetterBibTeX** | Reference management |
| **Notion OR Excel** | Lit matrix + weekly tracker |
| **Git + GitHub** | Version control (MANDATORY) |
| **Google Drive** | Backup (MANDATORY — save everything here too) |

### 🤖 AI Subscriptions
| Tool | Use |
|---|---|
| Claude (Opus 4.8 / Sonnet 4.5) | Code review, lit review summaries, writing edits |
| GPT-4 / GPT-5 class | Code generation, latex help |
| GitHub Copilot | In-editor autocomplete |

---

## 8. AI USAGE GUIDE PER STEP

> **🚨 Critical Rule**: AI is your **assistant**, NOT your **author**. Every output must be reviewed, verified, and reworded. Submitting AI-generated text verbatim = plagiarism + may violate journal policy.

---

### 🤖 AI Strategy Summary

| Phase | AI Role | What AI Does | What YOU Do |
|---|---|---|---|
| 0. Setup | Coder | Generate folder commands | Run them, verify |
| 1. RQs | Editor | Suggest RQ formats, identify gaps | Decide which to use |
| 2. Lit Review | **Researcher** | Summarize papers, find connections | Read papers, validate facts |
| 3. Proposal | **Writer + Editor** | Draft sections, suggest arguments | Verify claims, restructure |
| 4. EDA | Coder | Generate plots code | Interpret, write insights |
| 5. Preprocessing | Coder | Write preprocessing functions | Validate output, debug |
| 6. Models | Coder + Tuner | Suggest hyperparameters | Validate results, run experiments |
| 7. XAI | Coder + Explainer | Generate SHAP/LIME code | Interpret plots, select cases |
| 8. Comparison | Analyst | Suggest metrics, run statistics | Design metrics, interpret tests |
| 9. Thesis | Writer + Editor | Polish prose, fix grammar | Write first draft, decide structure |
| 10. Paper | Writer | Condense, reformat | Restructure per journal template |
| 11. Revision | Editor | Draft reviewer responses | Decide what to change |

---

### 🔑 Specific AI Prompts per Phase

#### Phase 0: Setup
```
"Generate a bash script that creates the complete folder structure for a machine learning thesis with these folders: 01_proposal, 02_literature, 04_data/raw, etc."
```
Then verify each folder exists.

#### Phase 1: Scope Lock
```
"Generate 5 research questions comparing SHAP and LIME on ensemble machine learning models using disease datasets as benchmarks. Each RQ should be testable, specific, and aligned with quantitative comparison metrics."
```
Take the AI's RQs as drafts, rewrite them in YOUR voice.

#### Phase 2: Literature Review
**Prompt for paper summary:**
```
"Read the following paper abstract + conclusion and produce a structured summary in this format:
- Problem addressed
- Methods used
- Dataset(s)
- Key findings
- Limitations
- Relevance to studying SHAP vs LIME on ensemble models"
[Paste abstract + conclusion]
```
Save each summary in `02_literature/notes_per_paper/paper_XX.md`.

**Prompt for research gap:**
```
"Based on these 20 paper summaries, identify what is NOT being studied. Focus on: SHAP vs LIME comparisons, ensemble model explanations, multi-dataset validation, quantitative interpretability metrics. Output a 3-sentence research gap statement."
```

#### Phase 3: Proposal
**Prompt for introduction:**
```
"Write a 400-word introduction for a thesis titled 'Comparative Interpretability Analysis of Ensemble Machine Learning Models Using SHAP and LIME'. Structure: (1) ML in healthcare context, (2) ensemble model accuracy + black-box problem, (3) XAI tools SHAP and LIME, (4) gap in quantitative comparison, (5) our contribution. Academic tone, no hype."
```

**Prompt for self-critique:**
```
"Critique this proposal section for: logical flow, missing citations, unsupported claims, weak problem statement. Output as a numbered list."
```

#### Phase 4: EDA
**Prompt for EDA code:**
```
"Generate Python code using pandas, matplotlib, seaborn to perform EDA on the PIMA diabetes dataset. Include: shape, dtype, missing values heatmap, class balance, histograms, correlation heatmap, boxplots for outliers. Add comments explaining each step."
```

#### Phase 5: Preprocessing
**Prompt for pipeline:**
```
"Write a Python function preprocess(df, target_col) that:
- Imputes missing numeric values with median, categorical with mode
- Encodes categoricals with LabelEncoder + OneHot for >2 categories
- Scales numerics with StandardScaler
- Returns X_train, X_test, y_train, y_test (80/20 stratified split, random_state=42)
Include docstrings and type hints."
```

#### Phase 6: Models
**Prompt for ensemble model:**
```
"Write a function train_xgboost(X_train, y_train, X_test, y_test) that:
- Defines a small hyperparameter grid (max_depth: [3,5,7], n_estimators: [100,200], learning_rate: [0.01,0.1])
- Uses GridSearchCV with 5-fold stratified CV
- Returns the fitted best model, predictions, and a metrics dict {accuracy, precision, recall, f1, auc_roc}
- Saves the model to disk using joblib"
```

#### Phase 7: XAI
**Prompt for SHAP:**
```
"Generate Python code using shap library to explain an XGBoost model on the PIMA diabetes dataset:
- Use TreeExplainer
- Generate: summary_plot, bar_plot, force_plot for a single instance where model predicts class 1
- Save all plots as PNG to figures/ folder
- Include commentary on how to interpret each plot"
```

**Prompt for LIME:**
```
"Generate Python code using lime library to explain XGBoost predictions on PIMA diabetes:
- Use LimeTabularExplainer with feature_names and class_names
- Explain 5 sample instances (3 class=1, 2 class=0)
- Generate explanation.html + explanation.png
- Save outputs"
```

#### Phase 8: Comparison Metrics
**Prompt for novel metric design:**
```
"Design 5 quantitative metrics to compare SHAP and LIME explanations on a trained ensemble classifier. For each metric: name, formula, interpretation, when to use, expected range. Metrics must be reproducible and not require domain expertise."
```

**Prompt for statistical test:**
```
"Write code to compute Spearman rank correlation between SHAP and LIME feature importances for each model × dataset pair. Then run Wilcoxon signed-rank test comparing SHAP-vs-LIME correlation coefficients across all pairs. Save p-values and effect sizes."
```

#### Phase 9: Thesis Writing
**Prompt for chapter rewrite:**
```
"Rewrite this Methods section paragraph (provided below) to:
- Use formal academic tone
- Be 30% more concise
- Add transitions between sentences
- Ensure passive voice where appropriate
- Output ONLY the rewritten version, no commentary"
[Paste paragraph]
```

**Prompt for figure caption:**
```
"Write a publication-quality figure caption for a heatmap showing Spearman rank correlation between SHAP and LIME feature rankings across 5 models and 3 datasets. Caption should be 3-4 sentences, self-explanatory, cite the figure number."
```

#### Phase 10: Paper
**Prompt for journal adaptation:**
```
"Convert this 30-page thesis Methodology chapter into a 3-page Methodology section for a journal paper in IEEE Access format. Keep all equations, compress examples, remove background explanations. Output as a single Word-ready document with section headings."
```

#### Phase 11: Reviewer Response
**Prompt for response drafting:**
```
"Reviewer 2 comment: [paste comment]
Original paper text: [paste excerpt]
Write a respectful, technically rigorous 200-word response that:
- Thanks reviewer
- Acknowledges the concern
- Explains what we did/didn't do and why
- Describes the change made in the revision
- Cites new figure/equation if added"
```

---

### ⚠️ AI Usage DO's and DON'Ts

**DO** ✅
- Use AI to generate first drafts
- Use AI to explain unfamiliar code/concepts
- Use AI to find errors in your code/logic
- Use AI to summarize long papers
- Use AI to improve writing flow
- Use AI to format references

**DON'T** ❌
- Submit AI text verbatim (plagiarism)
- Use AI for medical/clinical claims (always verify with primary source)
- Use AI to fabricate citations (it hallucinates papers)
- Skip understanding AI-generated code
- Use AI to bypass learning (this thesis IS your learning)
- Trust AI math/facts without verification

---

## 9. RESOURCES & DIRECT LINKS

### 📊 Datasets

| Dataset | Link | Notes |
|---|---|---|
| PIMA Indians Diabetes | `https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database` | Mirror also at UCI |
| Heart Disease UCI | `https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset` | `heart.csv` by ronit |
| Chronic Kidney Disease | `https://www.kaggle.com/datasets/mansoordaku/ckdisease` | Mixed types |
| UCI Repository (all) | `https://archive.ics.uci.edu/ml/datasets.php` | Backup source |

### 📚 Papers Search Engines

| Engine | Link | Access |
|---|---|---|
| Google Scholar | `https://scholar.google.com` | Free |
| Semantic Scholar | `https://www.semanticscholar.org` | Free, AI-powered |
| Connected Papers | `https://www.connectedpapers.com` | Free (visual citation graph) |
| IEEE Xplore | `https://ieeexplore.ieee.org` | University login |
| Springer | `https://link.springer.com` | University login |
| Elsevier ScienceDirect | `https://www.sciencedirect.com` | University login |
| ArXiv | `https://arxiv.org` | Preprints |

### 🛠️ Tools

| Tool | Link | Purpose |
|---|---|---|
| Google Colab | `https://colab.research.google.com` | GPU/TPU compute |
| Kaggle Notebooks | `https://www.kaggle.com/code` | Free GPU |
| Overleaf | `https://www.overleaf.com` | LaTeX editor |
| Zotero | `https://www.zotero.org` | Reference manager |
| GitHub | `https://github.com` | Code version control |
| GitHub Desktop | `https://desktop.github.com` | GUI Git client |
| Anaconda | `https://www.anaconda.com/download` | Python distribution |

### 📺 Tutorials & Docs

| Topic | Resource | Link |
|---|---|---|
| SHAP | Official docs | `https://shap.readthedocs.io/en/latest/` |
| LIME | Official docs | `https://lime-ml.readthedocs.io/en/latest/` |
| XGBoost | Official docs | `https://xgboost.readthedocs.io` |
| LightGBM | Official docs | `https://lightgbm.readthedocs.io` |
| scikit-learn | Official tutorials | `https://scikit-learn.org/stable/tutorial/` |
| Ensemble Methods | StatQuest YouTube | `https://www.youtube.com/c/joshstarmer` |
| Writing papers | "How to Write a Thesis" by Umberto Eco | Free PDF online |
| LaTeX | Overleaf docs | `https://www.overleaf.com/learn` |

### 🎯 Key Papers to Start With (read these FIRST)

1. **Lundberg & Lee (2017)** — "A Unified Approach to Interpreting Model Predictions" — SHAP paper
2. **Ribeiro et al. (2016)** — "Why Should I Trust You?" — LIME paper
3. **Dietterich (2000)** — "Ensemble Methods in Machine Learning" — foundational
4. **Wolpert (1992)** — "Stacked Generalization" — stacking original

Find these on Google Scholar.

### 🤖 AI Subscriptions You Mentioned
- Use Claude / GPT for code review, writing edits, paper summaries
- You already have these — leverage them throughout

---

## 10. KEY DELIVERABLES TRACKER

| # | Deliverable | File Path | Target Date |
|---|---|---|---|
| 1 | Workspace folders created | `./` | Week 1 |
| 2 | RQ scope document | `01_proposal/rq_scope.md` | Week 2 |
| 3 | Lit matrix populated | `02_literature/literature_matrix.xlsx` | Week 4 |
| 4 | Proposal defended | `01_proposal/Final_Proposal.pdf` | Week 5 |
| 5 | EDA report | `04_data/EDA_REPORT.md` | Week 6 |
| 6 | Preprocessing done | `04_data/processed/*.csv` | Week 7 |
| 7 | All models trained | `05_models/results.csv` | Week 9 |
| 8 | SHAP plots generated | `06_xai_exploration/shap_outputs/` | Week 10 |
| 9 | LIME plots generated | `06_xai_exploration/lime_outputs/` | Week 10 |
| 10 | Comparison metrics done | `08_comparison/results/comparison_table.csv` | Week 11 |
| 11 | Thesis chapters drafted | `09_thesis/Thesis_v1.docx` | Week 13-14 |
| 12 | Plagiarism-checked thesis | `09_thesis/Thesis_Final.pdf` | Week 15 |
| 13 | Defense slides | `01_proposal/proposal_slides.pptx` (modified) | Week 15 |
| 14 | Journal paper submitted | `10_paper/IEEE_Access_Paper_v1.pdf` | Week 16 |
| 15 | Thesis defended | Confirmation email | Week 16 |
| 16 | Paper accepted | Journal email | Week 20-24 |

---

## 11. RISK REGISTER & MITIGATION

| # | Risk | Probability | Impact | Mitigation |
|---|---|---|---|---|
| 1 | Colab free tier disconnects mid-training | High | Low | Use Kaggle as backup; save checkpoints |
| 2 | PC (8 GB RAM) crashes on full dataset | Medium | Medium | Process in chunks; use Colab for heavy work |
| 3 | Plagiarism detected on AI-generated text | Medium | High | Always paraphrase, cite sources, manual rewrite |
| 4 | Advisor delays feedback | Medium | Medium | Send draft 3 days BEFORE meeting; polite reminder |
| 5 | Dataset imbalance causes model bias | Medium | Medium | Use SMOTE or class weights; report stratified metrics |
| 6 | SHAP times out on large model | Medium | Medium | Use TreeSHAP for tree models, sample subset for KernelSHAP |
| 7 | LIME explanations look inconsistent | High | Medium | This IS a finding — report as instability metric |
| 8 | Journal desk rejection | Medium | High | Read scope carefully; have 2 backup journals ready |
| 9 | Code lost (no backup) | Low | Critical | Git + GitHub + Google Drive — MANDATORY |
| 10 | Got stuck >2 days on bug | Medium | Medium | Use AI to debug; post on StackOverflow; ask advisor |

---

## 12. GLOSSARY OF TERMS

| Term | Definition |
|---|---|
| **XAI** | Explainable AI — methods to make ML decisions interpretable |
| **SHAP** | SHapley Additive exPlanations — game-theory-based feature attribution |
| **LIME** | Local Interpretable Model-agnostic Explanations — local surrogate model |
| **Ensemble** | Combining multiple models for better predictions |
| **Stacking** | Ensemble using a meta-learner over base learners |
| **Random Forest** | Bagging ensemble of decision trees |
| **XGBoost** | Extreme Gradient Boosting — sequential boosting ensemble |
| **LightGBM** | Light Gradient Boosting Machine — faster boosting variant |
| **TreeSHAP** | Fast SHAP implementation for tree models |
| **KernelSHAP** | Model-agnostic SHAP using weighted linear regression |
| **Fidelity** | How faithfully the explanation represents the model |
| **Stability** | How similar explanations are for similar inputs |
| **Spearman ρ** | Rank correlation coefficient |
| **Kendall τ** | Alternative rank correlation |
| **AUC-ROC** | Area Under ROC Curve — classification metric |
| **Stratified split** | Train/test split preserving class proportions |
| **EDA** | Exploratory Data Analysis |
| **APC** | Article Processing Charge (journal publication fee) |
| **Plagiarism** | Using others' work without attribution |

---

## 📌 NEXT IMMEDIATE STEPS (Do Today)

1. ✅ Create folder structure (copy command from Section 6)
2. ✅ Initialize Git repo (`git init` in workspace)
3. ✅ Install Python libraries listed in Section 7
4. ✅ Run "Hello SHAP" Colab test
5. ✅ Download all 3 datasets to `04_data/raw/`
6. ✅ Download 5 seed papers from Google Scholar
7. ✅ Start literature matrix Excel
8. ✅ Write your first entry in `NOTES.md`

---

## 🧭 REMINDERS

> **Remember**: This roadmap is a **living document**. Update it as you go. Cross out completed tasks. Add new ones you discover. The roadmap is **your accountability partner**.

> **When in doubt**: Ask your advisor first, then check this roadmap, then ask AI.

> **You are NOT alone in this journey**: I (the AI assistant) am here to help — paste any error, paste any draft, ask any question. We will finish this together.

---

## 📝 CHANGE LOG

| Date | Change | Author |
|---|---|---|
| 2026-07-06 | Initial roadmap created | MD. Marajul Haque + AI Assistant |

---

**🚀 Ready to start with Phase 0? Tell me which task from Section 6 / 7 / 9 you want help with first, and we'll build it together.**
