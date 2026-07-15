# 📘 PHASE 1 — Topic Finalization & Scope Lock (Detailed)

> **Phase Goal**: Lock the thesis scope — Research Questions, Hypothesis statements, datasets, models, metrics — BEFORE any code is written for EDA, modeling, or XAI. A thesis that drifts in scope after Phase 4 wastes weeks.

> **Time Estimate**: 3-5 days (across Week 1-2 of your timeline; designed for 1 advisor meeting)

> **Exit Criteria**: Your advisor (Prof.) has approved — verbally or via email — these five things: **(a)** 5 Research Questions, **(b)** Hypothesis statements, **(c)** datasets list, **(d)** model list, **(e)** evaluation metric list. Everything in Phases 2-11 derives from this lock.

---

## 📑 STEP INDEX

| Step | Title | Time |
|---|---|---|
| 1.1 | Review what's already locked from Phase 0 | 10 min |
| 1.2 | Read the standardized prompt and generate 5 RQ drafts | 30 min |
| 1.3 | Critique RQs against SMART criteria; rewrite in your voice | 45 min |
| 1.4 | Write 5 Hypothesis statements (H1-H5) that match RQs | 45 min |
| 1.5 | Lock the dataset list (3 datasets: PIMA / Heart / CKD) | 20 min |
| 1.6 | Lock the model list (5 models: LR / DT / RF / XGB / LGBM / Stacking) | 20 min |
| 1.7 | Lock the metric list (8 metrics: 5 performance + 5 interpretability) | 30 min |
| 1.8 | Build the Scope Lock document (`01_proposal/rq_scope.md`) | 60 min |
| 1.9 | Prepare advisor-meeting agenda + slides | 60 min |
| 1.10 | Run the advisor meeting; capture outcomes | 60 min (meeting) + 30 min (notes) |
| 1.11 | Update AGENT.md + commit Phase 1 to git | 15 min |

**Total time**: ~7-9 hours of focused work (plus the meeting itself).

---

## 🧭 STEP 1.1 — Review What's Already Locked from Phase 0

### 🎯 What we want to achieve
Before writing new scope items, **confirm** what is already locked from Phase 0 so we don't re-open solved decisions.

### 🤖 What AI will do
- Read `AGENT.md` §1-7 (your profile, datasets chosen, etc.)
- Read `THESIS_ROADMAP.md` §4 Phase 1 section (lines 153-175)
- Output a short list of "**already locked**" vs "**needs decision**" items

### 👤 What YOU will do
1. Open `AGENT.md` and skim sections §3 (Locked Datasets), §11 (Decisions Log).
2. Compare with the table below; mark any disagreement to the AI.

### ✅ Already locked from Phase 0 (do NOT re-decide)
| Item | Decision |
|---|---|
| Datasets | PIMA Diabetes + Heart Disease + CKD (3 tabular medical datasets) |
| Models baseline | Logistic Regression + Decision Tree (single-model baselines) |
| Models main | Random Forest + XGBoost + LightGBM + Stacking Ensemble |
| XAI methods | SHAP (TreeExplainer for tree models) + LIME (LimeTabularExplainer) |
| Comparison axes | 5 axes — agreement, stability, fidelity, runtime, medical-domain validity |
| Citation manager | Zotero + Better BibTeX |
| Notebook platform | VS Code + .venv (local); Colab reserved for GPU-heavy experiments |
| Drive backup target | `gdrive-thesis:` remote (your `marajul.cu@gmail.com`) |

### 🚨 Troubleshooting
- If `AGENT.md` says something different (e.g., 4 datasets instead of 3), stop and clarify with the AI before proceeding.
- Do NOT add a 4th dataset during Phase 1 — that breaks the timeline.

---

## 🧭 STEP 1.2 — Generate 5 Research Question Drafts (AI-Assisted)

### 🎯 What we want to achieve
Use the standardized Phase 1 prompt from `THESIS_ROADMAP.md` line 731 to get **AI-drafted** RQs. You will rewrite them in your own voice in Step 1.3 — AI drafts are scaffolding, not final copy.

### 🤖 What AI will do
1. Read the standardized prompt:
   > *"Generate 5 research questions comparing SHAP and LIME on ensemble machine learning models using disease datasets as benchmarks. Each RQ should be testable, specific, and aligned with quantitative comparison metrics."*
2. Read `THESIS_ROADMAP.md` §4 Phase 1 lines 158-163 (the 5 seed RQs already in the roadmap).
3. Output a numbered list of **5 RQ candidates** (drafts), each tagged with:
   - "Test type" (statistical test: e.g., paired Wilcoxon, Spearman correlation, ANCOVA)
   - "Mapped metric" (which of the 8 metrics answers this)
   - "Dataset scope" (all 3 datasets? single dataset?)
4. Suggest **3 alternative RQs** in case you want to swap any.

### 👤 What YOU will do
1. Copy this prompt into a fresh AI chat OR ask the AI in this chat:
   ```
   Use the standardized Phase 1 prompt from THESIS_ROADMAP.md line 731.
   Read THESIS_ROADMAP.md §4 Phase 1 (lines 153-175).
   Output 5 RQ drafts + 3 alternatives with the metadata I described.
   ```
2. Save the drafts to a scratch file `01_proposal/rq_drafts_raw.md` (temporary; will be deleted in Step 1.8).

### ✅ Success criteria
- [ ] 5 RQ drafts exist in `rq_drafts_raw.md`
- [ ] Each draft has its test type + mapped metric + dataset scope tagged
- [ ] 3 alternative RQs included for optional swap
- [ ] No RQ says "investigate" or "explore the role of" — those are too vague

### 🚨 Troubleshooting
| Problem | Fix |
|---|---|
| AI suggests 7+ RQs | Cut to 5; advisor-meeting agendas get bloated with too many questions |
| AI mixes qualitative & quantitative RQs | Drop qualitative ones — your thesis is quantitative only |
| AI RQs depend on data not yet collected | Reject — only use RQs that map to the 3 locked datasets |
| AI RQs say "user study" or "interview" | Reject — your thesis does NO user studies (time-constrained BSc) |

### ⏱️ Time: 30 min

---

## 🧭 STEP 1.3 — Critique RQs Against SMART Criteria; Rewrite in Your Voice

### 🎯 What we want to achieve
Turn AI-drafted RQs into **your own research questions** — phrased in your academic voice, SMART-compliant, and aligned with the locked scope.

### 🤖 What AI will do
- Provide a **SMART rubric** checklist for each RQ
- Suggest rewording for any RQ that fails the rubric
- Provide a "before/after" example using the roadmap's seed RQs as the starting point

### 👤 What YOU will do

#### SMART Rubric for each RQ
For each of your 5 RQs, you must answer YES to all 5:

| Letter | Criterion | Example of failure |
|---|---|---|
| **S** | **Specific** — names the method(s), dataset class, and metric class | ❌ "How do SHAP and LIME compare?" |
| **M** | **Measurable** — result is a number (ρ, τ, sec, %) | ❌ "Do they feel different?" |
| **A** | **Achievable** — testable with 3 datasets, 5 models, 8 metrics in 12 weeks | ❌ "Across all medical domains globally?" |
| **R** | **Relevant** — answers an interpretability question, not just an accuracy one | ❌ "Which model is most accurate?" |
| **T** | **Time-bound** — can be answered in Phase 7-8 timeframe (week 6-10) | ❌ "Over the next 5 years?" |

#### Starting point — the 5 RQs from THESIS_ROADMAP.md (rewrite these, don't copy verbatim)

The roadmap already gives you 5 seed RQs. **Use them as the baseline** — rewrite each in your own words:

| # | Seed RQ from roadmap | Pass SMART? |
|---|---|---|
| RQ1 | How consistent are SHAP and LIME feature rankings when applied to ensemble models trained on the same dataset? | Yes (Spearman ρ between SHAP and LIME rankings) |
| RQ2 | Does explanation stability (across similar patients) differ between SHAP and LIME? | Yes (variance of attributions across k-NN neighbors) |
| RQ3 | How does explanation fidelity (model-faithfulness) compare between SHAP and LIME on tree-based ensembles? | Yes (delete-and-predict correlation) |
| RQ4 | What is the computational trade-off between SHAP and LIME explanations across ensemble architectures? | Yes (sec/explanation) |
| RQ5 | Do SHAP and LIME identifications of "important features" agree with established medical risk factors in the literature? | Yes (overlap with published risk-factor list) |

#### Rewrite example

**AI draft** (too vague):
> *"RQ1: How well do SHAP and LIME explanations agree when applied to ensemble models on medical datasets?"*

**Your rewrite** (SMART, your voice):
> *"RQ1 — Agreement: To what extent do global feature-importance rankings produced by SHAP (TreeExplainer) and LIME (LimeTabularExplainer) agree when applied to Random Forest, XGBoost, and LightGBM models trained on PIMA Diabetes, Heart Disease, and CKD datasets, as quantified by Spearman rank correlation coefficient (ρ)?"*

The rewrite adds:
- The exact methods (TreeExplainer, LimeTabularExplainer)
- The exact models in scope (RF, XGB, LGBM — not DT/LR baselines)
- The exact datasets (PIMA, Heart, CKD)
- The exact metric (Spearman ρ)

### ✅ Success criteria
- [ ] All 5 RQs rewritten in `01_proposal/rq_scope.md` §1
- [ ] Every RQ passes all 5 SMART checks (you can mark ✔ in the rubric table)
- [ ] Each RQ explicitly names: methods × models × datasets × metric
- [ ] At most 5 RQs (no scope creep)

### 🚨 Troubleshooting
- If you write an RQ that mentions "user perception" or "expert review" — remove it; this is a quantitative BSc thesis.
- If two RQs are nearly identical (e.g., both about agreement), merge them — you want diversity, not duplication.

### ⏱️ Time: 45 min

---

## 🧭 STEP 1.4 — Write 5 Hypothesis Statements (H1-H5) Matching RQs

### 🎯 What we want to achieve
Translate each RQ into a **falsifiable hypothesis** with a stated statistical test. Hypotheses are how you write the "answer" to the RQ; they make Phase 8 (the comparison phase) mechanical, not improvised.

### 🤖 What AI will do
- Provide a hypothesis template per RQ
- Identify the correct statistical test for each H
- Provide a sample calculation / G*Power reference for effect size

### 👤 What YOU will do

#### Hypothesis template (one per RQ)

For each RQ, write **H0 (null)** and **H1 (alternative)**:

```
Hypothesis [H#]:
  H0: There is no significant difference between [SHAP metric] and [LIME metric]
      for [model list] trained on [dataset list], as measured by [test].
  H1: [SHAP metric] is [greater/less/different] than [LIME metric]
      for [model list] trained on [dataset list], as measured by [test]
      (α = 0.05).
```

#### Example for RQ1 (Agreement)

> **H1 — Agreement hypothesis:**
> *H0*: Spearman rank correlation between SHAP and LIME global feature-importance rankings does not differ significantly from 0.5 (moderate agreement).
> *H1*: Spearman rank correlation between SHAP and LIME rankings is significantly greater than 0.5 for ensemble models (RF, XGB, LGBM) across PIMA, Heart, and CKD datasets.
> *Test*: One-sample Wilcoxon signed-rank test on the 9 (3 models × 3 datasets) ρ values, against μ0 = 0.5, α = 0.05.

#### Statistical tests cheat-sheet

| RQ axis | Recommended test | Why |
|---|---|---|
| RQ1 — Agreement | Spearman ρ + Wilcoxon signed-rank | Rank-based, paired (SHAP & LIME on same data) |
| RQ2 — Stability | Variance ratio (F-test) or Levene's test | Compare spread across re-runs |
| RQ3 — Fidelity | Pearson r on delete-and-predict, paired t-test | Both distributions normal-ish |
| RQ4 — Runtime | Wilcoxon rank-sum (Mann-Whitney U) on times | Runtime is skewed |
| RQ5 — Medical-domain validity | Overlap coefficient + Fisher's exact test | Categorical "in literature" set membership |

#### H1 must be the version you are TRYING to confirm — it has a direction. H0 is "no difference."

| ❌ Bad (no direction) | ✅ Good (directional) |
|---|---|
| H1: SHAP and LIME differ in runtime | H1: SHAP runtime is **greater than** LIME runtime on tree ensembles |

### ✅ Success criteria
- [ ] 5 hypotheses in `01_proposal/rq_scope.md` §2
- [ ] Each H has H0 + H1
- [ ] Each H names the correct statistical test
- [ ] Significance level α = 0.05 is stated
- [ ] Direction is stated in H1 (>, <, ≠)

### 🚨 Troubleshooting
- If your H just restates the RQ as a yes/no, add the testable prediction (which one is bigger).
- If you forgot the test name — write "?" and ask the AI; do NOT leave it blank.
- If α is anything other than 0.05 — justify in a footnote (p < 0.01 for stricter comparisons).

### ⏱️ Time: 45 min

---

## 🧭 STEP 1.5 — Lock the Dataset List (PIMA / Heart / CKD)

### 🎯 What we want to achieve
Document the **final dataset choice** with: name, source URL, sample size, feature count, target column, license, ethics approval note. This locks Phase 4 (EDA) and Phase 5 (preprocessing).

### 🤖 What AI will do
- Read `AGENT.md` §3 (Datasets already chosen)
- Generate the canonical dataset table with 9 fields per dataset
- Provide Kaggle/UCI download commands

### 👤 What YOU will do

#### Dataset table to fill in

| Field | PIMA Diabetes | Heart Disease | CKD (Chronic Kidney Disease) |
|---|---|---|---|
| Source | UCI / Kaggle | UCI / Kaggle | UCI |
| URL | *paste* | *paste* | *paste* |
| Rows (n) | 768 | 303 | 400 |
| Features | 8 | 13 | 24 |
| Target column | `Outcome` | `target` (0/1) | `classification` (ckd/notckd) |
| Class balance | 500/268 (neg/pos) | 138/165 | 250/150 |
| Missing values? | No (but has zeros coded as "missing") | Yes (small) | Yes (many `?` strings) |
| License | CC0 / Public Domain | CC0 | CC0 |
| Why this dataset | Most-cited medical dataset | Balanced binary | Tests missing-value handling |

#### Why these 3?
1. **PIMA** — diabetes — most-cited medical ML dataset → results comparable to 1000s of papers
2. **Heart** — UCI Cleveland — classic benchmark, small enough to inspect row-by-row
3. **CKD** — has many missing values → tests robustness of preprocessing pipeline

This 3-dataset mix gives you: (a) a well-known benchmark, (b) a small/clean dataset, (c) a dataset with messy data.

#### Download commands (run later in Phase 4)

```bash
# PIMA from Kaggle (after API token configured in Phase 0 step 0.7):
kaggle datasets download -d uciml/pima-indians-diabetes-database -p 04_data/raw/

# Heart from UCI:
curl -L -o 04_data/raw/heart.csv "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

# CKD from UCI:
curl -L -o 04_data/raw/kidney_disease.csv "https://archive.ics.uci.edu/ml/machine-learning-databases/00272/Chronic_Kidney_Disease.rar"
# Need unrar or 7z to extract the .rar
```

### ✅ Success criteria
- [ ] Table complete with all 9 fields × 3 datasets in `rq_scope.md` §3
- [ ] Every dataset has source URL pasted
- [ ] Sample sizes add up to ~1500 (rough mental check for "3 modest datasets")

### 🚨 Troubleshooting
- **CKD has `?` strings instead of NaN** — note this in the "Missing values" row; Phase 5 must handle it.
- **License unclear** — default to "CC0 / Public Domain" if UCI-hosted; both are CC0 for our purposes.
- **Heart Disease has multiple versions** (Cleveland, Hungary, Switzerland, VA) — use **Cleveland only**.

### ⏱️ Time: 20 min

---

## 🧭 STEP 1.6 — Lock the Model List (5 Models + 2 Baselines)

### 🎯 What we want to achieve
Document the **final model list** — 1 baseline linear (LR), 1 baseline tree (DT), 3 main ensemble methods (RF, XGB, LGBM), and 1 stacking meta-learner. Each model has a reason.

### 🤖 What AI will do
- Generate the canonical model table
- Explain why this 5+1 model choice is the **right** scope for a BSc thesis (vs other choices)
- Suggest 1 alternate (e.g., CatBoost) ONLY IF you have time to spare

### 👤 What YOU will do

#### Final model table

| # | Model | Type | Role in thesis | Hyperparams to tune (Phase 6) |
|---|---|---|---|---|
| 1 | Logistic Regression | Linear baseline | "Before deep ensembles" — sets floor | `C` ∈ {0.01, 0.1, 1, 10}, `solver='liblinear'` |
| 2 | Decision Tree | Tree baseline | "Before ensembles of trees" — sets floor | `max_depth` ∈ {3, 5, 10, None} |
| 3 | Random Forest | Bagging ensemble | First ensemble method | `n_estimators=300`, `max_depth` ∈ {None, 10, 20} |
| 4 | XGBoost | Boosting ensemble | Most-cited gradient boosting library | `n_estimators=300`, `learning_rate=0.05`, `max_depth` ∈ {3, 5, 7} |
| 5 | LightGBM | Boosting ensemble | Faster XGBoost alternative | `n_estimators=300`, `learning_rate=0.05`, `num_leaves` ∈ {15, 31, 63} |
| 6 | Stacking (LR meta) | Meta-ensemble | Combines RF + XGB + LGBM | `final_estimator = LogisticRegression` |

#### Why this list?

- **LR** — baseline linear; XAI explanations are easy (coefficients) → useful for sanity-checking SHAP/LIME outputs.
- **DT** — baseline tree; gives interpretable tree (high fidelity with no XAI needed) → reference ceiling.
- **RF** — most popular bagging ensemble; SHAP has a fast TreeExplainer for it.
- **XGB** — most-cited gradient boosting; consistent baseline across literature.
- **LGBM** — modern fast LightGBM; slightly different tree structure than XGB → useful for "does the XAI tool generalize across boosting variants?"
- **Stacking** — demonstrates XAI on a meta-learner (rare in literature).

> ⚠️ **Critical constraint**: SHAP TreeExplainer only works with tree models. For LR (linear) we use SHAP `LinearExplainer`. For non-tree ensembles (any future ones), SHAP `KernelExplainer`. Phase 7 will codify this.

### ✅ Success criteria
- [ ] Table complete in `rq_scope.md` §4
- [ ] Reasoning column filled for each model
- [ ] 6 models total (not 5, not 7)
- [ ] Stacking uses **LR as meta-learner** (proven in literature; not exotic)

### 🚨 Troubleshooting
- If advisor asks "why not CatBoost?" — answer: scope is already 6 models; CatBoost is 1 more dataset prep pipeline to maintain.
- If advisor wants to **add** a model — defer to a follow-up thesis; this BSc thesis has time for 6 only.

### ⏱️ Time: 20 min

---

## 🧭 STEP 1.7 — Lock the Metric List (8 Metrics: 5 Performance + 5 Interpretability)

### 🎯 What we want to achieve
Lock the **two categories** of metrics you'll report in Phase 8 (Comparison):
1. **Performance metrics** (5) — does each model perform?
2. **Interpretability metrics** (5) — do SHAP/LIME perform as explanations?

This separation is essential — your thesis is about INTERPRETABILITY quality, not raw accuracy.

### 🤖 What AI will do
- Provide the canonical metric tables below
- Map each metric to which RQ / hypothesis it answers
- Provide the Python function name / library for each metric

### 👤 What YOU will do

#### Performance metrics (5)

| # | Metric | What it tells you | Library / Function | Used for which RQ |
|---|---|---|---|---|
| 1 | Accuracy | Fraction correct | `sklearn.metrics.accuracy_score` | Context only — not primary |
| 2 | Precision | Of those predicted pos, how many truly pos? | `sklearn.metrics.precision_score` | Context only |
| 3 | Recall (Sensitivity) | Of truly pos, how many caught? | `sklearn.metrics.recall_score` | Context only (medical matters most) |
| 4 | F1-Score | Harmonic mean of precision & recall | `sklearn.metrics.f1_score` | Context only |
| 5 | AUC-ROC | Threshold-independent discrimination | `sklearn.metrics.roc_auc_score` | Context only |

> The 5 performance metrics give you a **row in the results table** per (model × dataset). They are NOT the primary comparison axis.

#### Interpretability metrics (5) — these are the primary comparison

| # | Metric | What it tells you | Library / Code | Answers RQ |
|---|---|---|---|---|
| 1 | **Spearman ρ (rho)** | Rank correlation between SHAP and LIME global rankings | `scipy.stats.spearmanr` | RQ1 (Agreement) |
| 2 | **Kendall τ (tau)** | Tied-aware rank correlation; complementary to ρ | `scipy.stats.kendalltau` | RQ1 (Agreement — secondary) |
| 3 | **Stability index** | Std-dev of feature attributions across k runs of LIME (SHAP is deterministic for trees) | custom (var over re-runs) | RQ2 (Stability) |
| 4 | **Fidelity** | After keeping top-k features, does prediction still match? (delete-and-predict) | custom (correlation) | RQ3 (Fidelity) |
| 5 | **Runtime** | Wall-clock seconds per explanation | `time.time()` context manager | RQ4 (Runtime) |
| 6 (bonus) | **Domain-validity overlap** | Jaccard overlap with published risk factors per disease | custom (set overlap) | RQ5 (Medical) |

> Total: **8 metrics** (5 perf + 5 interp = 10; if RQ5 is a domain check you get 6 interp; choose 5 to keep it clean).

#### Reduce to 8 by dropping ONE

**Recommendation**: Drop **Precision** (least informative for imbalanced medical data; recall + AUC cover it). Final list = 4 perf + 5 interp = **9 metrics** maximum.

Or drop **Kendall τ** and keep Spearman ρ only (one rank correlation is enough for RQ1).

Pick one and document the decision in `rq_scope.md` §5.

### ✅ Success criteria
- [ ] Final metric list is **8 metrics** (or fewer)
- [ ] Each metric is mapped to an RQ
- [ ] Library / function name recorded for each
- [ ] Decision documented on which metric to drop

### 🚨 Troubleshooting
| Problem | Fix |
|---|---|
| Advisor wants 12 metrics | Refuse politely — 8 is already a full Phase 8 results table (12 rows × 8 cols) |
| Stability needs re-running LIME 10+ times | That's OK — runtime cost is captured separately in RQ4 |
| Fidelity has multiple definitions | Pick **delete-and-predict** (most cited); drop other variants |

### ⏱️ Time: 30 min

---

## 🧭 STEP 1.8 — Build the Scope Lock Document (`01_proposal/rq_scope.md`)

### 🎯 What we want to achieve
Produce one single document — `01_proposal/rq_scope.md` — that consolidates Steps 1.1-1.7 into a 5-page document ready for advisor review.

### 🤖 What AI will do
- Provide the **template** below for `rq_scope.md`
- Generate a markdown skeleton with all the tables from previous steps
- Save it to `01_proposal/rq_scope.md`

### 👤 What YOU will do

#### Template for `01_proposal/rq_scope.md`

```markdown
# Thesis Scope Lock — RQ / Hypotheses / Datasets / Models / Metrics

> **Status**: DRAFT (awaiting advisor approval)
> **Date**: YYYY-MM-DD
> **Author**: Md Marajul Islam (marajulcsecu)
> **Advisor**: [Prof. name]

---

## 1. Research Questions (5 RQs)

### RQ1 — Agreement
[Your rewritten RQ — full text]

### RQ2 — Stability
[Your rewritten RQ — full text]

### RQ3 — Fidelity
[Your rewritten RQ — full text]

### RQ4 — Runtime
[Your rewritten RQ — full text]

### RQ5 — Medical-domain validity
[Your rewritten RQ — full text]

---

## 2. Hypotheses (H1-H5)

### H1 — Agreement
- **H0**: [...]
- **H1**: [...]
- **Test**: One-sample Wilcoxon signed-rank, α = 0.05

### H2 — Stability
- **H0**: [...]
- **H1**: [...]
- **Test**: [...]

### H3 — Fidelity
- **H0**: [...]
- **H1**: [...]
- **Test**: [...]

### H4 — Runtime
- **H0**: [...]
- **H1**: [...]
- **Test**: [...]

### H5 — Medical-domain validity
- **H0**: [...]
- **H1**: [...]
- **Test**: [...]

---

## 3. Datasets (3)

| Field | PIMA Diabetes | Heart Disease | CKD |
|---|---|---|---|
| Source | ... | ... | ... |
| Rows | ... | ... | ... |
| Features | ... | ... | ... |
| Target | ... | ... | ... |
| License | ... | ... | ... |
| Why | ... | ... | ... |

---

## 4. Models (6)

| # | Model | Type | Role | Hyperparams |
|---|---|---|---|---|
| 1 | LR | Linear baseline | ... | ... |
| 2 | DT | Tree baseline | ... | ... |
| 3 | RF | Bagging | ... | ... |
| 4 | XGB | Boosting | ... | ... |
| 5 | LGBM | Boosting | ... | ... |
| 6 | Stacking(LR) | Meta | ... | ... |

---

## 5. Metrics (8)

### Performance (4)
1. Accuracy
2. Recall (Sensitivity)
3. F1-Score
4. AUC-ROC

[Drop Precision OR Kendall τ — see Step 1.7 decision]

### Interpretability (5)
1. Spearman ρ
2. Stability index
3. Fidelity
4. Runtime
5. Domain-validity overlap (Jaccard)

---

## 6. Sign-off

- [ ] Student: Md Marajul Islam
- [ ] Advisor: [Prof. name] — date: ____

> Once all items are signed (or advisor approval received), this file locks
> the thesis scope. Any deviation requires a NEW scope-lock amendment.
```

#### File creation commands

```bash
cd "/home/marajul/Desktop/ENG 672 Technical Communication and Writing/Thesis_V1"

# Ensure folder exists
mkdir -p 01_proposal

# Write the file (AI generates it from your answered tables)
# After AI generates, manually fill in any [bracketed] items
```

### ✅ Success criteria
- [ ] `01_proposal/rq_scope.md` exists
- [ ] All 6 sections filled (no `[bracketed]` placeholders remaining)
- [ ] Document length: 3-5 pages (printed)
- [ ] Sign-off checklist present at end
- [ ] File committed to git (Step 1.11)

### 🚨 Troubleshooting
- If the markdown table breaks when rendered in VS Code — make sure there is a blank line BEFORE and AFTER each table.
- If you keep editing after creating — that's fine; commit at end of Step 1.11.

### ⏱️ Time: 60 min

---

## 🧭 STEP 1.9 — Prepare Advisor-Meeting Agenda + Slides

### 🎯 What we want to achieve
Walk into the advisor meeting with **3 slides max** and a **1-page agenda** so the advisor can approve in 20 minutes (advisors are busy; less is more).

### 🤖 What AI will do
- Generate the 1-page agenda (5 bullets matching the 5 locked items)
- Provide slide-deck template (3 slides)
- Provide "anticipated advisor pushback" answers (5 most-likely objections)

### 👤 What YOU will do

#### 1-page Agenda (print this)

```
Advisor Meeting Agenda — Phase 1 Scope Lock
==========================================

Date: ____    Time: ____    Location: ____ / Zoom

Goal: Approve 5 items below; total time = 20 min

1. 5 Research Questions   (5 min)
   → Walk through each RQ; ask "any concerns?"

2. 5 Hypotheses           (5 min)
   → Confirm each has H0 + H1 + statistical test named

3. 3 Datasets             (3 min)
   → PIMA, Heart, CKD — confirm scope

4. 6 Models               (3 min)
   → 2 baselines + 3 ensemble + 1 stacking meta — confirm 6-model scope

5. 8 Metrics              (4 min)
   → 4 performance + 5 interpretability — confirm 8-metric scope

Wrap-up:  Email approval by Friday or schedule follow-up meeting.
```

#### 3 Slides (LaTeX Beamer OR PowerPoint OR Google Slides)

| Slide # | Title | Content |
|---|---|---|
| 1 | Thesis Title + 5 RQs | Title; 1 line per RQ |
| 2 | Datasets + Models | 3 datasets table; 6 models table |
| 3 | Metrics + Hypotheses | 8 metrics table; 5 H (H0/H1 only) |

#### Anticipated pushback (read this BEFORE the meeting)

| Likely objection | Your prepared response |
|---|---|
| "Why not deep learning?" | Scope already at 6 models; adding DL means 2 datasets × 2 architectures × 3 XAI tools = 12 more cells. Out of BSc scope. |
| "Why 3 datasets, not 10?" | Statistical validity needs ≥2 datasets for paired tests; 3 provides robustness across dataset sizes (small/medium/large). |
| "Why not include Grad-CAM / Integrated Gradients?" | SHAP and LIME are post-hoc for tabular; Grad-CAM requires images. Out of scope (tabular-only thesis). |
| "5 RQs is too many" | Each RQ maps to one hypothesis = one test cell in results table. 5 RQs × 3 datasets = 15 cells — reasonable. |
| "Why Stacking meta-learner = LR?" | LR is the most-cited meta-learner in stacking literature; it's interpretable too. |

### ✅ Success criteria
- [ ] 1-page agenda printed (or open in browser)
- [ ] 3 slides ready (PDF, PPTX, or Google Slides URL)
- [ ] Pushback answers rehearsed (say them out loud once)

### 🚨 Troubleshooting
- If advisor doesn't have time for a meeting — email the `rq_scope.md` file and request email approval instead. That's an acceptable alternative.
- If advisor wants to **change** a dataset / model — open scope amendment (write a new `rq_scope_v2.md`), do not edit original silently.

### ⏱️ Time: 60 min

---

## 🧭 STEP 1.10 — Run the Advisor Meeting; Capture Outcomes

### 🎯 What we want to achieve
Get **explicit approval** (verbal in meeting, or email reply) on all 5 locked items. Capture outcomes in writing for Phase 2.

### 🤖 What AI will do
- After you return with meeting notes, help rewrite the RQs / H if the advisor requested changes
- Draft the "thanks + summary" follow-up email for you to send

### 👤 What YOU will do

#### During the meeting
- Bring printed agenda + rq_scope.md printout
- Take handwritten notes on a separate sheet (not on the rq_scope.md)
- Don't argue — write down each suggestion even if you disagree

#### Immediately after the meeting (within 1 hour)
1. Write meeting notes to `01_proposal/advisor_meeting_1.md`:
   ```markdown
   # Phase 1 Advisor Meeting Notes

   **Date**: YYYY-MM-DD HH:MM
   **Advisor**: [name]
   **Student**: Md Marajul Islam

   ## Decisions
   - [x] RQs approved as-is / approved with edits: [...]
   - [x] Hypotheses approved as-is / approved with edits: [...]
   - [x] Datasets approved: [...]
   - [x] Models approved: [...]
   - [x] Metrics approved: [...]

   ## Action items
   - [ ] Student: [list any tasks]
   - [ ] Advisor: [list any tasks]

   ## Open questions for next meeting
   1. [...]
   ```

2. Send a thank-you email summarizing:
   ```
   Subject: Phase 1 Scope Lock — Approved? ([date])

   Dear [Prof. last name],

   Thank you for the meeting today. Confirming the locked scope:

   1. RQs — 5 [approved / with edits X / Y]
   2. Hypotheses — 5 [approved / with edit Z]
   3. Datasets — PIMA, Heart, CKD
   4. Models — LR, DT, RF, XGB, LGBM, Stacking(LR)
   5. Metrics — [list of 8]

   Please reply "approved" if this is correct, or let me know of any changes.

   Best,
   Md Marajul Islam
   ```

### ✅ Success criteria
- [ ] Meeting notes saved to `01_proposal/advisor_meeting_1.md`
- [ ] Thank-you email SENT (not just drafted)
- [ ] Advisor reply "approved" OR explicit list of changes
- [ ] rq_scope.md updated to FINAL status (replace "DRAFT" with "LOCKED YYYY-MM-DD" in header)

### 🚨 Troubleshooting
- If advisor doesn't reply within 3 days — send 1 gentle nudge email.
- If advisor wants major scope change (e.g., new dataset) — write a 1-paragraph "scope amendment note" at the top of rq_scope.md before the change.
- If meeting runs over 30 min — wrap up; remaining items can be handled by email.

### ⏱️ Time: 60 min (meeting) + 30 min (notes + email)

---

## 🧭 STEP 1.11 — Update AGENT.md + Commit Phase 1 to Git

### 🎯 What we want to achieve
Mark Phase 1 complete in `AGENT.md`, capture the Phase 1 decisions in the decision log, and commit the work to git (and push to Drive backup).

### 🤖 What AI will do
- Open `AGENT.md` and propose the edits (do NOT silently edit)
- Generate the git commands
- Show diffs before committing

### 👤 What YOU will do

#### Edit `AGENT.md` — three small updates

##### Edit 1: §8 Progress table — mark Phase 1 done

Search for the Phase 1 row in §8 (Current Status / Progress) and update:

```markdown
| Phase | Status | Notes |
|---|---|---|
| 0 — Foundation | ✅ COMPLETE | All 14 steps done |
| 1 — Scope Lock | ✅ COMPLETE | Advisor approved [date] — see rq_scope.md |
| 2 — Literature | ⏳ NOT STARTED | Next |
```

##### Edit 2: §11 Decisions Log — append 3 new entries

```markdown
| # | Date | Phase | Decision |
|---|---|---|---|
| 14 | YYYY-MM-DD | 1 | 5 RQs locked: [paste final 5 RQs in 1 line each] |
| 15 | YYYY-MM-DD | 1 | 5 hypotheses locked: 1-sample Wilcoxon (RQ1), variance ratio (RQ2), Pearson t-test (RQ3), Mann-Whitney U (RQ4), Fisher's exact (RQ5) |
| 16 | YYYY-MM-DD | 1 | 8 metrics locked: Accuracy, Recall, F1, AUC-ROC, Spearman ρ, Stability, Fidelity, Runtime |
```

##### Edit 3: §1 — add confirmed advisor name + meeting date

Update §1 with:
```markdown
- **Advisor**: Prof. [Name], [Department]
- **Phase 1 approval date**: YYYY-MM-DD
```

#### Commit to git

```bash
cd "/home/marajul/Desktop/ENG 672 Technical Communication and Writing/Thesis_V1"

# Status check
git status

# Should show:
#   modified:   AGENT.md
#   new file:   01_proposal/rq_scope.md
#   new file:   01_proposal/advisor_meeting_1.md
#   (maybe new file: 01_proposal/rq_drafts_raw.md → if so, REMOVE it first; keep repo clean)

# If rq_drafts_raw.md exists:
rm 01_proposal/rq_drafts_raw.md
git add 01_proposal/rq_drafts_raw.md
git commit -m "chore: remove temporary AI draft file"

# Commit Phase 1 deliverable
git add 01_proposal/rq_scope.md 01_proposal/advisor_meeting_1.md AGENT.md
git commit -m "Phase 1 (Scope Lock) complete — 5 RQs, 5 H, 3 datasets, 6 models, 8 metrics — advisor approved YYYY-MM-DD"

# Push
git push
```

#### Drive backup sync

```bash
# Sync to your personal Drive (thesis Google account)
rclone sync . "gdrive-thesis:Thesis_V1" --progress \
  --exclude=".venv/**" \
  --exclude=".git/**" \
  --exclude=".puku/**" \
  --exclude="04_data/raw/**"  # too large; download on-demand

# Verify
rclone ls "gdrive-thesis:Thesis_V1/01_proposal" --max-depth 1
```

### ✅ Success criteria
- [ ] `AGENT.md` updated with Phase 1 ✅
- [ ] Decisions log has 3 new entries (14, 15, 16)
- [ ] `rq_scope.md` committed
- [ ] `advisor_meeting_1.md` committed
- [ ] `rq_drafts_raw.md` DELETED (keep repo clean)
- [ ] GitHub push successful
- [ ] Drive sync ran clean

### 🚨 Troubleshooting
- **Git push fails (rejected)**: pull first → `git pull --rebase` → resolve any conflicts → push again.
- **rclone uploads `.puku/` again**: check `--exclude` flags; add `--exclude=".puku/**"` (must be **before** the `--progress` flag).
- **Forgot the commit message format**: see Phase 0 style in git log — `type(scope): description`. This thesis uses `Phase N: ...` for phase-completion commits.

### ⏱️ Time: 15 min

---

## ✅ PHASE 1 EXIT CHECKLIST

Before saying "Phase 1 complete," verify ALL of these:

```
Phase 1 Exit Checklist
======================

[ ] Step 1.1 — Reviewed what's already locked from Phase 0
[ ] Step 1.2 — AI drafted 5 RQs (+ 3 alternates) in rq_drafts_raw.md
[ ] Step 1.3 — Rewrote all 5 RQs in your own voice; SMART-pass
[ ] Step 1.4 — Wrote 5 hypotheses (H1-H5) with H0 + H1 + test + α
[ ] Step 1.5 — Locked 3 datasets (PIMA / Heart / CKD) with full table
[ ] Step 1.6 — Locked 6 models (LR / DT / RF / XGB / LGBM / Stacking)
[ ] Step 1.7 — Locked 8 metrics (4 perf + 5 interp - 1 = 8 OR 5 perf + 5 interp - 2 = 8)
[ ] Step 1.8 — rq_scope.md document complete (~3-5 pages)
[ ] Step 1.9 — Advisor-meeting agenda + 3 slides + pushback answers prepared
[ ] Step 1.10 — Advisor meeting completed; notes saved; thank-you email SENT
[ ] Step 1.11 — AGENT.md updated; committed; pushed; Drive synced

Total: 11/11 ✅  →  Phase 1 COMPLETE
```

When all 11 are ✅, **Phase 1 is complete**. The locked `rq_scope.md` becomes the contract for Phases 2-11.

---

## 🚨 TROUBLESHOOTING — COMMON PHASE 1 PITFALLS

### Pitfall 1 — Vague RQs
**Symptom**: RQ1 says "compare SHAP and LIME."  
**Fix**: Every RQ must name **method × model × dataset × metric**. Use the SMART rubric.

### Pitfall 2 — Wrong number of datasets / models
**Symptom**: You have 7 models instead of 6 because "I added CatBoost."  
**Fix**: Stick to 6. Any addition = scope amendment + advisor re-approval.

### Pitfall 3 — Metrics not mappable to RQ
**Symptom**: You added "Confusion Matrix" as a metric.  
**Fix**: Confusion matrix is NOT a metric — it's a tool. Use Precision/Recall/F1 derived from it.

### Pitfall 4 — No statistical test named in H1
**Symptom**: H1 says "SHAP is faster" but no test.  
**Fix**: Always name the test (Wilcoxon / t-test / Fisher's exact). "Faster" without a test is not a hypothesis.

### Pitfall 5 — LIME not deterministic but you forgot Stability metric
**Symptom**: In Phase 8 you discover LIME top-1 feature changes between runs; you didn't plan for this.  
**Fix**: RQ2 (Stability) catches this. Already covered if RQ2 is in your rq_scope.md.

### Pitfall 6 — Forgetting the advisor's name / title
**Symptom**: Your rq_scope.md says "Advisor: ____" 6 weeks later.  
**Fix**: Fill it in NOW (Step 1.8). It's embarrassing to back-fill.

---

## 📚 QUICK REFERENCE — Phase 1 in 5 Bullets

1. **Goal**: Lock scope before any code is written.
2. **Output**: `01_proposal/rq_scope.md` + advisor approval (email/meeting).
3. **RQs**: 5 RQs, each SMART, each named method × model × dataset × metric.
4. **Datasets**: 3 (PIMA, Heart, CKD).
5. **Models**: 6 (LR, DT, RF, XGB, LGBM, Stacking-LR-meta).
6. **Metrics**: 8 (4 perf + 5 interp − 1 dropped = 8).
7. **Hypotheses**: 5 H with H0 + H1 + statistical test + α = 0.05.
8. **Advisor meeting**: One 20-minute meeting to approve everything.

---

## 🚀 NEXT: Phase 2 — Literature Review

Once ALL Phase 1 exit criteria are ✅, ask me: **"Create Phase 2"** and I'll build `phase_02_LITERATURE_REVIEW.md` with:
- 25-30 paper search strategy (Scholar + IEEE + Springer + ArXiv)
- 3-round reading protocol (abstract → skim → deep read)
- Literature matrix template (Excel/Notion)
- Research-gap identification prompt
- Zotero workflow per paper
- Daily reading targets (3 papers/day for 10 days = 30 papers)
